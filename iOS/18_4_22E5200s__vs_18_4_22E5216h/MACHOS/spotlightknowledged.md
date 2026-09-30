## spotlightknowledged

> `/System/Library/Frameworks/CoreSpotlight.framework/spotlightknowledged`

```diff

-2333.18.0.8.0
-  __TEXT.__text: 0xb8790
-  __TEXT.__auth_stubs: 0x1d30
-  __TEXT.__objc_stubs: 0xc440
-  __TEXT.__objc_methlist: 0x5e30
-  __TEXT.__const: 0x6a2
-  __TEXT.__gcc_except_tab: 0x519c
-  __TEXT.__cstring: 0x7e0d
-  __TEXT.__oslogstring: 0x7372
-  __TEXT.__objc_classname: 0xa11
-  __TEXT.__objc_methname: 0xe1d0
-  __TEXT.__objc_methtype: 0x15d4
+2333.7.0.1.0
+  __TEXT.__text: 0xbfd60
+  __TEXT.__auth_stubs: 0x1d40
+  __TEXT.__objc_stubs: 0xcce0
+  __TEXT.__objc_methlist: 0x6098
+  __TEXT.__const: 0x6aa
+  __TEXT.__gcc_except_tab: 0x5410
+  __TEXT.__cstring: 0x8372
+  __TEXT.__oslogstring: 0x7fbd
+  __TEXT.__objc_classname: 0xa1a
+  __TEXT.__objc_methname: 0xeb31
+  __TEXT.__objc_methtype: 0x167a
   __TEXT.__dlopen_cstrs: 0x5e
-  __TEXT.__unwind_info: 0x2a38
-  __DATA_CONST.__auth_got: 0xeb0
-  __DATA_CONST.__got: 0x7e0
+  __TEXT.__unwind_info: 0x2b20
+  __DATA_CONST.__auth_got: 0xeb8
+  __DATA_CONST.__got: 0x818
   __DATA_CONST.__auth_ptr: 0x18
-  __DATA_CONST.__const: 0x48e0
-  __DATA_CONST.__cfstring: 0x9e00
-  __DATA_CONST.__objc_classlist: 0x440
+  __DATA_CONST.__const: 0x4b50
+  __DATA_CONST.__cfstring: 0xa480
+  __DATA_CONST.__objc_classlist: 0x448
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x2b0
-  __DATA_CONST.__objc_intobj: 0x630
-  __DATA_CONST.__objc_arraydata: 0xa70
-  __DATA_CONST.__objc_arrayobj: 0x780
-  __DATA_CONST.__objc_dictobj: 0x1e0
+  __DATA_CONST.__objc_superrefs: 0x2b8
+  __DATA_CONST.__objc_intobj: 0x660
+  __DATA_CONST.__objc_arraydata: 0xac0
+  __DATA_CONST.__objc_arrayobj: 0x750
+  __DATA_CONST.__objc_dictobj: 0x208
   __DATA_CONST.__objc_doubleobj: 0x20
-  __DATA.__objc_const: 0xa5a0
-  __DATA.__objc_selrefs: 0x3850
-  __DATA.__objc_ivar: 0x698
-  __DATA.__objc_data: 0x2a80
+  __DATA.__objc_const: 0xa848
+  __DATA.__objc_selrefs: 0x3a78
+  __DATA.__objc_ivar: 0x6cc
+  __DATA.__objc_data: 0x2ad0
   __DATA.__data: 0x550
-  __DATA.__bss: 0xdb0
+  __DATA.__bss: 0xe10
   __DATA.__common: 0x4
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers
   - /System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/BackgroundSystemTasks
+  - /System/Library/PrivateFrameworks/BiomeFoundation.framework/BiomeFoundation
   - /System/Library/PrivateFrameworks/CascadeSets.framework/CascadeSets
   - /System/Library/PrivateFrameworks/CipherML.framework/CipherML
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 3401
-  Symbols:   722
-  CStrings:  4947
+  Functions: 3484
+  Symbols:   728
+  CStrings:  5148
 
Symbols:
+ _OBJC_CLASS_$_BMFileBackedDictionary
+ _OBJC_CLASS_$_LNAvailabilityChecker
+ _OBJC_CLASS_$_NSDateInterval
+ _OBJC_CLASS_$_NSThread
+ _OBJC_CLASS_$_PIRGeoListSnippet
+ _OBJC_CLASS_$_SPHistoricalReportManager
+ _SPEmbeddingModelErrorDomain
+ _xpc_array_create
+ _xpc_dictionary_get_double
- _OBJC_CLASS_$_LNSpotlightCascadeLedger
- _OBJC_METACLASS_$_LNSpotlightCascadeLedger
- _renameat
CStrings:
+ "\x031"
+ "\n== Extraction report =="
+ "\nTotals: bundleCount: %ld,%@"
+ " %@: %@"
+ "### %@ %@ retry loop after error (%@) for journal update with serialNumber: %lld bundle: %@"
+ "### %@ Adding count (%ld) from Spotlight in the countChangedHandler (bundle: %@)"
+ "### %@ Asked to cancel. Deferring journal update with serialNumber: %lld bundle: %@"
+ "### %@ Cleanup failed to clear ledger for bundleIdentifier: %@ error: %@"
+ "### %@ Cleanup failed to load ledger for bundleIdentifier: %@ skipping delete: %@"
+ "### %@ Deleting %ld extraneous files in ledger directory (%@): %@"
+ "### %@ Deleting ledger and lockfile for bundles: [%@] in ledger directory (%@) not contained in spotlight bundles: %@"
+ "### %@ Deleting lock file for %@ lockFile fd %d"
+ "### %@ Exceeded timeout for AppEntity count Spotlight query for bundle: %@ (%u seconds)"
+ "### %@ Excluding bundle after couting zero AppEntities: %@"
+ "### %@ Failed to clean up extraneous file (%@): %@"
+ "### %@ Failed to reset ledger after completing full set donation: %@"
+ "### %@ Failed to reset ledger after completing journal update: %@"
+ "### %@ Failed to reset ledger after resetting journal update attempts: %@"
+ "### %@ Failed to update ledger after completed full set donation: %@"
+ "### %@ Failed to update ledger after completed journal update: %@"
+ "### %@ Failed to update ledger for full set donation attempt (%u): %@"
+ "### %@ Failed to update ledger for journal update attempt (%u): %@"
+ "### %@ Failed to update ledger to increment version (%llu): %@"
+ "### %@ Failed to update ledger to reset journal update attempts: %@"
+ "### %@ Found no ledger / lock files in directory (%@) that need to be cleaned up"
+ "### %@ Full donation retries exhausted (limit %u). Skipping nightly verification for bundle: %@"
+ "### %@ Full donation retries exhausted (limit %u). Stopping attempts of full set donations for bundle: %@"
+ "### %@ Including bundle despite failed count query: %@"
+ "### %@ Initial full set donation is required per ledger for bundle: %@"
+ "### %@ Ledger reset after completing full set donation"
+ "### %@ Ledger reset after completing journal update"
+ "### %@ Ledger reset after resetting journal update attempts"
+ "### %@ Nightly verification successfully recovered bundle: %@"
+ "### %@ No extraneous files found in ledger directory (%@)"
+ "### %@ Performing full Cascade donation with reason: %@ bundle: %@"
+ "### %@ Received %ld items from Spotlight in the foundItemsHandler from %@"
+ "### %@ Retries exhausted (limit %u). Abandoning journal update with serialNumber: %lld bundle: %@"
+ "### %@ Spotlight AppEntity count query (bundle: %@) completed (result: %ld) after %.3f seconds"
+ "### %@ Spotlight AppEntity count query (bundle: %@) hit error: %@ after %.3f seconds"
+ "### %@ Spotlight AppEntity count query (bundle: %@) was cancelled after %.3f seconds"
+ "### %@ Spotlight query %@ for bundle: %@ after registering %u items with Cascade in %.3f seconds"
+ "### %@ Starting AppEntity count Spotlight query for bundle: %@"
+ "### %@ Starting full set donation Spotlight query for bundle: %@"
+ "### %@ Verifying all applicable bundles: %@"
+ "### %@ Will not attempt full Cascade donation with reason: %@ bundle: %@ because the initial full donation has already been attempted once"
+ "### %@ Will not attempt full Cascade donation with reason: %@ bundle: %@ because the initial full donation is not required"
+ "### %@ fetchBundleIds returned bundles: [%@]"
+ "### %@ fetchBundleIds returned error: %@"
+ "### %@ foundItemsHandler: Query was stopped for bundle: %@"
+ "### EmbeddingCache HIT for %@ string (%{sensitive}@), key size %lu"
+ "### EmbeddingCache MISS for %@ string (%{sensitive}@), key size %lu"
+ "### calculateDirectorySize begin"
+ "### calculateDirectorySize end %llu"
+ "### purgeFilesInOrderUntilThresholdReached number of files: %zu"
+ "%@\n\t%@: %@"
+ "%@\n%@\n%@\n%@"
+ "%@ ### Requesting Cascade donation (%@, version: %llu)"
+ "%@ (%@)"
+ "%@/%@_%@_%@"
+ "%@:\t%@"
+ "%s-%s/%@"
+ "-ledger"
+ "-lockfile"
+ "== Pipeline report =="
+ "=== %@ ===\n"
+ "=== Cleaned up %llu items [of %llu items seen] for query %@"
+ "=== Monitor for requestCSCleanupForUpdater has %llu items added, out of %llu items seen. %@ %@"
+ "=== Monitor for requestCSCleanupWithProtectionClasses has %llu items added, out of %llu items seen. (%@)"
+ "=== Skip cleanup item %@ from bundle %@ b/c found in monitor"
+ "@\"BMFileBackedDictionary\""
+ "@\"SKGQueryStringBuilder\"24@?0@\"NSString\"8@\"NSArray\"16"
+ "@120@0:8I16@20@28@36@44@52@60@68@76@84q92B100@104@?112"
+ "@20@0:8I16"
+ "@24@0:8Q16"
+ "@36@0:8I16@20@?28"
+ "B24@0:8^@16"
+ "B24@?0@\"NSString\"8@\"CSSearchableItem\"16"
+ "B40@0:8@16@24Q32"
+ "B44@0:8@\"CSEventListenerDonation\"16B24@?<v@?Qq@\"NSError\">28@?<B@?>36"
+ "B44@0:8@16B24@?28@?36"
+ "B56@0:8@16@24@32B40^B44B52"
+ "B60@0:8@16@24B32@?36@?44@?52"
+ "B72@0:8@16@24@32Q40^q48Q56@?64"
+ "Build"
+ "CSAppEntityCascadeLedger"
+ "CSProcessingStateUpdater#handleDonation log:%@, handled(%d)"
+ "CannotProcesseFromPriorityUpdater1"
+ "CannotProcesseFromPriorityUpdater2"
+ "CannotProcesseFromPriorityUpdater3"
+ "DOMAIN_PARSEC"
+ "Fail to save progress report of type:%u"
+ "Failure"
+ "FieldMatch(%@,%@)"
+ "Full"
+ "KeyphraseProgressReport"
+ "Ledger file for bundle: \"%@\" was written on build (%@) different from current (%@)"
+ "Options"
+ "ProgressReport"
+ "Request redonation of item %@ from %@"
+ "Reset ledger file for bundle: \"%@\" on current build (%@): %@"
+ "Running Turbo Cleanup Locked for %d"
+ "Running Turbo Cleanup Unlocked for %d"
+ "Running Turbo Post Task Work Done for %d"
+ "Running Turbo Updates Locked for %d"
+ "Running Turbo Updates Unlocked for %d"
+ "S"
+ "SBSearchDisabledDomains"
+ "SKGItemMonitor: Deleting folder %@"
+ "SKGItemMonitor: Error deleting folder %@: %@"
+ "SKGItemMonitor: Error reading directory: %@ %@"
+ "SKGJobReporter"
+ "T@\"NSString\",R,N,V_bundleIdentifier"
+ "T@?,R,N,V_withFieldMatch"
+ "TQ,R,N,V_fullSetDonationAttempts"
+ "TQ,R,N,V_journalUpdateAttempts"
+ "Values must be non-nil and contain at least 1 string"
+ "Version"
+ "[Document Embedding Generation] Embedding generation for primary embeddings timed out for bundleID %@. %llu retries left."
+ "[Document Embedding Generation] Embedding generation for secondary embeddings timed out for bundleID %@. %llu retries left."
+ "[Document Embedding Generation] Start primary embedding generation for item bundleID %@. %llu retries left."
+ "[Document Embedding Generation] Start secondary embedding generation for item bundleID %@. %llu retries left."
+ "_acquireLockFileInDirectory:bundleIdentifier:error:"
+ "_boxedVersion:"
+ "_countAppEntitiesFromBundle:"
+ "_counter"
+ "_dictionary"
+ "_directory"
+ "_fetchAttributes"
+ "_fetchBundleIDsWithCompletionHandler:"
+ "_fullSetDonationAttemptCount"
+ "_fullSetDonationAttempts"
+ "_increment:processor:bundleIdentifier:key:count:"
+ "_journalUpdateAttemptCount"
+ "_journalUpdateAttempts"
+ "_kMDItemExtractedLocationsConfidences"
+ "_kMDItemExtractedLocationsCountry"
+ "_kMDItemExtractedLocationsLatitude"
+ "_kMDItemExtractedLocationsLongitude"
+ "_kMDItemExtractedLocationsParent"
+ "_kMDItemExtractedLocationsValues"
+ "_loadKeyphraseConfig:"
+ "_loadLedgerFileInDirectory:bundleIdentifier:error:"
+ "_lockFileURLWithDirectory:bundleIdentifier:"
+ "_queryCountingPairs"
+ "_queryReportingPairs"
+ "_queryString"
+ "_releaseLock:"
+ "_reportingCounter"
+ "_runCSCleanupForQueryString:trackingAttributes:queryContext:batchUpdatedBlock:cancelBlock:"
+ "_runCSCounterForQueryString:queryContext:filesQuery:counterItemBlock:counterAttrBlock:cancelBlock:"
+ "_runCSPollingQueryString:queryContext:foundItemBlock:"
+ "_values"
+ "_withFieldMatch"
+ "addAttribute:processor:bundleIdentifier:"
+ "addEmbeddingsToProcessedItem:primaryTextInputs:secondaryTextInputs:firstChunkLength:workCost:timeoutRetries:cancelBlock:"
+ "attemptFullSetDonation"
+ "attemptJournalUpdate"
+ "bundleFileQueriesDict"
+ "bundleQueriesDict"
+ "canProcessEventForRecord:bundleIdentifier:"
+ "cleanup"
+ "clear:"
+ "com.apple.CloudDocs.MobileDocumentsFileProvider"
+ "com.apple.CloudDocs.iCloudDriveFileProvider"
+ "com.apple.journal"
+ "com.apple.metadata"
+ "com.apple.spotlightui"
+ "com.apple.tips"
+ "completeFullSetDonationWithVersion:"
+ "completeJournalUpdate"
+ "completedProcessing"
+ "compressedGeoList"
+ "contentsOfDirectoryAtPath:error:"
+ "copyArrayFromRecord:key:"
+ "copyStringArrayFromRecordAndConcatenate:key:"
+ "counter"
+ "currentBuildVersion"
+ "dateWithTimeIntervalSinceReferenceDate:"
+ "decompressedDataUsingAlgorithm:error:"
+ "deleteLedgerFilesInDirectory:notContainedInActiveBundles:"
+ "encodeProcessorReport:"
+ "enumerateCountingAttributesForProcessor:usingBlock:"
+ "enumerateFlagsUsingBlock:"
+ "enumerateReportingAttributesForProcessor:usingBlock:"
+ "extractedAddresses"
+ "extractedLocations"
+ "failed to decompress the response: %@"
+ "failureCount"
+ "fileExistsAtPath:isDirectory:"
+ "fileQuery"
+ "fileURLWithPath:relativeToURL:"
+ "fullSetDonationAttempts"
+ "generateCSReportForQueryFlags:protectionClasses:fetchAttributePairs:additionalQueryString:processedField:succesfullyProcessedField:eligibleFields:dayCompletionStr:genStartTime:bundleIDs:daysToCompleteApproach:onlyFiles:mergeBundleStatistics:withCancelBlock:"
+ "generateCSReportWithFlags:protectionClasses:withCancelBlock:"
+ "generateEmbeddingForTextInputs:extendedContextLength:bundleID:queryID:clientBundleID:timeout:workCost:error:"
+ "getReportsForDateInterval:reportHandler:"
+ "handleDonation:turboEnabled:completionHandler:cancelBlock:"
+ "handleHistoricalReports"
+ "handleHistoricalReports:"
+ "handleProgressReport for protection classes:%@"
+ "handleProgressReport:"
+ "hasAddresses"
+ "hasBreadcrumbs"
+ "hasCompressedGeoList"
+ "hasKeyphrases"
+ "hasLocations"
+ "hasModernPrimaryCategoryId"
+ "hasNamedLocations"
+ "historicalReports"
+ "hit error: %@"
+ "incrementProcessor:bundleIdentifier:"
+ "incrementVersion"
+ "initWithFilename:protectionClass:directory:readOnly:create:initialDictionary:error:"
+ "initWithFlags:"
+ "initWithStartDate:duration:"
+ "isSemanticSearchAvailable"
+ "journalUpdateAttempts"
+ "kMDItemExtractedAddresses"
+ "kMDItemExtractedAddressesLabels"
+ "kMDItemExtractedAddressesSynonyms"
+ "kMDItemExtractedAddressesSynonymsConfidences"
+ "kMDItemExtractedAddressesSynonymsCounts"
+ "kMDItemExtractedLocations"
+ "keyphraseIncludeBundles"
+ "keyphrasesSupportsBundle:domainID:"
+ "loadAllParametersForClient:"
+ "logAttribute:bundleIdentifier:value:"
+ "longValue"
+ "modernPrimaryCategoryId"
+ "needsSKGJournalKeyphrasesRecord:bundleID:protectionClass:recordHasText:shouldMarkComplete:isUpdate:"
+ "needsSKGReindexerKeyphrasesForRecord:bundleID:itemHasText:"
+ "needsSKGReindexingForRecord:bundleID:processorFlags:"
+ "not"
+ "parsecIsEnabled"
+ "processTextContentFromRecord:keyphraser:entities"
+ "progressReport"
+ "purgeOld:"
+ "query"
+ "queryString"
+ "reindex"
+ "releaseLock"
+ "reports"
+ "resetJournalUpdateAttempts"
+ "reverseObjectEnumerator"
+ "saveReport:withType:errorHandler:"
+ "setAttribute:processor:bundleIdentifier:count:"
+ "setCountChangedHandler:"
+ "setCounting:"
+ "sleepForTimeInterval:"
+ "startDate"
+ "stillProcessing"
+ "stringByDeletingLastPathComponent"
+ "substringToIndex:"
+ "territories.territory.cities"
+ "territories.territory.countries"
+ "territories.territory.states"
+ "timeIntervalSinceNow"
+ "unsignedShortValue"
+ "updateArchivePathWithCurrentDateAndDeviceUnlocked:isCleanupPath:"
+ "v20@?0@\"NSString\"8I16"
+ "verbose"
+ "was cancelled"
+ "withFieldMatch"
+ "writeUpdatedObject:forKey:error:"
+ "writeUpdatedObjects:forKeys:error:"
+ "yyyy-MM-dd"
- "### %@ %@ full Cascade donation with reason: %@ ledger: %@"
- "### %@ %@ retry loop after error (%@) for journal update with serialNumber: %lld ledger: %@"
- "### %@ Asked to cancel. Deferring journal update with serialNumber: %lld ledger: %@"
- "### %@ Deleting files: [%@] in ledger directory (%@) not contained in spotlight bundles: %@"
- "### %@ Exceeded timeout for full set donation Spotlight query (%u seconds)"
- "### %@ Failed to delete url (%@) in ledger directory (%@) error: %@"
- "### %@ Failed to record full donation attempt for bundle: %@ error %@"
- "### %@ Failed to record incremental donation attempt for bundle: %@ error %@"
- "### %@ Full donation retries exhausted (limit %u). Skipping nightly verification for ledger: %@"
- "### %@ Full donation retries exhausted (limit %u). Stopping attempts of full set donations for ledger: %@"
- "### %@ Incremental donation retries exhausted (limit %u). Abandoning journal update with serialNumber: %lld ledger: %@"
- "### %@ Ledger directory (%@) contains no extraneous files"
- "### %@ Ledger reset after abandoning donation: %@"
- "### %@ Ledger reset after completing donation: %@"
- "### %@ Ledger reset failed: %@ error: %@"
- "### %@ Received %ld items from Spotlight in the foundItemsHandler"
- "### %@ Received %ld items from Spotlight in the foundItemsHandler from %@."
- "### %@ Resetting ledger after failing to record abandoned donation: %@ error: %@"
- "### %@ Resetting ledger after failing to record completed donation: %@ error: %@"
- "### %@ Spotlight query completed with error: %@"
- "### %@ Spotlight query completed."
- "### %@ Spotlight query was cancelled."
- "### %@ Starting full set donation Spotlight query"
- "### %@ Verifying all allowed bundles: %@"
- "### EmbeddingCache Hit for string (%@), key size %lu"
- "### appentity checking 0x%x"
- "%@\n%@\n%@\n%@\n%@"
- "%@ Requesting Cascade donation (%@, version: %llu)"
- "%@-lockfile"
- "%@/%@.%@.%@"
- "%@: %d"
- "(kMDItemKeyphraseVersion=*&&kMDItemKeyphraseVersion=%ld)"
- "/tmp/%@.%@.%@"
- "@112@0:8I16@20@28@36@44@52@60@68@76@84q92B100@?104"
- "B40@0:8@\"CSEventListenerDonation\"16@?<v@?Qq@\"NSError\">24@?<B@?>32"
- "B64@0:8@16@24@32Q40^q48@?56"
- "CSProcessingStateUpdater#handleDonation log:%@"
- "CSProtectedSpotlightCascadeLedger"
- "CannotProcesseFromPriorityUpdater"
- "MMMM d, Y"
- "Running Turbo Cleanup 1"
- "Running Turbo Cleanup 2"
- "Running Turbo Post Task Work Done"
- "Running Turbo Updates 1"
- "Running Turbo Updates 2"
- "_recordAbandonedDonationType:orResetLedger:"
- "_recordCompletedDonationType:withVersion:orResetLedger:"
- "_removeLedgersNotContainedInSpotlightBundles:"
- "_runCSCleanupForQueryString:requiredAttributes:queryContext:batchUpdatedBlock:cancelBlock:"
- "_runCSCounterForQueryString:queryContext:counterItemBlock:counterAttrBlock:cancelBlock:"
- "abandonDonationType:error:"
- "addEmbeddingsToProcessedItem:primaryTextInputs:secondaryTextInputs:firstChunkLength:workCost:cancelBlock:"
- "attemptDonationType:error:"
- "canProcessEventForRecord:"
- "completeDonationType:version:error:"
- "copyStringArrayFromRecordAndConcatnate:key:"
- "countAttemptsOfDonationType:"
- "generateCSKeyphraseReportForProtectionClasses:withCancelBlock:"
- "generateCSKeyphraseReportWithCancelBlock:"
- "generateCSReportForQueryFlags:protectionClasses:fetchAttributePairs:additionalQueryString:processedField:succesfullyProcessedField:eligibleFields:dayCompletionStr:genStartTime:bundleIDs:daysToCompleteApproach:includeFiles:withCancelBlock:"
- "generateEmbeddingForTextInputs:extendedContextLength:bundleID:queryID:timeout:workCost:error:"
- "handleDonation:completionHandler:cancelBlock:"
- "itemsWithKeyphrases"
- "keyphraseGenerationProgress"
- "keyphraseReport"
- "keyphrasesGenCompleteDay"
- "releaseProtectedLedger"
- "v36@0:8C16Q20@28"

```
