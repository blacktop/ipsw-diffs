## NewsToday

> `/System/Library/PrivateFrameworks/NewsToday.framework/NewsToday`

```diff

-5681.0.0.0.0
-  __TEXT.__text: 0x3c7f0
+5691.0.0.0.0
+  __TEXT.__text: 0x3cad4
   __TEXT.__auth_stubs: 0xa80
-  __TEXT.__objc_methlist: 0x568c
-  __TEXT.__const: 0x25a
-  __TEXT.__oslogstring: 0x10c0
-  __TEXT.__cstring: 0x7b25
+  __TEXT.__objc_methlist: 0x567c
+  __TEXT.__const: 0x2ba
+  __TEXT.__oslogstring: 0x11a0
+  __TEXT.__cstring: 0x7a45
   __TEXT.__ustring: 0x16
   __TEXT.__gcc_except_tab: 0xb00
   __TEXT.__constg_swiftt: 0x6c

   __TEXT.__swift5_types: 0x8
   __TEXT.__swift_as_entry: 0x1c
   __TEXT.__swift_as_ret: 0x20
-  __TEXT.__unwind_info: 0xbd8
+  __TEXT.__unwind_info: 0xbd0
   __TEXT.__eh_frame: 0x3d0
-  __TEXT.__objc_classname: 0xa1c
-  __TEXT.__objc_methname: 0xff27
-  __TEXT.__objc_methtype: 0x1bff
-  __TEXT.__objc_stubs: 0x8900
-  __DATA_CONST.__got: 0x920
-  __DATA_CONST.__const: 0x1668
+  __TEXT.__objc_classname: 0xa1a
+  __TEXT.__objc_methname: 0xfeb2
+  __TEXT.__objc_methtype: 0x1beb
+  __TEXT.__objc_stubs: 0x8940
+  __DATA_CONST.__got: 0x928
+  __DATA_CONST.__const: 0x1690
   __DATA_CONST.__objc_classlist: 0x1d0
   __DATA_CONST.__objc_catlist: 0x78
   __DATA_CONST.__objc_protolist: 0x180
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3510
+  __DATA_CONST.__objc_selrefs: 0x3530
   __DATA_CONST.__objc_protorefs: 0x60
   __DATA_CONST.__objc_superrefs: 0x1a8
   __DATA_CONST.__objc_arraydata: 0x1a0
   __AUTH_CONST.__auth_got: 0x550
   __AUTH_CONST.__const: 0x6e8
   __AUTH_CONST.__cfstring: 0x1cc0
-  __AUTH_CONST.__objc_const: 0xbe88
-  __AUTH_CONST.__objc_intobj: 0xf0
+  __AUTH_CONST.__objc_const: 0xbe58
+  __AUTH_CONST.__objc_intobj: 0x120
   __AUTH_CONST.__objc_dictobj: 0x1b8
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH.__objc_data: 0x2f0
   __AUTH.__data: 0x30
-  __DATA.__objc_ivar: 0x53c
-  __DATA.__data: 0xf10
+  __DATA.__objc_ivar: 0x534
+  __DATA.__data: 0xeb0
   __DATA.__bss: 0x1b0
   __DATA_DIRTY.__objc_data: 0xfa0
   __DATA_DIRTY.__bss: 0x78

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: C707EFA7-409D-3F1A-BD95-2D6A8B4D8973
-  Functions: 1653
-  Symbols:   6223
-  CStrings:  3609
+  UUID: D3EC44B8-4313-3876-8E41-968E3A8C23E9
+  Functions: 1647
+  Symbols:   6211
+  CStrings:  3606
 
Symbols:
+ -[NTTodayConfigConversionOperation _collectRecordIDsReferencedByTodayConfig:withArticleListIDs:articleIDs:]
+ -[NTTodayConfigConversionOperation _todayConfigWithConfigJSON:error:]
+ -[NTTodayContext writeUserDidReadHeadlineWithAnalyticsElement:atDate:]
+ -[NTTodayContext writeUserDidReadHeadlineWithAnalyticsElement:atDate:].cold.1
+ -[NTTodayContext writeUserDidReadHeadlineWithAnalyticsElement:atDate:].cold.2
+ -[NTTodayContext writeUserDidSeeHeadlinesWithAnalyticsElements:atDate:]
+ -[NTTodayContext writeUserDidSeeHeadlinesWithAnalyticsElements:atDate:].cold.1
+ -[NTTodayContext writeUserDidSeeHeadlinesWithAnalyticsElements:atDate:].cold.2
+ -[NTWidgetConfigDataOperation _finishByConvertingRecordsWithArticlesByID:articleListsByID:tagsByID:]
+ -[NTWidgetConfigDataOperation _finishByFetchingRecordsForArticleIDs:articleListIDs:]
+ -[NTWidgetConfigDataOperation configuration]
+ -[NTWidgetConfigDataOperation expectedArticleIDs]
+ -[NTWidgetConfigDataOperation expectedArticleListIDs]
+ -[NTWidgetConfigDataOperation performOperation].cold.1
+ -[NTWidgetConfigDataOperation setConfiguration:]
+ -[NTWidgetConfigDataOperation setExpectedArticleIDs:]
+ -[NTWidgetConfigDataOperation setExpectedArticleListIDs:]
+ -[NTWidgetConfigDataOperation validateOperation].cold.4
+ _FCWidgetShouldIgnoreJSONRecordsSharedPreferenceKey
+ _OBJC_IVAR_$_NTWidgetConfigDataOperation._configuration
+ _OBJC_IVAR_$_NTWidgetConfigDataOperation._expectedArticleIDs
+ _OBJC_IVAR_$_NTWidgetConfigDataOperation._expectedArticleListIDs
+ ___100-[NTWidgetConfigDataOperation _finishByConvertingRecordsWithArticlesByID:articleListsByID:tagsByID:]_block_invoke
+ ___100-[NTWidgetConfigDataOperation _finishByConvertingRecordsWithArticlesByID:articleListsByID:tagsByID:]_block_invoke.33
+ ___100-[NTWidgetConfigDataOperation _finishByConvertingRecordsWithArticlesByID:articleListsByID:tagsByID:]_block_invoke.34
+ ___100-[NTWidgetConfigDataOperation _finishByConvertingRecordsWithArticlesByID:articleListsByID:tagsByID:]_block_invoke.36
+ ___100-[NTWidgetConfigDataOperation _finishByConvertingRecordsWithArticlesByID:articleListsByID:tagsByID:]_block_invoke_2
+ ___52-[NTTodayConfigConversionOperation performOperation]_block_invoke.25
+ ___69-[NTTodayConfigConversionOperation _todayConfigWithConfigJSON:error:]_block_invoke
+ ___71-[NTTodayContext writeUserDidSeeHeadlinesWithAnalyticsElements:atDate:]_block_invoke
+ ___71-[NTTodayContext writeUserDidSeeHeadlinesWithAnalyticsElements:atDate:]_block_invoke_2
+ ___84-[NTWidgetConfigDataOperation _finishByFetchingRecordsForArticleIDs:articleListIDs:]_block_invoke
+ ___block_descriptor_40_e8_32s_e34_v24?0"NSDictionary"8"NSError"16ls32l8
+ ___block_descriptor_56_e8_32s40s48s_e58_v40?0"NSArray"8"NSArray"16"NSDictionary"24"NSError"32ls32l8s40l8s48l8
+ _objc_msgSend$_collectRecordIDsReferencedByTodayConfig:withArticleListIDs:articleIDs:
+ _objc_msgSend$_finishByConvertingRecordsWithArticlesByID:articleListsByID:tagsByID:
+ _objc_msgSend$_finishByFetchingRecordsForArticleIDs:articleListIDs:
+ _objc_msgSend$_todayConfigWithConfigJSON:error:
+ _objc_msgSend$allRecordIDs
+ _objc_msgSend$edgeCacheHintForWidgetArticles
+ _objc_msgSend$edgeCacheHintForWidgetConfig
+ _objc_msgSend$expectedArticleIDs
+ _objc_msgSend$expectedArticleListIDs
+ _objc_msgSend$fc_removeObjectsFromArray:
+ _objc_msgSend$setCachePolicyForArticleLists:
+ _objc_msgSend$setCachePolicyForArticles:
+ _objc_msgSend$setExpectedArticleIDs:
+ _objc_msgSend$setExpectedArticleListIDs:
+ _objc_msgSend$setHeldRecordsCompletionHandler:
+ _objc_msgSend$writeReadHistoryItem:
+ _objc_msgSend$writeSeenHistoryItems:
- -[NTTodayConfigConversionOperation _todayConfigWithConfigJSON:articleListIDs:articleIDs:error:]
- -[NTTodayConfigConversionOperation _todayConfigWithConfigJSON:articleListIDs:articleIDs:error:].cold.1
- -[NTTodayConfigConversionOperation _todayConfigWithConfigJSON:articleListIDs:articleIDs:error:].cold.2
- -[NTTodayContext writeUserDidReadHeadlineWithAnalyticsElement:atDate:withCompletion:]
- -[NTTodayContext writeUserDidReadHeadlineWithAnalyticsElement:atDate:withCompletion:].cold.1
- -[NTTodayContext writeUserDidReadHeadlineWithAnalyticsElement:atDate:withCompletion:].cold.2
- -[NTTodayContext writeUserDidSeeHeadlinesWithAnalyticsElements:atDate:withCompletion:]
- -[NTTodayContext writeUserDidSeeHeadlinesWithAnalyticsElements:atDate:withCompletion:].cold.1
- -[NTTodayContext writeUserDidSeeHeadlinesWithAnalyticsElements:atDate:withCompletion:].cold.2
- -[NTWidgetConfigDataOperation _collectRecordsFromWidgetConfigDictionary:]
- -[NTWidgetConfigDataOperation _collectRecordsFromWidgetConfigDictionary:].cold.1
- -[NTWidgetConfigDataOperation _collectRecordsFromWidgetConfigDictionary:].cold.2
- -[NTWidgetConfigDataOperation _collectRecordsFromWidgetConfigDictionary:].cold.3
- -[NTWidgetConfigDataOperation _finalizeResultFromCachedRecords]
- -[NTWidgetConfigDataOperation cachedRecords]
- -[NTWidgetConfigDataOperation resultArticleIDs]
- -[NTWidgetConfigDataOperation resultArticleListIDs]
- -[NTWidgetConfigDataOperation resultDefaultConfigurationDictionary]
- -[NTWidgetConfigDataOperation resultSingleTagConfigurationDictionary]
- -[NTWidgetConfigDataOperation setCachedRecords:]
- -[NTWidgetConfigDataOperation setResultArticleIDs:]
- -[NTWidgetConfigDataOperation setResultArticleListIDs:]
- -[NTWidgetConfigDataOperation setResultDefaultConfigurationDictionary:]
- -[NTWidgetConfigDataOperation setResultSingleTagConfigurationDictionary:]
- _OBJC_IVAR_$_NTWidgetConfigDataOperation._cachedRecords
- _OBJC_IVAR_$_NTWidgetConfigDataOperation._resultArticleIDs
- _OBJC_IVAR_$_NTWidgetConfigDataOperation._resultArticleListIDs
- _OBJC_IVAR_$_NTWidgetConfigDataOperation._resultDefaultConfigurationDictionary
- _OBJC_IVAR_$_NTWidgetConfigDataOperation._resultSingleTagConfigurationDictionary
- ___52-[NTTodayConfigConversionOperation performOperation]_block_invoke.18
- ___63-[NTWidgetConfigDataOperation _finalizeResultFromCachedRecords]_block_invoke
- ___63-[NTWidgetConfigDataOperation _finalizeResultFromCachedRecords]_block_invoke_2
- ___73-[NTWidgetConfigDataOperation _collectRecordsFromWidgetConfigDictionary:]_block_invoke
- ___73-[NTWidgetConfigDataOperation _collectRecordsFromWidgetConfigDictionary:]_block_invoke.28
- ___73-[NTWidgetConfigDataOperation _collectRecordsFromWidgetConfigDictionary:]_block_invoke.29
- ___86-[NTTodayContext writeUserDidSeeHeadlinesWithAnalyticsElements:atDate:withCompletion:]_block_invoke
- ___86-[NTTodayContext writeUserDidSeeHeadlinesWithAnalyticsElements:atDate:withCompletion:]_block_invoke_2
- ___95-[NTTodayConfigConversionOperation _todayConfigWithConfigJSON:articleListIDs:articleIDs:error:]_block_invoke
- ___block_descriptor_40_e8_32s_e92_v56?0"NSDictionary"8"NSDictionary"16"NSArray"24"NSArray"32"NSDictionary"40"NSError"48ls32l8
- _objc_msgSend$_collectRecordsFromWidgetConfigDictionary:
- _objc_msgSend$_finalizeResultFromCachedRecords
- _objc_msgSend$cachedRecords
- _objc_msgSend$edgeCacheHintForToday
- _objc_msgSend$resultArticleIDs
- _objc_msgSend$resultArticleListIDs
- _objc_msgSend$resultDefaultConfigurationDictionary
- _objc_msgSend$resultSingleTagConfigurationDictionary
- _objc_msgSend$setCachedRecords:
- _objc_msgSend$setResultArticleIDs:
- _objc_msgSend$setResultArticleListIDs:
- _objc_msgSend$setResultDefaultConfigurationDictionary:
- _objc_msgSend$setResultSingleTagConfigurationDictionary:
- _objc_msgSend$writeReadHistoryItem:withCompletion:
- _objc_msgSend$writeSeenHistoryItems:withCompletion:
CStrings:
+ "%{public}@ received defaultConfigDictionary: %@, singleTagConfigDictionary: %@, articleIDs: %@, articleListIDs: %@, error: %@"
+ "%{public}@ will adopt records from widget config because all are present"
+ "%{public}@ will fetch records from CK because some are missing from the widget config, missingArticles=%{public}@, missingLists=%{public}@"
+ "%{public}@ will fetch records from CK because they're not included in the widget config"
+ "%{public}@ will fetch records from CK due to internal settings override"
+ "-[NTTodayContext writeUserDidReadHeadlineWithAnalyticsElement:atDate:]"
+ "-[NTTodayContext writeUserDidSeeHeadlinesWithAnalyticsElements:atDate:]"
+ "@32@0:8@16^@24"
+ "T@\"NSArray\",C,N,V_expectedArticleIDs"
+ "T@\"NSArray\",C,N,V_expectedArticleListIDs"
+ "Today config data operation requires a completion handler."
+ "Today config data operation requires a configuration."
+ "Today config data operation requires context."
+ "Today config data operation requires widgetConfiguration."
+ "_collectRecordIDsReferencedByTodayConfig:withArticleListIDs:articleIDs:"
+ "_expectedArticleIDs"
+ "_expectedArticleListIDs"
+ "_finishByConvertingRecordsWithArticlesByID:articleListsByID:tagsByID:"
+ "_finishByFetchingRecordsForArticleIDs:articleListIDs:"
+ "_todayConfigWithConfigJSON:error:"
+ "adSponsorshipsEnabled"
+ "allRecordIDs"
+ "edgeCacheHintForWidgetArticles"
+ "edgeCacheHintForWidgetConfig"
+ "expectedArticleIDs"
+ "expectedArticleListIDs"
+ "fc_removeObjectsFromArray:"
+ "isTodaySponsorshipEligible"
+ "setCachePolicyForArticleLists:"
+ "setCachePolicyForArticles:"
+ "setExpectedArticleIDs:"
+ "setExpectedArticleListIDs:"
+ "setHeldRecordsCompletionHandler:"
+ "v32@0:8@\"<NTHeadlineAnalyticsElementProviding>\"16@\"NSDate\"24"
+ "v32@0:8@\"NSArray\"16@\"NSDate\"24"
+ "v40@?0@\"NSArray\"8@\"NSArray\"16@\"NSDictionary\"24@\"NSError\"32"
+ "writeReadHistoryItem:"
+ "writeSeenHistoryItems:"
+ "writeUserDidReadHeadlineWithAnalyticsElement:atDate:"
+ "writeUserDidSeeHeadlinesWithAnalyticsElements:atDate:"
- "\t"
- "%{public}@ parsed default configuration %{public}@"
- "%{public}@ parsed single tag configuration %{public}@"
- "%{public}@ received defaultConfigDictionary: %@, singleTagConfigDictionary: %@, articleIDs: %@, articleListIDs: %@, error: %@ "
- "%{public}@ will convert widget config data"
- "-[NTTodayConfigConversionOperation _todayConfigWithConfigJSON:articleListIDs:articleIDs:error:]"
- "-[NTTodayContext writeUserDidReadHeadlineWithAnalyticsElement:atDate:withCompletion:]"
- "-[NTTodayContext writeUserDidSeeHeadlinesWithAnalyticsElements:atDate:withCompletion:]"
- "@\"FCHeldRecords\""
- "Record chain conversion conversion operation requires widgetConfiguration."
- "Record chain conversion operation requires a completion handler."
- "Record chain conversion operation requires context."
- "T@\"FCHeldRecords\",&,N,V_cachedRecords"
- "T@\"NSArray\",&,N,V_resultArticleIDs"
- "T@\"NSArray\",&,N,V_resultArticleListIDs"
- "T@\"NSDictionary\",&,N,V_resultDefaultConfigurationDictionary"
- "T@\"NSDictionary\",&,N,V_resultSingleTagConfigurationDictionary"
- "_cachedRecords"
- "_collectRecordsFromWidgetConfigDictionary:"
- "_finalizeResultFromCachedRecords"
- "_resultArticleIDs"
- "_resultArticleListIDs"
- "_resultDefaultConfigurationDictionary"
- "_resultSingleTagConfigurationDictionary"
- "articleIDs referenced in the JSON have to be included in the full list of article records"
- "cachedRecords"
- "edgeCacheHintForToday"
- "resultArticleIDs"
- "resultArticleListIDs"
- "resultDefaultConfigurationDictionary"
- "resultSingleTagConfigurationDictionary"
- "setCachedRecords:"
- "setResultArticleIDs:"
- "setResultArticleListIDs:"
- "setResultDefaultConfigurationDictionary:"
- "setResultSingleTagConfigurationDictionary:"
- "v40@0:8@\"<NTHeadlineAnalyticsElementProviding>\"16@\"NSDate\"24@?<v@?>32"
- "v40@0:8@\"NSArray\"16@\"NSDate\"24@?<v@?>32"
- "v56@?0@\"NSDictionary\"8@\"NSDictionary\"16@\"NSArray\"24@\"NSArray\"32@\"NSDictionary\"40@\"NSError\"48"
- "writeReadHistoryItem:withCompletion:"
- "writeSeenHistoryItems:withCompletion:"
- "writeUserDidReadHeadlineWithAnalyticsElement:atDate:withCompletion:"
- "writeUserDidSeeHeadlinesWithAnalyticsElements:atDate:withCompletion:"

```
