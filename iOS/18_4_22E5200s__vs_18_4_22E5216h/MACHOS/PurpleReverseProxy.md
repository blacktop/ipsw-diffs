## PurpleReverseProxy

> `/usr/libexec/PurpleReverseProxy`

```diff

-98.0.0.0.0
-  __TEXT.__text: 0x6704
-  __TEXT.__auth_stubs: 0x800
+100.0.0.0.1
+  __TEXT.__text: 0x6850
+  __TEXT.__auth_stubs: 0x810
   __TEXT.__const: 0x6c
   __TEXT.__gcc_except_tab: 0x108
-  __TEXT.__cstring: 0x139f
-  __TEXT.__unwind_info: 0x1e0
-  __DATA_CONST.__auth_got: 0x408
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
-  Functions: 103
-  Symbols:   147
-  CStrings:  201
+  Functions: 105
+  Symbols:   148
+  CStrings:  204
 
Symbols:
+ ___assert_rtn
CStrings:
+ "!has_synced_to_queue_hint(oldTargetQ, _queue)"
+ "RPSocket.cpp"
+ "fromSock->_targetQueue == toSock->_targetQueue"
+ "set_target_queue"
- "com.apple.PurpleReverseProxy.ExchangeData"

```
