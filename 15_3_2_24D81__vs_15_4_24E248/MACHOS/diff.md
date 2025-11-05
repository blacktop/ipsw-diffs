## diff

> `/usr/bin/diff`

```diff

-66.0.0.0.0
-  __TEXT.__text: 0xac50
-  __TEXT.__auth_stubs: 0x600
-  __TEXT.__const: 0x83
-  __TEXT.__cstring: 0xf4e
-  __TEXT.__unwind_info: 0x180
-  __DATA_CONST.__auth_got: 0x300
+70.0.0.0.0
+  __TEXT.__text: 0xaedc
+  __TEXT.__auth_stubs: 0x620
+  __TEXT.__const: 0xa3
+  __TEXT.__cstring: 0xf4f
+  __TEXT.__unwind_info: 0x188
+  __DATA_CONST.__auth_got: 0x310
   __DATA_CONST.__got: 0x40
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x100
   __DATA.__data: 0x590
-  __DATA.__bss: 0x100
+  __DATA.__bss: 0x1c4
   __DATA.__common: 0x1e8
   - /usr/lib/libSystem.B.dylib
-  UUID: 92558D3F-73B4-3493-99AA-B69E5253B105
+  UUID: ED5D34CA-C223-391F-AD38-09785153BE5E
   Functions: 97
-  Symbols:   107
-  CStrings:  188
+  Symbols:   109
+  CStrings:  187
 
Symbols:
+ _getline
+ _sigaction
+ _siglongjmp
+ _sigsetjmp
- _fgetln
- _strndup
CStrings:
+ "%s truncated"
+ "cannot use Myers algorithm with selected options"
- "--"
- "cannot use myers algorithm with selected options"
- "xstrndup"

```
