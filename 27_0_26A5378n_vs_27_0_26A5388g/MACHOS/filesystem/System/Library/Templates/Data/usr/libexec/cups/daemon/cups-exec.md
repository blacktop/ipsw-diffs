## cups-exec

> `/System/Library/Templates/Data/usr/libexec/cups/daemon/cups-exec`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__got`

```diff

-530.0.0.0.0
-  __TEXT.__text: 0x39c
-  __TEXT.__auth_stubs: 0x160
-  __TEXT.__cstring: 0x107
+531.1.0.0.0
+  __TEXT.__text: 0x3d4
+  __TEXT.__auth_stubs: 0x170
+  __TEXT.__cstring: 0x136
   __TEXT.__unwind_info: 0x60
-  __DATA_CONST.__auth_got: 0xb0
+  __DATA_CONST.__auth_got: 0xb8
   __DATA_CONST.__got: 0x10
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcups.2.dylib
   Functions: 4
-  Symbols:   26
-  CStrings:  8
+  Symbols:   27
+  CStrings:  9
 
Symbols:
+ _fwrite
Functions:
~ sub_1000004e8 : 788 -> 844
CStrings:
+ "DEBUG: execv of %s failed. err:%d, %s\n"
+ "STATE: +com.apple.badarch-error\n"
- "DEBUG: execv failed: %s\n"
```
