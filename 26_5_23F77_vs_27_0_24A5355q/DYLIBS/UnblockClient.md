## UnblockClient

> `/System/Library/PrivateFrameworks/UnblockClient.framework/UnblockClient`

```diff

-14.0.0.0.0
-  __TEXT.__text: 0x6828
-  __TEXT.__auth_stubs: 0x470
+17.0.0.0.0
+  __TEXT.__text: 0x71b8
   __TEXT.__objc_methlist: 0x558
-  __TEXT.__const: 0x78
-  __TEXT.__gcc_except_tab: 0x10c
-  __TEXT.__cstring: 0xf28
+  __TEXT.__const: 0xca
+  __TEXT.__gcc_except_tab: 0x150
+  __TEXT.__cstring: 0xffa
   __TEXT.__oslogstring: 0x615
-  __TEXT.__unwind_info: 0x168
-  __TEXT.__objc_classname: 0x9f
-  __TEXT.__objc_methname: 0xfc9
-  __TEXT.__objc_methtype: 0x1d5
-  __TEXT.__objc_stubs: 0xc40
-  __DATA_CONST.__got: 0xd8
-  __DATA_CONST.__const: 0x1e0
+  __TEXT.__swift5_typeref: 0x82
+  __TEXT.__swift5_capture: 0x10
+  __TEXT.__swift_as_entry: 0x4
+  __TEXT.__swift_as_ret: 0x4
+  __TEXT.__swift_as_cont: 0xc
+  __TEXT.__unwind_info: 0x1b8
+  __TEXT.__eh_frame: 0x70
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x218
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x400
+  __DATA_CONST.__objc_selrefs: 0x408
   __DATA_CONST.__objc_superrefs: 0x30
-  __AUTH_CONST.__auth_got: 0x248
-  __AUTH_CONST.__const: 0xc0
-  __AUTH_CONST.__cfstring: 0x1100
+  __DATA_CONST.__got: 0x110
+  __AUTH_CONST.__const: 0x110
+  __AUTH_CONST.__cfstring: 0x1180
   __AUTH_CONST.__objc_const: 0xb78
   __AUTH_CONST.__objc_intobj: 0x30
+  __AUTH_CONST.__auth_got: 0x3c8
   __DATA.__objc_ivar: 0x8c
-  __DATA.__data: 0xc0
+  __DATA.__data: 0x100
   __DATA_DIRTY.__objc_data: 0x1e0
   __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 19A8089B-9AA5-35DE-866A-92299B32DBF3
-  Functions: 146
-  Symbols:   609
-  CStrings:  544
+  - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_Concurrency.dylib
+  UUID: 95F9B469-FDA5-303B-85BC-ED5265533E25
+  Functions: 163
+  Symbols:   674
+  CStrings:  315
 
Symbols:
+ __Block_copy
+ __Block_release
+ ___58-[UBStuckServiceRecoveryResult _recoveryHadEffectiveness:]_block_invoke.371
+ ___58-[UBStuckServiceRecoveryResult _recoveryHadEffectiveness:]_block_invoke_2.382
+ ___61-[UBUnblockClient recover:stackshotData:replyQueue:callback:]_block_invoke.675
+ ___61-[UBUnblockClient recover:stackshotData:replyQueue:callback:]_block_invoke.676
+ ___block_literal_global.384
+ ___block_literal_global.395
+ ___block_literal_global.403
+ ___block_literal_global.634
+ ___chkstk_darwin
+ ___swift_async_cont_functlets
+ ___swift_async_entry_functlets
+ ___swift_async_ret_functlets
+ ___swift_closure_destructor
+ ___swift_instantiateConcreteTypeFromMangledNameV2
+ ___swift_reflection_version
+ __swiftEmptyDictionarySingleton
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftCoreFoundation_$_UnblockClient
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftDispatch_$_UnblockClient
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftFoundation_$_UnblockClient
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftObjectiveC_$_UnblockClient
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swiftXPC_$_UnblockClient
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_Builtin_float_$_UnblockClient
+ __swift_implicitisolationactor_to_executor_cast
+ _block_copy_helper
+ _block_descriptor
+ _block_destroy_helper
+ _objc_allocWithZone
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$initWithDomain:code:userInfo:
+ _objc_msgSend$recover:stackshotData:replyQueue:callback:
+ _objc_opt_self
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x24
+ _objc_retain_x28
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x8
+ _swift_allocObject
+ _swift_bridgeObjectRelease
+ _swift_bridgeObjectRetain
+ _swift_continuation_await
+ _swift_continuation_init
+ _swift_deallocObject
+ _swift_errorRetain
+ _swift_getObjCClassMetadata
+ _swift_getObjectType
+ _swift_getTypeByMangledNameInContext2
+ _swift_initStackObject
+ _swift_release
+ _swift_release_x20
+ _swift_release_x8
+ _swift_retain_x2
+ _swift_retain_x20
+ _swift_setDeallocating
+ _swift_task_alloc
+ _swift_task_dealloc
+ _swift_task_switch
+ _swift_willThrow
+ _symbolic SS_ypt
+ _symbolic SaySo28UBStuckServiceRecoveryResultCG
+ _symbolic ScCySaySo28UBStuckServiceRecoveryResultCG______pG s5ErrorP
+ _symbolic ______p s5ErrorP
+ _symbolic _____ySS_yptG s23_ContiguousArrayStorageC
+ _symbolic _____ySSypG s18_DictionaryStorageC
- _OUTLINED_FUNCTION_6
- _OUTLINED_FUNCTION_7
- ___58-[UBStuckServiceRecoveryResult _recoveryHadEffectiveness:]_block_invoke.369
- ___58-[UBStuckServiceRecoveryResult _recoveryHadEffectiveness:]_block_invoke_2.380
- ___61-[UBUnblockClient recover:stackshotData:replyQueue:callback:]_block_invoke.664
- ___61-[UBUnblockClient recover:stackshotData:replyQueue:callback:]_block_invoke.665
- ___block_literal_global.382
- ___block_literal_global.393
- ___block_literal_global.401
- ___block_literal_global.623
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x26
CStrings:
+ " (%@s after service became stuck)\n"
+ "No results returned and no error provided"
+ "Unknown process"
+ "no queue/thread name"
+ "recover(stuckServices:stackshotData:)"
+ "recovery not attempted (dry run)"
- ".cxx_destruct"
- "@\"NSArray\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_xpc_object>\""
- "@\"NSString\""
- "@\"NSUUID\""
- "@\"UBProcessInfo\""
- "@\"UBStuckService\""
- "@\"UBThreadInfo\""
- "@16@0:8"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@32@0:8@16@24"
- "@32@0:8i16@20B28"
- "@40@0:8@16@24^@32"
- "@44@0:8i16Q20d28@36"
- "@48@0:8Q16@24Q32@40"
- "B"
- "B16@0:8"
- "NSCoding"
- "NSSecureCoding"
- "Q"
- "Q16@0:8"
- "T@\"NSArray\",&,V_processesAndThreadsInvolved"
- "T@\"NSArray\",&,V_processesBlockedByOtherIssuesOnly"
- "T@\"NSArray\",&,V_processesBlockedByThisAndOtherIssues"
- "T@\"NSArray\",&,V_processesBlockedByThisIssueOnly"
- "T@\"NSArray\",&,V_serviceDependencyChain"
- "T@\"NSString\",&,V_clientName"
- "T@\"NSString\",&,V_serviceProcessName"
- "T@\"NSString\",R,V_clientName"
- "T@\"NSString\",R,V_dqLabel"
- "T@\"NSString\",R,V_name"
- "T@\"NSString\",R,V_threadName"
- "T@\"NSUUID\",R,V_incidentUUID"
- "T@\"UBProcessInfo\",&,V_process"
- "T@\"UBProcessInfo\",&,V_selectedProcess"
- "T@\"UBStuckService\",&,V_service"
- "T@\"UBThreadInfo\",R,V_thread"
- "TB,R"
- "TB,R,V_is3P"
- "TB,V_serviceProcessIs3P"
- "TQ,R"
- "TQ,R,V_dqid"
- "TQ,R,V_tid"
- "TQ,V_threadID"
- "Td,R,V_timeElapsed"
- "Td,V_timeSinceIssueBegan"
- "Ti,R"
- "Ti,R,V_pid"
- "Tq,V_effectiveness"
- "Tq,V_issueType"
- "Tq,V_numOtherIssues"
- "Tq,V_numThreadsBlockedByOtherIssues"
- "Tq,V_numThreadsBlockedByThisIssue"
- "Tq,V_recoveryConfidence"
- "Tq,V_recoveryStatus"
- "UBProcessInfo"
- "UBProcessThreadInfo"
- "UBStuckService"
- "UBStuckServiceRecoveryResult"
- "UBThreadInfo"
- "UBUnblockClient"
- "UTF8String"
- "UUIDString"
- "XPCHandling"
- "_connection"
- "_effectiveness"
- "_lock"
- "_recoveryHadEffectiveness:"
- "_replyQueue"
- "addCharactersInString:"
- "addObject:"
- "alphanumericCharacterSet"
- "appendFormat:"
- "appendString:"
- "archivedDataWithRootObject:requiringSecureCoding:error:"
- "bytes"
- "clientName"
- "compare:options:"
- "componentsJoinedByString:"
- "componentsSeparatedByCharactersInSet:"
- "copy"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "d"
- "d16@0:8"
- "dataWithBytes:length:"
- "dealloc"
- "debugDescription"
- "decodeArrayOfObjectsOfClass:forKey:"
- "decodeBoolForKey:"
- "decodeDoubleForKey:"
- "decodeInt32ForKey:"
- "decodeInt64ForKey:"
- "decodeIntegerForKey:"
- "decodeObjectOfClass:forKey:"
- "description"
- "dictionaryWithObject:forKey:"
- "doubleValue"
- "dqLabel"
- "dqid"
- "effectiveness"
- "encodeBool:forKey:"
- "encodeDouble:forKey:"
- "encodeInt32:forKey:"
- "encodeInt64:forKey:"
- "encodeInteger:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "errorWithDomain:code:userInfo:"
- "firstObject"
- "formUnionWithCharacterSet:"
- "handleRecoverReply:input_services:err:"
- "headerDescription"
- "i16@0:8"
- "incidentUUID"
- "init"
- "initForPid:threadID:timeElapsed:incidentUUID:"
- "initWithCapacity:"
- "initWithCoder:"
- "initWithFormat:"
- "initWithPid:name:is3P:"
- "initWithProcess:thread:"
- "initWithService:clientName:"
- "initWithTid:threadName:dqid:dqLabel:"
- "initWithUUIDString:"
- "integerValue"
- "invertedSet"
- "is3P"
- "isEqual:"
- "isEqualToString:"
- "issueType"
- "length"
- "longValue"
- "mutableCopy"
- "name"
- "numOtherIssues"
- "numThreadsBlockedByOtherIssues"
- "numThreadsBlockedByThisIssue"
- "numberWithDouble:"
- "numberWithInt:"
- "numberWithInteger:"
- "numberWithUnsignedInteger:"
- "objectAtIndexedSubscript:"
- "objectForKeyedSubscript:"
- "openConnectionToUnblockService"
- "pid"
- "prepareRecoverRequest:stackshot_data:err:"
- "process"
- "processesAndThreadsInvolved"
- "processesBlockedByOtherIssuesOnly"
- "processesBlockedByThisAndOtherIssues"
- "processesBlockedByThisIssueOnly"
- "q"
- "q16@0:8"
- "recover:stackshotData:replyQueue:callback:"
- "recoveryConfidence"
- "recoveryHadEffectiveness:"
- "recoveryStatus"
- "selectedProcess"
- "service"
- "serviceDependencyChain"
- "serviceProcessIs3P"
- "serviceProcessName"
- "setClientName:"
- "setEffectiveness:"
- "setIssueType:"
- "setNumOtherIssues:"
- "setNumThreadsBlockedByOtherIssues:"
- "setNumThreadsBlockedByThisIssue:"
- "setObject:atIndexedSubscript:"
- "setObject:forKeyedSubscript:"
- "setProcess:"
- "setProcessesAndThreadsInvolved:"
- "setProcessesBlockedByOtherIssuesOnly:"
- "setProcessesBlockedByThisAndOtherIssues:"
- "setProcessesBlockedByThisIssueOnly:"
- "setRecoveryConfidence:"
- "setRecoveryStatus:"
- "setSelectedProcess:"
- "setService:"
- "setServiceDependencyChain:"
- "setServiceProcessIs3P:"
- "setServiceProcessName:"
- "setThreadID:"
- "setTimeSinceIssueBegan:"
- "sortUsingComparator:"
- "stringWithUTF8String:"
- "supportsSecureCoding"
- "suppressTelemetry"
- "telemetryName"
- "thread"
- "threadID"
- "threadName"
- "tid"
- "timeElapsed"
- "timeSinceIssueBegan"
- "unarchivedArrayOfObjectsOfClass:fromData:error:"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@16"
- "v24@0:8Q16"
- "v24@0:8d16"
- "v24@0:8q16"
- "v48@0:8@16@24@32@?40"
- "whitespaceAndNewlineCharacterSet"
- "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"

```
