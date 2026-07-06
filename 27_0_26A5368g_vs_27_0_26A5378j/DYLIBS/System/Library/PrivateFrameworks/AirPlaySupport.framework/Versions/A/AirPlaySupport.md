## AirPlaySupport

> `/System/Library/PrivateFrameworks/AirPlaySupport.framework/Versions/A/AirPlaySupport`

```diff

-  __TEXT.__text: 0xc3568
-  __TEXT.__objc_methlist: 0x344
+  __TEXT.__text: 0xc6384
+  __TEXT.__objc_methlist: 0x38c
   __TEXT.__const: 0xee8
-  __TEXT.__dlopen_cstrs: 0x100
-  __TEXT.__gcc_except_tab: 0x324
-  __TEXT.__cstring: 0x31142
+  __TEXT.__dlopen_cstrs: 0x158
+  __TEXT.__gcc_except_tab: 0x374
+  __TEXT.__cstring: 0x32035
   __TEXT.__oslogstring: 0x1cc
-  __TEXT.__unwind_info: 0x1d68
+  __TEXT.__unwind_info: 0x1dd8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2688
-  __DATA_CONST.__objc_classlist: 0x28
+  __DATA_CONST.__const: 0x2708
+  __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x550
+  __DATA_CONST.__objc_selrefs: 0x600
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x28
-  __DATA_CONST.__objc_arraydata: 0x58
-  __DATA_CONST.__got: 0x620
-  __AUTH_CONST.__const: 0x4408
-  __AUTH_CONST.__cfstring: 0x6c40
-  __AUTH_CONST.__objc_const: 0x678
+  __DATA_CONST.__objc_arraydata: 0x60
+  __DATA_CONST.__got: 0x650
+  __AUTH_CONST.__const: 0x44a8
+  __AUTH_CONST.__cfstring: 0x6fe0
+  __AUTH_CONST.__objc_const: 0x7a8
   __AUTH_CONST.__weak_auth_got: 0x10
+  __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x190
   __AUTH.__data: 0x350
-  __DATA.__objc_ivar: 0x20
-  __DATA.__data: 0x2628
-  __DATA.__bss: 0xae8
-  __DATA_DIRTY.__data: 0x990
-  __DATA_DIRTY.__bss: 0x628
+  __DATA.__objc_ivar: 0x2c
+  __DATA.__data: 0x25b8
+  __DATA.__bss: 0xb10
+  __DATA_DIRTY.__objc_data: 0x1e0
+  __DATA_DIRTY.__data: 0xa00
+  __DATA_DIRTY.__bss: 0x658
   - /System/Library/Frameworks/AudioToolbox.framework/Versions/A/AudioToolbox
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreMedia.framework/Versions/A/CoreMedia

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2586
-  Symbols:   5209
-  CStrings:  5106
+  Functions: 2616
+  Symbols:   5304
+  CStrings:  5201
 
Sections:
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __AUTH_CONST.__weak_auth_got : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH.__data : content changed
Symbols:
+ +[APSRadarComponentEntry componentEntryWithName:version:ID:]
+ -[APSRadarComponentEntry componentID]
+ -[APSRadarComponentEntry componentName]
+ -[APSRadarComponentEntry componentVersion]
+ APSGetNANPerformanceForecastThresholds.sOnce
+ APSGetNANPerformanceForecastThresholds.sThresholds
+ GCC_except_table1136
+ GCC_except_table1222
+ GCC_except_table1223
+ GCC_except_table1229
+ GCC_except_table1297
+ GCC_except_table1302
+ GCC_except_table1315
+ GCC_except_table1343
+ GCC_except_table1492
+ GCC_except_table1494
+ GCC_except_table1534
+ GCC_except_table1540
+ GCC_except_table1780
+ GCC_except_table1783
+ GCC_except_table1786
+ GCC_except_table1790
+ GCC_except_table2088
+ GCC_except_table2229
+ GCC_except_table2462
+ GCC_except_table2465
+ GCC_except_table2466
+ GCC_except_table2538
+ GCC_except_table499
+ GCC_except_table536
+ GCC_except_table949
+ OBJC_IVAR_$_APSRadarComponentEntry.componentID
+ OBJC_IVAR_$_APSRadarComponentEntry.componentName
+ OBJC_IVAR_$_APSRadarComponentEntry.componentVersion
+ TapToRadarKitLibraryCore.frameworkLibrary
+ _APSAdaptiveLatencyManagerUpdatePacketsExpiredBurstCount
+ _APSGetNANPerformanceForecastThresholds
+ _APSRTCPCCFBProcessorGetPacketsExpiredBurstCount
+ _CFDictionaryGetEmpty
+ _CFUserNotificationCreate
+ _CFUserNotificationReceiveResponse
+ _OBJC_CLASS_$_APSRadarComponentEntry
+ _OBJC_METACLASS_$_APSRadarComponentEntry
+ _TapToRadarKitLibrary
+ __OBJC_$_CLASS_METHODS_APSRadarComponentEntry
+ __OBJC_$_INSTANCE_METHODS_APSRadarComponentEntry
+ __OBJC_$_INSTANCE_VARIABLES_APSRadarComponentEntry
+ __OBJC_$_PROP_LIST_APSRadarComponentEntry
+ __OBJC_CLASS_RO_$_APSRadarComponentEntry
+ __OBJC_METACLASS_RO_$_APSRadarComponentEntry
+ ___APSGetNANPerformanceForecastThresholds_block_invoke
+ ___TapToRadarKitLibraryCore_block_invoke
+ ___apsRadarLogging_radarComponentEntryForAPSRadarComponentID_block_invoke
+ ___apsTapToRadarInvokeDetailed_block_invoke
+ ___apsTapToRadarInvokeDetailed_block_invoke_2
+ ___block_descriptor_32_e17_v16?0"NSError"8l
+ ___block_descriptor_73_e5_v8?0l
+ ___copy_helper_block_8_32r40r48r
+ ___copy_helper_block_8_32r40r48r56r64r
+ ___destroy_helper_block_8_32r40r48r
+ ___destroy_helper_block_8_32r40r48r56r64r
+ ___getRadarComponentClass_block_invoke
+ ___getRadarDraftClass_block_invoke
+ ___getTapToRadarServiceClass_block_invoke
+ ___hoseControllerAPAT_computeEffectiveTrailingUnReceivedRangeInternal_block_invoke
+ ___hoseControllerMulticastAPAT_MulticastGroupInfoDidChange_block_invoke_2
+ __dispatch_main_q
+ _alm_AppendWindowSamples
+ _alm_GetWindowCount
+ _audit_stringTapToRadarKit
+ _getTapToRadarServiceClass
+ _hoseControllerAPAT_MulticastGroupInfoDidApply
+ _hoseControllerAPAT_SetParentControllerCallbacks
+ _hoseControllerAPAT_computeEffectiveTrailingUnReceivedRangeInternal
+ _hoseControllerMulticastAPAT_multicastGroupInfoDidApplyCallback
+ _kAPSAudioProtocolDriverHoseControllerProperty_MulticastPromotionPending
+ _kAPSAudioProtocolDriverHoseProperty_SupportsTerminus
+ _kCFUserNotificationAlertHeaderKey
+ _kCFUserNotificationAlertMessageKey
+ _kCFUserNotificationAlternateButtonTitleKey
+ _kCFUserNotificationDefaultButtonTitleKey
+ _objc_msgSend$authorizationStatus
+ _objc_msgSend$componentEntryWithName:version:ID:
+ _objc_msgSend$componentID
+ _objc_msgSend$componentName
+ _objc_msgSend$componentVersion
+ _objc_msgSend$copy
+ _objc_msgSend$createDraft:forProcessNamed:withDisplayReason:completionHandler:
+ _objc_msgSend$initWithName:version:identifier:
+ _objc_msgSend$integerValue
+ _objc_msgSend$localizedDescription
+ _objc_msgSend$serviceSettings
+ _objc_msgSend$setClassification:
+ _objc_msgSend$setComponent:
+ _objc_msgSend$setDeviceIDs:
+ _objc_msgSend$setDiagnosticExtensionIDs:
+ _objc_msgSend$setIsUserInitiated:
+ _objc_msgSend$setProblemDescription:
+ _objc_msgSend$setReproducibility:
+ _objc_msgSend$setShouldCapturePerformanceTrace:
+ _objc_msgSend$setTitle:
+ _objc_msgSend$stringWithFormat:
+ _objc_msgSend$valueForKey:
+ _priorityDispatcher_heartbeatTick
+ _protocolDriverReceiverAPAT_failedToAddSeqNumLogger
+ apsRadarLogging_radarComponentEntryForAPSRadarComponentID.entries
+ apsRadarLogging_radarComponentEntryForAPSRadarComponentID.onceToken
+ getRadarComponentClass.softClass
+ getRadarDraftClass.softClass
+ getTapToRadarServiceClass.softClass
+ hoseControllerMulticastAPAT_AddSubHoseController.multicastCallbacks
- GCC_except_table1131
- GCC_except_table1277
- GCC_except_table1282
- GCC_except_table1295
- GCC_except_table1323
- GCC_except_table1470
- GCC_except_table1472
- GCC_except_table1512
- GCC_except_table1518
- GCC_except_table1758
- GCC_except_table1761
- GCC_except_table1764
- GCC_except_table1768
- GCC_except_table2061
- GCC_except_table2202
- GCC_except_table2435
- GCC_except_table2438
- GCC_except_table2439
- GCC_except_table2511
- GCC_except_table498
- GCC_except_table535
- GCC_except_table945
- ___copy_helper_block_8_32r40r48r56r
- ___destroy_helper_block_8_32r40r48r56r
- _hoseControllerAPAT_SetFeedbackProcessorCallbacks
- hoseControllerMulticastAPAT_AddSubHoseController.stateCallbacks
CStrings:
+ "%@ (%@)"
+ "1158817"
+ "1158818"
+ "629193"
+ "629196"
+ "629211"
+ "629212"
+ "953616"
+ "APATSendWindow"
+ "APSAdaptiveLatencyManagerRegisterEndpoint inEndpointID: %u [0x%04X], outStatsInput: [%{ptr}]"
+ "APSAdaptiveLatencyManagerRegisterEndpoint inEndpointID: %u, initialLatencyMs: %u, leadingLatencyMs: %u, trailingLatencyMs: %u, maxNetworkLatencyMs: %u"
+ "APSAdaptiveLatencyManagerUpdatePacketsExpiredBurstCount"
+ "APSPriorityDispatcher.%{ptr}"
+ "APSPriorityDispatcher.heartbeat"
+ "APSRTCPCCFBProcessorGetPacketsExpiredBurstCount"
+ "APSRTPSeqNumRange hoseControllerAPAT_computeEffectiveTrailingUnReceivedRangeInternal(APSAudioProtocolDriverSenderHoseControllerAPATRef)"
+ "AirPlay Error"
+ "AirPlay has detected an internal error"
+ "AirPlay has detected an internal error. Please help us make AirPlay better by logging a bug. Thanks."
+ "All"
+ "Cancel"
+ "Failed to create draft in Tap-to-Radar: %@"
+ "Invoking tap-to-radar (noDialogScreen=%d) with radar title: %@ for component %@\n"
+ "MulticastPromotionPending"
+ "Not invoking TTR on non-internal builds\n"
+ "Not invoking Tap-to-Radar because the user has denied authorization"
+ "OSStatus APSAdaptiveLatencyManagerCacheCopyRoleLatencies(APSAdaptiveLatencyManagerCacheRef, CFDataRef, uint32_t, uint32_t, CFDictionaryRef *)"
+ "OSStatus APSAdaptiveLatencyManagerUpdatePacketsExpiredBurstCount(APSAdaptiveLatencyManagerRef, uint32_t, uint64_t)"
+ "OSStatus APSAdaptiveLatencyManagerUpdatePacketsExpiredCount(APSAdaptiveLatencyManagerRef, uint32_t, uint64_t)"
+ "OSStatus alm_UpdateRoleLatencies(APSAdaptiveLatencyManagerRef, Boolean)_block_invoke"
+ "OSStatus hoseControllerAPAT_PrunePacketsWithinRange(APSAudioProtocolDriverSenderHoseControllerAPATRef, APSRTPSeqNumRange, Boolean, Boolean)"
+ "OSStatus hoseControllerAPAT_SetParentControllerCallbacks(APSAudioProtocolDriverSenderHoseControllerAPATRef, const APSAudioProtocolDriverSenderHoseControllerAPATParentControllerCallbacks *, CFTypeRef)"
+ "OSStatus hoseControllerMulticastAPAT_completePromotionInternal(APSAudioProtocolDriverSenderHoseControllerAPATRef, APSAudioProtocolDriverSenderHoseControllerAPATRef)"
+ "OSStatus hoseControllerMulticastAPAT_multicastGroupInfoDidApplyCallback(CFTypeRef, APSAudioProtocolDriverSenderHoseControllerAPATRef, CFDictionaryRef, OSStatus)"
+ "RadarComponent"
+ "RadarDraft"
+ "SupportsTerminus"
+ "Tap-to-Radar"
+ "TapToRadarService"
+ "TapToRadarService does not exist. A radar cannot be started\n"
+ "[%{ptr}] ### Effective TUR length %u exceeds max, clamping"
+ "[%{ptr}] (%@) TUR: %u..<%u, EffectiveTUR: %u..<%u, SendWindow: %@ (async log latency: %1.3f ms)"
+ "[%{ptr}] APSAVCLatencyAnalyzerSetMetricsOffsets endpointID: %u packetsSentCount: %llu packetsReceivedCount: %llu packetsExpiredCount: %llu packetsExpiredBurstCount: %llu packetsLostCount: %llu maxBurstLost: %llu packetsRecoveredCount: %llu"
+ "[%{ptr}] DeregisterHose [%{ptr}]: metricType=%@, usedMulticast=%s, isOnSameMeshAsSender=%s, glitches=%llu, multicastExpectedButUnused=%s"
+ "[%{ptr}] Failed to add seqNum:%hu to RTCPCCFBGenerator, err:%#m (log latency: %1.3f ms)\n"
+ "[%{ptr}] Failed to update LatencyManager packets expired burst count with err %d"
+ "[%{ptr}] HoseController [%{ptr}] failed to setMulticastGroupInfo with err=%d -- staying in unicast"
+ "[%{ptr}] No pending subHoseController [%{ptr}] promotion found"
+ "[%{ptr}] Pending multicast promotion for subHoseController [%{ptr}]"
+ "[%{ptr}] Recorded flushed range %u..<%u, flushed ranges: %@"
+ "[%{ptr}] Skipping old SetMulticastGroupInfo for hoseController [%{ptr}]"
+ "[%{ptr}] endpointID: %@ endpointPacketsExpired: %u numEvicted: %u"
+ "[%{ptr}] endpointID: %@ endpointPacketsExpiredBursts: %u numEvicted: %u"
+ "[%{ptr}] endpointID: %u appended %llu samples to packetsExpiredBurstsWindowSamples"
+ "[%{ptr}] endpointID: %u appended %llu samples to packetsExpiredWindowSamples"
+ "[%{ptr}] hoseControllerAPAT_SetParentControllerCallbacks"
+ "[%{ptr}] updateOnLatencyChange: %s, exceededThreshold: %s, packetsExpiredInWindow: %u, packetsExpiredThreshold: %u, packetsExpiredBurstsInWindow: %u, packetsExpiredBurstThreshold: %u"
+ "almMaxInitialLatencyInfra"
+ "almMaxInitialLatencyP2P"
+ "almMinInitialLatencyInfra"
+ "almMinInitialLatencyP2P"
+ "almPacketsExpiredBurstThreshold"
+ "almPacketsExpiredWindowSec"
+ "alm_AppendWindowSamples"
+ "alm_GetWindowCount"
+ "apsRadarLogging_radarComponentEntryForAPSRadarComponentID_block_invoke"
+ "apsTapToRadarInvokeDetailed"
+ "apsTapToRadarInvokeDetailed_block_invoke"
+ "cachedFrontMs: %u, cachedRearMs: %u, inMinLatency: %u, inMaxLatency: %u"
+ "com.apple.coremedia.CoreMediaDiagnostics.CoreMediaDiagnosticExtension"
+ "hoseControllerAPAT_MulticastGroupInfoDidApply"
+ "hoseControllerMulticastAPATDemotionMinSendPacketCount"
+ "hoseControllerMulticastAPAT_completePromotionInternal"
+ "hoseControllerMulticastAPAT_multicastGroupInfoDidApplyCallback"
+ "nanLatencyThreshold"
+ "nanLocalInfraRatioThreshold"
+ "nanSignalStrengthThreshold"
+ "nanThroughputThreshold"
+ "softlink:o:path:/AppleInternal/Library/Frameworks/TapToRadarKit.framework/TapToRadarKit"
+ "v16@?0@\"NSError\"8"
+ "void apsTapToRadarInvokeDetailed(CFStringRef, CFStringRef, CFStringRef, CFStringRef, CFStringRef, CFStringRef, CFStringRef, CFArrayRef, Boolean)"
+ "void apsTapToRadarInvokeDetailed(CFStringRef, CFStringRef, CFStringRef, CFStringRef, CFStringRef, CFStringRef, CFStringRef, CFArrayRef, Boolean)_block_invoke_2"
+ "void protocolDriverReceiverAPAT_failedToAddSeqNumLogger(const APSAsyncLoggerParameters *, Float64)"
- "###  %@\n"
- "### TapToRadar Invoked on unsupported platform. Details: \n"
- "### inAPSRadarComponentID: %@\n"
- "### inAlertMessageTag:     %@\n"
- "### inDeviceIDs:\n"
- "### inNoDialogScreen:      %d\n"
- "### inRadarDescription:    %@\n"
- "### inRadarTitle:          %@\n"
- "APSAdaptiveLatencyManagerRegisterEndpoint inEndpointID: %u, initialLatencyMs: %u, leadingLatencyMs: %u, trailingLatencyMs: %u, maxNetworkLatencyMs: %u, outStatsInput: [%{ptr}]"
- "OSStatus hoseControllerAPAT_SetFeedbackProcessorCallbacks(APSAudioProtocolDriverSenderHoseControllerAPATRef, const APSAudioProtocolDriverSenderHoseControllerAPATFeedbackProcessorCallbacks *, CFTypeRef)"
- "[%{ptr}] (%@) TUR: %u..<%u, SendWindow: %@ (async log latency: %1.3f ms)"
- "[%{ptr}] APSAVCLatencyAnalyzerSetMetricsOffsets packetsSentCount: %llu packetsReceivedCount: %llu packetsExpiredCount: %llu packetsLostCount: %llu maxBurstLost: %llu packetsRecoveredCount: %llu"
- "[%{ptr}] DeregisterHose [%{ptr}]: metricType=%@, usedMulticast=%s, isOnSameMeshAsSender=%s, glitches=%llu, eligibleForMulticast=%s"
- "[%{ptr}] Failed to add seqNum:%d to RTCPCCFBGenerator, err:%d\n"
- "[%{ptr}] hoseControllerAPAT_SetFeedbackProcessorCallbacks"
- "[%{ptr}] updateOnLatencyChange: %s, exceededPacketsExpiredThreshold: %s, packetsExpiredDelta: %llu, packetsExpiredThreshold: %u"
- "staticDictionary_SetValue"

```
