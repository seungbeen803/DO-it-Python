# 패키지 = 모듈 여러 개 모아놓은 것
# __init__.py : 패키지 관련 설정 하는 곳
import game.sound.echo # game 안에 sound 안에 echo
game.sound.echo.echo_test()

from game.sound import echo # game의 sound폴드 안 쪽에 있는 echo
echo.echo_test()

from game.sound.echo import echo_test
echo_test()

from game.sound.echo import echo_test as e
e()

from game.sound import *
echo.echo_test()
