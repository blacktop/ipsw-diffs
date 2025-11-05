## tftpd

> `/usr/libexec/tftpd`

```diff

-303.0.2.0.0
-  __TEXT.__text: 0x3d80
-  __TEXT.__auth_stubs: 0x400
+306.0.0.0.0
+  __TEXT.__text: 0x3d3c
+  __TEXT.__auth_stubs: 0x3f0
   __TEXT.__const: 0x78
-  __TEXT.__cstring: 0xdd6
-  __TEXT.__unwind_info: 0xf0
-  __DATA_CONST.__auth_got: 0x200
+  __TEXT.__cstring: 0xdf8
+  __TEXT.__unwind_info: 0xe8
+  __DATA_CONST.__auth_got: 0x1f8
   __DATA_CONST.__got: 0x20
   __DATA_CONST.__auth_ptr: 0x20
   __DATA_CONST.__const: 0x30
-  __DATA.__data: 0x342
+  __DATA.__data: 0x346
   __DATA.__bss: 0x10c68
   __DATA.__common: 0x10c
   - /usr/lib/libSystem.B.dylib
-  UUID: 0AE52908-E93C-3737-904A-93D7870E898B
-  Functions: 45
-  Symbols:   71
-  CStrings:  162
+  UUID: 5149FD04-0725-34BC-A7C8-84146C805179
+  Functions: 44
+  Symbols:   70
+  CStrings:  161
 
Symbols:
+ _arc4random
- ___strcpy_chk
- _random
CStrings:
+ "%s%n"
+ "Filename suffix too long (%zu characters maximum)"
+ "Filename too long (%zu characters, %zu maximum)"
+ "Rejecting %zd-byte request from %s"
+ "cCd::F:ilnoOp:s:Su:U:wW"
- "../"
- "0"
- "1"
- "Filename suffix too long (%d characters maximum)"
- "Filename too long (%zd characters, %zd maximum)"
- "cCd::F:ilnoOp:s:u:U:wW"

```
