## PurpleReverseProxy

> `/usr/libexec/PurpleReverseProxy`

```diff

-95.0.0.0.0
-  __TEXT.__text: 0x65f0
-  __TEXT.__auth_stubs: 0x7c0
+100.0.0.0.1
+  __TEXT.__text: 0x6850
+  __TEXT.__auth_stubs: 0x810
   __TEXT.__const: 0x6c
-  __TEXT.__gcc_except_tab: 0xc0
-  __TEXT.__cstring: 0x1379
-  __TEXT.__unwind_info: 0x1b8
-  __DATA_CONST.__auth_got: 0x3e8
+  __TEXT.__gcc_except_tab: 0x108
+  __TEXT.__cstring: 0x13f0
+  __TEXT.__unwind_info: 0x1e8
+  __DATA_CONST.__auth_got: 0x410
   __DATA_CONST.__got: 0x58
-  __DATA_CONST.__const: 0x478
+  __DATA_CONST.__const: 0x498
   __DATA_CONST.__cfstring: 0xe80
   __DATA.__data: 0x19c
   __DATA.__bss: 0x70

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 99
-  Symbols:   143
-  CStrings:  200
+  Functions: 105
+  Symbols:   148
+  CStrings:  204
 
Symbols:
+ ___assert_rtn
+ _dispatch_get_specific
+ _dispatch_queue_get_specific
+ _dispatch_queue_set_specific
+ _dispatch_set_target_queue
CStrings:
+ "!has_synced_to_queue_hint(oldTargetQ, _queue)"
+ "RPSocket.cpp"
+ "com.apple.PurpleReverseProxy.RPSocket"
+ "fromSock->_targetQueue == toSock->_targetQueue"
+ "invoke"
+ "set_target_queue"
- "com.apple.PurpleReverseProxy.ExchangeData"
- "signal"

```
