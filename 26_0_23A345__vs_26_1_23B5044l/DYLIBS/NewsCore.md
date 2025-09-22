## NewsCore

> `/System/Library/PrivateFrameworks/NewsCore.framework/NewsCore`

```diff

-5739.4.0.0.0
-  __TEXT.__text: 0x3e1334
-  __TEXT.__auth_stubs: 0x3ae0
-  __TEXT.__objc_methlist: 0x33de4
-  __TEXT.__const: 0xae08
+5756.0.0.0.0
+  __TEXT.__text: 0x3e1ce4
+  __TEXT.__auth_stubs: 0x3a40
+  __TEXT.__objc_methlist: 0x33f9c
+  __TEXT.__const: 0xae18
   __TEXT.__swift5_typeref: 0x391c
   __TEXT.__constg_swiftt: 0x2bf0
   __TEXT.__swift5_reflstr: 0x1e16

   __TEXT.__swift5_capture: 0xd08
   __TEXT.__swift_as_entry: 0x294
   __TEXT.__swift_as_ret: 0x304
-  __TEXT.__cstring: 0x5094b
+  __TEXT.__cstring: 0x509c8
   __TEXT.__swift5_builtin: 0x140
   __TEXT.__swift5_protos: 0x64
-  __TEXT.__oslogstring: 0x172e8
+  __TEXT.__oslogstring: 0x1754a
   __TEXT.__swift5_assocty: 0x3a8
   __TEXT.__swift5_mpenum: 0x4c
-  __TEXT.__gcc_except_tab: 0x556c
+  __TEXT.__gcc_except_tab: 0x5558
   __TEXT.__dlopen_cstrs: 0x11c
   __TEXT.__ustring: 0x27a
-  __TEXT.__unwind_info: 0xe520
-  __TEXT.__eh_frame: 0x9168
-  __TEXT.__objc_classname: 0x7642
-  __TEXT.__objc_methname: 0x851ed
-  __TEXT.__objc_methtype: 0xc56c
-  __TEXT.__objc_stubs: 0x35180
+  __TEXT.__unwind_info: 0xe548
+  __TEXT.__eh_frame: 0x90f4
+  __TEXT.__objc_classname: 0x7645
+  __TEXT.__objc_methname: 0x855a2
+  __TEXT.__objc_methtype: 0xc59a
+  __TEXT.__objc_stubs: 0x353c0
   __DATA_CONST.__got: 0x2ba8
-  __DATA_CONST.__const: 0x11898
+  __DATA_CONST.__const: 0x11970
   __DATA_CONST.__objc_classlist: 0x1c80
   __DATA_CONST.__objc_catlist: 0x2b0
   __DATA_CONST.__objc_protolist: 0x8c0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x14540
+  __DATA_CONST.__objc_selrefs: 0x145e0
   __DATA_CONST.__objc_protorefs: 0x208
   __DATA_CONST.__objc_superrefs: 0x15a0
   __DATA_CONST.__objc_arraydata: 0x1d48
-  __AUTH_CONST.__auth_got: 0x1d88
-  __AUTH_CONST.__const: 0xb2b0
-  __AUTH_CONST.__cfstring: 0x30a80
-  __AUTH_CONST.__objc_const: 0x76be0
+  __AUTH_CONST.__auth_got: 0x1d38
+  __AUTH_CONST.__const: 0xb2d0
+  __AUTH_CONST.__cfstring: 0x30c80
+  __AUTH_CONST.__objc_const: 0x76d00
   __AUTH_CONST.__objc_arrayobj: 0x540
   __AUTH_CONST.__objc_intobj: 0x13c8
   __AUTH_CONST.__objc_dictobj: 0xbe0
   __AUTH_CONST.__objc_doubleobj: 0x120
   __AUTH.__objc_data: 0x4088
   __AUTH.__data: 0x488
-  __DATA.__objc_ivar: 0x4444
+  __DATA.__objc_ivar: 0x4448
   __DATA.__data: 0x64c8
   __DATA.__bss: 0xa298
   __DATA.__common: 0xa8

   __DATA_DIRTY.__objc_data: 0xdd10
   __DATA_DIRTY.__data: 0x2710
   __DATA_DIRTY.__common: 0x3a8
-  __DATA_DIRTY.__bss: 0x7268
+  __DATA_DIRTY.__bss: 0x7240
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
-  - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMLCompute.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 92F3A783-7924-3964-A02D-B57CEFE1EA9C
-  Functions: 23805
-  Symbols:   65179
-  CStrings:  37199
+  UUID: 811B65E6-5CAB-3C6A-A43A-5154ABD3BA66
+  Functions: 23842
+  Symbols:   65265
+  CStrings:  37250
 
Symbols:
+ -[FCCKOrderFeedQueryOperation _responseForRequest:feedItemAndArticleRecords:allFeedItemAndArticleRecords:wasDropped:reachedMinOrder:reachedEnd:nextOrder:]
+ -[FCCKTestContentDatabase countOfOperationsHandled]
+ -[FCCKTestContentDatabase populateWithLargeTestFeeds]
+ -[FCCacheCoordinator _flushKeys:]
+ -[FCCacheCoordinator pruneToMaxCount:]
+ -[FCFDBConnection _queryToSelectFeedItemIDsWithFeedLookupIDs:feedRange:feature:maxCountByFeedLookupID:totalMaxCount:]
+ -[FCFDBConnection _queryToSelectFeedItemIDsWithFeedLookupIDs:feedRange:feature:totalMaxCount:]
+ -[FCFDBConnection _queryWhereClauseForFeedLookupIDs:feedRange:feature:]
+ -[FCFDBConnection selectFeedItemIDsWithFeedLookupIDs:feedRange:feature:maxCountByFeedLookupID:totalMaxCount:]
+ -[FCFeedDatabaseLookup cachedOnly]
+ -[FCFeedDatabaseLookup feedID]
+ -[FCFeedDatabaseLookup feedRange]
+ -[FCFeedDatabaseLookup hasMaxCount]
+ -[FCFeedDatabaseLookup maxCount]
+ -[FCFeedDatabaseLookup requiredFeature]
+ -[FCFeedDatabaseLookup setCachedOnly:]
+ -[FCFeedDatabaseLookup setFeedID:]
+ -[FCFeedDatabaseLookup setFeedRange:]
+ -[FCFeedDatabaseLookup setMaxCount:]
+ -[FCFeedDatabaseLookup setRequiredFeature:]
+ -[FCFeedDatabaseLookupResult ckFromCursor]
+ -[FCFeedDatabaseLookupResult ckFromOrder]
+ -[FCFeedDatabaseLookupResult ckToOrder]
+ -[FCFeedDatabaseLookupResult exhaustedRange]
+ -[FCFeedDatabaseLookupResult feedItems]
+ -[FCFeedDatabaseLookupResult feedRange]
+ -[FCFeedDatabaseLookupResult insertionToken]
+ -[FCFeedDatabaseLookupResult setCkFromCursor:]
+ -[FCFeedDatabaseLookupResult setCkFromOrder:]
+ -[FCFeedDatabaseLookupResult setCkToOrder:]
+ -[FCFeedDatabaseLookupResult setExhaustedRange:]
+ -[FCFeedDatabaseLookupResult setFeedItems:]
+ -[FCFeedDatabaseLookupResult setFeedRange:]
+ -[FCFeedRequest hasMaxCount]
+ _.str.112
+ _FCIsWidgetDebugInspectionEnabled
+ _FCStringFromArticleContentType
+ _FCURLForWidgetDebugLogs
+ _FCWidgetBundlePaidFeedDisabledSharedPreferenceKey
+ _FCWidgetBundlePaidMultiplierDisabledSharedPreferenceKey
+ _FCWidgetDebugInspectionEnabledSharedPreferenceKey
+ _FCWidgetForYouBestOfEnabledSharedPreferenceKey
+ _FCWidgetForYouTopicDiversificationDisabledSharedPreferenceKey
+ _FCWidgetForYouVisibilitySharedPreferenceKey
+ _OBJC_IVAR_$_FCCKTestContentDatabase._countOfOperationsHandled
+ __OBJC_$_PROP_LIST_FCFeedDatabaseLookup
+ __OBJC_$_PROP_LIST_FCFeedDatabaseLookupResult
+ ___109-[FCFDBConnection selectFeedItemIDsWithFeedLookupIDs:feedRange:feature:maxCountByFeedLookupID:totalMaxCount:]_block_invoke
+ ___117-[FCFDBConnection _queryToSelectFeedItemIDsWithFeedLookupIDs:feedRange:feature:maxCountByFeedLookupID:totalMaxCount:]_block_invoke
+ ___189+[FCPersonalizationUtilities diversifyItems:withPreselectedItems:limit:similarityStartExpectation:similarityEndExpectation:publisherDiversificationSlope:publisherDiversificationYIntercept:]_block_invoke.32
+ ___189+[FCPersonalizationUtilities diversifyItems:withPreselectedItems:limit:similarityStartExpectation:similarityEndExpectation:publisherDiversificationSlope:publisherDiversificationYIntercept:]_block_invoke.33
+ ___38-[FCCacheCoordinator pruneToMaxCount:]_block_invoke
+ ___38-[FCCacheCoordinator pruneToMaxCount:]_block_invoke_2
+ ___38-[FCCacheCoordinator pruneToMaxCount:]_block_invoke_3
+ ___38-[FCCacheCoordinator pruneToMaxCount:]_block_invoke_4
+ ___38-[FCCacheCoordinator pruneToMaxCount:]_block_invoke_5
+ ___53-[FCFeedDatabase _feedItemsForLookups:withFeedsByID:]_block_invoke.65
+ ___55-[FCFeedRequestOperation operationWillFinishWithError:]_block_invoke.52
+ ___56-[FCFeedDatabase performDatabaseLookups:boundedByCount:]_block_invoke_4
+ ___65-[FCFeedRequestOperation _finishPrewarmingWithCompletionHandler:]_block_invoke.69
+ ___65-[FCFeedRequestOperation _finishPrewarmingWithCompletionHandler:]_block_invoke.70
+ ___65-[FCFeedRequestOperation _finishPrewarmingWithCompletionHandler:]_block_invoke.71
+ ___65-[FCFeedRequestOperation _finishPrewarmingWithCompletionHandler:]_block_invoke_2.73
+ ___67-[FCFDBConnection insertFeatureIndexesForFeedItems:knownFeedsByID:]_block_invoke.54
+ ___71-[FCFDBConnection _queryWhereClauseForFeedLookupIDs:feedRange:feature:]_block_invoke
+ ___75-[FCCKTestFeedQueryEndpoint handleQueryOperation:withRecords:droppedFeeds:]_block_invoke.188
+ ___76-[FCFeedRequestOperation _gatherAllOrderFeedResponsesWithCompletionHandler:]_block_invoke.86
+ ___83-[FCFDBStorage feedItemsForFeedIDs:feedRange:feature:maxCountByFeed:totalMaxCount:]_block_invoke_9
+ ___block_descriptor_32_e43_"<NSCopying>"16?0"FCFeedDatabaseLookup"8l
+ ___block_descriptor_48_e8_32r40r_e22_v16?0"NSDictionary"8lr32l8r40l8
+ ___block_descriptor_64_e8_32s40s48s_e29_v16?0"NSMutableDictionary"8ls32l8s40l8s48l8
+ ___block_descriptor_80_e8_32s40s48s56s64s_e15_"NSString"8?0ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_80_e8_32s40s48s56s64s_e5_B8?0ls32l8s40l8s48l8s56l8s64l8
+ ___block_literal_global.257
+ ___block_literal_global.265
+ ___block_literal_global.563
+ _objc_msgSend$_queryToSelectFeedItemIDsWithFeedLookupIDs:feedRange:feature:maxCountByFeedLookupID:totalMaxCount:
+ _objc_msgSend$_queryToSelectFeedItemIDsWithFeedLookupIDs:feedRange:feature:totalMaxCount:
+ _objc_msgSend$_queryWhereClauseForFeedLookupIDs:feedRange:feature:
+ _objc_msgSend$_responseForRequest:feedItemAndArticleRecords:allFeedItemAndArticleRecords:wasDropped:reachedMinOrder:reachedEnd:nextOrder:
+ _objc_msgSend$ckFromOrder
+ _objc_msgSend$ckToOrder
+ _objc_msgSend$enumerateRangesMissingFromLookups:visitor:
+ _objc_msgSend$exhaustedRange
+ _objc_msgSend$fc_setByUnioningSet:
+ _objc_msgSend$hasMaxCount
+ _objc_msgSend$insertionToken
+ _objc_msgSend$performDatabaseLookups:
+ _objc_msgSend$performDatabaseLookups:boundedByCount:
+ _objc_msgSend$saveFeedItems:feedIDs:extentByFeedID:requestRangeByFeedID:
+ _objc_msgSend$saveFeedItems:forFeedID:insertionToken:requestDate:reachedToOrder:extent:reachedEnd:
+ _objc_msgSend$selectFeedItemIDsWithFeedLookupIDs:feedRange:feature:maxCountByFeedLookupID:totalMaxCount:
+ _objc_msgSend$setCkFromOrder:
+ _objc_msgSend$setCkToOrder:
+ _objc_msgSend$setExhaustedRange:
+ _objc_msgSend$setInsertionToken:
- -[FCFDBConnection selectAllFeedItemIDsWithFeedLookupIDs:feedRange:]
- -[FCFDBConnection selectFeedItemIDsWithFeedLookupIDs:feedRange:feature:maxCount:]
- -[NTPBFeedItem(FCFeedItem) publisherArticleVersion]
- _.str.115
- _.str.26
- _OUTLINED_FUNCTION_0
- ___189+[FCPersonalizationUtilities diversifyItems:withPreselectedItems:limit:similarityStartExpectation:similarityEndExpectation:publisherDiversificationSlope:publisherDiversificationYIntercept:]_block_invoke.28
- ___189+[FCPersonalizationUtilities diversifyItems:withPreselectedItems:limit:similarityStartExpectation:similarityEndExpectation:publisherDiversificationSlope:publisherDiversificationYIntercept:]_block_invoke.29
- ___53-[FCFeedDatabase _feedItemsForLookups:withFeedsByID:]_block_invoke.62
- ___55-[FCFeedRequestOperation operationWillFinishWithError:]_block_invoke.55
- ___65-[FCFeedRequestOperation _finishPrewarmingWithCompletionHandler:]_block_invoke.72
- ___65-[FCFeedRequestOperation _finishPrewarmingWithCompletionHandler:]_block_invoke.73
- ___65-[FCFeedRequestOperation _finishPrewarmingWithCompletionHandler:]_block_invoke.74
- ___65-[FCFeedRequestOperation _finishPrewarmingWithCompletionHandler:]_block_invoke_2.76
- ___67-[FCFDBConnection insertFeatureIndexesForFeedItems:knownFeedsByID:]_block_invoke.68
- ___67-[FCFDBConnection selectAllFeedItemIDsWithFeedLookupIDs:feedRange:]_block_invoke
- ___75-[FCCKTestFeedQueryEndpoint handleQueryOperation:withRecords:droppedFeeds:]_block_invoke.175
- ___76-[FCFeedRequestOperation _gatherAllOrderFeedResponsesWithCompletionHandler:]_block_invoke.89
- ___81-[FCFDBConnection selectFeedItemIDsWithFeedLookupIDs:feedRange:feature:maxCount:]_block_invoke
- ___block_descriptor_72_e8_32s40s48s_e5_B8?0ls32l8s40l8s48l8
- ___block_literal_global.268
- ___block_literal_global.545
- ___isPlatformVersionAtLeast
- ___isPlatformVersionAtLeast.cold.1
- ___isPlatformVersionAtLeast.cold.2
- __availability_version_check
- __initializeAvailabilityCheck
- __swift_FORCE_LOAD_$_swiftCoreImage
- __swift_FORCE_LOAD_$_swiftCoreImage_$_NewsCore
- _compatibilityInitializeAvailabilityCheck
- _dispatch_once_f
- _dlsym
- _fclose
- _fopen
- _fread
- _fseek
- _ftell
- _initializeAvailabilityCheck
- _objc_msgSend$selectFeedItemIDsWithFeedLookupIDs:feedRange:feature:maxCount:
- _objc_msgSend$unsignedLongValue
- _rewind
- _sscanf
CStrings:
+ " AND row_num <= %@)"
+ " OR (feed_lookup_id = %@"
+ "%{public}@ received an invalid Results record; will repair nextOrder to correspond to the last feed item instead of a greater value, feedID=%{public}@"
+ "%{public}@ received an invalid Results record; will repair nextOrder to correspond to the last feed item instead of zero, feedID=%{public}@"
+ "%{public}@ received an invalid Results record; will repair reachedMinOrder to be false, feedID=%{public}@"
+ "%{public}@ received an invalid Results record; will repair response to look like the range was exhausted, feedID=%{public}@"
+ "(feed_lookup_id = %@"
+ ")"
+ ") SELECT feed_lookup_id, feed_item_order FROM items WHERE "
+ "@\"<NSCopying>\"16@?0@\"FCFeedDatabaseLookup\"8"
+ "@\"NSArray\"56@0:8@\"NSArray\"16@\"FCFeedRange\"24@\"FCFeedItemFeature\"32@\"NSDictionary\"40Q48"
+ "ANF"
+ "Atest_feed1_article%lu"
+ "Atest_feed2_article%lu"
+ "Disabling topic diversification due to internal settings override"
+ "SELECT feed_lookup_id, feed_item_order FROM feed_item_lookup "
+ "T@\"NSData\",C,N,V_ckFromCursor"
+ "T@,&,N,V_insertionToken"
+ "TB,N,V_exhaustedRange"
+ "TQ,N,V_ckFromOrder"
+ "TQ,N,V_ckToOrder"
+ "TQ,R,N,V_countOfOperationsHandled"
+ "Video"
+ "WHERE feed_lookup_id IN ("
+ "WITH items AS (SELECT feed_lookup_id, feed_item_order, ROW_NUMBER() OVER (PARTITION BY feed_lookup_id ORDER BY feed_item_order DESC) AS row_num FROM feed_item_lookup "
+ "Web"
+ "_countOfOperationsHandled"
+ "_queryToSelectFeedItemIDsWithFeedLookupIDs:feedRange:feature:maxCountByFeedLookupID:totalMaxCount:"
+ "_queryToSelectFeedItemIDsWithFeedLookupIDs:feedRange:feature:totalMaxCount:"
+ "_queryWhereClauseForFeedLookupIDs:feedRange:feature:"
+ "_responseForRequest:feedItemAndArticleRecords:allFeedItemAndArticleRecords:wasDropped:reachedMinOrder:reachedEnd:nextOrder:"
+ "ckFromCursor"
+ "countOfOperationsHandled"
+ "enumerateRangesMissingFromLookups:visitor:"
+ "hasMaxCount"
+ "performDatabaseLookups:"
+ "performDatabaseLookups:boundedByCount:"
+ "populateWithLargeTestFeeds"
+ "saveFeedItems:feedIDs:extentByFeedID:requestRangeByFeedID:"
+ "saveFeedItems:forFeedID:insertionToken:requestDate:reachedToOrder:extent:reachedEnd:"
+ "selectFeedItemIDsWithFeedLookupIDs:feedRange:feature:maxCountByFeedLookupID:totalMaxCount:"
+ "setCkFromCursor:"
+ "setCkFromOrder:"
+ "setCkToOrder:"
+ "setExhaustedRange:"
+ "setInsertionToken:"
+ "subscribedTagIDs: %@ autoFavoriteTagIDs: %@ mutedTagIDs: %@"
+ "v64@0:8@16@24@32@40B48Q52B60"
+ "widget-debug-logs"
+ "widget_bundle_paid_feed_disabled"
+ "widget_bundle_paid_multiplier_disabled"
+ "widget_debug_inspection_enabled"
+ "widget_for_you_best_of_enabled"
+ "widget_for_you_topic_diversification_disabled"
+ "widget_for_you_visibility"
- "%d.%d.%d"
- "-[NTPBFeedItem(FCFeedItem) publisherArticleVersion]"
- "/System/Library/CoreServices/SystemVersion.plist"
- "@\"NSArray\"48@0:8@\"NSArray\"16@\"FCFeedRange\"24@\"FCFeedItemFeature\"32Q40"
- "CFDataCreateWithBytesNoCopy"
- "CFDictionaryGetValue"
- "CFGetTypeID"
- "CFPropertyListCreateFromXMLData"
- "CFPropertyListCreateWithData"
- "CFRelease"
- "CFStringCreateWithCStringNoCopy"
- "CFStringGetCString"
- "CFStringGetTypeID"
- "OrderFeed returned a bad nextOrder value for request UUID %@"
- "ProductVersion"
- "SELECT feed_lookup_id, feed_item_order FROM feed_item_lookup WHERE feed_lookup_id IN ("
- "feed requests must have a non-zero max count"
- "kCFAllocatorNull"
- "news.today_widget.for_you_best_of_enabled"
- "r"
- "selectAllFeedItemIDsWithFeedLookupIDs:feedRange:"
- "selectFeedItemIDsWithFeedLookupIDs:feedRange:feature:maxCount:"
- "subscribedTagIDs: %@ mutedTagIDs: %@"
- "unsignedLongValue"

```
