## HangLogsDiagnosticExtension

> `/System/Library/PrivateFrameworks/HangTracer.framework/PlugIns/HangLogsDiagnosticExtension.appex/HangLogsDiagnosticExtension`

```diff

-354.4.0.0.0
-  __TEXT.__text: 0xb8a4
-  __TEXT.__auth_stubs: 0x770
+375.0.0.0.0
+  __TEXT.__text: 0x10fb8
+  __TEXT.__auth_stubs: 0x9a0
   __TEXT.__delay_helper: 0xc8
-  __TEXT.__objc_stubs: 0x11a0
-  __TEXT.__objc_methlist: 0x994
-  __TEXT.__const: 0x118
-  __TEXT.__cstring: 0x1b39
-  __TEXT.__oslogstring: 0x1123
-  __TEXT.__objc_classname: 0x95
-  __TEXT.__gcc_except_tab: 0xd0
-  __TEXT.__objc_methname: 0x37c6
-  __TEXT.__objc_methtype: 0x6bd
-  __TEXT.__unwind_info: 0x298
-  __DATA_CONST.__auth_got: 0x3c8
-  __DATA_CONST.__got: 0xf8
-  __DATA_CONST.__const: 0x8e0
-  __DATA_CONST.__cfstring: 0x1a20
-  __DATA_CONST.__objc_classlist: 0x38
+  __TEXT.__objc_stubs: 0x1840
+  __TEXT.__objc_methlist: 0xb34
+  __TEXT.__const: 0x148
+  __TEXT.__cstring: 0x2527
+  __TEXT.__oslogstring: 0x17dd
+  __TEXT.__gcc_except_tab: 0x1cc
+  __TEXT.__objc_methname: 0x3f87
+  __TEXT.__objc_classname: 0xb2
+  __TEXT.__objc_methtype: 0x751
+  __TEXT.__ustring: 0xe0
+  __TEXT.__unwind_info: 0x388
+  __DATA_CONST.__auth_got: 0x4e0
+  __DATA_CONST.__got: 0x198
+  __DATA_CONST.__const: 0xb58
+  __DATA_CONST.__cfstring: 0x2480
+  __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x18
-  __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0x1b38
-  __DATA.__objc_selrefs: 0x8d8
-  __DATA.__objc_ivar: 0x1e8
-  __DATA.__objc_data: 0x230
-  __DATA.__data: 0x98
-  __DATA.__bss: 0xa8
-  __DATA.__common: 0x8
+  __DATA_CONST.__objc_superrefs: 0x20
+  __DATA_CONST.__objc_intobj: 0x60
+  __DATA.__objc_const: 0x1eb8
+  __DATA.__objc_selrefs: 0xa98
+  __DATA.__objc_ivar: 0x218
+  __DATA.__objc_data: 0x2d0
+  __DATA.__data: 0xb4
+  __DATA.__bss: 0xd0
+  __DATA.__common: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libapp_launch_measurement.dylib
   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2A9847A9-6720-31BC-934B-96A58552BD78
-  Functions: 321
-  Symbols:   344
-  CStrings:  1119
+  UUID: D281F789-B761-3592-A147-0CD49CE5EC41
+  Functions: 414
+  Symbols:   431
+  CStrings:  1413
 
Symbols:
+ _CAEventHTForegroundTrackingTelemetry
+ _GetSharedPage
+ _HTCollectHangLogsBundleWithStartEndTime
+ _HTCollectHangLogsErrorCodeToLocalizedDescription
+ _HTCollectHangLogsGenerateClientResponseHandler
+ _HTConnectionQueue
+ _HTForegroundTrackingBegin
+ _HTForegroundTrackingEnd
+ _MATU_TO_SEC
+ _NSLocalizedDescriptionKey
+ _NSURLCreationDateKey
+ _OBJC_CLASS_$_HTHangClient
+ _OBJC_CLASS_$_HTHangRequest
+ _OBJC_CLASS_$_NSError
+ _OBJC_CLASS_$_NSUUID
+ _OBJC_METACLASS_$_HTHangClient
+ _OBJC_METACLASS_$_HTHangRequest
+ _SANDBOX_EXTENSION_DEFAULT
+ __HTHangClientSingletonInstance
+ __htMonitorConnectionQueue
+ __xpc_error_connection_invalid
+ __xpc_type_array
+ __xpc_type_bool
+ __xpc_type_connection
+ __xpc_type_data
+ __xpc_type_date
+ __xpc_type_dictionary
+ __xpc_type_double
+ __xpc_type_endpoint
+ __xpc_type_fd
+ __xpc_type_int64
+ __xpc_type_null
+ __xpc_type_string
+ __xpc_type_uint64
+ __xpc_type_uuid
+ _checkForRollingFGTelemetryEmission
+ _close
+ _createXPCObjectString
+ _dispatch_semaphore_create
+ _dispatch_semaphore_signal
+ _dispatch_semaphore_wait
+ _exit
+ _generateStringFormatForFGAppDurations
+ _getColPrefixForHTUsageDataSource
+ _getHTForegroundTrackingDurations
+ _getHangHistoryDescriptionWithForegroundSources
+ _isOverMinEmissionThreshold
+ _isOverPersistentEmissionThreshold
+ _kHTCoreAnalyticsAssertionTime
+ _kHTCoreAnalyticsForegroundTime
+ _kHTCoreAnalyticsHTForegroundUpdateType
+ _kHTCoreAnalyticsRunloopTime
+ _kHTPrefsMinFGEmissionThresholdSec
+ _kHTPrefsPersistentFGEmissionThresholdSec
+ _kHTPrefsShouldEmitTelemetry
+ _kHTTailspinReportingThresholdSec
+ _mmap
+ _objc_opt_class
+ _objc_opt_isKindOfClass
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x23
+ _objc_retain_x28
+ _printf
+ _puts
+ _sandbox_extension_issue_file
+ _syncConnectionToHangTracer
+ _updateHTForegroundTrackingState
+ _xpc_array_get_count
+ _xpc_array_get_value
+ _xpc_bool_get_value
+ _xpc_connection_cancel
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
- _NSLog
- _getHangHistoryDescription
CStrings:
+ "\n%-20s %5s %15s %10s %10s %10s"
+ "\n%@]"
+ "\n%@}"
+ "\nTotal Foreground Time\n———————————————"
+ " "
+ " %*@ %*@"
+ "\"%@\""
+ "\"<invalid string ptr>\""
+ "%-20s %5d %15s %10s"
+ "%@\n"
+ "%@ %*s %*s"
+ "%@ %@"
+ "%@\"%@\": %@"
+ "%@%@"
+ "%f"
+ "%lld"
+ "%s: %*.2f s\n"
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
+ "="
+ "@\"NSObject<OS_xpc_object>\""
+ "@32@0:8@16^@24"
+ "@32@0:8^{?=II[8{hangEvent=QQdAiCCCC^{_opaque_pthread_t}Qi[64c][256c]B^?AQAQAQBB}][10{HTAssertionInfo=QQQQ[64c]B}]iQAQ}16Q24"
+ "@40@0:8@16@24^@32"
+ "@?24@0:8@?16"
+ "An unknown error occurred"
+ "App with bundleID:%s is no longer foreground at time=%llu, attempting to emit telemetry with emission type: %@"
+ "Attempting to emit telemetry for rolling foreground case with HTForegroundUpdateType: %@ with data from the past %f seconds"
+ "B24@0:8^@16"
+ "B24@?0r*8@\"NSObject<OS_xpc_object>\"16"
+ "B40@0:8r*16@24@32"
+ "BiomeForegroundDurationHours"
+ "Could not create sandbox extension for '%@'. This may be due to lack of sufficient permissions to access the directory."
+ "Could not create xpc_object_t request dictionary from dictionary '%@'"
+ "Directory path not provided by client"
+ "ERROR: Biome lookup failed — %s\n"
+ "ERROR: Signpost extraction failed — %s"
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
+ "Failed to extract signposts with error: %@"
+ "Failed to get sharedPage, cannot report total assertion time."
+ "File '%@' does not exist"
+ "File '%@' is not a directory."
+ "Found %llu signpost intervals from %lu unique processes from %s to %s\nTotal Duration — %.2f hours\n\n"
+ "Found %zu hang intervals between %@ and %@ which took %@\n"
+ "Found file: %@"
+ "Got response from HangTracer: %@"
+ "HTFG"
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
+ "Processing signposts..."
+ "Querying Biome Database..."
+ "Recieved XPC_ERROR_CONNECTION_INVALID connection from HangTracer with reason: %s"
+ "Recieved an unexpected XPC response from hangtracerd"
+ "SELECT bundleID, sum(duration) FROM (     SELECT *, end_timestamp-start_timestamp AS duration FROM     (         SELECT bundleID,            CASE WHEN starting=1 THEN eventTimestamp ELSE NULL END AS start_timestamp,            CASE WHEN next_starting=0 THEN next_timestamp                  WHEN starting==0 AND previous_starting==0 THEN next_timestamp ELSE NULL END AS end_timestamp         FROM         (             SELECT bundleID, starting, eventTimestamp, lead(eventTimestamp) OVER win AS next_timestamp, lead(starting) OVER win AS next_starting, lag(starting) OVER win AS previous_starting FROM                 \"App.InFocus\"                 where eventTimestamp > %ld AND eventTimestamp < %ld                 WINDOW win AS (PARTITION BY bundleID ORDER BY eventTimestamp)         )     ) WHERE         start_timestamp IS NOT NULL OR end_timestamp IS NOT NULL     ORDER BY start_timestamp ) GROUP BY bundleID ORDER BY sum(duration) DESC "
+ "SignpostForegroundDurationHours"
+ "SignpostID: %-15llu Begin: %-30s End: %-30s Duration(s): %-10.2f Emitting Process: %-30s BundleID: %s\n"
+ "Signposts are not enabled for HTForegroundTrackingSignpost logger, will not emit signposts for foreground tracking."
+ "SpringBoard emitted telemetry: %d"
+ "Start Date: %@ is later than End Date: %@"
+ "Started os_signpost_interval_begin for newSignpostID:%llu and bundleID:%s"
+ "Started os_signpost_interval_end for signpostID:%llu and bundleID:%s"
+ "T@\"NSDate\",&,N,V_endDate"
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
+ "Tf,N,V_BiomeForegroundDurationHours"
+ "Tf,N,V_SignpostForegroundDurationHours"
+ "This SPI should only be invoked by when an app is backgrounded, invalid client: %@"
+ "Timed out waiting for response from hangtracerd"
+ "UUIDString"
+ "Unable to create shared page: %{errno}d"
+ "Unexpected error: %s"
+ "Updating event->rollingFGTimestamp from INVALID_FOREGROUND_TIMESTAMP to %llu"
+ "Usage Time (%s): %f seconds\n"
+ "[\n"
+ "\\\""
+ "^{?=II[8{hangEvent=QQdAiCCCC^{_opaque_pthread_t}Qi[64c][256c]B^?AQAQAQBB}][10{HTAssertionInfo=QQQQ[64c]B}]iQAQ}"
+ "^{?=II[8{hangEvent=QQdAiCCCC^{_opaque_pthread_t}Qi[64c][256c]B^?AQAQAQBB}][10{HTAssertionInfo=QQQQ[64c]B}]iQAQ}16@0:8"
+ "_BiomeForegroundDurationHours"
+ "_SignpostForegroundDurationHours"
+ "_checkDirectoryPathIsValid"
+ "_checkValidXPCDictResponse:"
+ "_connection"
+ "_connectionQueue"
+ "_createXPCDictionary:"
+ "_createXPCReplyHandler:"
+ "_endDate"
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
+ "array"
+ "assertion_time"
+ "cStringUsingEncoding:"
+ "charValue"
+ "com.apple.app-sandbox.read-write"
+ "com.apple.hangtracer.client-reply"
+ "com.apple.hangtracer.foreground_tracking"
+ "componentsJoinedByString:"
+ "connection"
+ "connectionQueue"
+ "dateByAddingTimeInterval:"
+ "dateWithTimeIntervalSince1970:"
+ "description"
+ "errorCode"
+ "errorWithDomain:code:userInfo:"
+ "establishHangTracerConnection"
+ "event->rollingFGTimestamp is later than now, this should never happen. (start:%llu > end:%llu)"
+ "event->rollingFGTimestamp was not set to INVALID_FOREGROUND_TIMESTAMP, not updating timestamp."
+ "false"
+ "fileName"
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
+ "longLongValue"
+ "longValue"
+ "metadata"
+ "minFGEmissionThresholdSec"
+ "mutableCopy"
+ "now"
+ "null"
+ "numberWithFloat:"
+ "numberWithUnsignedInt:"
+ "numberWithUnsignedInteger:"
+ "objCType"
+ "persistentFGEmissionThresholdSec"
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
+ "setBiomeForegroundDurationHours:"
+ "setDateStyle:"
+ "setEndDate:"
+ "setSignpostForegroundDurationHours:"
+ "setTimeStyle:"
+ "sharedDirectoryPath"
+ "shortValue"
+ "shouldEmitTelemetry"
+ "signpostId"
+ "sortUsingSelector:"
+ "string"
+ "stringByPaddingToLength:withString:startingAtIndex:"
+ "stringByReplacingOccurrencesOfString:withString:"
+ "success"
+ "tailspinReportingThresholdSec"
+ "timeIntervalSince1970"
+ "true"
+ "v24@?0@\"NSObject<OS_xpc_object>\"8@\"NSError\"16"
+ "v32@0:8@16@?24"
+ "v32@?0@8@16^B24"
+ "{\n"
+ "\xf0\xf0Q!V!"
- "\n%-20s %5s %15s %10s %10s %10s\n"
- "%-20s %5d %15s %10s\n"
- "%-20s %5d %15s %10s %10s %10s\n"
- "@32@0:8^{?=II[8{hangEvent=QQdAiCCCC^{_opaque_pthread_t}Qi[64c][256c]B^?}][10{HTAssertionInfo=QQQQ[64c]B}]iQ}16Q24"
- "Found %zu hang intervals in last 24 hours which took %@\n"
- "SELECT bundleID, sum(duration) FROM (     SELECT *, end_timestamp-start_timestamp AS duration FROM     (         SELECT bundleID,            CASE WHEN starting=1 THEN eventTimestamp ELSE NULL END AS start_timestamp,            CASE WHEN next_starting=0 THEN next_timestamp                  WHEN starting==0 AND previous_starting==0 THEN next_timestamp ELSE NULL END AS end_timestamp         FROM         (             SELECT bundleID, starting, eventTimestamp, lead(eventTimestamp) OVER win AS next_timestamp, lead(starting) OVER win AS next_starting, lag(starting) OVER win AS previous_starting FROM                 \"App.InFocus\"                 where eventTimestamp > unixepoch(\"now\", \"-%d hours\")                 WINDOW win AS (PARTITION BY bundleID ORDER BY eventTimestamp)         )     ) WHERE         start_timestamp IS NOT NULL OR end_timestamp IS NOT NULL     ORDER BY start_timestamp ) GROUP BY bundleID ORDER BY sum(duration) DESC "
- "T^{?=II[8{hangEvent=QQdAiCCCC^{_opaque_pthread_t}Qi[64c][256c]B^?}][10{HTAssertionInfo=QQQQ[64c]B}]iQ},R,V_shmem_region"
- "Tf,N,V_foregroundDurationHours"
- "^{?=II[8{hangEvent=QQdAiCCCC^{_opaque_pthread_t}Qi[64c][256c]B^?}][10{HTAssertionInfo=QQQQ[64c]B}]iQ}"
- "^{?=II[8{hangEvent=QQdAiCCCC^{_opaque_pthread_t}Qi[64c][256c]B^?}][10{HTAssertionInfo=QQQQ[64c]B}]iQ}16@0:8"
- "_foregroundDurationHours"
- "dateWithTimeIntervalSinceNow:"
- "foregroundDurationHours"
- "setForegroundDurationHours:"
- "\xf0\xf0A!&!"

```
