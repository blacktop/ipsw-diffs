## CoreSpotlight

> `/System/Library/Frameworks/CoreSpotlight.framework/Versions/A/CoreSpotlight`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__weak_got`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_floatobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-2451.1.401.0.0
-  __TEXT.__text: 0x1938e0
-  __TEXT.__objc_methlist: 0x14490
-  __TEXT.__const: 0xf00
-  __TEXT.__cstring: 0x2bf5f
-  __TEXT.__oslogstring: 0xb39c
-  __TEXT.__gcc_except_tab: 0x93e4
+2454.100.0.0.0
+  __TEXT.__text: 0x194574
+  __TEXT.__objc_methlist: 0x14518
+  __TEXT.__const: 0xf50
+  __TEXT.__cstring: 0x2c1bf
+  __TEXT.__oslogstring: 0xb833
+  __TEXT.__gcc_except_tab: 0x9444
   __TEXT.__ustring: 0x2040
   __TEXT.__dlopen_cstrs: 0x40f
-  __TEXT.__swift5_typeref: 0x2b4
-  __TEXT.__swift5_reflstr: 0x89
+  __TEXT.__constg_swiftt: 0x1bc
+  __TEXT.__swift5_typeref: 0x2ba
+  __TEXT.__swift5_reflstr: 0x8e
+  __TEXT.__swift5_fieldmd: 0x15c
+  __TEXT.__swift5_types: 0x30
   __TEXT.__swift5_assocty: 0x150
-  __TEXT.__constg_swiftt: 0x1a0
-  __TEXT.__swift5_fieldmd: 0x140
   __TEXT.__swift5_proto: 0x60
-  __TEXT.__swift5_types: 0x2c
   __TEXT.__swift5_capture: 0x10c
   __TEXT.__swift_as_entry: 0x24
   __TEXT.__swift_as_ret: 0x24
   __TEXT.__swift_as_cont: 0xc
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x5f68
+  __TEXT.__unwind_info: 0x5fa0
   __TEXT.__eh_frame: 0x1e8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x3ec0
+  __DATA_CONST.__const: 0x3ed0
   __DATA_CONST.__objc_classlist: 0xaa0
   __DATA_CONST.__objc_catlist: 0x60
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa4b8
+  __DATA_CONST.__objc_selrefs: 0xa4e0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x718
-  __DATA_CONST.__objc_arraydata: 0x110c8
-  __DATA_CONST.__got: 0xea8
-  __AUTH_CONST.__const: 0x5240
-  __AUTH_CONST.__cfstring: 0x2daa0
-  __AUTH_CONST.__objc_const: 0x1f9e8
+  __DATA_CONST.__objc_arraydata: 0x110d0
+  __DATA_CONST.__got: 0xea0
+  __AUTH_CONST.__const: 0x5310
+  __AUTH_CONST.__cfstring: 0x2dc00
+  __AUTH_CONST.__objc_const: 0x1fa98
   __AUTH_CONST.__weak_auth_got: 0x10
-  __AUTH_CONST.__objc_arrayobj: 0x3a68
+  __AUTH_CONST.__objc_arrayobj: 0x3a80
   __AUTH_CONST.__objc_dictobj: 0xaf78
-  __AUTH_CONST.__objc_intobj: 0xdf8
-  __AUTH_CONST.__objc_doubleobj: 0x170
+  __AUTH_CONST.__objc_intobj: 0xe58
+  __AUTH_CONST.__objc_doubleobj: 0x180
   __AUTH_CONST.__objc_floatobj: 0x10
-  __AUTH_CONST.__auth_got: 0x1240
+  __AUTH_CONST.__auth_got: 0x1230
   __AUTH.__objc_data: 0x5af0
   __AUTH.__data: 0x3a0
-  __DATA.__objc_ivar: 0x1410
+  __DATA.__objc_ivar: 0x141c
   __DATA.__data: 0x1be0
-  __DATA.__bss: 0x1900
+  __DATA.__bss: 0x1930
   __DATA_DIRTY.__objc_data: 0xf50
   __DATA_DIRTY.__data: 0x20
   __DATA_DIRTY.__bss: 0xa7e0

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 8956
-  Symbols:   17911
-  CStrings:  8016
+  Functions: 8993
+  Symbols:   17949
+  CStrings:  8034
 
Symbols:
+ +[CSInlineDonation fetchLastClientState:forName:overrideBundleID:protectionClass:error:]
+ +[_CSAgenticQuery _prepareEmbeddingParserOnce]
+ +[_CSAgenticQuery _prepareSearchQueryOnce]
+ +[_CSAgenticQuery prepare]
+ -[CSInlineDonation _shouldEnforceExpectedClientState]
+ -[CSInlineDonation _verifyExpectedClientStateWithDonation:error:]
+ -[CSSearchQuery _shouldEmitSignpostTelemetry]
+ -[CSSearchQuery setSignpostTelemetryEnabled:]
+ -[CSSearchQuery signpostTelemetryEnabled]
+ -[CSSearchQueryContext longQueryHandlingModeOverride]
+ -[CSSearchQueryContext longQueryTimeoutOverride]
+ -[CSSearchQueryContext setLongQueryHandlingModeOverride:]
+ -[CSSearchQueryContext setLongQueryTimeoutOverride:]
+ -[CSUserQueryParser _CSUserQueryPreheatWithOptionsDictSync:]
+ -[_CSAnnQueryPredicate annClauseForAttribute:embeddingIdx:vectorDistanceSubIndex:]
+ -[_CSAnnQueryPredicate compileToMDQueryStringWithContext:]
+ -[_CSQueryOperation compileToMDQueryStringWithContext:]
+ GCC_except_table248
+ GCC_except_table249
+ GCC_except_table253
+ GCC_except_table259
+ GCC_except_table260
+ GCC_except_table269
+ GCC_except_table275
+ GCC_except_table285
+ GCC_except_table292
+ GCC_except_table303
+ GCC_except_table307
+ GCC_except_table313
+ GCC_except_table318
+ GCC_except_table322
+ GCC_except_table331
+ GCC_except_table358
+ GCC_except_table359
+ GCC_except_table366
+ GCC_except_table367
+ GCC_except_table381
+ GCC_except_table391
+ GCC_except_table392
+ GCC_except_table398
+ GCC_except_table400
+ GCC_except_table405
+ GCC_except_table408
+ GCC_except_table415
+ GCC_except_table428
+ GCC_except_table429
+ GCC_except_table432
+ GCC_except_table438
+ GCC_except_table442
+ GCC_except_table448
+ GCC_except_table449
+ GCC_except_table456
+ GCC_except_table458
+ GCC_except_table551
+ GCC_except_table552
+ GCC_except_table553
+ GCC_except_table554
+ GCC_except_table562
+ GCC_except_table599
+ OBJC_IVAR_$_CSSearchQuery._signpostTelemetryEnabled
+ OBJC_IVAR_$_CSSearchQueryContext._longQueryHandlingModeOverride
+ OBJC_IVAR_$_CSSearchQueryContext._longQueryTimeoutOverride
+ __56-[CSUserQueryParser _CSUserQueryPreheatWithOptionsDict:]_block_invoke
+ __CSQueryNodeEmbeddingsSinkKey
+ __CSQueryNodeParseOptionsKey
+ __OBJC_$_CLASS_METHODS__CSAgenticQuery
+ __ZZ47-[_CSQueryStage executeWithContext:completion:]E23sAgenticPipelineQueryID
+ ___42+[_CSAgenticQuery _prepareSearchQueryOnce]_block_invoke
+ ___46+[_CSAgenticQuery _prepareEmbeddingParserOnce]_block_invoke
+ ___60-[CSUserQueryParser _CSUserQueryPreheatWithOptionsDictSync:]_block_invoke
+ ___block_descriptor_65_e8_32s40s48s56w_e5_v8?0l
+ ___logForCSSignpostLongRunningQuery_block_invoke
+ ___logForCSSignpostQueryTelemetry_block_invoke
+ __clientStateFromString
+ __inlineDonationSourceIdentifier
+ __isNoSuchSetError
+ __setFetchClientStateError
+ _escapeStringForMDQuery
+ _getCCSetDescriptorClass
+ _isNoSuchSetError
+ _logForCSSignpostLongRunningQuery
+ _logForCSSignpostQueryTelemetry
+ _objc_msgSend$_prepareEmbeddingParserOnce
+ _objc_msgSend$_prepareSearchQueryOnce
+ _objc_msgSend$_shouldEmitSignpostTelemetry
+ _objc_msgSend$_shouldEnforceExpectedClientState
+ _objc_msgSend$_verifyExpectedClientStateWithDonation:error:
+ _objc_msgSend$annClauseForAttribute:embeddingIdx:vectorDistanceSubIndex:
+ _objc_msgSend$longQueryHandlingModeOverride
+ _objc_msgSend$longQueryTimeoutOverride
+ _objc_msgSend$setLongQueryHandlingModeOverride:
+ _objc_msgSend$setLongQueryTimeoutOverride:
+ _objc_msgSend$setSignpostTelemetryEnabled:
+ _objc_msgSend$signpostTelemetryEnabled
+ _os_variant_has_internal_diagnostics
+ _prepareEmbeddingParserOnce.onceToken
+ _prepareSearchQueryOnce.onceToken
+ _symbolic _____ 13CoreSpotlight14SearchableItemV
+ _type_layout_string 13CoreSpotlight14SearchableItemV
+ logForCSSignpostLongRunningQuery
+ logForCSSignpostLongRunningQuery.onceToken
+ logForCSSignpostLongRunningQuery.sLongRunningQueryLog
+ logForCSSignpostQueryTelemetry
+ logForCSSignpostQueryTelemetry.onceToken
+ logForCSSignpostQueryTelemetry.sQueryTelemetryLog
- -[_CSAnnQueryPredicate annClauseForAttribute:version:vector:]
- -[_CSAnnQueryPredicate currentEmbeddingVersion]
- -[_CSAnnQueryPredicate generateEmbeddingForText:]
- -[_CSAnnQueryPredicate hexStringFromEmbeddingData:]
- -[_CSAuthorPredicate escapeString:]
- -[_CSKeywordsPredicate escapeString:]
- GCC_except_table251
- GCC_except_table255
- GCC_except_table256
- GCC_except_table262
- GCC_except_table279
- GCC_except_table287
- GCC_except_table294
- GCC_except_table300
- GCC_except_table305
- GCC_except_table306
- GCC_except_table309
- GCC_except_table323
- GCC_except_table324
- GCC_except_table327
- GCC_except_table335
- GCC_except_table360
- GCC_except_table361
- GCC_except_table364
- GCC_except_table365
- GCC_except_table368
- GCC_except_table369
- GCC_except_table376
- GCC_except_table393
- GCC_except_table394
- GCC_except_table402
- GCC_except_table403
- GCC_except_table409
- GCC_except_table410
- GCC_except_table423
- GCC_except_table424
- GCC_except_table427
- GCC_except_table433
- GCC_except_table437
- GCC_except_table443
- GCC_except_table444
- GCC_except_table451
- GCC_except_table453
- GCC_except_table544
- GCC_except_table545
- GCC_except_table546
- GCC_except_table547
- GCC_except_table555
- GCC_except_table592
- _OBJC_CLASS_$_SPTextInput
- _SPEmbeddingProviderGetShared
- _SPEmbeddingProviderGetVersion
- ___block_descriptor_48_e8_32bs40w_e33_v16?0"NSObject<OS_xpc_object>"8l
- ___block_descriptor_73_e8_32s40s48s56bs64w_e5_v8?0l
- ___copy_helper_block_e8_32b40w
- ___copy_helper_block_e8_32s40s48s56b64w
- _csr_check
- _objc_msgSend$annClauseForAttribute:version:vector:
- _objc_msgSend$currentEmbeddingVersion
- _objc_msgSend$elementCount
- _objc_msgSend$elementType
- _objc_msgSend$embeddingData
- _objc_msgSend$generateEmbeddingForText:
- _objc_msgSend$generateEmbeddingForTextInputs:extendedContextLength:queryID:timeout:error:
- _objc_msgSend$hexStringFromEmbeddingData:
- _objc_msgSend$initWithText:
- _objc_msgSend$stringWithCapacity:
CStrings:
+ "%@ || aNN.data(%@, 0, %ld, %f, %u, i%d)"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ztoXOd/Sources/CoreSpotlight_frameworks/corespotlight/CoreSpotlight/CoreSpotlightStructuredQuery/StructuredQuery-Model/_CSQueryOperation.m"
+ "CSInlineDonation fetchLastClientState: failed to resolve descriptor for sourceIdentifier=%@ error=%@ (donationCode=%ld)"
+ "CSInlineDonation fetchLastClientState: failed to start donation for sourceIdentifier=%@ error=%@ (donationCode=%ld)"
+ "CSInlineDonation fetchLastClientState: no set yet for sourceIdentifier=%@"
+ "CSInlineDonation fetchLastClientState: revision token is not valid base64 for clientStateName=%@ sourceIdentifier=%@ (donationCode=%ld)"
+ "CSInlineDonation fetchLastClientState: sourceIdentifier=%@ clientStateName=%@ protectionClass=%@"
+ "CSInlineDonation fetchLastClientState: unidentifiable source (donationCode=%ld)"
+ "ErrorCode=%{public,signpost.telemetry:string1}s, QueryLength=%{public,signpost.telemetry:number1}lu, FoundCount=%{public,signpost.telemetry:number2}lu "
+ "LongRunningQuery"
+ "Prior client state missing (expected: %@) for client name: %@"
+ "QueryClass=%{signpost.description:attribute}s, queryID=%{public,name=queryID}lu"
+ "QueryClass=%{signpost.description:attribute}s, queryID=%{public,name=queryID}lu, BundleID=%{signpost.description:attribute}s"
+ "QueryTelemetry"
+ "_CSAnnQueryPredicate compileToMDQueryString called without an embeddings sink — use compileToMDQueryStringWithContext: with %@ set to a NSMutableArray<NSData *>"
+ "_CSAnnQueryPredicate: empty queryText"
+ "_CSAnnQueryPredicate: failed to unarchive embeddingResultKey: %{public}@"
+ "_CSAnnQueryPredicate: missing embeddings sink in context — semantic predicate cannot compile"
+ "_CSAnnQueryPredicate: missing parse options in context — caller must enable embedding generation"
+ "_CSAnnQueryPredicate: noArgCompile branch (queryLen=%lu) — returning nil; caller must switch to compileToMDQueryStringWithContext: to get the keyword fallback"
+ "_CSAnnQueryPredicate: parser dict missing MDItemPrimaryTextEmbedding for query"
+ "_CSAnnQueryPredicate: query parser produced no embeddingResultKey(embedding generation timed out or failed)"
+ "_CSAnnQueryPredicate: semantic search unavailable on this device (CSGenerativeModelsAvailabilityManager.isSemanticSearchAvailable == NO)@"
+ "_CSQueryNodeEmbeddingsSink"
+ "_CSQueryNodeParseOptions"
+ "_CSUserQueryPreheatWithOptionsDict QOS %d"
+ "aNN.data(%@, %lu, %ld, %f, 0, i%d)"
+ "aNN.data(%@, 0, %ld, %f, %u, i%d)"
+ "com.apple.assetsd"
+ "com.apple.siriactionsd"
+ "com.apple.spotlightknowledged"
+ "com.apple.suggestd"
+ "com.apple.textunderstanding"
+ "fetchLastClientState: failed to resolve sourceIdentifier descriptor"
+ "fetchLastClientState: failed to start donation for read"
+ "fetchLastClientState: revision token is not valid base64"
+ "fetchLastClientState: unidentifiable source"
+ "lqmo"
+ "lqto"
- "%08x"
- "%@ || aNN.data(%@, 0, %ld, %f, %u)"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uflnlB/Sources/CoreSpotlight_frameworks/corespotlight/CoreSpotlight/CoreSpotlightStructuredQuery/StructuredQuery-Model/_CSQueryOperation.m"
- "CSUserQueryCounting"
- "CSUserQuerySuggestions"
- "CSUserQueryTopHits"
- "Cannot generate embedding for empty text"
- "Embedding generation failed: %@"
- "Embedding generation returned no results"
- "Embedding result contains no data"
- "Failed to create SPTextInput"
- "Failed to generate embedding for query: %@"
- "Generated embedding: %lu dimensions, version %lu"
- "No embedding provider registered - semantic search unavailable"
- "No embedding provider registered, using version 0"
- "QueryClass=%{signpost.description:attribute}s, qid=%{signpost.description:attribute}lu"
- "QueryClass=%{signpost.description:attribute}s, qid=%{signpost.description:attribute}lu, BundleID=%{signpost.description:attribute}s"
- "Unexpected embedding element type: %lu (expected Float32)"
- "aNN(%@, %ld, %ld, %@, %@, %ld, %f)"
- "v%lu"
- "v0"
```
