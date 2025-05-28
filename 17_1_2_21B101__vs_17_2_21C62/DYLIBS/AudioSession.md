## AudioSession

> `/System/Library/PrivateFrameworks/AudioSession.framework/AudioSession`

```diff

-263.2.7.0.0
-  __TEXT.__text: 0x33cd0
-  __TEXT.__auth_stubs: 0xb00
-  __TEXT.__objc_methlist: 0x15d8
-  __TEXT.__gcc_except_tab: 0x51dc
-  __TEXT.__cstring: 0x1f10
+263.3.7.0.0
+  __TEXT.__text: 0x347b0
+  __TEXT.__auth_stubs: 0xb30
+  __TEXT.__objc_methlist: 0x1608
+  __TEXT.__gcc_except_tab: 0x533c
+  __TEXT.__cstring: 0x1fa3
   __TEXT.__const: 0x230
-  __TEXT.__oslogstring: 0x2201
-  __TEXT.__unwind_info: 0x20c0
+  __TEXT.__oslogstring: 0x234f
+  __TEXT.__unwind_info: 0x2118
   __TEXT.__eh_frame: 0x38
   __TEXT.__objc_classname: 0x25d
-  __TEXT.__objc_methname: 0x3bf8
+  __TEXT.__objc_methname: 0x3c80
   __TEXT.__objc_methtype: 0x116d
-  __TEXT.__objc_stubs: 0x2280
-  __DATA_CONST.__got: 0x7d8
-  __DATA_CONST.__const: 0x680
+  __TEXT.__objc_stubs: 0x22e0
+  __DATA_CONST.__got: 0x868
+  __DATA_CONST.__const: 0x698
   __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_catlist: 0x0
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1018
-  __DATA_CONST.__objc_selrefs: 0x10e0
+  __DATA_CONST.__objc_const: 0x1028
+  __DATA_CONST.__objc_selrefs: 0x1108
   __DATA_CONST.__objc_arraydata: 0x8
   __AUTH_CONST.__cfstring: 0x1aa0
   __AUTH_CONST.__objc_const: 0x630

   __AUTH_CONST.__objc_doubleobj: 0x30
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_floatobj: 0x40
-  __AUTH_CONST.__auth_got: 0x590
+  __AUTH_CONST.__auth_got: 0x5a8
   __AUTH.__objc_data: 0xa0
   __DATA.__got_weak: 0x8
   __DATA.__objc_classrefs: 0xf8
   __DATA.__objc_superrefs: 0x68
   __DATA.__objc_ivar: 0x5c
-  __DATA.__data: 0x370
+  __DATA.__data: 0x380
   __DATA.__common: 0x1
   __DATA.__bss: 0xd0
   __DATA_DIRTY.__objc_data: 0x3c0

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1184
-  Symbols:   4132
-  CStrings:  1187
+  Functions: 1192
+  Symbols:   4184
+  CStrings:  1198
 
Symbols:
+ -[AVAudioSession privateHandleBadgeTypeChange:]
+ -[AVAudioSession privateHandleRenderingCapabilitiesChange]
+ -[AVAudioSession renderingMode]
+ -[AVAudioSession supportedOutputChannelLayouts]
+ GCC_except_table212
+ GCC_except_table216
+ GCC_except_table237
+ GCC_except_table244
+ GCC_except_table248
+ GCC_except_table250
+ GCC_except_table257
+ GCC_except_table270
+ GCC_except_table284
+ GCC_except_table285
+ GCC_except_table286
+ GCC_except_table302
+ GCC_except_table303
+ GCC_except_table307
+ GCC_except_table312
+ GCC_except_table325
+ GCC_except_table332
+ GCC_except_table347
+ GCC_except_table350
+ GCC_except_table357
+ GCC_except_table358
+ GCC_except_table359
+ GCC_except_table360
+ GCC_except_table361
+ GCC_except_table375
+ GCC_except_table377
+ GCC_except_table378
+ GCC_except_table380
+ GCC_except_table388
+ GCC_except_table390
+ GCC_except_table391
+ GCC_except_table393
+ GCC_except_table412
+ GCC_except_table416
+ GCC_except_table421
+ GCC_except_table448
+ GCC_except_table455
+ GCC_except_table460
+ GCC_except_table461
+ GCC_except_table462
+ GCC_except_table464
+ GCC_except_table465
+ GCC_except_table476
+ GCC_except_table477
+ GCC_except_table480
+ GCC_except_table502
+ GCC_except_table503
+ GCC_except_table514
+ GCC_except_table515
+ GCC_except_table518
+ GCC_except_table519
+ GCC_except_table520
+ GCC_except_table531
+ GCC_except_table532
+ GCC_except_table535
+ GCC_except_table537
+ GCC_except_table544
+ GCC_except_table551
+ GCC_except_table562
+ GCC_except_table590
+ GCC_except_table591
+ GCC_except_table594
+ GCC_except_table600
+ GCC_except_table601
+ GCC_except_table619
+ GCC_except_table621
+ GCC_except_table644
+ GCC_except_table645
+ GCC_except_table650
+ GCC_except_table651
+ GCC_except_table664
+ GCC_except_table673
+ GCC_except_table674
+ GCC_except_table689
+ GCC_except_table690
+ GCC_except_table691
+ GCC_except_table701
+ GCC_except_table702
+ GCC_except_table705
+ GCC_except_table706
+ GCC_except_table707
+ GCC_except_table717
+ GCC_except_table718
+ GCC_except_table721
+ _AVAudioSessionRenderingCapabilitiesChangeNotification
+ _AVAudioSessionRenderingModeChangeNotification
+ _AVAudioSessionRenderingModeNewRenderingModeKey
+ _NSClassFromString
+ __ZGVZN11AVFSoftLink8instanceEvE9gInstance
+ __ZN11AVFSoftLink8instanceEv
+ __ZN11AVFSoftLinkC2Ev
+ __ZN12_GLOBAL__N_126TranslateFromMXBadgingTypeEP8NSString
+ __ZZN11AVFSoftLink8instanceEvE9gInstance
+ ___56-[AVAudioSession activateWithOptions:completionHandler:]_block_invoke.129
+ ____ZL21HandleDeferredMessageP14AVAudioSessionP8NSStringP12NSDictionary_block_invoke_11
+ _dlopen
+ _kMXSessionNotificationKey_BadgeTypeDidChange_BadgeType
+ _kMXSessionNotificationKey_PrefersConcurrentAirPlayAudio
+ _kMXSessionNotificationKey_ReporterIDsDidChange_ReporterIDs
+ _kMXSessionNotificationKey_SpeechDetectStyleDidChange_MXSessionSpeechDetectStyle
+ _kMXSessionNotification_BadgeTypeDidChange
+ _kMXSessionNotification_PrefersConcurrentAirPlayAudioDidChange
+ _kMXSessionNotification_ReporterIDsDidChange
+ _kMXSessionNotification_SpeechDetectStyleDidChange
+ _kMXSessionProperty_BadgeType
+ _kMXSessionProperty_PrefersConcurrentAirPlayAudio
+ _kMXSessionProperty_SpeechDetectStyle
+ _kMXSessionProperty_UnduckToLevelScalar
+ _kMXSession_BadgeType_DolbyAtmos
+ _kMXSession_BadgeType_DolbyAudio
+ _kMXSession_BadgeType_NotApplicable
+ _kMXSession_BadgeType_SpatialAudio
+ _kMXSession_BadgeType_Stereo
+ _kMXSession_BadgeType_Surround
+ _objc_msgSend$initWithLayoutTag:
+ _objc_msgSend$privateHandleBadgeTypeChange:
+ _objc_msgSend$privateHandleRenderingCapabilitiesChange
+ _objc_retain_x28
- GCC_except_table213
- GCC_except_table217
- GCC_except_table238
- GCC_except_table246
- GCC_except_table249
- GCC_except_table251
- GCC_except_table261
- GCC_except_table272
- GCC_except_table289
- GCC_except_table290
- GCC_except_table291
- GCC_except_table305
- GCC_except_table309
- GCC_except_table313
- GCC_except_table315
- GCC_except_table330
- GCC_except_table342
- GCC_except_table352
- GCC_except_table355
- GCC_except_table365
- GCC_except_table366
- GCC_except_table367
- GCC_except_table368
- GCC_except_table369
- GCC_except_table381
- GCC_except_table384
- GCC_except_table406
- GCC_except_table410
- GCC_except_table415
- GCC_except_table442
- GCC_except_table449
- GCC_except_table452
- GCC_except_table453
- GCC_except_table454
- GCC_except_table456
- GCC_except_table468
- GCC_except_table469
- GCC_except_table472
- GCC_except_table494
- GCC_except_table495
- GCC_except_table506
- GCC_except_table507
- GCC_except_table510
- GCC_except_table511
- GCC_except_table512
- GCC_except_table523
- GCC_except_table524
- GCC_except_table527
- GCC_except_table529
- GCC_except_table536
- GCC_except_table543
- GCC_except_table554
- GCC_except_table578
- GCC_except_table582
- GCC_except_table583
- GCC_except_table584
- GCC_except_table585
- GCC_except_table603
- GCC_except_table613
- GCC_except_table636
- GCC_except_table637
- GCC_except_table642
- GCC_except_table643
- GCC_except_table656
- GCC_except_table657
- GCC_except_table666
- GCC_except_table681
- GCC_except_table682
- GCC_except_table683
- GCC_except_table693
- GCC_except_table694
- GCC_except_table697
- GCC_except_table698
- GCC_except_table699
- GCC_except_table709
- GCC_except_table710
- GCC_except_table713
- ___56-[AVAudioSession activateWithOptions:completionHandler:]_block_invoke.138
CStrings:
+ "%25s:%-5d Get SupportedOutputChannelLayouts failed with code: %d"
+ "%25s:%-5d Get renderingMode failed with code: %d"
+ "%25s:%-5d Invalid badge type: %@. Returning NotApplicable"
+ "%25s:%-5d Session 0x%x posting AVAudioSessionRenderingCapabilitiesChangeNotification"
+ "%25s:%-5d Session 0x%x posting AVAudioSessionRenderingModeChangeNotification"
+ "/System/Library/Frameworks/AVFoundation.framework/AVFoundation"
+ "AVAudioChannelLayout"
+ "AVAudioFormat"
+ "AVAudioSessionRenderingCapabilitiesChangeNotification"
+ "AVAudioSessionRenderingModeChangeNotification"
+ "AVAudioSessionRenderingModeNewRenderingModeKey"
+ "SupportedOutputChannelLayouts"
+ "SupportedOutputChannelLayoutsDidChange"
+ "initWithLayoutTag:"
+ "privateHandleBadgeTypeChange:"
+ "privateHandleRenderingCapabilitiesChange"
+ "renderingMode"
+ "supportedOutputChannelLayouts"
- "PrefersConcurrentAirPlayAudio"
- "PrefersConcurrentAirPlayAudioDidChange"
- "ReporterIDs"
- "ReporterIDsDidChange"
- "SpeechDetectStyle"
- "SpeechDetectStyleDidChange"
- "UnduckToLevelScalar"

```
