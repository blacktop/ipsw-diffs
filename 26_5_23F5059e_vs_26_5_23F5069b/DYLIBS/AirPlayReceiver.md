## AirPlayReceiver

> `/System/Library/PrivateFrameworks/AirPlayReceiver.framework/AirPlayReceiver`

```diff

-950.6.1.0.0
-  __TEXT.__text: 0x15ffcc
+950.7.1.0.0
+  __TEXT.__text: 0x15ffe0
   __TEXT.__auth_stubs: 0x3890
   __TEXT.__objc_methlist: 0xae4
   __TEXT.__const: 0x326d5
   __TEXT.__dlopen_cstrs: 0xad
   __TEXT.__gcc_except_tab: 0x7e4
-  __TEXT.__cstring: 0x2fba0
+  __TEXT.__cstring: 0x2fb5d
   __TEXT.__unwind_info: 0x1498
   __TEXT.__eh_frame: 0x80
   __TEXT.__objc_classname: 0x144

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6C0A99B2-61EF-3ACF-A981-DE1AE8640740
+  UUID: 596A41A9-3852-32D4-973C-6AFC5C8F24AE
   Functions: 1597
   Symbols:   5128
-  CStrings:  6910
+  CStrings:  6909
 
Symbols:
+ _APReceiverRequestProcessorCopyProperty.3979
+ _APReceiverRequestProcessorCopyProperty.7082
+ _APReceiverRequestProcessorCopyProperty.7570
+ _APReceiverRequestProcessorSetProperty.4529
+ _CMBaseObjectNotificationBarrier.3357
+ __Finalize.2425
+ __Finalize.6359
+ __GetTypeID.6356
+ __UpdateAVAudioSessionAudioMode.5458
+ ___Block_byref_object_copy_.2935
+ ___Block_byref_object_dispose_.2936
+ ___block_descriptor_tmp.109
+ ___block_descriptor_tmp.143.5330
+ ___block_descriptor_tmp.171.6239
+ ___block_descriptor_tmp.172.6240
+ ___block_descriptor_tmp.2338
+ ___block_descriptor_tmp.29.3332
+ ___block_descriptor_tmp.305
+ ___block_descriptor_tmp.3288
+ ___block_descriptor_tmp.3350
+ ___block_descriptor_tmp.3504
+ ___block_descriptor_tmp.3724
+ ___block_descriptor_tmp.3842
+ ___block_descriptor_tmp.3976
+ ___block_descriptor_tmp.42.7155
+ ___block_descriptor_tmp.49.3865
+ ___block_descriptor_tmp.494
+ ___block_descriptor_tmp.52.3311
+ ___block_descriptor_tmp.52.7495
+ ___block_descriptor_tmp.5355
+ ___block_descriptor_tmp.5921
+ ___block_descriptor_tmp.60.3314
+ ___block_descriptor_tmp.6111
+ ___block_descriptor_tmp.67.3306
+ ___block_descriptor_tmp.7062
+ ___block_descriptor_tmp.7158
+ ___block_descriptor_tmp.7488
+ ___block_literal_global.169
+ ___block_literal_global.2119
+ ___block_literal_global.2455
+ ___block_literal_global.2908
+ ___block_literal_global.303
+ ___block_literal_global.3286
+ ___block_literal_global.3369
+ ___block_literal_global.3722
+ ___block_literal_global.3840
+ ___block_literal_global.491
+ ___block_literal_global.5640
+ ___block_literal_global.5862
+ ___block_literal_global.5919
+ ___block_literal_global.7141
+ ___block_literal_global.7486
+ _audioSession_audioDecoderDecodeCallback.6201
+ _audioSession_audioDecoderDecodeFrame.6188
+ _audioSession_handleMediaDataControlRequest.3736
+ _audioSession_handleMediaDataControlRequest.6078
+ _audioSession_log.6212
+ _audioSession_networkThread.6222
+ _audioSession_performPeriodicTasks.6217
+ _audioSession_sessionLock.6115
+ _audioSession_sessionUnlock.6117
+ _gAirTunesRelativeTimeOffset.6243
+ _kAPRRemoteControlSessionMediaRemoteVTable.3325
+ _kAPRRemoteControlSessionMediaRemote_Class.3342
+ _kAPRRemoteControlSessionSession_BaseClassWrapper.3355
- _APReceiverRequestProcessorCopyProperty.3976
- _APReceiverRequestProcessorCopyProperty.7079
- _APReceiverRequestProcessorCopyProperty.7567
- _APReceiverRequestProcessorSetProperty.4525
- _CMBaseObjectNotificationBarrier.3353
- __Finalize.2422
- __Finalize.6355
- __GetTypeID.6352
- __UpdateAVAudioSessionAudioMode.5454
- ___Block_byref_object_copy_.2932
- ___Block_byref_object_dispose_.2933
- ___block_descriptor_tmp.107.1046
- ___block_descriptor_tmp.143.5326
- ___block_descriptor_tmp.171.6235
- ___block_descriptor_tmp.172.6236
- ___block_descriptor_tmp.2337
- ___block_descriptor_tmp.29.3328
- ___block_descriptor_tmp.306
- ___block_descriptor_tmp.3285
- ___block_descriptor_tmp.3346
- ___block_descriptor_tmp.3501
- ___block_descriptor_tmp.3721
- ___block_descriptor_tmp.3839
- ___block_descriptor_tmp.3973
- ___block_descriptor_tmp.42.7152
- ___block_descriptor_tmp.49.3862
- ___block_descriptor_tmp.495
- ___block_descriptor_tmp.52.3307
- ___block_descriptor_tmp.52.7492
- ___block_descriptor_tmp.5351
- ___block_descriptor_tmp.5917
- ___block_descriptor_tmp.60.3310
- ___block_descriptor_tmp.6107
- ___block_descriptor_tmp.66
- ___block_descriptor_tmp.7059
- ___block_descriptor_tmp.7155
- ___block_descriptor_tmp.7485
- ___block_literal_global.168
- ___block_literal_global.2120
- ___block_literal_global.2452
- ___block_literal_global.2905
- ___block_literal_global.304
- ___block_literal_global.3283
- ___block_literal_global.3365
- ___block_literal_global.3719
- ___block_literal_global.3837
- ___block_literal_global.492
- ___block_literal_global.5636
- ___block_literal_global.5858
- ___block_literal_global.5915
- ___block_literal_global.7138
- ___block_literal_global.7483
- _audioSession_audioDecoderDecodeCallback.6197
- _audioSession_audioDecoderDecodeFrame.6184
- _audioSession_handleMediaDataControlRequest.3733
- _audioSession_handleMediaDataControlRequest.6074
- _audioSession_log.6208
- _audioSession_networkThread.6218
- _audioSession_performPeriodicTasks.6213
- _audioSession_sessionLock.6111
- _audioSession_sessionUnlock.6113
- _gAirTunesRelativeTimeOffset.6239
- _kAPRRemoteControlSessionMediaRemoteVTable.3321
- _kAPRRemoteControlSessionMediaRemote_Class.3338
- _kAPRRemoteControlSessionSession_BaseClassWrapper.3351
Functions:
~ __Finalize : 376 -> 380
~ _AirPlayReceiverSessionSetup : 18996 -> 19012
CStrings:
+ "950.7.1"
- "950.6.1"
- "void _Cleanup(APMulticastProbeReceiverRef, OSStatus, int *, int *)"

```
