#petscii code from https://github.com/jalbarracinv/python-cbm-petscii-bbs
class petscii():
    petscii={'A':b'\xc1','B':b'\xc2','C':b'\xc3','D':b'\xc4','E':b'\xc5','F':b'\xc6','G':b'\xc7','H':b'\xc8',
    'I':b'\xc9','J':b'\xca','K':b'\xcb','L':b'\xcc','M':b'\xcd','N':b'\xce','O':b'\xcf','P':b'\xd0',
    'Q':b'\xd1','R':b'\xd2','S':b'\xd3','T':b'\xd4','U':b'\xd5','V':b'\xd6','W':b'\xd7','X':b'\xd8','Y':b'\xd9',
    'Z':b'\xda','a':b'A','b':b'B','c':b'C','d':b'D','e':b'E','f':b'F','g':b'G','h':b'H','i':b'I','j':b'J',
    'k':b'K','l':b'L','m':b'M','n':b'N','o':b'O','p':b'P','q':b'Q','r':b'R','s':b'S','t':b'T','u':b'U',
    'w':b'W','x':b'X','y':b'Y','z':b'Z','v':b'V','0':b'0','1':b'1','2':b'2','3':b'3','4':b'4','5':b'5',
    '6':b'6','7':b'7','8':b'8','9':b'9','!':b'!','"':b'"','$':b'$','%':b'%','&':b'&','/':b'/','(':b'(',
    ')':b')','*':b'*','-':b'-','+':b'+','<':b'<','>':b'>',' ':b' ',':':b':','\n':b'\r\n','.':b'.',
    ',':b',','?':b'?','@':b'@','£':b'\\','┌':b'\xb0','┐':b'\xae','└':b'\xad','┘':b'\xbd','─':b'\xc0',
    '├':b'\xab','┤':b'\xb3','#':b'#','\x1c':b'\x1c','\x1e':b'\x1e','\x1f':b'\x1f','\x9c':b'\x9c',
    '\x98':b'\x98','\x1d':b'\x1d','\x11':b'\x11','\x91':b'\x91','\x9d':b'\x9d','\x93':b'\x93',
    '\x12':b'\x12','\x92':b'\x92','\x81':b'\x81','\x90':b'\x90','\x95':b'\x95','\x96':b'\x96',
    '\x97':b'\x97','\x98':b'\x98','\x99':b'\x99','\x9a':b'\x9a','\x9b':b'\x9b','\x9e':b'\x9e',
    '\x9f':b'\x9f','\x13':b'\x13',
    "'":b"\x27","=":b"\x3d","[":b"[","]":b"]",";":b";","↑":b"\x5e","←":b"\x5f"}

    def ascii2petscii(self,tx):
         out = b''
         for n in tx:
            out=out+(self.petscii[n])
         return out

    def petscii2ascii(self,tx):
         out = ''
         for n in range(0,len(tx)):
            byte=tx[n:n+1]
            for k,v in self.petscii.items():
               if(v==byte):
                  out=out+str(k)
            if byte==b'a': out=out+"A"
            if byte==b'b': out=out+"B"
            if byte==b'c': out=out+"C"
            if byte==b'd': out=out+"D"
            if byte==b'e': out=out+"E"
            if byte==b'f': out=out+"F"
            if byte==b'g': out=out+"G"
            if byte==b'h': out=out+"H"
            if byte==b'i': out=out+"I"
            if byte==b'j': out=out+"J"
            if byte==b'k': out=out+"K"
            if byte==b'l': out=out+"L"
            if byte==b'm': out=out+"M"
            if byte==b'n': out=out+"N"
            if byte==b'o': out=out+"O"
            if byte==b'p': out=out+"P"
            if byte==b'q': out=out+"Q"
            if byte==b'r': out=out+"R"
            if byte==b's': out=out+"S"
            if byte==b't': out=out+"T"
            if byte==b'u': out=out+"U"
            if byte==b'v': out=out+"V"
            if byte==b'w': out=out+"W"
            if byte==b'x': out=out+"X"
            if byte==b'y': out=out+"Y"
            if byte==b'z': out=out+"Z"
            if byte==b'\x8d':out=out+"\n"
            if byte==b'\r':out=out+"\n"
         return out
