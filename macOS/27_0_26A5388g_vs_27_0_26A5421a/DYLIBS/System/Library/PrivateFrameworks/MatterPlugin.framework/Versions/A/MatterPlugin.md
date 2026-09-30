## MatterPlugin

> `/System/Library/PrivateFrameworks/MatterPlugin.framework/Versions/A/MatterPlugin`

```diff

-86.0.0.0.0
-  __TEXT.__text: 0x4e190
-  __TEXT.__objc_methlist: 0x4994
+86.1.1.0.0
+  __TEXT.__text: 0x4e55c
+  __TEXT.__objc_methlist: 0x49e4
   __TEXT.__const: 0xf8
   __TEXT.__cstring: 0x13ab
-  __TEXT.__oslogstring: 0x5b0b
-  __TEXT.__gcc_except_tab: 0x1a3c
-  __TEXT.__unwind_info: 0x1268
+  __TEXT.__oslogstring: 0x5b68
+  __TEXT.__gcc_except_tab: 0x1aa4
+  __TEXT.__unwind_info: 0x1288
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1cf0
+  __DATA_CONST.__objc_selrefs: 0x1d30
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x188
   __DATA_CONST.__objc_arraydata: 0x288
   __DATA_CONST.__got: 0x460
-  __AUTH_CONST.__const: 0xb50
+  __AUTH_CONST.__const: 0xbb0
   __AUTH_CONST.__cfstring: 0x1a80
-  __AUTH_CONST.__objc_const: 0x6ba8
+  __AUTH_CONST.__objc_const: 0x6c38
   __AUTH_CONST.__objc_intobj: 0x990
   __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x1450
-  __DATA.__objc_ivar: 0x3a4
+  __DATA.__objc_ivar: 0x3b0
   __DATA.__data: 0x600
   __DATA.__bss: 0xd0
   __DATA.__common: 0x8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1734
-  Symbols:   3563
-  CStrings:  604
+  Functions: 1746
+  Symbols:   3588
+  CStrings:  605
 
Symbols:
+ -[MTRPluginClientXPCProxy callRemoteProxyObject:applyBackpressureCap:]
+ -[MTRPluginClientXPCProxy inFlightPossiblyCappedSendCount]
+ -[MTRPluginClientXPCProxy lastDropLogNSec]
+ -[MTRPluginClientXPCProxy setInFlightPossiblyCappedSendCount:]
+ -[MTRPluginClientXPCProxy setLastDropLogNSec:]
+ -[MTRPluginClientXPCProxy setSuppressedDropCount:]
+ -[MTRPluginClientXPCProxy suppressedDropCount]
+ OBJC_IVAR_$_MTRPluginClientXPCProxy._inFlightPossiblyCappedSendCount
+ OBJC_IVAR_$_MTRPluginClientXPCProxy._lastDropLogNSec
+ OBJC_IVAR_$_MTRPluginClientXPCProxy._suppressedDropCount
+ __70-[MTRPluginClientXPCProxy callRemoteProxyObject:applyBackpressureCap:]_block_invoke
+ ___70-[MTRPluginClientXPCProxy callRemoteProxyObject:applyBackpressureCap:]_block_invoke
+ ___block_descriptor_40_e8_32w_e5_v8?0l
+ ___block_descriptor_57_e8_32s40bs48w_e5_v8?0l
+ ___copy_helper_block_e8_32s40b48w
+ ___copy_helper_block_e8_32w
+ ___destroy_helper_block_e8_32s40s48w
+ ___destroy_helper_block_e8_32w
+ _clock_gettime_nsec_np
+ _objc_msgSend$callRemoteProxyObject:applyBackpressureCap:
+ _objc_msgSend$inFlightPossiblyCappedSendCount
+ _objc_msgSend$lastDropLogNSec
+ _objc_msgSend$scheduleSendBarrierBlock:
+ _objc_msgSend$setInFlightPossiblyCappedSendCount:
+ _objc_msgSend$setLastDropLogNSec:
+ _objc_msgSend$setSuppressedDropCount:
+ _objc_msgSend$suppressedDropCount
- __49-[MTRPluginClientXPCProxy callRemoteProxyObject:]_block_invoke
- ___49-[MTRPluginClientXPCProxy callRemoteProxyObject:]_block_invoke
CStrings:
+ "%@ dropping XPC send to client - in-flight count %lu >= cap %lu (%lu drop(s) since last log)"
```
