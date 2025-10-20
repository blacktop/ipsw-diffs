## MobileSpotlightIndex

> `/System/Library/PrivateFrameworks/MobileSpotlightIndex.framework/MobileSpotlightIndex`

```diff

-2400.13.1.101.0
-  __TEXT.__text: 0x46ccac
-  __TEXT.__auth_stubs: 0x37f0
-  __TEXT.__objc_methlist: 0x950
+2400.14.100.0.0
+  __TEXT.__text: 0x464540
+  __TEXT.__auth_stubs: 0x3780
+  __TEXT.__objc_methlist: 0x7a8
   __TEXT.__const: 0x9dbb
-  __TEXT.__cstring: 0x273b7
+  __TEXT.__cstring: 0x2620f
   __TEXT.__gcc_except_tab: 0x40d8
-  __TEXT.__oslogstring: 0x215c8
+  __TEXT.__oslogstring: 0x20b38
   __TEXT.__dlopen_cstrs: 0x150
   __TEXT.__ustring: 0x116c
   __TEXT.__dof_mds: 0x29b
-  __TEXT.__unwind_info: 0x5d70
+  __TEXT.__unwind_info: 0x5c98
   __TEXT.__eh_frame: 0x220
   __TEXT.__objc_classname: 0xd4
-  __TEXT.__objc_methname: 0x208d
-  __TEXT.__objc_methtype: 0xebd
-  __TEXT.__objc_stubs: 0x1f80
-  __DATA_CONST.__got: 0x310
-  __DATA_CONST.__const: 0x9250
+  __TEXT.__objc_methname: 0x1ca9
+  __TEXT.__objc_methtype: 0xe2c
+  __TEXT.__objc_stubs: 0x18a0
+  __DATA_CONST.__got: 0x2f8
+  __DATA_CONST.__const: 0x8fd0
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x948
+  __DATA_CONST.__objc_selrefs: 0x800
   __DATA_CONST.__objc_superrefs: 0x60
   __DATA_CONST.__objc_arraydata: 0x250
-  __AUTH_CONST.__auth_got: 0x1c08
-  __AUTH_CONST.__const: 0x87d0
-  __AUTH_CONST.__cfstring: 0xcc20
-  __AUTH_CONST.__objc_const: 0x1100
-  __AUTH_CONST.__objc_intobj: 0xf0
+  __AUTH_CONST.__auth_got: 0x1bd0
+  __AUTH_CONST.__const: 0x8730
+  __AUTH_CONST.__cfstring: 0xba00
+  __AUTH_CONST.__objc_const: 0x10c0
+  __AUTH_CONST.__objc_intobj: 0x108
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_doubleobj: 0x1b0
   __AUTH.__objc_data: 0x410
   __AUTH.__data: 0x1628
-  __DATA.__objc_ivar: 0xd4
-  __DATA.__data: 0x10d0
-  __DATA.__bss: 0x111778
+  __DATA.__objc_ivar: 0xcc
+  __DATA.__data: 0x10c8
+  __DATA.__bss: 0x111768
   __DATA_DIRTY.__data: 0x3f8
   __DATA_DIRTY.__bss: 0x8b88
   __DATA_DIRTY.__common: 0x24004

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 87965CD8-8D17-3625-8444-E0E9B0673F49
-  Functions: 7384
-  Symbols:   20011
-  CStrings:  11142
+  UUID: 9CCA7374-3F31-3368-98C5-54D7D7186EEA
+  Functions: 7310
+  Symbols:   19769
+  CStrings:  10707
 
Symbols:
+ +[SIAnalytics setResourcesCallback:]
+ -[SIAnalytics droppedIndexDataWithError:]
+ -[SIAnalytics heartbeatAnalyticsDataWithReset:error:]
+ -[SIAnalytics incrementPerIndexHeartbeatCount:forKey:withError:]
+ -[SIAnalytics indexDropAnalyticsDataFromDroppedIndexData:withError:]
+ -[SIAnalytics indexDropType:]
+ -[SIAnalytics initWithParentDirectoryPath:corespotlight:heartbeatIndex:]
+ -[SIAnalytics refreshPerIndexHeartbeatFieldsForIndex:protectionClass:withError:]
+ -[SIAnalytics setPerIndexHeartbeatTimestamp:forKey:withError:]
+ -[SIAnalytics setSharedHeartbeatTimestamp:forKey:withError:]
+ -[SIAnalyticsIndexData heartbeatData]
+ -[SIAnalyticsIndexData incrementCount:forKey:]
+ -[SIAnalyticsIndexData initWithPrefix:data:]
+ -[SIAnalyticsIndexData setTimestamp:forKey:]
+ GCC_except_table1516
+ GCC_except_table1518
+ GCC_except_table1526
+ GCC_except_table1529
+ GCC_except_table1596
+ GCC_except_table1764
+ GCC_except_table1767
+ GCC_except_table1801
+ GCC_except_table2313
+ GCC_except_table2324
+ GCC_except_table2325
+ GCC_except_table2328
+ GCC_except_table2738
+ GCC_except_table3497
+ GCC_except_table3498
+ GCC_except_table3499
+ GCC_except_table3500
+ GCC_except_table3501
+ GCC_except_table3502
+ GCC_except_table3503
+ GCC_except_table3504
+ GCC_except_table3505
+ GCC_except_table3506
+ GCC_except_table3507
+ GCC_except_table3508
+ GCC_except_table3509
+ GCC_except_table3515
+ GCC_except_table3525
+ GCC_except_table3526
+ GCC_except_table3528
+ GCC_except_table3532
+ GCC_except_table3545
+ GCC_except_table3550
+ GCC_except_table3555
+ GCC_except_table3556
+ GCC_except_table3559
+ GCC_except_table3560
+ GCC_except_table3561
+ GCC_except_table3562
+ GCC_except_table3565
+ GCC_except_table3566
+ GCC_except_table3567
+ GCC_except_table5397
+ GCC_except_table5399
+ GCC_except_table5860
+ GCC_except_table5862
+ GCC_except_table5864
+ GCC_except_table5866
+ GCC_except_table5868
+ GCC_except_table5870
+ GCC_except_table5874
+ GCC_except_table5877
+ GCC_except_table5880
+ GCC_except_table5883
+ GCC_except_table5885
+ GCC_except_table5892
+ GCC_except_table5893
+ GCC_except_table5895
+ GCC_except_table5897
+ GCC_except_table5906
+ GCC_except_table5907
+ GCC_except_table5908
+ GCC_except_table5912
+ GCC_except_table5924
+ GCC_except_table5925
+ GCC_except_table5926
+ GCC_except_table5927
+ GCC_except_table5928
+ GCC_except_table5929
+ GCC_except_table5930
+ GCC_except_table5931
+ GCC_except_table5932
+ GCC_except_table5933
+ GCC_except_table5935
+ GCC_except_table5952
+ GCC_except_table5953
+ GCC_except_table5955
+ GCC_except_table5956
+ GCC_except_table5964
+ GCC_except_table5965
+ GCC_except_table5968
+ GCC_except_table5983
+ GCC_except_table5984
+ GCC_except_table5985
+ GCC_except_table5987
+ GCC_except_table5988
+ GCC_except_table6048
+ GCC_except_table6051
+ GCC_except_table6054
+ GCC_except_table6055
+ GCC_except_table6056
+ GCC_except_table6253
+ GCC_except_table6290
+ GCC_except_table6291
+ GCC_except_table6292
+ GCC_except_table6293
+ GCC_except_table6299
+ GCC_except_table6303
+ GCC_except_table6306
+ GCC_except_table6307
+ GCC_except_table6308
+ GCC_except_table6309
+ GCC_except_table6310
+ GCC_except_table6312
+ GCC_except_table6313
+ GCC_except_table6316
+ GCC_except_table6317
+ GCC_except_table6318
+ GCC_except_table6319
+ GCC_except_table6320
+ GCC_except_table6321
+ GCC_except_table6322
+ GCC_except_table6323
+ GCC_except_table6324
+ GCC_except_table6325
+ GCC_except_table6326
+ GCC_except_table6328
+ GCC_except_table6329
+ GCC_except_table6330
+ GCC_except_table6335
+ GCC_except_table6340
+ GCC_except_table6341
+ GCC_except_table6342
+ GCC_except_table6343
+ GCC_except_table6344
+ GCC_except_table6345
+ GCC_except_table6346
+ GCC_except_table6347
+ GCC_except_table6348
+ GCC_except_table6349
+ GCC_except_table6350
+ GCC_except_table6351
+ GCC_except_table6352
+ GCC_except_table6354
+ GCC_except_table6368
+ GCC_except_table6370
+ GCC_except_table6372
+ GCC_except_table6411
+ GCC_except_table6412
+ GCC_except_table6566
+ GCC_except_table7268
+ GCC_except_table7269
+ GCC_except_table7277
+ GCC_except_table7279
+ GCC_except_table7280
+ GCC_except_table7282
+ GCC_except_table7289
+ GCC_except_table7293
+ GCC_except_table7296
+ GCC_except_table7297
+ GCC_except_table7298
+ GCC_except_table7299
+ GCC_except_table7300
+ GCC_except_table7302
+ GCC_except_table7321
+ GCC_except_table7323
+ GCC_except_table7324
+ GCC_except_table7326
+ GCC_except_table7327
+ GCC_except_table7330
+ GCC_except_table7331
+ GCC_except_table7332
+ _FlatStorePageEntryWrite2.3163
+ _MurmurHash3_x86_32.16803
+ __PayloadWriteData.3709
+ __SIGetFieldNameForId
+ __SISetVectorIndexDropCallback
+ __ZGVZL12MetadataKeysvE13_metadataKeys.16751
+ __ZGVZL17GenericFilterKeysvE18_genericFilterKeys.16770
+ __ZGVZL18PhRetrievalAttribsvE17_retrievalAttribs.16471
+ __ZGVZL25GenericFilterTopLevelKeysvE26_genericFilterTopLevelKeys.16762
+ __ZGVZL26PhExactMatchRankingAttribsvE27_phExactMatchRankingAttribs.16654
+ __ZL10commonHashjPKhj.15714
+ __ZL11MAX_OIDINFO.16209
+ __ZL11TOK_ID_FROM.4081
+ __ZL12ZERO_OIDINFO.16208
+ __ZL13PhAttribNodesPKcRKNSt3__113unordered_setINS1_12basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEENS1_4hashIS8_EENS1_8equal_toIS8_EENS6_IS8_EEEEbb.16514
+ __ZL13v2_readVInt64PKhPm.8717
+ __ZL13v2_readVInt64RPKhRmRy.9271
+ __ZL14ZERO_FETCHINFO.5696
+ __ZL14v2_writeVInt64Phmy.8711
+ __ZL14v2_writeVInt64RPhy.9270
+ __ZL16__message_assertPKcz.15688
+ __ZL16__message_assertPKcz.15719
+ __ZL16__message_assertPKcz.16231
+ __ZL16__message_assertPKcz.3896
+ __ZL16__message_assertPKcz.5454
+ __ZL16__message_assertPKcz.5602
+ __ZL16__message_assertPKcz.5966
+ __ZL16__message_assertPKcz.7985
+ __ZL16__message_assertPKcz.8726
+ __ZL16si_analytics_logPKcz.8164
+ __ZL17ZERO_RANKING_BITS.16154
+ __ZL18PhRankingBoostTreev.16399
+ __ZL18PhRetrievalAttribsv.16411
+ __ZL18QueryParserLibraryv.10574
+ __ZL18QueryParserLibraryv.12834
+ __ZL18QueryParserLibraryv.16536
+ __ZL18isGenericFilterKeyRKNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE.16756
+ __ZL20PhRankingTreeFromStrPKcfPi.16382
+ __ZL22__si_assert_copy_extraP6fd_obji.15684
+ __ZL22__si_assert_copy_extraP6fd_obji.15715
+ __ZL22__si_assert_copy_extraP6fd_obji.16227
+ __ZL22__si_assert_copy_extraP6fd_obji.3892
+ __ZL22__si_assert_copy_extraP6fd_obji.5450
+ __ZL22__si_assert_copy_extraP6fd_obji.5597
+ __ZL22__si_assert_copy_extraP6fd_obji.5962
+ __ZL22__si_assert_copy_extraP6fd_obji.7980
+ __ZL22__si_assert_copy_extraP6fd_obji.8721
+ __ZL22getkQPQUOutputTokenKeyv.16492
+ __ZL23audit_stringQueryParser.10586
+ __ZL23audit_stringQueryParser.12844
+ __ZL23audit_stringQueryParser.16548
+ __ZL23store_stream_read_bytesP14store_stream_tPhm.8718
+ __ZL24store_stream_write_bytesP14store_stream_tPKhm.8710
+ __ZL25convertASTNodeToQueryNodeP9PRAstNodeP9PRContext.4038
+ __ZL26PhExactMatchRankingAttribsv.16651
+ __ZL26PhImpAttributesRankingNodePKc.16396
+ __ZL26getkQPQUOutputTokenInfoKeyv.16371
+ __ZL26isGenericFilterTopLevelKeyRKNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE.16758
+ __ZL27_containsOnlyCharsInCharsetP8NSStringP14NSCharacterSet.16386
+ __ZL27getkQPQUOutputTokenRangeKeyv.12847
+ __ZL27getkQPQUOutputTokenRangeKeyv.16489
+ __ZL28getkQPQUOutputTokenArgIdsKeyv.10622
+ __ZL28getkQPQUOutputTokenArgIdsKeyv.12848
+ __ZL28getkQPQUOutputTokenArgIdsKeyv.16490
+ __ZL31getkQPQUOutputTokenArgScoresKeyv.12849
+ __ZL31getkQPQUOutputTokenArgScoresKeyv.16491
+ __ZL32PhImpAttributesPrefixRankingNodePKc.16395
+ __ZL6sTotal.16149
+ __ZL6sTotal.16329
+ __ZL6sTotal.16440
+ __ZL6sTotal.4054
+ __ZL6sTotal.5447
+ __ZL6sTotal.5603
+ __ZL6sTotal.7360
+ __ZL6sTotal.8408
+ __ZL7Attribsv.4073
+ __ZL9TOK_ID_TO.4086
+ __ZL9intervals.8393
+ __ZZL11CurrentYearvE8currYear.16625
+ __ZZL11CurrentYearvE9onceToken.16624
+ __ZZL12MetadataKeysvE13_metadataKeys.16752
+ __ZZL12MetadataKeysvE9onceToken.16753
+ __ZZL14PhThreeYearAgovE7oldYear.16628
+ __ZZL14PhThreeYearAgovE9onceToken.16627
+ __ZZL16utf8_byte_lengthhE14utf8_len_table.16271
+ __ZZL17GenericFilterKeysvE18_genericFilterKeys.16771
+ __ZZL17GenericFilterKeysvE9onceToken.16772
+ __ZZL18PhRetrievalAttribsvE17_retrievalAttribs.16412
+ __ZZL18PhRetrievalAttribsvE9onceToken.16472
+ __ZZL18utf8_to_code_pointPKhE20utf8_first_char_mask.16272
+ __ZZL22QueryParserLibraryCorePPcE16frameworkLibrary.0.10582
+ __ZZL22QueryParserLibraryCorePPcE16frameworkLibrary.0.12840
+ __ZZL22QueryParserLibraryCorePPcE16frameworkLibrary.0.16544
+ __ZZL24utf8_byte_length_noerrorhE14utf8_len_table.16273
+ __ZZL25GenericFilterTopLevelKeysvE26_genericFilterTopLevelKeys.16763
+ __ZZL25GenericFilterTopLevelKeysvE9onceToken.16764
+ __ZZL26PhExactMatchRankingAttribsvE27_phExactMatchRankingAttribs.16652
+ __ZZL26PhExactMatchRankingAttribsvE9onceToken.16655
+ __ZZL28NanoSecondsSinceAbsoluteTimeyE13sTimebaseInfo.16402
+ __ZZL28NanoSecondsSinceAbsoluteTimeyE9onceToken.16401
+ __ZZL31getkQPQUOutputTokenKeySymbolLocvE3ptr.0.10597
+ __ZZL31getkQPQUOutputTokenKeySymbolLocvE3ptr.0.12850
+ __ZZL31getkQPQUOutputTokenKeySymbolLocvE3ptr.0.16549
+ __ZZL35getkQPQUOutputTokenInfoKeySymbolLocvE3ptr.0.16740
+ __ZZL36getkQPParseAttributeDateKeySymbolLocvE3ptr.0.12995
+ __ZZL36getkQPQUOutputTokenRangeKeySymbolLocvE3ptr.0.10631
+ __ZZL36getkQPQUOutputTokenRangeKeySymbolLocvE3ptr.0.12862
+ __ZZL36getkQPQUOutputTokenRangeKeySymbolLocvE3ptr.0.16561
+ __ZZL37getkQPParseAttributeMediaKeySymbolLocvE3ptr.0.12974
+ __ZZL37getkQPQUOutputTokenArgIdsKeySymbolLocvE3ptr.0.10623
+ __ZZL37getkQPQUOutputTokenArgIdsKeySymbolLocvE3ptr.0.12858
+ __ZZL37getkQPQUOutputTokenArgIdsKeySymbolLocvE3ptr.0.16557
+ __ZZL38getkQPParseAttributeSenderKeySymbolLocvE3ptr.0.12982
+ __ZZL38getkQPParseAttributeUnreadKeySymbolLocvE3ptr.0.12962
+ __ZZL40getkQPQUOutputTokenArgScoresKeySymbolLocvE3ptr.0.12854
+ __ZZL40getkQPQUOutputTokenArgScoresKeySymbolLocvE3ptr.0.16553
+ __ZZL41getkQPParseAttributeDueActionKeySymbolLocvE3ptr.0.12901
+ __ZZL41getkQPParseAttributeRecipientKeySymbolLocvE3ptr.0.12978
+ __ZZL42getkQPParseAttributeAttachmentKeySymbolLocvE3ptr.0.12968
+ __ZZL42getkQPParseAttributeJunkActionKeySymbolLocvE3ptr.0.12893
+ __ZZL43getkQPParseAttributeDescriptionKeySymbolLocvE3ptr.0.12889
+ __ZZL43getkQPParseAttributeDraftActionKeySymbolLocvE3ptr.0.12897
+ __ZZL43getkQPParseAttributeHotelActionKeySymbolLocvE3ptr.0.12925
+ __ZZL44getkQPParseAttributeFlightActionKeySymbolLocvE3ptr.0.12938
+ __ZZL44getkQPParseAttributeLatestActionKeySymbolLocvE3ptr.0.12909
+ __ZZL44getkQPParseAttributeTaggedPersonKeySymbolLocvE3ptr.0.12991
+ __ZZL45getkQPParseAttributeArchiveActionKeySymbolLocvE3ptr.0.12885
+ __ZZL45getkQPParseAttributePrintedActionKeySymbolLocvE3ptr.0.12944
+ __ZZL46getkQPParseAttributeEarliestActionKeySymbolLocvE3ptr.0.12913
+ __ZZL46getkQPParseAttributeGroundedPersonKeySymbolLocvE3ptr.0.12986
+ __ZZL47getkQPParseAttributeCompletedActionKeySymbolLocvE3ptr.0.12905
+ __ZZL48getkQPParseAttributeRestaurantActionKeySymbolLocvE3ptr.0.12919
+ __ZZL53getkQPParseAttributeFlightArrivalLocationKeySymbolLocvE3ptr.0.12929
+ __ZZL55getkQPParseAttributeFlightDepartureLocationKeySymbolLocvE3ptr.0.12933
+ ___Block_byref_object_copy_.10642
+ ___Block_byref_object_copy_.12883
+ ___Block_byref_object_copy_.13345
+ ___Block_byref_object_copy_.16195
+ ___Block_byref_object_copy_.7499
+ ___Block_byref_object_dispose_.10643
+ ___Block_byref_object_dispose_.12884
+ ___Block_byref_object_dispose_.13346
+ ___Block_byref_object_dispose_.16196
+ ___Block_byref_object_dispose_.7500
+ ____ZL11CurrentYearv_block_invoke.16641
+ ____ZL12MetadataKeysv_block_invoke.16788
+ ____ZL14PhThreeYearAgov_block_invoke.16638
+ ____ZL17GenericFilterKeysv_block_invoke.16776
+ ____ZL18PhRetrievalAttribsv_block_invoke.16474
+ ____ZL19convertQPFilterNodeP17PRAstQPFilterNodeP9PRContext_block_invoke.4092
+ ____ZL20PhRankingTreeFromStrPKcfPi_block_invoke.16644
+ ____ZL22QueryParserLibraryCorePPc_block_invoke.10583
+ ____ZL22QueryParserLibraryCorePPc_block_invoke.12841
+ ____ZL22QueryParserLibraryCorePPc_block_invoke.16545
+ ____ZL25GenericFilterTopLevelKeysv_block_invoke.16768
+ ____ZL26PhExactMatchRankingAttribsv_block_invoke.16657
+ ____ZL28NanoSecondsSinceAbsoluteTimey_block_invoke.16623
+ ____ZL28PhPopulateAllFilterFromParseP18NSAttributedStringP14NSMutableArrayIP8NSStringEPS1_IP7NSValueES9_S9_S9__block_invoke.16375
+ ____ZL29PhPopulateDateFilterFromParseP18NSAttributedStringP14NSMutableArrayIP8NSStringEPS1_IP7NSValueE_block_invoke.16485
+ ____ZL30PhPopulateSomeFiltersFromParseP18NSAttributedStringP14NSMutableArrayIP8NSStringEPS1_IP7NSValueES5_S9__block_invoke.16482
+ ____ZL31getkQPQUOutputTokenKeySymbolLocv_block_invoke.10598
+ ____ZL31getkQPQUOutputTokenKeySymbolLocv_block_invoke.12851
+ ____ZL31getkQPQUOutputTokenKeySymbolLocv_block_invoke.16550
+ ____ZL35getkQPQUOutputTokenInfoKeySymbolLocv_block_invoke.16741
+ ____ZL36getkQPParseAttributeDateKeySymbolLocv_block_invoke.12996
+ ____ZL36getkQPQUOutputTokenRangeKeySymbolLocv_block_invoke.10632
+ ____ZL36getkQPQUOutputTokenRangeKeySymbolLocv_block_invoke.12863
+ ____ZL36getkQPQUOutputTokenRangeKeySymbolLocv_block_invoke.16562
+ ____ZL37getkQPParseAttributeMediaKeySymbolLocv_block_invoke.12975
+ ____ZL37getkQPQUOutputTokenArgIdsKeySymbolLocv_block_invoke.10624
+ ____ZL37getkQPQUOutputTokenArgIdsKeySymbolLocv_block_invoke.12859
+ ____ZL37getkQPQUOutputTokenArgIdsKeySymbolLocv_block_invoke.16558
+ ____ZL38getkQPParseAttributeSenderKeySymbolLocv_block_invoke.12983
+ ____ZL38getkQPParseAttributeUnreadKeySymbolLocv_block_invoke.12963
+ ____ZL40getkQPQUOutputTokenArgScoresKeySymbolLocv_block_invoke.12855
+ ____ZL40getkQPQUOutputTokenArgScoresKeySymbolLocv_block_invoke.16554
+ ____ZL41getkQPParseAttributeDueActionKeySymbolLocv_block_invoke.12902
+ ____ZL41getkQPParseAttributeRecipientKeySymbolLocv_block_invoke.12979
+ ____ZL42getkQPParseAttributeAttachmentKeySymbolLocv_block_invoke.12969
+ ____ZL42getkQPParseAttributeJunkActionKeySymbolLocv_block_invoke.12894
+ ____ZL43getkQPParseAttributeDescriptionKeySymbolLocv_block_invoke.12890
+ ____ZL43getkQPParseAttributeDraftActionKeySymbolLocv_block_invoke.12898
+ ____ZL43getkQPParseAttributeHotelActionKeySymbolLocv_block_invoke.12926
+ ____ZL44getkQPParseAttributeFlightActionKeySymbolLocv_block_invoke.12939
+ ____ZL44getkQPParseAttributeLatestActionKeySymbolLocv_block_invoke.12910
+ ____ZL44getkQPParseAttributeTaggedPersonKeySymbolLocv_block_invoke.12992
+ ____ZL45getkQPParseAttributeArchiveActionKeySymbolLocv_block_invoke.12886
+ ____ZL45getkQPParseAttributePrintedActionKeySymbolLocv_block_invoke.12945
+ ____ZL46getkQPParseAttributeEarliestActionKeySymbolLocv_block_invoke.12914
+ ____ZL46getkQPParseAttributeGroundedPersonKeySymbolLocv_block_invoke.12987
+ ____ZL47getkQPParseAttributeCompletedActionKeySymbolLocv_block_invoke.12906
+ ____ZL48getkQPParseAttributeRestaurantActionKeySymbolLocv_block_invoke.12920
+ ____ZL53getkQPParseAttributeFlightArrivalLocationKeySymbolLocv_block_invoke.12930
+ ____ZL55getkQPParseAttributeFlightDepartureLocationKeySymbolLocv_block_invoke.12934
+ ___block_descriptor_40_e8_32o_e39_v32?0"NSString"8"NSDictionary"16^B24ls32l8
+ ___block_descriptor_tmp.1.5477
+ ___block_descriptor_tmp.10.14168
+ ___block_descriptor_tmp.10.15355
+ ___block_descriptor_tmp.1084.8218
+ ___block_descriptor_tmp.1095.8027
+ ___block_descriptor_tmp.11.15740
+ ___block_descriptor_tmp.11.8862
+ ___block_descriptor_tmp.1100.8034
+ ___block_descriptor_tmp.11023
+ ___block_descriptor_tmp.111.15258
+ ___block_descriptor_tmp.111.6101
+ ___block_descriptor_tmp.11117
+ ___block_descriptor_tmp.11244
+ ___block_descriptor_tmp.113.8161
+ ___block_descriptor_tmp.11329
+ ___block_descriptor_tmp.117.15529
+ ___block_descriptor_tmp.117.9701
+ ___block_descriptor_tmp.118.5707
+ ___block_descriptor_tmp.11842
+ ___block_descriptor_tmp.12.11147
+ ___block_descriptor_tmp.12.15376
+ ___block_descriptor_tmp.12.16026
+ ___block_descriptor_tmp.12.16244
+ ___block_descriptor_tmp.12.4312
+ ___block_descriptor_tmp.12.5952
+ ___block_descriptor_tmp.12.8292
+ ___block_descriptor_tmp.12.8874
+ ___block_descriptor_tmp.121.15528
+ ___block_descriptor_tmp.1215.8123
+ ___block_descriptor_tmp.123.15309
+ ___block_descriptor_tmp.123.8165
+ ___block_descriptor_tmp.123.8961
+ ___block_descriptor_tmp.1243.8214
+ ___block_descriptor_tmp.126.8166
+ ___block_descriptor_tmp.12774
+ ___block_descriptor_tmp.128.14612
+ ___block_descriptor_tmp.129.14818
+ ___block_descriptor_tmp.13.15382
+ ___block_descriptor_tmp.13.16245
+ ___block_descriptor_tmp.13.4307
+ ___block_descriptor_tmp.13.5403
+ ___block_descriptor_tmp.13.5482
+ ___block_descriptor_tmp.13.6374
+ ___block_descriptor_tmp.13.8875
+ ___block_descriptor_tmp.13.8963
+ ___block_descriptor_tmp.130
+ ___block_descriptor_tmp.13083
+ ___block_descriptor_tmp.131.9877
+ ___block_descriptor_tmp.136.5712
+ ___block_descriptor_tmp.13632
+ ___block_descriptor_tmp.138.5813
+ ___block_descriptor_tmp.13842
+ ___block_descriptor_tmp.14.4965
+ ___block_descriptor_tmp.14054
+ ___block_descriptor_tmp.14157
+ ___block_descriptor_tmp.14340
+ ___block_descriptor_tmp.14555
+ ___block_descriptor_tmp.146.14739
+ ___block_descriptor_tmp.14646
+ ___block_descriptor_tmp.1473.8149
+ ___block_descriptor_tmp.15.5483
+ ___block_descriptor_tmp.151.9952
+ ___block_descriptor_tmp.15349
+ ___block_descriptor_tmp.154.8245
+ ___block_descriptor_tmp.155.14757
+ ___block_descriptor_tmp.156.8253
+ ___block_descriptor_tmp.15697
+ ___block_descriptor_tmp.157.8256
+ ___block_descriptor_tmp.15709
+ ___block_descriptor_tmp.159.14950
+ ___block_descriptor_tmp.15974
+ ___block_descriptor_tmp.16.11153
+ ___block_descriptor_tmp.16.4966
+ ___block_descriptor_tmp.16.7902
+ ___block_descriptor_tmp.160.14669
+ ___block_descriptor_tmp.160.7994
+ ___block_descriptor_tmp.161.14804
+ ___block_descriptor_tmp.16167
+ ___block_descriptor_tmp.167.15561
+ ___block_descriptor_tmp.168.15562
+ ___block_descriptor_tmp.17.13099
+ ___block_descriptor_tmp.17.7001
+ ___block_descriptor_tmp.170.10025
+ ___block_descriptor_tmp.170.15559
+ ___block_descriptor_tmp.172.15420
+ ___block_descriptor_tmp.172.6059
+ ___block_descriptor_tmp.18.14643
+ ___block_descriptor_tmp.18.8982
+ ___block_descriptor_tmp.187.15173
+ ___block_descriptor_tmp.19.10159
+ ___block_descriptor_tmp.19.13102
+ ___block_descriptor_tmp.19.15422
+ ___block_descriptor_tmp.19.2517
+ ___block_descriptor_tmp.2.16239
+ ___block_descriptor_tmp.2.5405
+ ___block_descriptor_tmp.2.5478
+ ___block_descriptor_tmp.2.5619
+ ___block_descriptor_tmp.2.7915
+ ___block_descriptor_tmp.2.9282
+ ___block_descriptor_tmp.20.12713
+ ___block_descriptor_tmp.20.16267
+ ___block_descriptor_tmp.20.4126
+ ___block_descriptor_tmp.21.11185
+ ___block_descriptor_tmp.21.11674
+ ___block_descriptor_tmp.22.13626
+ ___block_descriptor_tmp.22.14640
+ ___block_descriptor_tmp.23.15418
+ ___block_descriptor_tmp.23.4148
+ ___block_descriptor_tmp.23.9007
+ ___block_descriptor_tmp.24.3453
+ ___block_descriptor_tmp.24.4147
+ ___block_descriptor_tmp.25.11189
+ ___block_descriptor_tmp.25.11683
+ ___block_descriptor_tmp.25.16096
+ ___block_descriptor_tmp.2528
+ ___block_descriptor_tmp.26.13106
+ ___block_descriptor_tmp.26.14847
+ ___block_descriptor_tmp.26.15450
+ ___block_descriptor_tmp.26.16097
+ ___block_descriptor_tmp.26.6414
+ ___block_descriptor_tmp.2690
+ ___block_descriptor_tmp.27.15455
+ ___block_descriptor_tmp.27.5673
+ ___block_descriptor_tmp.28.10148
+ ___block_descriptor_tmp.28.13108
+ ___block_descriptor_tmp.28.15456
+ ___block_descriptor_tmp.28.4153
+ ___block_descriptor_tmp.28.6446
+ ___block_descriptor_tmp.28.8548
+ ___block_descriptor_tmp.29.11688
+ ___block_descriptor_tmp.29.4152
+ ___block_descriptor_tmp.29.7701
+ ___block_descriptor_tmp.2918
+ ___block_descriptor_tmp.3.15977
+ ___block_descriptor_tmp.3.9288
+ ___block_descriptor_tmp.30.11691
+ ___block_descriptor_tmp.30.14841
+ ___block_descriptor_tmp.30.15493
+ ___block_descriptor_tmp.30.15989
+ ___block_descriptor_tmp.31.14111
+ ___block_descriptor_tmp.31.4962
+ ___block_descriptor_tmp.31.7922
+ ___block_descriptor_tmp.32.4717
+ ___block_descriptor_tmp.33.13091
+ ___block_descriptor_tmp.33.14112
+ ___block_descriptor_tmp.33.14839
+ ___block_descriptor_tmp.33.15491
+ ___block_descriptor_tmp.33.4156
+ ___block_descriptor_tmp.33.4480
+ ___block_descriptor_tmp.3365
+ ___block_descriptor_tmp.34.14113
+ ___block_descriptor_tmp.34.15991
+ ___block_descriptor_tmp.34.4155
+ ___block_descriptor_tmp.35.4957
+ ___block_descriptor_tmp.35.7926
+ ___block_descriptor_tmp.36.14837
+ ___block_descriptor_tmp.36.15501
+ ___block_descriptor_tmp.37.15509
+ ___block_descriptor_tmp.3736
+ ___block_descriptor_tmp.39.14118
+ ___block_descriptor_tmp.39.14835
+ ___block_descriptor_tmp.3955
+ ___block_descriptor_tmp.4.15981
+ ___block_descriptor_tmp.4.5467
+ ___block_descriptor_tmp.4.5620
+ ___block_descriptor_tmp.4.9291
+ ___block_descriptor_tmp.40.15507
+ ___block_descriptor_tmp.40.2529
+ ___block_descriptor_tmp.41.4974
+ ___block_descriptor_tmp.411.9878
+ ___block_descriptor_tmp.4129
+ ___block_descriptor_tmp.42.13123
+ ___block_descriptor_tmp.42.14832
+ ___block_descriptor_tmp.4305
+ ___block_descriptor_tmp.4339
+ ___block_descriptor_tmp.45.2548
+ ___block_descriptor_tmp.4542
+ ___block_descriptor_tmp.4578
+ ___block_descriptor_tmp.46.13118
+ ___block_descriptor_tmp.47.15521
+ ___block_descriptor_tmp.48.13121
+ ___block_descriptor_tmp.48.14922
+ ___block_descriptor_tmp.48.15522
+ ___block_descriptor_tmp.48.9376
+ ___block_descriptor_tmp.49.15525
+ ___block_descriptor_tmp.4907
+ ___block_descriptor_tmp.4943
+ ___block_descriptor_tmp.5.7916
+ ___block_descriptor_tmp.51.14129
+ ___block_descriptor_tmp.51.14920
+ ___block_descriptor_tmp.51.7823
+ ___block_descriptor_tmp.51.9373
+ ___block_descriptor_tmp.5183
+ ___block_descriptor_tmp.52.13126
+ ___block_descriptor_tmp.52.2557
+ ___block_descriptor_tmp.52.7198
+ ___block_descriptor_tmp.52.9067
+ ___block_descriptor_tmp.53.14130
+ ___block_descriptor_tmp.5337
+ ___block_descriptor_tmp.5381
+ ___block_descriptor_tmp.54.14918
+ ___block_descriptor_tmp.54.7830
+ ___block_descriptor_tmp.5466
+ ___block_descriptor_tmp.55.14115
+ ___block_descriptor_tmp.56.7824
+ ___block_descriptor_tmp.5618
+ ___block_descriptor_tmp.57.13137
+ ___block_descriptor_tmp.57.14116
+ ___block_descriptor_tmp.57.5776
+ ___block_descriptor_tmp.58.2833
+ ___block_descriptor_tmp.58.5777
+ ___block_descriptor_tmp.59.14899
+ ___block_descriptor_tmp.59.2559
+ ___block_descriptor_tmp.5903
+ ___block_descriptor_tmp.6.16197
+ ___block_descriptor_tmp.6.4303
+ ___block_descriptor_tmp.6.4346
+ ___block_descriptor_tmp.6.4900
+ ___block_descriptor_tmp.6.5469
+ ___block_descriptor_tmp.6.5625
+ ___block_descriptor_tmp.60.16210
+ ___block_descriptor_tmp.60.5778
+ ___block_descriptor_tmp.62.13736
+ ___block_descriptor_tmp.6291
+ ___block_descriptor_tmp.63.15547
+ ___block_descriptor_tmp.6368
+ ___block_descriptor_tmp.64.14164
+ ___block_descriptor_tmp.65.15650
+ ___block_descriptor_tmp.65.3615
+ ___block_descriptor_tmp.65.4383
+ ___block_descriptor_tmp.65.9141
+ ___block_descriptor_tmp.6531
+ ___block_descriptor_tmp.655.8222
+ ___block_descriptor_tmp.66.13735
+ ___block_descriptor_tmp.66.5741
+ ___block_descriptor_tmp.68.5744
+ ___block_descriptor_tmp.68.9139
+ ___block_descriptor_tmp.6969
+ ___block_descriptor_tmp.7.11140
+ ___block_descriptor_tmp.7.3953
+ ___block_descriptor_tmp.7.4343
+ ___block_descriptor_tmp.7.4902
+ ___block_descriptor_tmp.7.5622
+ ___block_descriptor_tmp.70.13798
+ ___block_descriptor_tmp.7069
+ ___block_descriptor_tmp.72.5745
+ ___block_descriptor_tmp.73.3633
+ ___block_descriptor_tmp.74.6102
+ ___block_descriptor_tmp.7598
+ ___block_descriptor_tmp.76.15673
+ ___block_descriptor_tmp.76.7753
+ ___block_descriptor_tmp.7643
+ ___block_descriptor_tmp.77.14946
+ ___block_descriptor_tmp.77.15676
+ ___block_descriptor_tmp.7888
+ ___block_descriptor_tmp.7952
+ ___block_descriptor_tmp.7973
+ ___block_descriptor_tmp.8.11832
+ ___block_descriptor_tmp.8.15689
+ ___block_descriptor_tmp.8.4017
+ ___block_descriptor_tmp.8.7962
+ ___block_descriptor_tmp.80.6103
+ ___block_descriptor_tmp.83.13824
+ ___block_descriptor_tmp.84.9158
+ ___block_descriptor_tmp.8499
+ ___block_descriptor_tmp.8561
+ ___block_descriptor_tmp.874.8148
+ ___block_descriptor_tmp.8861
+ ___block_descriptor_tmp.8958
+ ___block_descriptor_tmp.9.14374
+ ___block_descriptor_tmp.9.5409
+ ___block_descriptor_tmp.9.5679
+ ___block_descriptor_tmp.9.8236
+ ___block_descriptor_tmp.908.8221
+ ___block_descriptor_tmp.9278
+ ___block_descriptor_tmp.9334
+ ___block_descriptor_tmp.9566
+ ___block_descriptor_tmp.96.15193
+ ___block_descriptor_tmp.972.8219
+ ___block_descriptor_tmp.986.8220
+ ___block_literal_global.10155
+ ___block_literal_global.10644
+ ___block_literal_global.11.14368
+ ___block_literal_global.1102.8028
+ ___block_literal_global.11021
+ ___block_literal_global.11115
+ ___block_literal_global.11242
+ ___block_literal_global.117.16702
+ ___block_literal_global.11840
+ ___block_literal_global.11864
+ ___block_literal_global.125.4713
+ ___block_literal_global.125.8957
+ ___block_literal_global.12772
+ ___block_literal_global.13087
+ ___block_literal_global.133
+ ___block_literal_global.13624
+ ___block_literal_global.13840
+ ___block_literal_global.14.11145
+ ___block_literal_global.14.16022
+ ___block_literal_global.14052
+ ___block_literal_global.14338
+ ___block_literal_global.14636
+ ___block_literal_global.15.15380
+ ___block_literal_global.15.5392
+ ___block_literal_global.15.6372
+ ___block_literal_global.15374
+ ___block_literal_global.15695
+ ___block_literal_global.15707
+ ___block_literal_global.15975
+ ___block_literal_global.16.6518
+ ___block_literal_global.16224
+ ___block_literal_global.16346
+ ___block_literal_global.16754
+ ___block_literal_global.18.11151
+ ___block_literal_global.18.7900
+ ___block_literal_global.20.14637
+ ___block_literal_global.21.13100
+ ___block_literal_global.21.15415
+ ___block_literal_global.22.16265
+ ___block_literal_global.23.11183
+ ___block_literal_global.25.15416
+ ___block_literal_global.2526
+ ___block_literal_global.26.4145
+ ___block_literal_global.2688
+ ___block_literal_global.27.11187
+ ___block_literal_global.2831
+ ___block_literal_global.29.5640
+ ___block_literal_global.31.4150
+ ___block_literal_global.32.14825
+ ___block_literal_global.32.15488
+ ___block_literal_global.32.15986
+ ___block_literal_global.32.16773
+ ___block_literal_global.33.4954
+ ___block_literal_global.33.7920
+ ___block_literal_global.3482
+ ___block_literal_global.35.13088
+ ___block_literal_global.35.14826
+ ___block_literal_global.35.15489
+ ___block_literal_global.35.4441
+ ___block_literal_global.37.4955
+ ___block_literal_global.37.7924
+ ___block_literal_global.38.14827
+ ___block_literal_global.3856
+ ___block_literal_global.39.15504
+ ___block_literal_global.4.5387
+ ___block_literal_global.4.7913
+ ___block_literal_global.4015
+ ___block_literal_global.4078
+ ___block_literal_global.41.14828
+ ___block_literal_global.4124
+ ___block_literal_global.42.15505
+ ___block_literal_global.43.4971
+ ___block_literal_global.4309
+ ___block_literal_global.4340
+ ___block_literal_global.44.14829
+ ___block_literal_global.4557
+ ___block_literal_global.4941
+ ___block_literal_global.50.14875
+ ___block_literal_global.50.9361
+ ___block_literal_global.51.13125
+ ___block_literal_global.51.15523
+ ___block_literal_global.53.14876
+ ___block_literal_global.53.9362
+ ___block_literal_global.5335
+ ___block_literal_global.5379
+ ___block_literal_global.5621
+ ___block_literal_global.5901
+ ___block_literal_global.6.15979
+ ___block_literal_global.6289
+ ___block_literal_global.6366
+ ___block_literal_global.65.16765
+ ___block_literal_global.6502
+ ___block_literal_global.67.15609
+ ___block_literal_global.67.9138
+ ___block_literal_global.6993
+ ___block_literal_global.7209
+ ___block_literal_global.7886
+ ___block_literal_global.7971
+ ___block_literal_global.8497
+ ___block_literal_global.8510
+ ___block_literal_global.9.11138
+ ___block_literal_global.9.4341
+ ___block_literal_global.9005
+ ___block_literal_global.9313
+ ___block_literal_global.94.7573
+ ___block_literal_global.9564
+ ___block_literal_global.98.15191
+ ___isAppleInternalInstall_block_invoke.13138
+ ___message_assert.11265
+ ___message_assert.11501
+ ___message_assert.11831
+ ___message_assert.12651
+ ___message_assert.12696
+ ___message_assert.12754
+ ___message_assert.13164
+ ___message_assert.13442
+ ___message_assert.13501
+ ___message_assert.13561
+ ___message_assert.13620
+ ___message_assert.14069
+ ___message_assert.14201
+ ___message_assert.14349
+ ___message_assert.14577
+ ___message_assert.15339
+ ___message_assert.15764
+ ___message_assert.16001
+ ___message_assert.17058
+ ___message_assert.2713
+ ___message_assert.2932
+ ___message_assert.2953
+ ___message_assert.3135
+ ___message_assert.3238
+ ___message_assert.3696
+ ___message_assert.3757
+ ___message_assert.3921
+ ___message_assert.4105
+ ___message_assert.4119
+ ___message_assert.4179
+ ___message_assert.4338
+ ___message_assert.4522
+ ___message_assert.4551
+ ___message_assert.4939
+ ___message_assert.5909
+ ___message_assert.6251
+ ___message_assert.6337
+ ___message_assert.6550
+ ___message_assert.6965
+ ___message_assert.7058
+ ___message_assert.7619
+ ___message_assert.7650
+ ___message_assert.7856
+ ___message_assert.8435
+ ___message_assert.8460
+ ___message_assert.8520
+ ___message_assert.8761
+ ___message_assert.8900
+ ___message_assert.8933
+ ___message_assert.9358
+ ___message_assert.9596
+ ___path_bundle_index_block_invoke.10161
+ ___si_assert_copy_extra.11261
+ ___si_assert_copy_extra.11827
+ ___si_assert_copy_extra.12646
+ ___si_assert_copy_extra.12691
+ ___si_assert_copy_extra.12750
+ ___si_assert_copy_extra.13160
+ ___si_assert_copy_extra.13438
+ ___si_assert_copy_extra.13497
+ ___si_assert_copy_extra.13556
+ ___si_assert_copy_extra.13615
+ ___si_assert_copy_extra.14064
+ ___si_assert_copy_extra.14196
+ ___si_assert_copy_extra.14344
+ ___si_assert_copy_extra.14572
+ ___si_assert_copy_extra.15335
+ ___si_assert_copy_extra.15760
+ ___si_assert_copy_extra.15996
+ ___si_assert_copy_extra.16993
+ ___si_assert_copy_extra.2708
+ ___si_assert_copy_extra.2928
+ ___si_assert_copy_extra.2949
+ ___si_assert_copy_extra.3130
+ ___si_assert_copy_extra.3233
+ ___si_assert_copy_extra.3692
+ ___si_assert_copy_extra.3753
+ ___si_assert_copy_extra.3916
+ ___si_assert_copy_extra.4101
+ ___si_assert_copy_extra.4115
+ ___si_assert_copy_extra.4174
+ ___si_assert_copy_extra.4333
+ ___si_assert_copy_extra.4518
+ ___si_assert_copy_extra.4546
+ ___si_assert_copy_extra.4934
+ ___si_assert_copy_extra.5905
+ ___si_assert_copy_extra.6246
+ ___si_assert_copy_extra.6332
+ ___si_assert_copy_extra.6546
+ ___si_assert_copy_extra.6961
+ ___si_assert_copy_extra.7054
+ ___si_assert_copy_extra.7615
+ ___si_assert_copy_extra.7645
+ ___si_assert_copy_extra.7852
+ ___si_assert_copy_extra.8432
+ ___si_assert_copy_extra.8455
+ ___si_assert_copy_extra.8515
+ ___si_assert_copy_extra.8756
+ ___si_assert_copy_extra.8895
+ ___si_assert_copy_extra.8928
+ ___si_assert_copy_extra.9354
+ ___si_assert_copy_extra.9591
+ __psid_insert.5014
+ _bit_vector_create.15954
+ _bit_vector_create.17090
+ _bit_vector_init.4656
+ _bit_vector_internal_touch_for_set.4691
+ _bit_vector_set.13535
+ _bit_vector_set.15898
+ _bit_vector_set.17054
+ _bit_vector_set.2766
+ _bit_vector_set.3411
+ _bit_vector_set.4242
+ _bit_vector_set.4833
+ _bit_vector_set.7166
+ _bit_vector_set_bits.4698
+ _checkNearness.14185
+ _commonHash.11754
+ _commonHash.16992
+ _data_entry_store.16962
+ _emitTerms.7725
+ _getSize.memSize.11825
+ _getSize.memSize.13630
+ _getSize.memSize.4562
+ _get_string_and_length_for_id.15021
+ _hash64.7816
+ _index_comp.11839
+ _index_comp.13636
+ _index_comp.4567
+ _isAppleInternalInstall.isInternalInstall.13133
+ _isAppleInternalInstall.onceToken.13132
+ _keycompare.4999
+ _localizedFieldTermMatch.14134
+ _log_map_access_error.15821
+ _log_map_access_error.16935
+ _log_map_access_error.7114
+ _master_fid_rec.4983
+ _master_fid_rec_size.4985
+ _objc_msgSend$heartbeatData
+ _objc_msgSend$initWithDomain:code:userInfo:
+ _objc_msgSend$initWithPrefix:data:
+ _objc_msgSend$numberWithDouble:
+ _oqpush.13659
+ _oqpush.3290
+ _oqpush.4581
+ _packingCount.13804
+ _path_bundle_index.sDummyFD.10156
+ _pqDisposeApplier.7720
+ _psid_lookup.5012
+ _qsort_cached_allocations.11823
+ _qsort_cached_allocations.13628
+ _qsort_cached_allocations.4560
+ _query_realloc.8905
+ _readCompactPosition.13808
+ _remapping_keys.11804
+ _restoreVInt32.12670
+ _restoreVInt32.3354
+ _restoreVInt32.3928
+ _sDataMapExceptionCallbacks.15775
+ _sDataMapExceptionCallbacks.16910
+ _sResourcesCallback
+ _sTotal.13683
+ _sTotal.14063
+ _sTotal.14546
+ _sTotal.15332
+ _sTotal.4537
+ _sTotal.4940
+ _sTotal.5923
+ _sTotal.6326
+ _sTotal.8910
+ _sTotal.9353
+ _sTotal.9528
+ _sVectorIndexDropCallback
+ _si_analytics_log.14362
+ _si_analytics_log.14761
+ _si_analytics_log.15813
+ _si_analytics_log.16996
+ _si_analytics_log.2752
+ _si_analytics_log.3138
+ _si_analytics_log.3636
+ _si_analytics_log.3718
+ _si_analytics_log.4247
+ _si_analytics_log.4767
+ _si_analytics_log.6257
+ _si_analytics_log.7109
+ _si_analytics_log.7679
+ _si_analytics_log.8636
+ _si_analytics_log.8973
+ _si_rwlock_wrunlock.3589
+ _storeVInt64.13516
+ _storeVInt64.4196
+ _store_stream_read_bytes.13603
+ _store_stream_read_bytes.3410
+ _store_stream_read_bytes.4392
+ _store_stream_read_bytes.4884
+ _store_stream_read_bytes.6874
+ _store_stream_read_vint32.13599
+ _store_stream_read_vint32.3407
+ _store_stream_read_vint32.4390
+ _store_stream_read_vint32.6870
+ _store_stream_write_bytes.13609
+ _store_stream_write_bytes.3266
+ _store_stream_write_bytes.4380
+ _store_stream_write_bytes.4888
+ _store_stream_write_bytes.6862
+ _store_stream_write_vint32.13606
+ _store_stream_write_vint32.3268
+ _store_stream_write_vint32.4381
+ _store_stream_write_vint32.6863
+ _strHash.17284
+ _table_extra_bytes.14628
+ _takeBuddyPage.4233
+ _termPropertyID.14135
+ _thread_count.11824
+ _thread_count.13629
+ _thread_count.4561
+ _v2_readVInt32.4408
+ _v2_readVInt64.11331
+ _v2_readVInt64.13796
+ _v2_readVInt64.14180
+ _v2_readVInt64.14222
+ _v2_readVInt64.2873
+ _v2_readVInt64.3194
+ _v2_readVInt64.4403
+ _v2_readVInt64.7800
+ _v2_writeVInt64.11288
+ _v2_writeVInt64.13611
+ _v2_writeVInt64.3164
+ _vector_dimension.vec_sizes.15424
+ _vector_size.elem_sizes.15423
+ _writeVInt64.13608
+ _writeVInt64.14235
+ _writeVInt64.3720
+ _writeVInt64.4382
+ _writeVInt64.4654
+ _writeVInt64.6254
+ _writeVectorIndexDrop
- +[SIAnalytics getCurrentSpotlightVersionWithRoots:]
- +[SIAnalytics getPreviousBuild]
- +[SIAnalytics hasSpotlightRoots]
- +[SIAnalytics isHeartbeatReportingDisabled]
- +[SIAnalytics isIndexDropReportingDisabled]
- +[SIAnalytics recordRequestsForIndex:adds:updates:deletes:]
- +[SIAnalytics runCommand:]
- +[SIAnalytics sendHeartbeatEvent]
- +[SIAnalytics sendIndexDropEventWithCorruptIndex:path:readOnly:reason:]
- +[SIAnalytics setPurgeability:forIndex:]
- +[SIAnalytics setSpotlightVersion]
- +[SIAnalytics sharedInstance]
- -[SIAnalytics createDropDataForIndex:path:error:]
- -[SIAnalytics createHeartbeatDataWithRefresh:error:]
- -[SIAnalytics dealloc]
- -[SIAnalytics eventCount]
- -[SIAnalytics getIndexDataForPrefix:]
- -[SIAnalytics getPreviousBuild]
- -[SIAnalytics initWithParentDirectoryPath:corespotlight:heartbeatIndex:resourcesCallback:]
- -[SIAnalytics initializeSharedHearbeatFields]
- -[SIAnalytics migrateFromLegacyHeartbeatData:]
- -[SIAnalytics populateIndexDropData:forIndex:reason:error:]
- -[SIAnalytics recordLocaleChange:]
- -[SIAnalytics recordOpen:forIndex:dirty:]
- -[SIAnalytics recordRequestsForIndex:adds:updates:deletes:]
- -[SIAnalytics resetAfterHeartbeat]
- -[SIAnalytics runCommand:]
- -[SIAnalytics sendHeartbeatEventWithData:withReset:]
- -[SIAnalytics sendHeartbeatEvent]
- -[SIAnalytics sendIndexDropEventWithCorruptIndex:path:readOnly:reason:]
- -[SIAnalytics sendIndexDropEventWithData:]
- -[SIAnalytics sendLegacyHeartbeatEventWithData:]
- -[SIAnalytics sendLegacyIndexDropEventWithData:readOnly:prefix:]
- -[SIAnalytics sendVectorIndexDropForIndex:vectorCount:readOnly:prefix:propertyName:dropReason:]
- -[SIAnalytics setHeartbeatTimestampForPrefix:key:]
- -[SIAnalytics setPurgeability:forIndex:]
- -[SIAnalytics shouldReportIndexDrop:]
- -[SIAnalytics usageInfoForCommand:]
- -[SIAnalyticsIndexData copyHeartbeatData]
- -[SIAnalyticsIndexData dealloc]
- -[SIAnalyticsIndexData initWithPrefix:]
- -[SIAnalyticsIndexData recordDrop:]
- -[SIAnalyticsIndexData recordOpen:dirty:]
- -[SIAnalyticsIndexData recordRequestedAdds:updates:deletes:]
- -[SIAnalyticsIndexData refreshHeartbeatDataWithIndex:path:errors:]
- -[SIAnalyticsIndexData resetAfterHeartbeat]
- -[SIAnalyticsIndexData setPurgeability:]
- -[SIAnalyticsIndexData setTimestampForKey:]
- -[SIAnalyticsIndexData shouldReportIndexDrop:]
- -[SIAnalyticsIndexData updateWithData:]
- GCC_except_table1515
- GCC_except_table1517
- GCC_except_table1524
- GCC_except_table1527
- GCC_except_table1595
- GCC_except_table1762
- GCC_except_table1766
- GCC_except_table1798
- GCC_except_table2386
- GCC_except_table2397
- GCC_except_table2398
- GCC_except_table2401
- GCC_except_table2811
- GCC_except_table3571
- GCC_except_table3572
- GCC_except_table3573
- GCC_except_table3574
- GCC_except_table3575
- GCC_except_table3576
- GCC_except_table3577
- GCC_except_table3578
- GCC_except_table3579
- GCC_except_table3580
- GCC_except_table3581
- GCC_except_table3582
- GCC_except_table3583
- GCC_except_table3589
- GCC_except_table3599
- GCC_except_table3600
- GCC_except_table3602
- GCC_except_table3606
- GCC_except_table3619
- GCC_except_table3624
- GCC_except_table3629
- GCC_except_table3630
- GCC_except_table3633
- GCC_except_table3634
- GCC_except_table3635
- GCC_except_table3636
- GCC_except_table3639
- GCC_except_table3640
- GCC_except_table3641
- GCC_except_table5471
- GCC_except_table5473
- GCC_except_table5938
- GCC_except_table5940
- GCC_except_table5944
- GCC_except_table5948
- GCC_except_table5957
- GCC_except_table5959
- GCC_except_table5969
- GCC_except_table5971
- GCC_except_table5980
- GCC_except_table5981
- GCC_except_table5982
- GCC_except_table5998
- GCC_except_table5999
- GCC_except_table6000
- GCC_except_table6001
- GCC_except_table6002
- GCC_except_table6003
- GCC_except_table6004
- GCC_except_table6005
- GCC_except_table6006
- GCC_except_table6007
- GCC_except_table6008
- GCC_except_table6009
- GCC_except_table6010
- GCC_except_table6016
- GCC_except_table6025
- GCC_except_table6026
- GCC_except_table6027
- GCC_except_table6028
- GCC_except_table6029
- GCC_except_table6030
- GCC_except_table6038
- GCC_except_table6039
- GCC_except_table6040
- GCC_except_table6041
- GCC_except_table6042
- GCC_except_table6058
- GCC_except_table6059
- GCC_except_table6060
- GCC_except_table6061
- GCC_except_table6062
- GCC_except_table6122
- GCC_except_table6125
- GCC_except_table6128
- GCC_except_table6129
- GCC_except_table6130
- GCC_except_table6131
- GCC_except_table6364
- GCC_except_table6365
- GCC_except_table6366
- GCC_except_table6367
- GCC_except_table6373
- GCC_except_table6377
- GCC_except_table6380
- GCC_except_table6381
- GCC_except_table6383
- GCC_except_table6384
- GCC_except_table6386
- GCC_except_table6387
- GCC_except_table6390
- GCC_except_table6391
- GCC_except_table6392
- GCC_except_table6393
- GCC_except_table6394
- GCC_except_table6396
- GCC_except_table6397
- GCC_except_table6398
- GCC_except_table6400
- GCC_except_table6401
- GCC_except_table6402
- GCC_except_table6403
- GCC_except_table6404
- GCC_except_table6409
- GCC_except_table6414
- GCC_except_table6415
- GCC_except_table6416
- GCC_except_table6417
- GCC_except_table6418
- GCC_except_table6419
- GCC_except_table6420
- GCC_except_table6421
- GCC_except_table6422
- GCC_except_table6423
- GCC_except_table6424
- GCC_except_table6425
- GCC_except_table6426
- GCC_except_table6428
- GCC_except_table6442
- GCC_except_table6444
- GCC_except_table6446
- GCC_except_table6456
- GCC_except_table6469
- GCC_except_table6473
- GCC_except_table6485
- GCC_except_table6486
- GCC_except_table6640
- GCC_except_table7342
- GCC_except_table7343
- GCC_except_table7351
- GCC_except_table7353
- GCC_except_table7354
- GCC_except_table7356
- GCC_except_table7363
- GCC_except_table7367
- GCC_except_table7370
- GCC_except_table7371
- GCC_except_table7372
- GCC_except_table7373
- GCC_except_table7374
- GCC_except_table7376
- GCC_except_table7395
- GCC_except_table7397
- GCC_except_table7398
- GCC_except_table7400
- GCC_except_table7401
- GCC_except_table7404
- GCC_except_table7405
- GCC_except_table7406
- _AnalyticsSendEvent
- _FlatStorePageEntryWrite2.3344
- _MurmurHash3_x86_32.17114
- _NSHomeDirectory
- _OBJC_CLASS_$_NSDateFormatter
- _OBJC_CLASS_$_NSMutableString
- _OBJC_CLASS_$_NSProcessInfo
- _OBJC_IVAR_$_SIAnalytics._readHeartbeat
- _OBJC_IVAR_$_SIAnalytics._resourcesCallback
- _SIAnalyticsCopyData
- _SIAnalyticsHeartbeatRecordIndexOpen
- _SIAnalyticsHeartbeatSetTimestamp
- _SIAnalyticsIndexIncrementCounts
- _SIAnalyticsInitialize.onceToken
- _SIAnalyticsReportVectorIndexDrop
- _SIGetDirectorySize
- _SIGetIndexDirectorySize
- __PayloadWriteData.3878
- __ZGVZL12MetadataKeysvE13_metadataKeys.17062
- __ZGVZL17GenericFilterKeysvE18_genericFilterKeys.17081
- __ZGVZL18PhRetrievalAttribsvE17_retrievalAttribs.16780
- __ZGVZL25GenericFilterTopLevelKeysvE26_genericFilterTopLevelKeys.17073
- __ZGVZL26PhExactMatchRankingAttribsvE27_phExactMatchRankingAttribs.16963
- __ZL10commonHashjPKhj.16027
- __ZL11MAX_OIDINFO.16522
- __ZL11TOK_ID_FROM.4250
- __ZL12ZERO_OIDINFO.16521
- __ZL13PhAttribNodesPKcRKNSt3__113unordered_setINS1_12basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEENS1_4hashIS8_EENS1_8equal_toIS8_EENS6_IS8_EEEEbb.16823
- __ZL13v2_readVInt64PKhPm.8910
- __ZL13v2_readVInt64RPKhRmRy.9464
- __ZL14ZERO_FETCHINFO.5865
- __ZL14v2_writeVInt64Phmy.8904
- __ZL14v2_writeVInt64RPhy.9463
- __ZL16__message_assertPKcz.16001
- __ZL16__message_assertPKcz.16032
- __ZL16__message_assertPKcz.16544
- __ZL16__message_assertPKcz.4065
- __ZL16__message_assertPKcz.5623
- __ZL16__message_assertPKcz.5771
- __ZL16__message_assertPKcz.6138
- __ZL16__message_assertPKcz.8169
- __ZL16__message_assertPKcz.8919
- __ZL16si_analytics_logPKcz.8357
- __ZL17ZERO_RANKING_BITS.16467
- __ZL18PhRankingBoostTreev.16712
- __ZL18PhRetrievalAttribsv.16724
- __ZL18QueryParserLibraryv.10812
- __ZL18QueryParserLibraryv.13135
- __ZL18QueryParserLibraryv.16845
- __ZL18isGenericFilterKeyRKNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE.17067
- __ZL20PhRankingTreeFromStrPKcfPi.16695
- __ZL22__si_assert_copy_extraP6fd_obji.15997
- __ZL22__si_assert_copy_extraP6fd_obji.16028
- __ZL22__si_assert_copy_extraP6fd_obji.16540
- __ZL22__si_assert_copy_extraP6fd_obji.4061
- __ZL22__si_assert_copy_extraP6fd_obji.5619
- __ZL22__si_assert_copy_extraP6fd_obji.5766
- __ZL22__si_assert_copy_extraP6fd_obji.6134
- __ZL22__si_assert_copy_extraP6fd_obji.8164
- __ZL22__si_assert_copy_extraP6fd_obji.8914
- __ZL22getkQPQUOutputTokenKeyv.16801
- __ZL23audit_stringQueryParser.10824
- __ZL23audit_stringQueryParser.13145
- __ZL23audit_stringQueryParser.16857
- __ZL23store_stream_read_bytesP14store_stream_tPhm.8911
- __ZL24store_stream_write_bytesP14store_stream_tPKhm.8903
- __ZL25convertASTNodeToQueryNodeP9PRAstNodeP9PRContext.4207
- __ZL26PhExactMatchRankingAttribsv.16960
- __ZL26PhImpAttributesRankingNodePKc.16709
- __ZL26getkQPQUOutputTokenInfoKeyv.16684
- __ZL26isGenericFilterTopLevelKeyRKNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE.17069
- __ZL27_containsOnlyCharsInCharsetP8NSStringP14NSCharacterSet.16699
- __ZL27getkQPQUOutputTokenRangeKeyv.13148
- __ZL27getkQPQUOutputTokenRangeKeyv.16798
- __ZL28getkQPQUOutputTokenArgIdsKeyv.10860
- __ZL28getkQPQUOutputTokenArgIdsKeyv.13149
- __ZL28getkQPQUOutputTokenArgIdsKeyv.16799
- __ZL31getkQPQUOutputTokenArgScoresKeyv.13150
- __ZL31getkQPQUOutputTokenArgScoresKeyv.16800
- __ZL32PhImpAttributesPrefixRankingNodePKc.16708
- __ZL6sTotal.16462
- __ZL6sTotal.16642
- __ZL6sTotal.16751
- __ZL6sTotal.4223
- __ZL6sTotal.5616
- __ZL6sTotal.5772
- __ZL6sTotal.7540
- __ZL6sTotal.8601
- __ZL7Attribsv.4242
- __ZL9TOK_ID_TO.4255
- __ZL9intervals.8586
- __ZZL11CurrentYearvE8currYear.16934
- __ZZL11CurrentYearvE9onceToken.16933
- __ZZL12MetadataKeysvE13_metadataKeys.17063
- __ZZL12MetadataKeysvE9onceToken.17064
- __ZZL14PhThreeYearAgovE7oldYear.16937
- __ZZL14PhThreeYearAgovE9onceToken.16936
- __ZZL16utf8_byte_lengthhE14utf8_len_table.16584
- __ZZL17GenericFilterKeysvE18_genericFilterKeys.17082
- __ZZL17GenericFilterKeysvE9onceToken.17083
- __ZZL18PhRetrievalAttribsvE17_retrievalAttribs.16725
- __ZZL18PhRetrievalAttribsvE9onceToken.16781
- __ZZL18utf8_to_code_pointPKhE20utf8_first_char_mask.16585
- __ZZL22QueryParserLibraryCorePPcE16frameworkLibrary.0.10820
- __ZZL22QueryParserLibraryCorePPcE16frameworkLibrary.0.13141
- __ZZL22QueryParserLibraryCorePPcE16frameworkLibrary.0.16853
- __ZZL24utf8_byte_length_noerrorhE14utf8_len_table.16586
- __ZZL25GenericFilterTopLevelKeysvE26_genericFilterTopLevelKeys.17074
- __ZZL25GenericFilterTopLevelKeysvE9onceToken.17075
- __ZZL26PhExactMatchRankingAttribsvE27_phExactMatchRankingAttribs.16961
- __ZZL26PhExactMatchRankingAttribsvE9onceToken.16964
- __ZZL28NanoSecondsSinceAbsoluteTimeyE13sTimebaseInfo.16715
- __ZZL28NanoSecondsSinceAbsoluteTimeyE9onceToken.16714
- __ZZL31getkQPQUOutputTokenKeySymbolLocvE3ptr.0.10835
- __ZZL31getkQPQUOutputTokenKeySymbolLocvE3ptr.0.13151
- __ZZL31getkQPQUOutputTokenKeySymbolLocvE3ptr.0.16858
- __ZZL35getkQPQUOutputTokenInfoKeySymbolLocvE3ptr.0.17051
- __ZZL36getkQPParseAttributeDateKeySymbolLocvE3ptr.0.13296
- __ZZL36getkQPQUOutputTokenRangeKeySymbolLocvE3ptr.0.10869
- __ZZL36getkQPQUOutputTokenRangeKeySymbolLocvE3ptr.0.13163
- __ZZL36getkQPQUOutputTokenRangeKeySymbolLocvE3ptr.0.16870
- __ZZL37getkQPParseAttributeMediaKeySymbolLocvE3ptr.0.13275
- __ZZL37getkQPQUOutputTokenArgIdsKeySymbolLocvE3ptr.0.10861
- __ZZL37getkQPQUOutputTokenArgIdsKeySymbolLocvE3ptr.0.13159
- __ZZL37getkQPQUOutputTokenArgIdsKeySymbolLocvE3ptr.0.16866
- __ZZL38getkQPParseAttributeSenderKeySymbolLocvE3ptr.0.13283
- __ZZL38getkQPParseAttributeUnreadKeySymbolLocvE3ptr.0.13263
- __ZZL40getkQPQUOutputTokenArgScoresKeySymbolLocvE3ptr.0.13155
- __ZZL40getkQPQUOutputTokenArgScoresKeySymbolLocvE3ptr.0.16862
- __ZZL41getkQPParseAttributeDueActionKeySymbolLocvE3ptr.0.13202
- __ZZL41getkQPParseAttributeRecipientKeySymbolLocvE3ptr.0.13279
- __ZZL42getkQPParseAttributeAttachmentKeySymbolLocvE3ptr.0.13269
- __ZZL42getkQPParseAttributeJunkActionKeySymbolLocvE3ptr.0.13194
- __ZZL43getkQPParseAttributeDescriptionKeySymbolLocvE3ptr.0.13190
- __ZZL43getkQPParseAttributeDraftActionKeySymbolLocvE3ptr.0.13198
- __ZZL43getkQPParseAttributeHotelActionKeySymbolLocvE3ptr.0.13226
- __ZZL44getkQPParseAttributeFlightActionKeySymbolLocvE3ptr.0.13239
- __ZZL44getkQPParseAttributeLatestActionKeySymbolLocvE3ptr.0.13210
- __ZZL44getkQPParseAttributeTaggedPersonKeySymbolLocvE3ptr.0.13292
- __ZZL45getkQPParseAttributeArchiveActionKeySymbolLocvE3ptr.0.13186
- __ZZL45getkQPParseAttributePrintedActionKeySymbolLocvE3ptr.0.13245
- __ZZL46getkQPParseAttributeEarliestActionKeySymbolLocvE3ptr.0.13214
- __ZZL46getkQPParseAttributeGroundedPersonKeySymbolLocvE3ptr.0.13287
- __ZZL47getkQPParseAttributeCompletedActionKeySymbolLocvE3ptr.0.13206
- __ZZL48getkQPParseAttributeRestaurantActionKeySymbolLocvE3ptr.0.13220
- __ZZL53getkQPParseAttributeFlightArrivalLocationKeySymbolLocvE3ptr.0.13230
- __ZZL55getkQPParseAttributeFlightDepartureLocationKeySymbolLocvE3ptr.0.13234
- ___26+[SIAnalytics runCommand:]_block_invoke
- ___33+[SIAnalytics sendHeartbeatEvent]_block_invoke
- ___34+[SIAnalytics setSpotlightVersion]_block_invoke
- ___34-[SIAnalytics resetAfterHeartbeat]_block_invoke
- ___34-[SIAnalytics resetAfterHeartbeat]_block_invoke_2
- ___39-[SIAnalyticsIndexData updateWithData:]_block_invoke
- ___40+[SIAnalytics setPurgeability:forIndex:]_block_invoke
- ___49-[SIAnalytics createDropDataForIndex:path:error:]_block_invoke
- ___49-[SIAnalytics createDropDataForIndex:path:error:]_block_invoke_2
- ___49-[SIAnalytics createDropDataForIndex:path:error:]_block_invoke_3
- ___52-[SIAnalytics createHeartbeatDataWithRefresh:error:]_block_invoke
- ___52-[SIAnalytics createHeartbeatDataWithRefresh:error:]_block_invoke_2
- ___52-[SIAnalytics createHeartbeatDataWithRefresh:error:]_block_invoke_3
- ___52-[SIAnalytics createHeartbeatDataWithRefresh:error:]_block_invoke_4
- ___52-[SIAnalytics createHeartbeatDataWithRefresh:error:]_block_invoke_5
- ___59+[SIAnalytics recordRequestsForIndex:adds:updates:deletes:]_block_invoke
- ___66-[SIAnalyticsIndexData refreshHeartbeatDataWithIndex:path:errors:]_block_invoke
- ___71+[SIAnalytics sendIndexDropEventWithCorruptIndex:path:readOnly:reason:]_block_invoke
- ___Block_byref_object_copy_.10880
- ___Block_byref_object_copy_.13184
- ___Block_byref_object_copy_.13650
- ___Block_byref_object_copy_.16508
- ___Block_byref_object_copy_.2634
- ___Block_byref_object_copy_.7683
- ___Block_byref_object_dispose_.10881
- ___Block_byref_object_dispose_.13185
- ___Block_byref_object_dispose_.13651
- ___Block_byref_object_dispose_.16509
- ___Block_byref_object_dispose_.2635
- ___Block_byref_object_dispose_.7684
- ___SIAnalyticsHeartbeatRecordIndexOpen_block_invoke
- ___SIAnalyticsHeartbeatSetTimestamp_block_invoke
- ___SIAnalyticsInitialize_block_invoke
- ___SIAnalyticsReportVectorIndexDrop_block_invoke
- ____ZL11CurrentYearv_block_invoke.16950
- ____ZL12MetadataKeysv_block_invoke.17099
- ____ZL14PhThreeYearAgov_block_invoke.16947
- ____ZL17GenericFilterKeysv_block_invoke.17087
- ____ZL18PhRetrievalAttribsv_block_invoke.16783
- ____ZL19convertQPFilterNodeP17PRAstQPFilterNodeP9PRContext_block_invoke.4261
- ____ZL20PhRankingTreeFromStrPKcfPi_block_invoke.16953
- ____ZL22QueryParserLibraryCorePPc_block_invoke.10821
- ____ZL22QueryParserLibraryCorePPc_block_invoke.13142
- ____ZL22QueryParserLibraryCorePPc_block_invoke.16854
- ____ZL25GenericFilterTopLevelKeysv_block_invoke.17079
- ____ZL26PhExactMatchRankingAttribsv_block_invoke.16966
- ____ZL28NanoSecondsSinceAbsoluteTimey_block_invoke.16932
- ____ZL28PhPopulateAllFilterFromParseP18NSAttributedStringP14NSMutableArrayIP8NSStringEPS1_IP7NSValueES9_S9_S9__block_invoke.16688
- ____ZL29PhPopulateDateFilterFromParseP18NSAttributedStringP14NSMutableArrayIP8NSStringEPS1_IP7NSValueE_block_invoke.16794
- ____ZL30PhPopulateSomeFiltersFromParseP18NSAttributedStringP14NSMutableArrayIP8NSStringEPS1_IP7NSValueES5_S9__block_invoke.16791
- ____ZL31getkQPQUOutputTokenKeySymbolLocv_block_invoke.10836
- ____ZL31getkQPQUOutputTokenKeySymbolLocv_block_invoke.13152
- ____ZL31getkQPQUOutputTokenKeySymbolLocv_block_invoke.16859
- ____ZL35getkQPQUOutputTokenInfoKeySymbolLocv_block_invoke.17052
- ____ZL36getkQPParseAttributeDateKeySymbolLocv_block_invoke.13297
- ____ZL36getkQPQUOutputTokenRangeKeySymbolLocv_block_invoke.10870
- ____ZL36getkQPQUOutputTokenRangeKeySymbolLocv_block_invoke.13164
- ____ZL36getkQPQUOutputTokenRangeKeySymbolLocv_block_invoke.16871
- ____ZL37getkQPParseAttributeMediaKeySymbolLocv_block_invoke.13276
- ____ZL37getkQPQUOutputTokenArgIdsKeySymbolLocv_block_invoke.10862
- ____ZL37getkQPQUOutputTokenArgIdsKeySymbolLocv_block_invoke.13160
- ____ZL37getkQPQUOutputTokenArgIdsKeySymbolLocv_block_invoke.16867
- ____ZL38getkQPParseAttributeSenderKeySymbolLocv_block_invoke.13284
- ____ZL38getkQPParseAttributeUnreadKeySymbolLocv_block_invoke.13264
- ____ZL40getkQPQUOutputTokenArgScoresKeySymbolLocv_block_invoke.13156
- ____ZL40getkQPQUOutputTokenArgScoresKeySymbolLocv_block_invoke.16863
- ____ZL41getkQPParseAttributeDueActionKeySymbolLocv_block_invoke.13203
- ____ZL41getkQPParseAttributeRecipientKeySymbolLocv_block_invoke.13280
- ____ZL42getkQPParseAttributeAttachmentKeySymbolLocv_block_invoke.13270
- ____ZL42getkQPParseAttributeJunkActionKeySymbolLocv_block_invoke.13195
- ____ZL43getkQPParseAttributeDescriptionKeySymbolLocv_block_invoke.13191
- ____ZL43getkQPParseAttributeDraftActionKeySymbolLocv_block_invoke.13199
- ____ZL43getkQPParseAttributeHotelActionKeySymbolLocv_block_invoke.13227
- ____ZL44getkQPParseAttributeFlightActionKeySymbolLocv_block_invoke.13240
- ____ZL44getkQPParseAttributeLatestActionKeySymbolLocv_block_invoke.13211
- ____ZL44getkQPParseAttributeTaggedPersonKeySymbolLocv_block_invoke.13293
- ____ZL45getkQPParseAttributeArchiveActionKeySymbolLocv_block_invoke.13187
- ____ZL45getkQPParseAttributePrintedActionKeySymbolLocv_block_invoke.13246
- ____ZL46getkQPParseAttributeEarliestActionKeySymbolLocv_block_invoke.13215
- ____ZL46getkQPParseAttributeGroundedPersonKeySymbolLocv_block_invoke.13288
- ____ZL47getkQPParseAttributeCompletedActionKeySymbolLocv_block_invoke.13207
- ____ZL48getkQPParseAttributeRestaurantActionKeySymbolLocv_block_invoke.13221
- ____ZL53getkQPParseAttributeFlightArrivalLocationKeySymbolLocv_block_invoke.13231
- ____ZL55getkQPParseAttributeFlightDepartureLocationKeySymbolLocv_block_invoke.13235
- ___block_descriptor_32_e35_v32?0"NSString"8"NSNumber"16^B24l
- ___block_descriptor_32_e47_v32?0"NSString"8"SIAnalyticsIndexData"16^B24l
- ___block_descriptor_40_e8_32o_e35_v32?0"NSString"8"NSObject"16^B24ls32l8
- ___block_descriptor_41_e8_32o_e5_v8?0ls32l8
- ___block_descriptor_48_e8_32o40o_e35_v32?0"NSString"8"NSNumber"16^B24ls32l8s40l8
- ___block_descriptor_48_e8_32o40o_e35_v32?0"NSString"8"NSObject"16^B24ls32l8s40l8
- ___block_descriptor_48_e8_32o40o_e39_v32?0"NSString"8"NSDictionary"16^B24ls32l8s40l8
- ___block_descriptor_48_e8_32o40o_e5_v8?0ls32l8s40l8
- ___block_descriptor_48_e8_32o40r_e5_v8?0lr40l8s32l8
- ___block_descriptor_48_e8_32o_e35_v32?0"NSString"8"NSObject"16^B24ls32l8
- ___block_descriptor_49_e8_32o_e5_v8?0ls32l8
- ___block_descriptor_56_e8_32o40o_e35_v32?0"NSString"8"NSObject"16^B24ls32l8s40l8
- ___block_descriptor_57_e8_32o40o48o_e5_v8?0ls32l8s40l8s48l8
- ___block_descriptor_57_e8_32o40o_e47_v32?0"NSString"8"SIAnalyticsIndexData"16^B24ls32l8s40l8
- ___block_descriptor_64_e8_32o_e5_v8?0ls32l8
- ___block_descriptor_65_e8_32o40o_e5_v8?0ls32l8s40l8
- ___block_descriptor_tmp.1.5646
- ___block_descriptor_tmp.10.14480
- ___block_descriptor_tmp.10.15666
- ___block_descriptor_tmp.1084.8411
- ___block_descriptor_tmp.1095.8211
- ___block_descriptor_tmp.11.16053
- ___block_descriptor_tmp.11.9055
- ___block_descriptor_tmp.1100.8218
- ___block_descriptor_tmp.111.15569
- ___block_descriptor_tmp.111.6273
- ___block_descriptor_tmp.11261
- ___block_descriptor_tmp.113.8354
- ___block_descriptor_tmp.11355
- ___block_descriptor_tmp.11482
- ___block_descriptor_tmp.11567
- ___block_descriptor_tmp.116
- ___block_descriptor_tmp.117.15842
- ___block_descriptor_tmp.117.5876
- ___block_descriptor_tmp.117.9917
- ___block_descriptor_tmp.118.3738
- ___block_descriptor_tmp.118.5877
- ___block_descriptor_tmp.12.11385
- ___block_descriptor_tmp.12.15687
- ___block_descriptor_tmp.12.16339
- ___block_descriptor_tmp.12.16557
- ___block_descriptor_tmp.12.4481
- ___block_descriptor_tmp.12.6124
- ___block_descriptor_tmp.12.8485
- ___block_descriptor_tmp.12.9067
- ___block_descriptor_tmp.12080
- ___block_descriptor_tmp.121.15841
- ___block_descriptor_tmp.1215.8311
- ___block_descriptor_tmp.123.15620
- ___block_descriptor_tmp.123.8358
- ___block_descriptor_tmp.123.9154
- ___block_descriptor_tmp.1243.8407
- ___block_descriptor_tmp.126.8359
- ___block_descriptor_tmp.128.14924
- ___block_descriptor_tmp.13.15693
- ___block_descriptor_tmp.13.16558
- ___block_descriptor_tmp.13.4476
- ___block_descriptor_tmp.13.5572
- ___block_descriptor_tmp.13.5651
- ___block_descriptor_tmp.13.6546
- ___block_descriptor_tmp.13.9068
- ___block_descriptor_tmp.13.9156
- ___block_descriptor_tmp.13075
- ___block_descriptor_tmp.13384
- ___block_descriptor_tmp.136.5882
- ___block_descriptor_tmp.138.5983
- ___block_descriptor_tmp.13944
- ___block_descriptor_tmp.14.5134
- ___block_descriptor_tmp.14154
- ___block_descriptor_tmp.14366
- ___block_descriptor_tmp.14469
- ___block_descriptor_tmp.146.15051
- ___block_descriptor_tmp.14652
- ___block_descriptor_tmp.1473.8342
- ___block_descriptor_tmp.14867
- ___block_descriptor_tmp.14958
- ___block_descriptor_tmp.15.5652
- ___block_descriptor_tmp.151.10190
- ___block_descriptor_tmp.154.8438
- ___block_descriptor_tmp.155.15069
- ___block_descriptor_tmp.156.8446
- ___block_descriptor_tmp.15660
- ___block_descriptor_tmp.157.8449
- ___block_descriptor_tmp.159.15261
- ___block_descriptor_tmp.16.11391
- ___block_descriptor_tmp.16.5135
- ___block_descriptor_tmp.16.8086
- ___block_descriptor_tmp.160.14981
- ___block_descriptor_tmp.160.8178
- ___block_descriptor_tmp.16010
- ___block_descriptor_tmp.16022
- ___block_descriptor_tmp.161.15116
- ___block_descriptor_tmp.16287
- ___block_descriptor_tmp.16480
- ___block_descriptor_tmp.167.15874
- ___block_descriptor_tmp.168.15875
- ___block_descriptor_tmp.17.13400
- ___block_descriptor_tmp.17.7180
- ___block_descriptor_tmp.170.10263
- ___block_descriptor_tmp.170.15872
- ___block_descriptor_tmp.172.15731
- ___block_descriptor_tmp.172.6231
- ___block_descriptor_tmp.18.14955
- ___block_descriptor_tmp.18.9175
- ___block_descriptor_tmp.187.15484
- ___block_descriptor_tmp.19.10397
- ___block_descriptor_tmp.19.13403
- ___block_descriptor_tmp.19.15733
- ___block_descriptor_tmp.19.2700
- ___block_descriptor_tmp.2.16552
- ___block_descriptor_tmp.2.5574
- ___block_descriptor_tmp.2.5647
- ___block_descriptor_tmp.2.5788
- ___block_descriptor_tmp.2.8099
- ___block_descriptor_tmp.2.9475
- ___block_descriptor_tmp.20.13014
- ___block_descriptor_tmp.20.16580
- ___block_descriptor_tmp.20.4295
- ___block_descriptor_tmp.21.11423
- ___block_descriptor_tmp.21.11912
- ___block_descriptor_tmp.22.13938
- ___block_descriptor_tmp.22.14952
- ___block_descriptor_tmp.23.15729
- ___block_descriptor_tmp.23.4317
- ___block_descriptor_tmp.23.9200
- ___block_descriptor_tmp.24.3619
- ___block_descriptor_tmp.24.4316
- ___block_descriptor_tmp.25.11427
- ___block_descriptor_tmp.25.11921
- ___block_descriptor_tmp.25.16409
- ___block_descriptor_tmp.26.13407
- ___block_descriptor_tmp.26.15158
- ___block_descriptor_tmp.26.15763
- ___block_descriptor_tmp.26.16410
- ___block_descriptor_tmp.26.6586
- ___block_descriptor_tmp.27.15768
- ___block_descriptor_tmp.27.5842
- ___block_descriptor_tmp.2711
- ___block_descriptor_tmp.28.10386
- ___block_descriptor_tmp.28.13409
- ___block_descriptor_tmp.28.15769
- ___block_descriptor_tmp.28.4322
- ___block_descriptor_tmp.28.6618
- ___block_descriptor_tmp.28.8741
- ___block_descriptor_tmp.2873
- ___block_descriptor_tmp.29.11926
- ___block_descriptor_tmp.29.4321
- ___block_descriptor_tmp.29.7885
- ___block_descriptor_tmp.3.16290
- ___block_descriptor_tmp.3.9481
- ___block_descriptor_tmp.30.11929
- ___block_descriptor_tmp.30.15152
- ___block_descriptor_tmp.30.15806
- ___block_descriptor_tmp.30.16302
- ___block_descriptor_tmp.31.14423
- ___block_descriptor_tmp.31.5131
- ___block_descriptor_tmp.31.8106
- ___block_descriptor_tmp.3101
- ___block_descriptor_tmp.32.4886
- ___block_descriptor_tmp.33.13392
- ___block_descriptor_tmp.33.14424
- ___block_descriptor_tmp.33.15150
- ___block_descriptor_tmp.33.15804
- ___block_descriptor_tmp.33.4325
- ___block_descriptor_tmp.33.4649
- ___block_descriptor_tmp.34.14425
- ___block_descriptor_tmp.34.16304
- ___block_descriptor_tmp.34.4324
- ___block_descriptor_tmp.35.5126
- ___block_descriptor_tmp.35.8110
- ___block_descriptor_tmp.3546
- ___block_descriptor_tmp.36.15148
- ___block_descriptor_tmp.36.15814
- ___block_descriptor_tmp.37.15822
- ___block_descriptor_tmp.39.14430
- ___block_descriptor_tmp.39.15146
- ___block_descriptor_tmp.3905
- ___block_descriptor_tmp.4.16294
- ___block_descriptor_tmp.4.5636
- ___block_descriptor_tmp.4.5789
- ___block_descriptor_tmp.4.9484
- ___block_descriptor_tmp.40.15820
- ___block_descriptor_tmp.40.2712
- ___block_descriptor_tmp.41.5143
- ___block_descriptor_tmp.411.10118
- ___block_descriptor_tmp.4124
- ___block_descriptor_tmp.42.13424
- ___block_descriptor_tmp.42.15143
- ___block_descriptor_tmp.4298
- ___block_descriptor_tmp.4474
- ___block_descriptor_tmp.45.2731
- ___block_descriptor_tmp.4508
- ___block_descriptor_tmp.46.13419
- ___block_descriptor_tmp.47.15834
- ___block_descriptor_tmp.4711
- ___block_descriptor_tmp.4747
- ___block_descriptor_tmp.48.13422
- ___block_descriptor_tmp.48.15233
- ___block_descriptor_tmp.48.15835
- ___block_descriptor_tmp.48.9569
- ___block_descriptor_tmp.49.15838
- ___block_descriptor_tmp.5.8100
- ___block_descriptor_tmp.5076
- ___block_descriptor_tmp.51.14441
- ___block_descriptor_tmp.51.15231
- ___block_descriptor_tmp.51.8007
- ___block_descriptor_tmp.51.9566
- ___block_descriptor_tmp.5112
- ___block_descriptor_tmp.52.13427
- ___block_descriptor_tmp.52.2740
- ___block_descriptor_tmp.52.7377
- ___block_descriptor_tmp.52.9260
- ___block_descriptor_tmp.53.14442
- ___block_descriptor_tmp.5352
- ___block_descriptor_tmp.54.15229
- ___block_descriptor_tmp.54.8014
- ___block_descriptor_tmp.55.14427
- ___block_descriptor_tmp.5506
- ___block_descriptor_tmp.5550
- ___block_descriptor_tmp.56.8008
- ___block_descriptor_tmp.5635
- ___block_descriptor_tmp.57.13438
- ___block_descriptor_tmp.57.14428
- ___block_descriptor_tmp.57.5946
- ___block_descriptor_tmp.5787
- ___block_descriptor_tmp.58.3016
- ___block_descriptor_tmp.58.5947
- ___block_descriptor_tmp.59.15210
- ___block_descriptor_tmp.59.2742
- ___block_descriptor_tmp.6.16510
- ___block_descriptor_tmp.6.4472
- ___block_descriptor_tmp.6.4515
- ___block_descriptor_tmp.6.5069
- ___block_descriptor_tmp.6.5638
- ___block_descriptor_tmp.6.5794
- ___block_descriptor_tmp.60.16523
- ___block_descriptor_tmp.60.5948
- ___block_descriptor_tmp.6075
- ___block_descriptor_tmp.62.14048
- ___block_descriptor_tmp.63.15860
- ___block_descriptor_tmp.64.14476
- ___block_descriptor_tmp.6463
- ___block_descriptor_tmp.65.15963
- ___block_descriptor_tmp.65.3784
- ___block_descriptor_tmp.65.4552
- ___block_descriptor_tmp.65.9334
- ___block_descriptor_tmp.6540
- ___block_descriptor_tmp.655.8415
- ___block_descriptor_tmp.66.14047
- ___block_descriptor_tmp.66.5911
- ___block_descriptor_tmp.6709
- ___block_descriptor_tmp.68.5914
- ___block_descriptor_tmp.68.9332
- ___block_descriptor_tmp.7.11378
- ___block_descriptor_tmp.7.4122
- ___block_descriptor_tmp.7.4512
- ___block_descriptor_tmp.7.5071
- ___block_descriptor_tmp.7.5791
- ___block_descriptor_tmp.70.14110
- ___block_descriptor_tmp.7148
- ___block_descriptor_tmp.72.5915
- ___block_descriptor_tmp.7248
- ___block_descriptor_tmp.73.3802
- ___block_descriptor_tmp.74.6274
- ___block_descriptor_tmp.76.15986
- ___block_descriptor_tmp.76.7937
- ___block_descriptor_tmp.77.15257
- ___block_descriptor_tmp.77.15989
- ___block_descriptor_tmp.7782
- ___block_descriptor_tmp.7827
- ___block_descriptor_tmp.8.12070
- ___block_descriptor_tmp.8.16002
- ___block_descriptor_tmp.8.4186
- ___block_descriptor_tmp.8.8146
- ___block_descriptor_tmp.80.6275
- ___block_descriptor_tmp.8072
- ___block_descriptor_tmp.8136
- ___block_descriptor_tmp.8157
- ___block_descriptor_tmp.83.14136
- ___block_descriptor_tmp.84.9351
- ___block_descriptor_tmp.8692
- ___block_descriptor_tmp.874.8341
- ___block_descriptor_tmp.8754
- ___block_descriptor_tmp.9.14686
- ___block_descriptor_tmp.9.5578
- ___block_descriptor_tmp.9.5848
- ___block_descriptor_tmp.9.8429
- ___block_descriptor_tmp.9054
- ___block_descriptor_tmp.908.8414
- ___block_descriptor_tmp.9151
- ___block_descriptor_tmp.9471
- ___block_descriptor_tmp.9527
- ___block_descriptor_tmp.96.15504
- ___block_descriptor_tmp.972.8412
- ___block_descriptor_tmp.9759
- ___block_descriptor_tmp.986.8413
- ___block_literal_global.10393
- ___block_literal_global.10882
- ___block_literal_global.11.14680
- ___block_literal_global.1102.8212
- ___block_literal_global.11259
- ___block_literal_global.11353
- ___block_literal_global.11480
- ___block_literal_global.117.17013
- ___block_literal_global.120.3736
- ___block_literal_global.12078
- ___block_literal_global.12102
- ___block_literal_global.125.4882
- ___block_literal_global.125.9150
- ___block_literal_global.13073
- ___block_literal_global.13388
- ___block_literal_global.13936
- ___block_literal_global.14.11383
- ___block_literal_global.14.16335
- ___block_literal_global.14152
- ___block_literal_global.14364
- ___block_literal_global.14650
- ___block_literal_global.14948
- ___block_literal_global.15.15691
- ___block_literal_global.15.5561
- ___block_literal_global.15.6544
- ___block_literal_global.15685
- ___block_literal_global.16.6690
- ___block_literal_global.16008
- ___block_literal_global.16020
- ___block_literal_global.16288
- ___block_literal_global.16537
- ___block_literal_global.16659
- ___block_literal_global.17065
- ___block_literal_global.18.11389
- ___block_literal_global.18.8084
- ___block_literal_global.20.14949
- ___block_literal_global.21.13401
- ___block_literal_global.21.15726
- ___block_literal_global.22.16578
- ___block_literal_global.23.11421
- ___block_literal_global.25.15727
- ___block_literal_global.26.4314
- ___block_literal_global.2644
- ___block_literal_global.27.11425
- ___block_literal_global.2709
- ___block_literal_global.2871
- ___block_literal_global.29.5809
- ___block_literal_global.3014
- ___block_literal_global.31.4319
- ___block_literal_global.32.15136
- ___block_literal_global.32.15801
- ___block_literal_global.32.16299
- ___block_literal_global.32.17084
- ___block_literal_global.33.5123
- ___block_literal_global.33.8104
- ___block_literal_global.35.13389
- ___block_literal_global.35.15137
- ___block_literal_global.35.15802
- ___block_literal_global.35.4610
- ___block_literal_global.3648
- ___block_literal_global.37.5124
- ___block_literal_global.37.8108
- ___block_literal_global.38.15138
- ___block_literal_global.39.15817
- ___block_literal_global.4.5556
- ___block_literal_global.4.8097
- ___block_literal_global.4025
- ___block_literal_global.41.15139
- ___block_literal_global.4184
- ___block_literal_global.42.15818
- ___block_literal_global.4247
- ___block_literal_global.4293
- ___block_literal_global.43.5140
- ___block_literal_global.44.15140
- ___block_literal_global.4478
- ___block_literal_global.4509
- ___block_literal_global.462
- ___block_literal_global.464
- ___block_literal_global.4726
- ___block_literal_global.50.15186
- ___block_literal_global.50.9554
- ___block_literal_global.508
- ___block_literal_global.51.13426
- ___block_literal_global.51.15836
- ___block_literal_global.5110
- ___block_literal_global.53.15187
- ___block_literal_global.53.9555
- ___block_literal_global.5504
- ___block_literal_global.5548
- ___block_literal_global.5790
- ___block_literal_global.6.16292
- ___block_literal_global.6073
- ___block_literal_global.6461
- ___block_literal_global.65.17076
- ___block_literal_global.6538
- ___block_literal_global.6674
- ___block_literal_global.67.15922
- ___block_literal_global.67.9331
- ___block_literal_global.7172
- ___block_literal_global.7388
- ___block_literal_global.770
- ___block_literal_global.8070
- ___block_literal_global.8155
- ___block_literal_global.8690
- ___block_literal_global.8703
- ___block_literal_global.9.11376
- ___block_literal_global.9.4510
- ___block_literal_global.9198
- ___block_literal_global.94.7757
- ___block_literal_global.9506
- ___block_literal_global.9757
- ___block_literal_global.98.15502
- ___isAppleInternalInstall_block_invoke.13439
- ___message_assert.11503
- ___message_assert.11739
- ___message_assert.12069
- ___message_assert.12952
- ___message_assert.12997
- ___message_assert.13055
- ___message_assert.13465
- ___message_assert.13754
- ___message_assert.13813
- ___message_assert.13873
- ___message_assert.13932
- ___message_assert.14381
- ___message_assert.14513
- ___message_assert.14661
- ___message_assert.14889
- ___message_assert.15650
- ___message_assert.16077
- ___message_assert.16314
- ___message_assert.17369
- ___message_assert.2896
- ___message_assert.3115
- ___message_assert.3136
- ___message_assert.3316
- ___message_assert.3419
- ___message_assert.3865
- ___message_assert.3926
- ___message_assert.4090
- ___message_assert.4274
- ___message_assert.4288
- ___message_assert.4348
- ___message_assert.4507
- ___message_assert.4691
- ___message_assert.4720
- ___message_assert.5108
- ___message_assert.6081
- ___message_assert.6423
- ___message_assert.6509
- ___message_assert.6728
- ___message_assert.7144
- ___message_assert.7237
- ___message_assert.7803
- ___message_assert.7834
- ___message_assert.8040
- ___message_assert.8628
- ___message_assert.8653
- ___message_assert.8713
- ___message_assert.8954
- ___message_assert.9093
- ___message_assert.9126
- ___message_assert.9551
- ___message_assert.9789
- ___path_bundle_index_block_invoke.10399
- ___si_assert_copy_extra.11737
- ___si_assert_copy_extra.12065
- ___si_assert_copy_extra.12947
- ___si_assert_copy_extra.12992
- ___si_assert_copy_extra.13051
- ___si_assert_copy_extra.13461
- ___si_assert_copy_extra.13750
- ___si_assert_copy_extra.13809
- ___si_assert_copy_extra.13868
- ___si_assert_copy_extra.13927
- ___si_assert_copy_extra.14376
- ___si_assert_copy_extra.14508
- ___si_assert_copy_extra.14656
- ___si_assert_copy_extra.14884
- ___si_assert_copy_extra.15646
- ___si_assert_copy_extra.16073
- ___si_assert_copy_extra.16309
- ___si_assert_copy_extra.17304
- ___si_assert_copy_extra.2891
- ___si_assert_copy_extra.3111
- ___si_assert_copy_extra.3132
- ___si_assert_copy_extra.3311
- ___si_assert_copy_extra.3414
- ___si_assert_copy_extra.3861
- ___si_assert_copy_extra.3922
- ___si_assert_copy_extra.4085
- ___si_assert_copy_extra.4270
- ___si_assert_copy_extra.4284
- ___si_assert_copy_extra.4343
- ___si_assert_copy_extra.4502
- ___si_assert_copy_extra.4687
- ___si_assert_copy_extra.4715
- ___si_assert_copy_extra.5103
- ___si_assert_copy_extra.6077
- ___si_assert_copy_extra.6418
- ___si_assert_copy_extra.6504
- ___si_assert_copy_extra.6724
- ___si_assert_copy_extra.7140
- ___si_assert_copy_extra.7233
- ___si_assert_copy_extra.7799
- ___si_assert_copy_extra.7829
- ___si_assert_copy_extra.8036
- ___si_assert_copy_extra.8625
- ___si_assert_copy_extra.8648
- ___si_assert_copy_extra.8708
- ___si_assert_copy_extra.8949
- ___si_assert_copy_extra.9088
- ___si_assert_copy_extra.9121
- ___si_assert_copy_extra.9547
- ___si_assert_copy_extra.9784
- __psid_insert.5183
- _bit_vector_create.16267
- _bit_vector_create.17401
- _bit_vector_init.4825
- _bit_vector_internal_touch_for_set.4860
- _bit_vector_set.13847
- _bit_vector_set.16211
- _bit_vector_set.17365
- _bit_vector_set.2949
- _bit_vector_set.3577
- _bit_vector_set.4411
- _bit_vector_set.5002
- _bit_vector_set.7345
- _bit_vector_set_bits.4867
- _checkNearness.14497
- _commonHash.11992
- _commonHash.17303
- _data_entry_store.17273
- _dirfd
- _emitTerms.7909
- _gAnalytics
- _gAnalyticsQueue
- _getLegacyPCEnum
- _getPrefixForPCPriority
- _getPrefixForProtectionClass
- _getPrefixForShorthand
- _getSize.memSize.12063
- _getSize.memSize.13942
- _getSize.memSize.4731
- _get_string_and_length_for_id.15332
- _hash64.8000
- _index_comp.12077
- _index_comp.13948
- _index_comp.4736
- _isAppleInternalInstall.isInternalInstall.13434
- _isAppleInternalInstall.onceToken.13433
- _keycompare.5168
- _localizedFieldTermMatch.14446
- _log_map_access_error.16134
- _log_map_access_error.17246
- _log_map_access_error.7293
- _master_fid_rec.5152
- _master_fid_rec_size.5154
- _objc_msgSend$appendFormat:
- _objc_msgSend$copyHeartbeatData
- _objc_msgSend$createDropDataForIndex:path:error:
- _objc_msgSend$createHeartbeatDataWithRefresh:error:
- _objc_msgSend$description
- _objc_msgSend$errorWithDomain:code:userInfo:
- _objc_msgSend$eventCount
- _objc_msgSend$getCurrentSpotlightVersionWithRoots:
- _objc_msgSend$getIndexDataForPrefix:
- _objc_msgSend$getPreviousBuild
- _objc_msgSend$hasSpotlightRoots
- _objc_msgSend$initWithBool:
- _objc_msgSend$initWithCString:encoding:
- _objc_msgSend$initWithFormat:
- _objc_msgSend$initWithLong:
- _objc_msgSend$initWithPrefix:
- _objc_msgSend$initWithSuiteName:
- _objc_msgSend$initWithUnsignedInt:
- _objc_msgSend$initWithUnsignedLongLong:
- _objc_msgSend$initializeSharedHearbeatFields
- _objc_msgSend$isHeartbeatReportingDisabled
- _objc_msgSend$isIndexDropReportingDisabled
- _objc_msgSend$migrateFromLegacyHeartbeatData:
- _objc_msgSend$populateIndexDropData:forIndex:reason:error:
- _objc_msgSend$processInfo
- _objc_msgSend$processName
- _objc_msgSend$readFromHeartbeatFileWithError:
- _objc_msgSend$recordDrop:
- _objc_msgSend$recordOpen:dirty:
- _objc_msgSend$recordOpen:forIndex:dirty:
- _objc_msgSend$recordRequestedAdds:updates:deletes:
- _objc_msgSend$recordRequestsForIndex:adds:updates:deletes:
- _objc_msgSend$refreshHeartbeatDataWithIndex:path:errors:
- _objc_msgSend$refreshSharedHeartbeatFieldsWithError:
- _objc_msgSend$removeItemAtPath:error:
- _objc_msgSend$removeObjectForKey:
- _objc_msgSend$resetAfterHeartbeat
- _objc_msgSend$runCommand:
- _objc_msgSend$sendHeartbeatEvent
- _objc_msgSend$sendHeartbeatEventWithData:withReset:
- _objc_msgSend$sendIndexDropEventWithCorruptIndex:path:readOnly:reason:
- _objc_msgSend$sendIndexDropEventWithData:
- _objc_msgSend$sendLegacyHeartbeatEventWithData:
- _objc_msgSend$sendLegacyIndexDropEventWithData:readOnly:prefix:
- _objc_msgSend$sendVectorIndexDropForIndex:vectorCount:readOnly:prefix:propertyName:dropReason:
- _objc_msgSend$setDateFormat:
- _objc_msgSend$setHeartbeatTimestampForPrefix:key:
- _objc_msgSend$setPurgeability:
- _objc_msgSend$setPurgeability:forIndex:
- _objc_msgSend$setSpotlightVersion
- _objc_msgSend$setTimestampForKey:
- _objc_msgSend$sharedInstance
- _objc_msgSend$shouldReportIndexDrop:
- _objc_msgSend$stringFromDate:
- _objc_msgSend$timeIntervalSince1970
- _objc_msgSend$unsignedLongLongValue
- _objc_msgSend$updateWithData:
- _objc_msgSend$usageInfoForCommand:
- _objc_msgSend$writeToHeartbeatFileWithError:
- _objc_release
- _objc_release_x19
- _objc_release_x23
- _oqpush.13971
- _oqpush.3471
- _oqpush.4750
- _packingCount.14116
- _path_bundle_index.sDummyFD.10394
- _pqDisposeApplier.7904
- _psid_lookup.5181
- _qsort_cached_allocations.12061
- _qsort_cached_allocations.13940
- _qsort_cached_allocations.4729
- _query_realloc.9098
- _readCompactPosition.14120
- _remapping_keys.12042
- _restoreVInt32.12971
- _restoreVInt32.3535
- _restoreVInt32.4097
- _sDataMapExceptionCallbacks.16088
- _sDataMapExceptionCallbacks.17221
- _sRefs
- _sRefsLock
- _sSpotlightVersion.7126
- _sTotal.13995
- _sTotal.14375
- _sTotal.14858
- _sTotal.15643
- _sTotal.4706
- _sTotal.5109
- _sTotal.6095
- _sTotal.6498
- _sTotal.9103
- _sTotal.9546
- _sTotal.9721
- _sendIndexDropEventWithCorruptIndex:path:readOnly:reason:.spid
- _setBool
- _setLong
- _setSpotlightVersion.onceToken
- _setString
- _setUInt32
- _setUInt64
- _si_analytics_log.14674
- _si_analytics_log.15073
- _si_analytics_log.16126
- _si_analytics_log.17307
- _si_analytics_log.2935
- _si_analytics_log.3319
- _si_analytics_log.3805
- _si_analytics_log.3887
- _si_analytics_log.4416
- _si_analytics_log.4936
- _si_analytics_log.6429
- _si_analytics_log.7288
- _si_analytics_log.7863
- _si_analytics_log.8829
- _si_analytics_log.9166
- _si_rwlock_wrunlock.3758
- _storeVInt64.13828
- _storeVInt64.4365
- _store_stream_read_bytes.13915
- _store_stream_read_bytes.3576
- _store_stream_read_bytes.4561
- _store_stream_read_bytes.5053
- _store_stream_read_bytes.7052
- _store_stream_read_vint32.13911
- _store_stream_read_vint32.3573
- _store_stream_read_vint32.4559
- _store_stream_read_vint32.7048
- _store_stream_write_bytes.13921
- _store_stream_write_bytes.3447
- _store_stream_write_bytes.4549
- _store_stream_write_bytes.5057
- _store_stream_write_bytes.7040
- _store_stream_write_vint32.13918
- _store_stream_write_vint32.3449
- _store_stream_write_vint32.4550
- _store_stream_write_vint32.7041
- _strHash.17595
- _sysctlbyname
- _table_extra_bytes.14940
- _takeBuddyPage.4402
- _termPropertyID.14447
- _thread_count.12062
- _thread_count.13941
- _thread_count.4730
- _timeSinceBoot
- _v2_readVInt32.4577
- _v2_readVInt64.11569
- _v2_readVInt64.14108
- _v2_readVInt64.14492
- _v2_readVInt64.14534
- _v2_readVInt64.3056
- _v2_readVInt64.3375
- _v2_readVInt64.4572
- _v2_readVInt64.7984
- _v2_writeVInt64.11526
- _v2_writeVInt64.13923
- _v2_writeVInt64.3345
- _vector_dimension.vec_sizes.15735
- _vector_size.elem_sizes.15734
- _writeVInt64.13920
- _writeVInt64.14547
- _writeVInt64.3889
- _writeVInt64.4551
- _writeVInt64.4823
- _writeVInt64.6426
CStrings:
+ "%s:%d: %@ is not a counter field"
+ "%s:%d: %@ is not a timestamp field"
+ "%s:%d: ARC disabled in SIAnalytics"
+ "%s:%d: No index"
+ "%s:%d: Skipping updating resources fields since callback has not been set"
+ "-[SIAnalytics incrementPerIndexHeartbeatCount:forKey:withError:]"
+ "-[SIAnalytics initWithParentDirectoryPath:corespotlight:heartbeatIndex:]"
+ "-[SIAnalytics refreshPerIndexHeartbeatFieldsForIndex:protectionClass:withError:]"
+ "-[SIAnalytics setPerIndexHeartbeatTimestamp:forKey:withError:]"
+ "-[SIAnalytics setSharedHeartbeatTimestamp:forKey:withError:]"
+ "2400.14.100"
+ "9999.99.99"
+ "@24@0:8^@16"
+ "@32@0:8@16B24B28"
+ "@32@0:8@16^@24"
+ "B40@0:8^{__SI=Q{SIFileOps=^?^?^?}{SIGuardedFd=iQ}isII^{SIWatchDog}^{__CFDictionary}{_opaque_pthread_rwlock_t=q[192c]}{si_missing_oids_s={os_unfair_lock_s=I}^{__RLEOIDArray}^{__RLEOIDArray}}{si_missing_oids_s={os_unfair_lock_s=I}^{__RLEOIDArray}^{__RLEOIDArray}}{os_unfair_lock_s=I}{si_comm_dates_s=^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}}{si_comm_dates_s=^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}}{si_comm_dates_s=^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}}{si_comm_dates_s=^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}}{si_comm_dates_s=^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}}^{__CFDictionary}^{_MDPlistContainer}Bi[18^{si_scheduler_token_s}]iI[4@]{?=[18^{_si_work_scheduler}][21^{_si_workqueue}]^{si_workqueue_list_s}}@^{datastore_info}{CIMetaInfo=i^{fd_obj}iQIIIIIIIIqqiiBI}^{DocStore}QQ{_opaque_pthread_mutex_t=q[56c]}^{ContentIndexList}^{ContentIndexList}iII^{_SI_PersistentIDStore}{__SIStoreToken={?=CCCCCCCCCCCCCCCC}^{__CFUUID}}ACAII{os_unfair_lock_s=I}ddBiI^{__CFDictionary}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{os_unfair_lock_s=I}^{__CFBag}{_opaque_pthread_mutex_t=q[56c]}^{__CFSet}^{__CFDictionary}Q^{__CFBag}^{__CFDictionary}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_cond_t=q[40c]}iIIIIIIIIIIIIIIIIIIIBBAq^{__CFDictionary}^{__CFBitVector}^{si_mobile_journal}^{si_mobile_journal}^{si_mobile_journal}AqAqAqd^?^vdd{?=^{fd_obj}IIIq{os_unfair_lock_s=I}BB}III^{FinderDateFields}{_opaque_pthread_mutex_t=q[56c]}^{fd_obj}^{fd_obj}^{fd_obj}iii^{_SIIndexCallbacks}^{__CFArray}^{__CFArray}qqqQIIiiBBBBBBBABB^{si_scheduler_token_s}BBBBBQq[4096c]{os_unfair_lock_s=I}{os_unfair_lock_s=I}b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b2b1^i^{__CFSet}^{__CFDictionary}^{__SIUINT64Set}^{ReverseDirStore_s}^{FileTree_Overlay_s}^{__CFSet}^{TermUpdateSet}{_opaque_pthread_rwlock_t=q[192c]}[16C]Bi^{datastore_info}AIBB[5i]*iI^vB^{fd_obj}iiii{AccumulatedCounts_s={_opaque_pthread_mutex_t=q[56c]}[256q][256I]}BB}16@24^@32"
+ "B40@0:8d16@24^@32"
+ "B40@0:8q16@24^@32"
+ "Build: %@"
+ "Got index directory birthtime %ld"
+ "Initializing shared heartbeat fields"
+ "Q24@0:8@16"
+ "Read from heartbeat file"
+ "Set SpotlightResources callback"
+ "Spotlight roots are installed!"
+ "Spotlight version changed %@ -> %s"
+ "Spotlight-%s"
+ "SpotlightResources config: (%@, %@, %@)"
+ "Volume property flags: 0x%llx"
+ "Wrote to heartbeat file"
+ "age_"
+ "droppedIndexDataWithError:"
+ "heartbeatAnalyticsDataWithReset:error:"
+ "heartbeatData"
+ "incrementCount:forKey:"
+ "incrementPerIndexHeartbeatCount:forKey:withError:"
+ "index init:%@"
+ "indexDropAnalyticsDataFromDroppedIndexData:withError:"
+ "indexDropType:"
+ "init:%@, cs:%d, hb:%d"
+ "initWithDomain:code:userInfo:"
+ "initWithParentDirectoryPath:corespotlight:heartbeatIndex:"
+ "initWithPrefix:data:"
+ "numberWithDouble:"
+ "prefixForPCPriority"
+ "prefixForProtectionClass"
+ "refreshPerIndexHeartbeatFieldsForIndex:protectionClass:withError:"
+ "setPerIndexHeartbeatTimestamp:forKey:withError:"
+ "setResourcesCallback:"
+ "setSharedHeartbeatTimestamp:forKey:withError:"
+ "setTimestamp:forKey:"
+ "statfs: (%s, flags:0x%x, blockSize:0x%llx, blocks:0x%llx, free:0x%llx)"
+ "time_since_"
+ "v24@0:8@?16"
+ "v32@0:8d16@24"
+ "v32@0:8q16@24"
+ "v40@?0^{__SI=Q{SIFileOps=^?^?^?}{SIGuardedFd=iQ}isII^{SIWatchDog}^{__CFDictionary}{_opaque_pthread_rwlock_t=q[192c]}{si_missing_oids_s={os_unfair_lock_s=I}^{__RLEOIDArray}^{__RLEOIDArray}}{si_missing_oids_s={os_unfair_lock_s=I}^{__RLEOIDArray}^{__RLEOIDArray}}{os_unfair_lock_s=I}{si_comm_dates_s=^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}}{si_comm_dates_s=^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}}{si_comm_dates_s=^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}}{si_comm_dates_s=^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}}{si_comm_dates_s=^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}}^{__CFDictionary}^{_MDPlistContainer}Bi[18^{si_scheduler_token_s}]iI[4^{dispatch_semaphore_s}]{?=[18^{_si_work_scheduler}][21^{_si_workqueue}]^{si_workqueue_list_s}}^{dispatch_queue_s}^{datastore_info}{CIMetaInfo=i^{fd_obj}iQIIIIIIIIqqiiBI}^{DocStore}QQ{_opaque_pthread_mutex_t=q[56c]}^{ContentIndexList}^{ContentIndexList}iII^{_SI_PersistentIDStore}{__SIStoreToken={?=CCCCCCCCCCCCCCCC}^{__CFUUID}}ACAII{os_unfair_lock_s=I}ddBiI^{__CFDictionary}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{os_unfair_lock_s=I}^{__CFBag}{_opaque_pthread_mutex_t=q[56c]}^{__CFSet}^{__CFDictionary}Q^{__CFBag}^{__CFDictionary}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_cond_t=q[40c]}iIIIIIIIIIIIIIIIIIIIBBAq^{__CFDictionary}^{__CFBitVector}^{si_mobile_journal}^{si_mobile_journal}^{si_mobile_journal}AqAqAqd^?^vdd{?=^{fd_obj}IIIq{os_unfair_lock_s=I}BB}III^{FinderDateFields}{_opaque_pthread_mutex_t=q[56c]}^{fd_obj}^{fd_obj}^{fd_obj}iii^{_SIIndexCallbacks}^{__CFArray}^{__CFArray}qqqQIIiiBBBBBBBABB^{si_scheduler_token_s}BBBBBQq[4096c]{os_unfair_lock_s=I}{os_unfair_lock_s=I}b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b2b1^i^{__CFSet}^{__CFDictionary}^{__SIUINT64Set}^{ReverseDirStore_s}^{FileTree_Overlay_s}^{__CFSet}^{TermUpdateSet}{_opaque_pthread_rwlock_t=q[192c]}[16C]Bi^{datastore_info}AIBB[5i]*iI^vB^{fd_obj}iiii{AccumulatedCounts_s={_opaque_pthread_mutex_t=q[56c]}[256q][256I]}BB}8^{_xpc_activity_s=}16^B24^{dispatch_group_s=}32"
- "\t\ta: NSFileProtectionComplete\n"
- "\t\tb: NSFileProtectionCompleteUnlessOpen\n"
- "\t\tc: NSFileProtectionCompleteUntilFirstUserAuthentication or Default\n"
- "\t\tcx: NSFileProtectionCompleteWhileUserInactive\n"
- "\t\theartbeat\n"
- "\t\tindex\n"
- "\t\tindexdrop\n"
- "\t\tm: MobileMailIndex\n"
- "\t\tp: Priority\n"
- "\tshorthands:\n"
- "\tsubcommands:\n"
- "%@/Library/Logs/CrashReporter/DiagnosticLogs/Search"
- "%@/indexOpenRecord.plist"
- "%@/spotlight_heartbeat_last.txt"
- "%@/spotlight_index_drop.%@.%d.%@.%@.%02d.txt"
- "%@/spotlight_index_drop.%@.%d.%@.%@.txt"
- "%@_%@"
- "%s:%d: Error %d opening path: %s"
- "%s:%d: Error gathering heartbeat data: %@"
- "%s:%d: Error getting index size (%u)"
- "%s:%d: Failed refreshing shared heartbeat fields: %@"
- "%s:%d: Failed to collect data about dropped index: %@"
- "%s:%d: Failed to delete legacy file: %@"
- "%s:%d: Failed to get device RAM with error: %d"
- "%s:%d: Failed to get index path (pc: %u)"
- "%s:%d: Failed to get index ref (%@)"
- "%s:%d: Failed to get journal file info (%u)"
- "%s:%d: Failed to get path index (%u)"
- "%s:%d: Failed to identify index %u"
- "%s:%d: Failed to parse reason"
- "%s:%d: Failed to stat index (%u): %d"
- "%s:%d: Failed to write heartbeat report to file: %@"
- "%s:%d: Failed to write index drop report to file: %@"
- "%s:%d: Invalid prefix %@"
- "%s:%d: No info for heartbeat event"
- "%s:%d: Over 10 drops with same timestamp %@"
- "%s:%d: SIAnalytics object already exists"
- "%s:%d: Skipping data collection for read fail"
- "%s:%d: Skipping heartbeat events for read fail"
- "%s:%d: Skipping locale change %ld for read fail"
- "%s:%d: Skipping open (%@, %d, %ld) for read fail"
- "%s:%d: Skipping purgeability (%@, %d) for read fail"
- "%s:%d: Skipping refresh because read failed"
- "%s:%d: Skipping requests (%@, %llu, %llu, %llu) for read fail"
- "%s:%d: Skipping reset for read fail"
- "%s:%d: Skipping timestamp (%@, %@) for read fail"
- "%s:%d: Skipping write because read failed"
- "%s:%d: analytics object malloc error (%u)"
- "%s:%d: analytics set up failed (count, %u, %d)"
- "%s:%d: analytics set up failed (creation, %u, %u, %u)"
- "%s:%d: analytics set up failed (reset, %u)"
- "%s:%d: calloc failed copy data %u"
- "%s:%d: calloc failed for creation (%u, %u, %u)"
- "%s:%d: count data file init fail: %d"
- "%s:%d: count data file not available (%u, %d)"
- "%s:%d: count data file not available (reset, %u)"
- "%s:%d: count data file truncate fail: %d"
- "%s:%d: count data open fail (%u, %d): %d"
- "%s:%d: count data open fail (reset, %u): %d"
- "%s:%d: count data read fail (%u, %d): %ld / %d"
- "%s:%d: count data read fail index (%u): %ld / %d"
- "%s:%d: count data read open fail (%u): %d"
- "%s:%d: count data write fail (%d): %ld / %d"
- "%s:%d: count data write fail (reset, %u): %ld / %d"
- "%s:%d: creation data file init fail: %d"
- "%s:%d: creation data file not available (%u, %u, %u)"
- "%s:%d: creation data open fail (%u, %u, %u): %d"
- "%s:%d: creation data read open fail (%u): %d"
- "%s:%d: creation data write fail (%u, %u, %u): %d"
- "%s:%d: fstatat error %d for %s"
- "-[SIAnalytics createHeartbeatDataWithRefresh:error:]"
- "-[SIAnalytics initWithParentDirectoryPath:corespotlight:heartbeatIndex:resourcesCallback:]"
- "-[SIAnalytics migrateFromLegacyHeartbeatData:]"
- "-[SIAnalytics populateIndexDropData:forIndex:reason:error:]"
- "-[SIAnalytics recordLocaleChange:]"
- "-[SIAnalytics recordOpen:forIndex:dirty:]"
- "-[SIAnalytics recordRequestsForIndex:adds:updates:deletes:]"
- "-[SIAnalytics resetAfterHeartbeat]"
- "-[SIAnalytics sendHeartbeatEventWithData:withReset:]"
- "-[SIAnalytics sendHeartbeatEvent]"
- "-[SIAnalytics sendIndexDropEventWithCorruptIndex:path:readOnly:reason:]"
- "-[SIAnalytics sendIndexDropEventWithData:]"
- "-[SIAnalytics setHeartbeatTimestampForPrefix:key:]"
- "-[SIAnalytics setPurgeability:forIndex:]"
- "-[SIAnalyticsIndexData refreshHeartbeatDataWithIndex:path:errors:]"
- "2400.13.1.101"
- "@24@0:8^B16"
- "@40@0:8@16@24^@32"
- "@40@0:8@16B24B28@?32"
- "@?"
- "B24@0:8q16"
- "Deleted legacy file"
- "Failed to create diagnostics directory: %@"
- "Getting size of directory %s"
- "Heartbeat reporting is disabled"
- "Index drop reporting is disabled"
- "Migrating existing heartbeat data to new format"
- "No data retrieved.\n"
- "Not reporting index drop (%@): directory age < 3600s"
- "Not reporting index drop (%@): no data for index"
- "Not reporting index drop (%@): no opens since last report"
- "Null pc, should be Metadata index"
- "Reading from heartbeat file"
- "Reporting heartbeat"
- "Reporting index drop for %@"
- "Reporting vector index drop (%u)"
- "Reset fields as if a Spotlight Heartbeat report was just sent.\n"
- "SIAnalyticsCopyData"
- "SIAnalyticsGetJournalInfo"
- "SIAnalyticsIndexCountDataFileInit"
- "SIAnalyticsIndexCreationDataFileInit"
- "SIAnalyticsIndexIncrementCounts"
- "SIAnalyticsIndexInit"
- "SIAnalyticsIndexSetCreationInfo"
- "SIAnalyticsInitialize"
- "SIAnalyticsReportVectorIndexDrop"
- "SIAnalyticsResetCounts"
- "SIGetDirectorySize"
- "SIGetIndexDirectorySize"
- "Sending heartbeat event"
- "Sending index drop event (%@)"
- "Sending legacy heartbeat event"
- "Sending legacy index drop event"
- "Skipping initialize because read failed"
- "Skipping updating resources fields since callback has not been set"
- "Spotlight version changed %@ -> %@"
- "Spotlight-%@"
- "SpotlightHeartbeat"
- "SpotlightIndexDrop"
- "Writing to heartbeat file"
- "Wrote to %@"
- "_readHeartbeat"
- "_reportPID"
- "_reportProcessName"
- "_reportTime"
- "_resourcesCallback"
- "age"
- "analyticsCountData"
- "analyticsCreationData"
- "appendFormat:"
- "build"
- "buildbeforeupgrade"
- "classification"
- "com.apple.searchd.indexes.heartbeat"
- "com.apple.searchd.indexrebuildcount"
- "com.apple.searchd.vectorindexdrop"
- "com.apple.spotlightindex.analytics"
- "command: %@"
- "component"
- "copyHeartbeatData"
- "count data read hit EOF (%u, %d), starting from 0"
- "count_add_journaled"
- "count_add_processed"
- "count_add_request"
- "count_delete_journaled"
- "count_delete_processed"
- "count_delete_request"
- "count_drop"
- "count_drop_total"
- "count_open_clean"
- "count_open_dirty"
- "count_update_journaled"
- "count_update_processed"
- "count_update_request"
- "createDropDataForIndex:path:error:"
- "createHeartbeatDataWithRefresh:error:"
- "creation data read fail flags (%u): %ld / %d"
- "creation_flags_index"
- "creation_flags_sdb"
- "creation_version_spotlight"
- "data_collection_error"
- "disable_heartbeat_reporting"
- "disable_index_drop_reporting"
- "diskimage"
- "drop_reason"
- "drop_timestamp"
- "droppedindexage"
- "droppedindexsize"
- "droptime"
- "embeddingdonationon"
- "errorWithDomain:code:userInfo:"
- "eventCount"
- "externalvolume"
- "fileprotection"
- "filesystemflags"
- "filesystemfree"
- "filesystemsize"
- "filesystemtype"
- "getCurrentSpotlightVersionWithRoots:"
- "getIndexDataForPrefix:"
- "getLegacyPCEnum"
- "getPrefixForPCPriority"
- "getPrefixForProtectionClass"
- "getPreviousBuild"
- "hasSpotlightRoots"
- "heartbeat"
- "heartbeat_age"
- "hw.memsize"
- "index"
- "index_%@"
- "index_dropped"
- "index_name"
- "indexrebuildcount"
- "initWithBool:"
- "initWithCString:encoding:"
- "initWithFormat:"
- "initWithLong:"
- "initWithParentDirectoryPath:corespotlight:heartbeatIndex:resourcesCallback:"
- "initWithPrefix:"
- "initWithSuiteName:"
- "initWithUnsignedInt:"
- "initWithUnsignedLongLong:"
- "initializeSharedHearbeatFields"
- "isHeartbeatReportingDisabled"
- "isIndexDropReportingDisabled"
- "journalAttr"
- "lastSent"
- "max_index_gen_merge_level"
- "max_journal_file_bytes"
- "migrateFromLegacyHeartbeatData:"
- "num_file"
- "num_index_gen_compacted"
- "num_index_gen_non_compacted"
- "num_index_gen_read_only"
- "num_index_gen_writeable"
- "num_journal_file"
- "num_object_sdb"
- "otaversion"
- "parentDirectory_age"
- "pcA_age"
- "pcA_obj_count"
- "pcA_wipes"
- "pcA_wipes_aggregate"
- "pcB_age"
- "pcB_obj_count"
- "pcB_wipes"
- "pcB_wipes_aggregate"
- "pcCX_age"
- "pcCX_obj_count"
- "pcCX_wipes"
- "pcCX_wipes_aggregate"
- "pcC_age"
- "pcC_obj_count"
- "pcC_wipes"
- "pcC_wipes_aggregate"
- "pcMail_age"
- "pcMail_obj_count"
- "pcMail_wipes"
- "pcMail_wipes_aggregate"
- "pcPriority_age"
- "pcPriority_obj_count"
- "pcPriority_wipes"
- "pcPriority_wipes_aggregate"
- "pid"
- "populateIndexDropData:forIndex:reason:error:"
- "previousbuild"
- "previousspotlightversion"
- "processInfo"
- "process_id"
- "process_name"
- "processname"
- "purgeable"
- "read"
- "readonlyfilesystem"
- "readonlyopen"
- "recordDrop:"
- "recordLocaleChange:"
- "recordOpen:dirty:"
- "recordOpen:forIndex:dirty:"
- "recordRequestedAdds:updates:deletes:"
- "recordRequestsForIndex:adds:updates:deletes:"
- "refreshHeartbeatDataWithIndex:path:errors:"
- "removeItemAtPath:error:"
- "removeObjectForKey:"
- "reset"
- "resetAfterHeartbeat"
- "rootsinstalled"
- "runCommand:"
- "runCommand: %@"
- "searchutil -c analytics:<subcommand>[:arguments:...]\n"
- "searchutil -c analytics:heartbeat:all  : print all heartbeat data that would be sent by a Spotlight heartbeat event.\n"
- "searchutil -c analytics:heartbeat:index:<shorthand>  : collect and dump values of per-index heartbeat fields.\n"
- "searchutil -c analytics:heartbeat:read  : read heartbeat.plist into memory; note that this might undo any in-memory updates.\n"
- "searchutil -c analytics:heartbeat:reset  : reset certain fields as if a Spotlight heartbeat event has been reported.\n"
- "searchutil -c analytics:heartbeat:send  : create Spotlight heartbeat event and send it to CoreAnalytics.\n"
- "searchutil -c analytics:heartbeat:shared  : refresh shared heartbeat fields and dump values.\n"
- "searchutil -c analytics:heartbeat:write  : flush out in-memory heartbeat data to heartbeat.plist\n"
- "searchutil -c analytics:index:<shorthand>  : dump contents of index's analyticsCreationData and analyticsCountData files.\n"
- "sendHeartbeatEvent"
- "sendHeartbeatEventWithData:withReset:"
- "sendIndexDropEventWithCorruptIndex:path:readOnly:reason:"
- "sendIndexDropEventWithData:"
- "sendLegacyHeartbeatEventWithData:"
- "sendLegacyIndexDropEventWithData:readOnly:prefix:"
- "sendVectorIndexDropForIndex:vectorCount:readOnly:prefix:propertyName:dropReason:"
- "setDateFormat:"
- "setHeartbeatTimestampForPrefix:key:"
- "setPurgeability:"
- "setPurgeability:forIndex:"
- "setSpotlightVersion"
- "setTimestampForKey:"
- "sharedInstance"
- "shouldReportIndexDrop:"
- "size_bytes"
- "spotlightversion"
- "stringFromDate:"
- "supportspsid"
- "textsemanticsearchon"
- "timeIntervalSince1970"
- "time_since"
- "time_since_boot"
- "time_since_compaction_end"
- "time_since_compaction_start"
- "time_since_drop"
- "time_since_last_heartbeat"
- "time_since_last_open_clean"
- "time_since_last_open_dirty"
- "time_since_locale_change"
- "time_since_merge_end"
- "time_since_merge_start"
- "time_since_merge_vacuum_end"
- "time_since_merge_vacuum_start"
- "time_since_purgeability_change"
- "timesinceboot"
- "unsignedLongLongValue"
- "updateWithData:"
- "usageInfoForCommand:"
- "v2"
- "v28@0:8@16B24"
- "v28@0:8B16@20"
- "v28@0:8q16B24"
- "v32@0:8@16@24"
- "v32@?0@\"NSString\"8@\"NSNumber\"16^B24"
- "v32@?0@\"NSString\"8@\"NSObject\"16^B24"
- "v36@0:8@16B24@28"
- "v36@0:8q16@24B32"
- "v40@0:8Q16Q24Q32"
- "v40@0:8^{__SI=Q{SIFileOps=^?^?^?}{SIGuardedFd=iQ}isII^{SIWatchDog}^{__CFDictionary}{_opaque_pthread_rwlock_t=q[192c]}{si_missing_oids_s={os_unfair_lock_s=I}^{__RLEOIDArray}^{__RLEOIDArray}}{si_missing_oids_s={os_unfair_lock_s=I}^{__RLEOIDArray}^{__RLEOIDArray}}{os_unfair_lock_s=I}{si_comm_dates_s=^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}}{si_comm_dates_s=^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}}{si_comm_dates_s=^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}}{si_comm_dates_s=^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}}{si_comm_dates_s=^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}}^{__CFDictionary}^{_MDPlistContainer}Bi[18^{si_scheduler_token_s}]iI[4@]{?=[18^{_si_work_scheduler}][21^{_si_workqueue}]^{si_workqueue_list_s}}@^{datastore_info}{CIMetaInfo=i^{fd_obj}iQIIIIIIIIqqiiBI}^{DocStore}QQ{_opaque_pthread_mutex_t=q[56c]}^{ContentIndexList}^{ContentIndexList}iII^{_SI_PersistentIDStore}{__SIStoreToken={?=CCCCCCCCCCCCCCCC}^{__CFUUID}}ACAII{os_unfair_lock_s=I}ddBiI^{__CFDictionary}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{os_unfair_lock_s=I}^{__CFBag}{_opaque_pthread_mutex_t=q[56c]}^{__CFSet}^{__CFDictionary}Q^{__CFBag}^{__CFDictionary}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_cond_t=q[40c]}iIIIIIIIIIIIIIIIIIIIBBAq^{__CFDictionary}^{__CFBitVector}^{si_mobile_journal}^{si_mobile_journal}^{si_mobile_journal}AqAqAqd^?^vdd{?=^{fd_obj}IIIq{os_unfair_lock_s=I}BB}III^{FinderDateFields}{_opaque_pthread_mutex_t=q[56c]}^{fd_obj}^{fd_obj}^{fd_obj}iii^{_SIIndexCallbacks}^{__CFArray}^{__CFArray}qqqQIIiiBBBBBBBABB^{si_scheduler_token_s}BBBBBQq[4096c]{os_unfair_lock_s=I}{os_unfair_lock_s=I}b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b2b1^i^{__CFSet}^{__CFDictionary}^{__SIUINT64Set}^{ReverseDirStore_s}^{FileTree_Overlay_s}^{__CFSet}^{TermUpdateSet}{_opaque_pthread_rwlock_t=q[192c]}[16C]Bi^{datastore_info}AIBB[5i]*iI^vB^{fd_obj}iiii{AccumulatedCounts_s={_opaque_pthread_mutex_t=q[56c]}[256q][256I]}BB^{si_analytics_s}}16@24^Q32"
- "v40@?0^{__SI=Q{SIFileOps=^?^?^?}{SIGuardedFd=iQ}isII^{SIWatchDog}^{__CFDictionary}{_opaque_pthread_rwlock_t=q[192c]}{si_missing_oids_s={os_unfair_lock_s=I}^{__RLEOIDArray}^{__RLEOIDArray}}{si_missing_oids_s={os_unfair_lock_s=I}^{__RLEOIDArray}^{__RLEOIDArray}}{os_unfair_lock_s=I}{si_comm_dates_s=^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}}{si_comm_dates_s=^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}}{si_comm_dates_s=^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}}{si_comm_dates_s=^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}}{si_comm_dates_s=^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}}^{__CFDictionary}^{_MDPlistContainer}Bi[18^{si_scheduler_token_s}]iI[4^{dispatch_semaphore_s}]{?=[18^{_si_work_scheduler}][21^{_si_workqueue}]^{si_workqueue_list_s}}^{dispatch_queue_s}^{datastore_info}{CIMetaInfo=i^{fd_obj}iQIIIIIIIIqqiiBI}^{DocStore}QQ{_opaque_pthread_mutex_t=q[56c]}^{ContentIndexList}^{ContentIndexList}iII^{_SI_PersistentIDStore}{__SIStoreToken={?=CCCCCCCCCCCCCCCC}^{__CFUUID}}ACAII{os_unfair_lock_s=I}ddBiI^{__CFDictionary}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{os_unfair_lock_s=I}^{__CFBag}{_opaque_pthread_mutex_t=q[56c]}^{__CFSet}^{__CFDictionary}Q^{__CFBag}^{__CFDictionary}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_cond_t=q[40c]}iIIIIIIIIIIIIIIIIIIIBBAq^{__CFDictionary}^{__CFBitVector}^{si_mobile_journal}^{si_mobile_journal}^{si_mobile_journal}AqAqAqd^?^vdd{?=^{fd_obj}IIIq{os_unfair_lock_s=I}BB}III^{FinderDateFields}{_opaque_pthread_mutex_t=q[56c]}^{fd_obj}^{fd_obj}^{fd_obj}iii^{_SIIndexCallbacks}^{__CFArray}^{__CFArray}qqqQIIiiBBBBBBBABB^{si_scheduler_token_s}BBBBBQq[4096c]{os_unfair_lock_s=I}{os_unfair_lock_s=I}b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b2b1^i^{__CFSet}^{__CFDictionary}^{__SIUINT64Set}^{ReverseDirStore_s}^{FileTree_Overlay_s}^{__CFSet}^{TermUpdateSet}{_opaque_pthread_rwlock_t=q[192c]}[16C]Bi^{datastore_info}AIBB[5i]*iI^vB^{fd_obj}iiii{AccumulatedCounts_s={_opaque_pthread_mutex_t=q[56c]}[256q][256I]}BB^{si_analytics_s}}8^{_xpc_activity_s=}16^B24^{dispatch_group_s=}32"
- "v44@0:8@16@24B32@36"
- "v48@0:8@16@24@32^@40"
- "v48@0:8@16Q24Q32Q40"
- "v52@0:8@16I24B28@32@40I48"
- "vectorindexon"
- "write"
- "yyyy-MM-dd-HH-mm-ss"

```
