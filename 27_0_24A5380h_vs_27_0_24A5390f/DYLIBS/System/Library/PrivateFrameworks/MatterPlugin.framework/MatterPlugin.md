## MatterPlugin

> `/System/Library/PrivateFrameworks/MatterPlugin.framework/MatterPlugin`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-85.0.0.0.0
-  __TEXT.__text: 0x4a318
-  __TEXT.__objc_methlist: 0x49cc
+86.0.0.0.0
+  __TEXT.__text: 0x4a8bc
+  __TEXT.__objc_methlist: 0x49ec
   __TEXT.__const: 0x110
   __TEXT.__cstring: 0x1413
-  __TEXT.__oslogstring: 0x5db9
-  __TEXT.__gcc_except_tab: 0x1a90
-  __TEXT.__unwind_info: 0x1220
+  __TEXT.__oslogstring: 0x5e5b
+  __TEXT.__gcc_except_tab: 0x1ab0
+  __TEXT.__unwind_info: 0x1240
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1d68
+  __DATA_CONST.__objc_selrefs: 0x1d88
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x188
   __DATA_CONST.__objc_arraydata: 0x288

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1705
-  Symbols:   3538
-  CStrings:  622
+  Functions: 1713
+  Symbols:   3548
+  CStrings:  625
 
Symbols:
+ -[MTRPluginResidentClientSession _readyDeviceForNodeID:controller:]
+ -[MTRPluginServer _safeQueryIsNodeReady:homeUUID:]
+ -[MTRPluginServer _unsafeQueryIsNodeReady:homeUUID:]
+ GCC_except_table26
+ GCC_except_table39
+ GCC_except_table47
+ ___50-[MTRPluginServer _safeQueryIsNodeReady:homeUUID:]_block_invoke
+ _objc_msgSend$_readyDeviceForNodeID:controller:
+ _objc_msgSend$_safeQueryIsNodeReady:homeUUID:
+ _objc_msgSend$_unsafeQueryIsNodeReady:homeUUID:
+ _objc_msgSend$isNodeReady:homeUUID:
- GCC_except_table23
CStrings:
+ "%@ Not querying node readiness, we are not running"
+ "%@ isNodeReady response was: %@ for nodeID: %@ homeUUID: %@"
+ "%@ nodeID %@ not ready - refusing to create device"
```
