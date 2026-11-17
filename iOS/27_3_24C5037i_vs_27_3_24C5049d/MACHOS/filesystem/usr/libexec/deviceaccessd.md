## deviceaccessd

> `/usr/libexec/deviceaccessd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methtype`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-2702.5.0.0.0
-  __TEXT.__text: 0x9567c
-  __TEXT.__auth_stubs: 0x22a0
-  __TEXT.__objc_stubs: 0x85c0
-  __TEXT.__objc_methlist: 0x28a0
-  __TEXT.__const: 0x1d68
-  __TEXT.__cstring: 0x16aa4
+2702.8.0.0.0
+  __TEXT.__text: 0x98c70
+  __TEXT.__auth_stubs: 0x22b0
+  __TEXT.__objc_stubs: 0x8960
+  __TEXT.__objc_methlist: 0x2920
+  __TEXT.__const: 0x1d78
+  __TEXT.__cstring: 0x16f64
   __TEXT.__objc_classname: 0x3f5
   __TEXT.__objc_methtype: 0x1bda
-  __TEXT.__gcc_except_tab: 0x4610
-  __TEXT.__objc_methname: 0xab1f
+  __TEXT.__gcc_except_tab: 0x4980
+  __TEXT.__objc_methname: 0xae9f
   __TEXT.__dlopen_cstrs: 0x62
   __TEXT.__swift5_typeref: 0x9ee
   __TEXT.__swift5_fieldmd: 0x490

   __TEXT.__swift_as_ret: 0x24
   __TEXT.__swift_as_cont: 0x3c
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x24a8
+  __TEXT.__unwind_info: 0x24d8
   __TEXT.__eh_frame: 0x10a8
-  __DATA_CONST.__const: 0x29c0
-  __DATA_CONST.__cfstring: 0x22a0
+  __DATA_CONST.__const: 0x2980
+  __DATA_CONST.__cfstring: 0x2340
   __DATA_CONST.__objc_classlist: 0xa0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x48
+  __DATA_CONST.__objc_intobj: 0xd8
   __DATA_CONST.__objc_arraydata: 0x88
   __DATA_CONST.__objc_arrayobj: 0x48
-  __DATA_CONST.__objc_intobj: 0xc0
-  __DATA_CONST.__auth_got: 0x1160
-  __DATA_CONST.__got: 0x8d8
+  __DATA_CONST.__auth_got: 0x1168
+  __DATA_CONST.__got: 0x8e8
   __DATA_CONST.__auth_ptr: 0x2b8
-  __DATA.__objc_const: 0x3728
-  __DATA.__objc_selrefs: 0x28e8
-  __DATA.__objc_ivar: 0x308
+  __DATA.__objc_const: 0x3778
+  __DATA.__objc_selrefs: 0x29d8
+  __DATA.__objc_ivar: 0x310
   __DATA.__objc_data: 0x8c0
   __DATA.__data: 0x13e8
   __DATA.__common: 0x38

   - /System/Library/PrivateFrameworks/AccessorySetupKitCore.framework/AccessorySetupKitCore
   - /System/Library/PrivateFrameworks/AppConduit.framework/AppConduit
   - /System/Library/PrivateFrameworks/ApplePushService.framework/ApplePushService
+  - /System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/BackgroundSystemTasks
   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
   - /System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi
   - /System/Library/PrivateFrameworks/DANECPWrapper.framework/DANECPWrapper

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2573
-  Symbols:   918
-  CStrings:  4157
+  Functions: 2592
+  Symbols:   921
+  CStrings:  4221
 
Symbols:
+ _OBJC_CLASS_$_BGNonRepeatingSystemTaskRequest
+ _OBJC_CLASS_$_BGSystemTaskScheduler
+ _SipHash
CStrings:
+ "### Asserted %@ refused, '%@' is not paired with LE Secure Connections"
+ "### MigrateAppAccess moved per-app service '%@' %@ -> %@ on %@"
+ "### RemoveAppsAccess: removing %@ for '%@' failed: %@"
+ "### RemovedDevice: failed to delete messages for '%@': %@"
+ "### Secure Connections check for '%@' failed: %@"
+ "### Skip adding extension session, '%@' has no authorized feature: %@"
+ "### Worker task %@ was not submitted, registered %s: %@"
+ "'%@' has no authorized feature on device '%@'"
+ "'%@' is not granted %@ on device '%@'"
+ "-[DABluetoothPairingManager _addNewTask:completion:bluetoothOp:pairCTKD:displayName:taskTimeout:appConfirmsAuth:supportsHID:classicOnly:launchedWithProximityPairing:]"
+ "-[DABluetoothPairingManager persistBluetoothDevice:pairingRequired:pairWithCTKD:displayName:taskTimeout:appConfirmsAuth:supportsHID:pairClassicOnly:launchedWithProximityPairing:completion:]"
+ "-[DADaemonServer _authorizedExtensionBundleIDsForDevice:]"
+ "-[DADaemonServer _isSecureConnectionsPairedDevice:bundleID:]"
+ "-[DADaemonServer _reportRemovedDevice:appID:discovery:]_block_invoke"
+ "-[DADaemonServer _updateAssertedFlagsForDaemonSession:]"
+ "-[DADaemonServer setUpTCCNotificationForService:]_block_invoke_2"
+ "-[DAExtensionCoordinator _workerTaskExpired:flag:]"
+ "-[DAExtensionCoordinator _workerTaskFinish:]"
+ "-[DAExtensionCoordinator _workerTaskIdentifier:]"
+ "-[DAExtensionCoordinator _workerTaskLaunched:flag:]"
+ "-[DAExtensionCoordinator _workerTaskSubmit:]"
+ "AccessoryGPUWorker"
+ "AccessoryWorker"
+ "Added daemon session for '%@': %@"
+ "CPU"
+ "Device '%@' has authorized extension features for %@"
+ "ExtensionSessionRuntimeAssertion: '%@' resolved to app '%@'"
+ "GPU"
+ "GetDevices: stored device unreadable, returning the coordinator's copy: %@"
+ "No authorized extension feature, device not found: %@"
+ "RemovedDevice: deleted all messages for '%@'"
+ "TB,N,V_launchedWithProximityPairing"
+ "TCC authorization updated previous: %lu, current: %lu for deviceID:%@ service:%@ app:%@"
+ "Worker task %@ cancelled"
+ "Worker task %@ completed"
+ "Worker task %@ expired, dasd suspended %@"
+ "Worker task %@ launched"
+ "Worker task %@ launched after release, completing"
+ "Worker task %@ left by a previous launch, cancelled"
+ "Worker task %@ submitted %s"
+ "Worker task hashes: BundleID '%@' -> %016llx, DeviceID '%@' -> %016llx"
+ "_addNewTask:completion:bluetoothOp:pairCTKD:displayName:taskTimeout:appConfirmsAuth:supportsHID:classicOnly:launchedWithProximityPairing:"
+ "_authorizedExtensionBundleIDsForDevice:"
+ "_daemonExtensionSessions"
+ "_daemonExtensionsMap"
+ "_isSecureConnectionsPairedDevice:bundleID:"
+ "_launchedWithProximityPairing"
+ "_runnableAssertedFlags"
+ "_workerTaskExpired:flag:"
+ "_workerTaskFinish:"
+ "_workerTaskIdentifier:"
+ "_workerTaskLaunched:flag:"
+ "_workerTaskMap"
+ "_workerTaskSubmit:"
+ "accessoryServicesMapForBundleID:"
+ "appServices"
+ "appServicesInternalMap"
+ "cancelTaskRequestWithIdentifier:error:"
+ "com.apple.deviceaccessd.%@.%016llx.%016llx"
+ "compare:"
+ "dasd declined %@"
+ "dasd stopped %@"
+ "deregisterTaskWithIdentifier:"
+ "extensionWithBundleID:"
+ "initWithBundleIdentifier:error:"
+ "launchedWithProximityPairing"
+ "launchedWithProximityPairing %d"
+ "loadPersistentServices:authorizations:"
+ "missing capability flags"
+ "no bundle ID for %@"
+ "no bundle ID: %@"
+ "normalizedPersistentServices:"
+ "persistBluetoothDevice:pairingRequired:pairWithCTKD:displayName:taskTimeout:appConfirmsAuth:supportsHID:pairClassicOnly:launchedWithProximityPairing:completion:"
+ "registerForTaskWithIdentifier:usingQueue:launchHandler:"
+ "scopedToBundleID:"
+ "setAppServicesInternalMap:"
+ "setEncodeAppServices:"
+ "setExpirationHandler:"
+ "setLaunchedWithProximityPairing:"
+ "setPriority:"
+ "setRelatedApplications:"
+ "setResources:"
+ "setTaskCompleted"
+ "sharedScheduler"
+ "sortedArrayUsingSelector:"
+ "submitTaskRequest:error:"
+ "v16@?0@\"BGSystemTask\"8"
+ "v72@0:8@16B24B28@32@40B48B52B56B60@?64"
+ "v76@0:8@16@?24q32B40@44@52B60B64B68B72"
- "### Failed to delete messages for device '%@': %@"
- "### Skip adding extension session with no authorized feature: %@"
- "-[DABluetoothPairingManager _addNewTask:completion:bluetoothOp:pairCTKD:displayName:taskTimeout:appConfirmsAuth:supportsHID:classicOnly:]"
- "-[DABluetoothPairingManager persistBluetoothDevice:pairingRequired:pairWithCTKD:displayName:taskTimeout:appConfirmsAuth:supportsHID:pairClassicOnly:completion:]"
- "-[DADaemonServer _deviceHasAuthorizedExtensionFeature:bundleID:]"
- "-[DADaemonServer _deviceHasAuthorizedExtensionFeature:bundleID:]_block_invoke_2"
- "-[DADaemonServer getDevicesWithFlags:appID:error:]_block_invoke_4"
- "-[DAExtensionCoordinator _deleteMessagesForDevice:]_block_invoke"
- "Added daemon session: %@"
- "Deleted all messages for device: '%@'"
- "Device '%@' has authorized extension feature: %@, Level %lu"
- "No authorized extension feature, missing access info: %@"
- "No authorized extension feature, missing bundle identifier: %@"
- "No authorized extension feature, missing services: %@"
- "No authorized extension feature, not authorized (info): %@"
- "No authorized extension feature, not authorized (service): %@"
- "[ServiceInfo Decoding Error] %@"
- "_addNewTask:completion:bluetoothOp:pairCTKD:displayName:taskTimeout:appConfirmsAuth:supportsHID:classicOnly:"
- "_deviceHasAuthorizedExtensionFeature:bundleID:"
- "_extensionSessionMap"
- "initWithPersistentDictionaryRepresentation:deviceID:error:"
- "persistBluetoothDevice:pairingRequired:pairWithCTKD:displayName:taskTimeout:appConfirmsAuth:supportsHID:pairClassicOnly:completion:"
- "v32@?0@\"NSString\"8@\"DADaemonExtensionSession\"16^B24"
- "v68@0:8@16B24B28@32@40B48B52B56@?60"
- "v72@0:8@16@?24q32B40@44@52B60B64B68"
```
