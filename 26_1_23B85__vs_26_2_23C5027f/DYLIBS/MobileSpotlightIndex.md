## MobileSpotlightIndex

> `/System/Library/PrivateFrameworks/MobileSpotlightIndex.framework/MobileSpotlightIndex`

```diff

-2400.14.100.0.0
-  __TEXT.__text: 0x464540
-  __TEXT.__auth_stubs: 0x3780
-  __TEXT.__objc_methlist: 0x7a8
+2400.16.0.0.0
+  __TEXT.__text: 0x46fdc4
+  __TEXT.__auth_stubs: 0x37f0
+  __TEXT.__objc_methlist: 0x97c
   __TEXT.__const: 0x9dbb
-  __TEXT.__cstring: 0x2620f
+  __TEXT.__cstring: 0x279a3
   __TEXT.__gcc_except_tab: 0x40d8
-  __TEXT.__oslogstring: 0x20b38
+  __TEXT.__oslogstring: 0x20a4c
   __TEXT.__dlopen_cstrs: 0x150
   __TEXT.__ustring: 0x116c
   __TEXT.__dof_mds: 0x29b
-  __TEXT.__unwind_info: 0x5c98
+  __TEXT.__unwind_info: 0x5da0
   __TEXT.__eh_frame: 0x220
   __TEXT.__objc_classname: 0xd4
-  __TEXT.__objc_methname: 0x1ca9
-  __TEXT.__objc_methtype: 0xe2c
-  __TEXT.__objc_stubs: 0x18a0
-  __DATA_CONST.__got: 0x2f8
-  __DATA_CONST.__const: 0x8fd0
+  __TEXT.__objc_methname: 0x214a
+  __TEXT.__objc_methtype: 0xf2a
+  __TEXT.__objc_stubs: 0x1fa0
+  __DATA_CONST.__got: 0x310
+  __DATA_CONST.__const: 0x9250
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x800
+  __DATA_CONST.__objc_selrefs: 0x970
   __DATA_CONST.__objc_superrefs: 0x60
   __DATA_CONST.__objc_arraydata: 0x250
-  __AUTH_CONST.__auth_got: 0x1bd0
-  __AUTH_CONST.__const: 0x8730
-  __AUTH_CONST.__cfstring: 0xba00
-  __AUTH_CONST.__objc_const: 0x10c0
-  __AUTH_CONST.__objc_intobj: 0x108
+  __AUTH_CONST.__auth_got: 0x1c08
+  __AUTH_CONST.__const: 0x87f0
+  __AUTH_CONST.__cfstring: 0xcce0
+  __AUTH_CONST.__objc_const: 0x1120
+  __AUTH_CONST.__objc_intobj: 0xf0
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_doubleobj: 0x1b0
   __AUTH.__objc_data: 0x410
   __AUTH.__data: 0x1628
-  __DATA.__objc_ivar: 0xcc
-  __DATA.__data: 0x10c8
-  __DATA.__bss: 0x111768
+  __DATA.__objc_ivar: 0xd8
+  __DATA.__data: 0x10e0
+  __DATA.__bss: 0x111798
   __DATA_DIRTY.__data: 0x3f8
-  __DATA_DIRTY.__bss: 0x8b88
+  __DATA_DIRTY.__bss: 0x8b78
   __DATA_DIRTY.__common: 0x24004
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: A3327324-B6B0-31CB-BDCA-362148B441BB
-  Functions: 7310
-  Symbols:   19769
-  CStrings:  10707
+  UUID: 1FE06EE5-082D-3C74-AD3E-DF9D2CE5E782
+  Functions: 7396
+  Symbols:   20034
+  CStrings:  11165
 
Symbols:
+ +[SIAnalytics getCurrentSpotlightVersionWithRoots:]
+ +[SIAnalytics getPreviousBuild]
+ +[SIAnalytics hasSpotlightRoots]
+ +[SIAnalytics isHeartbeatReportingDisabled]
+ +[SIAnalytics isIndexDropReportingDisabled]
+ +[SIAnalytics recordRequestsForIndex:adds:updates:deletes:]
+ +[SIAnalytics runCommand:]
+ +[SIAnalytics sendHeartbeatEvent]
+ +[SIAnalytics sendIndexDropEventWithCorruptIndex:path:readOnly:reason:]
+ +[SIAnalytics setPurgeTimestampForIndex:start:]
+ +[SIAnalytics setPurgeability:forIndex:]
+ +[SIAnalytics setSpotlightVersion]
+ +[SIAnalytics sharedInstance]
+ -[SIAnalytics createDropDataForPrefix:path:error:]
+ -[SIAnalytics createHeartbeatDataWithRefresh:error:]
+ -[SIAnalytics dealloc]
+ -[SIAnalytics eventCount]
+ -[SIAnalytics getIndexDataForPrefix:]
+ -[SIAnalytics getPreviousBuild]
+ -[SIAnalytics initWithParentDirectoryPath:corespotlight:heartbeatIndex:resourcesCallback:]
+ -[SIAnalytics initializeSharedHearbeatFields]
+ -[SIAnalytics migrateFromLegacyHeartbeatData:]
+ -[SIAnalytics populateIndexDropData:index:prefix:reason:error:]
+ -[SIAnalytics recordLocaleChange:]
+ -[SIAnalytics recordOpen:forIndex:dirty:]
+ -[SIAnalytics recordRequestsForIndex:adds:updates:deletes:]
+ -[SIAnalytics resetAfterHeartbeat]
+ -[SIAnalytics runCommand:]
+ -[SIAnalytics sendHeartbeatEventWithData:withReset:]
+ -[SIAnalytics sendHeartbeatEvent]
+ -[SIAnalytics sendIndexDropEventWithCorruptIndex:prefix:path:readOnly:reason:]
+ -[SIAnalytics sendIndexDropEventWithData:]
+ -[SIAnalytics sendLegacyHeartbeatEventWithData:]
+ -[SIAnalytics sendLegacyIndexDropEventWithData:prefix:readOnly:reason:]
+ -[SIAnalytics sendVectorIndexDropForIndex:vectorCount:readOnly:prefix:propertyName:dropReason:]
+ -[SIAnalytics setHeartbeatTimestamp:prefix:key:]
+ -[SIAnalytics setPurgeTimestamp:prefix:start:]
+ -[SIAnalytics setPurgeability:prefix:]
+ -[SIAnalytics shouldReportIndexDrop:]
+ -[SIAnalytics usageInfoForCommand:]
+ -[SIAnalyticsIndexData copyHeartbeatData]
+ -[SIAnalyticsIndexData dealloc]
+ -[SIAnalyticsIndexData initWithPrefix:]
+ -[SIAnalyticsIndexData recordDrop:]
+ -[SIAnalyticsIndexData recordOpen:dirty:]
+ -[SIAnalyticsIndexData recordRequestedAdds:updates:deletes:]
+ -[SIAnalyticsIndexData refreshHeartbeatDataWithIndex:path:errors:]
+ -[SIAnalyticsIndexData resetAfterHeartbeat]
+ -[SIAnalyticsIndexData setConfigFlag:]
+ -[SIAnalyticsIndexData setPurgeability:]
+ -[SIAnalyticsIndexData setTimestamp:key:]
+ -[SIAnalyticsIndexData shouldReportIndexDrop:]
+ -[SIAnalyticsIndexData updateWithData:]
+ GCC_except_table1515
+ GCC_except_table1517
+ GCC_except_table1524
+ GCC_except_table1527
+ GCC_except_table1595
+ GCC_except_table1762
+ GCC_except_table1766
+ GCC_except_table1798
+ GCC_except_table2394
+ GCC_except_table2405
+ GCC_except_table2406
+ GCC_except_table2409
+ GCC_except_table2819
+ GCC_except_table3579
+ GCC_except_table3580
+ GCC_except_table3581
+ GCC_except_table3582
+ GCC_except_table3583
+ GCC_except_table3584
+ GCC_except_table3585
+ GCC_except_table3586
+ GCC_except_table3587
+ GCC_except_table3588
+ GCC_except_table3589
+ GCC_except_table3590
+ GCC_except_table3591
+ GCC_except_table3597
+ GCC_except_table3607
+ GCC_except_table3608
+ GCC_except_table3610
+ GCC_except_table3614
+ GCC_except_table3627
+ GCC_except_table3632
+ GCC_except_table3637
+ GCC_except_table3638
+ GCC_except_table3641
+ GCC_except_table3642
+ GCC_except_table3643
+ GCC_except_table3644
+ GCC_except_table3647
+ GCC_except_table3648
+ GCC_except_table3649
+ GCC_except_table5479
+ GCC_except_table5481
+ GCC_except_table5944
+ GCC_except_table5946
+ GCC_except_table5948
+ GCC_except_table5950
+ GCC_except_table5959
+ GCC_except_table5962
+ GCC_except_table5974
+ GCC_except_table5975
+ GCC_except_table5977
+ GCC_except_table5979
+ GCC_except_table5989
+ GCC_except_table5990
+ GCC_except_table5994
+ GCC_except_table6006
+ GCC_except_table6007
+ GCC_except_table6008
+ GCC_except_table6009
+ GCC_except_table6010
+ GCC_except_table6011
+ GCC_except_table6012
+ GCC_except_table6013
+ GCC_except_table6014
+ GCC_except_table6015
+ GCC_except_table6016
+ GCC_except_table6017
+ GCC_except_table6018
+ GCC_except_table6024
+ GCC_except_table6033
+ GCC_except_table6034
+ GCC_except_table6035
+ GCC_except_table6036
+ GCC_except_table6037
+ GCC_except_table6038
+ GCC_except_table6046
+ GCC_except_table6047
+ GCC_except_table6049
+ GCC_except_table6050
+ GCC_except_table6065
+ GCC_except_table6066
+ GCC_except_table6067
+ GCC_except_table6068
+ GCC_except_table6069
+ GCC_except_table6070
+ GCC_except_table6130
+ GCC_except_table6133
+ GCC_except_table6136
+ GCC_except_table6137
+ GCC_except_table6138
+ GCC_except_table6139
+ GCC_except_table6373
+ GCC_except_table6374
+ GCC_except_table6375
+ GCC_except_table6381
+ GCC_except_table6385
+ GCC_except_table6388
+ GCC_except_table6389
+ GCC_except_table6390
+ GCC_except_table6391
+ GCC_except_table6392
+ GCC_except_table6394
+ GCC_except_table6398
+ GCC_except_table6400
+ GCC_except_table6401
+ GCC_except_table6402
+ GCC_except_table6403
+ GCC_except_table6404
+ GCC_except_table6405
+ GCC_except_table6406
+ GCC_except_table6407
+ GCC_except_table6408
+ GCC_except_table6409
+ GCC_except_table6410
+ GCC_except_table6417
+ GCC_except_table6422
+ GCC_except_table6423
+ GCC_except_table6424
+ GCC_except_table6425
+ GCC_except_table6426
+ GCC_except_table6427
+ GCC_except_table6428
+ GCC_except_table6429
+ GCC_except_table6430
+ GCC_except_table6431
+ GCC_except_table6432
+ GCC_except_table6433
+ GCC_except_table6434
+ GCC_except_table6436
+ GCC_except_table6450
+ GCC_except_table6452
+ GCC_except_table6454
+ GCC_except_table6464
+ GCC_except_table6477
+ GCC_except_table6481
+ GCC_except_table6493
+ GCC_except_table6494
+ GCC_except_table6648
+ GCC_except_table7354
+ GCC_except_table7355
+ GCC_except_table7363
+ GCC_except_table7365
+ GCC_except_table7366
+ GCC_except_table7368
+ GCC_except_table7375
+ GCC_except_table7379
+ GCC_except_table7382
+ GCC_except_table7383
+ GCC_except_table7384
+ GCC_except_table7385
+ GCC_except_table7386
+ GCC_except_table7388
+ GCC_except_table7407
+ GCC_except_table7409
+ GCC_except_table7410
+ GCC_except_table7412
+ GCC_except_table7413
+ GCC_except_table7416
+ GCC_except_table7417
+ GCC_except_table7418
+ _AnalyticsSendEvent
+ _FlatStorePageEntryWrite2.3367
+ _MurmurHash3_x86_32.17435
+ _NSHomeDirectory
+ _OBJC_CLASS_$_NSDateFormatter
+ _OBJC_CLASS_$_NSMutableString
+ _OBJC_CLASS_$_NSProcessInfo
+ _OBJC_IVAR_$_SIAnalytics._readHeartbeat
+ _OBJC_IVAR_$_SIAnalytics._resourcesCallback
+ _OBJC_IVAR_$_SIAnalyticsIndexData._configFlags
+ _SIAnalyticsCopyData
+ _SIAnalyticsGetSDBSize
+ _SIAnalyticsHeartbeatRecordIndexOpen
+ _SIAnalyticsHeartbeatSetTimestamp
+ _SIAnalyticsIndexDestroy
+ _SIAnalyticsIndexIncrementCounts
+ _SIAnalyticsIndexInit.onceToken
+ _SIAnalyticsInitialize.onceToken
+ _SIAnalyticsReportVectorIndexDrop
+ _SICopyError
+ _SIErrorKey
+ _SIErrorKeyOnce
+ _SIGetDirectorySize
+ _SIGetErrorCode
+ _SIGetErrorString
+ _SIGetIndexDirectorySize
+ _SIGetInvalidTermUpdateSet
+ _SIIndexFdKey
+ _SIInvalidTermUpdateSetKey
+ _SIReleaseError
+ _SISetError
+ _SISetInvalidTermUpdateSet
+ __PayloadWriteData.3923
+ __SICopyErrorFromBuffer
+ __SIErrorCopy
+ __SIErrorDestroy
+ __SIErrorInit
+ __SIGetError
+ __SIGetErrorIsIntentional
+ __SISetIndexFd
+ __ZGVZL12MetadataKeysvE13_metadataKeys.17383
+ __ZGVZL17GenericFilterKeysvE18_genericFilterKeys.17402
+ __ZGVZL18PhRetrievalAttribsvE17_retrievalAttribs.17103
+ __ZGVZL25GenericFilterTopLevelKeysvE26_genericFilterTopLevelKeys.17394
+ __ZGVZL26PhExactMatchRankingAttribsvE27_phExactMatchRankingAttribs.17286
+ __ZL10commonHashjPKhj.16349
+ __ZL11MAX_OIDINFO.16844
+ __ZL11TOK_ID_FROM.4295
+ __ZL12ZERO_OIDINFO.16843
+ __ZL13PhAttribNodesPKcRKNSt3__113unordered_setINS1_12basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEENS1_4hashIS8_EENS1_8equal_toIS8_EENS6_IS8_EEEEbb.17146
+ __ZL13v2_readVInt64PKhPm.8962
+ __ZL13v2_readVInt64RPKhRmRy.9521
+ __ZL14ZERO_FETCHINFO.5907
+ __ZL14v2_writeVInt64Phmy.8956
+ __ZL14v2_writeVInt64RPhy.9520
+ __ZL16__message_assertPKcz.16323
+ __ZL16__message_assertPKcz.16354
+ __ZL16__message_assertPKcz.16866
+ __ZL16__message_assertPKcz.2155
+ __ZL16__message_assertPKcz.4110
+ __ZL16__message_assertPKcz.5665
+ __ZL16__message_assertPKcz.5813
+ __ZL16__message_assertPKcz.6188
+ __ZL16__message_assertPKcz.8217
+ __ZL16__message_assertPKcz.8971
+ __ZL16si_analytics_logPKcz.8409
+ __ZL17ZERO_RANKING_BITS.16789
+ __ZL18PhRankingBoostTreev.17035
+ __ZL18PhRetrievalAttribsv.17047
+ __ZL18QueryParserLibraryv.10861
+ __ZL18QueryParserLibraryv.13423
+ __ZL18QueryParserLibraryv.17168
+ __ZL18isGenericFilterKeyRKNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE.17388
+ __ZL20PhRankingTreeFromStrPKcfPi.17018
+ __ZL22__si_assert_copy_extraP6fd_obji.16319
+ __ZL22__si_assert_copy_extraP6fd_obji.16350
+ __ZL22__si_assert_copy_extraP6fd_obji.16862
+ __ZL22__si_assert_copy_extraP6fd_obji.2151
+ __ZL22__si_assert_copy_extraP6fd_obji.4106
+ __ZL22__si_assert_copy_extraP6fd_obji.5661
+ __ZL22__si_assert_copy_extraP6fd_obji.5808
+ __ZL22__si_assert_copy_extraP6fd_obji.6184
+ __ZL22__si_assert_copy_extraP6fd_obji.8212
+ __ZL22__si_assert_copy_extraP6fd_obji.8966
+ __ZL22getkQPQUOutputTokenKeyv.17124
+ __ZL23audit_stringQueryParser.10873
+ __ZL23audit_stringQueryParser.13433
+ __ZL23audit_stringQueryParser.17180
+ __ZL23store_stream_read_bytesP14store_stream_tPhm.8963
+ __ZL24store_stream_write_bytesP14store_stream_tPKhm.8955
+ __ZL25convertASTNodeToQueryNodeP9PRAstNodeP9PRContext.4252
+ __ZL26PhExactMatchRankingAttribsv.17283
+ __ZL26PhImpAttributesRankingNodePKc.17032
+ __ZL26getkQPQUOutputTokenInfoKeyv.17007
+ __ZL26isGenericFilterTopLevelKeyRKNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE.17390
+ __ZL27_containsOnlyCharsInCharsetP8NSStringP14NSCharacterSet.17022
+ __ZL27getkQPQUOutputTokenRangeKeyv.13436
+ __ZL27getkQPQUOutputTokenRangeKeyv.17121
+ __ZL28getkQPQUOutputTokenArgIdsKeyv.10909
+ __ZL28getkQPQUOutputTokenArgIdsKeyv.13437
+ __ZL28getkQPQUOutputTokenArgIdsKeyv.17122
+ __ZL31getkQPQUOutputTokenArgScoresKeyv.13438
+ __ZL31getkQPQUOutputTokenArgScoresKeyv.17123
+ __ZL32PhImpAttributesPrefixRankingNodePKc.17031
+ __ZL6sTotal.1073
+ __ZL6sTotal.1633
+ __ZL6sTotal.16784
+ __ZL6sTotal.16964
+ __ZL6sTotal.17074
+ __ZL6sTotal.1878
+ __ZL6sTotal.4268
+ __ZL6sTotal.5658
+ __ZL6sTotal.5814
+ __ZL6sTotal.7590
+ __ZL6sTotal.8653
+ __ZL6sTotal.872
+ __ZL7Attribsv.4287
+ __ZL9TOK_ID_TO.4300
+ __ZL9intervals.8638
+ __ZZL11CurrentYearvE8currYear.17257
+ __ZZL11CurrentYearvE9onceToken.17256
+ __ZZL12MetadataKeysvE13_metadataKeys.17384
+ __ZZL12MetadataKeysvE9onceToken.17385
+ __ZZL14PhThreeYearAgovE7oldYear.17260
+ __ZZL14PhThreeYearAgovE9onceToken.17259
+ __ZZL16utf8_byte_lengthhE14utf8_len_table.16906
+ __ZZL17GenericFilterKeysvE18_genericFilterKeys.17403
+ __ZZL17GenericFilterKeysvE9onceToken.17404
+ __ZZL18PhRetrievalAttribsvE17_retrievalAttribs.17048
+ __ZZL18PhRetrievalAttribsvE9onceToken.17104
+ __ZZL18utf8_to_code_pointPKhE20utf8_first_char_mask.16907
+ __ZZL22QueryParserLibraryCorePPcE16frameworkLibrary.0.10869
+ __ZZL22QueryParserLibraryCorePPcE16frameworkLibrary.0.13429
+ __ZZL22QueryParserLibraryCorePPcE16frameworkLibrary.0.17176
+ __ZZL24utf8_byte_length_noerrorhE14utf8_len_table.16908
+ __ZZL25GenericFilterTopLevelKeysvE26_genericFilterTopLevelKeys.17395
+ __ZZL25GenericFilterTopLevelKeysvE9onceToken.17396
+ __ZZL26PhExactMatchRankingAttribsvE27_phExactMatchRankingAttribs.17284
+ __ZZL26PhExactMatchRankingAttribsvE9onceToken.17287
+ __ZZL28NanoSecondsSinceAbsoluteTimeyE13sTimebaseInfo.17038
+ __ZZL28NanoSecondsSinceAbsoluteTimeyE9onceToken.17037
+ __ZZL31getkQPQUOutputTokenKeySymbolLocvE3ptr.0.10884
+ __ZZL31getkQPQUOutputTokenKeySymbolLocvE3ptr.0.13439
+ __ZZL31getkQPQUOutputTokenKeySymbolLocvE3ptr.0.17181
+ __ZZL35getkQPQUOutputTokenInfoKeySymbolLocvE3ptr.0.17372
+ __ZZL36getkQPParseAttributeDateKeySymbolLocvE3ptr.0.13584
+ __ZZL36getkQPQUOutputTokenRangeKeySymbolLocvE3ptr.0.10918
+ __ZZL36getkQPQUOutputTokenRangeKeySymbolLocvE3ptr.0.13451
+ __ZZL36getkQPQUOutputTokenRangeKeySymbolLocvE3ptr.0.17193
+ __ZZL37getkQPParseAttributeMediaKeySymbolLocvE3ptr.0.13563
+ __ZZL37getkQPQUOutputTokenArgIdsKeySymbolLocvE3ptr.0.10910
+ __ZZL37getkQPQUOutputTokenArgIdsKeySymbolLocvE3ptr.0.13447
+ __ZZL37getkQPQUOutputTokenArgIdsKeySymbolLocvE3ptr.0.17189
+ __ZZL38getkQPParseAttributeSenderKeySymbolLocvE3ptr.0.13571
+ __ZZL38getkQPParseAttributeUnreadKeySymbolLocvE3ptr.0.13551
+ __ZZL40getkQPQUOutputTokenArgScoresKeySymbolLocvE3ptr.0.13443
+ __ZZL40getkQPQUOutputTokenArgScoresKeySymbolLocvE3ptr.0.17185
+ __ZZL41getkQPParseAttributeDueActionKeySymbolLocvE3ptr.0.13490
+ __ZZL41getkQPParseAttributeRecipientKeySymbolLocvE3ptr.0.13567
+ __ZZL42getkQPParseAttributeAttachmentKeySymbolLocvE3ptr.0.13557
+ __ZZL42getkQPParseAttributeJunkActionKeySymbolLocvE3ptr.0.13482
+ __ZZL43getkQPParseAttributeDescriptionKeySymbolLocvE3ptr.0.13478
+ __ZZL43getkQPParseAttributeDraftActionKeySymbolLocvE3ptr.0.13486
+ __ZZL43getkQPParseAttributeHotelActionKeySymbolLocvE3ptr.0.13514
+ __ZZL44getkQPParseAttributeFlightActionKeySymbolLocvE3ptr.0.13527
+ __ZZL44getkQPParseAttributeLatestActionKeySymbolLocvE3ptr.0.13498
+ __ZZL44getkQPParseAttributeTaggedPersonKeySymbolLocvE3ptr.0.13580
+ __ZZL45getkQPParseAttributeArchiveActionKeySymbolLocvE3ptr.0.13474
+ __ZZL45getkQPParseAttributePrintedActionKeySymbolLocvE3ptr.0.13533
+ __ZZL46getkQPParseAttributeEarliestActionKeySymbolLocvE3ptr.0.13502
+ __ZZL46getkQPParseAttributeGroundedPersonKeySymbolLocvE3ptr.0.13575
+ __ZZL47getkQPParseAttributeCompletedActionKeySymbolLocvE3ptr.0.13494
+ __ZZL48getkQPParseAttributeRestaurantActionKeySymbolLocvE3ptr.0.13508
+ __ZZL53getkQPParseAttributeFlightArrivalLocationKeySymbolLocvE3ptr.0.13518
+ __ZZL55getkQPParseAttributeFlightDepartureLocationKeySymbolLocvE3ptr.0.13522
+ ___26+[SIAnalytics runCommand:]_block_invoke
+ ___33+[SIAnalytics sendHeartbeatEvent]_block_invoke
+ ___34+[SIAnalytics setSpotlightVersion]_block_invoke
+ ___34-[SIAnalytics resetAfterHeartbeat]_block_invoke
+ ___34-[SIAnalytics resetAfterHeartbeat]_block_invoke_2
+ ___39-[SIAnalyticsIndexData updateWithData:]_block_invoke
+ ___40+[SIAnalytics setPurgeability:forIndex:]_block_invoke
+ ___47+[SIAnalytics setPurgeTimestampForIndex:start:]_block_invoke
+ ___50-[SIAnalytics createDropDataForPrefix:path:error:]_block_invoke
+ ___50-[SIAnalytics createDropDataForPrefix:path:error:]_block_invoke_2
+ ___50-[SIAnalytics createDropDataForPrefix:path:error:]_block_invoke_3
+ ___52-[SIAnalytics createHeartbeatDataWithRefresh:error:]_block_invoke
+ ___52-[SIAnalytics createHeartbeatDataWithRefresh:error:]_block_invoke_2
+ ___52-[SIAnalytics createHeartbeatDataWithRefresh:error:]_block_invoke_3
+ ___52-[SIAnalytics createHeartbeatDataWithRefresh:error:]_block_invoke_4
+ ___52-[SIAnalytics createHeartbeatDataWithRefresh:error:]_block_invoke_5
+ ___59+[SIAnalytics recordRequestsForIndex:adds:updates:deletes:]_block_invoke
+ ___66-[SIAnalyticsIndexData refreshHeartbeatDataWithIndex:path:errors:]_block_invoke
+ ___71+[SIAnalytics sendIndexDropEventWithCorruptIndex:path:readOnly:reason:]_block_invoke
+ ___Block_byref_object_copy_.10929
+ ___Block_byref_object_copy_.13472
+ ___Block_byref_object_copy_.13944
+ ___Block_byref_object_copy_.16830
+ ___Block_byref_object_copy_.2123
+ ___Block_byref_object_copy_.2654
+ ___Block_byref_object_copy_.7730
+ ___Block_byref_object_dispose_.10930
+ ___Block_byref_object_dispose_.13473
+ ___Block_byref_object_dispose_.13945
+ ___Block_byref_object_dispose_.16831
+ ___Block_byref_object_dispose_.2124
+ ___Block_byref_object_dispose_.2655
+ ___Block_byref_object_dispose_.7731
+ ___InnerMerge_block_invoke.802
+ ___SIAnalyticsHeartbeatRecordIndexOpen_block_invoke
+ ___SIAnalyticsHeartbeatSetTimestamp_block_invoke
+ ___SIAnalyticsIndexInit_block_invoke
+ ___SIAnalyticsInitialize_block_invoke
+ ___SIAnalyticsReportVectorIndexDrop_block_invoke
+ ___SICreateNewIndex_block_invoke.379
+ ___SIInitIndex_block_invoke.1109
+ ___SIInitIndex_block_invoke.1117
+ ___SIInitIndex_block_invoke.1124
+ ___SIInitIndex_block_invoke.1126
+ ____SIContinueIssueMerge2_block_invoke.1976
+ ____SIOpenIndexFilesWithState_block_invoke.961
+ ____SIOpenIndexFilesWithState_block_invoke.971
+ ____SIOpenIndexFilesWithState_block_invoke.975
+ ____SIOpenIndexFilesWithState_block_invoke_2.973
+ ____SIOpenIndexFilesWithState_block_invoke_2.977
+ ____SIOpenIndex_block_invoke.912
+ ____SIOpenIndex_block_invoke.937
+ ____SIOpenIndex_block_invoke.944
+ ____ZL11CurrentYearv_block_invoke.17273
+ ____ZL12MetadataKeysv_block_invoke.17420
+ ____ZL12processItemsP14datastore_infommP24si_localized_value_cachePmbU13block_pointerFPv15SI_OBJECT_EVENT15si_event_data_tmS4_ES4_ooPtmPhbjmbP16dispatch_queue_sS4_jP14__MDPlistBytes14ranking_mode_sP16ci_rankingbits_sP17ci_tc_distances_tP21ci_vector_distances_tP19PartialQueryResultsRP20SISearchCtx_METADATAiRbP10ReadData_sPV3$_0P22ci_combobits_wrapped_sP20dispatch_semaphore_s_block_invoke.157
+ ____ZL14PhThreeYearAgov_block_invoke.17270
+ ____ZL14readSDBForOidsP20SISearchCtx_METADATAPxPtP16ci_rankingbits_sP17ci_tc_distances_tP21ci_vector_distances_tmPhP19PartialQueryResultsP14__MDPlistBytesbb_block_invoke.122
+ ____ZL14readSDBForOidsP20SISearchCtx_METADATAPxPtP16ci_rankingbits_sP17ci_tc_distances_tP21ci_vector_distances_tmPhP19PartialQueryResultsP14__MDPlistBytesbb_block_invoke.129
+ ____ZL14readSDBForOidsP20SISearchCtx_METADATAPxPtP16ci_rankingbits_sP17ci_tc_distances_tP21ci_vector_distances_tmPhP19PartialQueryResultsP14__MDPlistBytesbb_block_invoke_2.133
+ ____ZL17GenericFilterKeysv_block_invoke.17408
+ ____ZL18PhRetrievalAttribsv_block_invoke.17106
+ ____ZL19convertQPFilterNodeP17PRAstQPFilterNodeP9PRContext_block_invoke.4306
+ ____ZL20PhRankingTreeFromStrPKcfPi_block_invoke.17276
+ ____ZL22QueryParserLibraryCorePPc_block_invoke.10870
+ ____ZL22QueryParserLibraryCorePPc_block_invoke.13430
+ ____ZL22QueryParserLibraryCorePPc_block_invoke.17177
+ ____ZL25GenericFilterTopLevelKeysv_block_invoke.17400
+ ____ZL26PhExactMatchRankingAttribsv_block_invoke.17289
+ ____ZL28NanoSecondsSinceAbsoluteTimey_block_invoke.17255
+ ____ZL28PhPopulateAllFilterFromParseP18NSAttributedStringP14NSMutableArrayIP8NSStringEPS1_IP7NSValueES9_S9_S9__block_invoke.17011
+ ____ZL29PhPopulateDateFilterFromParseP18NSAttributedStringP14NSMutableArrayIP8NSStringEPS1_IP7NSValueE_block_invoke.17117
+ ____ZL30PhPopulateSomeFiltersFromParseP18NSAttributedStringP14NSMutableArrayIP8NSStringEPS1_IP7NSValueES5_S9__block_invoke.17114
+ ____ZL31getkQPQUOutputTokenKeySymbolLocv_block_invoke.10885
+ ____ZL31getkQPQUOutputTokenKeySymbolLocv_block_invoke.13440
+ ____ZL31getkQPQUOutputTokenKeySymbolLocv_block_invoke.17182
+ ____ZL35getkQPQUOutputTokenInfoKeySymbolLocv_block_invoke.17373
+ ____ZL36getkQPParseAttributeDateKeySymbolLocv_block_invoke.13585
+ ____ZL36getkQPQUOutputTokenRangeKeySymbolLocv_block_invoke.10919
+ ____ZL36getkQPQUOutputTokenRangeKeySymbolLocv_block_invoke.13452
+ ____ZL36getkQPQUOutputTokenRangeKeySymbolLocv_block_invoke.17194
+ ____ZL37getkQPParseAttributeMediaKeySymbolLocv_block_invoke.13564
+ ____ZL37getkQPQUOutputTokenArgIdsKeySymbolLocv_block_invoke.10911
+ ____ZL37getkQPQUOutputTokenArgIdsKeySymbolLocv_block_invoke.13448
+ ____ZL37getkQPQUOutputTokenArgIdsKeySymbolLocv_block_invoke.17190
+ ____ZL38getkQPParseAttributeSenderKeySymbolLocv_block_invoke.13572
+ ____ZL38getkQPParseAttributeUnreadKeySymbolLocv_block_invoke.13552
+ ____ZL40getkQPQUOutputTokenArgScoresKeySymbolLocv_block_invoke.13444
+ ____ZL40getkQPQUOutputTokenArgScoresKeySymbolLocv_block_invoke.17186
+ ____ZL41getkQPParseAttributeDueActionKeySymbolLocv_block_invoke.13491
+ ____ZL41getkQPParseAttributeRecipientKeySymbolLocv_block_invoke.13568
+ ____ZL42getkQPParseAttributeAttachmentKeySymbolLocv_block_invoke.13558
+ ____ZL42getkQPParseAttributeJunkActionKeySymbolLocv_block_invoke.13483
+ ____ZL43getkQPParseAttributeDescriptionKeySymbolLocv_block_invoke.13479
+ ____ZL43getkQPParseAttributeDraftActionKeySymbolLocv_block_invoke.13487
+ ____ZL43getkQPParseAttributeHotelActionKeySymbolLocv_block_invoke.13515
+ ____ZL44getkQPParseAttributeFlightActionKeySymbolLocv_block_invoke.13528
+ ____ZL44getkQPParseAttributeLatestActionKeySymbolLocv_block_invoke.13499
+ ____ZL44getkQPParseAttributeTaggedPersonKeySymbolLocv_block_invoke.13581
+ ____ZL45getkQPParseAttributeArchiveActionKeySymbolLocv_block_invoke.13475
+ ____ZL45getkQPParseAttributePrintedActionKeySymbolLocv_block_invoke.13534
+ ____ZL46getkQPParseAttributeEarliestActionKeySymbolLocv_block_invoke.13503
+ ____ZL46getkQPParseAttributeGroundedPersonKeySymbolLocv_block_invoke.13576
+ ____ZL47getkQPParseAttributeCompletedActionKeySymbolLocv_block_invoke.13495
+ ____ZL48getkQPParseAttributeRestaurantActionKeySymbolLocv_block_invoke.13509
+ ____ZL53getkQPParseAttributeFlightArrivalLocationKeySymbolLocv_block_invoke.13519
+ ____ZL55getkQPParseAttributeFlightDepartureLocationKeySymbolLocv_block_invoke.13523
+ ____bt_findBulk_block_invoke.83
+ ____page_fetch_with_fd_block_invoke.215
+ ____si_init_localized_terms_block_invoke.1147
+ ___block_descriptor_32_e35_v32?0"NSString"8"NSNumber"16^B24l
+ ___block_descriptor_32_e47_v32?0"NSString"8"SIAnalyticsIndexData"16^B24l
+ ___block_descriptor_40_e8_32o_e35_v32?0"NSString"8"NSObject"16^B24ls32l8
+ ___block_descriptor_41_e8_32o_e5_v8?0ls32l8
+ ___block_descriptor_48_e8_32o40o_e35_v32?0"NSString"8"NSNumber"16^B24ls32l8s40l8
+ ___block_descriptor_48_e8_32o40o_e35_v32?0"NSString"8"NSObject"16^B24ls32l8s40l8
+ ___block_descriptor_48_e8_32o40o_e39_v32?0"NSString"8"NSDictionary"16^B24ls32l8s40l8
+ ___block_descriptor_48_e8_32o40r_e5_v8?0lr40l8s32l8
+ ___block_descriptor_48_e8_32o_e35_v32?0"NSString"8"NSObject"16^B24ls32l8
+ ___block_descriptor_49_e8_32o_e5_v8?0ls32l8
+ ___block_descriptor_56_e8_32o40o_e35_v32?0"NSString"8"NSObject"16^B24ls32l8s40l8
+ ___block_descriptor_56_e8_32o40o_e5_v8?0ls32l8s40l8
+ ___block_descriptor_57_e8_32o40o_e47_v32?0"NSString"8"SIAnalyticsIndexData"16^B24ls32l8s40l8
+ ___block_descriptor_64_e8_32o_e5_v8?0ls32l8
+ ___block_descriptor_65_e8_32o40o48o_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_65_e8_32o40o_e5_v8?0ls32l8s40l8
+ ___block_descriptor_tmp.1.5688
+ ___block_descriptor_tmp.10.14774
+ ___block_descriptor_tmp.10.15989
+ ___block_descriptor_tmp.1018
+ ___block_descriptor_tmp.102
+ ___block_descriptor_tmp.1053
+ ___block_descriptor_tmp.1069
+ ___block_descriptor_tmp.1075
+ ___block_descriptor_tmp.1079
+ ___block_descriptor_tmp.1081
+ ___block_descriptor_tmp.1085
+ ___block_descriptor_tmp.1090
+ ___block_descriptor_tmp.1094
+ ___block_descriptor_tmp.1099
+ ___block_descriptor_tmp.11.16375
+ ___block_descriptor_tmp.11.9107
+ ___block_descriptor_tmp.1102
+ ___block_descriptor_tmp.1105
+ ___block_descriptor_tmp.111.9269
+ ___block_descriptor_tmp.1110
+ ___block_descriptor_tmp.112.16164
+ ___block_descriptor_tmp.1121
+ ___block_descriptor_tmp.1125
+ ___block_descriptor_tmp.1127
+ ___block_descriptor_tmp.113.8405
+ ___block_descriptor_tmp.1130
+ ___block_descriptor_tmp.11309
+ ___block_descriptor_tmp.1136
+ ___block_descriptor_tmp.1139
+ ___block_descriptor_tmp.11405
+ ___block_descriptor_tmp.1143
+ ___block_descriptor_tmp.1148
+ ___block_descriptor_tmp.115.8406
+ ___block_descriptor_tmp.1150
+ ___block_descriptor_tmp.11524
+ ___block_descriptor_tmp.1153
+ ___block_descriptor_tmp.1158
+ ___block_descriptor_tmp.116
+ ___block_descriptor_tmp.11609
+ ___block_descriptor_tmp.117.15890
+ ___block_descriptor_tmp.117.16165
+ ___block_descriptor_tmp.1171.8353
+ ___block_descriptor_tmp.1177
+ ___block_descriptor_tmp.1180
+ ___block_descriptor_tmp.119
+ ___block_descriptor_tmp.1199
+ ___block_descriptor_tmp.12.11435
+ ___block_descriptor_tmp.12.16010
+ ___block_descriptor_tmp.12.16661
+ ___block_descriptor_tmp.12.4526
+ ___block_descriptor_tmp.12.6174
+ ___block_descriptor_tmp.12.8534
+ ___block_descriptor_tmp.12.9119
+ ___block_descriptor_tmp.120.16166
+ ___block_descriptor_tmp.1202
+ ___block_descriptor_tmp.1208
+ ___block_descriptor_tmp.1211
+ ___block_descriptor_tmp.12122
+ ___block_descriptor_tmp.1215.8366
+ ___block_descriptor_tmp.1216
+ ___block_descriptor_tmp.1235.8458
+ ___block_descriptor_tmp.1247
+ ___block_descriptor_tmp.1248
+ ___block_descriptor_tmp.125
+ ___block_descriptor_tmp.127
+ ___block_descriptor_tmp.127.15932
+ ___block_descriptor_tmp.13.16016
+ ___block_descriptor_tmp.13.4521
+ ___block_descriptor_tmp.13.5614
+ ___block_descriptor_tmp.13.5693
+ ___block_descriptor_tmp.13.6594
+ ___block_descriptor_tmp.13.9120
+ ___block_descriptor_tmp.13.9205
+ ___block_descriptor_tmp.13363
+ ___block_descriptor_tmp.134.15233
+ ___block_descriptor_tmp.135
+ ___block_descriptor_tmp.13672
+ ___block_descriptor_tmp.138.5922
+ ___block_descriptor_tmp.14.2142
+ ___block_descriptor_tmp.14.5180
+ ___block_descriptor_tmp.140
+ ___block_descriptor_tmp.140.6024
+ ___block_descriptor_tmp.141.9252
+ ___block_descriptor_tmp.1414
+ ___block_descriptor_tmp.142
+ ___block_descriptor_tmp.14238
+ ___block_descriptor_tmp.143.3785
+ ___block_descriptor_tmp.144
+ ___block_descriptor_tmp.14448
+ ___block_descriptor_tmp.1450
+ ___block_descriptor_tmp.14660
+ ___block_descriptor_tmp.14763
+ ___block_descriptor_tmp.1478
+ ___block_descriptor_tmp.14946
+ ___block_descriptor_tmp.15.1095
+ ___block_descriptor_tmp.15.1480
+ ___block_descriptor_tmp.15.16881
+ ___block_descriptor_tmp.15.2169
+ ___block_descriptor_tmp.15.5694
+ ___block_descriptor_tmp.15174
+ ___block_descriptor_tmp.15269
+ ___block_descriptor_tmp.153
+ ___block_descriptor_tmp.153.15362
+ ___block_descriptor_tmp.156.15363
+ ___block_descriptor_tmp.156.8496
+ ___block_descriptor_tmp.15983
+ ___block_descriptor_tmp.16.11441
+ ___block_descriptor_tmp.16.1491
+ ___block_descriptor_tmp.16.16882
+ ___block_descriptor_tmp.16.5181
+ ___block_descriptor_tmp.16.8134
+ ___block_descriptor_tmp.160.8226
+ ___block_descriptor_tmp.16332
+ ___block_descriptor_tmp.16344
+ ___block_descriptor_tmp.164
+ ___block_descriptor_tmp.165.15381
+ ___block_descriptor_tmp.16609
+ ___block_descriptor_tmp.16802
+ ___block_descriptor_tmp.169.15580
+ ___block_descriptor_tmp.169.9413
+ ___block_descriptor_tmp.17.13688
+ ___block_descriptor_tmp.170.15292
+ ___block_descriptor_tmp.170.16197
+ ___block_descriptor_tmp.171.15428
+ ___block_descriptor_tmp.171.16195
+ ___block_descriptor_tmp.172.16054
+ ___block_descriptor_tmp.172.6281
+ ___block_descriptor_tmp.174
+ ___block_descriptor_tmp.176
+ ___block_descriptor_tmp.18.9224
+ ___block_descriptor_tmp.1826
+ ___block_descriptor_tmp.1858
+ ___block_descriptor_tmp.1864
+ ___block_descriptor_tmp.1885
+ ___block_descriptor_tmp.1895
+ ___block_descriptor_tmp.19.10446
+ ___block_descriptor_tmp.19.13691
+ ___block_descriptor_tmp.19.1509
+ ___block_descriptor_tmp.19.16056
+ ___block_descriptor_tmp.19.2718
+ ___block_descriptor_tmp.1911
+ ___block_descriptor_tmp.1916
+ ___block_descriptor_tmp.1919
+ ___block_descriptor_tmp.192
+ ___block_descriptor_tmp.1922
+ ___block_descriptor_tmp.1924
+ ___block_descriptor_tmp.1925
+ ___block_descriptor_tmp.1933
+ ___block_descriptor_tmp.1934
+ ___block_descriptor_tmp.1935
+ ___block_descriptor_tmp.1944
+ ___block_descriptor_tmp.1948
+ ___block_descriptor_tmp.1952
+ ___block_descriptor_tmp.1954
+ ___block_descriptor_tmp.1956
+ ___block_descriptor_tmp.1957
+ ___block_descriptor_tmp.196
+ ___block_descriptor_tmp.1977
+ ___block_descriptor_tmp.198.15775
+ ___block_descriptor_tmp.1980
+ ___block_descriptor_tmp.1981
+ ___block_descriptor_tmp.199
+ ___block_descriptor_tmp.2.16874
+ ___block_descriptor_tmp.2.5616
+ ___block_descriptor_tmp.2.5689
+ ___block_descriptor_tmp.2.5830
+ ___block_descriptor_tmp.2.8147
+ ___block_descriptor_tmp.2.9532
+ ___block_descriptor_tmp.20.13302
+ ___block_descriptor_tmp.20.15266
+ ___block_descriptor_tmp.20.4340
+ ___block_descriptor_tmp.2003
+ ___block_descriptor_tmp.2007
+ ___block_descriptor_tmp.2018
+ ___block_descriptor_tmp.2019
+ ___block_descriptor_tmp.2020
+ ___block_descriptor_tmp.205
+ ___block_descriptor_tmp.21.11465
+ ___block_descriptor_tmp.21.11954
+ ___block_descriptor_tmp.2108
+ ___block_descriptor_tmp.2109
+ ___block_descriptor_tmp.2125
+ ___block_descriptor_tmp.2128
+ ___block_descriptor_tmp.2131
+ ___block_descriptor_tmp.2137
+ ___block_descriptor_tmp.2146
+ ___block_descriptor_tmp.22.14232
+ ___block_descriptor_tmp.22.16902
+ ___block_descriptor_tmp.225
+ ___block_descriptor_tmp.226.15329
+ ___block_descriptor_tmp.23.16052
+ ___block_descriptor_tmp.23.4362
+ ___block_descriptor_tmp.23.9249
+ ___block_descriptor_tmp.230
+ ___block_descriptor_tmp.231
+ ___block_descriptor_tmp.24.15263
+ ___block_descriptor_tmp.24.1533
+ ___block_descriptor_tmp.24.4361
+ ___block_descriptor_tmp.25.11469
+ ___block_descriptor_tmp.25.11963
+ ___block_descriptor_tmp.25.16731
+ ___block_descriptor_tmp.26.13695
+ ___block_descriptor_tmp.26.16084
+ ___block_descriptor_tmp.26.16732
+ ___block_descriptor_tmp.27.16089
+ ___block_descriptor_tmp.27.3598
+ ___block_descriptor_tmp.27.5884
+ ___block_descriptor_tmp.2729
+ ___block_descriptor_tmp.28.10435
+ ___block_descriptor_tmp.28.1101
+ ___block_descriptor_tmp.28.13697
+ ___block_descriptor_tmp.28.1536
+ ___block_descriptor_tmp.28.15477
+ ___block_descriptor_tmp.28.16090
+ ___block_descriptor_tmp.28.4367
+ ___block_descriptor_tmp.28.6665
+ ___block_descriptor_tmp.28.8793
+ ___block_descriptor_tmp.2893
+ ___block_descriptor_tmp.29.11968
+ ___block_descriptor_tmp.29.1542
+ ___block_descriptor_tmp.29.4366
+ ___block_descriptor_tmp.29.7932
+ ___block_descriptor_tmp.299
+ ___block_descriptor_tmp.3.16612
+ ___block_descriptor_tmp.3.9538
+ ___block_descriptor_tmp.30.11971
+ ___block_descriptor_tmp.30.16127
+ ___block_descriptor_tmp.30.16624
+ ___block_descriptor_tmp.309.8466
+ ___block_descriptor_tmp.31.14717
+ ___block_descriptor_tmp.31.2145
+ ___block_descriptor_tmp.31.5177
+ ___block_descriptor_tmp.31.8154
+ ___block_descriptor_tmp.310
+ ___block_descriptor_tmp.3124
+ ___block_descriptor_tmp.32.2148
+ ___block_descriptor_tmp.33.13680
+ ___block_descriptor_tmp.33.14718
+ ___block_descriptor_tmp.33.15466
+ ___block_descriptor_tmp.33.16125
+ ___block_descriptor_tmp.33.4370
+ ___block_descriptor_tmp.33.4694
+ ___block_descriptor_tmp.34.14719
+ ___block_descriptor_tmp.34.16626
+ ___block_descriptor_tmp.34.4369
+ ___block_descriptor_tmp.34.4932
+ ___block_descriptor_tmp.35.5172
+ ___block_descriptor_tmp.35.8158
+ ___block_descriptor_tmp.357
+ ___block_descriptor_tmp.3579
+ ___block_descriptor_tmp.358
+ ___block_descriptor_tmp.36.15464
+ ___block_descriptor_tmp.36.16135
+ ___block_descriptor_tmp.36.3662
+ ___block_descriptor_tmp.363
+ ___block_descriptor_tmp.37.16143
+ ___block_descriptor_tmp.38
+ ___block_descriptor_tmp.381
+ ___block_descriptor_tmp.39.14724
+ ___block_descriptor_tmp.39.15462
+ ___block_descriptor_tmp.39.1554
+ ___block_descriptor_tmp.3950
+ ___block_descriptor_tmp.4.1436
+ ___block_descriptor_tmp.4.16616
+ ___block_descriptor_tmp.4.5678
+ ___block_descriptor_tmp.4.5831
+ ___block_descriptor_tmp.4.9541
+ ___block_descriptor_tmp.40.1108
+ ___block_descriptor_tmp.40.16141
+ ___block_descriptor_tmp.40.2730
+ ___block_descriptor_tmp.41.1567
+ ___block_descriptor_tmp.41.5189
+ ___block_descriptor_tmp.411.10168
+ ___block_descriptor_tmp.4169
+ ___block_descriptor_tmp.42.13712
+ ___block_descriptor_tmp.42.1570
+ ___block_descriptor_tmp.4343
+ ___block_descriptor_tmp.44.15460
+ ___block_descriptor_tmp.44.1578
+ ___block_descriptor_tmp.45.2749
+ ___block_descriptor_tmp.4519
+ ___block_descriptor_tmp.4553
+ ___block_descriptor_tmp.46.13707
+ ___block_descriptor_tmp.47.16155
+ ___block_descriptor_tmp.4756
+ ___block_descriptor_tmp.4793
+ ___block_descriptor_tmp.48.13710
+ ___block_descriptor_tmp.48.15458
+ ___block_descriptor_tmp.48.16156
+ ___block_descriptor_tmp.48.9626
+ ___block_descriptor_tmp.49.16159
+ ___block_descriptor_tmp.5.8148
+ ___block_descriptor_tmp.51.14735
+ ___block_descriptor_tmp.51.8055
+ ___block_descriptor_tmp.51.9623
+ ___block_descriptor_tmp.5122
+ ___block_descriptor_tmp.5158
+ ___block_descriptor_tmp.52.13715
+ ___block_descriptor_tmp.52.1428
+ ___block_descriptor_tmp.52.2758
+ ___block_descriptor_tmp.52.7427
+ ___block_descriptor_tmp.53.14736
+ ___block_descriptor_tmp.537.8393
+ ___block_descriptor_tmp.5398
+ ___block_descriptor_tmp.54.15552
+ ___block_descriptor_tmp.54.8062
+ ___block_descriptor_tmp.54.9315
+ ___block_descriptor_tmp.543
+ ___block_descriptor_tmp.55.14721
+ ___block_descriptor_tmp.5548
+ ___block_descriptor_tmp.5592
+ ___block_descriptor_tmp.56.8056
+ ___block_descriptor_tmp.5677
+ ___block_descriptor_tmp.57.13726
+ ___block_descriptor_tmp.57.14722
+ ___block_descriptor_tmp.57.15551
+ ___block_descriptor_tmp.573
+ ___block_descriptor_tmp.5829
+ ___block_descriptor_tmp.589
+ ___block_descriptor_tmp.59.2760
+ ___block_descriptor_tmp.59.5984
+ ___block_descriptor_tmp.6.1466
+ ___block_descriptor_tmp.6.4517
+ ___block_descriptor_tmp.6.4560
+ ___block_descriptor_tmp.6.5115
+ ___block_descriptor_tmp.6.5680
+ ___block_descriptor_tmp.6.5836
+ ___block_descriptor_tmp.60.15549
+ ___block_descriptor_tmp.60.3038
+ ___block_descriptor_tmp.60.5985
+ ___block_descriptor_tmp.6125
+ ___block_descriptor_tmp.62.14343
+ ___block_descriptor_tmp.62.16845
+ ___block_descriptor_tmp.63.14342
+ ___block_descriptor_tmp.63.16184
+ ___block_descriptor_tmp.636
+ ___block_descriptor_tmp.64.14770
+ ___block_descriptor_tmp.64.4778
+ ___block_descriptor_tmp.643
+ ___block_descriptor_tmp.648.9804
+ ___block_descriptor_tmp.65.15530
+ ___block_descriptor_tmp.65.16286
+ ___block_descriptor_tmp.65.4597
+ ___block_descriptor_tmp.6511
+ ___block_descriptor_tmp.655.8465
+ ___block_descriptor_tmp.6588
+ ___block_descriptor_tmp.66.14341
+ ___block_descriptor_tmp.6757
+ ___block_descriptor_tmp.68.9388
+ ___block_descriptor_tmp.7.11428
+ ___block_descriptor_tmp.7.1469
+ ___block_descriptor_tmp.7.4167
+ ___block_descriptor_tmp.7.4557
+ ___block_descriptor_tmp.7.5117
+ ___block_descriptor_tmp.7.5833
+ ___block_descriptor_tmp.70.14405
+ ___block_descriptor_tmp.71
+ ___block_descriptor_tmp.71.9387
+ ___block_descriptor_tmp.7199
+ ___block_descriptor_tmp.72.5953
+ ___block_descriptor_tmp.7298
+ ___block_descriptor_tmp.74.6323
+ ___block_descriptor_tmp.759
+ ___block_descriptor_tmp.76.16309
+ ___block_descriptor_tmp.76.7985
+ ___block_descriptor_tmp.774
+ ___block_descriptor_tmp.7829
+ ___block_descriptor_tmp.7874
+ ___block_descriptor_tmp.79
+ ___block_descriptor_tmp.8.12112
+ ___block_descriptor_tmp.8.16324
+ ___block_descriptor_tmp.8.2125
+ ___block_descriptor_tmp.8.4231
+ ___block_descriptor_tmp.8.8194
+ ___block_descriptor_tmp.801
+ ___block_descriptor_tmp.804.8463
+ ___block_descriptor_tmp.807
+ ___block_descriptor_tmp.810
+ ___block_descriptor_tmp.811
+ ___block_descriptor_tmp.8120
+ ___block_descriptor_tmp.813.8464
+ ___block_descriptor_tmp.8184
+ ___block_descriptor_tmp.8205
+ ___block_descriptor_tmp.83.15576
+ ___block_descriptor_tmp.834
+ ___block_descriptor_tmp.841
+ ___block_descriptor_tmp.844
+ ___block_descriptor_tmp.85.3067
+ ___block_descriptor_tmp.85.9404
+ ___block_descriptor_tmp.862
+ ___block_descriptor_tmp.866
+ ___block_descriptor_tmp.867
+ ___block_descriptor_tmp.87
+ ___block_descriptor_tmp.8744
+ ___block_descriptor_tmp.878.8392
+ ___block_descriptor_tmp.879
+ ___block_descriptor_tmp.880
+ ___block_descriptor_tmp.8806
+ ___block_descriptor_tmp.881
+ ___block_descriptor_tmp.89.9405
+ ___block_descriptor_tmp.895
+ ___block_descriptor_tmp.9.14984
+ ___block_descriptor_tmp.9.16832
+ ___block_descriptor_tmp.9.5620
+ ___block_descriptor_tmp.9.5890
+ ___block_descriptor_tmp.9.8480
+ ___block_descriptor_tmp.90.7964
+ ___block_descriptor_tmp.901
+ ___block_descriptor_tmp.904
+ ___block_descriptor_tmp.9106
+ ___block_descriptor_tmp.918
+ ___block_descriptor_tmp.920
+ ___block_descriptor_tmp.9202
+ ___block_descriptor_tmp.921
+ ___block_descriptor_tmp.922
+ ___block_descriptor_tmp.923
+ ___block_descriptor_tmp.924
+ ___block_descriptor_tmp.938
+ ___block_descriptor_tmp.945
+ ___block_descriptor_tmp.9528
+ ___block_descriptor_tmp.954
+ ___block_descriptor_tmp.956
+ ___block_descriptor_tmp.9584
+ ___block_descriptor_tmp.962
+ ___block_descriptor_tmp.963.8460
+ ___block_descriptor_tmp.97
+ ___block_descriptor_tmp.972.8462
+ ___block_descriptor_tmp.974
+ ___block_descriptor_tmp.976
+ ___block_descriptor_tmp.98
+ ___block_descriptor_tmp.980
+ ___block_descriptor_tmp.9816
+ ___block_descriptor_tmp.983
+ ___block_descriptor_tmp.987.8461
+ ___block_descriptor_tmp.99
+ ___block_descriptor_tmp.99.15821
+ ___block_descriptor_tmp.990
+ ___block_descriptor_tmp.996
+ ___block_literal_global.101
+ ___block_literal_global.1020
+ ___block_literal_global.104
+ ___block_literal_global.10442
+ ___block_literal_global.1055
+ ___block_literal_global.1071
+ ___block_literal_global.1077
+ ___block_literal_global.1087
+ ___block_literal_global.1089
+ ___block_literal_global.1092
+ ___block_literal_global.10931
+ ___block_literal_global.11.14978
+ ___block_literal_global.11.1869
+ ___block_literal_global.1104
+ ___block_literal_global.1107
+ ___block_literal_global.11307
+ ___block_literal_global.1132
+ ___block_literal_global.1138
+ ___block_literal_global.114.16162
+ ___block_literal_global.11403
+ ___block_literal_global.1141
+ ___block_literal_global.11522
+ ___block_literal_global.117.17334
+ ___block_literal_global.1179
+ ___block_literal_global.1182
+ ___block_literal_global.1210
+ ___block_literal_global.12120
+ ___block_literal_global.1213
+ ___block_literal_global.12144
+ ___block_literal_global.127
+ ___block_literal_global.129
+ ___block_literal_global.132
+ ___block_literal_global.13361
+ ___block_literal_global.13676
+ ___block_literal_global.137
+ ___block_literal_global.14.11433
+ ___block_literal_global.14.16657
+ ___block_literal_global.142
+ ___block_literal_global.14230
+ ___block_literal_global.14446
+ ___block_literal_global.145
+ ___block_literal_global.146
+ ___block_literal_global.1464
+ ___block_literal_global.14658
+ ___block_literal_global.1480
+ ___block_literal_global.14944
+ ___block_literal_global.15.16014
+ ___block_literal_global.15.5603
+ ___block_literal_global.15.6592
+ ___block_literal_global.15257
+ ___block_literal_global.16.6737
+ ___block_literal_global.16008
+ ___block_literal_global.16330
+ ___block_literal_global.16342
+ ___block_literal_global.16610
+ ___block_literal_global.16859
+ ___block_literal_global.16981
+ ___block_literal_global.17.1093
+ ___block_literal_global.17.2167
+ ___block_literal_global.17386
+ ___block_literal_global.18.11439
+ ___block_literal_global.18.8132
+ ___block_literal_global.1828
+ ___block_literal_global.1865
+ ___block_literal_global.1921
+ ___block_literal_global.1971
+ ___block_literal_global.201.15806
+ ___block_literal_global.21.13689
+ ___block_literal_global.21.16049
+ ___block_literal_global.2122
+ ___block_literal_global.2139
+ ___block_literal_global.2148
+ ___block_literal_global.22.15258
+ ___block_literal_global.23.11463
+ ___block_literal_global.233
+ ___block_literal_global.25.16050
+ ___block_literal_global.26.15259
+ ___block_literal_global.26.4359
+ ___block_literal_global.2668
+ ___block_literal_global.27.11467
+ ___block_literal_global.2727
+ ___block_literal_global.2891
+ ___block_literal_global.29.5851
+ ___block_literal_global.30.15445
+ ___block_literal_global.3036
+ ___block_literal_global.31.4364
+ ___block_literal_global.32.16122
+ ___block_literal_global.32.16621
+ ___block_literal_global.32.17405
+ ___block_literal_global.323
+ ___block_literal_global.33.5169
+ ___block_literal_global.33.8152
+ ___block_literal_global.35.13677
+ ___block_literal_global.35.1483
+ ___block_literal_global.35.15450
+ ___block_literal_global.35.16123
+ ___block_literal_global.35.4655
+ ___block_literal_global.360
+ ___block_literal_global.3691
+ ___block_literal_global.37.5170
+ ___block_literal_global.37.8156
+ ___block_literal_global.38.15451
+ ___block_literal_global.39.16138
+ ___block_literal_global.4.5598
+ ___block_literal_global.4.8145
+ ___block_literal_global.4070
+ ___block_literal_global.41.15452
+ ___block_literal_global.42.16139
+ ___block_literal_global.4229
+ ___block_literal_global.4292
+ ___block_literal_global.43.5186
+ ___block_literal_global.4338
+ ___block_literal_global.4523
+ ___block_literal_global.4554
+ ___block_literal_global.46
+ ___block_literal_global.4771
+ ___block_literal_global.484
+ ___block_literal_global.486
+ ___block_literal_global.50.15455
+ ___block_literal_global.50.9611
+ ___block_literal_global.51.13714
+ ___block_literal_global.51.16157
+ ___block_literal_global.5156
+ ___block_literal_global.53.9612
+ ___block_literal_global.533
+ ___block_literal_global.539
+ ___block_literal_global.5546
+ ___block_literal_global.5590
+ ___block_literal_global.5832
+ ___block_literal_global.59.15505
+ ___block_literal_global.6.16614
+ ___block_literal_global.6123
+ ___block_literal_global.638
+ ___block_literal_global.64
+ ___block_literal_global.645
+ ___block_literal_global.65.17397
+ ___block_literal_global.650
+ ___block_literal_global.6509
+ ___block_literal_global.6586
+ ___block_literal_global.67.15510
+ ___block_literal_global.67.16245
+ ___block_literal_global.6721
+ ___block_literal_global.711
+ ___block_literal_global.7223
+ ___block_literal_global.73
+ ___block_literal_global.7438
+ ___block_literal_global.76
+ ___block_literal_global.806
+ ___block_literal_global.8118
+ ___block_literal_global.8203
+ ___block_literal_global.831
+ ___block_literal_global.8742
+ ___block_literal_global.8755
+ ___block_literal_global.881
+ ___block_literal_global.9.11426
+ ___block_literal_global.9.4555
+ ___block_literal_global.9247
+ ___block_literal_global.94.7804
+ ___block_literal_global.947
+ ___block_literal_global.9563
+ ___block_literal_global.9814
+ ___block_literal_global.982
+ ___block_literal_global.985
+ ___block_literal_global.989
+ ___block_literal_global.992
+ ___db2_get_datastore_with_ctx_block_invoke.63
+ ___db2_update_datastore_state_block_invoke.32
+ ___db2_update_datastore_state_block_invoke.43
+ ___db2_update_datastore_state_block_invoke_2.47
+ ___flush_updateset_locked_block_invoke.154
+ ___isAppleInternalInstall_block_invoke.13727
+ ___message_assert.11545
+ ___message_assert.11781
+ ___message_assert.12111
+ ___message_assert.13240
+ ___message_assert.13285
+ ___message_assert.13343
+ ___message_assert.13753
+ ___message_assert.14048
+ ___message_assert.14107
+ ___message_assert.14167
+ ___message_assert.1422
+ ___message_assert.14226
+ ___message_assert.14675
+ ___message_assert.14807
+ ___message_assert.14955
+ ___message_assert.15198
+ ___message_assert.1596
+ ___message_assert.15973
+ ___message_assert.16399
+ ___message_assert.16636
+ ___message_assert.1732
+ ___message_assert.17690
+ ___message_assert.2211
+ ___message_assert.2916
+ ___message_assert.3138
+ ___message_assert.3159
+ ___message_assert.3339
+ ___message_assert.3442
+ ___message_assert.3910
+ ___message_assert.3971
+ ___message_assert.4135
+ ___message_assert.4319
+ ___message_assert.4333
+ ___message_assert.4393
+ ___message_assert.4552
+ ___message_assert.4736
+ ___message_assert.4765
+ ___message_assert.5154
+ ___message_assert.6131
+ ___message_assert.6471
+ ___message_assert.6557
+ ___message_assert.6776
+ ___message_assert.7195
+ ___message_assert.7287
+ ___message_assert.7850
+ ___message_assert.7881
+ ___message_assert.8088
+ ___message_assert.8680
+ ___message_assert.8705
+ ___message_assert.8765
+ ___message_assert.9006
+ ___message_assert.9145
+ ___message_assert.9178
+ ___message_assert.9608
+ ___message_assert.9845
+ ___path_bundle_index_block_invoke.10448
+ ___prepareForTransaction_block_invoke.1946
+ ___processOneCS_block_invoke.1449
+ ___setCSAttributes2_block_invoke.1915
+ ___setCSAttributes2_block_invoke.1918
+ ___si_assert_copy_extra.11541
+ ___si_assert_copy_extra.11779
+ ___si_assert_copy_extra.12107
+ ___si_assert_copy_extra.13235
+ ___si_assert_copy_extra.13280
+ ___si_assert_copy_extra.13339
+ ___si_assert_copy_extra.13749
+ ___si_assert_copy_extra.14044
+ ___si_assert_copy_extra.14103
+ ___si_assert_copy_extra.14162
+ ___si_assert_copy_extra.1417
+ ___si_assert_copy_extra.14221
+ ___si_assert_copy_extra.14670
+ ___si_assert_copy_extra.14802
+ ___si_assert_copy_extra.14950
+ ___si_assert_copy_extra.15191
+ ___si_assert_copy_extra.1592
+ ___si_assert_copy_extra.15969
+ ___si_assert_copy_extra.16395
+ ___si_assert_copy_extra.16631
+ ___si_assert_copy_extra.1727
+ ___si_assert_copy_extra.17625
+ ___si_assert_copy_extra.2206
+ ___si_assert_copy_extra.2911
+ ___si_assert_copy_extra.3134
+ ___si_assert_copy_extra.3155
+ ___si_assert_copy_extra.3334
+ ___si_assert_copy_extra.3437
+ ___si_assert_copy_extra.3906
+ ___si_assert_copy_extra.3967
+ ___si_assert_copy_extra.4130
+ ___si_assert_copy_extra.4315
+ ___si_assert_copy_extra.4329
+ ___si_assert_copy_extra.4388
+ ___si_assert_copy_extra.4547
+ ___si_assert_copy_extra.4732
+ ___si_assert_copy_extra.4760
+ ___si_assert_copy_extra.5149
+ ___si_assert_copy_extra.6127
+ ___si_assert_copy_extra.6466
+ ___si_assert_copy_extra.6552
+ ___si_assert_copy_extra.6772
+ ___si_assert_copy_extra.7191
+ ___si_assert_copy_extra.7283
+ ___si_assert_copy_extra.7846
+ ___si_assert_copy_extra.7876
+ ___si_assert_copy_extra.8084
+ ___si_assert_copy_extra.8677
+ ___si_assert_copy_extra.8700
+ ___si_assert_copy_extra.8760
+ ___si_assert_copy_extra.9001
+ ___si_assert_copy_extra.9140
+ ___si_assert_copy_extra.9173
+ ___si_assert_copy_extra.9604
+ ___si_assert_copy_extra.9840
+ ___si_set_scan_count_block_invoke.1951
+ ___si_set_scan_count_block_invoke_2.1953
+ ___si_set_scan_count_block_invoke_3.1955
+ ___writeDBOToPlistBytes_block_invoke.69
+ __page_fetch_with_fd._crashCount.210
+ __page_fetch_with_fd._crashCount.212
+ __psid_insert.5229
+ _bit_vector_create.16589
+ _bit_vector_create.17722
+ _bit_vector_init.4871
+ _bit_vector_internal_touch_for_set.4908
+ _bit_vector_set.14141
+ _bit_vector_set.16533
+ _bit_vector_set.17686
+ _bit_vector_set.2971
+ _bit_vector_set.3612
+ _bit_vector_set.4456
+ _bit_vector_set.5048
+ _bit_vector_set.7395
+ _bit_vector_set_bits.4915
+ _checkNearness.14791
+ _commonHash.12034
+ _commonHash.17624
+ _data_entry_store.17594
+ _deleteDocument._COUNT_.78
+ _dirfd
+ _emitTerms.7956
+ _gAnalytics
+ _gAnalyticsQueue
+ _getLegacyPCEnum
+ _getLockForPCPriority
+ _getPrefixForPCPriority
+ _getPrefixForProtectionClass
+ _getPrefixForShorthand
+ _getSize.memSize.12105
+ _getSize.memSize.14236
+ _getSize.memSize.4776
+ _get_string_and_length_for_id.15651
+ _hash64.8048
+ _index_comp.12119
+ _index_comp.14242
+ _index_comp.4782
+ _isAppleInternalInstall.isInternalInstall.13722
+ _isAppleInternalInstall.onceToken.13721
+ _keycompare.5214
+ _localizedFieldTermMatch.14740
+ _log_map_access_error.16456
+ _log_map_access_error.17567
+ _log_map_access_error.7343
+ _master_fid_rec.5198
+ _master_fid_rec_size.5200
+ _objc_msgSend$appendFormat:
+ _objc_msgSend$copyHeartbeatData
+ _objc_msgSend$createDropDataForPrefix:path:error:
+ _objc_msgSend$createHeartbeatDataWithRefresh:error:
+ _objc_msgSend$description
+ _objc_msgSend$errorWithDomain:code:userInfo:
+ _objc_msgSend$eventCount
+ _objc_msgSend$getCurrentSpotlightVersionWithRoots:
+ _objc_msgSend$getIndexDataForPrefix:
+ _objc_msgSend$getPreviousBuild
+ _objc_msgSend$hasSpotlightRoots
+ _objc_msgSend$initWithBool:
+ _objc_msgSend$initWithCString:encoding:
+ _objc_msgSend$initWithFormat:
+ _objc_msgSend$initWithLong:
+ _objc_msgSend$initWithPrefix:
+ _objc_msgSend$initWithSuiteName:
+ _objc_msgSend$initWithUnsignedInt:
+ _objc_msgSend$initWithUnsignedLongLong:
+ _objc_msgSend$initializeSharedHearbeatFields
+ _objc_msgSend$isHeartbeatReportingDisabled
+ _objc_msgSend$isIndexDropReportingDisabled
+ _objc_msgSend$migrateFromLegacyHeartbeatData:
+ _objc_msgSend$populateIndexDropData:index:prefix:reason:error:
+ _objc_msgSend$processInfo
+ _objc_msgSend$processName
+ _objc_msgSend$readFromHeartbeatFileWithError:
+ _objc_msgSend$recordDrop:
+ _objc_msgSend$recordOpen:dirty:
+ _objc_msgSend$recordOpen:forIndex:dirty:
+ _objc_msgSend$recordRequestedAdds:updates:deletes:
+ _objc_msgSend$recordRequestsForIndex:adds:updates:deletes:
+ _objc_msgSend$refreshHeartbeatDataWithIndex:path:errors:
+ _objc_msgSend$refreshSharedHeartbeatFieldsWithError:
+ _objc_msgSend$removeItemAtPath:error:
+ _objc_msgSend$removeObjectForKey:
+ _objc_msgSend$resetAfterHeartbeat
+ _objc_msgSend$runCommand:
+ _objc_msgSend$sendHeartbeatEvent
+ _objc_msgSend$sendHeartbeatEventWithData:withReset:
+ _objc_msgSend$sendIndexDropEventWithCorruptIndex:prefix:path:readOnly:reason:
+ _objc_msgSend$sendIndexDropEventWithData:
+ _objc_msgSend$sendLegacyHeartbeatEventWithData:
+ _objc_msgSend$sendLegacyIndexDropEventWithData:prefix:readOnly:reason:
+ _objc_msgSend$sendVectorIndexDropForIndex:vectorCount:readOnly:prefix:propertyName:dropReason:
+ _objc_msgSend$setDateFormat:
+ _objc_msgSend$setHeartbeatTimestamp:prefix:key:
+ _objc_msgSend$setPurgeTimestamp:prefix:start:
+ _objc_msgSend$setPurgeability:
+ _objc_msgSend$setPurgeability:prefix:
+ _objc_msgSend$setSpotlightVersion
+ _objc_msgSend$setTimestamp:key:
+ _objc_msgSend$sharedInstance
+ _objc_msgSend$shouldReportIndexDrop:
+ _objc_msgSend$stringFromDate:
+ _objc_msgSend$timeIntervalSince1970
+ _objc_msgSend$unsignedLongLongValue
+ _objc_msgSend$updateWithData:
+ _objc_msgSend$usageInfoForCommand:
+ _objc_msgSend$writeToHeartbeatFileWithError:
+ _objc_release
+ _objc_release_x19
+ _objc_release_x23
+ _oqpush.14265
+ _oqpush.3494
+ _oqpush.4796
+ _packingCount.14411
+ _path_bundle_index.sDummyFD.10443
+ _pqDisposeApplier.7951
+ _psid_lookup.5227
+ _qsort_cached_allocations.12103
+ _qsort_cached_allocations.14234
+ _qsort_cached_allocations.4774
+ _query_realloc.9150
+ _readCompactPosition.14415
+ _reassignDocument._COUNT_.80
+ _remapping_keys.12084
+ _restoreVInt32.13259
+ _restoreVInt32.3565
+ _restoreVInt32.4142
+ _sDataMapExceptionCallbacks.16410
+ _sDataMapExceptionCallbacks.17542
+ _sIndexLock
+ _sIndexLockInit
+ _sRefs
+ _sRefsLock
+ _sSpotlightVersion.7177
+ _sTotal.14289
+ _sTotal.14669
+ _sTotal.15162
+ _sTotal.15966
+ _sTotal.4751
+ _sTotal.5155
+ _sTotal.6145
+ _sTotal.6546
+ _sTotal.9155
+ _sTotal.9603
+ _sTotal.9778
+ _sendIndexDropEventWithCorruptIndex:prefix:path:readOnly:reason:.spid
+ _setBool
+ _setDocumentAttributes._COUNT_.69
+ _setDocumentAttributes._COUNT_.71
+ _setLong
+ _setSpotlightVersion.onceToken
+ _setString
+ _setUInt32
+ _setUInt64
+ _si_analytics_log.14972
+ _si_analytics_log.15385
+ _si_analytics_log.16448
+ _si_analytics_log.17628
+ _si_analytics_log.2957
+ _si_analytics_log.3342
+ _si_analytics_log.3850
+ _si_analytics_log.3932
+ _si_analytics_log.4461
+ _si_analytics_log.4982
+ _si_analytics_log.6477
+ _si_analytics_log.7338
+ _si_analytics_log.7910
+ _si_analytics_log.8881
+ _si_analytics_log.9215
+ _si_rwlock_wrunlock.3805
+ _storeVInt64.14122
+ _storeVInt64.4410
+ _store_stream_read_bytes.14209
+ _store_stream_read_bytes.3611
+ _store_stream_read_bytes.4606
+ _store_stream_read_bytes.5099
+ _store_stream_read_bytes.708
+ _store_stream_read_bytes.7103
+ _store_stream_read_vint32.14205
+ _store_stream_read_vint32.3608
+ _store_stream_read_vint32.4604
+ _store_stream_read_vint32.707
+ _store_stream_read_vint32.7099
+ _store_stream_write_bytes.14215
+ _store_stream_write_bytes.3470
+ _store_stream_write_bytes.4594
+ _store_stream_write_bytes.5103
+ _store_stream_write_bytes.7091
+ _store_stream_write_vint32.14212
+ _store_stream_write_vint32.3472
+ _store_stream_write_vint32.4595
+ _store_stream_write_vint32.7092
+ _strHash.17916
+ _sysctlbyname
+ _table_extra_bytes.15249
+ _takeBuddyPage.4447
+ _termPropertyID.14741
+ _thread_count.12104
+ _thread_count.14235
+ _thread_count.4775
+ _timeSinceBoot
+ _v2_readVInt32.4622
+ _v2_readVInt64.11611
+ _v2_readVInt64.14403
+ _v2_readVInt64.14786
+ _v2_readVInt64.14828
+ _v2_readVInt64.3079
+ _v2_readVInt64.3398
+ _v2_readVInt64.4617
+ _v2_readVInt64.8032
+ _v2_writeVInt64.11568
+ _v2_writeVInt64.14217
+ _v2_writeVInt64.3368
+ _vector_dimension.vec_sizes.16058
+ _vector_size.elem_sizes.16057
+ _writeVInt64.14214
+ _writeVInt64.14841
+ _writeVInt64.3934
+ _writeVInt64.4596
+ _writeVInt64.4869
+ _writeVInt64.6474
- +[SIAnalytics setResourcesCallback:]
- -[SIAnalytics droppedIndexDataWithError:]
- -[SIAnalytics heartbeatAnalyticsDataWithReset:error:]
- -[SIAnalytics incrementPerIndexHeartbeatCount:forKey:withError:]
- -[SIAnalytics indexDropAnalyticsDataFromDroppedIndexData:withError:]
- -[SIAnalytics indexDropType:]
- -[SIAnalytics initWithParentDirectoryPath:corespotlight:heartbeatIndex:]
- -[SIAnalytics refreshPerIndexHeartbeatFieldsForIndex:protectionClass:withError:]
- -[SIAnalytics setPerIndexHeartbeatTimestamp:forKey:withError:]
- -[SIAnalytics setSharedHeartbeatTimestamp:forKey:withError:]
- -[SIAnalyticsIndexData heartbeatData]
- -[SIAnalyticsIndexData incrementCount:forKey:]
- -[SIAnalyticsIndexData initWithPrefix:data:]
- -[SIAnalyticsIndexData setTimestamp:forKey:]
- GCC_except_table1516
- GCC_except_table1518
- GCC_except_table1526
- GCC_except_table1529
- GCC_except_table1596
- GCC_except_table1764
- GCC_except_table1767
- GCC_except_table1801
- GCC_except_table2313
- GCC_except_table2324
- GCC_except_table2325
- GCC_except_table2328
- GCC_except_table2738
- GCC_except_table3497
- GCC_except_table3498
- GCC_except_table3499
- GCC_except_table3500
- GCC_except_table3501
- GCC_except_table3502
- GCC_except_table3503
- GCC_except_table3504
- GCC_except_table3505
- GCC_except_table3506
- GCC_except_table3507
- GCC_except_table3508
- GCC_except_table3509
- GCC_except_table3515
- GCC_except_table3525
- GCC_except_table3526
- GCC_except_table3528
- GCC_except_table3532
- GCC_except_table3545
- GCC_except_table3550
- GCC_except_table3555
- GCC_except_table3556
- GCC_except_table3559
- GCC_except_table3560
- GCC_except_table3561
- GCC_except_table3562
- GCC_except_table3565
- GCC_except_table3566
- GCC_except_table3567
- GCC_except_table5397
- GCC_except_table5399
- GCC_except_table5860
- GCC_except_table5862
- GCC_except_table5864
- GCC_except_table5866
- GCC_except_table5868
- GCC_except_table5870
- GCC_except_table5874
- GCC_except_table5877
- GCC_except_table5880
- GCC_except_table5883
- GCC_except_table5885
- GCC_except_table5892
- GCC_except_table5893
- GCC_except_table5895
- GCC_except_table5897
- GCC_except_table5906
- GCC_except_table5907
- GCC_except_table5908
- GCC_except_table5912
- GCC_except_table5924
- GCC_except_table5925
- GCC_except_table5926
- GCC_except_table5927
- GCC_except_table5928
- GCC_except_table5929
- GCC_except_table5930
- GCC_except_table5931
- GCC_except_table5932
- GCC_except_table5933
- GCC_except_table5934
- GCC_except_table5935
- GCC_except_table5936
- GCC_except_table5951
- GCC_except_table5953
- GCC_except_table5954
- GCC_except_table5955
- GCC_except_table5964
- GCC_except_table5966
- GCC_except_table5968
- GCC_except_table5983
- GCC_except_table5984
- GCC_except_table5985
- GCC_except_table5986
- GCC_except_table5987
- GCC_except_table6051
- GCC_except_table6054
- GCC_except_table6055
- GCC_except_table6056
- GCC_except_table6057
- GCC_except_table6253
- GCC_except_table6290
- GCC_except_table6291
- GCC_except_table6292
- GCC_except_table6293
- GCC_except_table6299
- GCC_except_table6303
- GCC_except_table6306
- GCC_except_table6307
- GCC_except_table6308
- GCC_except_table6309
- GCC_except_table6310
- GCC_except_table6312
- GCC_except_table6313
- GCC_except_table6316
- GCC_except_table6317
- GCC_except_table6318
- GCC_except_table6319
- GCC_except_table6320
- GCC_except_table6321
- GCC_except_table6322
- GCC_except_table6323
- GCC_except_table6324
- GCC_except_table6325
- GCC_except_table6326
- GCC_except_table6327
- GCC_except_table6328
- GCC_except_table6329
- GCC_except_table6330
- GCC_except_table6340
- GCC_except_table6341
- GCC_except_table6342
- GCC_except_table6343
- GCC_except_table6344
- GCC_except_table6345
- GCC_except_table6346
- GCC_except_table6347
- GCC_except_table6348
- GCC_except_table6349
- GCC_except_table6350
- GCC_except_table6351
- GCC_except_table6352
- GCC_except_table6354
- GCC_except_table6368
- GCC_except_table6370
- GCC_except_table6382
- GCC_except_table6566
- GCC_except_table7268
- GCC_except_table7269
- GCC_except_table7277
- GCC_except_table7279
- GCC_except_table7280
- GCC_except_table7282
- GCC_except_table7289
- GCC_except_table7293
- GCC_except_table7296
- GCC_except_table7297
- GCC_except_table7298
- GCC_except_table7299
- GCC_except_table7300
- GCC_except_table7302
- GCC_except_table7321
- GCC_except_table7323
- GCC_except_table7324
- GCC_except_table7326
- GCC_except_table7327
- GCC_except_table7330
- GCC_except_table7331
- GCC_except_table7332
- _FlatStorePageEntryWrite2.3163
- _MurmurHash3_x86_32.16803
- _SIGetPreviousError
- _SIGetRebuildReason
- __PayloadWriteData.3709
- __SIGetFieldNameForId
- __SISetVectorIndexDropCallback
- __ZGVZL12MetadataKeysvE13_metadataKeys.16751
- __ZGVZL17GenericFilterKeysvE18_genericFilterKeys.16770
- __ZGVZL18PhRetrievalAttribsvE17_retrievalAttribs.16471
- __ZGVZL25GenericFilterTopLevelKeysvE26_genericFilterTopLevelKeys.16762
- __ZGVZL26PhExactMatchRankingAttribsvE27_phExactMatchRankingAttribs.16654
- __ZL10commonHashjPKhj.15714
- __ZL11MAX_OIDINFO.16209
- __ZL11TOK_ID_FROM.4081
- __ZL12ZERO_OIDINFO.16208
- __ZL13PhAttribNodesPKcRKNSt3__113unordered_setINS1_12basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEENS1_4hashIS8_EENS1_8equal_toIS8_EENS6_IS8_EEEEbb.16514
- __ZL13v2_readVInt64PKhPm.8717
- __ZL13v2_readVInt64RPKhRmRy.9271
- __ZL14ZERO_FETCHINFO.5696
- __ZL14v2_writeVInt64Phmy.8711
- __ZL14v2_writeVInt64RPhy.9270
- __ZL16__message_assertPKcz.15688
- __ZL16__message_assertPKcz.15719
- __ZL16__message_assertPKcz.16231
- __ZL16__message_assertPKcz.2150
- __ZL16__message_assertPKcz.3896
- __ZL16__message_assertPKcz.5454
- __ZL16__message_assertPKcz.5602
- __ZL16__message_assertPKcz.5966
- __ZL16__message_assertPKcz.7985
- __ZL16__message_assertPKcz.8726
- __ZL16si_analytics_logPKcz.8164
- __ZL17ZERO_RANKING_BITS.16154
- __ZL18PhRankingBoostTreev.16399
- __ZL18PhRetrievalAttribsv.16411
- __ZL18QueryParserLibraryv.10574
- __ZL18QueryParserLibraryv.12834
- __ZL18QueryParserLibraryv.16536
- __ZL18isGenericFilterKeyRKNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE.16756
- __ZL20PhRankingTreeFromStrPKcfPi.16382
- __ZL22__si_assert_copy_extraP6fd_obji.15684
- __ZL22__si_assert_copy_extraP6fd_obji.15715
- __ZL22__si_assert_copy_extraP6fd_obji.16227
- __ZL22__si_assert_copy_extraP6fd_obji.2146
- __ZL22__si_assert_copy_extraP6fd_obji.3892
- __ZL22__si_assert_copy_extraP6fd_obji.5450
- __ZL22__si_assert_copy_extraP6fd_obji.5597
- __ZL22__si_assert_copy_extraP6fd_obji.5962
- __ZL22__si_assert_copy_extraP6fd_obji.7980
- __ZL22__si_assert_copy_extraP6fd_obji.8721
- __ZL22getkQPQUOutputTokenKeyv.16492
- __ZL23audit_stringQueryParser.10586
- __ZL23audit_stringQueryParser.12844
- __ZL23audit_stringQueryParser.16548
- __ZL23store_stream_read_bytesP14store_stream_tPhm.8718
- __ZL24store_stream_write_bytesP14store_stream_tPKhm.8710
- __ZL25convertASTNodeToQueryNodeP9PRAstNodeP9PRContext.4038
- __ZL26PhExactMatchRankingAttribsv.16651
- __ZL26PhImpAttributesRankingNodePKc.16396
- __ZL26getkQPQUOutputTokenInfoKeyv.16371
- __ZL26isGenericFilterTopLevelKeyRKNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE.16758
- __ZL27_containsOnlyCharsInCharsetP8NSStringP14NSCharacterSet.16386
- __ZL27getkQPQUOutputTokenRangeKeyv.12847
- __ZL27getkQPQUOutputTokenRangeKeyv.16489
- __ZL28getkQPQUOutputTokenArgIdsKeyv.10622
- __ZL28getkQPQUOutputTokenArgIdsKeyv.12848
- __ZL28getkQPQUOutputTokenArgIdsKeyv.16490
- __ZL31getkQPQUOutputTokenArgScoresKeyv.12849
- __ZL31getkQPQUOutputTokenArgScoresKeyv.16491
- __ZL32PhImpAttributesPrefixRankingNodePKc.16395
- __ZL6sTotal.1072
- __ZL6sTotal.16149
- __ZL6sTotal.1628
- __ZL6sTotal.16329
- __ZL6sTotal.16440
- __ZL6sTotal.1873
- __ZL6sTotal.4054
- __ZL6sTotal.5447
- __ZL6sTotal.5603
- __ZL6sTotal.7360
- __ZL6sTotal.8408
- __ZL6sTotal.868
- __ZL7Attribsv.4073
- __ZL9TOK_ID_TO.4086
- __ZL9intervals.8393
- __ZZL11CurrentYearvE8currYear.16625
- __ZZL11CurrentYearvE9onceToken.16624
- __ZZL12MetadataKeysvE13_metadataKeys.16752
- __ZZL12MetadataKeysvE9onceToken.16753
- __ZZL14PhThreeYearAgovE7oldYear.16628
- __ZZL14PhThreeYearAgovE9onceToken.16627
- __ZZL16utf8_byte_lengthhE14utf8_len_table.16271
- __ZZL17GenericFilterKeysvE18_genericFilterKeys.16771
- __ZZL17GenericFilterKeysvE9onceToken.16772
- __ZZL18PhRetrievalAttribsvE17_retrievalAttribs.16412
- __ZZL18PhRetrievalAttribsvE9onceToken.16472
- __ZZL18utf8_to_code_pointPKhE20utf8_first_char_mask.16272
- __ZZL22QueryParserLibraryCorePPcE16frameworkLibrary.0.10582
- __ZZL22QueryParserLibraryCorePPcE16frameworkLibrary.0.12840
- __ZZL22QueryParserLibraryCorePPcE16frameworkLibrary.0.16544
- __ZZL24utf8_byte_length_noerrorhE14utf8_len_table.16273
- __ZZL25GenericFilterTopLevelKeysvE26_genericFilterTopLevelKeys.16763
- __ZZL25GenericFilterTopLevelKeysvE9onceToken.16764
- __ZZL26PhExactMatchRankingAttribsvE27_phExactMatchRankingAttribs.16652
- __ZZL26PhExactMatchRankingAttribsvE9onceToken.16655
- __ZZL28NanoSecondsSinceAbsoluteTimeyE13sTimebaseInfo.16402
- __ZZL28NanoSecondsSinceAbsoluteTimeyE9onceToken.16401
- __ZZL31getkQPQUOutputTokenKeySymbolLocvE3ptr.0.10597
- __ZZL31getkQPQUOutputTokenKeySymbolLocvE3ptr.0.12850
- __ZZL31getkQPQUOutputTokenKeySymbolLocvE3ptr.0.16549
- __ZZL35getkQPQUOutputTokenInfoKeySymbolLocvE3ptr.0.16740
- __ZZL36getkQPParseAttributeDateKeySymbolLocvE3ptr.0.12995
- __ZZL36getkQPQUOutputTokenRangeKeySymbolLocvE3ptr.0.10631
- __ZZL36getkQPQUOutputTokenRangeKeySymbolLocvE3ptr.0.12862
- __ZZL36getkQPQUOutputTokenRangeKeySymbolLocvE3ptr.0.16561
- __ZZL37getkQPParseAttributeMediaKeySymbolLocvE3ptr.0.12974
- __ZZL37getkQPQUOutputTokenArgIdsKeySymbolLocvE3ptr.0.10623
- __ZZL37getkQPQUOutputTokenArgIdsKeySymbolLocvE3ptr.0.12858
- __ZZL37getkQPQUOutputTokenArgIdsKeySymbolLocvE3ptr.0.16557
- __ZZL38getkQPParseAttributeSenderKeySymbolLocvE3ptr.0.12982
- __ZZL38getkQPParseAttributeUnreadKeySymbolLocvE3ptr.0.12962
- __ZZL40getkQPQUOutputTokenArgScoresKeySymbolLocvE3ptr.0.12854
- __ZZL40getkQPQUOutputTokenArgScoresKeySymbolLocvE3ptr.0.16553
- __ZZL41getkQPParseAttributeDueActionKeySymbolLocvE3ptr.0.12901
- __ZZL41getkQPParseAttributeRecipientKeySymbolLocvE3ptr.0.12978
- __ZZL42getkQPParseAttributeAttachmentKeySymbolLocvE3ptr.0.12968
- __ZZL42getkQPParseAttributeJunkActionKeySymbolLocvE3ptr.0.12893
- __ZZL43getkQPParseAttributeDescriptionKeySymbolLocvE3ptr.0.12889
- __ZZL43getkQPParseAttributeDraftActionKeySymbolLocvE3ptr.0.12897
- __ZZL43getkQPParseAttributeHotelActionKeySymbolLocvE3ptr.0.12925
- __ZZL44getkQPParseAttributeFlightActionKeySymbolLocvE3ptr.0.12938
- __ZZL44getkQPParseAttributeLatestActionKeySymbolLocvE3ptr.0.12909
- __ZZL44getkQPParseAttributeTaggedPersonKeySymbolLocvE3ptr.0.12991
- __ZZL45getkQPParseAttributeArchiveActionKeySymbolLocvE3ptr.0.12885
- __ZZL45getkQPParseAttributePrintedActionKeySymbolLocvE3ptr.0.12944
- __ZZL46getkQPParseAttributeEarliestActionKeySymbolLocvE3ptr.0.12913
- __ZZL46getkQPParseAttributeGroundedPersonKeySymbolLocvE3ptr.0.12986
- __ZZL47getkQPParseAttributeCompletedActionKeySymbolLocvE3ptr.0.12905
- __ZZL48getkQPParseAttributeRestaurantActionKeySymbolLocvE3ptr.0.12919
- __ZZL53getkQPParseAttributeFlightArrivalLocationKeySymbolLocvE3ptr.0.12929
- __ZZL55getkQPParseAttributeFlightDepartureLocationKeySymbolLocvE3ptr.0.12933
- ___Block_byref_object_copy_.10642
- ___Block_byref_object_copy_.12883
- ___Block_byref_object_copy_.13345
- ___Block_byref_object_copy_.16195
- ___Block_byref_object_copy_.2118
- ___Block_byref_object_copy_.7499
- ___Block_byref_object_dispose_.10643
- ___Block_byref_object_dispose_.12884
- ___Block_byref_object_dispose_.13346
- ___Block_byref_object_dispose_.16196
- ___Block_byref_object_dispose_.2119
- ___Block_byref_object_dispose_.7500
- ___InnerMerge_block_invoke.797
- ___SICreateNewIndex_block_invoke.378
- ___SIInitIndex_block_invoke.1107
- ___SIInitIndex_block_invoke.1116
- ___SIInitIndex_block_invoke.1123
- ___SIInitIndex_block_invoke.1125
- ____SIContinueIssueMerge2_block_invoke.1968
- ____SIOpenIndexFilesWithState_block_invoke.958
- ____SIOpenIndexFilesWithState_block_invoke.969
- ____SIOpenIndexFilesWithState_block_invoke.974
- ____SIOpenIndexFilesWithState_block_invoke_2.971
- ____SIOpenIndexFilesWithState_block_invoke_2.976
- ____SIOpenIndex_block_invoke.904
- ____SIOpenIndex_block_invoke.930
- ____SIOpenIndex_block_invoke.939
- ____ZL11CurrentYearv_block_invoke.16641
- ____ZL12MetadataKeysv_block_invoke.16788
- ____ZL12processItemsP14datastore_infommP24si_localized_value_cachePmbU13block_pointerFPv15SI_OBJECT_EVENT15si_event_data_tmS4_ES4_ooPtmPhbjmbP16dispatch_queue_sS4_jP14__MDPlistBytes14ranking_mode_sP16ci_rankingbits_sP17ci_tc_distances_tP21ci_vector_distances_tP19PartialQueryResultsRP20SISearchCtx_METADATAiRbP10ReadData_sPV3$_0P22ci_combobits_wrapped_sP20dispatch_semaphore_s_block_invoke.155
- ____ZL14PhThreeYearAgov_block_invoke.16638
- ____ZL14readSDBForOidsP20SISearchCtx_METADATAPxPtP16ci_rankingbits_sP17ci_tc_distances_tP21ci_vector_distances_tmPhP19PartialQueryResultsP14__MDPlistBytesbb_block_invoke.120
- ____ZL14readSDBForOidsP20SISearchCtx_METADATAPxPtP16ci_rankingbits_sP17ci_tc_distances_tP21ci_vector_distances_tmPhP19PartialQueryResultsP14__MDPlistBytesbb_block_invoke.125
- ____ZL14readSDBForOidsP20SISearchCtx_METADATAPxPtP16ci_rankingbits_sP17ci_tc_distances_tP21ci_vector_distances_tmPhP19PartialQueryResultsP14__MDPlistBytesbb_block_invoke_2.131
- ____ZL17GenericFilterKeysv_block_invoke.16776
- ____ZL18PhRetrievalAttribsv_block_invoke.16474
- ____ZL19convertQPFilterNodeP17PRAstQPFilterNodeP9PRContext_block_invoke.4092
- ____ZL20PhRankingTreeFromStrPKcfPi_block_invoke.16644
- ____ZL22QueryParserLibraryCorePPc_block_invoke.10583
- ____ZL22QueryParserLibraryCorePPc_block_invoke.12841
- ____ZL22QueryParserLibraryCorePPc_block_invoke.16545
- ____ZL25GenericFilterTopLevelKeysv_block_invoke.16768
- ____ZL26PhExactMatchRankingAttribsv_block_invoke.16657
- ____ZL28NanoSecondsSinceAbsoluteTimey_block_invoke.16623
- ____ZL28PhPopulateAllFilterFromParseP18NSAttributedStringP14NSMutableArrayIP8NSStringEPS1_IP7NSValueES9_S9_S9__block_invoke.16375
- ____ZL29PhPopulateDateFilterFromParseP18NSAttributedStringP14NSMutableArrayIP8NSStringEPS1_IP7NSValueE_block_invoke.16485
- ____ZL30PhPopulateSomeFiltersFromParseP18NSAttributedStringP14NSMutableArrayIP8NSStringEPS1_IP7NSValueES5_S9__block_invoke.16482
- ____ZL31getkQPQUOutputTokenKeySymbolLocv_block_invoke.10598
- ____ZL31getkQPQUOutputTokenKeySymbolLocv_block_invoke.12851
- ____ZL31getkQPQUOutputTokenKeySymbolLocv_block_invoke.16550
- ____ZL35getkQPQUOutputTokenInfoKeySymbolLocv_block_invoke.16741
- ____ZL36getkQPParseAttributeDateKeySymbolLocv_block_invoke.12996
- ____ZL36getkQPQUOutputTokenRangeKeySymbolLocv_block_invoke.10632
- ____ZL36getkQPQUOutputTokenRangeKeySymbolLocv_block_invoke.12863
- ____ZL36getkQPQUOutputTokenRangeKeySymbolLocv_block_invoke.16562
- ____ZL37getkQPParseAttributeMediaKeySymbolLocv_block_invoke.12975
- ____ZL37getkQPQUOutputTokenArgIdsKeySymbolLocv_block_invoke.10624
- ____ZL37getkQPQUOutputTokenArgIdsKeySymbolLocv_block_invoke.12859
- ____ZL37getkQPQUOutputTokenArgIdsKeySymbolLocv_block_invoke.16558
- ____ZL38getkQPParseAttributeSenderKeySymbolLocv_block_invoke.12983
- ____ZL38getkQPParseAttributeUnreadKeySymbolLocv_block_invoke.12963
- ____ZL40getkQPQUOutputTokenArgScoresKeySymbolLocv_block_invoke.12855
- ____ZL40getkQPQUOutputTokenArgScoresKeySymbolLocv_block_invoke.16554
- ____ZL41getkQPParseAttributeDueActionKeySymbolLocv_block_invoke.12902
- ____ZL41getkQPParseAttributeRecipientKeySymbolLocv_block_invoke.12979
- ____ZL42getkQPParseAttributeAttachmentKeySymbolLocv_block_invoke.12969
- ____ZL42getkQPParseAttributeJunkActionKeySymbolLocv_block_invoke.12894
- ____ZL43getkQPParseAttributeDescriptionKeySymbolLocv_block_invoke.12890
- ____ZL43getkQPParseAttributeDraftActionKeySymbolLocv_block_invoke.12898
- ____ZL43getkQPParseAttributeHotelActionKeySymbolLocv_block_invoke.12926
- ____ZL44getkQPParseAttributeFlightActionKeySymbolLocv_block_invoke.12939
- ____ZL44getkQPParseAttributeLatestActionKeySymbolLocv_block_invoke.12910
- ____ZL44getkQPParseAttributeTaggedPersonKeySymbolLocv_block_invoke.12992
- ____ZL45getkQPParseAttributeArchiveActionKeySymbolLocv_block_invoke.12886
- ____ZL45getkQPParseAttributePrintedActionKeySymbolLocv_block_invoke.12945
- ____ZL46getkQPParseAttributeEarliestActionKeySymbolLocv_block_invoke.12914
- ____ZL46getkQPParseAttributeGroundedPersonKeySymbolLocv_block_invoke.12987
- ____ZL47getkQPParseAttributeCompletedActionKeySymbolLocv_block_invoke.12906
- ____ZL48getkQPParseAttributeRestaurantActionKeySymbolLocv_block_invoke.12920
- ____ZL53getkQPParseAttributeFlightArrivalLocationKeySymbolLocv_block_invoke.12930
- ____ZL55getkQPParseAttributeFlightDepartureLocationKeySymbolLocv_block_invoke.12934
- ____bt_findBulk_block_invoke.81
- ____page_fetch_with_fd_block_invoke.204
- ____si_init_localized_terms_block_invoke.1146
- ___block_descriptor_40_e8_32o_e39_v32?0"NSString"8"NSDictionary"16^B24ls32l8
- ___block_descriptor_tmp.1.5477
- ___block_descriptor_tmp.10.14168
- ___block_descriptor_tmp.10.15355
- ___block_descriptor_tmp.1016
- ___block_descriptor_tmp.1052
- ___block_descriptor_tmp.106
- ___block_descriptor_tmp.1068
- ___block_descriptor_tmp.107
- ___block_descriptor_tmp.1074
- ___block_descriptor_tmp.1078
- ___block_descriptor_tmp.1080
- ___block_descriptor_tmp.1084.8218
- ___block_descriptor_tmp.1088
- ___block_descriptor_tmp.1093
- ___block_descriptor_tmp.1095.8027
- ___block_descriptor_tmp.11.15740
- ___block_descriptor_tmp.11.8862
- ___block_descriptor_tmp.110
- ___block_descriptor_tmp.1100.8034
- ___block_descriptor_tmp.11023
- ___block_descriptor_tmp.1103
- ___block_descriptor_tmp.1108
- ___block_descriptor_tmp.111.15258
- ___block_descriptor_tmp.111.6101
- ___block_descriptor_tmp.11117
- ___block_descriptor_tmp.1120
- ___block_descriptor_tmp.1124
- ___block_descriptor_tmp.11244
- ___block_descriptor_tmp.1126
- ___block_descriptor_tmp.1129
- ___block_descriptor_tmp.113.8161
- ___block_descriptor_tmp.11329
- ___block_descriptor_tmp.1135
- ___block_descriptor_tmp.1138
- ___block_descriptor_tmp.1142
- ___block_descriptor_tmp.1147
- ___block_descriptor_tmp.1149
- ___block_descriptor_tmp.1151
- ___block_descriptor_tmp.1154
- ___block_descriptor_tmp.117.15529
- ___block_descriptor_tmp.117.9701
- ___block_descriptor_tmp.1170
- ___block_descriptor_tmp.1176
- ___block_descriptor_tmp.1179
- ___block_descriptor_tmp.118.5707
- ___block_descriptor_tmp.11842
- ___block_descriptor_tmp.1198
- ___block_descriptor_tmp.12.11147
- ___block_descriptor_tmp.12.15376
- ___block_descriptor_tmp.12.16026
- ___block_descriptor_tmp.12.16244
- ___block_descriptor_tmp.12.4312
- ___block_descriptor_tmp.12.5952
- ___block_descriptor_tmp.12.8292
- ___block_descriptor_tmp.12.8874
- ___block_descriptor_tmp.1200
- ___block_descriptor_tmp.1203
- ___block_descriptor_tmp.121.15528
- ___block_descriptor_tmp.1210
- ___block_descriptor_tmp.1214
- ___block_descriptor_tmp.1215.8123
- ___block_descriptor_tmp.123.15309
- ___block_descriptor_tmp.123.8165
- ___block_descriptor_tmp.123.8961
- ___block_descriptor_tmp.1235
- ___block_descriptor_tmp.1243.8214
- ___block_descriptor_tmp.1244
- ___block_descriptor_tmp.126.8166
- ___block_descriptor_tmp.12774
- ___block_descriptor_tmp.128.14612
- ___block_descriptor_tmp.129.14818
- ___block_descriptor_tmp.13.15382
- ___block_descriptor_tmp.13.16245
- ___block_descriptor_tmp.13.4307
- ___block_descriptor_tmp.13.5403
- ___block_descriptor_tmp.13.5482
- ___block_descriptor_tmp.13.6374
- ___block_descriptor_tmp.13.8875
- ___block_descriptor_tmp.13.8963
- ___block_descriptor_tmp.13083
- ___block_descriptor_tmp.131.9877
- ___block_descriptor_tmp.132
- ___block_descriptor_tmp.136
- ___block_descriptor_tmp.136.5712
- ___block_descriptor_tmp.13632
- ___block_descriptor_tmp.137
- ___block_descriptor_tmp.138.5813
- ___block_descriptor_tmp.13842
- ___block_descriptor_tmp.14.2137
- ___block_descriptor_tmp.14.4965
- ___block_descriptor_tmp.14054
- ___block_descriptor_tmp.1408
- ___block_descriptor_tmp.14157
- ___block_descriptor_tmp.14340
- ___block_descriptor_tmp.1445
- ___block_descriptor_tmp.14555
- ___block_descriptor_tmp.146.14739
- ___block_descriptor_tmp.14646
- ___block_descriptor_tmp.1473.8149
- ___block_descriptor_tmp.15.1094
- ___block_descriptor_tmp.15.1473
- ___block_descriptor_tmp.15.2164
- ___block_descriptor_tmp.15.5483
- ___block_descriptor_tmp.151.9952
- ___block_descriptor_tmp.15349
- ___block_descriptor_tmp.154.8245
- ___block_descriptor_tmp.155.14757
- ___block_descriptor_tmp.156.8253
- ___block_descriptor_tmp.15697
- ___block_descriptor_tmp.157.8256
- ___block_descriptor_tmp.15709
- ___block_descriptor_tmp.159.14950
- ___block_descriptor_tmp.15974
- ___block_descriptor_tmp.16.11153
- ___block_descriptor_tmp.16.1484
- ___block_descriptor_tmp.16.4966
- ___block_descriptor_tmp.16.7902
- ___block_descriptor_tmp.160.14669
- ___block_descriptor_tmp.160.7994
- ___block_descriptor_tmp.161.14804
- ___block_descriptor_tmp.16167
- ___block_descriptor_tmp.167.15561
- ___block_descriptor_tmp.168.15562
- ___block_descriptor_tmp.17.13099
- ___block_descriptor_tmp.17.7001
- ___block_descriptor_tmp.170.10025
- ___block_descriptor_tmp.170.15559
- ___block_descriptor_tmp.172.15420
- ___block_descriptor_tmp.172.6059
- ___block_descriptor_tmp.18.14643
- ___block_descriptor_tmp.18.8982
- ___block_descriptor_tmp.182
- ___block_descriptor_tmp.1821
- ___block_descriptor_tmp.184
- ___block_descriptor_tmp.1853
- ___block_descriptor_tmp.1859
- ___block_descriptor_tmp.187.15173
- ___block_descriptor_tmp.188
- ___block_descriptor_tmp.1880
- ___block_descriptor_tmp.1889
- ___block_descriptor_tmp.19.10159
- ___block_descriptor_tmp.19.13102
- ___block_descriptor_tmp.19.1503
- ___block_descriptor_tmp.19.15422
- ___block_descriptor_tmp.19.2517
- ___block_descriptor_tmp.1903
- ___block_descriptor_tmp.1904
- ___block_descriptor_tmp.1909
- ___block_descriptor_tmp.1912
- ___block_descriptor_tmp.1915
- ___block_descriptor_tmp.1918
- ___block_descriptor_tmp.1926
- ___block_descriptor_tmp.1927
- ___block_descriptor_tmp.1928
- ___block_descriptor_tmp.193
- ___block_descriptor_tmp.1936
- ___block_descriptor_tmp.1937
- ___block_descriptor_tmp.1938
- ___block_descriptor_tmp.1940
- ___block_descriptor_tmp.1941
- ___block_descriptor_tmp.1942
- ___block_descriptor_tmp.1961
- ___block_descriptor_tmp.1972
- ___block_descriptor_tmp.1973
- ___block_descriptor_tmp.1998
- ___block_descriptor_tmp.2.16239
- ___block_descriptor_tmp.2.5405
- ___block_descriptor_tmp.2.5478
- ___block_descriptor_tmp.2.5619
- ___block_descriptor_tmp.2.7915
- ___block_descriptor_tmp.2.9282
- ___block_descriptor_tmp.20.12713
- ___block_descriptor_tmp.20.16267
- ___block_descriptor_tmp.20.4126
- ___block_descriptor_tmp.2002
- ___block_descriptor_tmp.2013
- ___block_descriptor_tmp.2014
- ___block_descriptor_tmp.2015
- ___block_descriptor_tmp.21.11185
- ___block_descriptor_tmp.21.11674
- ___block_descriptor_tmp.2103
- ___block_descriptor_tmp.2104
- ___block_descriptor_tmp.2120
- ___block_descriptor_tmp.2123
- ___block_descriptor_tmp.2126
- ___block_descriptor_tmp.2132
- ___block_descriptor_tmp.214
- ___block_descriptor_tmp.2141
- ___block_descriptor_tmp.215
- ___block_descriptor_tmp.219
- ___block_descriptor_tmp.22.13626
- ___block_descriptor_tmp.22.14640
- ___block_descriptor_tmp.220
- ___block_descriptor_tmp.23.15418
- ___block_descriptor_tmp.23.4148
- ___block_descriptor_tmp.23.9007
- ___block_descriptor_tmp.24.1527
- ___block_descriptor_tmp.24.3453
- ___block_descriptor_tmp.24.4147
- ___block_descriptor_tmp.25.11189
- ___block_descriptor_tmp.25.11683
- ___block_descriptor_tmp.25.16096
- ___block_descriptor_tmp.2528
- ___block_descriptor_tmp.26.13106
- ___block_descriptor_tmp.26.14847
- ___block_descriptor_tmp.26.15450
- ___block_descriptor_tmp.26.16097
- ___block_descriptor_tmp.26.6414
- ___block_descriptor_tmp.2690
- ___block_descriptor_tmp.27.15455
- ___block_descriptor_tmp.27.5673
- ___block_descriptor_tmp.28.10148
- ___block_descriptor_tmp.28.1100
- ___block_descriptor_tmp.28.13108
- ___block_descriptor_tmp.28.1530
- ___block_descriptor_tmp.28.15456
- ___block_descriptor_tmp.28.4153
- ___block_descriptor_tmp.28.6446
- ___block_descriptor_tmp.28.8548
- ___block_descriptor_tmp.29.11688
- ___block_descriptor_tmp.29.1536
- ___block_descriptor_tmp.29.4152
- ___block_descriptor_tmp.29.7701
- ___block_descriptor_tmp.2918
- ___block_descriptor_tmp.297
- ___block_descriptor_tmp.3.15977
- ___block_descriptor_tmp.3.9288
- ___block_descriptor_tmp.30.11691
- ___block_descriptor_tmp.30.14841
- ___block_descriptor_tmp.30.15493
- ___block_descriptor_tmp.30.15989
- ___block_descriptor_tmp.301
- ___block_descriptor_tmp.306
- ___block_descriptor_tmp.31.14111
- ___block_descriptor_tmp.31.2140
- ___block_descriptor_tmp.31.4962
- ___block_descriptor_tmp.31.7922
- ___block_descriptor_tmp.32.2143
- ___block_descriptor_tmp.32.4717
- ___block_descriptor_tmp.33.13091
- ___block_descriptor_tmp.33.14112
- ___block_descriptor_tmp.33.14839
- ___block_descriptor_tmp.33.15491
- ___block_descriptor_tmp.33.4156
- ___block_descriptor_tmp.33.4480
- ___block_descriptor_tmp.3365
- ___block_descriptor_tmp.34.14113
- ___block_descriptor_tmp.34.15991
- ___block_descriptor_tmp.34.4155
- ___block_descriptor_tmp.35.4957
- ___block_descriptor_tmp.35.7926
- ___block_descriptor_tmp.355
- ___block_descriptor_tmp.356
- ___block_descriptor_tmp.36.14837
- ___block_descriptor_tmp.36.15501
- ___block_descriptor_tmp.361
- ___block_descriptor_tmp.37.15509
- ___block_descriptor_tmp.3736
- ___block_descriptor_tmp.380
- ___block_descriptor_tmp.39.14118
- ___block_descriptor_tmp.39.14835
- ___block_descriptor_tmp.39.1548
- ___block_descriptor_tmp.3955
- ___block_descriptor_tmp.4.1429
- ___block_descriptor_tmp.4.15981
- ___block_descriptor_tmp.4.5467
- ___block_descriptor_tmp.4.5620
- ___block_descriptor_tmp.4.9291
- ___block_descriptor_tmp.40.1107
- ___block_descriptor_tmp.40.15507
- ___block_descriptor_tmp.40.2529
- ___block_descriptor_tmp.41.1562
- ___block_descriptor_tmp.41.4974
- ___block_descriptor_tmp.411.9878
- ___block_descriptor_tmp.4129
- ___block_descriptor_tmp.42.13123
- ___block_descriptor_tmp.42.14832
- ___block_descriptor_tmp.42.1565
- ___block_descriptor_tmp.4305
- ___block_descriptor_tmp.4339
- ___block_descriptor_tmp.44.1573
- ___block_descriptor_tmp.45.2548
- ___block_descriptor_tmp.4542
- ___block_descriptor_tmp.4578
- ___block_descriptor_tmp.46.13118
- ___block_descriptor_tmp.47.15521
- ___block_descriptor_tmp.48.13121
- ___block_descriptor_tmp.48.14922
- ___block_descriptor_tmp.48.15522
- ___block_descriptor_tmp.48.9376
- ___block_descriptor_tmp.49.15525
- ___block_descriptor_tmp.4907
- ___block_descriptor_tmp.4943
- ___block_descriptor_tmp.5.7916
- ___block_descriptor_tmp.51.14129
- ___block_descriptor_tmp.51.14920
- ___block_descriptor_tmp.51.7823
- ___block_descriptor_tmp.51.9373
- ___block_descriptor_tmp.5183
- ___block_descriptor_tmp.52.13126
- ___block_descriptor_tmp.52.1421
- ___block_descriptor_tmp.52.2557
- ___block_descriptor_tmp.52.7198
- ___block_descriptor_tmp.52.9067
- ___block_descriptor_tmp.53.14130
- ___block_descriptor_tmp.5337
- ___block_descriptor_tmp.536
- ___block_descriptor_tmp.5381
- ___block_descriptor_tmp.54.14918
- ___block_descriptor_tmp.54.7830
- ___block_descriptor_tmp.542
- ___block_descriptor_tmp.5466
- ___block_descriptor_tmp.55.14115
- ___block_descriptor_tmp.56.7824
- ___block_descriptor_tmp.561
- ___block_descriptor_tmp.5618
- ___block_descriptor_tmp.57.13137
- ___block_descriptor_tmp.57.14116
- ___block_descriptor_tmp.57.5776
- ___block_descriptor_tmp.58.2833
- ___block_descriptor_tmp.58.5777
- ___block_descriptor_tmp.581
- ___block_descriptor_tmp.59.14899
- ___block_descriptor_tmp.59.2559
- ___block_descriptor_tmp.5903
- ___block_descriptor_tmp.6.1459
- ___block_descriptor_tmp.6.16197
- ___block_descriptor_tmp.6.4303
- ___block_descriptor_tmp.6.4346
- ___block_descriptor_tmp.6.4900
- ___block_descriptor_tmp.6.5469
- ___block_descriptor_tmp.6.5625
- ___block_descriptor_tmp.60.16210
- ___block_descriptor_tmp.60.5778
- ___block_descriptor_tmp.61
- ___block_descriptor_tmp.62.13736
- ___block_descriptor_tmp.6291
- ___block_descriptor_tmp.63.15547
- ___block_descriptor_tmp.632
- ___block_descriptor_tmp.635
- ___block_descriptor_tmp.6368
- ___block_descriptor_tmp.64.14164
- ___block_descriptor_tmp.644
- ___block_descriptor_tmp.65.15650
- ___block_descriptor_tmp.65.3615
- ___block_descriptor_tmp.65.4383
- ___block_descriptor_tmp.65.9141
- ___block_descriptor_tmp.6531
- ___block_descriptor_tmp.655.8222
- ___block_descriptor_tmp.66.13735
- ___block_descriptor_tmp.66.5741
- ___block_descriptor_tmp.67
- ___block_descriptor_tmp.68.5744
- ___block_descriptor_tmp.68.9139
- ___block_descriptor_tmp.6969
- ___block_descriptor_tmp.7.11140
- ___block_descriptor_tmp.7.1462
- ___block_descriptor_tmp.7.3953
- ___block_descriptor_tmp.7.4343
- ___block_descriptor_tmp.7.4902
- ___block_descriptor_tmp.7.5622
- ___block_descriptor_tmp.70.13798
- ___block_descriptor_tmp.7069
- ___block_descriptor_tmp.72.5745
- ___block_descriptor_tmp.73.3633
- ___block_descriptor_tmp.74.6102
- ___block_descriptor_tmp.754
- ___block_descriptor_tmp.7598
- ___block_descriptor_tmp.76.15673
- ___block_descriptor_tmp.76.7753
- ___block_descriptor_tmp.7643
- ___block_descriptor_tmp.769
- ___block_descriptor_tmp.77.14946
- ___block_descriptor_tmp.77.15676
- ___block_descriptor_tmp.7888
- ___block_descriptor_tmp.7952
- ___block_descriptor_tmp.796
- ___block_descriptor_tmp.7973
- ___block_descriptor_tmp.799
- ___block_descriptor_tmp.8.11832
- ___block_descriptor_tmp.8.15689
- ___block_descriptor_tmp.8.2120
- ___block_descriptor_tmp.8.4017
- ___block_descriptor_tmp.8.7962
- ___block_descriptor_tmp.80.6103
- ___block_descriptor_tmp.802
- ___block_descriptor_tmp.805
- ___block_descriptor_tmp.806
- ___block_descriptor_tmp.808
- ___block_descriptor_tmp.824
- ___block_descriptor_tmp.83.13824
- ___block_descriptor_tmp.835
- ___block_descriptor_tmp.838
- ___block_descriptor_tmp.84.9158
- ___block_descriptor_tmp.8499
- ___block_descriptor_tmp.855
- ___block_descriptor_tmp.8561
- ___block_descriptor_tmp.859
- ___block_descriptor_tmp.86
- ___block_descriptor_tmp.860
- ___block_descriptor_tmp.871
- ___block_descriptor_tmp.872
- ___block_descriptor_tmp.873
- ___block_descriptor_tmp.874.8148
- ___block_descriptor_tmp.8861
- ___block_descriptor_tmp.888
- ___block_descriptor_tmp.893
- ___block_descriptor_tmp.8958
- ___block_descriptor_tmp.896
- ___block_descriptor_tmp.9.14374
- ___block_descriptor_tmp.9.5409
- ___block_descriptor_tmp.9.5679
- ___block_descriptor_tmp.9.8236
- ___block_descriptor_tmp.905
- ___block_descriptor_tmp.906
- ___block_descriptor_tmp.907
- ___block_descriptor_tmp.908.8221
- ___block_descriptor_tmp.910
- ___block_descriptor_tmp.912
- ___block_descriptor_tmp.9278
- ___block_descriptor_tmp.931
- ___block_descriptor_tmp.9334
- ___block_descriptor_tmp.94
- ___block_descriptor_tmp.940
- ___block_descriptor_tmp.949
- ___block_descriptor_tmp.951
- ___block_descriptor_tmp.9566
- ___block_descriptor_tmp.959
- ___block_descriptor_tmp.96.15193
- ___block_descriptor_tmp.960
- ___block_descriptor_tmp.970
- ___block_descriptor_tmp.972.8219
- ___block_descriptor_tmp.975
- ___block_descriptor_tmp.977
- ___block_descriptor_tmp.982
- ___block_descriptor_tmp.986.8220
- ___block_descriptor_tmp.989
- ___block_descriptor_tmp.995
- ___block_literal_global.10155
- ___block_literal_global.1019
- ___block_literal_global.1054
- ___block_literal_global.10644
- ___block_literal_global.1070
- ___block_literal_global.1076
- ___block_literal_global.108
- ___block_literal_global.1086
- ___block_literal_global.1088
- ___block_literal_global.1091
- ___block_literal_global.11.14368
- ___block_literal_global.11.1864
- ___block_literal_global.1102.8028
- ___block_literal_global.11021
- ___block_literal_global.1105
- ___block_literal_global.11115
- ___block_literal_global.11242
- ___block_literal_global.1131
- ___block_literal_global.1137
- ___block_literal_global.1140
- ___block_literal_global.117.16702
- ___block_literal_global.1178
- ___block_literal_global.1181
- ___block_literal_global.11840
- ___block_literal_global.11864
- ___block_literal_global.1209
- ___block_literal_global.1212
- ___block_literal_global.125.4713
- ___block_literal_global.125.8957
- ___block_literal_global.12772
- ___block_literal_global.130
- ___block_literal_global.13087
- ___block_literal_global.131
- ___block_literal_global.133
- ___block_literal_global.134
- ___block_literal_global.13624
- ___block_literal_global.13840
- ___block_literal_global.14.11145
- ___block_literal_global.14.16022
- ___block_literal_global.140
- ___block_literal_global.14052
- ___block_literal_global.14338
- ___block_literal_global.1457
- ___block_literal_global.14636
- ___block_literal_global.1475
- ___block_literal_global.15.15380
- ___block_literal_global.15.5392
- ___block_literal_global.15.6372
- ___block_literal_global.15374
- ___block_literal_global.15695
- ___block_literal_global.15707
- ___block_literal_global.15975
- ___block_literal_global.16.6518
- ___block_literal_global.16224
- ___block_literal_global.16346
- ___block_literal_global.16754
- ___block_literal_global.17.1092
- ___block_literal_global.17.2162
- ___block_literal_global.18.11151
- ___block_literal_global.18.7900
- ___block_literal_global.1823
- ___block_literal_global.1855
- ___block_literal_global.189
- ___block_literal_global.1914
- ___block_literal_global.1963
- ___block_literal_global.20.14637
- ___block_literal_global.21.13100
- ___block_literal_global.21.15415
- ___block_literal_global.2117
- ___block_literal_global.2134
- ___block_literal_global.2143
- ___block_literal_global.22.16265
- ___block_literal_global.222
- ___block_literal_global.23.11183
- ___block_literal_global.25.15416
- ___block_literal_global.2526
- ___block_literal_global.26.4145
- ___block_literal_global.2688
- ___block_literal_global.27.11187
- ___block_literal_global.28
- ___block_literal_global.2831
- ___block_literal_global.29.5640
- ___block_literal_global.31.4150
- ___block_literal_global.32.14825
- ___block_literal_global.32.15488
- ___block_literal_global.32.15986
- ___block_literal_global.32.16773
- ___block_literal_global.33.4954
- ___block_literal_global.33.7920
- ___block_literal_global.3482
- ___block_literal_global.35.13088
- ___block_literal_global.35.1476
- ___block_literal_global.35.14826
- ___block_literal_global.35.15489
- ___block_literal_global.35.4441
- ___block_literal_global.358
- ___block_literal_global.37.4955
- ___block_literal_global.37.7924
- ___block_literal_global.38.14827
- ___block_literal_global.3856
- ___block_literal_global.39.15504
- ___block_literal_global.4.5387
- ___block_literal_global.4.7913
- ___block_literal_global.4015
- ___block_literal_global.4078
- ___block_literal_global.41.14828
- ___block_literal_global.4124
- ___block_literal_global.42.15505
- ___block_literal_global.43.4971
- ___block_literal_global.4309
- ___block_literal_global.4340
- ___block_literal_global.44.14829
- ___block_literal_global.4557
- ___block_literal_global.4941
- ___block_literal_global.50.14875
- ___block_literal_global.50.9361
- ___block_literal_global.51.13125
- ___block_literal_global.51.15523
- ___block_literal_global.53.14876
- ___block_literal_global.53.9362
- ___block_literal_global.5335
- ___block_literal_global.5379
- ___block_literal_global.538
- ___block_literal_global.5621
- ___block_literal_global.5901
- ___block_literal_global.6.15979
- ___block_literal_global.61
- ___block_literal_global.6289
- ___block_literal_global.634
- ___block_literal_global.6366
- ___block_literal_global.637
- ___block_literal_global.646
- ___block_literal_global.65.16765
- ___block_literal_global.6502
- ___block_literal_global.67.15609
- ___block_literal_global.67.9138
- ___block_literal_global.6993
- ___block_literal_global.710
- ___block_literal_global.7209
- ___block_literal_global.74
- ___block_literal_global.7886
- ___block_literal_global.7971
- ___block_literal_global.826
- ___block_literal_global.8497
- ___block_literal_global.8510
- ___block_literal_global.877
- ___block_literal_global.9.11138
- ___block_literal_global.9.4341
- ___block_literal_global.9005
- ___block_literal_global.9313
- ___block_literal_global.94.7573
- ___block_literal_global.942
- ___block_literal_global.95
- ___block_literal_global.9564
- ___block_literal_global.98.15191
- ___block_literal_global.981
- ___block_literal_global.984
- ___block_literal_global.988
- ___block_literal_global.991
- ___db2_get_datastore_with_ctx_block_invoke.57
- ___db2_update_datastore_state_block_invoke.29
- ___db2_update_datastore_state_block_invoke_4
- ___db2_update_datastore_state_block_invoke_5
- ___flush_updateset_locked_block_invoke.144
- ___isAppleInternalInstall_block_invoke.13138
- ___message_assert.11265
- ___message_assert.11501
- ___message_assert.11831
- ___message_assert.12651
- ___message_assert.12696
- ___message_assert.12754
- ___message_assert.13164
- ___message_assert.13442
- ___message_assert.13501
- ___message_assert.13561
- ___message_assert.13620
- ___message_assert.14069
- ___message_assert.1415
- ___message_assert.14201
- ___message_assert.14349
- ___message_assert.14577
- ___message_assert.15339
- ___message_assert.15764
- ___message_assert.1591
- ___message_assert.16001
- ___message_assert.17058
- ___message_assert.1727
- ___message_assert.2206
- ___message_assert.2713
- ___message_assert.2932
- ___message_assert.2953
- ___message_assert.3135
- ___message_assert.3238
- ___message_assert.3696
- ___message_assert.3757
- ___message_assert.3921
- ___message_assert.4105
- ___message_assert.4119
- ___message_assert.4179
- ___message_assert.4338
- ___message_assert.4522
- ___message_assert.4551
- ___message_assert.4939
- ___message_assert.5909
- ___message_assert.6251
- ___message_assert.6337
- ___message_assert.6550
- ___message_assert.6965
- ___message_assert.7058
- ___message_assert.7619
- ___message_assert.7650
- ___message_assert.7856
- ___message_assert.8435
- ___message_assert.8460
- ___message_assert.8520
- ___message_assert.8761
- ___message_assert.8900
- ___message_assert.8933
- ___message_assert.9358
- ___message_assert.9596
- ___path_bundle_index_block_invoke.10161
- ___prepareForTransaction_block_invoke.1939
- ___processOneCS_block_invoke.1444
- ___setCSAttributes2_block_invoke.1908
- ___setCSAttributes2_block_invoke.1911
- ___si_assert_copy_extra.11261
- ___si_assert_copy_extra.11499
- ___si_assert_copy_extra.11827
- ___si_assert_copy_extra.12646
- ___si_assert_copy_extra.12691
- ___si_assert_copy_extra.12750
- ___si_assert_copy_extra.13160
- ___si_assert_copy_extra.13438
- ___si_assert_copy_extra.13497
- ___si_assert_copy_extra.13556
- ___si_assert_copy_extra.13615
- ___si_assert_copy_extra.14064
- ___si_assert_copy_extra.1410
- ___si_assert_copy_extra.14196
- ___si_assert_copy_extra.14344
- ___si_assert_copy_extra.14572
- ___si_assert_copy_extra.15335
- ___si_assert_copy_extra.15760
- ___si_assert_copy_extra.1587
- ___si_assert_copy_extra.15996
- ___si_assert_copy_extra.16993
- ___si_assert_copy_extra.1722
- ___si_assert_copy_extra.2201
- ___si_assert_copy_extra.2708
- ___si_assert_copy_extra.2928
- ___si_assert_copy_extra.2949
- ___si_assert_copy_extra.3130
- ___si_assert_copy_extra.3233
- ___si_assert_copy_extra.3692
- ___si_assert_copy_extra.3753
- ___si_assert_copy_extra.3916
- ___si_assert_copy_extra.4101
- ___si_assert_copy_extra.4115
- ___si_assert_copy_extra.4174
- ___si_assert_copy_extra.4333
- ___si_assert_copy_extra.4518
- ___si_assert_copy_extra.4546
- ___si_assert_copy_extra.4934
- ___si_assert_copy_extra.5905
- ___si_assert_copy_extra.6246
- ___si_assert_copy_extra.6332
- ___si_assert_copy_extra.6546
- ___si_assert_copy_extra.6961
- ___si_assert_copy_extra.7054
- ___si_assert_copy_extra.7615
- ___si_assert_copy_extra.7645
- ___si_assert_copy_extra.7852
- ___si_assert_copy_extra.8432
- ___si_assert_copy_extra.8455
- ___si_assert_copy_extra.8515
- ___si_assert_copy_extra.8756
- ___si_assert_copy_extra.8895
- ___si_assert_copy_extra.8928
- ___si_assert_copy_extra.9354
- ___si_assert_copy_extra.9591
- ___si_error_from_file_key
- ___si_error_str_key
- ___si_index_rebuild_reason_key
- ___si_invalid_term_update_set_key
- ___si_set_error_str
- ___si_set_rebuild_reason
- ___si_set_scan_count_block_invoke.1944
- ___si_set_scan_count_block_invoke_2.1946
- ___si_set_scan_count_block_invoke_3.1948
- ___si_write_error_to_file
- ___writeDBOToPlistBytes_block_invoke.67
- __page_fetch_with_fd._crashCount.197
- __page_fetch_with_fd._crashCount.198
- __psid_insert.5014
- __si_load_error_from_file
- __si_set_error_from_file
- __si_set_error_str
- __si_set_invalid_term_update_set
- __si_set_rebuild_reason
- _bit_vector_create.15954
- _bit_vector_create.17090
- _bit_vector_init.4656
- _bit_vector_internal_touch_for_set.4691
- _bit_vector_set.13535
- _bit_vector_set.15898
- _bit_vector_set.17054
- _bit_vector_set.2766
- _bit_vector_set.3411
- _bit_vector_set.4242
- _bit_vector_set.4833
- _bit_vector_set.7166
- _bit_vector_set_bits.4698
- _checkNearness.14185
- _commonHash.11754
- _commonHash.16992
- _data_entry_store.16962
- _deleteDocument._COUNT_.53
- _emitTerms.7725
- _getSize.memSize.11825
- _getSize.memSize.13630
- _getSize.memSize.4562
- _get_string_and_length_for_id.15021
- _hash64.7816
- _index_comp.11839
- _index_comp.13636
- _index_comp.4567
- _isAppleInternalInstall.isInternalInstall.13133
- _isAppleInternalInstall.onceToken.13132
- _keycompare.4999
- _localizedFieldTermMatch.14134
- _log_map_access_error.15821
- _log_map_access_error.16935
- _log_map_access_error.7114
- _master_fid_rec.4983
- _master_fid_rec_size.4985
- _objc_msgSend$heartbeatData
- _objc_msgSend$initWithDomain:code:userInfo:
- _objc_msgSend$initWithPrefix:data:
- _objc_msgSend$numberWithDouble:
- _oqpush.13659
- _oqpush.3290
- _oqpush.4581
- _packingCount.13804
- _path_bundle_index.sDummyFD.10156
- _pqDisposeApplier.7720
- _psid_lookup.5012
- _qsort_cached_allocations.11823
- _qsort_cached_allocations.13628
- _qsort_cached_allocations.4560
- _query_realloc.8905
- _readCompactPosition.13808
- _reassignDocument._COUNT_.55
- _remapping_keys.11804
- _restoreVInt32.12670
- _restoreVInt32.3354
- _restoreVInt32.3928
- _sDataMapExceptionCallbacks.15775
- _sDataMapExceptionCallbacks.16910
- _sFetchedPCs
- _sResourcesCallback
- _sTotal.13683
- _sTotal.14063
- _sTotal.14546
- _sTotal.15332
- _sTotal.4537
- _sTotal.4940
- _sTotal.5923
- _sTotal.6326
- _sTotal.8910
- _sTotal.9353
- _sTotal.9528
- _sVectorIndexDropCallback
- _setDocumentAttributes._COUNT_.44
- _setDocumentAttributes._COUNT_.46
- _si_analytics_log.14362
- _si_analytics_log.14761
- _si_analytics_log.15813
- _si_analytics_log.16996
- _si_analytics_log.2752
- _si_analytics_log.3138
- _si_analytics_log.3636
- _si_analytics_log.3718
- _si_analytics_log.4247
- _si_analytics_log.4767
- _si_analytics_log.6257
- _si_analytics_log.7109
- _si_analytics_log.7679
- _si_analytics_log.8636
- _si_analytics_log.8973
- _si_rwlock_wrunlock.3589
- _storeVInt64.13516
- _storeVInt64.4196
- _store_stream_read_bytes.13603
- _store_stream_read_bytes.3410
- _store_stream_read_bytes.4392
- _store_stream_read_bytes.4884
- _store_stream_read_bytes.6874
- _store_stream_read_bytes.707
- _store_stream_read_vint32.13599
- _store_stream_read_vint32.3407
- _store_stream_read_vint32.4390
- _store_stream_read_vint32.6870
- _store_stream_read_vint32.706
- _store_stream_write_bytes.13609
- _store_stream_write_bytes.3266
- _store_stream_write_bytes.4380
- _store_stream_write_bytes.4888
- _store_stream_write_bytes.6862
- _store_stream_write_vint32.13606
- _store_stream_write_vint32.3268
- _store_stream_write_vint32.4381
- _store_stream_write_vint32.6863
- _strHash.17284
- _table_extra_bytes.14628
- _takeBuddyPage.4233
- _termPropertyID.14135
- _thread_count.11824
- _thread_count.13629
- _thread_count.4561
- _v2_readVInt32.4408
- _v2_readVInt64.11331
- _v2_readVInt64.13796
- _v2_readVInt64.14180
- _v2_readVInt64.14222
- _v2_readVInt64.2873
- _v2_readVInt64.3194
- _v2_readVInt64.4403
- _v2_readVInt64.7800
- _v2_writeVInt64.11288
- _v2_writeVInt64.13611
- _v2_writeVInt64.3164
- _vector_dimension.vec_sizes.15424
- _vector_size.elem_sizes.15423
- _writeVInt64.13608
- _writeVInt64.14235
- _writeVInt64.3720
- _writeVInt64.4382
- _writeVInt64.4654
- _writeVInt64.6254
- _writeVectorIndexDrop
CStrings:
+ "\t\ta: NSFileProtectionComplete\n"
+ "\t\tb: NSFileProtectionCompleteUnlessOpen\n"
+ "\t\tc: NSFileProtectionCompleteUntilFirstUserAuthentication or Default\n"
+ "\t\tcx: NSFileProtectionCompleteWhileUserInactive\n"
+ "\t\theartbeat\n"
+ "\t\tindex\n"
+ "\t\tindexdrop\n"
+ "\t\tm: MobileMailIndex\n"
+ "\t\tp: Priority\n"
+ "\tshorthands:\n"
+ "\tsubcommands:\n"
+ "%@/Library/Logs/CrashReporter/DiagnosticLogs/Search"
+ "%@/indexOpenRecord.plist"
+ "%@/spotlight_heartbeat_last.txt"
+ "%@/spotlight_index_drop.%@.%d.%@.%@.%02d.txt"
+ "%@/spotlight_index_drop.%@.%d.%@.%@.txt"
+ "%@_%@"
+ "%p %s"
+ "%p _SIOpenIndex: %d"
+ "%s : read_query: page at offset 0x%llx not valid (skipping %d)! (0x%x %d %d 0x%x)\n"
+ "%s failed to acquire lock (SMB)"
+ "%s failed to acquire lock, %d"
+ "%s fd_create fail, %d"
+ "%s fd_open fail, %d"
+ "%s fd_pread %zd != %zd, %d"
+ "%s fd_pwrite %zd != %zd, %d"
+ "%s fd_pwrite fail, %d"
+ "%s flag check fail, %d"
+ "%s fstatfs fail, %d"
+ "%s malformed, %d"
+ "%s missing"
+ "%s open fail, %d"
+ "%s read fail, %d"
+ "%s/%s %s"
+ "%s/.store.db"
+ "%s/store.db"
+ "%s:%d: %p %s"
+ "%s:%d: %s"
+ "%s:%d: %s %s"
+ "%s:%d: %s/%s %s"
+ "%s:%d: (%p) %s"
+ "%s:%d: (%s) %s"
+ "%s:%d: (%s) could not recover path index"
+ "%s:%d: (%s) could not recover term index"
+ "%s:%d: Error %d opening path: %s"
+ "%s:%d: Error gathering heartbeat data: %@"
+ "%s:%d: Error getting index size (%u)"
+ "%s:%d: Failed refreshing shared heartbeat fields: %@"
+ "%s:%d: Failed to calloc merge context: %d"
+ "%s:%d: Failed to collect data about dropped index: %@"
+ "%s:%d: Failed to delete creation touch file with errno: %d"
+ "%s:%d: Failed to delete legacy file: %@"
+ "%s:%d: Failed to get device RAM with error: %d"
+ "%s:%d: Failed to get index ref (%@)"
+ "%s:%d: Failed to get journal file info (%u)"
+ "%s:%d: Failed to get path index (%u)"
+ "%s:%d: Failed to identify index %u"
+ "%s:%d: Failed to set up count lock %u"
+ "%s:%d: Failed to set up creation lock %u"
+ "%s:%d: Failed to set up error object, skipping (%u, %u, %u, %s)"
+ "%s:%d: Failed to stat index (%u): %d"
+ "%s:%d: Failed to write heartbeat report to file: %@"
+ "%s:%d: Failed to write index drop report to file: %@"
+ "%s:%d: Failed to write to %d/errorFile1: %d"
+ "%s:%d: Invalid prefix %@"
+ "%s:%d: No info for heartbeat event"
+ "%s:%d: No path specified"
+ "%s:%d: Over 10 drops with same timestamp %@"
+ "%s:%d: SIAnalytics object already exists"
+ "%s:%d: Skipping data collection for read fail"
+ "%s:%d: Skipping heartbeat events for read fail"
+ "%s:%d: Skipping locale change %ld for read fail"
+ "%s:%d: Skipping open (%@, %d, %ld) for read fail"
+ "%s:%d: Skipping purge timestamp (%@, %d, %ld) for read fail"
+ "%s:%d: Skipping purgeability (%@, %d) for read fail"
+ "%s:%d: Skipping refresh because read failed"
+ "%s:%d: Skipping requests (%@, %llu, %llu, %llu) for read fail"
+ "%s:%d: Skipping reset for read fail"
+ "%s:%d: Skipping timestamp (%@, %@) for read fail"
+ "%s:%d: Skipping write because read failed"
+ "%s:%d: analytics object calloc error (%u)"
+ "%s:%d: analytics set up failed (count, %u, %d)"
+ "%s:%d: analytics set up failed (creation, %u, %u, %u)"
+ "%s:%d: analytics set up failed (reset, %u)"
+ "%s:%d: calloc failed copy data %u"
+ "%s:%d: calloc failed for creation (%u, %u, %u)"
+ "%s:%d: count data file init fail: %d"
+ "%s:%d: count data file truncate fail: %d"
+ "%s:%d: count data read fail (%u, %d): %ld / %d"
+ "%s:%d: count data read fail index (%u): %ld / %d"
+ "%s:%d: count data write fail (%d): %ld / %d"
+ "%s:%d: count data write fail (reset, %u): %ld / %d"
+ "%s:%d: creation data file init fail: %d"
+ "%s:%d: creation data write fail (%u, %u, %u): %d"
+ "%s:%d: fstatat error %d for %s"
+ "%s:%d: stat(%s) error: %d"
+ "%s:%u: failed assertion '%s' %s invalid length %hu"
+ "*warn* %s"
+ "*warn* %s; it might already be open by another machine's mds_stores."
+ "*warn* (%s) %s"
+ "-[SIAnalytics createHeartbeatDataWithRefresh:error:]"
+ "-[SIAnalytics initWithParentDirectoryPath:corespotlight:heartbeatIndex:resourcesCallback:]"
+ "-[SIAnalytics migrateFromLegacyHeartbeatData:]"
+ "-[SIAnalytics recordLocaleChange:]"
+ "-[SIAnalytics recordOpen:forIndex:dirty:]"
+ "-[SIAnalytics recordRequestsForIndex:adds:updates:deletes:]"
+ "-[SIAnalytics resetAfterHeartbeat]"
+ "-[SIAnalytics sendHeartbeatEventWithData:withReset:]"
+ "-[SIAnalytics sendHeartbeatEvent]"
+ "-[SIAnalytics sendIndexDropEventWithCorruptIndex:prefix:path:readOnly:reason:]"
+ "-[SIAnalytics sendIndexDropEventWithData:]"
+ "-[SIAnalytics setHeartbeatTimestamp:prefix:key:]"
+ "-[SIAnalytics setPurgeTimestamp:prefix:start:]"
+ "-[SIAnalytics setPurgeability:prefix:]"
+ "-[SIAnalyticsIndexData refreshHeartbeatDataWithIndex:path:errors:]"
+ "2400.16"
+ "@24@0:8^B16"
+ "@40@0:8@16@24^@32"
+ "@40@0:8@16B24B28@?32"
+ "@?"
+ "B20@?0^{query_piece=*^?^?iCqiiiff(?=I{?=b2b2b20b1b7})f*(?=ii)^II(?=A^vA^A^v)^{qp_string_id_cache}^v^?^IIQI[17(value_type=*^*qiscfd^d^q^v)]}8I16"
+ "B24@0:8q16"
+ "CIMetaInfoRead fail, %d"
+ "Deleted creation touch file"
+ "Deleted legacy file"
+ "Failed to create diagnostics directory: %@"
+ "Failed to open %d/errorFile1: %d"
+ "Failed to open %d/errorFile2: %d"
+ "Failed to open %d/errorFile3: %d"
+ "Getting size of directory %s"
+ "Heartbeat reporting is disabled"
+ "Index drop reporting is disabled"
+ "Migrating existing heartbeat data to new format"
+ "No data retrieved.\n"
+ "Not reporting index drop (%@): directory age < 3600s"
+ "Not reporting index drop (%@): no data for index"
+ "Not reporting index drop (%@): no opens since last report"
+ "Null pc, should be Metadata index"
+ "Reading from heartbeat file"
+ "Reporting heartbeat"
+ "Reporting index drop for %@"
+ "Reporting vector index drop (%u)"
+ "Reset fields as if a Spotlight Heartbeat report was just sent.\n"
+ "SIAnalyticsCopyData"
+ "SIAnalyticsGetJournalInfo"
+ "SIAnalyticsGetSDBSize"
+ "SIAnalyticsIndexCountDataFileInit"
+ "SIAnalyticsIndexCreationDataFileInit"
+ "SIAnalyticsIndexIncrementCounts"
+ "SIAnalyticsIndexInit"
+ "SIAnalyticsIndexSetCreationInfo"
+ "SIAnalyticsInitialize"
+ "SIAnalyticsReportVectorIndexDrop"
+ "SIAnalyticsResetCounts"
+ "SIGetDirectorySize"
+ "SISetError"
+ "Sending heartbeat event"
+ "Sending index drop event (%@)"
+ "Sending legacy heartbeat event"
+ "Sending legacy index drop event"
+ "Skipping for invalid index fd %d"
+ "Skipping initialize because read failed"
+ "Skipping new heartbeat on this turn %ld"
+ "Skipping non-overwrite error: %u, %u, %u"
+ "Skipping updating resources fields since callback has not been set"
+ "Spotlight version changed %@ -> %@"
+ "Spotlight-%@"
+ "SpotlightHeartbeat"
+ "SpotlightIndexDrop"
+ "Writing previous error to file: %ld, %u, %u, %u, %s"
+ "Writing to heartbeat file"
+ "Wrote to %@"
+ "_SIErrorWriteToFile"
+ "_configFlags"
+ "_readHeartbeat"
+ "_reportPID"
+ "_reportProcessName"
+ "_reportTime"
+ "_resourcesCallback"
+ "age"
+ "analyticsC"
+ "analyticsCountData"
+ "analyticsCreationData"
+ "appendFormat:"
+ "build"
+ "buildbeforeupgrade"
+ "calloc fail"
+ "classification"
+ "com.apple.searchd.indexes.heartbeat"
+ "com.apple.searchd.indexrebuildcount"
+ "com.apple.searchd.vectorindexdrop"
+ "com.apple.spotlight.heartbeat"
+ "com.apple.spotlight.indexdrop"
+ "com.apple.spotlightindex.analytics"
+ "command: %@"
+ "component"
+ "config"
+ "config_global"
+ "content index verify fail, %d"
+ "copyFile for recovery %s->%s, %d"
+ "copyFile for recovery directoryStoreFile.shadow->directoryStoreFile, %d"
+ "copyFile needs shadow %s->%s, %d"
+ "copyHeartbeatData"
+ "could not recover vector index, %d"
+ "count data read hit EOF (%u, %d), starting from 0"
+ "count_add_journaled"
+ "count_add_processed"
+ "count_add_request"
+ "count_delete_journaled"
+ "count_delete_processed"
+ "count_delete_request"
+ "count_drop"
+ "count_drop_total"
+ "count_open_clean"
+ "count_open_dirty"
+ "count_update_journaled"
+ "count_update_processed"
+ "count_update_request"
+ "create index canceled"
+ "create index fail 1"
+ "create index fail 2"
+ "create live index fail, %d"
+ "createDropDataForPrefix:path:error:"
+ "createHeartbeatDataWithRefresh:error:"
+ "createIndex calloc fail"
+ "createIndex create forward store failed"
+ "createIndex open %s fail"
+ "createIndex open %s fail, %d"
+ "createIndex open burst trie fail"
+ "creation data read fail flags (%u): %ld / %d"
+ "creation_flags_index"
+ "creation_flags_sdb"
+ "creation_version_spotlight"
+ "data_collection_error"
+ "datastore dirty, reverse store needs shadow, %u, %u, %u"
+ "datastore needs shadow, reverse store dirty, %u, %u, %u"
+ "db_update_datastore_state"
+ "dbo write back fail, %d"
+ "disable_heartbeat_reporting"
+ "disable_index_drop_reporting"
+ "diskimage"
+ "drop_reason"
+ "drop_reason_string"
+ "drop_timestamp"
+ "droppedindexage"
+ "droppedindexsize"
+ "droptime"
+ "embeddingdonationon"
+ "errorFile1"
+ "errorFile2"
+ "errorFile3"
+ "errorWithDomain:code:userInfo:"
+ "eventCount"
+ "externalvolume"
+ "fileprotection"
+ "filesystemflags"
+ "filesystemfree"
+ "filesystemsize"
+ "filesystemtype"
+ "flush cache fail, %d"
+ "flush index error %d"
+ "get datastore fail"
+ "get datastore fail, %d"
+ "getCurrentSpotlightVersionWithRoots:"
+ "getIndexDataForPrefix:"
+ "getLegacyPCEnum"
+ "getPrefixForPCPriority"
+ "getPrefixForProtectionClass"
+ "getPreviousBuild"
+ "hasSpotlightRoots"
+ "heartbeat"
+ "heartbeat_age"
+ "huge journals or merge files"
+ "hw.memsize"
+ "i16@?0^{query_piece=*^?^?iCqiiiff(?=I{?=b2b2b20b1b7})f*(?=ii)^II(?=A^vA^A^v)^{qp_string_id_cache}^v^?^IIQI[17(value_type=*^*qiscfd^d^q^v)]}8"
+ "index"
+ "index commit shadow fail, %d"
+ "index inactive sdb shrink cache fail, %d"
+ "index open canceled"
+ "index shadow fail, %d"
+ "index write back sdb validation fail"
+ "indexShadowFiles %s fd_create fail, %d"
+ "indexShadowFiles %s fd_pwrite fail, %d"
+ "indexShadowFiles %s shadow fail"
+ "indexShadowFiles burst trie shadow fail"
+ "indexShadowFiles can't shadow %s"
+ "indexShadowFiles groups shadow fail, %d"
+ "indexShadowFiles trying to modify read-only index %s"
+ "index_%@"
+ "index_dropped"
+ "index_name"
+ "indexing caught up sdb shrink cache fail, %d"
+ "indexrebuildcount"
+ "init index fail, %d"
+ "initWithBool:"
+ "initWithCString:encoding:"
+ "initWithFormat:"
+ "initWithLong:"
+ "initWithParentDirectoryPath:corespotlight:heartbeatIndex:resourcesCallback:"
+ "initWithPrefix:"
+ "initWithSuiteName:"
+ "initWithUnsignedInt:"
+ "initWithUnsignedLongLong:"
+ "initial indexing ended sdb shrink cache fail, %d"
+ "initializeSharedHearbeatFields"
+ "invalid index version - recovering, %d, %d, %d"
+ "invalid index version reindexing %d, %d, %d"
+ "invalid meta info %u < %u"
+ "invalid path, %d"
+ "invalid reverse store, %u, %u, %u"
+ "invalid sdb version %d"
+ "isHeartbeatReportingDisabled"
+ "isIndexDropReportingDisabled"
+ "journalAttr"
+ "lastSent"
+ "locked indexing index state, %d"
+ "logged_error"
+ "logged_error_string"
+ "mark index unavailable %u, %u, %d"
+ "marking invalid %s flags:0x%x"
+ "max_index_gen_merge_level"
+ "max_journal_file_bytes"
+ "merge rename index fail"
+ "migrateFromLegacyHeartbeatData:"
+ "name table missing dummy values"
+ "needs recovery: invalid term update set"
+ "no meta info"
+ "not created with unigrams"
+ "num_file"
+ "num_index_gen_compacted"
+ "num_index_gen_non_compacted"
+ "num_index_gen_read_only"
+ "num_index_gen_writeable"
+ "num_journal_file"
+ "num_object_sdb"
+ "open from fast flush canceled"
+ "open index canceled"
+ "open persistent ID store fail"
+ "otaversion"
+ "parentDirectory_age"
+ "pcA_age"
+ "pcA_obj_count"
+ "pcA_wipes"
+ "pcA_wipes_aggregate"
+ "pcB_age"
+ "pcB_obj_count"
+ "pcB_wipes"
+ "pcB_wipes_aggregate"
+ "pcCX_age"
+ "pcCX_obj_count"
+ "pcCX_wipes"
+ "pcCX_wipes_aggregate"
+ "pcC_age"
+ "pcC_obj_count"
+ "pcC_wipes"
+ "pcC_wipes_aggregate"
+ "pcMail_age"
+ "pcMail_obj_count"
+ "pcMail_wipes"
+ "pcMail_wipes_aggregate"
+ "pcPriority_age"
+ "pcPriority_obj_count"
+ "pcPriority_wipes"
+ "pcPriority_wipes_aggregate"
+ "pid"
+ "populateIndexDropData:index:prefix:reason:error:"
+ "previousbuild"
+ "previousspotlightversion"
+ "process terminating while initializing index"
+ "processInfo"
+ "processOneCS out of space, %d"
+ "processOneCS write back fail, %d"
+ "process_id"
+ "process_name"
+ "processname"
+ "purgeable"
+ "query - sdb validate fail"
+ "read"
+ "readonlyfilesystem"
+ "readonlyopen"
+ "rebuildreason"
+ "recordDrop:"
+ "recordLocaleChange:"
+ "recordOpen:dirty:"
+ "recordOpen:forIndex:dirty:"
+ "recordRequestedAdds:updates:deletes:"
+ "recordRequestsForIndex:adds:updates:deletes:"
+ "recover datastore fail, %d"
+ "recovery issued"
+ "recovery not allowed %u"
+ "recovery not allowed due to locked indexing"
+ "recycle due to %s"
+ "refreshHeartbeatDataWithIndex:path:errors:"
+ "remap for index sdb shrink cache fail, %d"
+ "removeItemAtPath:error:"
+ "removeObjectForKey:"
+ "reset"
+ "resetAfterHeartbeat"
+ "restore datastore dirty pages fail, %d"
+ "restore reverse store dirty pages fail, %d"
+ "reverse store update state fail, %d"
+ "rootsinstalled"
+ "runCommand:"
+ "runCommand: %@"
+ "sdb2_internal.h"
+ "sdb2_query.c"
+ "sdb_file_size_bytes"
+ "sdb_shadow_file_size_bytes"
+ "searchutil -c analytics:<subcommand>[:arguments:...]\n"
+ "searchutil -c analytics:heartbeat:all  : print all heartbeat data that would be sent by a Spotlight heartbeat event.\n"
+ "searchutil -c analytics:heartbeat:index:<shorthand>  : collect and dump values of per-index heartbeat fields.\n"
+ "searchutil -c analytics:heartbeat:read  : read heartbeat.plist into memory; note that this might undo any in-memory updates.\n"
+ "searchutil -c analytics:heartbeat:reset  : reset certain fields as if a Spotlight heartbeat event has been reported.\n"
+ "searchutil -c analytics:heartbeat:send  : create Spotlight heartbeat event and send it to CoreAnalytics.\n"
+ "searchutil -c analytics:heartbeat:shared  : refresh shared heartbeat fields and dump values.\n"
+ "searchutil -c analytics:heartbeat:write  : flush out in-memory heartbeat data to heartbeat.plist\n"
+ "searchutil -c analytics:index:<shorthand>  : dump contents of index's analyticsCreationData and analyticsCountData files.\n"
+ "sendHeartbeatEvent"
+ "sendHeartbeatEventWithData:withReset:"
+ "sendIndexDropEventWithCorruptIndex:path:readOnly:reason:"
+ "sendIndexDropEventWithCorruptIndex:prefix:path:readOnly:reason:"
+ "sendIndexDropEventWithData:"
+ "sendLegacyHeartbeatEventWithData:"
+ "sendLegacyIndexDropEventWithData:prefix:readOnly:reason:"
+ "sendVectorIndexDropForIndex:vectorCount:readOnly:prefix:propertyName:dropReason:"
+ "set attributes PSID store resolve fail, %d"
+ "setConfigFlag:"
+ "setDateFormat:"
+ "setHeartbeatTimestamp:prefix:key:"
+ "setPurgeTimestamp:prefix:start:"
+ "setPurgeTimestampForIndex:start:"
+ "setPurgeability:"
+ "setPurgeability:forIndex:"
+ "setPurgeability:prefix:"
+ "setSpotlightVersion"
+ "setTimestamp:key:"
+ "sharedInstance"
+ "shouldReportIndexDrop:"
+ "size_bytes"
+ "spotlightversion"
+ "stringFromDate:"
+ "success: no data in index - rebuilding"
+ "supportspsid"
+ "sync index error %d, %d, %d"
+ "term update set restore fail, %d"
+ "textsemanticsearchon"
+ "timeIntervalSince1970"
+ "time_since"
+ "time_since_boot"
+ "time_since_compaction_end"
+ "time_since_compaction_start"
+ "time_since_drop"
+ "time_since_error"
+ "time_since_last_heartbeat"
+ "time_since_last_open_clean"
+ "time_since_last_open_dirty"
+ "time_since_locale_change"
+ "time_since_merge_end"
+ "time_since_merge_start"
+ "time_since_merge_vacuum_end"
+ "time_since_merge_vacuum_start"
+ "time_since_purge_end"
+ "time_since_purge_start"
+ "time_since_purgeability_change"
+ "timesinceboot"
+ "tokenizer version %d < %d"
+ "trie validation failed"
+ "unsignedLongLongValue"
+ "updateWithData:"
+ "usageInfoForCommand:"
+ "v2"
+ "v24@0:8Q16"
+ "v24@?0^{query_piece=*^?^?iCqiiiff(?=I{?=b2b2b20b1b7})f*(?=ii)^II(?=A^vA^A^v)^{qp_string_id_cache}^v^?^IIQI[17(value_type=*^*qiscfd^d^q^v)]}8^{_ContentIndexDocSet=}16"
+ "v24@?0^{query_piece=*^?^?iCqiiiff(?=I{?=b2b2b20b1b7})f*(?=ii)^II(?=A^vA^A^v)^{qp_string_id_cache}^v^?^IIQI[17(value_type=*^*qiscfd^d^q^v)]}8r^{db_obj_eval_ctx=}16"
+ "v28@0:8@16B24"
+ "v28@0:8B16@20"
+ "v28@0:8q16B24"
+ "v32@?0@\"NSString\"8@\"NSNumber\"16^B24"
+ "v32@?0@\"NSString\"8@\"NSObject\"16^B24"
+ "v36@0:8q16@24B32"
+ "v40@0:8Q16Q24Q32"
+ "v40@0:8^{__SI=Q{SIFileOps=^?^?^?}{SIGuardedFd=iQ}isII^{SIWatchDog}^{__CFDictionary}{_opaque_pthread_rwlock_t=q[192c]}{si_missing_oids_s={os_unfair_lock_s=I}^{__RLEOIDArray}^{__RLEOIDArray}}{si_missing_oids_s={os_unfair_lock_s=I}^{__RLEOIDArray}^{__RLEOIDArray}}{os_unfair_lock_s=I}{si_comm_dates_s=^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}}{si_comm_dates_s=^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}}{si_comm_dates_s=^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}}{si_comm_dates_s=^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}}{si_comm_dates_s=^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}}^{__CFDictionary}^{_MDPlistContainer}Bi[18^{si_scheduler_token_s}]iI[4@]{?=[18^{_si_work_scheduler}][21^{_si_workqueue}]^{si_workqueue_list_s}}@^{datastore_info}{CIMetaInfo=i^{fd_obj}iQIIIIIIIIqqiiBI}^{DocStore}QQ{_opaque_pthread_mutex_t=q[56c]}^{ContentIndexList}^{ContentIndexList}iII^{_SI_PersistentIDStore}{__SIStoreToken={?=CCCCCCCCCCCCCCCC}^{__CFUUID}}ACAII{os_unfair_lock_s=I}ddBiI^{__CFDictionary}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{os_unfair_lock_s=I}^{__CFBag}{_opaque_pthread_mutex_t=q[56c]}^{__CFSet}^{__CFDictionary}Q^{__CFBag}^{__CFDictionary}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_cond_t=q[40c]}iIIIIIIIIIIIIIIIIIIIBBAq^{__CFDictionary}^{__CFBitVector}^{si_mobile_journal}^{si_mobile_journal}^{si_mobile_journal}AqAqAqd^?^vdd{?=^{fd_obj}IIIq{os_unfair_lock_s=I}BB}III^{FinderDateFields}{_opaque_pthread_mutex_t=q[56c]}^{fd_obj}^{fd_obj}^{fd_obj}iii^{_SIIndexCallbacks}^{__CFArray}^{__CFArray}qqqQIIiiBBBBBBBABB^{si_scheduler_token_s}BBBBBQq[4096c]{os_unfair_lock_s=I}{os_unfair_lock_s=I}b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b2b1^i^{__CFSet}^{__CFDictionary}^{__SIUINT64Set}^{ReverseDirStore_s}^{FileTree_Overlay_s}^{__CFSet}^{TermUpdateSet}{_opaque_pthread_rwlock_t=q[192c]}[16C]Bi^{datastore_info}AIBB[5i]*iI^vB^{fd_obj}iiii{AccumulatedCounts_s={_opaque_pthread_mutex_t=q[56c]}[256q][256I]}BB^{si_analytics_s}}16@24^Q32"
+ "v40@0:8q16@24@32"
+ "v40@?0^{__SI=Q{SIFileOps=^?^?^?}{SIGuardedFd=iQ}isII^{SIWatchDog}^{__CFDictionary}{_opaque_pthread_rwlock_t=q[192c]}{si_missing_oids_s={os_unfair_lock_s=I}^{__RLEOIDArray}^{__RLEOIDArray}}{si_missing_oids_s={os_unfair_lock_s=I}^{__RLEOIDArray}^{__RLEOIDArray}}{os_unfair_lock_s=I}{si_comm_dates_s=^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}}{si_comm_dates_s=^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}}{si_comm_dates_s=^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}}{si_comm_dates_s=^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}}{si_comm_dates_s=^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}}^{__CFDictionary}^{_MDPlistContainer}Bi[18^{si_scheduler_token_s}]iI[4^{dispatch_semaphore_s}]{?=[18^{_si_work_scheduler}][21^{_si_workqueue}]^{si_workqueue_list_s}}^{dispatch_queue_s}^{datastore_info}{CIMetaInfo=i^{fd_obj}iQIIIIIIIIqqiiBI}^{DocStore}QQ{_opaque_pthread_mutex_t=q[56c]}^{ContentIndexList}^{ContentIndexList}iII^{_SI_PersistentIDStore}{__SIStoreToken={?=CCCCCCCCCCCCCCCC}^{__CFUUID}}ACAII{os_unfair_lock_s=I}ddBiI^{__CFDictionary}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{os_unfair_lock_s=I}^{__CFBag}{_opaque_pthread_mutex_t=q[56c]}^{__CFSet}^{__CFDictionary}Q^{__CFBag}^{__CFDictionary}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_cond_t=q[40c]}iIIIIIIIIIIIIIIIIIIIBBAq^{__CFDictionary}^{__CFBitVector}^{si_mobile_journal}^{si_mobile_journal}^{si_mobile_journal}AqAqAqd^?^vdd{?=^{fd_obj}IIIq{os_unfair_lock_s=I}BB}III^{FinderDateFields}{_opaque_pthread_mutex_t=q[56c]}^{fd_obj}^{fd_obj}^{fd_obj}iii^{_SIIndexCallbacks}^{__CFArray}^{__CFArray}qqqQIIiiBBBBBBBABB^{si_scheduler_token_s}BBBBBQq[4096c]{os_unfair_lock_s=I}{os_unfair_lock_s=I}b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b2b1^i^{__CFSet}^{__CFDictionary}^{__SIUINT64Set}^{ReverseDirStore_s}^{FileTree_Overlay_s}^{__CFSet}^{TermUpdateSet}{_opaque_pthread_rwlock_t=q[192c]}[16C]Bi^{datastore_info}AIBB[5i]*iI^vB^{fd_obj}iiii{AccumulatedCounts_s={_opaque_pthread_mutex_t=q[56c]}[256q][256I]}BB^{si_analytics_s}}8^{_xpc_activity_s=}16^B24^{dispatch_group_s=}32"
+ "v44@0:8@16@24B32^{si_error_s=qIII[1024c]}36"
+ "v48@0:8@16Q24Q32Q40"
+ "v52@0:8@16@24@32B40^{si_error_s=qIII[1024c]}44"
+ "v52@0:8@16I24B28@32@40I48"
+ "v56@0:8@16@24@32^{si_error_s=qIII[1024c]}40^@48"
+ "vectorindexon"
+ "write"
+ "write index state %d->%d fail, %d"
+ "write index state fail, %d"
+ "yyyy-MM-dd-HH-mm-ss"
- "%d, %u, %u, %s"
- "%p _SIOpenIndex: %d %s"
- "%p open from fast flush canceled:%d"
- "%s:%d: %@ is not a counter field"
- "%s:%d: %@ is not a timestamp field"
- "%s:%d: %p CIMetaInfoRead err:%d"
- "%s:%d: %p Too many live indexes %d/%d"
- "%s:%d: %s : read_query: page at offset 0x%llx not valid (skipping %d)! (0x%x %d %d 0x%x)\n"
- "%s:%d: (%u) Could not open/create error file: %d"
- "%s:%d: (%u) Could not truncate error file: %d"
- "%s:%d: (%u) Error %d writing to error file"
- "%s:%d: (%u) Error opening error file: %d"
- "%s:%d: (%u) Error writing to error file %lld != %lld"
- "%s:%d: (%u) lseek error on error file: %d"
- "%s:%d: (%u) pread error on error file %lld != %lld"
- "%s:%d: (%u) pread error on error file: %d"
- "%s:%d: ARC disabled in SIAnalytics"
- "%s:%d: CIMetaInfoOpenAndLock error %d"
- "%s:%d: CIMetaInfoRead error %d"
- "%s:%d: Could not get schedule protection class for pc \"%s\""
- "%s:%d: Could not recover %s"
- "%s:%d: Failed creating %s/%s, result:%d"
- "%s:%d: Failed to copyfile for recovery %s->%s"
- "%s:%d: No index"
- "%s:%d: Skipping updating resources fields since callback has not been set"
- "%s:%d: Unrecoverable error: Missing positions file (%s)"
- "%s:%d: Unrecoverable error: Missing postings file (%s)"
- "%s:%d: Unrecoverable error: could not open index head file (%s) %d"
- "%s:%d: Unrecoverable error: could not open shadow head file (%s) %d"
- "%s:%d: Unrecoverable error: could not open update file (%s)"
- "%s:%d: Unrecoverable error: could not read shadow head file (%s) %d, %d"
- "%s:%d: Unrecoverable error: could not recover groups file (%s)"
- "%s:%d: Unrecoverable error: could not recover path index (%s)"
- "%s:%d: Unrecoverable error: could not recover term id file (%s)"
- "%s:%d: Unrecoverable error: could not recover term id file (positions) (%s)"
- "%s:%d: Unrecoverable error: could not recover term index (%s)"
- "%s:%d: Unrecoverable error: could not write index head file (%s) %d"
- "%s:%d: [IndexLoss] Failed to delete creation touch file with errno: %d"
- "%s:%d: can't shadow %s"
- "%s:%d: db2_page_uncompress_swap failed, error:%d, pgnum:%lu, pgoff:0x%llx, signature:0x%x, size:%d, used_bytes:%d, flags:0x%x, name:%s"
- "%s:%d: error: could not recover vector index (%s)"
- "%s:%d: index commit shadow err:%d at %s\n"
- "%s:%d: index shadow err:%d at %s\n"
- "%s:%d: invalid pc_priority %u"
- "%s:%d: marking invalid %s flags:0x%x"
- "%s:%d: open indexstate not clean for locked indexing: %d"
- "%s:%d: page_fetch found an invalid page, pgnum:%lu, pgoff:0x%llx, signature:0x%x, size:%d, used_bytes:%d, flags:0x%x, name:%s"
- "%s:%d: reverseStoreUpdateState err:%d"
- "%s:%d: si_write_index_state err:%d"
- "%s:%d: update_db_header (%s) fd_create failed"
- "%s:%d: update_db_header (%s) fd_pread %zd != %zd"
- "%s:%d: update_db_header (%s) flags check failed"
- "%s:%d: update_db_header (%s) write failed"
- "%s:%u: failed assertion '%s' %s invalid length for %s"
- "(%u) No error file"
- "*warn* Couldn't statfs the CIMetaInfo. errno:%d"
- "*warn* Failed to acquire lock on CIMetaInfo object: errno=%d"
- "*warn* Failed to acquire lock on SMB CIMetaInfo; it might already be open by another machine's mds_stores."
- "*warn* Index version %d out of date, expected %d, recovering"
- "*warn* Index version %d out of date, expected %d, reindexing"
- "*warn* Marking the index as unavailable, error:%d, reason:\"%s\", options:0x%lx, path:%s"
- "*warn* Unrecoverable error: Missing data in index head file (%s) %d %d"
- "*warn* Unrecoverable error: Missing shadow head file (%s) %d"
- "*warn* datastore dirty, reverse store needs shadow -- forcing repair (%u, %u, %u)"
- "*warn* datastore needs shadow, reverse store dirty -- forcing repair"
- "*warn* failed to create fd_ref err: %d,  %s"
- "*warn* failed to open fd_ref err: %d,  %s"
- "-[SIAnalytics incrementPerIndexHeartbeatCount:forKey:withError:]"
- "-[SIAnalytics initWithParentDirectoryPath:corespotlight:heartbeatIndex:]"
- "-[SIAnalytics refreshPerIndexHeartbeatFieldsForIndex:protectionClass:withError:]"
- "-[SIAnalytics setPerIndexHeartbeatTimestamp:forKey:withError:]"
- "-[SIAnalytics setSharedHeartbeatTimestamp:forKey:withError:]"
- "2400.14.100"
- "9999.99.99"
- ":MD:kMDItemPath"
- "@24@0:8^@16"
- "@32@0:8@16B24B28"
- "@32@0:8@16^@24"
- "B20@?0^{query_piece=*^?^?iCqiiiff(?=I{?=b2b2b20b1b7})f*(?=ii)^II(?=^v^^v)^{qp_string_id_cache}^v^?^IIQI[17(value_type=*^*qiscfd^d^q^v)]}8I16"
- "B40@0:8^{__SI=Q{SIFileOps=^?^?^?}{SIGuardedFd=iQ}isII^{SIWatchDog}^{__CFDictionary}{_opaque_pthread_rwlock_t=q[192c]}{si_missing_oids_s={os_unfair_lock_s=I}^{__RLEOIDArray}^{__RLEOIDArray}}{si_missing_oids_s={os_unfair_lock_s=I}^{__RLEOIDArray}^{__RLEOIDArray}}{os_unfair_lock_s=I}{si_comm_dates_s=^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}}{si_comm_dates_s=^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}}{si_comm_dates_s=^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}}{si_comm_dates_s=^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}}{si_comm_dates_s=^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}}^{__CFDictionary}^{_MDPlistContainer}Bi[18^{si_scheduler_token_s}]iI[4@]{?=[18^{_si_work_scheduler}][21^{_si_workqueue}]^{si_workqueue_list_s}}@^{datastore_info}{CIMetaInfo=i^{fd_obj}iQIIIIIIIIqqiiBI}^{DocStore}QQ{_opaque_pthread_mutex_t=q[56c]}^{ContentIndexList}^{ContentIndexList}iII^{_SI_PersistentIDStore}{__SIStoreToken={?=CCCCCCCCCCCCCCCC}^{__CFUUID}}ACAII{os_unfair_lock_s=I}ddBiI^{__CFDictionary}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{os_unfair_lock_s=I}^{__CFBag}{_opaque_pthread_mutex_t=q[56c]}^{__CFSet}^{__CFDictionary}Q^{__CFBag}^{__CFDictionary}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_cond_t=q[40c]}iIIIIIIIIIIIIIIIIIIIBBAq^{__CFDictionary}^{__CFBitVector}^{si_mobile_journal}^{si_mobile_journal}^{si_mobile_journal}AqAqAqd^?^vdd{?=^{fd_obj}IIIq{os_unfair_lock_s=I}BB}III^{FinderDateFields}{_opaque_pthread_mutex_t=q[56c]}^{fd_obj}^{fd_obj}^{fd_obj}iii^{_SIIndexCallbacks}^{__CFArray}^{__CFArray}qqqQIIiiBBBBBBBABB^{si_scheduler_token_s}BBBBBQq[4096c]{os_unfair_lock_s=I}{os_unfair_lock_s=I}b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b2b1^i^{__CFSet}^{__CFDictionary}^{__SIUINT64Set}^{ReverseDirStore_s}^{FileTree_Overlay_s}^{__CFSet}^{TermUpdateSet}{_opaque_pthread_rwlock_t=q[192c]}[16C]Bi^{datastore_info}AIBB[5i]*iI^vB^{fd_obj}iiii{AccumulatedCounts_s={_opaque_pthread_mutex_t=q[56c]}[256q][256I]}BB}16@24^@32"
- "B40@0:8d16@24^@32"
- "B40@0:8q16@24^@32"
- "Build: %@"
- "CIMetaInfoOpenAndLock failed with %d"
- "CIMetaInfoRead failed %d"
- "CIMetaInfoRead failed with %d"
- "ContentIndexOpenBulk err %d, %d"
- "ContentIndexOpenBulk failed %d, %d"
- "Error: unknown"
- "Got index directory birthtime %ld"
- "Initializing shared heartbeat fields"
- "Intentional: "
- "No meta info"
- "Q24@0:8@16"
- "Read from heartbeat file"
- "Set SpotlightResources callback"
- "Spotlight roots are installed!"
- "Spotlight version changed %@ -> %s"
- "Spotlight-%s"
- "SpotlightResources config: (%@, %@, %@)"
- "Volume property flags: 0x%llx"
- "Wrote to heartbeat file"
- "[IndexLoss] Deleted creation touch file"
- "_SIOpenIndexFilesWithState failed with -1"
- "__si_write_error_to_file"
- "_si_load_error_from_file"
- "age_"
- "config_feature_flags"
- "config_trial_rollout_id"
- "config_trial_treatment_id"
- "content index open failed %d"
- "create index error 1"
- "create index error 2"
- "db_update_datastore_state failed %d, %d"
- "droppedIndexDataWithError:"
- "ds dirty, rs needs shadow"
- "ds needs shadow, rs dirty"
- "failed to acquire lock for meta info"
- "failed to create meta info fd %d"
- "failed to flock meta info %d"
- "failed to open meta info %d"
- "failed to statfs meta info %d"
- "get datastore failed"
- "heartbeatAnalyticsDataWithReset:error:"
- "heartbeatData"
- "i16@?0^{query_piece=*^?^?iCqiiiff(?=I{?=b2b2b20b1b7})f*(?=ii)^II(?=^v^^v)^{qp_string_id_cache}^v^?^IIQI[17(value_type=*^*qiscfd^d^q^v)]}8"
- "incrementCount:forKey:"
- "incrementPerIndexHeartbeatCount:forKey:withError:"
- "index init:%@"
- "index not created with unigrams error"
- "indexDropAnalyticsDataFromDroppedIndexData:withError:"
- "indexDropType:"
- "init index error %d"
- "init:%@, cs:%d, hb:%d"
- "initWithDomain:code:userInfo:"
- "initWithParentDirectoryPath:corespotlight:heartbeatIndex:"
- "initWithPrefix:data:"
- "invalid index version recovering %d, %d"
- "invalid index version reindexing %d, %d"
- "invalid meta info %d, %d"
- "invalid meta info, cleanGeneration:%ld, shadowedGeneraton:%ld"
- "invalid path"
- "invalid reverse store %d"
- "name table is missing dummy values"
- "needs recovery"
- "no data in index"
- "no data in index - rebuilding, result:%d"
- "numberWithDouble:"
- "open datastore failed %d"
- "open from fast flush canceled %d"
- "open index shadow error"
- "open index state failed %d, %d"
- "open persistent id store error"
- "open recovered index error"
- "prefixForPCPriority"
- "prefixForProtectionClass"
- "process terminating"
- "processing item"
- "processing oid: %lld source: %d"
- "processing oid: %lld source: %d %s"
- "rebuild for tokenizer"
- "rebuilding index because of huge journals or merge files"
- "recover datastore error"
- "recover datastore error %d"
- "recover index error"
- "recovery not allowed for %s/%s due to locked indexing"
- "refreshPerIndexHeartbeatFieldsForIndex:protectionClass:withError:"
- "restore db dirty pages failed %d"
- "restore rs dirty pages failed %d"
- "restoring term update set failed %d"
- "reverseStoreUpdateState err %d"
- "setPerIndexHeartbeatTimestamp:forKey:withError:"
- "setResourcesCallback:"
- "setSharedHeartbeatTimestamp:forKey:withError:"
- "setTimestamp:forKey:"
- "si_pc_priority_from_string"
- "si_write_index_state err %d"
- "si_write_index_state failed %d, %d"
- "statfs: (%s, flags:0x%x, blockSize:0x%llx, blocks:0x%llx, free:0x%llx)"
- "success: no data in index, rebuilding"
- "time_since_"
- "tokenizer"
- "v24@0:8@?16"
- "v24@?0^{query_piece=*^?^?iCqiiiff(?=I{?=b2b2b20b1b7})f*(?=ii)^II(?=^v^^v)^{qp_string_id_cache}^v^?^IIQI[17(value_type=*^*qiscfd^d^q^v)]}8^{_ContentIndexDocSet=}16"
- "v24@?0^{query_piece=*^?^?iCqiiiff(?=I{?=b2b2b20b1b7})f*(?=ii)^II(?=^v^^v)^{qp_string_id_cache}^v^?^IIQI[17(value_type=*^*qiscfd^d^q^v)]}8r^{db_obj_eval_ctx=}16"
- "v32@0:8d16@24"
- "v40@?0^{__SI=Q{SIFileOps=^?^?^?}{SIGuardedFd=iQ}isII^{SIWatchDog}^{__CFDictionary}{_opaque_pthread_rwlock_t=q[192c]}{si_missing_oids_s={os_unfair_lock_s=I}^{__RLEOIDArray}^{__RLEOIDArray}}{si_missing_oids_s={os_unfair_lock_s=I}^{__RLEOIDArray}^{__RLEOIDArray}}{os_unfair_lock_s=I}{si_comm_dates_s=^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}}{si_comm_dates_s=^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}}{si_comm_dates_s=^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}}{si_comm_dates_s=^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}}{si_comm_dates_s=^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}}^{__CFDictionary}^{_MDPlistContainer}Bi[18^{si_scheduler_token_s}]iI[4^{dispatch_semaphore_s}]{?=[18^{_si_work_scheduler}][21^{_si_workqueue}]^{si_workqueue_list_s}}^{dispatch_queue_s}^{datastore_info}{CIMetaInfo=i^{fd_obj}iQIIIIIIIIqqiiBI}^{DocStore}QQ{_opaque_pthread_mutex_t=q[56c]}^{ContentIndexList}^{ContentIndexList}iII^{_SI_PersistentIDStore}{__SIStoreToken={?=CCCCCCCCCCCCCCCC}^{__CFUUID}}ACAII{os_unfair_lock_s=I}ddBiI^{__CFDictionary}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{os_unfair_lock_s=I}^{__CFBag}{_opaque_pthread_mutex_t=q[56c]}^{__CFSet}^{__CFDictionary}Q^{__CFBag}^{__CFDictionary}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_cond_t=q[40c]}iIIIIIIIIIIIIIIIIIIIBBAq^{__CFDictionary}^{__CFBitVector}^{si_mobile_journal}^{si_mobile_journal}^{si_mobile_journal}AqAqAqd^?^vdd{?=^{fd_obj}IIIq{os_unfair_lock_s=I}BB}III^{FinderDateFields}{_opaque_pthread_mutex_t=q[56c]}^{fd_obj}^{fd_obj}^{fd_obj}iii^{_SIIndexCallbacks}^{__CFArray}^{__CFArray}qqqQIIiiBBBBBBBABB^{si_scheduler_token_s}BBBBBQq[4096c]{os_unfair_lock_s=I}{os_unfair_lock_s=I}b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b2b1^i^{__CFSet}^{__CFDictionary}^{__SIUINT64Set}^{ReverseDirStore_s}^{FileTree_Overlay_s}^{__CFSet}^{TermUpdateSet}{_opaque_pthread_rwlock_t=q[192c]}[16C]Bi^{datastore_info}AIBB[5i]*iI^vB^{fd_obj}iiii{AccumulatedCounts_s={_opaque_pthread_mutex_t=q[56c]}[256q][256I]}BB}8^{_xpc_activity_s=}16^B24^{dispatch_group_s=}32"

```
