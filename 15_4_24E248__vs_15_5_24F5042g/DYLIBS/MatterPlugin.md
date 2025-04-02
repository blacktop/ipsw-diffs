## MatterPlugin

> `/System/Library/PrivateFrameworks/MatterPlugin.framework/Versions/A/MatterPlugin`

```diff

-49.5.14.0.0
-  __TEXT.__text: 0x4bb38
+49.6.11.0.0
+  __TEXT.__text: 0x4ad10
   __TEXT.__auth_stubs: 0x5d0
-  __TEXT.__objc_methlist: 0x46d4
+  __TEXT.__objc_methlist: 0x46a4
   __TEXT.__const: 0xf0
-  __TEXT.__cstring: 0x11fd
-  __TEXT.__oslogstring: 0x5421
-  __TEXT.__gcc_except_tab: 0x1d28
-  __TEXT.__unwind_info: 0x11a0
-  __TEXT.__objc_classname: 0x9a2
-  __TEXT.__objc_methname: 0x7671
-  __TEXT.__objc_methtype: 0x1547
-  __TEXT.__objc_stubs: 0x59c0
+  __TEXT.__cstring: 0x11e0
+  __TEXT.__oslogstring: 0x502a
+  __TEXT.__gcc_except_tab: 0x1ce8
+  __TEXT.__unwind_info: 0x1180
+  __TEXT.__objc_classname: 0x9a1
+  __TEXT.__objc_methname: 0x74f1
+  __TEXT.__objc_methtype: 0x1536
+  __TEXT.__objc_stubs: 0x5900
   __DATA_CONST.__got: 0x460
   __DATA_CONST.__const: 0x210
   __DATA_CONST.__objc_classlist: 0x218
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1b48
+  __DATA_CONST.__objc_selrefs: 0x1b18
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x180
   __DATA_CONST.__objc_arraydata: 0x40
   __AUTH_CONST.__auth_got: 0x2f8
-  __AUTH_CONST.__const: 0x9d0
+  __AUTH_CONST.__const: 0x9a0
   __AUTH_CONST.__cfstring: 0x18c0
-  __AUTH_CONST.__objc_const: 0x6790
+  __AUTH_CONST.__objc_const: 0x6708
   __AUTH_CONST.__objc_intobj: 0x438
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH.__objc_data: 0x14f0
-  __DATA.__objc_ivar: 0x36c
+  __DATA.__objc_ivar: 0x368
   __DATA.__data: 0x600
   __DATA.__bss: 0xf0
   __DATA.__common: 0x8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1642
-  Symbols:   3570
-  CStrings:  2067
+  Functions: 1637
+  Symbols:   3555
+  CStrings:  2045
 
Symbols:
+ -[MTRPluginClient registeredNodeIDs]
+ -[MTRPluginClient setRegisteredNodeIDs:]
+ -[MTRPluginLocalClient _deviceForControllerUUID:nodeID:]
+ -[MTRPluginLocalClient _deviceForControllerUUID:nodeID:].cold.1
+ -[MTRPluginLocalClient _registerDevice:]
+ OBJC_IVAR_$_MTRPluginClient._registeredNodeIDs
+ __205-[MTRPluginLocalClient deviceController:nodeID:invokeCommandWithEndpointID:clusterID:commandID:commandFields:expectedValues:expectedValueInterval:timedInvokeTimeout:serverSideProcessingTimeout:completion:]_block_invoke.28
+ __74-[MTRPluginLocalClient deviceController:nodeID:invokeCommands:completion:]_block_invoke.34
+ __85-[MTRPluginLocalClient deviceController:nodeID:downloadLogOfType:timeout:completion:]_block_invoke.38
+ ___40-[MTRPluginLocalClient _registerDevice:]_block_invoke
+ _objc_msgSend$_deviceForControllerUUID:nodeID:
+ _objc_msgSend$_registerDevice:
- -[MTRPluginDeviceControllerRegistry _forceUpdateRunningModeForController:]
- -[MTRPluginDeviceControllerRegistry devicesChangedForController:]
- -[MTRPluginLocalClient _deviceForControllerUUID:nodeID:requestedViaDelegate:]
- -[MTRPluginLocalClient _deviceForControllerUUID:nodeID:requestedViaDelegate:].cold.1
- -[MTRPluginLocalClient _registerDevice:addedViaDelegate:]
- -[MTRPluginLocalClient setTemporarilyRegisteredNodeIDs:]
- -[MTRPluginLocalClient setTemporaryDeviceCleanupSource:]
- -[MTRPluginLocalClient temporarilyRegisteredNodeIDs]
- -[MTRPluginLocalClient temporaryDeviceCleanupSource]
- GCC_except_table22
- GCC_except_table28
- OBJC_IVAR_$_MTRPluginLocalClient._temporarilyRegisteredNodeIDs
- OBJC_IVAR_$_MTRPluginLocalClient._temporaryDeviceCleanupSource
- __205-[MTRPluginLocalClient deviceController:nodeID:invokeCommandWithEndpointID:clusterID:commandID:commandFields:expectedValues:expectedValueInterval:timedInvokeTimeout:serverSideProcessingTimeout:completion:]_block_invoke.37
- __57-[MTRPluginLocalClient _registerDevice:addedViaDelegate:]_block_invoke.26
- __74-[MTRPluginLocalClient deviceController:nodeID:invokeCommands:completion:]_block_invoke.43
- __85-[MTRPluginLocalClient deviceController:nodeID:downloadLogOfType:timeout:completion:]_block_invoke.47
- __OBJC_CLASS_PROTOCOLS_$_MTRPluginDeviceControllerRegistry
- ___57-[MTRPluginLocalClient _registerDevice:addedViaDelegate:]_block_invoke
- ___block_descriptor_49_e8_32s40s_e5_v8?0l
- _objc_msgSend$_deviceForControllerUUID:nodeID:requestedViaDelegate:
- _objc_msgSend$_forceUpdateRunningModeForController:
- _objc_msgSend$_registerDevice:addedViaDelegate:
- _objc_msgSend$devices
- _objc_msgSend$setTemporarilyRegisteredNodeIDs:
- _objc_msgSend$setTemporaryDeviceCleanupSource:
- _objc_msgSend$temporarilyRegisteredNodeIDs
- _objc_msgSend$temporaryDeviceCleanupSource
CStrings:
+ "\x14"
+ "\x1e"
+ "%@  => controller: %@ self.pluginClient.registeredNodeIDs: %@"
+ "%@  => registering device: %@"
+ "%@ Setting running mode for controller: %@ to local, unsuspending controller"
+ "%@ Setting running mode for controller: %@ to remote, suspending controller"
+ "%@ Setting running mode for controller: %@ to unknown, resuming controller"
+ "<%@: %p xpc %p pid: %d, clientType: %@>"
+ "_deviceForControllerUUID:nodeID:"
+ "_registerDevice:"
+ "eventCount"
+ "reportCount"
- "\x01\x15"
- "\x1d"
- " => Device wasn't registered in temporary list, ignoring"
- "%@  => *** Not cleaning up temporary device, as it's permanent now: %@"
- "%@  => registering device: %@ addedViaDelegate: %@"
- "%@  => registering temporary device: %@ addedViaDelegate: %@"
- "%@  => unregistering temporary device: %@"
- "%@ => Done cleaning up temporary nodeIDs: %@"
- "%@ Cleaning up temporary nodeIDs: %@  (permanent ones: %@)"
- "%@ Device controller delegate devices changed for controller UUID %@ devices count %lu"
- "%@ Setting running mode for controller: %@ to local (forced pairing mode), unsuspending controller (devices count %lu)"
- "%@ Setting running mode for controller: %@ to local, but no active devices, suspending controller (devices count %lu)"
- "%@ Setting running mode for controller: %@ to local, resuming controller because we have active devices (devices count %lu)"
- "%@ Setting running mode for controller: %@ to remote, suspending controller (devices count %lu)"
- "%@ Setting running mode for controller: %@ to unknown, but no active devices, suspending controller (devices count %lu)"
- "%@ Setting running mode for controller: %@ to unknown, resuming controller because we have active devices (devices count %lu)"
- "%@ _forceUpdateRunningModeForController for controller %@"
- "%@ _forceUpdateRunningModeForController found controller UUID %@ homeUUID %@ current running mode %@"
- "<%@: %p xpc %p pid: %d, clientType: %@ registeredNodeIDs: %@>"
- "@36@0:8@16@24B32"
- "T@\"NSMutableSet\",&,V_temporarilyRegisteredNodeIDs"
- "T@\"NSObject<OS_dispatch_source>\",&,V_temporaryDeviceCleanupSource"
- "_deviceForControllerUUID:nodeID:requestedViaDelegate:"
- "_forceUpdateRunningModeForController:"
- "_registerDevice:addedViaDelegate:"
- "_temporarilyRegisteredNodeIDs"
- "_temporaryDeviceCleanupSource"
- "attributeCounter"
- "devices"
- "eventCounter"
- "setTemporarilyRegisteredNodeIDs:"
- "setTemporaryDeviceCleanupSource:"
- "temporarilyRegisteredNodeIDs"
- "temporaryDeviceCleanupSource"

```
