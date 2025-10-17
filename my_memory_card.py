#создай приложение для запоминания информации
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt




app =QApplication([])
main_win =QWidget()
main_win.setWindowTitle('Memory Card')
main_win.resize(700,700)
label =QLabel('Какой национальности не существует?')
button =QPushButton('Ответить')
radio1 =QRadioButton('Энцы')
radio2 =QRadioButton('Смурфы')
radio3 =QRadioButton('Чулымцы')
radio4 =QRadioButton('Алеуты')
group_box=QGroupBox('Варианты ответов')
btn_group =QButtonGroup()
btn_group.addButton(radio1)
btn_group.addButton(radio2)
btn_group.addButton(radio3)
btn_group.addButton(radio4)
group_line1 =QHBoxLayout()
group_line2 =QHBoxLayout()
group_col =QVBoxLayout()
result_group =QGroupBox('Результаты')
lbresult =QLabel('Прав ты или нет?')
lbcorrect = QLabel('Ответ будет тут')
res_line =QVBoxLayout()
res_line.addWidget(lbresult,alignment=(Qt.AlignLeft | Qt.AlignTop))
res_line.addWidget(lbcorrect,alignment=Qt.AlignHCenter, stretch=2)
result_group.setLayout(res_line)




group_line1.addWidget(radio1)
group_line1.addWidget(radio3)
group_line2.addWidget(radio2)
group_line2.addWidget(radio4)
group_col.addLayout(group_line1)
group_col.addLayout(group_line2)
result_group.setLayout(group_col)
l1 =QHBoxLayout()
l2 =QVBoxLayout()
l3 =QVBoxLayout()
l2.addWidget(radio1)
l2.addWidget(radio2)
l3.addWidget(radio3)
l3.addWidget(radio4)
l1.addLayout(l2)
l1.addLayout(l3)
group_box.setLayout(l1)
line1 =QHBoxLayout()
line2 =QHBoxLayout()
line3 =QHBoxLayout()
main_Layout =QVBoxLayout()
line1.addWidget(label,alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
line2.addWidget(group_box)
line2.addWidget(result_group)
result_group.hide()
line3.addStretch(1)
line3.addWidget(button,stretch = 2)
line3.addStretch(1)
main_Layout.addLayout(line1,stretch = 5)
main_Layout.addLayout(line2,stretch = 2)
main_Layout.addStretch(1)
main_Layout.addLayout(line3,stretch = 1)
main_Layout.addStretch(1)
main_Layout.setSpacing(5)
main_win.setLayout(main_Layout)

answer =[radio1,radio2,radio3,radio4]
from random import shuffle


def show_result():
    group_box.hide()
    result_group.show()
    button.setText('Следующий вопрос')
def show_question():
    group_box.show()
    result_group.hide()
    button.setText('Ответить')
    btn_group.setExclusive(False)
    radio1.setChecked(False) 
    radio2.setChecked(False)
    radio3.setChecked(False)
    radio4.setChecked(False)
    btn_group.setExclusive(True)


def show_correct(result):
    lbresult.setText(result)
    show_result()


def check_answer():
    
    if answer [0].isChecked():
        show_correct('Правильно')
        main_win.score += 1
        print('Статистика\n-Всего вопросов: ', main_win.total, '\n-Правильных ответов: ', main_win.score)
        print('Рейтинг: ', (main_win.score/main_win.total*100), '%')
    else:
        if answer[1].isChecked() or answer[2].isChecked() or answer[3].isChecked():
            show_correct('Не верно')
     

def ask(q:Question):
    shuffle(answer)
    label.setText(q.question)
    answer[0].setText(q.right_answer)
    answer[1].setText(q.wrong1)
    answer[2].setText(q.wrong2)
    answer[3].setText(q.wrong3)
    lbresult.setText(q.question)
    lbcorrect.setText(q.right_answer)
    show_question()

q =Question('Можно ли в Расте ловить рыбу?','да','нет','только с модом','только в бэте')
q2 =Question('Сколько планет в Млечном путе?','8','9','7','10')
q3 =Question('Сколько штатов в Америке?', '50','51','48','49')
q4 =Question('Стольца РФ','Москва','Санкт-Петербург','Новосибирск','Севастополь')
q5 =Question('Какая самая большая страна?','Россия','США','Канада','Бразилия')
q6 =Question('На какой реке стоит Санк-Петербург?','Нева','Ока','Волга','Енисей')
q7 =Question('Сколько океанов на земле?','5','6','7','4')
q8 =Question('Какой самый большой океан на земле?','Тихий','Антлантичейский','Индийский','Северо-Ледовитый')
q9 =Question('Как называется участок суши окружённый водой с трех сторон?','полуостров','остров',"каньон",'залив')
q10 =Question('Какое животное является эндемиком Байкала?',"нерпа", "волк", "лисица", "лось")
questions =[]
questions.append(q)
questions.append(q2)
questions.append(q3)
questions.append(q4)
questions.append(q5)
questions.append(q6)
questions.append(q7)
questions.append(q8)
questions.append(q9)
questions.append(q10)
shuffle(questions)
def next_question():
    main_win.total += 1
    print('Статистика\n-Всего вопросов: ', main_win.total, '\n-Правильных ответов: ', main_win.score)
    main_win.cur_question += 1
    if main_win.cur_question >= len(questions):
        main_win.cur_question = 0
    q = questions[main_win.cur_question]
    ask(q)


def click_ok():
    if button.text() == 'Ответить':
        check_answer()
    else:
        next_question()



def test():
    if button.text() == 'Ответить':
        show_result()
    else:
        show_question()


main_win.cur_question = -1
button.clicked.connect(click_ok)
main_win.total = 0
main_win.score = 0

next_question()


main_win.show()
app.exec_()




