## libReverseProxyDevice.dylib

> `/usr/lib/libReverseProxyDevice.dylib`

```diff

-95.0.0.0.0
-  __TEXT.__text: 0x4244
-  __TEXT.__auth_stubs: 0x620
-  __TEXT.__objc_methlist: 0xbc
+102.0.0.0.0
+  __TEXT.__text: 0x43e4
+  __TEXT.__auth_stubs: 0x660
+  __TEXT.__objc_methlist: 0x2bc
   __TEXT.__const: 0x30
-  __TEXT.__gcc_except_tab: 0x84
-  __TEXT.__cstring: 0xb66
-  __TEXT.__unwind_info: 0x160
+  __TEXT.__gcc_except_tab: 0xcc
+  __TEXT.__cstring: 0xb63
+  __TEXT.__unwind_info: 0x188
   __TEXT.__objc_classname: 0x61
-  __TEXT.__objc_methname: 0x6dc
-  __TEXT.__objc_methtype: 0x600
+  __TEXT.__objc_methname: 0x6e2
+  __TEXT.__objc_methtype: 0x603
   __TEXT.__objc_stubs: 0x240
   __DATA_CONST.__got: 0x60
   __DATA_CONST.__const: 0x80
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb8
-  __AUTH_CONST.__auth_got: 0x320
-  __AUTH_CONST.__const: 0x188
+  __DATA_CONST.__objc_selrefs: 0x1e0
+  __AUTH_CONST.__auth_got: 0x340
+  __AUTH_CONST.__const: 0x198
   __AUTH_CONST.__cfstring: 0x820
-  __AUTH_CONST.__objc_const: 0x790
+  __AUTH_CONST.__objc_const: 0x3d8
   __AUTH.__objc_data: 0x50
   __AUTH.__data: 0x110
   __DATA.__objc_classrefs: 0x10

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9EEF0EB1-A577-3503-8AF4-16F116E7591B
-  Functions: 85
-  Symbols:   280
+  UUID: F0EE7D48-2DD6-3CB9-8239-8D8C57EAD8B2
+  Functions: 90
+  Symbols:   291
   CStrings:  312
 
Symbols:
+ -[RPStreamDevice initWithHost:port:cb:userContext:queue:]
+ GCC_except_table10
+ GCC_except_table23
+ GCC_except_table29
+ GCC_except_table50
+ GCC_except_table8
+ _RPSocketResume
+ __ZL24add_synced_to_queue_hintP16dispatch_queue_sS0_
+ __ZN11RPSocket_fd19latch_target_queuesEv
+ __ZN8RPSocket13EventCallback4sendEv
+ __ZN8RPSocket13EventCallback6invokeEv
+ __ZN8RPSocket13EventCallback9invoke_fnEPS0_
+ __ZN8RPSocket19latch_target_queuesEv
+ __ZNK8RPSocket13EventCallback10retain_allEv
+ __ZNK8RPSocket13EventCallback11release_allEv
+ __block_descriptor_tmp.103
+ __block_descriptor_tmp.19
+ _dispatch_get_specific
+ _dispatch_queue_get_specific
+ _dispatch_queue_set_specific
+ _dispatch_set_target_queue
- -[RPStreamDevice initWithHost:port:cb:userContext:]
- GCC_except_table11
- GCC_except_table45
- GCC_except_table9
- __ZN8RPSocket6resumeEv
- __ZN8RPSocket6signalEm
- __ZN8RPSocket7suspendEv
- __ZN8RPSocket9invoke_cbEPv
- __block_descriptor_tmp.118
- __block_descriptor_tmp.20
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/PurpleReverseProxy/Common/Logging.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/PurpleReverseProxy/Common/RPSocket.cpp"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/PurpleReverseProxy/Common/Utilities.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/PurpleReverseProxy/ReverseProxyDevice/ReverseProxyDevice.c"
+ "@56@0:8@16@24^?32^v40@48"
+ "com.apple.PurpleReverseProxy.RPSocket"
+ "initWithHost:port:cb:userContext:queue:"
+ "invoke"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/PurpleReverseProxy/Common/Logging.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/PurpleReverseProxy/Common/RPSocket.cpp"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/PurpleReverseProxy/Common/Utilities.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/PurpleReverseProxy/ReverseProxyDevice/ReverseProxyDevice.c"
- "@48@0:8@16@24^?32^v40"
- "com.apple.PurpleReverseProxy.SetLogLevel"
- "initWithHost:port:cb:userContext:"
- "signal"

```
