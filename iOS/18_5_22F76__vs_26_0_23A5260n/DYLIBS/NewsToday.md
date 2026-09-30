## NewsToday

> `/System/Library/PrivateFrameworks/NewsToday.framework/NewsToday`

```diff

-5681.0.0.0.0
-  __TEXT.__text: 0x3c7f0
+5718.1.0.0.0
+  __TEXT.__text: 0x3c6c4
   __TEXT.__auth_stubs: 0xa80
-  __TEXT.__objc_methlist: 0x568c
-  __TEXT.__const: 0x25a
-  __TEXT.__oslogstring: 0x10c0
-  __TEXT.__cstring: 0x7b25
+  __TEXT.__objc_methlist: 0x576c
+  __TEXT.__const: 0x2ba
+  __TEXT.__oslogstring: 0x1120
+  __TEXT.__cstring: 0x7aa5
   __TEXT.__ustring: 0x16
   __TEXT.__gcc_except_tab: 0xb00
   __TEXT.__constg_swiftt: 0x6c
-  __TEXT.__swift5_typeref: 0x17d
+  __TEXT.__swift5_typeref: 0x17f
   __TEXT.__swift5_reflstr: 0x1d
   __TEXT.__swift5_fieldmd: 0x38
   __TEXT.__swift5_capture: 0x6c

   __TEXT.__swift5_types: 0x8
   __TEXT.__swift_as_entry: 0x1c
   __TEXT.__swift_as_ret: 0x20
-  __TEXT.__unwind_info: 0xbd8
-  __TEXT.__eh_frame: 0x3d0
+  __TEXT.__unwind_info: 0xbb8
+  __TEXT.__eh_frame: 0x400
   __TEXT.__objc_classname: 0xa1c
-  __TEXT.__objc_methname: 0xff27
-  __TEXT.__objc_methtype: 0x1bff
+  __TEXT.__objc_methname: 0x1010b
+  __TEXT.__objc_methtype: 0x1bed
   __TEXT.__objc_stubs: 0x8900
   __DATA_CONST.__got: 0x920
-  __DATA_CONST.__const: 0x1668
+  __DATA_CONST.__const: 0x15f8
   __DATA_CONST.__objc_classlist: 0x1d0
   __DATA_CONST.__objc_catlist: 0x78
   __DATA_CONST.__objc_protolist: 0x180
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3510
+  __DATA_CONST.__objc_selrefs: 0x35a8
   __DATA_CONST.__objc_protorefs: 0x60
   __DATA_CONST.__objc_superrefs: 0x1a8
   __DATA_CONST.__objc_arraydata: 0x1a0
   __AUTH_CONST.__auth_got: 0x550
   __AUTH_CONST.__const: 0x6e8
-  __AUTH_CONST.__cfstring: 0x1cc0
-  __AUTH_CONST.__objc_const: 0xbe88
+  __AUTH_CONST.__cfstring: 0x1d20
+  __AUTH_CONST.__objc_const: 0xc060
   __AUTH_CONST.__objc_intobj: 0xf0
   __AUTH_CONST.__objc_dictobj: 0x1b8
   __AUTH_CONST.__objc_arrayobj: 0x30

   __AUTH.__objc_data: 0x2f0
   __AUTH.__data: 0x30
   __DATA.__objc_ivar: 0x53c
-  __DATA.__data: 0xf10
+  __DATA.__data: 0xeb0
   __DATA.__bss: 0x1b0
   __DATA_DIRTY.__objc_data: 0xfa0
   __DATA_DIRTY.__bss: 0x78

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
+  - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
-  - /usr/lib/swift/libswiftCryptoTokenKit.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftMLCompute.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftNaturalLanguage.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_errno.dylib
-  - /usr/lib/swift/libswift_math.dylib
-  - /usr/lib/swift/libswift_signal.dylib
-  - /usr/lib/swift/libswift_stdio.dylib
-  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  - /usr/lib/swift/libswiftsys_time.dylib
-  - /usr/lib/swift/libswiftunistd.dylib
-  UUID: C707EFA7-409D-3F1A-BD95-2D6A8B4D8973
-  Functions: 1653
-  Symbols:   6223
-  CStrings:  3609
+  UUID: 2F0CA9CE-FF17-3BA8-9258-E71E6381BB44
+  Functions: 1655
+  Symbols:   6018
+  CStrings:  3631
 
Symbols:
+ -[NTTodayContext writeUserDidReadHeadlineWithAnalyticsElement:atDate:]
+ -[NTTodayContext writeUserDidReadHeadlineWithAnalyticsElement:atDate:].cold.1
+ -[NTTodayContext writeUserDidReadHeadlineWithAnalyticsElement:atDate:].cold.2
+ -[NTTodayContext writeUserDidSeeHeadlinesWithAnalyticsElements:atDate:]
+ -[NTTodayContext writeUserDidSeeHeadlinesWithAnalyticsElements:atDate:].cold.1
+ -[NTTodayContext writeUserDidSeeHeadlinesWithAnalyticsElements:atDate:].cold.2
+ _NTTodaySectionReadArticlesFilterMethodToNSString
+ _NTTodaySectionSeenArticlesFilterMethodToNSString
+ ___71-[NTTodayContext writeUserDidSeeHeadlinesWithAnalyticsElements:atDate:]_block_invoke
+ ___71-[NTTodayContext writeUserDidSeeHeadlinesWithAnalyticsElements:atDate:]_block_invoke_2
+ ___block_descriptor_32_e32_16?0"<FCReadingHistoryItem>"8l
+ ___block_literal_global.30
+ ___block_literal_global.32
+ ___block_literal_global.36
+ ___block_literal_global.45
+ __swift_FORCE_LOAD_$_swiftAccelerate
+ __swift_FORCE_LOAD_$_swiftAccelerate_$_NewsToday
+ __swift_FORCE_LOAD_$_swiftCoreImage
+ __swift_FORCE_LOAD_$_swiftCoreImage_$_NewsToday
+ __swift_FORCE_LOAD_$_swiftMLCompute
+ __swift_FORCE_LOAD_$_swiftMLCompute_$_NewsToday
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_NewsToday
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_NewsToday
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_NewsToday
+ _objc_msgSend$writeReadHistoryItem:
+ _objc_msgSend$writeSeenHistoryItems:
+ _symbolic So7NSArrayCSgSo12NSDictionaryCSg_____So7NSErrorCSgIeyBhyyyy_ 10ObjectiveC8ObjCBoolV
- -[NTTodayContext writeUserDidReadHeadlineWithAnalyticsElement:atDate:withCompletion:]
- -[NTTodayContext writeUserDidReadHeadlineWithAnalyticsElement:atDate:withCompletion:].cold.1
- -[NTTodayContext writeUserDidReadHeadlineWithAnalyticsElement:atDate:withCompletion:].cold.2
- -[NTTodayContext writeUserDidSeeHeadlinesWithAnalyticsElements:atDate:withCompletion:]
- -[NTTodayContext writeUserDidSeeHeadlinesWithAnalyticsElements:atDate:withCompletion:].cold.1
- -[NTTodayContext writeUserDidSeeHeadlinesWithAnalyticsElements:atDate:withCompletion:].cold.2
- ___86-[NTTodayContext writeUserDidSeeHeadlinesWithAnalyticsElements:atDate:withCompletion:]_block_invoke
- ___86-[NTTodayContext writeUserDidSeeHeadlinesWithAnalyticsElements:atDate:withCompletion:]_block_invoke_2
- ___block_descriptor_32_e34_16?0"<FCTodaySeenHistoryItem>"8l
- ___block_descriptor_32_e34_q16?0"<FCTodaySeenHistoryItem>"8l
- ___block_descriptor_32_e42_"NSDate"16?0"<FCTodaySeenHistoryItem>"8l
- ___block_descriptor_32_e44_"NSString"16?0"<FCTodaySeenHistoryItem>"8l
- ___block_literal_global.48
- __swift_FORCE_LOAD_$_swiftCryptoTokenKit
- __swift_FORCE_LOAD_$_swiftCryptoTokenKit_$_NewsToday
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_errno_$_NewsToday
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_math_$_NewsToday
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_signal_$_NewsToday
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_stdio_$_NewsToday
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swift_time_$_NewsToday
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftsys_time_$_NewsToday
- __swift_FORCE_LOAD_$_swiftunistd
- __swift_FORCE_LOAD_$_swiftunistd_$_NewsToday
- _objc_msgSend$writeReadHistoryItem:withCompletion:
- _objc_msgSend$writeSeenHistoryItems:withCompletion:
- _symbolic So7NSArrayCSgSo12NSDictionaryCSg_____So7NSErrorCSgIeyByyyy_ 10ObjectiveC8ObjCBoolV
CStrings:
+ "-[NTTodayContext writeUserDidReadHeadlineWithAnalyticsElement:atDate:]"
+ "-[NTTodayContext writeUserDidSeeHeadlinesWithAnalyticsElements:atDate:]"
+ "@16@?0@\"<FCReadingHistoryItem>\"8"
+ "ArticleID"
+ "None"
+ "Version"
+ "adSponsorshipsEnabled"
+ "configurableOffersEnabled"
+ "configurableOffersMappingResourceId"
+ "defaultTTLForArticleRecords"
+ "defaultTTLForIssueRecords"
+ "defaultTTLForPurchaseLookupRecords"
+ "defaultTTLForPuzzleRecords"
+ "defaultTTLForPuzzleTypeRecords"
+ "defaultTTLForRecipeListRecords"
+ "defaultTTLForRecipeRecords"
+ "defaultTTLForSportsEventRecords"
+ "defaultTTLForTagRecords"
+ "exportToGroceryListEnabled"
+ "freeRecentRecipeListIDs"
+ "freeTagRecipeListIDPrefix"
+ "isTodaySponsorshipEligible"
+ "lastModifiedDate"
+ "paidRecentRecipeListIDs"
+ "paidTagRecipeListIDPrefix"
+ "recipeAutoFavoritesServiceConfigurationJSONData"
+ "recipePersonalizationAllowlistResourceId"
+ "recipePersonalizationBundleIdMappingResourceId"
+ "recipePersonalizationUrlMappingResourceId"
+ "todayWidgetForYouMaxAIGArticles"
+ "v32@0:8@\"<NTHeadlineAnalyticsElementProviding>\"16@\"NSDate\"24"
+ "v32@0:8@\"NSArray\"16@\"NSDate\"24"
+ "will apply filter transformation to section, name=%{public}@, supplementalOptions=%{public}@, readFilterMethod=%{public}@, seenFilterMethod=%{public}@, minimumTimeSinceFirstSeenToFilter=%lld"
+ "writeReadHistoryItem:"
+ "writeSeenHistoryItems:"
+ "writeUserDidReadHeadlineWithAnalyticsElement:atDate:"
+ "writeUserDidSeeHeadlinesWithAnalyticsElements:atDate:"
- "-[NTTodayContext writeUserDidReadHeadlineWithAnalyticsElement:atDate:withCompletion:]"
- "-[NTTodayContext writeUserDidSeeHeadlinesWithAnalyticsElements:atDate:withCompletion:]"
- "@\"NSDate\"16@?0@\"<FCTodaySeenHistoryItem>\"8"
- "@\"NSString\"16@?0@\"<FCTodaySeenHistoryItem>\"8"
- "@16@?0@\"<FCTodaySeenHistoryItem>\"8"
- "q16@?0@\"<FCTodaySeenHistoryItem>\"8"
- "recipeCatalogSearchConfigurationProfiles"
- "recipeTagRecipeListIDPrefix"
- "respectRecipeChannelGroupingEligibility"
- "sportsSearchConfigurationProfiles"
- "sportsSyncingConfigurationV2ResourceId"
- "v40@0:8@\"<NTHeadlineAnalyticsElementProviding>\"16@\"NSDate\"24@?<v@?>32"
- "v40@0:8@\"NSArray\"16@\"NSDate\"24@?<v@?>32"
- "will apply filter transformation to section, name=%{public}@, supplementalOptions=%{public}@"
- "writeReadHistoryItem:withCompletion:"
- "writeSeenHistoryItems:withCompletion:"
- "writeUserDidReadHeadlineWithAnalyticsElement:atDate:withCompletion:"
- "writeUserDidSeeHeadlinesWithAnalyticsElements:atDate:withCompletion:"

```
