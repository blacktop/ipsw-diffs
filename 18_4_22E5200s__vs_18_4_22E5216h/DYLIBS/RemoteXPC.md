## RemoteXPC

> `/System/Library/PrivateFrameworks/RemoteXPC.framework/RemoteXPC`

```diff

-2894.100.71.502.1
-  __TEXT.__text: 0xf4cc
-  __TEXT.__auth_stubs: 0xa10
+2894.100.80.0.0
+  __TEXT.__text: 0xf59c
+  __TEXT.__auth_stubs: 0xa60
   __TEXT.__objc_methlist: 0x2ac
-  __TEXT.__const: 0xa8
+  __TEXT.__const: 0xa0
   __TEXT.__gcc_except_tab: 0x318
-  __TEXT.__cstring: 0xb0a
+  __TEXT.__cstring: 0xb27
   __TEXT.__oslogstring: 0x2722
-  __TEXT.__unwind_info: 0x400
+  __TEXT.__unwind_info: 0x410
   __TEXT.__objc_classname: 0xdf
   __TEXT.__objc_methname: 0x79e
   __TEXT.__objc_methtype: 0x28d

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x158
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x518
-  __AUTH_CONST.__const: 0xc0
+  __AUTH_CONST.__auth_got: 0x540
+  __AUTH_CONST.__const: 0xe0
   __AUTH_CONST.__objc_const: 0xf88
   __DATA.__objc_ivar: 0x12c
   __DATA.__data: 0xc8
+  __DATA.__bss: 0x10
   __DATA_DIRTY.__objc_data: 0x230
   __DATA_DIRTY.__data: 0xe0
   __DATA_DIRTY.__bss: 0x40

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 356
-  Symbols:   616
-  CStrings:  459
+  Functions: 358
+  Symbols:   623
+  CStrings:  460
 
Symbols:
+ _dispatch_queue_get_qos_class
+ _nw_context_create
+ _nw_context_set_isolate_protocol_stack
+ _nw_context_set_scheduling_mode
+ _nw_parameters_set_context
CStrings:
+ "remotexpc_realtime_messaging"

```
