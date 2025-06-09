## DoNotDisturbServer

> `/System/Library/PrivateFrameworks/DoNotDisturbServer.framework/DoNotDisturbServer`

```diff

-433.6.1.0.0
-  __TEXT.__text: 0xc2d18
-  __TEXT.__auth_stubs: 0x1340
-  __TEXT.__objc_methlist: 0xa908
-  __TEXT.__const: 0x458
-  __TEXT.__cstring: 0x8894
-  __TEXT.__oslogstring: 0x11270
+461.0.0.0.0
+  __TEXT.__text: 0xc3190
+  __TEXT.__auth_stubs: 0x1350
+  __TEXT.__objc_methlist: 0xa9d8
+  __TEXT.__const: 0x520
+  __TEXT.__cstring: 0x8924
+  __TEXT.__oslogstring: 0x11390
   __TEXT.__gcc_except_tab: 0xf74
   __TEXT.__dlopen_cstrs: 0x59
   __TEXT.__constg_swiftt: 0x14c

   __TEXT.__swift5_proto: 0xc
   __TEXT.__swift_as_entry: 0x2c
   __TEXT.__swift_as_ret: 0x2c
-  __TEXT.__unwind_info: 0x2800
-  __TEXT.__eh_frame: 0x540
-  __TEXT.__objc_classname: 0x28c2
-  __TEXT.__objc_methname: 0x19818
-  __TEXT.__objc_methtype: 0x7570
-  __TEXT.__objc_stubs: 0x10ae0
-  __DATA_CONST.__got: 0xe58
-  __DATA_CONST.__const: 0x25d8
+  __TEXT.__unwind_info: 0x2818
+  __TEXT.__eh_frame: 0x530
+  __TEXT.__objc_classname: 0x28e9
+  __TEXT.__objc_methname: 0x19a50
+  __TEXT.__objc_methtype: 0x7688
+  __TEXT.__objc_stubs: 0x10ba0
+  __DATA_CONST.__got: 0xe60
+  __DATA_CONST.__const: 0x25f8
   __DATA_CONST.__objc_classlist: 0x5f8
   __DATA_CONST.__objc_catlist: 0x148
-  __DATA_CONST.__objc_protolist: 0x3d0
+  __DATA_CONST.__objc_protolist: 0x3d8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4c58
+  __DATA_CONST.__objc_selrefs: 0x4ca8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x3e0
   __DATA_CONST.__objc_arraydata: 0x330
-  __AUTH_CONST.__auth_got: 0x9b0
-  __AUTH_CONST.__const: 0x1030
-  __AUTH_CONST.__cfstring: 0x7940
-  __AUTH_CONST.__objc_const: 0x25f38
+  __AUTH_CONST.__auth_got: 0x9b8
+  __AUTH_CONST.__const: 0x1058
+  __AUTH_CONST.__cfstring: 0x7980
+  __AUTH_CONST.__objc_const: 0x25fb0
   __AUTH_CONST.__objc_intobj: 0x2d0
   __AUTH_CONST.__objc_dictobj: 0x488
   __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH.__objc_data: 0x808
-  __DATA.__objc_ivar: 0xa38
-  __DATA.__data: 0x3330
+  __DATA.__objc_ivar: 0xa3c
+  __DATA.__data: 0x32c0
   __DATA.__bss: 0x1c0
   __DATA_DIRTY.__objc_data: 0x3568
   __DATA_DIRTY.__data: 0xa8

   - /System/Library/Frameworks/HealthKit.framework/HealthKit
   - /System/Library/Frameworks/Intents.framework/Intents
   - /System/Library/Frameworks/Network.framework/Network
+  - /System/Library/Frameworks/_LocationEssentials.framework/_LocationEssentials
   - /System/Library/PrivateFrameworks/AppPredictionClient.framework/AppPredictionClient
   - /System/Library/PrivateFrameworks/AvailabilityKit.framework/AvailabilityKit
   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard

   - /System/Library/PrivateFrameworks/WorkflowUIServices.framework/WorkflowUIServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib

   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_errno.dylib
-  - /usr/lib/swift/libswift_math.dylib
-  - /usr/lib/swift/libswift_signal.dylib
-  - /usr/lib/swift/libswift_stdio.dylib
-  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  - /usr/lib/swift/libswiftsys_time.dylib
-  - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 38377036-0F65-3F1A-B74C-C5AE20E839DD
-  Functions: 3786
-  Symbols:   14317
-  CStrings:  7604
+  UUID: 0FE9A9B4-C8A8-31AD-B26F-08C42346555E
+  Functions: 3806
+  Symbols:   14327
+  CStrings:  7630
 
Symbols:
+ -[DNDSAppConfigurationManager appSpecificSettingsManager:receivedSyncedAppSpecificSettings:ofType:applicationIdentifier:modeIdentifier:]
+ -[DNDSAppConfigurationManager appSpecificSettingsManager:receivedSyncedClearForAppSpecificSettings:ofType:applicationIdentifier:modeIdentifier:]
+ -[DNDSAppFocusConfigurationCoordinator _effectiveBundleIDForBundleID:]
+ -[DNDSAppFocusConfigurationCoordinator resetAppConfigurationState]
+ -[DNDSAppSpecificSettingsManager appSpecificSettingsDictinariesForModeIdentifier:]
+ -[DNDSAppSpecificSettingsManager delegate]
+ -[DNDSAppSpecificSettingsManager setDelegate:]
+ -[DNDSMeDeviceService devicesChanged]
+ -[DNDSMeDeviceService meDeviceChanged]
+ -[DNDSRemoteServiceProvider resetAppConfigurationStateWithRequestDetails:completionHandler:]
+ -[DNDSRemoteServiceProvider resetAppConfigurationStateWithRequestDetails:completionHandler:].cold.1
+ -[DNDSServer remoteServiceProviderResetAppConfigurationState:]
+ GCC_except_table110
+ GCC_except_table164
+ GCC_except_table20
+ GCC_except_table34
+ _OBJC_IVAR_$_DNDSAppSpecificSettingsManager._delegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_DNDSAppSpecificSettingsManagerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_DNDSAppSpecificSettingsManagerDelegate
+ __OBJC_$_PROTOCOL_REFS_DNDSAppSpecificSettingsManagerDelegate
+ __OBJC_LABEL_PROTOCOL_$_DNDSAppSpecificSettingsManagerDelegate
+ __OBJC_PROTOCOL_$_DNDSAppSpecificSettingsManagerDelegate
+ ___37-[DNDSMeDeviceService devicesChanged]_block_invoke
+ ___38-[DNDSMeDeviceService meDeviceChanged]_block_invoke
+ ___48-[DNDSMeDeviceService _loadDataFromBackingStore]_block_invoke.26
+ ___53-[DNDSMeDeviceService startMonitoringMeDeviceChanges]_block_invoke.14
+ ___53-[DNDSMeDeviceService startMonitoringMeDeviceChanges]_block_invoke.15
+ ___65-[DNDSMetricsManager assertionTaken:withClientDetails:lockState:]_block_invoke.312
+ ___66-[DNDSAppFocusConfigurationCoordinator resetAppConfigurationState]_block_invoke
+ ___68-[DNDSAppFocusConfigurationCoordinator _workQueue_handleFirstLaunch]_block_invoke_3
+ ___82-[DNDSAppSpecificSettingsManager appSpecificSettingsDictinariesForModeIdentifier:]_block_invoke
+ ___82-[DNDSAppSpecificSettingsManager appSpecificSettingsDictinariesForModeIdentifier:]_block_invoke.cold.1
+ ___block_descriptor_40_e8_32s_e34_16?0"DNDApplicationIdentifier"8ls32l8
+ __swiftImmortalRefCount
+ __swift_FORCE_LOAD_$_swiftAccelerate
+ __swift_FORCE_LOAD_$_swiftAccelerate_$_DoNotDisturbServer
+ __swift_FORCE_LOAD_$_swiftCoreImage
+ __swift_FORCE_LOAD_$_swiftCoreImage_$_DoNotDisturbServer
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers_$_DoNotDisturbServer
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_DoNotDisturbServer
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_DoNotDisturbServer
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_DoNotDisturbServer
+ _fmlDevicesChangedNotificationCallback
+ _fmlMeDeviceChangedNotificationCallback
+ _objc_msgSend$_effectiveBundleIDForBundleID:
+ _objc_msgSend$appSpecificSettingsDictinariesForModeIdentifier:
+ _objc_msgSend$devicesChanged
+ _objc_msgSend$initWithType:bundleIdentifier:url:
+ _objc_msgSend$meDeviceChanged
+ _objc_msgSend$remoteServiceProviderResetAppConfigurationState:
+ _objc_msgSend$resetAppConfigurationState
- GCC_except_table107
- GCC_except_table163
- GCC_except_table18
- GCC_except_table22
- GCC_except_table24
- GCC_except_table30
- GCC_except_table33
- ___48-[DNDSMeDeviceService _loadDataFromBackingStore]_block_invoke.20
- ___53-[DNDSMeDeviceService startMonitoringMeDeviceChanges]_block_invoke.8
- ___53-[DNDSMeDeviceService startMonitoringMeDeviceChanges]_block_invoke.9
- ___65-[DNDSMetricsManager assertionTaken:withClientDetails:lockState:]_block_invoke.309
- ___68-[DNDSAppSpecificSettingsManager idsSyncEngine:prepareRecordToSave:]_block_invoke
- ___68-[DNDSAppSpecificSettingsManager idsSyncEngine:prepareRecordToSave:]_block_invoke.cold.1
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_errno_$_DoNotDisturbServer
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_math_$_DoNotDisturbServer
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_signal_$_DoNotDisturbServer
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_stdio_$_DoNotDisturbServer
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swift_time_$_DoNotDisturbServer
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftsys_time_$_DoNotDisturbServer
- __swift_FORCE_LOAD_$_swiftunistd
- __swift_FORCE_LOAD_$_swiftunistd_$_DoNotDisturbServer
- _objc_msgSend$initWithType:bundleIdentifier:
CStrings:
+ "@\"<DNDSAppSpecificSettingsManagerDelegate>\""
+ "@16@?0@\"DNDApplicationIdentifier\"8"
+ "B24@0:8@\"DNDSRemoteServiceProvider\"16"
+ "DNDSAppSpecificSettingsManagerDelegate"
+ "FMLDevicesChangedNotification"
+ "FMLMeDeviceChangedNotification"
+ "T@\"<DNDSAppSpecificSettingsManagerDelegate>\",W,N,V_delegate"
+ "[%{public}@] XPC connection without any valid entitlements tried to reset app configuration state, will invalidate: connection=%{public}@"
+ "_effectiveBundleIDForBundleID:"
+ "appSpecificSettingsDictinariesForModeIdentifier:"
+ "appSpecificSettingsManager:receivedSyncedAppSpecificSettings:ofType:applicationIdentifier:modeIdentifier:"
+ "appSpecificSettingsManager:receivedSyncedClearForAppSpecificSettings:ofType:applicationIdentifier:modeIdentifier:"
+ "classification.classifyUserNotification"
+ "devicesChanged"
+ "executor:needsChoiceWithRequest:"
+ "initWithType:bundleIdentifier:url:"
+ "meDeviceChanged"
+ "received notification that 'Me Device' devices changed fetching Me Device"
+ "received notification that 'Me Device' status changed fetching Me Device"
+ "remoteServiceProviderResetAppConfigurationState:"
+ "resetAppConfigurationState"
+ "resetAppConfigurationStateWithRequestDetails:completionHandler:"
+ "v32@0:8@\"LNActionExecutor\"16@\"LNChoiceRequest\"24"
+ "v56@0:8@\"DNDSAppSpecificSettingsManager\"16@\"NSObject<DNDSAppSpecificSettings>\"24#32@\"DNDApplicationIdentifier\"40@\"NSString\"48"
+ "v56@0:8@16@24#32@40@48"
- "initWithType:bundleIdentifier:"

```
