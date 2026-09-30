## AirPlaySender

> `/System/Library/PrivateFrameworks/AirPlaySender.framework/AirPlaySender`

```diff

-920.10.1.0.0
-  __TEXT.__text: 0x213470
-  __TEXT.__auth_stubs: 0x5610
+925.3.2.0.0
+  __TEXT.__text: 0x214048
+  __TEXT.__auth_stubs: 0x5690
   __TEXT.__objc_methlist: 0x7c4
-  __TEXT.__cstring: 0x833c8
+  __TEXT.__cstring: 0x83732
   __TEXT.__const: 0x10070
   __TEXT.__gcc_except_tab: 0x9a8
   __TEXT.__dlopen_cstrs: 0x671
   __TEXT.__oslogstring: 0x7c5
-  __TEXT.__unwind_info: 0x5230
+  __TEXT.__unwind_info: 0x5240
   __TEXT.__objc_classname: 0x1c5
   __TEXT.__objc_methname: 0x2116
   __TEXT.__objc_methtype: 0xd78
   __TEXT.__objc_stubs: 0x1da0
   __DATA_CONST.__got: 0x1f80
-  __DATA_CONST.__const: 0x6bc8
+  __DATA_CONST.__const: 0x6bd0
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x48

   __DATA_CONST.__objc_selrefs: 0x9b0
   __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_arraydata: 0x88
-  __AUTH_CONST.__auth_got: 0x2b18
+  __AUTH_CONST.__auth_got: 0x2b58
   __AUTH_CONST.__const: 0x7f00
-  __AUTH_CONST.__cfstring: 0x129e0
+  __AUTH_CONST.__cfstring: 0x12be0
   __AUTH_CONST.__objc_const: 0xec0
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_intobj: 0x48

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 027D30DB-9148-3D15-B4FD-B76A422DA6C4
-  Functions: 9774
-  Symbols:   24605
-  CStrings:  13530
+  UUID: BC4ADD99-6A3D-34B6-8265-E6AFD7E72047
+  Functions: 9784
+  Symbols:   24634
+  CStrings:  13571
 
Symbols:
+ _APSAudioHoseMetricCollectorReportBufferLevelEventMetrics
+ _APSAudioHoseMetricCollectorReportPlaybackTimelineMetrics
+ _APSAudioHoseMetricCollectorSetFirstRemoteMediaTime
+ _APSAudioHoseMetricCollectorSetPlaybackTimelineID
+ _APSAudioHoseMetricCollectorUpdateStartupTypeForHose
+ _APSIsAudioWiFiMetricsCollectionEnabled
+ _CFDataAppendBytes
+ _FigCFArrayAppendValue
+ _FigCFArrayRemoveAllValues
+ __MergedGlobals.941
+ ___block_descriptor_tmp.155
+ ___block_descriptor_tmp.345
+ ___block_descriptor_tmp.356
+ ___block_descriptor_tmp.442
+ ___block_descriptor_tmp.460
+ ___block_descriptor_tmp.478
+ ___block_descriptor_tmp.506
+ ___block_descriptor_tmp.516
+ ___block_descriptor_tmp.528
+ ___block_descriptor_tmp.850
+ ___block_descriptor_tmp.853
+ ___block_descriptor_tmp.856
+ ___block_descriptor_tmp.866
+ ___block_descriptor_tmp.883
+ ___block_descriptor_tmp.885
+ ___block_literal_global.347
+ ___block_literal_global.358
+ ___block_literal_global.462
+ ___block_literal_global.508
+ ___block_literal_global.530
+ _bufferedAudioEngine_addHose.cold.4
+ _bufferedAudioEngine_generateNewFirstRemoteMediaTime.cold.4
+ _bufferedAudioEngine_generateNewFirstRemoteMediaTime.cold.5
+ _bufferedAudioEngine_tearDownResumedStateAndStructuresInternal.cold.10
+ _bufferedAudioEngine_tearDownResumedStateAndStructuresInternal.cold.11
+ _bufferedAudioEngine_tearDownResumedStateAndStructuresInternal.cold.4
+ _bufferedAudioEngine_tearDownResumedStateAndStructuresInternal.cold.5
+ _bufferedAudioEngine_tearDownResumedStateAndStructuresInternal.cold.6
+ _bufferedAudioEngine_tearDownResumedStateAndStructuresInternal.cold.7
+ _bufferedAudioEngine_tearDownResumedStateAndStructuresInternal.cold.8
+ _bufferedAudioEngine_tearDownResumedStateAndStructuresInternal.cold.9
+ _kAPEndpointStreamProperty_WifiMetrics
- _APSAudioHoseMetricCollectorReportMetrics
- __MergedGlobals.896
- ___block_descriptor_tmp.152
- ___block_descriptor_tmp.301
- ___block_descriptor_tmp.312
- ___block_descriptor_tmp.397
- ___block_descriptor_tmp.415
- ___block_descriptor_tmp.433
- ___block_descriptor_tmp.438
- ___block_descriptor_tmp.461
- ___block_descriptor_tmp.471
- ___block_descriptor_tmp.805
- ___block_descriptor_tmp.808
- ___block_descriptor_tmp.811
- ___block_descriptor_tmp.821
- ___block_descriptor_tmp.840
- ___block_literal_global.303
- ___block_literal_global.314
- ___block_literal_global.417
- ___block_literal_global.463
- ___block_literal_global.485
CStrings:
+ "2GHzBandCount"
+ "5GHzBandCount"
+ "6GHzBandCount"
+ "6GHzPSCBandCount"
+ "925.3.2"
+ "BAE [%{ptr}] %sGot wifiMetrics [%{ptr}] %@"
+ "Histogram_RSSI"
+ "OSStatus audioStream_setupAudioStream(FigEndpointStreamRef, APSenderSessionRef, Boolean, APSAudioFormatDescriptionRef, CFDataRef, CFStringRef, Boolean, CFNumberRef, Boolean, uint64_t, CFStringRef, CFNumberRef, CFStringRef, CFStringRef, Boolean, APTransportStreamType, CFDataRef, Boolean, APTransportConnectionTransportProtocol, uint64_t *, uint64_t *, Boolean *, int *, int32_t *, int *, CFDictionaryRef *, CFDataRef *)"
+ "OSStatus bufferedAudioEngine_addHose(FigEndpointStreamAudioEngineRef, APSAudioProtocolDriverHoseControlRef, APSEndpointStreamAudioHoseRef, int32_t *)"
+ "OSStatus bufferedAudioEngine_calculateWiFiMetrics(FigEndpointStreamAudioEngineRef, CFMutableDictionaryRef)"
+ "WiFiMetrics"
+ "[%{ptr}] Added wifiMetrics to inReportStats dict %@"
+ "[%{ptr}] Created rssiHistogram [%{ptr}]"
+ "[%{ptr}] The device connected to (discoveryID=%@) did not match the desired device (discoveryID=%@). Ignoring new ID (discoveryID=%@) and using original (discoveryID=%@). This usually indicates two devices with the same bonjour host name."
+ "[%{ptr}] wifiMetrics %@"
+ "bufferedAudioEngine_calculateWiFiMetrics"
+ "bufferedAudioEngine_generateNewFirstRemoteMediaTime"
+ "bufferedAudioEngine_generateNewPlaybackTimelineID"
+ "dBm"
+ "ipV4NetworkSignature"
+ "ipV6NetworkSignature"
+ "rssi"
+ "rssiHistogram"
+ "ssid"
+ "uniqueNetworkSSIDCount"
+ "uniqueNetworkSignatureCount"
+ "wiFiMetrics"
+ "wifiBand"
- "920.10.1"
- "OSStatus audioStream_setupAudioStream(FigEndpointStreamRef, APSenderSessionRef, Boolean, APSAudioFormatDescriptionRef, CFDataRef, CFStringRef, Boolean, CFNumberRef, Boolean, uint64_t, CFStringRef, CFNumberRef, CFStringRef, CFStringRef, Boolean, APTransportStreamType, CFDataRef, Boolean, APTransportConnectionTransportProtocol, uint64_t *, uint64_t *, Boolean *, int *, int32_t *, int *, CFDataRef *)"
- "[%{ptr}] The device connected to (discoveryID=%@) did not match the desired device (discoveryID=%@). This usually indicates two devices with the same bonjour host name.\n"

```
