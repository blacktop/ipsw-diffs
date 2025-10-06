## PurpleReverseProxy

> `/usr/libexec/PurpleReverseProxy`

```diff

-83.0.0.0.0
-  __TEXT.__text: 0x5e18
-  __TEXT.__auth_stubs: 0x7b0
+85.0.0.0.0
+  __TEXT.__text: 0x5e24
+  __TEXT.__auth_stubs: 0x7c0
   __TEXT.__gcc_except_tab: 0xb8
   __TEXT.__const: 0x6c
-  __TEXT.__cstring: 0x1192
+  __TEXT.__cstring: 0x1191
   __TEXT.__unwind_info: 0x1a8
   __TEXT.__eh_frame: 0x38
-  __DATA_CONST.__auth_got: 0x3e0
+  __DATA_CONST.__auth_got: 0x3e8
   __DATA_CONST.__got: 0x58
   __DATA_CONST.__const: 0x458
   __DATA_CONST.__cfstring: 0xd60

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 51A941D9-3AE0-3562-BB1A-E7E0BCA28E76
+  UUID: FD03CCA4-CC96-3A4B-AE47-951028CC23A2
   Functions: 95
-  Symbols:   142
+  Symbols:   143
   CStrings:  293
 
Symbols:
+ _fdopen
+ _open
- _fopen
CStrings:
+ "w"
- "w+"

```
