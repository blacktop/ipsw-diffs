## AirPlaySender

> `/System/Library/PrivateFrameworks/AirPlaySender.framework/Versions/A/AirPlaySender`

```diff

-  __TEXT.__text: 0x1d6f94
+  __TEXT.__text: 0x1d8898
   __TEXT.__objc_methlist: 0x92c
-  __TEXT.__const: 0xd430
+  __TEXT.__const: 0xd4f0
   __TEXT.__gcc_except_tab: 0x5ec
-  __TEXT.__cstring: 0x71aed
+  __TEXT.__cstring: 0x72046
   __TEXT.__dlopen_cstrs: 0x164
   __TEXT.__oslogstring: 0xb29
-  __TEXT.__unwind_info: 0x4468
+  __TEXT.__unwind_info: 0x44a0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x4298
+  __DATA_CONST.__const: 0x4328
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x30

   __DATA_CONST.__objc_selrefs: 0xaf0
   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_arraydata: 0x170
-  __DATA_CONST.__got: 0x1dc0
+  __DATA_CONST.__got: 0x1dd0
   __AUTH_CONST.__const: 0x7390
-  __AUTH_CONST.__cfstring: 0x109a0
+  __AUTH_CONST.__cfstring: 0x10b60
   __AUTH_CONST.__objc_const: 0xc58
   __AUTH_CONST.__objc_intobj: 0x150
   __AUTH_CONST.__objc_dictobj: 0x1b8

   __AUTH.__data: 0x840
   __DATA.__objc_ivar: 0x84
   __DATA.__data: 0x17990
-  __DATA.__bss: 0xe78
+  __DATA.__bss: 0xe80
   __DATA_DIRTY.__data: 0xcf0
   __DATA_DIRTY.__bss: 0x2a8
   - /System/Library/Frameworks/AudioToolbox.framework/Versions/A/AudioToolbox

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 9084
-  Symbols:   13827
-  CStrings:  11423
+  Functions: 9129
+  Symbols:   13890
+  CStrings:  11475
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH.__objc_data : content changed
~ __AUTH.__data : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__data : content changed
Symbols:
+ GCC_except_table129
+ _APEndpointCreateDecoratedName
+ _APTNANDataSessionGetRSSI
+ _APTransportDeviceCopyNANDataSession
+ _APTransportDeviceIsTransportRecommended
+ _CFAppendPrintF
+ _CFDateFormatterCreateISO8601Formatter
+ _CFDateFormatterCreateStringWithAbsoluteTime
+ _CFDateFormatterSetProperty
+ _CFTimeZoneCopySystem
+ _OUTLINED_FUNCTION_262
+ _OUTLINED_FUNCTION_263
+ _OUTLINED_FUNCTION_264
+ _OUTLINED_FUNCTION_265
+ _OUTLINED_FUNCTION_266
+ _OUTLINED_FUNCTION_267
+ _OUTLINED_FUNCTION_268
+ _OUTLINED_FUNCTION_269
+ _OUTLINED_FUNCTION_270
+ _OUTLINED_FUNCTION_271
+ _OUTLINED_FUNCTION_272
+ _OUTLINED_FUNCTION_273
+ _OUTLINED_FUNCTION_274
+ _OUTLINED_FUNCTION_275
+ _OUTLINED_FUNCTION_276
+ _OUTLINED_FUNCTION_277
+ ___apsession_startNANRSSISamplingIfNeeded_block_invoke
+ ___apsession_startNANRSSISamplingIfNeeded_block_invoke_2
+ ___block_descriptor_41_e5_v8?0l
+ ___copy_assignment_8_8_pa0_25192_0_pa0_56546_8_pa0_42274_16
+ ___screenstreamudp_handleClearScreen_block_invoke
+ __screenstreamudp_handleClearScreen_block_invoke
+ _apsession_connectionTypeToTransportDeviceAddressType
+ _apsession_copyNANRSSIHistogramString
+ _apsession_getNANRSSI
+ _endpointCluster_copyDecoratedName
+ _endpoint_copyDecoratedName
+ _kAPEndpointStreamAudioEngineCreationOption_IsCarPlay
+ _kAPSAudioProtocolDriverHoseProperty_SupportsTerminus
+ _kAPSenderSessionCreationOption_IsAuxiliaryScreenSession
+ _kAPSenderSessionProperty_NANRSSIHistogram
+ _kAPSenderSessionStreamKey_MulticastGroupInfo
+ _kCFDateFormatterTimeZone
+ apsession_stopSenderNetworkClockIfNeeded
+ bufferedAudioEngine_maybeTriggerTerminusAcquisitionMissedTTR.sNextDialogTicks
- GCC_except_table128
- screenstreamudp_handleClearScreen
CStrings:
+ "%@ [%@]"
+ "980.67.2"
+ "AirPlay Issue"
+ "BAE [%{ptr}] %sInvoking TTR for terminus acquisition missed\n"
+ "BAE [%{ptr}] %sThrottling terminus acquisition missed TTR\n"
+ "BAE [%{ptr}] %speriodic measured latencies - frontLatency: %u rearLatency: %u; current configured HAL latencies frontMs: %u rearMs: %u\n"
+ "BES [%{ptr}] isTerminusSupported=%s supportsTerminusAPAT=%s\n"
+ "Boolean apsession_isTransportRecommended(APSenderSessionRef, APSenderSessionConnectionType)"
+ "DeviceID: %llu\n"
+ "Endpoint: %@\n"
+ "Error: %#m\n"
+ "IsAuxiliaryScreenSession"
+ "NAN connection attempt failed causing Infra fallback\n\n"
+ "NANRSSIHistogram"
+ "Name: %@\n"
+ "PairedSessionEnded"
+ "Reason: %#{flags}\n"
+ "Sender: %@\n"
+ "Session: %{ptr}\n"
+ "TTR: APSenderSessionAirPlay: NAN Failure with Infra Fallback"
+ "TTR: Terminus Acquisition Missed"
+ "Terminus acquisition missed"
+ "Time: %@\n"
+ "[%{ptr}] %@ is%s recommended?{end} with err=%#m"
+ "[%{ptr}] NAN RSSI sample: %lld dBm (count=%ld)\n"
+ "[%{ptr}] Should perform key exchange: %s\n"
+ "[%{ptr}] Skipping transport recommendation check as usage is not mirroring"
+ "apsession_isTransportRecommended"
+ "apsession_startNANRSSISamplingIfNeeded"
+ "bufferedAudioEngine_maybeTriggerTerminusAcquisitionMissedTTR"
+ "discoveryNANRSSI"
+ "includeTransportTypeInEndpointName"
+ "isAuxiliaryScreenSession"
+ "isCarPlay"
+ "multicastGroupInfo"
+ "nanRSSIHist"
+ "nanRSSIHistogram"
+ "screenstreamudp_handleClearScreenInternal"
+ "setupMulticastGroupInfo"
+ "void apsession_sampleNANRSSI(APSenderSessionRef)"
+ "void bufferedAudioEngine_maybeTriggerTerminusAcquisitionMissedTTR(FigEndpointStreamAudioEngineRef)"
+ "void screenstreamudp_handleClearScreenInternal(CFTypeRef, Boolean)"
- "980.63.2"
- "BAE [%{ptr}] %speriodic measured latencies - frontLatency: %u rearLatency: %u\n"
- "screenstreamudp_handleClearScreen"
- "void screenstreamudp_handleClearScreen(CFTypeRef, Boolean)"

```
