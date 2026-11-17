## AssistantServices

> `/System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices`

```diff

-3610.11.2.0.0
-  __TEXT.__text: 0x19dc98
-  __TEXT.__objc_methlist: 0x1f704
-  __TEXT.__const: 0x3d0
+3610.19.4.0.0
+  __TEXT.__text: 0x19e854
+  __TEXT.__objc_methlist: 0x1f794
+  __TEXT.__const: 0x3e0
   __TEXT.__dlopen_cstrs: 0x538
-  __TEXT.__gcc_except_tab: 0x22e4
-  __TEXT.__cstring: 0x3e593
-  __TEXT.__oslogstring: 0x10683
+  __TEXT.__gcc_except_tab: 0x2334
+  __TEXT.__cstring: 0x3e870
+  __TEXT.__oslogstring: 0x10709
   __TEXT.__ustring: 0x2ac
-  __TEXT.__unwind_info: 0xa170
+  __TEXT.__unwind_info: 0xa1d8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x8890
+  __DATA_CONST.__const: 0x88e8
   __DATA_CONST.__objc_classlist: 0xf00
   __DATA_CONST.__objc_catlist: 0x2a8
   __DATA_CONST.__objc_protolist: 0x608
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc438
+  __DATA_CONST.__objc_selrefs: 0xc4a8
   __DATA_CONST.__objc_protorefs: 0x178
   __DATA_CONST.__objc_superrefs: 0xf18
-  __DATA_CONST.__objc_arraydata: 0x2458
-  __DATA_CONST.__got: 0x1828
-  __AUTH_CONST.__const: 0x3ec0
-  __AUTH_CONST.__cfstring: 0x28cc0
-  __AUTH_CONST.__objc_const: 0x36ad8
+  __DATA_CONST.__objc_arraydata: 0x2308
+  __DATA_CONST.__got: 0x1838
+  __AUTH_CONST.__const: 0x3ee0
+  __AUTH_CONST.__cfstring: 0x28d60
+  __AUTH_CONST.__objc_const: 0x36b38
   __AUTH_CONST.__objc_intobj: 0x2730
   __AUTH_CONST.__objc_dictobj: 0xd20
-  __AUTH_CONST.__objc_arrayobj: 0x5e8
+  __AUTH_CONST.__objc_arrayobj: 0x5b8
   __AUTH_CONST.__objc_doubleobj: 0x40
   __AUTH_CONST.__auth_got: 0xb00
   __AUTH.__objc_data: 0x84f8
-  __AUTH.__data: 0x278
+  __AUTH.__data: 0x280
   __AUTH.__thread_vars: 0x30
   __AUTH.__thread_bss: 0x10
-  __DATA.__objc_ivar: 0x25fc
+  __DATA.__objc_ivar: 0x2604
   __DATA.__data: 0x4988
   __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0x1108
   __DATA_DIRTY.__data: 0x18
-  __DATA_DIRTY.__bss: 0x1c8
+  __DATA_DIRTY.__bss: 0x1a8
   __DATA_DIRTY.__common: 0xf8
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /System/Library/PrivateFrameworks/SAObjects.framework/SAObjects
   - /System/Library/PrivateFrameworks/SiriAnalytics.framework/SiriAnalytics
+  - /System/Library/PrivateFrameworks/SiriAvailability.framework/SiriAvailability
   - /System/Library/PrivateFrameworks/SiriCrossDeviceArbitration.framework/SiriCrossDeviceArbitration
   - /System/Library/PrivateFrameworks/SiriCrossDeviceArbitrationFeedback.framework/SiriCrossDeviceArbitrationFeedback
   - /System/Library/PrivateFrameworks/SiriInstrumentation.framework/SiriInstrumentation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 12346
-  Symbols:   22626
-  CStrings:  8793
+  Functions: 12371
+  Symbols:   22660
+  CStrings:  8812
 
Symbols:
+ +[AFFeatureFlags(SWEFeatureFlags) isHomePodPauseMusicOnRequestEnabled]
+ +[AFFeatureFlags(SWEFeatureFlags) isPebbleFutureLocaleWavesEnabled]
+ +[AFFeatureFlags(SWEFeatureFlags) isPebbleRecognitionWithVoiceProfileEnabled]
+ +[AFFeatureFlags(SWEFeatureFlags) isPebbleVoiceIdMUDownloadEnabled]
+ -[AFDictationConnection _homeAccessoryDictationIsAvailableForLanguage:offlineDictationStatus:]
+ -[AFSettingsConnection fetchCompanionSiriAvailabilityForSetup:completion:]
+ -[AFSiriAvailability isLinwoodCapableIgnoringUserSettingWithCompanionSiriAvailability:]
+ -[AFSpeechConnectionRequestContext initWithRequestId:inputOrigin:]
+ -[AFSpeechConnectionRequestContext inputOrigin]
+ -[_AFSpeechConnectionRequestContextMutation getInputOrigin]
+ -[_AFSpeechConnectionRequestContextMutation setInputOrigin:]
+ GCC_except_table10028
+ GCC_except_table10033
+ GCC_except_table10163
+ GCC_except_table10373
+ GCC_except_table10413
+ GCC_except_table10444
+ GCC_except_table10449
+ GCC_except_table10450
+ GCC_except_table10454
+ GCC_except_table10643
+ GCC_except_table10814
+ GCC_except_table10843
+ GCC_except_table10940
+ GCC_except_table10944
+ GCC_except_table10948
+ GCC_except_table10977
+ GCC_except_table11331
+ GCC_except_table11333
+ GCC_except_table11336
+ GCC_except_table11348
+ GCC_except_table11419
+ GCC_except_table11465
+ GCC_except_table11471
+ GCC_except_table11634
+ GCC_except_table11636
+ GCC_except_table11639
+ GCC_except_table11645
+ GCC_except_table11649
+ GCC_except_table11655
+ GCC_except_table11862
+ GCC_except_table12186
+ GCC_except_table12320
+ GCC_except_table12323
+ GCC_except_table12325
+ GCC_except_table2200
+ GCC_except_table2323
+ GCC_except_table2337
+ GCC_except_table2349
+ GCC_except_table2357
+ GCC_except_table2360
+ GCC_except_table2366
+ GCC_except_table2413
+ GCC_except_table2415
+ GCC_except_table2417
+ GCC_except_table2435
+ GCC_except_table2441
+ GCC_except_table2484
+ GCC_except_table2496
+ GCC_except_table2645
+ GCC_except_table2734
+ GCC_except_table2788
+ GCC_except_table3025
+ GCC_except_table3028
+ GCC_except_table3029
+ GCC_except_table3229
+ GCC_except_table3288
+ GCC_except_table3503
+ GCC_except_table3506
+ GCC_except_table3518
+ GCC_except_table3519
+ GCC_except_table3532
+ GCC_except_table3533
+ GCC_except_table3534
+ GCC_except_table3540
+ GCC_except_table3578
+ GCC_except_table3584
+ GCC_except_table3590
+ GCC_except_table3658
+ GCC_except_table3660
+ GCC_except_table3695
+ GCC_except_table3698
+ GCC_except_table3809
+ GCC_except_table3872
+ GCC_except_table3874
+ GCC_except_table3876
+ GCC_except_table3878
+ GCC_except_table3892
+ GCC_except_table3898
+ GCC_except_table4023
+ GCC_except_table4032
+ GCC_except_table4050
+ GCC_except_table4413
+ GCC_except_table4428
+ GCC_except_table4435
+ GCC_except_table4451
+ GCC_except_table4529
+ GCC_except_table4559
+ GCC_except_table4597
+ GCC_except_table4598
+ GCC_except_table4599
+ GCC_except_table4624
+ GCC_except_table4648
+ GCC_except_table5008
+ GCC_except_table5031
+ GCC_except_table5034
+ GCC_except_table5037
+ GCC_except_table5067
+ GCC_except_table5213
+ GCC_except_table5216
+ GCC_except_table5277
+ GCC_except_table5285
+ GCC_except_table5290
+ GCC_except_table5303
+ GCC_except_table5647
+ GCC_except_table5660
+ GCC_except_table5664
+ GCC_except_table5676
+ GCC_except_table5680
+ GCC_except_table5793
+ GCC_except_table5795
+ GCC_except_table5873
+ GCC_except_table5917
+ GCC_except_table6289
+ GCC_except_table6295
+ GCC_except_table6297
+ GCC_except_table6299
+ GCC_except_table6351
+ GCC_except_table6353
+ GCC_except_table6359
+ GCC_except_table6364
+ GCC_except_table6368
+ GCC_except_table6390
+ GCC_except_table6395
+ GCC_except_table6407
+ GCC_except_table6410
+ GCC_except_table6424
+ GCC_except_table6426
+ GCC_except_table6428
+ GCC_except_table6430
+ GCC_except_table6432
+ GCC_except_table6434
+ GCC_except_table6436
+ GCC_except_table6483
+ GCC_except_table6509
+ GCC_except_table6566
+ GCC_except_table6626
+ GCC_except_table7034
+ GCC_except_table7182
+ GCC_except_table7327
+ GCC_except_table7565
+ GCC_except_table7574
+ GCC_except_table7592
+ GCC_except_table7967
+ GCC_except_table7971
+ GCC_except_table8016
+ GCC_except_table8022
+ GCC_except_table8047
+ GCC_except_table8053
+ GCC_except_table8278
+ GCC_except_table8387
+ GCC_except_table8398
+ GCC_except_table8431
+ GCC_except_table8434
+ GCC_except_table8511
+ GCC_except_table8515
+ GCC_except_table8525
+ GCC_except_table8536
+ GCC_except_table8549
+ GCC_except_table8634
+ GCC_except_table8636
+ GCC_except_table8660
+ GCC_except_table8783
+ GCC_except_table8846
+ GCC_except_table8849
+ GCC_except_table8853
+ GCC_except_table8870
+ GCC_except_table8884
+ GCC_except_table8961
+ GCC_except_table9019
+ GCC_except_table9045
+ GCC_except_table9072
+ GCC_except_table9334
+ GCC_except_table9480
+ GCC_except_table9494
+ GCC_except_table9539
+ GCC_except_table9635
+ GCC_except_table9739
+ GCC_except_table9839
+ _AFAttentionAwarenessSupportsFaceDetect
+ _AFCDAFaceDetectionHelper
+ _AFIsIPad.isiPad
+ _AFIsLinwoodCandidateHomePodWithoutLinwood
+ _AFIsSiriAvailabilityFrameworkLoaded
+ _AFIsSiriAvailabilityFrameworkLoaded.isLoaded
+ _AFIsSiriAvailabilityFrameworkLoaded.onceToken
+ _AFPreferencesRecognizedSpeakerTwentyFourHourTimeDisplay
+ _AFPreferencesSetRecognizedSpeakerTwentyFourHourTimeDisplay
+ _AFRecognizedSpeakerHasNoTwentyFourHourTimeChoice
+ _AFSUPPrefersTwentyFourHourTime
+ _AFSettingsServiceXPCInterface.__onceToken
+ _AFSettingsServiceXPCInterface.interface
+ _AFUsesRecognizedSpeakerTwentyFourHourTime
+ _AWAttentionAwarenessConfigurationFunction
+ _AttentionAwarenessLibrary.frameworkLibrary
+ _OBJC_CLASS_$_SODeviceDescriptor
+ _OBJC_CLASS_$_SOHomePodDescriptor
+ _OBJC_IVAR_$_AFSpeechConnectionRequestContext._inputOrigin
+ _OBJC_IVAR_$__AFSpeechConnectionRequestContextMutation._inputOrigin
+ __AFPreferencesResolveUseDeviceSpeakerForTTS
+ ___66-[AFSpeechConnectionRequestContext initWithRequestId:inputOrigin:]_block_invoke
+ ___74-[AFSettingsConnection fetchCompanionSiriAvailabilityForSetup:completion:]_block_invoke
+ ___74-[AFSettingsConnection fetchCompanionSiriAvailabilityForSetup:completion:]_block_invoke_2
+ ___AFIsSiriAvailabilityFrameworkLoaded_block_invoke
+ ___AFSettingsServiceXPCInterface_block_invoke
+ ___block_descriptor_48_e8_32s40s_e52_v16?0"<AFSpeechConnectionRequestContextMutating>"8ls32l8s40l8
+ ___block_descriptor_56_e8_32s40r48r_e40_v24?0"AFSiriAvailability"8"NSError"16lr40l8r48l8s32l8
+ ___block_descriptor_64_e8_32bs40r48r56r_e8_v16?0q8ls32l8r40l8r48l8r56l8
+ ___initAWAttentionAwarenessConfiguration_block_invoke
+ _classAWAttentionAwarenessConfiguration
+ _getAWAttentionAwarenessConfigurationClass
+ _initAWAttentionAwarenessConfiguration
+ _initAWAttentionAwarenessConfiguration.sOnce
- -[AFSpeechConnectionRequestContext initWithRequestId:]
- GCC_except_table10004
- GCC_except_table10009
- GCC_except_table10139
- GCC_except_table10349
- GCC_except_table10389
- GCC_except_table10420
- GCC_except_table10425
- GCC_except_table10426
- GCC_except_table10430
- GCC_except_table10619
- GCC_except_table10790
- GCC_except_table10819
- GCC_except_table10916
- GCC_except_table10920
- GCC_except_table10924
- GCC_except_table10953
- GCC_except_table11307
- GCC_except_table11309
- GCC_except_table11312
- GCC_except_table11324
- GCC_except_table11394
- GCC_except_table11415
- GCC_except_table11446
- GCC_except_table11605
- GCC_except_table11609
- GCC_except_table11611
- GCC_except_table11614
- GCC_except_table11620
- GCC_except_table11624
- GCC_except_table11837
- GCC_except_table12161
- GCC_except_table12295
- GCC_except_table12298
- GCC_except_table12300
- GCC_except_table2199
- GCC_except_table2322
- GCC_except_table2335
- GCC_except_table2348
- GCC_except_table2355
- GCC_except_table2359
- GCC_except_table2365
- GCC_except_table2412
- GCC_except_table2414
- GCC_except_table2416
- GCC_except_table2434
- GCC_except_table2440
- GCC_except_table2483
- GCC_except_table2495
- GCC_except_table2644
- GCC_except_table2732
- GCC_except_table2786
- GCC_except_table3023
- GCC_except_table3026
- GCC_except_table3027
- GCC_except_table3224
- GCC_except_table3283
- GCC_except_table3498
- GCC_except_table3501
- GCC_except_table3513
- GCC_except_table3514
- GCC_except_table3527
- GCC_except_table3528
- GCC_except_table3529
- GCC_except_table3535
- GCC_except_table3573
- GCC_except_table3579
- GCC_except_table3585
- GCC_except_table3653
- GCC_except_table3655
- GCC_except_table3690
- GCC_except_table3693
- GCC_except_table3804
- GCC_except_table3867
- GCC_except_table3869
- GCC_except_table3871
- GCC_except_table3873
- GCC_except_table3887
- GCC_except_table3893
- GCC_except_table4018
- GCC_except_table4022
- GCC_except_table4404
- GCC_except_table4419
- GCC_except_table4426
- GCC_except_table4442
- GCC_except_table4511
- GCC_except_table4550
- GCC_except_table4588
- GCC_except_table4589
- GCC_except_table4590
- GCC_except_table4615
- GCC_except_table4639
- GCC_except_table4999
- GCC_except_table5004
- GCC_except_table5007
- GCC_except_table5010
- GCC_except_table5058
- GCC_except_table5204
- GCC_except_table5207
- GCC_except_table5268
- GCC_except_table5276
- GCC_except_table5281
- GCC_except_table5294
- GCC_except_table5638
- GCC_except_table5651
- GCC_except_table5655
- GCC_except_table5667
- GCC_except_table5671
- GCC_except_table5784
- GCC_except_table5786
- GCC_except_table5864
- GCC_except_table5908
- GCC_except_table6275
- GCC_except_table6288
- GCC_except_table6290
- GCC_except_table6292
- GCC_except_table6344
- GCC_except_table6346
- GCC_except_table6352
- GCC_except_table6357
- GCC_except_table6361
- GCC_except_table6367
- GCC_except_table6376
- GCC_except_table6400
- GCC_except_table6403
- GCC_except_table6417
- GCC_except_table6419
- GCC_except_table6421
- GCC_except_table6423
- GCC_except_table6425
- GCC_except_table6427
- GCC_except_table6429
- GCC_except_table6476
- GCC_except_table6502
- GCC_except_table6559
- GCC_except_table6615
- GCC_except_table7022
- GCC_except_table7170
- GCC_except_table7315
- GCC_except_table7553
- GCC_except_table7562
- GCC_except_table7580
- GCC_except_table7955
- GCC_except_table7959
- GCC_except_table8004
- GCC_except_table8010
- GCC_except_table8035
- GCC_except_table8041
- GCC_except_table8263
- GCC_except_table8372
- GCC_except_table8383
- GCC_except_table8416
- GCC_except_table8419
- GCC_except_table8496
- GCC_except_table8500
- GCC_except_table8510
- GCC_except_table8521
- GCC_except_table8534
- GCC_except_table8619
- GCC_except_table8621
- GCC_except_table8645
- GCC_except_table8768
- GCC_except_table8831
- GCC_except_table8834
- GCC_except_table8838
- GCC_except_table8855
- GCC_except_table8869
- GCC_except_table8945
- GCC_except_table9003
- GCC_except_table9029
- GCC_except_table9056
- GCC_except_table9310
- GCC_except_table9456
- GCC_except_table9470
- GCC_except_table9515
- GCC_except_table9611
- GCC_except_table9715
- GCC_except_table9815
- _AFIsIPad.isIPad
- _AFLocaleIdentifierSupportsSAE.once
- _AFLocaleIdentifierSupportsSAE.supportedGlobalLocalesWave2
- _AFLocaleIdentifierSupportsSAE.supportedLocales
- ___54-[AFSpeechConnectionRequestContext initWithRequestId:]_block_invoke
- ___65+[AFFeatureFlags(SWEFeatureFlags) isSiriUODAvailableForLanguage:]_block_invoke
- ___AFLocaleIdentifierSupportsSAE_block_invoke
- ___block_descriptor_40_e8_32s_e52_v16?0"<AFSpeechConnectionRequestContextMutating>"8ls32l8
- _isSiriUODAvailableForLanguage:.bottomLocales
- _isSiriUODAvailableForLanguage:.once
- _isSiriUODAvailableForLanguage:.top13Locales
CStrings:
+ "%@ {requestId = %@, inputOrigin = %@}"
+ "%s #SiriAvailability fetching Siri availability for setup with the companion's: %{public}@"
+ "%s 24-hour time: %d (speaker %@, owner %@)"
+ "-[AFSUPFunctionProvider _currentTime:]"
+ "-[AFSettingsConnection fetchCompanionSiriAvailabilityForSetup:completion:]"
+ "-[AFSettingsConnection fetchCompanionSiriAvailabilityForSetup:completion:]_block_invoke_2"
+ "/System/Library/PrivateFrameworks/AttentionAwareness.framework/AttentionAwareness"
+ "AFSpeechConnectionRequestContext::inputOrigin"
+ "AWAttentionAwarenessConfiguration"
+ "AttentionAwarenessLibrary"
+ "Foundation"
+ "NSLocaleLanguageSupport2"
+ "No connection to assistantd"
+ "Recognized Speaker Twenty Four Hour Time Display"
+ "classAWAttentionAwarenessConfiguration"
+ "enablePebbleRecognitionWithVoiceProfile"
+ "hi-Latn"
+ "homepod_pause_music_on_request"
+ "initAWAttentionAwarenessConfiguration_block_invoke"
+ "v24@?0@\"AFSiriAvailability\"8@\"NSError\"16"
- "%@ {requestId = %@}"
```
