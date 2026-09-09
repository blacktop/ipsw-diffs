## PersonalizedSensingService

> `/System/Library/PrivateFrameworks/PersonalizedSensing.framework/XPCServices/PersonalizedSensingService.xpc/PersonalizedSensingService`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

 417.0.0.0.0
-  __TEXT.__text: 0x129098
+  __TEXT.__text: 0x1289d4
   __TEXT.__auth_stubs: 0x1c30
-  __TEXT.__objc_stubs: 0xb000
+  __TEXT.__objc_stubs: 0xafc0
   __TEXT.__objc_methlist: 0x68d0
   __TEXT.__objc_classname: 0x1335
   __TEXT.__objc_methtype: 0xf3b
-  __TEXT.__cstring: 0xed60
-  __TEXT.__objc_methname: 0x12c6a
+  __TEXT.__cstring: 0xea60
+  __TEXT.__objc_methname: 0x12c5a
   __TEXT.__const: 0x404e
   __TEXT.__gcc_except_tab: 0xd14
   __TEXT.__oslogstring: 0xafbd

   __TEXT.__swift_as_cont: 0x23c
   __TEXT.__swift5_mpenum: 0x30
   __TEXT.__swift5_protos: 0x18
-  __TEXT.__unwind_info: 0x3220
+  __TEXT.__unwind_info: 0x3210
   __TEXT.__eh_frame: 0x36f8
   __DATA_CONST.__const: 0x9439
-  __DATA_CONST.__cfstring: 0xe840
+  __DATA_CONST.__cfstring: 0xe660
   __DATA_CONST.__objc_classlist: 0x450
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x70

   __DATA_CONST.__objc_floatobj: 0x1c0
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__auth_got: 0xe30
-  __DATA_CONST.__got: 0xab8
+  __DATA_CONST.__got: 0xab0
   __DATA_CONST.__auth_ptr: 0x498
   __DATA.__objc_const: 0xe020
-  __DATA.__objc_selrefs: 0x3ab8
+  __DATA.__objc_selrefs: 0x3aa8
   __DATA.__objc_ivar: 0x8b0
   __DATA.__objc_data: 0x35b8
   __DATA.__data: 0x2f90

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 5327
-  Symbols:   14051
-  CStrings:  5916
+  Symbols:   14048
+  CStrings:  5918
 
Symbols:
+ -[MOEventBundleRankingInput peopleCountMaxNormalized]
+ -[MOEventBundleRankingInput peopleCountWeightedAverageNormalized]
+ -[MOEventBundleRankingInput peopleCountWeightedSumNormalized]
+ -[MOEventBundleRankingInput setPeopleCountMaxNormalized:]
+ -[MOEventBundleRankingInput setPeopleCountWeightedAverageNormalized:]
+ -[MOEventBundleRankingInput setPeopleCountWeightedSumNormalized:]
+ OBJC_IVAR_$_MOEventBundleRankingInput._peopleCountMaxNormalized
+ OBJC_IVAR_$_MOEventBundleRankingInput._peopleCountWeightedAverageNormalized
+ OBJC_IVAR_$_MOEventBundleRankingInput._peopleCountWeightedSumNormalized
+ _objc_msgSend$peopleCountMaxNormalized
+ _objc_msgSend$peopleCountWeightedAverageNormalized
+ _objc_msgSend$peopleCountWeightedSumNormalized
+ _objc_msgSend$setPeopleCountMaxNormalized:
+ _objc_msgSend$setPeopleCountWeightedAverageNormalized:
+ _objc_msgSend$setPeopleCountWeightedSumNormalized:
- -[MOEventBundleRankingInput pCountMaxNormalized]
- -[MOEventBundleRankingInput pCountWeightedAverageNormalized]
- -[MOEventBundleRankingInput pCountWeightedSumNormalized]
- -[MOEventBundleRankingInput setPCountMaxNormalized:]
- -[MOEventBundleRankingInput setPCountWeightedAverageNormalized:]
- -[MOEventBundleRankingInput setPCountWeightedSumNormalized:]
- OBJC_IVAR_$_MOEventBundleRankingInput._pCountMaxNormalized
- OBJC_IVAR_$_MOEventBundleRankingInput._pCountWeightedAverageNormalized
- OBJC_IVAR_$_MOEventBundleRankingInput._pCountWeightedSumNormalized
- _OBJC_CLASS_$_NSAssertionHandler
- _objc_msgSend$currentHandler
- _objc_msgSend$handleFailureInMethod:object:file:lineNumber:description:
- _objc_msgSend$pCountMaxNormalized
- _objc_msgSend$pCountWeightedAverageNormalized
- _objc_msgSend$pCountWeightedSumNormalized
- _objc_msgSend$setPCountMaxNormalized:
- _objc_msgSend$setPCountWeightedAverageNormalized:
- _objc_msgSend$setPCountWeightedSumNormalized:
Functions:
~ -[MODefaultsManager objectForKey:] : 332 -> 248
~ -[MODefaultsManager objectForKeyWithoutLog:] : 260 -> 164
~ -[MODefaultsManager deleteObjectForKey:] : 312 -> 236
~ -[MODefaultsManager setObject:forKey:] : 348 -> 264
~ -[MODefaultsManager setObjectWithoutLog:forKey:] : 216 -> 100
~ -[MOEventBundleLabelFormat initWithFormat:capitalizationType:] : 268 -> 200
~ +[MODictionaryEncoder encodeDictionary:] : 408 -> 320
~ +[MODictionaryEncoder decodeToDictionary:] : 408 -> 320
~ -[MOResource initWithIdentifier:] : 248 -> 172
~ ___98-[MOTemplateBasedContextBuilder _generateContextStringsFromTemplateWithBundleContent:withHandler:]_block_invoke : 1876 -> 1872
~ +[MOPlatformInfo isSeedBuild] : 8 -> 112
~ -[MOEventBundleLabelTemplate initWithConditionStrings:labels:context:] : 336 -> 276
~ -[MOEventBundleLabelTemplate initWithConditions:labels:context:] : 520 -> 460
~ -[MOEventBundleLabelTemplate initWithConditions:formats:context:] : 324 -> 264
~ +[MOEventBundleLabelLocalizer _Moments_LocalizedStringForKey:withTable:] : 668 -> 604
~ +[MOEventBundleLabelLocalizer _Moments_LocalizedStringWithFormat:arguments:] : 952 -> 884
~ -[MOTime initWithIdentifier:] : 288 -> 204
~ -[MOPlace initWithIdentifier:] : 268 -> 192
~ -[MOEventBundleRanking initWithUniverse:] : 232 -> 164
~ -[MOEventBundleRanking initWithConfigurationManager:] : 16740 -> 16680
~ -[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:] : 31016 -> 30952
~ -[MOEventBundleRanking _mergeScoresToBundles:usingScore:] : 1776 -> 1664
~ -[MOEventBundleRanking _submitEventBundleRankingAnalytics:withRankingInput:andSubmissionDate:] : 8980 -> 8852
~ -[MOEventBundleRanking updateTripMetaDataForRank:] : 1200 -> 1036
~ -[MOStringArrayTransformer transformedValue:] : 380 -> 284
~ -[MOStringArrayTransformer reverseTransformedValue:] : 352 -> 256
~ _$ss17_NativeDictionaryV4copyyyFSS_SiTg5 : 352 -> 356
~ _$ss17_NativeDictionaryV4copyyyFSS_yXlTg5 : 360 -> 364
~ _$ss17_NativeDictionaryV4copyyyFSS_So8NSObjectCTg5Tm : 340 -> 344
~ _$ss17_NativeDictionaryV4copyyyFSS_SaySo14NSSecureCoding_pGTg5Tm : 344 -> 348
~ _$ss17_NativeDictionaryV4copyyyFSS_s5Error_pTg5 : 360 -> 364
~ _$ss17_NativeDictionaryV4copyyyFSS_26PersonalizedSensingService12StreamResultVTg5 : 384 -> 388
~ _$s26PersonalizedSensingService11BaseDonatorC12getDonations5count8bookmarkSDySSSaySo14NSSecureCoding_pGG_SDySSyXlGtSi_AJtYaKFyScGys6ResultOyAI_AJts5Error_pGGzYaXEfU_TY2_ : 2372 -> 2380
~ _$s26PersonalizedSensingService11BaseDonatorC15encodeDonations_8encodingSDySSSayAA8EncodingOGGSDySSSaySo14NSSecureCoding_pGG_AGtYaKFyScGyAA0E0_p_s6ResultOyAIs5Error_pGtGzYaXEfU_TY2_ : 1704 -> 1708
~ _$sSTsE21_copySequenceContents12initializing8IteratorQz_SitSry7ElementQzG_tFSDySSSiG_Tg5 : 340 -> 344
~ _$s26PersonalizedSensingService15PSSContextEventC21getSourceAppBundleIDs4fromSaySSGSo07MOEventI0C_tFZTf4nd_n : 2460 -> 2468
~ _$s26PersonalizedSensingService22PSSContextSignificanceC4from6bundleACSgSo13MOEventBundleC_tFZSSSgyXEfU_ : 428 -> 432
~ _$sSr15_stableSortImpl2byySbx_xtKXE_tKFySryxGz_SiztKXEfU_26PersonalizedSensingService18SignificanceReasonO_Tg504$s26ef19Service22PSSContexth51C4from7bundlesACSgSaySo13MOEventBundleCG_tFZSbAA0E6I11O_AKtXEfU2_Tf1nnncn_n : 4780 -> 4772
~ _$s26PersonalizedSensingService22PSSContextSignificanceC26getAbbreviatedActivityName33_B085BF70867D4F83BF674E190BA79095LL4fromSSSgSDySSypG_tFZTf4nd_n : 400 -> 404
~ _$s26PersonalizedSensingService22PSSContextSignificanceC03getE7Reasons33_B085BF70867D4F83BF674E190BA79095LLySayAA0E6ReasonOGSo13MOEventBundleCFZTf4nd_n : 6816 -> 6840
~ _$sSD8grouping2bySDyxSay7ElementQyd__GGqd__n_xADqd_0_YKXEtqd_0_YKcAERs_STRd__s5ErrorRd_0_r0_lufCSS_Say26PersonalizedSensingService15PSSContextEventCGs5NeverOTt2g504$s26ef42Service16AnalyticsDonatorC26processAndEmiti109Metrics9donations10donationID0L4TimeAA0iJ6ResultVSDySSSaySo14NSSecureCoding_pGG_SS10Foundation4DateVtFSSAA010H8I0CXEfU_Tf1nc_nTf4g_n : 716 -> 724
~ _$s26PersonalizedSensingService13CommonMetricsV10measurable9payloadID5index12donationTime23additionalCheckedFields0l6FilledN021includeActionPresence0pK15ContextsInDepthAcA20PSSContextMeasurable_p_SSSi10Foundation4DateVS2iS2btcfCTf4ennnnnnnn_nAA0V5EventC_Tt7g5 : 6556 -> 6692
~ _$sSD8grouping2bySDyxSay7ElementQyd__GGqd__n_xADqd_0_YKXEtqd_0_YKcAERs_STRd__s5ErrorRd_0_r0_lufCSS_Say26PersonalizedSensingService17PSSContextPatternCGs5NeverOTt2g504$s26ef42Service16AnalyticsDonatorC28processAndEmiti109Metrics9donations10donationID0L4TimeAA0iJ6ResultVSDySSSaySo14NSSecureCoding_pGG_SS10Foundation4DateVtFSSAA010H8I0CXEfU_Tf1nc_nTf4g_n : 716 -> 724
~ _$ss17_NativeDictionaryV6filteryAByxq_GSbx3key_q_5valuet_tqd__YKXEqd__YKs5ErrorRd__lFADs13_UnsafeBitsetVqd__YKXEfU_SS_Sis5NeverOTg5 : 388 -> 392
~ _$sSr15_stableSortImpl2byySbx_xtKXE_tKFySryxGz_SiztKXEfU_SS3key_Si5valuet_Tg5202$s26PersonalizedSensingService37PSSPatternSummaryDescriptionGeneratorC19generateWorkoutList33_90C55FE0D0ABE292AC72F5C2D5163D74LL4fromSSSgAA21BehavioralPatternDataC_tFSbSS3key_Si5valuet_SSAJ_SiAKttXEfU0_Tf1nnncn_n : 1024 -> 1028
~ _$s26PersonalizedSensingService37PSSPatternSummaryDescriptionGeneratorC34generateAdditionalContextSentences33_90C55FE0D0ABE292AC72F5C2D5163D74LL12activityType14behavioralData7patternSaySSGSS_AA017BehavioralPatternX0CAA17PSSContextPatternCtFTf4nndd_n : 936 -> 872
~ _$s26PersonalizedSensingService16AnalyticsDonatorC31aggregatePatternCategoryMetricsyAA0ghI0VSayAFGFTf4nd_n : 1996 -> 1948
~ _$s26PersonalizedSensingService16AnalyticsDonatorC29aggregateEventCategoryMetricsyAA0ghI0VSayAFGFTf4nd_n : 1776 -> 1780
~ _$s26PersonalizedSensingService14PSSContextTimeC14bundleMetadata33_1406910C490B88AC7F464CC37DBF63BCLL4fromSSSg7holiday_SbSg10isBirthdayAG17birthdayContactIdAG0s6PhotosU0tSo13MOEventBundleC_tFZTf4nd_n : 880 -> 884
~ _$s26PersonalizedSensingService17PSSContextPatternC4toCCSo14CCItemInstanceCySo0H7Content_So0H7MessageCXcSo0h4MetaJ0_AIXcGyKF : 4736 -> 4792
~ _$s26PersonalizedSensingService21BehavioralPatternDataC9isWeekendSbSgvg : 240 -> 244
~ _$s26PersonalizedSensingService21BehavioralPatternDataC20topLevelActivityTypeSSSgvgTm : 180 -> 184
~ _$s26PersonalizedSensingService21BehavioralPatternDataC12isWithFamilySbSgvgTm : 176 -> 180
~ _$s26PersonalizedSensingService15PSSContextMediaC06createE033_1AC081EF1B5B200D67D27EF0FD5FC0B2LL4fromACSgSo10MOResourceC_tFZTf4nd_n : 1732 -> 1752
~ _$sSr15_stableSortImpl2byySbx_xtKXE_tKFySryxGz_SiztKXEfU_26PersonalizedSensingService15PSSContextMediaC_Tg504$s26ef35Service19PSSMediaDescriptionC15sorti52ByTime33_E7D61B8A316BB5D3CEC3102CAEE4BFC9LLySayAA010H20G0CGAHFSbAG_AGtXEfU_Tf1nnncn_n : 4300 -> 4292
~ _$s26PersonalizedSensingService21CleanTransformDonatorC15_mergeEncodings33_987ECA0F93BA7D78874779F5E7FEC084LL_4withSDySSSayAA8EncodingOGGAJ_AJtKF : 868 -> 872
~ _$sSr15_stableSortImpl2byySbx_xtKXE_tKFySryxGz_SiztKXEfU_26PersonalizedSensingService15PSSContextPlaceC_Tg504$s26ef103Service30PSSActivityLocationDescriptionC16sortPlacesByTime33_2CFC9B44FA2E8EBC6D25BA770A66A05FLLySayAA15hI18CGAHFSbAG_AGtXEfU_Tf1nnncn_n : 4300 -> 4292
CStrings:
+ "PlatformInfoOverrideIsSeedBuild"
+ "Tf,N,V_peopleCountMaxNormalized"
+ "Tf,N,V_peopleCountWeightedAverageNormalized"
+ "Tf,N,V_peopleCountWeightedSumNormalized"
+ "_peopleCountMaxNormalized"
+ "_peopleCountWeightedAverageNormalized"
+ "_peopleCountWeightedSumNormalized"
+ "peopleCountMaxNormalized"
+ "peopleCountWeightedAverageNormalized"
+ "peopleCountWeightedSumNormalized"
+ "setPeopleCountMaxNormalized:"
+ "setPeopleCountWeightedAverageNormalized:"
+ "setPeopleCountWeightedSumNormalized:"
- "Tf,N,V_pCountMaxNormalized"
- "Tf,N,V_pCountWeightedAverageNormalized"
- "Tf,N,V_pCountWeightedSumNormalized"
- "_pCountMaxNormalized"
- "_pCountWeightedAverageNormalized"
- "_pCountWeightedSumNormalized"
- "currentHandler"
- "handleFailureInMethod:object:file:lineNumber:description:"
- "setPCountMaxNormalized:"
- "setPCountWeightedAverageNormalized:"
- "setPCountWeightedSumNormalized:"
```
