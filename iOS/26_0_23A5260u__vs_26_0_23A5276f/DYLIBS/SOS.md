## SOS

> `/System/Library/PrivateFrameworks/SOS.framework/SOS`

```diff

-651.100.2.0.0
-  __TEXT.__text: 0x3739c
+652.100.2.0.0
+  __TEXT.__text: 0x373c0
   __TEXT.__auth_stubs: 0x890
   __TEXT.__objc_methlist: 0x38a4
   __TEXT.__const: 0x266

   __TEXT.__swift5_types: 0x4
   __TEXT.__unwind_info: 0xf90
   __TEXT.__objc_classname: 0x586
-  __TEXT.__objc_methname: 0xaa60
+  __TEXT.__objc_methname: 0xaa66
   __TEXT.__objc_methtype: 0x1acb
-  __TEXT.__objc_stubs: 0x7640
+  __TEXT.__objc_stubs: 0x7660
   __DATA_CONST.__got: 0x368
-  __DATA_CONST.__const: 0x1120
+  __DATA_CONST.__const: 0x1100
   __DATA_CONST.__objc_classlist: 0x118
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2700
+  __DATA_CONST.__objc_selrefs: 0x2708
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0xd8
   __DATA_CONST.__objc_arraydata: 0x100

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
-  UUID: 974E6B7F-805C-33CA-AA6C-9C99AA85D5A6
+  UUID: 4D2337BD-7736-37C0-9178-EF160ADAC9D8
   Functions: 1432
-  Symbols:   5053
-  CStrings:  3551
+  Symbols:   5046
+  CStrings:  3552
 
Symbols:
+ ___101+[SOSUtilities setKappaTriggersEmergencySOS:isWristDetectionEnabled:confirmationDelegate:completion:]_block_invoke.911
+ ___101+[SOSUtilities setKappaTriggersEmergencySOS:isWristDetectionEnabled:confirmationDelegate:completion:]_block_invoke.915
+ ___111+[SOSUtilities setKappaThirdPartyActive:forApp:forPairedDevice:presentConfirmationOnViewController:completion:]_block_invoke.1027
+ ___120+[SOSUtilities setNewtonTriggersEmergencySOS:isWristDetectionEnabled:newtonEligibility:confirmationDelegate:completion:]_block_invoke.606
+ ___120+[SOSUtilities setNewtonTriggersEmergencySOS:isWristDetectionEnabled:newtonEligibility:confirmationDelegate:completion:]_block_invoke.607
+ ___120+[SOSUtilities setNewtonTriggersEmergencySOS:isWristDetectionEnabled:newtonEligibility:confirmationDelegate:completion:]_block_invoke.608
+ ___132+[SOSUtilities setNewtonTriggersEmergencySOSWorkoutsOnly:isWristDetectionEnabled:newtonEligibility:confirmationDelegate:completion:]_block_invoke.609
+ ___18-[SOSManager init]_block_invoke.365
+ ___18-[SOSManager init]_block_invoke.369
+ ___24-[SOSManager connection]_block_invoke.375
+ ___24-[SOSManager connection]_block_invoke.376
+ ___38-[SOSEngine dismissSOSWithCompletion:]_block_invoke.376
+ ___40-[SOSManager _resetStateWithCompletion:]_block_invoke.386
+ ___42-[SOSContactsManager initWithHealthStore:]_block_invoke.329
+ ___48-[SOSEngine listener:shouldAcceptNewConnection:]_block_invoke.532
+ ___52+[SOSEngine shiftedLocationWithLocation:completion:]_block_invoke.402
+ ___55-[SOSContactsManager _fetchSafetyMonitorSessionHandles]_block_invoke.355
+ ___55-[SOSStatusManager listener:shouldAcceptNewConnection:]_block_invoke.310
+ ___56-[SOSCoordinator processEventWithUUID:triggerMechanism:]_block_invoke.346
+ ___77+[SOSUtilities setKappaTriggersEmergencySOS:confirmationDelegate:completion:]_block_invoke.922
+ ___87+[SOSEngine _sendMessageToRecipients:withLocation:isFirstMessage:medicalIDName:Reason:]_block_invoke.395
+ ___87+[SOSEngine _sendMessageToRecipients:withLocation:isFirstMessage:medicalIDName:Reason:]_block_invoke.395.cold.1
+ ___91+[SOSNewtonManager newtonEligibilityWithHealthStore:deviceSupportsWorkoutsOnly:completion:]_block_invoke.302
+ ___block_literal_global.1039
+ ___block_literal_global.1041
+ ___block_literal_global.1043
+ ___block_literal_global.1055
+ ___block_literal_global.340
+ ___block_literal_global.346
+ ___block_literal_global.367
+ ___block_literal_global.369
+ ___block_literal_global.371
+ ___block_literal_global.373
+ ___block_literal_global.379
+ ___block_literal_global.381
+ ___block_literal_global.384
+ ___block_literal_global.401
+ ___block_literal_global.493
+ ___block_literal_global.495
+ ___block_literal_global.517
+ ___block_literal_global.583
+ ___block_literal_global.611
+ ___block_literal_global.701
+ ___block_literal_global.711
+ ___block_literal_global.887
+ ___block_literal_global.894
+ ___block_literal_global.896
+ ___block_literal_global.924
+ _objc_msgSend$array
- ___101+[SOSUtilities setKappaTriggersEmergencySOS:isWristDetectionEnabled:confirmationDelegate:completion:]_block_invoke.908
- ___101+[SOSUtilities setKappaTriggersEmergencySOS:isWristDetectionEnabled:confirmationDelegate:completion:]_block_invoke.912
- ___111+[SOSUtilities setKappaThirdPartyActive:forApp:forPairedDevice:presentConfirmationOnViewController:completion:]_block_invoke.1024
- ___120+[SOSUtilities setNewtonTriggersEmergencySOS:isWristDetectionEnabled:newtonEligibility:confirmationDelegate:completion:]_block_invoke.603
- ___120+[SOSUtilities setNewtonTriggersEmergencySOS:isWristDetectionEnabled:newtonEligibility:confirmationDelegate:completion:]_block_invoke.604
- ___120+[SOSUtilities setNewtonTriggersEmergencySOS:isWristDetectionEnabled:newtonEligibility:confirmationDelegate:completion:]_block_invoke.605
- ___132+[SOSUtilities setNewtonTriggersEmergencySOSWorkoutsOnly:isWristDetectionEnabled:newtonEligibility:confirmationDelegate:completion:]_block_invoke.606
- ___18-[SOSManager init]_block_invoke.362
- ___18-[SOSManager init]_block_invoke.366
- ___24-[SOSManager connection]_block_invoke.372
- ___24-[SOSManager connection]_block_invoke.373
- ___38-[SOSEngine dismissSOSWithCompletion:]_block_invoke.367
- ___40-[SOSManager _resetStateWithCompletion:]_block_invoke.383
- ___42-[SOSContactsManager initWithHealthStore:]_block_invoke.326
- ___48-[SOSEngine listener:shouldAcceptNewConnection:]_block_invoke.523
- ___52+[SOSEngine shiftedLocationWithLocation:completion:]_block_invoke.393
- ___55-[SOSContactsManager _fetchSafetyMonitorSessionHandles]_block_invoke.352
- ___55-[SOSStatusManager listener:shouldAcceptNewConnection:]_block_invoke.307
- ___56-[SOSCoordinator processEventWithUUID:triggerMechanism:]_block_invoke.343
- ___77+[SOSUtilities setKappaTriggersEmergencySOS:confirmationDelegate:completion:]_block_invoke.919
- ___87+[SOSEngine _sendMessageToRecipients:withLocation:isFirstMessage:medicalIDName:Reason:]_block_invoke.386
- ___87+[SOSEngine _sendMessageToRecipients:withLocation:isFirstMessage:medicalIDName:Reason:]_block_invoke.386.cold.1
- ___91+[SOSNewtonManager newtonEligibilityWithHealthStore:deviceSupportsWorkoutsOnly:completion:]_block_invoke.299
- ___block_literal_global.1036
- ___block_literal_global.1038
- ___block_literal_global.1040
- ___block_literal_global.1052
- ___block_literal_global.337
- ___block_literal_global.343
- ___block_literal_global.360
- ___block_literal_global.362
- ___block_literal_global.364
- ___block_literal_global.366
- ___block_literal_global.370
- ___block_literal_global.372
- ___block_literal_global.383
- ___block_literal_global.484
- ___block_literal_global.486
- ___block_literal_global.508
- ___block_literal_global.580
- ___block_literal_global.608
- ___block_literal_global.698
- ___block_literal_global.708
- ___block_literal_global.884
- ___block_literal_global.891
- ___block_literal_global.893
- ___block_literal_global.921
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swiftDarwin_$_SOS
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_SOS
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_SOS
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_SOS
Functions:
~ -[SOSEmergencyCallVoiceLoopManager stopConfirmationUtterancesForPlaybackState:remoteVariant:verbalizedActionOut:] : 648 -> 684
CStrings:
+ "array"

```
