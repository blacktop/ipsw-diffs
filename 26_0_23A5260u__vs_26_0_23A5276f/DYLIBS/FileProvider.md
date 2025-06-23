## FileProvider

> `/System/Library/Frameworks/FileProvider.framework/FileProvider`

```diff

-3762.0.0.0.0
-  __TEXT.__text: 0x130848
+3833.0.0.502.1
+  __TEXT.__text: 0x131d7c
   __TEXT.__auth_stubs: 0x1d10
-  __TEXT.__objc_methlist: 0xe4f4
+  __TEXT.__objc_methlist: 0xe51c
   __TEXT.__const: 0x87e
-  __TEXT.__gcc_except_tab: 0xa1b0
-  __TEXT.__cstring: 0x147e2
-  __TEXT.__oslogstring: 0xdc26
+  __TEXT.__gcc_except_tab: 0xa3a4
+  __TEXT.__cstring: 0x144e2
+  __TEXT.__oslogstring: 0xdc6f
   __TEXT.__dlopen_cstrs: 0x79f
   __TEXT.__ustring: 0x21e
   __TEXT.__swift5_typeref: 0xb4

   __TEXT.__swift5_types: 0x8
   __TEXT.__swift_as_entry: 0x4
   __TEXT.__swift_as_ret: 0x4
-  __TEXT.__unwind_info: 0x5638
+  __TEXT.__unwind_info: 0x5820
   __TEXT.__eh_frame: 0xa0
   __TEXT.__objc_classname: 0x2045
-  __TEXT.__objc_methname: 0x23b91
-  __TEXT.__objc_methtype: 0x6811
-  __TEXT.__objc_stubs: 0x13d40
-  __DATA_CONST.__got: 0xa90
-  __DATA_CONST.__const: 0x6088
+  __TEXT.__objc_methname: 0x23cbc
+  __TEXT.__objc_methtype: 0x67f1
+  __TEXT.__objc_stubs: 0x13d60
+  __DATA_CONST.__got: 0xa98
+  __DATA_CONST.__const: 0x6068
   __DATA_CONST.__objc_classlist: 0x690
   __DATA_CONST.__objc_catlist: 0x88
   __DATA_CONST.__objc_protolist: 0x2a0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6d08
+  __DATA_CONST.__objc_selrefs: 0x6d18
   __DATA_CONST.__objc_protorefs: 0x158
   __DATA_CONST.__objc_superrefs: 0x550
   __DATA_CONST.__objc_arraydata: 0xab0
   __AUTH_CONST.__auth_got: 0xe98
   __AUTH_CONST.__const: 0x1c08
-  __AUTH_CONST.__cfstring: 0x11080
-  __AUTH_CONST.__objc_const: 0x24740
+  __AUTH_CONST.__cfstring: 0x110e0
+  __AUTH_CONST.__objc_const: 0x247a0
   __AUTH_CONST.__objc_intobj: 0x108
   __AUTH_CONST.__objc_arrayobj: 0x198
   __AUTH.__objc_data: 0x500
   __AUTH.__data: 0x10
-  __DATA.__objc_ivar: 0x1080
+  __DATA.__objc_ivar: 0x1088
   __DATA.__data: 0x20c0
   __DATA.__bss: 0xac0
   __DATA.__common: 0x39

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
-  UUID: C63BC528-62FB-31D8-BFA5-70C398DA37B7
-  Functions: 7169
-  Symbols:   23362
-  CStrings:  12248
+  UUID: C14A9D0B-5751-3036-B230-A69BCFFB7590
+  Functions: 7238
+  Symbols:   23424
+  CStrings:  12249
 
Symbols:
+ +[FPSearchOnServerEnumerator enumeratorForQuery:providerDomainID:desiredNumberOfResults:completionHandler:]
+ -[FPSearchOnServerEnumerator initWithQuery:domainIDs:desiredNumberOfResults:]
+ -[FPSearchOnServerRequestDescriptor desiredNumberOfResults]
+ -[FPSearchOnServerRequestDescriptor initWithQuery:desiredNumberOfResults:maximumNumberOfResultsPerPage:]
+ -[FPSearchOnServerRequestDescriptor maximumNumberOfResultsPerPage]
+ -[FPXSearchEnumerator initWithDomainContext:vendorEnumerator:queue:maximumNumberOfResultsPerPage:]
+ -[FPXSearchEnumeratorObserver initWithMaximumNumberOfResultsPerPage:completionHandler:]
+ -[FPXSearchEnumeratorObserver maximumNumberOfResultsPerPage]
+ -[FPXWrappedSearchEnumeratorObserver initWithTarget:providerID:domainIdentifier:maximumNumberOfResultsPerPage:]
+ -[FPXWrappedSearchEnumeratorObserver maximumNumberOfResultsPerPage]
+ -[FPXWrappedSearchEnumeratorObserver setMaximumNumberOfResultsPerPage:]
+ -[NSFileProviderStringSearchRequest desiredNumberOfResults]
+ -[NSFileProviderStringSearchRequest initWithQuery:desiredNumberOfResults:]
+ GCC_except_table290
+ GCC_except_table309
+ GCC_except_table316
+ GCC_except_table318
+ GCC_except_table319
+ GCC_except_table323
+ GCC_except_table325
+ GCC_except_table331
+ GCC_except_table339
+ GCC_except_table341
+ GCC_except_table345
+ GCC_except_table349
+ GCC_except_table351
+ GCC_except_table354
+ GCC_except_table356
+ GCC_except_table360
+ GCC_except_table366
+ GCC_except_table367
+ GCC_except_table373
+ GCC_except_table375
+ GCC_except_table382
+ GCC_except_table387
+ GCC_except_table390
+ GCC_except_table409
+ GCC_except_table411
+ GCC_except_table413
+ GCC_except_table425
+ GCC_except_table426
+ GCC_except_table428
+ GCC_except_table432
+ _OBJC_CLASS_$_UMUserPersonaAttributes
+ _OBJC_IVAR_$_FPSearchOnServerRequestDescriptor._desiredNumberOfResults
+ _OBJC_IVAR_$_FPSearchOnServerRequestDescriptor._maximumNumberOfResultsPerPage
+ _OBJC_IVAR_$_FPXSearchEnumerator._maximumNumberOfResultsPerPage
+ _OBJC_IVAR_$_FPXSearchEnumeratorObserver._maximumNumberOfResultsPerPage
+ _OBJC_IVAR_$_FPXWrappedSearchEnumeratorObserver._maximumNumberOfResultsPerPage
+ _OBJC_IVAR_$_NSFileProviderStringSearchRequest._desiredNumberOfResults
+ _OUTLINED_FUNCTION_33
+ _OUTLINED_FUNCTION_34
+ _OUTLINED_FUNCTION_35
+ _OUTLINED_FUNCTION_36
+ _OUTLINED_FUNCTION_37
+ _OUTLINED_FUNCTION_38
+ _OUTLINED_FUNCTION_39
+ _OUTLINED_FUNCTION_40
+ _OUTLINED_FUNCTION_41
+ _OUTLINED_FUNCTION_42
+ _OUTLINED_FUNCTION_43
+ _OUTLINED_FUNCTION_44
+ _OUTLINED_FUNCTION_45
+ ___100-[FPXExtensionContext _singleItemChange:changedFields:bounce:bounceIndex:request:completionHandler:]_block_invoke.292
+ ___100-[FPXExtensionContext _singleItemChange:changedFields:bounce:bounceIndex:request:completionHandler:]_block_invoke_2.cold.1
+ ___103-[FPXExtensionContext modifyItem:baseVersion:changedFields:contents:options:request:completionHandler:]_block_invoke.285
+ ___109-[FPXExtensionContext performActionWithIdentifier:onItemsWithIdentifiers:domainIdentifier:completionHandler:]_block_invoke.562
+ ___109-[FPXExtensionContext signalNeedsReindexItemsWithIdentifiers:domainIdentifier:indexReason:completionHandler:]_block_invoke.305
+ ___109-[FPXExtensionContext signalNeedsReindexItemsWithIdentifiers:domainIdentifier:indexReason:completionHandler:]_block_invoke.305.cold.1
+ ___109-[FPXExtensionContext signalNeedsReindexItemsWithIdentifiers:domainIdentifier:indexReason:completionHandler:]_block_invoke.307
+ ___110-[FPXExtensionContext URLForItemID:creatingPlaceholderIfMissing:ignoreAlternateContentsURL:completionHandler:]_block_invoke.337
+ ___110-[FPXExtensionContext URLForItemID:creatingPlaceholderIfMissing:ignoreAlternateContentsURL:completionHandler:]_block_invoke.337.cold.1
+ ___112-[FPXExtensionContext fetchDefaultContainerForBundleIdentifier:defaultName:inDomainIdentifier:lookupOnly:reply:]_block_invoke.542
+ ___112-[FPXExtensionContext fetchDefaultContainerForBundleIdentifier:defaultName:inDomainIdentifier:lookupOnly:reply:]_block_invoke.546
+ ___120-[FPXExtensionContext _createItemBasedOnTemplate:fields:contents:options:request:bounce:bounceNumber:completionHandler:]_block_invoke.532
+ ___120-[FPXExtensionContext _createItemBasedOnTemplate:fields:contents:options:request:bounce:bounceNumber:completionHandler:]_block_invoke.532.cold.1
+ ___120-[FPXExtensionContext _createItemBasedOnTemplate:fields:contents:options:request:bounce:bounceNumber:completionHandler:]_block_invoke.532.cold.2
+ ___120-[FPXExtensionContext _createItemBasedOnTemplate:fields:contents:options:request:bounce:bounceNumber:completionHandler:]_block_invoke.532.cold.3
+ ___120-[FPXExtensionContext _createItemBasedOnTemplate:fields:contents:options:request:bounce:bounceNumber:completionHandler:]_block_invoke.532.cold.4
+ ___120-[FPXExtensionContext _createItemBasedOnTemplate:fields:contents:options:request:bounce:bounceNumber:completionHandler:]_block_invoke.532.cold.5
+ ___120-[FPXExtensionContext _createItemBasedOnTemplate:fields:contents:options:request:bounce:bounceNumber:completionHandler:]_block_invoke.532.cold.6
+ ___120-[FPXExtensionContext _createItemBasedOnTemplate:fields:contents:options:request:bounce:bounceNumber:completionHandler:]_block_invoke.536
+ ___137-[FPXExtensionContext fetchContentsForItemWithID:version:request:estimatedItemSize:isSymlink:extent:alignment:options:completionHandler:]_block_invoke.248
+ ___137-[FPXExtensionContext fetchContentsForItemWithID:version:request:estimatedItemSize:isSymlink:extent:alignment:options:completionHandler:]_block_invoke.262
+ ___155-[FPXExtensionContext fetchContentsForItemWithID:version:usingExistingContentsAtURL:existingVersion:request:estimatedItemSize:isSymlink:completionHandler:]_block_invoke.278
+ ___155-[FPXExtensionContext fetchContentsForItemWithID:version:usingExistingContentsAtURL:existingVersion:request:estimatedItemSize:isSymlink:completionHandler:]_block_invoke.279
+ ___52-[FPXExtensionContext itemForURL:completionHandler:]_block_invoke.332
+ ___56-[FPXExtensionContext trashItemAtURL:completionHandler:]_block_invoke.341
+ ___56-[FPXExtensionContext trashItemAtURL:completionHandler:]_block_invoke.345
+ ___56-[FPXExtensionContext trashItemAtURL:completionHandler:]_block_invoke.346
+ ___56-[FPXExtensionContext trashItemAtURL:completionHandler:]_block_invoke.346.cold.1
+ ___56-[FPXExtensionContext trashItemAtURL:completionHandler:]_block_invoke.351
+ ___56-[FPXExtensionContext trashItemAtURL:completionHandler:]_block_invoke_2.cold.1
+ ___56-[FPXExtensionContext trashItemAtURL:completionHandler:]_block_invoke_2.cold.2
+ ___63-[FPXExtensionContext itemForItemID:request:completionHandler:]_block_invoke.321
+ ___63-[FPXExtensionContext preflightTrashItemIDs:completionHandler:]_block_invoke.311
+ ___65-[FPXExtensionContext getKnownFolderLocations:completionHandler:]_block_invoke.623
+ ___65-[FPXExtensionContext getKnownFolderLocations:completionHandler:]_block_invoke.623.cold.1
+ ___65-[FPXExtensionContext providePlaceholderAtURL:completionHandler:]_block_invoke.317
+ ___65-[FPXExtensionContext waitForStabilizationWithCompletionHandler:]_block_invoke.629
+ ___66-[FPXExtensionContext fetchTrashIdentifiersWithCompletionHandler:]_block_invoke.608
+ ___66-[FPXExtensionContext wakeForSessionIdentifier:completionHandler:]_block_invoke.568
+ ___66-[FPXExtensionContext wakeForSessionIdentifier:completionHandler:]_block_invoke.568.cold.1
+ ___67-[FPXExtensionContext bulkEvictItemsWithItemIDs:completionHandler:]_block_invoke.569
+ ___67-[FPXExtensionContext bulkEvictItemsWithItemIDs:completionHandler:]_block_invoke.571
+ ___68-[FPXExtensionContext disconnectDomainID:options:completionHandler:]_block_invoke.558
+ ___68-[FPXExtensionContext preflightReparentItemIDs:underParentID:reply:]_block_invoke.500
+ ___69-[FPXExtensionContext deleteItemsWithIDs:baseVersions:options:reply:]_block_invoke.519.cold.1
+ ___69-[FPXExtensionContext deleteItemsWithIDs:baseVersions:options:reply:]_block_invoke.525
+ ___69-[FPXExtensionContext fetchPublishingURLForItemID:completionHandler:]_block_invoke.552
+ ___71-[FPXExtensionContext bulkItemChanges:changedFields:completionHandler:]_block_invoke.297
+ ___71-[FPXExtensionContext valuesForAttributes:forItemID:completionHandler:]_block_invoke.432
+ ___72-[FPXExtensionContext shouldConnectExternalDomainWithCompletionHandler:]_block_invoke.635
+ ___77-[FPSearchOnServerEnumerator initWithQuery:domainIDs:desiredNumberOfResults:]_block_invoke
+ ___77-[FPSearchOnServerEnumerator initWithQuery:domainIDs:desiredNumberOfResults:]_block_invoke_2
+ ___77-[FPSearchOnServerEnumerator initWithQuery:domainIDs:desiredNumberOfResults:]_block_invoke_3
+ ___77-[FPSearchOnServerEnumerator initWithQuery:domainIDs:desiredNumberOfResults:]_block_invoke_3.cold.1
+ ___78-[FPXExtensionContext attemptRecoveryFromError:optionIndex:completionHandler:]_block_invoke.574
+ ___80-[FPXExtensionContext startProvidingItemAtURL:readingOptions:completionHandler:]_block_invoke.198
+ ___80-[FPXExtensionContext startProvidingItemAtURL:readingOptions:completionHandler:]_block_invoke.198.cold.1
+ ___80-[FPXExtensionContext startProvidingItemAtURL:readingOptions:completionHandler:]_block_invoke.198.cold.2
+ ___86-[FPXExtensionContext deleteItemWithID:baseVersion:options:request:completionHandler:]_block_invoke.526
+ ___87-[FPXExtensionContext fetchServicesForItemID:allowRestrictedSources:completionHandler:]_block_invoke.483
+ ___90-[FPXExtensionContext removeTrashedItemsOlderThanDate:domainIdentifier:completionHandler:]_block_invoke.224
+ ___90-[FPXExtensionContext removeTrashedItemsOlderThanDate:domainIdentifier:completionHandler:]_block_invoke.224.cold.1
+ ___93-[FPXExtensionContext startOperation:toFetchThumbnailsWithDictionary:size:completionHandler:]_block_invoke.413
+ ___93-[FPXExtensionContext startOperation:toFetchThumbnailsWithDictionary:size:completionHandler:]_block_invoke.413.cold.1
+ ___93-[FPXExtensionContext startOperation:toFetchThumbnailsWithDictionary:size:completionHandler:]_block_invoke.426
+ ___93-[FPXExtensionContext startOperation:toFetchThumbnailsWithDictionary:size:completionHandler:]_block_invoke.426.cold.1
+ ___93-[FPXExtensionContext startOperation:toFetchThumbnailsWithDictionary:size:completionHandler:]_block_invoke.428
+ ___93-[FPXExtensionContext startOperation:toFetchThumbnailsWithDictionary:size:completionHandler:]_block_invoke.431
+ ___94-[FPXExtensionContext didUpdateAlternateContentsDocumentForDocumentWithURL:completionHandler:]_block_invoke.319
+ ___94-[FPXExtensionContext didUpdateAlternateContentsDocumentForDocumentWithURL:completionHandler:]_block_invoke.319.cold.1
+ ___94-[FPXExtensionContext didUpdateAlternateContentsDocumentForDocumentWithURL:completionHandler:]_block_invoke.319.cold.2
+ ___94-[FPXExtensionContext didUpdateAlternateContentsDocumentForDocumentWithURL:completionHandler:]_block_invoke.319.cold.3
+ ___94-[FPXExtensionContext didUpdateAlternateContentsDocumentForDocumentWithURL:completionHandler:]_block_invoke.319.cold.4
+ ___94-[FPXExtensionContext didUpdateAlternateContentsDocumentForDocumentWithURL:completionHandler:]_block_invoke.320
+ ___95-[FPXExtensionContext fetchAndStartEnumeratingWithSettings:observer:request:completionHandler:]_block_invoke.458
+ ___97-[FPXExtensionContext startOperation:toFetchThumbnailsForItemIdentifiers:size:completionHandler:]_block_invoke.363
+ ___97-[FPXExtensionContext startOperation:toFetchThumbnailsForItemIdentifiers:size:completionHandler:]_block_invoke.382
+ ___97-[FPXExtensionContext startOperation:toFetchThumbnailsForItemIdentifiers:size:completionHandler:]_block_invoke.382.cold.1
+ ___97-[FPXExtensionContext startOperation:toFetchThumbnailsForItemIdentifiers:size:completionHandler:]_block_invoke.384
+ ___97-[FPXExtensionContext startOperation:toFetchThumbnailsForItemIdentifiers:size:completionHandler:]_block_invoke.387
+ ___97-[FPXExtensionContext startOperation:toFetchThumbnailsForItemIdentifiers:size:completionHandler:]_block_invoke_2.386
+ ___97-[FPXExtensionContext startOperation:toFetchThumbnailsForItemIdentifiers:size:completionHandler:]_block_invoke_2.386.cold.1
+ ___FPCrossDeviceItemIDForItemID_block_invoke.75
+ ___FPItemIDFromCrossDeviceItemID_block_invoke.101
+ ___FPItemURLForCrossDeviceItemID_block_invoke.83
+ ___FPItemURLForCrossDeviceItemID_block_invoke.83.cold.1
+ ___FPItemURLForCrossDeviceItemID_block_invoke.88
+ ___FPItemURLForCrossDeviceItemID_block_invoke.88.cold.1
+ ___block_literal_global.183
+ ___block_literal_global.187
+ ___block_literal_global.286
+ ___block_literal_global.366
+ ___block_literal_global.425
+ ___block_literal_global.434
+ ___block_literal_global.461
+ ___block_literal_global.486
+ ___block_literal_global.498
+ ___block_literal_global.578
+ ___block_literal_global.580
+ ___block_literal_global.619
+ _do_unlinkat
+ _fpfs_mkdirat
+ _objc_msgSend$enumeratorForQuery:providerDomainID:desiredNumberOfResults:completionHandler:
+ _objc_msgSend$initWithMaximumNumberOfResultsPerPage:completionHandler:
+ _objc_msgSend$initWithQuery:desiredNumberOfResults:maximumNumberOfResultsPerPage:
+ _objc_msgSend$initWithQuery:domainIDs:desiredNumberOfResults:
+ _objc_msgSend$initWithTarget:providerID:domainIdentifier:maximumNumberOfResultsPerPage:
+ _objc_msgSend$personaAttributesForPersonaType:
- +[FPSearchOnServerEnumerator enumeratorForQuery:providerDomainID:completionHandler:]
- -[FPSearchOnServerRequestDescriptor initWithQuery:maxNumberOfResults:]
- -[FPSearchOnServerRequestDescriptor maxNumberOfResults]
- -[FPXExtensionContext createItemBasedOnTemplate:fields:contents:options:request:bounce:completionHandler:].cold.1
- -[FPXExtensionContext deleteSearchableItemsWithSpotlightDomainIdentifiers:domainIdentifier:indexReason:completionHandler:].cold.2
- -[FPXExtensionContext itemForURL:completionHandler:].cold.2
- -[FPXSearchEnumerator initWithDomainContext:vendorEnumerator:queue:maxNumberOfResults:]
- -[FPXSearchEnumeratorObserver initWithMaxNumberOfResults:completionHandler:]
- -[FPXSearchEnumeratorObserver maxNumberOfResults]
- -[FPXWrappedSearchEnumeratorObserver initWithTarget:maxNumberOfResults:providerID:domainIdentifier:]
- -[FPXWrappedSearchEnumeratorObserver maxNumberOfResults]
- -[FPXWrappedSearchEnumeratorObserver setMaxNumberOfResults:]
- -[NSFileProviderStringSearchRequest initWithQuery:]
- GCC_except_table350
- GCC_except_table368
- GCC_except_table377
- GCC_except_table392
- GCC_except_table429
- GCC_except_table431
- _OBJC_IVAR_$_FPSearchOnServerRequestDescriptor._maxNumberOfResults
- _OBJC_IVAR_$_FPXSearchEnumerator._maxNumberOfResults
- _OBJC_IVAR_$_FPXSearchEnumeratorObserver._maxNumberOfResults
- _OBJC_IVAR_$_FPXWrappedSearchEnumeratorObserver._maxNumberOfResults
- ___100-[FPXExtensionContext _singleItemChange:changedFields:bounce:bounceIndex:request:completionHandler:]_block_invoke_3
- ___100-[FPXExtensionContext _singleItemChange:changedFields:bounce:bounceIndex:request:completionHandler:]_block_invoke_3.cold.1
- ___103-[FPXExtensionContext modifyItem:baseVersion:changedFields:contents:options:request:completionHandler:]_block_invoke.287
- ___109-[FPXExtensionContext performActionWithIdentifier:onItemsWithIdentifiers:domainIdentifier:completionHandler:]_block_invoke_2
- ___109-[FPXExtensionContext signalNeedsReindexItemsWithIdentifiers:domainIdentifier:indexReason:completionHandler:]_block_invoke.306
- ___109-[FPXExtensionContext signalNeedsReindexItemsWithIdentifiers:domainIdentifier:indexReason:completionHandler:]_block_invoke_2
- ___109-[FPXExtensionContext signalNeedsReindexItemsWithIdentifiers:domainIdentifier:indexReason:completionHandler:]_block_invoke_2.cold.1
- ___110-[FPXExtensionContext URLForItemID:creatingPlaceholderIfMissing:ignoreAlternateContentsURL:completionHandler:]_block_invoke.334
- ___110-[FPXExtensionContext URLForItemID:creatingPlaceholderIfMissing:ignoreAlternateContentsURL:completionHandler:]_block_invoke.334.cold.1
- ___112-[FPXExtensionContext fetchDefaultContainerForBundleIdentifier:defaultName:inDomainIdentifier:lookupOnly:reply:]_block_invoke.538
- ___112-[FPXExtensionContext fetchDefaultContainerForBundleIdentifier:defaultName:inDomainIdentifier:lookupOnly:reply:]_block_invoke_2.539
- ___120-[FPXExtensionContext _createItemBasedOnTemplate:fields:contents:options:request:bounce:bounceNumber:completionHandler:]_block_invoke.525
- ___120-[FPXExtensionContext _createItemBasedOnTemplate:fields:contents:options:request:bounce:bounceNumber:completionHandler:]_block_invoke.525.cold.1
- ___120-[FPXExtensionContext _createItemBasedOnTemplate:fields:contents:options:request:bounce:bounceNumber:completionHandler:]_block_invoke.525.cold.2
- ___120-[FPXExtensionContext _createItemBasedOnTemplate:fields:contents:options:request:bounce:bounceNumber:completionHandler:]_block_invoke.525.cold.3
- ___120-[FPXExtensionContext _createItemBasedOnTemplate:fields:contents:options:request:bounce:bounceNumber:completionHandler:]_block_invoke.525.cold.4
- ___120-[FPXExtensionContext _createItemBasedOnTemplate:fields:contents:options:request:bounce:bounceNumber:completionHandler:]_block_invoke.525.cold.5
- ___120-[FPXExtensionContext _createItemBasedOnTemplate:fields:contents:options:request:bounce:bounceNumber:completionHandler:]_block_invoke.525.cold.6
- ___120-[FPXExtensionContext _createItemBasedOnTemplate:fields:contents:options:request:bounce:bounceNumber:completionHandler:]_block_invoke.529
- ___137-[FPXExtensionContext fetchContentsForItemWithID:version:request:estimatedItemSize:isSymlink:extent:alignment:options:completionHandler:]_block_invoke.263
- ___137-[FPXExtensionContext fetchContentsForItemWithID:version:request:estimatedItemSize:isSymlink:extent:alignment:options:completionHandler:]_block_invoke_2.271
- ___155-[FPXExtensionContext fetchContentsForItemWithID:version:usingExistingContentsAtURL:existingVersion:request:estimatedItemSize:isSymlink:completionHandler:]_block_invoke.280
- ___155-[FPXExtensionContext fetchContentsForItemWithID:version:usingExistingContentsAtURL:existingVersion:request:estimatedItemSize:isSymlink:completionHandler:]_block_invoke.281
- ___52-[FPXExtensionContext itemForURL:completionHandler:]_block_invoke.329
- ___54-[FPSearchOnServerEnumerator initWithQuery:domainIDs:]_block_invoke
- ___54-[FPSearchOnServerEnumerator initWithQuery:domainIDs:]_block_invoke_2
- ___54-[FPSearchOnServerEnumerator initWithQuery:domainIDs:]_block_invoke_3
- ___54-[FPSearchOnServerEnumerator initWithQuery:domainIDs:]_block_invoke_3.cold.1
- ___56-[FPXExtensionContext trashItemAtURL:completionHandler:]_block_invoke.338
- ___56-[FPXExtensionContext trashItemAtURL:completionHandler:]_block_invoke.342
- ___56-[FPXExtensionContext trashItemAtURL:completionHandler:]_block_invoke.343
- ___56-[FPXExtensionContext trashItemAtURL:completionHandler:]_block_invoke.343.cold.1
- ___56-[FPXExtensionContext trashItemAtURL:completionHandler:]_block_invoke_3
- ___56-[FPXExtensionContext trashItemAtURL:completionHandler:]_block_invoke_3.cold.1
- ___56-[FPXExtensionContext trashItemAtURL:completionHandler:]_block_invoke_3.cold.2
- ___63-[FPXExtensionContext itemForItemID:request:completionHandler:]_block_invoke_2
- ___63-[FPXExtensionContext preflightTrashItemIDs:completionHandler:]_block_invoke.310
- ___64-[FPXEnumerator enumerateItemsFromPage:suggestedPageSize:reply:]_block_invoke.cold.1
- ___65-[FPXExtensionContext getKnownFolderLocations:completionHandler:]_block_invoke.613
- ___65-[FPXExtensionContext getKnownFolderLocations:completionHandler:]_block_invoke.613.cold.1
- ___65-[FPXExtensionContext providePlaceholderAtURL:completionHandler:]_block_invoke.316
- ___65-[FPXExtensionContext waitForStabilizationWithCompletionHandler:]_block_invoke.619
- ___66-[FPXExtensionContext fetchTrashIdentifiersWithCompletionHandler:]_block_invoke.598
- ___66-[FPXExtensionContext wakeForSessionIdentifier:completionHandler:]_block_invoke.558
- ___66-[FPXExtensionContext wakeForSessionIdentifier:completionHandler:]_block_invoke.558.cold.1
- ___67-[FPXExtensionContext bulkEvictItemsWithItemIDs:completionHandler:]_block_invoke.559
- ___67-[FPXExtensionContext bulkEvictItemsWithItemIDs:completionHandler:]_block_invoke.561
- ___68-[FPXExtensionContext disconnectDomainID:options:completionHandler:]_block_invoke_3
- ___68-[FPXExtensionContext preflightReparentItemIDs:underParentID:reply:]_block_invoke.494
- ___69-[FPXExtensionContext deleteItemsWithIDs:baseVersions:options:reply:]_block_invoke.513
- ___69-[FPXExtensionContext deleteItemsWithIDs:baseVersions:options:reply:]_block_invoke.513.cold.1
- ___69-[FPXExtensionContext fetchPublishingURLForItemID:completionHandler:]_block_invoke_2
- ___71-[FPXExtensionContext bulkItemChanges:changedFields:completionHandler:]_block_invoke_4
- ___71-[FPXExtensionContext valuesForAttributes:forItemID:completionHandler:]_block_invoke_2
- ___72-[FPXExtensionContext shouldConnectExternalDomainWithCompletionHandler:]_block_invoke.625
- ___78-[FPXExtensionContext attemptRecoveryFromError:optionIndex:completionHandler:]_block_invoke.564
- ___80-[FPXExtensionContext startProvidingItemAtURL:readingOptions:completionHandler:]_block_invoke.201
- ___80-[FPXExtensionContext startProvidingItemAtURL:readingOptions:completionHandler:]_block_invoke.201.cold.1
- ___80-[FPXExtensionContext startProvidingItemAtURL:readingOptions:completionHandler:]_block_invoke.201.cold.2
- ___86-[FPXExtensionContext deleteItemWithID:baseVersion:options:request:completionHandler:]_block_invoke_2
- ___87-[FPXExtensionContext fetchServicesForItemID:allowRestrictedSources:completionHandler:]_block_invoke_2
- ___90-[FPXExtensionContext removeTrashedItemsOlderThanDate:domainIdentifier:completionHandler:]_block_invoke_2
- ___90-[FPXExtensionContext removeTrashedItemsOlderThanDate:domainIdentifier:completionHandler:]_block_invoke_2.cold.1
- ___93-[FPXExtensionContext startOperation:toFetchThumbnailsWithDictionary:size:completionHandler:]_block_invoke.409
- ___93-[FPXExtensionContext startOperation:toFetchThumbnailsWithDictionary:size:completionHandler:]_block_invoke.409.cold.1
- ___93-[FPXExtensionContext startOperation:toFetchThumbnailsWithDictionary:size:completionHandler:]_block_invoke.422
- ___93-[FPXExtensionContext startOperation:toFetchThumbnailsWithDictionary:size:completionHandler:]_block_invoke.422.cold.1
- ___93-[FPXExtensionContext startOperation:toFetchThumbnailsWithDictionary:size:completionHandler:]_block_invoke.424
- ___93-[FPXExtensionContext startOperation:toFetchThumbnailsWithDictionary:size:completionHandler:]_block_invoke.427
- ___94-[FPXExtensionContext didUpdateAlternateContentsDocumentForDocumentWithURL:completionHandler:]_block_invoke.318
- ___94-[FPXExtensionContext didUpdateAlternateContentsDocumentForDocumentWithURL:completionHandler:]_block_invoke_2
- ___94-[FPXExtensionContext didUpdateAlternateContentsDocumentForDocumentWithURL:completionHandler:]_block_invoke_2.cold.1
- ___94-[FPXExtensionContext didUpdateAlternateContentsDocumentForDocumentWithURL:completionHandler:]_block_invoke_2.cold.2
- ___94-[FPXExtensionContext didUpdateAlternateContentsDocumentForDocumentWithURL:completionHandler:]_block_invoke_2.cold.3
- ___94-[FPXExtensionContext didUpdateAlternateContentsDocumentForDocumentWithURL:completionHandler:]_block_invoke_2.cold.4
- ___95-[FPXExtensionContext fetchAndStartEnumeratingWithSettings:observer:request:completionHandler:]_block_invoke.453
- ___97-[FPXExtensionContext startOperation:toFetchThumbnailsForItemIdentifiers:size:completionHandler:]_block_invoke.359
- ___97-[FPXExtensionContext startOperation:toFetchThumbnailsForItemIdentifiers:size:completionHandler:]_block_invoke.378
- ___97-[FPXExtensionContext startOperation:toFetchThumbnailsForItemIdentifiers:size:completionHandler:]_block_invoke.378.cold.1
- ___97-[FPXExtensionContext startOperation:toFetchThumbnailsForItemIdentifiers:size:completionHandler:]_block_invoke.380
- ___97-[FPXExtensionContext startOperation:toFetchThumbnailsForItemIdentifiers:size:completionHandler:]_block_invoke.383
- ___97-[FPXExtensionContext startOperation:toFetchThumbnailsForItemIdentifiers:size:completionHandler:]_block_invoke_2.382
- ___97-[FPXExtensionContext startOperation:toFetchThumbnailsForItemIdentifiers:size:completionHandler:]_block_invoke_2.382.cold.1
- ___FPCrossDeviceItemIDForItemID_block_invoke.76
- ___FPItemIDFromCrossDeviceItemID_block_invoke.102
- ___FPItemURLForCrossDeviceItemID_block_invoke.84
- ___FPItemURLForCrossDeviceItemID_block_invoke.84.cold.1
- ___FPItemURLForCrossDeviceItemID_block_invoke.89.cold.1
- ___FPItemURLForCrossDeviceItemID_block_invoke.90
- ___block_literal_global.135
- ___block_literal_global.186
- ___block_literal_global.190
- ___block_literal_global.285
- ___block_literal_global.362
- ___block_literal_global.426
- ___block_literal_global.435
- ___block_literal_global.456
- ___block_literal_global.480
- ___block_literal_global.579
- ___block_literal_global.581
- ___block_literal_global.609
- ___block_literal_global.67
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swiftDarwin_$_FileProvider
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_FileProvider
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_FileProvider
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_FileProvider
- _gatherDefaultPersona
- _objc_msgSend$enumeratorForQuery:providerDomainID:completionHandler:
- _objc_msgSend$initWithMaxNumberOfResults:completionHandler:
- _objc_msgSend$initWithQuery:maxNumberOfResults:
- _objc_msgSend$initWithTarget:maxNumberOfResults:providerID:domainIdentifier:
- _objc_msgSend$listAllPersonaWithAttributes
CStrings:
+ "-[FPXExtensionContext bulkItemChanges:changedFields:completionHandler:]_block_invoke_3"
+ "-[FPXExtensionContext disconnectDomainID:options:completionHandler:]_block_invoke_2"
+ "-[FPXExtensionContext trashItemAtURL:completionHandler:]_block_invoke_2"
+ "3833.0.0.502.1"
+ "@40@0:8@16Q24Q32"
+ "Sync is already paused."
+ "Sync is not paused."
+ "TQ,N,V_maximumNumberOfResultsPerPage"
+ "TQ,R,N,V_desiredNumberOfResults"
+ "TQ,R,N,V_maximumNumberOfResultsPerPage"
+ "[ERROR] Non matching personas for the extension %@ (%@, expect %@) on %s"
+ "_desiredNumberOfResults"
+ "_maximumNumberOfResultsPerPage"
+ "desiredNumberOfResults"
+ "enumeratorForQuery:providerDomainID:desiredNumberOfResults:completionHandler:"
+ "initWithDomainContext:vendorEnumerator:queue:maximumNumberOfResultsPerPage:"
+ "initWithMaximumNumberOfResultsPerPage:completionHandler:"
+ "initWithQuery:desiredNumberOfResults:"
+ "initWithQuery:desiredNumberOfResults:maximumNumberOfResultsPerPage:"
+ "initWithQuery:domainIDs:desiredNumberOfResults:"
+ "initWithTarget:providerID:domainIdentifier:maximumNumberOfResultsPerPage:"
+ "maximumNumberOfResultsPerPage"
+ "personaAttributesForPersonaType:"
+ "setMaximumNumberOfResultsPerPage:"
- "-[FPXExtensionContext bulkItemChanges:changedFields:completionHandler:]_block_invoke_4"
- "-[FPXExtensionContext deleteItemWithID:baseVersion:options:request:completionHandler:]_block_invoke_2"
- "-[FPXExtensionContext disconnectDomainID:options:completionHandler:]_block_invoke_3"
- "-[FPXExtensionContext fetchContentsForItemWithID:version:request:estimatedItemSize:isSymlink:extent:alignment:options:completionHandler:]_block_invoke_2"
- "-[FPXExtensionContext fetchDefaultContainerForBundleIdentifier:defaultName:inDomainIdentifier:lookupOnly:reply:]_block_invoke_2"
- "-[FPXExtensionContext fetchPublishingURLForItemID:completionHandler:]_block_invoke_2"
- "-[FPXExtensionContext itemForItemID:request:completionHandler:]_block_invoke_2"
- "-[FPXExtensionContext performActionWithIdentifier:onItemsWithIdentifiers:domainIdentifier:completionHandler:]_block_invoke_2"
- "-[FPXExtensionContext removeTrashedItemsOlderThanDate:domainIdentifier:completionHandler:]_block_invoke_2"
- "-[FPXExtensionContext trashItemAtURL:completionHandler:]_block_invoke_3"
- "-[FPXExtensionContext valuesForAttributes:forItemID:completionHandler:]_block_invoke_2"
- "3762"
- "@32@0:8@16q24"
- "@32@0:8q16@?24"
- "@48@0:8@16q24@32@40"
- "Tq,N,V_maxNumberOfResults"
- "Tq,R,N,V_maxNumberOfResults"
- "_maxNumberOfResults"
- "enumeratorForQuery:providerDomainID:completionHandler:"
- "initWithDomainContext:vendorEnumerator:queue:maxNumberOfResults:"
- "initWithMaxNumberOfResults:completionHandler:"
- "initWithQuery:"
- "initWithQuery:maxNumberOfResults:"
- "initWithTarget:maxNumberOfResults:providerID:domainIdentifier:"
- "listAllPersonaWithAttributes"
- "maxNumberOfResults"
- "setMaxNumberOfResults:"

```
