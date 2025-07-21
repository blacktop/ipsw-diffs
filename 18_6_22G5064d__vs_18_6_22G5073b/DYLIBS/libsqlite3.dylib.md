## libsqlite3.dylib

> `/usr/lib/libsqlite3.dylib`

```diff

-360.2.0.0.0
-  __TEXT.__text: 0x16931c
+360.3.0.0.0
+  __TEXT.__text: 0x169278
   __TEXT.__auth_stubs: 0xa70
   __TEXT.__const: 0x7e54
-  __TEXT.__cstring: 0xbda9
+  __TEXT.__cstring: 0xbdc6
   __TEXT.__oslogstring: 0x6d8
-  __TEXT.__unwind_info: 0x1d68
+  __TEXT.__unwind_info: 0x1d60
   __DATA_CONST.__got: 0x68
   __DATA_CONST.__const: 0x1d00
   __AUTH_CONST.__auth_got: 0x538

   __DATA_DIRTY.__data: 0x3970
   __DATA_DIRTY.__bss: 0x2d0
   - /usr/lib/libSystem.B.dylib
-  UUID: 56151912-D599-33DB-8017-CE03EDCA431A
+  UUID: 12F6BE8D-088A-385D-AA07-2827085C51DA
   Functions: 2436
   Symbols:   569
-  CStrings:  2223
+  CStrings:  2224
 
Functions (modified):
~ _sqlite3_str_vappendf : 13340 -> 13144

Functions (added):
+ sub_1b1476970
+ sub_1b15062a8
+ sub_1b151b97c
+ sub_1b151bb14

Functions (removed):
- sub_1b20b13b4
- sub_1b20b18ec
- sub_1b20b2570
- sub_1b20b2a68
CStrings:
+ "more than %d aggregate terms"

```
