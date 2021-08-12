import json
from flask import Flask, url_for, render_template, request, redirect, make_response, jsonify
from pynput.keyboard import Key, Controller as keycontroller
from pynput.mouse import Button ,Controller as mousec
from os import environ ,system
from webbrowser import open as opensite
from platform import platform
from time import sleep
import requests as reqli
import os
import sys
##################################################
###########    WElCOME   ;;; html
def wel():
    w='''
    <!DOCTYPE html>
    <html>
    <head>
    <title>  WELCOME  </title>
    </head>
    <h1> Welcome </h>
    <body>
    <h1>     </h1>
    <p>       </p>
    <div id="adityamukhiya">

        <button class="Aditya" id="touch"     onclick="resulttouch()">       TouchPad       </button>
        <button class="mukh"   id="keyboard" onclick="resultkey()">       keyBoard       </button>
    </div>
    <p class="info">Press on keyboard to use keyBoard  OR   touchPad to use TouchPad </p>
       
    <p class="red">Note :-</p>

    <p class="aditya">1 } In keyboard you can't use two or more button at a time
        But you can type the name of two or more button in input box
        Eg:-  ctrl+m  or ctrl+shift+s</p>

    <p class="maha">2 } TouchPad only works in touch Devices</p>

    <p class="infom">3 } This only works in Local Network ,
        To use it outside the local network ,
        you can use portForwarding</p>
        
    <p class="com" >4 } If you have any problem , let me know in comment </p>

    </p>
    <style>

    p.info {
      margin-left: 10px ;
      color: green;
      font-size: 350%;
      background-color: lightyellow;
      font-style: italic;
      padding: 10px 10px 10px 10px;

    }
    p.red {
      margin-left: 10px ;
      color: red;
      font-size: 550%;
      
      padding: 10px 10px 10px 10px;
    }
    p.aditya {
      margin-left: 10px ;
      color: orange;
      font-style: italic;
      background-color: lightyellow;
      font-size: 350%;
      padding: 10px 10px 10px 10px;
    }
    p.maha {
      margin-left: 10px ;
      color: blue;
      background-color:powderblue;
      font-size: 350%;
      padding: 10px 10px 10px 10px;
    }
    p.infom {
      margin-left: 10px ;
      color: yellow;
      font-size: 350%;
      background-color:skyblue;
      font-style: italic;
      padding: 10px 10px 10px 10px;
    }
    p.com {
      margin-left: 10px ;
      color: black;
      font-size: 350%;
      background-color:lightgrey;
      padding: 10px 10px 10px 10px;
    }
    button.Aditya {
      margin-left: 380px ;
      color: blue;
      font-size: 520%;
      font-style: italic;
      border: 3px solid green;
      padding: 10px 100px 10px 100px;
      
    }
    button.mukh {
      margin-left: 380px ;
      color: gold;
      font-size: 520%;
      font-style: italic;
      border: 3px solid green;
      padding: 10px 130px 10px 100px;
      
    }
    </style>
    <script>
    function resulttouch() {
        window.location.href = "touchpad";
    }
    function resultkey() {
        window.location.href = "keyboard";
    }
    </script>
    </body> 
    </html>
    '''
    return w
###   TouchPad HTML   Code  ######################
def aditya():
    w='''
    <!DOCTYPE html>
    <html>
    <head>
    <title>Touch Pad</title>
    </head>
    <body>
    <body scroll="no" style="overflow: hidden">
    <h1>   Touch Pad    </h1>
    <h1>     </h1>
    <p>       </p>
    <div id="adityamukhiya">
        <button id="leftbut"   onclick="mymouse('left')">       Left Click       </button>
        <button id="rightbut" onclick="mymouse('right')">  Right Click      </button>
    </div>

    <style>
    button.ad {
      margin-left: 380px ;
      color: red;
      font-size: 220%;
      border: 3px solid black;
      padding: 10px 100px 10px 100px;
    }
    button.it {
      margin-left: 250px ;
      color: green;
      font-size: 220%;
      border: 3px solid green;
      padding: 10px 100px 10px 100px;
      
    }
    button.ya {
      color: orange;
      font-size: 220%;
      border: 3px solid orange;
      padding: 10px 100px 10px 100px;
    }
    button.mu {
      margin-left: 380px ;
      color: blue;
      font-size: 220%;
      border: 3px solid blue;
      padding: 10px 100px 10px 100px;
    }
    </style>
    <canvas  id="DemoCanvas" width="950" height="800"></canvas>
    <br />

    <div id="adityamukhiya1">

        <button class="ad" id="upkey"   onClick={mymouse("upkey")}>       ↑        </button>
        <br />
        <button class="it" id="leftkey" onclick="mymouse('leftkey')">  ←     </button>
        <button class="ya" id="rightkey"   onclick="mymouse('rightkey')">       →       </button>
        <br />
        <button class="mu" id="downkey" onclick="mymouse('downkey')">  ↓    </button>
    </div>
    <h1 id="adityaresult">  g </h1>
    <script>
    var lastTouchEnd = 0;
    document.addEventListener('touchend', function (event) {
      var now = (new Date()).getTime();
      if (now - lastTouchEnd <= 300) {
        event.preventDefault();
      }
      lastTouchEnd = now;
    }, false);
    function readMouseMove(event) {

        cdata ="onmove"+"_"+event.touches[0].clientX.toString()+"_"+event.touches[0].clientY.toString()
        fetch(`${window.origin}/touchpad`, {
                method: "POST",
                credentials: "include",
                body: JSON.stringify(cdata),
                cache: "no-cache",
                headers:  new Headers({
                    "content-type": "application/json"
                })
            })
    }
    document.getElementById("DemoCanvas").style.padding = "3px 10px 10px 1px";
    document.getElementById("leftbut").style.padding = "20px 210px 20px 200px";
    document.getElementById("rightbut").style.padding = "20px 210px 20px 200px";
    var canvas = document.getElementById("DemoCanvas");

    function countTouches(event) {
        var result_x = document.getElementById("adityaresult");
        result_x.innerHTML ="No. of finger touching TouchPad = " +event.touches.length;
        cdata ="tcount"+"_"+event.touches.length.toString()
        fetch(`${window.origin}/touchpad`, {
                method: "POST",
                credentials: "include",
                body: JSON.stringify(cdata),
                cache: "no-cache",
                headers:  new Headers({
                    "content-type": "application/json"
                })
            })
    }
    function initvaluexy(event) {
        cdata ="init"
        fetch(`${window.origin}/touchpad`, {
                method: "POST",
                credentials: "include",
                body: JSON.stringify(cdata),
                cache: "no-cache",
                headers:  new Headers({
                    "content-type": "application/json"
                })
            })
    }
    function mymouse(e) {
        var result_x = document.getElementById("adityaresult");
        result_x.innerHTML =" Button : " +e;
        cdata ="mousebut"+"_"+e
        fetch(`${window.origin}/touchpad`, {
                method: "POST",
                credentials: "include",
                body: JSON.stringify(cdata),
                cache: "no-cache",
                headers:  new Headers({
                    "content-type": "application/json"
                })
            })
    }
    if (canvas.getContext) 
    {
      var ctx = canvas.getContext('2d');
      ctx.fillStyle='#DCDCDC';    // color of fill
      ctx.fillRect(0, 0, 950, 800); // create rectangle  
    }

    canvas.addEventListener( "touchmove", readMouseMove, false)

    canvas.addEventListener( "touchstart", countTouches, false)
    canvas.addEventListener( "touchend", initvaluexy, false)
    </script>
    </body> 
    </html>
    '''
    return w
###########################################################################

######    KEYBOARD HTML CODE        #############
def mahadev():
    w='''
    <!DOCTYPE html>
    <html>
    <title> Keyboard  </title>
    <body>



    <p id="demo"> Virtual Keyboard for PC  </p>
    <style>
    .adityab {
      background-color: lightgrey; /* Green */
      border: 3px solid black ;
      color: black;
      padding: 20px 22px;
      text-align: center;
      text-decoration: none;
      display: inline-block;
      margin: 4px 0px;
      cursor: pointer;
    }

    </style>

    <p>A function is triggered when the button is clicked. The function  click the key of your PC .</p>
    <div>
        <p>Type keys name to input </p>
        <input id="mukhiya" type="text"   size="80" />
        <button onclick="mykeyboard()">  Click to Send   </button>

        <p>  </p>

    </div>

    <script>
    var lastTouchEnd = 0;
    document.addEventListener('touchend', function (event) {
      var now = (new Date()).getTime();
      if (now - lastTouchEnd <= 300) {
        event.preventDefault();
      }
      lastTouchEnd = now;
    }, false);
    function myFunction(e) {
        cdata ="-ke"+"_"+e
        fetch(`${window.origin}/keyboard`, {
                method: "POST",
                credentials: "include",
                body: JSON.stringify(cdata),
                cache: "no-cache",
                headers:  new Headers({
                    "content-type": "application/json"
                })
            })
    }

    function mykeyboard() {
        var e =document.getElementById('mukhiya').value
        document.getElementById('mukhiya').value=""
        cdata ="-keall"+"_"+e
        fetch(`${window.origin}/keyboard`, {
                method: "POST",
                credentials: "include",
                body: JSON.stringify(cdata),
                cache: "no-cache",
                headers:  new Headers({
                    "content-type": "application/json"
                })
            })
    }
    </script>
    <div id="VirtualKey">
        <p> Or use Keyboard </p>
        <p id="aditya">  .</p>
        <input class="adityab" type="button" value="   |   " onclick="myFunction('|')" />
        <input class="adityab" type="button" value=" ` " onclick="myFunction('`')" />
        <input class="adityab" type="button" value="  : " onclick="myFunction(':')" />
        <input class="adityab" type="button" value="  '' " onclick="myFunction('"')" />
        <input class="adityab" type="button" value="  esc " onclick="myFunction('esc')" />
        <input class="adityab" type="button" value="  f2 " onclick="myFunction('f2')" />
        <input class="adityab" type="button" value="  f4 " onclick="myFunction('f4')" />
        <input class="adityab" type="button" value="  f5 " onclick="myFunction('f5')" />
        <input class="adityab" type="button" value=" del" onclick="myFunction('delete')" />
        <input class="adityab" type="button" value=" prt sc" onclick="myFunction('print_screen')" />
        <input class="adityab" type="button" value=" insert" onclick="myFunction('insert')" />
        <input class="adityab" type="button" value=" restart" style="color:darkgreen;padding: 20px 50px;" onclick="myFunction('rest--')" />
        <input class="adityab" type="button" value=" shutdown" style="color:red;padding: 20px 43px;" onclick="myFunction('shut--')"/>
        <br />
        <input class="adityab" type="button" value=" ! " onclick="myFunction('!')" />
        <input class="adityab" type="button" value=" @ " onclick="myFunction('@')" />
        <input class="adityab" type="button" value=" # " onclick="myFunction('#')" />
        <input class="adityab" type="button" value=" $ " onclick="myFunction('$')" />
        <input class="adityab" type="button" value=" % " onclick="myFunction('%')" />
        <input class="adityab" type="button" value=" ^ " onclick="myFunction('^')" />
        <input class="adityab" type="button" value=" & " onclick="myFunction('&')" />
        <input class="adityab" type="button" value=" * " onclick="myFunction('*')" />
        <input class="adityab" type="button" value=" ( " onclick="myFunction('(')" />
        <input class="adityab" type="button" value=" ) " onclick="myFunction(')')" />
        <input class="adityab" type="button" value=" _ " onclick="myFunction('_')" />
        <input class="adityab" type="button" value=" = " onclick="myFunction('=')" />
        <input class="adityab" type="button" value=" { " onclick="myFunction('{')" />
        <input class="adityab" type="button" value=" } " onclick="myFunction('}')" />
        <input class="adityab" type="button" value="  < " onclick="myFunction('<')" />
        <input class="adityab" type="button" value="  > " onclick="myFunction('>')" />
        <input class="adityab" type="button" value="  ?  " onclick="myFunction('?')" />
        <br />
        <input class="adityab" type="button" value=" ~" onclick="myFunction('~')" />
        <input class="adityab" type="button" value="  1 " onclick="myFunction('1')" />
        <input class="adityab" type="button" value="  2 " onclick="myFunction('2')" />
        <input class="adityab" type="button" value="  3 " onclick="myFunction('3')" />
        <input class="adityab" type="button" value="  4 " onclick="myFunction('4')" />
        <input class="adityab" type="button" value="  5 " onclick="myFunction('5')" />
        <input class="adityab" type="button" value="  6 " onclick="myFunction('6')" />
        <input class="adityab" type="button" value="  7 " onclick="myFunction('7')" />
        <input class="adityab" type="button" value="  8 " onclick="myFunction('8')" />
        <input class="adityab" type="button" value=" 9 " onclick="myFunction('9')" />
        <input class="adityab" type="button" value=" 0 " onclick="myFunction('0')" />
        <input class="adityab" type="button" value=" - " onclick="myFunction('-')" />
        <input class="adityab" type="button" value=" + " onclick="myFunction('+')" />
        <input class="adityab" type="button" style="color:#D35400;padding: 20px 41px;" value=" backspace " onclick="myFunction('back')" />
        <input class="adityab" type="button" value="home" onclick="myFunction('home')" />
        <br />
        <input class="adityab" type="button" style="color:#229954 ;padding: 20px 53px;" value="tab" onclick="myFunction('tab')" />
        <input class="adityab" type="button" value="  Q " onclick="myFunction('Q')" />
        <input class="adityab" type="button" value="  W " onclick="myFunction('W')" />
        <input class="adityab" type="button" value="  E " onclick="myFunction('E')" />
        <input class="adityab" type="button" value="  R " onclick="myFunction('R')" />
        <input class="adityab" type="button" value="  T " onclick="myFunction('T')" />
        <input class="adityab" type="button" value="  Y " onclick="myFunction('Y')" />
        <input class="adityab" type="button" value="  U " onclick="myFunction('U')" />
        <input class="adityab" type="button" value="  I " onclick="myFunction('I')" />
        <input class="adityab" type="button" value="  O " onclick="myFunction('O')" />
        <input class="adityab" type="button" value="  P " onclick="myFunction('P')" />
        <input class="adityab" type="button" value="  [ " onclick="myFunction('[')" />
        <input class="adityab" type="button" value="  ] " onclick="myFunction(']')" />
        <input class="adityab" type="button" value="    \ " onclick="myFunction('\')" />
        <input class="adityab" type="button" value=" pgup " onclick="myFunction('pgup')" />
        <br />
        <input class="adityab" type="button" value=" caps lock      " onclick="myFunction('caps')" />
        <input class="adityab" type="button" value=" A " onclick="myFunction('A')" />
        <input class="adityab" type="button" value=" S " onclick="myFunction('S')" />
        <input class="adityab" type="button" value=" D " onclick="myFunction('D')" />
        <input class="adityab" type="button" value=" F " onclick="myFunction('F')" />
        <input class="adityab" type="button" value=" G " onclick="myFunction('G')" />
        <input class="adityab" type="button" value=" H " onclick="myFunction('H')" />
        <input class="adityab" type="button" value=" J " onclick="myFunction('J')" />
        <input class="adityab" type="button" value=" K " onclick="myFunction('K')" />
        <input class="adityab" type="button" value=" L " onclick="myFunction('L')" />
        <input class="adityab" type="button" value=" ; " onclick="myFunction(';')" />
        <input class="adityab" type="button" value=" ' " onclick="myFunction('’')" />
        <input class="adityab" type="button" style="color:blue;padding: 20px 57px;" value="      enter    " onclick="myFunction('enter')" />
        <input class="adityab" type="button" value=" pgdn " onclick="myFunction('pgdn')" />
        <br />
        <input class="adityab" type="button" style="color:red;padding: 20px 32px;"value="   shift         " onclick="myFunction('shift')" />
        <input class="adityab" type="button" value="  Z  " onclick="myFunction('Z')" />
        <input class="adityab" type="button" value="  X  " onclick="myFunction('X')" />
        <input class="adityab" type="button" value="  C  " onclick="myFunction('C')" />
        <input class="adityab" type="button" value="  V  " onclick="myFunction('V')" />
        <input class="adityab" type="button" value="  B  " onclick="myFunction('B')" />
        <input class="adityab" type="button" value="  N  " onclick="myFunction('N')" />
        <input class="adityab" type="button" value="  M  " onclick="myFunction('M')" />
        <input class="adityab" type="button" value="  ,  " onclick="myFunction(',')" />
        <input class="adityab" type="button" value="  .  " onclick="myFunction('.')" />
        <input class="adityab" type="button" value="  /  " onclick="myFunction('/')" />
        <input class="adityab" type="button" style="color:#7E5109;padding: 20px 63px;"value="  shift   " onclick="myFunction('shift_r')" />
        <input class="adityab" type="button" value="  end   " onclick="myFunction('end')" />
        <br />
        <input class="adityab" type="button" style="color:#0E6251;padding: 20px 42px;" value=" ctrl     " onclick="myFunction('ctrl')" />
        <input class="adityab" type="button" value=" fn " onclick="myFunction('fn')" />
        <input class="adityab" type="button" style="color:#3498DB;padding: 20px 42px;"value=" window " onclick="myFunction('start')" />
        <input class="adityab" type="button" value=" alt " onclick="myFunction('alt')" />
        <input class="adityab" type="button" style="color:#6C3483 ;padding: 20px 155px;"value=" space" onclick="myFunction('space')" />
        <input class="adityab" type="button" value=" ctrl " onclick="myFunction('ctrl_r')" />
        <input class="adityab" type="button" value=" ← " onclick="myFunction('left')" />
        <input class="adityab" type="button" value="  → " onclick="myFunction('right')" />
        <input class="adityab" type="button" value=" ↑   " onclick="myFunction('up')" />
        <input class="adityab" type="button" value=" ↓ " onclick="myFunction('down')" />


    </div>
    </body>
    </html>
    '''
    return w

###########################################   ######
keypress =keycontroller()
mouse=mousec()
fingtouch__=''
x_=''
y_=''
shift='n'
stop_cur='n'
def ip_address():
    return "192.160.43.150"
def web_browser(site):
    webbrowser.open(site)
    
def mouse_but(but):
    if but =='left':
        but=Button.left
    elif but =="right" :
        but=Button.right
    else:
        but=Button.left
    mouse.press(but)
    mouse.release(but) 
def move_cur(x,y):
    sleep(0.01)
    global stop_cur
    if stop_cur=='y':
        print('st ]]')
        pass
    else:
        mouse.move (x, y)
def pos_cur(x,y):
    mouse.position(x,y)
def scroll(x,y):
    mouse.scroll(x, y)   
def on_finger_touch(fingtouch_):

    try:
        fingtouch_=fingtouch_.replace(' ','')
    except:
        pass        
    fingtouch_=fingtouch_.split('_')
    print(fingtouch_)
    i__=0
    for i in fingtouch_:
        try:
            i=int(i)
            
            if i <= i__:
                pass
            else:
                i__= i
        except:
            pass
    print('i___ ',i__)
    global x_
    global y_
    if i__== 0:
        pass
    elif i__ == 1 and x_=='' and y_=='':
        mouse_but('left')
        print(' Left click')
                

    elif i__==2:
        mouse_but('right')
    elif i__==3:
        reqli.post("https://maker.ifttt.com/trigger/light_off/with/key/jZnlwT1C3JCShiclzfxiKq1z64I6-fQdvMwcj1XfNGC")
        print(' Light is off ')
        print()
    elif i__==4:
        reqli.post("https://maker.ifttt.com/trigger/light_on/with/key/jZnlwT1C3JCShiclzfxiKq1z64I6-fQdvMwcj1XfNGC")
        print(' Light is on ')
        print()
    elif i__ ==5:
        opensite('www.google.com')
    elif i__ ==6:
        if 'Linux' in platform():
            system('shutdown -r')
        else:
            system('shutdown /r')

    elif i__ ==7:
         if 'Linux' in platform():
            system('shutdown -s')
         else:
            system('shutdown /s')

    else:
        print('No. of fingure : ',i__)
    global fingtouch__
    fingtouch__=''
def keyboard_but(data):
    def k(key):
        try:
            keypress.press(key)
            keypress.release(key)
        except:
            pass
    def v_key(i):
        if i == "ctrl":
            i=Key.ctrl_l
        elif i == "ctrl_r":
            i=Key.ctrl_r
        elif i == "print_screen":
            i=Key.print_screen
        elif i == "shift_r":
            i=Key.shift_r
        elif i == "home":
            i=Key.home
        elif i == "pgup":
            i=Key.page_up
        elif i == "pgdn":
            i=Key.page_down
        elif i == "end":
            i=Key.end
        elif i == "pause":
            i=Key.pause
        elif i == "shift":
            i=Key.shift
        elif i=="alt":
            i=Key.alt_l
        elif i=="alt_r":
            i=Key.alt_r
        elif  i== 'f1':
            i=Key.f1
        elif i == 'f2':
            i=Key.f2
        elif i == 'f3':
            i=Key.f3
        elif i == 'f4':
            i=Key.f4
        elif i == 'f5':
            i=Key.f5
        elif i == 'f6':
            i=Key.f6
        elif i == 'f7':
            i=Key.f7
        elif i == 'f8':
            i=Key.f8
        elif i == 'f9':
            i=Key.f9
        elif i == 'f10':
            i=Key.f10
        elif i == 'f11':
            i=Key.f11
        elif i == 'f12':
            i=Key.f12
        elif i == 'start':
            i=Key.cmd
        elif i == 'esc':
            i=Key.esc
        elif i == 'enter':
            i=Key.enter
        elif i == 'back':
            i=Key.backspace
        elif i == 'up':
            i=Key.up
        elif i == 'down':
            i=Key.down
        elif i == 'left':
            i=Key.left
        elif i == 'right':
            i=Key.right
        elif i == 'caps':
            i=Key.caps_lock

        elif i == 'space':
            i=Key.space
        elif i == 'delete':
            i=Key.delete
        elif i == 'insert':
            i=Key.insert
        elif i == 'space':
            i=Key.space
        else:
            i =i
        return i
    if '+' in data and (data.split('+')[0]) in ['ctrl','ctrl_r','shift','alt','alt_r','start','fn','delete','insert','space','right','left'
       ,'up','down','back','esc','caps','home','end','pgdn','pgup','f1','f2','f3','f4','f5','f6','f7'
       ,'f8','f9','f10','f11','f12','pause','print_screen']:
        print('hello')
        x=data.split('+')
        for i in x:
            i=v_key(i)
            try:
                keypress.press(i)
            except:
                pass
        for i in x:
            i=v_key(i)
            try:
                keypress.release(i)
            except:
                pass
    elif data=='rest--':
        if 'Linux' in platform():
            system('shutdown -r')
        else:
            system('shutdown /r')

    elif data =="shut--":
         if 'Linux' in platform():
            system('shutdown -s')
         else:
            system('shutdown /s')

    else:
        ke=v_key(data)
        if ke != data:
            k(ke)
        else:                
            for _k in data:
                try:
                    keypress.press(_k)
                    keypress.release(_k)
                except:
                    pass
        print('key')
                

app = Flask(__name__,static_folder='static',
            template_folder='templates')
@app.route('/')
def index():
    return wel()


@app.route('/touchpad', methods=['GET','POST'])
def touchpad():
    req=request.get_json()
    print(req)
    global x_ ,y_
    global fingtouch__
    global stop_cur
    if req==None:
        pass
    else:
        req=req.split('_')
        if req[0]=='tcount':
            stop_cur='n'            
            req=req[1]
            fingtouch__=fingtouch__+req+'_'
            print(' No of finger',req)

        elif req[0]=="init":
            stop_cur='y'
            on_finger_touch(fingtouch__)
            x_=''
            y_=''
        elif req[0]=="mousebut":
            b=req[1]
            if b =='1':
                pass
            elif b =='left' or b == '1' or b =='2':
                mouse_but('left')                
            elif b =='right' or b == '3':
                mouse_but('right')
            elif b =='upkey':
                keyboard_but('up')
            elif b =='downkey':
                keyboard_but('down')
            elif b =='leftkey':
                keyboard_but('left')
            elif b =='rightkey':
                keyboard_but('right')
            elif b=='3':
                pass
            else:
                pass
            
            
        elif req[0]=='onmove':
            x=req[1]
            x=x.split('.')
            x=x[0]
            x=int(x)
            if x_ =='':
                x_=x
            else:
                xv=x -x_
                x_=x
                y=req[2]
                y=y.split('.')
                y=y[0]
                y=int(y)
                if y_ =='':
                    y_=y
                else:
                    yv=y-y_
                    y_=y
                    move_cur(xv,yv)
 
        else:
            pass
            
    return aditya()# html

@app.route('/keyboard', methods=['GET','POST'])
def keyboard():
    req=request.get_json()
    print(req)
    reqs=req
    if req==None:
        pass
    else:
        req=req.split('_')
        if req[0] =='-ke':
            req=req[1]
            global shift                
            if req=='shift':
                if shift =='n':
                    shift='y'
                elif shift =='y':
                    shift='n'
                else:
                    pass
            else:
                if shift=='y':
                    pass
                else:
                    req=req.lower()                        
                keyboard_but(req)
        elif req[0] == '-keall':
            reqs=reqs[7:]
            keyboard_but(reqs)
        else:
            pass
           
    return mahadev()  # Keyboard HTML Code


@app.route('/adityA')
def adityA():
    return '<h style="background-color:skyblue;color: gold;font-style: italic;font-size: 4000%;">    Aditya </h>'


if __name__ == '__main__':
    n=int(input(' Enter Port Number  : '))
    port = int(environ.get('PORT', 8070))
    print(' ____________________________________________________________')
    print('|                                                            |')
    print('| Your Local IP Address   : ',"http://"+str(ip_address())+':'+str(port)+'/',"    |")
    print('|                                                            |')
    print('|     __Use this IP to use touchpad And Keyboard__           |')
    print("|____________________________________________________________|")
    app.run(host='0.0.0.0', port=port)

