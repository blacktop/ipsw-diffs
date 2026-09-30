## BackgroundSecurityImprovement

> `/System/Library/PreferenceBundles/BackgroundSecurityImprovement.bundle/BackgroundSecurityImprovement`

```diff

-508.40.55.0.0
-  __TEXT.__text: 0x96ff0
-  __TEXT.__auth_stubs: 0x1370
-  __TEXT.__objc_methlist: 0x394
-  __TEXT.__const: 0x1e8c
-  __TEXT.__swift5_typeref: 0x39bc
-  __TEXT.__cstring: 0x16e0
-  __TEXT.__objc_methname: 0xc7d
-  __TEXT.__swift5_capture: 0x1a10
-  __TEXT.__oslogstring: 0x186c
-  __TEXT.__swift5_reflstr: 0x660
-  __TEXT.__swift5_assocty: 0xd8
-  __TEXT.__constg_swiftt: 0x78c
-  __TEXT.__swift5_fieldmd: 0x400
-  __TEXT.__swift5_proto: 0x3c
-  __TEXT.__swift5_types: 0x88
-  __TEXT.__swift5_builtin: 0x3c
+508.60.28.502.1
+  __TEXT.__text: 0xa2d7c
+  __TEXT.__auth_stubs: 0x13a0
+  __TEXT.__objc_methlist: 0x3ac
+  __TEXT.__const: 0x1eac
+  __TEXT.__swift5_typeref: 0x3a70
+  __TEXT.__cstring: 0x18e0
+  __TEXT.__objc_methname: 0xd22
+  __TEXT.__swift5_capture: 0x1cf4
+  __TEXT.__oslogstring: 0x1d13
+  __TEXT.__swift5_reflstr: 0x740
+  __TEXT.__swift5_assocty: 0xf0
+  __TEXT.__constg_swiftt: 0x7a8
+  __TEXT.__swift5_fieldmd: 0x448
+  __TEXT.__swift5_proto: 0x40
+  __TEXT.__swift5_types: 0x8c
+  __TEXT.__swift5_builtin: 0x50
   __TEXT.__swift5_mpenum: 0x14
-  __TEXT.__swift_as_entry: 0xb0
+  __TEXT.__swift_as_entry: 0xb8
   __TEXT.__swift_as_ret: 0x5c
   __TEXT.__objc_classname: 0x21
   __TEXT.__objc_methtype: 0x630
-  __TEXT.__unwind_info: 0x1858
-  __TEXT.__eh_frame: 0x14bc
-  __DATA_CONST.__auth_got: 0x9b8
-  __DATA_CONST.__got: 0x418
+  __TEXT.__unwind_info: 0x1b38
+  __TEXT.__eh_frame: 0x1764
+  __DATA_CONST.__auth_got: 0x9d0
+  __DATA_CONST.__got: 0x4b0
   __DATA_CONST.__auth_ptr: 0x3b8
-  __DATA_CONST.__const: 0x42b0
+  __DATA_CONST.__const: 0x4a00
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA.__objc_const: 0x5e8
-  __DATA.__objc_selrefs: 0x3e0
-  __DATA.__objc_data: 0x170
-  __DATA.__data: 0x1010
-  __DATA.__bss: 0x970
+  __DATA.__objc_const: 0x648
+  __DATA.__objc_selrefs: 0x428
+  __DATA.__objc_data: 0x188
+  __DATA.__data: 0x1050
+  __DATA.__bss: 0x9f0
   __DATA.__common: 0x30
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 814392E5-458B-30B7-BE87-0DDC85E75FE7
-  Functions: 2254
-  Symbols:   143
-  CStrings:  415
+  UUID: 22B8D42D-9FB1-3B20-935C-C473502FAE86
+  Functions: 2442
+  Symbols:   149
+  CStrings:  458
 
Symbols:
+ _OBJC_CLASS_$_SUCoreDevice
+ _OBJC_CLASS_$_SUUtility
+ _OBJC_CLASS_$_UIDevice
+ _UIDeviceBatteryLevelDidChangeNotification
+ _UIDeviceBatteryStateDidChangeNotification
+ _swift_dynamicCastMetatype
CStrings:
+ "% battery while connected to a power source."
+ "% battery."
+ "%@"
+ "%d"
+ "%f"
+ "%lf"
+ "%lld"
+ "%llu"
+ "%u"
+ "Attempted to change state from .waitingForReboot to %s - waitingForReboot is a terminal state and cannot be changed"
+ "Background Security Improvements cannot be managed while software update is in progress."
+ "Battery level changed: %f -> %f"
+ "Battery monitoring initialized: level=%f, connected=%{bool}d"
+ "Battery state changed: %{bool}d -> %{bool}d"
+ "Float value cannot be converted to Int because it is either infinite or NaN"
+ "Float value cannot be converted to Int because the result would be greater than Int.max"
+ "Float value cannot be converted to Int because the result would be less than Int.min"
+ "No entries in InstallHistoryEvents, lastUpdateHistoryEntry will stay nil"
+ "Rollback in progress (suClient.isRollingBack) not detected"
+ "Rollback is disabled in preferencesManager"
+ "Rollback is running"
+ "SUUtility.isSplatOnlyUpdateInstalled is false, lastInstalledSplatUpdate will stay nil"
+ "Semi-splat (SUCoreDevice.shared().hasSemiSplatActive) is not active"
+ "Semi-splat active detected, setting state to waitingForReboot and quit initializeState"
+ "StatefulManager initialized"
+ "Swift/IntegerTypes.swift"
+ "This security improvement requires at least "
+ "_batteryLevel"
+ "_connectedToPowerSource"
+ "_lastInstalledSplatUpdate"
+ "_lastInstalledSplatUpdateDocumentationData"
+ "_lastUpdateHistoryEntry"
+ "addObserver:selector:name:object:"
+ "batteryLevel"
+ "batteryLevelChanged"
+ "batteryState"
+ "batteryStateChanged"
+ "com.apple.SoftwareUpdateUI"
+ "currentDevice"
+ "getSplatDocumentationData().readmeSummary is nil"
+ "hasNonSplatDescriptor is true, can't allow rollback in this state"
+ "hasSemiSplatActive"
+ "info.circle"
+ "isAutomaticSecurityUpdatesManaged: shouldDisableAutoInstallRSRToggle returned %{bool}d"
+ "isSplatOnlyUpdateInstalled"
+ "isSplatOnlyUpdateRollbackAllowed is %{bool}d, that will determine if we can allow rollback action"
+ "lastInstalledSplatUpdate: %s"
+ "lastUpdateHistoryEntry: %s"
+ "managerState == .checking, can't allow rollback yet"
+ "managerState == .idle, can't allow rollback yet"
+ "managerState == .installing, can't allow rollback at this point"
+ "managerState == .waitingForReboot, can't allow rollback at this point"
+ "operationRawValue is not SUS_HISTORY_OP_INSTALL_COMPLETE, lastInstalledSplatUpdate will stay nil"
+ "setBatteryMonitoringEnabled:"
+ "sharedDevice"
+ "shouldDisableAutoInstallRSRToggle"
- "Background Security Updates cannot be managed while software update is in progress."
- "Clicked 'Remove' Action in UpdateHistoryView but Rollback not Allowed"
- "Received rollbackDidFail event with descriptor: %s,\nbut that's not the displaying descriptor: %s, ignoring this callback"
- "Received rollbackDidFinish event with descriptor: %s, \nbut that's not the displaying descriptor: %s, ignoring this callback"
- "Security update history loaded: %s"
- "UILogic"
- "_lastUpdateHistory"
- "_splatDocumentationData"
- "autoInstallSecurityResponseForceOff"
- "autoInstallSecurityResponseForceOn"
- "ellipsis.circle"
- "found last event"
- "no events"

```
