import sys
import re
import sqlite3
import webbrowser
from MainTextUI import Ui_MainWindow
from beginUI import Ui_Form
from fontUI import Ui_Font
from razmerUI import Ui_Razmer
from newstileUI import Ui_NewStile
from rgbUI import Ui_rgb
from linkUI import Ui_link
from findreplaseUI import Ui_Text
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import *
from PyQt5.QtGui import QColor, QPainter, QBrush, QFont
from PyQt5.QtWidgets import QWidget, QMainWindow, QMenu, QAction, QTextEdit, QFileDialog, QMessageBox, QInputDialog, QWidgetAction
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtPrintSupport import *


class Begin(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self, main_window):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.new_file)
        self.pushButton_2.clicked.connect(self.open_file)
        self.pushButton_3.clicked.connect(self.close)
        self.main_window = main_window

    def new_file(self):
        self.hide()
        self.main_window.show()

    def open_file(self):
        self.hide()
        self.main_window.show()
        self.main_window.open_html_file()
    def close(self):
        sys.exit()


class Font(QtWidgets.QMainWindow, Ui_Font):
    def __init__(self, textedit):
        super().__init__()
        self.setupUi(self)
        self.move(500, 300)
        self.textedit = textedit
        self.pushButton.clicked.connect(self.ok)

    def ok(self):
        font = self.fontComboBox.currentText()
        self.textedit.setCurrentFont(QFont(font))
        self.hide()

class Razmer(QtWidgets.QMainWindow, Ui_Razmer):
    def __init__(self, textedit, button, main_window):
        super().__init__()
        self.setupUi(self)
        self.move(500, 300)
        self.spinBox.setValue(12)
        self.textedit = textedit
        self.main_window = main_window
        self.button = button
        if self.button.text() == "Интервалы":
            self.spinBox.setValue(20)
            self.spinBox.setMinimum(0)  # Минимальное значение
            self.spinBox.setMaximum(1000)  # Максимальное значение
            self.spinBox.setSingleStep(50)  # Устанавливаем шаг изменения на 100
        self.pushButton.clicked.connect(self.ok)

    def ok(self):
        value = self.spinBox.value()
        if self.button.text() == "Размер":
            self.textedit.setFontPointSize(value)
        else:
            cursor = self.textedit.textCursor()
            cursor.select(QTextCursor.Document)
            format = QTextBlockFormat()
            format.setLineHeight(value, 1)
            cursor.mergeBlockFormat(format)
        self.hide()

class RGB(QtWidgets.QMainWindow, Ui_rgb):
    def __init__(self, textedit, main_window):
        super().__init__()
        self.setupUi(self)
        self.move(500, 300)
        self.cur_color = None
        self.main_window = main_window
        self.pushButton.clicked.connect(self.ok)

    def ok(self):
        try:
            red = int(self.lineEdit.text())
            green = int(self.lineEdit_2.text())
            blue = int(self.lineEdit_3.text())
            if 0 <= red <= 255 and 0 <= green <= 255 and 0 <= blue <= 255:
                self.cur_color = QColor(red, green, blue)  # Сохраняем цвет
                self.hide()
                self.main_window.handle_color()
            else:
                QMessageBox.warning(self, "Ошибка", "Значения RGB должны быть от 0 до 255.")
        except ValueError:
            QMessageBox.warning(self, "Ошибка", "Введите корректные числовые значения.")

    def result(self):
        return self.cur_color


class Link(QtWidgets.QMainWindow, Ui_link):
    def __init__(self, parent=None, text_edit=None):
        super().__init__(parent)
        self.setupUi(self)
        self.move(500, 300)
        self.pushButton.clicked.connect(self.ok)
        self.textEdit = text_edit

    def ok(self):
        name = self.lineEdit.text().strip()
        link = self.lineEdit_2.text().strip()
        if name and link and self.textEdit:
            self.textEdit.hyperlinks[name] = link
            cursor = self.textEdit.textCursor()
            cursor.insertHtml(f'<a href="{link}">{name}</a> ')
            self.textEdit.setTextCursor(cursor)
            self.close()
        else:
            QMessageBox.warning(self, 'Ошибка', 'Пожалуйста, заполните оба поля.')
        

class Text(QtWidgets.QMainWindow, Ui_Text):
    def __init__(self, textedit):
        super().__init__()
        self.setupUi(self)
        self.move(500, 300)
        self.textedit = textedit
        self.pushButton.clicked.connect(self.find_text)
        self.pushButton_2.clicked.connect(self.replace_text)
        self.pushButton_2.setEnabled(False)
        self.pushButton_3.clicked.connect(self.remove_highlight)
        self.pushButton_4.clicked.connect(self.ok)

    def find_text(self):
        text_to_find = self.lineEdit.text()
        text = self.textedit.toPlainText()

        flags = 0
        if not self.checkBox.isChecked():
            flags = re.IGNORECASE

        if self.checkBox_2.isChecked():
            text_to_find = r'\b' + re.escape(text_to_find) + r'\b'

        if self.checkBox_3.isChecked() or self.checkBox_2.isChecked():
            pattern = text_to_find
        else:
            pattern = re.escape(text_to_find)

        matches = [(m.start(), m.end()) for m in re.finditer(pattern, text, flags)]
        self.remove_highlight()

        if matches:
            highlight_color = QColor(255, 255, 0)
            extra_selections = []
            for start, end in matches:
                cursor = self.textedit.textCursor()
                cursor.setPosition(start)
                cursor.movePosition(QTextCursor.Right, QTextCursor.KeepAnchor, end - start)

                selection = QTextEdit.ExtraSelection()
                selection.format.setBackground(highlight_color)
                selection.cursor = cursor
                extra_selections.append(selection)

            self.textedit.setExtraSelections(extra_selections)
            self.label_2.setText(f"Найдено: {len(matches)}")
            self.pushButton_2.setEnabled(True)
            QMessageBox.information(self, "Найдено", f"Текст '{text_to_find}' найден и выделен!")
        else:
            self.label_2.setText("Найдено: 0")
            self.pushButton_2.setEnabled(False)
            QMessageBox.warning(self, "Не найдено", f"Текст '{text_to_find}' не найден!")

    def remove_highlight(self):
        self.textedit.setExtraSelections([])
        self.label_2.setText("Найдено: 0")
        self.pushButton_2.setEnabled(False)

    def replace_text(self):
        text_to_find = self.lineEdit.text()
        text_to_replace = self.lineEdit_2.text()
        text = self.textedit.toPlainText()

        flags = 0
        if not self.checkBox.isChecked():
            flags = re.IGNORECASE

        if self.checkBox_2.isChecked():
            text_to_find = r'\b' + re.escape(text_to_find) + r'\b'

        if self.checkBox_3.isChecked() or self.checkBox_2.isChecked():
            pattern = text_to_find
        else:
            pattern = re.escape(text_to_find)

        new_text = re.sub(pattern, text_to_replace, text, flags=flags)
        self.textedit.setPlainText(new_text)
        self.textedit.setTextCursor(self.textedit.textCursor())

        QMessageBox.information(self, "Заменено", f"Текст '{text_to_find}' заменен на '{text_to_replace}'")

    def ok(self):
        self.hide()

class ColorSquare(QWidget):
    def __init__(self, color, parent=None):
        super().__init__(parent)
        self.color = color
        self.setFixedSize(30, 30)  # Устанавливаем размер квадрата

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setBrush(QBrush(self.color))
        painter.drawRect(0, 0, 30, 30)  # Рисуем квадрат

class NewStile(QtWidgets.QMainWindow, Ui_NewStile):
    def __init__(self, textedit):
        super().__init__()
        self.setupUi(self)
        self.move(500, 300)
        self.spinBox.setValue(12)
        self.textedit = textedit
        self.pushButton.clicked.connect(self.ok)
        self.pushButton_2.clicked.connect(self.hide)

    def ok(self):
        name = self.lineEdit_4.text()
        value = self.spinBox.value()
        font = self.fontComboBox.currentText()
        red = int(self.lineEdit.text())
        green = int(self.lineEdit_2.text())
        blue = int(self.lineEdit_3.text())
        if self.checkBox.isChecked():
            bold = "да"
        else:
            bold = "нет"
        if self.checkBox_2.isChecked():
            italic = "да"
        else:
            italic = "нет"
        if self.checkBox_3.isChecked():
            underl = "да"
        else:
            underl = "нет"

        connection = sqlite3.connect('stiles.db')
        cursor = connection.cursor()

        cursor.execute('INSERT INTO Stiles (name, size, font, red, green, blue, bold, italic, underl) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)',
                       (name, value, font, red, green, blue, bold, italic, underl))
        connection.commit()
        connection.close()

        self.hide()
class TextEdiror(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.text_edit = self.textEdit
        self.assign_hyperlink_functions(self.textEdit)
        self.link_dialog = Link(self, self.textEdit)
        self.link_Button.clicked.connect(self.link_dialog.show)
        self.icon_only_widget.setHidden(True)
        self.file_frame.setHidden(True)
        self.find_frame.setHidden(True)
        self.new_frame.setHidden(True)
        self.stile_frame.setHidden(True)
        self.file_Button_1.clicked.connect(self.file_context_menu)
        self.find_Button_1.clicked.connect(self.find_context_menu)
        self.new_Button_1.clicked.connect(self.new_context_menu)
        self.stile_Button_1.clicked.connect(self.stile_context_menu)
        self.pushButton_17.clicked.connect(self.hideeditor)
        self.allcheck_Button_1.clicked.connect(self.select_all)
        self.plamp_Button_1.clicked.connect(self.bold_text)
        self.italic_Button_1.clicked.connect(self.italic_text)
        self.underline_Button_1.clicked.connect(self.underline_text)
        self.copy_Button_1.clicked.connect(self.copyr)
        self.paste_Button_1.clicked.connect(self.pastee)
        self.allcheck_Button_2.clicked.connect(self.select_all)
        self.plamp_Button_2.clicked.connect(self.bold_text)
        self.italic_Button_2.clicked.connect(self.italic_text)
        self.underline_Button_2.clicked.connect(self.underline_text)
        self.copy_Button_2.clicked.connect(self.copyr)
        self.paste_Button_2.clicked.connect(self.pastee)
        self.font = Font(self.textEdit)
        self.shripht_Button_1.clicked.connect(self.font_show)
        self.shripht_Button_2.clicked.connect(self.font_show)
        self.razmer = Razmer(self.textEdit, self.size_Button_2, self)
        self.size_Button_1.clicked.connect(self.razmer_show)
        self.size_Button_2.clicked.connect(self.razmer_show)
        self.interv = Razmer(self.textEdit, self.interval_Button_2, self)
        self.interval_Button_1.clicked.connect(self.interval_ch)
        self.interval_Button_2.clicked.connect(self.interval_ch)
        self.stile = NewStile(self.textEdit)
        self.yourstile_Button.clicked.connect(self.stile.show)
        self.stile_Button.clicked.connect(lambda: self.stile_menu_show(self.stile_Button))
        self.colors = {
            "Черный": QColor(0, 0, 0),
            "Синий": QColor(0, 0, 255),
            "Зеленый": QColor(0, 255, 0),
            "Красный": QColor(255, 0, 0),
            "Желтый": QColor(255, 255, 0),
            "Серый": QColor(128, 128, 128),
        }
        self.color = RGB(self.textEdit, self)
        self.color_Button_2.clicked.connect(lambda: self.show_color_menu(self.color_Button_2))
        self.color_Button_1.clicked.connect(lambda: self.show_color_menu(self.color_Button_1))
        self.newfile_Button.clicked.connect(self.new_file)
        self.savehtmlfile_Button.clicked.connect(self.save_as_html)
        self.openfile_Button.clicked.connect(self.open_html_file)
        self.savepdffile_Button.clicked.connect(self.save_pdf)
        self.otstup_Button_2.clicked.connect(lambda: self.otstup_menu(self.otstup_Button_2))
        self.otstup_Button_1.clicked.connect(lambda: self.otstup_menu(self.otstup_Button_1))
        self.otstup = 0
        self.image_Button.clicked.connect(self.image_show)
        self.findar = Text(self.textEdit)
        self.find_Button_1.clicked.connect(self.findandreplase)
        self.find_Button_2.clicked.connect(self.findandreplase)
    def assign_hyperlink_functions(self, text_edit):

        text_edit.hyperlinks = {}

        def mouse_press_event(event):
            if event.button() == QtCore.Qt.LeftButton:
                cursor = text_edit.cursorForPosition(event.pos())
                cursor.select(cursor.WordUnderCursor)
                word = cursor.selectedText()

                # Проверяем есть ли гиперссылка по клику
                if word in text_edit.hyperlinks:
                    url = text_edit.hyperlinks[word]
                    webbrowser.open(url)  # Открываем URL в браузере
                    return  # Обработка завершена

            # Вызов стандартного поведения
            QTextEdit.mousePressEvent(text_edit, event)

        # Присваиваем новую функцию обработки клика
        text_edit.mousePressEvent = mouse_press_event

    def findandreplase(self):
        self.findar.show()
        if self.find_Button_2.isChecked():
            self.find_Button_2.setChecked(False)
            self.find_frame.setHidden(True)
    def image_show(self):
        path, _ = QFileDialog.getOpenFileName(self, "Insert file", "", "Images (*.png )")
        if not path:
            return
        try:
            with open(path, 'r') as f:
                text = f.read()
            self.textEdit.textCursor().insertText(text)
        except Exception:
            self.textEdit.textCursor().insertImage(path)


    def file_context_menu(self):
        self.show_context_menu(self.file_Button_1, ["Создать", "Открыть", "Сохранить как .pdf", "Сохранить как .html"])
    def find_context_menu(self):
        self.show_context_menu(self.find_Button_1, ["Найти", "Заменить"])
    def new_context_menu(self):
        self.show_context_menu(self.new_Button_1, ["Ссылка", "Изображение"])
    def stile_context_menu(self):
        self.show_context_menu(self.stile_Button_1, ["Стили", "Добавить свой"])

    def otstup_menu(self, button):
        self.show_context_menu(button, ["Вправо", "Влево"])

    def show_context_menu(self, button, menu_items):
        menu = QMenu(self)
        menu.setStyleSheet("QMenu{\n"
"    background-color: rgb(255, 170, 255);\n"
"    color: black;\n"
"}\n"
"QMenu:selected{\n"
"    background-color: white;\n"
"    color:rgba(65,105,225,225);\n"
"}")
        for item_text in menu_items:
            action = QAction(item_text, self)
            action.triggered.connect(self.menu_item_click)
            menu.addAction(action)

        menu.move(button.mapToGlobal(button.rect().topRight()))
        menu.exec()

    def menu_item_click(self):
        text = self.sender().text()

        if text == "Создать":
            self.new_file()
        elif text == "Открыть":
            self.open_html_file()
        elif text == "Сохранить как .pdf":
            self.save_pdf()
        elif text == "Сохранить как .html":
            self.save_as_html()
        elif text == "Найти":
            self.findandreplase()
        elif text == "Заменить":
            self.findandreplase()
        elif text == "Стили":
            self.stile_menu_show(self.new_Button_1)
        elif text == "Добавить свой":
            self.stile.show()
        elif text == "Ссылка":
            self.link_dialog.show()
        elif text == "Изображение":
            self.image_show()
        elif text == "Вправо":
            try:
                if self.otstup_Button_2.isChecked():
                    self.otstup_Button_2.setChecked(False)
                self.otstup += 20
                cursor = self.textEdit.textCursor()
                cursor.select(QTextCursor.Document)
                format = QTextBlockFormat()
                format.setTextIndent(self.otstup)
                cursor.mergeBlockFormat(format)
            except Exception as e:
                print(e)
        elif text == "Влево":
            if self.otstup_Button_2.isChecked():
                self.otstup_Button_2.setChecked(False)
            cursor = self.textEdit.textCursor()
            cursor.select(QTextCursor.Document)
            format = QTextBlockFormat()
            if self.otstup >= 20:
                self.otstup -= 20
                format.setTextIndent(self.otstup)
            else:
                self.otstup = 0
                format.setTextIndent(self.otstup)
            cursor.mergeBlockFormat(format)


    def hideeditor(self):
        self.hide()
        begin.show()

    def italic_text(self):
        if self.pushButton.isChecked():
            if self.italic_Button_1.isChecked():
                state = self.textEdit.fontItalic()
                self.textEdit.setFontItalic(not (state))
        else:
            if self.italic_Button_2.isChecked():
                state = self.textEdit.fontItalic()
                self.textEdit.setFontItalic(not (state))
            else:
                self.textEdit.setFontItalic(False)


    def underline_text(self):
        if self.pushButton.isChecked():
            if self.underline_Button_1.isChecked():
                state = self.textEdit.fontUnderline()
                self.textEdit.setFontUnderline(not (state))
        else:
            if self.underline_Button_2.isChecked():
                state = self.textEdit.fontUnderline()
                self.textEdit.setFontUnderline(not (state))
            else:
                self.textEdit.setFontUnderline(False)

    def bold_text(self):
        if self.pushButton.isChecked():
            if self.plamp_Button_1.isChecked():
                if self.textEdit.fontWeight() != QFont.Bold:
                    self.textEdit.setFontWeight(QFont.Bold)
                    return
                self.textEdit.setFontWeight(QFont.Normal)
            else:
                self.textEdit.setFontWeight(QFont.Normal)
        else:
            if self.plamp_Button_2.isChecked():
                if self.textEdit.fontWeight() != QFont.Bold:
                    self.textEdit.setFontWeight(QFont.Bold)
                    return
                self.textEdit.setFontWeight(QFont.Normal)
            else:
                self.textEdit.setFontWeight(QFont.Normal)

    def select_all(self):
        if self.pushButton.isChecked():
            if self.allcheck_Button_1.isChecked():
                self.textEdit.selectAll()
            else:
                cursor = self.textEdit.textCursor()
                cursor.clearSelection()
                self.textEdit.setTextCursor(cursor)
        else:
            if self.allcheck_Button_2.isChecked():
                self.textEdit.selectAll()
            else:
                cursor = self.textEdit.textCursor()
                cursor.clearSelection()
                self.textEdit.setTextCursor(cursor)


    def copyr(self):
        self.textEdit.copy()
        if self.copy_Button_2.isChecked():
            self.copy_Button_2.setChecked(False)

    def pastee(self):
        self.textEdit.paste()
        if self.paste_Button_2.isChecked():
            self.paste_Button_2.setChecked(False)


    def font_show(self):
        self.font.show()
        if self.shripht_Button_2.isChecked():
            self.shripht_Button_2.setChecked(False)

    def razmer_show(self):
        self.razmer.show()
        if self.size_Button_2.isChecked():
            self.size_Button_2.setChecked(False)

    def interval_ch(self):
        self.interv.show()
        if self.interval_Button_2.isChecked():
            self.interval_Button_2.setChecked(False)



    def color_show(self):
        self.color.show()
        if self.color_Button_2.isChecked():
            self.color_Button_2.setChecked(False)

    def stile_menu_show(self, but):
        button = but
        menu = QMenu(self)
        menu.setStyleSheet("QMenu{\n"
                           "    background-color: rgb(255, 170, 255);\n"
                           "    color: black;\n"
                           "}\n"
                           "QMenu:selected{\n"
                           "    background-color: white;\n"
                           "    color:rgba(65,105,225,225);\n"
                           "}")

        connection = sqlite3.connect('stiles.db')
        cursor = connection.cursor()

        cursor.execute('SELECT name FROM Stiles')
        results = cursor.fetchall()

        for row in results:
            print(row[0])
            action = QAction(row[0], self)
            action.triggered.connect(self.menu_stile_click)
            menu.addAction(action)

        menu.move(button.mapToGlobal(button.rect().topRight()))
        menu.exec()
        connection.close()

    def menu_stile_click(self):
        text = self.sender().text()

        connection = sqlite3.connect('stiles.db')
        cursor = connection.cursor()

        cursor.execute('SELECT size, font, red, green, blue, bold, italic, underl FROM Stiles WHERE name = ?', (text,))
        results = cursor.fetchall()

        for row in results:
            print(row)
            self.textEdit.setFontPointSize(row[0])
            self.textEdit.setCurrentFont(QFont(row[1]))
            color = QColor(row[2], row[3], row[4])
            self.textEdit.setTextColor(color)
            if row[5] == "да": self.textEdit.setFontWeight(QFont.Bold)
            else: self.textEdit.setFontWeight(QFont.Normal)
            if row[6] == "да": self.textEdit.setFontItalic(True)
            else: self.textEdit.setFontItalic(False)
            if row[7] == "да": self.textEdit.setFontUnderline(True)
            else: self.textEdit.setFontUnderline(False)
        connection.close()

    def show_color_menu(self, button):
        menu = QMenu(self)
        for color_name, color_value in self.colors.items():
            color_square = ColorSquare(color_value)
            action = QWidgetAction(menu)
            action.setDefaultWidget(color_square)
            action.triggered.connect(lambda checked, col=color_value: self.change_text_color(col))
            menu.addAction(action)

        custom_color_action = menu.addAction("Добавить свой цвет...")
        custom_color_action.triggered.connect(self.open_color_dialog)

        menu.move(button.mapToGlobal(button.rect().topRight()))
        menu.exec()

    def open_color_dialog(self):
        self.color.show()
    def handle_color(self):
        new_color = self.color.result()
        if new_color:
            color_name = f"RGB({new_color.red()}, {new_color.green()}, {new_color.blue()})"
            self.colors[color_name] = new_color
            if self.pushButton.isChecked():
                but = self.color_Button_1
            else:
                but = self.color_Button_2
            self.show_color_menu(but)
    def change_text_color(self, color):
        if self.color_Button_2.isChecked():
            self.color_Button_2.setChecked(False)
        self.textEdit.setTextColor(color)

    def new_file(self):
        warning_message = (
            "Сохраните текуший файл\n"
            "Он будет удалён"
        )
        reply = QMessageBox.warning(
            self,
            "Предупреждение",
            warning_message,
            QMessageBox.Ok,
            QMessageBox.Cancel
        )

        if reply == QMessageBox.Cancel:
            self.textEdit.clear()
        else:
            return

    def save_as_html(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Сохранить как", "", "HTML files (*.html);;All Files (*)")

        if file_path:
            try:
                with open(file_path, 'w', encoding='utf-8') as html_file:
                    html_file.write(self.textEdit.toHtml())
                    self.textEdit.clear()
                QMessageBox.information(self, "Успех", "Файл успешно сохранен.")
            except Exception as e:
                QMessageBox.critical(self, "Ошибка", f"Не удалось сохранить файл: {e}")

    def open_html_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Открыть файл", "", "HTML files (*.html);;Text files (*.txt)")

        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    if file_path.endswith('.html'):
                        self.textEdit.setHtml(content)
                    else:
                        self.textEdit.setPlainText(content)
                QMessageBox.information(self, "Успех", "Файл успешно открыт.")
            except Exception as e:
                QMessageBox.critical(self, "Ошибка", f"Не удалось открыть файл: {e}")

    def save_pdf(self):
        f_name, _ = QFileDialog.getSaveFileName(self, "Export PDF", None, "PDF files (*.pdf);;All files()")

        self.namefile = f_name

        try:
            printer = QPrinter(QPrinter.HighResolution)
            printer.setOutputFormat(QPrinter.PdfFormat)
            printer.setOutputFileName(f_name)

            final_document = QTextDocument()

            full_html = "<html><body>"

            html = self.textEdit.toHtml()

            full_html += f"<div>{html}</div>"

            full_html += "</body></html>"

            final_document.setHtml(full_html)
            final_document.print_(printer)

            self.textEdit.clear()

            QMessageBox.information(self, "Ура", f"Документ сохранен в формате pdf")

        except Exception as e:
            QMessageBox.critical(self, "Ошибка сохранения", f"Произошла ошибка при сохранении PDF: {str(e)}")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = TextEdiror()
    begin = Begin(main_window)
    begin.show()
    sys.exit(app.exec_())

