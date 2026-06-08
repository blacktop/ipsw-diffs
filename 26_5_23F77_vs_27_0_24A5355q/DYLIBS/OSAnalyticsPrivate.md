## OSAnalyticsPrivate

> `/System/Library/PrivateFrameworks/OSAnalyticsPrivate.framework/OSAnalyticsPrivate`

```diff

-934.120.2.0.0
-  __TEXT.__text: 0x17748
-  __TEXT.__auth_stubs: 0x970
-  __TEXT.__objc_methlist: 0xec4
-  __TEXT.__const: 0x110
-  __TEXT.__gcc_except_tab: 0xb0
-  __TEXT.__cstring: 0x144d
-  __TEXT.__oslogstring: 0x2381
-  __TEXT.__unwind_info: 0x370
-  __TEXT.__objc_classname: 0x1ec
-  __TEXT.__objc_methname: 0x2f50
-  __TEXT.__objc_methtype: 0x1532
-  __TEXT.__objc_stubs: 0x2700
-  __DATA_CONST.__got: 0x268
-  __DATA_CONST.__const: 0x3c8
-  __DATA_CONST.__objc_classlist: 0x78
+1049.0.0.502.1
+  __TEXT.__text: 0x1a968
+  __TEXT.__objc_methlist: 0x1010
+  __TEXT.__const: 0x132
+  __TEXT.__gcc_except_tab: 0x9c
+  __TEXT.__cstring: 0x15be
+  __TEXT.__oslogstring: 0x28bc
+  __TEXT.__swift5_typeref: 0x41
+  __TEXT.__swift5_capture: 0x10
+  __TEXT.__unwind_info: 0x430
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x470
+  __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x50
+  __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xd00
-  __DATA_CONST.__objc_protorefs: 0x8
+  __DATA_CONST.__objc_selrefs: 0xdd8
+  __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x68
-  __DATA_CONST.__objc_arraydata: 0xf8
-  __AUTH_CONST.__auth_got: 0x4c8
-  __AUTH_CONST.__const: 0x60
-  __AUTH_CONST.__cfstring: 0x2360
-  __AUTH_CONST.__objc_const: 0x26a8
+  __DATA_CONST.__objc_arraydata: 0x118
+  __DATA_CONST.__got: 0x2d8
+  __AUTH_CONST.__const: 0x120
+  __AUTH_CONST.__cfstring: 0x24e0
+  __AUTH_CONST.__objc_const: 0x28d0
   __AUTH_CONST.__objc_intobj: 0xa8
-  __AUTH_CONST.__objc_dictobj: 0x118
+  __AUTH_CONST.__objc_dictobj: 0x168
   __AUTH_CONST.__objc_arrayobj: 0x90
-  __DATA.__objc_ivar: 0x18c
-  __DATA.__data: 0x3c0
-  __DATA.__bss: 0x10
-  __DATA_DIRTY.__objc_data: 0x4b0
+  __AUTH_CONST.__auth_got: 0x758
+  __AUTH.__objc_data: 0x48
+  __DATA.__objc_ivar: 0x198
+  __DATA.__data: 0x478
+  __DATA.__bss: 0x28
+  __DATA_DIRTY.__objc_data: 0x4d8
+  __DATA_DIRTY.__data: 0x28
   __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CrashReporterSupport.framework/CrashReporterSupport
+  - /System/Library/PrivateFrameworks/DiagnosticRequest.framework/DiagnosticRequest
   - /System/Library/PrivateFrameworks/IDS.framework/IDS
+  - /System/Library/PrivateFrameworks/IDSFoundation.framework/IDSFoundation
   - /System/Library/PrivateFrameworks/OSAnalytics.framework/OSAnalytics
   - /System/Library/PrivateFrameworks/RemoteServiceDiscovery.framework/RemoteServiceDiscovery
   - /System/Library/PrivateFrameworks/RemoteXPC.framework/RemoteXPC

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 90548DFB-C438-3BDE-8D9B-6759C624285F
-  Functions: 315
-  Symbols:   1516
-  CStrings:  1540
+  - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswiftos.dylib
+  UUID: 500BC4A1-C4D2-3D6A-829D-5535557256AB
+  Functions: 385
+  Symbols:   1678
+  CStrings:  881
 
Symbols:
+ -[PCCEndpoint setWantsProgress:]
+ -[PCCEndpoint wantsProgress]
+ -[PCCGroupJob initWithID:forTarget:options:].cold.1
+ -[PCCIDSEndpoint service:account:identifier:sentBytes:totalBytes:]
+ -[PCCIDSEndpoint service:account:identifier:sentBytes:totalBytes:].cold.1
+ -[PCCProxiedDevice generateLogList:]
+ -[PCCProxiedDevice isOnDeviceLog:]
+ -[PCCProxiedDevice transferProgress:sentBytes:totalBytes:]
+ -[PCCProxyingDevice handleFile:from:metadata:].cold.3
+ -[PCCProxyingDevice handleFile:from:metadata:].cold.4
+ -[PCCProxyingDevice request:generateTransparencyLogs:]
+ -[PCCProxyingDevice startRequest:message:callerConnection:onComplete:]
+ -[PCCRequest clientConnection]
+ -[PCCRequest filePath]
+ -[PCCRequest setClientConnection:]
+ _DRGetAllLogFileURLs
+ _IDSSendMessageOptionWantsProgress
+ _OBJC_CLASS_$_NSLock
+ _OBJC_CLASS_$_NSXPCConnection
+ _OBJC_CLASS_$_OSAEventPublisher
+ _OBJC_CLASS_$_OS_dispatch_queue
+ _OBJC_IVAR_$_PCCEndpoint._wantsProgress
+ _OBJC_IVAR_$_PCCRequest._clientConnection
+ _OBJC_IVAR_$_PCCRequest._filePath
+ _OBJC_METACLASS_$_OSAEventPublisher
+ __Block_copy
+ __Block_release
+ __CLASS_METHODS_OSAEventPublisher
+ __DATA_OSAEventPublisher
+ __INSTANCE_METHODS_OSAEventPublisher
+ __IVARS_OSAEventPublisher
+ __METACLASS_DATA_OSAEventPublisher
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OSASyncProxyCallbacks
+ __OBJC_$_PROTOCOL_METHOD_TYPES_OSASyncProxyCallbacks
+ __OBJC_$_PROTOCOL_REFS_OSASyncProxyCallbacks
+ __OBJC_LABEL_PROTOCOL_$_OSASyncProxyCallbacks
+ __OBJC_PROTOCOL_$_OSASyncProxyCallbacks
+ __OBJC_PROTOCOL_REFERENCE_$_OSASyncProxyCallbacks
+ __PROPERTIES_OSAEventPublisher
+ ___36-[PCCProxiedDevice generateLogList:]_block_invoke
+ ___36-[PCCProxiedDevice generateLogList:]_block_invoke.174
+ ___39-[PCCProxiedDevice handleMessage:from:]_block_invoke.130
+ ___40-[PCCProxyingDevice handleMessage:from:]_block_invoke
+ ___40-[PCCProxyingDevice handleMessage:from:]_block_invoke.251
+ ___40-[PCCProxyingDevice handleMessage:from:]_block_invoke.251.cold.1
+ ___42-[PCCProxyingDevice finishRequest:result:]_block_invoke.475
+ ___70-[PCCProxyingDevice startRequest:message:callerConnection:onComplete:]_block_invoke
+ ___block_descriptor_32_e17_v16?0"NSError"8l
+ ___block_descriptor_41_e8_32s_e15_v16?0"NSURL"8ls32l8
+ ___block_descriptor_49_e8_32s40s_e15_v16?0"NSURL"8ls32l8s40l8
+ ___block_descriptor_64_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_72_e8_32s40s48s56s64bs_e5_v8?0ls32l8s40l8s48l8s64l8s56l8
+ ___chkstk_darwin
+ ___swift__destructor
+ ___swift_destroy_boxed_opaque_existential_0
+ ___swift_instantiateConcreteTypeFromMangledNameAbstractV2
+ ___swift_instantiateConcreteTypeFromMangledNameV2
+ ___swift_reflection_version
+ __swiftEmptyArrayStorage
+ __swiftEmptySetSingleton
+ __swiftImmortalRefCount
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftCoreFoundation_$_OSAnalyticsPrivate
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftDispatch_$_OSAnalyticsPrivate
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftFoundation_$_OSAnalyticsPrivate
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftObjectiveC_$_OSAnalyticsPrivate
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swiftXPC_$_OSAnalyticsPrivate
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_Builtin_float_$_OSAnalyticsPrivate
+ __swift_FORCE_LOAD_$_swiftos
+ __swift_FORCE_LOAD_$_swiftos_$_OSAnalyticsPrivate
+ __swift_stdlib_malloc_size
+ __swift_stdlib_reportUnimplementedInitializer
+ _block_copy_helper
+ _block_copy_helper.2
+ _block_descriptor
+ _block_descriptor.4
+ _block_destroy_helper
+ _block_destroy_helper.3
+ _bzero
+ _kOSALogOptionProxiedDeviceID
+ _malloc_size
+ _memcpy
+ _memmove
+ _objc_allocWithZone
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$clientConnection
+ _objc_msgSend$currentConnection
+ _objc_msgSend$filePath
+ _objc_msgSend$generateLogList:
+ _objc_msgSend$generateSensorDataLog
+ _objc_msgSend$handleSubscriptionEventWithAction:token:descriptor:
+ _objc_msgSend$initWithStream:
+ _objc_msgSend$initialBarrierReceived
+ _objc_msgSend$isOnDeviceLog:
+ _objc_msgSend$isOnDeviceLogType:
+ _objc_msgSend$lock
+ _objc_msgSend$publisher
+ _objc_msgSend$remoteObjectProxyWithErrorHandler:
+ _objc_msgSend$sendEventToSubscribers:waitForReplies:
+ _objc_msgSend$setClientConnection:
+ _objc_msgSend$setRemoteObjectInterface:
+ _objc_msgSend$setSubscriberTokens:
+ _objc_msgSend$setWantsProgress:
+ _objc_msgSend$setXattrWithName:value:at:
+ _objc_msgSend$startPublisher
+ _objc_msgSend$startRequest:message:callerConnection:onComplete:
+ _objc_msgSend$subscriberTokens
+ _objc_msgSend$tokensLock
+ _objc_msgSend$transferProgress:sentBytes:totalBytes:
+ _objc_msgSend$transferProgressForFilePath:sentBytes:totalBytes:
+ _objc_msgSend$unlock
+ _objc_msgSend$wantsProgress
+ _objc_opt_respondsToSelector
+ _objc_opt_self
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x5
+ _swift_allocObject
+ _swift_beginAccess
+ _swift_bridgeObjectRelease
+ _swift_bridgeObjectRetain
+ _swift_bridgeObjectRetain_n
+ _swift_deallocObject
+ _swift_getObjCClassFromMetadata
+ _swift_getObjCClassMetadata
+ _swift_getObjectType
+ _swift_getTypeByMangledNameInContext2
+ _swift_getTypeByMangledNameInContextInMetadataState2
+ _swift_getWitnessTable
+ _swift_isUniquelyReferenced_nonNull_native
+ _swift_once
+ _swift_release
+ _swift_release_x20
+ _swift_release_x21
+ _swift_release_x23
+ _swift_release_x8
+ _swift_retain
+ _swift_retain_x2
+ _swift_retain_x20
+ _swift_slowAlloc
+ _swift_slowDealloc
+ _swift_unknownObjectRelease
+ _swift_unknownObjectRetain
+ _swift_unknownObjectWeakDestroy
+ _swift_unknownObjectWeakInit
+ _swift_unknownObjectWeakLoadStrong
+ _symbolic Say_____G So17OS_dispatch_queueC8DispatchE10AttributesV
+ _symbolic So17OSAEventPublisherCSgXw
+ _symbolic _____y_____G s11_SetStorageC s6UInt64V
+ _symbolic _____y_____G s23_ContiguousArrayStorageC s5UInt8V
+ _xpc_dictionary_create
+ _xpc_event_publisher_activate
+ _xpc_event_publisher_create
+ _xpc_event_publisher_fire
+ _xpc_event_publisher_fire_with_reply_sync
+ _xpc_event_publisher_set_error_handler
+ _xpc_event_publisher_set_handler
- -[PCCProxyingDevice startRequest:message:onComplete:]
- _OUTLINED_FUNCTION_4
- ___39-[PCCProxiedDevice handleMessage:from:]_block_invoke.125
- ___42-[PCCProxyingDevice finishRequest:result:]_block_invoke.428
- ___53-[PCCProxyingDevice startRequest:message:onComplete:]_block_invoke
- ___block_descriptor_40_e8_32s_e15_v16?0"NSURL"8ls32l8
- ___block_descriptor_64_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s48l8s56l8
- _objc_msgSend$startRequest:message:onComplete:
- _objc_release_x10
CStrings:
+ "/private/var/mobile/Library/Logs/CrashReporter/DiagnosticLogs/sysdiagnose"
+ "Event publisher XPC error: %d"
+ "Event publisher for stream '%s' finished processing all pending subscriber events"
+ "Event publisher for stream '%s' received unknown event '%u'"
+ "Event publisher for stream '%s' registered subscriber with token %llu"
+ "Event publisher for stream '%s' removed subscriber with token %llu"
+ "Event publisher for stream '%s' sent async event to subscriber with token %llu"
+ "Event publisher for stream '%s' sent synchronous event to subscriber with token %llu"
+ "Event publisher timed out after 2 minutes while waiting for initial barrer"
+ "Failed to set proxied device ID xattr on %@"
+ "Including diagnostic pipeline logs in log list"
+ "Including sysdiagnoses in log list"
+ "Initializing event publisher with stream %s"
+ "Not including diagnostic pipeline logs in log list: DRGetAllLogFileURLs unavailable on current platform"
+ "OSAnalyticsPrivate.OSAEventPublisher"
+ "Publishing event to %ld subscribers for stream '%s'"
+ "Q"
+ "Setting %@=%@ xattr on %@"
+ "com.apple.CoreReporting.GenerateSensorDataLog"
+ "generateTransparencyLogs"
+ "includeDPLogs"
+ "includeMetadata"
+ "includeSysdiagnoses"
+ "init()"
+ "jobProgress"
+ "jobProgress: no clientConnection on request %{public}@"
+ "jobProgress: no filePath on request %{public}@ (group transfer?), skipping"
+ "jobProgress: no request found for jobId %{public}@"
+ "none"
+ "onDeviceLog"
+ "progress callback error: %{public}@"
+ "received jobProgress for %{public}@: %lld / %lld"
+ "received request %@ (%@); posting %@ logs"
+ "relaying progress for job %{public}@: %ld / %ld bytes"
+ "sentBytes"
+ "totalBytes"
+ "transfer progress %{public}@: %ld / %ld bytes"
+ "v16@?0@\"NSError\"8"
+ "wantsProgress"
- "#16@0:8"
- "*"
- ".cxx_destruct"
- "@\"<OSASyncProxyHandler>\""
- "@\"IDSService\""
- "@\"NSArray\""
- "@\"NSData\""
- "@\"NSDate\""
- "@\"NSDictionary\""
- "@\"NSError\""
- "@\"NSHTTPURLResponse\""
- "@\"NSMutableArray\""
- "@\"NSMutableData\""
- "@\"NSMutableDictionary\""
- "@\"NSMutableSet\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_dispatch_semaphore>\""
- "@\"NSObject<OS_dispatch_source>\""
- "@\"NSObject<OS_os_transaction>\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSURLSessionDataTask\""
- "@\"OSALog\""
- "@\"OS_remote_device_browser\""
- "@\"OS_xpc_remote_connection\""
- "@\"PCCEndpoint\""
- "@\"PCCGroupJob\""
- "@16@0:8"
- "@20@0:8i16"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@28@0:8@16B24"
- "@28@0:8^{__sFILE=*iiss{__sbuf=*i}i^v^?^?^?^?{__sbuf=*i}^{__sFILEX}i[3C][1C]{__sbuf=*i}iq}16I24"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8@16^@24"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "@40@0:8@16@24^@32"
- "@48@0:8@16@24@32@40"
- "@48@0:8@16@24@32^@40"
- "@56@0:8@16@24@32@40^@48"
- "@72@0:8@16@24@32@40@48@56@64"
- "@?"
- "@?16@0:8"
- "B"
- "B16@0:8"
- "B20@0:8I16"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B32@0:8@\"NSXPCListener\"16@\"NSXPCConnection\"24"
- "B32@0:8@16@24"
- "B32@0:8@16d24"
- "I16@0:8"
- "IDSServiceDelegate"
- "JSONObjectWithData:options:error:"
- "NSCoding"
- "NSObject"
- "NSSecureCoding"
- "NSURLSessionDataDelegate"
- "NSURLSessionDelegate"
- "NSURLSessionTaskDelegate"
- "NSXPCListenerDelegate"
- "OSADeviceRecoveryEnvHelper"
- "OSAEphemeralLog"
- "OSAStreamDeflater"
- "OSASubmissionPolicy"
- "OSASubmitterExtension"
- "OSASyncProxyHandler"
- "OSASyncProxyServices"
- "OverrideMountPathRequest"
- "PCCBridgeEndpoint"
- "PCCEndpoint"
- "PCCExtension"
- "PCCGroupJob"
- "PCCIDSEndpoint"
- "PCCJob"
- "PCCProxiedDevice"
- "PCCProxyingDevice"
- "PCCRequest"
- "Q16@0:8"
- "T#,R"
- "T@\"NSArray\",C,V_internalWhitelist"
- "T@\"NSArray\",R,V_deviceIds"
- "T@\"NSArray\",R,V_sandboxExtensions"
- "T@\"NSDate\",R,V_lastTouch"
- "T@\"NSDictionary\",C,V_launchInfo"
- "T@\"NSDictionary\",R"
- "T@\"NSDictionary\",R,V_metadata"
- "T@\"NSDictionary\",R,V_options"
- "T@\"NSMutableDictionary\",R,V_scanOptions"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",C,V_connectionType"
- "T@\"NSString\",R"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,V_event"
- "T@\"NSString\",R,V_jid"
- "T@\"NSString\",R,V_target"
- "T@\"NSString\",R,V_type"
- "T@,R"
- "T@?,C,V_callback"
- "TB,R"
- "TB,R,V_hasTasking"
- "TB,V_allowUnsignedBlobs"
- "TB,V_capViolation"
- "TB,V_ignoreProxies"
- "TB,V_preserveFiles"
- "TI,V_fileTimeout"
- "TQ,R"
- "Td,V_jobTimeout"
- "Td,V_requestTimeout"
- "UDIDForRemoteDevice:"
- "URLByAppendingPathExtension:"
- "URLSession:dataTask:didBecomeDownloadTask:"
- "URLSession:dataTask:didBecomeStreamTask:"
- "URLSession:dataTask:didReceiveData:"
- "URLSession:dataTask:didReceiveResponse:completionHandler:"
- "URLSession:dataTask:willCacheResponse:completionHandler:"
- "URLSession:didBecomeInvalidWithError:"
- "URLSession:didCreateTask:"
- "URLSession:didReceiveChallenge:completionHandler:"
- "URLSession:task:didCompleteWithError:"
- "URLSession:task:didFinishCollectingMetrics:"
- "URLSession:task:didReceiveChallenge:completionHandler:"
- "URLSession:task:didReceiveInformationalResponse:"
- "URLSession:task:didSendBodyData:totalBytesSent:totalBytesExpectedToSend:"
- "URLSession:task:needNewBodyStream:"
- "URLSession:task:needNewBodyStreamFromOffset:completionHandler:"
- "URLSession:task:willBeginDelayedRequest:completionHandler:"
- "URLSession:task:willPerformHTTPRedirection:newRequest:completionHandler:"
- "URLSession:taskIsWaitingForConnectivity:"
- "URLSessionDidFinishEventsForBackgroundURLSession:"
- "URLWithString:"
- "UTF8String"
- "UUID"
- "UUIDString"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_accumulateKey:value:"
- "_allowOptOutByRouting"
- "_allowUnsignedBlobs"
- "_callback"
- "_capViolation"
- "_connectionType"
- "_consecutive_error_count"
- "_content"
- "_dataTask"
- "_default_template"
- "_delegate"
- "_deviceIds"
- "_device_browser"
- "_dryRun"
- "_endpoint"
- "_errObj"
- "_error_count"
- "_event"
- "_eventQueue"
- "_expiryTimer"
- "_fileTimeout"
- "_groupXferJob"
- "_group_type"
- "_hasTasking"
- "_homeDeviceService"
- "_identifier"
- "_ignoreProxies"
- "_in"
- "_initializationQueue"
- "_internalWhitelist"
- "_interruptedDevices"
- "_jid"
- "_jobByTracker"
- "_jobCount"
- "_jobTimeout"
- "_job_queue"
- "_lastTouch"
- "_last_thoughput_check"
- "_launchInfo"
- "_listeningConnection"
- "_loadPreviousResults"
- "_log_sets"
- "_metadata"
- "_options"
- "_out"
- "_outgoingConnections"
- "_pairedWatchService"
- "_payload"
- "_prefaces"
- "_preserveFiles"
- "_primary_template"
- "_recordRetirement:reason:"
- "_rejected_count"
- "_remoteCRKeys"
- "_remoteDevices"
- "_reqById"
- "_reqByTracker"
- "_requestTimeout"
- "_requestURL"
- "_request_queue"
- "_response"
- "_responseCode"
- "_responseData"
- "_responseError"
- "_responseHeaders"
- "_results"
- "_sandboxExtensions"
- "_scanOptions"
- "_serviceByDevice"
- "_setQueue:"
- "_specific_files"
- "_strm"
- "_submissionSem"
- "_success_count"
- "_sync_proxy_queue"
- "_sync_summary"
- "_target"
- "_tasking_summary"
- "_thoughput_warnings"
- "_total_count"
- "_txn"
- "_type"
- "abort"
- "acceptTaskingFile:forRouting:withId:"
- "acceptTaskingPayload:forRouting:withId:"
- "accounts"
- "ack:result:error:"
- "addDelegate:queue:"
- "addEntriesFromDictionary:"
- "addObject:"
- "addObjectsFromArray:"
- "addRequest:event:type:onComplete:"
- "addSenderToMessage:"
- "addSuiteNamed:"
- "allHeaderFields"
- "allKeys"
- "allValues"
- "allowUnsignedBlobs"
- "appendBytes:length:"
- "appendData:"
- "appleInternal"
- "applyTasking:taskId:fromBlob:"
- "applyTasking:taskId:usingConfig:fromBlob:"
- "array"
- "arrayByAddingObjectsFromArray:"
- "arrayWithArray:"
- "arrayWithCapacity:"
- "arrayWithObjects:count:"
- "assembleMetadataAt:withOptions:"
- "attributesOfItemAtPath:error:"
- "autorelease"
- "boolForKey:"
- "boolValue"
- "buildSubmissionTemplateForConfig:"
- "buildVersion"
- "callback"
- "cancel"
- "cancelCurrentTask"
- "capViolation"
- "cheaterTaskingWithSets:usingConfig:resultsCallback:"
- "class"
- "cleanupRetired:"
- "clientWithIdentifier:"
- "closeFile"
- "closeFileStream"
- "code"
- "compare:options:"
- "componentsJoinedByString:"
- "conformsToProtocol:"
- "connectionForIdentifier:"
- "connectionType"
- "containsObject:"
- "copy"
- "copyDeflatedDataFromStream:withCap:"
- "countByEnumeratingWithState:objects:count:"
- "createRetiredDirectoriesForUser:"
- "d"
- "d16@0:8"
- "data"
- "dataTaskWithRequest:"
- "dataWithContentsOfFile:"
- "dataWithContentsOfURL:options:error:"
- "dataWithJSONObject:options:error:"
- "dataWithPropertyList:format:options:error:"
- "date"
- "dealloc"
- "debugDescription"
- "decodeArrayOfObjectsOfClass:forKey:"
- "defaultManager"
- "defaultSessionConfiguration"
- "deliver:taskingFile:routing:taskId:asMessage:overRSD:"
- "deviceIds"
- "devices"
- "diagnosticResultsEvent:type:result:"
- "dictionary"
- "dictionaryWithContentsOfFile:"
- "dictionaryWithContentsOfURL:error:"
- "dictionaryWithDictionary:"
- "dictionaryWithObjects:forKeys:count:"
- "doWork:"
- "domain"
- "doubleValue"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "endpointToString:"
- "ensureUsablePath:component:options:"
- "enterInterruptedStateFrom:"
- "enumerateKeysAndObjectsUsingBlock:"
- "errorWithDomain:code:userInfo:"
- "exitInterruptedStateFrom:"
- "expire_count"
- "extractAuthenticatedBlob:error:"
- "fastLane"
- "fileExistsAtPath:"
- "fileExistsAtPath:isDirectory:"
- "fileHandleForReadingFromURL:error:"
- "fileModificationDate"
- "fileSystemRepresentation"
- "fileTimeout"
- "fileURLWithPath:"
- "fileURLWithPathComponents:"
- "fileValue"
- "file_count"
- "filepath"
- "finish:target:event:type:result:"
- "finishRequest:result:"
- "finishRequestWithMessage:result:"
- "finishTasksAndInvalidate"
- "firstObject"
- "getAdditionalRequestHeaders"
- "getAvailableTaskingRoutings"
- "getResourceValue:forKey:error:"
- "getUUIDBytes:"
- "getXattrBoolValWithName:at:"
- "getXattrWithName:at:"
- "handleConnection:from:"
- "handleFile:from:metadata:"
- "handleMessage:from:"
- "hasPrefix:"
- "hasTasking"
- "hash"
- "identifier"
- "identifierForRemoteDevice:"
- "identifierForTarget:"
- "ignoreProxies"
- "init"
- "initFromPath:"
- "initWithBytes:length:encoding:"
- "initWithCapacity:"
- "initWithCoder:"
- "initWithData:andMetadata:"
- "initWithEndpoint:"
- "initWithFileDescriptor:closeOnDealloc:"
- "initWithID:forTarget:options:"
- "initWithID:forTarget:options:forFile:"
- "initWithMessage:options:"
- "initWithPath:forRouting:usingConfig:options:error:"
- "initWithSandboxExtensions:"
- "initWithService:"
- "initWithSuiteName:"
- "initWithTemplate:options:"
- "initWithUUIDBytes:"
- "initWithUUIDString:"
- "initiate:transferGroupWithOptions:job:"
- "initiate:transferLog:withOptions:job:"
- "installCATasking:withId:untasked:"
- "intValue"
- "interfaceWithProtocol:"
- "internalWhitelist"
- "isActive"
- "isCloudConnected"
- "isConnected"
- "isDataVaultEnabled"
- "isDefaultPairedDevice"
- "isDeviceNearby:"
- "isEqual:"
- "isEqualToString:"
- "isFilenameReasonable:"
- "isInDeviceRecoveryEnvironment"
- "isKindOfClass:"
- "isLocallyPaired"
- "isMemberOfClass:"
- "isNearby"
- "isProxy"
- "isSupportedRemoteDeviceType:"
- "isWhitelisted:forDomain:"
- "iterateLogsWithOptions:usingBlock:"
- "jid"
- "jobTimeout"
- "job_count"
- "lastPathComponent"
- "lastTouch"
- "latestResults"
- "launchInfo"
- "levelForFactor:withNamespaceName:"
- "listDevices:"
- "listener:shouldAcceptNewConnection:"
- "localizedDescription"
- "locateLog:forRouting:usingConfig:options:error:"
- "logDomain"
- "longLongValue"
- "markFile:withKey:value:"
- "metaData"
- "modelCode"
- "modelIdentifier"
- "moveItemAtPath:toPath:error:"
- "msg_count"
- "mutableCopy"
- "nextFilepath"
- "numberWithBool:"
- "numberWithDouble:"
- "numberWithInt:"
- "numberWithInteger:"
- "numberWithLong:"
- "numberWithLongLong:"
- "numberWithUnsignedInt:"
- "numberWithUnsignedInteger:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "optInApple"
- "osTrain"
- "overrideMountPath"
- "overrideMountPath:"
- "packageLog:forRouting:info:options:"
- "pathComponents"
- "pathDiagnostics"
- "pathExtension"
- "pathSubmission"
- "pathSubmissionDataVault"
- "pathWithComponents:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "persist"
- "postContent:withHeaders:toEndpoint:"
- "prefaceSubmission:withData:usingArchive:andHeaders:"
- "prepConfig:"
- "prepareNext"
- "preserveFiles"
- "primarySubmissionPaths"
- "processJob:forRouting:including:usingConfig:taskings:summarize:additionalRequestHeaders:"
- "processSubmissionJobs:usingConfig:summarize:"
- "productBuildVersion"
- "productVersion"
- "propertyListWithData:options:format:error:"
- "proxyTasking:taskId:usingConfig:fromBlob:"
- "q"
- "readDataOfLength:"
- "received request %@ (%@); posting %@ %lu logs"
- "receivedReport:from:metadata:"
- "recordEvent:with:"
- "recoveryModeReason"
- "registerResult:error:"
- "registerRouting:result:"
- "release"
- "releaseSandboxExtensions"
- "releaseType"
- "remoteDeviceForIdentifier:"
- "removeAllObjects"
- "removeItemAtPath:error:"
- "removeItemAtURL:error:"
- "removeObject:"
- "removeObjectAtIndex:"
- "removeObjectForKey:"
- "removeObjectsForKeys:"
- "rename:"
- "request:logList:"
- "request:logListWithOptions:onComplete:"
- "request:transferGroupWithOptions:onComplete:"
- "request:transferLog:onComplete:"
- "request:transferLog:withOptions:onComplete:"
- "requestProxyMetadata:onComplete:"
- "requestTimeout"
- "requestWithURL:cachePolicy:timeoutInterval:"
- "request_count"
- "respondsToSelector:"
- "resume"
- "retain"
- "retainCount"
- "retire:"
- "runWithDelegate:"
- "sandboxExtensions"
- "scanLogs:from:"
- "scanLogs:from:options:"
- "scanOptions"
- "scanProxies:"
- "self"
- "send:file:metadata:error:"
- "send:message:error:"
- "sendDeviceMetadata:"
- "sendMessage:toDestinations:priority:options:identifier:error:"
- "sendResourceAtURL:metadata:toDestinations:priority:options:identifier:error:"
- "service:account:didReceiveLocalNetworkHandshake:fromID:context:"
- "service:account:identifier:didSendWithSuccess:error:"
- "service:account:identifier:didSendWithSuccess:error:context:"
- "service:account:identifier:fromID:hasBeenDeliveredWithContext:"
- "service:account:identifier:hasBeenDeliveredWithContext:"
- "service:account:identifier:sentBytes:totalBytes:"
- "service:account:incomingData:fromID:context:"
- "service:account:incomingMessage:fromID:"
- "service:account:incomingMessage:fromID:context:"
- "service:account:incomingOpportunisticData:withIdentifier:fromID:context:"
- "service:account:incomingPendingMessageOfType:fromID:context:"
- "service:account:incomingResourceAtURL:fromID:context:"
- "service:account:incomingResourceAtURL:metadata:fromID:context:"
- "service:account:incomingUnhandledProtobuf:fromID:context:"
- "service:account:inviteDroppedForSessionID:fromID:context:error:"
- "service:account:inviteReceivedForSession:fromID:"
- "service:account:inviteReceivedForSession:fromID:withContext:"
- "service:account:inviteReceivedForSession:fromID:withOptions:"
- "service:account:pendingResourceWithMetadata:fromID:acknowledgementBlock:context:"
- "service:account:receivedGroupSessionParticipantDataUpdate:"
- "service:account:receivedGroupSessionParticipantUpdate:"
- "service:account:receivedGroupSessionParticipantUpdate:context:"
- "service:activeAccountsChanged:"
- "service:connectedDevicesChanged:"
- "service:devicesChanged:"
- "service:didCancelMessageWithSuccess:error:identifier:"
- "service:didSendOpportunisticDataWithIdentifier:toIDs:"
- "service:didSwitchActivePairedDevice:acknowledgementBlock:"
- "service:linkedDevicesChanged:"
- "service:nearbyDevicesChanged:"
- "serviceAllowedTrafficClassifiersDidReset:"
- "serviceByDeviceID:"
- "serviceSpaceDidBecomeAvailable:"
- "sessionWithConfiguration:delegate:delegateQueue:"
- "set"
- "setAllowUnsignedBlobs:"
- "setCallback:"
- "setCapViolation:"
- "setConnectionType:"
- "setExportedInterface:"
- "setExportedObject:"
- "setFileTimeout:"
- "setHTTPBody:"
- "setHTTPMethod:"
- "setHTTPShouldHandleCookies:"
- "setIgnoreProxies:"
- "setInternalWhitelist:"
- "setJobTimeout:"
- "setLaunchInfo:"
- "setLength:"
- "setNetworkServiceType:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setPreserveFiles:"
- "setRequestTimeout:"
- "setValue:forHTTPHeaderField:"
- "setValue:forKey:"
- "setWithObject:"
- "set_usesNWLoader:"
- "setupDeviceStateChangeHandler"
- "setupIncomingEventListener"
- "setupOutgoingConnection:"
- "sharedInstance"
- "shouldSubmitRouting:"
- "standardUserDefaults"
- "startRequest:message:onComplete:"
- "startService:"
- "startTimer"
- "stashCrashReporterKeyForIdentifier:"
- "statusCode"
- "stream"
- "stringByAppendingPathComponent:"
- "stringByAppendingPathExtension:"
- "stringByAppendingString:"
- "stringByDeletingLastPathComponent"
- "stringByDeletingPathExtension"
- "stringByReplacingOccurrencesOfString:withString:"
- "stringByStandardizingPath"
- "stringWithFormat:"
- "stringWithUTF8String:"
- "submissionParam:"
- "submissionPathsWithHomeDirectory:withProxies:"
- "submissionsDisabled"
- "submitLogsUsingPolicy:resultsCallback:"
- "submitToUAT"
- "summarizeLog:reason:"
- "superclass"
- "supportsSecureCoding"
- "synchronize:withOptions:"
- "synchronize:withOptions:onComplete:"
- "target"
- "targetAudience"
- "taskingKeyForRouting:withConfig:"
- "taskingNeedsRefreshForRouting:at:"
- "temporaryFileWithPrefix:fd:"
- "timeIntervalSince1970"
- "timeIntervalSinceNow"
- "timeIntervalSinceReferenceDate"
- "uniqueID"
- "up_count"
- "updateProxiedDeviceMetadata:from:"
- "updateTaskingLastSuccessfulRequest:at:"
- "userInfo"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8I16"
- "v24@0:8@\"IDSService\"16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@\"NSURLSession\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?@@\"NSError\">16"
- "v24@0:8d16"
- "v24@0:8r*16"
- "v28@0:8@16B24"
- "v28@0:8B16@\"NSString\"20"
- "v28@0:8B16@20"
- "v32@0:8@\"IDSService\"16@\"NSArray\"24"
- "v32@0:8@\"IDSService\"16@\"NSSet\"24"
- "v32@0:8@\"NSDictionary\"16@\"NSString\"24"
- "v32@0:8@\"NSString\"16@?<v@?@@\"NSError\">24"
- "v32@0:8@\"NSURLSession\"16@\"NSError\"24"
- "v32@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v32@0:8@16d24"
- "v32@0:8@16q24"
- "v36@0:8@\"NSString\"16B24@\"NSError\"28"
- "v36@0:8@16@24i32"
- "v36@0:8@16B24@28"
- "v40@0:8@\"IDSService\"16@\"IDSAccount\"24@\"IDSGroupSessionParticipantUpdate\"32"
- "v40@0:8@\"IDSService\"16@\"IDSDevice\"24@?<v@?>32"
- "v40@0:8@\"IDSService\"16@\"NSString\"24@\"NSArray\"32"
- "v40@0:8@\"NSString\"16@\"NSDictionary\"24@?<v@?@@\"NSError\">32"
- "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@@\"NSError\">32"
- "v40@0:8@\"NSURL\"16@\"NSString\"24@\"NSDictionary\"32"
- "v40@0:8@\"NSURLSession\"16@\"NSURLAuthenticationChallenge\"24@?<v@?q@\"NSURLCredential\">32"
- "v40@0:8@\"NSURLSession\"16@\"NSURLSessionDataTask\"24@\"NSData\"32"
- "v40@0:8@\"NSURLSession\"16@\"NSURLSessionDataTask\"24@\"NSURLSessionDownloadTask\"32"
- "v40@0:8@\"NSURLSession\"16@\"NSURLSessionDataTask\"24@\"NSURLSessionStreamTask\"32"
- "v40@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSError\"32"
- "v40@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSHTTPURLResponse\"32"
- "v40@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSURLSessionTaskMetrics\"32"
- "v40@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@?<v@?@\"NSInputStream\">32"
- "v40@0:8@16@24@32"
- "v40@0:8@16@24@?32"
- "v44@0:8@\"IDSService\"16B24@\"NSError\"28@\"NSString\"36"
- "v44@0:8@16B24@28@36"
- "v48@0:8@\"IDSService\"16@\"IDSAccount\"24@\"IDSGroupSessionParticipantUpdate\"32@\"IDSMessageContext\"40"
- "v48@0:8@\"IDSService\"16@\"IDSAccount\"24@\"IDSSession\"32@\"NSString\"40"
- "v48@0:8@\"IDSService\"16@\"IDSAccount\"24@\"NSString\"32@40"
- "v48@0:8@\"NSString\"16@\"NSString\"24@\"NSDictionary\"32@?<v@?@@\"NSError\">40"
- "v48@0:8@\"NSURLSession\"16@\"NSURLSessionDataTask\"24@\"NSCachedURLResponse\"32@?<v@?@\"NSCachedURLResponse\">40"
- "v48@0:8@\"NSURLSession\"16@\"NSURLSessionDataTask\"24@\"NSURLResponse\"32@?<v@?q>40"
- "v48@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSURLAuthenticationChallenge\"32@?<v@?q@\"NSURLCredential\">40"
- "v48@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSURLRequest\"32@?<v@?q@\"NSURLRequest\">40"
- "v48@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24q32@?<v@?@\"NSInputStream\">40"
- "v48@0:8@16@24@32@40"
- "v48@0:8@16@24@32@?40"
- "v48@0:8@16@24q32@?40"
- "v52@0:8@\"IDSService\"16@\"IDSAccount\"24@\"NSString\"32B40@\"NSError\"44"
- "v52@0:8@\"IDSService\"16@\"IDSAccount\"24B32@\"NSString\"36@\"NSData\"44"
- "v52@0:8@16@24@32B40@44"
- "v52@0:8@16@24B32@36@44"
- "v56@0:8@\"IDSService\"16@\"IDSAccount\"24@\"IDSProtobuf\"32@\"NSString\"40@\"IDSMessageContext\"48"
- "v56@0:8@\"IDSService\"16@\"IDSAccount\"24@\"IDSSession\"32@\"NSString\"40@\"NSData\"48"
- "v56@0:8@\"IDSService\"16@\"IDSAccount\"24@\"IDSSession\"32@\"NSString\"40@\"NSDictionary\"48"
- "v56@0:8@\"IDSService\"16@\"IDSAccount\"24@\"NSData\"32@\"NSString\"40@\"IDSMessageContext\"48"
- "v56@0:8@\"IDSService\"16@\"IDSAccount\"24@\"NSDictionary\"32@\"NSString\"40@\"IDSMessageContext\"48"
- "v56@0:8@\"IDSService\"16@\"IDSAccount\"24@\"NSString\"32@\"NSString\"40@48"
- "v56@0:8@\"IDSService\"16@\"IDSAccount\"24@\"NSString\"32q40q48"
- "v56@0:8@\"IDSService\"16@\"IDSAccount\"24@\"NSURL\"32@\"NSString\"40@\"IDSMessageContext\"48"
- "v56@0:8@\"IDSService\"16@\"IDSAccount\"24q32@\"NSString\"40@\"IDSMessageContext\"48"
- "v56@0:8@\"NSString\"16@\"NSURL\"24@\"NSString\"32@\"NSString\"40B48B52"
- "v56@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSHTTPURLResponse\"32@\"NSURLRequest\"40@?<v@?@\"NSURLRequest\">48"
- "v56@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24q32q40q48"
- "v56@0:8@16@24@32@40@48"
- "v56@0:8@16@24@32@40@?48"
- "v56@0:8@16@24@32@40B48B52"
- "v56@0:8@16@24@32q40q48"
- "v56@0:8@16@24q32@40@48"
- "v56@0:8@16@24q32q40q48"
- "v60@0:8@\"IDSService\"16@\"IDSAccount\"24@\"NSString\"32B40@\"NSError\"44@\"IDSMessageContext\"52"
- "v60@0:8@16@24@32B40@44@52"
- "v64@0:8@\"IDSService\"16@\"IDSAccount\"24@\"NSData\"32@\"NSString\"40@\"NSString\"48@\"IDSMessageContext\"56"
- "v64@0:8@\"IDSService\"16@\"IDSAccount\"24@\"NSDictionary\"32@\"NSString\"40@?<v@?B>48@\"IDSMessageContext\"56"
- "v64@0:8@\"IDSService\"16@\"IDSAccount\"24@\"NSString\"32@\"NSString\"40@\"NSData\"48@\"NSError\"56"
- "v64@0:8@\"IDSService\"16@\"IDSAccount\"24@\"NSURL\"32@\"NSDictionary\"40@\"NSString\"48@\"IDSMessageContext\"56"
- "v64@0:8@16@24@32@40@48@56"
- "v64@0:8@16@24@32@40@?48@56"
- "validateFirstLineAsJSON:"
- "valueForKey:"
- "writeData:error:"
- "writeToFile:atomically:"
- "writeToFile:atomically:encoding:error:"
- "zone"
- "{z_stream_s=\"next_in\"*\"avail_in\"I\"total_in\"Q\"next_out\"*\"avail_out\"I\"total_out\"Q\"msg\"*\"state\"^{internal_state}\"zalloc\"^?\"zfree\"^?\"opaque\"^v\"data_type\"i\"adler\"Q\"reserved\"Q}"

```
