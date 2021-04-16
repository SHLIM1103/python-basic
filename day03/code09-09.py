""" 모듈: 공용 함수들의 집합(자바에서의 클래스 개념) """
# 모듈을 불러오는 방법 : "import 모듈명" 또는 "from 모듈 import 함수명" 선언

import module1

module1.func1()
module1.func2()
module1.func3()

from module1 import *  # 함수명만으로 호출하고 싶을 때

func1()
func2()
func3()

""" 패키지: 모듈의 집합 """
# from 패키지명.모듈 import 함수(또는 *) 선언
