from hello_world.hello_world import HelloWorld

def test_go_returns_hello_world():
  hw = HelloWorld()
  assert hw.go() == "Hello World"
