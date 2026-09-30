## AirPlayReceiver

> `/System/Library/PrivateFrameworks/AirPlayReceiver.framework/AirPlayReceiver`

```diff

-890.79.1.2.0
-  __TEXT.__text: 0x14cd2c
+920.5.1.11.1
+  __TEXT.__text: 0x14ce40
   __TEXT.__auth_stubs: 0x3820
   __TEXT.__objc_methlist: 0xad4
   __TEXT.__const: 0x32335
   __TEXT.__dlopen_cstrs: 0xad
   __TEXT.__gcc_except_tab: 0x7e8
-  __TEXT.__cstring: 0x2f832
+  __TEXT.__cstring: 0x2f8e4
   __TEXT.__unwind_info: 0x1478
   __TEXT.__eh_frame: 0x80
   __TEXT.__objc_classname: 0x144
   __TEXT.__objc_methname: 0x2756
   __TEXT.__objc_methtype: 0x1605
   __TEXT.__objc_stubs: 0x2880
-  __DATA_CONST.__got: 0x870
+  __DATA_CONST.__got: 0x880
   __DATA_CONST.__const: 0x1dd8
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0x18

   __DATA_CONST.__objc_arraydata: 0x10
   __AUTH_CONST.__auth_got: 0x1c20
   __AUTH_CONST.__const: 0xaf08
-  __AUTH_CONST.__cfstring: 0xaf80
+  __AUTH_CONST.__cfstring: 0xaf60
   __AUTH_CONST.__objc_const: 0x1530
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0x280

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 247EDD5C-DE9E-3965-BBF5-3A8C1080533A
+  UUID: 714A9559-51B0-365D-8726-0CBE9F66B502
   Functions: 1591
-  Symbols:   5091
-  CStrings:  6871
+  Symbols:   5093
+  CStrings:  6872
 
Symbols:
+ _APReceiverRequestProcessorCopyProperty.3962
+ _APReceiverRequestProcessorCopyProperty.7069
+ _APReceiverRequestProcessorCopyProperty.7557
+ _APReceiverRequestProcessorSetProperty.4525
+ _CMBaseObjectNotificationBarrier.3338
+ __Finalize.2412
+ __Finalize.6349
+ __GetTypeID.6346
+ __UpdateAVAudioSessionAudioMode.5448
+ ___Block_byref_object_copy_.2919
+ ___Block_byref_object_dispose_.2920
+ ___block_descriptor_tmp.1007
+ ___block_descriptor_tmp.107.1047
+ ___block_descriptor_tmp.143.5320
+ ___block_descriptor_tmp.171.6229
+ ___block_descriptor_tmp.172.6230
+ ___block_descriptor_tmp.2327
+ ___block_descriptor_tmp.29.3313
+ ___block_descriptor_tmp.3270
+ ___block_descriptor_tmp.3331
+ ___block_descriptor_tmp.3486
+ ___block_descriptor_tmp.3706
+ ___block_descriptor_tmp.3824
+ ___block_descriptor_tmp.3958
+ ___block_descriptor_tmp.42.7142
+ ___block_descriptor_tmp.49.3847
+ ___block_descriptor_tmp.52.3292
+ ___block_descriptor_tmp.52.7482
+ ___block_descriptor_tmp.5345
+ ___block_descriptor_tmp.5911
+ ___block_descriptor_tmp.60.3295
+ ___block_descriptor_tmp.6101
+ ___block_descriptor_tmp.7048
+ ___block_descriptor_tmp.7145
+ ___block_descriptor_tmp.7475
+ ___block_literal_global.1005
+ ___block_literal_global.1622
+ ___block_literal_global.2143
+ ___block_literal_global.2441
+ ___block_literal_global.2892
+ ___block_literal_global.3268
+ ___block_literal_global.3350
+ ___block_literal_global.3704
+ ___block_literal_global.3822
+ ___block_literal_global.561
+ ___block_literal_global.5630
+ ___block_literal_global.5852
+ ___block_literal_global.5909
+ ___block_literal_global.7128
+ ___block_literal_global.7473
+ ___block_literal_global.847
+ ___kCFBooleanFalse
+ _audioSession_audioDecoderDecodeCallback.6191
+ _audioSession_audioDecoderDecodeFrame.6178
+ _audioSession_handleMediaDataControlRequest.3718
+ _audioSession_handleMediaDataControlRequest.6068
+ _audioSession_log.6202
+ _audioSession_networkThread.6212
+ _audioSession_performPeriodicTasks.6207
+ _audioSession_sessionLock.6105
+ _audioSession_sessionUnlock.6107
+ _gAirTunesRelativeTimeOffset.6233
+ _kAPRRemoteControlSessionMediaRemoteVTable.3306
+ _kAPRRemoteControlSessionMediaRemote_Class.3323
+ _kAPRRemoteControlSessionSession_BaseClassWrapper.3336
+ _kMXSessionProperty_IsEligibleForNowPlayingAppConsideration
- _APReceiverRequestProcessorCopyProperty.3957
- _APReceiverRequestProcessorCopyProperty.7065
- _APReceiverRequestProcessorCopyProperty.7553
- _APReceiverRequestProcessorSetProperty.4520
- _CMBaseObjectNotificationBarrier.3333
- __Finalize.2415
- __Finalize.6344
- __GetTypeID.6341
- __UpdateAVAudioSessionAudioMode.5443
- ___Block_byref_object_copy_.2914
- ___Block_byref_object_dispose_.2915
- ___block_descriptor_tmp.107.1039
- ___block_descriptor_tmp.143.5315
- ___block_descriptor_tmp.171.6224
- ___block_descriptor_tmp.172.6225
- ___block_descriptor_tmp.2330
- ___block_descriptor_tmp.29.3308
- ___block_descriptor_tmp.3265
- ___block_descriptor_tmp.3326
- ___block_descriptor_tmp.3481
- ___block_descriptor_tmp.3701
- ___block_descriptor_tmp.3819
- ___block_descriptor_tmp.3953
- ___block_descriptor_tmp.42.7138
- ___block_descriptor_tmp.49.3842
- ___block_descriptor_tmp.52.3287
- ___block_descriptor_tmp.52.7478
- ___block_descriptor_tmp.5340
- ___block_descriptor_tmp.5906
- ___block_descriptor_tmp.60.3290
- ___block_descriptor_tmp.6096
- ___block_descriptor_tmp.7044
- ___block_descriptor_tmp.7141
- ___block_descriptor_tmp.7471
- ___block_descriptor_tmp.999
- ___block_literal_global.1616
- ___block_literal_global.2141
- ___block_literal_global.2444
- ___block_literal_global.2887
- ___block_literal_global.3263
- ___block_literal_global.3345
- ___block_literal_global.3699
- ___block_literal_global.3817
- ___block_literal_global.5625
- ___block_literal_global.564
- ___block_literal_global.5847
- ___block_literal_global.5904
- ___block_literal_global.7124
- ___block_literal_global.7469
- ___block_literal_global.839
- ___block_literal_global.997
- _audioSession_audioDecoderDecodeCallback.6186
- _audioSession_audioDecoderDecodeFrame.6173
- _audioSession_handleMediaDataControlRequest.3713
- _audioSession_handleMediaDataControlRequest.6063
- _audioSession_log.6197
- _audioSession_networkThread.6207
- _audioSession_performPeriodicTasks.6202
- _audioSession_sessionLock.6100
- _audioSession_sessionUnlock.6102
- _gAirTunesRelativeTimeOffset.6228
- _kAPRRemoteControlSessionMediaRemoteVTable.3301
- _kAPRRemoteControlSessionMediaRemote_Class.3318
- _kAPRRemoteControlSessionSession_BaseClassWrapper.3331
Functions:
~ -[APAVAudioSessionManager setUpSessionWithIsMixable:] : 1148 -> 1440
~ _sysInfo_copyInfoDictInternal : 2800 -> 2784
CStrings:
+ "920.5.1.11.1"
+ "[%@] Failed to set IsAirPlayReceiverSession property with err: %@.\n"
+ "[%@] Failed to set IsEligibleForNowPlayingAppConsideration property with err: %@.\n"
+ "[%@] IsAirPlayReceiverSession property set to YES.\n"
+ "[%@] IsEligibleForNowPlayingAppConsideration property set to NO.\n"
- "890.79.1.2"
- "SharePlayWithAirPlayVideo"
- "[%@] IsAirPlayReceiverSession property set. success: %d. err: %@.\n"

```
