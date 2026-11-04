## MediaPlaybackCore

> `/System/Library/PrivateFrameworks/MediaPlaybackCore.framework/MediaPlaybackCore`

```diff

-26210.26.40.301.0
-  __TEXT.__text: 0x48e1b8
-  __TEXT.__objc_methlist: 0x17f60
+26300.26.43.301.0
+  __TEXT.__text: 0x4a527c
+  __TEXT.__objc_methlist: 0x180b0
   __TEXT.__dlopen_cstrs: 0x114
-  __TEXT.__const: 0x10a80
-  __TEXT.__oslogstring: 0x4d157
-  __TEXT.__cstring: 0x26063
-  __TEXT.__swift5_typeref: 0x54d0
-  __TEXT.__swift5_capture: 0xb1bc
-  __TEXT.__constg_swiftt: 0x7bdc
-  __TEXT.__swift5_reflstr: 0x5b02
-  __TEXT.__swift5_fieldmd: 0x5718
-  __TEXT.__swift5_builtin: 0x6f4
+  __TEXT.__const: 0x11200
+  __TEXT.__oslogstring: 0x4e408
+  __TEXT.__cstring: 0x263a6
+  __TEXT.__swift5_typeref: 0x5702
+  __TEXT.__swift5_capture: 0xb29c
+  __TEXT.__constg_swiftt: 0x7ea4
+  __TEXT.__swift5_reflstr: 0x5d12
+  __TEXT.__swift5_fieldmd: 0x59c4
+  __TEXT.__swift5_builtin: 0x708
   __TEXT.__swift5_mpenum: 0x130
-  __TEXT.__swift5_assocty: 0xbc0
-  __TEXT.__swift5_proto: 0x934
-  __TEXT.__swift5_types: 0x568
-  __TEXT.__swift_as_entry: 0x4b8
-  __TEXT.__swift_as_ret: 0x5e0
-  __TEXT.__swift_as_cont: 0xe54
-  __TEXT.__swift5_protos: 0xd8
+  __TEXT.__swift5_assocty: 0xc08
+  __TEXT.__swift5_proto: 0x970
+  __TEXT.__swift5_types: 0x58c
+  __TEXT.__swift_as_entry: 0x4f8
+  __TEXT.__swift_as_ret: 0x620
+  __TEXT.__swift_as_cont: 0xf10
+  __TEXT.__swift5_protos: 0xe8
   __TEXT.__swift5_types2: 0x4
-  __TEXT.__gcc_except_tab: 0x5a6c
+  __TEXT.__gcc_except_tab: 0x5ab4
   __TEXT.__ustring: 0x4dc
-  __TEXT.__unwind_info: 0x10cd0
-  __TEXT.__eh_frame: 0x10648
+  __TEXT.__unwind_info: 0x11350
+  __TEXT.__eh_frame: 0x11500
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x9498
-  __DATA_CONST.__objc_classlist: 0xd30
+  __DATA_CONST.__const: 0x95e0
+  __DATA_CONST.__objc_classlist: 0xd48
   __DATA_CONST.__objc_catlist: 0x298
   __DATA_CONST.__objc_protolist: 0x7f0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xcc18
+  __DATA_CONST.__objc_selrefs: 0xccf0
   __DATA_CONST.__objc_protorefs: 0x3a0
   __DATA_CONST.__objc_superrefs: 0x6d8
   __DATA_CONST.__objc_arraydata: 0x288
-  __DATA_CONST.__got: 0x34a0
-  __AUTH_CONST.__const: 0x24018
-  __AUTH_CONST.__cfstring: 0x1ede0
-  __AUTH_CONST.__objc_const: 0x349d0
-  __AUTH_CONST.__objc_intobj: 0x8a0
-  __AUTH_CONST.__objc_arrayobj: 0x270
+  __DATA_CONST.__got: 0x3510
+  __AUTH_CONST.__const: 0x24430
+  __AUTH_CONST.__cfstring: 0x1f060
+  __AUTH_CONST.__objc_const: 0x35168
+  __AUTH_CONST.__objc_intobj: 0x8b8
+  __AUTH_CONST.__objc_arrayobj: 0x258
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__objc_doubleobj: 0x60
-  __AUTH_CONST.__auth_got: 0x34a0
-  __AUTH.__objc_data: 0x5a40
-  __AUTH.__data: 0x40f0
-  __DATA.__objc_ivar: 0x1adc
-  __DATA.__data: 0x7310
-  __DATA.__common: 0x238
-  __DATA_DIRTY.__objc_data: 0x3598
-  __DATA_DIRTY.__data: 0x45d8
+  __AUTH_CONST.__auth_got: 0x3570
+  __AUTH.__objc_data: 0x5b98
+  __AUTH.__data: 0x4360
+  __DATA.__objc_ivar: 0x1b00
+  __DATA.__data: 0x7580
+  __DATA.__common: 0x280
+  __DATA_DIRTY.__objc_data: 0x35d8
+  __DATA_DIRTY.__data: 0x45c8
   __DATA_DIRTY.__bss: 0x1328
   __DATA_DIRTY.__common: 0xc8
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 24730
-  Symbols:   18718
-  CStrings:  8299
+  Functions: 25224
+  Symbols:   18855
+  CStrings:  8386
 
Symbols:
+ +[MPCPlaybackPerformanceController supportsAssetConnectionPrewarming]
+ -[MPCModelGenericAVItem _computeNormalizedGainFromPlayerItem:reason:]
+ -[MPCModelGenericAVItem cachedTimebase]
+ -[MPCModelGenericAVItem normalizedGain]
+ -[MPCModelGenericAVItem setCachedTimebase:]
+ -[MPCModelGenericAVItem setNormalizedGain:]
+ -[MPCPlayPerfMetrics set_tokenMintWaitTime:]
+ -[MPCPlayPerfMetrics tokenMintWaitTime]
+ -[MPCPlaybackAccountManager _defaultMediaUserChangedNotification:]
+ -[MPCPlaybackEngine assetTokenManager]
+ -[MPCPlaybackEngine audioTapDelegate]
+ -[MPCPlaybackEngine setAudioTapDelegate:]
+ -[MPCPlaybackPerformanceController prewarmFrequentHLSConnections]
+ -[MPCPlaybackPerformanceController recordHLSAssetURL:options:]
+ -[MPCPlayerItemConfigurator assetTokenManager]
+ -[MPCReportingLyricsViewEvent isSelfieSingShare]
+ -[MPCReportingLyricsViewEvent setSelfieSingShare:]
+ -[MPCSingleTrackAudioProcessor currentContentItemID]
+ -[MPCSingleTrackAudioProcessor setCurrentContentItemID:]
+ GCC_except_table1000
+ GCC_except_table1004
+ GCC_except_table1007
+ GCC_except_table1010
+ GCC_except_table1203
+ GCC_except_table1205
+ GCC_except_table1375
+ GCC_except_table1377
+ GCC_except_table1424
+ GCC_except_table1435
+ GCC_except_table1442
+ GCC_except_table1449
+ GCC_except_table1486
+ GCC_except_table1507
+ GCC_except_table1550
+ GCC_except_table1723
+ GCC_except_table1725
+ GCC_except_table1738
+ GCC_except_table1743
+ GCC_except_table1813
+ GCC_except_table1899
+ GCC_except_table1900
+ GCC_except_table2011
+ GCC_except_table2031
+ GCC_except_table2033
+ GCC_except_table2070
+ GCC_except_table2075
+ GCC_except_table2077
+ GCC_except_table2080
+ GCC_except_table2091
+ GCC_except_table2101
+ GCC_except_table2216
+ GCC_except_table2267
+ GCC_except_table2271
+ GCC_except_table2274
+ GCC_except_table2300
+ GCC_except_table2324
+ GCC_except_table2356
+ GCC_except_table2436
+ GCC_except_table2623
+ GCC_except_table2651
+ GCC_except_table2678
+ GCC_except_table2823
+ GCC_except_table2844
+ GCC_except_table2851
+ GCC_except_table2852
+ GCC_except_table2877
+ GCC_except_table2884
+ GCC_except_table2890
+ GCC_except_table2892
+ GCC_except_table2894
+ GCC_except_table2897
+ GCC_except_table2932
+ GCC_except_table2937
+ GCC_except_table2943
+ GCC_except_table2949
+ GCC_except_table2954
+ GCC_except_table2957
+ GCC_except_table2960
+ GCC_except_table2980
+ GCC_except_table2988
+ GCC_except_table3031
+ GCC_except_table3121
+ GCC_except_table3125
+ GCC_except_table3136
+ GCC_except_table3137
+ GCC_except_table3161
+ GCC_except_table3169
+ GCC_except_table3211
+ GCC_except_table3212
+ GCC_except_table3228
+ GCC_except_table3285
+ GCC_except_table3302
+ GCC_except_table3303
+ GCC_except_table3313
+ GCC_except_table3355
+ GCC_except_table3357
+ GCC_except_table3375
+ GCC_except_table3379
+ GCC_except_table3423
+ GCC_except_table3468
+ GCC_except_table3473
+ GCC_except_table3605
+ GCC_except_table3626
+ GCC_except_table3633
+ GCC_except_table3658
+ GCC_except_table3662
+ GCC_except_table3672
+ GCC_except_table3729
+ GCC_except_table3734
+ GCC_except_table3738
+ GCC_except_table3808
+ GCC_except_table3909
+ GCC_except_table3920
+ GCC_except_table3942
+ GCC_except_table3951
+ GCC_except_table4079
+ GCC_except_table4124
+ GCC_except_table4125
+ GCC_except_table4126
+ GCC_except_table4145
+ GCC_except_table4154
+ GCC_except_table4173
+ GCC_except_table4180
+ GCC_except_table4194
+ GCC_except_table4217
+ GCC_except_table4228
+ GCC_except_table4317
+ GCC_except_table4336
+ GCC_except_table4349
+ GCC_except_table4360
+ GCC_except_table4391
+ GCC_except_table4562
+ GCC_except_table4563
+ GCC_except_table4741
+ GCC_except_table4776
+ GCC_except_table4786
+ GCC_except_table4794
+ GCC_except_table4817
+ GCC_except_table4825
+ GCC_except_table4835
+ GCC_except_table4850
+ GCC_except_table4894
+ GCC_except_table4924
+ GCC_except_table4927
+ GCC_except_table4933
+ GCC_except_table4985
+ GCC_except_table5023
+ GCC_except_table5111
+ GCC_except_table513
+ GCC_except_table5212
+ GCC_except_table530
+ GCC_except_table5457
+ GCC_except_table5458
+ GCC_except_table547
+ GCC_except_table5537
+ GCC_except_table5630
+ GCC_except_table5782
+ GCC_except_table5807
+ GCC_except_table5924
+ GCC_except_table6005
+ GCC_except_table6013
+ GCC_except_table6014
+ GCC_except_table6078
+ GCC_except_table6103
+ GCC_except_table6138
+ GCC_except_table6141
+ GCC_except_table6144
+ GCC_except_table6230
+ GCC_except_table6447
+ GCC_except_table6464
+ GCC_except_table6512
+ GCC_except_table6525
+ GCC_except_table7041
+ GCC_except_table7375
+ GCC_except_table7390
+ GCC_except_table7484
+ GCC_except_table7493
+ GCC_except_table7582
+ GCC_except_table7589
+ GCC_except_table7607
+ GCC_except_table7658
+ GCC_except_table7659
+ GCC_except_table7662
+ GCC_except_table7667
+ GCC_except_table7683
+ GCC_except_table798
+ GCC_except_table854
+ GCC_except_table934
+ GCC_except_table968
+ GCC_except_table975
+ GCC_except_table977
+ GCC_except_table990
+ GCC_except_table994
+ _AVPlayerInterstitialEventMonitorCurrentEventDidChangeNotification
+ _AVPlayerInterstitialEventMonitorEventsDidChangeNotification
+ _AudioFormatGetProperty
+ _ICUserProfileStoreDefaultMediaUserDidChangeNotification
+ _MPCPlaybackEngineEventAssetTokenSourceCached
+ _MPCPlaybackEngineEventAssetTokenSourceMinted
+ _MPCPlaybackEngineEventAssetTokenSourceResumeRefresh
+ _MPCPlaybackEngineEventAssetTokenSourceScheduledRefresh
+ _MPCPlaybackEngineEventAssetTokenSourceSeekRefresh
+ _MPCPlaybackEngineEventItemMetadataKeyRequiresAssetToken
+ _MPCPlaybackEngineEventPayloadKeyAssetTokenDurationSeconds
+ _MPCPlaybackEngineEventPayloadKeyAssetTokenError
+ _MPCPlaybackEngineEventPayloadKeyAssetTokenExpiration
+ _MPCPlaybackEngineEventPayloadKeyAssetTokenRefreshAttempt
+ _MPCPlaybackEngineEventPayloadKeyAssetTokenSource
+ _MPCPlaybackEngineEventPayloadKeyAssetTokenTTLSeconds
+ _MPCPlaybackEngineEventPayloadKeyInterstitialDuration
+ _MPCPlaybackEngineEventTypeAssetTokenAcquired
+ _MPModelPropertySongVisualTraits
+ _MPNowPlayingContentItemUserInfoKeyPodcastEpisodeRequiresAssetToken
+ _OBJC_CLASS_$_AVPlayerInterstitialEventController
+ _OBJC_CLASS_$_MPCAssetTokenManager
+ _OBJC_IVAR_$_MPCModelGenericAVItem._cachedTimebase
+ _OBJC_IVAR_$_MPCModelGenericAVItem._normalizedGain
+ _OBJC_IVAR_$_MPCPlaybackEngine._assetTokenManager
+ _OBJC_IVAR_$_MPCPlaybackEngine._audioTapDelegate
+ _OBJC_IVAR_$_MPCPlaybackPerformanceController._hlsHostCounts
+ _OBJC_IVAR_$_MPCPlaybackPerformanceController._hlsPrewarmOptions
+ _OBJC_IVAR_$_MPCPlaybackPerformanceController._hlsTotalPlays
+ _OBJC_IVAR_$_MPCPlaybackPerformanceController._lastHLSConnectionActivity
+ _OBJC_IVAR_$_MPCReportingLyricsViewEvent._selfieSingShare
+ _OBJC_IVAR_$_MPCSingleTrackAudioProcessor._currentContentItemID
+ _OBJC_METACLASS_$_MPCAssetTokenManager
+ _OUTLINED_FUNCTION_498
+ _OUTLINED_FUNCTION_499
+ _OUTLINED_FUNCTION_622
+ _OUTLINED_FUNCTION_623
+ _OUTLINED_FUNCTION_624
+ _OUTLINED_FUNCTION_625
+ _OUTLINED_FUNCTION_626
+ _OUTLINED_FUNCTION_627
+ _OUTLINED_FUNCTION_628
+ _OUTLINED_FUNCTION_629
+ _OUTLINED_FUNCTION_630
+ _OUTLINED_FUNCTION_631
+ _OUTLINED_FUNCTION_632
+ _OUTLINED_FUNCTION_633
+ _OUTLINED_FUNCTION_634
+ _OUTLINED_FUNCTION_635
+ _OUTLINED_FUNCTION_636
+ _OUTLINED_FUNCTION_637
+ _OUTLINED_FUNCTION_638
+ _OUTLINED_FUNCTION_639
+ _OUTLINED_FUNCTION_640
+ _OUTLINED_FUNCTION_641
+ _OUTLINED_FUNCTION_642
+ _OUTLINED_FUNCTION_643
+ _OUTLINED_FUNCTION_644
+ _OUTLINED_FUNCTION_645
+ _OUTLINED_FUNCTION_646
+ __DATA_MPCAssetTokenManager
+ __DATA__TtC17MediaPlaybackCore17AssetTokenSession
+ __DATA__TtC17MediaPlaybackCore32InterstitialRestrictionOverrider
+ __IVARS_MPCAssetTokenManager
+ __IVARS__TtC17MediaPlaybackCore17AssetTokenSession
+ __IVARS__TtC17MediaPlaybackCore32InterstitialRestrictionOverrider
+ __METACLASS_DATA_MPCAssetTokenManager
+ __METACLASS_DATA__TtC17MediaPlaybackCore17AssetTokenSession
+ __METACLASS_DATA__TtC17MediaPlaybackCore32InterstitialRestrictionOverrider
+ __MPCFreeAudioBufferList
+ __OBJC_$_CLASS_METHODS_MPCAssetTokenManager(MediaPlaybackCore|MediaPlaybackCore1)
+ __OBJC_$_INSTANCE_METHODS_MPCAssetTokenManager(MediaPlaybackCore|MediaPlaybackCore1)
+ __OBJC_CLASS_PROTOCOLS_$_MPCAssetTokenManager(MediaPlaybackCore|MediaPlaybackCore1)
+ ___64-[MPCPlayPerfMetrics addAssetSelectionWithCursor:itemIDPayload:]_block_invoke_2
+ ___65-[MPCPlaybackPerformanceController prewarmFrequentHLSConnections]_block_invoke
+ ___65-[MPCPlaybackPerformanceController prewarmFrequentHLSConnections]_block_invoke_2
+ ____MPCAudioTapProcess_block_invoke
+ ___block_descriptor_32_e31_q24?0"NSNumber"8"NSNumber"16l
+ ___block_descriptor_48_e8_32bs40w_e8_v16?0q8lw40l8s32l8
+ ___block_descriptor_48_e8_32s_e18_B16?0"NSString"8ls32l8
+ ___block_descriptor_88_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ ___swift_closure_destructor.107Tm
+ ___swift_closure_destructor.113Tm
+ ___swift_closure_destructor.226Tm
+ ___swift_closure_destructor.28Tm
+ ___swift_closure_destructor.499Tm
+ ___swift_closure_destructor.608Tm
+ ___swift_closure_destructor.97Tm
+ ___swift_memcpy41_8
+ ___unnamed_11
+ _associated conformance 17MediaPlaybackCore17AssetTokenManagerC18InvalidationReasonOSHAASQ
+ _associated conformance SC31MPCAssistantXSchemeURLErrorCodeLeV10Foundation13CustomNSErrorSCs5Error
+ _associated conformance SC31MPCAssistantXSchemeURLErrorCodeLeV10Foundation21_BridgedStoredNSErrorSC0D0AcDP_8RawValueSYs17FixedWidthInteger
+ _associated conformance SC31MPCAssistantXSchemeURLErrorCodeLeV10Foundation21_BridgedStoredNSErrorSC0D0AcDP_AC06_ErrorD8Protocol
+ _associated conformance SC31MPCAssistantXSchemeURLErrorCodeLeV10Foundation21_BridgedStoredNSErrorSC0D0AcDP_SY
+ _associated conformance SC31MPCAssistantXSchemeURLErrorCodeLeV10Foundation21_BridgedStoredNSErrorSCAC06CustomH0
+ _associated conformance SC31MPCAssistantXSchemeURLErrorCodeLeV10Foundation21_BridgedStoredNSErrorSCAC26_ObjectiveCBridgeableError
+ _associated conformance SC31MPCAssistantXSchemeURLErrorCodeLeV10Foundation21_BridgedStoredNSErrorSCSH
+ _associated conformance SC31MPCAssistantXSchemeURLErrorCodeLeV10Foundation26_ObjectiveCBridgeableErrorSCs0H0
+ _associated conformance SC31MPCAssistantXSchemeURLErrorCodeLeVSHSCSQ
+ _associated conformance So31MPCAssistantXSchemeURLErrorCodeV10Foundation06_ErrorD8ProtocolSC01_F4TypeAcDP_AC21_BridgedStoredNSError
+ _associated conformance So31MPCAssistantXSchemeURLErrorCodeV10Foundation06_ErrorD8ProtocolSCSQ
+ _bzero
+ _get_enum_tag_for_layout_string 17MediaPlaybackCore17PodcastsPlayEvent33_9E2A88F7161E17A7C0D0C9ACE6FC197BLLV14AssetPlacementO
+ _objc_getProperty
+ _objc_setProperty_atomic_copy
+ _symbolic $s17MediaPlaybackCore15AssetTokenClockP
+ _symbolic $s17MediaPlaybackCore20AssetTokenRequestingP
+ _symbolic $s17MediaPlaybackCore21AssetTokenManagerHostP
+ _symbolic $s17MediaPlaybackCore25AssetTokenSessionReporterP
+ _symbolic SDySS_____G 17MediaPlaybackCore17AssetTokenSessionC
+ _symbolic SDy__________G 18PodcastsFoundation17AssetTokenRequestV 17MediaPlaybackCore06CachedD0V
+ _symbolic SSSg2id_SdSg13startPositionAC8durationt
+ _symbolic ScTy___________pGSg 18PodcastsFoundation10AssetTokenV s5ErrorP
+ _symbolic So35AVPlayerInterstitialEventControllerC
+ _symbolic _____ 17MediaPlaybackCore11CachedTokenV
+ _symbolic _____ 17MediaPlaybackCore11SystemClockV
+ _symbolic _____ 17MediaPlaybackCore17AssetTokenManagerC
+ _symbolic _____ 17MediaPlaybackCore17AssetTokenManagerC18InvalidationReasonO
+ _symbolic _____ 17MediaPlaybackCore17AssetTokenSessionC
+ _symbolic _____ 17MediaPlaybackCore17PodcastsPlayEvent33_9E2A88F7161E17A7C0D0C9ACE6FC197BLLV14AssetPlacementO
+ _symbolic _____ 17MediaPlaybackCore32InterstitialRestrictionOverriderC
+ _symbolic _____ 18PodcastsFoundation10AssetTokenV
+ _symbolic _____ 18PodcastsFoundation17AssetTokenRequestV
+ _symbolic _____ 18PodcastsFoundation23AssetTokenRefreshPolicyV
+ _symbolic _____ SC31MPCAssistantXSchemeURLErrorCodeLeV
+ _symbolic _____ So31MPCAssistantXSchemeURLErrorCodeV
+ _symbolic _____Sg 17MediaPlaybackCore32InterstitialRestrictionOverriderC
+ _symbolic _____Sg 18PodcastsFoundation10AssetTokenV
+ _symbolic _____SgXw 17MediaPlaybackCore17AssetTokenManagerC
+ _symbolic _____SgXw 17MediaPlaybackCore17AssetTokenSessionC
+ _symbolic _____SgXw 17MediaPlaybackCore32InterstitialRestrictionOverriderC
+ _symbolic _____SgXwz_Xx 17MediaPlaybackCore17AssetTokenManagerC
+ _symbolic _____SgXwz_Xx 17MediaPlaybackCore17AssetTokenSessionC
+ _symbolic ______p 17MediaPlaybackCore15AssetTokenClockP
+ _symbolic ______p 18PodcastsFoundation18AssetTokenProviderP
+ _symbolic ______pSgXw 17MediaPlaybackCore21AssetTokenManagerHostP
+ _symbolic ______pSgXw 17MediaPlaybackCore25AssetTokenSessionReporterP
+ _type_layout_string 17MediaPlaybackCore17PodcastsPlayEvent33_9E2A88F7161E17A7C0D0C9ACE6FC197BLLV14AssetPlacementO
+ _type_layout_string SC31MPCAssistantXSchemeURLErrorCodeLeV
- -[MPCPlaybackPerformanceController lastCDNWarming]
- -[MPCPlaybackPerformanceController loadAVAssetWithURL:]
- -[MPCPlaybackPerformanceController markCDNConnectionWarmed]
- -[MPCPlaybackPerformanceController setLastCDNWarming:]
- -[MPCPlaybackPerformanceController warmCDNConnection]
- GCC_except_table1002
- GCC_except_table1005
- GCC_except_table1192
- GCC_except_table1196
- GCC_except_table1366
- GCC_except_table1368
- GCC_except_table1415
- GCC_except_table1426
- GCC_except_table1433
- GCC_except_table1440
- GCC_except_table1477
- GCC_except_table1489
- GCC_except_table1541
- GCC_except_table1714
- GCC_except_table1716
- GCC_except_table1729
- GCC_except_table1734
- GCC_except_table1804
- GCC_except_table1890
- GCC_except_table1891
- GCC_except_table2002
- GCC_except_table2022
- GCC_except_table2024
- GCC_except_table2052
- GCC_except_table2066
- GCC_except_table2068
- GCC_except_table2071
- GCC_except_table2082
- GCC_except_table2092
- GCC_except_table2207
- GCC_except_table2258
- GCC_except_table2262
- GCC_except_table2265
- GCC_except_table2291
- GCC_except_table2315
- GCC_except_table2347
- GCC_except_table2427
- GCC_except_table2614
- GCC_except_table2642
- GCC_except_table2669
- GCC_except_table2814
- GCC_except_table2835
- GCC_except_table2842
- GCC_except_table2843
- GCC_except_table2868
- GCC_except_table2870
- GCC_except_table2875
- GCC_except_table2881
- GCC_except_table2883
- GCC_except_table2885
- GCC_except_table2914
- GCC_except_table2928
- GCC_except_table2930
- GCC_except_table2934
- GCC_except_table2940
- GCC_except_table2945
- GCC_except_table2951
- GCC_except_table2971
- GCC_except_table2979
- GCC_except_table3022
- GCC_except_table3108
- GCC_except_table3112
- GCC_except_table3123
- GCC_except_table3124
- GCC_except_table3148
- GCC_except_table3156
- GCC_except_table3197
- GCC_except_table3198
- GCC_except_table3214
- GCC_except_table3271
- GCC_except_table3289
- GCC_except_table3298
- GCC_except_table3340
- GCC_except_table3342
- GCC_except_table3349
- GCC_except_table3360
- GCC_except_table3408
- GCC_except_table3453
- GCC_except_table3458
- GCC_except_table3590
- GCC_except_table3611
- GCC_except_table3618
- GCC_except_table3643
- GCC_except_table3647
- GCC_except_table3657
- GCC_except_table3714
- GCC_except_table3719
- GCC_except_table3723
- GCC_except_table3793
- GCC_except_table3890
- GCC_except_table3894
- GCC_except_table3921
- GCC_except_table3927
- GCC_except_table4064
- GCC_except_table4109
- GCC_except_table4110
- GCC_except_table4111
- GCC_except_table4130
- GCC_except_table4139
- GCC_except_table4157
- GCC_except_table4162
- GCC_except_table4164
- GCC_except_table4201
- GCC_except_table4212
- GCC_except_table4301
- GCC_except_table4320
- GCC_except_table4333
- GCC_except_table4344
- GCC_except_table4375
- GCC_except_table4546
- GCC_except_table4547
- GCC_except_table4725
- GCC_except_table4760
- GCC_except_table4762
- GCC_except_table4770
- GCC_except_table4793
- GCC_except_table4801
- GCC_except_table4819
- GCC_except_table4834
- GCC_except_table4878
- GCC_except_table4892
- GCC_except_table4911
- GCC_except_table4917
- GCC_except_table4969
- GCC_except_table5007
- GCC_except_table5095
- GCC_except_table512
- GCC_except_table5196
- GCC_except_table528
- GCC_except_table5439
- GCC_except_table5440
- GCC_except_table545
- GCC_except_table5516
- GCC_except_table5608
- GCC_except_table5760
- GCC_except_table5785
- GCC_except_table5902
- GCC_except_table5983
- GCC_except_table5991
- GCC_except_table5992
- GCC_except_table6056
- GCC_except_table6081
- GCC_except_table6116
- GCC_except_table6119
- GCC_except_table6122
- GCC_except_table6208
- GCC_except_table6425
- GCC_except_table6442
- GCC_except_table6490
- GCC_except_table6503
- GCC_except_table7019
- GCC_except_table7353
- GCC_except_table7368
- GCC_except_table7462
- GCC_except_table7471
- GCC_except_table7560
- GCC_except_table7567
- GCC_except_table7585
- GCC_except_table7636
- GCC_except_table7637
- GCC_except_table7640
- GCC_except_table7645
- GCC_except_table7661
- GCC_except_table797
- GCC_except_table853
- GCC_except_table929
- GCC_except_table960
- GCC_except_table963
- GCC_except_table972
- GCC_except_table985
- GCC_except_table989
- GCC_except_table995
- GCC_except_table999
- _OBJC_IVAR_$_MPCPlaybackPerformanceController._lastCDNWarming
- _OUTLINED_FUNCTION_512
- _OUTLINED_FUNCTION_513
- ___55-[MPCPlaybackPerformanceController loadAVAssetWithURL:]_block_invoke
- ___swift_closure_destructor.106Tm
- ___swift_closure_destructor.112Tm
- ___swift_closure_destructor.225Tm
- ___swift_closure_destructor.22Tm
- ___swift_closure_destructor.498Tm
- ___swift_closure_destructor.607Tm
- ___swift_closure_destructor.96Tm
- ___unnamed_10
- _kMXSessionProperty_HostProcessAttribution
- _kMXSession_HostProcessAttributionKey_AuditToken
- _kMXSession_HostProcessAttributionKey_BundleID
- _symbolic So14MPMediaLibraryCIego_
- _symbolic ySSc
- _type_layout_string SC7AVErrorLeV
CStrings:
+ "Acquiring token, contentItemID=%{public}s"
+ "Active account changed, dropping %ld cached token(s)"
+ "Already paused, ignoring"
+ "Asset Token Refresh"
+ "Asset needs no FairPlay key session, using url: %{private}s"
+ "Asset token refresh"
+ "AssetConnectionPrewarming"
+ "AssetTokenRefresh"
+ "HTTP %ld on CAT-protected stream for episode=%{private,mask.hash}s. Clearing CAT state to retry with a fresh token."
+ "Invalidating manager, %ld session(s)"
+ "Invalidating session, hadTimer=%{bool,public}d hadToken=%{bool,public}d contentItemID=%{public}s"
+ "Invalidating session, reason=%{public}s contentItemID=%{public}s"
+ "Joining pending fetch, contentItemID=%{public}s"
+ "MPCAssetTokenManager"
+ "MPCPlaybackPerformanceHLSHostCounts"
+ "MPCPlaybackPerformanceHLSPrewarmOptions"
+ "MPCPlaybackPerformanceHLSTotalPlays"
+ "MediaPlaybackCore.AssetTokenManager"
+ "Mint failed offline for downloaded item=%{private,mask.hash}s error=%{public}s; falling back to the download."
+ "No AssetTokenManager set on item=%{private,mask.hash}s; cannot acquire token"
+ "Offline; playing the download for item=%{private,mask.hash}s"
+ "Pausing"
+ "Pausing session, cancelling timer, contentItemID=%{public}s"
+ "PodcastsAssetToken"
+ "Position jumped, contentItemID=%{public}s"
+ "Pre-fetch cancelled, contentItemID=%{public}s"
+ "Pre-fetch failed, contentItemID=%{public}s error=%{public}s"
+ "Pre-fetching token, contentItemID=%{public}s"
+ "Prefetch failed, contentItemID=%{public}s error=%{public}s"
+ "Prefetching token for next item, contentItemID=%{public}s"
+ "Rate changed, rate=%{public}f contentItemID=%{public}s"
+ "Refresh already in flight, coalescing, contentItemID=%{public}s"
+ "Refresh skipped, host gone, contentItemID=%{public}s"
+ "Refresh skipped, item mismatch: current=%{public}s session=%{public}s"
+ "Refresh skipped, no cached token, contentItemID=%{public}s"
+ "Refreshing on resume, contentItemID=%{public}s"
+ "Refreshing on seek, contentItemID=%{public}s"
+ "Resume ignored, no cached token, contentItemID=%{public}s"
+ "Resume ignored, no session, contentItemID=%{public}s"
+ "Resume ignored, not paused, contentItemID=%{public}s"
+ "Returning cached token, contentItemID=%{public}s"
+ "SEED"
+ "Scheduling refresh in %lds, contentItemID=%{public}s"
+ "Scheduling refresh timer on resume, contentItemID=%{public}s"
+ "Skipping prewarm; deferring asset load until activation."
+ "Skipping refresh, token outlives playback, contentItemID=%{public}s"
+ "Skipping teardown invalidate, item still current, contentItemID=%{public}s"
+ "TokenMint"
+ "[%{public}@]-[LeaseRatePreparation] - %{public}@: Not waiting for key renewals [downloaded asset]"
+ "[%{public}@]-[SelfieSing] - %{public}@ - normalizedGain changed from %f to %f. Update reason=%{public}@, track=%{public}@"
+ "[LeaseRatePreparation] - %{public}@: Stopped waiting for key renewals [timeout] reason=%ld"
+ "[PL:%{public}s] PLAYER CONTROLLER: An interstitial event could not be carried over, so the provider's schedule is left in place rather than unscheduling an ad break"
+ "[PL:%{public}s] PLAYER CONTROLLER: Dropped navigation restrictions from %{public}ld of %{public}ld interstitial events"
+ "[PL:%{public}s] PLAYER PROCESSING: InternalPlayerController - Lifted forwardBufferDuration cap on current item: %{public}@ [item became current while capped]"
+ "[PL:%{public}s] PLAYER PROCESSING: InternalPlayerController - Saving playback resume time: %{public}f [%{public}s]"
+ "[PL:%{public}s] PLAYER PROCESSING: InternalPlayerController - Seek to time completed [%{public}s] - target time:%{public}f - identifier: %{public}s"
+ "[PL:%{public}s] STACK PROCESSING: Reloading current item [%{public}s] - Asset loading is suspended %{public}s, nothing to reload"
+ "[PL:%{public}s] STACK PROCESSING: Reloading current item [%{public}s] - Lifting asset load prevention %{public}s"
+ "[Prewarm] Failed to prewarm HLS connection to %{public}@: %{public}@"
+ "[Prewarm] Prewarmed HLS connection to %{public}@"
+ "[Prewarm] Prewarming HLS connection to %{public}@"
+ "[SelfieSing] - %{public}@ - normalizedGain set to %.1f: AudioFormatGetProperty(ComputeLoudnessScalar) failed: %d. Update reason=%{public}@, track=%{public}@"
+ "[SelfieSing] - %{public}@ - normalizedGain set to %.1f: effectiveLoudnessInfo is nil. Update reason=%{public}@"
+ "[SelfieSing] - %{public}@ - queueItem.timebase is nil at configuration time for item: %{public}@"
+ "[SelfieSing] - audio tap callback skipped: contentItemID changed from %{public}@ to %{public}@"
+ "[SelfieSing] - audio tap callback skipped: currentItem is nil"
+ "[SelfieSing] - audio tap callback skipped: failed to copy audio buffer list"
+ "[XSQ:%{sonic:fourCC}u] fitContent(...) | pre-check []\nplaybackAccountID=%{public}s\ncanPlaySubscriptionContent=%{bool}d \ncanBorrowAndPlaySubscriptionContent=%{bool}d \nborrowableCatalogPlaybackAccountID=%{public}s\ncanRemoteSetQueue=%{bool}d \nintentDestination=%{public}s"
+ "[XSQ:%{sonic:fourCC}u] fitContent(...) | restored content [purchases not in library, borrowing subscription] \nborrowableCatalogPlaybackAccountID=%{public}s\ncontent=%{public}s\nitems=%{public}s"
+ "asset-token-acquired"
+ "asset-token-duration-seconds"
+ "asset-token-error"
+ "asset-token-expiration"
+ "asset-token-refresh-attempt"
+ "asset-token-source"
+ "asset-token-ttl-seconds"
+ "a\xf0\x91"
+ "forwarded to incoming item "
+ "https"
+ "interstitial-duration"
+ "itemIsReadyToPlay"
+ "minted"
+ "non-subscriber-default"
+ "playbackDidStart"
+ "playbackStartTimeOverride set on queue item "
+ "q24@?0@\"NSNumber\"8@\"NSNumber\"16"
+ "requires-asset-token"
+ "resume-refresh"
+ "scheduled-refresh"
+ "seek-refresh"
+ "selfie_sing"
+ "tokenMintWaitTime"
+ "tracksDidChange"
+ "|%{public}@ %{public}@ %2i %{public}@  │ requiresAssetToken: %{BOOL}u"
+ "|%{public}@ %{public}@ %2i %{public}@  ╰ duration: %0.2f"
+ "|%{public}@ %{public}@ %2i %{public}@  ╰ ttl: %.0fs; expires: %{public}@"
+ "|%{public}@ %{public}@ %2i %{public}@ ╲╭ source: %{public}@; attempt: %ld"
+ "\xf0\xf0\xf0\xc1"
- "Asset is STDQ, no fairplay needed, using url: %{private}s"
- "Completed warming asset CDN connection with asset: %{public}@"
- "MUSIC_PLAYBACK_PERFORMANCE_WARMING_CDN"
- "Warming asset CDN connection with URL: %@"
- "[PL:%{public}s] PLAYER PROCESSING: InternalPlayerController - Saving playback resume time: %{public}f [playbackStartTimeOverride set on queue item]"
- "[PL:%{public}s] PLAYER PROCESSING: InternalPlayerController - Seek to time completed [playbackStartTimeOverride set on queue item] - target time:%{public}f - queue item:%{public}s - identifier: %{public}s"
- "[XSQ:%{sonic:fourCC}u] fitContent(...) | pre-check [] \ncanPlaySubscriptionContent=%{bool}d \ncanRemoteSetQueue=%{bool}d \nintentDestination=%{public}s"
- "assetURL1"
- "assetURL2"
- "warmingInterval"
- "\xf0\xf0\xf0\xa1"
```
