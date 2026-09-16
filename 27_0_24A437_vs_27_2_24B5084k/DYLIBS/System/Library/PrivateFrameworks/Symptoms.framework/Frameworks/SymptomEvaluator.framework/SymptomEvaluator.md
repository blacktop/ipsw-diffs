## SymptomEvaluator

> `/System/Library/PrivateFrameworks/Symptoms.framework/Frameworks/SymptomEvaluator.framework/SymptomEvaluator`

```diff

-2394.0.4.0.0
-  __TEXT.__text: 0x299a4c
-  __TEXT.__objc_methlist: 0x18cf8
-  __TEXT.__cstring: 0x27970
-  __TEXT.__const: 0x1268
-  __TEXT.__oslogstring: 0x47eb5
-  __TEXT.__gcc_except_tab: 0x52c8
+2394.40.15.0.0
+  __TEXT.__text: 0x29ce68
+  __TEXT.__objc_methlist: 0x18ee0
+  __TEXT.__cstring: 0x27c00
+  __TEXT.__const: 0x12f8
+  __TEXT.__oslogstring: 0x47fc5
+  __TEXT.__gcc_except_tab: 0x5378
   __TEXT.__dlopen_cstrs: 0x56
   __TEXT.__swift5_typeref: 0x38d
   __TEXT.__swift5_capture: 0x518

   __TEXT.__swift_as_cont: 0x78
   __TEXT.evaluator_cfg: 0x6532
   __TEXT.default_clp: 0x2fe0
-  __TEXT.symptoms_clp: 0x6000
+  __TEXT.symptoms_clp: 0x6010
   __TEXT.network_clp: 0x4bb0
   __TEXT.baseband_clp: 0xed50
   __TEXT.bb_MAV_clp: 0x89e0
   __TEXT.bb_INT_clp: 0x6d20
   __TEXT.modules_clp: 0x16e0
-  __TEXT.__unwind_info: 0x92e0
+  __TEXT.__unwind_info: 0x93b8
   __TEXT.__eh_frame: 0x7d8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x7058
-  __DATA_CONST.__objc_classlist: 0x8b8
+  __DATA_CONST.__const: 0x70e8
+  __DATA_CONST.__objc_classlist: 0x8c0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x1c0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0xd548
+  __DATA_CONST.__objc_selrefs: 0xd750
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0x5d8
+  __DATA_CONST.__objc_superrefs: 0x5e8
   __DATA_CONST.__objc_arraydata: 0x980
-  __DATA_CONST.__got: 0x10c0
-  __AUTH_CONST.__const: 0x3230
-  __AUTH_CONST.__cfstring: 0x1f560
-  __AUTH_CONST.__objc_const: 0x41b80
+  __DATA_CONST.__got: 0x10e8
+  __AUTH_CONST.__const: 0x3250
+  __AUTH_CONST.__cfstring: 0x1fbc0
+  __AUTH_CONST.__objc_const: 0x42298
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_arrayobj: 0x1c8
   __AUTH_CONST.__objc_dictobj: 0xa00
   __AUTH_CONST.__objc_intobj: 0x9f0
   __AUTH_CONST.__objc_doubleobj: 0x50
   __AUTH_CONST.__objc_floatobj: 0x30
-  __AUTH_CONST.__auth_got: 0x1790
-  __AUTH.__objc_data: 0x11c8
+  __AUTH_CONST.__auth_got: 0x17c8
+  __AUTH.__objc_data: 0x1268
   __AUTH.__data: 0xc8
-  __DATA.__objc_ivar: 0x31b8
+  __DATA.__objc_ivar: 0x31f4
   __DATA.__data: 0x1f20
   __DATA.__crash_info: 0x148
   __DATA.__common: 0xa8
-  __DATA_DIRTY.__objc_data: 0x4588
+  __DATA_DIRTY.__objc_data: 0x4538
   __DATA_DIRTY.__data: 0x1f0
-  __DATA_DIRTY.__bss: 0x18d0
+  __DATA_DIRTY.__bss: 0x1800
   __DATA_DIRTY.__common: 0x1a8
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreData.framework/CoreData

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 12241
-  Symbols:   25126
-  CStrings:  12231
+  Functions: 12302
+  Symbols:   25255
+  CStrings:  12269
 
Symbols:
+ -[CellFallbackHandler _dataStallRefreshSecsForTesting]
+ -[CellFallbackHandler _polledScoreSampleCountForTesting]
+ -[CellFallbackHandler _registerPolledFlowObserver]
+ -[CellFallbackHandler _setDataStallHandlerForTesting:]
+ -[CellFallbackHandler _setDataStallRefreshSecsForTesting:]
+ -[CellFallbackHandler _setDataStallTimeSecsForTesting:]
+ -[CellFallbackHandler _unregisterPolledFlowObserver]
+ -[NWActivityHandler openTelemetryExporter]
+ -[NWActivityHandler setOpenTelemetryExporter:]
+ -[OpenTelemetryExporter .cxx_destruct]
+ -[OpenTelemetryExporter URLSession:didReceiveChallenge:completionHandler:]
+ -[OpenTelemetryExporter _enqueueSpanBytes:serviceName:]
+ -[OpenTelemetryExporter _flushPendingSpans]
+ -[OpenTelemetryExporter _lookupTraceIDForActivityUUID:]
+ -[OpenTelemetryExporter _resolveTraceIDForActivityUUID:parent:]
+ -[OpenTelemetryExporter _sendPayload:retryCount:]
+ -[OpenTelemetryExporter activityTraceIDCache]
+ -[OpenTelemetryExporter clientAttributesCache]
+ -[OpenTelemetryExporter collectorURL]
+ -[OpenTelemetryExporter consecutiveFailures]
+ -[OpenTelemetryExporter dealloc]
+ -[OpenTelemetryExporter exportActivityEpilogue:externalUUID:externalParentUUID:]
+ -[OpenTelemetryExporter exportActivityStart:externalUUID:externalParentUUID:]
+ -[OpenTelemetryExporter exportFragmentWithUUID:fragmentType:attributes:]
+ -[OpenTelemetryExporter exportQueue]
+ -[OpenTelemetryExporter flushTimerSuspended]
+ -[OpenTelemetryExporter flushTimer]
+ -[OpenTelemetryExporter flush]
+ -[OpenTelemetryExporter grpcCollectorURL]
+ -[OpenTelemetryExporter initWithCollectorURL:teamKey:]
+ -[OpenTelemetryExporter isShutdown]
+ -[OpenTelemetryExporter lastFailureBackoffTime]
+ -[OpenTelemetryExporter pendingSpans]
+ -[OpenTelemetryExporter scopeBytes]
+ -[OpenTelemetryExporter setConsecutiveFailures:]
+ -[OpenTelemetryExporter setFlushTimer:]
+ -[OpenTelemetryExporter setFlushTimerSuspended:]
+ -[OpenTelemetryExporter setIsShutdown:]
+ -[OpenTelemetryExporter setLastFailureBackoffTime:]
+ -[OpenTelemetryExporter setSpanCounter:]
+ -[OpenTelemetryExporter shutdown]
+ -[OpenTelemetryExporter spanCounter]
+ -[OpenTelemetryExporter staticResourceAttributesBytes]
+ -[OpenTelemetryExporter teamKey]
+ -[OpenTelemetryExporter urlSession]
+ -[OpenTelemetryPendingSpan .cxx_destruct]
+ -[OpenTelemetryPendingSpan initWithSpanBytes:serviceName:]
+ -[OpenTelemetryPendingSpan serviceName]
+ -[OpenTelemetryPendingSpan spanBytes]
+ -[SymptomsCAObserver(XCTestFunctions) addDelegateForTesting:]
+ -[SymptomsCAObserver(XCTestFunctions) delegateCountForTesting]
+ GCC_except_table143
+ GCC_except_table52
+ _CC_SHA256_Final
+ _CC_SHA256_Init
+ _CC_SHA256_Update
+ _NSURLAuthenticationMethodServerTrust
+ _OBJC_CLASS_$_NSCache
+ _OBJC_CLASS_$_NSURLComponents
+ _OBJC_CLASS_$_NSURLCredential
+ _OBJC_CLASS_$_OpenTelemetryExporter
+ _OBJC_CLASS_$_OpenTelemetryPendingSpan
+ _OBJC_IVAR_$_CellFallbackHandler.dataStallRefreshPending
+ _OBJC_IVAR_$_NWActivityHandler._openTelemetryExporter
+ _OBJC_IVAR_$_OpenTelemetryExporter._activityTraceIDCache
+ _OBJC_IVAR_$_OpenTelemetryExporter._clientAttributesCache
+ _OBJC_IVAR_$_OpenTelemetryExporter._collectorURL
+ _OBJC_IVAR_$_OpenTelemetryExporter._consecutiveFailures
+ _OBJC_IVAR_$_OpenTelemetryExporter._exportQueue
+ _OBJC_IVAR_$_OpenTelemetryExporter._flushTimer
+ _OBJC_IVAR_$_OpenTelemetryExporter._flushTimerSuspended
+ _OBJC_IVAR_$_OpenTelemetryExporter._grpcCollectorURL
+ _OBJC_IVAR_$_OpenTelemetryExporter._isShutdown
+ _OBJC_IVAR_$_OpenTelemetryExporter._lastFailureBackoffTime
+ _OBJC_IVAR_$_OpenTelemetryExporter._pendingSpans
+ _OBJC_IVAR_$_OpenTelemetryExporter._scopeBytes
+ _OBJC_IVAR_$_OpenTelemetryExporter._spanCounter
+ _OBJC_IVAR_$_OpenTelemetryExporter._staticResourceAttributesBytes
+ _OBJC_IVAR_$_OpenTelemetryExporter._teamKey
+ _OBJC_IVAR_$_OpenTelemetryExporter._urlSession
+ _OBJC_IVAR_$_OpenTelemetryPendingSpan._serviceName
+ _OBJC_IVAR_$_OpenTelemetryPendingSpan._spanBytes
+ _OBJC_METACLASS_$_OpenTelemetryExporter
+ _OBJC_METACLASS_$_OpenTelemetryPendingSpan
+ _SFGetStandardQueue.SFTargetQueueMetrics
+ __NWActivityAnonymizeUUID
+ __OBJC_$_INSTANCE_METHODS_OpenTelemetryExporter
+ __OBJC_$_INSTANCE_METHODS_OpenTelemetryPendingSpan
+ __OBJC_$_INSTANCE_METHODS_SymptomsCAObserver(XCTestFunctions)
+ __OBJC_$_INSTANCE_VARIABLES_OpenTelemetryExporter
+ __OBJC_$_INSTANCE_VARIABLES_OpenTelemetryPendingSpan
+ __OBJC_$_PROP_LIST_OpenTelemetryExporter
+ __OBJC_$_PROP_LIST_OpenTelemetryPendingSpan
+ __OBJC_CLASS_PROTOCOLS_$_OpenTelemetryExporter
+ __OBJC_CLASS_RO_$_OpenTelemetryExporter
+ __OBJC_CLASS_RO_$_OpenTelemetryPendingSpan
+ __OBJC_METACLASS_RO_$_OpenTelemetryExporter
+ __OBJC_METACLASS_RO_$_OpenTelemetryPendingSpan
+ ___30-[OpenTelemetryExporter flush]_block_invoke
+ ___33-[OpenTelemetryExporter shutdown]_block_invoke
+ ___49-[OpenTelemetryExporter _sendPayload:retryCount:]_block_invoke
+ ___49-[OpenTelemetryExporter _sendPayload:retryCount:]_block_invoke_2
+ ___50-[CellFallbackHandler _registerPolledFlowObserver]_block_invoke
+ ___50-[CellFallbackHandler _registerPolledFlowObserver]_block_invoke_2
+ ___54-[OpenTelemetryExporter initWithCollectorURL:teamKey:]_block_invoke
+ ___55-[OpenTelemetryExporter _enqueueSpanBytes:serviceName:]_block_invoke
+ ___61-[SymptomsCAObserver(XCTestFunctions) addDelegateForTesting:]_block_invoke
+ ___62-[SymptomsCAObserver(XCTestFunctions) delegateCountForTesting]_block_invoke
+ ____NWActivityAnonymizeUUID_block_invoke
+ ____deviceModel_block_invoke
+ ____pbAppendAttributesFlattened_block_invoke
+ ___block_descriptor_48_ea8_32s40r_e5_v8?0lr40l8s32l8
+ ___block_descriptor_48_ea8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_52_e8_32s40s_e15_v32?0816^B24ls32l8s40l8
+ ___block_descriptor_56_e8_32w_e5_v8?0lw32l8
+ ___block_descriptor_72_e8_32s40s48s56w_e46_v32?0"NSData"8"NSURLResponse"16"NSError"24ls32l8w56l8s40l8s48l8
+ ___block_descriptor_88_e8_32s40s48s56s64s72w_e5_v8?0lw72l8s32l8s40l8s48l8s56l8s64l8
+ __currentTimeNanos
+ __deviceModel.model
+ __deviceModel.onceToken
+ __pbAppendAttributesFlattened
+ __pbAppendBytesPtr
+ __pbAppendFixed64
+ __pbAppendInt
+ __pbAppendKeyValue
+ __pbAppendMessage
+ __pbAppendString
+ __traceIDBytesFromUUID
+ _nw_activity_set_reporting_strategy
+ _nw_settings_copy_activity_opentelemetry_collector_url
+ _nw_settings_copy_honeycomb_team_key
+ _objc_msgSend$URL
+ _objc_msgSend$_enqueueSpanBytes:serviceName:
+ _objc_msgSend$_flushPendingSpans
+ _objc_msgSend$_lookupTraceIDForActivityUUID:
+ _objc_msgSend$_registerPolledFlowObserver
+ _objc_msgSend$_resolveTraceIDForActivityUUID:parent:
+ _objc_msgSend$_sendPayload:retryCount:
+ _objc_msgSend$_unregisterPolledFlowObserver
+ _objc_msgSend$activityTraceIDCache
+ _objc_msgSend$allHeaderFields
+ _objc_msgSend$authenticationMethod
+ _objc_msgSend$buildPlatform
+ _objc_msgSend$clientAttributesCache
+ _objc_msgSend$clientMetric
+ _objc_msgSend$clientMetricName
+ _objc_msgSend$collectorURL
+ _objc_msgSend$completionReason
+ _objc_msgSend$componentsWithURL:resolvingAgainstBaseURL:
+ _objc_msgSend$consecutiveFailures
+ _objc_msgSend$credentialForTrust:
+ _objc_msgSend$dataForKey:
+ _objc_msgSend$durationMsecs
+ _objc_msgSend$endTimeUnixNano
+ _objc_msgSend$exportActivityEpilogue:externalUUID:externalParentUUID:
+ _objc_msgSend$exportActivityStart:externalUUID:externalParentUUID:
+ _objc_msgSend$exportFragmentWithUUID:fragmentType:attributes:
+ _objc_msgSend$externallyVisibleNwActivity
+ _objc_msgSend$grpcCollectorURL
+ _objc_msgSend$initWithCollectorURL:teamKey:
+ _objc_msgSend$initWithSpanBytes:serviceName:
+ _objc_msgSend$initWithURL:cachePolicy:timeoutInterval:
+ _objc_msgSend$invalidateAndCancel
+ _objc_msgSend$lastFailureBackoffTime
+ _objc_msgSend$objCType
+ _objc_msgSend$observeSetupAssistantFinished
+ _objc_msgSend$openTelemetryExporter
+ _objc_msgSend$pendingSpans
+ _objc_msgSend$productType
+ _objc_msgSend$protectionSpace
+ _objc_msgSend$requireUserNotification
+ _objc_msgSend$scopeBytes
+ _objc_msgSend$serverTrust
+ _objc_msgSend$serviceName
+ _objc_msgSend$setConsecutiveFailures:
+ _objc_msgSend$setCountLimit:
+ _objc_msgSend$setHTTPBody:
+ _objc_msgSend$setHTTPMethod:
+ _objc_msgSend$setLastFailureBackoffTime:
+ _objc_msgSend$setPath:
+ _objc_msgSend$setSpanCounter:
+ _objc_msgSend$setTimeoutIntervalForRequest:
+ _objc_msgSend$setTimeoutIntervalForResource:
+ _objc_msgSend$set_nw_activity:
+ _objc_msgSend$spanBytes
+ _objc_msgSend$spanCounter
+ _objc_msgSend$startTimeUnixNano
+ _objc_msgSend$staticResourceAttributesBytes
+ _objc_msgSend$statusCode
+ _objc_msgSend$teamKey
+ _objc_msgSend$underlyingErrorCode
+ _objc_msgSend$underlyingErrorDomainString
+ _objc_msgSend$urlSession
+ _sUUIDSalt
+ _sUUIDSaltOnce
+ _uname
- -[NWActivityHandler _pruneOldMappings]
- -[NWActivityHandler mappedMetrics]
- -[NWActivityHandler mapperForUUID:reason:]
- -[NWActivityHandler nullUUIDMapper]
- -[NWUUIDMapper .cxx_destruct]
- -[NWUUIDMapper description]
- -[NWUUIDMapper externalUUID]
- -[NWUUIDMapper lastAccessDate]
- -[NWUUIDMapper setExternalUUID:]
- -[NWUUIDMapper setLastAccessDate:]
- -[NWUUIDMapper setUsageFlags:]
- -[NWUUIDMapper usageFlags]
- GCC_except_table57
- GCC_except_table87
- _OBJC_CLASS_$_NWUUIDMapper
- _OBJC_IVAR_$_NWActivityHandler._mappedMetrics
- _OBJC_IVAR_$_NWActivityHandler._nullUUIDMapper
- _OBJC_IVAR_$_NWUUIDMapper._externalUUID
- _OBJC_IVAR_$_NWUUIDMapper._lastAccessDate
- _OBJC_IVAR_$_NWUUIDMapper._usageFlags
- _OBJC_METACLASS_$_NWUUIDMapper
- __OBJC_$_INSTANCE_METHODS_NWUUIDMapper
- __OBJC_$_INSTANCE_METHODS_SymptomsCAObserver
- __OBJC_$_INSTANCE_VARIABLES_NWUUIDMapper
- __OBJC_$_PROP_LIST_NWUUIDMapper
- __OBJC_CLASS_RO_$_NWUUIDMapper
- __OBJC_METACLASS_RO_$_NWUUIDMapper
- ___38-[NWActivityHandler _pruneOldMappings]_block_invoke
- _minAgeAtEviction
- _numEvictionsConnection
- _numEvictionsNWActivity
- _numHitLookupsConnectionFromCFNetworkArray
- _numHitLookupsConnectionFromLibnetcore
- _numHitLookupsNWActivity
- _numHitLookupsNWActivityClientMetric
- _numHitLookupsNWActivityEpilogue
- _numHitLookupsNWActivityEpilogueParent
- _numHitLookupsNWActivityFromCFNetwork
- _numHitLookupsNWActivityFromCellArray
- _numHitLookupsNWActivityFromLibnetcoreArray
- _numHitLookupsNWActivityFromTerminusArray
- _numHitLookupsNWActivityFromWiFiArray
- _numHitLookupsNWActivityParent
- _numMissedLookupsConnectionFromCFNetworkArray
- _numMissedLookupsConnectionFromLibnetcore
- _numMissedLookupsNWActivity
- _numMissedLookupsNWActivityClientMetric
- _numMissedLookupsNWActivityEpilogue
- _numMissedLookupsNWActivityEpilogueParent
- _numMissedLookupsNWActivityFromCFNetwork
- _numMissedLookupsNWActivityFromCellArray
- _numMissedLookupsNWActivityFromLibnetcoreArray
- _numMissedLookupsNWActivityFromTerminusArray
- _numMissedLookupsNWActivityFromWiFiArray
- _numMissedLookupsNWActivityParent
- _numPrunes
- _objc_msgSend$_pruneOldMappings
- _objc_msgSend$externalUUID
- _objc_msgSend$lastAccessDate
- _objc_msgSend$mappedMetrics
- _objc_msgSend$mapperForUUID:reason:
- _objc_msgSend$nullUUIDMapper
- _objc_msgSend$setExternalUUID:
- _objc_msgSend$setLastAccessDate:
- _objc_msgSend$setUsageFlags:
- _objc_msgSend$usageFlags
- _totalAgeAtEviction
CStrings:
+ "%@.%lu"
+ "%lu"
+ "%s:%d (completion %u)"
+ "/opentelemetry.proto.collector.trace.v1.TraceService/Export"
+ "1.0"
+ "ClientAttributes"
+ "Content-Type"
+ "Grpc-Message"
+ "Grpc-Status"
+ "NWACT: OpenTelemetry export disabled: collectorURL=%{public}s teamKey=%{public}s"
+ "NWACT: OpenTelemetry export enabled"
+ "NWACT: failed to anonymize UUID for activity uuid %@"
+ "NWACT: failed to anonymize UUID for activityStats %@"
+ "NWACT: failed to anonymize UUID for client metric %@"
+ "NWACT: failed to anonymize UUID for connection uuid %@"
+ "NWACT: failed to anonymize UUID for epilogue %@"
+ "NWACT: failed to anonymize UUID for parent connection uuid %@"
+ "NWACT: failed to anonymize UUID for session stats %@"
+ "NWActivityUUIDSalt"
+ "No matching delegate entry to unregister for %@"
+ "OpenTelemetry: Dropped %lu pending spans due to overflow (max %lu)"
+ "OpenTelemetry: Export failed (status %ld, grpc-status %{public}@, grpc-message %{public}@, error %@), retrying. Response headers: %{public}@. Response body: %{public}@"
+ "OpenTelemetry: Export failed after retry (status %ld, grpc-status %{public}@, grpc-message %{public}@, error %@), dropping batch. Consecutive failures: %lu. Response headers: %{public}@. Response body: %{public}@"
+ "OpenTelemetry: Export succeeded, resetting failure counter from %lu"
+ "OpenTelemetry: Exporter initialized with collector URL %{public}@"
+ "OpenTelemetry: Retrying after backoff period"
+ "OpenTelemetry: Uploading batch of %lu spans (%lu services) to %{private}@ (protobuf %lu bytes)"
+ "OpenTelemetry: gRPC POST %{private}@ body_bytes=%lu (protobuf=%lu) retry=%lu"
+ "OpenTelemetry: protobuf encoding produced empty payload"
+ "OpenTelemetryExporter.activityTraceIDCache"
+ "OpenTelemetryExporter.clientAttributesCache"
+ "POST"
+ "TE"
+ "application/grpc+proto"
+ "cell.fragment"
+ "client.metric"
+ "com.apple.symptoms.opentelemetry.export"
+ "com.apple.symptoms.standard.metrics.queue"
+ "device.class"
+ "device.internal"
+ "device.model.identifier"
+ "device.product.type"
+ "device.seed_build"
+ "fragment.%u"
+ "grpc-accept-encoding"
+ "grpc-message"
+ "grpc-status"
+ "http.method"
+ "http.status_code"
+ "httpMethod"
+ "identity"
+ "meta.annotation_type"
+ "missing"
+ "nw.activity.%u.%u"
+ "nw.activity.%u.%u.start"
+ "nw.client_metric.name"
+ "nw.fragment.type"
+ "nwConnection.fragment"
+ "nw_activity"
+ "nw_activity_bringup"
+ "os.build"
+ "os.build.platform"
+ "os.name"
+ "os.version"
+ "service.name"
+ "span.name"
+ "span_event"
+ "statusCode"
+ "taskMetrics.fragment"
+ "terminus.fragment"
+ "trailers"
+ "wifi.fragment"
+ "x-honeycomb-team"
- " client-metric"
- " conn-cfnet"
- " conn-libnetcore"
- " null-uuid"
- " nw-activity"
- " nw-cell"
- " nw-cfnet"
- " nw-epi-parent"
- " nw-epilogue"
- " nw-libnetcore"
- " nw-parent"
- " nw-wifi"
- "<private>"
- "NWACT Cache hits Activity %lld (parent %lld) Epilogue %lld (parent %lld)"
- "NWACT Cache hits CFNet activity %lld CFNet connection %lld  NWConnection activity %lld NWConnection connection %lld"
- "NWACT Cache hits Cell activity %lld"
- "NWACT Cache hits WiFi activity %lld"
- "NWACT Cache misses Activity %lld (parent %lld) Epilogue %lld (parent %lld)"
- "NWACT Cache misses CFNet activity %lld CFNet connection %lld  NWConnection activity %lld NWConnection connection %lld"
- "NWACT Cache misses Cell activity %lld"
- "NWACT Cache misses WiFi activity %lld"
- "NWACT Cache prunes %lld evictions: connection %lld activity %lld (average age %.3f minimum age %.3f)"
- "NWACT: Add mapper %p to dictionary %@"
- "NWACT: Prune cache, invocation %lld"
- "NWACT: Use null mapper for unknown libnetcore activity uuid"
- "NWACT: mapper for %@ is %@"
- "NWACT: no activity mapper for activity uuid %@"
- "NWACT: no activity mapper for activityStats %@"
- "NWACT: no activity mapper for client metric %@"
- "NWACT: no activity mapper for connection uuid %@"
- "NWACT: no activity mapper for epilogue %@"
- "NWACT: no activity mapper for parent connection uuid %@"
- "NWACT: no activity mapper for session stats %@"
- "NWUUIDMapper at %p external UUID %@ lastAccess %@ %s%s%s%s%s%s%s%s%s%s%s%s"
- "com.apple.symptoms.metrics.queue"
```
