import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QTextEdit, QVBoxLayout, QWidget

class Calculator(QMainWindow):
    """
    PyQt5를 사용한 기본 계산기 애플리케이션의 메인 윈도우 클래스입니다.
    """
    def __init__(self):
        """
        생성자: 부모 클래스의 생성자를 호출하고 UI를 초기화합니다.
        """
        super().__init__()
        self.initUI()

    def initUI(self):
        """
        사용자 인터페이스(UI)를 초기화하고 설정합니다.
        """
        # 윈도우 제목 설정
        self.setWindowTitle('계산기')

        # 텍스트 에디터 생성
        self.text_edit = QTextEdit()
        self.text_edit.setReadOnly(True) # 읽기 전용으로 설정

        # 메시지 버튼 생성
        btn = QPushButton('메시지', self)
        btn.clicked.connect(self.showMessage)

        # 수직 레이아웃 생성 및 위젯 추가
        vbox = QVBoxLayout()
        vbox.addWidget(self.text_edit)
        vbox.addWidget(btn)

        # 중앙 위젯 생성 및 레이아웃 설정
        central_widget = QWidget()
        central_widget.setLayout(vbox)
        self.setCentralWidget(central_widget)

        # 윈도우 위치와 크기 설정 (x, y, width, height)
        self.setGeometry(300, 300, 400, 500)
        
        # 윈도우를 화면에 표시
        self.show()

    def showMessage(self):
        """
        버튼 클릭 시 텍스트 에디터에 "Button Clicked" 메시지를 추가합니다.
        """
        self.text_edit.append('Button Clicked')

if __name__ == '__main__':
    # QApplication 인스턴스 생성
    app = QApplication(sys.argv)
    
    # Calculator 클래스의 인스턴스 생성
    ex = Calculator()
    
    # 이벤트 루프 시작
    sys.exit(app.exec_())
