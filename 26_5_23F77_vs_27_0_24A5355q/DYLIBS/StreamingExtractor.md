## StreamingExtractor

> `/System/Library/PrivateFrameworks/StreamingExtractor.framework/StreamingExtractor`

```diff

-44.100.3.0.0
-  __TEXT.__text: 0xa39c
-  __TEXT.__auth_stubs: 0x520
-  __TEXT.__objc_methlist: 0x74c
+51.0.0.0.0
+  __TEXT.__text: 0xa210
+  __TEXT.__objc_methlist: 0x7cc
   __TEXT.__const: 0xd0
-  __TEXT.__cstring: 0x16d0
-  __TEXT.__oslogstring: 0xc9e
-  __TEXT.__gcc_except_tab: 0x3b4
-  __TEXT.__unwind_info: 0x330
-  __TEXT.__objc_classname: 0xe2
-  __TEXT.__objc_methname: 0x1484
-  __TEXT.__objc_methtype: 0x498
-  __TEXT.__objc_stubs: 0xe40
-  __DATA_CONST.__got: 0xa8
-  __DATA_CONST.__const: 0x410
-  __DATA_CONST.__objc_classlist: 0x20
+  __TEXT.__cstring: 0x17a8
+  __TEXT.__oslogstring: 0xd18
+  __TEXT.__gcc_except_tab: 0x1ec
+  __TEXT.__unwind_info: 0x2e0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x4b0
+  __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x560
+  __DATA_CONST.__objc_selrefs: 0x600
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x18
-  __AUTH_CONST.__auth_got: 0x2a0
+  __DATA_CONST.__objc_superrefs: 0x20
+  __DATA_CONST.__got: 0xb8
   __AUTH_CONST.__const: 0x40
-  __AUTH_CONST.__cfstring: 0x7a0
-  __AUTH_CONST.__objc_const: 0xa38
-  __AUTH.__objc_data: 0xf0
-  __DATA.__objc_ivar: 0x60
+  __AUTH_CONST.__cfstring: 0x7e0
+  __AUTH_CONST.__objc_const: 0xb88
+  __AUTH_CONST.__auth_got: 0x0
+  __AUTH.__objc_data: 0x140
+  __DATA.__objc_ivar: 0x70
   __DATA.__data: 0x328
   __DATA.__bss: 0x10
   __DATA_DIRTY.__objc_data: 0x50

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7036D4C5-A659-3E68-B51D-ADFFF2A2972E
-  Functions: 285
-  Symbols:   965
-  CStrings:  557
+  UUID: B9AE6B6A-3D03-351F-A3E5-1AB36192926C
+  Functions: 293
+  Symbols:   1013
+  CStrings:  265
 
Symbols:
+ -[ExtractionServiceInfo cancelPendingReservationsForExtractor:]
+ -[ExtractionServiceInfo reserveExtractionMemoryForExtractor:targetQueue:completion:]
+ -[ExtractionServiceInfo reserveExtractionMemoryForExtractor:targetQueue:completion:].cold.1
+ -[ExtractionServiceInfo reserveExtractionMemoryForExtractor:targetQueue:completion:].cold.2
+ -[ExtractionServiceInfo reserveExtractionMemoryForExtractor:targetQueue:completion:].cold.3
+ -[ExtractionServiceInfo reserveExtractionMemoryForExtractor:targetQueue:completion:].cold.4
+ -[ExtractionServiceInfo setWaiters:]
+ -[ExtractionServiceInfo waiters]
+ -[STExtractionMemoryWaiter .cxx_destruct]
+ -[STExtractionMemoryWaiter _invokeWaiterWithError:]
+ -[STExtractionMemoryWaiter completion]
+ -[STExtractionMemoryWaiter extractor]
+ -[STExtractionMemoryWaiter initWithExtractor:targetQueue:completion:]
+ -[STExtractionMemoryWaiter rejectWithError:]
+ -[STExtractionMemoryWaiter satisfy]
+ -[STExtractionMemoryWaiter setCompletion:]
+ -[STExtractionMemoryWaiter targetQueue]
+ -[STRemoteExtractor dataStreamReservationInFlight]
+ -[STRemoteExtractor pendingPostReservationBlocks]
+ -[STRemoteExtractor setDataStreamReservationInFlight:]
+ -[STRemoteExtractor setPendingPostReservationBlocks:]
+ GCC_except_table113
+ GCC_except_table38
+ GCC_except_table4
+ GCC_except_table48
+ _OBJC_CLASS_$_NSMutableArray
+ _OBJC_CLASS_$_NSMutableIndexSet
+ _OBJC_CLASS_$_STExtractionMemoryWaiter
+ _OBJC_IVAR_$_ExtractionServiceInfo._availableExtractionServiceMemoryLock
+ _OBJC_IVAR_$_ExtractionServiceInfo._waiters
+ _OBJC_IVAR_$_STExtractionMemoryWaiter._completion
+ _OBJC_IVAR_$_STExtractionMemoryWaiter._extractor
+ _OBJC_IVAR_$_STExtractionMemoryWaiter._targetQueue
+ _OBJC_IVAR_$_STRemoteExtractor._dataStreamReservationInFlight
+ _OBJC_IVAR_$_STRemoteExtractor._pendingPostReservationBlocks
+ _OBJC_METACLASS_$_STExtractionMemoryWaiter
+ __OBJC_$_INSTANCE_METHODS_STExtractionMemoryWaiter
+ __OBJC_$_INSTANCE_VARIABLES_STExtractionMemoryWaiter
+ __OBJC_$_PROP_LIST_STExtractionMemoryWaiter
+ __OBJC_CLASS_RO_$_STExtractionMemoryWaiter
+ __OBJC_METACLASS_RO_$_STExtractionMemoryWaiter
+ ___42-[STRemoteExtractor _sendData:completion:]_block_invoke.150
+ ___42-[STRemoteExtractor _sendData:completion:]_block_invoke.150.cold.1
+ ___42-[STRemoteExtractor _sendData:completion:]_block_invoke.151
+ ___42-[STRemoteExtractor _sendData:completion:]_block_invoke.156
+ ___42-[STRemoteExtractor _sendData:completion:]_block_invoke.156.cold.1
+ ___42-[STRemoteExtractor _sendData:completion:]_block_invoke.156.cold.2
+ ___42-[STRemoteExtractor _sendData:completion:]_block_invoke.156.cold.3
+ ___42-[STRemoteExtractor _sendData:completion:]_block_invoke.162
+ ___42-[STRemoteExtractor _sendData:completion:]_block_invoke.163
+ ___42-[STRemoteExtractor _sendData:completion:]_block_invoke.164
+ ___42-[STRemoteExtractor _sendData:completion:]_block_invoke.164.cold.1
+ ___42-[STRemoteExtractor _sendData:completion:]_block_invoke.164.cold.2
+ ___51-[STExtractionMemoryWaiter _invokeWaiterWithError:]_block_invoke
+ ___53-[STRemoteExtractor finishStreamWithCompletionBlock:]_block_invoke.196
+ ___53-[STRemoteExtractor supplyBytes:withCompletionBlock:]_block_invoke.184
+ ___53-[STRemoteExtractor supplyBytes:withCompletionBlock:]_block_invoke.184.cold.1
+ ___53-[STRemoteExtractor supplyBytes:withCompletionBlock:]_block_invoke.184.cold.2
+ ___53-[STRemoteExtractor supplyBytes:withCompletionBlock:]_block_invoke.184.cold.3
+ ___53-[STRemoteExtractor supplyBytes:withCompletionBlock:]_block_invoke.184.cold.4
+ ___54-[STRemoteExtractor suspendStreamWithCompletionBlock:]_block_invoke.195
+ ___62-[STRemoteExtractor terminateStreamWithError:completionBlock:]_block_invoke.197
+ ___63-[ExtractionServiceInfo cancelPendingReservationsForExtractor:]_block_invoke
+ ___64-[STRemoteExtractor prepareForExtractionToPath:completionBlock:]_block_invoke.128
+ ___64-[STRemoteExtractor prepareForExtractionToPath:completionBlock:]_block_invoke.128.cold.1
+ ___64-[STRemoteExtractor prepareForExtractionToPath:completionBlock:]_block_invoke.129
+ ___64-[STRemoteExtractor prepareForExtractionToPath:completionBlock:]_block_invoke.133
+ ___64-[STRemoteExtractor prepareForExtractionToPath:completionBlock:]_block_invoke_2.132
+ ___84-[ExtractionServiceInfo reserveExtractionMemoryForExtractor:targetQueue:completion:]_block_invoke
+ ___block_descriptor_40_e8_32s_e17_v16?0"NSError"8ls32l8
+ ___block_descriptor_48_e8_32bs40bs_e17_v16?0"NSError"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e5_v8?0ls40l8s32l8
+ ___block_descriptor_48_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48s_e41_v32?0"STExtractionMemoryWaiter"8Q16^B24ls32l8s40l8s48l8
+ _objc_claimAutoreleasedReturnValue
+ _objc_enumerationMutation
+ _objc_msgSend$_invokeWaiterWithError:
+ _objc_msgSend$addIndex:
+ _objc_msgSend$addObject:
+ _objc_msgSend$array
+ _objc_msgSend$availableExtractionServiceMemory
+ _objc_msgSend$cancelPendingReservationsForExtractor:
+ _objc_msgSend$completion
+ _objc_msgSend$count
+ _objc_msgSend$countByEnumeratingWithState:objects:count:
+ _objc_msgSend$dataStreamReservationInFlight
+ _objc_msgSend$enumerateObjectsUsingBlock:
+ _objc_msgSend$extractor
+ _objc_msgSend$indexSet
+ _objc_msgSend$initWithExtractor:targetQueue:completion:
+ _objc_msgSend$pendingPostReservationBlocks
+ _objc_msgSend$rejectWithError:
+ _objc_msgSend$removeAllObjects
+ _objc_msgSend$removeObjectsAtIndexes:
+ _objc_msgSend$removeObjectsInRange:
+ _objc_msgSend$reserveExtractionMemoryForExtractor:targetQueue:completion:
+ _objc_msgSend$satisfy
+ _objc_msgSend$setAvailableExtractionServiceMemory:
+ _objc_msgSend$setCompletion:
+ _objc_msgSend$setDataStreamReservationInFlight:
+ _objc_msgSend$setPendingPostReservationBlocks:
+ _objc_msgSend$targetQueue
+ _objc_msgSend$waiters
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x24
+ _objc_retain_x25
+ _objc_retain_x3
+ _objc_retain_x9
+ _objc_setProperty_nonatomic_copy
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
+ _qos_class_self
- -[ExtractionServiceInfo availableExtractionServiceMemoryCondition]
- -[ExtractionServiceInfo availableExtractionServiceMemoryMutex]
- -[ExtractionServiceInfo dealloc]
- -[ExtractionServiceInfo extractionBecameInvalid]
- -[ExtractionServiceInfo reserveExtractionMemory:]
- -[ExtractionServiceInfo reserveExtractionMemory:].cold.1
- -[ExtractionServiceInfo reserveExtractionMemory:].cold.2
- -[STRemoteExtractor _reserveExtractionMemory]
- -[STRemoteExtractor prepareForExtractionToPath:completionBlock:].cold.3
- -[STRemoteExtractor reservationQueue]
- GCC_except_table101
- GCC_except_table125
- GCC_except_table126
- GCC_except_table128
- GCC_except_table129
- GCC_except_table130
- GCC_except_table131
- GCC_except_table133
- GCC_except_table134
- GCC_except_table138
- GCC_except_table139
- GCC_except_table172
- GCC_except_table29
- GCC_except_table39
- _OBJC_IVAR_$_ExtractionServiceInfo._availableExtractionServiceMemoryCondition
- _OBJC_IVAR_$_ExtractionServiceInfo._availableExtractionServiceMemoryMutex
- _OBJC_IVAR_$_STRemoteExtractor._reservationQueue
- _OUTLINED_FUNCTION_60
- _OUTLINED_FUNCTION_61
- _OUTLINED_FUNCTION_62
- _OUTLINED_FUNCTION_63
- _OUTLINED_FUNCTION_64
- ___42-[STRemoteExtractor _sendData:completion:]_block_invoke.126
- ___42-[STRemoteExtractor _sendData:completion:]_block_invoke.126.cold.1
- ___42-[STRemoteExtractor _sendData:completion:]_block_invoke.127
- ___42-[STRemoteExtractor _sendData:completion:]_block_invoke.132
- ___42-[STRemoteExtractor _sendData:completion:]_block_invoke.132.cold.1
- ___42-[STRemoteExtractor _sendData:completion:]_block_invoke.132.cold.2
- ___42-[STRemoteExtractor _sendData:completion:]_block_invoke.132.cold.3
- ___42-[STRemoteExtractor _sendData:completion:]_block_invoke.138
- ___42-[STRemoteExtractor _sendData:completion:]_block_invoke.139
- ___42-[STRemoteExtractor _sendData:completion:]_block_invoke.140
- ___42-[STRemoteExtractor _sendData:completion:]_block_invoke.140.cold.1
- ___42-[STRemoteExtractor _sendData:completion:]_block_invoke.140.cold.2
- ___53-[STRemoteExtractor finishStreamWithCompletionBlock:]_block_invoke.172
- ___53-[STRemoteExtractor supplyBytes:withCompletionBlock:]_block_invoke.160
- ___53-[STRemoteExtractor supplyBytes:withCompletionBlock:]_block_invoke.160.cold.1
- ___53-[STRemoteExtractor supplyBytes:withCompletionBlock:]_block_invoke.160.cold.2
- ___53-[STRemoteExtractor supplyBytes:withCompletionBlock:]_block_invoke.160.cold.3
- ___53-[STRemoteExtractor supplyBytes:withCompletionBlock:]_block_invoke.160.cold.4
- ___54-[STRemoteExtractor suspendStreamWithCompletionBlock:]_block_invoke.171
- ___62-[STRemoteExtractor terminateStreamWithError:completionBlock:]_block_invoke.173
- ___64-[STRemoteExtractor prepareForExtractionToPath:completionBlock:]_block_invoke.104
- ___64-[STRemoteExtractor prepareForExtractionToPath:completionBlock:]_block_invoke.104.cold.1
- ___64-[STRemoteExtractor prepareForExtractionToPath:completionBlock:]_block_invoke.105
- ___64-[STRemoteExtractor prepareForExtractionToPath:completionBlock:]_block_invoke.109
- ___64-[STRemoteExtractor prepareForExtractionToPath:completionBlock:]_block_invoke_2.108
- ___block_descriptor_56_e8_32s40bs48bs_e5_v8?0ls32l8s40l8s48l8
- _objc_msgSend$_reserveExtractionMemory
- _objc_msgSend$extractionBecameInvalid
- _objc_msgSend$reservationQueue
- _objc_msgSend$reserveExtractionMemory:
- _objc_retainAutoreleasedReturnValue
- _objc_unsafeClaimAutoreleasedReturnValue
- _pthread_cond_broadcast
- _pthread_cond_destroy
- _pthread_cond_init
- _pthread_mutex_destroy
- _pthread_mutex_init
CStrings:
+ "%{public}s: Cancelled %lu pending reservation(s) for invalid extractor"
+ "%{public}s: Rejecting pending reservation: extractor invalid"
+ "%{public}s: Rejecting pending reservation: need [%zu] exceeds max [%d]"
+ "%{public}s: nil completion handler for extraction memory reservation, request will be dropped"
+ "%{public}s: waiting for available extraction memory (need [%zu] - avail [%zu] - waiters [%lu])"
+ "-[ExtractionServiceInfo cancelPendingReservationsForExtractor:]"
+ "-[ExtractionServiceInfo reserveExtractionMemoryForExtractor:targetQueue:completion:]"
+ "STRemoteExtractor invalid before extraction memory reservation"
+ "completion != nil"
+ "no targetQueue for extraction memory reservation"
+ "pending extraction memory reservation cancelled during drain"
+ "targetQueue != NULL"
+ "v32@?0@\"STExtractionMemoryWaiter\"8Q16^B24"
- "#16@0:8"
- "%{public}s: Extraction invalid - signaling to allow possible thread waiting for extraction memory to return"
- "%{public}s: available memory notification (need [%zu] - avail [%zu] - isValid [%d]"
- "%{public}s: waiting for available extraction memory (need [%zu] - avail [%zu])"
- "-[ExtractionServiceInfo extractionBecameInvalid]"
- "-[ExtractionServiceInfo reserveExtractionMemory:]"
- ".cxx_destruct"
- "@\"<STExtractionOriginatorProtocol>\""
- "@\"<STExtractorDelegate>\""
- "@\"<STExtractorDelegate>\"16@0:8"
- "@\"ExtractionServiceInfo\""
- "@\"NSError\""
- "@\"NSMutableDictionary\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSUUID\""
- "@\"NSXPCConnection\""
- "@\"STExtractionOriginator\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@24@0:8^@16"
- "@24@0:8^{_NSZone=}16"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8Q16^@24"
- "@40@0:8:16@24@32"
- "AB"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B32@0:8@16@24"
- "ExtractionServiceInfo"
- "Failed to get global concurrent queue for extraction memory reservations"
- "NSCoding"
- "NSCopying"
- "NSObject"
- "NSSecureCoding"
- "Q"
- "Q16@0:8"
- "STAEAExtractor"
- "STAEAExtractorWithOptions:"
- "STExtractionOriginator"
- "STExtractionOriginatorProtocol"
- "STExtractionServiceProtocol"
- "STExtractor"
- "STRemoteExtractor"
- "STReservableSpacePolicy"
- "T#,R"
- "T@\"<STExtractionOriginatorProtocol>\",W,V_originator"
- "T@\"<STExtractorDelegate>\",W,N"
- "T@\"<STExtractorDelegate>\",W,N,V_extractorDelegate"
- "T@\"ExtractionServiceInfo\",R,N,V_extractionServiceInfo"
- "T@\"NSData\",&,N"
- "T@\"NSDictionary\",R,N,V_options"
- "T@\"NSError\",&,N,V_error"
- "T@\"NSObject<OS_dispatch_queue>\",R,N,V_ioQueue"
- "T@\"NSObject<OS_dispatch_queue>\",R,N,V_reservationQueue"
- "T@\"NSString\",&,N"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,N,V_pluginBundlePath"
- "T@\"NSUUID\",R,N,V_uuid"
- "T@\"NSXPCConnection\",R,N,V_extractionServiceConnection"
- "T@\"STExtractionOriginator\",R,N,V_internalExtractionOriginator"
- "TB,?,R,N"
- "TB,N"
- "TB,N,V_dataStreamStarted"
- "TB,N,V_finalBytesSent"
- "TB,N,V_isInvalid"
- "TB,N,V_isPrepared"
- "TB,N,V_privileged"
- "TB,R"
- "TB,R,N"
- "TQ,N,V_availableExtractionServiceMemory"
- "TQ,N,V_lastResumptionOffset"
- "TQ,N,V_policyType"
- "TQ,N,V_requiredExtractionMemory"
- "TQ,N,V_reservedExtractionMemory"
- "TQ,R"
- "T{_opaque_pthread_cond_t=q[40c]},R,N,V_availableExtractionServiceMemoryCondition"
- "T{_opaque_pthread_mutex_t=q[56c]},R,N,V_availableExtractionServiceMemoryMutex"
- "UTF8String"
- "UUID"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "__setErrorForPtr:code:"
- "_availableExtractionServiceMemory"
- "_availableExtractionServiceMemoryCondition"
- "_availableExtractionServiceMemoryMutex"
- "_checkForInvalidExtractionMemoryReservation"
- "_dataStreamStarted"
- "_error"
- "_extractionServiceConnection"
- "_extractionServiceInfo"
- "_extractorDelegate"
- "_finalBytesSent"
- "_internalExtractionOriginator"
- "_invalidate"
- "_invalidated"
- "_ioQueue"
- "_isInvalid"
- "_isPrepared"
- "_lastResumptionOffset"
- "_options"
- "_originator"
- "_pluginBundlePath"
- "_policyType"
- "_privileged"
- "_releaseExtractionMemory"
- "_requiredExtractionMemory"
- "_reservationQueue"
- "_reservationQueue != NULL"
- "_reserveExtractionMemory"
- "_reservedExtractionMemory"
- "_sendData:completion:"
- "_uuid"
- "_xpcConnection"
- "addEntriesFromDictionary:"
- "allocWithZone:"
- "archiveID"
- "arrayWithObjects:count:"
- "asymmetricDecryptionKey"
- "autorelease"
- "availableExtractionServiceMemory"
- "availableExtractionServiceMemoryCondition"
- "availableExtractionServiceMemoryMutex"
- "boolValue"
- "bundleForClass:"
- "bundlePath"
- "class"
- "conformsToProtocol:"
- "connection"
- "copy"
- "copyWithZone:"
- "createDirectoryAtPath:withIntermediateDirectories:attributes:error:"
- "createOutputDir:"
- "dataStreamStarted"
- "dealloc"
- "debugDescription"
- "decodeBoolForKey:"
- "decodePropertyListForKey:"
- "defaultManager"
- "description"
- "dictionary"
- "dictionaryWithCapacity:"
- "dictionaryWithObjects:forKeys:count:"
- "doesConsumeExtractedData"
- "encodeBool:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "enumerateByteRangesUsingBlock:"
- "error"
- "errorWithDomain:code:userInfo:"
- "extractionBecameInvalid"
- "extractionCompleteAtArchivePath:"
- "extractionEnteredPassthroughMode"
- "extractionServiceConnection"
- "extractionServiceInfo"
- "extractionServiceInfoForPluginBundlePath:"
- "extractorDelegate"
- "fileExistsAtPath:"
- "fileSystemRepresentationWithPath:"
- "finalBytesSent"
- "finishStreamWithCompletionBlock:"
- "fullReplacementSTAEAExtractor:"
- "getUUIDBytes:"
- "hash"
- "incrementalPatchSTAEAExtractor:srcDirectory:"
- "init"
- "initWithCoder:"
- "initWithOptions:"
- "initWithPluginBundlePath:"
- "initWithPolicyType:errorPtr:"
- "initWithServiceName:"
- "initWithUUID:pluginBundlePath:"
- "interfaceWithProtocol:"
- "internalExtractionOriginator"
- "invalidate"
- "ioQueue"
- "isEqual:"
- "isInvalid"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isPrepared"
- "isProxy"
- "lastResumptionOffset"
- "length"
- "mutableCopy"
- "numberWithBool:"
- "numberWithUnsignedShort:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "originator"
- "pathWithComponents:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "pluginBundlePath"
- "pluginDirectory"
- "policyType"
- "prepareForExtractionToPath:completionBlock:"
- "processPolicyWithErrorPtr:"
- "release"
- "releaseExtractionMemory:"
- "remoteObjectProxyWithErrorHandler:"
- "remote_extractionCompleteAtArchivePath:"
- "remote_extractionEnteredPassthroughMode"
- "remote_finishStreamWithCompletionBlock:"
- "remote_prepareForExtractionToPath:sandboxExtensionToken:options:withCompletionBlock:"
- "remote_setExtractionProgress:"
- "remote_supplyBytes:withCompletionBlock:"
- "remote_suspendStreamWithCompletionBlock:"
- "remote_terminateStreamWithError:completionBlock:"
- "removeItemAtPath:error:"
- "requiredExtractionMemory"
- "reservationQueue"
- "reserveExtractionMemory:"
- "reservedExtractionMemory"
- "respondsToSelector:"
- "resume"
- "retain"
- "retainCount"
- "self"
- "sessionID"
- "setArchiveID:"
- "setAsymmetricDecryptionKey:"
- "setAvailableExtractionServiceMemory:"
- "setDataStreamStarted:"
- "setError:"
- "setExportedInterface:"
- "setExportedObject:"
- "setExtractionProgress:"
- "setExtractorDelegate:"
- "setFinalBytesSent:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setIsInvalid:"
- "setIsPrepared:"
- "setLastResumptionOffset:"
- "setObject:forKey:"
- "setOption:forKey:"
- "setOriginator:"
- "setPluginBundlePath:"
- "setPluginDirectory:"
- "setPolicyType:"
- "setPrivileged:"
- "setRemoteObjectInterface:"
- "setRequiredExtractionMemory:"
- "setReservedExtractionMemory:"
- "setSessionID:"
- "setSigningPublicKey:"
- "setSourceDirectory:"
- "setSourceDirectory:sandboxExtension:"
- "setSymmetricDecryptionKey:"
- "setUsesReserveAccessPolicy:"
- "setValue:forKey:"
- "signingPublicKey"
- "sourceDirectory"
- "stringWithCString:encoding:"
- "stringWithFileSystemRepresentation:length:"
- "stringWithFormat:"
- "subdataWithRange:"
- "superclass"
- "supplyBytes:withCompletionBlock:"
- "supportsSecureCoding"
- "suppressCompletionsDuringShutdown"
- "suspendStreamWithCompletionBlock:"
- "symmetricDecryptionKey"
- "terminateStreamWithError:completionBlock:"
- "threadPolicyWithErrorPtr:"
- "unsignedLongLongValue"
- "userInfo"
- "usesReserveAccessPolicy"
- "uuid"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"<STExtractorDelegate>\"16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@\"NSString\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?@\"NSError\">16"
- "v24@0:8@?<v@?Q@\"NSError\">16"
- "v24@0:8Q16"
- "v24@0:8d16"
- "v32@0:8@\"NSData\"16@?<v@?@\"NSError\"B>24"
- "v32@0:8@\"NSError\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"NSString\"16@?<v@?Q@\"NSError\">24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v32@0:8^@16Q24"
- "v48@0:8@\"NSString\"16@\"NSString\"24@\"NSDictionary\"32@?<v@?@\"NSDictionary\"Q@\"NSError\">40"
- "v48@0:8@16@24@32@?40"
- "valueForEntitlement:"
- "zone"
- "{_opaque_pthread_cond_t=\"__sig\"q\"__opaque\"[40c]}"
- "{_opaque_pthread_cond_t=q[40c]}16@0:8"
- "{_opaque_pthread_mutex_t=\"__sig\"q\"__opaque\"[56c]}"
- "{_opaque_pthread_mutex_t=q[56c]}16@0:8"

```
