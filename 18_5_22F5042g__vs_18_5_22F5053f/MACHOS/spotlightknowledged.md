## spotlightknowledged

> `/System/Library/Frameworks/CoreSpotlight.framework/spotlightknowledged`

```diff

-2333.41.0.1.0
-  __TEXT.__text: 0xc71f8
+2333.47.0.0.0
+  __TEXT.__text: 0xc7bc8
   __TEXT.__auth_stubs: 0x1d90
-  __TEXT.__objc_stubs: 0xd580
-  __TEXT.__objc_methlist: 0x6580
-  __TEXT.__const: 0x6d2
-  __TEXT.__gcc_except_tab: 0x5284
-  __TEXT.__cstring: 0x8871
-  __TEXT.__oslogstring: 0x818d
+  __TEXT.__objc_stubs: 0xd5c0
+  __TEXT.__objc_methlist: 0x6588
+  __TEXT.__const: 0x6f2
+  __TEXT.__gcc_except_tab: 0x5324
+  __TEXT.__cstring: 0x861a
+  __TEXT.__oslogstring: 0x844c
   __TEXT.__objc_classname: 0xa4e
-  __TEXT.__objc_methname: 0xf9ae
-  __TEXT.__objc_methtype: 0x1727
+  __TEXT.__objc_methname: 0xf9fb
+  __TEXT.__objc_methtype: 0x1728
   __TEXT.__dlopen_cstrs: 0x5e
   __TEXT.__unwind_info: 0x2c30
   __DATA_CONST.__auth_got: 0xee0
-  __DATA_CONST.__got: 0x840
+  __DATA_CONST.__got: 0x848
   __DATA_CONST.__auth_ptr: 0x18
-  __DATA_CONST.__const: 0x4ca8
-  __DATA_CONST.__cfstring: 0xaaa0
+  __DATA_CONST.__const: 0x4d20
+  __DATA_CONST.__cfstring: 0xaa00
   __DATA_CONST.__objc_classlist: 0x458
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x20

   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x2c0
   __DATA_CONST.__objc_intobj: 0x750
-  __DATA_CONST.__objc_arraydata: 0xb00
-  __DATA_CONST.__objc_arrayobj: 0x6c0
+  __DATA_CONST.__objc_arraydata: 0xb28
+  __DATA_CONST.__objc_arrayobj: 0x6d8
   __DATA_CONST.__objc_dictobj: 0x258
   __DATA_CONST.__objc_doubleobj: 0x20
-  __DATA.__objc_const: 0xaf98
-  __DATA.__objc_selrefs: 0x3d40
-  __DATA.__objc_ivar: 0x744
+  __DATA.__objc_const: 0xafc8
+  __DATA.__objc_selrefs: 0x3d50
+  __DATA.__objc_ivar: 0x748
   __DATA.__objc_data: 0x2b70
   __DATA.__data: 0x550
   __DATA.__bss: 0xe20

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 3600
-  Symbols:   738
-  CStrings:  5350
+  Functions: 3603
+  Symbols:   739
+  CStrings:  5360
 
Symbols:
+ _SGErrorDomain
CStrings:
+ "### SGSuggestionsService event extraction refused with error: %@"
+ "%{public}@"
+ "=== Skip cleanup of item with bundle %@ oid 0x%x (%@) since item is present in item monitor"
+ "=== Skip cleanup of item with bundle com.apple.%@ oid 0x%x (%@) since item is present in item monitor"
+ "=== Will cleanup item with bundle %@ oid 0x%x (%@)"
+ "=== Will cleanup item with bundle com.apple.%@ oid 0x%x (%@)"
+ "BundleReport"
+ "HandleDonation"
+ "ProcessJournals"
+ "Request redonation of item with bundle %@ oid 0x%x (%@)"
+ "Request redonation of item with bundle com.apple.%@ oid 0x%x (%@)"
+ "TB,R,N,V_logFullItemIDs"
+ "TotalReport"
+ "_logFullItemIDs"
+ "_processJournalsWithProcessedJournalsCount:completionHandler:"
+ "cancelled"
+ "didCancel=%{BOOL}d bundle=%@ indexType=%d totalItemsCount=%u donationsWithNeedsEmbedding=%lu processedItemsCount=%lu embeddingsCount=%lu cacheHitRate=%u cacheItemCount=%u"
+ "empty-queue"
+ "eof-or-error"
+ "last-journal"
+ "logFullItemIDs"
+ "queryForEligibleItemsWithTaskQueries:excludeBundles:"
+ "queryForPipelineUpdatesWithTaskQueries:excludeBundles:throttleHorizonDate:"
+ "skipping item with bundle %@ oid 0x%x (%@) since item is present in item monitor"
+ "skipping item with bundle com.apple.%@ oid 0x%x (%@) since item is present in item monitor"
+ "stopReason=%{public}@ indexType=%d taskName=%@ processedJournalsCount=%lu journalQueueCount=%lu"
+ "substringFromIndex:"
+ "v24@?0Q8@\"NSString\"16"
+ "v32@0:8Q16@?24"
- "### no journals available - %@, queue size = %lu"
- "((_kMDItemUpdaterVersion=*&&_kMDItemUpdaterVersion!=%ld)||(_kMDItemUpdaterLastRequested=*&&_kMDItemUpdaterLastRequested<%ld)&&(_kMDItemUpdaterRequestedCount=*&&_kMDItemUpdaterRequestedCount<10))"
- "(_kMDItemEmbeddingsError=*&&_kMDItemEmbeddingsError<4)"
- "(_kMDItemKeyphrasesError=*&&_kMDItemKeyphrasesError<4)"
- "(_kMDItemMediaEmbeddingVersion=*&&_kMDItemMediaEmbeddingVersion!=%ld)"
- "(_kMDItemUpdaterVersion!=*&&(%@))"
- "(kMDItemDocumentUnderstandingVersion=*&&kMDItemDocumentUnderstandingVersion!=%ld)"
- "(kMDItemEmbeddingVersion=*&&kMDItemEmbeddingVersion!=%ld)"
- "(kMDItemKeyphraseVersion=*&&kMDItemKeyphraseVersion!=%ld)"
- "(kMDItemSuggestedEventsVersion=*&&kMDItemSuggestedEventsVersion!=%ld)"
- "(true)"
- "=== Skip cleanup item %@ from bundle %@ b/c found in monitor"
- "=== Will cleanup item %@ from bundle %@"
- "@32@0:8@16q24"
- "CSEmbeddingsUpdaterHandleDonation"
- "Request redonation of item %@ from %@"
- "_incrementFieldInDictionary:forKey:creatingIfNeeded:"
- "queryForPipelineUpdatesWithExcludeBundles:taskQueries:throttleHorizonDate:"
- "queryForPipelineUpdatesWithTaskQueries:throttleHorizonDate:"
- "skipping item with bundle %@ oid %@ since item is present in item monitor"

```
