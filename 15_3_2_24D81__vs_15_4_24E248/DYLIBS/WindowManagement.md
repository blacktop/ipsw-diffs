## WindowManagement

> `/System/Library/PrivateFrameworks/WindowManagement.framework/Versions/A/WindowManagement`

```diff

-278.2.7.0.0
-  __TEXT.__text: 0x11ec0
+278.4.7.0.0
+  __TEXT.__text: 0x12188
   __TEXT.__auth_stubs: 0x580
-  __TEXT.__objc_methlist: 0x1c70
+  __TEXT.__objc_methlist: 0x1ecc
   __TEXT.__const: 0x34a
   __TEXT.__cstring: 0xfdc
   __TEXT.__gcc_except_tab: 0x10c

   __TEXT.__swift5_fieldmd: 0xb4
   __TEXT.__swift5_proto: 0x14
   __TEXT.__swift5_types: 0x18
-  __TEXT.__unwind_info: 0x5a8
+  __TEXT.__unwind_info: 0x5b0
   __TEXT.__objc_classname: 0x44f
   __TEXT.__objc_methname: 0x415e
   __TEXT.__objc_methtype: 0xa5b

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xd10
+  __DATA_CONST.__objc_selrefs: 0xd90
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0xd0
   __DATA_CONST.__objc_arraydata: 0x90
   __AUTH_CONST.__auth_got: 0x2d0
   __AUTH_CONST.__const: 0x6b8
   __AUTH_CONST.__cfstring: 0x1320
-  __AUTH_CONST.__objc_const: 0x40c8
+  __AUTH_CONST.__objc_const: 0x3c80
   __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH_CONST.__objc_arrayobj: 0x1b0
   __AUTH.__objc_data: 0xa00

   - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: B4C658EF-EE12-3371-AF90-D8B6CA3B736B
-  Functions: 719
-  Symbols:   1643
+  UUID: D6E37C71-7D90-3A36-ABF6-C6654BED20D3
+  Functions: 751
+  Symbols:   1674
   CStrings:  1160
 
Symbols:
+ -[WMClientWindowManager _reconnect].cold.1
+ -[WMClientWindowManager invalidate].cold.1
+ -[WMClientWindowManager notifyClickDidEndOnDesktopBackgroundWindow:].cold.1
+ -[WMClientWindowManager performWindowTransaction:].cold.1
+ -[WMClientWindowManager prepareWindowTransaction:].cold.1
+ -[WMClientWindowManager proposeKeyWindowWithInfo:].cold.1
+ -[WMClientWindowManager proposeMainWindowWithInfo:].cold.1
+ -[WMClientWindowManager stages].cold.1
+ -[WMWindowAgentPropertySnapshot propertiesByMergingProperties:].cold.1
+ -[WMWindowPropertySnapshot propertiesByMergingProperties:].cold.1
+ -[WMWindowTransactionAction initWithCyclingType:fences:].cold.1
+ -[WMWindowTransactionAction initWithFullscreenTransitionType:windowIDs:spaceID:fences:].cold.1
+ -[WMWindowTransactionAction initWithHidingType:fences:].cold.1
+ -[WMWindowTransactionAction initWithLoginTransitionType:fences:].cold.1
+ -[WMWindowTransactionAction initWithMiniaturizationType:windows:fences:].cold.1
+ -[WMWindowTransactionAction initWithProposeKeyAndMainWindowRequestType:windowInfo:fences:].cold.1
+ -[WMXPCWindowTransactionAction initCycleActionWithType:fences:].cold.1
+ -[WMXPCWindowTransactionAction initHideActionWithType:fences:].cold.1
+ -[WMXPCWindowTransactionAction initLoginTransitionActionWithType:fences:].cold.1
+ -[WMXPCWindowTransactionAction initMiniaturizationActionWithType:properties:fences:].cold.1
+ -[WMXPCWindowTransactionAction initMiniaturizationActionWithType:windowIDs:fences:].cold.1
+ -[WMXPCWindowTransactionAction initWithFullscreenTransitionType:windowIDs:spaceID:fences:].cold.1
+ -[WMXPCWindowTransactionAction initWithProposeKeyAndMainWindowRequestType:windowInfo:fences:].cold.1
+ -[_WMResizeTargetGeometry contentsGravity].cold.1
+ -[_WMResizeTargetGeometry frame].cold.1
+ -[_WMResizeTargetGeometry size].cold.1
+ -[_WMWindow _markPropertiesDirty:].cold.1
+ -[_WMWindow _markServerPropertiesDirty:].cold.1
+ WMLogHandle.cold.1
- _OUTLINED_FUNCTION_6
- _OUTLINED_FUNCTION_7

```
