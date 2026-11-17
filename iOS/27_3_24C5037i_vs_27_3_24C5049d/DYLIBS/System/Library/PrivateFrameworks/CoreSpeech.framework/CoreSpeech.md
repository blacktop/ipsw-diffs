## CoreSpeech

> `/System/Library/PrivateFrameworks/CoreSpeech.framework/CoreSpeech`

```diff

-3610.11.1.0.0
-  __TEXT.__text: 0x148954
+3610.19.5.0.0
+  __TEXT.__text: 0x149e98
   __TEXT.__lazy_helpers: 0xa8
-  __TEXT.__objc_methlist: 0x150ec
+  __TEXT.__objc_methlist: 0x1522c
   __TEXT.__const: 0x45c
   __TEXT.__dlopen_cstrs: 0x197
-  __TEXT.__gcc_except_tab: 0x32f0
-  __TEXT.__cstring: 0x28faa
-  __TEXT.__oslogstring: 0x20a17
-  __TEXT.__unwind_info: 0x6310
+  __TEXT.__gcc_except_tab: 0x32fc
+  __TEXT.__cstring: 0x29107
+  __TEXT.__oslogstring: 0x20cf6
+  __TEXT.__unwind_info: 0x6368
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x4348
+  __DATA_CONST.__const: 0x4460
   __DATA_CONST.__objc_classlist: 0x868
   __DATA_CONST.__objc_catlist: 0x40
-  __DATA_CONST.__objc_protolist: 0x4e8
+  __DATA_CONST.__objc_protolist: 0x4f8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0xaf80
+  __DATA_CONST.__objc_selrefs: 0xb030
   __DATA_CONST.__objc_protorefs: 0x98
   __DATA_CONST.__objc_superrefs: 0x6a0
   __DATA_CONST.__objc_arraydata: 0x3f0
   __DATA_CONST.__got: 0x1b60
-  __AUTH_CONST.__const: 0x1ea0
-  __AUTH_CONST.__cfstring: 0x9680
-  __AUTH_CONST.__objc_const: 0x21630
+  __AUTH_CONST.__const: 0x1e80
+  __AUTH_CONST.__cfstring: 0x96a0
+  __AUTH_CONST.__objc_const: 0x217a8
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__lazy_load_got: 0x10
   __AUTH_CONST.__objc_intobj: 0x9c0

   __AUTH_CONST.__objc_arrayobj: 0x120
   __AUTH_CONST.__auth_got: 0xdb8
   __AUTH.__objc_data: 0x3ca0
-  __DATA.__objc_ivar: 0x19c8
-  __DATA.__data: 0x3a74
+  __DATA.__objc_ivar: 0x19e0
+  __DATA.__data: 0x3b34
   __DATA.__common: 0x10
   __DATA_DIRTY.__objc_data: 0x1770
   __DATA_DIRTY.__data: 0xc0

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 8206
-  Symbols:   14275
-  CStrings:  5626
+  Functions: 8236
+  Symbols:   14324
+  CStrings:  5643
 
Symbols:
+ +[CSAudioInjectionServices invalidateConnection:]
+ -[CSBuiltInVoiceTrigger _finishEnrollmentGateWithTriggerInfo:errorCode:]
+ -[CSBuiltInVoiceTrigger _handleEnrollmentGateSecondPassResult:]
+ -[CSBuiltInVoiceTrigger _setExclaveAsset:fallbackLocale:completion:]
+ -[CSBuiltInVoiceTrigger _shouldRunVoiceTrigger]
+ -[CSBuiltInVoiceTrigger awaitEnrollmentVoiceTriggerWithCompletion:]
+ -[CSBuiltInVoiceTrigger beginEnrollmentForLocale:]
+ -[CSBuiltInVoiceTrigger cancelEnrollmentVoiceTriggerWait]
+ -[CSBuiltInVoiceTrigger endEnrollment]
+ -[CSBuiltInVoiceTrigger enrollmentGateCompletion]
+ -[CSBuiltInVoiceTrigger enrollmentGateStartedAPVoiceTrigger]
+ -[CSBuiltInVoiceTrigger enrollmentLocale]
+ -[CSBuiltInVoiceTrigger isEnrollmentGateActive]
+ -[CSBuiltInVoiceTrigger setEnrollmentGateCompletion:]
+ -[CSBuiltInVoiceTrigger setEnrollmentGateStartedAPVoiceTrigger:]
+ -[CSBuiltInVoiceTrigger setEnrollmentLocale:]
+ -[CSBuiltInVoiceTrigger setIsEnrollmentGateActive:]
+ -[CSEndpointerXPCClient cachedEventTypeByRequestId]
+ -[CSEndpointerXPCClient cachedMetricsByRequestId]
+ -[CSEndpointerXPCClient setCachedEventTypeByRequestId:]
+ -[CSEndpointerXPCClient setCachedMetricsByRequestId:]
+ -[CSOnDeviceCachedIrPurgingHandler _cleanUpSecondPassCheckerCachedIrs]
+ -[CSSpeechManager builtInVoiceTrigger]
+ -[CSVoiceTriggerSecondPassRequestOption setSuppressSiriActivation:]
+ -[CSVoiceTriggerSecondPassRequestOption suppressSiriActivation]
+ GCC_except_table2496
+ GCC_except_table2529
+ GCC_except_table2640
+ GCC_except_table2699
+ GCC_except_table2711
+ GCC_except_table2742
+ GCC_except_table2767
+ GCC_except_table2778
+ GCC_except_table2816
+ GCC_except_table2820
+ GCC_except_table2823
+ GCC_except_table2827
+ GCC_except_table2831
+ GCC_except_table2840
+ GCC_except_table2846
+ GCC_except_table2849
+ GCC_except_table2919
+ GCC_except_table3189
+ GCC_except_table3268
+ GCC_except_table3307
+ GCC_except_table3321
+ GCC_except_table3343
+ GCC_except_table3346
+ GCC_except_table3349
+ GCC_except_table3382
+ GCC_except_table3442
+ GCC_except_table3616
+ GCC_except_table3642
+ GCC_except_table3670
+ GCC_except_table3706
+ GCC_except_table3708
+ GCC_except_table3710
+ GCC_except_table3726
+ GCC_except_table3728
+ GCC_except_table3730
+ GCC_except_table3732
+ GCC_except_table3734
+ GCC_except_table3736
+ GCC_except_table3738
+ GCC_except_table3741
+ GCC_except_table3749
+ GCC_except_table3752
+ GCC_except_table3758
+ GCC_except_table3760
+ GCC_except_table3762
+ GCC_except_table3764
+ GCC_except_table3766
+ GCC_except_table3771
+ GCC_except_table3775
+ GCC_except_table3782
+ GCC_except_table3785
+ GCC_except_table3788
+ GCC_except_table3796
+ GCC_except_table3804
+ GCC_except_table3945
+ GCC_except_table3969
+ GCC_except_table4035
+ GCC_except_table4051
+ GCC_except_table4072
+ GCC_except_table4164
+ GCC_except_table4416
+ GCC_except_table4488
+ GCC_except_table4492
+ GCC_except_table4495
+ GCC_except_table4499
+ GCC_except_table4524
+ GCC_except_table4527
+ GCC_except_table4580
+ GCC_except_table4586
+ GCC_except_table4860
+ GCC_except_table4867
+ GCC_except_table4874
+ GCC_except_table4880
+ GCC_except_table4963
+ GCC_except_table5126
+ GCC_except_table5136
+ GCC_except_table5160
+ GCC_except_table5180
+ GCC_except_table5263
+ GCC_except_table5277
+ GCC_except_table5286
+ GCC_except_table5293
+ GCC_except_table5299
+ GCC_except_table5301
+ GCC_except_table5304
+ GCC_except_table5312
+ GCC_except_table5314
+ GCC_except_table5318
+ GCC_except_table5320
+ GCC_except_table5332
+ GCC_except_table5337
+ GCC_except_table5344
+ GCC_except_table5349
+ GCC_except_table5351
+ GCC_except_table5353
+ GCC_except_table5358
+ GCC_except_table5364
+ GCC_except_table5368
+ GCC_except_table5370
+ GCC_except_table5385
+ GCC_except_table5416
+ GCC_except_table5473
+ GCC_except_table5477
+ GCC_except_table5531
+ GCC_except_table5561
+ GCC_except_table5564
+ GCC_except_table5656
+ GCC_except_table5670
+ GCC_except_table5677
+ GCC_except_table5689
+ GCC_except_table5693
+ GCC_except_table5703
+ GCC_except_table5942
+ GCC_except_table5988
+ GCC_except_table5993
+ GCC_except_table6033
+ GCC_except_table6042
+ GCC_except_table6072
+ GCC_except_table6146
+ GCC_except_table6288
+ GCC_except_table6393
+ GCC_except_table6401
+ GCC_except_table6421
+ GCC_except_table6426
+ GCC_except_table6532
+ GCC_except_table6587
+ GCC_except_table6667
+ GCC_except_table6689
+ GCC_except_table6690
+ GCC_except_table6700
+ GCC_except_table6701
+ GCC_except_table6713
+ GCC_except_table6744
+ GCC_except_table6755
+ GCC_except_table6760
+ GCC_except_table6765
+ GCC_except_table6793
+ GCC_except_table6865
+ GCC_except_table6877
+ GCC_except_table6900
+ GCC_except_table6914
+ GCC_except_table6937
+ GCC_except_table6949
+ GCC_except_table6996
+ GCC_except_table7246
+ GCC_except_table7282
+ GCC_except_table7355
+ GCC_except_table7409
+ GCC_except_table7432
+ GCC_except_table7468
+ GCC_except_table7487
+ GCC_except_table7498
+ GCC_except_table7643
+ GCC_except_table7651
+ GCC_except_table7767
+ GCC_except_table7768
+ GCC_except_table7769
+ GCC_except_table7770
+ GCC_except_table7771
+ GCC_except_table7776
+ GCC_except_table7839
+ GCC_except_table7885
+ GCC_except_table7893
+ GCC_except_table7899
+ GCC_except_table7927
+ GCC_except_table7933
+ GCC_except_table7939
+ GCC_except_table8078
+ _OBJC_IVAR_$_CSBuiltInVoiceTrigger._enrollmentGateCompletion
+ _OBJC_IVAR_$_CSBuiltInVoiceTrigger._enrollmentGateStartedAPVoiceTrigger
+ _OBJC_IVAR_$_CSBuiltInVoiceTrigger._enrollmentLocale
+ _OBJC_IVAR_$_CSBuiltInVoiceTrigger._isEnrollmentGateActive
+ _OBJC_IVAR_$_CSEndpointerXPCClient._cachedEventTypeByRequestId
+ _OBJC_IVAR_$_CSEndpointerXPCClient._cachedMetricsByRequestId
+ _OBJC_IVAR_$_CSVoiceTriggerSecondPassRequestOption._suppressSiriActivation
+ _OBJC_IVAR_$_CSVoiceTriggerStatistics._vtStatsBiomeSource
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSBuiltInVoiceTriggering
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSVoiceTriggerManagerProviding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSBuiltInVoiceTriggering
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSVoiceTriggerManagerProviding
+ __OBJC_$_PROTOCOL_REFS_CSBuiltInVoiceTriggering
+ __OBJC_$_PROTOCOL_REFS_CSVoiceTriggerManagerProviding
+ __OBJC_LABEL_PROTOCOL_$_CSBuiltInVoiceTriggering
+ __OBJC_LABEL_PROTOCOL_$_CSVoiceTriggerManagerProviding
+ __OBJC_PROTOCOL_$_CSBuiltInVoiceTriggering
+ __OBJC_PROTOCOL_$_CSVoiceTriggerManagerProviding
+ ___38-[CSBuiltInVoiceTrigger endEnrollment]_block_invoke
+ ___50-[CSBuiltInVoiceTrigger beginEnrollmentForLocale:]_block_invoke
+ ___57-[CSBuiltInVoiceTrigger cancelEnrollmentVoiceTriggerWait]_block_invoke
+ ___63-[CSBuiltInVoiceTrigger _handleEnrollmentGateSecondPassResult:]_block_invoke
+ ___67-[CSBuiltInVoiceTrigger awaitEnrollmentVoiceTriggerWithCompletion:]_block_invoke
+ ___68-[CSBuiltInVoiceTrigger _setExclaveAsset:fallbackLocale:completion:]_block_invoke
+ ___70-[CSOnDeviceCachedIrPurgingHandler _cleanUpSecondPassCheckerCachedIrs]_block_invoke
+ ___block_descriptor_41_e8_32s_e8_v16?0Q8ls32l8
+ ___block_descriptor_48_e8_32bs_e5_v8?0ls32l8
+ ___block_descriptor_48_e8_32s40bs_e8_v16?0Q8ls40l8s32l8
+ ___block_descriptor_48_e8_32s40s_e8_v12?0B8ls32l8s40l8
+ ___block_descriptor_56_e8_32s40bs_e18_v16?0"NSString"8ls32l8s40l8
+ ___block_descriptor_56_e8_32s40bs_e23_v28?0B8"NSError"12Q20ls32l8s40l8
+ ___block_descriptor_56_e8_32s40bs_e26_v36?0B8"NSError"12Q20Q28ls32l8s40l8
+ ___block_descriptor_73_e8_32s40s48s56w_e58_v24?0"CSVoiceTriggerSecondPassResultHolder"8"NSError"16ls32l8w56l8s40l8s48l8
- -[CSEndpointerXPCClient cachedEventType]
- -[CSEndpointerXPCClient cachedMetrics]
- -[CSEndpointerXPCClient setCachedEventType:]
- -[CSEndpointerXPCClient setCachedMetrics:]
- -[CSOnDeviceCachedIrPurgingHandler _cleanUpOnDeviceCompilationPath]
- GCC_except_table2495
- GCC_except_table2528
- GCC_except_table2639
- GCC_except_table2698
- GCC_except_table2710
- GCC_except_table2741
- GCC_except_table2766
- GCC_except_table2777
- GCC_except_table2811
- GCC_except_table2819
- GCC_except_table2822
- GCC_except_table2825
- GCC_except_table2829
- GCC_except_table2839
- GCC_except_table2845
- GCC_except_table2847
- GCC_except_table2918
- GCC_except_table3188
- GCC_except_table3267
- GCC_except_table3306
- GCC_except_table3320
- GCC_except_table3342
- GCC_except_table3345
- GCC_except_table3348
- GCC_except_table3381
- GCC_except_table3441
- GCC_except_table3615
- GCC_except_table3641
- GCC_except_table3669
- GCC_except_table3704
- GCC_except_table3707
- GCC_except_table3709
- GCC_except_table3725
- GCC_except_table3727
- GCC_except_table3729
- GCC_except_table3731
- GCC_except_table3733
- GCC_except_table3735
- GCC_except_table3737
- GCC_except_table3740
- GCC_except_table3748
- GCC_except_table3751
- GCC_except_table3757
- GCC_except_table3759
- GCC_except_table3761
- GCC_except_table3763
- GCC_except_table3765
- GCC_except_table3767
- GCC_except_table3772
- GCC_except_table3777
- GCC_except_table3783
- GCC_except_table3786
- GCC_except_table3795
- GCC_except_table3800
- GCC_except_table3944
- GCC_except_table3968
- GCC_except_table4034
- GCC_except_table4050
- GCC_except_table4071
- GCC_except_table4163
- GCC_except_table4415
- GCC_except_table4486
- GCC_except_table4491
- GCC_except_table4494
- GCC_except_table4498
- GCC_except_table4523
- GCC_except_table4526
- GCC_except_table4579
- GCC_except_table4585
- GCC_except_table4859
- GCC_except_table4866
- GCC_except_table4873
- GCC_except_table4879
- GCC_except_table4962
- GCC_except_table5125
- GCC_except_table5135
- GCC_except_table5159
- GCC_except_table5179
- GCC_except_table5262
- GCC_except_table5276
- GCC_except_table5285
- GCC_except_table5292
- GCC_except_table5298
- GCC_except_table5300
- GCC_except_table5303
- GCC_except_table5311
- GCC_except_table5313
- GCC_except_table5317
- GCC_except_table5319
- GCC_except_table5330
- GCC_except_table5336
- GCC_except_table5343
- GCC_except_table5348
- GCC_except_table5350
- GCC_except_table5352
- GCC_except_table5354
- GCC_except_table5359
- GCC_except_table5365
- GCC_except_table5369
- GCC_except_table5384
- GCC_except_table5415
- GCC_except_table5472
- GCC_except_table5476
- GCC_except_table5530
- GCC_except_table5560
- GCC_except_table5563
- GCC_except_table5653
- GCC_except_table5667
- GCC_except_table5674
- GCC_except_table5686
- GCC_except_table5690
- GCC_except_table5700
- GCC_except_table5931
- GCC_except_table5964
- GCC_except_table5969
- GCC_except_table6007
- GCC_except_table6016
- GCC_except_table6046
- GCC_except_table6120
- GCC_except_table6262
- GCC_except_table6367
- GCC_except_table6375
- GCC_except_table6395
- GCC_except_table6400
- GCC_except_table6506
- GCC_except_table6561
- GCC_except_table6641
- GCC_except_table6663
- GCC_except_table6664
- GCC_except_table6674
- GCC_except_table6675
- GCC_except_table6687
- GCC_except_table6718
- GCC_except_table6729
- GCC_except_table6734
- GCC_except_table6739
- GCC_except_table6767
- GCC_except_table6839
- GCC_except_table6851
- GCC_except_table6874
- GCC_except_table6885
- GCC_except_table6888
- GCC_except_table6923
- GCC_except_table6970
- GCC_except_table7220
- GCC_except_table7256
- GCC_except_table7329
- GCC_except_table7383
- GCC_except_table7406
- GCC_except_table7442
- GCC_except_table7461
- GCC_except_table7472
- GCC_except_table7617
- GCC_except_table7625
- GCC_except_table7741
- GCC_except_table7742
- GCC_except_table7743
- GCC_except_table7744
- GCC_except_table7745
- GCC_except_table7750
- GCC_except_table7813
- GCC_except_table7859
- GCC_except_table7867
- GCC_except_table7873
- GCC_except_table7898
- GCC_except_table7904
- GCC_except_table7910
- GCC_except_table8048
- _OBJC_IVAR_$_CSEndpointerXPCClient._cachedEventType
- _OBJC_IVAR_$_CSEndpointerXPCClient._cachedMetrics
- ___67-[CSOnDeviceCachedIrPurgingHandler _cleanUpOnDeviceCompilationPath]_block_invoke
- ___block_descriptor_72_e8_32s40s48s56w_e58_v24?0"CSVoiceTriggerSecondPassResultHolder"8"NSError"16ls32l8w56l8s40l8s48l8
CStrings:
+ "%s Audio injection enabled, skip creating CSAggressiveECModeHandler"
+ "%s CSVoiceTriggerSecondPass[%{public}@]:Siri activation suppressed, skip prewarm"
+ "%s Cannot wait for enrollment voice trigger : %{public}@"
+ "%s Disable PHS since the enrollment gate only needs a Hey Siri detection"
+ "%s Enrollment ended, restoring the exclave asset"
+ "%s Enrollment for locale %{public}@"
+ "%s Enrollment gate finished with error code %lu"
+ "%s Enrollment gate got second pass result %d"
+ "%s Fingerprint frame skip rate : %lu"
+ "%s Setting the exclave asset for enrollment locale %{public}@ failed, restoring the regular asset"
+ "%s VoiceTrigger is already listening, reuse it for the enrollment gate"
+ "%s VoiceTrigger is disabled, clean up second pass checker cached irs"
+ "%s VoiceTrigger is disabled, keep cached irs on HomePod"
+ "%s Waiting for enrollment voice trigger"
+ "%s skip purging cached irs for endpoint asset"
+ "-[CSAggressiveECModeHandler init]"
+ "-[CSBuiltInVoiceTrigger _finishEnrollmentGateWithTriggerInfo:errorCode:]"
+ "-[CSBuiltInVoiceTrigger _handleEnrollmentGateSecondPassResult:]"
+ "-[CSBuiltInVoiceTrigger _setExclaveAsset:fallbackLocale:completion:]_block_invoke"
+ "-[CSBuiltInVoiceTrigger awaitEnrollmentVoiceTriggerWithCompletion:]_block_invoke"
+ "-[CSBuiltInVoiceTrigger beginEnrollmentForLocale:]_block_invoke"
+ "-[CSBuiltInVoiceTrigger endEnrollment]_block_invoke"
- "%s Created OSDAnalyzer: %{public}@"
- "%s VoiceTrigger is disabled, clean up cached ir path"
- "%s purging for specific device is not handled here"
- "-[CSOnDeviceCachedIrPurgingHandler _purgeCachedIrFilesWithAsset:]"
- "CSOnDeviceCachedIrPurgingHandler"
```
