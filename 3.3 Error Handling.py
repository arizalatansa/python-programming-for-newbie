# Syntax Error
fruit_list = ['Apple','Banana','Watermelon']

for fruit in fruit_list # lupa ga pake : # SyntaxError: expected ':'
    print(fruit)

# Logical Error
#1
nilai = 10
pembagi = 0
# hasil = nilai/pembagi # ZeroDivisionError: division by zero

#2
print(dir(locals()['__builtins__']))
# Jenis masalah :
# ['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BaseExceptionGroup', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EncodingWarning', 'EnvironmentError', 'Exception', 'ExceptionGroup', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'WindowsError', 'ZeroDivisionError', '__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__', 'abs', 'aiter', 'all', 'anext', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']

# Error Handling yang kita lakukan kalau ada error
try:
    nilai = 10
    pembagi = 0
    print(nilai/pembagi) # tidak akan dijalankan dan akan keluar tanda dari except
except:
    print('Ops Jadi Error, Sad!')

# Pendetailan Error Handling
try:
    nilai = 10
    pembagi = 0
    print(nilai/pembagi) # tidak akan dijalankan dan akan keluar tanda dari except
except Exception as e:
    print('Ops Jadi Error-nya adalah di', e.__class__,".")

    ### atau

try:
    nilai = 10
    pembagi = 0
    print(nilai/pembagi) # tidak akan dijalankan dan akan keluar tanda dari except
except ZeroDivisionError:
    print('Ops terjadi ZeroDivisionError')
except ValueError:
    print(' Ops Terjadi ValueError')
except:
    print('Ops terjadi error yang tidak dikenali')

# Buat Error Handling sendiri
class ValueTooSmallError(Exception):
    pass

class ValueTooLargeError(Exception):
    pass

number = 10

while True:

    try:
        i_num = int(input('Coba tebak angka, masukkan angka: '))

        if i_num < number:
            raise ValueTooSmallError
        elif i_num > number:
            raise ValueTooLargeError
        break
    
    except ValueTooSmallError:
        print('Wah angkanya masih terlalu kecil, coba lagi')
        print()
    except ValueTooLargeError:
        print('Wah angkanya masih terlalu besar, coba lagi')
        print()
    
print('Wah jago banget si nebaknya, pinjam dulu seratus')

# Instruksi cetak di bawah menyebabkan program terhenti karena mengalami IndexError
# Tangani error tersebut dengan teknik Error Handling yang sudah dipelajari
# Setelah itu, jalankan program dan pastikan tidak ada lagi pemberitahuan error pada program

# versi 1
list = [1, 3, 5, 7, 9, 11, 13, 15]

try:
    print(list[20])

except IndexError:
    print('kesalahan ini karena IndexError')

# versi 2

list = [1, 3, 5, 7, 9, 11, 13, 15]

try:
    print(list[20])

except Exception as e:
    print('Kesalahan ini karena :', e.__class__,". Ayo kita usaha lagi!")