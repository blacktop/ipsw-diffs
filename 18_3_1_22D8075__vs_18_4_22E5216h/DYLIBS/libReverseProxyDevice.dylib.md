## libReverseProxyDevice.dylib

> `/usr/lib/libReverseProxyDevice.dylib`

```diff

-95.0.0.0.0
-  __TEXT.__text: 0x471c
-  __TEXT.__auth_stubs: 0x6b0
+100.0.0.0.1
+  __TEXT.__text: 0x4890
+  __TEXT.__auth_stubs: 0x6f0
   __TEXT.__const: 0x28
-  __TEXT.__gcc_except_tab: 0x84
-  __TEXT.__cstring: 0xd87
-  __TEXT.__unwind_info: 0x168
+  __TEXT.__gcc_except_tab: 0xcc
+  __TEXT.__cstring: 0xd84
+  __TEXT.__unwind_info: 0x188
   __DATA_CONST.__got: 0x78
   __DATA_CONST.__const: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __AUTH_CONST.__auth_got: 0x360
-  __AUTH_CONST.__const: 0x178
+  __AUTH_CONST.__auth_got: 0x380
+  __AUTH_CONST.__const: 0x188
   __AUTH_CONST.__cfstring: 0x9e0
   __DATA.__data: 0x4
   __DATA.__bss: 0x68

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 72
-  Symbols:   198
+  Functions: 77
+  Symbols:   207
   CStrings:  144
 
Symbols:
+ _dispatch_get_specific
+ _dispatch_queue_get_specific
+ _dispatch_queue_set_specific
+ _dispatch_set_target_queue
CStrings:
+ "com.apple.PurpleReverseProxy.RPSocket"
+ "invoke"
- "com.apple.PurpleReverseProxy.SetLogLevel"
- "signal"

```
