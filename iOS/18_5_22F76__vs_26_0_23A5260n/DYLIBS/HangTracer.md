## HangTracer

> `/System/Library/PrivateFrameworks/HangTracer.framework/HangTracer`

```diff

-354.4.0.0.0
-  __TEXT.__text: 0xfef4
-  __TEXT.__auth_stubs: 0x8c0
-  __TEXT.__objc_methlist: 0x808
-  __TEXT.__const: 0x130
-  __TEXT.__cstring: 0x3877
-  __TEXT.__gcc_except_tab: 0x1a8
-  __TEXT.__oslogstring: 0x2011
-  __TEXT.__unwind_info: 0x418
-  __TEXT.__objc_classname: 0x37
-  __TEXT.__objc_methname: 0x32e6
-  __TEXT.__objc_methtype: 0x67d
-  __TEXT.__objc_stubs: 0xda0
-  __DATA_CONST.__got: 0x130
-  __DATA_CONST.__const: 0x13b8
-  __DATA_CONST.__objc_classlist: 0x18
+375.0.0.0.0
+  __TEXT.__text: 0x14ab8
+  __TEXT.__auth_stubs: 0xb10
+  __TEXT.__objc_methlist: 0x978
+  __TEXT.__const: 0x160
+  __TEXT.__cstring: 0x4148
+  __TEXT.__gcc_except_tab: 0x21c
+  __TEXT.__oslogstring: 0x271d
+  __TEXT.__ustring: 0xe0
+  __TEXT.__unwind_info: 0x4e0
+  __TEXT.__objc_classname: 0x54
+  __TEXT.__objc_methname: 0x394f
+  __TEXT.__objc_methtype: 0x71c
+  __TEXT.__objc_stubs: 0x12a0
+  __DATA_CONST.__got: 0x1c8
+  __DATA_CONST.__const: 0x1560
+  __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x788
-  __DATA_CONST.__objc_superrefs: 0x18
-  __AUTH_CONST.__auth_got: 0x470
-  __AUTH_CONST.__const: 0x340
-  __AUTH_CONST.__cfstring: 0x4b40
-  __AUTH_CONST.__objc_const: 0x1688
-  __AUTH_CONST.__objc_intobj: 0x18
-  __DATA.__objc_ivar: 0x1b8
-  __DATA.__data: 0x1a8
-  __DATA.__bss: 0x78
-  __DATA.__common: 0x8
+  __DATA_CONST.__objc_selrefs: 0x8e8
+  __DATA_CONST.__objc_superrefs: 0x20
+  __AUTH_CONST.__auth_got: 0x598
+  __AUTH_CONST.__const: 0x400
+  __AUTH_CONST.__cfstring: 0x5520
+  __AUTH_CONST.__objc_const: 0x19a8
+  __AUTH_CONST.__objc_intobj: 0x60
+  __AUTH.__objc_data: 0xa0
+  __DATA.__objc_ivar: 0x1e0
+  __DATA.__data: 0x1c8
+  __DATA.__common: 0x18
+  __DATA.__bss: 0x80
   __DATA_DIRTY.__objc_data: 0xf0
-  __DATA_DIRTY.__bss: 0xe0
+  __DATA_DIRTY.__bss: 0xf0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/AggregateDictionary.framework/AggregateDictionary

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libapp_launch_measurement.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C8014918-3318-3085-B466-3374848713FA
-  Functions: 435
-  Symbols:   1594
-  CStrings:  1907
+  UUID: 4D1A013C-9CED-31A3-87F7-EAB4B64A9FC3
+  Functions: 525
+  Symbols:   1920
+  CStrings:  2173
 
Symbols:
+ +[HTHangClient getClient]
+ +[HTHangClient getClient].cold.1
+ +[HTHangRequest sandboxExtensionForPath:]
+ -[HTHangClient .cxx_destruct]
+ -[HTHangClient _checkValidXPCDictResponse:]
+ -[HTHangClient _createXPCReplyHandler:]
+ -[HTHangClient connectionQueue]
+ -[HTHangClient connection]
+ -[HTHangClient dealloc]
+ -[HTHangClient establishHangTracerConnection]
+ -[HTHangClient pingConnectionAsyncAPI:]
+ -[HTHangClient pingConnectionSyncAPI:]
+ -[HTHangClient replyQueue]
+ -[HTHangClient sendMessageToHangTracerWithReply:responseHandler:]
+ -[HTHangClient sendMessageToHangTracerWithReplySync:error:]
+ -[HTHangRequest .cxx_destruct]
+ -[HTHangRequest _checkDirectoryPathIsValid]
+ -[HTHangRequest _createXPCDictionary:]
+ -[HTHangRequest _createXPCDictionary:].cold.1
+ -[HTHangRequest _createXPCDictionary:].cold.2
+ -[HTHangRequest _createXPCDictionary:].cold.3
+ -[HTHangRequest _insertNSNumberInXPCDictionaryUsingKey:number:dict:]
+ -[HTHangRequest _insertNSNumberInXPCDictionaryUsingKey:number:dict:].cold.1
+ -[HTHangRequest initRequest:error:]
+ -[HTHangRequest initRequestWithPath:dictionary:error:]
+ -[HTHangRequest requestXPCDictionary]
+ -[HTHangRequest sandboxExtension]
+ -[HTHangRequest sharedDirectoryPath]
+ -[HTPrefs minFGEmissionThresholdSec]
+ -[HTPrefs persistentFGEmissionThresholdSec]
+ -[HTPrefs shouldEmitTelemetry]
+ -[HTPrefs tailspinReportingThresholdSec]
+ GCC_except_table1
+ GCC_except_table10
+ GCC_except_table39
+ GCC_except_table41
+ GCC_except_table43
+ GCC_except_table46
+ GCC_except_table51
+ GCC_except_table57
+ GCC_except_table62
+ GCC_except_table63
+ GCC_except_table7
+ GCC_except_table72
+ _CAEventHTForegroundTrackingTelemetry
+ _GetSharedPage
+ _GetSharedPage.cold.1
+ _HTCollectHangLogsBundleWithStartEndTime
+ _HTCollectHangLogsBundleWithStartEndTime.cold.1
+ _HTCollectHangLogsBundleWithStartEndTimeSync
+ _HTCollectHangLogsBundleWithStartEndTimeSync.cold.1
+ _HTCollectHangLogsErrorCodeToLocalizedDescription
+ _HTCollectHangLogsErrorDomain
+ _HTCollectHangLogsGenerateClientResponseHandler
+ _HTForegroundTrackingBegin
+ _HTForegroundTrackingBegin.cold.1
+ _HTForegroundTrackingBegin.cold.2
+ _HTForegroundTrackingBegin.cold.3
+ _HTForegroundTrackingEnd
+ _HTForegroundTrackingEnd.cold.1
+ _HTResumeForegroundHangTracing
+ _HTResumeHangTracingWithStartTime
+ _HTResumeHangTracingWithStartTime.cold.1
+ _HTSuspendForegroundHangTracing
+ _HTSuspendHangTracingWithEndTime
+ _HTSuspendHangTracingWithEndTime.cold.1
+ _HTUpdateHangTracing.cold.1
+ _NSPOSIXErrorDomain
+ _OBJC_CLASS_$_HTHangClient
+ _OBJC_CLASS_$_HTHangRequest
+ _OBJC_CLASS_$_NSMutableString
+ _OBJC_CLASS_$_NSUUID
+ _OBJC_IVAR_$_HTHangClient._connection
+ _OBJC_IVAR_$_HTHangClient._connectionQueue
+ _OBJC_IVAR_$_HTHangClient._replyQueue
+ _OBJC_IVAR_$_HTHangRequest._requestXPCDictionary
+ _OBJC_IVAR_$_HTHangRequest._sandboxExtension
+ _OBJC_IVAR_$_HTHangRequest._sharedDirectoryPath
+ _OBJC_IVAR_$_HTPrefs._minFGEmissionThresholdSec
+ _OBJC_IVAR_$_HTPrefs._persistentFGEmissionThresholdSec
+ _OBJC_IVAR_$_HTPrefs._shouldEmitTelemetry
+ _OBJC_IVAR_$_HTPrefs._tailspinReportingThresholdSec
+ _OBJC_METACLASS_$_HTHangClient
+ _OBJC_METACLASS_$_HTHangRequest
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ _SANDBOX_EXTENSION_DEFAULT
+ __HTHangClientSingletonInstance
+ __OBJC_$_CLASS_METHODS_HTHangClient
+ __OBJC_$_CLASS_METHODS_HTHangRequest
+ __OBJC_$_INSTANCE_METHODS_HTHangClient
+ __OBJC_$_INSTANCE_METHODS_HTHangRequest
+ __OBJC_$_INSTANCE_VARIABLES_HTHangClient
+ __OBJC_$_INSTANCE_VARIABLES_HTHangRequest
+ __OBJC_$_PROP_LIST_HTHangClient
+ __OBJC_$_PROP_LIST_HTHangRequest
+ __OBJC_CLASS_RO_$_HTHangClient
+ __OBJC_CLASS_RO_$_HTHangRequest
+ __OBJC_METACLASS_RO_$_HTHangClient
+ __OBJC_METACLASS_RO_$_HTHangRequest
+ ___25+[HTHangClient getClient]_block_invoke
+ ___25+[HTHangClient getClient]_block_invoke.cold.1
+ ___39-[HTHangClient _createXPCReplyHandler:]_block_invoke
+ ___39-[HTHangClient _createXPCReplyHandler:]_block_invoke_2
+ ___39-[HTHangClient _createXPCReplyHandler:]_block_invoke_2.cold.1
+ ___39-[HTHangClient pingConnectionAsyncAPI:]_block_invoke
+ ___41+[HTMonitorPidHangEvent checkHangForPid:]_block_invoke
+ ___59-[HTHangClient sendMessageToHangTracerWithReplySync:error:]_block_invoke
+ ___59-[HTHangClient sendMessageToHangTracerWithReplySync:error:]_block_invoke.cold.1
+ ___65-[HTHangClient sendMessageToHangTracerWithReply:responseHandler:]_block_invoke
+ ___Block_byref_object_copy_
+ ___Block_byref_object_dispose_
+ ___HTCollectHangLogsBundleWithStartEndTimeSync_block_invoke
+ ___HTCollectHangLogsGenerateClientResponseHandler_block_invoke
+ ___HTConnectToHTMonitor_block_invoke.25
+ ___HTHangEventCreateWithBundleID_block_invoke.44
+ ___HTInitializeHangTracerMonitor_block_invoke.32
+ ___HTInitializeHangTracerMonitor_block_invoke.32.cold.1
+ ___HTInitializeHangTracerMonitor_block_invoke.32.cold.2
+ ___HTInitializeHangTracerMonitor_block_invoke.32.cold.3
+ ___HTInitializeHangTracerMonitor_block_invoke.36
+ ___StartMonitoringWatchdogDisablement_block_invoke.162
+ ___block_descriptor_36_e5_v8?0l
+ ___block_descriptor_40_e8_32bs_e45_v24?0"NSObject<OS_xpc_object>"8"NSError"16ls32l8
+ ___block_descriptor_48_e8_32r_e30_v24?0"NSString"8"NSError"16lr32l8
+ ___block_descriptor_48_e8_32s40bs_e33_v16?0"NSObject<OS_xpc_object>"8ls32l8s40l8
+ ___block_descriptor_56_e8_32s40r_e45_v24?0"NSObject<OS_xpc_object>"8"NSError"16ls32l8r40l8
+ ___block_descriptor_56_e8_32s40s_e37_B24?0r*8"NSObject<OS_xpc_object>"16ls32l8s40l8
+ ___block_descriptor_64_e8_32s40s48bs56bs_e5_v8?0ls32l8s48l8s40l8s56l8
+ ___block_descriptor_64_e8_32s40s48r_e5_v8?0ls32l8r48l8s40l8
+ ___block_descriptor_72_e19_"NSDictionary"8?0l
+ ___block_literal_global.142
+ ___block_literal_global.150
+ ___block_literal_global.156
+ ___block_literal_global.166
+ ___block_literal_global.169
+ ___block_literal_global.171
+ ___block_literal_global.19
+ ___block_literal_global.20
+ ___block_literal_global.21
+ ___block_literal_global.218
+ ___block_literal_global.25
+ ___block_literal_global.27
+ ___block_literal_global.30
+ ___block_literal_global.31
+ ___block_literal_global.33
+ ___block_literal_global.38
+ ___block_literal_global.41
+ ___block_literal_global.43
+ ___checkForHangWithUserMovedAwayAndRecentAssertions_block_invoke.203
+ ___createXPCObjectStringRecursive_block_invoke
+ ___foregroundTrackingSignpost_block_invoke
+ ___handleSettingChange_block_invoke.148
+ ___syncConnectionToHangTracer_block_invoke
+ ___syncConnectionToHangTracer_block_invoke_2
+ ___updateHTForegroundTrackingState_block_invoke
+ __htMonitorConnectionQueue
+ __xpc_error_connection_invalid
+ __xpc_type_array
+ __xpc_type_bool
+ __xpc_type_data
+ __xpc_type_date
+ __xpc_type_double
+ __xpc_type_endpoint
+ __xpc_type_fd
+ __xpc_type_int64
+ __xpc_type_null
+ __xpc_type_string
+ __xpc_type_uint64
+ __xpc_type_uuid
+ _checkForRollingFGTelemetryEmission
+ _checkForRollingFGTelemetryEmission.cold.1
+ _close
+ _createXPCObjectString
+ _createXPCObjectStringRecursive
+ _dispatch_semaphore_create
+ _dispatch_semaphore_signal
+ _dispatch_semaphore_wait
+ _foregroundTrackingSignpost
+ _foregroundTrackingSignpost._signpostLog
+ _foregroundTrackingSignpost.cold.1
+ _foregroundTrackingSignpost.onceToken
+ _getClient.onceToken
+ _getProcessName
+ _getStringFromHTForegroundUpdateType
+ _isOverMinEmissionThreshold
+ _isOverPersistentEmissionThreshold
+ _kHTCoreAnalyticsAssertionTime
+ _kHTCoreAnalyticsForegroundTime
+ _kHTCoreAnalyticsHTForegroundUpdateType
+ _kHTCoreAnalyticsRunloopTime
+ _kHTOldestTailspinCreationTimeInSpool
+ _kHTPrefsMinFGEmissionThresholdSec
+ _kHTPrefsPersistentFGEmissionThresholdSec
+ _kHTPrefsShouldEmitTelemetry
+ _kHTSuccessfulTailspinSaves
+ _kHTTailspinReportingThresholdSec
+ _kHTTailspinsInSpool
+ _kHTTailspinsOverReportingThreshold
+ _kHTTailspinsProcessed
+ _kHTTailspinsUnprocessed
+ _objc_autorelease
+ _objc_msgSend$UUIDString
+ _objc_msgSend$_checkDirectoryPathIsValid
+ _objc_msgSend$_checkValidXPCDictResponse:
+ _objc_msgSend$_createXPCDictionary:
+ _objc_msgSend$_createXPCReplyHandler:
+ _objc_msgSend$_insertNSNumberInXPCDictionaryUsingKey:number:dict:
+ _objc_msgSend$appendFormat:
+ _objc_msgSend$appendString:
+ _objc_msgSend$charValue
+ _objc_msgSend$compare:
+ _objc_msgSend$componentsJoinedByString:
+ _objc_msgSend$connection
+ _objc_msgSend$connectionQueue
+ _objc_msgSend$dateWithTimeIntervalSince1970:
+ _objc_msgSend$description
+ _objc_msgSend$establishHangTracerConnection
+ _objc_msgSend$getClient
+ _objc_msgSend$initRequest:error:
+ _objc_msgSend$initRequestWithPath:dictionary:error:
+ _objc_msgSend$initWithFormat:
+ _objc_msgSend$initWithUUIDBytes:
+ _objc_msgSend$longValue
+ _objc_msgSend$minFGEmissionThresholdSec
+ _objc_msgSend$mutableCopy
+ _objc_msgSend$numberWithUnsignedInteger:
+ _objc_msgSend$objCType
+ _objc_msgSend$persistentFGEmissionThresholdSec
+ _objc_msgSend$replyQueue
+ _objc_msgSend$requestXPCDictionary
+ _objc_msgSend$sandboxExtension
+ _objc_msgSend$sandboxExtensionForPath:
+ _objc_msgSend$sendMessageToHangTracerWithReply:responseHandler:
+ _objc_msgSend$sendMessageToHangTracerWithReplySync:error:
+ _objc_msgSend$sharedDirectoryPath
+ _objc_msgSend$shortValue
+ _objc_msgSend$sortUsingSelector:
+ _objc_msgSend$string
+ _objc_msgSend$stringByPaddingToLength:withString:startingAtIndex:
+ _objc_msgSend$stringByReplacingOccurrencesOfString:withString:
+ _objc_msgSend$timeIntervalSince1970
+ _objc_opt_class
+ _objc_opt_isKindOfClass
+ _objc_release_x28
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x28
+ _objc_retain_x3
+ _pidForProcessName
+ _pidForProcessName.cold.1
+ _pidForProcessName.cold.2
+ _populateEmissionScenario
+ _proc_listpids
+ _proc_name
+ _sandbox_extension_issue_file
+ _strcmp
+ _strerror
+ _syncConnectionToHangTracer
+ _systemAppBundleID
+ _updateHTForegroundTrackingState
+ _updateHTForegroundTrackingState.cold.1
+ _updateHTForegroundTrackingState.cold.2
+ _updateHTForegroundTrackingState.cold.3
+ _updateHTForegroundTrackingState.cold.4
+ _xpc_array_get_count
+ _xpc_array_get_value
+ _xpc_bool_get_value
+ _xpc_connection_copy_invalidation_reason
+ _xpc_connection_send_message_with_reply
+ _xpc_data_get_length
+ _xpc_date_get_value
+ _xpc_dictionary_apply
+ _xpc_dictionary_get_bool
+ _xpc_dictionary_get_uint64
+ _xpc_dictionary_set_bool
+ _xpc_dictionary_set_date
+ _xpc_dictionary_set_double
+ _xpc_dictionary_set_int64
+ _xpc_dictionary_set_string
+ _xpc_double_get_value
+ _xpc_fd_dup
+ _xpc_int64_get_value
+ _xpc_string_get_string_ptr
+ _xpc_uint64_get_value
+ _xpc_uuid_get_bytes
- GCC_except_table31
- GCC_except_table33
- GCC_except_table35
- GCC_except_table38
- GCC_except_table40
- GCC_except_table42
- GCC_except_table48
- GCC_except_table49
- GCC_except_table6
- GCC_except_table60
- _HTResumeHangTracing.cold.1
- ___HTCollectHangLogsBundle_block_invoke
- ___HTConnectToHTMonitor_block_invoke.23
- ___HTEndNonResponsiveTaskAtTime_block_invoke
- ___HTHangEventCreateWithBundleID_block_invoke.33
- ___HTInitializeHangTracerMonitor_block_invoke.28
- ___HTInitializeHangTracerMonitor_block_invoke.28.cold.1
- ___HTInitializeHangTracerMonitor_block_invoke.28.cold.2
- ___HTInitializeHangTracerMonitor_block_invoke.28.cold.3
- ___HTInitializeHangTracerMonitor_block_invoke.33
- ___StartMonitoringWatchdogDisablement_block_invoke.118
- ____HTBeginNonResponsiveAssertionAtStartTime_block_invoke
- ___block_descriptor_40_e8_32s_e33_v16?0"NSObject<OS_xpc_object>"8ls32l8
- ___block_descriptor_41_e8_32s_e5_v8?0ls32l8
- ___block_descriptor_57_e19_"NSDictionary"8?0l
- ___block_literal_global.11
- ___block_literal_global.112
- ___block_literal_global.122
- ___block_literal_global.125
- ___block_literal_global.129
- ___block_literal_global.131
- ___block_literal_global.15
- ___block_literal_global.178
- ___block_literal_global.18
- ___block_literal_global.32
- ___block_literal_global.35
- ___block_literal_global.83
- ___block_literal_global.85
- ___block_literal_global.93
- ___checkForHangWithUserMovedAwayAndRecentAssertions_block_invoke.163
- ___handleSettingChange_block_invoke.91
- _checkForHang
- _checkForHang.cold.1
CStrings:
+ "\n%@]"
+ "\n%@}"
+ " "
+ "\""
+ "\"%@\""
+ "\"<invalid string ptr>\""
+ "%@\"%@\": %@"
+ "%@%@"
+ "%f"
+ "%lld"
+ "%s: %@"
+ ",\n"
+ "<Connection: %s>"
+ "<Connection: unknown>"
+ "<Data: %zu bytes>"
+ "<Date: %@ (%lld ns)>"
+ "<Endpoint: %s>"
+ "<Endpoint: unknown>"
+ "<Error: %s>"
+ "<Error: unknown>"
+ "<FD: %d>"
+ "<FD: invalid>"
+ "<UUID: %@>"
+ "<UUID: invalid bytes>"
+ "<Unknown XPC Type: %s>"
+ "<Unknown XPC Type>"
+ "<null internal xpc_object_t>"
+ "<null xpc_object_t>"
+ "@\"NSObject<OS_xpc_object>\""
+ "@24@0:8@16"
+ "@32@0:8@16^@24"
+ "@32@0:8^{?=II[8{hangEvent=QQdAiCCCC^{_opaque_pthread_t}Qi[64c][256c]B^?AQAQAQBB}][10{HTAssertionInfo=QQQQ[64c]B}]iQAQ}16Q24"
+ "@40@0:8@16@24^@32"
+ "@?24@0:8@?16"
+ "An unknown error occurred"
+ "App transitioned to background, suspending HangTracing."
+ "App transitioned to foreground, resuming HangTracing."
+ "App with bundleID:%s is no longer foreground at time=%llu, attempting to emit telemetry with emission type: %@"
+ "Attempting to emit telemetry for rolling foreground case with HTForegroundUpdateType: %@ with data from the past %f seconds"
+ "B24@0:8^@16"
+ "B24@?0r*8@\"NSObject<OS_xpc_object>\"16"
+ "B40@0:8r*16@24@32"
+ "Could not create sandbox extension for '%@'. This may be due to lack of sufficient permissions to access the directory."
+ "Could not create xpc_object_t request dictionary from dictionary '%@'"
+ "Creating hang event with BundleID: %{public}@"
+ "Directory path not provided by client"
+ "Encountered invalid event->rollingFGTimestamp, not going to double emit telemetry"
+ "Encountered non-NSSting key of class '%@' in request dictionary: %@"
+ "Encountered non-dictionary event: %s"
+ "Event nil, returning early."
+ "Failed to access connection queue with HangTracer."
+ "Failed to consume sandbox extension"
+ "Failed to create archive for hang logs"
+ "Failed to create reply queue for client."
+ "Failed to establish a connection to HangTracer with error: %@"
+ "Failed to establish connection with HangTracer."
+ "Failed to establish xpc connection with hangtracerd"
+ "Failed to get sharedPage, cannot report total assertion time."
+ "File '%@' does not exist"
+ "File '%@' is not a directory."
+ "Found matching pid:%d for processName:%s"
+ "Got response from HangTracer: %@"
+ "HTFGTrackingTelemetryMinEmissionThresholdSec"
+ "HTFGTrackingTelemetryPersistentEmissionRateSec"
+ "HTFGUpdateAppBackgrounded"
+ "HTFGUpdateHangOcurred"
+ "HTFGUpdatePersistentForegroundness"
+ "HTFGUpdateUserSwitchedAway"
+ "HTForegroundTracking"
+ "HTForegroundTracking telemetry already emitted by another process, returning early to not double-emit telemetry."
+ "HTHangClient"
+ "HTHangClientError"
+ "HTHangRequest"
+ "HangTracerShouldEmitTelemetry"
+ "Key '%@' in dictionary has value '%@' that is not an NSNumber, NSDate, or NSString."
+ "One or more of required XPC Keys were not recieved by hangtracerd"
+ "Passed invalid sandbox token to hangtracerd"
+ "Passed nil `HTHangRequest` parameter."
+ "Passed nil archive save path"
+ "Passed nil key or value. key: '%@', val: '%@'"
+ "Passed unsupported NSNumber primitive type: %s"
+ "Process is missing required entitlement: com.apple.hangtracer.collect-logs"
+ "Recieved XPC_ERROR_CONNECTION_INVALID connection from HangTracer with reason: %s"
+ "Recieved an unexpected XPC response from hangtracerd"
+ "Signposts are not enabled for HTForegroundTrackingSignpost logger, will not emit signposts for foreground tracking."
+ "SpringBoard emitted telemetry: %d"
+ "Start Date: %@ is later than End Date: %@"
+ "Started os_signpost_interval_begin for newSignpostID:%llu and bundleID:%s"
+ "Started os_signpost_interval_end for signpostID:%llu and bundleID:%s"
+ "T@\"NSObject<OS_dispatch_queue>\",R,N,V_connectionQueue"
+ "T@\"NSObject<OS_dispatch_queue>\",R,N,V_replyQueue"
+ "T@\"NSObject<OS_xpc_object>\",R,N,V_connection"
+ "T@\"NSObject<OS_xpc_object>\",R,N,V_requestXPCDictionary"
+ "T@\"NSString\",R,N,V_sandboxExtension"
+ "T@\"NSString\",R,N,V_sharedDirectoryPath"
+ "TB,R,V_shouldEmitTelemetry"
+ "T^{?=II[8{hangEvent=QQdAiCCCC^{_opaque_pthread_t}Qi[64c][256c]B^?AQAQAQBB}][10{HTAssertionInfo=QQQQ[64c]B}]iQAQ},R,V_shmem_region"
+ "Td,R,V_minFGEmissionThresholdSec"
+ "Td,R,V_persistentFGEmissionThresholdSec"
+ "Td,R,V_tailspinReportingThresholdSec"
+ "This SPI should only be invoked by when an app is backgrounded, invalid client: %@"
+ "Timed out waiting for response from hangtracerd"
+ "UUIDString"
+ "Unable to allocate pids buffer of size %d with error: %s"
+ "Unable to list all pids with error: %s"
+ "Unexpected error: %s"
+ "Updating event->rollingFGTimestamp from INVALID_FOREGROUND_TIMESTAMP to %llu"
+ "[\n"
+ "\\\""
+ "^{?=II[8{hangEvent=QQdAiCCCC^{_opaque_pthread_t}Qi[64c][256c]B^?AQAQAQBB}][10{HTAssertionInfo=QQQQ[64c]B}]iQAQ}"
+ "^{?=II[8{hangEvent=QQdAiCCCC^{_opaque_pthread_t}Qi[64c][256c]B^?AQAQAQBB}][10{HTAssertionInfo=QQQQ[64c]B}]iQAQ}16@0:8"
+ "_checkDirectoryPathIsValid"
+ "_checkValidXPCDictResponse:"
+ "_connection"
+ "_connectionQueue"
+ "_createXPCDictionary:"
+ "_createXPCReplyHandler:"
+ "_insertNSNumberInXPCDictionaryUsingKey:number:dict:"
+ "_minFGEmissionThresholdSec"
+ "_persistentFGEmissionThresholdSec"
+ "_replyQueue"
+ "_requestXPCDictionary"
+ "_sandboxExtension"
+ "_sharedDirectoryPath"
+ "_shouldEmitTelemetry"
+ "_tailspinReportingThresholdSec"
+ "appendFormat:"
+ "appendString:"
+ "assertion_time"
+ "charValue"
+ "com.apple.app-sandbox.read-write"
+ "com.apple.hangtracer.client-reply"
+ "com.apple.hangtracer.foreground_tracking"
+ "compare:"
+ "componentsJoinedByString:"
+ "conclave limit"
+ "connection"
+ "connectionQueue"
+ "dateWithTimeIntervalSince1970:"
+ "description"
+ "errorCode"
+ "establishHangTracerConnection"
+ "event->rollingFGTimestamp is later than now, this should never happen. (start:%llu > end:%llu)"
+ "event->rollingFGTimestamp was not set to INVALID_FOREGROUND_TIMESTAMP, not updating timestamp."
+ "false"
+ "foregroundAppBundleID=%{public}@"
+ "foreground_time"
+ "foreground_tracking"
+ "foreground_update_type"
+ "getClient"
+ "initRequest:error:"
+ "initRequestWithPath:dictionary:error:"
+ "initWithFormat:"
+ "initWithUUIDBytes:"
+ "kHTCollectHangLogsError"
+ "kHTHangRequestError"
+ "longValue"
+ "minFGEmissionThresholdSec"
+ "mutableCopy"
+ "null"
+ "numberWithUnsignedInteger:"
+ "objCType"
+ "oldestTailspinCreationSeconds"
+ "persistentFGEmissionThresholdSec"
+ "pidForProcessName"
+ "ping"
+ "pingConnectionAsyncAPI:"
+ "pingConnectionSyncAPI:"
+ "replyQueue"
+ "requestXPCDictionary"
+ "runloop_time"
+ "sandboxExtension"
+ "sandboxExtensionForPath:"
+ "sendMessageToHangTracerWithReply:responseHandler:"
+ "sendMessageToHangTracerWithReplySync:error:"
+ "sharedDirectoryPath"
+ "shortValue"
+ "shouldEmitTelemetry"
+ "sortUsingSelector:"
+ "string"
+ "stringByPaddingToLength:withString:startingAtIndex:"
+ "stringByReplacingOccurrencesOfString:withString:"
+ "success"
+ "successfulTailspinSaves"
+ "tailspinReportingThresholdSec"
+ "tailspinsInSpool"
+ "tailspinsOverReportingThresholds"
+ "tailspinsProcessed"
+ "tailspinsUnprocessed"
+ "timeIntervalSince1970"
+ "true"
+ "unblock deadlock"
+ "unblock thread limit"
+ "v24@?0@\"NSObject<OS_xpc_object>\"8@\"NSError\"16"
+ "v24@?0@\"NSString\"8@\"NSError\"16"
+ "v32@0:8@16@?24"
+ "{\n"
+ "\xf0\xf0Q!V!"
- "@32@0:8^{?=II[8{hangEvent=QQdAiCCCC^{_opaque_pthread_t}Qi[64c][256c]B^?}][10{HTAssertionInfo=QQQQ[64c]B}]iQ}16Q24"
- "T^{?=II[8{hangEvent=QQdAiCCCC^{_opaque_pthread_t}Qi[64c][256c]B^?}][10{HTAssertionInfo=QQQQ[64c]B}]iQ},R,V_shmem_region"
- "^{?=II[8{hangEvent=QQdAiCCCC^{_opaque_pthread_t}Qi[64c][256c]B^?}][10{HTAssertionInfo=QQQQ[64c]B}]iQ}"
- "^{?=II[8{hangEvent=QQdAiCCCC^{_opaque_pthread_t}Qi[64c][256c]B^?}][10{HTAssertionInfo=QQQQ[64c]B}]iQ}16@0:8"
- "appliedTimeoutSecs"
- "assertionDurationMs"
- "assertionName"
- "com.apple.hangtracer_assertion_begin"
- "com.apple.hangtracer_assertion_end"
- "missedTimeout"
- "requestedTimeoutSecs"
- "timeoutOverMaximum"
- "\xf0\xf0A!&!"

```
