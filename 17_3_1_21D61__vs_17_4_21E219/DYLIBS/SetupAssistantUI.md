## SetupAssistantUI

> `/System/Library/PrivateFrameworks/SetupAssistantUI.framework/SetupAssistantUI`

```diff

-5076.0.0.0.0
-  __TEXT.__text: 0x1f39c
-  __TEXT.__auth_stubs: 0xa10
+5116.0.0.0.0
+  __TEXT.__text: 0x1f9b4
+  __TEXT.__auth_stubs: 0xa80
   __TEXT.__objc_methlist: 0x2174
   __TEXT.__const: 0x1e6
-  __TEXT.__cstring: 0xd70
-  __TEXT.__oslogstring: 0xd4c
+  __TEXT.__cstring: 0xfc0
+  __TEXT.__oslogstring: 0xd99
   __TEXT.__gcc_except_tab: 0x1c0
   __TEXT.__dlopen_cstrs: 0x30d
   __TEXT.__swift5_typeref: 0xae

   __TEXT.__swift5_reflstr: 0x53
   __TEXT.__swift5_fieldmd: 0x44
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x92c
+  __TEXT.__unwind_info: 0x938
   __TEXT.__objc_classname: 0x7dc
-  __TEXT.__objc_methname: 0x8103
+  __TEXT.__objc_methname: 0x8175
   __TEXT.__objc_methtype: 0x29f8
-  __TEXT.__objc_stubs: 0x5540
+  __TEXT.__objc_stubs: 0x5500
   __DATA_CONST.__got: 0x170
-  __DATA_CONST.__const: 0x630
+  __DATA_CONST.__const: 0x650
   __DATA_CONST.__objc_classlist: 0x168
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x118
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x5ec0
-  __DATA_CONST.__objc_selrefs: 0x1ac0
+  __DATA_CONST.__objc_selrefs: 0x1ab0
+  __DATA_CONST.__objc_protorefs: 0x28
+  __DATA_CONST.__objc_classrefs: 0x340
+  __DATA_CONST.__objc_superrefs: 0x108
   __AUTH_CONST.__objc_const: 0x1120
   __AUTH_CONST.__objc_intobj: 0x60
-  __AUTH_CONST.__cfstring: 0x780
+  __AUTH_CONST.__cfstring: 0x760
   __AUTH_CONST.__const: 0xa0
-  __AUTH_CONST.__auth_got: 0x518
+  __AUTH_CONST.__auth_got: 0x550
   __AUTH.__objc_data: 0xd98
   __AUTH.__data: 0xc0
-  __DATA.__objc_protorefs: 0x28
-  __DATA.__objc_classrefs: 0x348
-  __DATA.__objc_superrefs: 0x108
   __DATA.__objc_ivar: 0x284
-  __DATA.__data: 0xd00
+  __DATA.__data: 0xcf0
   __DATA.__bss: 0x130
   __DATA.__common: 0x30
   __DATA_DIRTY.__objc_data: 0xa0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib

   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 8C24306B-06DA-3C75-936F-DC36414D6B13
-  Functions: 846
-  Symbols:   3333
-  CStrings:  2046
+  - /usr/lib/swift/libswiftsimd.dylib
+  UUID: EDDBD641-5B01-3441-B61B-434DD12AAE75
+  Functions: 849
+  Symbols:   3342
+  CStrings:  2060
 
Symbols:
+ +[BFFViewControllerSpinnerManager startAnimatingSpinnerFor:identifier:].cold.2
+ _OUTLINED_FUNCTION_1
+ __swift_FORCE_LOAD_$_swiftAccelerate
+ __swift_FORCE_LOAD_$_swiftAccelerate_$_SetupAssistantUI
+ __swift_FORCE_LOAD_$_swiftsimd
+ __swift_FORCE_LOAD_$_swiftsimd_$_SetupAssistantUI
+ _objc_retain_x25
+ _objc_retain_x26
+ _objc_retain_x27
+ _objc_retain_x28
- _OBJC_CLASS_$_CLLocationManager
- _objc_msgSend$bundleWithPath:
- _objc_msgSend$setAuthorizationStatusByType:forBundle:
CStrings:
+ "Fatal error"
+ "Insufficient space allocated to copy string contents"
+ "Swift/ContiguousArrayBuffer.swift"
+ "Swift/StringTesting.swift"
+ "Swift/StringUTF8View.swift"
+ "Swift/UnsafeBufferPointer.swift"
+ "Swift/UnsafePointer.swift"
+ "Swift/UnsafeRawPointer.swift"
+ "T@\"<BYCapabilities>\",?,&,N"
+ "T@\"<BYDeviceConfiguration>\",?,&,N"
+ "T@\"<BYDeviceProvider>\",?,&,N"
+ "T@\"<BYRunState>\",?,&,N"
+ "T@\"<BuddyCombinedTermsProvider>\",?,&,N"
+ "T@\"<BuddyEmergencyExecutor>\",?,&,N"
+ "T@\"<BuddyFeatureFlags>\",?,&,N"
+ "T@\"<BuddyNetworkProvider>\",?,&,N"
+ "T@\"<LockdownModeProvider>\",?,&,N"
+ "T@\"AppearanceModeProvider\",?,&,N"
+ "T@\"BFFBackupDeviceController\",?,&,N"
+ "T@\"BFFSettingsManager\",?,&,N"
+ "T@\"BYAnalyticsEventAppearance\",?,&,N"
+ "T@\"BYAnalyticsManager\",?,&,N"
+ "T@\"BYChronicle\",?,&,N"
+ "T@\"BYFlowSkipController\",?,&,N"
+ "T@\"BYPaneFeatureAnalyticsManager\",?,&,N"
+ "T@\"BYPreferencesController\",?,&,N"
+ "T@\"BYSeedProgramManager\",?,&,N"
+ "T@\"BYSoftwareUpdateCache\",?,&,N"
+ "T@\"BuddyActivationRecord\",?,&,N"
+ "T@\"BuddyActivationState\",?,&,N"
+ "T@\"BuddyBetaEnrollmentStateManager\",?,&,N"
+ "T@\"BuddyButtonMonitor\",?,&,N"
+ "T@\"BuddyChildSetupPresenter\",?,&,N"
+ "T@\"BuddyDisplayZoomExecutor\",?,&,N"
+ "T@\"BuddyEnrollmentCoordinator\",?,&,N"
+ "T@\"BuddyExistingSettings\",?,&,N"
+ "T@\"BuddyFlowItemDispositionProvider\",?,&,N"
+ "T@\"BuddyMiscState\",?,&,N"
+ "T@\"BuddyPasscodeCacheManager\",?,&,N"
+ "T@\"BuddyPendingRestoreState\",?,&,N"
+ "T@\"BuddyProximityAutomatedDeviceEnrollmentController\",?,&,N"
+ "T@\"BuddySetupMethod\",?,&,N"
+ "T@\"BuddySuspendTask\",?,&,N"
+ "T@\"BuddySystemTimeUpdateManager\",?,&,N"
+ "T@\"DMCReturnToServiceController\",?,&,N"
+ "T@\"MCProfileConnection\",?,&,N"
+ "T@\"NSString\",?,R,C"
+ "T@\"ProximitySetupController\",?,&,N"
+ "T@\"SetupUserDispositionProvider\",?,&,N"
+ "T@?,?,C,N"
+ "Unexpectedly found nil while unwrapping an Optional value"
+ "UnsafeMutableBufferPointer with negative count"
+ "UnsafeMutablePointer.initialize overlapping range"
+ "UnsafeMutablePointer.moveInitialize with negative count"
+ "UnsafeMutableRawPointer.initializeMemory overlapping range"
+ "invalid Collection: less than 'count' elements in collection"
+ "startAnimatingSpinnerFor called with nil view controller for identifier: %@."
- "/System/Library/PrivateFrameworks/AssistantServices.framework"
- "T@\"<BYCapabilities>\",&,N"
- "T@\"<BYDeviceConfiguration>\",&,N"
- "T@\"<BYDeviceProvider>\",&,N"
- "T@\"<BYRunState>\",&,N"
- "T@\"<BuddyCombinedTermsProvider>\",&,N"
- "T@\"<BuddyEmergencyExecutor>\",&,N"
- "T@\"<BuddyFeatureFlags>\",&,N"
- "T@\"<BuddyNetworkProvider>\",&,N"
- "T@\"<LockdownModeProvider>\",&,N"
- "T@\"AppearanceModeProvider\",&,N"
- "T@\"BFFBackupDeviceController\",&,N"
- "T@\"BFFSettingsManager\",&,N"
- "T@\"BYAnalyticsEventAppearance\",&,N"
- "T@\"BYAnalyticsManager\",&,N"
- "T@\"BYChronicle\",&,N"
- "T@\"BYPreferencesController\",&,N"
- "T@\"BYSeedProgramManager\",&,N"
- "T@\"BYSoftwareUpdateCache\",&,N"
- "T@\"BuddyActivationRecord\",&,N"
- "T@\"BuddyActivationState\",&,N"
- "T@\"BuddyBetaEnrollmentStateManager\",&,N"
- "T@\"BuddyButtonMonitor\",&,N"
- "T@\"BuddyChildSetupPresenter\",&,N"
- "T@\"BuddyDisplayZoomExecutor\",&,N"
- "T@\"BuddyEnrollmentCoordinator\",&,N"
- "T@\"BuddyExistingSettings\",&,N"
- "T@\"BuddyFlowItemDispositionProvider\",&,N"
- "T@\"BuddyMiscState\",&,N"
- "T@\"BuddyPasscodeCacheManager\",&,N"
- "T@\"BuddyPendingRestoreState\",&,N"
- "T@\"BuddyProximityAutomatedDeviceEnrollmentController\",&,N"
- "T@\"BuddySetupMethod\",&,N"
- "T@\"BuddySuspendTask\",&,N"
- "T@\"BuddySystemTimeUpdateManager\",&,N"
- "T@\"DMCReturnToServiceController\",&,N"
- "T@\"MCProfileConnection\",&,N"
- "T@\"ProximitySetupController\",&,N"
- "T@\"SetupUserDispositionProvider\",&,N"
- "T@?,C,N"
- "bundleWithPath:"
- "setAuthorizationStatusByType:forBundle:"

```
