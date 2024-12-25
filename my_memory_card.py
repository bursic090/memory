#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel,QMessageBox, QRadioButton,QGroupBox,QButtonGroup
from random import shuffle




class Question():
    def __init__ (self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

questions_list = []
questions_list.append(Question('Создатели игры Watch Dogs','Ubisoft','Riot Games','Supecell','Valve'))
questions_list.append(Question('Какая группа придумала строчку:"Замученный дорогой я выбился из сил','Король и Шут','Кино','Руки Вверх!','Сектор Газа'))
questions_list.append(Question('На какой тачке гонял Доминик в восьмом форсаже','Dodge Charger','Lada Granta','Toyota Supra','Porsche 911'))




app = QApplication([])

btn_OK = QPushButton('Ответить')
ib_Question = QLabel('Самый сложный вопрос в мире!')

RadioGroupeBox = QGroupBox('Варианты ответов')
rbtn_1 = QRadioButton('Вариант 1')
rbtn_2 = QRadioButton('Вариант 2')
rbtn_3 = QRadioButton('Вариант 3')
rbtn_4 = QRadioButton('Вариант 4')

RadioGroup=QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

Layout_ans1 = QHBoxLayout()
Layout_ans2 = QVBoxLayout()
Layout_ans3 = QVBoxLayout()

Layout_ans2.addWidget(rbtn_1)
Layout_ans2.addWidget(rbtn_2)
Layout_ans3.addWidget(rbtn_3)
Layout_ans3.addWidget(rbtn_4)

Layout_ans1.addLayout(Layout_ans2)
Layout_ans1.addLayout(Layout_ans3)


RadioGroupeBox.setLayout(Layout_ans1)

ansGroupBox = QGroupBox('Результат теста')
ib_Result = QLabel('прав или нет')
ib_Correct = QLabel('Ответ тут')

layout_res = QVBoxLayout()
layout_res.addWidget(ib_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(ib_Correct, alignment=Qt.AlignHCenter, stretch=2)
ansGroupBox.setLayout(layout_res)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(ib_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupeBox)   
layout_line2.addWidget(ansGroupBox)  
ansGroupBox.hide()

layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2)
layout_line3.addStretch(1)


layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.addStretch(5)

def show_result():
    RadioGroupeBox.hide()
    ansGroupBox.show()
    btn_OK.setText('Следующий вопрос')

def show_question():
    RadioGroupeBox.show()
    ansGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]


def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    ib_Question.setText(q.question)
    ib_Correct.setText(q.right_answer)
    show_question()

def show_correct(res):
    ib_Result.setText(res)
    show_result()

def  check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно')

def next_question():
    window.cur_question = window.cur_question + 1
    if window.cur_question >= len(questions_list):
        window.cur_question = 0
    q = questions_list[window.cur_question]
    ask(q)

def click_OK():
    if btn_OK.text() == 'Ответить':
        check_answer()
    else:
        next_question()

window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memo card')
window.cur_question = -1


btn_OK.clicked.connect(click_OK)

next_question()
window.resize(400, 300)
window.show()
app.exec()
