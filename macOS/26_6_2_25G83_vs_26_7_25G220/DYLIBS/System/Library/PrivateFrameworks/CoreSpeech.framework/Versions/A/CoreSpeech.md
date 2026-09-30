## CoreSpeech

> `/System/Library/PrivateFrameworks/CoreSpeech.framework/Versions/A/CoreSpeech`

```diff

 3525.5.8.0.0
-  __TEXT.__text: 0x1549c4
-  __TEXT.__auth_stubs: 0x17f0
+  __TEXT.__text: 0x154a9c
+  __TEXT.__auth_stubs: 0x1810
   __TEXT.__objc_methlist: 0x13640
-  __TEXT.__const: 0x3fc
+  __TEXT.__const: 0x42c
   __TEXT.__dlopen_cstrs: 0x4e
   __TEXT.__gcc_except_tab: 0x3acc
   __TEXT.__cstring: 0x24385

   __TEXT.__objc_methtype: 0x71de
   __TEXT.__objc_stubs: 0x1a400
   __DATA_CONST.__got: 0x1830
-  __DATA_CONST.__const: 0xce0
+  __DATA_CONST.__const: 0xd10
   __DATA_CONST.__objc_classlist: 0x7f0
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x468

   __DATA_CONST.__objc_protorefs: 0xa0
   __DATA_CONST.__objc_superrefs: 0x628
   __DATA_CONST.__objc_arraydata: 0x3f0
-  __AUTH_CONST.__auth_got: 0xc10
+  __AUTH_CONST.__auth_got: 0xc20
   __AUTH_CONST.__const: 0x5780
   __AUTH_CONST.__cfstring: 0x9020
   __AUTH_CONST.__objc_const: 0x1eb78
-  __AUTH_CONST.__objc_intobj: 0x900
+  __AUTH_CONST.__objc_intobj: 0x960
   __AUTH_CONST.__objc_doubleobj: 0x90
   __AUTH_CONST.__objc_dictobj: 0x3e8
   __AUTH_CONST.__objc_floatobj: 0x4d0

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 7587
-  Symbols:   16683
+  Symbols:   16685
   CStrings:  13308
 
Symbols:
+ _AFIsWaffleiron
+ _CSIsHorseTV
Functions:
~ -[CSAsset(SmartSiriVolume) SSVCADeviceSimpleASVOffMinTTSVolume] : 340 -> 344
~ -[CSAsset(SmartSiriVolume) SSVCADeviceSimpleMaxTTSVolume] : 152 -> 156
~ -[CSAsset(SmartSiriVolume) SSVCADeviceSimpleMinTTSVolume] : 152 -> 156
~ -[CSAsset(SmartSiriVolume) SSVCAMaxTTSSystemVolume] : 152 -> 156
~ -[CSAsset(SmartSiriVolume) SSVCAMinTTSSystemVolume] : 152 -> 156
~ -[CSAsset(SmartSiriVolume) SSVCADeviceSimpleOutputSlope] : 152 -> 156
~ -[CSAsset(SmartSiriVolume) SSVCADeviceSimpleOutputMaxTargetDB] : 132 -> 136
~ -[CSAsset(SmartSiriVolume) SSVCADeviceSimpleOutputMinTargetDB] : 152 -> 156
~ -[CSAsset(SmartSiriVolume) SSVCASignalToSigmoidMusicSteepnessDeviceSimple] : 324 -> 328
~ -[CSAsset(SmartSiriVolume) SSVCASignalToSigmoidMusicHOffsetDeviceSimple] : 336 -> 340
~ -[CSAsset(SmartSiriVolume) SSVCASignalToSigmoidMusicVOffsetDeviceSimple] : 320 -> 324
~ -[CSAsset(SmartSiriVolume) SSVCASignalToSigmoidMusicVSpreadDeviceSimple] : 320 -> 324
~ -[CSAsset(SmartSiriVolume) SSVCASignalToSigmoidMusicDilationFactorDeviceSimple] : 340 -> 344
~ -[CSAsset(SmartSiriVolume) SSVDistanceChannelBitset] : 152 -> 164
~ -[CSAsset(SmartSiriVolume) SSVLKFSChannelBitset] : 136 -> 156
~ -[CSAsset(SmartSiriVolume) SSVNoiseLevelChannelBitset] : 152 -> 164
~ +[CSAsset(SmartSiriVolume) getSSVDeviceType] : 48 -> 68
~ +[CSAsset(SmartSiriVolume) SSVDefaultDistanceChannelCount] : 104 -> 120
~ +[CSAsset(SmartSiriVolume) SSVDefaultLKFSChannelCount] : 92 -> 108
~ +[CSAsset(SmartSiriVolume) SSVDefaultNoiseChannelCount] : 104 -> 116
~ -[CSSpeechController recordSettings] : 796 -> 804
~ -[CSSiriAudioActivationInfo _csAudioRecordType] : 56 -> 64
~ -[CSSiriAudioActivationInfo _activationMode] : 60 -> 76
~ +[CSSiriAudioActivationInfo _alertDictionaryForRecordRoute:playbackRoute:speechEvent:ringerState:startingAlertBeepOverideID:presentationMode:hasPlayedStartAlert:supportsEchoCancellation:isVoiceOverTouchEnabled:isVibrationEnabled:isVibrationSupported:activationHostTime:isVoiceOverSiriSoundsEnabled:] : 1368 -> 1376
~ +[CSSiriAudioActivationInfo _dictationAlertBehaviorDictionaryForRecordRoute:playbackRoute:ringerState:usePrelistening:suppressStartAlert:supportsEchoCancellation:isVibrationEnabled:isVibrationSupported:isVoiceOverTouchEnabled:] : 380 -> 388
~ -[CSSiriSpeechRecorder _playStopAlertIfNecessaryForReason:error:] : 1192 -> 1200
```
