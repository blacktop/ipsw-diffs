## WiFiPolicy

> `/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`

```diff

-751.41.4.0.0
-  __TEXT.__text: 0xa0bc4
-  __TEXT.__auth_stubs: 0x1280
-  __TEXT.__objc_methlist: 0xea34
+753.6.0.0.0
+  __TEXT.__text: 0xab0b4
+  __TEXT.__auth_stubs: 0x15d0
+  __TEXT.__objc_methlist: 0xeecc
   __TEXT.__const: 0x4e8
-  __TEXT.__cstring: 0x16002
-  __TEXT.__gcc_except_tab: 0x104c
-  __TEXT.__oslogstring: 0x4660
+  __TEXT.__cstring: 0x1aa8e
+  __TEXT.__gcc_except_tab: 0x134c
+  __TEXT.__oslogstring: 0x3217
   __TEXT.__dlopen_cstrs: 0x56
-  __TEXT.__unwind_info: 0x1da4
+  __TEXT.__unwind_info: 0x1f34
   __TEXT.__eh_frame: 0x38
-  __TEXT.__objc_classname: 0x11f3
-  __TEXT.__objc_methname: 0x2bcd2
-  __TEXT.__objc_methtype: 0x2e4a
-  __TEXT.__objc_stubs: 0x15880
-  __DATA_CONST.__got: 0x2a0
-  __DATA_CONST.__const: 0x1cd0
-  __DATA_CONST.__objc_classlist: 0x4d0
+  __TEXT.__objc_classname: 0x124f
+  __TEXT.__objc_methname: 0x2c962
+  __TEXT.__objc_methtype: 0x2f6b
+  __TEXT.__objc_stubs: 0x161a0
+  __DATA_CONST.__got: 0x2b0
+  __DATA_CONST.__const: 0x1f88
+  __DATA_CONST.__objc_classlist: 0x4e8
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x22b80
-  __DATA_CONST.__objc_selrefs: 0x8480
+  __DATA_CONST.__objc_const: 0x1ae88
+  __DATA_CONST.__objc_selrefs: 0x8750
   __DATA_CONST.__objc_arraydata: 0xa58
-  __AUTH_CONST.__cfstring: 0x14300
-  __AUTH_CONST.__objc_const: 0x41c0
-  __AUTH_CONST.__objc_intobj: 0x1308
+  __AUTH_CONST.__cfstring: 0x17040
+  __AUTH_CONST.__objc_const: 0x42e0
+  __AUTH_CONST.__objc_intobj: 0x1680
   __AUTH_CONST.__objc_arrayobj: 0x390
-  __AUTH_CONST.__const: 0x260
+  __AUTH_CONST.__const: 0x320
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH_CONST.__auth_got: 0x958
-  __AUTH.__objc_data: 0x870
+  __AUTH_CONST.__auth_got: 0xb00
+  __AUTH.__objc_data: 0x960
   __DATA.__objc_protorefs: 0x20
-  __DATA.__objc_classrefs: 0x6c8
-  __DATA.__objc_superrefs: 0x3e8
-  __DATA.__objc_ivar: 0x1ca4
+  __DATA.__objc_classrefs: 0x6e0
+  __DATA.__objc_superrefs: 0x400
+  __DATA.__objc_ivar: 0x1d70
   __DATA.__data: 0x1a48
-  __DATA.__bss: 0xa
+  __DATA.__bss: 0x40
   __DATA_DIRTY.__objc_data: 0x27b0
   __DATA_DIRTY.__bss: 0x240
   __DATA_DIRTY.__common: 0x20

   - /System/Library/Frameworks/CoreTelephony.framework/CoreTelephony
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
+  - /System/Library/Frameworks/Network.framework/Network
   - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration

   - /System/Library/PrivateFrameworks/SymptomDiagnosticReporter.framework/SymptomDiagnosticReporter
   - /System/Library/PrivateFrameworks/Symptoms.framework/Frameworks/SymptomAnalytics.framework/SymptomAnalytics
   - /System/Library/PrivateFrameworks/Symptoms.framework/Frameworks/SymptomPresentationFeed.framework/SymptomPresentationFeed
+  - /System/Library/PrivateFrameworks/Trial.framework/Trial
+  - /System/Library/PrivateFrameworks/TrialProto.framework/TrialProto
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A8F48FC9-5A92-3E92-8BFC-0B5938B3A2CA
-  Functions: 5383
-  Symbols:   17907
-  CStrings:  14183
+  UUID: 03EBFEE9-1657-37D8-9D84-CEE27031C96B
+  Functions: 5429
+  Symbols:   17886
+  CStrings:  15004
 
Symbols:
+ +[WiFiPolicyNetworkActivityTracing sharedNetworkActivityTracing]
+ -[SiriNWConnection .cxx_destruct]
+ -[SiriNWConnection _cancelOpenTimer]
+ -[SiriNWConnection _closeWithError:]
+ -[SiriNWConnection _configureConnection:]
+ -[SiriNWConnection _getAttemptedEndpoints]
+ -[SiriNWConnection _getNWConnectionWithInitialData:completion:]
+ -[SiriNWConnection _invokeOpenCompletionWithError:]
+ -[SiriNWConnection _queue]
+ -[SiriNWConnection _setParametersForHost:useTLS:initialPayload:]
+ -[SiriNWConnection _setupOpenTimer]
+ -[SiriNWConnection close]
+ -[SiriNWConnection dealloc]
+ -[SiriNWConnection hasActiveConnection]
+ -[SiriNWConnection initWithQueueAndCompletion:reason:callback:]
+ -[SiriNWConnection openConnectionForURL:withConnectionId:initialPayload:completion:]
+ -[SiriNWConnection resolvedHost]
+ -[SiriNWConnection runSiriProbeWithDepth:trafficClass:]
+ -[WFMeasure dispatchSiriTest:trafficClass:]
+ -[WFMeasure dispatchSiriTest:trafficClass:].cold.1
+ -[WFMeasure getApsdSampleTrafficClass]
+ -[WFMeasure getLazyNSStringPreference:exists:]
+ -[WFMeasure getPeriodicSampleTrafficClass]
+ -[WFMeasure getTimeoutSampleTrafficClass]
+ -[WFMeasure initWithType:andReason:prevTestedOptions:andInterfaceName:]
+ -[WFMeasure isApsdTimeout]
+ -[WFMeasure isRetest]
+ -[WFMeasure isSiriTimeout]
+ -[WFMeasure setIsApsdTimeout:]
+ -[WFMeasure setIsRetest:]
+ -[WFMeasure setIsSiriTimeout:]
+ -[WFMeasure setTclass:]
+ -[WFMeasure shouldApsdSampleSiriTCP]
+ -[WFMeasure shouldApsdSampleSiriTLS]
+ -[WFMeasure shouldPeriodicSampleSiriTCP]
+ -[WFMeasure shouldPeriodicSampleSiriTLS]
+ -[WFMeasure shouldTimeoutSampleSiriTCP]
+ -[WFMeasure shouldTimeoutSampleSiriTLS]
+ -[WFMeasure tclass]
+ -[WFMeasureResult copyWithZone:]
+ -[WFMeasureResult dnsServers]
+ -[WFMeasureResult gatewayAddress]
+ -[WFMeasureResult setDnsServers:]
+ -[WFMeasureResult setGatewayAddress:]
+ -[WFMeasureResult setSiriACEResultsValid:]
+ -[WFMeasureResult setSiriACESuccess:]
+ -[WFMeasureResult setSiriTCPResultsValid:]
+ -[WFMeasureResult setSiriTCPSuccess:]
+ -[WFMeasureResult setSiriTLSResultsValid:]
+ -[WFMeasureResult setSiriTLSSuccess:]
+ -[WFMeasureResult setSiriTrafficClass:]
+ -[WFMeasureResult siriACEResultsValid]
+ -[WFMeasureResult siriACESuccess]
+ -[WFMeasureResult siriTCPResultsValid]
+ -[WFMeasureResult siriTCPSuccess]
+ -[WFMeasureResult siriTLSResultsValid]
+ -[WFMeasureResult siriTLSSuccess]
+ -[WFMeasureResult statusForSiriTCP]
+ -[WFMeasureResult statusForSiriTLS]
+ -[WiFiPolicyNetworkActivity .cxx_destruct]
+ -[WiFiPolicyNetworkActivity _cancelActivityTimer]
+ -[WiFiPolicyNetworkActivity _networkActivityAbort]
+ -[WiFiPolicyNetworkActivity _networkActivityRestart]
+ -[WiFiPolicyNetworkActivity _networkActivityState:]
+ -[WiFiPolicyNetworkActivity _startActivityTimer]
+ -[WiFiPolicyNetworkActivity _startMaxActivityLifetime]
+ -[WiFiPolicyNetworkActivity activate]
+ -[WiFiPolicyNetworkActivity addConnection:]
+ -[WiFiPolicyNetworkActivity description]
+ -[WiFiPolicyNetworkActivity getState]
+ -[WiFiPolicyNetworkActivity hasStarted]
+ -[WiFiPolicyNetworkActivity initWithLabel:parent:]
+ -[WiFiPolicyNetworkActivity nwActivityToken]
+ -[WiFiPolicyNetworkActivity nwActivity]
+ -[WiFiPolicyNetworkActivity parentLabel]
+ -[WiFiPolicyNetworkActivity removeConnection:]
+ -[WiFiPolicyNetworkActivity setHasStarted:]
+ -[WiFiPolicyNetworkActivity setQueue:]
+ -[WiFiPolicyNetworkActivity stopWithCompletionReason:withClientMetric:withClientDict:andError:]
+ -[WiFiPolicyNetworkActivityTracing .cxx_destruct]
+ -[WiFiPolicyNetworkActivityTracing _networkActivityActivate:]
+ -[WiFiPolicyNetworkActivityTracing _networkActivityAddNWConnection:toActivityWithLabel:]
+ -[WiFiPolicyNetworkActivityTracing _networkActivityRemoveNWConnection:fromActivityWithLabel:completion:]
+ -[WiFiPolicyNetworkActivityTracing _networkActivityStart:activate:]
+ -[WiFiPolicyNetworkActivityTracing _networkActivityStop:withReason:withClientMetric:withClientDict:andError:]
+ -[WiFiPolicyNetworkActivityTracing _networkActivityTracingCancel]
+ -[WiFiPolicyNetworkActivityTracing currentNetworkActivityTokenWithCompletion:]
+ -[WiFiPolicyNetworkActivityTracing hasActivitiesRunning]
+ -[WiFiPolicyNetworkActivityTracing init]
+ -[WiFiPolicyNetworkActivityTracing networkActivityActivate:]
+ -[WiFiPolicyNetworkActivityTracing networkActivityAddNWConnection:toActivityWithLabel:]
+ -[WiFiPolicyNetworkActivityTracing networkActivityRemoveNWConnection:fromActivityWithLabel:completion:]
+ -[WiFiPolicyNetworkActivityTracing networkActivityStart:activate:]
+ -[WiFiPolicyNetworkActivityTracing networkActivityStop:withReason:withClientMetric:withClientDict:andError:]
+ -[WiFiPolicyNetworkActivityTracing networkActivityTracingCompleteConnectionsActivities]
+ -[WiFiUsageLinkSession addDictionary:withKeysPrefix:toFlatDictionary:]
+ -[WiFiUsageLinkSession getLazyNSNumberPreference:exists:]
+ -[WiFiUsageLinkSession retryLinkTestInOneMinute]
+ GCC_except_table20
+ GCC_except_table206
+ GCC_except_table22
+ GCC_except_table33
+ GCC_except_table41
+ GCC_except_table47
+ GCC_except_table51
+ GCC_except_table55
+ GCC_except_table86
+ _OBJC_CLASS_$_SiriNWConnection
+ _OBJC_CLASS_$_WiFiPolicyNetworkActivity
+ _OBJC_CLASS_$_WiFiPolicyNetworkActivityTracing
+ _OBJC_IVAR_$_SiriNWConnection._activity
+ _OBJC_IVAR_$_SiriNWConnection._attemptedEndpoints
+ _OBJC_IVAR_$_SiriNWConnection._betterPathAvailableNotificationMachTime
+ _OBJC_IVAR_$_SiriNWConnection._connection
+ _OBJC_IVAR_$_SiriNWConnection._connectionId
+ _OBJC_IVAR_$_SiriNWConnection._connectionUnviableTimer
+ _OBJC_IVAR_$_SiriNWConnection._content_context
+ _OBJC_IVAR_$_SiriNWConnection._dateToDisable
+ _OBJC_IVAR_$_SiriNWConnection._endpoint
+ _OBJC_IVAR_$_SiriNWConnection._interfaceIndex
+ _OBJC_IVAR_$_SiriNWConnection._isCanceled
+ _OBJC_IVAR_$_SiriNWConnection._isEstablishing
+ _OBJC_IVAR_$_SiriNWConnection._isReady
+ _OBJC_IVAR_$_SiriNWConnection._mostRecentErrorFromNWConnection
+ _OBJC_IVAR_$_SiriNWConnection._network_traffic_class
+ _OBJC_IVAR_$_SiriNWConnection._openCompletion
+ _OBJC_IVAR_$_SiriNWConnection._openTimer
+ _OBJC_IVAR_$_SiriNWConnection._probeLabel
+ _OBJC_IVAR_$_SiriNWConnection._queue
+ _OBJC_IVAR_$_SiriNWConnection._readWriteCounter
+ _OBJC_IVAR_$_SiriNWConnection._reason
+ _OBJC_IVAR_$_SiriNWConnection._resolvedHost
+ _OBJC_IVAR_$_SiriNWConnection._staleConnectionTimer
+ _OBJC_IVAR_$_SiriNWConnection._url
+ _OBJC_IVAR_$_SiriNWConnection._usingTLS
+ _OBJC_IVAR_$_SiriNWConnection._wfcompletion
+ _OBJC_IVAR_$_WFMeasure._isApsdTimeout
+ _OBJC_IVAR_$_WFMeasure._isRetest
+ _OBJC_IVAR_$_WFMeasure._isSiriTimeout
+ _OBJC_IVAR_$_WFMeasure._tclass
+ _OBJC_IVAR_$_WFMeasureResult._dnsServers
+ _OBJC_IVAR_$_WFMeasureResult._gatewayAddress
+ _OBJC_IVAR_$_WFMeasureResult._siriACEResultsValid
+ _OBJC_IVAR_$_WFMeasureResult._siriACESuccess
+ _OBJC_IVAR_$_WFMeasureResult._siriTCPResultsValid
+ _OBJC_IVAR_$_WFMeasureResult._siriTCPSuccess
+ _OBJC_IVAR_$_WFMeasureResult._siriTLSResultsValid
+ _OBJC_IVAR_$_WFMeasureResult._siriTLSSuccess
+ _OBJC_IVAR_$_WiFiPolicyNetworkActivity._activity
+ _OBJC_IVAR_$_WiFiPolicyNetworkActivity._activityTimer
+ _OBJC_IVAR_$_WiFiPolicyNetworkActivity._connections
+ _OBJC_IVAR_$_WiFiPolicyNetworkActivity._hasStarted
+ _OBJC_IVAR_$_WiFiPolicyNetworkActivity._parentActivity
+ _OBJC_IVAR_$_WiFiPolicyNetworkActivity._parentLabel
+ _OBJC_IVAR_$_WiFiPolicyNetworkActivity._queue
+ _OBJC_IVAR_$_WiFiPolicyNetworkActivity._state
+ _OBJC_IVAR_$_WiFiPolicyNetworkActivityTracing._activities
+ _OBJC_IVAR_$_WiFiPolicyNetworkActivityTracing._connections
+ _OBJC_IVAR_$_WiFiPolicyNetworkActivityTracing._queue
+ _OBJC_IVAR_$_WiFiUsageLinkSession._lastFaultEventHandledOptions
+ _OBJC_IVAR_$_WiFiUsageLinkSession._linkTestResult
+ _OBJC_METACLASS_$_SiriNWConnection
+ _OBJC_METACLASS_$_WiFiPolicyNetworkActivity
+ _OBJC_METACLASS_$_WiFiPolicyNetworkActivityTracing
+ _WiFiFaultHandlingLimitsStringMap
+ _WiFiFaultHandlingLimitsStringMap.onceToken
+ _WiFiUsageFaultReasonStringMap
+ _WiFiUsageFaultReasonStringMap.onceToken
+ __OBJC_$_CLASS_METHODS_WiFiPolicyNetworkActivityTracing
+ __OBJC_$_INSTANCE_METHODS_SiriNWConnection
+ __OBJC_$_INSTANCE_METHODS_WiFiPolicyNetworkActivity
+ __OBJC_$_INSTANCE_METHODS_WiFiPolicyNetworkActivityTracing
+ __OBJC_$_INSTANCE_VARIABLES_SiriNWConnection
+ __OBJC_$_INSTANCE_VARIABLES_WiFiPolicyNetworkActivity
+ __OBJC_$_INSTANCE_VARIABLES_WiFiPolicyNetworkActivityTracing
+ __OBJC_CLASS_PROTOCOLS_$_WFMeasureResult
+ __OBJC_CLASS_RO_$_SiriNWConnection
+ __OBJC_CLASS_RO_$_WiFiPolicyNetworkActivity
+ __OBJC_CLASS_RO_$_WiFiPolicyNetworkActivityTracing
+ __OBJC_METACLASS_RO_$_SiriNWConnection
+ __OBJC_METACLASS_RO_$_WiFiPolicyNetworkActivity
+ __OBJC_METACLASS_RO_$_WiFiPolicyNetworkActivityTracing
+ ___103-[WiFiPolicyNetworkActivityTracing networkActivityRemoveNWConnection:fromActivityWithLabel:completion:]_block_invoke
+ ___104-[WiFiPolicyNetworkActivityTracing _networkActivityRemoveNWConnection:fromActivityWithLabel:completion:]_block_invoke
+ ___108-[WiFiPolicyNetworkActivityTracing networkActivityStop:withReason:withClientMetric:withClientDict:andError:]_block_invoke
+ ___109-[WiFiPolicyNetworkActivityTracing _networkActivityStop:withReason:withClientMetric:withClientDict:andError:]_block_invoke
+ ___24-[WiFiUsageMonitor init]_block_invoke.215
+ ___24-[WiFiUsageMonitor init]_block_invoke.219
+ ___25-[SiriNWConnection close]_block_invoke
+ ___30-[WFMeasure dispatchPingTest:]_block_invoke.394
+ ___30-[WFMeasure dispatchPingTest:]_block_invoke.cold.1
+ ___35-[SiriNWConnection _setupOpenTimer]_block_invoke
+ ___36-[SiriNWConnection _closeWithError:]_block_invoke
+ ___36-[SiriNWConnection _closeWithError:]_block_invoke_2
+ ___36-[SiriNWConnection _closeWithError:]_block_invoke_3
+ ___36-[SiriNWConnection _closeWithError:]_block_invoke_4
+ ___36-[WFLoggerFile startWatchingLogFile]_block_invoke.78
+ ___36-[WFMeasure shouldApsdSampleSiriTCP]_block_invoke
+ ___36-[WFMeasure shouldApsdSampleSiriTCP]_block_invoke_2
+ ___36-[WFMeasure shouldApsdSampleSiriTLS]_block_invoke
+ ___36-[WFMeasure shouldApsdSampleSiriTLS]_block_invoke_2
+ ___36-[WiFiUsageMonitor submitAnalytics:]_block_invoke.598
+ ___38-[WFMeasure getApsdSampleTrafficClass]_block_invoke
+ ___39-[WFMeasure shouldTimeoutSampleSiriTCP]_block_invoke
+ ___39-[WFMeasure shouldTimeoutSampleSiriTCP]_block_invoke_2
+ ___39-[WFMeasure shouldTimeoutSampleSiriTLS]_block_invoke
+ ___39-[WFMeasure shouldTimeoutSampleSiriTLS]_block_invoke_2
+ ___40-[WFMeasure shouldPeriodicSampleSiriTCP]_block_invoke
+ ___40-[WFMeasure shouldPeriodicSampleSiriTCP]_block_invoke_2
+ ___40-[WFMeasure shouldPeriodicSampleSiriTLS]_block_invoke
+ ___40-[WFMeasure shouldPeriodicSampleSiriTLS]_block_invoke_2
+ ___41-[SiriNWConnection _configureConnection:]_block_invoke
+ ___41-[SiriNWConnection _configureConnection:]_block_invoke_2
+ ___41-[SiriNWConnection _configureConnection:]_block_invoke_3
+ ___41-[WFMeasure getTimeoutSampleTrafficClass]_block_invoke
+ ___42-[WFMeasure getPeriodicSampleTrafficClass]_block_invoke
+ ___43-[WFMeasure dispatchSiriTest:trafficClass:]_block_invoke
+ ___43-[WFMeasure dispatchSiriTest:trafficClass:]_block_invoke_2
+ ___43-[WFMeasure dispatchSiriTest:trafficClass:]_block_invoke_3
+ ___43-[WFMeasure dispatchSiriTest:trafficClass:]_block_invoke_4
+ ___43-[WFMeasure dispatchSiriTest:trafficClass:]_block_invoke_5
+ ___43-[WFMeasure dispatchSiriTest:trafficClass:]_block_invoke_6
+ ___43-[WFMeasure dispatchSiriTest:trafficClass:]_block_invoke_7
+ ___43-[WFMeasure dispatchSiriTest:trafficClass:]_block_invoke_8
+ ___48-[WiFiUsageLinkSession retryLinkTestInOneMinute]_block_invoke
+ ___53-[WFTrafficEngManager __registerCallbacksAndActivate]_block_invoke.56
+ ___54-[WiFiPolicyNetworkActivity _startMaxActivityLifetime]_block_invoke
+ ___55-[SiriNWConnection runSiriProbeWithDepth:trafficClass:]_block_invoke
+ ___56-[WFTrafficEngManager __configureRapportDiscoveryClient]_block_invoke.41
+ ___56-[WFTrafficEngManager __configureRapportDiscoveryClient]_block_invoke.46
+ ___56-[WiFiPolicyNetworkActivityTracing hasActivitiesRunning]_block_invoke
+ ___60-[WiFiPolicyNetworkActivityTracing networkActivityActivate:]_block_invoke
+ ___62-[WiFiUsageLinkSession performLinkTestFor:isTriggeredByFault:]_block_invoke.cold.1
+ ___63-[WFBlacklistEngine removeBlacklistedStateWithUnblacklistType:]_block_invoke.110
+ ___64+[WiFiPolicyNetworkActivityTracing sharedNetworkActivityTracing]_block_invoke
+ ___64-[SiriNWConnection _setParametersForHost:useTLS:initialPayload:]_block_invoke
+ ___64-[SiriNWConnection _setParametersForHost:useTLS:initialPayload:]_block_invoke_2
+ ___64-[WFTrafficEngManager __requestCriticalAppInfo:completionBlock:]_block_invoke.72
+ ___64-[WFTrafficEngManager __requestCriticalAppInfo:completionBlock:]_block_invoke.77
+ ___65-[WiFiPolicyNetworkActivityTracing _networkActivityTracingCancel]_block_invoke
+ ___66-[WiFiPolicyNetworkActivityTracing networkActivityStart:activate:]_block_invoke
+ ___69-[WiFiUsageMonitor startMonitoringWiFiInterface:withLinkSessionOnly:]_block_invoke.237
+ ___70-[WiFiUsageLinkSession addDictionary:withKeysPrefix:toFlatDictionary:]_block_invoke
+ ___71-[WFMeasure initWithType:andReason:prevTestedOptions:andInterfaceName:]_block_invoke
+ ___71-[WFMeasure initWithType:andReason:prevTestedOptions:andInterfaceName:]_block_invoke_2
+ ___71-[WFMeasure initWithType:andReason:prevTestedOptions:andInterfaceName:]_block_invoke_3
+ ___71-[WFMeasure initWithType:andReason:prevTestedOptions:andInterfaceName:]_block_invoke_4
+ ___71-[WFMeasure initWithType:andReason:prevTestedOptions:andInterfaceName:]_block_invoke_5
+ ___78-[WiFiPolicyNetworkActivityTracing currentNetworkActivityTokenWithCompletion:]_block_invoke
+ ___84-[SiriNWConnection openConnectionForURL:withConnectionId:initialPayload:completion:]_block_invoke
+ ___84-[SiriNWConnection openConnectionForURL:withConnectionId:initialPayload:completion:]_block_invoke_2
+ ___85-[WiFiUsageMonitor updateKnownNetworksSupportingSeamless:forBSS:andSSID:beaconCache:]_block_invoke.636
+ ___85-[WiFiUsageMonitor updateKnownNetworksSupportingSeamless:forBSS:andSSID:beaconCache:]_block_invoke.692
+ ___87-[WiFiPolicyNetworkActivityTracing networkActivityAddNWConnection:toActivityWithLabel:]_block_invoke
+ ___87-[WiFiPolicyNetworkActivityTracing networkActivityTracingCompleteConnectionsActivities]_block_invoke
+ ___88-[WiFiPolicyNetworkActivityTracing _networkActivityAddNWConnection:toActivityWithLabel:]_block_invoke
+ ___95-[WiFiPolicyNetworkActivity stopWithCompletionReason:withClientMetric:withClientDict:andError:]_block_invoke
+ ___95-[WiFiPolicyNetworkActivity stopWithCompletionReason:withClientMetric:withClientDict:andError:]_block_invoke.cold.1
+ ___98-[WiFiUsageMonitor setScanningState:client:neighborBSS:otherBSS:withChannelInfoList:forInterface:]_block_invoke.555
+ ___WiFiFaultHandlingLimitsStringMap_block_invoke
+ ___WiFiUsageFaultReasonStringMap_block_invoke
+ ___block_descriptor_32_e31_v16?0"NSObject<OS_nw_error>"8l
+ ___block_descriptor_32_e42_v16?0"NSObject<OS_nw_protocol_options>"8l
+ ___block_descriptor_32_e52_v32?0"NSString"8"WiFiPolicyNetworkActivity"16^B24l
+ ___block_descriptor_33_e42_v16?0"NSObject<OS_nw_protocol_options>"8l
+ ___block_descriptor_40_e8_32s_e25_v32?0"NSString"816^B24ls32l8
+ ___block_descriptor_40_e8_32s_e48_v24?0"NSObject<OS_nw_connection>"8"NSError"16ls32l8
+ ___block_descriptor_41_e8_32r_e18_v16?0"NSNumber"8lr32l8
+ ___block_descriptor_48_e8_32s40bs_e17_v16?0"NSError"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e25_v32?0"NSString"816^B24ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e34_v20?0i8"NSObject<OS_nw_error>"12ls32l8s40l8
+ ___block_descriptor_48_e8_32s_e52_v32?0"NSString"8"WiFiPolicyNetworkActivity"16^B24ls32l8
+ ___block_descriptor_49_e8_32s40w_e34_v24?0"NSDictionary"8"NSArray"16lw40l8s32l8
+ ___block_descriptor_49_e8_32s40w_e37_v24?0"NPTMetricResult"8"NSError"16lw40l8s32l8
+ ___block_descriptor_52_e8_32s_e20_v20?0B8"NSError"12ls32l8
+ ___block_descriptor_52_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_64_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_76_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_92_e8_32s40s48s56r64r_e52_v32?0"NSString"8"WiFiPolicyNetworkActivity"16^B24ls32l8s40l8s48l8r56l8r64l8
+ ___block_literal_global.156
+ ___block_literal_global.202
+ ___block_literal_global.218
+ ___block_literal_global.221
+ ___block_literal_global.54
+ ___block_literal_global.639
+ __labelDescription
+ __labelDescription.cold.1
+ __nw_content_context_final_send
+ __nw_parameters_configure_protocol_disable
+ __os_log_fault_impl
+ __unnamed_array_storage.362
+ __unnamed_array_storage.369
+ __unnamed_array_storage.374
+ _class_getProperty
+ _dispatch_queue_attr_make_with_qos_class
+ _gWiFiFaultHandlingLimitsStringMap
+ _gWiFiUsageFaultReasonStringMap
+ _nw_activity_activate
+ _nw_activity_complete_with_reason
+ _nw_activity_complete_with_reason_and_underlying_error
+ _nw_activity_create
+ _nw_activity_get_domain
+ _nw_activity_get_label
+ _nw_activity_get_token
+ _nw_activity_set_parent_activity
+ _nw_activity_submit_metrics
+ _nw_array_get_count
+ _nw_array_get_object_at_index
+ _nw_connection_cancel
+ _nw_connection_copy_attempted_endpoint_array
+ _nw_connection_create
+ _nw_connection_end_activity
+ _nw_connection_get_id
+ _nw_connection_send
+ _nw_connection_set_event_handler
+ _nw_connection_set_queue
+ _nw_connection_set_read_close_handler
+ _nw_connection_set_write_close_handler
+ _nw_connection_start
+ _nw_connection_start_activity
+ _nw_context_create
+ _nw_context_set_isolate_protocol_cache
+ _nw_context_set_isolate_protocol_stack
+ _nw_context_set_privacy_level
+ _nw_context_set_scheduling_mode
+ _nw_endpoint_create_host
+ _nw_endpoint_get_description
+ _nw_error_copy_cf_error
+ _nw_error_get_error_code
+ _nw_error_get_error_domain
+ _nw_parameters_create_secure_tcp
+ _nw_parameters_set_context
+ _nw_parameters_set_data_mode
+ _nw_parameters_set_expired_dns_behavior
+ _nw_parameters_set_indefinite
+ _nw_parameters_set_initial_data_payload
+ _nw_parameters_set_source_application
+ _nw_parameters_set_tfo
+ _nw_parameters_set_tls_session_id
+ _nw_parameters_set_traffic_class
+ _nw_tcp_options_set_no_delay
+ _nw_tls_copy_sec_protocol_options
+ _objc_msgSend$URLWithString:
+ _objc_msgSend$_cancelActivityTimer
+ _objc_msgSend$_cancelOpenTimer
+ _objc_msgSend$_closeWithError:
+ _objc_msgSend$_configureConnection:
+ _objc_msgSend$_getAttemptedEndpoints
+ _objc_msgSend$_getNWConnectionWithInitialData:completion:
+ _objc_msgSend$_invokeOpenCompletionWithError:
+ _objc_msgSend$_networkActivityAbort
+ _objc_msgSend$_networkActivityActivate:
+ _objc_msgSend$_networkActivityAddNWConnection:toActivityWithLabel:
+ _objc_msgSend$_networkActivityRemoveNWConnection:fromActivityWithLabel:completion:
+ _objc_msgSend$_networkActivityRestart
+ _objc_msgSend$_networkActivityStart:activate:
+ _objc_msgSend$_networkActivityState:
+ _objc_msgSend$_networkActivityStop:withReason:withClientMetric:withClientDict:andError:
+ _objc_msgSend$_networkActivityTracingCancel
+ _objc_msgSend$_setParametersForHost:useTLS:initialPayload:
+ _objc_msgSend$_setupOpenTimer
+ _objc_msgSend$_startActivityTimer
+ _objc_msgSend$_startMaxActivityLifetime
+ _objc_msgSend$activate
+ _objc_msgSend$addConnection:
+ _objc_msgSend$addDictionary:withKeysPrefix:toFlatDictionary:
+ _objc_msgSend$backhaulResultsValid
+ _objc_msgSend$dateFromString:
+ _objc_msgSend$dispatchSiriTest:trafficClass:
+ _objc_msgSend$downloadError
+ _objc_msgSend$gatewayResultsValid
+ _objc_msgSend$getState
+ _objc_msgSend$hasActivitiesRunning
+ _objc_msgSend$hasStarted
+ _objc_msgSend$host
+ _objc_msgSend$initWithDomain:code:userInfo:
+ _objc_msgSend$initWithLabel:parent:
+ _objc_msgSend$initWithQueueAndCompletion:reason:callback:
+ _objc_msgSend$initWithType:andReason:prevTestedOptions:andInterfaceName:
+ _objc_msgSend$initWithUUIDBytes:
+ _objc_msgSend$networkActivityAddNWConnection:toActivityWithLabel:
+ _objc_msgSend$networkActivityRemoveNWConnection:fromActivityWithLabel:completion:
+ _objc_msgSend$networkActivityStart:activate:
+ _objc_msgSend$networkActivityStop:withReason:withClientMetric:withClientDict:andError:
+ _objc_msgSend$networkActivityTracingCompleteConnectionsActivities
+ _objc_msgSend$nwActivity
+ _objc_msgSend$nwActivityToken
+ _objc_msgSend$openConnectionForURL:withConnectionId:initialPayload:completion:
+ _objc_msgSend$parentLabel
+ _objc_msgSend$port
+ _objc_msgSend$publicResultsValid
+ _objc_msgSend$removeConnection:
+ _objc_msgSend$removeObjectsForKeys:
+ _objc_msgSend$retryLinkTestInOneMinute
+ _objc_msgSend$runSiriProbeWithDepth:trafficClass:
+ _objc_msgSend$scheme
+ _objc_msgSend$setHasStarted:
+ _objc_msgSend$setSavedLastJoinFailure:
+ _objc_msgSend$setSavedPreviousDisconnectReason:
+ _objc_msgSend$setSiriACEResultsValid:
+ _objc_msgSend$setSiriACESuccess:
+ _objc_msgSend$setSiriTCPResultsValid:
+ _objc_msgSend$setSiriTCPSuccess:
+ _objc_msgSend$setSiriTLSResultsValid:
+ _objc_msgSend$setSiriTLSSuccess:
+ _objc_msgSend$setSiriTrafficClass:
+ _objc_msgSend$setTclass:
+ _objc_msgSend$sharedNetworkActivityTracing
+ _objc_msgSend$siriACESuccess
+ _objc_msgSend$siriTCPSuccess
+ _objc_msgSend$siriTLSSuccess
+ _objc_msgSend$siriTrafficClass
+ _objc_msgSend$statusForSiriTCP
+ _objc_msgSend$statusForSiriTLS
+ _objc_msgSend$stopWithCompletionReason:withClientMetric:withClientDict:andError:
+ _objc_msgSend$stringByAppendingString:
+ _objc_msgSend$tclass
+ _sec_protocol_options_set_tls_tickets_enabled
+ _sharedNetworkActivityTracing.sActivityTracer
+ _sharedNetworkActivityTracing.sActivityTracerInitToken
+ _strlen
+ _task_info
+ _uuid_is_null
+ _xpc_data_create
+ _xpc_dictionary_set_double
- -[WFBlackListNode _copyCreateBlacklistedState:reason:reasonData:].cold.1
- -[WFBlackListNode addBlacklistTrigger:reasonData:bssid:].cold.1
- -[WFBlackListNode addBlacklistedState:reason:reasonData:].cold.1
- -[WFBlackListNode addBlacklistedStateHistory:state:reason:reasonData:].cold.1
- -[WFBlackListNode addBlacklistedStateHistory:state:reason:reasonData:].cold.2
- -[WFBlackListNode initWithBlacklistNetwork:].cold.1
- -[WFBlackListNode initWithBlacklistNetwork:].cold.2
- -[WFBlackListNode initWithBlacklistNetwork:].cold.3
- -[WFBlackListNode initWithBlacklistNetwork:].cold.4
- -[WFBlackListNode initWithBlacklistNetwork:].cold.5
- -[WFBlackListNode networkPruned].cold.2
- -[WFBlackListNode processBlacklistedStateMetric:unblacklisting:unblacklistingReason:].cold.2
- -[WFBlackListNode processBlacklistedStateMetric:unblacklisting:unblacklistingReason:].cold.3
- -[WFBlackListNode processBlacklistedStateMetric:unblacklisting:unblacklistingReason:].cold.4
- -[WFBlackListNode processBlacklistedStateMetric:unblacklisting:unblacklistingReason:].cold.5
- -[WFBlackListNode processBlacklistedStateMetric:unblacklisting:unblacklistingReason:].cold.6
- -[WFBlacklistEngine _evaluateTriggersForBlacklisting:reason:reasonData:bssid:ssid:state:].cold.1
- -[WFBlacklistEngine _evaluateTriggersForUnblacklisting:unblacklistReason:ssid:].cold.1
- -[WFBlacklistEngine _evaluateTriggersForUnblacklisting:unblacklistReason:ssid:].cold.2
- -[WFBlacklistEngine _ignoreTriggersForDeviceProfile:node:].cold.1
- -[WFBlacklistEngine _ignoreTriggersForDeviceProfile:node:].cold.2
- -[WFBlacklistEngine _ignoreTriggersForDeviceProfile:node:].cold.3
- -[WFBlacklistEngine changeBlacklistingThresholds:value:perSsid:].cold.1
- -[WFBlacklistEngine clearTriggerForNetworkWithUnblacklistReason:reason:].cold.2
- -[WFBlacklistEngine clearTriggerForNetworkWithUnblacklistReason:reason:].cold.3
- -[WFBlacklistEngine clearTriggerForNetworkWithUnblacklistReason:reason:].cold.4
- -[WFBlacklistEngine configureBlacklistedStateExpiryIntervalInSec:state:].cold.1
- -[WFBlacklistEngine configureBlacklistedStateExpiryIntervalInSec:state:].cold.2
- -[WFBlacklistEngine configureBlacklistedStateExpiryIntervalInSec:state:].cold.3
- -[WFBlacklistEngine configureBlacklistedStateExpiryIntervalInSec:state:].cold.4
- -[WFBlacklistEngine getBlacklistedNetworkCount].cold.1
- -[WFBlacklistEngine initWithBlacklistDelegate:profile:].cold.1
- -[WFBlacklistEngine initWithBlacklistDelegate:profile:].cold.2
- -[WFBlacklistEngine initWithBlacklistDelegate:profile:].cold.3
- -[WFBlacklistEngine initWithBlacklistDelegate:profile:].cold.4
- -[WFBlacklistEngine initWithBlacklistDelegate:profile:].cold.5
- -[WFBlacklistEngine networkPruned:].cold.2
- -[WFBlacklistEngine networkPruned:].cold.3
- -[WFBlacklistEngine removeBlacklistedStateForNetworkWithReason:state:reason:].cold.1
- -[WFBlacklistEngine removeBlacklistedStateWithUnblacklistType:].cold.1
- -[WFBlacklistEngine removeBlacklistedStateWithUnblacklistType:].cold.2
- -[WFBlacklistEngine removeBlacklistedStateWithUnblacklistType:].cold.3
- -[WFBlacklistEngine removeBlacklistedStates].cold.1
- -[WFBlacklistEngine removeExpiredBlacklistedState:].cold.1
- -[WFBlacklistEngine removeExpiredBlacklistedState:].cold.2
- -[WFBlacklistEngine retrieveBlacklistedNetworkSsids:].cold.1
- -[WFBlacklistEngine retrieveBlacklistedNetworkSsids:].cold.2
- -[WFBlacklistEngine retrieveBlacklistedStateHistoryForNetwork:state:timestamps:reasonData:].cold.1
- -[WFBlacklistEngine retrieveBlacklistedStateHistoryForNetwork:state:timestamps:reasonData:].cold.2
- -[WFBlacklistEngine retrieveNetworksInBlacklistedState:].cold.1
- -[WFBlacklistEngine retrieveNetworksInBlacklistedStateHistory:].cold.1
- -[WFBlacklistEngine retrieveReasonsForNetworkInBlacklistedState:state:timestamps:reasonData:].cold.1
- -[WFBlacklistEngine retrieveReasonsForNetworkInBlacklistedState:state:timestamps:reasonData:].cold.2
- -[WFBlacklistEngine setTriggerForNetworkWithReasonAndState:reason:reasonData:bssid:state:].cold.1
- -[WFLogger setDestinationFile:runLoopRef:runLoopMode:classC:dateFormatter:maxFileSizeInMB:logLifespanInDays:].cold.1
- -[WFLogger setDestinationFileLocation:fileNamePrefix:runLoopRef:runLoopMode:classC:dateFormatter:maxFileSizeInMB:logLifespanInDays:].cold.1
- -[WFLogger setDestinationFileLocation:fileNamePrefix:runLoopRef:runLoopMode:classC:dateFormatter:maxFileSizeInMB:logLifespanInDays:].cold.2
- -[WFLogger setDestinationOsLog:category:logLifespanInDays:logLevel:logPrivacy:].cold.1
- -[WFLoggerFile createDateString].cold.1
- -[WFLoggerFile createLogFile:fileClassC:].cold.1
- -[WFLoggerFile createLogFile:fileClassC:].cold.2
- -[WFLoggerFile createLogFile:fileClassC:].cold.3
- -[WFLoggerFile createLogFile:fileClassC:].cold.4
- -[WFLoggerFile generateLogFileName].cold.1
- -[WFLoggerFile getLogLevelPersist].cold.1
- -[WFLoggerFile removeLogFilesFromDir:].cold.1
- -[WFLoggerFile rotateLogFile:].cold.1
- -[WFLoggerFile rotateLogFile:].cold.2
- -[WFLoggerFile rotateLogFile:].cold.3
- -[WFLoggerFile rotateLogFile:].cold.4
- -[WFLoggerFile rotateLogFile:].cold.5
- -[WFLoggerFile rotateLogFile:].cold.6
- -[WFLoggerFile rotateLogFile:].cold.7
- -[WFLoggerFile setLogLevelEnable:].cold.1
- -[WFLoggerFile setLogLevelPersist:].cold.1
- -[WFLoggerFile setLogLifespanInDays:].cold.1
- -[WFLoggerFile setLogPrivacy:].cold.1
- -[WFLoggerFile setMaxFileSizeInMB:].cold.1
- -[WFLoggerFile startWatchingLogFile].cold.1
- -[WFLoggerFile startWatchingLogFile].cold.2
- -[WFLoggerFile startWatchingLogFile].cold.3
- -[WFLoggerFile startWatchingLogFile].cold.4
- -[WFMeasure initWithType:andReason:andInterfaceName:]
- -[WFTrafficEngManager __collectCriticalAppInfo].cold.1
- -[WFTrafficEngManager __configureRapportDiscoveryClient].cold.1
- -[WFTrafficEngManager __configureRapportDiscoveryClient].cold.2
- -[WFTrafficEngManager __sendPeriodicEvent:].cold.1
- -[WFTrafficEngManager initWithTrafficEngDelegate:].cold.1
- -[WFTrafficEngManager initWithTrafficEngDelegate:].cold.2
- -[WFTrafficEngManager initWithTrafficEngDelegate:].cold.3
- -[WiFiUsageLinkSession retryLinkTest]
- GCC_except_table202
- GCC_except_table21
- GCC_except_table25
- GCC_except_table82
- _WFLoggerTimerTmoCallBack.cold.1
- _WFLoggerTimerTmoCallBack.cold.2
- ___24-[WiFiUsageMonitor init]_block_invoke.34
- ___24-[WiFiUsageMonitor init]_block_invoke.38
- ___30-[WFMeasure dispatchPingTest:]_block_invoke_6
- ___36-[WFLoggerFile startWatchingLogFile]_block_invoke.36
- ___36-[WFLoggerFile startWatchingLogFile]_block_invoke.cold.1
- ___36-[WiFiUsageMonitor submitAnalytics:]_block_invoke.419
- ___37-[WiFiUsageLinkSession retryLinkTest]_block_invoke
- ___53-[WFMeasure initWithType:andReason:andInterfaceName:]_block_invoke
- ___53-[WFMeasure initWithType:andReason:andInterfaceName:]_block_invoke_2
- ___53-[WFMeasure initWithType:andReason:andInterfaceName:]_block_invoke_3
- ___53-[WFMeasure initWithType:andReason:andInterfaceName:]_block_invoke_4
- ___53-[WFTrafficEngManager __registerCallbacksAndActivate]_block_invoke.19
- ___53-[WFTrafficEngManager __registerCallbacksAndActivate]_block_invoke_2.cold.1
- ___55-[WFTrafficEngManager __sendKeepAliveEvent:dictionary:]_block_invoke.cold.1
- ___56-[WFTrafficEngManager __configureRapportDiscoveryClient]_block_invoke.16
- ___56-[WFTrafficEngManager __configureRapportDiscoveryClient]_block_invoke.16.cold.1
- ___56-[WFTrafficEngManager __configureRapportDiscoveryClient]_block_invoke.18
- ___56-[WFTrafficEngManager __configureRapportDiscoveryClient]_block_invoke.18.cold.1
- ___56-[WFTrafficEngManager __configureRapportDiscoveryClient]_block_invoke.cold.1
- ___63-[WFBlacklistEngine removeBlacklistedStateWithUnblacklistType:]_block_invoke.15
- ___64-[WFTrafficEngManager __requestCriticalAppInfo:completionBlock:]_block_invoke.23
- ___64-[WFTrafficEngManager __requestCriticalAppInfo:completionBlock:]_block_invoke.23.cold.1
- ___64-[WFTrafficEngManager __requestCriticalAppInfo:completionBlock:]_block_invoke.25
- ___64-[WFTrafficEngManager __requestCriticalAppInfo:completionBlock:]_block_invoke.cold.1
- ___69-[WiFiUsageMonitor startMonitoringWiFiInterface:withLinkSessionOnly:]_block_invoke.56
- ___85-[WiFiUsageMonitor updateKnownNetworksSupportingSeamless:forBSS:andSSID:beaconCache:]_block_invoke.457
- ___85-[WiFiUsageMonitor updateKnownNetworksSupportingSeamless:forBSS:andSSID:beaconCache:]_block_invoke.507
- ___98-[WiFiUsageMonitor setScanningState:client:neighborBSS:otherBSS:withChannelInfoList:forInterface:]_block_invoke.375
- ___block_descriptor_41_e8_32w_e34_v24?0"NSDictionary"8"NSArray"16lw32l8
- ___block_descriptor_41_e8_32w_e37_v24?0"NPTMetricResult"8"NSError"16lw32l8
- ___block_literal_global.40
- ___block_literal_global.460
- __os_log_debug_impl
- __unnamed_array_storage.208
- __unnamed_array_storage.215
- __unnamed_array_storage.220
- _objc_msgSend$initWithType:andReason:andInterfaceName:
- _objc_msgSend$retryLinkTest
CStrings:
+ "\x01\"\x12"
+ "\x03\x15\x11#\x11\x14"
+ "\x12R!"
+ "\"\x1a"
+ "%s Rejected due to [WiFiUsagePrivacyFilter isInternalInstall]\n"
+ "%s fault type %lu %@ Rejected _linkUp %d _didBecomePrimary %d\n"
+ "%s fault type %lu %@ Rejected since _lastFaultIndicationTime %f ago\n"
+ "%s kWiFiUsageFaultReasonApsdTimedOut Rejected _linkUp %d _didBecomePrimary %d\n"
+ "%s kWiFiUsageFaultReasonApsdTimedOut Rejected since _lastFaultIndicationTime %f ago\n"
+ "%s kWiFiUsageFaultReasonSiriTimedOut Rejected _linkUp %d _didBecomePrimary %d\n"
+ "%s kWiFiUsageFaultReasonSiriTimedOut Rejected since _lastFaultIndicationTime %f ago\n"
+ "%s: Activating activity"
+ "%s: Activity has _state %ld, moving to WiFiPolicyNetworkActivityTracingStarted"
+ "%s: Activity still active after %lus"
+ "%s: Adding Client Metrics %s: %@"
+ "%s: Apsd Test Not Selected for Siri TCP sampling via odds of numerator %u denominator %u"
+ "%s: Apsd Test Not Selected for Siri TLS sampling via odds of numerator %u denominator %u"
+ "%s: Apsd Test Selected for Siri TCP sampling via odds of numerator %u denominator %u"
+ "%s: Apsd Test Selected for Siri TLS sampling via odds of numerator %u denominator %u"
+ "%s: Apsd Traffic Class Class for Siri to use BE"
+ "%s: Because _isRetest using previous test options 0x%lx"
+ "%s: Because prevTestedOptions is nonzero, assuming this is a retest"
+ "%s: Cancelling activity due to timeout %@"
+ "%s: Creating activity label: %@ hasParent %d"
+ "%s: Ending activity due to remove"
+ "%s: Ending activity with connection"
+ "%s: Failed to activate %@ bad _state %ld"
+ "%s: Failed to activate %@ incorrect _state %ld"
+ "%s: Failed to addConnection. Activity %@ has _state %ld"
+ "%s: Failed to create connection %@"
+ "%s: Failed to create endpoint %@"
+ "%s: Failed to find activity with label %@ _activities %@"
+ "%s: Failed to find label description: %ld"
+ "%s: Failed to find port in _url %@"
+ "%s: Failed to find supported data type with key: %@ %@"
+ "%s: Failed to get task_info"
+ "%s: Failed to properly end activity: hasStarted %d %@"
+ "%s: Failed to removeConnection. Activity %@ has _state %ld"
+ "%s: Failed to start Existing Activity with label %@, activityExists %@ _activities %@"
+ "%s: Failed to stop activity with label %@ _activities %@"
+ "%s: Failed to stop network notStarted Child Activity %@ with coompletion %d and error: %@"
+ "%s: Fault with seenSpecificAcFailure - %@ linkTestFailureReasonString %@ results %@"
+ "%s: Got nw_connection callback event while _isCanceled %d or for other connection, ignoring"
+ "%s: LinkTest %@"
+ "%s: Network traffic class used=%u"
+ "%s: OVERRIDING kWFMeasurePreferenceApsdRetestResult success from %u to %u"
+ "%s: OVERRIDING kWFMeasurePreferenceApsdSamplingRateDenominator samplingDenominator from %u to %u"
+ "%s: OVERRIDING kWFMeasurePreferenceApsdSamplingRateNumerator samplingNumerator from %u to %u"
+ "%s: OVERRIDING kWFMeasurePreferenceApsdTestResult success from %u to %u"
+ "%s: OVERRIDING kWFMeasurePreferenceApsdTrafficClass to %u"
+ "%s: OVERRIDING kWFMeasurePreferencePeriodicSiriRetestResult success from %u to %u"
+ "%s: OVERRIDING kWFMeasurePreferencePeriodicSiriSamplingRateDenominator samplingDenominator from %u to %u"
+ "%s: OVERRIDING kWFMeasurePreferencePeriodicSiriSamplingRateNumerator samplingNumerator from %u to %u"
+ "%s: OVERRIDING kWFMeasurePreferencePeriodicSiriTestResult success from %u to %u"
+ "%s: OVERRIDING kWFMeasurePreferencePeriodicSiriTrafficClass to %u"
+ "%s: OVERRIDING kWFMeasurePreferenceSiriTimeoutRetestResult success from %u to %u"
+ "%s: OVERRIDING kWFMeasurePreferenceSiriTimeoutSamplingRateDenominator samplingDenominator from %u to %u"
+ "%s: OVERRIDING kWFMeasurePreferenceSiriTimeoutSamplingRateNumerator samplingNumerator from %u to %u"
+ "%s: OVERRIDING kWFMeasurePreferenceSiriTimeoutTestResult success from %u to %u"
+ "%s: OVERRIDING kWFMeasurePreferenceSiriTimeoutTrafficClass to %u"
+ "%s: Open timer firing"
+ "%s: PERIODIC TEST SELECTED for Siri TCP sampling via odds of numerator %u denominator %u"
+ "%s: PERIODIC TEST SELECTED for Siri TLS sampling via odds of numerator %u denominator %u"
+ "%s: Periodic Test Not Selected for Siri TCP sampling via odds of numerator %u denominator %u"
+ "%s: Periodic Test Not Selected for Siri TLS sampling via odds of numerator %u denominator %u"
+ "%s: Perodic Traffic Class for Siri to use BE"
+ "%s: Pinging LocalDNS PublicDNS or Gateway failed due to no pingAddress"
+ "%s: Probing has been disabled from running after %@, it is now %@"
+ "%s: Probing ok to run before %@, it is now %@"
+ "%s: Reporting to nw_activity that WiFiPolicyNetworkActivity failed with error code %d and underlying error code %d"
+ "%s: Requesting test type: %lu for Reason: %@ prevTestedOptions: %lx using interface: %@"
+ "%s: Setting _isRetest from %u to %u"
+ "%s: Start activity with label %@ _activities %@ %@"
+ "%s: Starting NWConnection to Siri using traffic class %d, depth %ld"
+ "%s: Starting activity"
+ "%s: Stopping Parent Activity %@ %@"
+ "%s: Stopping activity with label %@ _activities %@ %@"
+ "%s: Stopping network Child Activity %@ with coompletion %d and error: %@"
+ "%s: Stopping network Child Activity %@ with coompletion %d clientMetric %s clientDict %@ and error: %@"
+ "%s: Stopping network activity %@ with completion %d and error: %@"
+ "%s: Stopping network activity %@ with completion %d clientMetric %s clientDict %@ and error: %@"
+ "%s: There are %lu remaining activities _activities %@"
+ "%s: Timeout Test Not Selected for Siri TCP sampling via odds of numerator %u denominator %u"
+ "%s: Timeout Test Not Selected for Siri TLS sampling via odds of numerator %u denominator %u"
+ "%s: Timeout Test Selected for Siri TCP sampling via odds of numerator %u denominator %u"
+ "%s: Timeout Test Selected for Siri TLS sampling via odds of numerator %u denominator %u"
+ "%s: Timeout Traffic Class Class for Siri to use BE"
+ "%s: When stopping parent activity - there are %lu remaining activities _activities %@"
+ "%s: Will Remove Ended Activity %@ %@"
+ "%s: Will Remove Ended Child Activity %@ %@"
+ "%s: Will test type: %lu for Reason: %@ prevTestedOptions: 0x%lx options: 0x%lx using interface: %@"
+ "%s: cached %@"
+ "%s: close error is %@"
+ "%s: closing"
+ "%s: closing with error %@"
+ "%s: is alredy cancelled, returning"
+ "%s: keyWithPrefix already exists in dictionary: keyWithPrefix: %@ existing value %@ objValue %@"
+ "%s: openConnectionForURL complete closing connection"
+ "%s: openConnectionForURL returned error %@"
+ "%s: openConnectionForURL returned success"
+ "%s: optimisticDNS"
+ "%s: read closed"
+ "%s: state: %d error: %@ for connection: %llu"
+ "%s: state: nw_connection_state_cancelled for connection: %llu"
+ "%s: state: nw_connection_state_failed for connection: %llu"
+ "%s: state: nw_connection_state_invalid for connection: %llu"
+ "%s: state: nw_connection_state_preparing for connection: %llu"
+ "%s: state: nw_connection_state_ready for connection: %llu"
+ "%s: state: nw_connection_state_waiting for connection: %llu"
+ "%s: statusForLocal - %@ linkTestFailureReasonString %@ results %@"
+ "%s: statusForSiriTCP - %@ linkTestFailureReasonString %@ results %@"
+ "%s: statusForSiriTLS - %@ linkTestFailureReasonString %@ results %@"
+ "%s: write closed"
+ "%s:%u: Attempting to reset chip with vague reason %@, linkTestIniated %@\n"
+ "%s:%u: Found successful linktest\n"
+ "%s:%u: Handling fault event is not supported for %@\n"
+ "%s:%u: Link test completed after _didHandleFaultEvent, %@\n"
+ "%s:%u: Link test did not pass, skipping recovery (skips = %lu)\n"
+ "%s:%u: Not proceeding with linktest\n"
+ "%s:%u: Will induce fault recovery with reason: %@  :foundCriticalFailure %d foundNonCriticalFailure %d foundFailure w seenSpecificAcFailure %d\n"
+ "%{public}s"
+ "-[SiriNWConnection _closeWithError:]"
+ "-[SiriNWConnection _closeWithError:]_block_invoke_4"
+ "-[SiriNWConnection _configureConnection:]_block_invoke"
+ "-[SiriNWConnection _configureConnection:]_block_invoke_2"
+ "-[SiriNWConnection _configureConnection:]_block_invoke_3"
+ "-[SiriNWConnection _getAttemptedEndpoints]"
+ "-[SiriNWConnection _getNWConnectionWithInitialData:completion:]"
+ "-[SiriNWConnection _setParametersForHost:useTLS:initialPayload:]"
+ "-[SiriNWConnection _setupOpenTimer]_block_invoke"
+ "-[SiriNWConnection runSiriProbeWithDepth:trafficClass:]"
+ "-[SiriNWConnection runSiriProbeWithDepth:trafficClass:]_block_invoke"
+ "-[WFMeasure dispatchPingTest:]_block_invoke"
+ "-[WFMeasure dispatchSiriTest:trafficClass:]"
+ "-[WFMeasure dispatchSiriTest:trafficClass:]_block_invoke_2"
+ "-[WFMeasure dispatchSiriTest:trafficClass:]_block_invoke_3"
+ "-[WFMeasure dispatchSiriTest:trafficClass:]_block_invoke_4"
+ "-[WFMeasure dispatchSiriTest:trafficClass:]_block_invoke_5"
+ "-[WFMeasure dispatchSiriTest:trafficClass:]_block_invoke_6"
+ "-[WFMeasure dispatchSiriTest:trafficClass:]_block_invoke_7"
+ "-[WFMeasure dispatchSiriTest:trafficClass:]_block_invoke_8"
+ "-[WFMeasure getApsdSampleTrafficClass]"
+ "-[WFMeasure getApsdSampleTrafficClass]_block_invoke"
+ "-[WFMeasure getLazyNSStringPreference:exists:]"
+ "-[WFMeasure getPeriodicSampleTrafficClass]"
+ "-[WFMeasure getPeriodicSampleTrafficClass]_block_invoke"
+ "-[WFMeasure getTimeoutSampleTrafficClass]"
+ "-[WFMeasure getTimeoutSampleTrafficClass]_block_invoke"
+ "-[WFMeasure initWithType:andReason:prevTestedOptions:andInterfaceName:]"
+ "-[WFMeasure initWithType:andReason:prevTestedOptions:andInterfaceName:]_block_invoke"
+ "-[WFMeasure initWithType:andReason:prevTestedOptions:andInterfaceName:]_block_invoke_2"
+ "-[WFMeasure initWithType:andReason:prevTestedOptions:andInterfaceName:]_block_invoke_3"
+ "-[WFMeasure initWithType:andReason:prevTestedOptions:andInterfaceName:]_block_invoke_4"
+ "-[WFMeasure initWithType:andReason:prevTestedOptions:andInterfaceName:]_block_invoke_5"
+ "-[WFMeasure shouldApsdSampleSiriTCP]"
+ "-[WFMeasure shouldApsdSampleSiriTCP]_block_invoke"
+ "-[WFMeasure shouldApsdSampleSiriTCP]_block_invoke_2"
+ "-[WFMeasure shouldApsdSampleSiriTLS]"
+ "-[WFMeasure shouldApsdSampleSiriTLS]_block_invoke"
+ "-[WFMeasure shouldApsdSampleSiriTLS]_block_invoke_2"
+ "-[WFMeasure shouldPeriodicSampleSiriTCP]"
+ "-[WFMeasure shouldPeriodicSampleSiriTCP]_block_invoke"
+ "-[WFMeasure shouldPeriodicSampleSiriTCP]_block_invoke_2"
+ "-[WFMeasure shouldPeriodicSampleSiriTLS]"
+ "-[WFMeasure shouldPeriodicSampleSiriTLS]_block_invoke"
+ "-[WFMeasure shouldPeriodicSampleSiriTLS]_block_invoke_2"
+ "-[WFMeasure shouldTimeoutSampleSiriTCP]"
+ "-[WFMeasure shouldTimeoutSampleSiriTCP]_block_invoke"
+ "-[WFMeasure shouldTimeoutSampleSiriTCP]_block_invoke_2"
+ "-[WFMeasure shouldTimeoutSampleSiriTLS]"
+ "-[WFMeasure shouldTimeoutSampleSiriTLS]_block_invoke"
+ "-[WFMeasure shouldTimeoutSampleSiriTLS]_block_invoke_2"
+ "-[WiFiPolicyNetworkActivity _startMaxActivityLifetime]_block_invoke"
+ "-[WiFiPolicyNetworkActivity activate]"
+ "-[WiFiPolicyNetworkActivity addConnection:]"
+ "-[WiFiPolicyNetworkActivity initWithLabel:parent:]"
+ "-[WiFiPolicyNetworkActivity removeConnection:]"
+ "-[WiFiPolicyNetworkActivity stopWithCompletionReason:withClientMetric:withClientDict:andError:]"
+ "-[WiFiPolicyNetworkActivity stopWithCompletionReason:withClientMetric:withClientDict:andError:]_block_invoke"
+ "-[WiFiPolicyNetworkActivityTracing _networkActivityActivate:]"
+ "-[WiFiPolicyNetworkActivityTracing _networkActivityStart:activate:]"
+ "-[WiFiPolicyNetworkActivityTracing _networkActivityStop:withReason:withClientMetric:withClientDict:andError:]"
+ "-[WiFiPolicyNetworkActivityTracing _networkActivityStop:withReason:withClientMetric:withClientDict:andError:]_block_invoke"
+ "-[WiFiPolicyNetworkActivityTracing _networkActivityTracingCancel]_block_invoke"
+ "-[WiFiPolicyNetworkActivityTracing networkActivityStop:withReason:withClientMetric:withClientDict:andError:]"
+ "-[WiFiUsageLinkSession addDictionary:withKeysPrefix:toFlatDictionary:]_block_invoke"
+ "-[WiFiUsageLinkSession faultEventDetected:]"
+ "-[WiFiUsageLinkSession getLazyNSNumberPreference:exists:]"
+ "-[WiFiUsageLinkSession retryLinkTestInOneMinute]"
+ "-[WiFiUsageMonitor updateBeaconInfo:andParsedIE:forInterface:]"
+ "2023-01-30"
+ "2023-12-30"
+ "443"
+ "80"
+ "@\"NSObject<OS_nw_activity>\""
+ "@\"NSObject<OS_nw_connection>\""
+ "@\"NSObject<OS_nw_content_context>\""
+ "@\"NSObject<OS_nw_endpoint>\""
+ "@36@0:8r*16B24@28"
+ "@40@0:8@16@24@?32"
+ "@48@0:8Q16@24Q32@40"
+ "Arp Failure"
+ "A\xf0\xb2"
+ "Backhaul"
+ "BeforeInduceingFault_"
+ "BeforeNonCriticalFailureRetest_"
+ "DNS"
+ "DidBecomePrimary"
+ "FaultEventLinkNotRecovered"
+ "FaultEventRecoveredLink"
+ "FinalResults_"
+ "FltBadAC"
+ "FoundFailure"
+ "Internet"
+ "Invoke"
+ "LinkRecoverySkips"
+ "LinkTestFailure_%@"
+ "Local"
+ "Past Siri Probe Functional Date"
+ "Pinging LocalDNS PublicDNS or Gateway failed due to no pingAddress"
+ "SeenSpecificAcFailure %d "
+ "SiriNWConnection"
+ "SiriNWConnection Starting"
+ "SiriNWConnection has failed with error %@"
+ "SiriNWConnection has succeeded"
+ "SiriTCP"
+ "SiriTCP: %@ (TrafficClass %ld) "
+ "SiriTLS"
+ "SiriTLS: %@ (TrafficClass %ld) "
+ "SiriTrafficClass"
+ "SkippingRecovery"
+ "SuccessfulLinkTest"
+ "TB,N,V_isApsdTimeout"
+ "TB,N,V_isRetest"
+ "TB,N,V_isSiriTimeout"
+ "TB,N,V_siriACEResultsValid"
+ "TB,N,V_siriACESuccess"
+ "TB,N,V_siriTCPResultsValid"
+ "TB,N,V_siriTCPSuccess"
+ "TB,N,V_siriTLSResultsValid"
+ "TB,N,V_siriTLSSuccess"
+ "TI,N,V_tclass"
+ "Tq,N,V_siriTrafficClass"
+ "URLWithString:"
+ "WiFiFaultHandlingLimitedLinkOrPrimaryNotSet"
+ "WiFiFaultHandlingLimitedRateLastFaultIndication"
+ "WiFiFaultHandlingLimitedRateMinBrokenLinkDetectedInterval"
+ "WiFiFaultHandlingLimitedRecoveryDisabled"
+ "WiFiFaultHandlingNotIgnored"
+ "WiFiPolicyActivityTracing.m"
+ "WiFiPolicyNetworkActivity"
+ "WiFiPolicyNetworkActivityTracing"
+ "WiFiUsageLinkSession.m"
+ "WillAttemptRetest"
+ "WillInduceFaultEvent"
+ "[30Q]"
+ "[WiFiPolicy] %s"
+ "_%@"
+ "_FltBadAC"
+ "_SiriTCP"
+ "_SiriTLS"
+ "_activities"
+ "_activity"
+ "_activityTimer"
+ "_attemptedEndpoints"
+ "_betterPathAvailableNotificationMachTime"
+ "_cancelActivityTimer"
+ "_cancelOpenTimer"
+ "_closeWithError:"
+ "_configureConnection:"
+ "_connection"
+ "_connectionId"
+ "_connectionUnviableTimer"
+ "_connections"
+ "_content_context"
+ "_dateToDisable"
+ "_endpoint"
+ "_getAttemptedEndpoints"
+ "_getNWConnectionWithInitialData:completion:"
+ "_hasStarted"
+ "_interfaceIndex"
+ "_invokeOpenCompletionWithError:"
+ "_isApsdTimeout"
+ "_isCanceled"
+ "_isEstablishing"
+ "_isReady"
+ "_isRetest"
+ "_isSiriTimeout"
+ "_labelDescription"
+ "_lastFaultEventHandledOptions"
+ "_linkTestResult"
+ "_mostRecentErrorFromNWConnection"
+ "_networkActivityAbort"
+ "_networkActivityActivate:"
+ "_networkActivityAddNWConnection:toActivityWithLabel:"
+ "_networkActivityRemoveNWConnection:fromActivityWithLabel:completion:"
+ "_networkActivityRestart"
+ "_networkActivityStart:activate:"
+ "_networkActivityState:"
+ "_networkActivityStop:withReason:withClientMetric:withClientDict:andError:"
+ "_networkActivityTracingCancel"
+ "_network_traffic_class"
+ "_openCompletion"
+ "_openTimer"
+ "_parentActivity"
+ "_parentLabel"
+ "_probeLabel"
+ "_readWriteCounter"
+ "_resolvedHost"
+ "_setParametersForHost:useTLS:initialPayload:"
+ "_setupOpenTimer"
+ "_siriACEResultsValid"
+ "_siriACESuccess"
+ "_siriTCPResultsValid"
+ "_siriTCPSuccess"
+ "_siriTLSResultsValid"
+ "_siriTLSSuccess"
+ "_staleConnectionTimer"
+ "_startActivityTimer"
+ "_startMaxActivityLifetime"
+ "_state"
+ "_tclass"
+ "_url"
+ "_usingTLS"
+ "_wfcompletion"
+ "activate"
+ "addConnection:"
+ "addDictionary:withKeysPrefix:toFlatDictionary:"
+ "apsd_result"
+ "apsd_retest_result"
+ "apsd_sampling_denominator"
+ "apsd_sampling_numerator"
+ "apsd_tclass"
+ "badport"
+ "behave_as_retest"
+ "close"
+ "com.apple.wifi.policy"
+ "com.apple.wifi.policy.nwactivity"
+ "com.apple.wifi.policy.siri"
+ "com.apple.wifipolicy.usagelinksession"
+ "currentNetworkActivityTokenWithCompletion:"
+ "dateFromString:"
+ "dispatchSiriTest got results for invalid probeDepth"
+ "dispatchSiriTest:trafficClass:"
+ "expireddate"
+ "fullTest"
+ "gatewayTest"
+ "getApsdSampleTrafficClass"
+ "getLazyNSStringPreference:exists:"
+ "getPeriodicSampleTrafficClass"
+ "getState"
+ "getTimeoutSampleTrafficClass"
+ "hasActiveConnection"
+ "hasActivitiesRunning"
+ "hasStarted"
+ "host"
+ "http://guzzoni.apple.com:443/"
+ "http://guzzoni.apple.com:80/"
+ "https"
+ "https://guzzoni.apple.com:443/"
+ "https://guzzoni.apple.com:443/ace"
+ "initWithLabel:parent:"
+ "initWithQueueAndCompletion:reason:callback:"
+ "initWithType:andReason:prevTestedOptions:andInterfaceName:"
+ "initWithUUIDBytes:"
+ "invalid"
+ "isApsdTimeout"
+ "isRetest"
+ "isSiriTimeout"
+ "kWiFiUsageFaultReasonApsdTimedOut"
+ "kWiFiUsageFaultReasonArpFailure"
+ "kWiFiUsageFaultReasonBrokenBackhaulLinkFailed"
+ "kWiFiUsageFaultReasonBssidBlocklisted"
+ "kWiFiUsageFaultReasonDatapathStall"
+ "kWiFiUsageFaultReasonDelayedAutoJoin"
+ "kWiFiUsageFaultReasonDextCrashed"
+ "kWiFiUsageFaultReasonDhcpFailure"
+ "kWiFiUsageFaultReasonFirmwareTrap"
+ "kWiFiUsageFaultReasonLinkTestDNSCheckFailed"
+ "kWiFiUsageFaultReasonLinkTestInternetCheckFailed"
+ "kWiFiUsageFaultReasonLinkTestLocalCheckFailed"
+ "kWiFiUsageFaultReasonLinkTestSiriTCPCheckFailed"
+ "kWiFiUsageFaultReasonLinkTestSiriTLSCheckFailed"
+ "kWiFiUsageFaultReasonLowPowerBudgetExceeded"
+ "kWiFiUsageFaultReasonPrivateMACFallback"
+ "kWiFiUsageFaultReasonSiriTimedOut"
+ "kWiFiUsageFaultReasonSleepPowerBudgetExceeded"
+ "kWiFiUsageFaultReasonSlowWiFiAP"
+ "kWiFiUsageFaultReasonSlowWiFiDUT"
+ "kWiFiUsageFaultReasonSlowWiFiDnsFailure"
+ "kWiFiUsageFaultReasonSsidBlocklisted"
+ "kWiFiUsageFaultReasonSymptomLowRssiArpFailure"
+ "kWiFiUsageFaultReasonSymptomLowRssiDataStall"
+ "kWiFiUsageFaultReasonSymptomLowRssiDnsFailure"
+ "kWiFiUsageFaultReasonSymptomLowRssiRTTFailure"
+ "kWiFiUsageFaultReasonSymptomLowRssiShortFlow"
+ "kWiFiUsageFaultReasonUnknown"
+ "kWiFiUsageFaultReasonUserOverridesCellularOutranking"
+ "kWiFiUsageFaultReasonWatchdogReset"
+ "linkTest"
+ "localDNSTest"
+ "network.activity.tracing"
+ "networkActivityActivate:"
+ "networkActivityAddNWConnection:toActivityWithLabel:"
+ "networkActivityRemoveNWConnection:fromActivityWithLabel:completion:"
+ "networkActivityStart:activate:"
+ "networkActivityStop:withReason:withClientMetric:withClientDict:andError:"
+ "networkActivityTracingCompleteConnectionsActivities"
+ "nwActivity"
+ "nwActivityToken"
+ "nw_activity %d:%d[%@]"
+ "nw_activity %d:%d[%@] parent nw_activity %d:%d[%@]"
+ "openConnectionForURL:withConnectionId:initialPayload:completion:"
+ "parentLabel"
+ "periodic_sampling_siri_denominator"
+ "periodic_sampling_siri_numerator"
+ "periodic_siri_result"
+ "periodic_siri_retest_result"
+ "periodic_siri_tclass"
+ "port"
+ "probeSiriACE"
+ "probeSiriTCP"
+ "probeSiriTLS"
+ "publicDNSTest"
+ "removeConnection:"
+ "removeObjectsForKeys:"
+ "resolveAppleTest"
+ "resolvedHost"
+ "retryLinkTestInOneMinute"
+ "runSiriProbeWithDepth:trafficClass:"
+ "scheme"
+ "setHasStarted:"
+ "setIsApsdTimeout:"
+ "setIsRetest:"
+ "setIsSiriTimeout:"
+ "setSiriACEResultsValid:"
+ "setSiriACESuccess:"
+ "setSiriTCPResultsValid:"
+ "setSiriTCPSuccess:"
+ "setSiriTLSResultsValid:"
+ "setSiriTLSSuccess:"
+ "setSiriTrafficClass:"
+ "setTclass:"
+ "sharedNetworkActivityTracing"
+ "shouldApsdSampleSiriTCP"
+ "shouldApsdSampleSiriTLS"
+ "shouldPeriodicSampleSiriTCP"
+ "shouldPeriodicSampleSiriTLS"
+ "shouldTimeoutSampleSiriTCP"
+ "shouldTimeoutSampleSiriTLS"
+ "siriACEResultsValid"
+ "siriACESuccess"
+ "siriTCPResultsValid"
+ "siriTCPSuccess"
+ "siriTLSResultsValid"
+ "siriTLSSuccess"
+ "siri_timeout_result"
+ "siri_timeout_retest_result"
+ "siri_timeout_sampling_denominator"
+ "siri_timeout_sampling_numerator"
+ "siri_timeout_tclass"
+ "statusForSiriTCP"
+ "statusForSiriTLS"
+ "stopWithCompletionReason:withClientMetric:withClientDict:andError:"
+ "stringByAppendingString:"
+ "tclass"
+ "throughputTest"
+ "v16@?0@\"NSObject<OS_nw_error>\"8"
+ "v16@?0@\"NSObject<OS_nw_protocol_options>\"8"
+ "v20@?0B8@\"NSError\"12"
+ "v20@?0i8@\"NSObject<OS_nw_error>\"12"
+ "v24@?0@\"NSObject<OS_nw_connection>\"8@\"NSError\"16"
+ "v28@0:8q16I24"
+ "v32@0:8@16q24"
+ "v32@?0@\"NSString\"8@\"WiFiPolicyNetworkActivity\"16^B24"
+ "v32@?0@\"NSString\"8@16^B24"
+ "v40@0:8@16q24@?32"
+ "v44@0:8i16r*20@28@36"
+ "v48@0:8@16@24@32@?40"
+ "v52@0:8q16i24r*28@36@44"
+ "yyyy-MM-dd"
+ "\xf0\xf0\x81\x11:\xf0\xf01\x81\xb9"
+ "\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xa1s\x11#\x11\x8f\x0f\x03\xf0\xf0\xf0\x91s\xf0\xf0\xf0\x91\xb2t\xb2S'\x11\xa1\xf0\xa1\x11\xa3"
- "\x12\x1a"
- "\x12R"
- "%.2X:%.2X:%.2X"
- "%s ether_aton returns null. Invalid bssid"
- "%s: Requesting test type: %lu for Reason: %@ using interface: %@"
- "%s: Will test type: %lu for Reason: %@ options: 0x%lx using interface: %@"
- "%s:%u: Handling fault event is not supported\n"
- "%s:%u: Link test never passed, skipping recovery (skips = %lu)\n"
- "%s:%u: Will induce fault recovery with reason: %@ : foundCriticalFailure %d foundNonCriticalFailure %d foundFailure with seenSpecificAcFailure %d statusForAcFailure %@\n"
- "-[WFMeasure dispatchPingTest:]_block_invoke_6"
- "-[WFMeasure initWithType:andReason:andInterfaceName:]"
- "-[WFMeasure initWithType:andReason:andInterfaceName:]_block_invoke"
- "-[WFMeasure initWithType:andReason:andInterfaceName:]_block_invoke_2"
- "-[WFMeasure initWithType:andReason:andInterfaceName:]_block_invoke_3"
- "-[WFMeasure initWithType:andReason:andInterfaceName:]_block_invoke_4"
- "-[WiFiUsageLinkSession retryLinkTest]"
- "-[WiFiUsageMonitor updateBeaconInfo:andParsedIE:forInterface:]_block_invoke"
- "Fault Detected"
- "Tq,R,N,V_siriTrafficClass"
- "[28Q]"
- "initWithType:andReason:andInterfaceName:"
- "\xf0\xf0a\x11:\xf0\xf01\x81\xb9"
- "\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\x81s\x11#\x11\x8f\x0f\x03\xf0\xf0\xf0\x91s\xf0\xf0\xf0\x91\xb2t\xb2S'\x11\xa1\xf0\xa1\x11\xa3"

```
