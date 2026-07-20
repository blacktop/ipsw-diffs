## MatterPlugin

> `/System/Library/PrivateFrameworks/MatterPlugin.framework/Versions/A/MatterPlugin`

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
-  __TEXT.__text: 0x4db94
-  __TEXT.__objc_methlist: 0x4974
+86.0.0.0.0
+  __TEXT.__text: 0x4e190
+  __TEXT.__objc_methlist: 0x4994
   __TEXT.__const: 0xf8
   __TEXT.__cstring: 0x13ab
-  __TEXT.__oslogstring: 0x5a69
-  __TEXT.__gcc_except_tab: 0x1a1c
-  __TEXT.__unwind_info: 0x1248
+  __TEXT.__oslogstring: 0x5b0b
+  __TEXT.__gcc_except_tab: 0x1a3c
+  __TEXT.__unwind_info: 0x1268
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1cd0
+  __DATA_CONST.__objc_selrefs: 0x1cf0
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x188
   __DATA_CONST.__objc_arraydata: 0x288

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1726
-  Symbols:   3558
-  CStrings:  601
+  Functions: 1734
+  Symbols:   3563
+  CStrings:  604
 
Symbols:
+ -[MTRPluginResidentClientSession _readyDeviceForNodeID:controller:]
+ -[MTRPluginServer _safeQueryIsNodeReady:homeUUID:]
+ -[MTRPluginServer _unsafeQueryIsNodeReady:homeUUID:]
+ GCC_except_table30
+ GCC_except_table41
+ GCC_except_table54
+ ___50-[MTRPluginServer _safeQueryIsNodeReady:homeUUID:]_block_invoke
+ _objc_msgSend$_readyDeviceForNodeID:controller:
+ _objc_msgSend$_safeQueryIsNodeReady:homeUUID:
+ _objc_msgSend$_unsafeQueryIsNodeReady:homeUUID:
+ _objc_msgSend$isNodeReady:homeUUID:
- GCC_except_table23
- GCC_except_table43
- GCC_except_table48
- GCC_except_table56
- GCC_except_table59
- GCC_except_table9
CStrings:
+ "%@ Not querying node readiness, we are not running"
+ "%@ isNodeReady response was: %@ for nodeID: %@ homeUUID: %@"
+ "%@ nodeID %@ not ready - refusing to create device"
```
