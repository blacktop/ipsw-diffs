## AirPlaySender

> `/System/Library/PrivateFrameworks/AirPlaySender.framework/AirPlaySender`

```diff

-920.5.1.11.1
-  __TEXT.__text: 0x212ef4
-  __TEXT.__auth_stubs: 0x55f0
+920.8.2.0.0
+  __TEXT.__text: 0x21395c
+  __TEXT.__auth_stubs: 0x5610
   __TEXT.__objc_methlist: 0x7c4
-  __TEXT.__cstring: 0x83234
+  __TEXT.__cstring: 0x83219
   __TEXT.__const: 0x10070
   __TEXT.__gcc_except_tab: 0x9a8
   __TEXT.__dlopen_cstrs: 0x671
   __TEXT.__oslogstring: 0x7c5
-  __TEXT.__unwind_info: 0x5240
+  __TEXT.__unwind_info: 0x5248
   __TEXT.__objc_classname: 0x1c5
   __TEXT.__objc_methname: 0x2116
   __TEXT.__objc_methtype: 0xd78
   __TEXT.__objc_stubs: 0x1da0
-  __DATA_CONST.__got: 0x1f78
-  __DATA_CONST.__const: 0x6be0
+  __DATA_CONST.__got: 0x1f80
+  __DATA_CONST.__const: 0x6bc0
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x48

   __DATA_CONST.__objc_selrefs: 0x9b0
   __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_arraydata: 0x88
-  __AUTH_CONST.__auth_got: 0x2b08
+  __AUTH_CONST.__auth_got: 0x2b18
   __AUTH_CONST.__const: 0x7f00
-  __AUTH_CONST.__cfstring: 0x12900
+  __AUTH_CONST.__cfstring: 0x129c0
   __AUTH_CONST.__objc_const: 0xec0
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_intobj: 0x48

   __AUTH.__data: 0x7b0
   __DATA.__objc_ivar: 0x88
   __DATA.__data: 0x186b8
-  __DATA.__bss: 0xaa0
+  __DATA.__bss: 0xa90
   __DATA.__common: 0xa10
   __DATA_DIRTY.__objc_data: 0xa0
   __DATA_DIRTY.__data: 0xcc8
-  __DATA_DIRTY.__bss: 0x2f0
+  __DATA_DIRTY.__bss: 0x300
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CoreAudio.framework/CoreAudio
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7196CAAD-F59A-3500-AFB6-7078A1BE24CB
-  Functions: 9798
-  Symbols:   24657
-  CStrings:  13534
+  UUID: 84A67423-8E52-349F-B60A-85B6A2BAA1B8
+  Functions: 9804
+  Symbols:   24660
+  CStrings:  13522
 
Symbols:
+ GCC_except_table85
+ GCC_except_table88
+ _APSRoundToSignificantFigures
+ _APSenderSessionUtilityCopyGetInfoResponseWithUGLAddressesUpdatedFromSenderSession
+ _APSenderSessionUtilityCopyGetInfoResponseWithUGLAddressesUpdatedFromTransportStream
+ _APTransportStreamCopyConvertedLinkLocalIPv6Addresses
+ _FigSignalErrorAtGM
+ ___block_descriptor_tmp.174
+ ___block_descriptor_tmp.175
+ ___block_descriptor_tmp.196
+ ___block_descriptor_tmp.275
+ ___block_descriptor_tmp.278
+ ___block_descriptor_tmp.314
+ ___block_descriptor_tmp.325
+ ___block_literal_global.600
+ _apEndpoint_handleUpdateInfoCommand
+ _apEndpoint_handleUpdateInfoCommand.cold.1
+ _endpointCluster_metricsTimerFired.cold.1
+ _kAPEndpointProperty_ActualTransportType
+ _kAPSenderSessionActualTransportType_AWDL
+ _kAPSenderSessionActualTransportType_DirectLink
+ _kAPSenderSessionActualTransportType_Infra
+ _kAPSenderSessionActualTransportType_Mixed
+ _kAPSenderSessionActualTransportType_NAN
+ _kAPSenderSessionActualTransportType_None
+ _kAPSenderSessionProperty_ActualTransportType
+ _kFigEndpointProperty_TransportTypeForMetrics
+ _manager_removeAllEndpointsForDictIfNeeded
- GCC_except_table84
- _FigSignalErrorAt3
- ___block_descriptor_tmp.124
- ___block_descriptor_tmp.172
- ___block_descriptor_tmp.223
- ___block_descriptor_tmp.230
- ___block_descriptor_tmp.245
- ___block_descriptor_tmp.252
- ___block_descriptor_tmp.267
- ___block_descriptor_tmp.269
- ___block_descriptor_tmp.308
- ___block_descriptor_tmp.319
- ___block_literal_global.599
- _apsession_ensureConnectedInternal.cold.59
CStrings:
+ "%s signalled err=%d at <>:%d"
+ "920.8.2"
+ "ActualTransportType"
+ "BAE [%{ptr}] %sReceived sample with duration:%1.3f, set nextRemoteMediaTimestamp to duration of the sample: %1.6f (%lld/%d)\n receivedTruncatedSbuf: %s"
+ "BAE [%{ptr}] %s[0x%04X] PrepMsg SBufTimestamp = %1.6f (%lld/%d) SBufOutputTimestamp = %1.6f (%lld/%d) sbufDuration = %1.6f (%lld/%d) sbufEndPTS = %1.6f (%lld/%d) RemoteMediaTimestamp = %1.6f (%lld/%d)\n"
+ "CFDictionaryRef APSenderSessionUtilityCopyGetInfoResponseWithUGLAddressesUpdatedFromTransportStream(FigTransportStreamRef, CFDictionaryRef, LogCategory *, void *)"
+ "Mixed"
+ "OSStatus apEndpoint_handleUpdateInfoCommand(FigEndpointRef, CFDictionaryRef)"
+ "Unhandled connection type when looking for fallback: %@\n"
+ "[%{ptr}] %@ %s available (retry %ld of %ld)\n"
+ "[%{ptr}] %@ not available yet. Waiting and retrying %ld times...\n"
+ "[%{ptr}] <APUGL> Converted addresses: %@\n"
+ "[%{ptr}] <APUGL> Converting addresses if IPv6 link local: %@\n"
+ "[%{ptr}] <APUGL> New info: %@\n"
+ "[%{ptr}] <APUGL> Not removing shadow endpoint [%{ptr}] b/c normal RC endpoint [%{ptr}] still exists & has active UGL session"
+ "[%{ptr}] <APUGL> Replacing getInfo response with new addresses %@\n"
+ "[%{ptr}] <APUGLPort> GetInfo response (usage %s) includes UGL server port: %@\n"
+ "[%{ptr}] <APUGLPort> UpdateInfo payload for local RC includes UGL server port: %@\n"
+ "[%{ptr}] Connect over %@ with %''@ ( preferredConnection = %@, isInfraAvailable = %d, isAWDLAvailable = %d, isNANAvailable = %d )\n"
+ "[%{ptr}] Connection over %@ failed%?{end}, trying again over %@\n"
+ "[%{ptr}] Pair-setup over %@ with %''@ \n"
+ "[%{ptr}] Prefer %@ for connection\n"
+ "[%{ptr}] Updated discovery mode %@ with seed %llu\n"
+ "activationRemoteUncategorizedMs"
+ "apEndpoint_handleUpdateInfoCommand"
- "%s%s%s signalled err=%d (%s) (%s) at %s:%d"
- "920.5.1.11.1"
- "APAudioEngineBufferedAdapter.c"
- "APEndpoint.m"
- "APEndpointPlaybackSessionRemoteControl.m"
- "APEndpointStreamAggregateAudio.c"
- "APVirtualDisplayTestSink.c"
- "Action not supported"
- "Allocation error"
- "BAE [%{ptr}] %sReceived truncated sample (duration:%1.3f), adjust nextRemoteMediaTimestamp to duration of the sample: %1.3f\n"
- "BAE [%{ptr}] %s[0x%04X] PrepMsg SBufTimestamp = %1.6f (%lld/%d) SBufOutputTimestamp = %1.6f (%lld/%d) RemoteMediaTimestamp = %1.6f (%lld/%d)\n"
- "Cannot register path"
- "Failed allocating audio buffer"
- "Failed to create deep copy"
- "Failed to de-serialize"
- "Failed to serialize"
- "Item is NULL"
- "No data in response"
- "No incoming message"
- "No matched request found"
- "Object invalidated"
- "Unhandled connection type when looking for fallback: %s\n"
- "[%{ptr}] %###s Updated discovery mode %@ with seed %llu\n"
- "[%{ptr}] %s %s available (retry %ld of %ld)\n"
- "[%{ptr}] %s not available yet. Waiting and retrying %ld times...\n"
- "[%{ptr}] <APUGLPort> UpdateInfo payload includes UGL server port: %@\n"
- "[%{ptr}] Connect over %s with %''@ ( preferredConnection = %s, isInfraAvailable = %d, isAWDLAvailable = %d, isNANAvailable = %d )\n"
- "[%{ptr}] Connection over %s failed%?{end}, trying again over %s\n"
- "[%{ptr}] Pair-setup over %s with %''@ \n"
- "[%{ptr}] Prefer %s for connection\n"
- "alloc failed"
- "can't find valid video track"
- "err"
- "kCMBaseObjectError_AllocationFailed"
- "kCMBaseObjectError_Invalidated"
- "kCMBaseObjectError_ParamErr"
- "kCMBaseObjectError_ValueNotAvailable"
- "kFigEndpointError_AllocationFailed"
- "kFigEndpointPlaybackSessionError_AllocationFailed"
- "kFigEndpointPlaybackSessionError_InvalidParameter"
- "kFigEndpointStreamAudioEngineError_AllocationFailed"
- "messageID is missing in response event"
- "type is missing in response event"

```
