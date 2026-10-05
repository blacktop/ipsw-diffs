## memoryanalyticsd

> `/usr/libexec/memoryanalyticsd`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__auth_ptr`

```diff

-103.0.0.0.0
-  __TEXT.__text: 0x19054
-  __TEXT.__auth_stubs: 0xa70
-  __TEXT.__objc_stubs: 0x29e0
-  __TEXT.__objc_methlist: 0xc7c
-  __TEXT.__const: 0x208
-  __TEXT.__objc_methname: 0x2b69
-  __TEXT.__oslogstring: 0x3662
-  __TEXT.__objc_classname: 0x135
-  __TEXT.__objc_methtype: 0x3e8
-  __TEXT.__cstring: 0x348e
-  __TEXT.__gcc_except_tab: 0x1f4
-  __TEXT.__unwind_info: 0x720
-  __DATA_CONST.__const: 0xad8
-  __DATA_CONST.__cfstring: 0x35e0
-  __DATA_CONST.__objc_classlist: 0x80
+105.0.0.0.0
+  __TEXT.__text: 0x1b8d4
+  __TEXT.__auth_stubs: 0xb40
+  __TEXT.__objc_stubs: 0x3120
+  __TEXT.__objc_methlist: 0x10d4
+  __TEXT.__const: 0x220
+  __TEXT.__gcc_except_tab: 0x2e4
+  __TEXT.__cstring: 0x3731
+  __TEXT.__objc_methname: 0x3415
+  __TEXT.__oslogstring: 0x3976
+  __TEXT.__objc_classname: 0x213
+  __TEXT.__objc_methtype: 0x610
+  __TEXT.__unwind_info: 0x8c0
+  __DATA_CONST.__const: 0xc78
+  __DATA_CONST.__cfstring: 0x37c0
+  __DATA_CONST.__objc_classlist: 0xb8
+  __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x70
+  __DATA_CONST.__objc_superrefs: 0xa8
   __DATA_CONST.__objc_arraydata: 0x3d0
   __DATA_CONST.__objc_arrayobj: 0x60
   __DATA_CONST.__objc_intobj: 0x858
   __DATA_CONST.__objc_doubleobj: 0x1a0
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA_CONST.__auth_got: 0x548
-  __DATA_CONST.__got: 0x228
+  __DATA_CONST.__auth_got: 0x5b0
+  __DATA_CONST.__got: 0x238
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA.__objc_const: 0x17d8
-  __DATA.__objc_selrefs: 0xb48
-  __DATA.__objc_ivar: 0x134
-  __DATA.__objc_data: 0x500
-  __DATA.__data: 0x448
+  __DATA.__objc_const: 0x2210
+  __DATA.__objc_selrefs: 0xdc8
+  __DATA.__objc_ivar: 0x1a0
+  __DATA.__objc_data: 0x730
+  __DATA.__data: 0x568
   __DATA.__common: 0x29
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/DiagnosticRequest.framework/DiagnosticRequest
   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
   - /System/Library/PrivateFrameworks/MemoryDiagnostics.framework/MemoryDiagnostics
+  - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/OSAnalytics.framework/OSAnalytics
   - /System/Library/PrivateFrameworks/PowerLog.framework/PowerLog
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/Symbolication.framework/Symbolication
+  - /System/Library/PrivateFrameworks/Trial.framework/Trial
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 538
-  Symbols:   246
-  CStrings:  1438
+  Functions: 632
+  Symbols:   261
+  CStrings:  1629
 
Symbols:
+ _MKBDeviceUnlockedSinceBoot
+ _OBJC_CLASS_$_RBSProcessMonitor
+ _OBJC_CLASS_$_TRIClient
+ _access
+ _dispatch_after
+ _dispatch_assert_queue_not$V2
+ _dispatch_time
+ _mlock
+ _notify_cancel
+ _objc_copyWeak
+ _objc_destroyWeak
+ _objc_initWeak
+ _objc_loadWeakRetained
+ _objc_retain_x4
+ _unlink
CStrings:
+ "#16@0:8"
+ "/private/var/db/com.apple.memoryanalyticsd.model-loading-trial-enrolled"
+ "@\"<MTCameraActivityObserving>\""
+ "@\"<MTTrialFactorProviding>\""
+ "@\"MTCameraActivityState\""
+ "@\"MTModelLoadingTrialConfig\""
+ "@\"MTModelLoadingTrialConfigReader\""
+ "@\"MTStaticMemoryCost\""
+ "@\"NSNumber\"32@0:8@\"NSString\"16@\"NSString\"24"
+ "@\"NSObject<OS_os_transaction>\""
+ "@\"NSString\"16@0:8"
+ "@\"RBSProcessMonitor\""
+ "@\"TRIClient\""
+ "@24@0:8:16"
+ "@24@0:8Q16"
+ "@32@0:8:16@24"
+ "@32@0:8@16@24"
+ "@32@0:8d16@24"
+ "@40@0:8:16@24@32"
+ "@64@0:8@16@24@32@40@48@56"
+ "AAA"
+ "B24@0:8#16"
+ "B24@0:8:16"
+ "B24@0:8@\"NSString\"16"
+ "B24@0:8@\"Protocol\"16"
+ "Camera %{public}@"
+ "Could not observe %{public}s (status %u)"
+ "Could not read %{public}@ state (status %u)"
+ "Could not remove %{public}@: %{darwin.errno}d; launchd will keep relaunching a daemon with nothing to do"
+ "Could not write %{public}@: %{darwin.errno}d; the trial will not resume after a reboot"
+ "MEMORY_ANALYSIS_MODEL_LOADING"
+ "MTCameraActivityObserver"
+ "MTCameraActivityObserving"
+ "MTCameraActivityState"
+ "MTModelLoadingTrialConfig"
+ "MTModelLoadingTrialConfigReader"
+ "MTModelLoadingTrialEngine"
+ "MTStaticMemoryCost"
+ "MTTrialClient"
+ "MTTrialFactorProviding"
+ "Model loading trial active: static cost %lu MiB"
+ "Model loading trial configuration unchanged"
+ "Model loading trial disabled, tearing down"
+ "ModelLoadingTrial"
+ "ModelManager game assertion tier: %{public}@"
+ "NSObject"
+ "Received XPC Event via notifyd: notification name = %{public}@"
+ "StaticMemoryCostMiB"
+ "T#,R"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",R,C"
+ "T@?,C,N,V_activeStateChangedHandler"
+ "TB,R,N,GisCameraActive,V_cameraActive"
+ "TB,R,N,GisHoldingResidency"
+ "TB,R,N,GisReadable"
+ "TB,R,N,GisTrialReadable"
+ "TQ,R"
+ "TQ,R,N,V_staticCostMiB"
+ "Trial factor %{public}@ is not a long (case %d), using default"
+ "Trial factor %{public}@ out of range (%lld), clamping"
+ "Trial unreadable before first unlock, deferring"
+ "Vv16@0:8"
+ "XPC Event via notifyd carried no notification name"
+ "^{_NSZone=}16@0:8"
+ "_activeStateChangedHandler"
+ "_address"
+ "_appliedConfig"
+ "_cameraActive"
+ "_cameraObserver"
+ "_client"
+ "_configReader"
+ "_cooldown"
+ "_factorProvider"
+ "_firstUnlockToken"
+ "_foregroundPIDs"
+ "_gameAssertionNotificationName"
+ "_gameAssertionPolicy"
+ "_gameAssertionToken"
+ "_heldMiB"
+ "_keepAliveMarkerPath"
+ "_lockStatusToken"
+ "_processMonitor"
+ "_releaseGeneration"
+ "_residencyTransaction"
+ "_state"
+ "_staticCost"
+ "_staticCostMiB"
+ "active"
+ "activeStateChangedHandler"
+ "applyConfigurationOnQueue:"
+ "autorelease"
+ "cacheFactorLevelsWithNamespaceName:"
+ "cameraActive"
+ "class"
+ "client"
+ "com.apple.CameraHostedService"
+ "com.apple.camera"
+ "com.apple.camera.CameraMessagesApp"
+ "com.apple.camera.lockscreen"
+ "com.apple.memoryanalyticsd.model-loading-trial"
+ "com.apple.mobile.keybagd.first_unlock"
+ "com.apple.mobile.keybagd.lock_status"
+ "com.apple.system.console_mode_model_manager_assertion_changed"
+ "com.apple.trial.NamespaceUpdate.MEMORY_ANALYSIS_MODEL_LOADING"
+ "conformsToProtocol:"
+ "dealloc"
+ "factorLevelsWithNamespaceName:"
+ "gameAssertionDidChangeOnQueue"
+ "hasFactorLevelsWithNamespaceName:"
+ "hash"
+ "holdingResidency"
+ "inactive"
+ "initWithConfigReader:staticCost:gameAssertionNotificationName:cameraObserver:keepAliveMarkerPath:queue:"
+ "initWithCooldown:queue:"
+ "initWithFactorProvider:"
+ "initWithQueue:"
+ "initWithStaticCostMiB:"
+ "integerLevelForFactor:withNamespaceName:"
+ "isCameraActive"
+ "isHoldingResidency"
+ "isKindOfClass:"
+ "isMemberOfClass:"
+ "isProxy"
+ "isReadable"
+ "isTrialReadable"
+ "keepAliveMarkerExists"
+ "levelForFactor:withNamespaceName:"
+ "levelOneOfCase"
+ "longLongValue"
+ "longValue"
+ "mach_vm_allocate failed: %d"
+ "mach_vm_deallocate failed: %d"
+ "mlock failed: %{darwin.errno}d"
+ "monitorWithConfiguration:"
+ "none"
+ "noteProcess:foreground:forState:"
+ "numberWithLongLong:"
+ "performSelector:"
+ "performSelector:withObject:"
+ "performSelector:withObject:withObject:"
+ "predicateMatchingBundleIdentifiers:"
+ "readAndApplyOnQueue"
+ "readConfig"
+ "readGameAssertionOnQueue"
+ "readable"
+ "reapplyConfiguration"
+ "reevaluate"
+ "refresh"
+ "release"
+ "releaseHold"
+ "removeKeepAliveMarkerOnQueue"
+ "residentMiB"
+ "resizeToMiB:"
+ "respondsToSelector:"
+ "retain"
+ "retainCount"
+ "self"
+ "set"
+ "setActive:"
+ "setActiveStateChangedHandler:"
+ "setEvents:"
+ "setPredicates:"
+ "setProcess:foreground:"
+ "setStateDescriptor:"
+ "setUpdateHandler:"
+ "standard"
+ "startObservingCameraOnQueue"
+ "startObservingGameAssertionOnQueue"
+ "startProcessMonitor"
+ "startWithHandler:"
+ "state"
+ "states"
+ "staticCostMiB"
+ "stopObservingCameraOnQueue"
+ "stopObservingGameAssertionOnQueue"
+ "stopWaitingForTrialOnQueue"
+ "superclass"
+ "takeHoldOfMiB:"
+ "takeResidencyOnQueue"
+ "tearDownOnQueue"
+ "trialReadable"
+ "unrecognized"
+ "updateStaticCostOnQueue"
+ "v12@?0B8"
+ "v16@?0@\"<RBSProcessMonitorConfiguring>\"8"
+ "v24@0:8@?<v@?B>16"
+ "v24@0:8i16B20"
+ "v32@0:8i16B20@24"
+ "v32@?0@\"RBSProcessMonitor\"8@\"RBSProcessHandle\"16@\"RBSProcessStateUpdate\"24"
+ "waitForTrialOnQueue"
+ "writeKeepAliveMarkerOnQueue"
+ "zone"
- "Received XPC Event via notifyd: notification name = %@"
```
