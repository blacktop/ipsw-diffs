## AirPlayReceiver

> `/System/Library/PrivateFrameworks/AirPlayReceiver.framework/Versions/A/AirPlayReceiver`

```diff

 960.13.25.1.0
-  __TEXT.__text: 0xe15c4
-  __TEXT.__auth_stubs: 0x35e0
+  __TEXT.__text: 0xe1270
+  __TEXT.__auth_stubs: 0x35d0
   __TEXT.__objc_methlist: 0x924
   __TEXT.__const: 0xd155
   __TEXT.__dlopen_cstrs: 0xad
   __TEXT.__gcc_except_tab: 0x720
-  __TEXT.__cstring: 0x2a5d8
+  __TEXT.__cstring: 0x2a58a
   __TEXT.__unwind_info: 0x1158
   __TEXT.__objc_classname: 0x12c
   __TEXT.__objc_methname: 0x1f66

   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__auth_got: 0x1b00
+  __AUTH_CONST.__auth_got: 0x1af8
   __AUTH_CONST.__const: 0x4b50
   __AUTH_CONST.__cfstring: 0xa600
   __AUTH_CONST.__objc_const: 0x1358

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 1336
-  Symbols:   3356
-  CStrings:  4891
+  Symbols:   3355
+  CStrings:  4887
 
Symbols:
- _APSIsHomeAccessory
Functions:
~ sub_2327e9990 -> sub_232575990 : 304 -> 280
~ _APReceiverAudioSessionRealTimeCreate : 13364 -> 13236
~ _APReceiverAudioSessionCreate : 13092 -> 12980
~ _sysInfo_updateAdvertiserInfoAndNotify : 3244 -> 3220
~ _sysInfo_createFeaturesInternal : 1228 -> 1204
~ _sysInfo_handleInfoDictUpdate : 524 -> 516
~ _sysInfo_copyInfoDictInternal : 2796 -> 2784
~ _sysInfo_updateAPGroupInfo : 1184 -> 1176
~ _sysInfo_handleAuthStringUpdate : 380 -> 372
~ _APReceiverSystemInfoHandleAPServicesReset : 156 -> 148
~ _AirPlayReceiverServerCreate : 10368 -> 10312
~ _airplayReqProcessor_requestProcessSetupPlist : 4064 -> 4112
~ _airplayReqProcessor_createSessionInfoDict : 432 -> 424
~ _APReceiverAudioSessionBufferedHoseCreate : 9208 -> 9096
~ _audioSessionBufferedHose_audioFormatChangedNotification : 3092 -> 2980
~ __MainAudioEnsureSetup : 7232 -> 7120
~ audioSession_networkThread.5720 -> audioSession_networkThread.5725 : 5628 -> 5532
~ __GeneralAudioSetup : 10860 -> 10812
CStrings:
- "AAC_ELD/48000/7.1.4"
- "AAC_ELD/48000/9.1.6"
- "AAC_LC/48000/7.1.4"
- "AAC_LC/48000/9.1.6"
```
