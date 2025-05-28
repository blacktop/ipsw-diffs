## AirPlayReceiver

> `/System/Library/PrivateFrameworks/AirPlayReceiver.framework/AirPlayReceiver`

```diff

-755.3.1.0.0
-  __TEXT.__text: 0x138e54
-  __TEXT.__auth_stubs: 0x3510
+760.20.1.0.0
+  __TEXT.__text: 0x143f38
+  __TEXT.__auth_stubs: 0x3540
   __TEXT.__objc_methlist: 0x910
-  __TEXT.__const: 0x30a76
+  __TEXT.__const: 0x325ce
   __TEXT.__gcc_except_tab: 0x30c
-  __TEXT.__cstring: 0x2b6bf
-  __TEXT.__unwind_info: 0x13dc
-  __TEXT.__eh_frame: 0x50
+  __TEXT.__cstring: 0x2b7cc
+  __TEXT.__unwind_info: 0x22c4
+  __TEXT.__eh_frame: 0x1c68
   __TEXT.__objc_classname: 0x144
-  __TEXT.__objc_methname: 0x2635
-  __TEXT.__objc_methtype: 0x1414
+  __TEXT.__objc_methname: 0x2649
+  __TEXT.__objc_methtype: 0x142a
   __TEXT.__objc_stubs: 0x2780
-  __DATA_CONST.__got: 0x708
-  __DATA_CONST.__const: 0x2c50
+  __DATA_CONST.__got: 0x730
+  __DATA_CONST.__const: 0x1d18
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x1330
   __DATA_CONST.__objc_selrefs: 0xab0
+  __DATA_CONST.__objc_protorefs: 0x8
+  __DATA_CONST.__objc_classrefs: 0x180
+  __DATA_CONST.__objc_superrefs: 0x40
   __DATA_CONST.__objc_arraydata: 0x10
   __AUTH_CONST.__auth_ptr: 0x18
-  __AUTH_CONST.__const: 0xa110
-  __AUTH_CONST.__cfstring: 0xa220
+  __AUTH_CONST.__const: 0xb698
+  __AUTH_CONST.__cfstring: 0xa2c0
   __AUTH_CONST.__objc_const: 0x438
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__auth_got: 0x1a98
+  __AUTH_CONST.__auth_got: 0x1ab0
   __AUTH.__objc_data: 0x370
   __AUTH.__data: 0x188
-  __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0x180
-  __DATA.__objc_superrefs: 0x40
   __DATA.__objc_ivar: 0x168
-  __DATA.__data: 0x177b0
-  __DATA.__common: 0x9fc
-  __DATA.__bss: 0x628
+  __DATA.__data: 0x17818
+  __DATA.__bss: 0x638
+  __DATA.__common: 0xa10
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1540
-  Symbols:   4891
-  CStrings:  5127
+  Functions: 1553
+  Symbols:   4908
+  CStrings:  5137
 
Symbols:
+ GCC_except_table1014
+ GCC_except_table1033
+ GCC_except_table1084
+ GCC_except_table1088
+ GCC_except_table1143
+ GCC_except_table1153
+ _APReceiverRequestProcessorCopyProperty.3802
+ _APReceiverRequestProcessorCopyProperty.6721
+ _APReceiverRequestProcessorCopyProperty.7136
+ _APReceiverRequestProcessorSetProperty.4309
+ _APSIsSetMRInfoCommandEnabled
+ _APTransportConnectionTCPUnbufferedNWCreate
+ _CMBaseObjectNotificationBarrier.3139
+ _VLxCLgDpiF
+ __Finalize.6053
+ __GetTypeID.6050
+ __UpdateAVAudioSessionAudioMode.5177
+ ___APReceiverMediaRemoteXPCService_copyProperty_block_invoke
+ ___Block_byref_object_copy_.2732
+ ___Block_byref_object_dispose_.2733
+ ___block_descriptor_tmp.125
+ ___block_descriptor_tmp.132
+ ___block_descriptor_tmp.133
+ ___block_descriptor_tmp.2183
+ ___block_descriptor_tmp.230
+ ___block_descriptor_tmp.268
+ ___block_descriptor_tmp.276
+ ___block_descriptor_tmp.284
+ ___block_descriptor_tmp.3074
+ ___block_descriptor_tmp.3132
+ ___block_descriptor_tmp.317
+ ___block_descriptor_tmp.319
+ ___block_descriptor_tmp.321
+ ___block_descriptor_tmp.323
+ ___block_descriptor_tmp.325
+ ___block_descriptor_tmp.3360
+ ___block_descriptor_tmp.347
+ ___block_descriptor_tmp.35.6785
+ ___block_descriptor_tmp.3568
+ ___block_descriptor_tmp.3679
+ ___block_descriptor_tmp.3799
+ ___block_descriptor_tmp.383
+ ___block_descriptor_tmp.392
+ ___block_descriptor_tmp.49.3702
+ ___block_descriptor_tmp.5079
+ ___block_descriptor_tmp.5626
+ ___block_descriptor_tmp.57.3096
+ ___block_descriptor_tmp.57.839
+ ___block_descriptor_tmp.5805
+ ___block_descriptor_tmp.607
+ ___block_descriptor_tmp.6700
+ ___block_descriptor_tmp.6788
+ ___block_descriptor_tmp.681
+ ___block_descriptor_tmp.7089
+ ___block_descriptor_tmp.716
+ ___block_descriptor_tmp.718
+ ___block_descriptor_tmp.834
+ ___block_literal_global.112.838
+ ___block_literal_global.1424
+ ___block_literal_global.1986
+ ___block_literal_global.2287
+ ___block_literal_global.2705
+ ___block_literal_global.3072
+ ___block_literal_global.3192
+ ___block_literal_global.3241
+ ___block_literal_global.3566
+ ___block_literal_global.3677
+ ___block_literal_global.388
+ ___block_literal_global.436
+ ___block_literal_global.5348
+ ___block_literal_global.5572
+ ___block_literal_global.5624
+ ___block_literal_global.649
+ ___block_literal_global.6774
+ ___block_literal_global.7087
+ ___block_literal_global.832
+ _audioSessionBufferedHose_handleAudioDataConnectionEvent
+ _audioSession_audioDecoderDecodeCallback.5896
+ _audioSession_audioDecoderDecodeFrame.5883
+ _audioSession_handleMediaDataControlRequest.3580
+ _audioSession_handleMediaDataControlRequest.5774
+ _audioSession_log.5908
+ _audioSession_networkThread.5918
+ _audioSession_performPeriodicTasks.5913
+ _audioSession_sessionLock.5809
+ _audioSession_sessionUnlock.5811
+ _controlServer_acceptConnection.sOne
+ _gAirTunesRelativeTimeOffset.5937
+ _kAPRRemoteControlSessionMediaRemoteVTable.3108
+ _kAPRRemoteControlSessionMediaRemote_Class.3124
+ _kAPRRemoteControlSessionSession_BaseClassWrapper.3137
+ _kAPTransportConnectionPackageType_BufferedAPAP
+ _kAPTransportConnectionPackageType_RTPBuffered
+ _kAPTransportConnectionProperty_BBufBackingAllocator
+ _kAPTransportConnectionProperty_LocalNetworkPort
+ _kAPTransportConnectionProperty_ShouldReceivePackages
+ _malloc
+ _setsockopt
- GCC_except_table1012
- GCC_except_table1031
- GCC_except_table1082
- GCC_except_table1086
- GCC_except_table1141
- GCC_except_table1149
- _APReceiverRequestProcessorCopyProperty.3795
- _APReceiverRequestProcessorCopyProperty.6720
- _APReceiverRequestProcessorCopyProperty.7137
- _APReceiverRequestProcessorSetProperty.4293
- _CMBaseObjectNotificationBarrier.3137
- __Finalize.6031
- __GetTypeID.6028
- __UpdateAVAudioSessionAudioMode.5155
- ___Block_byref_object_copy_.2731
- ___Block_byref_object_dispose_.2732
- ___block_descriptor_tmp.122
- ___block_descriptor_tmp.129
- ___block_descriptor_tmp.130
- ___block_descriptor_tmp.2182
- ___block_descriptor_tmp.225
- ___block_descriptor_tmp.263
- ___block_descriptor_tmp.271
- ___block_descriptor_tmp.279
- ___block_descriptor_tmp.3072
- ___block_descriptor_tmp.312
- ___block_descriptor_tmp.3130
- ___block_descriptor_tmp.314
- ___block_descriptor_tmp.316
- ___block_descriptor_tmp.318
- ___block_descriptor_tmp.320
- ___block_descriptor_tmp.342
- ___block_descriptor_tmp.35.6786
- ___block_descriptor_tmp.3561
- ___block_descriptor_tmp.3672
- ___block_descriptor_tmp.378
- ___block_descriptor_tmp.3792
- ___block_descriptor_tmp.386
- ___block_descriptor_tmp.49.3695
- ___block_descriptor_tmp.5057
- ___block_descriptor_tmp.5604
- ___block_descriptor_tmp.57.3094
- ___block_descriptor_tmp.57.836
- ___block_descriptor_tmp.5783
- ___block_descriptor_tmp.602
- ___block_descriptor_tmp.6699
- ___block_descriptor_tmp.676
- ___block_descriptor_tmp.6789
- ___block_descriptor_tmp.7090
- ___block_descriptor_tmp.711
- ___block_descriptor_tmp.713
- ___block_descriptor_tmp.831
- ___block_literal_global.112.835
- ___block_literal_global.1423
- ___block_literal_global.1981
- ___block_literal_global.2286
- ___block_literal_global.2704
- ___block_literal_global.3070
- ___block_literal_global.3190
- ___block_literal_global.3239
- ___block_literal_global.3559
- ___block_literal_global.3670
- ___block_literal_global.382
- ___block_literal_global.432
- ___block_literal_global.5326
- ___block_literal_global.5550
- ___block_literal_global.5602
- ___block_literal_global.645
- ___block_literal_global.6775
- ___block_literal_global.7088
- ___block_literal_global.829
- _audioSession_audioDecoderDecodeCallback.5874
- _audioSession_audioDecoderDecodeFrame.5861
- _audioSession_handleMediaDataControlRequest.3573
- _audioSession_handleMediaDataControlRequest.5752
- _audioSession_log.5886
- _audioSession_networkThread.5896
- _audioSession_performPeriodicTasks.5891
- _audioSession_sessionLock.5787
- _audioSession_sessionUnlock.5789
- _gAirTunesRelativeTimeOffset.5915
- _kAPRRemoteControlSessionMediaRemoteVTable.3106
- _kAPRRemoteControlSessionMediaRemote_Class.3122
- _kAPRRemoteControlSessionSession_BaseClassWrapper.3135
CStrings:
+ "*** HTTP connection from %##a closed [%{ptr}], last request ID 0x%04llX\n"
+ "760.20.1"
+ "APReceiverMediaRemoteXPCService_copyProperty_block_invoke"
+ "AirPlay/760.20.1"
+ "BufferedNW"
+ "MRInfo"
+ "T@\"NSString\",?,R,C"
+ "[%{ptr}] Posting MRInfo did change"
+ "^{AirPlayReceiverSessionPrivate={__CFRuntimeBase=QAQ}@^{AirPlayReceiverServerPrivate}^{OpaqueAPReceiverRequestProcessor}^{APReceiverSessionManagerOpaque}^v{?=^v^v^?^?^?^?^?^?}[32c][17c]^{OpaqueAPReceiverStatsCollector}@I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})[16C]iQ[6C]^{__CFString}CC^{__CFString}^{__CFString}^{__CFString}^{__CFString}QIQQ{?=^{_CCCryptor}[16C]}^{?}[16C][16C]CCC^{OpaqueAPSNetworkClock}CCC^{HTTPClientPrivate}Iiii^{APPairingServicesPrivate}iIIQQQIQiiC^{__CFDictionary}^{APReceiverAudioSessionPrivate}I^{OpaqueFigValeria}^{OpaqueAPReceiverUIController}I^{OpaqueAPReceiverScreenSession}dCCI^{__CFString}CCCCCQ^{__CFDictionary}^{__CFArray}fCICd^{__CFDictionary}^{__CFSet}CCC^{__CFData}}"
+ "audioSessionBufferedHose_handleAudioDataConnectionEvent"
+ "com.apple.airplay.mrInfoDidChange"
+ "disableTTRNoThrottling"
+ "mrInfo"
+ "setMRInfo"
+ "v32@0:8^{AirPlayReceiverSessionPrivate={__CFRuntimeBase=QAQ}@^{AirPlayReceiverServerPrivate}^{OpaqueAPReceiverRequestProcessor}^{APReceiverSessionManagerOpaque}^v{?=^v^v^?^?^?^?^?^?}[32c][17c]^{OpaqueAPReceiverStatsCollector}@I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})[16C]iQ[6C]^{__CFString}CC^{__CFString}^{__CFString}^{__CFString}^{__CFString}QIQQ{?=^{_CCCryptor}[16C]}^{?}[16C][16C]CCC^{OpaqueAPSNetworkClock}CCC^{HTTPClientPrivate}Iiii^{APPairingServicesPrivate}iIIQQQIQiiC^{__CFDictionary}^{APReceiverAudioSessionPrivate}I^{OpaqueFigValeria}^{OpaqueAPReceiverUIController}I^{OpaqueAPReceiverScreenSession}dCCI^{__CFString}CCCCCQ^{__CFDictionary}^{__CFArray}fCICd^{__CFDictionary}^{__CFSet}CCC^{__CFData}}16i24i28"
- "*** HTTP connection from %##a closed [%{ptr}]\n"
- "755.3.1"
- "AirPlay/755.3.1"
- "^{AirPlayReceiverSessionPrivate={__CFRuntimeBase=QAQ}@^{AirPlayReceiverServerPrivate}^{OpaqueAPReceiverRequestProcessor}^{APReceiverSessionManagerOpaque}^v{?=^v^v^?^?^?^?^?^?}[32c][17c]^{OpaqueAPReceiverStatsCollector}@I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})[16C]iQ[6C]^{__CFString}CC^{__CFString}^{__CFString}^{__CFString}^{__CFString}QIQQ{?=^{_CCCryptor}[16C]}^{?}[16C][16C]CCC^{OpaqueAPSNetworkClock}CCC^{HTTPClientPrivate}Iiii^{APPairingServicesPrivate}iIIQQQIQiiC^{__CFDictionary}^{APReceiverAudioSessionPrivate}I^{OpaqueFigValeria}^{OpaqueAPReceiverUIController}I^{OpaqueAPReceiverScreenSession}dCCI^{__CFString}CCCCCQ^{__CFDictionary}^{__CFArray}fCICd^{__CFDictionary}^{__CFSet}CCC}"
- "v32@0:8^{AirPlayReceiverSessionPrivate={__CFRuntimeBase=QAQ}@^{AirPlayReceiverServerPrivate}^{OpaqueAPReceiverRequestProcessor}^{APReceiverSessionManagerOpaque}^v{?=^v^v^?^?^?^?^?^?}[32c][17c]^{OpaqueAPReceiverStatsCollector}@I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})[16C]iQ[6C]^{__CFString}CC^{__CFString}^{__CFString}^{__CFString}^{__CFString}QIQQ{?=^{_CCCryptor}[16C]}^{?}[16C][16C]CCC^{OpaqueAPSNetworkClock}CCC^{HTTPClientPrivate}Iiii^{APPairingServicesPrivate}iIIQQQIQiiC^{__CFDictionary}^{APReceiverAudioSessionPrivate}I^{OpaqueFigValeria}^{OpaqueAPReceiverUIController}I^{OpaqueAPReceiverScreenSession}dCCI^{__CFString}CCCCCQ^{__CFDictionary}^{__CFArray}fCICd^{__CFDictionary}^{__CFSet}CCC}16i24i28"

```
