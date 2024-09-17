## spotlightknowledged

> `/System/Library/Frameworks/CoreSpotlight.framework/spotlightknowledged`

```diff

-2314.4.1.0.1
-  __TEXT.__text: 0x80ca8
-  __TEXT.__auth_stubs: 0x1c20
-  __TEXT.__objc_stubs: 0x8560
-  __TEXT.__objc_methlist: 0x4480
-  __TEXT.__const: 0x6a8
-  __TEXT.__cstring: 0x4db8
-  __TEXT.__oslogstring: 0x2aef
-  __TEXT.__gcc_except_tab: 0x3cb8
-  __TEXT.__objc_classname: 0x712
-  __TEXT.__objc_methname: 0x9bae
-  __TEXT.__objc_methtype: 0xf06
+2314.6.0.0.0
+  __TEXT.__text: 0x813d8
+  __TEXT.__auth_stubs: 0x1c60
+  __TEXT.__objc_stubs: 0x8620
+  __TEXT.__objc_methlist: 0x448c
+  __TEXT.__const: 0x6d0
+  __TEXT.__cstring: 0x50a3
+  __TEXT.__oslogstring: 0x2e58
+  __TEXT.__gcc_except_tab: 0x3d34
+  __TEXT.__objc_classname: 0x716
+  __TEXT.__objc_methname: 0x9c88
+  __TEXT.__objc_methtype: 0xf5e
   __TEXT.__dlopen_cstrs: 0x5e
-  __TEXT.__unwind_info: 0x2160
-  __DATA_CONST.__auth_got: 0xe28
-  __DATA_CONST.__got: 0x5d0
+  __TEXT.__unwind_info: 0x20e0
+  __DATA_CONST.__auth_got: 0xe48
+  __DATA_CONST.__got: 0x5d8
   __DATA_CONST.__auth_ptr: 0x28
-  __DATA_CONST.__const: 0x3538
-  __DATA_CONST.__cfstring: 0x6c00
+  __DATA_CONST.__const: 0x32f0
+  __DATA_CONST.__cfstring: 0x6f00
   __DATA_CONST.__objc_classlist: 0x338
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x1f8
-  __DATA_CONST.__objc_arraydata: 0x5e0
-  __DATA_CONST.__objc_arrayobj: 0x3a8
-  __DATA_CONST.__objc_dictobj: 0xc8
+  __DATA_CONST.__objc_arraydata: 0x648
+  __DATA_CONST.__objc_arrayobj: 0x3d8
+  __DATA_CONST.__objc_dictobj: 0xf0
   __DATA_CONST.__objc_doubleobj: 0x20
-  __DATA_CONST.__objc_intobj: 0x330
-  __DATA.__objc_const: 0x7d40
-  __DATA.__objc_selrefs: 0x27c0
-  __DATA.__objc_ivar: 0x4e4
+  __DATA_CONST.__objc_intobj: 0x348
+  __DATA.__objc_const: 0x7d00
+  __DATA.__objc_selrefs: 0x27e0
+  __DATA.__objc_ivar: 0x4e0
   __DATA.__objc_data: 0x2030
   __DATA.__data: 0x560
-  __DATA.__bss: 0xae8
+  __DATA.__bss: 0xb28
   __DATA.__common: 0x30010
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2492
-  Symbols:   635
-  CStrings:  3407
+  Functions: 2466
+  Symbols:   640
+  CStrings:  3452
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _SecTaskCreateFromSelf
+ ___exp10
+ _log10
+ _OBJC_CLASS_$_BGSystemTaskCheckpoints
CStrings:
+ "beginInferenceTaskWithName:deviceUnlocked:knowledgedQueue:completeBlock:cancelBlock:deferBlock:"
+ "handleDonation:completionHandler:cancelBlock:"
+ "beginIndexingTaskWithName:deviceUnlocked:knowledgedQueue:completeBlock:cancelBlock:deferBlock:"
+ "\n%!s(MISSING) at time %!s(MISSING) for item - bundle: %!s(MISSING) identifier: %!s(MISSING) oid: 0x%!l(MISSING)lx info:%!s(MISSING)"
+ "SecTaskCopyValueForEntitlement failed for \"%!@(MISSING)\", error:%!@(MISSING)"
+ "### Not processing next journal entry for %!s(MISSING) because task is cancelled"
+ "Found \"%!@(MISSING)\" entitlement, value:%!@(MISSING)"
+ "addPurgeJournalsEventForItemWithPath:size:"
+ "YES"
+ "verbose"
+ "### Not processed journal entry %!@(MISSING) at offset = %!l(MISSING)lu for %!@(MISSING) because of err = %!@(MISSING) or task cancelled"
+ "totalItems"
+ "((%!@(MISSING)) && kMDItemAttributeChangeDate<$time.this_month)"
+ "### timeout %!@(MISSING) for %!@(MISSING)"
+ "needsEmbeddingsForRecord:bundleID:"
+ "state"
+ "[EXIT] updateChunks"
+ "[EXIT] generateEmbeddingForTextInputs"
+ "addVerboseEventForItemWithString:identifier:str:"
+ "B40@0:8@\"CSEventListenerDonation\"16@?<v@?Qq@\"NSError\">24@?<B@?>32"
+ "PurgeJournals"
+ "canGenerateEmbeddingsForRecord:bundleID:"
+ "### cleanup journal [cookie:%!s(MISSING) jno:%!l(MISSING)lu] due to cookie mismatch with the event message recieved [%!@(MISSING)]"
+ "_peopleScores"
+ "[EXIT] Invalid item"
+ "\x01\x11"
+ "### skip offset %!l(MISSING)lu because JournalProcessor have retried enough to process its journal entry"
+ "_runCSCleanupForQueryString:queryContext:flags:batchProcessedBlock:batchUpdatedBlock:cancelBlock:"
+ "handleActivityJournalVerboseSet:"
+ "B40@0:8@16@?24@?32"
+ "v92@0:8@16q24@32B40@44@?52@?60@?68@?76@?84"
+ "starting batch cleanup"
+ "### Processed journal entry %!@(MISSING) at offset %!l(MISSING)lu for %!@(MISSING)"
+ "requestCSCleanupWithBatchProcessedBlock:batchUpdatedBlock:cancelBlock:"
+ "Failed to report task progress %!@(MISSING): %!@(MISSING)"
+ "runWithJobContext:queue:group:progressBlock:checkpointBlock:completeBlock:cancelBlock:deferBlock:"
+ "v40@?0Q8@\"NSString\"16Q24Q32"
+ "[EXIT] semanticSearchEnabled"
+ "_runKnowledgeUpdatingWithJobContext:group:queue:deferBlock:progressBlock:checkpointBlock:completeBlock:cancelBlock:"
+ "### priority batches completed, deferring failed with error: %!@(MISSING); marking complete %!@(MISSING)"
+ "modelVersion"
+ "beginReportTaskWithName:deviceUnlocked:knowledgedQueue:progressBlock:checkpointBlock:completeBlock:cancelBlock:deferBlock:"
+ "[EXIT] canProcessEvent: %!d(MISSING), canProcessRecord: %!d(MISSING)"
+ "setWithObjects:"
+ "handleActivityJournalVerbose"
+ "beginTaskWithName:knowledgeEvent:logMessage:deviceUnlocked:knowledgedQueue:progressBlock:checkpointBlock:completeBlock:cancelBlock:deferBlock:"
+ "beginJournalingTaskWithName:deviceUnlocked:knowledgedQueue:completeBlock:cancelBlock:deferBlock:"
+ "completeness"
+ "itemsWithEmebdding"
+ "beginUpdatesTaskWithName:deviceUnlocked:knowledgedQueue:completeBlock:cancelBlock:deferBlock:"
+ "com.apple.private.iokit.powersource-control"
+ "peopleScoreWithCancelBlock:"
+ "v80@0:8@16@24@32@?40@?48@?56@?64@?72"
+ "_errorProcessingPeople"
+ "[EXIT] serialNumber:%!l(MISSING)lu < latestSerialNumber:%!l(MISSING)lu"
+ "reportTaskWorkloadProgress:completed:category:subCategory:error:"
+ "processReportWithJobContext:group:progressBlock:checkpointBlock:cancelBlock:"
+ "setVerbose:"
+ "TB,N,V_verbose"
+ "### background batches completed, deferring failed with error: %!@(MISSING); marking complete %!@(MISSING)"
+ "_verbose"
+ "### Will retry the offset %!l(MISSING)lu, processing count so far = %!l(MISSING)lu, startOffset = %!l(MISSING)lu"
+ "@\"NSLock\""
+ "updaterStatusLock"
+ "reportFeatureCheckpoint:forFeature:error:"
+ "_kMDItemTextContentLength"
+ "Couldn't find \"%!@(MISSING)\" entitlement"
+ "end batch cleanup"
+ "errorProcessingPeople"
+ "[EXIT] shouldHandleJournalItem"
+ "findAllContactInfoForNode:info:reference:foundUser:"
+ "v76@0:8@16B24@28@?36@?44@?52@?60@?68"
+ "\n%!s(MISSING) at time(s) %!s(MISSING) - path:%!s(MISSING) size: %!l(MISSING)lu"
+ "_kMDItemNeedsPriority=1"
+ "semantic-index"
+ "[EXIT] extractContentFromRecord"
+ "B16@?0@\"CSEventDonationJournalItem\"8"
+ "generatePeopleUsingBlock:"
+ "4 `"
+ "[EXIT] invalid Index"
+ "v16@?0r^{skg_playback_info=Ii(?={?=Id*}{?=dqq}{?=*}{?=**q}{?=d}{?=I}{?=d**q*}{?=dQ*})}8"
+ "peopleUpdateInfo:attributeKey:attribute:forNode:person:score:rank:bestCount:"
+ "_toc_retry_counter"
+ "activityJournalVerbose"
+ "### cancelling %!s(MISSING) due to expiration request while processing type='%!s(MISSING)' sn:'%!l(MISSING)lu'"
+ "q\xb3"
+ "systemOidLock"
+ "_kMDItemNeedsKeyphrases=1"
+ "needsKeyphrasesForRecord:bundleID:"
+ "setErrorProcessingPeople:"
+ "[EXIT] processLanguageOfTextContentFromRecord"
+ "peopleUpdateNetwork:sourceNodeId:nodes:"
+ "integerForKey:"
+ "peopleAnalyzeWithCancelBlock:"
+ "### background batches completed; marking deferred %!@(MISSING)"
+ "### priority batches completed; marking deferred %!@(MISSING)"
+ "VerboseEvent"
+ "TB,N,V_errorProcessingPeople"
+ "eligibleItems"
+ "setInteger:forKey:"
+ "_kMDItemNeedsEmbeddings=1"
- "v72@0:8@16@24@32@40@?48@?56@?64"
- "### background batches completed; marking complete %!@(MISSING)"
- "### priority batches completed; marking complete %!@(MISSING)"
- "arrayByAddingObjectsFromArray:"
- "TB,N,V_shouldProcessKeyphrases"
- "couldNotProcessEmbeddings"
- "_shouldProcessEmbeddings"
- "locked_peopleAnalyzeWithCancelBlock:"
- "_kMDItemTextContentEmbedCheckLen"
- "beginIndexingTaskWithName:deviceUnlocked:knowledgedQueue:deferBlock:completeBlock:cancelBlock:"
- "locked_peopleScoreWithCancelBlock:"
- "v16@?0@\"CSEventDonationJournalItem\"8"
- "locked_peopleUpdateInfo:attributeKey:attribute:forNode:person:score:rank:bestCount:"
- "locked_peopleUpdateNetwork:sourceNodeId:nodes:"
- "runWithJobContext:queue:group:delegate:deferBlock:completeBlock:cancelBlock:"
- "unsignedLongValue"
- "beginUpdatesTaskWithName:deviceUnlocked:knowledgedQueue:deferBlock:completeBlock:cancelBlock:"
- "v16@?0r^{skg_playback_info=Ii(?={?=Id*}{?=dqq}{?=*}{?=**q}{?=d}{?=I})}8"
- "shouldProcessEmbeddings"
- "beginInferenceTaskWithName:deviceUnlocked:knowledgedQueue:deferBlock:completeBlock:cancelBlock:"
- "setCouldNotProcessKeyphrases:"
- "beginTaskWithName:knowledgeEvent:logMessage:deviceUnlocked:knowledgedQueue:deferBlock:completeBlock:cancelBlock:"
- "locked_findAllContactInfoForNode:info:reference:foundUser:"
- "setCouldNotProcessEmbeddings:"
- "couldNotProcessKeyphrases"
- "beginReportTaskWithName:deviceUnlocked:knowledgedQueue:deferBlock:completeBlock:cancelBlock:"
- "setShouldProcessEmbeddings:"
- "q\xa3"
- "turboState"
- "v76@0:8@16q24@32B40@44@?52@?60@?68"
- "com.apple.spotlight.SpotlightKnowledge.Graph"
- "_runKnowledgeUpdatingWithJobContext:group:queue:delegate:deferBlock:completeBlock:cancelBlock:"
- "canGenerateEmbeddingsForRecord:bundleIdentifier:"
- "_lockedPeopleScores"
- "shouldProcessKeyphrases"
- "\x03\x11"
- "embedding generation progress for bundle: %!@(MISSING) %!@(MISSING)"
- "TB,N,V_couldNotProcessKeyphrases"
- "_graphQueue"
- "locked_enumeratePeopleUsingBlock:"
- "handleDonation:completionHandler:"
- "daysSinceEnabled"
- "_shouldProcessKeyphrases"
- "beginJournalingTaskWithName:deviceUnlocked:knowledgedQueue:deferBlock:completeBlock:cancelBlock:"
- "B32@0:8@\"CSEventListenerDonation\"16@?<v@?Qq@\"NSError\">24"
- "### timeout %!@(MISSING) for %!@(MISSING), continuing to wait"
- "_couldNotProcessEmbeddings"
- "com.apple.SpotlightKnowledge.SKGGraph.graph"
- "setShouldProcessKeyphrases:"
- "graphQueue"
- "needsKeyphrasesForRecord:"
- "_couldNotProcessKeyphrases"
- "needsEmbeddingsForRecord:"
- "TB,N,V_couldNotProcessEmbeddings"
- "TB,N,V_shouldProcessEmbeddings"
- "processReportWithJobContext:group:cancelBlock:"
- "_lockedGraph"

```
