## SpotlightServices

> `/System/Library/PrivateFrameworks/SpotlightServices.framework/SpotlightServices`

```diff

-2268.1.8.0.0
-  __TEXT.__text: 0xe4238
+2274.0.3.0.0
+  __TEXT.__text: 0xe5928
   __TEXT.__auth_stubs: 0x1370
-  __TEXT.__objc_methlist: 0x94ec
+  __TEXT.__objc_methlist: 0x9544
   __TEXT.__const: 0x21f0
-  __TEXT.__cstring: 0x2b846
-  __TEXT.__oslogstring: 0x2d63
-  __TEXT.__gcc_except_tab: 0x2b4c
+  __TEXT.__cstring: 0x2b8d4
+  __TEXT.__oslogstring: 0x2dda
+  __TEXT.__gcc_except_tab: 0x2bbc
   __TEXT.__ustring: 0x3e
-  __TEXT.__unwind_info: 0x2224
+  __TEXT.__unwind_info: 0x2250
   __TEXT.__objc_classname: 0xe06
-  __TEXT.__objc_methname: 0x1c96c
-  __TEXT.__objc_methtype: 0x26c3
-  __TEXT.__objc_stubs: 0x14ce0
-  __DATA_CONST.__got: 0xb40
-  __DATA_CONST.__const: 0xf398
+  __TEXT.__objc_methname: 0x1cb0e
+  __TEXT.__objc_methtype: 0x26d9
+  __TEXT.__objc_stubs: 0x14e00
+  __DATA_CONST.__got: 0xb60
+  __DATA_CONST.__const: 0xf3d8
   __DATA_CONST.__objc_classlist: 0x420
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xba40
-  __DATA_CONST.__objc_selrefs: 0x6400
+  __DATA_CONST.__objc_const: 0xba70
+  __DATA_CONST.__objc_selrefs: 0x6450
   __DATA_CONST.__objc_arraydata: 0xa38
-  __AUTH_CONST.__cfstring: 0x24300
+  __AUTH_CONST.__cfstring: 0x243e0
   __AUTH_CONST.__objc_const: 0x4138
-  __AUTH_CONST.__const: 0x1a50
+  __AUTH_CONST.__const: 0x1a90
   __AUTH_CONST.__objc_floatobj: 0x10
-  __AUTH_CONST.__objc_intobj: 0x2100
+  __AUTH_CONST.__objc_intobj: 0x2160
   __AUTH_CONST.__objc_doubleobj: 0x1c0
   __AUTH_CONST.__objc_arrayobj: 0x498
   __AUTH_CONST.__objc_dictobj: 0xf0

   __AUTH.__objc_data: 0x5a0
   __AUTH.__data: 0x28
   __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0xa50
+  __DATA.__objc_classrefs: 0xa58
   __DATA.__objc_superrefs: 0x350
-  __DATA.__objc_ivar: 0xd90
-  __DATA.__data: 0xd68
+  __DATA.__objc_ivar: 0xd94
+  __DATA.__data: 0xd78
   __DATA.__thread_ptrs: 0x8
-  __DATA.__bss: 0x390
+  __DATA.__bss: 0x3b0
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x23a0
   __DATA_DIRTY.__data: 0x2a8

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 02D9B792-1CAB-3AA1-BAE5-A69B54FAABFC
-  Functions: 4027
-  Symbols:   14651
-  CStrings:  15013
+  UUID: 8B76EEE7-46D5-3D78-BAE7-AE36B7B06197
+  Functions: 4037
+  Symbols:   14696
+  CStrings:  15041
 
Symbols:
+ +[PRSRankingItemRanker shouldFilterResult:currentTime:isScopedSearch:]
+ +[PRSRankingItemRanker thresholdResultsInSection:userQuery:queryID:isEntitiesSearch:currentTime:isScopedSearch:]
+ +[SSLocalCEP isAllowlistedBundle:]
+ +[SSRankingManager topHitCandidacyThresholdingForSection:]
+ -[NSString(MatchScore) hasSpecialAppPrefix]
+ -[SFSearchResult_SpotlightExtras initWithIdentifier:bundleIdentifier:protectionClass:attributeKeys:attributeValues:type:completion:]
+ -[SSRankingManager logPommesScoringForRankingItem:queryId:query:bundleID:name:topicality:freshness:engagement:likelihood:launchPortion:launchCount:engagedInSpotlight:exactMatchedLaunchString:lastUsedDate:recentEngagementDateInSpotlight:recentEngagementDateOutSpotlight:nominateLocalTopHit:]
+ -[SSShortcutResultBuilder entityBadgeType]
+ -[SSShortcutResultBuilder setEntityBadgeType:]
+ GCC_except_table23
+ GCC_except_table30
+ GCC_except_table36
+ GCC_except_table40
+ GCC_except_table42
+ GCC_except_table52
+ GCC_except_table55
+ GCC_except_table71
+ GCC_except_table82
+ GCC_except_table85
+ _MDItemHasTopHitAppShortcuts
+ _MDItemRunnableShortcutsPrimaryPhrase
+ _MDItemRunnableShortcutsTopHitBadge
+ _NSFileProtectionNone
+ _OBJC_CLASS_$_NSSortDescriptor
+ _OBJC_IVAR_$_SSShortcutResultBuilder._entityBadgeType
+ _PASSBOOK_ORDER
+ _SSFaceTimeBundleIdentifier
+ _SSPhoneBundleIdentifier
+ _SSRankingManagerPommesLocalTopHitThreshold
+ ___112+[PRSRankingItemRanker thresholdResultsInSection:userQuery:queryID:isEntitiesSearch:currentTime:isScopedSearch:]_block_invoke
+ ___34+[SSLocalCEP isAllowlistedBundle:]_block_invoke
+ ___57+[SSWorldClockUtilities onDeviceResultsForLocationQuery:]_block_invoke
+ ___63-[PRSRankingItem(Scoring) matchScoreForShortcutsWithEvaluator:]_block_invoke
+ ___block_descriptor_48_e8_32r40r_e35_v32?0"NSNumber"8"NSNumber"16^B24lr32l8r40l8
+ ___block_descriptor_66_e8_32s40s_e57_B24?0"SFSearchResult_SpotlightExtras"8"NSDictionary"16ls32l8s40l8
+ ___block_literal_global.14
+ ___block_literal_global.170
+ ___block_literal_global.205
+ ___block_literal_global.224
+ ___block_literal_global.270
+ ___block_literal_global.273
+ ___block_literal_global.328
+ ___block_literal_global.333
+ ___block_literal_global.341
+ ___block_literal_global.364
+ ___block_literal_global.375
+ ___block_literal_global.439
+ ___block_literal_global.482
+ ___block_literal_global.490
+ ___block_literal_global.523
+ ___block_literal_global.70
+ __unnamed_array_storage.346
+ __unnamed_array_storage.355
+ __unnamed_array_storage.358
+ __unnamed_array_storage.370
+ __unnamed_array_storage.373
+ __unnamed_array_storage.382
+ __unnamed_array_storage.395
+ __unnamed_array_storage.401
+ _isAllowlistedBundle:.allowlistedBundles
+ _isAllowlistedBundle:.onceToken
+ _matchScoreForShortcutsWithEvaluator:.appPrefixActionBundleIDs
+ _matchScoreForShortcutsWithEvaluator:.onceToken
+ _objc_msgSend$defaultCityForTimeZone:
+ _objc_msgSend$entityBadgeType
+ _objc_msgSend$hasSpecialAppPrefix
+ _objc_msgSend$initWithIdentifier:bundleIdentifier:protectionClass:attributeKeys:attributeValues:type:completion:
+ _objc_msgSend$localizedLowercaseString
+ _objc_msgSend$logPommesScoringForRankingItem:queryId:query:bundleID:name:topicality:freshness:engagement:likelihood:launchPortion:launchCount:engagedInSpotlight:exactMatchedLaunchString:lastUsedDate:recentEngagementDateInSpotlight:recentEngagementDateOutSpotlight:nominateLocalTopHit:
+ _objc_msgSend$setEntityBadgeType:
+ _objc_msgSend$shouldFilterResult:currentTime:isScopedSearch:
+ _objc_msgSend$sortDescriptorWithKey:ascending:
+ _objc_msgSend$sortedArrayUsingDescriptors:
+ _objc_msgSend$topHitCandidacyThresholdingForSection:
+ _objc_msgSend$whiteSpaceCondensedDescriptions:
+ _timeZoneOffsetDescriptionForDate:timeZone:.onceToken.271
- +[PRSRankingItemRanker shouldFilterResult:currentTime:]
- +[PRSRankingItemRanker thresholdResultsInSection:userQuery:queryID:isEntitiesSearch:currentTime:]
- -[SSRankingManager logPommesScoringForRankingItem:queryId:query:bundleID:name:topicality:freshness:engagement:likelihood:launchPortion:launchCount:engagedInSpotlight:exactMatchedLaunchString:lastUsedDate:recentEngagementDateInSpotlight:recentEngagementDateOutSpotlight:]
- GCC_except_table22
- GCC_except_table25
- GCC_except_table29
- GCC_except_table31
- GCC_except_table37
- GCC_except_table43
- GCC_except_table51
- GCC_except_table54
- GCC_except_table69
- GCC_except_table80
- GCC_except_table83
- GCC_except_table86
- ___97+[PRSRankingItemRanker thresholdResultsInSection:userQuery:queryID:isEntitiesSearch:currentTime:]_block_invoke
- ___block_descriptor_65_e8_32s40s_e57_B24?0"SFSearchResult_SpotlightExtras"8"NSDictionary"16ls32l8s40l8
- ___block_literal_global.154
- ___block_literal_global.200
- ___block_literal_global.245
- ___block_literal_global.320
- ___block_literal_global.336
- ___block_literal_global.358
- ___block_literal_global.369
- ___block_literal_global.436
- ___block_literal_global.476
- ___block_literal_global.484
- ___block_literal_global.517
- __unnamed_array_storage.325
- __unnamed_array_storage.331
- __unnamed_array_storage.334
- __unnamed_array_storage.337
- __unnamed_array_storage.340
- __unnamed_array_storage.349
- __unnamed_array_storage.374
- __unnamed_array_storage.380
- _objc_msgSend$initWithIdentifier:bundleIdentifier:protectionClass:attributeKeys:attributeValues:
- _objc_msgSend$logPommesScoringForRankingItem:queryId:query:bundleID:name:topicality:freshness:engagement:likelihood:launchPortion:launchCount:engagedInSpotlight:exactMatchedLaunchString:lastUsedDate:recentEngagementDateInSpotlight:recentEngagementDateOutSpotlight:
- _objc_msgSend$shouldFilterResult:currentTime:
- _timeZoneOffsetDescriptionForDate:timeZone:.onceToken.264
CStrings:
+ "@68@0:8@16@24@32@40@48i56@60"
+ "My"
+ "TQ,N,V_entityBadgeType"
+ "WEATHER"
+ "[SpotlightRanking] <Engagement_Debug> Rule: app %@ TH candidacy thresholded in favor of app %@ with shortcuts."
+ "[SpotlightRanking] <Engagement_Debug> [TH=%d] qid: %llu, query: %@, isLocalCand: %d, bundleID: %@, name: %@, topicality: %f, freshness: %f, launchPortion: %f, launchCount: %f, engagement: %f, likelihood: %f, engagedInSpotlight: %d, exactMatchedLaunchString: %d, lastUsedDate: %@, recentEngInSpotlight: %@, recentEngOutSpotlight: %@, ri: %p/%p/%lu"
+ "_entityBadgeType"
+ "com.apple.facetime"
+ "com.apple.finance.order"
+ "com.apple.mobilephone"
+ "com.mr-brightside.myParcel"
+ "defaultCityForTimeZone:"
+ "entityBadgeType"
+ "hasSpecialAppPrefix"
+ "initWithIdentifier:bundleIdentifier:protectionClass:attributeKeys:attributeValues:type:completion:"
+ "isAllowlistedBundle:"
+ "localizedLowercaseString"
+ "logPommesScoringForRankingItem:queryId:query:bundleID:name:topicality:freshness:engagement:likelihood:launchPortion:launchCount:engagedInSpotlight:exactMatchedLaunchString:lastUsedDate:recentEngagementDateInSpotlight:recentEngagementDateOutSpotlight:nominateLocalTopHit:"
+ "my"
+ "setEntityBadgeType:"
+ "shouldFilterResult:currentTime:isScopedSearch:"
+ "sortDescriptorWithKey:ascending:"
+ "sortedArrayUsingDescriptors:"
+ "thresholdResultsInSection:userQuery:queryID:isEntitiesSearch:currentTime:isScopedSearch:"
+ "topHitCandidacyThresholdingForSection:"
+ "v116@0:8@16Q24@32@40@48f56f60f64f68f72f76B80B84@88@96@104B112"
+ "v32@?0@\"NSNumber\"8@\"NSNumber\"16^B24"
+ "v56@0:8@16@24q32B40d44B52"
- "B32@0:8@16d24"
- "[SpotlightRanking] <Engagement_Debug> qid: %llu, query: %@, isLocalCand: %d, bundleID: %@, name: %@, topicality: %f, freshness: %f, launchPortion: %f, launchCount: %f, engagement: %f, likelihood: %f, engagedInSpotlight: %d, exactMatchedLaunchString: %d, lastUsedDate: %@, recentEngInSpotlight: %@, recentEngOutSpotlight: %@, ri: %p/%p/%lu"
- "logPommesScoringForRankingItem:queryId:query:bundleID:name:topicality:freshness:engagement:likelihood:launchPortion:launchCount:engagedInSpotlight:exactMatchedLaunchString:lastUsedDate:recentEngagementDateInSpotlight:recentEngagementDateOutSpotlight:"
- "shouldFilterResult:currentTime:"
- "thresholdResultsInSection:userQuery:queryID:isEntitiesSearch:currentTime:"
- "v112@0:8@16Q24@32@40@48f56f60f64f68f72f76B80B84@88@96@104"
- "v52@0:8@16@24q32B40d44"

```
