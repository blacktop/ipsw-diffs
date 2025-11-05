## SafetyMonitor

> `/System/Library/PrivateFrameworks/SafetyMonitor.framework/Versions/A/SafetyMonitor`

```diff

-986.0.1.0.0
-  __TEXT.__text: 0x7c370
-  __TEXT.__auth_stubs: 0xf10
-  __TEXT.__objc_methlist: 0x42a4
-  __TEXT.__cstring: 0xba63
-  __TEXT.__const: 0xed0
-  __TEXT.__constg_swiftt: 0x348
-  __TEXT.__swift5_typeref: 0x3e6
+990.0.10.0.0
+  __TEXT.__text: 0x7b13c
+  __TEXT.__auth_stubs: 0xea0
+  __TEXT.__objc_methlist: 0x4c04
+  __TEXT.__const: 0xec0
+  __TEXT.__dlopen_cstrs: 0x60
+  __TEXT.__cstring: 0xb807
+  __TEXT.__constg_swiftt: 0x33c
+  __TEXT.__swift5_typeref: 0x37a
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_reflstr: 0x28e
   __TEXT.__swift5_assocty: 0x60
   __TEXT.__swift5_proto: 0x90
   __TEXT.__swift5_types: 0x3c
-  __TEXT.__oslogstring: 0x40be
-  __TEXT.__swift5_fieldmd: 0x390
-  __TEXT.__swift5_capture: 0x1e0
+  __TEXT.__oslogstring: 0x4092
+  __TEXT.__swift5_fieldmd: 0x384
+  __TEXT.__swift5_capture: 0x100
+  __TEXT.__swift_as_entry: 0x3c
+  __TEXT.__swift_as_ret: 0x40
   __TEXT.__swift5_protos: 0x4
   __TEXT.__ustring: 0xd34
-  __TEXT.__gcc_except_tab: 0xf6c
-  __TEXT.__dlopen_cstrs: 0x60
-  __TEXT.__unwind_info: 0x1788
+  __TEXT.__gcc_except_tab: 0xf68
+  __TEXT.__unwind_info: 0x1750
   __TEXT.__eh_frame: 0x7b4
-  __TEXT.__objc_classname: 0x9f1
-  __TEXT.__objc_methname: 0xc41b
-  __TEXT.__objc_methtype: 0x21b0
-  __TEXT.__objc_stubs: 0x5740
-  __DATA_CONST.__got: 0x4a0
+  __TEXT.__objc_classname: 0x9c9
+  __TEXT.__objc_methname: 0xc31a
+  __TEXT.__objc_methtype: 0x2155
+  __TEXT.__objc_stubs: 0x56a0
+  __DATA_CONST.__got: 0x498
   __DATA_CONST.__const: 0x930
-  __DATA_CONST.__objc_classlist: 0x268
+  __DATA_CONST.__objc_classlist: 0x260
   __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x120
+  __DATA_CONST.__objc_protolist: 0x118
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1fe8
+  __DATA_CONST.__objc_selrefs: 0x2210
   __DATA_CONST.__objc_protorefs: 0x38
-  __DATA_CONST.__objc_superrefs: 0x1b0
-  __AUTH_CONST.__auth_got: 0x798
-  __AUTH_CONST.__const: 0x1820
-  __AUTH_CONST.__cfstring: 0x4ee0
-  __AUTH_CONST.__objc_const: 0x95a8
+  __DATA_CONST.__objc_superrefs: 0x1a8
+  __AUTH_CONST.__auth_got: 0x760
+  __AUTH_CONST.__const: 0x15f0
+  __AUTH_CONST.__cfstring: 0x4e00
+  __AUTH_CONST.__objc_const: 0x80f8
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH.__objc_data: 0x1ae8
+  __AUTH.__objc_data: 0x1a88
   __AUTH.__data: 0x2d8
-  __DATA.__objc_ivar: 0x56c
-  __DATA.__data: 0x1300
+  __DATA.__objc_ivar: 0x554
+  __DATA.__data: 0x1368
   __DATA.__bss: 0x1230
-  __DATA.__common: 0x110
+  __DATA.__common: 0x88
   - /System/Library/Frameworks/CloudKit.framework/Versions/A/CloudKit
   - /System/Library/Frameworks/Contacts.framework/Versions/A/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 986B7367-5BC8-3391-908B-20B35ED25FD9
-  Functions: 2179
-  Symbols:   4031
-  CStrings:  3958
+  UUID: 3EA00D40-2820-3284-AFD8-C99D93D21503
+  Functions: 2147
+  Symbols:   3990
+  CStrings:  3922
 
Symbols:
+ +[SMFeatureFlags zelkovaKoreaEnabled]
+ GCC_except_table309
+ GCC_except_table313
+ GCC_except_table318
+ GCC_except_table322
+ GCC_except_table326
+ GCC_except_table330
+ GCC_except_table360
+ __43-[SMSafetyMonitorManager _createConnection]_block_invoke.322
+ __43-[SMSafetyMonitorManager _createConnection]_block_invoke.324
+ __43-[SMSafetyMonitorManager _createConnection]_block_invoke_2.323
+ __45-[SMSafetyMonitorManager iMessageDeletedFor:]_block_invoke.432
+ __54-[SMSafetyMonitorManager kickedFromIMessageGroupWith:]_block_invoke.437
+ __55-[SMSafetyMonitorManager iMessageGroupPhotoChangedFor:]_block_invoke.436
+ __56-[SMSafetyMonitorManager detailsViewOpenedForSessionID:]_block_invoke.463
+ __57-[SMSafetyMonitorManager iMessageConversationDeletedFor:]_block_invoke.433
+ __58-[SMSafetyMonitorManager cancelInitializationWithHandler:]_block_invoke.353
+ __58-[SMSafetyMonitorManager fetchSOSReceiversWithCompletion:]_block_invoke.380
+ __60-[SMSafetyMonitorManager iMessageGroupMembershipChangedFor:]_block_invoke.434
+ __60-[SMSafetyMonitorManager iMessageScheduledSendTriggeredFor:]_block_invoke.428
+ __61-[SMSafetyMonitorManager handoffSessionForSessionID:handler:]_block_invoke.361
+ __61-[SMSafetyMonitorManager iMessageGroupDisplayNameChangedFor:]_block_invoke.435
+ __61-[SMSafetyMonitorManager iMessageReceived:fromHandle:fromMe:]_block_invoke.431
+ __62-[SMSafetyMonitorManager fetchCurrentSessionStateWithHandler:]_block_invoke.392
+ __62-[SMSafetyMonitorManager sendSafetyCacheForSessionID:handler:]_block_invoke.365
+ __64-[SMSafetyMonitorManager endSessionForSessionID:reason:handler:]_block_invoke.357
+ __64-[SMSafetyMonitorManager startSessionWithConfiguration:handler:]_block_invoke.366
+ __64-[SMSafetyMonitorManager stopMonitoringSessionStateWithHandler:]_block_invoke.391
+ __65-[SMSafetyMonitorManager fetchCurrentWorkoutSnapshotWithHandler:]_block_invoke.376
+ __65-[SMSafetyMonitorManager modifySessionWithConfiguration:handler:]_block_invoke.364
+ __65-[SMSafetyMonitorManager startMonitoringSessionStateWithHandler:]_block_invoke.387
+ __67-[SMSafetyMonitorManager cancelInitializationForSessionID:handler:]_block_invoke.356
+ __67-[SMSafetyMonitorManager fetchCurrentLocalSessionStateWithHandler:]_block_invoke.395
+ __68-[SMSafetyMonitorManager fetchMostLikelyReceiverHandlesWithHandler:]_block_invoke.409
+ __68-[SMSafetyMonitorManager iMessageSendFor:guid:successful:withError:]_block_invoke.422
+ __68-[SMSafetyMonitorManager initializeSessionWithConversation:handler:]_block_invoke.348
+ __69-[SMSafetyMonitorManager stopMonitoringLocalSessionStateWithHandler:]_block_invoke.402
+ __70-[SMSafetyMonitorManager fetchAllReceiverSessionStatusWithCompletion:]_block_invoke.444
+ __70-[SMSafetyMonitorManager startMonitoringLocalSessionStateWithHandler:]_block_invoke.399
+ __72-[SMSafetyMonitorManager fetchMostLikelySessionDestinationsWithHandler:]_block_invoke.414
+ __72-[SMSafetyMonitorManager startMonitoringReceiverSafetyCacheWithHandler:]_block_invoke.458
+ __73-[SMSafetyMonitorManager startMonitoringInitiatorSafetyCacheWithHandler:]_block_invoke.440
+ __74-[SMSafetyMonitorManager checkEligibilityOfDestination:completionHandler:]_block_invoke.470
+ __74-[SMSafetyMonitorManager fetchReceiverSafetyCacheForSessionID:completion:]_block_invoke.454
+ __74-[SMSafetyMonitorManager promptTimerEndedVerificationWithContext:handler:]_block_invoke.370
+ __74-[SMSafetyMonitorManager startMonitoringReceiverSessionStatusWithHandler:]_block_invoke.446
+ __74-[SMSafetyMonitorManager stopMonitoringReceiverSafetyCacheWithCompletion:]_block_invoke.462
+ __75-[SMSafetyMonitorManager calculateDistanceToDestination:completionHandler:]_block_invoke.471
+ __75-[SMSafetyMonitorManager fetchInitiatorSafetyCacheForSessionID:completion:]_block_invoke.384
+ __76-[SMSafetyMonitorManager fetchMostLikelyReceiverHandlesWithOptions:handler:]_block_invoke.413
+ __76-[SMSafetyMonitorManager fetchReceiverSessionStatusForSessionID:completion:]_block_invoke.445
+ __76-[SMSafetyMonitorManager stopMonitoringReceiverSessionStatusWithCompletion:]_block_invoke.450
+ __76-[SMSafetyMonitorManager userRequestedCacheDownloadForSessionID:completion:]_block_invoke.453
+ __77-[SMSafetyMonitorManager initializeAndStartSessionWithConfiguration:handler:]_block_invoke.367
+ __78-[SMSafetyMonitorManager iMessageScheduledSendCancelFor:successful:withError:]_block_invoke.426
+ __78-[SMSafetyMonitorManager respondToTriggerPromptForSessionID:response:handler:]_block_invoke.368
+ __82-[SMSafetyMonitorManager promptDestinationAnomalyVerificationWithContext:handler:]_block_invoke.369
+ __83-[SMSafetyMonitorManager estimateEtaToDestination:transportType:completionHandler:]_block_invoke.472
+ __86-[SMSafetyMonitorManager iMessageScheduledSendScheduledFor:guid:successful:withError:]_block_invoke.425
+ ___block_descriptor_48_e8_32bs40r_e53_v40?0"RTPlaceInference"8Q16"NSArray"24"NSError"32l
+ ___swift_async_entry_functlets
+ ___swift_async_ret_functlets
+ __block_literal_global.374
+ __block_literal_global.568
- +[SMSessionReceipt supportsSecureCoding]
- -[SMSafetyMonitorManager fetchSessionReceiptForSessionID:completion:]
- -[SMSessionReceipt .cxx_destruct]
- -[SMSessionReceipt description]
- -[SMSessionReceipt encodeWithCoder:]
- -[SMSessionReceipt endTime]
- -[SMSessionReceipt initWithCoder:]
- -[SMSessionReceipt initWithSessionID:sessionType:sessionStartTime:sessionEndTime:receiverHandles:safetyCacheReadStaus:]
- -[SMSessionReceipt readStatus]
- -[SMSessionReceipt receiverHandles]
- -[SMSessionReceipt sessionID]
- -[SMSessionReceipt sessionType]
- -[SMSessionReceipt startTime]
- GCC_except_table312
- GCC_except_table316
- GCC_except_table321
- GCC_except_table325
- GCC_except_table329
- GCC_except_table333
- GCC_except_table363
- OBJC_IVAR_$_SMSessionReceipt._endTime
- OBJC_IVAR_$_SMSessionReceipt._readStatus
- OBJC_IVAR_$_SMSessionReceipt._receiverHandles
- OBJC_IVAR_$_SMSessionReceipt._sessionID
- OBJC_IVAR_$_SMSessionReceipt._sessionType
- OBJC_IVAR_$_SMSessionReceipt._startTime
- _OBJC_CLASS_$_SMSessionReceipt
- _OBJC_METACLASS_$_SMSessionReceipt
- __43-[SMSafetyMonitorManager _createConnection]_block_invoke.325
- __43-[SMSafetyMonitorManager _createConnection]_block_invoke.327
- __43-[SMSafetyMonitorManager _createConnection]_block_invoke_2.326
- __45-[SMSafetyMonitorManager iMessageDeletedFor:]_block_invoke.435
- __54-[SMSafetyMonitorManager kickedFromIMessageGroupWith:]_block_invoke.440
- __55-[SMSafetyMonitorManager iMessageGroupPhotoChangedFor:]_block_invoke.439
- __56-[SMSafetyMonitorManager detailsViewOpenedForSessionID:]_block_invoke.467
- __57-[SMSafetyMonitorManager iMessageConversationDeletedFor:]_block_invoke.436
- __58-[SMSafetyMonitorManager cancelInitializationWithHandler:]_block_invoke.356
- __58-[SMSafetyMonitorManager fetchSOSReceiversWithCompletion:]_block_invoke.383
- __60-[SMSafetyMonitorManager iMessageGroupMembershipChangedFor:]_block_invoke.437
- __60-[SMSafetyMonitorManager iMessageScheduledSendTriggeredFor:]_block_invoke.431
- __61-[SMSafetyMonitorManager handoffSessionForSessionID:handler:]_block_invoke.364
- __61-[SMSafetyMonitorManager iMessageGroupDisplayNameChangedFor:]_block_invoke.438
- __61-[SMSafetyMonitorManager iMessageReceived:fromHandle:fromMe:]_block_invoke.434
- __62-[SMSafetyMonitorManager fetchCurrentSessionStateWithHandler:]_block_invoke.395
- __62-[SMSafetyMonitorManager sendSafetyCacheForSessionID:handler:]_block_invoke.368
- __64-[SMSafetyMonitorManager endSessionForSessionID:reason:handler:]_block_invoke.360
- __64-[SMSafetyMonitorManager startSessionWithConfiguration:handler:]_block_invoke.369
- __64-[SMSafetyMonitorManager stopMonitoringSessionStateWithHandler:]_block_invoke.394
- __65-[SMSafetyMonitorManager fetchCurrentWorkoutSnapshotWithHandler:]_block_invoke.379
- __65-[SMSafetyMonitorManager modifySessionWithConfiguration:handler:]_block_invoke.367
- __65-[SMSafetyMonitorManager startMonitoringSessionStateWithHandler:]_block_invoke.390
- __67-[SMSafetyMonitorManager cancelInitializationForSessionID:handler:]_block_invoke.359
- __67-[SMSafetyMonitorManager fetchCurrentLocalSessionStateWithHandler:]_block_invoke.398
- __68-[SMSafetyMonitorManager fetchMostLikelyReceiverHandlesWithHandler:]_block_invoke.412
- __68-[SMSafetyMonitorManager iMessageSendFor:guid:successful:withError:]_block_invoke.425
- __68-[SMSafetyMonitorManager initializeSessionWithConversation:handler:]_block_invoke.351
- __69-[SMSafetyMonitorManager fetchSessionReceiptForSessionID:completion:]_block_invoke.441
- __69-[SMSafetyMonitorManager stopMonitoringLocalSessionStateWithHandler:]_block_invoke.405
- __70-[SMSafetyMonitorManager fetchAllReceiverSessionStatusWithCompletion:]_block_invoke.448
- __70-[SMSafetyMonitorManager startMonitoringLocalSessionStateWithHandler:]_block_invoke.402
- __72-[SMSafetyMonitorManager fetchMostLikelySessionDestinationsWithHandler:]_block_invoke.417
- __72-[SMSafetyMonitorManager startMonitoringReceiverSafetyCacheWithHandler:]_block_invoke.462
- __73-[SMSafetyMonitorManager startMonitoringInitiatorSafetyCacheWithHandler:]_block_invoke.444
- __74-[SMSafetyMonitorManager checkEligibilityOfDestination:completionHandler:]_block_invoke.474
- __74-[SMSafetyMonitorManager fetchReceiverSafetyCacheForSessionID:completion:]_block_invoke.458
- __74-[SMSafetyMonitorManager promptTimerEndedVerificationWithContext:handler:]_block_invoke.373
- __74-[SMSafetyMonitorManager startMonitoringReceiverSessionStatusWithHandler:]_block_invoke.450
- __74-[SMSafetyMonitorManager stopMonitoringReceiverSafetyCacheWithCompletion:]_block_invoke.466
- __75-[SMSafetyMonitorManager calculateDistanceToDestination:completionHandler:]_block_invoke.475
- __75-[SMSafetyMonitorManager fetchInitiatorSafetyCacheForSessionID:completion:]_block_invoke.387
- __76-[SMSafetyMonitorManager fetchMostLikelyReceiverHandlesWithOptions:handler:]_block_invoke.416
- __76-[SMSafetyMonitorManager fetchReceiverSessionStatusForSessionID:completion:]_block_invoke.449
- __76-[SMSafetyMonitorManager stopMonitoringReceiverSessionStatusWithCompletion:]_block_invoke.454
- __76-[SMSafetyMonitorManager userRequestedCacheDownloadForSessionID:completion:]_block_invoke.457
- __77-[SMSafetyMonitorManager initializeAndStartSessionWithConfiguration:handler:]_block_invoke.370
- __78-[SMSafetyMonitorManager iMessageScheduledSendCancelFor:successful:withError:]_block_invoke.429
- __78-[SMSafetyMonitorManager respondToTriggerPromptForSessionID:response:handler:]_block_invoke.371
- __82-[SMSafetyMonitorManager promptDestinationAnomalyVerificationWithContext:handler:]_block_invoke.372
- __83-[SMSafetyMonitorManager estimateEtaToDestination:transportType:completionHandler:]_block_invoke.476
- __86-[SMSafetyMonitorManager iMessageScheduledSendScheduledFor:guid:successful:withError:]_block_invoke.428
- __OBJC_$_CLASS_METHODS_SMSessionReceipt
- __OBJC_$_CLASS_PROP_LIST_SMSessionReceipt
- __OBJC_$_INSTANCE_METHODS_SMSessionReceipt
- __OBJC_$_INSTANCE_VARIABLES_SMSessionReceipt
- __OBJC_$_PROP_LIST_SMSessionReceipt
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_SMInitiatorProtocol
- __OBJC_$_PROTOCOL_METHOD_TYPES_SMInitiatorProtocol
- __OBJC_CLASS_PROTOCOLS_$_SMSessionReceipt
- __OBJC_CLASS_RO_$_SMSessionReceipt
- __OBJC_LABEL_PROTOCOL_$_SMInitiatorProtocol
- __OBJC_METACLASS_RO_$_SMSessionReceipt
- __OBJC_PROTOCOL_$_SMInitiatorProtocol
- ___69-[SMSafetyMonitorManager fetchSessionReceiptForSessionID:completion:]_block_invoke
- ___block_descriptor_48_e8_32bs40r_e50_v32?0"RTPlaceInference"8"NSArray"16"NSError"24l
- __block_literal_global.377
- __block_literal_global.572
- _objc_msgSend$endTime
- _objc_msgSend$fetchSessionReceiptForSessionID:completion:
- _objc_msgSend$initWithSessionID:sessionType:sessionStartTime:sessionEndTime:receiverHandles:safetyCacheReadStaus:
- _objc_msgSend$readStatus
- _objc_msgSend$startTime
- _swift_beginAccess
- _swift_initStackObject
- _symbolic So22SMSessionConfigurationC
- _symbolic SuIegd_
- _symbolic SuIegr_
- _symbolic _____ 2os6LoggerV
- _symbolic _____ s5UInt8V
- _symbolic _____yySpy_____Gz_SpySo8NSObjectCSgGSgzSpyypGSgztcG s23_ContiguousArrayStorageC s5UInt8V
CStrings:
+ "#SafetyCache,%@,sessionID:%@,logCache,transactionID:%@,%@,locationsDuringSession,location,%lu,%{sensitive}@"
+ "#SafetyCache,%@,sessionID:%@,logCache,transactionID:%@,%@,lockLocation,%{sensitive}@"
+ "#SafetyCache,%@,sessionID:%@,logCache,transactionID:%@,%@,mostRecentLocation,%{sensitive}@"
+ "#SafetyCache,%@,sessionID:%@,logCache,transactionID:%@,%@,offWristLocation,%{sensitive}@"
+ "#SafetyCache,%@,sessionID:%@,logCache,transactionID:%@,%@,parkedCarLocation,%{sensitive}@"
+ "#SafetyCache,%@,sessionID:%@,logCache,transactionID:%@,%@,startingLocation,%{sensitive}@"
+ "#SafetyCache,%@,sessionID:%@,logCache,transactionID:%@,%@,unlockLocation,%{sensitive}@"
+ "SafetyMonitor-CloudKitFunction"
+ "SafetyMonitor-ContactsManager"
+ "SafetyMonitor-InitiatorAlert"
+ "SafetyMonitor-Intents"
+ "SafetyMonitor-LiveActivity"
+ "SafetyMonitor-SuggestionsManager"
+ "SafetyMonitor-TTR"
+ "SafetyMonitorUI-Initiator"
+ "SafetyMonitorUI-Receiver"
+ "SafetyMonitorUI-Shared"
+ "Zelkova_Korea"
+ "shifted locationDuringSession to %{sensitive}f,%{sensitive}f"
+ "shifted lockLocation to %{sensitive}f,%{sensitive}f"
+ "shifted mostRecentLocation to %{sensitive}f,%{sensitive}f"
+ "shifted offWristLocation to %{sensitive}f,%{sensitive}f"
+ "shifted parkedCarLocation to %{sensitive}f,%{sensitive}f"
+ "shifted startingLocation to %{sensitive}f,%{sensitive}f"
+ "shifted unlockLocation to %{sensitive}f,%{sensitive}f"
+ "shifted workoutEvent's location to %{sensitive}f,%{sensitive}f"
+ "v24@0:8@?<v@?@\"RTPlaceInference\"Q@\"NSArray\"@\"NSError\">16"
+ "v40@?0@\"RTPlaceInference\"8Q16@\"NSArray\"24@\"NSError\"32"
+ "zelkovaKoreaEnabled"
- "#SafetyCache,%@,sessionID:%@,logCache,transactionID:%@,%@,locationsDuringSession,location,%lu,%@"
- "#SafetyCache,%@,sessionID:%@,logCache,transactionID:%@,%@,lockLocation,%@"
- "#SafetyCache,%@,sessionID:%@,logCache,transactionID:%@,%@,mostRecentLocation,%@"
- "#SafetyCache,%@,sessionID:%@,logCache,transactionID:%@,%@,offWristLocation,%@"
- "#SafetyCache,%@,sessionID:%@,logCache,transactionID:%@,%@,parkedCarLocation,%@"
- "#SafetyCache,%@,sessionID:%@,logCache,transactionID:%@,%@,startingLocation,%@"
- "#SafetyCache,%@,sessionID:%@,logCache,transactionID:%@,%@,unlockLocation,%@"
- "#SafetyCache,Initiator,sessionID:%@,%@,%@,fetching session receipt"
- "@60@0:8@16Q24@32@40@48B56"
- "CloudKitFunction"
- "Fatal error"
- "Insufficient space allocated to copy string contents"
- "Invalid parameter not satisfying: endTime"
- "Invalid parameter not satisfying: startTime"
- "SMInitiatorProtocol"
- "SMSessionReceipt"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "T@\"NSDate\",R,N,V_endTime"
- "T@\"NSDate\",R,N,V_startTime"
- "TB,R,N,V_readStatus"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "__kSMSessionReceiptEndTimeKey"
- "__kSMSessionReceiptReadStatusKey"
- "__kSMSessionReceiptReceiverHandlesKey"
- "__kSMSessionReceiptSessionIDKey"
- "__kSMSessionReceiptSessionTypeKey"
- "__kSMSessionReceiptStartTimeKey"
- "_endTime"
- "_readStatus"
- "_startTime"
- "com.apple.SafetyMonitor"
- "endTime"
- "fetchSessionReceiptForSessionID:completion:"
- "initWithSessionID:sessionType:sessionStartTime:sessionEndTime:receiverHandles:safetyCacheReadStaus:"
- "invalid Collection: less than 'count' elements in collection"
- "logger"
- "readStatus"
- "sessionID, %@, sessionType, %d, receiverHandles, %@, startTime, %@, endTime, %@, readStatus, %d"
- "shifted locationDuringSession to %{private}f,%{private}f"
- "shifted lockLocation to %{private}f,%{private}f"
- "shifted mostRecentLocation to %{private}f,%{private}f"
- "shifted offWristLocation to %{private}f,%{private}f"
- "shifted parkedCarLocation to %{private}f,%{private}f"
- "shifted startingLocation to %{private}f,%{private}f"
- "shifted unlockLocation to %{private}f,%{private}f"
- "shifted workoutEvent's location to %{private}f,%{private}f"
- "startTime"
- "v24@0:8@?<v@?@\"RTPlaceInference\"@\"NSArray\"@\"NSError\">16"
- "v32@0:8@\"NSUUID\"16@?<v@?@\"NSUUID\"@\"SMSessionReceipt\"@\"NSError\">24"
- "v32@?0@\"RTPlaceInference\"8@\"NSArray\"16@\"NSError\"24"

```
