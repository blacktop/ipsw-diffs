## PurpleReverseProxy

> `/usr/libexec/PurpleReverseProxy`

```diff

-95.0.0.0.0
-  __TEXT.__text: 0x65f0
-  __TEXT.__auth_stubs: 0x7c0
+98.0.0.0.0
+  __TEXT.__text: 0x6704
+  __TEXT.__auth_stubs: 0x800
   __TEXT.__const: 0x6c
-  __TEXT.__gcc_except_tab: 0xc0
-  __TEXT.__cstring: 0x1379
-  __TEXT.__unwind_info: 0x1b8
-  __DATA_CONST.__auth_got: 0x3e8
+  __TEXT.__gcc_except_tab: 0x108
+  __TEXT.__cstring: 0x139f
+  __TEXT.__unwind_info: 0x1e0
+  __DATA_CONST.__auth_got: 0x408
   __DATA_CONST.__got: 0x58
   __DATA_CONST.__const: 0x478
   __DATA_CONST.__cfstring: 0xe80

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 99
-  Symbols:   143
-  CStrings:  200
+  Functions: 103
+  Symbols:   147
+  CStrings:  201
 
Symbols:
+ _dispatch_get_specific
+ _dispatch_queue_get_specific
+ _dispatch_queue_set_specific
+ _dispatch_set_target_queue
CStrings:
+ "com.apple.PurpleReverseProxy.RPSocket"
+ "invoke"
- "signal"

```
