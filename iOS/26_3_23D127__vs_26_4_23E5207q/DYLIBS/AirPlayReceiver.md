## AirPlayReceiver

> `/System/Library/PrivateFrameworks/AirPlayReceiver.framework/AirPlayReceiver`

```diff

-935.7.1.0.0
-  __TEXT.__text: 0x14d770
+940.19.1.0.0
+  __TEXT.__text: 0x170e34
   __TEXT.__auth_stubs: 0x3890
   __TEXT.__objc_methlist: 0xae4
-  __TEXT.__const: 0x32335
+  __TEXT.__const: 0x32365
   __TEXT.__dlopen_cstrs: 0xad
-  __TEXT.__gcc_except_tab: 0x7e8
-  __TEXT.__cstring: 0x2fb15
-  __TEXT.__unwind_info: 0x1488
-  __TEXT.__eh_frame: 0x80
+  __TEXT.__gcc_except_tab: 0x7e4
+  __TEXT.__cstring: 0x2fba1
+  __TEXT.__unwind_info: 0x14a8
   __TEXT.__objc_classname: 0x144
   __TEXT.__objc_methname: 0x2819
   __TEXT.__objc_methtype: 0x1645

   __DATA_CONST.__objc_superrefs: 0x40
   __DATA_CONST.__objc_arraydata: 0x10
   __AUTH_CONST.__auth_got: 0x1c58
-  __AUTH_CONST.__const: 0xaf08
-  __AUTH_CONST.__cfstring: 0xb060
+  __AUTH_CONST.__const: 0xb9f8
+  __AUTH_CONST.__cfstring: 0xb080
   __AUTH_CONST.__objc_const: 0x1530
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0x280
   __DATA.__objc_ivar: 0x170
-  __DATA.__data: 0x175f8
+  __DATA.__data: 0x17ae0
   __DATA.__bss: 0x5c8
-  __DATA.__common: 0xa14
+  __DATA.__common: 0xa84
   __DATA_DIRTY.__objc_data: 0xf0
   __DATA_DIRTY.__data: 0x310
   __DATA_DIRTY.__bss: 0x198

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1BD58C0C-7325-3913-A3DB-6CFF832BEDF3
-  Functions: 1598
-  Symbols:   5123
-  CStrings:  6906
+  UUID: 36AE59F4-B639-3C5F-921E-6299A4D4DEEF
+  Functions: 1597
+  Symbols:   5128
+  CStrings:  6910
 
Symbols:
+ _APReceiverRequestProcessorCopyProperty.3976
+ _APReceiverRequestProcessorCopyProperty.7079
+ _APReceiverRequestProcessorCopyProperty.7567
+ _APReceiverRequestProcessorSetProperty.4525
+ _CMBaseObjectNotificationBarrier.3353
+ __Finalize.2422
+ __Finalize.6355
+ __GetTypeID.6352
+ __UpdateAVAudioSessionAudioMode.5454
+ ___Block_byref_object_copy_.2932
+ ___Block_byref_object_dispose_.2933
+ ___block_descriptor_tmp.107.1046
+ ___block_descriptor_tmp.143.5326
+ ___block_descriptor_tmp.171.6235
+ ___block_descriptor_tmp.172.6236
+ ___block_descriptor_tmp.2337
+ ___block_descriptor_tmp.29.3328
+ ___block_descriptor_tmp.306
+ ___block_descriptor_tmp.3285
+ ___block_descriptor_tmp.3346
+ ___block_descriptor_tmp.3501
+ ___block_descriptor_tmp.3721
+ ___block_descriptor_tmp.3839
+ ___block_descriptor_tmp.3973
+ ___block_descriptor_tmp.42.7152
+ ___block_descriptor_tmp.49.3862
+ ___block_descriptor_tmp.495
+ ___block_descriptor_tmp.52.3307
+ ___block_descriptor_tmp.52.7492
+ ___block_descriptor_tmp.5351
+ ___block_descriptor_tmp.5917
+ ___block_descriptor_tmp.60.3310
+ ___block_descriptor_tmp.6107
+ ___block_descriptor_tmp.66
+ ___block_descriptor_tmp.7059
+ ___block_descriptor_tmp.7155
+ ___block_descriptor_tmp.7485
+ ___block_literal_global.1620
+ ___block_literal_global.168
+ ___block_literal_global.2120
+ ___block_literal_global.2452
+ ___block_literal_global.2905
+ ___block_literal_global.304
+ ___block_literal_global.3283
+ ___block_literal_global.3365
+ ___block_literal_global.370
+ ___block_literal_global.3719
+ ___block_literal_global.3837
+ ___block_literal_global.492
+ ___block_literal_global.5636
+ ___block_literal_global.570
+ ___block_literal_global.5858
+ ___block_literal_global.5915
+ ___block_literal_global.7138
+ ___block_literal_global.7483
+ _abort
+ _audioSession_audioDecoderDecodeCallback.6197
+ _audioSession_audioDecoderDecodeFrame.6184
+ _audioSession_handleMediaDataControlRequest.3733
+ _audioSession_handleMediaDataControlRequest.6074
+ _audioSession_log.6208
+ _audioSession_networkThread.6218
+ _audioSession_performPeriodicTasks.6213
+ _audioSession_sessionLock.6111
+ _audioSession_sessionUnlock.6113
+ _gAirTunesRelativeTimeOffset.6239
+ _kAPRRemoteControlSessionMediaRemoteVTable.3321
+ _kAPRRemoteControlSessionMediaRemote_Class.3338
+ _kAPRRemoteControlSessionSession_BaseClassWrapper.3351
+ _mmap
+ _munmap
+ _sched_yield
+ _sysconf
- _APReceiverRequestProcessorCopyProperty.3921
- _APReceiverRequestProcessorCopyProperty.7090
- _APReceiverRequestProcessorCopyProperty.7578
- _APReceiverRequestProcessorSetProperty.4505
- _CMBaseObjectNotificationBarrier.3299
- __Finalize.2349
- __Finalize.6327
- __GetTypeID.6324
- __UpdateAVAudioSessionAudioMode.5426
- ___Block_byref_object_copy_.2878
- ___Block_byref_object_dispose_.2879
- ___block_descriptor_tmp.109
- ___block_descriptor_tmp.143.5298
- ___block_descriptor_tmp.171.6207
- ___block_descriptor_tmp.172.6208
- ___block_descriptor_tmp.2262
- ___block_descriptor_tmp.29.3274
- ___block_descriptor_tmp.305
- ___block_descriptor_tmp.3230
- ___block_descriptor_tmp.3292
- ___block_descriptor_tmp.3446
- ___block_descriptor_tmp.3666
- ___block_descriptor_tmp.3784
- ___block_descriptor_tmp.3917
- ___block_descriptor_tmp.42.7163
- ___block_descriptor_tmp.49.3807
- ___block_descriptor_tmp.494
- ___block_descriptor_tmp.52.3253
- ___block_descriptor_tmp.52.7503
- ___block_descriptor_tmp.5323
- ___block_descriptor_tmp.5889
- ___block_descriptor_tmp.60.3256
- ___block_descriptor_tmp.6079
- ___block_descriptor_tmp.67.3248
- ___block_descriptor_tmp.7069
- ___block_descriptor_tmp.7166
- ___block_descriptor_tmp.7496
- ___block_literal_global.1622
- ___block_literal_global.169
- ___block_literal_global.2067
- ___block_literal_global.2379
- ___block_literal_global.2851
- ___block_literal_global.303
- ___block_literal_global.3228
- ___block_literal_global.3311
- ___block_literal_global.365
- ___block_literal_global.3664
- ___block_literal_global.3782
- ___block_literal_global.491
- ___block_literal_global.5608
- ___block_literal_global.571
- ___block_literal_global.5830
- ___block_literal_global.5887
- ___block_literal_global.7149
- ___block_literal_global.7494
- _audioSession_audioDecoderDecodeCallback.6169
- _audioSession_audioDecoderDecodeFrame.6156
- _audioSession_handleMediaDataControlRequest.3678
- _audioSession_handleMediaDataControlRequest.6046
- _audioSession_log.6180
- _audioSession_networkThread.6190
- _audioSession_performPeriodicTasks.6185
- _audioSession_sessionLock.6083
- _audioSession_sessionUnlock.6085
- _gAirTunesRelativeTimeOffset.6211
- _kAPRRemoteControlSessionMediaRemoteVTable.3267
- _kAPRRemoteControlSessionMediaRemote_Class.3284
- _kAPRRemoteControlSessionSession_BaseClassWrapper.3297
CStrings:
+ "940.19.1"
+ "Interrupting any audio played in other processes with media AVAudioSession\n"
+ "[%{ptr}] Pre-warming audio HW\n"
+ "[%{ptr}] shouldReceiverPrewarmAudioHW=%s from prefs\n"
+ "shouldReceiverPrewarmAudioHWOverride"
+ "void _Cleanup(APMulticastProbeReceiverRef, OSStatus, int *, int *)"
- "935.7.1"
- "Interrupting any audio played in other processes by activating the media AVAudioSession\n"
- "Invalid device enclosure color: %@\n"

```
