## CoreCaptureDaemon

> `/System/Library/PrivateFrameworks/CoreCaptureDaemon.framework/CoreCaptureDaemon`

```diff

-1180.60.0.0.0
-  __TEXT.__text: 0x36f1c
-  __TEXT.__auth_stubs: 0xf10
+1180.61.0.0.0
+  __TEXT.__text: 0x37298
+  __TEXT.__auth_stubs: 0xf20
   __TEXT.__const: 0x4f0
   __TEXT.__gcc_except_tab: 0xa0
-  __TEXT.__oslogstring: 0x5bf9
-  __TEXT.__cstring: 0x6e7b
-  __TEXT.__unwind_info: 0x578
+  __TEXT.__oslogstring: 0x5c3f
+  __TEXT.__cstring: 0x6eda
+  __TEXT.__unwind_info: 0x580
   __TEXT.__objc_classname: 0x1
   __TEXT.__objc_methname: 0x9f
   __TEXT.__objc_stubs: 0x100
   __DATA_CONST.__got: 0x138
-  __DATA_CONST.__const: 0x1d0
+  __DATA_CONST.__const: 0x1f0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x40
-  __AUTH_CONST.__auth_got: 0x798
-  __AUTH_CONST.__const: 0xfc8
+  __AUTH_CONST.__auth_got: 0x7a0
+  __AUTH_CONST.__const: 0xff8
   __AUTH_CONST.__cfstring: 0x940
   __DATA.__bss: 0x11a
   __DATA.__common: 0x24

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 466
-  Symbols:   836
-  CStrings:  1044
+  Functions: 469
+  Symbols:   840
+  CStrings:  1047
 
Symbols:
+ __ZN15CCPipeInterface16setDispatchQueueEv
+ _dispatch_async
+ __ZN15CCPipeInterface16getDispatchQueueEv
CStrings:
+ "tapLoopImpl_block_invoke"
+ "%!s(MISSING):%!d(MISSING) MADHU processEvent entry:%!u(MISSING) Owner:%!s(MISSING) Name:%!s(MISSING)"
+ "CCPipeInterface::setDispatchQueue failed to create a serial dispatch queue for continuous pipe\n"
+ "CCPipeInterface::setDispatchQueue entry:%!u(MISSING) fConnectRef(%!d(MISSING))\n"
- "%!s(MISSING):%!d(MISSING) processEvent entry:%!u(MISSING) Owner:%!s(MISSING) Name:%!s(MISSING)"
- "CCPipeInterface::waitForEvent failed to create a serial dispatch queue for continuous pipe\n"

```
