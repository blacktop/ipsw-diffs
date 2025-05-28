## SafetyMonitor

> `/System/Library/PrivateFrameworks/SafetyMonitor.framework/SafetyMonitor`

```diff

-896.0.1.0.1
-  __TEXT.__text: 0x58630
-  __TEXT.__auth_stubs: 0x11e0
-  __TEXT.__objc_methlist: 0x3588
+900.0.12.0.0
+  __TEXT.__text: 0x59a20
+  __TEXT.__auth_stubs: 0x1220
+  __TEXT.__objc_methlist: 0x35bc
   __TEXT.__const: 0xe70
-  __TEXT.__cstring: 0x6f73
+  __TEXT.__cstring: 0x729c
   __TEXT.__swift5_typeref: 0x441
   __TEXT.__swift5_capture: 0xf4
   __TEXT.__constg_swiftt: 0x358

   __TEXT.__swift5_assocty: 0x48
   __TEXT.__swift5_proto: 0xb0
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__oslogstring: 0x3267
+  __TEXT.__oslogstring: 0x32c8
   __TEXT.__ustring: 0x8c4
-  __TEXT.__gcc_except_tab: 0x7c8
-  __TEXT.__dlopen_cstrs: 0xa0
-  __TEXT.__unwind_info: 0x1ce4
-  __TEXT.__eh_frame: 0x9c8
+  __TEXT.__gcc_except_tab: 0x7d0
+  __TEXT.__dlopen_cstrs: 0x56
+  __TEXT.__unwind_info: 0x1da0
+  __TEXT.__eh_frame: 0xa18
   __TEXT.__objc_classname: 0x7d7
-  __TEXT.__objc_methname: 0x98da
-  __TEXT.__objc_methtype: 0x1726
+  __TEXT.__objc_methname: 0x9922
+  __TEXT.__objc_methtype: 0x170f
   __TEXT.__objc_stubs: 0x4920
-  __DATA_CONST.__got: 0x148
-  __DATA_CONST.__const: 0x1168
+  __DATA_CONST.__got: 0x140
+  __DATA_CONST.__const: 0x1128
   __DATA_CONST.__objc_classlist: 0x200
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x5a20
-  __DATA_CONST.__objc_selrefs: 0x1a58
+  __DATA_CONST.__objc_const: 0x5a40
+  __DATA_CONST.__objc_selrefs: 0x1a60
+  __DATA_CONST.__objc_protorefs: 0x38
+  __DATA_CONST.__objc_classrefs: 0x338
+  __DATA_CONST.__objc_superrefs: 0x158
   __AUTH_CONST.__const: 0x7c8
   __AUTH_CONST.__objc_const: 0x1c58
   __AUTH_CONST.__auth_ptr: 0x40
-  __AUTH_CONST.__cfstring: 0x4260
+  __AUTH_CONST.__cfstring: 0x4220
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH_CONST.__auth_got: 0x900
-  __AUTH.__objc_data: 0x1008
+  __AUTH_CONST.__auth_got: 0x920
+  __AUTH.__objc_data: 0xfb8
   __AUTH.__data: 0x2b8
-  __DATA.__objc_protorefs: 0x38
-  __DATA.__objc_classrefs: 0x338
-  __DATA.__objc_superrefs: 0x158
   __DATA.__objc_ivar: 0x304
-  __DATA.__data: 0xdc0
-  __DATA.__common: 0xf8
+  __DATA.__data: 0xeb8
+  __DATA.__common: 0x118
   __DATA.__bss: 0x1200
   __DATA_DIRTY.__objc_ivar: 0x184
-  __DATA_DIRTY.__objc_data: 0x6f0
-  __DATA_DIRTY.__data: 0xd8
+  __DATA_DIRTY.__objc_data: 0x740
+  __DATA_DIRTY.__data: 0xc0
   __DATA_DIRTY.__common: 0x8
-  __DATA_DIRTY.__bss: 0x410
+  __DATA_DIRTY.__bss: 0x400
   - /System/Library/Frameworks/ActivityKit.framework/ActivityKit
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /System/Library/PrivateFrameworks/InternalSwiftProtobuf.framework/InternalSwiftProtobuf
   - /System/Library/PrivateFrameworks/NanoPreferencesSync.framework/NanoPreferencesSync
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
-  - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
-  - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
-  - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
-  - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1754
-  Symbols:   4624
-  CStrings:  2594
+  Functions: 1769
+  Symbols:   4622
+  CStrings:  2611
 
Symbols:
+ +[SMTriggerDestinationState convertSMDirectionTransportTypeToString:]
+ -[SMEligibilityChecker iMessageIDSService]
+ -[SMEligibilityChecker initWithQueue:IDSIDQueryController:iMessageIDSService:iCloudIDSService:]
+ -[SMEligibilityChecker setIMessageIDSService:]
+ -[SMSafetyMonitorManager initializeAndStartSessionWithConfiguration:handler:]
+ -[SMSessionConfiguration coarseEstimatedEndDate]
+ -[SMSessionConfiguration copyConfigurationWithNewSessionID:]
+ -[SMSessionConfiguration estimatedEndDate]
+ GCC_except_table108
+ GCC_except_table246
+ GCC_except_table263
+ GCC_except_table73
+ GCC_except_table81
+ _OBJC_IVAR_$_SMEligibilityChecker._iMessageIDSService
+ ___101-[SMEligibilityChecker resolveEndpointsForDestinations:service:requiredCapabilities:completionBlock:]_block_invoke.26
+ ___43-[SMSafetyMonitorManager _createConnection]_block_invoke.276
+ ___43-[SMSafetyMonitorManager _createConnection]_block_invoke_2.275
+ ___45-[SMSafetyMonitorManager iMessageDeletedFor:]_block_invoke.325
+ ___56-[SMSafetyMonitorManager detailsViewOpenedForSessionID:]_block_invoke.340
+ ___57-[SMEligibilityChecker checkReceiverEligibility:handler:]_block_invoke.21
+ ___57-[SMEligibilityChecker checkReceiverEligibility:handler:]_block_invoke.22
+ ___57-[SMSafetyMonitorManager iMessageConversationDeletedFor:]_block_invoke.326
+ ___58-[SMSafetyMonitorManager cancelInitializationWithHandler:]_block_invoke.303
+ ___60-[SMSafetyMonitorManager iMessageScheduledSendTriggeredFor:]_block_invoke.323
+ ___61-[SMSafetyMonitorManager iMessageReceived:fromHandle:fromMe:]_block_invoke.324
+ ___62-[SMSafetyMonitorManager fetchCurrentSessionStateWithHandler:]_block_invoke.319
+ ___62-[SMSafetyMonitorManager initializeSessionWithHandle:handler:]_block_invoke.300
+ ___62-[SMSafetyMonitorManager sendSafetyCacheForSessionID:handler:]_block_invoke.307
+ ___64-[SMSafetyMonitorManager endSessionForSessionID:reason:handler:]_block_invoke.305
+ ___64-[SMSafetyMonitorManager startSessionWithConfiguration:handler:]_block_invoke.308
+ ___64-[SMSafetyMonitorManager stopMonitoringSessionStateWithHandler:]_block_invoke.318
+ ___65-[SMSafetyMonitorManager modifySessionWithConfiguration:handler:]_block_invoke.306
+ ___65-[SMSafetyMonitorManager startMonitoringSessionStateWithHandler:]_block_invoke.316
+ ___67-[SMSafetyMonitorManager cancelInitializationForSessionID:handler:]_block_invoke.304
+ ___68-[SMSafetyMonitorManager iMessageSendFor:guid:successful:withError:]_block_invoke.320
+ ___69-[SMSafetyMonitorManager fetchSessionReceiptForSessionID:completion:]_block_invoke.327
+ ___70-[SMSafetyMonitorManager fetchAllReceiverSessionStatusWithCompletion:]_block_invoke.329
+ ___72-[SMSafetyMonitorManager startMonitoringReceiverSafetyCacheWithHandler:]_block_invoke.337
+ ___74-[SMSafetyMonitorManager checkEligibilityOfDestination:completionHandler:]_block_invoke.342
+ ___74-[SMSafetyMonitorManager fetchReceiverSafetyCacheForSessionID:completion:]_block_invoke.335
+ ___74-[SMSafetyMonitorManager promptTimerEndedVerificationWithContext:handler:]_block_invoke.312
+ ___74-[SMSafetyMonitorManager startMonitoringReceiverSessionStatusWithHandler:]_block_invoke.331
+ ___74-[SMSafetyMonitorManager stopMonitoringReceiverSafetyCacheWithCompletion:]_block_invoke.339
+ ___75-[SMSafetyMonitorManager calculateDistanceToDestination:completionHandler:]_block_invoke.343
+ ___75-[SMSafetyMonitorManager fetchInitiatorSafetyCacheForSessionID:completion:]_block_invoke.315
+ ___76-[SMSafetyMonitorManager fetchReceiverSessionStatusForSessionID:completion:]_block_invoke.330
+ ___76-[SMSafetyMonitorManager stopMonitoringReceiverSessionStatusWithCompletion:]_block_invoke.333
+ ___76-[SMSafetyMonitorManager userRequestedCacheDownloadForSessionID:completion:]_block_invoke.334
+ ___77-[SMSafetyMonitorManager initializeAndStartSessionWithConfiguration:handler:]_block_invoke
+ ___77-[SMSafetyMonitorManager initializeAndStartSessionWithConfiguration:handler:]_block_invoke.309
+ ___77-[SMSafetyMonitorManager initializeAndStartSessionWithConfiguration:handler:]_block_invoke_2
+ ___78-[SMSafetyMonitorManager iMessageScheduledSendCancelFor:successful:withError:]_block_invoke.322
+ ___78-[SMSafetyMonitorManager respondToTriggerPromptForSessionID:response:handler:]_block_invoke.310
+ ___82-[SMSafetyMonitorManager promptDestinationAnomalyVerificationWithContext:handler:]_block_invoke.311
+ ___83-[SMSafetyMonitorManager estimateEtaToDestination:transportType:completionHandler:]_block_invoke.344
+ ___86-[SMSafetyMonitorManager iMessageScheduledSendScheduledFor:guid:successful:withError:]_block_invoke.321
+ ___91-[SMSafetyMonitorManager prepareUserInfoForNotificationContent:initiatorHandle:messageUrl:]_block_invoke.349
+ ___block_literal_global.314
+ ___block_literal_global.433
+ _malloc
+ _objc_msgSend$convertSMDirectionTransportTypeToString:
+ _objc_msgSend$iMessageIDSService
+ _objc_msgSend$initWithQueue:IDSIDQueryController:iMessageIDSService:iCloudIDSService:
+ _objc_msgSend$initializeAndStartSessionWithConfiguration:handler:
+ _swift_initStaticObject
- +[SMTriggerDestinationState convertMKDirectionTransportTypeToString:]
- -[SMEligibilityChecker iMAccountController]
- -[SMEligibilityChecker initWithQueue:IDSIDQueryController:IMAccountController:iCloudIDSService:]
- -[SMEligibilityChecker setIMAccountController:]
- GCC_except_table238
- GCC_except_table247
- GCC_except_table77
- GCC_except_table96
- _IDSServiceNameMultiplex1
- _MGGetStringAnswer
- _OBJC_IVAR_$_SMEligibilityChecker._iMAccountController
- ___101-[SMEligibilityChecker resolveEndpointsForDestinations:service:requiredCapabilities:completionBlock:]_block_invoke.59
- ___43-[SMSafetyMonitorManager _createConnection]_block_invoke.272
- ___43-[SMSafetyMonitorManager _createConnection]_block_invoke_2.273
- ___45-[SMSafetyMonitorManager iMessageDeletedFor:]_block_invoke.322
- ___56-[SMSafetyMonitorManager detailsViewOpenedForSessionID:]_block_invoke.337
- ___57-[SMEligibilityChecker checkReceiverEligibility:handler:]_block_invoke.54
- ___57-[SMEligibilityChecker checkReceiverEligibility:handler:]_block_invoke.55
- ___57-[SMSafetyMonitorManager iMessageConversationDeletedFor:]_block_invoke.323
- ___58-[SMSafetyMonitorManager cancelInitializationWithHandler:]_block_invoke.301
- ___60-[SMSafetyMonitorManager iMessageScheduledSendTriggeredFor:]_block_invoke.320
- ___61-[SMSafetyMonitorManager iMessageReceived:fromHandle:fromMe:]_block_invoke.321
- ___62-[SMSafetyMonitorManager fetchCurrentSessionStateWithHandler:]_block_invoke.316
- ___62-[SMSafetyMonitorManager initializeSessionWithHandle:handler:]_block_invoke.298
- ___62-[SMSafetyMonitorManager sendSafetyCacheForSessionID:handler:]_block_invoke.305
- ___64-[SMSafetyMonitorManager endSessionForSessionID:reason:handler:]_block_invoke.303
- ___64-[SMSafetyMonitorManager startSessionWithConfiguration:handler:]_block_invoke.306
- ___64-[SMSafetyMonitorManager stopMonitoringSessionStateWithHandler:]_block_invoke.315
- ___65-[SMSafetyMonitorManager modifySessionWithConfiguration:handler:]_block_invoke.304
- ___65-[SMSafetyMonitorManager startMonitoringSessionStateWithHandler:]_block_invoke.313
- ___67-[SMSafetyMonitorManager cancelInitializationForSessionID:handler:]_block_invoke.302
- ___68-[SMSafetyMonitorManager iMessageSendFor:guid:successful:withError:]_block_invoke.317
- ___69-[SMSafetyMonitorManager fetchSessionReceiptForSessionID:completion:]_block_invoke.324
- ___70-[SMSafetyMonitorManager fetchAllReceiverSessionStatusWithCompletion:]_block_invoke.326
- ___72-[SMSafetyMonitorManager startMonitoringReceiverSafetyCacheWithHandler:]_block_invoke.334
- ___74-[SMSafetyMonitorManager checkEligibilityOfDestination:completionHandler:]_block_invoke.339
- ___74-[SMSafetyMonitorManager fetchReceiverSafetyCacheForSessionID:completion:]_block_invoke.332
- ___74-[SMSafetyMonitorManager promptTimerEndedVerificationWithContext:handler:]_block_invoke.309
- ___74-[SMSafetyMonitorManager startMonitoringReceiverSessionStatusWithHandler:]_block_invoke.328
- ___74-[SMSafetyMonitorManager stopMonitoringReceiverSafetyCacheWithCompletion:]_block_invoke.336
- ___75-[SMSafetyMonitorManager calculateDistanceToDestination:completionHandler:]_block_invoke.340
- ___75-[SMSafetyMonitorManager fetchInitiatorSafetyCacheForSessionID:completion:]_block_invoke.312
- ___76-[SMSafetyMonitorManager fetchReceiverSessionStatusForSessionID:completion:]_block_invoke.327
- ___76-[SMSafetyMonitorManager stopMonitoringReceiverSessionStatusWithCompletion:]_block_invoke.330
- ___76-[SMSafetyMonitorManager userRequestedCacheDownloadForSessionID:completion:]_block_invoke.331
- ___78-[SMSafetyMonitorManager iMessageScheduledSendCancelFor:successful:withError:]_block_invoke.319
- ___78-[SMSafetyMonitorManager respondToTriggerPromptForSessionID:response:handler:]_block_invoke.307
- ___82-[SMSafetyMonitorManager promptDestinationAnomalyVerificationWithContext:handler:]_block_invoke.308
- ___83-[SMSafetyMonitorManager estimateEtaToDestination:transportType:completionHandler:]_block_invoke.341
- ___86-[SMSafetyMonitorManager iMessageScheduledSendScheduledFor:guid:successful:withError:]_block_invoke.318
- ___91-[SMSafetyMonitorManager prepareUserInfoForNotificationContent:initiatorHandle:messageUrl:]_block_invoke.346
- ___IMCoreLibraryCore_block_invoke
- ___block_literal_global.311
- ___block_literal_global.430
- ___getIMAccountControllerClass_block_invoke
- __swift_FORCE_LOAD_$_swiftAccelerate
- __swift_FORCE_LOAD_$_swiftAccelerate_$_SafetyMonitor
- __swift_FORCE_LOAD_$_swiftCoreImage
- __swift_FORCE_LOAD_$_swiftCoreImage_$_SafetyMonitor
- __swift_FORCE_LOAD_$_swiftDataDetection
- __swift_FORCE_LOAD_$_swiftDataDetection_$_SafetyMonitor
- __swift_FORCE_LOAD_$_swiftFileProvider
- __swift_FORCE_LOAD_$_swiftFileProvider_$_SafetyMonitor
- __swift_FORCE_LOAD_$_swiftUIKit
- __swift_FORCE_LOAD_$_swiftUIKit_$_SafetyMonitor
- _audit_stringIMCore
- _objc_msgSend$connectedAccounts
- _objc_msgSend$convertMKDirectionTransportTypeToString:
- _objc_msgSend$iMAccountController
- _objc_msgSend$initWithQueue:IDSIDQueryController:IMAccountController:iCloudIDSService:
CStrings:
+ " has been notified your timer ended."
+ "%@, checking recipient handle, recipientHandle, %@, self aliases, %@"
+ "Index out of range"
+ "Insufficient space allocated to copy string contents"
+ "Range requires lowerBound <= upperBound"
+ "SMDirectionsTransportTypeAny"
+ "SMDirectionsTransportTypeAutomobile"
+ "SMDirectionsTransportTypeTransit"
+ "SMDirectionsTransportTypeWalking"
+ "SMInitializeAndStartSession"
+ "Swift/ContiguousArrayBuffer.swift"
+ "Swift/Range.swift"
+ "Swift/StringTesting.swift"
+ "Swift/StringUTF8View.swift"
+ "Swift/UnsafeBufferPointer.swift"
+ "Swift/UnsafePointer.swift"
+ "Swift/UnsafeRawPointer.swift"
+ "T@\"IDSService\",&,N,V_iMessageIDSService"
+ "T@\"NSString\",?,R,C"
+ "Unexpectedly found nil while unwrapping an Optional value"
+ "UnsafeMutableBufferPointer with negative count"
+ "UnsafeMutablePointer.initialize overlapping range"
+ "UnsafeMutablePointer.initialize with negative count"
+ "UnsafeMutablePointer.moveInitialize with negative count"
+ "UnsafeMutableRawPointer.initializeMemory overlapping range"
+ "_iMessageIDSService"
+ "convertSMDirectionTransportTypeToString:"
+ "copyConfigurationWithNewSessionID:"
+ "iMessageIDSService"
+ "initWithQueue:IDSIDQueryController:iMessageIDSService:iCloudIDSService:"
+ "initializeAndStartSessionWithConfiguration:handler:"
+ "invalid Collection: less than 'count' elements in collection"
+ "setIMessageIDSService:"
- "@\"IMAccountController\""
- "DeviceClass"
- "IMAccountController"
- "MKDirectionsTransportTypeAny"
- "MKDirectionsTransportTypeAutomobile"
- "MKDirectionsTransportTypeTransit"
- "MKDirectionsTransportTypeWalking"
- "T@\"IMAccountController\",&,N,V_iMAccountController"
- "_iMAccountController"
- "connectedAccounts"
- "convertMKDirectionTransportTypeToString:"
- "iMAccountController"
- "iPhone"
- "initWithQueue:IDSIDQueryController:IMAccountController:iCloudIDSService:"
- "setIMAccountController:"
- "softlink:r:path:/System/Library/PrivateFrameworks/IMCore.framework/IMCore"

```
