## ToneLibrary

> `/System/Library/PrivateFrameworks/ToneLibrary.framework/ToneLibrary`

```diff

-660.0.0.0.0
-  __TEXT.__text: 0x4c7e4
+663.501.0.0.0
+  __TEXT.__text: 0x4c8f4
   __TEXT.__auth_stubs: 0x8d0
-  __TEXT.__objc_methlist: 0x2dd0
+  __TEXT.__objc_methlist: 0x2de0
   __TEXT.__const: 0x160
   __TEXT.__gcc_except_tab: 0x16c8
-  __TEXT.__cstring: 0x6084
+  __TEXT.__cstring: 0x60ae
   __TEXT.__oslogstring: 0xdcdf
   __TEXT.__ustring: 0x4
   __TEXT.__dlopen_cstrs: 0x534
   __TEXT.__unwind_info: 0x1290
   __TEXT.__objc_classname: 0x597
-  __TEXT.__objc_methname: 0xacec
+  __TEXT.__objc_methname: 0xad0f
   __TEXT.__objc_methtype: 0x1136
-  __TEXT.__objc_stubs: 0x7100
+  __TEXT.__objc_stubs: 0x7120
   __DATA_CONST.__got: 0x458
   __DATA_CONST.__const: 0x1950
   __DATA_CONST.__objc_classlist: 0x158
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2100
+  __DATA_CONST.__objc_selrefs: 0x2108
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x120
   __DATA_CONST.__objc_arraydata: 0x58
   __AUTH_CONST.__auth_got: 0x480
   __AUTH_CONST.__const: 0x380
   __AUTH_CONST.__cfstring: 0x5b40
-  __AUTH_CONST.__objc_const: 0x4e40
+  __AUTH_CONST.__objc_const: 0x4e50
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_intobj: 0x30

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6253BD02-976E-31FB-B09F-D98E781F9A50
-  Functions: 1428
-  Symbols:   5371
-  CStrings:  3848
+  UUID: 5D264B0D-04F9-334D-AB60-90C8F87055CF
+  Functions: 1429
+  Symbols:   5374
+  CStrings:  3851
 
Symbols:
+ -[TLCapabilitiesManager supportsMediaExperienceAlarmVolume]
+ GCC_except_table16
+ _objc_msgSend$supportsMediaExperienceAlarmVolume
Functions:
+ -[TLCapabilitiesManager supportsMediaExperienceAlarmVolume]
~ -[TLAlertQueuePlayerController _restoreAudioEnvironmentForStateDescriptor:isForMusicPlayback:] : 2728 -> 2864
~ +[TLAlertQueuePlayerController _audioVolumeApplicationPolicyForAlert:externalEnvironmentValues:] : 364 -> 480
CStrings:
+ "/Library/Caches/com.apple.xbs/7C4BEA62-37E1-46F0-86ED-E8027AE90EC1/TemporaryDirectory.6Vvisi/Sources/ToneLibrary/Library/Playback/BackEnds/QueuePlayer/AttentionAwarenessEffects/TLAttentionAwarenessEffectProcessor.m"
+ "/Library/Caches/com.apple.xbs/7C4BEA62-37E1-46F0-86ED-E8027AE90EC1/TemporaryDirectory.6Vvisi/Sources/ToneLibrary/Library/Playback/BackEnds/QueuePlayer/TLAlertQueuePlayerController.m"
+ "/Library/Caches/com.apple.xbs/7C4BEA62-37E1-46F0-86ED-E8027AE90EC1/TemporaryDirectory.6Vvisi/Sources/ToneLibrary/Library/Playback/BackEnds/SystemSound/TLAlertSystemSoundController.m"
+ "/Library/Caches/com.apple.xbs/7C4BEA62-37E1-46F0-86ED-E8027AE90EC1/TemporaryDirectory.6Vvisi/Sources/ToneLibrary/Library/Playback/TLAlertController.m"
+ "/Library/Caches/com.apple.xbs/7C4BEA62-37E1-46F0-86ED-E8027AE90EC1/TemporaryDirectory.6Vvisi/Sources/ToneLibrary/Library/Playback/TLAlertType.m"
+ "/Library/Caches/com.apple.xbs/7C4BEA62-37E1-46F0-86ED-E8027AE90EC1/TemporaryDirectory.6Vvisi/Sources/ToneLibrary/Library/Tones/TLToneManager.m"
+ "/Library/Caches/com.apple.xbs/7C4BEA62-37E1-46F0-86ED-E8027AE90EC1/TemporaryDirectory.6Vvisi/Sources/ToneLibrary/Library/Tones/ToneStoreDownloads/Embedded/TLToneStoreDownloadStoreServicesController.m"
+ "/Library/Caches/com.apple.xbs/7C4BEA62-37E1-46F0-86ED-E8027AE90EC1/TemporaryDirectory.6Vvisi/Sources/ToneLibrary/Library/Utilities/TLAttentionAwarenessObserver.m"
+ "/Library/Caches/com.apple.xbs/7C4BEA62-37E1-46F0-86ED-E8027AE90EC1/TemporaryDirectory.6Vvisi/Sources/ToneLibrary/Library/Utilities/TLAudioQueue.m"
+ "/Library/Caches/com.apple.xbs/7C4BEA62-37E1-46F0-86ED-E8027AE90EC1/TemporaryDirectory.6Vvisi/Sources/ToneLibrary/Library/Utilities/TLBacklight.m"
+ "/Library/Caches/com.apple.xbs/7C4BEA62-37E1-46F0-86ED-E8027AE90EC1/TemporaryDirectory.6Vvisi/Sources/ToneLibrary/Library/Utilities/TLContentProtectionStateObserver.m"
+ "/Library/Caches/com.apple.xbs/7C4BEA62-37E1-46F0-86ED-E8027AE90EC1/TemporaryDirectory.6Vvisi/Sources/ToneLibrary/Library/Utilities/TLSilentModeController.m"
+ "/Library/Caches/com.apple.xbs/7C4BEA62-37E1-46F0-86ED-E8027AE90EC1/TemporaryDirectory.6Vvisi/Sources/ToneLibrary/Library/Vibrations/TLVibrationManager.m"
+ "/Library/Caches/com.apple.xbs/7C4BEA62-37E1-46F0-86ED-E8027AE90EC1/TemporaryDirectory.6Vvisi/Sources/ToneLibrary/Library/Vibrations/TLVibrationPersistenceUtilities.m"
+ "9b2fb519-d14b-49ab-bb91-67a6bf4e2b9a"
+ "IndependentVolumeControls"
+ "MediaExperience"
+ "supportsMediaExperienceAlarmVolume"
- "/Library/Caches/com.apple.xbs/1F6CCAC9-8DD9-40B0-B128-747D1AEC1550/TemporaryDirectory.mtmKtm/Sources/ToneLibrary/Library/Playback/BackEnds/QueuePlayer/AttentionAwarenessEffects/TLAttentionAwarenessEffectProcessor.m"
- "/Library/Caches/com.apple.xbs/1F6CCAC9-8DD9-40B0-B128-747D1AEC1550/TemporaryDirectory.mtmKtm/Sources/ToneLibrary/Library/Playback/BackEnds/QueuePlayer/TLAlertQueuePlayerController.m"
- "/Library/Caches/com.apple.xbs/1F6CCAC9-8DD9-40B0-B128-747D1AEC1550/TemporaryDirectory.mtmKtm/Sources/ToneLibrary/Library/Playback/BackEnds/SystemSound/TLAlertSystemSoundController.m"
- "/Library/Caches/com.apple.xbs/1F6CCAC9-8DD9-40B0-B128-747D1AEC1550/TemporaryDirectory.mtmKtm/Sources/ToneLibrary/Library/Playback/TLAlertController.m"
- "/Library/Caches/com.apple.xbs/1F6CCAC9-8DD9-40B0-B128-747D1AEC1550/TemporaryDirectory.mtmKtm/Sources/ToneLibrary/Library/Playback/TLAlertType.m"
- "/Library/Caches/com.apple.xbs/1F6CCAC9-8DD9-40B0-B128-747D1AEC1550/TemporaryDirectory.mtmKtm/Sources/ToneLibrary/Library/Tones/TLToneManager.m"
- "/Library/Caches/com.apple.xbs/1F6CCAC9-8DD9-40B0-B128-747D1AEC1550/TemporaryDirectory.mtmKtm/Sources/ToneLibrary/Library/Tones/ToneStoreDownloads/Embedded/TLToneStoreDownloadStoreServicesController.m"
- "/Library/Caches/com.apple.xbs/1F6CCAC9-8DD9-40B0-B128-747D1AEC1550/TemporaryDirectory.mtmKtm/Sources/ToneLibrary/Library/Utilities/TLAttentionAwarenessObserver.m"
- "/Library/Caches/com.apple.xbs/1F6CCAC9-8DD9-40B0-B128-747D1AEC1550/TemporaryDirectory.mtmKtm/Sources/ToneLibrary/Library/Utilities/TLAudioQueue.m"
- "/Library/Caches/com.apple.xbs/1F6CCAC9-8DD9-40B0-B128-747D1AEC1550/TemporaryDirectory.mtmKtm/Sources/ToneLibrary/Library/Utilities/TLBacklight.m"
- "/Library/Caches/com.apple.xbs/1F6CCAC9-8DD9-40B0-B128-747D1AEC1550/TemporaryDirectory.mtmKtm/Sources/ToneLibrary/Library/Utilities/TLContentProtectionStateObserver.m"
- "/Library/Caches/com.apple.xbs/1F6CCAC9-8DD9-40B0-B128-747D1AEC1550/TemporaryDirectory.mtmKtm/Sources/ToneLibrary/Library/Utilities/TLSilentModeController.m"
- "/Library/Caches/com.apple.xbs/1F6CCAC9-8DD9-40B0-B128-747D1AEC1550/TemporaryDirectory.mtmKtm/Sources/ToneLibrary/Library/Vibrations/TLVibrationManager.m"
- "/Library/Caches/com.apple.xbs/1F6CCAC9-8DD9-40B0-B128-747D1AEC1550/TemporaryDirectory.mtmKtm/Sources/ToneLibrary/Library/Vibrations/TLVibrationPersistenceUtilities.m"
- "9B2FB519-332F-481C-B7DE-7E80973B07BF"

```
