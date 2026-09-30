## NetworkQuality

> `/System/Library/PrivateFrameworks/NetworkQuality.framework/NetworkQuality`

```diff

-194.80.3.0.0
-  __TEXT.__text: 0x19498
-  __TEXT.__auth_stubs: 0xbb0
-  __TEXT.__objc_methlist: 0x1734
-  __TEXT.__const: 0x188
-  __TEXT.__gcc_except_tab: 0x538
-  __TEXT.__cstring: 0x253f
-  __TEXT.__oslogstring: 0x17bf
-  __TEXT.__unwind_info: 0x4e0
-  __TEXT.__objc_classname: 0x344
-  __TEXT.__objc_methname: 0x4028
-  __TEXT.__objc_methtype: 0xcd8
-  __TEXT.__objc_stubs: 0x34c0
-  __DATA_CONST.__got: 0x190
-  __DATA_CONST.__const: 0x5f8
-  __DATA_CONST.__objc_classlist: 0xc8
+194.100.9.0.0
+  __TEXT.__text: 0x21124
+  __TEXT.__auth_stubs: 0xc00
+  __TEXT.__objc_methlist: 0x1c88
+  __TEXT.__const: 0x1a8
+  __TEXT.__gcc_except_tab: 0x718
+  __TEXT.__cstring: 0x2b14
+  __TEXT.__oslogstring: 0x2138
+  __TEXT.__unwind_info: 0x678
+  __TEXT.__objc_classname: 0x375
+  __TEXT.__objc_methname: 0x505a
+  __TEXT.__objc_methtype: 0xd9f
+  __TEXT.__objc_stubs: 0x40a0
+  __DATA_CONST.__got: 0x1e8
+  __DATA_CONST.__const: 0x6f0
+  __DATA_CONST.__objc_classlist: 0xd0
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xf90
+  __DATA_CONST.__objc_selrefs: 0x12a8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0xa0
+  __DATA_CONST.__objc_superrefs: 0xb0
   __DATA_CONST.__objc_arraydata: 0x58
-  __AUTH_CONST.__auth_got: 0x5e8
+  __AUTH_CONST.__auth_got: 0x610
   __AUTH_CONST.__const: 0x80
-  __AUTH_CONST.__cfstring: 0x19e0
-  __AUTH_CONST.__objc_const: 0x37d0
+  __AUTH_CONST.__cfstring: 0x1d60
+  __AUTH_CONST.__objc_const: 0x4378
   __AUTH_CONST.__objc_intobj: 0x1c8
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH.__objc_data: 0x7d0
-  __DATA.__objc_ivar: 0x3cc
+  __AUTH.__objc_data: 0x820
+  __DATA.__objc_ivar: 0x4f8
   __DATA.__data: 0x360
   __DATA.__bss: 0x20
   __DATA.__common: 0x8

   - /System/Library/PrivateFrameworks/Rapport.framework/Rapport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 154CC959-9BD9-308C-8EF1-57D6EA267F91
-  Functions: 567
-  Symbols:   2337
-  CStrings:  1638
+  UUID: 9A629E23-3D6C-31F3-AB4D-B90A8F0A2414
+  Functions: 712
+  Symbols:   2868
+  CStrings:  1949
 
Symbols:
+ -[BodyWriter callCompletionHandlerWithBytesSent:]
+ -[BodyWriter completionHandler]
+ -[BodyWriter init]
+ -[BodyWriter setCompletionHandler:]
+ -[IdleLatencyURLSessionDelegate URLSession:task:didCompleteWithError:].cold.2
+ -[LatencyURLSessionDelegate attemptRecovery:]
+ -[LatencyURLSessionDelegate calculateMaxFailuresAllowed]
+ -[LatencyURLSessionDelegate captureDetailedError:context:recovered:]
+ -[LatencyURLSessionDelegate categorizeError:]
+ -[LatencyURLSessionDelegate categoryString:]
+ -[LatencyURLSessionDelegate clearErrorArrays]
+ -[LatencyURLSessionDelegate collectIdleLatencyMetricsFromTransactionMetrics:atMetricIndex:fromFullMetrics:]
+ -[LatencyURLSessionDelegate connectionErrors]
+ -[LatencyURLSessionDelegate dnsErrors]
+ -[LatencyURLSessionDelegate enrichErrorWithURL:url:]
+ -[LatencyURLSessionDelegate errorDetails]
+ -[LatencyURLSessionDelegate handleNetworkError:]
+ -[LatencyURLSessionDelegate httpErrors]
+ -[LatencyURLSessionDelegate incrementErrorCount:]
+ -[LatencyURLSessionDelegate networkErrors]
+ -[LatencyURLSessionDelegate populateErrorCounts]
+ -[LatencyURLSessionDelegate recoveredErrors]
+ -[LatencyURLSessionDelegate resetMeasurementState]
+ -[NetworkQualityAssessment idleLatencyProbeCompleted:]
+ -[NetworkQualityConfiguration continuousRunMode]
+ -[NetworkQualityConfiguration delegateTrafficBundleIdentifier]
+ -[NetworkQualityConfiguration heartbeatInterval]
+ -[NetworkQualityConfiguration idleLatencyOnly]
+ -[NetworkQualityConfiguration idleLatencyProbeCount]
+ -[NetworkQualityConfiguration loadBearingConnectionTTL]
+ -[NetworkQualityConfiguration maxConcurrentForeignProbes]
+ -[NetworkQualityConfiguration maxConcurrentSelfProbes]
+ -[NetworkQualityConfiguration maxFailurePercentage]
+ -[NetworkQualityConfiguration maxRecoveryAttempts]
+ -[NetworkQualityConfiguration maxRequestTimeout]
+ -[NetworkQualityConfiguration recoveryBackoffSeconds]
+ -[NetworkQualityConfiguration setContinuousRunMode:]
+ -[NetworkQualityConfiguration setDelegateTrafficBundleIdentifier:]
+ -[NetworkQualityConfiguration setHeartbeatInterval:]
+ -[NetworkQualityConfiguration setIdleLatencyOnly:]
+ -[NetworkQualityConfiguration setIdleLatencyProbeCount:]
+ -[NetworkQualityConfiguration setLoadBearingConnectionTTL:]
+ -[NetworkQualityConfiguration setMaxConcurrentForeignProbes:]
+ -[NetworkQualityConfiguration setMaxConcurrentSelfProbes:]
+ -[NetworkQualityConfiguration setMaxFailurePercentage:]
+ -[NetworkQualityConfiguration setMaxRecoveryAttempts:]
+ -[NetworkQualityConfiguration setMaxRequestTimeout:]
+ -[NetworkQualityConfiguration setRecoveryBackoffSeconds:]
+ -[NetworkQualityExecutions completeNWActivity:withError:]
+ -[NetworkQualityExecutions createDefaultNSURLSessionConfiguration].cold.1
+ -[NetworkQualityExecutions isErrorActivityCompleting:]
+ -[NetworkQualityExecutions reportIdleLatencyProbe:]
+ -[NetworkQualityExecutions scheduleHeartbeat]
+ -[NetworkQualityExecutionsResult clearAllMeasurements]
+ -[NetworkQualityExecutionsResult mutableCopyWithZone:]
+ -[NetworkQualityHTTPServer activeConnectionCount]
+ -[NetworkQualityHTTPServer connectionDidEnd]
+ -[NetworkQualityHTTPServer connectionDidEnd].cold.1
+ -[NetworkQualityHTTPServer connectionDidStart]
+ -[NetworkQualityHTTPServer connectionDidStart].cold.1
+ -[NetworkQualityHTTPServer dealloc]
+ -[NetworkQualityHTTPServer setIdleExitHandler:timeout:]
+ -[NetworkQualityHTTPServer startIdleTimer]
+ -[NetworkQualityResult connectionTimeouts]
+ -[NetworkQualityResult dnsErrors]
+ -[NetworkQualityResult downlinkPhaseEnd]
+ -[NetworkQualityResult downlinkPhaseStart]
+ -[NetworkQualityResult errorDetails]
+ -[NetworkQualityResult httpErrors]
+ -[NetworkQualityResult networkErrors]
+ -[NetworkQualityResult recoveredErrors]
+ -[NetworkQualityResult setConnectionTimeouts:]
+ -[NetworkQualityResult setDnsErrors:]
+ -[NetworkQualityResult setDownlinkPhaseEnd:]
+ -[NetworkQualityResult setDownlinkPhaseStart:]
+ -[NetworkQualityResult setErrorDetails:]
+ -[NetworkQualityResult setHttpErrors:]
+ -[NetworkQualityResult setNetworkErrors:]
+ -[NetworkQualityResult setRecoveredErrors:]
+ -[NetworkQualityResult setTotalNetworkErrors:]
+ -[NetworkQualityResult setUplinkPhaseEnd:]
+ -[NetworkQualityResult setUplinkPhaseStart:]
+ -[NetworkQualityResult totalNetworkErrors]
+ -[NetworkQualityResult uplinkPhaseEnd]
+ -[NetworkQualityResult uplinkPhaseStart]
+ -[NetworkQualityServerConfiguration accessLogEnabled]
+ -[NetworkQualityServerConfiguration setAccessLogEnabled:]
+ -[SequentialIdleLatencyURLSessionDelegate URLSession:task:didCompleteWithError:]
+ -[SequentialIdleLatencyURLSessionDelegate URLSession:task:didCompleteWithError:].cold.1
+ -[SequentialIdleLatencyURLSessionDelegate URLSession:task:didFinishCollectingMetrics:]
+ -[SequentialIdleLatencyURLSessionDelegate executeNextProbe]
+ -[SequentialIdleLatencyURLSessionDelegate executeTaskWithRequest:completionHandler:]
+ -[SequentialIdleLatencyURLSessionDelegate initWithConfiguration:testName:queue:testEndpoint:resultsObject:resultsDelegate:tcpKey:tlsKey:reqrespKey:selfKey:]
+ -[ThroughputDelegate attemptRecovery:]
+ -[ThroughputDelegate captureDetailedError:context:recovered:]
+ -[ThroughputDelegate categorizeError:]
+ -[ThroughputDelegate categoryString:]
+ -[ThroughputDelegate checkAndReplaceExpiredSessions]
+ -[ThroughputDelegate checkForNetworkOutage]
+ -[ThroughputDelegate clearErrorArrays]
+ -[ThroughputDelegate connectionErrors]
+ -[ThroughputDelegate dnsErrors]
+ -[ThroughputDelegate enrichErrorWithURL:url:]
+ -[ThroughputDelegate errorDetails]
+ -[ThroughputDelegate handleNetworkError:]
+ -[ThroughputDelegate httpErrors]
+ -[ThroughputDelegate incrementErrorCount:]
+ -[ThroughputDelegate networkErrors]
+ -[ThroughputDelegate populateErrorCounts]
+ -[ThroughputDelegate recoverFromNetworkOutage]
+ -[ThroughputDelegate recoveredErrors]
+ -[ThroughputDelegate streamCount]
+ -[WorkingLatencyURLSessionDelegate cancelWithCompletionHandler:]
+ -[WorkingLatencyURLSessionDelegate checkForResponsivenessOutage]
+ -[WorkingLatencyURLSessionDelegate recoverFromResponsivenessOutage]
+ -[WorkingLatencyURLSessionDelegate resetMeasurementState]
+ -[WorkingLatencyURLSessionDelegate startResponsivenessOutageMonitoring]
+ GCC_except_table10
+ GCC_except_table15
+ GCC_except_table16
+ GCC_except_table2
+ GCC_except_table22
+ GCC_except_table3
+ GCC_except_table31
+ GCC_except_table32
+ GCC_except_table33
+ GCC_except_table35
+ GCC_except_table36
+ GCC_except_table4
+ GCC_except_table45
+ GCC_except_table57
+ GCC_except_table6
+ GCC_except_table70
+ GCC_except_table9
+ _NSRunLoopCommonModes
+ _OBJC_CLASS_$_NSMapTable
+ _OBJC_CLASS_$_NSMutableSet
+ _OBJC_CLASS_$_NSRunLoop
+ _OBJC_CLASS_$_NSTimer
+ _OBJC_CLASS_$_SequentialIdleLatencyURLSessionDelegate
+ _OBJC_IVAR_$_BodyWriter._completionHandler
+ _OBJC_IVAR_$_BodyWriter._totalBytesSent
+ _OBJC_IVAR_$_LatencyURLSessionDelegate._connectionErrors
+ _OBJC_IVAR_$_LatencyURLSessionDelegate._dnsErrors
+ _OBJC_IVAR_$_LatencyURLSessionDelegate._errorDetailsArray
+ _OBJC_IVAR_$_LatencyURLSessionDelegate._failedRequests
+ _OBJC_IVAR_$_LatencyURLSessionDelegate._httpErrors
+ _OBJC_IVAR_$_LatencyURLSessionDelegate._maxFailuresAllowed
+ _OBJC_IVAR_$_LatencyURLSessionDelegate._networkErrorsArray
+ _OBJC_IVAR_$_LatencyURLSessionDelegate._otherErrors
+ _OBJC_IVAR_$_LatencyURLSessionDelegate._probesCompleted
+ _OBJC_IVAR_$_LatencyURLSessionDelegate._recoveredErrors
+ _OBJC_IVAR_$_LatencyURLSessionDelegate._recoveryAttempts
+ _OBJC_IVAR_$_LatencyURLSessionDelegate._sslErrors
+ _OBJC_IVAR_$_LatencyURLSessionDelegate._tasksWithHttpErrors
+ _OBJC_IVAR_$_LatencyURLSessionDelegate._totalProbes
+ _OBJC_IVAR_$_LatencyURLSessionDelegate._totalRequests
+ _OBJC_IVAR_$_NetworkQualityConfiguration._continuousRunMode
+ _OBJC_IVAR_$_NetworkQualityConfiguration._delegateTrafficBundleIdentifier
+ _OBJC_IVAR_$_NetworkQualityConfiguration._heartbeatInterval
+ _OBJC_IVAR_$_NetworkQualityConfiguration._idleLatencyOnly
+ _OBJC_IVAR_$_NetworkQualityConfiguration._idleLatencyProbeCount
+ _OBJC_IVAR_$_NetworkQualityConfiguration._loadBearingConnectionTTL
+ _OBJC_IVAR_$_NetworkQualityConfiguration._maxConcurrentForeignProbes
+ _OBJC_IVAR_$_NetworkQualityConfiguration._maxConcurrentSelfProbes
+ _OBJC_IVAR_$_NetworkQualityConfiguration._maxFailurePercentage
+ _OBJC_IVAR_$_NetworkQualityConfiguration._maxRecoveryAttempts
+ _OBJC_IVAR_$_NetworkQualityConfiguration._maxRequestTimeout
+ _OBJC_IVAR_$_NetworkQualityConfiguration._recoveryBackoffSeconds
+ _OBJC_IVAR_$_NetworkQualityExecutions._cumulativeConnectionErrors
+ _OBJC_IVAR_$_NetworkQualityExecutions._cumulativeDnsErrors
+ _OBJC_IVAR_$_NetworkQualityExecutions._cumulativeErrorDetails
+ _OBJC_IVAR_$_NetworkQualityExecutions._cumulativeHttpErrors
+ _OBJC_IVAR_$_NetworkQualityExecutions._cumulativeNetworkErrors
+ _OBJC_IVAR_$_NetworkQualityExecutions._cumulativeRecoveredErrors
+ _OBJC_IVAR_$_NetworkQualityExecutions._cumulativeTotalErrors
+ _OBJC_IVAR_$_NetworkQualityExecutions._heartbeatScheduled
+ _OBJC_IVAR_$_NetworkQualityHTTPServer._activeConnections
+ _OBJC_IVAR_$_NetworkQualityHTTPServer._idleExitHandler
+ _OBJC_IVAR_$_NetworkQualityHTTPServer._idleTimeout
+ _OBJC_IVAR_$_NetworkQualityHTTPServer._idleTimer
+ _OBJC_IVAR_$_NetworkQualityHTTPServer.accessLogEnabled
+ _OBJC_IVAR_$_NetworkQualityResult._connectionTimeouts
+ _OBJC_IVAR_$_NetworkQualityResult._dnsErrors
+ _OBJC_IVAR_$_NetworkQualityResult._downlinkPhaseEnd
+ _OBJC_IVAR_$_NetworkQualityResult._downlinkPhaseStart
+ _OBJC_IVAR_$_NetworkQualityResult._errorDetails
+ _OBJC_IVAR_$_NetworkQualityResult._httpErrors
+ _OBJC_IVAR_$_NetworkQualityResult._networkErrors
+ _OBJC_IVAR_$_NetworkQualityResult._recoveredErrors
+ _OBJC_IVAR_$_NetworkQualityResult._totalNetworkErrors
+ _OBJC_IVAR_$_NetworkQualityResult._uplinkPhaseEnd
+ _OBJC_IVAR_$_NetworkQualityResult._uplinkPhaseStart
+ _OBJC_IVAR_$_NetworkQualityServerConfiguration._accessLogEnabled
+ _OBJC_IVAR_$_SequentialIdleLatencyURLSessionDelegate._currentProbeIndex
+ _OBJC_IVAR_$_SequentialIdleLatencyURLSessionDelegate._totalProbes
+ _OBJC_IVAR_$_ThroughputDelegate._connectionErrors
+ _OBJC_IVAR_$_ThroughputDelegate._dnsErrors
+ _OBJC_IVAR_$_ThroughputDelegate._errorDetailsArray
+ _OBJC_IVAR_$_ThroughputDelegate._httpErrors
+ _OBJC_IVAR_$_ThroughputDelegate._lastThroughputMeasurement
+ _OBJC_IVAR_$_ThroughputDelegate._networkErrorsArray
+ _OBJC_IVAR_$_ThroughputDelegate._networkOutageDetected
+ _OBJC_IVAR_$_ThroughputDelegate._otherErrors
+ _OBJC_IVAR_$_ThroughputDelegate._outageDetectionTimer
+ _OBJC_IVAR_$_ThroughputDelegate._recoveredErrors
+ _OBJC_IVAR_$_ThroughputDelegate._recoveryAttempts
+ _OBJC_IVAR_$_ThroughputDelegate._sessionCreationTimes
+ _OBJC_IVAR_$_ThroughputDelegate._sslErrors
+ _OBJC_IVAR_$_ThroughputDelegate._taskToSessionMap
+ _OBJC_IVAR_$_ThroughputDelegate._tasksWithHttpErrors
+ _OBJC_IVAR_$_ThroughputDelegate._ttlCheckTimer
+ _OBJC_IVAR_$_WorkingLatencyURLSessionDelegate._lastProbeDataReceived
+ _OBJC_IVAR_$_WorkingLatencyURLSessionDelegate._responsivenessOutageDetected
+ _OBJC_IVAR_$_WorkingLatencyURLSessionDelegate._responsivenessOutageTimer
+ _OBJC_METACLASS_$_SequentialIdleLatencyURLSessionDelegate
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ __OBJC_$_INSTANCE_METHODS_SequentialIdleLatencyURLSessionDelegate
+ __OBJC_$_INSTANCE_VARIABLES_SequentialIdleLatencyURLSessionDelegate
+ __OBJC_$_PROP_LIST_NetworkQualityHTTPServer
+ __OBJC_CLASS_RO_$_SequentialIdleLatencyURLSessionDelegate
+ __OBJC_METACLASS_RO_$_SequentialIdleLatencyURLSessionDelegate
+ ___107-[LatencyURLSessionDelegate collectIdleLatencyMetricsFromTransactionMetrics:atMetricIndex:fromFullMetrics:]_block_invoke
+ ___107-[LatencyURLSessionDelegate collectIdleLatencyMetricsFromTransactionMetrics:atMetricIndex:fromFullMetrics:]_block_invoke_2
+ ___31-[NetworkQualityExecutions run]_block_invoke.105
+ ___31-[NetworkQualityExecutions run]_block_invoke.105.cold.1
+ ___31-[NetworkQualityExecutions run]_block_invoke.106
+ ___31-[NetworkQualityExecutions run]_block_invoke.119
+ ___31-[NetworkQualityExecutions run]_block_invoke.119.cold.1
+ ___31-[NetworkQualityExecutions run]_block_invoke.120
+ ___31-[NetworkQualityExecutions run]_block_invoke.91
+ ___31-[NetworkQualityExecutions run]_block_invoke.91.cold.1
+ ___31-[NetworkQualityExecutions run]_block_invoke.92
+ ___33-[NetworkQualityExecutions drain]_block_invoke.59
+ ___33-[NetworkQualityExecutions drain]_block_invoke.59.cold.1
+ ___33-[NetworkQualityExecutions drain]_block_invoke.63
+ ___33-[NetworkQualityExecutions drain]_block_invoke.63.cold.1
+ ___33-[NetworkQualityExecutions drain]_block_invoke.64
+ ___33-[NetworkQualityExecutions drain]_block_invoke.64.cold.1
+ ___34-[NetworkQualityHTTPServer start:]_block_invoke.22
+ ___40-[NetworkQualityHTTPServer receiveLoop:]_block_invoke.35
+ ___40-[NetworkQualityHTTPServer receiveLoop:]_block_invoke.67
+ ___40-[NetworkQualityHTTPServer receiveLoop:]_block_invoke_2.70
+ ___41-[ThroughputDelegate handleNetworkError:]_block_invoke
+ ___42-[NetworkQualityHTTPServer startIdleTimer]_block_invoke
+ ___45-[NetworkQualityExecutions scheduleHeartbeat]_block_invoke
+ ___48-[LatencyURLSessionDelegate handleNetworkError:]_block_invoke
+ ___50-[ThroughputDelegate addNewThroughputMeasurement:]_block_invoke
+ ___53-[NetworkQualityExecutions runWithCompletionHandler:]_block_invoke.123
+ ___53-[NetworkQualityExecutions runWithCompletionHandler:]_block_invoke.143
+ ___53-[NetworkQualityExecutions runWithCompletionHandler:]_block_invoke.143.cold.1
+ ___54-[NetworkQualityAssessment idleLatencyProbeCompleted:]_block_invoke
+ ___55-[WorkingLatencyURLSessionDelegate scheduleNewTaskSelf]_block_invoke.352
+ ___55-[WorkingLatencyURLSessionDelegate scheduleNewTaskSelf]_block_invoke_2
+ ___56-[NetworkQualityExecutions execDLWithCompletionHandler:]_block_invoke.190
+ ___56-[NetworkQualityExecutions execDLWithCompletionHandler:]_block_invoke.190.cold.1
+ ___56-[NetworkQualityExecutions execULWithCompletionHandler:]_block_invoke.196
+ ___56-[NetworkQualityExecutions execULWithCompletionHandler:]_block_invoke.196.cold.1
+ ___58-[WorkingLatencyURLSessionDelegate scheduleNewTaskForeign]_block_invoke.353
+ ___59-[ThroughputDelegate URLSession:task:didCompleteWithError:]_block_invoke
+ ___62-[NetworkQualityExecutions execParallelWithCompletionHandler:]_block_invoke.203
+ ___62-[NetworkQualityExecutions execParallelWithCompletionHandler:]_block_invoke.203.cold.1
+ ___62-[NetworkQualityExecutions execParallelWithCompletionHandler:]_block_invoke.204
+ ___62-[NetworkQualityExecutions execParallelWithCompletionHandler:]_block_invoke.205
+ ___62-[NetworkQualityExecutions execParallelWithCompletionHandler:]_block_invoke.205.cold.1
+ ___71-[WorkingLatencyURLSessionDelegate startResponsivenessOutageMonitoring]_block_invoke
+ ___81-[ThroughputDelegate executeTaskWithRequest:saturationHandler:completionHandler:]_block_invoke
+ ___86-[SequentialIdleLatencyURLSessionDelegate URLSession:task:didFinishCollectingMetrics:]_block_invoke
+ ___block_descriptor_40_e8_32s_e54_B28?0"NSObject<OS_nw_protocol_definition>"8i16i20B24ls32l8
+ ___block_descriptor_48_e8_32s40s_e34_v20?0i8"NSObject<OS_nw_error>"12ls32l8s40l8
+ ___block_descriptor_48_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_52_e8_32r_e8_v16?0Q8lr32l8
+ ___kCFBooleanTrue
+ ___stdoutp
+ __dispatch_main_q
+ __dispatch_source_type_timer
+ _dispatch_resume
+ _dispatch_source_cancel
+ _dispatch_source_create
+ _dispatch_source_set_event_handler
+ _dispatch_source_set_timer
+ _fflush
+ _objc_msgSend$_sourceApplicationBundleIdentifier
+ _objc_msgSend$accessLogEnabled
+ _objc_msgSend$addTimer:forMode:
+ _objc_msgSend$attemptRecovery:
+ _objc_msgSend$calculateMaxFailuresAllowed
+ _objc_msgSend$callCompletionHandlerWithBytesSent:
+ _objc_msgSend$captureDetailedError:context:recovered:
+ _objc_msgSend$categorizeError:
+ _objc_msgSend$categoryString:
+ _objc_msgSend$checkAndReplaceExpiredSessions
+ _objc_msgSend$checkForNetworkOutage
+ _objc_msgSend$clearAllMeasurements
+ _objc_msgSend$clearErrorArrays
+ _objc_msgSend$collectIdleLatencyMetricsFromTransactionMetrics:atMetricIndex:fromFullMetrics:
+ _objc_msgSend$completeNWActivity:withError:
+ _objc_msgSend$completionHandler
+ _objc_msgSend$connectionDidEnd
+ _objc_msgSend$connectionDidStart
+ _objc_msgSend$connectionErrors
+ _objc_msgSend$connectionTimeouts
+ _objc_msgSend$containsObject:
+ _objc_msgSend$continuousRunMode
+ _objc_msgSend$decodeDoubleForKey:
+ _objc_msgSend$delegateTrafficBundleIdentifier
+ _objc_msgSend$dnsErrors
+ _objc_msgSend$downlinkPhaseEnd
+ _objc_msgSend$downlinkPhaseStart
+ _objc_msgSend$encodeDouble:forKey:
+ _objc_msgSend$enrichErrorWithURL:url:
+ _objc_msgSend$errorDetails
+ _objc_msgSend$executeNextProbe
+ _objc_msgSend$handleNetworkError:
+ _objc_msgSend$heartbeatInterval
+ _objc_msgSend$httpErrors
+ _objc_msgSend$idleLatencyOnly
+ _objc_msgSend$idleLatencyProbeCompleted:
+ _objc_msgSend$idleLatencyProbeCount
+ _objc_msgSend$incrementErrorCount:
+ _objc_msgSend$invalidate
+ _objc_msgSend$isErrorActivityCompleting:
+ _objc_msgSend$loadBearingConnectionTTL
+ _objc_msgSend$mainRunLoop
+ _objc_msgSend$maxConcurrentForeignProbes
+ _objc_msgSend$maxConcurrentSelfProbes
+ _objc_msgSend$maxFailurePercentage
+ _objc_msgSend$maxRecoveryAttempts
+ _objc_msgSend$maxRequestTimeout
+ _objc_msgSend$networkErrors
+ _objc_msgSend$numberWithUnsignedInteger:
+ _objc_msgSend$populateErrorCounts
+ _objc_msgSend$recoverFromNetworkOutage
+ _objc_msgSend$recoverFromResponsivenessOutage
+ _objc_msgSend$recoveredErrors
+ _objc_msgSend$recoveryBackoffSeconds
+ _objc_msgSend$remoteAddress
+ _objc_msgSend$removeAllObjects
+ _objc_msgSend$removeObjectForKey:
+ _objc_msgSend$replaceObjectAtIndex:withObject:
+ _objc_msgSend$reportIdleLatencyProbe:
+ _objc_msgSend$resetMeasurementState
+ _objc_msgSend$scheduleHeartbeat
+ _objc_msgSend$scheduledTimerWithTimeInterval:target:selector:userInfo:repeats:
+ _objc_msgSend$setCompletionHandler:
+ _objc_msgSend$setConnectionTimeouts:
+ _objc_msgSend$setContinuousRunMode:
+ _objc_msgSend$setDelegateTrafficBundleIdentifier:
+ _objc_msgSend$setDnsErrors:
+ _objc_msgSend$setDownlinkPhaseEnd:
+ _objc_msgSend$setDownlinkPhaseStart:
+ _objc_msgSend$setErrorDetails:
+ _objc_msgSend$setHeartbeatInterval:
+ _objc_msgSend$setHttpErrors:
+ _objc_msgSend$setIdleLatencyOnly:
+ _objc_msgSend$setIdleLatencyProbeCount:
+ _objc_msgSend$setLoadBearingConnectionTTL:
+ _objc_msgSend$setMaxConcurrentForeignProbes:
+ _objc_msgSend$setMaxConcurrentSelfProbes:
+ _objc_msgSend$setMaxFailurePercentage:
+ _objc_msgSend$setMaxRecoveryAttempts:
+ _objc_msgSend$setMaxRequestTimeout:
+ _objc_msgSend$setNetworkErrors:
+ _objc_msgSend$setRecoveredErrors:
+ _objc_msgSend$setRecoveryBackoffSeconds:
+ _objc_msgSend$setTotalNetworkErrors:
+ _objc_msgSend$setUplinkPhaseEnd:
+ _objc_msgSend$setUplinkPhaseStart:
+ _objc_msgSend$set_sourceApplicationBundleIdentifier:
+ _objc_msgSend$startIdleTimer
+ _objc_msgSend$startResponsivenessOutageMonitoring
+ _objc_msgSend$streamCount
+ _objc_msgSend$strongToStrongObjectsMapTable
+ _objc_msgSend$totalNetworkErrors
+ _objc_msgSend$uplinkPhaseEnd
+ _objc_msgSend$uplinkPhaseStart
+ _objc_msgSend$userInfo
+ _objc_opt_respondsToSelector
+ _printf
- GCC_except_table0
- GCC_except_table21
- GCC_except_table38
- GCC_except_table40
- GCC_except_table50
- ___31-[NetworkQualityExecutions run]_block_invoke.110
- ___31-[NetworkQualityExecutions run]_block_invoke.110.cold.1
- ___31-[NetworkQualityExecutions run]_block_invoke.111
- ___31-[NetworkQualityExecutions run]_block_invoke.82
- ___31-[NetworkQualityExecutions run]_block_invoke.82.cold.1
- ___31-[NetworkQualityExecutions run]_block_invoke.83
- ___31-[NetworkQualityExecutions run]_block_invoke.96
- ___31-[NetworkQualityExecutions run]_block_invoke.96.cold.1
- ___31-[NetworkQualityExecutions run]_block_invoke.97
- ___33-[NetworkQualityExecutions drain]_block_invoke.51
- ___33-[NetworkQualityExecutions drain]_block_invoke.51.cold.1
- ___33-[NetworkQualityExecutions drain]_block_invoke.55
- ___33-[NetworkQualityExecutions drain]_block_invoke.55.cold.1
- ___33-[NetworkQualityExecutions drain]_block_invoke.56
- ___33-[NetworkQualityExecutions drain]_block_invoke.56.cold.1
- ___34-[NetworkQualityHTTPServer start:]_block_invoke.20
- ___40-[NetworkQualityHTTPServer receiveLoop:]_block_invoke.33
- ___40-[NetworkQualityHTTPServer receiveLoop:]_block_invoke.62
- ___53-[NetworkQualityExecutions runWithCompletionHandler:]_block_invoke.114
- ___53-[NetworkQualityExecutions runWithCompletionHandler:]_block_invoke.134
- ___53-[NetworkQualityExecutions runWithCompletionHandler:]_block_invoke.134.cold.1
- ___55-[WorkingLatencyURLSessionDelegate scheduleNewTaskSelf]_block_invoke.240
- ___56-[NetworkQualityExecutions execDLWithCompletionHandler:]_block_invoke.182
- ___56-[NetworkQualityExecutions execDLWithCompletionHandler:]_block_invoke.182.cold.1
- ___56-[NetworkQualityExecutions execULWithCompletionHandler:]_block_invoke.188
- ___56-[NetworkQualityExecutions execULWithCompletionHandler:]_block_invoke.188.cold.1
- ___58-[WorkingLatencyURLSessionDelegate scheduleNewTaskForeign]_block_invoke.241
- ___62-[NetworkQualityExecutions execParallelWithCompletionHandler:]_block_invoke.195
- ___62-[NetworkQualityExecutions execParallelWithCompletionHandler:]_block_invoke.195.cold.1
- ___62-[NetworkQualityExecutions execParallelWithCompletionHandler:]_block_invoke.196
- ___62-[NetworkQualityExecutions execParallelWithCompletionHandler:]_block_invoke.197
- ___62-[NetworkQualityExecutions execParallelWithCompletionHandler:]_block_invoke.197.cold.1
- ___76-[IdleLatencyURLSessionDelegate URLSession:task:didFinishCollectingMetrics:]_block_invoke
- ___76-[IdleLatencyURLSessionDelegate URLSession:task:didFinishCollectingMetrics:]_block_invoke_2
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
CStrings:
+ "%4d | size: %10zu bytes | %s | %s\n"
+ "%4d | size: %10zu bytes | %s | %s (received)\n"
+ "%4d | size: %10zu bytes | %s | %s (received, incomplete)\n"
+ "%s:%u - Connection ended, active count: %lu"
+ "%s:%u - Connection started, active count: %lu"
+ "%s:%u - Created SequentialIdleLatencyTask %lu/%lu: %@ on session %@"
+ "%s:%u - Downlink phase completed (draining): start=%@, end=%@"
+ "%s:%u - Downlink phase completed: start=%@, end=%@"
+ "%s:%u - Final completion: DL start=%@, DL end=%@, UL start=%@, UL end=%@"
+ "%s:%u - HTTP response status code is %ld on task %@ metrics %@ tMet %@ (failures: %lu/%lu)"
+ "%s:%u - Idle timeout expired, no active connections, calling exit handler"
+ "%s:%u - Initial connection error (failures: %lu/%lu)"
+ "%s:%u - Invalidated responsiveness outage detection timer"
+ "%s:%u - NSURLSessionConfiguration._sourceApplicationBundleIdentifier: %@"
+ "%s:%u - Network outage detected: setting responsiveness to 0 (no probe data)"
+ "%s:%u - Parallel phase completed (draining): DL start=%@, DL end=%@, UL start=%@, UL end=%@"
+ "%s:%u - Responsiveness outage detected: setting responsiveness to 0 (timer-detected outage)"
+ "%s:%u - Sequential load failed with error: %@"
+ "%s:%u - Skipping connection error for task %@ - already counted as HTTP error"
+ "%s:%u - Skipping failed request %lu/%lu (max allowed: %lu)"
+ "%s:%u - Skipping initial connection error %lu/%lu (max allowed: %lu)"
+ "%s:%u - Skipping metrics collection for first idle latency probe"
+ "%s:%u - Skipping metrics collection for first sequential idle latency probe"
+ "%s:%u - Starting idle timer for %.0f seconds"
+ "%s:%u - Uplink phase completed (draining): start=%@, end=%@"
+ "%s:%u - Uplink phase completed: start=%@, end=%@"
+ "%s:%u - [%d] About to create TTL timer with selector checkAndReplaceExpiredSessions"
+ "%s:%u - [%d] FIRST DATA: Starting outage monitoring on first throughput measurement"
+ "%s:%u - [%d] Ignoring HTTP error due to maxFailurePercentage=100: %@"
+ "%s:%u - [%d] Ignoring throughput error due to maxFailurePercentage=100: %@"
+ "%s:%u - [%d] Invalidated TTL checking timer"
+ "%s:%u - [%d] Invalidated outage detection dispatch timer"
+ "%s:%u - [%d] Skipping connection error for task %@ - already counted as HTTP error"
+ "%s:%u - [%d] Started TTL checking timer with interval %.1f seconds"
+ "%s:%u - [%d] Starting outage detection timer due to network error"
+ "%s:%u - [%d] TTL Session %@ exceeded TTL of %ld seconds, replacing"
+ "%s:%u - [%d] TTL check skipped - TTL:%ld, canceled:%d, exitCriteria:%d"
+ "%s:%u - [%d] Throughput error recovered, continuing test"
+ "%s:%u - [Continuous Mode] Attempting recovery for %@ error"
+ "%s:%u - [Continuous Mode] Recovering from %@ error: %@ (attempt %lu/%ld)"
+ "%s:%u - [Staging] Idle-latency-only mode - completing test"
+ "-[IdleLatencyURLSessionDelegate URLSession:task:didFinishCollectingMetrics:]"
+ "-[NetworkQualityExecutions createDefaultNSURLSessionConfiguration]"
+ "-[NetworkQualityExecutions reportingCompletionHandler:]"
+ "-[NetworkQualityHTTPServer connectionDidEnd]"
+ "-[NetworkQualityHTTPServer connectionDidStart]"
+ "-[NetworkQualityHTTPServer startIdleTimer]"
+ "-[NetworkQualityHTTPServer startIdleTimer]_block_invoke"
+ "-[SequentialIdleLatencyURLSessionDelegate URLSession:task:didCompleteWithError:]"
+ "-[SequentialIdleLatencyURLSessionDelegate URLSession:task:didFinishCollectingMetrics:]"
+ "-[SequentialIdleLatencyURLSessionDelegate executeNextProbe]"
+ "-[ThroughputDelegate attemptRecovery:]"
+ "-[ThroughputDelegate cancelWithCompletionHandler:]"
+ "-[ThroughputDelegate checkAndReplaceExpiredSessions]"
+ "-[ThroughputDelegate handleNetworkError:]"
+ "-[WorkingLatencyURLSessionDelegate cancelWithCompletionHandler:]"
+ "@\"NSMapTable\""
+ "@\"NSMutableSet\""
+ "@\"NSObject<OS_dispatch_source>\""
+ "@\"NSTimer\""
+ "@24@0:8Q16"
+ "@?16@0:8"
+ "Connection"
+ "DNS"
+ "Expected HTTP status code 200, got %ld"
+ "HTTP"
+ "HTTP/1.1"
+ "HTTP/2.0"
+ "HTTP/3.0"
+ "Other"
+ "Q24@0:8@16"
+ "SSL"
+ "SequentialIdleLatencyURLSessionDelegate"
+ "T@\"NSArray\",C,V_errorDetails"
+ "T@\"NSArray\",C,V_networkErrors"
+ "T@\"NSDate\",C,V_downlinkPhaseEnd"
+ "T@\"NSDate\",C,V_downlinkPhaseStart"
+ "T@\"NSDate\",C,V_uplinkPhaseEnd"
+ "T@\"NSDate\",C,V_uplinkPhaseStart"
+ "T@\"NSMutableDictionary\",&,N,V_idleLatencyResults"
+ "T@\"NSMutableDictionary\",&,N,V_mutableOtherValues"
+ "T@\"NSMutableDictionary\",&,N,V_mutableURLSessionMetrics"
+ "T@\"NSMutableDictionary\",&,N,V_workingLatencyResults"
+ "T@\"NSNumber\",C,V_connectionTimeouts"
+ "T@\"NSNumber\",C,V_dnsErrors"
+ "T@\"NSNumber\",C,V_httpErrors"
+ "T@\"NSNumber\",C,V_recoveredErrors"
+ "T@\"NSNumber\",C,V_totalNetworkErrors"
+ "T@\"NSString\",&,N,V_delegateTrafficBundleIdentifier"
+ "T@?,C,N,V_completionHandler"
+ "TB,N,V_accessLogEnabled"
+ "TB,V_continuousRunMode"
+ "TB,V_idleLatencyOnly"
+ "Td,V_heartbeatInterval"
+ "Td,V_recoveryBackoffSeconds"
+ "Too many incorrect response status codes (%lu/%lu) on latency measuring connections"
+ "Tq,V_idleLatencyProbeCount"
+ "Tq,V_loadBearingConnectionTTL"
+ "Tq,V_maxConcurrentForeignProbes"
+ "Tq,V_maxConcurrentSelfProbes"
+ "Tq,V_maxFailurePercentage"
+ "Tq,V_maxRecoveryAttempts"
+ "Tq,V_maxRequestTimeout"
+ "Unknown"
+ "_accessLogEnabled"
+ "_activeConnections"
+ "_connectionErrors"
+ "_connectionTimeouts"
+ "_continuousRunMode"
+ "_cumulativeConnectionErrors"
+ "_cumulativeDnsErrors"
+ "_cumulativeErrorDetails"
+ "_cumulativeHttpErrors"
+ "_cumulativeNetworkErrors"
+ "_cumulativeRecoveredErrors"
+ "_cumulativeTotalErrors"
+ "_currentProbeIndex"
+ "_delegateTrafficBundleIdentifier"
+ "_dnsErrors"
+ "_downlinkPhaseEnd"
+ "_downlinkPhaseStart"
+ "_errorDetails"
+ "_errorDetailsArray"
+ "_failedRequests"
+ "_heartbeatInterval"
+ "_heartbeatScheduled"
+ "_httpErrors"
+ "_idleExitHandler"
+ "_idleLatencyOnly"
+ "_idleLatencyProbeCount"
+ "_idleTimeout"
+ "_idleTimer"
+ "_lastProbeDataReceived"
+ "_lastThroughputMeasurement"
+ "_loadBearingConnectionTTL"
+ "_maxConcurrentForeignProbes"
+ "_maxConcurrentSelfProbes"
+ "_maxFailurePercentage"
+ "_maxFailuresAllowed"
+ "_maxRecoveryAttempts"
+ "_maxRequestTimeout"
+ "_networkErrors"
+ "_networkErrorsArray"
+ "_networkOutageDetected"
+ "_otherErrors"
+ "_outageDetectionTimer"
+ "_probesCompleted"
+ "_recoveredErrors"
+ "_recoveryAttempts"
+ "_recoveryBackoffSeconds"
+ "_responsivenessOutageDetected"
+ "_responsivenessOutageTimer"
+ "_sessionCreationTimes"
+ "_sourceApplicationBundleIdentifier"
+ "_sslErrors"
+ "_taskToSessionMap"
+ "_tasksWithHttpErrors"
+ "_totalBytesSent"
+ "_totalNetworkErrors"
+ "_totalProbes"
+ "_totalRequests"
+ "_ttlCheckTimer"
+ "_uplinkPhaseEnd"
+ "_uplinkPhaseStart"
+ "accessLogEnabled"
+ "activeConnectionCount"
+ "addTimer:forMode:"
+ "attemptRecovery:"
+ "calculateMaxFailuresAllowed"
+ "callCompletionHandlerWithBytesSent:"
+ "captureDetailedError:context:recovered:"
+ "categorizeError:"
+ "category"
+ "categoryName"
+ "categoryString:"
+ "checkAndReplaceExpiredSessions"
+ "checkForNetworkOutage"
+ "checkForResponsivenessOutage"
+ "clearAllMeasurements"
+ "clearErrorArrays"
+ "collectIdleLatencyMetricsFromTransactionMetrics:atMetricIndex:fromFullMetrics:"
+ "completeNWActivity:withError:"
+ "connectionDidEnd"
+ "connectionDidStart"
+ "connectionErrors"
+ "connectionTimeouts"
+ "containsObject:"
+ "context"
+ "continuousRunMode"
+ "d"
+ "d16@0:8"
+ "decodeDoubleForKey:"
+ "delegateTrafficBundleIdentifier"
+ "dnsErrors"
+ "downlinkPhaseEnd"
+ "downlinkPhaseStart"
+ "ecn_client_state"
+ "encodeDouble:forKey:"
+ "enrichErrorWithURL:url:"
+ "errorDetails"
+ "executeNextProbe"
+ "failedRequests"
+ "handleNetworkError:"
+ "heartbeatInterval"
+ "httpErrors"
+ "idleLatencyOnly"
+ "idleLatencyProbeCompleted:"
+ "idleLatencyProbeCount"
+ "incrementErrorCount:"
+ "invalidate"
+ "isErrorActivityCompleting:"
+ "l4s_enabled"
+ "loadBearingConnectionTTL"
+ "mainRunLoop"
+ "maxConcurrentForeignProbes"
+ "maxConcurrentSelfProbes"
+ "maxFailurePercentage"
+ "maxRecoveryAttempts"
+ "maxRequestTimeout"
+ "networkErrors"
+ "numberWithUnsignedInteger:"
+ "populateErrorCounts"
+ "probe_number"
+ "recoverFromNetworkOutage"
+ "recoverFromResponsivenessOutage"
+ "recovered"
+ "recoveredErrors"
+ "recoveryBackoffSeconds"
+ "remoteAddress"
+ "removeAllObjects"
+ "removeObjectForKey:"
+ "replaceObjectAtIndex:withObject:"
+ "reportIdleLatencyProbe:"
+ "resetMeasurementState"
+ "scheduleHeartbeat"
+ "scheduledTimerWithTimeInterval:target:selector:userInfo:repeats:"
+ "server_address"
+ "setAccessLogEnabled:"
+ "setCompletionHandler:"
+ "setConnectionTimeouts:"
+ "setContinuousRunMode:"
+ "setDelegateTrafficBundleIdentifier:"
+ "setDnsErrors:"
+ "setDownlinkPhaseEnd:"
+ "setDownlinkPhaseStart:"
+ "setErrorDetails:"
+ "setHeartbeatInterval:"
+ "setHttpErrors:"
+ "setIdleExitHandler:timeout:"
+ "setIdleLatencyOnly:"
+ "setIdleLatencyProbeCount:"
+ "setLoadBearingConnectionTTL:"
+ "setMaxConcurrentForeignProbes:"
+ "setMaxConcurrentSelfProbes:"
+ "setMaxFailurePercentage:"
+ "setMaxRecoveryAttempts:"
+ "setMaxRequestTimeout:"
+ "setNetworkErrors:"
+ "setRecoveredErrors:"
+ "setRecoveryBackoffSeconds:"
+ "setTotalNetworkErrors:"
+ "setUplinkPhaseEnd:"
+ "setUplinkPhaseStart:"
+ "set_sourceApplicationBundleIdentifier:"
+ "startIdleTimer"
+ "startResponsivenessOutageMonitoring"
+ "streamCount"
+ "strongToStrongObjectsMapTable"
+ "totalNetworkErrors"
+ "totalRequests"
+ "uplinkPhaseEnd"
+ "uplinkPhaseStart"
+ "userInfo"
+ "v16@?0Q8"
+ "v24@0:8@\"NSDictionary\"16"
+ "v24@0:8d16"
+ "v32@0:8@?16d24"
+ "v36@0:8@16@24B32"
+ "v36@0:8@16i24@28"
- "%s:%u - This should not happen - response status code is %ld on task %@ metrics %@ tMet %@"
- "7"
- "Incorrect response status code on latency measuring connection"
- "T@\"NSMutableDictionary\",&,V_idleLatencyResults"
- "T@\"NSMutableDictionary\",&,V_mutableOtherValues"
- "T@\"NSMutableDictionary\",&,V_mutableURLSessionMetrics"
- "T@\"NSMutableDictionary\",&,V_workingLatencyResults"

```
