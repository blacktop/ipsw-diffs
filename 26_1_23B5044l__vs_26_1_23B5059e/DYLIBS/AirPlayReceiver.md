## AirPlayReceiver

> `/System/Library/PrivateFrameworks/AirPlayReceiver.framework/AirPlayReceiver`

```diff

-920.5.1.11.1
-  __TEXT.__text: 0x14ce40
-  __TEXT.__auth_stubs: 0x3820
+920.8.2.0.0
+  __TEXT.__text: 0x14cfcc
+  __TEXT.__auth_stubs: 0x3830
   __TEXT.__objc_methlist: 0xad4
   __TEXT.__const: 0x32335
   __TEXT.__dlopen_cstrs: 0xad
   __TEXT.__gcc_except_tab: 0x7e8
-  __TEXT.__cstring: 0x2f8e4
+  __TEXT.__cstring: 0x2f982
   __TEXT.__unwind_info: 0x1478
   __TEXT.__eh_frame: 0x80
   __TEXT.__objc_classname: 0x144

   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x40
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__auth_got: 0x1c20
+  __AUTH_CONST.__auth_got: 0x1c28
   __AUTH_CONST.__const: 0xaf08
-  __AUTH_CONST.__cfstring: 0xaf60
+  __AUTH_CONST.__cfstring: 0xaf80
   __AUTH_CONST.__objc_const: 0x1530
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0x280

   __DATA.__common: 0xa14
   __DATA_DIRTY.__objc_data: 0xf0
   __DATA_DIRTY.__data: 0x310
-  __DATA_DIRTY.__bss: 0x188
+  __DATA_DIRTY.__bss: 0x198
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 714A9559-51B0-365D-8726-0CBE9F66B502
+  UUID: FBAC339A-ADEC-3610-9B15-D85C743FEA3C
   Functions: 1591
-  Symbols:   5093
-  CStrings:  6872
+  Symbols:   5094
+  CStrings:  6876
 
Symbols:
+ _APReceiverRequestProcessorCopyProperty.3958
+ _APReceiverRequestProcessorCopyProperty.7067
+ _APReceiverRequestProcessorCopyProperty.7555
+ _APReceiverRequestProcessorSetProperty.4504
+ _APSNetworkCopyConvertedLinkLocalIPv6Addresses
+ _CMBaseObjectNotificationBarrier.3336
+ __Finalize.2410
+ __Finalize.6325
+ __GetTypeID.6322
+ __UpdateAVAudioSessionAudioMode.5424
+ ___Block_byref_object_copy_.2916
+ ___Block_byref_object_dispose_.2917
+ ___block_descriptor_tmp.109
+ ___block_descriptor_tmp.143.5296
+ ___block_descriptor_tmp.171.6205
+ ___block_descriptor_tmp.172.6206
+ ___block_descriptor_tmp.2323
+ ___block_descriptor_tmp.29.3311
+ ___block_descriptor_tmp.305
+ ___block_descriptor_tmp.3267
+ ___block_descriptor_tmp.3329
+ ___block_descriptor_tmp.3483
+ ___block_descriptor_tmp.3703
+ ___block_descriptor_tmp.3821
+ ___block_descriptor_tmp.3954
+ ___block_descriptor_tmp.42.7140
+ ___block_descriptor_tmp.49.3844
+ ___block_descriptor_tmp.494
+ ___block_descriptor_tmp.52.3290
+ ___block_descriptor_tmp.52.7480
+ ___block_descriptor_tmp.5321
+ ___block_descriptor_tmp.5887
+ ___block_descriptor_tmp.60.3293
+ ___block_descriptor_tmp.6077
+ ___block_descriptor_tmp.67.3285
+ ___block_descriptor_tmp.7046
+ ___block_descriptor_tmp.7143
+ ___block_descriptor_tmp.7473
+ ___block_descriptor_tmp.996
+ ___block_literal_global.1612
+ ___block_literal_global.2138
+ ___block_literal_global.2439
+ ___block_literal_global.2889
+ ___block_literal_global.303
+ ___block_literal_global.3265
+ ___block_literal_global.3348
+ ___block_literal_global.3701
+ ___block_literal_global.3819
+ ___block_literal_global.491
+ ___block_literal_global.536
+ ___block_literal_global.5606
+ ___block_literal_global.5828
+ ___block_literal_global.5885
+ ___block_literal_global.7126
+ ___block_literal_global.7471
+ ___block_literal_global.830
+ ___block_literal_global.994
+ _audioSession_audioDecoderDecodeCallback.6167
+ _audioSession_audioDecoderDecodeFrame.6154
+ _audioSession_handleMediaDataControlRequest.3715
+ _audioSession_handleMediaDataControlRequest.6044
+ _audioSession_log.6178
+ _audioSession_networkThread.6188
+ _audioSession_performPeriodicTasks.6183
+ _audioSession_sessionLock.6081
+ _audioSession_sessionUnlock.6083
+ _gAirTunesRelativeTimeOffset.6209
+ _kAPRRemoteControlSessionMediaRemoteVTable.3304
+ _kAPRRemoteControlSessionMediaRemote_Class.3321
+ _kAPRRemoteControlSessionSession_BaseClassWrapper.3334
- _APReceiverRequestProcessorCopyProperty.3962
- _APReceiverRequestProcessorCopyProperty.7069
- _APReceiverRequestProcessorCopyProperty.7557
- _APReceiverRequestProcessorSetProperty.4525
- _CMBaseObjectNotificationBarrier.3338
- __Finalize.2412
- __Finalize.6349
- __GetTypeID.6346
- __UpdateAVAudioSessionAudioMode.5448
- ___Block_byref_object_copy_.2919
- ___Block_byref_object_dispose_.2920
- ___block_descriptor_tmp.1007
- ___block_descriptor_tmp.107.1047
- ___block_descriptor_tmp.143.5320
- ___block_descriptor_tmp.171.6229
- ___block_descriptor_tmp.172.6230
- ___block_descriptor_tmp.2327
- ___block_descriptor_tmp.29.3313
- ___block_descriptor_tmp.306
- ___block_descriptor_tmp.3270
- ___block_descriptor_tmp.3331
- ___block_descriptor_tmp.3486
- ___block_descriptor_tmp.3706
- ___block_descriptor_tmp.3824
- ___block_descriptor_tmp.3958
- ___block_descriptor_tmp.42.7142
- ___block_descriptor_tmp.49.3847
- ___block_descriptor_tmp.495
- ___block_descriptor_tmp.52.3292
- ___block_descriptor_tmp.52.7482
- ___block_descriptor_tmp.5345
- ___block_descriptor_tmp.5911
- ___block_descriptor_tmp.60.3295
- ___block_descriptor_tmp.6101
- ___block_descriptor_tmp.66
- ___block_descriptor_tmp.7048
- ___block_descriptor_tmp.7145
- ___block_descriptor_tmp.7475
- ___block_literal_global.1005
- ___block_literal_global.1622
- ___block_literal_global.2143
- ___block_literal_global.2441
- ___block_literal_global.2892
- ___block_literal_global.304
- ___block_literal_global.3268
- ___block_literal_global.3350
- ___block_literal_global.3704
- ___block_literal_global.3822
- ___block_literal_global.492
- ___block_literal_global.537
- ___block_literal_global.5630
- ___block_literal_global.5852
- ___block_literal_global.5909
- ___block_literal_global.7128
- ___block_literal_global.7473
- ___block_literal_global.847
- _audioSession_audioDecoderDecodeCallback.6191
- _audioSession_audioDecoderDecodeFrame.6178
- _audioSession_handleMediaDataControlRequest.3718
- _audioSession_handleMediaDataControlRequest.6068
- _audioSession_log.6202
- _audioSession_networkThread.6212
- _audioSession_performPeriodicTasks.6207
- _audioSession_sessionLock.6105
- _audioSession_sessionUnlock.6107
- _gAirTunesRelativeTimeOffset.6233
- _kAPRRemoteControlSessionMediaRemoteVTable.3306
- _kAPRRemoteControlSessionMediaRemote_Class.3323
- _kAPRRemoteControlSessionSession_BaseClassWrapper.3336
Functions:
~ __Finalize : 376 -> 380
~ _airplayReqProcessor_copyParentGroupInfoFromSetupRequest : 708 -> 1132
~ _AirPlayReceiverSessionSetup : 19324 -> 19292
CStrings:
+ "920.8.2"
+ "Addresses"
+ "CFDictionaryRef airplayReqProcessor_copyUGLInfoWithUpdatedAddresses(APReceiverRequestProcessorRef, CFDictionaryRef)"
+ "[%{ptr}] <APUGL> Converted addresses: %@\n"
+ "[%{ptr}] <APUGL> Converting addresses if IPv6 link local: %@\n"
- "920.5.1.11.1"
- "void _Cleanup(APMulticastProbeReceiverRef, OSStatus, int *, int *)"

```
