## spotlightknowledged

> `/System/Library/Frameworks/CoreSpotlight.framework/spotlightknowledged`

```diff

-2333.22.13.7.0
-  __TEXT.__text: 0xd4158
-  __TEXT.__auth_stubs: 0x1bb0
-  __TEXT.__objc_stubs: 0xcea0
-  __TEXT.__objc_methlist: 0x6130
-  __TEXT.__const: 0x6e2
-  __TEXT.__gcc_except_tab: 0x54a4
-  __TEXT.__cstring: 0x8485
-  __TEXT.__oslogstring: 0x8050
-  __TEXT.__objc_classname: 0xa1a
-  __TEXT.__objc_methname: 0xecdc
-  __TEXT.__objc_methtype: 0x1689
+2333.41.1.3.0
+  __TEXT.__text: 0xdc558
+  __TEXT.__auth_stubs: 0x1c00
+  __TEXT.__objc_stubs: 0xd660
+  __TEXT.__objc_methlist: 0x6598
+  __TEXT.__const: 0x70a
+  __TEXT.__gcc_except_tab: 0x5378
+  __TEXT.__cstring: 0x899a
+  __TEXT.__oslogstring: 0x81db
+  __TEXT.__objc_classname: 0xa4e
+  __TEXT.__objc_methname: 0xfa42
+  __TEXT.__objc_methtype: 0x1744
   __TEXT.__dlopen_cstrs: 0x5e
-  __TEXT.__unwind_info: 0x2ca0
-  __DATA_CONST.__auth_got: 0xdf0
-  __DATA_CONST.__got: 0x818
+  __TEXT.__unwind_info: 0x2db8
+  __DATA_CONST.__auth_got: 0xe18
+  __DATA_CONST.__got: 0x848
   __DATA_CONST.__auth_ptr: 0x18
-  __DATA_CONST.__const: 0x5210
-  __DATA_CONST.__cfstring: 0xa5c0
-  __DATA_CONST.__objc_classlist: 0x448
+  __DATA_CONST.__const: 0x53f0
+  __DATA_CONST.__cfstring: 0xaba0
+  __DATA_CONST.__objc_classlist: 0x458
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x2b8
-  __DATA_CONST.__objc_intobj: 0x6c0
-  __DATA_CONST.__objc_arraydata: 0xaa8
-  __DATA_CONST.__objc_arrayobj: 0x708
-  __DATA_CONST.__objc_dictobj: 0x230
+  __DATA_CONST.__objc_superrefs: 0x2c0
+  __DATA_CONST.__objc_intobj: 0x750
+  __DATA_CONST.__objc_arraydata: 0xaf8
+  __DATA_CONST.__objc_arrayobj: 0x690
+  __DATA_CONST.__objc_dictobj: 0x280
   __DATA_CONST.__objc_doubleobj: 0x20
-  __DATA.__objc_const: 0xa908
-  __DATA.__objc_selrefs: 0x3ae0
-  __DATA.__objc_ivar: 0x6dc
-  __DATA.__objc_data: 0x2ad0
+  __DATA.__objc_const: 0xaf98
+  __DATA.__objc_selrefs: 0x3d60
+  __DATA.__objc_ivar: 0x744
+  __DATA.__objc_data: 0x2b70
   __DATA.__data: 0x558
-  __DATA.__bss: 0xdf8
+  __DATA.__bss: 0xe08
   __DATA.__common: 0x4
   - /System/Library/Frameworks/Contacts.framework/Versions/A/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 3636
-  Symbols:   703
-  CStrings:  5186
+  Functions: 3754
+  Symbols:   714
+  CStrings:  5368
 
Symbols:
+ _MDItemCardType
+ _MDItemEmbeddingVersion
+ _MDItemEventType
+ _MDItemExtractedAddresses
+ _MDItemExtractedLocations
+ _MDItemKeyphraseLabels
+ _MDItemKeyphraseVersion
+ _OBJC_CLASS_$_NSCountedSet
+ _SIGeoIndexEnumerateGeoExpansionsForID
+ _SILanguagesIsCJK
+ _asin
+ _cos
+ _sin
- _OBJC_CLASS_$_LNSpotlightCascadeAllowList
- _OBJC_CLASS_$_NSNull
CStrings:
+ "\x06"
+ "\a\x16\xf0$"
+ "\t"
+ "\t\t"
+ "\t\t\t"
+ "\t%@:\n\t\t%@\n"
+ "\n\t"
+ "\n\t\t"
+ "\nTotal: bundles: %@,%@, total: %@"
+ "\x0f\x01FE"
+ "\x14"
+ " && (%@)"
+ " || "
+ "### %@ Excluding bundle after couting zero AppEntities: %@"
+ "### %@ Failed delete item with uniqueID: \"%@\" with error: %@"
+ "### %@ Failed to add or update item with uniqueID: \"%@\" with error: %@"
+ "### %@ Including bundle despite failed count query: %@"
+ "### %@ Retries exhausted (limit %u). Abandoning journal update with serialNumber: %lld for bundle: %@"
+ "### %@ fetchBundleIds returned bundles: [%@]"
+ "### %@ fetchBundleIds returned error: %@"
+ "### %@ handling %@ for journal update with serialNumber: %lld from bundle: %@ indexType: %s"
+ "%@\n\t%@\n"
+ "%@ SKIPPING add for item uniqueID: \"%@\" with serialNumber:%llu < latestSerialNumber:%llu from bundle: %@"
+ "%@ SKIPPING delete for item uniqueID: \"%@\" with serialNumber:%llu < latestSerialNumber:%llu from bundle: %@"
+ "%@!=%@"
+ "%@%@ %@, total: %@"
+ "%u"
+ "((_kMDItemUpdaterVersion=*&&_kMDItemUpdaterVersion!=%ld)||(_kMDItemUpdaterLastRequested=*&&_kMDItemUpdaterLastRequested<%ld)&&(_kMDItemUpdaterRequestedCount=*&&_kMDItemUpdaterRequestedCount<10))"
+ "** Extraction report **"
+ "** Pipeline report **"
+ "-[SKGUpdaterAgent handleLaunchUpgradeTasks:]"
+ "2`"
+ ":INC:_kMDItemUpdaterRequestedCount"
+ "<%@: %f %f %f %@>"
+ "=== end %@ ]\n"
+ "@\"SKGQueryStringBuilder\"24@?0@\"NSArray\"8@\"NSString\"16"
+ "@\"SKGQueryStringBuilder\"40@?0@\"NSString\"8@\"NSString\"16@\"NSString\"24@\"NSArray\"32"
+ "@128@0:8I16@20@28@36@?44@?52@?60@68@76@84@92q100B108@112@?120"
+ "@32@0:8@16q24"
+ "@40@0:8@16I24i28@?32"
+ "@72@0:8Q16r*24r*32{?=*Q{?=IC}}40i64I68"
+ "@?24@0:8@16"
+ "B24@?0@\"NSString\"8@\"NSDictionary\"16"
+ "B44@0:8@\"CSEventListenerDeletion\"16B24@?<v@?Qq@\"NSError\">28@?<B@?>36"
+ "B52@0:8@16@24B32@?36@?44"
+ "B52@0:8@16@24I32@36@?44"
+ "B52@0:8i16Q20Q28@?36@?44"
+ "B64@0:8@16@24Q32@?40@?48@?56"
+ "CSAppEntityUpdaterHandleDeletion"
+ "CSAppEntityUpdaterHandleDonation"
+ "CSEventListenerDeletion"
+ "ExtractedAddress"
+ "ExtractedLocations"
+ "NeedsDocumentUnderstanding"
+ "NeedsEmbeddings"
+ "NeedsKeyphrases"
+ "NeedsSuggestedEvents"
+ "PurgeCount"
+ "PurgedBytes"
+ "SKGAirportLocation"
+ "SKGTextQueryManager"
+ "SearchToolPhotosCrossBundleSearch"
+ "T@\"NSArray\",C,N,V_airportInfo"
+ "T@\"NSString\",C,N,V_airportCode"
+ "T@\"NSString\",C,N,V_airportCountry"
+ "T@\"NSString\",C,N,V_airportLocality"
+ "T@\"NSString\",C,N,V_airportRegion"
+ "T@?,R,N,V_withAttributeValues"
+ "T@?,R,N,V_withQueries"
+ "TB,N,V_isDepartureAirport"
+ "Td,N,V_distanceFactor1"
+ "Td,N,V_distanceFactor2"
+ "Tq,N,V_currentRedonationDate"
+ "Tq,N,V_maxJournalSizeWhenLowDiskSpace"
+ "Tq,N,V_redonationThrottleHorizonDate"
+ "[ === %@\n"
+ "_airportCode"
+ "_airportCountry"
+ "_airportInfo"
+ "_airportLocality"
+ "_airportLocations"
+ "_airportRegion"
+ "_allFieldsPresentPredicateWithFieldNames:"
+ "_anyFieldPresentPredicateWithFieldNames:"
+ "_buildCSAttributeReportWithQueryString:queryContext:bundleID:reporter:cancelBlock:"
+ "_buildCSCountingReportWithQueryString:queryContext:flags:reporter:cancelBlock:"
+ "_countingAttributes"
+ "_countingPairs"
+ "_currentRedonationDate"
+ "_disabledTypeIdentifiersClause:"
+ "_distanceFactor1"
+ "_distanceFactor2"
+ "_donateJournalUpdateWithRecursiveRetry:donation:deletion:ledger:cancelBlock:completion:"
+ "_donateToCascadeWithReason:ledger:donation:deletion:completion:"
+ "_embeddingGenCompleteness"
+ "_embeddingGenCompletenessLock"
+ "_expansions"
+ "_fetchBundleIDsWithCompletionHandler:"
+ "_fieldPresencePredicateWithFieldName:"
+ "_handleIncrementalCascadeDonation:withReason:ledger:donation:deletion:error:"
+ "_handleJournalUpdateWithDonation:orDeletion:cancelBlock:completion:"
+ "_incrementFieldInDictionary:forKey:creatingIfNeeded:"
+ "_isDepartureAirport"
+ "_isDict"
+ "_kMDItemExtractedAddressesValues"
+ "_kMDItemUpdaterLastRequested"
+ "_kMDItemUpdaterRequestedCount"
+ "_lookupCitiesFromLocalCacheWithString:locale:countries:parents:"
+ "_lookupCountriesFromLocalCacheWithString:locale:"
+ "_lookupExpansionsFromLocalCacheWithLocation:locale:"
+ "_lookupParentsFromLocalCacheWithString:locale:countries:"
+ "_maxJournalSizeWhenLowDiskSpace"
+ "_newCounterDictionaryForBundleIdentifier:additionalAttributes:"
+ "_redonationThrottleHorizonDate"
+ "_reportingAttributes"
+ "_reportingPairs"
+ "_runCSAttributeQueryString:queryContext:foundAttrBlock:"
+ "_runCSCounterForQueryString:queryContext:filesQuery:counterItemBlock:cancelBlock:"
+ "_runCSReindexForQueryString:queryContext:processorFlags:batchProcessedBlock:batchUpdatedBlock:cancelBlock:"
+ "_verbosity"
+ "_withAttributeValues"
+ "_withQueries"
+ "addAirportLocation:"
+ "addAttribute:bundleID:"
+ "addFromRecord:bundleID:"
+ "addValue:attribute:bundleID:"
+ "airportCode"
+ "airportCountry"
+ "airportInfo"
+ "airportLocality"
+ "airportLocations"
+ "airportRegion"
+ "arrayByAddingObjectsFromArray:"
+ "attributes"
+ "breadcrumbs"
+ "bundles"
+ "cards"
+ "cleanupCount"
+ "cleanupPerBundleCount"
+ "com.apple.spotlightknowledged.JournalPurge"
+ "countForObject:"
+ "countingAttributes"
+ "currentRedonationDate"
+ "deletion"
+ "disabledAppEntityTypeIdentifiersForBundleIdentifier:"
+ "distance:"
+ "distanceFactor1"
+ "distanceFactor2"
+ "document-understanding"
+ "donation"
+ "embeddingCompleteness"
+ "embeddingDonationCount"
+ "embeddingGenComplete"
+ "embeddingGenCompleteness#%@"
+ "enableCountingAttribute:message:processor:"
+ "enableReportingAttribute:message:processor:"
+ "end batch querying"
+ "enumerateAirportCodesInStringUsingGeoScanner:entityBlock:"
+ "eventAllowed:"
+ "expansions"
+ "extractionReportForProcessor:bundles:attributes:"
+ "generateCSReportForQueryFlags:protectionClasses:additionalQueryString:additionalFetchAttributes:processedPredicate:succesfullyProcessedPredicate:eligiblePredicate:additionalPredicates:dayCompletionStr:genStartTime:bundleIDs:daysToCompleteApproach:onlyFiles:mergeBundleStatistics:withCancelBlock:"
+ "generateCSReportWithProtectionClasses:flags:verbosity:cancelBlock:"
+ "getCleanupItemCountsForListenerType:"
+ "getEmbeddingDonationItemCounts"
+ "getEmbeddingGenCompletenessForBundle:"
+ "getReindexRequestItemCounts"
+ "getTextContent:processedItem:"
+ "handleDeletion:turboEnabled:completionHandler:cancelBlock:"
+ "handleEmbeddingCompleteness for bundle:%@"
+ "handleEmbeddingCompleteness:"
+ "handleLaunchUpgradeTasks:"
+ "hasCards"
+ "hasEmbeddings"
+ "hasEvents"
+ "historical-reports"
+ "initWithSerialNumber:bundle:journalCookie:itemsObj:indexType:bundleHash:"
+ "initWithStartDate:endDate:"
+ "initWithVerbosity:"
+ "isCJKLanguage:"
+ "isDepartureAirport"
+ "itemsAwaitingRedonation"
+ "itemsAwaitingRedonationDict"
+ "itemsRedonationRequestCapReached"
+ "itemsRedonationRequestCapReachedDict"
+ "itemsSuccessfullyProcessed"
+ "iterateIdentifiers:"
+ "journalItemHasItemEmbeddingsSN:"
+ "journalItemHasNeedsEmbedding:"
+ "kMDItemEventFlightArrivalAirportCountry"
+ "kMDItemEventFlightArrivalAirportRegion"
+ "kMDItemEventFlightDepartureAirportCountry"
+ "kMDItemEventFlightDepartureAirportRegion"
+ "launchQueryUpdatesTasks"
+ "launchUpgradeTasks"
+ "locality"
+ "logAttribute:values:bundleID:"
+ "logCleanupItemCounts:bundleId:listenerType:"
+ "logEmbeddingDonationItemCounts:bundleId:"
+ "logReindexRequestItemCounts:bundleId:"
+ "longValue"
+ "maxJournalSizeWhenLowDiskSpace"
+ "needsSKGReindexerDocUnderstandingForRecord:bundleID:itemHasText:"
+ "needsSKGReindexerEmbeddingsForRecord:bundleID:itemHasText:"
+ "needsSKGReindexerSuggestedEventsForRecord:bundleID:itemHasText:"
+ "newDonations"
+ "pipelineReportForProcessor:bundles:attributes:"
+ "primaryEmbedding"
+ "processJournalRecordWithFd:atOffset:withSize:addBlock:delBlock:"
+ "processed"
+ "processing"
+ "q60@0:8@16C24@28@36@44^@52"
+ "queried"
+ "queryForAttributesAbsent:"
+ "queryForAttributesExist:"
+ "queryForDocUnderstandingUpdatesIncludeBundles:"
+ "queryForEmbeddingsUpdatesExcludeBundles:"
+ "queryForEmbeddingsUpdatesIncludeBundles:"
+ "queryForKeyphrasesUpdatesExcludeBundles:"
+ "queryForKeyphrasesUpdatesIncludeBundles:"
+ "queryForPipelineReport"
+ "queryForPipelineUpdatesWithExcludeBundles:taskQueries:throttleHorizonDate:"
+ "queryForPipelineUpdatesWithTaskQueries:throttleHorizonDate:"
+ "queryForSuggestedEventsUpdatesIncludeBundles:"
+ "queryForUpdaterVersionsWithThrottleHorizonDate:"
+ "redonationThrottleHorizonDate"
+ "reindexRequestPerBundleCount"
+ "removeItemWithSourceItemIdentifier:error:"
+ "reportingAttributes"
+ "resetCleanupItemCountsForAllListenerTypes"
+ "resetCleanupItemCountsForListenerType:"
+ "resetEmbeddingDonationItemCounts"
+ "resetReindexRequestItemCounts"
+ "secondaryEmbedding"
+ "setAirportCode:"
+ "setAirportCountry:"
+ "setAirportInfo:"
+ "setAirportLocality:"
+ "setAirportRegion:"
+ "setAttribute:"
+ "setCurrentRedonationDate:"
+ "setDistanceFactor1:"
+ "setDistanceFactor2:"
+ "setEmbeddingGenCompleteness:forBundle:"
+ "setFoundAttributesHandler:"
+ "setIsDepartureAirport:"
+ "setMaxJournalSizeWhenLowDiskSpace:"
+ "setRedonationThrottleHorizonDate:"
+ "sortUsingSelector:"
+ "starting batch querying"
+ "suggested-events"
+ "transportation.airport"
+ "updateSKGReindexerEmbeddingAttributes:record:bundleID:itemHasText:"
+ "v24@?0@\"NSString\"8@\"NSArray\"16"
+ "v24@?0@\"NSString\"8@\"NSDictionary\"16"
+ "v24@?0^{__CFString=}8^B16"
+ "v36@0:8Q16@24i32"
+ "v52@0:8C16@20@28@36@?44"
+ "v52@?0q8r*16{?=*Q{?=IC}}24B48"
+ "v64@0:8Q16@24@32@40@?48@?56"
+ "withAttributeValues"
+ "withQueries"
- "\a\x16\xf0#"
- "\n== Extraction report =="
- "\nTotals: bundleCount: %ld,%@"
- "\x0fFE"
- "### %@ Failed to add or update item %@ with error: %@"
- "### %@ Received %ld items from Spotlight in the foundItemsHandler"
- "### %@ Retries exhausted (limit %u). Abandoning journal update with serialNumber: %lld bundle: %@"
- "### %@ Spotlight query completed after %.3f seconds"
- "### %@ Spotlight query hit error: %@ after %.3f seconds"
- "### %@ Spotlight query was cancelled after %.3f seconds"
- "### %@ handling journal update with serialNumber: %lld for bundle: %@"
- "%@\n\t%@: %@"
- "%@:\t%@"
- "(_kMDItemUpdaterVersion=*&&_kMDItemUpdaterVersion!=%ld)"
- "(false)"
- "<%@: %f %f %f>"
- "== Pipeline report =="
- "=== %@ ===\n"
- "@120@0:8I16@20@28@36@44@52@60@68@76@84q92B100@104@?112"
- "@20@0:8I16"
- "@28@0:8@16B24"
- "@28@0:8@16I24"
- "@36@0:8I16@20@?28"
- "B44@0:8i16Q20Q28@?36"
- "B60@0:8@16@24B32@?36@?44@?52"
- "SKGJobQueryManager"
- "SearchToolCleanSlateDenseRetrieval"
- "_donateJournalUpdateWithRecursiveRetry:ledger:cancelBlock:completion:"
- "_donateToCascadeWithReason:ledger:donation:completion:"
- "_handleIncrementalCascadeDonation:withReason:ledger:donation:error:"
- "_increment:processor:bundleIdentifier:key:count:"
- "_loadKeyphraseConfig:"
- "_queryCountingPairs"
- "_queryReportingPairs"
- "_queryString"
- "_reportingCounter"
- "_runCSCounterForQueryString:queryContext:filesQuery:counterItemBlock:counterAttrBlock:cancelBlock:"
- "_runCSReindexForQueryString:queryContext:flags:batchProcessedBlock:batchUpdatedBlock:cancelBlock:"
- "addAttribute:processor:bundleIdentifier:"
- "appEntitySearchableItemsFromDonation:"
- "arrayWithArray:"
- "beginUpdatesTaskWithName:deviceUnlocked:knowledgedQueue:completeBlock:cancelBlock:deferBlock:"
- "com.apple.corespotlight.InternalTestsHost"
- "com.apple.corespotlight.TestsHost"
- "completedProcessing"
- "counter"
- "dictionaryWithDictionary:"
- "enumerateCountingAttributesForProcessor:usingBlock:"
- "enumerateFlagsUsingBlock:"
- "enumerateReportingAttributesForProcessor:usingBlock:"
- "generateCSReportForQueryFlags:protectionClasses:fetchAttributePairs:additionalQueryString:processedField:succesfullyProcessedField:eligibleFields:dayCompletionStr:genStartTime:bundleIDs:daysToCompleteApproach:onlyFiles:mergeBundleStatistics:withCancelBlock:"
- "generateCSReportWithFlags:protectionClasses:withCancelBlock:"
- "hardwareSupportsEmbedding"
- "hasAddresses"
- "hasBreadcrumbs"
- "hasLocations"
- "hasNamedLocations"
- "incrementProcessor:bundleIdentifier:"
- "initWithFlags:"
- "kMDItemExtractedAddresses"
- "kMDItemExtractedLocations"
- "logAttribute:bundleIdentifier:value:"
- "processJournalRecordWithFd:atOffset:withSize:usingBlock:"
- "processUpdatesWithJobContext:group:cancelBlock:"
- "q52@0:8@16C24@28@36^@44"
- "queryForDocUnderstandingUpdatesIncludeBundles:enabled:"
- "queryForEmbeddingsUpdatesExcludeBundles:enabled:"
- "queryForExtractionAttributes:"
- "queryForKeyphrasesUpdatesExcludeBundles:enabled:"
- "queryForPipelineUpdatesWithExcludeBundles:flags:"
- "queryForSuggestedEventsUpdatesIncludeBundles:enabled:"
- "queryForUpdaterVersions"
- "queryString"
- "setAttribute:processor:bundleIdentifier:count:"
- "shouldProcessUpdates"
- "stillProcessing"
- "text updating all done"
- "updating"
- "v20@?0@\"NSString\"8I16"
- "v28@?0I8^{__CFString=}12^B20"
- "v32@?0@\"NSString\"8@\"NSString\"16@\"NSNumber\"24"
- "v44@0:8C16@20@28@?36"
- "v48@0:8@16@24@?32@?40"

```
