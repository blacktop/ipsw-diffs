## AirPlayReceiver

> `/System/Library/PrivateFrameworks/AirPlayReceiver.framework/Versions/A/AirPlayReceiver`

```diff

-850.19.1.0.0
-  __TEXT.__text: 0xd2cc4
+860.3.1.0.0
+  __TEXT.__text: 0xd2d80
   __TEXT.__auth_stubs: 0x3370
   __TEXT.__objc_methlist: 0x8e4
   __TEXT.__const: 0xd2c5
   __TEXT.__dlopen_cstrs: 0xad
   __TEXT.__gcc_except_tab: 0x710
-  __TEXT.__cstring: 0x27556
-  __TEXT.__unwind_info: 0x1080
+  __TEXT.__cstring: 0x275d3
+  __TEXT.__unwind_info: 0x1088
   __TEXT.__objc_classname: 0x12c
   __TEXT.__objc_methname: 0x1e06
-  __TEXT.__objc_methtype: 0x1480
+  __TEXT.__objc_methtype: 0x1482
   __TEXT.__objc_stubs: 0x1e60
   __DATA_CONST.__got: 0x718
   __DATA_CONST.__const: 0x15d8

   __DATA_CONST.__objc_arraydata: 0x10
   __AUTH_CONST.__auth_got: 0x19c8
   __AUTH_CONST.__const: 0x4b28
-  __AUTH_CONST.__cfstring: 0x9be0
+  __AUTH_CONST.__cfstring: 0x9c20
   __AUTH_CONST.__objc_const: 0x1338
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0x320

   - /System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/Versions/A/WiFiPeerToPeer
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1264
-  Symbols:   3275
-  CStrings:  4614
+  Functions: 1265
+  Symbols:   3276
+  CStrings:  4617
 
Symbols:
+ APReceiverRequestProcessorCopyProperty.3351
+ APReceiverRequestProcessorCopyProperty.6230
+ APReceiverRequestProcessorCopyProperty.6686
+ APReceiverRequestProcessorSetProperty.3860
+ GCC_except_table1000
+ GCC_except_table1008
+ GCC_except_table1010
+ GCC_except_table874
+ GCC_except_table893
+ GCC_except_table944
+ GCC_except_table948
+ _APReceiverMediaRemoteXPCService_copyPropertyFromMRSession
+ _Finalize.5538
+ _GetTypeID.5535
+ ___APReceiverMediaRemoteXPCService_copyPropertyFromMRSession_block_invoke
+ __block_descriptor_tmp.167.5436
+ __block_descriptor_tmp.231
+ __block_descriptor_tmp.269
+ __block_descriptor_tmp.281
+ __block_descriptor_tmp.291
+ __block_descriptor_tmp.3103
+ __block_descriptor_tmp.3219
+ __block_descriptor_tmp.324
+ __block_descriptor_tmp.326
+ __block_descriptor_tmp.328
+ __block_descriptor_tmp.330
+ __block_descriptor_tmp.332
+ __block_descriptor_tmp.3346
+ __block_descriptor_tmp.354
+ __block_descriptor_tmp.387
+ __block_descriptor_tmp.5133
+ __block_descriptor_tmp.5312
+ __block_descriptor_tmp.6210
+ __block_descriptor_tmp.625
+ __block_descriptor_tmp.6301
+ __block_descriptor_tmp.6611
+ __block_descriptor_tmp.719
+ __block_descriptor_tmp.755
+ __block_descriptor_tmp.759
+ __block_literal_global.3101
+ __block_literal_global.3217
+ __block_literal_global.5071
+ __block_literal_global.5131
+ __block_literal_global.6285
+ __block_literal_global.6609
+ audioSession_audioDecoderDecodeCallback.5397
+ audioSession_audioDecoderDecodeFrame.5384
+ audioSession_handleMediaDataControlRequest.3115
+ audioSession_handleMediaDataControlRequest.5286
+ audioSession_log.5409
+ audioSession_networkThread.5419
+ audioSession_performPeriodicTasks.5414
+ audioSession_sessionLock.5316
+ audioSession_sessionUnlock.5318
+ gAirTunesRelativeTimeOffset.5439
- APReceiverRequestProcessorCopyProperty.3349
- APReceiverRequestProcessorCopyProperty.6226
- APReceiverRequestProcessorCopyProperty.6682
- APReceiverRequestProcessorSetProperty.3858
- GCC_except_table1007
- GCC_except_table1009
- GCC_except_table873
- GCC_except_table892
- GCC_except_table943
- GCC_except_table947
- GCC_except_table999
- _Finalize.5534
- _GetTypeID.5531
- ___APReceiverMediaRemoteXPCService_copyProperty_block_invoke
- __block_descriptor_tmp.167.5432
- __block_descriptor_tmp.228
- __block_descriptor_tmp.266
- __block_descriptor_tmp.278
- __block_descriptor_tmp.288
- __block_descriptor_tmp.3101
- __block_descriptor_tmp.321
- __block_descriptor_tmp.3217
- __block_descriptor_tmp.323
- __block_descriptor_tmp.325
- __block_descriptor_tmp.327
- __block_descriptor_tmp.329
- __block_descriptor_tmp.3344
- __block_descriptor_tmp.351
- __block_descriptor_tmp.384
- __block_descriptor_tmp.5129
- __block_descriptor_tmp.5308
- __block_descriptor_tmp.6207
- __block_descriptor_tmp.622
- __block_descriptor_tmp.6297
- __block_descriptor_tmp.6607
- __block_descriptor_tmp.716
- __block_descriptor_tmp.752
- __block_descriptor_tmp.756
- __block_literal_global.3099
- __block_literal_global.3215
- __block_literal_global.5067
- __block_literal_global.5127
- __block_literal_global.6281
- __block_literal_global.6605
- audioSession_audioDecoderDecodeCallback.5393
- audioSession_audioDecoderDecodeFrame.5380
- audioSession_handleMediaDataControlRequest.3113
- audioSession_handleMediaDataControlRequest.5282
- audioSession_log.5405
- audioSession_networkThread.5415
- audioSession_performPeriodicTasks.5410
- audioSession_sessionLock.5312
- audioSession_sessionUnlock.5314
- gAirTunesRelativeTimeOffset.5435
CStrings:
+ "860.3.1"
+ "APReceiverMediaRemoteXPCService_copyPropertyFromMRSession"
+ "APReceiverMediaRemoteXPCService_copyPropertyFromMRSession_block_invoke"
+ "ParentGroupSupportsGroupCohesion"
+ "^{AirPlayReceiverSessionPrivate={__CFRuntimeBase=QAQ}@^{AirPlayReceiverServerPrivate}^{OpaqueAPReceiverRequestProcessor}^{APReceiverSessionManagerOpaque}^v{?=^v^v^?^?^?^?^?^?}[32c][17c]^{OpaqueAPReceiverStatsCollector}@I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})[16C]iQ[6C]^{__CFString}^{__CFString}^{__CFString}^{__CFString}^{__CFString}QIQQ{?=^{_CCCryptor}[16C]}^{?}[16C][16C]C^vCC^{OpaqueAPSNetworkClock}CCC^{HTTPClientPrivate}Iiii^{APPairingServicesPrivate}iIIQQQIQiiC^{__CFDictionary}^{APReceiverAudioSessionPrivate}I^{OpaqueFigValeria}^{OpaqueAPReceiverUIController}I^{OpaqueAPReceiverScreenSession}dCCI^{OpaqueFigPWDKeyExchangeReceiver}^{__CFString}CCCCCQ^{__CFDictionary}^{__CFArray}fCICd^{__CFDictionary}^{__CFSet}CCC^{__CFData}C}"
+ "supportsGroupCohesion"
+ "v32@0:8^{AirPlayReceiverSessionPrivate={__CFRuntimeBase=QAQ}@^{AirPlayReceiverServerPrivate}^{OpaqueAPReceiverRequestProcessor}^{APReceiverSessionManagerOpaque}^v{?=^v^v^?^?^?^?^?^?}[32c][17c]^{OpaqueAPReceiverStatsCollector}@I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})[16C]iQ[6C]^{__CFString}^{__CFString}^{__CFString}^{__CFString}^{__CFString}QIQQ{?=^{_CCCryptor}[16C]}^{?}[16C][16C]C^vCC^{OpaqueAPSNetworkClock}CCC^{HTTPClientPrivate}Iiii^{APPairingServicesPrivate}iIIQQQIQiiC^{__CFDictionary}^{APReceiverAudioSessionPrivate}I^{OpaqueFigValeria}^{OpaqueAPReceiverUIController}I^{OpaqueAPReceiverScreenSession}dCCI^{OpaqueFigPWDKeyExchangeReceiver}^{__CFString}CCCCCQ^{__CFDictionary}^{__CFArray}fCICd^{__CFDictionary}^{__CFSet}CCC^{__CFData}C}16i24i28"
- "850.19.1"
- "APReceiverMediaRemoteXPCService_copyProperty_block_invoke"
- "^{AirPlayReceiverSessionPrivate={__CFRuntimeBase=QAQ}@^{AirPlayReceiverServerPrivate}^{OpaqueAPReceiverRequestProcessor}^{APReceiverSessionManagerOpaque}^v{?=^v^v^?^?^?^?^?^?}[32c][17c]^{OpaqueAPReceiverStatsCollector}@I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})[16C]iQ[6C]^{__CFString}^{__CFString}^{__CFString}^{__CFString}^{__CFString}QIQQ{?=^{_CCCryptor}[16C]}^{?}[16C][16C]C^vCC^{OpaqueAPSNetworkClock}CCC^{HTTPClientPrivate}Iiii^{APPairingServicesPrivate}iIIQQQIQiiC^{__CFDictionary}^{APReceiverAudioSessionPrivate}I^{OpaqueFigValeria}^{OpaqueAPReceiverUIController}I^{OpaqueAPReceiverScreenSession}dCCI^{OpaqueFigPWDKeyExchangeReceiver}^{__CFString}CCCCCQ^{__CFDictionary}^{__CFArray}fCICd^{__CFDictionary}^{__CFSet}CCC^{__CFData}}"
- "v32@0:8^{AirPlayReceiverSessionPrivate={__CFRuntimeBase=QAQ}@^{AirPlayReceiverServerPrivate}^{OpaqueAPReceiverRequestProcessor}^{APReceiverSessionManagerOpaque}^v{?=^v^v^?^?^?^?^?^?}[32c][17c]^{OpaqueAPReceiverStatsCollector}@I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})[16C]iQ[6C]^{__CFString}^{__CFString}^{__CFString}^{__CFString}^{__CFString}QIQQ{?=^{_CCCryptor}[16C]}^{?}[16C][16C]C^vCC^{OpaqueAPSNetworkClock}CCC^{HTTPClientPrivate}Iiii^{APPairingServicesPrivate}iIIQQQIQiiC^{__CFDictionary}^{APReceiverAudioSessionPrivate}I^{OpaqueFigValeria}^{OpaqueAPReceiverUIController}I^{OpaqueAPReceiverScreenSession}dCCI^{OpaqueFigPWDKeyExchangeReceiver}^{__CFString}CCCCCQ^{__CFDictionary}^{__CFArray}fCICd^{__CFDictionary}^{__CFSet}CCC^{__CFData}}16i24i28"

```
