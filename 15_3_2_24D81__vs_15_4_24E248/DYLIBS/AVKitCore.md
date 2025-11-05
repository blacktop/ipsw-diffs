## AVKitCore

> `/System/Library/PrivateFrameworks/AVKitCore.framework/Versions/A/AVKitCore`

```diff

-1235.3.1.0.0
-  __TEXT.__text: 0x33084
+1240.20.1.0.0
+  __TEXT.__text: 0x33a2c
   __TEXT.__auth_stubs: 0x920
-  __TEXT.__objc_methlist: 0x3390
+  __TEXT.__objc_methlist: 0x376c
   __TEXT.__const: 0x1d4
-  __TEXT.__gcc_except_tab: 0x878
-  __TEXT.__cstring: 0x2f0d
-  __TEXT.__oslogstring: 0x1f11
+  __TEXT.__gcc_except_tab: 0x8a0
+  __TEXT.__cstring: 0x2fe6
+  __TEXT.__oslogstring: 0x1f4f
   __TEXT.__dlopen_cstrs: 0xb0
-  __TEXT.__unwind_info: 0xde0
-  __TEXT.__objc_classname: 0x67e
-  __TEXT.__objc_methname: 0xb00f
-  __TEXT.__objc_methtype: 0x1194
-  __TEXT.__objc_stubs: 0x75c0
+  __TEXT.__unwind_info: 0xe58
+  __TEXT.__objc_classname: 0x67f
+  __TEXT.__objc_methname: 0xb5f8
+  __TEXT.__objc_methtype: 0x11ca
+  __TEXT.__objc_stubs: 0x77e0
   __DATA_CONST.__got: 0x568
-  __DATA_CONST.__const: 0x2b8
+  __DATA_CONST.__const: 0x2d0
   __DATA_CONST.__objc_classlist: 0x140
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x27a8
+  __DATA_CONST.__objc_selrefs: 0x2970
   __DATA_CONST.__objc_superrefs: 0x110
-  __DATA_CONST.__objc_arraydata: 0x118
+  __DATA_CONST.__objc_arraydata: 0x190
   __AUTH_CONST.__auth_got: 0x4a0
-  __AUTH_CONST.__const: 0xdf0
-  __AUTH_CONST.__cfstring: 0x21a0
-  __AUTH_CONST.__objc_const: 0x5968
+  __AUTH_CONST.__const: 0xea0
+  __AUTH_CONST.__cfstring: 0x2260
+  __AUTH_CONST.__objc_const: 0x5680
   __AUTH_CONST.__objc_doubleobj: 0x60
   __AUTH_CONST.__objc_intobj: 0xc0
-  __AUTH_CONST.__objc_arrayobj: 0x138
+  __AUTH_CONST.__objc_arrayobj: 0x168
   __AUTH_CONST.__objc_floatobj: 0x20
   __AUTH.__objc_data: 0xc80
-  __DATA.__objc_ivar: 0x4d4
+  __DATA.__objc_ivar: 0x4ec
   __DATA.__data: 0x3f8
-  __DATA.__bss: 0x1b0
+  __DATA.__bss: 0x1c0
   - /System/Library/Frameworks/AVFAudio.framework/Versions/A/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: ABD12D79-5C67-395E-91AB-750AD4875CBA
-  Functions: 1297
-  Symbols:   3447
-  CStrings:  2891
+  UUID: 0B6140AB-C54C-3320-B437-F293AA309A31
+  Functions: 1335
+  Symbols:   3520
+  CStrings:  2953
 
Symbols:
+ +[AVPlayerController assetInspectionKeysForInterstitial]
+ +[AVPlayerController assetInspectionKeysForPrimary]
+ +[AVPlayerController videoTrackInspectionKeysForPrimary]
+ +[AVPlayerController(AVMediaSelection) _optionsForGroup:asset:]
+ +[AVPlayerController(AVMediaSelection) keyPathsForValuesAffectingCurrentAssetForAudioAndLegibleOptions]
+ -[AVKitGlobalSettings _platformSupportsIntegratedTimeline]
+ -[AVKitGlobalSettings animatedSkipButtonsEnabled]
+ -[AVKitGlobalSettings isIntegratedTimelineEnabledForLiveStreams]
+ -[AVKitGlobalSettings isIntegratedTimelineEnabled]
+ -[AVKitGlobalSettings playerTipsEnabled]
+ -[AVKitGlobalSettings prefersTintColorForPlaybackControlsView]
+ -[AVKitGlobalSettings timelineDiagnosticsEnabled]
+ -[AVPlayerController _activeTimebaseForUI]
+ -[AVPlayerController _anchorTimeWithTime:]
+ -[AVPlayerController _prepareAssetForInspection:assetKeys:videoTrackKeys:completion:]
+ -[AVPlayerController currentEnabledAssetTrackForMediaType:completionHandler:]
+ -[AVPlayerController interstitialAssetBeingPrepared]
+ -[AVPlayerController interstitialAssetIfReady]
+ -[AVPlayerController setInterstitialAssetBeingPrepared:]
+ -[AVPlayerController setInterstitialAssetIfReady:]
+ -[AVPlayerController setTimeline:]
+ -[AVPlayerController timeline]
+ -[AVPlayerController(AVMediaSelection) _legibleOptionsForPlayerItem:asset:]
+ -[AVPlayerController(AVMediaSelection) _mediaSelectionCriteriaCanBeAppliedAutomaticallyToLegibleMediaSelectionGroupForPlayerItem:asset:]
+ -[AVPlayerController(AVMediaSelection) _playableLegibleMediaSelectionOptionsForAsset:]
+ -[AVPlayerController(AVMediaSelection) _preferredLanguageCodesForPlayer:]
+ -[AVPlayerController(AVMediaSelection) _selectedMediaOptionWithMediaCharacteristic:playerItem:asset:]
+ -[AVPlayerController(AVMediaSelection) audioOptionsForAsset:]
+ -[AVPlayerController(AVMediaSelection) currentAssetForAudioAndLegibleOptions]
+ -[AVPlayerController(AVMediaSelection) currentAudioMediaSelectionOptionForPlayerItem:asset:]
+ -[AVPlayerController(AVMediaSelection) playerItemForAudioAndLegibleOptions]
+ GCC_except_table1070
+ GCC_except_table1080
+ GCC_except_table1082
+ GCC_except_table1083
+ GCC_except_table1152
+ GCC_except_table1162
+ GCC_except_table1274
+ GCC_except_table1276
+ GCC_except_table1329
+ GCC_except_table321
+ GCC_except_table334
+ GCC_except_table439
+ GCC_except_table583
+ GCC_except_table587
+ GCC_except_table588
+ GCC_except_table623
+ GCC_except_table631
+ GCC_except_table684
+ GCC_except_table708
+ GCC_except_table712
+ GCC_except_table714
+ GCC_except_table785
+ GCC_except_table808
+ GCC_except_table847
+ GCC_except_table859
+ GCC_except_table861
+ GCC_except_table958
+ OBJC_IVAR_$_AVKitGlobalSettings._animatedSkipButtonsEnabled
+ OBJC_IVAR_$_AVKitGlobalSettings._playerTipsEnabled
+ OBJC_IVAR_$_AVKitGlobalSettings._prefersTintColorForPlaybackControlsView
+ OBJC_IVAR_$_AVPlayerController._interstitialAssetBeingPrepared
+ OBJC_IVAR_$_AVPlayerController._interstitialAssetIfReady
+ OBJC_IVAR_$_AVPlayerController._timeline
+ VisionKitCoreLibraryCore.frameworkLibrary.1686
+ _AVIntervalSkipGlyphStateNameState1
+ _AVIntervalSkipGlyphStateNameState2
+ _AVMicaPackageNameIntervalSkipGlyph
+ __30-[AVPlayerController startKVO]_block_invoke.118
+ __33-[AVPlayerController setPlaying:]_block_invoke.281
+ __33-[AVPlayerController setPlaying:]_block_invoke_2.282
+ __33-[AVPlayerController setPlaying:]_block_invoke_3.283
+ __40-[AVPlayerController actuallySeekToTime]_block_invoke.382
+ __40-[AVPlayerController actuallySeekToTime]_block_invoke.383
+ __45-[AVPlayerController startInspectionIfNeeded]_block_invoke.44
+ __45-[AVPlayerController startInspectionIfNeeded]_block_invoke.62
+ __45-[AVPlayerController startInspectionIfNeeded]_block_invoke_2.65
+ __45-[AVPlayerController startInspectionIfNeeded]_block_invoke_3.68
+ __45-[AVPlayerController startInspectionIfNeeded]_block_invoke_4.75
+ __45-[AVPlayerController startInspectionIfNeeded]_block_invoke_5.79
+ __64-[AVPlayerController _observeValueForKeyPath:oldValue:newValue:]_block_invoke.194
+ __64-[AVPlayerController _observeValueForKeyPath:oldValue:newValue:]_block_invoke.206
+ __64-[AVPlayerController _observeValueForKeyPath:oldValue:newValue:]_block_invoke.215
+ __64-[AVPlayerController _observeValueForKeyPath:oldValue:newValue:]_block_invoke.223
+ __64-[AVPlayerController _observeValueForKeyPath:oldValue:newValue:]_block_invoke.229
+ __64-[AVPlayerController _observeValueForKeyPath:oldValue:newValue:]_block_invoke.261
+ __64-[AVPlayerController _observeValueForKeyPath:oldValue:newValue:]_block_invoke_2.205
+ __64-[AVPlayerController _observeValueForKeyPath:oldValue:newValue:]_block_invoke_2.211
+ __64-[AVPlayerController _observeValueForKeyPath:oldValue:newValue:]_block_invoke_2.219
+ __64-[AVPlayerController _observeValueForKeyPath:oldValue:newValue:]_block_invoke_2.230
+ __Block_byref_object_copy_.1039
+ __Block_byref_object_copy_.418
+ __Block_byref_object_copy_.610
+ __Block_byref_object_dispose_.1040
+ __Block_byref_object_dispose_.419
+ __Block_byref_object_dispose_.611
+ __VisionKitCoreLibraryCore_block_invoke.1687
+ ___51+[AVPlayerController assetInspectionKeysForPrimary]_block_invoke
+ ___54-[AVPlayerController _updateCurrentAudioTrackIfNeeded]_block_invoke
+ ___54-[AVPlayerController _updateCurrentVideoTrackIfNeeded]_block_invoke
+ ___61-[AVPlayerController(AVMediaSelection) audioOptionsForAsset:]_block_invoke
+ ___75-[AVPlayerController(AVMediaSelection) _legibleOptionsForPlayerItem:asset:]_block_invoke
+ ___75-[AVPlayerController(AVMediaSelection) _legibleOptionsForPlayerItem:asset:]_block_invoke_2
+ ___77-[AVPlayerController currentEnabledAssetTrackForMediaType:completionHandler:]_block_invoke
+ ___77-[AVPlayerController currentEnabledAssetTrackForMediaType:completionHandler:]_block_invoke_2
+ ___85-[AVPlayerController _prepareAssetForInspection:assetKeys:videoTrackKeys:completion:]_block_invoke
+ ___85-[AVPlayerController _prepareAssetForInspection:assetKeys:videoTrackKeys:completion:]_block_invoke_2
+ ___85-[AVPlayerController _prepareAssetForInspection:assetKeys:videoTrackKeys:completion:]_block_invoke_3
+ ___85-[AVPlayerController _prepareAssetForInspection:assetKeys:videoTrackKeys:completion:]_block_invoke_4
+ ___block_descriptor_40_e8_32w_e22_v16?0"AVAssetTrack"8l
+ ___block_descriptor_48_e8_32w40w_e5_v8?0l
+ ___block_descriptor_64_e8_32s40bs48r56w_e5_v8?0l
+ ___block_descriptor_64_e8_32s40bs48w56w_e5_v8?0l
+ ___block_descriptor_73_e8_32s40s48bs56r64w_e5_v8?0l
+ ___copy_helper_block_e8_32s40b48r56w
+ ___copy_helper_block_e8_32s40b48w56w
+ ___copy_helper_block_e8_32s40s48b56r64w
+ ___copy_helper_block_e8_32w40w
+ ___destroy_helper_block_e8_32s40s48r56w
+ ___destroy_helper_block_e8_32s40s48w56w
+ ___destroy_helper_block_e8_32w40w
+ __block_literal_global.1122
+ __block_literal_global.120
+ __block_literal_global.125
+ __block_literal_global.133
+ __block_literal_global.138.1119
+ __block_literal_global.1459
+ __block_literal_global.147
+ __block_literal_global.1535
+ __block_literal_global.155
+ __block_literal_global.163
+ __block_literal_global.165
+ __block_literal_global.1697
+ __block_literal_global.1712
+ __block_literal_global.1975
+ __block_literal_global.2137
+ __block_literal_global.218
+ __block_literal_global.2240
+ __block_literal_global.2375
+ __block_literal_global.437
+ __block_literal_global.450
+ __block_literal_global.46
+ __block_literal_global.472
+ __block_literal_global.53
+ __block_literal_global.55
+ __block_literal_global.55.1124
+ __block_literal_global.57
+ __block_literal_global.637
+ __block_literal_global.64
+ __block_literal_global.67
+ __block_literal_global.683
+ __block_literal_global.70
+ __block_literal_global.78
+ __block_literal_global.825
+ __getVKCImageAnalyzerClass_block_invoke.1685
+ _objc_msgSend$_activeTimebaseForUI
+ _objc_msgSend$_anchorTimeWithTime:
+ _objc_msgSend$_legibleOptionsForPlayerItem:asset:
+ _objc_msgSend$_mediaSelectionCriteriaCanBeAppliedAutomaticallyToLegibleMediaSelectionGroupForPlayerItem:asset:
+ _objc_msgSend$_optionsForGroup:asset:
+ _objc_msgSend$_platformSupportsIntegratedTimeline
+ _objc_msgSend$_playableLegibleMediaSelectionOptionsForAsset:
+ _objc_msgSend$_preferredLanguageCodesForPlayer:
+ _objc_msgSend$_prepareAssetForInspection:assetKeys:videoTrackKeys:completion:
+ _objc_msgSend$_selectedMediaOptionWithMediaCharacteristic:playerItem:asset:
+ _objc_msgSend$activeAssetIfReady
+ _objc_msgSend$assetInspectionKeysForPrimary
+ _objc_msgSend$audioOptionsForAsset:
+ _objc_msgSend$currentAssetForAudioAndLegibleOptions
+ _objc_msgSend$currentEnabledAssetTrackForMediaType:completionHandler:
+ _objc_msgSend$isIntegratedTimelineEnabled
+ _objc_msgSend$playerItemForAudioAndLegibleOptions
+ _objc_msgSend$timeline
+ _objc_msgSend$videoTrackInspectionKeysForPrimary
+ assetInspectionKeysForPrimary._assetKeysOfInterest
+ assetInspectionKeysForPrimary.onceToken
+ audit_stringVisionKitCore.1689
+ getVKCImageAnalyzerClass.softClass.1684
- -[AVPlayerController currentEnabledAssetTrackForMediaType:]
- GCC_except_table1037
- GCC_except_table1047
- GCC_except_table1049
- GCC_except_table1050
- GCC_except_table1112
- GCC_except_table1122
- GCC_except_table1234
- GCC_except_table1236
- GCC_except_table1290
- GCC_except_table316
- GCC_except_table328
- GCC_except_table428
- GCC_except_table566
- GCC_except_table567
- GCC_except_table570
- GCC_except_table603
- GCC_except_table611
- GCC_except_table662
- GCC_except_table682
- GCC_except_table757
- GCC_except_table780
- GCC_except_table818
- GCC_except_table830
- GCC_except_table832
- GCC_except_table925
- VisionKitCoreLibraryCore.frameworkLibrary.1636
- __30-[AVPlayerController startKVO]_block_invoke.117
- __33-[AVPlayerController setPlaying:]_block_invoke.280
- __33-[AVPlayerController setPlaying:]_block_invoke_2.281
- __33-[AVPlayerController setPlaying:]_block_invoke_3.282
- __40-[AVPlayerController actuallySeekToTime]_block_invoke.378
- __40-[AVPlayerController actuallySeekToTime]_block_invoke.379
- __45-[AVPlayerController startInspectionIfNeeded]_block_invoke.61
- __45-[AVPlayerController startInspectionIfNeeded]_block_invoke_2.64
- __45-[AVPlayerController startInspectionIfNeeded]_block_invoke_3.67
- __45-[AVPlayerController startInspectionIfNeeded]_block_invoke_4.74
- __45-[AVPlayerController startInspectionIfNeeded]_block_invoke_5.78
- __56-[AVPlayerController _prepareAssetForInspectionIfNeeded]_block_invoke.488
- __56-[AVPlayerController _prepareAssetForInspectionIfNeeded]_block_invoke.514
- __56-[AVPlayerController _prepareAssetForInspectionIfNeeded]_block_invoke_2.489
- __64-[AVPlayerController _observeValueForKeyPath:oldValue:newValue:]_block_invoke.192
- __64-[AVPlayerController _observeValueForKeyPath:oldValue:newValue:]_block_invoke.205
- __64-[AVPlayerController _observeValueForKeyPath:oldValue:newValue:]_block_invoke.214
- __64-[AVPlayerController _observeValueForKeyPath:oldValue:newValue:]_block_invoke.222
- __64-[AVPlayerController _observeValueForKeyPath:oldValue:newValue:]_block_invoke.227
- __64-[AVPlayerController _observeValueForKeyPath:oldValue:newValue:]_block_invoke.260
- __64-[AVPlayerController _observeValueForKeyPath:oldValue:newValue:]_block_invoke_2.204
- __64-[AVPlayerController _observeValueForKeyPath:oldValue:newValue:]_block_invoke_2.210
- __64-[AVPlayerController _observeValueForKeyPath:oldValue:newValue:]_block_invoke_2.218
- __64-[AVPlayerController _observeValueForKeyPath:oldValue:newValue:]_block_invoke_2.229
- __Block_byref_object_copy_.1028
- __Block_byref_object_copy_.423
- __Block_byref_object_copy_.590
- __Block_byref_object_dispose_.1029
- __Block_byref_object_dispose_.424
- __Block_byref_object_dispose_.591
- __VisionKitCoreLibraryCore_block_invoke.1637
- ___45-[AVPlayerController startInspectionIfNeeded]_block_invoke_8
- ___52-[AVPlayerController(AVMediaSelection) audioOptions]_block_invoke
- ___54-[AVPlayerController(AVMediaSelection) legibleOptions]_block_invoke
- ___54-[AVPlayerController(AVMediaSelection) legibleOptions]_block_invoke_2
- ___56-[AVPlayerController _prepareAssetForInspectionIfNeeded]_block_invoke_2
- ___56-[AVPlayerController _prepareAssetForInspectionIfNeeded]_block_invoke_3
- ___block_descriptor_56_e8_32s40s48r_e5_v8?0l
- ___block_descriptor_56_e8_32w40w48w_e5_v8?0l
- ___copy_helper_block_e8_32w40w48w
- ___destroy_helper_block_e8_32w40w48w
- __block_literal_global.1089
- __block_literal_global.119
- __block_literal_global.124
- __block_literal_global.132
- __block_literal_global.137
- __block_literal_global.1420
- __block_literal_global.146
- __block_literal_global.1493
- __block_literal_global.154
- __block_literal_global.162
- __block_literal_global.164
- __block_literal_global.1647
- __block_literal_global.1662
- __block_literal_global.1924
- __block_literal_global.2086
- __block_literal_global.217
- __block_literal_global.2191
- __block_literal_global.2327
- __block_literal_global.442
- __block_literal_global.446
- __block_literal_global.45
- __block_literal_global.48
- __block_literal_global.48.1090
- __block_literal_global.52
- __block_literal_global.54
- __block_literal_global.622
- __block_literal_global.63
- __block_literal_global.66
- __block_literal_global.668
- __block_literal_global.69
- __block_literal_global.77
- __block_literal_global.811
- __getVKCImageAnalyzerClass_block_invoke.1635
- _objc_msgSend$_optionsForGroup:
- _objc_msgSend$currentEnabledAssetTrackForMediaType:
- audit_stringVisionKitCore.1639
- getVKCImageAnalyzerClass.softClass.1634
CStrings:
+ "%s Main player rate changed. rate = %f, item currentTime = %f"
+ "-[AVPlayerController startInspectionIfNeeded]_block_invoke"
+ "@\"AVKitIntegratedTimeline\""
+ "IntervalSkipGlyph"
+ "State 1"
+ "State 2"
+ "T@\"AVAsset\",&,V_interstitialAssetBeingPrepared"
+ "T@\"AVAsset\",&,V_interstitialAssetIfReady"
+ "T@\"AVKitIntegratedTimeline\",&,V_timeline"
+ "TB,R,N,V_animatedSkipButtonsEnabled"
+ "TB,R,N,V_playerTipsEnabled"
+ "TB,R,N,V_prefersTintColorForPlaybackControlsView"
+ "TimelineDiagnostics"
+ "^{OpaqueCMTimebase=}16@0:8"
+ "_activeTimebaseForUI"
+ "_anchorTimeWithTime:"
+ "_animatedSkipButtonsEnabled"
+ "_interstitialAssetBeingPrepared"
+ "_interstitialAssetIfReady"
+ "_legibleOptionsForPlayerItem:asset:"
+ "_mediaSelectionCriteriaCanBeAppliedAutomaticallyToLegibleMediaSelectionGroupForPlayerItem:asset:"
+ "_optionsForGroup:asset:"
+ "_platformSupportsIntegratedTimeline"
+ "_playableLegibleMediaSelectionOptionsForAsset:"
+ "_playerTipsEnabled"
+ "_preferredLanguageCodesForPlayer:"
+ "_prefersTintColorForPlaybackControlsView"
+ "_prepareAssetForInspection:assetKeys:videoTrackKeys:completion:"
+ "_selectedMediaOptionWithMediaCharacteristic:playerItem:asset:"
+ "_timeline"
+ "activeAssetIfReady"
+ "animatedSkipButtons"
+ "animatedSkipButtonsEnabled"
+ "assetInspectionKeysForInterstitial"
+ "assetInspectionKeysForPrimary"
+ "audioOptionsForAsset:"
+ "currentAssetForAudioAndLegibleOptions"
+ "currentAudioMediaSelectionOptionForPlayerItem:asset:"
+ "currentEnabledAssetTrackForMediaType:completionHandler:"
+ "interstitialAssetBeingPrepared"
+ "interstitialAssetIfReady"
+ "isIntegratedTimelineEnabled"
+ "isIntegratedTimelineEnabledForLiveStreams"
+ "keyPathsForValuesAffectingCurrentAssetForAudioAndLegibleOptions"
+ "playerItemForAudioAndLegibleOptions"
+ "playerTipsEnabled"
+ "prefersTintColorForPlaybackControlsView"
+ "setInterstitialAssetBeingPrepared:"
+ "setInterstitialAssetIfReady:"
+ "setTimeline:"
+ "timeline"
+ "timelineDiagnosticsEnabled"
+ "tintColorForPlaybackControlsView"
+ "v16@?0@\"AVAssetTrack\"8"
+ "videoTrackInspectionKeysForPrimary"
+ "\xf0\xf0\xc1\xf0\xf0!"
- "currentEnabledAssetTrackForMediaType:"
- "\xf0\xf0\xc1\xf0\xf1"

```
