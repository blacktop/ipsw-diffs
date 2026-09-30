## game-mode-detect

> `/usr/bin/game-mode-detect`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`

```diff

-53.0.0.0.0
-  __TEXT.__text: 0x30
-  __TEXT.__auth_stubs: 0x10
+54.0.0.0.0
+  __TEXT.__text: 0x64
+  __TEXT.__auth_stubs: 0x30
   __TEXT.__const: 0x40
-  __TEXT.__cstring: 0x16
+  __TEXT.__cstring: 0x53
   __TEXT.__unwind_info: 0x58
-  __DATA_CONST.__auth_got: 0x8
+  __DATA_CONST.__auth_got: 0x18
   - /usr/lib/libSystem.B.dylib
   Functions: 1
-  Symbols:   3
-  CStrings:  1
+  Symbols:   5
+  CStrings:  2
 
Symbols:
+ _dlclose
+ _dlopen
Functions:
~ sub_1000004b0 : 48 -> 100
CStrings:
+ "/System/Library/Frameworks/AddressBook.framework/AddressBook"
```
