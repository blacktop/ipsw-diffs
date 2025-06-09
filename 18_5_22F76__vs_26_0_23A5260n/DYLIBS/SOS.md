## SOS

> `/System/Library/PrivateFrameworks/SOS.framework/SOS`

```diff

-630.500.161.0.0
-  __TEXT.__text: 0x36840
-  __TEXT.__auth_stubs: 0x870
-  __TEXT.__objc_methlist: 0x3800
-  __TEXT.__const: 0x238
-  __TEXT.__cstring: 0x4842
-  __TEXT.__oslogstring: 0x6057
+651.100.2.0.0
+  __TEXT.__text: 0x3739c
+  __TEXT.__auth_stubs: 0x890
+  __TEXT.__objc_methlist: 0x38a4
+  __TEXT.__const: 0x266
+  __TEXT.__cstring: 0x4ac2
+  __TEXT.__oslogstring: 0x6288
   __TEXT.__gcc_except_tab: 0x90c
   __TEXT.__dlopen_cstrs: 0x39f
-  __TEXT.__unwind_info: 0xf40
-  __TEXT.__objc_classname: 0x551
-  __TEXT.__objc_methname: 0xa851
-  __TEXT.__objc_methtype: 0x1a9d
-  __TEXT.__objc_stubs: 0x74c0
-  __DATA_CONST.__got: 0x380
-  __DATA_CONST.__const: 0x10d0
-  __DATA_CONST.__objc_classlist: 0x110
+  __TEXT.__swift5_typeref: 0x3a
+  __TEXT.__swift5_fieldmd: 0x20
+  __TEXT.__constg_swiftt: 0x50
+  __TEXT.__swift5_types: 0x4
+  __TEXT.__unwind_info: 0xf90
+  __TEXT.__objc_classname: 0x586
+  __TEXT.__objc_methname: 0xaa60
+  __TEXT.__objc_methtype: 0x1acb
+  __TEXT.__objc_stubs: 0x7640
+  __DATA_CONST.__got: 0x368
+  __DATA_CONST.__const: 0x1120
+  __DATA_CONST.__objc_classlist: 0x118
   __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0xc8
+  __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2678
-  __DATA_CONST.__objc_protorefs: 0x20
+  __DATA_CONST.__objc_selrefs: 0x2700
+  __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0xd8
   __DATA_CONST.__objc_arraydata: 0x100
-  __AUTH_CONST.__auth_got: 0x448
+  __AUTH_CONST.__auth_got: 0x458
   __AUTH_CONST.__const: 0x640
-  __AUTH_CONST.__cfstring: 0x4100
-  __AUTH_CONST.__objc_const: 0x4a18
+  __AUTH_CONST.__cfstring: 0x4160
+  __AUTH_CONST.__objc_const: 0x4b78
   __AUTH_CONST.__objc_intobj: 0x270
   __AUTH_CONST.__objc_arrayobj: 0x120
   __AUTH_CONST.__objc_floatobj: 0x10
-  __AUTH.__objc_data: 0x1e0
+  __AUTH.__objc_data: 0x5f0
+  __AUTH.__data: 0x98
   __DATA.__objc_ivar: 0x2f0
-  __DATA.__data: 0x990
+  __DATA.__data: 0x9f0
   __DATA.__bss: 0x250
-  __DATA_DIRTY.__objc_data: 0x8c0
+  __DATA_DIRTY.__objc_data: 0x4b0
   __DATA_DIRTY.__data: 0x1
   __DATA_DIRTY.__bss: 0xe8
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/CoreTelephony.framework/CoreTelephony
+  - /System/Library/Frameworks/DeveloperToolsSupport.framework/DeveloperToolsSupport
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/HealthKit.framework/HealthKit
   - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
   - /System/Library/Frameworks/Security.framework/Security
+  - /System/Library/Frameworks/_LocationEssentials.framework/_LocationEssentials
   - /System/Library/PrivateFrameworks/AccessibilityUtilities.framework/AccessibilityUtilities
   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
   - /System/Library/PrivateFrameworks/AssertionServices.framework/AssertionServices

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B0CD8F48-6F4D-3462-A7B6-2CC31DE78B25
-  Functions: 1417
-  Symbols:   4995
-  CStrings:  3506
+  - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftDarwin.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
+  UUID: 974E6B7F-805C-33CA-AA6C-9C99AA85D5A6
+  Functions: 1432
+  Symbols:   5053
+  CStrings:  3551
 
Symbols:
+ +[SOSUtilities deviceHasDynamicIsland]
+ +[SOSUtilities deviceHasDynamicIsland].cold.1
+ +[SOSUtilities isMessagesHandlingSMS]
+ +[SOSUtilities isSOSLiveActivityEnabled]
+ +[SOSUtilities sosLocationSharingLiveActivityAlertBody]
+ +[SOSUtilities sosLocationSharingLiveActivityAlertTitle]
+ +[SOSUtilities sosLocationSharingLiveActivityDetail]
+ -[SOSStatusManager _cancelCurrentDeviceClearStatusTimer]
+ -[SOSStatusManager _cancelHandoffFallbackTimer]
+ -[SOSStatusManager _cancelPairedDeviceClearStatusTimer]
+ -[SOSStatusManager _startCurrentDeviceClearStatusTimer]
+ -[SOSStatusManager _startHandoffFallbackTimer]
+ -[SOSStatusManager _startPairedDeviceClearStatusTimer]
+ -[SOSStatusManager startAudioSessionForFlowOnCurrentDevice:]
+ -[SOSStatusManager startAudioSessionForFlowOnCurrentDevice:].cold.1
+ -[SOSStatusManager startAudioSessionForFlowOnCurrentDevice:].cold.2
+ GCC_except_table12
+ GCC_except_table29
+ GCC_except_table47
+ _OBJC_CLASS_$_LSApplicationRecord
+ _OBJC_CLASS_$__TtCs12_SwiftObject
+ _OBJC_METACLASS_$__TtCs12_SwiftObject
+ __DATA__TtC3SOSP33_0B53F8EEBFBA16E9E89EF4365C2A4E0319ResourceBundleClass
+ __METACLASS_DATA__TtC3SOSP33_0B53F8EEBFBA16E9E89EF4365C2A4E0319ResourceBundleClass
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__TtP3SOS41SOSLocationSharingActivityManagerDelegate_
+ __OBJC_$_PROTOCOL_METHOD_TYPES__TtP3SOS41SOSLocationSharingActivityManagerDelegate_
+ __OBJC_LABEL_PROTOCOL_$__TtP3SOS41SOSLocationSharingActivityManagerDelegate_
+ __OBJC_PROTOCOL_$__TtP3SOS41SOSLocationSharingActivityManagerDelegate_
+ __PROTOCOL_INSTANCE_METHODS__TtP3SOS41SOSLocationSharingActivityManagerDelegate_
+ __PROTOCOL_METHOD_TYPES__TtP3SOS41SOSLocationSharingActivityManagerDelegate_
+ __PROTOCOL__TtP3SOS41SOSLocationSharingActivityManagerDelegate_
+ ___101+[SOSUtilities setKappaTriggersEmergencySOS:isWristDetectionEnabled:confirmationDelegate:completion:]_block_invoke.908
+ ___101+[SOSUtilities setKappaTriggersEmergencySOS:isWristDetectionEnabled:confirmationDelegate:completion:]_block_invoke.912
+ ___111+[SOSUtilities setKappaThirdPartyActive:forApp:forPairedDevice:presentConfirmationOnViewController:completion:]_block_invoke.1024
+ ___120+[SOSUtilities setNewtonTriggersEmergencySOS:isWristDetectionEnabled:newtonEligibility:confirmationDelegate:completion:]_block_invoke.603
+ ___120+[SOSUtilities setNewtonTriggersEmergencySOS:isWristDetectionEnabled:newtonEligibility:confirmationDelegate:completion:]_block_invoke.604
+ ___120+[SOSUtilities setNewtonTriggersEmergencySOS:isWristDetectionEnabled:newtonEligibility:confirmationDelegate:completion:]_block_invoke.605
+ ___132+[SOSUtilities setNewtonTriggersEmergencySOSWorkoutsOnly:isWristDetectionEnabled:newtonEligibility:confirmationDelegate:completion:]_block_invoke.606
+ ___18-[SOSManager init]_block_invoke.362
+ ___18-[SOSManager init]_block_invoke.366
+ ___24-[SOSManager connection]_block_invoke.372
+ ___24-[SOSManager connection]_block_invoke.373
+ ___38+[SOSUtilities deviceHasDynamicIsland]_block_invoke
+ ___38-[SOSEngine dismissSOSWithCompletion:]_block_invoke.367
+ ___40-[SOSManager _resetStateWithCompletion:]_block_invoke.383
+ ___40-[SOSStatusManager checkHandoffFallback]_block_invoke
+ ___42-[SOSContactsManager initWithHealthStore:]_block_invoke.326
+ ___46-[SOSStatusManager _startHandoffFallbackTimer]_block_invoke
+ ___46-[SOSStatusManager _startHandoffFallbackTimer]_block_invoke.cold.1
+ ___46-[SOSStatusManager cancelHandoffFallbackTimer]_block_invoke
+ ___48-[SOSEngine listener:shouldAcceptNewConnection:]_block_invoke.523
+ ___52+[SOSEngine shiftedLocationWithLocation:completion:]_block_invoke.393
+ ___54-[SOSStatusManager _startPairedDeviceClearStatusTimer]_block_invoke
+ ___54-[SOSStatusManager _startPairedDeviceClearStatusTimer]_block_invoke.cold.1
+ ___54-[SOSStatusManager cancelPairedDeviceClearStatusTimer]_block_invoke
+ ___55-[SOSContactsManager _fetchSafetyMonitorSessionHandles]_block_invoke.352
+ ___55-[SOSStatusManager _startCurrentDeviceClearStatusTimer]_block_invoke
+ ___55-[SOSStatusManager _startCurrentDeviceClearStatusTimer]_block_invoke.cold.1
+ ___55-[SOSStatusManager cancelCurrentDeviceClearStatusTimer]_block_invoke
+ ___56-[SOSCoordinator processEventWithUUID:triggerMechanism:]_block_invoke.343
+ ___77+[SOSUtilities setKappaTriggersEmergencySOS:confirmationDelegate:completion:]_block_invoke.919
+ ___79-[SOSEmergencyCallVoiceLoopManager shiftedLocationIfApplicable:withcompletion:]_block_invoke.114
+ ___87+[SOSEngine _sendMessageToRecipients:withLocation:isFirstMessage:medicalIDName:Reason:]_block_invoke.386
+ ___87+[SOSEngine _sendMessageToRecipients:withLocation:isFirstMessage:medicalIDName:Reason:]_block_invoke.386.cold.1
+ ___91+[SOSNewtonManager newtonEligibilityWithHealthStore:deviceSupportsWorkoutsOnly:completion:]_block_invoke.299
+ ___block_literal_global.1036
+ ___block_literal_global.1038
+ ___block_literal_global.1040
+ ___block_literal_global.1052
+ ___block_literal_global.337
+ ___block_literal_global.360
+ ___block_literal_global.364
+ ___block_literal_global.366
+ ___block_literal_global.370
+ ___block_literal_global.372
+ ___block_literal_global.375
+ ___block_literal_global.383
+ ___block_literal_global.392
+ ___block_literal_global.484
+ ___block_literal_global.486
+ ___block_literal_global.508
+ ___block_literal_global.580
+ ___block_literal_global.608
+ ___block_literal_global.698
+ ___block_literal_global.708
+ ___block_literal_global.884
+ ___block_literal_global.891
+ ___block_literal_global.893
+ ___block_literal_global.921
+ ___swift_reflection_version
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftCoreFoundation_$_SOS
+ __swift_FORCE_LOAD_$_swiftDarwin
+ __swift_FORCE_LOAD_$_swiftDarwin_$_SOS
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftDispatch_$_SOS
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftFoundation_$_SOS
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftObjectiveC_$_SOS
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swiftXPC_$_SOS
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_Builtin_float_$_SOS
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_SOS
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_SOS
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_SOS
+ _deviceHasDynamicIsland.__supportsDynamicIsland
+ _deviceHasDynamicIsland.onceToken
+ _objc_msgSend$_cancelCurrentDeviceClearStatusTimer
+ _objc_msgSend$_cancelHandoffFallbackTimer
+ _objc_msgSend$_cancelPairedDeviceClearStatusTimer
+ _objc_msgSend$_setError
+ _objc_msgSend$_startCurrentDeviceClearStatusTimer
+ _objc_msgSend$_startHandoffFallbackTimer
+ _objc_msgSend$_startPairedDeviceClearStatusTimer
+ _objc_msgSend$canChangeDefaultAppForCategory:
+ _objc_msgSend$defaultApplicationForCategory:error:
+ _objc_msgSend$deviceHasDynamicIsland
+ _objc_msgSend$getBytes:range:
+ _objc_msgSend$hasError
+ _objc_msgSend$initWithBundleIdentifier:allowPlaceholder:error:
+ _objc_msgSend$isMessagesHandlingSMS
+ _objc_msgSend$position
+ _objc_msgSend$setPosition:
+ _objc_msgSend$startAudioSessionForFlowOnCurrentDevice:
+ _objc_opt_self
+ _swift_deallocClassInstance
+ _swift_deletedMethodError
+ _symbolic $s3SOS41SOSLocationSharingActivityManagerDelegateP
+ _symbolic _____ 3SOS19ResourceBundleClass33_0B53F8EEBFBA16E9E89EF4365C2A4E03LLC
- +[SOSUtilities deviceHasSlot]
- +[SOSUtilities deviceHasSlot].cold.1
- -[SOSStatusManager flowStartedOnCurrentDevice]
- -[SOSStatusManager flowStartedOnEitherDevice]
- -[SOSStatusManager startAudioSession]
- -[SOSStatusManager startAudioSession].cold.1
- -[SOSStatusManager startAudioSession].cold.2
- GCC_except_table27
- GCC_except_table41
- OBJC_IVAR_$_PBDataReader._bytes
- OBJC_IVAR_$_PBDataReader._error
- OBJC_IVAR_$_PBDataReader._length
- OBJC_IVAR_$_PBDataReader._pos
- ___101+[SOSUtilities setKappaTriggersEmergencySOS:isWristDetectionEnabled:confirmationDelegate:completion:]_block_invoke.905
- ___101+[SOSUtilities setKappaTriggersEmergencySOS:isWristDetectionEnabled:confirmationDelegate:completion:]_block_invoke.909
- ___111+[SOSUtilities setKappaThirdPartyActive:forApp:forPairedDevice:presentConfirmationOnViewController:completion:]_block_invoke.1021
- ___120+[SOSUtilities setNewtonTriggersEmergencySOS:isWristDetectionEnabled:newtonEligibility:confirmationDelegate:completion:]_block_invoke.600
- ___120+[SOSUtilities setNewtonTriggersEmergencySOS:isWristDetectionEnabled:newtonEligibility:confirmationDelegate:completion:]_block_invoke.601
- ___120+[SOSUtilities setNewtonTriggersEmergencySOS:isWristDetectionEnabled:newtonEligibility:confirmationDelegate:completion:]_block_invoke.602
- ___132+[SOSUtilities setNewtonTriggersEmergencySOSWorkoutsOnly:isWristDetectionEnabled:newtonEligibility:confirmationDelegate:completion:]_block_invoke.603
- ___18-[SOSManager init]_block_invoke.359
- ___18-[SOSManager init]_block_invoke.363
- ___24-[SOSManager connection]_block_invoke.369
- ___24-[SOSManager connection]_block_invoke.370
- ___29+[SOSUtilities deviceHasSlot]_block_invoke
- ___38-[SOSEngine dismissSOSWithCompletion:]_block_invoke.346
- ___40-[SOSManager _resetStateWithCompletion:]_block_invoke.380
- ___42-[SOSContactsManager initWithHealthStore:]_block_invoke.323
- ___45-[SOSStatusManager startHandoffFallbackTimer]_block_invoke.306
- ___45-[SOSStatusManager startHandoffFallbackTimer]_block_invoke.306.cold.1
- ___48-[SOSEngine listener:shouldAcceptNewConnection:]_block_invoke.502
- ___52+[SOSEngine shiftedLocationWithLocation:completion:]_block_invoke.372
- ___53-[SOSStatusManager startPairedDeviceClearStatusTimer]_block_invoke.305
- ___53-[SOSStatusManager startPairedDeviceClearStatusTimer]_block_invoke.305.cold.1
- ___54-[SOSStatusManager startCurrentDeviceClearStatusTimer]_block_invoke.299
- ___54-[SOSStatusManager startCurrentDeviceClearStatusTimer]_block_invoke.299.cold.1
- ___55-[SOSContactsManager _fetchSafetyMonitorSessionHandles]_block_invoke.349
- ___56-[SOSCoordinator processEventWithUUID:triggerMechanism:]_block_invoke.340
- ___77+[SOSUtilities setKappaTriggersEmergencySOS:confirmationDelegate:completion:]_block_invoke.916
- ___79-[SOSEmergencyCallVoiceLoopManager shiftedLocationIfApplicable:withcompletion:]_block_invoke.96
- ___87+[SOSEngine _sendMessageToRecipients:withLocation:isFirstMessage:medicalIDName:Reason:]_block_invoke.365
- ___87+[SOSEngine _sendMessageToRecipients:withLocation:isFirstMessage:medicalIDName:Reason:]_block_invoke.365.cold.1
- ___91+[SOSNewtonManager newtonEligibilityWithHealthStore:deviceSupportsWorkoutsOnly:completion:]_block_invoke.296
- ___block_literal_global.1033
- ___block_literal_global.1037
- ___block_literal_global.1039
- ___block_literal_global.1041
- ___block_literal_global.334
- ___block_literal_global.339
- ___block_literal_global.340
- ___block_literal_global.341
- ___block_literal_global.345
- ___block_literal_global.349
- ___block_literal_global.351
- ___block_literal_global.354
- ___block_literal_global.361
- ___block_literal_global.371
- ___block_literal_global.463
- ___block_literal_global.465
- ___block_literal_global.487
- ___block_literal_global.577
- ___block_literal_global.605
- ___block_literal_global.695
- ___block_literal_global.705
- ___block_literal_global.881
- ___block_literal_global.888
- ___block_literal_global.890
- ___block_literal_global.918
- _deviceHasSlot.__supportsDynamicIsland
- _deviceHasSlot.onceToken
- _objc_msgSend$deviceHasSlot
- _objc_msgSend$flowStartedOnCurrentDevice
- _objc_msgSend$flowStartedOnEitherDevice
- _objc_msgSend$initWithIdentifier:
- _objc_msgSend$startAudioSession
CStrings:
+ "%s - %d"
+ "%s - Can't change default app so behaving as if Messages is the default"
+ "%s - Can't find application record for Messages, error %@"
+ "%s - FF is off"
+ "%s - Stopping timer, emergency contact notification no longer enabled"
+ "%s - assuming YES"
+ "+[SOSUtilities isMessagesHandlingSMS]"
+ "-[SOSManager isSendingLocationUpdate]"
+ "-[SOSManager mostRecentLocationSentWithCompletion:]"
+ "-[SOSManager startSendingLocationUpdateForReason:withCompletion:]"
+ "-[SOSManager startSendingLocationUpdateWithCompletion:]"
+ "-[SOSManager stopSendingLocationUpdate]"
+ "-[SOSManager willStartSendingLocationUpdate]"
+ "Messages app is not handling SMS, cannot message emergency contacts"
+ "MessagingAPI"
+ "SOSLocationSharingLiveActivity_Phone"
+ "SOSStatusManager,checkHandoffFallback,handoff flow ended"
+ "SOSStatusManager,checkHandoffFallback,handoff flow is active"
+ "SOSStatusManager,checkHandoffFallback,handoff flow not running"
+ "SOSStatusManager,checkHandoffFallback,handoff flow not yet active"
+ "SOSStatusManager,checkHandoffFallback,handoff flow progressed to call"
+ "SOSStatusManager,checkHandoffFallback,no handoff trigger UUID"
+ "SOS_LOCATION_SHARING_LIVE_ACTIVITY_ALERT_BODY"
+ "SOS_LOCATION_SHARING_LIVE_ACTIVITY_ALERT_TITLE"
+ "SOS_LOCATION_SHARING_LIVE_ACTIVITY_DETAIL"
+ "_TtC3SOSP33_0B53F8EEBFBA16E9E89EF4365C2A4E0319ResourceBundleClass"
+ "_TtP3SOS41SOSLocationSharingActivityManagerDelegate_"
+ "_cancelCurrentDeviceClearStatusTimer"
+ "_cancelHandoffFallbackTimer"
+ "_cancelPairedDeviceClearStatusTimer"
+ "_setError"
+ "_startCurrentDeviceClearStatusTimer"
+ "_startHandoffFallbackTimer"
+ "_startPairedDeviceClearStatusTimer"
+ "callCenter:receivedCaptions:"
+ "canChangeDefaultAppForCategory:"
+ "defaultApplicationForCategory:error:"
+ "deviceHasDynamicIsland"
+ "getBytes:range:"
+ "hasError"
+ "initWithBundleIdentifier:allowPlaceholder:error:"
+ "isMessagesHandlingSMS"
+ "isSOSLiveActivityEnabled"
+ "position"
+ "setPosition:"
+ "sosLocationSharingLiveActivityAlertBody"
+ "sosLocationSharingLiveActivityAlertTitle"
+ "sosLocationSharingLiveActivityDetail"
+ "startAudioSessionForFlowOnCurrentDevice:"
+ "v32@0:8@\"TUCallCenter\"16@\"TUCaptionsResult\"24"
- "Messages"
- "SOSStatusManager,handoff flow ended"
- "SOSStatusManager,handoff flow not running"
- "SOSStatusManager,handoff flow progressed to call"
- "deviceHasSlot"
- "flowStartedOnCurrentDevice"
- "flowStartedOnEitherDevice"
- "initWithIdentifier:"
- "sos_alerting"
- "startAudioSession"

```
