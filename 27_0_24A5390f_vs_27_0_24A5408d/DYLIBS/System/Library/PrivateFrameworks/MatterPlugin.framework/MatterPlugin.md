## MatterPlugin

> `/System/Library/PrivateFrameworks/MatterPlugin.framework/MatterPlugin`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-86.0.0.0.0
-  __TEXT.__text: 0x4a8bc
-  __TEXT.__objc_methlist: 0x49ec
+86.1.1.0.0
+  __TEXT.__text: 0x4abc0
+  __TEXT.__objc_methlist: 0x4a3c
   __TEXT.__const: 0x110
   __TEXT.__cstring: 0x1413
-  __TEXT.__oslogstring: 0x5e5b
-  __TEXT.__gcc_except_tab: 0x1ab0
-  __TEXT.__unwind_info: 0x1240
+  __TEXT.__oslogstring: 0x5eb8
+  __TEXT.__gcc_except_tab: 0x1b18
+  __TEXT.__unwind_info: 0x1288
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xa08
+  __DATA_CONST.__const: 0xa58
   __DATA_CONST.__objc_classlist: 0x220
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1d88
+  __DATA_CONST.__objc_selrefs: 0x1dc8
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x188
   __DATA_CONST.__objc_arraydata: 0x288
   __DATA_CONST.__got: 0x480
   __AUTH_CONST.__const: 0x2e0
   __AUTH_CONST.__cfstring: 0x1a80
-  __AUTH_CONST.__objc_const: 0x6c08
+  __AUTH_CONST.__objc_const: 0x6c98
   __AUTH_CONST.__objc_intobj: 0x990
   __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x1450
-  __DATA.__objc_ivar: 0x3ac
+  __DATA.__objc_ivar: 0x3b8
   __DATA.__data: 0x600
   __DATA.__bss: 0xd0
   __DATA.__common: 0x8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1713
-  Symbols:   3548
-  CStrings:  625
+  Functions: 1721
+  Symbols:   3569
+  CStrings:  626
 
Symbols:
+ -[MTRPluginClientXPCProxy callRemoteProxyObject:applyBackpressureCap:]
+ -[MTRPluginClientXPCProxy inFlightPossiblyCappedSendCount]
+ -[MTRPluginClientXPCProxy lastDropLogNSec]
+ -[MTRPluginClientXPCProxy setInFlightPossiblyCappedSendCount:]
+ -[MTRPluginClientXPCProxy setLastDropLogNSec:]
+ -[MTRPluginClientXPCProxy setSuppressedDropCount:]
+ -[MTRPluginClientXPCProxy suppressedDropCount]
+ _OBJC_IVAR_$_MTRPluginClientXPCProxy._inFlightPossiblyCappedSendCount
+ _OBJC_IVAR_$_MTRPluginClientXPCProxy._lastDropLogNSec
+ _OBJC_IVAR_$_MTRPluginClientXPCProxy._suppressedDropCount
+ ___70-[MTRPluginClientXPCProxy callRemoteProxyObject:applyBackpressureCap:]_block_invoke
+ ___block_descriptor_40_e8_32w_e5_v8?0lw32l8
+ ___block_descriptor_57_e8_32s40bs48w_e5_v8?0ls32l8s40l8w48l8
+ _clock_gettime_nsec_np
+ _objc_msgSend$callRemoteProxyObject:applyBackpressureCap:
+ _objc_msgSend$inFlightPossiblyCappedSendCount
+ _objc_msgSend$lastDropLogNSec
+ _objc_msgSend$scheduleSendBarrierBlock:
+ _objc_msgSend$setInFlightPossiblyCappedSendCount:
+ _objc_msgSend$setLastDropLogNSec:
+ _objc_msgSend$setSuppressedDropCount:
+ _objc_msgSend$suppressedDropCount
- ___49-[MTRPluginClientXPCProxy callRemoteProxyObject:]_block_invoke
CStrings:
+ "%@ dropping XPC send to client - in-flight count %lu >= cap %lu (%lu drop(s) since last log)"
```
