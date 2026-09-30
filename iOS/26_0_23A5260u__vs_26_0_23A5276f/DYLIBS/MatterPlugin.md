## MatterPlugin

> `/System/Library/PrivateFrameworks/MatterPlugin.framework/MatterPlugin`

```diff

-64.0.0.0.0
-  __TEXT.__text: 0x4690c
+66.0.0.0.0
+  __TEXT.__text: 0x47bdc
   __TEXT.__auth_stubs: 0x7d0
-  __TEXT.__objc_methlist: 0x46dc
-  __TEXT.__const: 0xf8
-  __TEXT.__cstring: 0x11f3
-  __TEXT.__oslogstring: 0x5467
+  __TEXT.__objc_methlist: 0x473c
+  __TEXT.__const: 0x110
+  __TEXT.__cstring: 0x12a7
+  __TEXT.__oslogstring: 0x5744
   __TEXT.__gcc_except_tab: 0x1cd0
-  __TEXT.__unwind_info: 0x1128
-  __TEXT.__objc_classname: 0x9a2
-  __TEXT.__objc_methname: 0x77ba
-  __TEXT.__objc_methtype: 0x15d8
-  __TEXT.__objc_stubs: 0x5aa0
-  __DATA_CONST.__got: 0x440
-  __DATA_CONST.__const: 0x8a0
+  __TEXT.__unwind_info: 0x1138
+  __TEXT.__objc_classname: 0x9a0
+  __TEXT.__objc_methname: 0x797d
+  __TEXT.__objc_methtype: 0x15ed
+  __TEXT.__objc_stubs: 0x5d40
+  __DATA_CONST.__got: 0x460
+  __DATA_CONST.__const: 0x998
   __DATA_CONST.__objc_classlist: 0x218
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1b88
+  __DATA_CONST.__objc_selrefs: 0x1c30
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x180
   __DATA_CONST.__objc_arraydata: 0x40
   __AUTH_CONST.__auth_got: 0x3f8
   __AUTH_CONST.__const: 0x220
-  __AUTH_CONST.__cfstring: 0x18c0
-  __AUTH_CONST.__objc_const: 0x6798
+  __AUTH_CONST.__cfstring: 0x1980
+  __AUTH_CONST.__objc_const: 0x67f8
   __AUTH_CONST.__objc_intobj: 0x438
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH.__objc_data: 0x1400
-  __DATA.__objc_ivar: 0x36c
+  __DATA.__objc_ivar: 0x374
   __DATA.__data: 0x600
   __DATA.__bss: 0x80
   __DATA.__common: 0x8

   - /System/Library/PrivateFrameworks/HMFoundation.framework/HMFoundation
   - /System/Library/PrivateFrameworks/HomeKitMetrics.framework/HomeKitMetrics
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
+  - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3571410D-B934-346F-8A4A-3D7915D8C5FB
-  Functions: 1612
-  Symbols:   5166
-  CStrings:  2265
+  UUID: 2E265CEE-CA8F-3DE2-B779-5D75FB20EFB0
+  Functions: 1624
+  Symbols:   5214
+  CStrings:  2322
 
Symbols:
+ -[MTRPluginMetricsObserver observeEvent:]
+ -[MTRPluginServer _pidResumed:]
+ -[MTRPluginServer _pidSuspended:]
+ -[MTRPluginServer _processStateUpdated:]
+ -[MTRPluginServer _updateProcessMonitor]
+ -[MTRPluginServer pidToStatusMap]
+ -[MTRPluginServer processMonitor]
+ -[MTRPluginServer setPidToStatusMap:]
+ -[MTRPluginServer setProcessMonitor:]
+ _OBJC_CLASS_$_RBSProcessIdentifier
+ _OBJC_CLASS_$_RBSProcessMonitor
+ _OBJC_CLASS_$_RBSProcessPredicate
+ _OBJC_CLASS_$_RBSProcessStateDescriptor
+ _OBJC_IVAR_$_MTRPluginServer._pidToStatusMap
+ _OBJC_IVAR_$_MTRPluginServer._processMonitor
+ ___33-[MTRPluginServer _pidSuspended:]_block_invoke
+ ___40-[MTRPluginServer _updateProcessMonitor]_block_invoke
+ ___40-[MTRPluginServer _updateProcessMonitor]_block_invoke.57
+ ___40-[MTRPluginServer _updateProcessMonitor]_block_invoke.58
+ ___62-[MTRPluginServer _deliverMessageToDelegate:homeUUID:timeout:]_block_invoke.46
+ ___62-[MTRPluginServer _deliverMessageToDelegate:homeUUID:timeout:]_block_invoke.46.cold.1
+ ___block_descriptor_40_e8_32s_e74_v32?0"RBSProcessMonitor"8"RBSProcessHandle"16"RBSProcessStateUpdate"24ls32l8
+ ___block_descriptor_44_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_48_e8_32s40s_e40_v16?0"<RBSProcessMonitorConfiguring>"8ls32l8s40l8
+ ___block_literal_global.105
+ ___block_literal_global.38
+ ___block_literal_global.96
+ _objc_msgSend$_pidResumed:
+ _objc_msgSend$_pidSuspended:
+ _objc_msgSend$_processStateUpdated:
+ _objc_msgSend$_updateProcessMonitor
+ _objc_msgSend$arrayWithObject:
+ _objc_msgSend$descriptor
+ _objc_msgSend$identifierForIdentifier:
+ _objc_msgSend$monitor
+ _objc_msgSend$pidToStatusMap
+ _objc_msgSend$predicateMatchingIdentifiers:
+ _objc_msgSend$previousState
+ _objc_msgSend$process
+ _objc_msgSend$processMonitor
+ _objc_msgSend$rangeOfString:
+ _objc_msgSend$setPidToStatusMap:
+ _objc_msgSend$setPredicates:
+ _objc_msgSend$setProcessMonitor:
+ _objc_msgSend$setStateDescriptor:
+ _objc_msgSend$setUpdateHandler:
+ _objc_msgSend$taskState
+ _objc_msgSend$updateConfiguration:
+ _swizzlePrewarm.onceToken.103
- -[MTRPluginMetricsObserver didReceiveEventFromDispatcher:]
- ___62-[MTRPluginServer _deliverMessageToDelegate:homeUUID:timeout:]_block_invoke.43
- ___62-[MTRPluginServer _deliverMessageToDelegate:homeUUID:timeout:]_block_invoke.43.cold.1
- ___block_literal_global.36
- ___block_literal_global.78
- ___block_literal_global.87
- _swizzlePrewarm.onceToken.85
CStrings:
+ " => %@ client type found pid: %d"
+ " => (Main Queue) Process monitor update handler invoked for PID: %d"
+ " => Found matching connection: %@, removing all delegates"
+ " => Ignoring client type: %@ for pid: %d"
+ " => pid %d No state"
+ " => pid %d running"
+ " => pid %d suspended"
+ " => pid %d unhandled state: %d"
+ " => pid %d unknown running state"
+ " => pid %d unknown state"
+ "@\"RBSProcessMonitor\""
+ "Bulletin"
+ "Carousel"
+ "Checking connection: %@   clientType: %@   pid: %d"
+ "Failed to remove pid from process map, pid was missing from connection"
+ "Intent"
+ "Notification"
+ "Process monitor update handler invoked for PID: %d"
+ "T@\"NSMutableDictionary\",&,V_pidToStatusMap"
+ "T@\"RBSProcessMonitor\",&,V_processMonitor"
+ "Updating process monitor config: %@"
+ "Updating process monitor, with pids to monitor: %@"
+ "Updating process state updated: %d   from: %d  to: %d"
+ "Widget"
+ "_pidResumed:"
+ "_pidSuspended:"
+ "_pidToStatusMap"
+ "_processMonitor"
+ "_processStateUpdated:"
+ "_updateProcessMonitor"
+ "arrayWithObject:"
+ "com.apple.NanoHome"
+ "descriptor"
+ "identifierForIdentifier:"
+ "monitor"
+ "observeEvent:"
+ "pid suspended: %d will check state in %d seconds"
+ "pid: %d is still running after %d seconds, not invalidating connection"
+ "pid: %d is still suspended after %d seconds, checking connection"
+ "pidToStatusMap"
+ "predicateMatchingIdentifiers:"
+ "previousState"
+ "process"
+ "processMonitor"
+ "rangeOfString:"
+ "setPidToStatusMap:"
+ "setPredicates:"
+ "setProcessMonitor:"
+ "setStateDescriptor:"
+ "setUpdateHandler:"
+ "taskState"
+ "updateConfiguration:"
+ "v16@?0@\"<RBSProcessMonitorConfiguring>\"8"
+ "v32@?0@\"RBSProcessMonitor\"8@\"RBSProcessHandle\"16@\"RBSProcessStateUpdate\"24"
- "%@  => DOUBLE registering device (already registered): %@"
- "%@ Cannot call addDelegate again to device %@ - ignoring"
- "didReceiveEventFromDispatcher:"

```
