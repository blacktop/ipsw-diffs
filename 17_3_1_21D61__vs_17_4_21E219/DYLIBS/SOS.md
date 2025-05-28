## SOS

> `/System/Library/PrivateFrameworks/SOS.framework/SOS`

```diff

-498.300.11.0.0
-  __TEXT.__text: 0x2fdb8
+498.500.101.0.0
+  __TEXT.__text: 0x2fd94
   __TEXT.__auth_stubs: 0x870
   __TEXT.__objc_methlist: 0x26fc
-  __TEXT.__const: 0x178
+  __TEXT.__const: 0x150
   __TEXT.__gcc_except_tab: 0x6e4
-  __TEXT.__cstring: 0x3d96
+  __TEXT.__cstring: 0x3db2
   __TEXT.__oslogstring: 0x4c10
   __TEXT.__dlopen_cstrs: 0x403
   __TEXT.__unwind_info: 0xd58
   __TEXT.__objc_classname: 0x3f4
-  __TEXT.__objc_methname: 0x8d1e
+  __TEXT.__objc_methname: 0x8d2a
   __TEXT.__objc_methtype: 0x177b
   __TEXT.__objc_stubs: 0x6280
   __DATA_CONST.__got: 0x130

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x38d8
   __DATA_CONST.__objc_selrefs: 0x1ed0
+  __DATA_CONST.__objc_protorefs: 0x20
+  __DATA_CONST.__objc_classrefs: 0x288
+  __DATA_CONST.__objc_superrefs: 0x90
   __DATA_CONST.__objc_arraydata: 0x98
-  __AUTH_CONST.__cfstring: 0x3260
+  __AUTH_CONST.__cfstring: 0x3280
   __AUTH_CONST.__objc_const: 0xc50
-  __AUTH_CONST.__const: 0x580
+  __AUTH_CONST.__const: 0x5a0
   __AUTH_CONST.__objc_intobj: 0x198
   __AUTH_CONST.__objc_arrayobj: 0xd8
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH_CONST.__auth_got: 0x448
   __AUTH.__objc_data: 0x2d0
-  __DATA.__objc_protorefs: 0x20
-  __DATA.__objc_classrefs: 0x288
-  __DATA.__objc_superrefs: 0x90
   __DATA.__objc_ivar: 0x21c
-  __DATA.__data: 0x818
-  __DATA.__bss: 0x200
+  __DATA.__data: 0x810
+  __DATA.__bss: 0x210
   __DATA_DIRTY.__objc_data: 0x4b0
   __DATA_DIRTY.__data: 0x1
-  __DATA_DIRTY.__bss: 0xe0
+  __DATA_DIRTY.__bss: 0xe8
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1234
-  Symbols:   4266
-  CStrings:  2485
+  Functions: 1235
+  Symbols:   4271
+  CStrings:  2487
 
Symbols:
+ GCC_except_table104
+ GCC_except_table199
+ GCC_except_table201
+ GCC_except_table206
+ GCC_except_table214
+ ___101+[SOSUtilities setKappaTriggersEmergencySOS:isWristDetectionEnabled:confirmationDelegate:completion:]_block_invoke.854
+ ___101+[SOSUtilities setKappaTriggersEmergencySOS:isWristDetectionEnabled:confirmationDelegate:completion:]_block_invoke.858
+ ___111+[SOSUtilities setKappaThirdPartyActive:forApp:forPairedDevice:presentConfirmationOnViewController:completion:]_block_invoke.970
+ ___120+[SOSUtilities setNewtonTriggersEmergencySOS:isWristDetectionEnabled:newtonEligibility:confirmationDelegate:completion:]_block_invoke.546
+ ___120+[SOSUtilities setNewtonTriggersEmergencySOS:isWristDetectionEnabled:newtonEligibility:confirmationDelegate:completion:]_block_invoke.547
+ ___120+[SOSUtilities setNewtonTriggersEmergencySOS:isWristDetectionEnabled:newtonEligibility:confirmationDelegate:completion:]_block_invoke.548
+ ___132+[SOSUtilities setNewtonTriggersEmergencySOSWorkoutsOnly:isWristDetectionEnabled:newtonEligibility:confirmationDelegate:completion:]_block_invoke.549
+ ___18-[SOSManager init]_block_invoke.320
+ ___18-[SOSManager init]_block_invoke.324
+ ___24-[SOSManager connection]_block_invoke.330
+ ___24-[SOSManager connection]_block_invoke.331
+ ___29+[SOSUtilities deviceHasSlot]_block_invoke
+ ___38-[SOSEngine dismissSOSWithCompletion:]_block_invoke.294
+ ___40-[SOSManager _resetStateWithCompletion:]_block_invoke.341
+ ___42-[SOSContactsManager initWithHealthStore:]_block_invoke.270
+ ___45-[SOSStatusManager startHandoffFallbackTimer]_block_invoke.258
+ ___45-[SOSStatusManager startHandoffFallbackTimer]_block_invoke.258.cold.1
+ ___48-[SOSEngine listener:shouldAcceptNewConnection:]_block_invoke.442
+ ___52+[SOSEngine shiftedLocationWithLocation:completion:]_block_invoke.317
+ ___53-[SOSStatusManager startPairedDeviceClearStatusTimer]_block_invoke.257
+ ___53-[SOSStatusManager startPairedDeviceClearStatusTimer]_block_invoke.257.cold.1
+ ___54-[SOSStatusManager startCurrentDeviceClearStatusTimer]_block_invoke.251
+ ___54-[SOSStatusManager startCurrentDeviceClearStatusTimer]_block_invoke.251.cold.1
+ ___55-[SOSStatusManager listener:shouldAcceptNewConnection:]_block_invoke.259
+ ___56-[SOSCoordinator processEventWithUUID:triggerMechanism:]_block_invoke.292
+ ___77+[SOSUtilities setKappaTriggersEmergencySOS:confirmationDelegate:completion:]_block_invoke.865
+ ___79-[SOSEmergencyCallVoiceLoopManager shiftedLocationIfApplicable:withcompletion:]_block_invoke.308
+ ___87+[SOSEngine _sendMessageToRecipients:withLocation:isFirstMessage:medicalIDName:Reason:]_block_invoke.312
+ ___87+[SOSEngine _sendMessageToRecipients:withLocation:isFirstMessage:medicalIDName:Reason:]_block_invoke.312.cold.1
+ ___91+[SOSNewtonManager newtonEligibilityWithHealthStore:deviceSupportsWorkoutsOnly:completion:]_block_invoke.248
+ ___block_literal_global.281
+ ___block_literal_global.289
+ ___block_literal_global.291
+ ___block_literal_global.293
+ ___block_literal_global.297
+ ___block_literal_global.299
+ ___block_literal_global.302
+ ___block_literal_global.311
+ ___block_literal_global.316
+ ___block_literal_global.322
+ ___block_literal_global.408
+ ___block_literal_global.430
+ ___block_literal_global.523
+ ___block_literal_global.551
+ ___block_literal_global.641
+ ___block_literal_global.651
+ ___block_literal_global.830
+ ___block_literal_global.837
+ ___block_literal_global.839
+ ___block_literal_global.867
+ ___block_literal_global.982
+ ___block_literal_global.986
+ ___block_literal_global.988
+ ___block_literal_global.990
+ __unnamed_array_storage.326
+ __unnamed_array_storage.335
+ __unnamed_array_storage.340
+ __unnamed_array_storage.343
+ __unnamed_array_storage.346
+ __unnamed_array_storage.349
+ __unnamed_array_storage.352
+ _deviceHasSlot.__supportsDynamicIsland
+ _deviceHasSlot.onceToken
- GCC_except_table103
- GCC_except_table198
- GCC_except_table200
- GCC_except_table204
- GCC_except_table213
- ___101+[SOSUtilities setKappaTriggersEmergencySOS:isWristDetectionEnabled:confirmationDelegate:completion:]_block_invoke.827
- ___101+[SOSUtilities setKappaTriggersEmergencySOS:isWristDetectionEnabled:confirmationDelegate:completion:]_block_invoke.831
- ___111+[SOSUtilities setKappaThirdPartyActive:forApp:forPairedDevice:presentConfirmationOnViewController:completion:]_block_invoke.943
- ___120+[SOSUtilities setNewtonTriggersEmergencySOS:isWristDetectionEnabled:newtonEligibility:confirmationDelegate:completion:]_block_invoke.522
- ___120+[SOSUtilities setNewtonTriggersEmergencySOS:isWristDetectionEnabled:newtonEligibility:confirmationDelegate:completion:]_block_invoke.523
- ___120+[SOSUtilities setNewtonTriggersEmergencySOS:isWristDetectionEnabled:newtonEligibility:confirmationDelegate:completion:]_block_invoke.524
- ___132+[SOSUtilities setNewtonTriggersEmergencySOSWorkoutsOnly:isWristDetectionEnabled:newtonEligibility:confirmationDelegate:completion:]_block_invoke.525
- ___18-[SOSManager init]_block_invoke.296
- ___18-[SOSManager init]_block_invoke.300
- ___24-[SOSManager connection]_block_invoke.306
- ___24-[SOSManager connection]_block_invoke.307
- ___38-[SOSEngine dismissSOSWithCompletion:]_block_invoke.270
- ___40-[SOSManager _resetStateWithCompletion:]_block_invoke.317
- ___42-[SOSContactsManager initWithHealthStore:]_block_invoke.246
- ___45-[SOSStatusManager startHandoffFallbackTimer]_block_invoke.234
- ___45-[SOSStatusManager startHandoffFallbackTimer]_block_invoke.234.cold.1
- ___48-[SOSEngine listener:shouldAcceptNewConnection:]_block_invoke.418
- ___52+[SOSEngine shiftedLocationWithLocation:completion:]_block_invoke.293
- ___53-[SOSStatusManager startPairedDeviceClearStatusTimer]_block_invoke.233
- ___53-[SOSStatusManager startPairedDeviceClearStatusTimer]_block_invoke.233.cold.1
- ___54-[SOSStatusManager startCurrentDeviceClearStatusTimer]_block_invoke.227
- ___54-[SOSStatusManager startCurrentDeviceClearStatusTimer]_block_invoke.227.cold.1
- ___55-[SOSStatusManager listener:shouldAcceptNewConnection:]_block_invoke.235
- ___56-[SOSCoordinator processEventWithUUID:triggerMechanism:]_block_invoke.268
- ___77+[SOSUtilities setKappaTriggersEmergencySOS:confirmationDelegate:completion:]_block_invoke.838
- ___79-[SOSEmergencyCallVoiceLoopManager shiftedLocationIfApplicable:withcompletion:]_block_invoke.284
- ___87+[SOSEngine _sendMessageToRecipients:withLocation:isFirstMessage:medicalIDName:Reason:]_block_invoke.288
- ___87+[SOSEngine _sendMessageToRecipients:withLocation:isFirstMessage:medicalIDName:Reason:]_block_invoke.288.cold.1
- ___91+[SOSNewtonManager newtonEligibilityWithHealthStore:deviceSupportsWorkoutsOnly:completion:]_block_invoke.224
- ___block_literal_global.257
- ___block_literal_global.263
- ___block_literal_global.265
- ___block_literal_global.267
- ___block_literal_global.269
- ___block_literal_global.273
- ___block_literal_global.275
- ___block_literal_global.278
- ___block_literal_global.292
- ___block_literal_global.298
- ___block_literal_global.382
- ___block_literal_global.384
- ___block_literal_global.499
- ___block_literal_global.527
- ___block_literal_global.624
- ___block_literal_global.803
- ___block_literal_global.810
- ___block_literal_global.812
- ___block_literal_global.840
- ___block_literal_global.955
- ___block_literal_global.959
- ___block_literal_global.961
- ___block_literal_global.963
- __unnamed_array_storage.295
- __unnamed_array_storage.302
- __unnamed_array_storage.311
- __unnamed_array_storage.316
- __unnamed_array_storage.322
- __unnamed_array_storage.325
- __unnamed_array_storage.328
CStrings:
+ "DeviceSupportsDynamicIsland"
+ "T@\"NSString\",?,R,C"

```
