## Spotlight

> `/System/Library/PrivateFrameworks/Spotlight.framework/Spotlight`

```diff

-2328.7.8.5.0
-  __TEXT.__text: 0x4e49c
-  __TEXT.__auth_stubs: 0x1030
-  __TEXT.__objc_methlist: 0x1d14
-  __TEXT.__const: 0x148
-  __TEXT.__cstring: 0x27d3
-  __TEXT.__oslogstring: 0x1fbd
-  __TEXT.__gcc_except_tab: 0x44a8
-  __TEXT.__unwind_info: 0xb08
-  __TEXT.__objc_classname: 0x230
-  __TEXT.__objc_methname: 0x9065
-  __TEXT.__objc_methtype: 0x1e16
-  __TEXT.__objc_stubs: 0x87c0
-  __DATA_CONST.__got: 0x1290
-  __DATA_CONST.__const: 0xb78
+2333.7.0.1.0
+  __TEXT.__text: 0x4f7ac
+  __TEXT.__auth_stubs: 0x1050
+  __TEXT.__objc_methlist: 0x1fcc
+  __TEXT.__const: 0x168
+  __TEXT.__gcc_except_tab: 0x46dc
+  __TEXT.__oslogstring: 0x21cc
+  __TEXT.__cstring: 0x2864
+  __TEXT.__unwind_info: 0xbf0
+  __TEXT.__eh_frame: 0x60
+  __TEXT.__objc_classname: 0x231
+  __TEXT.__objc_methname: 0x9249
+  __TEXT.__objc_methtype: 0x1e27
+  __TEXT.__objc_stubs: 0x8860
+  __DATA_CONST.__got: 0x12d0
+  __DATA_CONST.__const: 0xb70
   __DATA_CONST.__objc_classlist: 0xb0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2690
+  __DATA_CONST.__objc_selrefs: 0x2790
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x80
   __DATA_CONST.__objc_arraydata: 0x3f8
-  __AUTH_CONST.__auth_got: 0x830
-  __AUTH_CONST.__const: 0x708
-  __AUTH_CONST.__cfstring: 0x28a0
-  __AUTH_CONST.__objc_const: 0x3b00
+  __AUTH_CONST.__auth_got: 0x840
+  __AUTH_CONST.__const: 0x6c8
+  __AUTH_CONST.__cfstring: 0x29a0
+  __AUTH_CONST.__objc_const: 0x3730
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__objc_intobj: 0xf0
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH.__objc_data: 0xa0
   __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0x388
-  __DATA.__data: 0x280
-  __DATA.__bss: 0xc0
+  __DATA.__objc_ivar: 0x394
+  __DATA.__data: 0x298
+  __DATA.__bss: 0xa8
   __DATA_DIRTY.__objc_data: 0x640
-  __DATA_DIRTY.__data: 0x11
-  __DATA_DIRTY.__bss: 0x4f0
+  __DATA_DIRTY.__data: 0x21
+  __DATA_DIRTY.__bss: 0x460
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 862
-  Symbols:   1783
-  CStrings:  2422
+  Functions: 935
+  Symbols:   1872
+  CStrings:  2447
 
Symbols:
+ _MDItemAppEntityTitle
+ _MDItemEventRestaurantMealType
+ _MDItemEventUpdateStatus
+ _MDItemExtractedAddressesLabels
+ _MDItemExtractedCurrenciesValues
+ _MDItemExtractedDatesValues
+ _MDItemExtractedEmailsLabels
+ _MDItemExtractedFlightsLabels
+ _MDItemExtractedLinksLabels
+ _MDItemExtractedLocationsValues
+ _MDItemExtractedPhoneNumbersLabels
+ _MDItemExtractedTrackingNumbersLabels
+ _MDItemFileProviderFilename
+ _MDItemMessageType
+ _MDItemPassbookIsPaymentPass
+ _MDItemPhotosTitle
+ _MDItemThumbnailData
+ _OBJC_CLASS_$_SPECRGroundedPerson
+ __Z13printHeapInfoyRKNSt3__16vectorI17SPResultValueItemNS_9allocatorIS1_EEEEP8NSStringb
+ __Z14getContainerIdPK16CSSearchableItem
+ __Z18getGreaterOperatoribP8NSString
+ __Z19printRetrievedItemsyRKNSt3__13setIU8__strongP8NSStringNS_4lessIS3_EENS_9allocatorIS3_EEEEiS2_b
+ __Z21getRetrievalTypeIndexib
+ __ZN17SPResultValueItemC1EP16CSSearchableItemd
+ __ZN17SPResultValueItemC2EP16CSSearchableItemd
+ __ZNK37SPResultItemHashTableEntryRankingLessclERK31SPResultValueItemHashTableEntryS2_
+ __ZNK37SPResultItemHashTableEntryRecencyLessclERK31SPResultValueItemHashTableEntryS2_
+ _memcpy
+ _objc_retainAutoreleasedReturnValue
- _MDItemExtractedAddresses
- _MDItemExtractedCurrencies
- _MDItemExtractedDates
- _MDItemExtractedEmails
- _MDItemExtractedFlights
- _MDItemExtractedLinks
- _MDItemExtractedLocations
- _MDItemExtractedPhoneNumbers
- _MDItemExtractedTrackingNumbers
- _MDMessageIndexType
CStrings:
+ "\x02#"
+ "\x03\x11\x11\xf0*\x11\x13B\x111!"
+ "%@ %@"
+ "-[SPCSSearchQuery rankAndSendResultsWithResponseKind:withResultSections:withResultSets:withiCloudDriveResultSet:withMailResultSet:withCalendarResultSet:]"
+ "AlbumEntity"
+ "MemoryEntity"
+ "SharedAlbumEntity"
+ "T@\"NSArray\",&,N,V_ecrGroundedPersons"
+ "TB,N,V_isSearchTool"
+ "[qid=%llu][SpotlightRanking]<_resultHeaps> added %d items for bundle = %@, retrievalType = %d (min: %f, max: %f)"
+ "[qid=%llu][SpotlightRanking]<_resultHeaps> added %d items for bundle = %@, retrievalType = %d (minScore: %f, maxScore: %f - minTS: %f, maxTS: %f)"
+ "[qid=%llu][SpotlightRanking]<_resultHeaps> hash tables added %d items for bundle = %@, retrievalType = %d (min timestamp: %f, max timestamp: %f, queryTime: %f)"
+ "[qid=%llu][SpotlightRanking]<_resultHeaps> retrieved %d (out of %d) items for bundle = %@, retrievalType = %d: %@"
+ "[qid=%llu][SpotlightRanking]<_resultHeaps> retrieved %d items for bundle = %@, retrievalType = %d"
+ "_ecrGroundedPersons"
+ "_isSearchTool"
+ "_retrievedIds"
+ "attrHasPhotosAlbumMemoryResult:"
+ "collectSearchResults:"
+ "ecrGroundedPersons"
+ "foundItems:"
+ "initWithName:relationLabel:ecrToken:queryRawToken:"
+ "isCardEventSearch"
+ "isSearchTool"
+ "kMDItemAppEntityTitle"
+ "makePhotosAlbumMemoryResultForAppEntity:dataclass:queryContext:score:"
+ "nominateLocalTopHitsFromSections:withItemRanker:sectionHeader:maxInitiallyVisibleResults:shortcutResult:isBullseyeNonCommittedSearch:isBullseyeCommittedSearch:parsecEnabled:maxNumAppsInTopHitSection:queryId:isSearchToolClient:qu:currentTime:"
+ "parseQUQuery:"
+ "personRelationMap"
+ "rankAndSendResultsWithResponseKind:withResultSections:withResultSets:withiCloudDriveResultSet:withMailResultSet:withCalendarResultSet:"
+ "rankingConfigurationWithMeContact:emailAddresses:phoneFavorites:vipList:clientBundle:isScopedSearch:isAdvancedSyntax:spotlightQuery:userQuery:tokenString:queryKind:isPeopleSearch:isSearchToolClient:keyboardLanguage:"
+ "rawQueryToken"
+ "setEcrGroundedPersons:"
+ "setIsSearchTool:"
+ "thresholdResultsInSection:userQuery:queryID:isEntitiesSearch:currentTime:isScopedSearch:isSearchToolClient:"
+ "titleStringFromAttrsForAlbumMemory:"
+ "updateScoresForPreparedItems:isCJK:clientBundleID:thresholdValue:queryNodeMatchInfo:collectL2Signals:isCardSearch:"
+ "updateToDoItemResult:withAttrs:"
+ "v60@0:8i16@20@28@36@44@52"
+ "{vector<std::set<NSString *>, std::allocator<std::set<NSString *>>>=\"__begin_\"^v\"__end_\"^v\"__end_cap_\"{__compressed_pair<std::set<NSString *> *, std::allocator<std::set<NSString *>>>=\"__value_\"^v}}"
+ "{vector<std::vector<SPResultValueItem>, std::allocator<std::vector<SPResultValueItem>>>=\"__begin_\"^v\"__end_\"^v\"__end_cap_\"{__compressed_pair<std::vector<SPResultValueItem> *, std::allocator<std::vector<SPResultValueItem>>>=\"__value_\"^v}}"
+ "{vector<tt_hash_table<SPResultValueItemHashTableEntry>, std::allocator<tt_hash_table<SPResultValueItemHashTableEntry>>>=\"__begin_\"^v\"__end_\"^v\"__end_cap_\"{__compressed_pair<tt_hash_table<SPResultValueItemHashTableEntry> *, std::allocator<tt_hash_table<SPResultValueItemHashTableEntry>>>=\"__value_\"^v}}"
- "\x02\""
- "\x03\x11\x11\xea\x11\x132\x111!"
- "-[SPCSSearchQuery rankAndSendResultsWithResponseKind:withResultSections:withResultSets:withiCloudDriveSection:withMailResultSet:]"
- "[SpotlightRanking] <_resultHeaps> added %d items for bundle = %@, retrievalType = %d (min: %f, max: %f)"
- "authorStringFromAttrs:"
- "collectSearchResults:isSearchToolClient:"
- "foundItems:isSearchToolClient:"
- "initWithQueryString:context:"
- "makeDateBasedResult:result:"
- "nominateLocalTopHitsFromSections:withItemRanker:sectionHeader:maxInitiallyVisibleResults:shortcutResult:isBullseyeNonCommittedSearch:isBullseyeCommittedSearch:parsecEnabled:maxNumAppsInTopHitSection:queryId:queryKind:clientBundleID:qu:currentTime:"
- "parseQUQuery:isSearchToolClient:"
- "rankAndSendResultsWithResponseKind:withResultSections:withResultSets:withiCloudDriveSection:withMailResultSet:"
- "referenceDate"
- "sortResultsInSection:"
- "thresholdResultsInSection:userQuery:queryID:isEntitiesSearch:currentTime:isScopedSearch:queryKind:clientBundleID:isSearchToolClient:"
- "updateScoresForPreparedItems:isCJK:clientBundleID:thresholdValue:queryNodeMatchInfo:collectL2Signals:"
- "v52@0:8i16@20@28@36@44"
- "{vector<std::vector<(anonymous namespace)::SPResultValueItem>, std::allocator<std::vector<(anonymous namespace)::SPResultValueItem>>>=\"__begin_\"^v\"__end_\"^v\"__end_cap_\"{__compressed_pair<std::vector<(anonymous namespace)::SPResultValueItem> *, std::allocator<std::vector<(anonymous namespace)::SPResultValueItem>>>=\"__value_\"^v}}"
- "{vector<tt_hash_table<(anonymous namespace)::SPResultValueItemHashTableEntry>, std::allocator<tt_hash_table<(anonymous namespace)::SPResultValueItemHashTableEntry>>>=\"__begin_\"^v\"__end_\"^v\"__end_cap_\"{__compressed_pair<tt_hash_table<(anonymous namespace)::SPResultValueItemHashTableEntry> *, std::allocator<tt_hash_table<(anonymous namespace)::SPResultValueItemHashTableEntry>>>=\"__value_\"^v}}"

```
