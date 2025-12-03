## SOS

> `/System/Library/PrivateFrameworks/SOS.framework/SOS`

```diff

 656.300.1.0.0
   __TEXT.__text: 0x3738c
   __TEXT.__auth_stubs: 0x890
-  __TEXT.__objc_methlist: 0x38ac
+  __TEXT.__objc_methlist: 0x38cc
   __TEXT.__const: 0x266
   __TEXT.__cstring: 0x4a22
   __TEXT.__oslogstring: 0x62e9

   __TEXT.__swift5_types: 0x4
   __TEXT.__unwind_info: 0xfa8
   __TEXT.__objc_classname: 0x586
-  __TEXT.__objc_methname: 0xaaa7
-  __TEXT.__objc_methtype: 0x1b22
+  __TEXT.__objc_methname: 0xab06
+  __TEXT.__objc_methtype: 0x1b7a
   __TEXT.__objc_stubs: 0x7660
   __DATA_CONST.__got: 0x370
   __DATA_CONST.__const: 0x1100

   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2710
+  __DATA_CONST.__objc_selrefs: 0x2720
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0xd8
   __DATA_CONST.__objc_arraydata: 0x100
   __AUTH_CONST.__auth_got: 0x458
   __AUTH_CONST.__const: 0x640
   __AUTH_CONST.__cfstring: 0x40e0
-  __AUTH_CONST.__objc_const: 0x4b80
+  __AUTH_CONST.__objc_const: 0x4b90
   __AUTH_CONST.__objc_intobj: 0x270
   __AUTH_CONST.__objc_arrayobj: 0x120
   __AUTH_CONST.__objc_floatobj: 0x10

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  UUID: 12DD6698-E53C-3032-9E18-D27A99E41A53
+  UUID: C1A3FC39-ACAB-360F-85A7-20FD9800E0F8
   Functions: 1432
   Symbols:   5047
-  CStrings:  3547
+  CStrings:  3551
 
Symbols:
+ ___101+[SOSUtilities setKappaTriggersEmergencySOS:isWristDetectionEnabled:confirmationDelegate:completion:]_block_invoke.913
+ ___101+[SOSUtilities setKappaTriggersEmergencySOS:isWristDetectionEnabled:confirmationDelegate:completion:]_block_invoke.917
+ ___111+[SOSUtilities setKappaThirdPartyActive:forApp:forPairedDevice:presentConfirmationOnViewController:completion:]_block_invoke.1027
+ ___120+[SOSUtilities setNewtonTriggersEmergencySOS:isWristDetectionEnabled:newtonEligibility:confirmationDelegate:completion:]_block_invoke.615
+ ___120+[SOSUtilities setNewtonTriggersEmergencySOS:isWristDetectionEnabled:newtonEligibility:confirmationDelegate:completion:]_block_invoke.616
+ ___120+[SOSUtilities setNewtonTriggersEmergencySOS:isWristDetectionEnabled:newtonEligibility:confirmationDelegate:completion:]_block_invoke.617
+ ___132+[SOSUtilities setNewtonTriggersEmergencySOSWorkoutsOnly:isWristDetectionEnabled:newtonEligibility:confirmationDelegate:completion:]_block_invoke.618
+ ___18-[SOSManager init]_block_invoke.374
+ ___18-[SOSManager init]_block_invoke.378
+ ___24-[SOSManager connection]_block_invoke.384
+ ___24-[SOSManager connection]_block_invoke.385
+ ___38-[SOSEngine dismissSOSWithCompletion:]_block_invoke.387
+ ___40-[SOSManager _resetStateWithCompletion:]_block_invoke.395
+ ___42-[SOSContactsManager initWithHealthStore:]_block_invoke.338
+ ___48-[SOSEngine listener:shouldAcceptNewConnection:]_block_invoke.543
+ ___52+[SOSEngine shiftedLocationWithLocation:completion:]_block_invoke.413
+ ___55-[SOSContactsManager _fetchSafetyMonitorSessionHandles]_block_invoke.364
+ ___55-[SOSStatusManager listener:shouldAcceptNewConnection:]_block_invoke.319
+ ___56-[SOSCoordinator processEventWithUUID:triggerMechanism:]_block_invoke.355
+ ___77+[SOSUtilities setKappaTriggersEmergencySOS:confirmationDelegate:completion:]_block_invoke.924
+ ___87+[SOSEngine _sendMessageToRecipients:withLocation:isFirstMessage:medicalIDName:Reason:]_block_invoke.406
+ ___87+[SOSEngine _sendMessageToRecipients:withLocation:isFirstMessage:medicalIDName:Reason:]_block_invoke.406.cold.1
+ ___91+[SOSNewtonManager newtonEligibilityWithHealthStore:deviceSupportsWorkoutsOnly:completion:]_block_invoke.311
+ ___block_literal_global.1036
+ ___block_literal_global.1038
+ ___block_literal_global.1040
+ ___block_literal_global.1052
+ ___block_literal_global.349
+ ___block_literal_global.355
+ ___block_literal_global.376
+ ___block_literal_global.378
+ ___block_literal_global.380
+ ___block_literal_global.382
+ ___block_literal_global.390
+ ___block_literal_global.392
+ ___block_literal_global.395
+ ___block_literal_global.412
+ ___block_literal_global.504
+ ___block_literal_global.506
+ ___block_literal_global.528
+ ___block_literal_global.592
+ ___block_literal_global.620
+ ___block_literal_global.710
+ ___block_literal_global.720
+ ___block_literal_global.896
+ ___block_literal_global.898
+ ___block_literal_global.926
- ___101+[SOSUtilities setKappaTriggersEmergencySOS:isWristDetectionEnabled:confirmationDelegate:completion:]_block_invoke.904
- ___101+[SOSUtilities setKappaTriggersEmergencySOS:isWristDetectionEnabled:confirmationDelegate:completion:]_block_invoke.908
- ___111+[SOSUtilities setKappaThirdPartyActive:forApp:forPairedDevice:presentConfirmationOnViewController:completion:]_block_invoke.1018
- ___120+[SOSUtilities setNewtonTriggersEmergencySOS:isWristDetectionEnabled:newtonEligibility:confirmationDelegate:completion:]_block_invoke.606
- ___120+[SOSUtilities setNewtonTriggersEmergencySOS:isWristDetectionEnabled:newtonEligibility:confirmationDelegate:completion:]_block_invoke.607
- ___120+[SOSUtilities setNewtonTriggersEmergencySOS:isWristDetectionEnabled:newtonEligibility:confirmationDelegate:completion:]_block_invoke.608
- ___132+[SOSUtilities setNewtonTriggersEmergencySOSWorkoutsOnly:isWristDetectionEnabled:newtonEligibility:confirmationDelegate:completion:]_block_invoke.609
- ___18-[SOSManager init]_block_invoke.365
- ___18-[SOSManager init]_block_invoke.369
- ___24-[SOSManager connection]_block_invoke.375
- ___24-[SOSManager connection]_block_invoke.376
- ___38-[SOSEngine dismissSOSWithCompletion:]_block_invoke.378
- ___40-[SOSManager _resetStateWithCompletion:]_block_invoke.386
- ___42-[SOSContactsManager initWithHealthStore:]_block_invoke.329
- ___48-[SOSEngine listener:shouldAcceptNewConnection:]_block_invoke.534
- ___52+[SOSEngine shiftedLocationWithLocation:completion:]_block_invoke.404
- ___55-[SOSContactsManager _fetchSafetyMonitorSessionHandles]_block_invoke.355
- ___55-[SOSStatusManager listener:shouldAcceptNewConnection:]_block_invoke.310
- ___56-[SOSCoordinator processEventWithUUID:triggerMechanism:]_block_invoke.346
- ___77+[SOSUtilities setKappaTriggersEmergencySOS:confirmationDelegate:completion:]_block_invoke.915
- ___87+[SOSEngine _sendMessageToRecipients:withLocation:isFirstMessage:medicalIDName:Reason:]_block_invoke.397
- ___87+[SOSEngine _sendMessageToRecipients:withLocation:isFirstMessage:medicalIDName:Reason:]_block_invoke.397.cold.1
- ___91+[SOSNewtonManager newtonEligibilityWithHealthStore:deviceSupportsWorkoutsOnly:completion:]_block_invoke.302
- ___block_literal_global.1027
- ___block_literal_global.1029
- ___block_literal_global.1031
- ___block_literal_global.1043
- ___block_literal_global.340
- ___block_literal_global.346
- ___block_literal_global.367
- ___block_literal_global.369
- ___block_literal_global.371
- ___block_literal_global.373
- ___block_literal_global.377
- ___block_literal_global.381
- ___block_literal_global.383
- ___block_literal_global.394
- ___block_literal_global.495
- ___block_literal_global.497
- ___block_literal_global.519
- ___block_literal_global.583
- ___block_literal_global.611
- ___block_literal_global.701
- ___block_literal_global.711
- ___block_literal_global.880
- ___block_literal_global.887
- ___block_literal_global.917
CStrings:
+ "applicationsDidUpdateMetadata:"
+ "service:account:didReceiveLocalNetworkHandshake:fromID:context:"
+ "v52@0:8@\"IDSService\"16@\"IDSAccount\"24B32@\"NSString\"36@\"NSData\"44"
+ "v52@0:8@16@24B32@36@44"

```
