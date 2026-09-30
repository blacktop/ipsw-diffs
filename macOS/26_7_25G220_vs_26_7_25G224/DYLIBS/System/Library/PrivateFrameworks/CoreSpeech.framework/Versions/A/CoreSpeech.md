## CoreSpeech

> `/System/Library/PrivateFrameworks/CoreSpeech.framework/Versions/A/CoreSpeech`

```diff

 3525.5.8.0.0
-  __TEXT.__text: 0x154a9c
-  __TEXT.__auth_stubs: 0x1810
+  __TEXT.__text: 0x1549c4
+  __TEXT.__auth_stubs: 0x17f0
   __TEXT.__objc_methlist: 0x13640
-  __TEXT.__const: 0x42c
+  __TEXT.__const: 0x3fc
   __TEXT.__dlopen_cstrs: 0x4e
   __TEXT.__gcc_except_tab: 0x3acc
   __TEXT.__cstring: 0x24385

   __TEXT.__objc_methtype: 0x71de
   __TEXT.__objc_stubs: 0x1a400
   __DATA_CONST.__got: 0x1830
-  __DATA_CONST.__const: 0xd10
+  __DATA_CONST.__const: 0xce0
   __DATA_CONST.__objc_classlist: 0x7f0
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x468

   __DATA_CONST.__objc_protorefs: 0xa0
   __DATA_CONST.__objc_superrefs: 0x628
   __DATA_CONST.__objc_arraydata: 0x3f0
-  __AUTH_CONST.__auth_got: 0xc20
+  __AUTH_CONST.__auth_got: 0xc10
   __AUTH_CONST.__const: 0x5780
   __AUTH_CONST.__cfstring: 0x9020
   __AUTH_CONST.__objc_const: 0x1eb78
-  __AUTH_CONST.__objc_intobj: 0x960
+  __AUTH_CONST.__objc_intobj: 0x900
   __AUTH_CONST.__objc_doubleobj: 0x90
   __AUTH_CONST.__objc_dictobj: 0x3e8
   __AUTH_CONST.__objc_floatobj: 0x4d0

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 7587
-  Symbols:   16685
+  Symbols:   16683
   CStrings:  13308
 
Symbols:
- _AFIsWaffleiron
- _CSIsHorseTV
Functions:
~ -[CSAsset(SmartSiriVolume) SSVCADeviceSimpleASVOffMinTTSVolume] : 344 -> 340
~ -[CSAsset(SmartSiriVolume) SSVCADeviceSimpleMaxTTSVolume] : 156 -> 152
~ -[CSAsset(SmartSiriVolume) SSVCADeviceSimpleMinTTSVolume] : 156 -> 152
~ -[CSAsset(SmartSiriVolume) SSVCAMaxTTSSystemVolume] : 156 -> 152
~ -[CSAsset(SmartSiriVolume) SSVCAMinTTSSystemVolume] : 156 -> 152
~ -[CSAsset(SmartSiriVolume) SSVCADeviceSimpleOutputSlope] : 156 -> 152
~ -[CSAsset(SmartSiriVolume) SSVCADeviceSimpleOutputMaxTargetDB] : 136 -> 132
~ -[CSAsset(SmartSiriVolume) SSVCADeviceSimpleOutputMinTargetDB] : 156 -> 152
~ -[CSAsset(SmartSiriVolume) SSVCASignalToSigmoidMusicSteepnessDeviceSimple] : 328 -> 324
~ -[CSAsset(SmartSiriVolume) SSVCASignalToSigmoidMusicHOffsetDeviceSimple] : 340 -> 336
~ -[CSAsset(SmartSiriVolume) SSVCASignalToSigmoidMusicVOffsetDeviceSimple] : 324 -> 320
~ -[CSAsset(SmartSiriVolume) SSVCASignalToSigmoidMusicVSpreadDeviceSimple] : 324 -> 320
~ -[CSAsset(SmartSiriVolume) SSVCASignalToSigmoidMusicDilationFactorDeviceSimple] : 344 -> 340
~ -[CSAsset(SmartSiriVolume) SSVDistanceChannelBitset] : 164 -> 152
~ -[CSAsset(SmartSiriVolume) SSVLKFSChannelBitset] : 156 -> 136
~ -[CSAsset(SmartSiriVolume) SSVNoiseLevelChannelBitset] : 164 -> 152
~ +[CSAsset(SmartSiriVolume) getSSVDeviceType] : 68 -> 48
~ +[CSAsset(SmartSiriVolume) SSVDefaultDistanceChannelCount] : 120 -> 104
~ +[CSAsset(SmartSiriVolume) SSVDefaultLKFSChannelCount] : 108 -> 92
~ +[CSAsset(SmartSiriVolume) SSVDefaultNoiseChannelCount] : 116 -> 104
~ -[CSSpeechController recordSettings] : 804 -> 796
~ -[CSSiriAudioActivationInfo _csAudioRecordType] : 64 -> 56
~ -[CSSiriAudioActivationInfo _activationMode] : 76 -> 60
~ +[CSSiriAudioActivationInfo _alertDictionaryForRecordRoute:playbackRoute:speechEvent:ringerState:startingAlertBeepOverideID:presentationMode:hasPlayedStartAlert:supportsEchoCancellation:isVoiceOverTouchEnabled:isVibrationEnabled:isVibrationSupported:activationHostTime:isVoiceOverSiriSoundsEnabled:] : 1376 -> 1368
~ +[CSSiriAudioActivationInfo _dictationAlertBehaviorDictionaryForRecordRoute:playbackRoute:ringerState:usePrelistening:suppressStartAlert:supportsEchoCancellation:isVibrationEnabled:isVibrationSupported:isVoiceOverTouchEnabled:] : 388 -> 380
~ -[CSSiriSpeechRecorder _playStopAlertIfNecessaryForReason:error:] : 1200 -> 1192
```
