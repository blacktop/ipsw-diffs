## AudioSession

> `/System/Library/PrivateFrameworks/AudioSession.framework/AudioSession`

```diff

-263.1.8.30.2
-  __TEXT.__text: 0x33ac0
+263.2.7.0.0
+  __TEXT.__text: 0x33cd0
   __TEXT.__auth_stubs: 0xb00
-  __TEXT.__objc_methlist: 0x1658
-  __TEXT.__gcc_except_tab: 0x5178
-  __TEXT.__cstring: 0x1ed4
+  __TEXT.__objc_methlist: 0x15d8
+  __TEXT.__gcc_except_tab: 0x51dc
+  __TEXT.__cstring: 0x1f10
   __TEXT.__const: 0x230
-  __TEXT.__oslogstring: 0x2175
-  __TEXT.__unwind_info: 0x20bc
+  __TEXT.__oslogstring: 0x2201
+  __TEXT.__unwind_info: 0x20c0
   __TEXT.__eh_frame: 0x38
-  __TEXT.__objc_classname: 0x27f
-  __TEXT.__objc_methname: 0x3bc6
+  __TEXT.__objc_classname: 0x25d
+  __TEXT.__objc_methname: 0x3bf8
   __TEXT.__objc_methtype: 0x116d
-  __TEXT.__objc_stubs: 0x2260
-  __DATA_CONST.__got: 0x7c8
-  __DATA_CONST.__const: 0x670
-  __DATA_CONST.__objc_classlist: 0x78
+  __TEXT.__objc_stubs: 0x2280
+  __DATA_CONST.__got: 0x7d8
+  __DATA_CONST.__const: 0x680
+  __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_catlist: 0x0
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1118
-  __DATA_CONST.__objc_selrefs: 0x10c8
+  __DATA_CONST.__objc_const: 0x1018
+  __DATA_CONST.__objc_selrefs: 0x10e0
   __DATA_CONST.__objc_arraydata: 0x8
-  __AUTH_CONST.__cfstring: 0x1ae0
-  __AUTH_CONST.__objc_const: 0x6c0
+  __AUTH_CONST.__cfstring: 0x1aa0
+  __AUTH_CONST.__objc_const: 0x630
   __AUTH_CONST.__const: 0x11c0
   __AUTH_CONST.__objc_intobj: 0x138
   __AUTH_CONST.__objc_doubleobj: 0x30

   __AUTH.__objc_data: 0xa0
   __DATA.__got_weak: 0x8
   __DATA.__objc_classrefs: 0xf8
-  __DATA.__objc_superrefs: 0x70
-  __DATA.__objc_ivar: 0x6c
+  __DATA.__objc_superrefs: 0x68
+  __DATA.__objc_ivar: 0x5c
   __DATA.__data: 0x370
   __DATA.__common: 0x1
   __DATA.__bss: 0xd0
-  __DATA_DIRTY.__objc_data: 0x410
+  __DATA_DIRTY.__objc_data: 0x3c0
   __DATA_DIRTY.__data: 0xb0
   __DATA_DIRTY.__bss: 0x110
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F0DC4821-7235-3676-8DB2-E9FD2C0CA323
-  Functions: 1192
-  Symbols:   4155
-  CStrings:  1406
+  UUID: A49E57B5-D84F-3108-9DD6-58F7553716F7
+  Functions: 1184
+  Symbols:   4132
+  CStrings:  1400
 
Symbols:
+ +[AVAudioApplication(SPI) allowAppToInitiatePlaybackTemporarily:error:]
+ -[AVAudioSession prefersConcurrentAirPlayAudio]
+ -[AVAudioSession privateHandlePrefersConcurrentAirPlayAudioChange:]
+ -[AVAudioSession setPrefersConcurrentAirPlayAudio:error:]
+ GCC_except_table171
+ GCC_except_table174
+ GCC_except_table183
+ GCC_except_table210
+ GCC_except_table214
+ GCC_except_table235
+ GCC_except_table242
+ GCC_except_table243
+ GCC_except_table246
+ GCC_except_table255
+ GCC_except_table256
+ GCC_except_table268
+ GCC_except_table269
+ GCC_except_table282
+ GCC_except_table283
+ GCC_except_table300
+ GCC_except_table301
+ GCC_except_table304
+ GCC_except_table305
+ GCC_except_table309
+ GCC_except_table322
+ GCC_except_table329
+ GCC_except_table334
+ GCC_except_table344
+ GCC_except_table354
+ GCC_except_table355
+ GCC_except_table356
+ GCC_except_table372
+ GCC_except_table374
+ GCC_except_table385
+ GCC_except_table387
+ GCC_except_table406
+ GCC_except_table410
+ GCC_except_table415
+ GCC_except_table442
+ GCC_except_table452
+ GCC_except_table456
+ GCC_except_table457
+ GCC_except_table468
+ GCC_except_table472
+ GCC_except_table494
+ GCC_except_table495
+ GCC_except_table506
+ GCC_except_table510
+ GCC_except_table511
+ GCC_except_table512
+ GCC_except_table523
+ GCC_except_table527
+ GCC_except_table529
+ GCC_except_table536
+ GCC_except_table543
+ GCC_except_table554
+ GCC_except_table578
+ GCC_except_table584
+ GCC_except_table585
+ GCC_except_table586
+ GCC_except_table592
+ GCC_except_table593
+ GCC_except_table603
+ GCC_except_table611
+ GCC_except_table613
+ GCC_except_table636
+ GCC_except_table637
+ GCC_except_table642
+ GCC_except_table643
+ GCC_except_table656
+ GCC_except_table657
+ GCC_except_table665
+ GCC_except_table666
+ GCC_except_table681
+ GCC_except_table682
+ GCC_except_table683
+ GCC_except_table693
+ GCC_except_table697
+ GCC_except_table698
+ GCC_except_table699
+ GCC_except_table709
+ GCC_except_table713
+ _AVAudioSessionConcurrentAirPlayAudioPreferenceChangeNotification
+ _AVAudioSessionConcurrentAirPlayAudioPreferredKey
+ ___56-[AVAudioSession activateWithOptions:completionHandler:]_block_invoke.138
+ ___block_literal_global.121
+ ___block_literal_global.57
+ _kMXSessionProperty_PrefersInterruptionOnRouteDisconnect
+ _kMXSessionProperty_PrefersSpeechDetectEnabled
+ _objc_msgSend$allowAppToInitiatePlaybackTemporarilyFromBackground:reply:
+ _objc_msgSend$privateHandlePrefersConcurrentAirPlayAudioChange:
+ _objc_msgSend$setProperties:values:MXProperties:batchStrategy:genericMXPipe:reply:
- +[AVAudioApplicationSpecification supportsSecureCoding]
- -[AVAudioApplicationSpecification .cxx_destruct]
- -[AVAudioApplicationSpecification appAuditToken]
- -[AVAudioApplicationSpecification attributionBundleID]
- -[AVAudioApplicationSpecification audioAppType]
- -[AVAudioApplicationSpecification encodeWithCoder:]
- -[AVAudioApplicationSpecification initWithCoder:]
- -[AVAudioApplicationSpecification processName]
- -[AVAudioApplicationSpecification setAppAuditToken:]
- -[AVAudioApplicationSpecification setAttributionBundleID:]
- -[AVAudioApplicationSpecification setAudioAppType:]
- -[AVAudioApplicationSpecification setProcessName:]
- GCC_except_table166
- GCC_except_table173
- GCC_except_table178
- GCC_except_table185
- GCC_except_table212
- GCC_except_table216
- GCC_except_table237
- GCC_except_table244
- GCC_except_table245
- GCC_except_table250
- GCC_except_table259
- GCC_except_table260
- GCC_except_table270
- GCC_except_table271
- GCC_except_table287
- GCC_except_table288
- GCC_except_table302
- GCC_except_table303
- GCC_except_table306
- GCC_except_table310
- GCC_except_table312
- GCC_except_table325
- GCC_except_table332
- GCC_except_table337
- GCC_except_table350
- GCC_except_table362
- GCC_except_table363
- GCC_except_table364
- GCC_except_table378
- GCC_except_table403
- GCC_except_table407
- GCC_except_table412
- GCC_except_table439
- GCC_except_table446
- GCC_except_table450
- GCC_except_table451
- GCC_except_table465
- GCC_except_table466
- GCC_except_table491
- GCC_except_table492
- GCC_except_table503
- GCC_except_table504
- GCC_except_table508
- GCC_except_table509
- GCC_except_table520
- GCC_except_table521
- GCC_except_table526
- GCC_except_table533
- GCC_except_table540
- GCC_except_table551
- GCC_except_table575
- GCC_except_table579
- GCC_except_table580
- GCC_except_table581
- GCC_except_table589
- GCC_except_table590
- GCC_except_table600
- GCC_except_table608
- GCC_except_table610
- GCC_except_table633
- GCC_except_table634
- GCC_except_table639
- GCC_except_table640
- GCC_except_table653
- GCC_except_table654
- GCC_except_table662
- GCC_except_table663
- GCC_except_table678
- GCC_except_table679
- GCC_except_table680
- GCC_except_table690
- GCC_except_table691
- GCC_except_table695
- GCC_except_table696
- GCC_except_table706
- GCC_except_table707
- _OBJC_IVAR_$_AVAudioApplicationSpecification._appAuditToken
- _OBJC_IVAR_$_AVAudioApplicationSpecification.attributionBundleID
- _OBJC_IVAR_$_AVAudioApplicationSpecification.audioAppType
- _OBJC_IVAR_$_AVAudioApplicationSpecification.processName
- _OBJC_METACLASS_$_AVAudioApplicationSpecification
- __OBJC_$_CLASS_METHODS_AVAudioApplicationSpecification
- __OBJC_$_CLASS_PROP_LIST_AVAudioApplicationSpecification
- __OBJC_$_INSTANCE_METHODS_AVAudioApplicationSpecification
- __OBJC_$_INSTANCE_VARIABLES_AVAudioApplicationSpecification
- __OBJC_$_PROP_LIST_AVAudioApplicationSpecification
- __OBJC_CLASS_PROTOCOLS_$_AVAudioApplicationSpecification
- __OBJC_CLASS_RO_$_AVAudioApplicationSpecification
- __OBJC_METACLASS_RO_$_AVAudioApplicationSpecification
- ___56-[AVAudioSession activateWithOptions:completionHandler:]_block_invoke.135
- ___block_literal_global.118
- ___block_literal_global.54
- _objc_msgSend$setMXPropertyGenericPipe:values:reply:
- _objc_msgSend$setProperties:values:MXProperties:batchStrategy:reply:
CStrings:
+ "%25s:%-5d Notifying listeners that available Concurrent Airplay Audio changed"
+ "%25s:%-5d Request to initiate playback from background failed"
+ "AVAudioSessionConcurrentAirPlayAudioPreferenceChangeNotification"
+ "AVAudioSessionConcurrentAirPlayAudioPreferredKey"
+ "PrefersConcurrentAirPlayAudio"
+ "PrefersConcurrentAirPlayAudioDidChange"
+ "allowAppToInitiatePlaybackTemporarily:error:"
+ "allowAppToInitiatePlaybackTemporarilyFromBackground:reply:"
+ "prefersConcurrentAirPlayAudio"
+ "privateHandlePrefersConcurrentAirPlayAudioChange:"
+ "setPrefersConcurrentAirPlayAudio:error:"
+ "setProperties:values:MXProperties:batchStrategy:genericMXPipe:reply:"
- "\x12"
- "AVAudioApplicationSpecification"
- "PrefersInterruptionOnRouteDisconnect"
- "PrefersSpeechDetectEnabled"
- "T@\"NSString\",&,N,VattributionBundleID"
- "T@\"NSString\",&,N,VprocessName"
- "Tq,N,VaudioAppType"
- "T{?=[8I]},N,V_appAuditToken"
- "_appAuditToken"
- "attributionBundleID"
- "setMXPropertyGenericPipe:values:reply:"
- "setProperties:values:MXProperties:batchStrategy:reply:"

```
