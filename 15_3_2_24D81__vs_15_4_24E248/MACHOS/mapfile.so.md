## mapfile.so

> `/usr/lib/zsh/5.9/zsh/mapfile.so`

```diff

 108.0.0.0.0
-  __TEXT.__text: 0x3dc
-  __TEXT.__auth_stubs: 0x130
-  __TEXT.__cstring: 0xd
-  __TEXT.__unwind_info: 0x6c
-  __DATA_CONST.__auth_got: 0x98
+  __TEXT.__text: 0x4dc
+  __TEXT.__auth_stubs: 0x190
+  __TEXT.__cstring: 0x20
+  __TEXT.__unwind_info: 0x78
+  __DATA_CONST.__auth_got: 0xc8
   __DATA_CONST.__const: 0x30
   __DATA.__data: 0x78
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libiconv.2.dylib
   - /usr/lib/libncurses.5.4.dylib
   - /usr/lib/libpcre.0.dylib
-  UUID: 191C3CBF-A1F5-381F-893A-DDB821015A2C
+  UUID: 304759A0-A511-3464-80CB-BBADE20E17D0
   Functions: 11
-  Symbols:   29
+  Symbols:   35
   CStrings:  3
 
Symbols:
+ ___error
+ _close
+ _fstat
+ _ftruncate
+ _memcpy
+ _metafy
+ _mmap
+ _msync
+ _munmap
+ _zwarn
- _fclose
- _fopen
- _putc
- _readoutput
Functions:
~ sub_3ae4 -> sub_5e4 : 232 -> 336
~ sub_3d58 -> sub_8c0 : 164 -> 316
CStrings:
+ "ftruncate failed: %e"
- "w"

```
