## FileProvider

> `/System/Library/Frameworks/FileProvider.framework/FileProvider`

```diff

-1835.102.2.0.0
-  __TEXT.__text: 0x11de14
+1835.120.53.0.0
+  __TEXT.__text: 0x11e618
   __TEXT.__auth_stubs: 0x19f0
-  __TEXT.__objc_methlist: 0xba38
+  __TEXT.__objc_methlist: 0xba88
   __TEXT.__const: 0x3a0
   __TEXT.__gcc_except_tab: 0x7270
-  __TEXT.__cstring: 0x13104
-  __TEXT.__oslogstring: 0xd05d
+  __TEXT.__cstring: 0x131e0
+  __TEXT.__oslogstring: 0xd18e
   __TEXT.__dlopen_cstrs: 0x7ed
   __TEXT.__ustring: 0x8
-  __TEXT.__unwind_info: 0x4e80
-  __TEXT.__objc_classname: 0x1e49
-  __TEXT.__objc_methname: 0x21560
-  __TEXT.__objc_methtype: 0x5db7
-  __TEXT.__objc_stubs: 0x12e40
+  __TEXT.__unwind_info: 0x4f44
+  __TEXT.__objc_classname: 0x1e4d
+  __TEXT.__objc_methname: 0x216ec
+  __TEXT.__objc_methtype: 0x5e0e
+  __TEXT.__objc_stubs: 0x12ea0
   __DATA_CONST.__got: 0x4b8
-  __DATA_CONST.__const: 0x5e68
+  __DATA_CONST.__const: 0x5e80
   __DATA_CONST.__objc_classlist: 0x640
   __DATA_CONST.__objc_catlist: 0x88
   __DATA_CONST.__objc_protolist: 0x280
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x20478
-  __DATA_CONST.__objc_selrefs: 0x64a0
+  __DATA_CONST.__objc_const: 0x204e8
+  __DATA_CONST.__objc_selrefs: 0x64d8
   __DATA_CONST.__objc_protorefs: 0x128
-  __DATA_CONST.__objc_classrefs: 0x798
+  __DATA_CONST.__objc_classrefs: 0x7a0
   __DATA_CONST.__objc_superrefs: 0x500
   __DATA_CONST.__objc_arraydata: 0xa90
   __AUTH_CONST.__objc_const: 0x5660
-  __AUTH_CONST.__cfstring: 0xfca0
+  __AUTH_CONST.__cfstring: 0xfdc0
   __AUTH_CONST.__const: 0x1960
   __AUTH_CONST.__objc_intobj: 0x108
   __AUTH_CONST.__objc_arrayobj: 0x150
   __AUTH_CONST.__auth_got: 0xd08
-  __AUTH.__objc_data: 0x1e0
+  __AUTH.__objc_data: 0x190
   __AUTH.__data: 0x10
-  __DATA.__objc_ivar: 0xf40
-  __DATA.__data: 0x2240
-  __DATA.__bss: 0x308
-  __DATA_DIRTY.__objc_data: 0x3ca0
+  __DATA.__objc_ivar: 0xf4c
+  __DATA.__data: 0x22a8
+  __DATA.__bss: 0x298
+  __DATA_DIRTY.__objc_data: 0x3cf0
   __DATA_DIRTY.__data: 0x2c0
-  __DATA_DIRTY.__bss: 0x3d8
+  __DATA_DIRTY.__bss: 0x3e0
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8B431A72-F554-39EB-A6EF-4A519AC6C233
-  Functions: 6798
-  Symbols:   21656
-  CStrings:  11554
+  UUID: 9C546859-51BC-3285-899B-A7AFF716128C
+  Functions: 6811
+  Symbols:   21690
+  CStrings:  11593
 
Symbols:
+ +[FPFrameworkOverridesIterator newIteratorForURL:withNotFoundHandler:]
+ -[FPFrameworkOverridesIterator initWithOverrides:url:noSuitableModuleFoundHandler:]
+ -[FPFrameworkOverridesIterator initWithOverrides:url:noSuitableModuleFoundHandler:].cold.1
+ -[FPImportProgressReport setXpcActivityTimeSinceLastAbleToRun:]
+ -[FPImportProgressReport xpcActivityTimeSinceLastAbleToRun]
+ -[NSURL(FPAdditions) _fp_relationshipToItemAtURL:bothAreRealpaths:]
+ -[NSURL(FPAdditions) fp_fpfsProviderDomainID:skipTypeCheck:error:]
+ -[NSURL(FPAdditions) fp_realPathRelationshipToItemAtRealPathURL:]
+ OBJC_IVAR_$_FPFrameworkOverridesIterator._checkURL
+ OBJC_IVAR_$_FPFrameworkOverridesIterator._mightBeFPURL
+ _FPInvalidParameterErrorWithExpectation
+ _NSFileProviderInternalErrorActualKey
+ _NSFileProviderInternalErrorExpectedKey
+ _NSFileProviderInternalErrorParameterKey
+ _OBJC_CLASS_$_UMUserPersona
+ _OBJC_IVAR_$_FPImportProgressReport._xpcActivityTimeSinceLastAbleToRun
+ ___101-[FPXExtensionContext fetchDefaultContainerForBundleIdentifier:defaultName:inDomainIdentifier:reply:]_block_invoke.529
+ ___101-[FPXExtensionContext fetchDefaultContainerForBundleIdentifier:defaultName:inDomainIdentifier:reply:]_block_invoke_2.533
+ ___103-[FPXExtensionContext modifyItem:baseVersion:changedFields:contents:options:request:completionHandler:]_block_invoke.280
+ ___110-[FPXExtensionContext URLForItemID:creatingPlaceholderIfMissing:ignoreAlternateContentsURL:completionHandler:]_block_invoke.328
+ ___110-[FPXExtensionContext URLForItemID:creatingPlaceholderIfMissing:ignoreAlternateContentsURL:completionHandler:]_block_invoke.328.cold.1
+ ___120-[FPXExtensionContext _createItemBasedOnTemplate:fields:contents:options:request:bounce:bounceNumber:completionHandler:]_block_invoke.516
+ ___120-[FPXExtensionContext _createItemBasedOnTemplate:fields:contents:options:request:bounce:bounceNumber:completionHandler:]_block_invoke.516.cold.1
+ ___120-[FPXExtensionContext _createItemBasedOnTemplate:fields:contents:options:request:bounce:bounceNumber:completionHandler:]_block_invoke.516.cold.2
+ ___120-[FPXExtensionContext _createItemBasedOnTemplate:fields:contents:options:request:bounce:bounceNumber:completionHandler:]_block_invoke.516.cold.3
+ ___120-[FPXExtensionContext _createItemBasedOnTemplate:fields:contents:options:request:bounce:bounceNumber:completionHandler:]_block_invoke.516.cold.4
+ ___120-[FPXExtensionContext _createItemBasedOnTemplate:fields:contents:options:request:bounce:bounceNumber:completionHandler:]_block_invoke.516.cold.5
+ ___120-[FPXExtensionContext _createItemBasedOnTemplate:fields:contents:options:request:bounce:bounceNumber:completionHandler:]_block_invoke.516.cold.6
+ ___120-[FPXExtensionContext _createItemBasedOnTemplate:fields:contents:options:request:bounce:bounceNumber:completionHandler:]_block_invoke.520
+ ___137-[FPXExtensionContext fetchContentsForItemWithID:version:request:estimatedItemSize:isSymlink:extent:alignment:options:completionHandler:]_block_invoke.256
+ ___137-[FPXExtensionContext fetchContentsForItemWithID:version:request:estimatedItemSize:isSymlink:extent:alignment:options:completionHandler:]_block_invoke_2.264
+ ___144+[NSFileProviderManager addDomain:forProviderIdentifier:byImportingDirectoryAtURL:userAllowedDBDrop:knownFolders:synchronous:completionHandler:]_block_invoke.cold.1
+ ___155-[FPXExtensionContext fetchContentsForItemWithID:version:usingExistingContentsAtURL:existingVersion:request:estimatedItemSize:isSymlink:completionHandler:]_block_invoke.273
+ ___155-[FPXExtensionContext fetchContentsForItemWithID:version:usingExistingContentsAtURL:existingVersion:request:estimatedItemSize:isSymlink:completionHandler:]_block_invoke.274
+ ___52-[FPXExtensionContext itemForURL:completionHandler:]_block_invoke.323
+ ___56-[FPXExtensionContext trashItemAtURL:completionHandler:]_block_invoke.332
+ ___56-[FPXExtensionContext trashItemAtURL:completionHandler:]_block_invoke.336
+ ___56-[FPXExtensionContext trashItemAtURL:completionHandler:]_block_invoke.337
+ ___56-[FPXExtensionContext trashItemAtURL:completionHandler:]_block_invoke.337.cold.1
+ ___56-[FPXExtensionContext trashItemAtURL:completionHandler:]_block_invoke.338
+ ___63-[FPXExtensionContext preflightTrashItemIDs:completionHandler:]_block_invoke.304
+ ___65-[FPXExtensionContext providePlaceholderAtURL:completionHandler:]_block_invoke.310
+ ___65-[FPXExtensionContext waitForStabilizationWithCompletionHandler:]_block_invoke.602
+ ___66-[FPXExtensionContext fetchTrashIdentifiersWithCompletionHandler:]_block_invoke.589
+ ___66-[FPXExtensionContext wakeForSessionIdentifier:completionHandler:]_block_invoke.549
+ ___66-[FPXExtensionContext wakeForSessionIdentifier:completionHandler:]_block_invoke.549.cold.1
+ ___67-[FPPendingSetEnumerator enumerateItemsForObserver:startingAtPage:]_block_invoke.440
+ ___67-[FPXExtensionContext bulkEvictItemsWithItemIDs:completionHandler:]_block_invoke.550
+ ___67-[FPXExtensionContext bulkEvictItemsWithItemIDs:completionHandler:]_block_invoke.552
+ ___68-[FPXExtensionContext preflightReparentItemIDs:underParentID:reply:]_block_invoke.485
+ ___69-[FPPendingSetEnumerator enumerateChangesForObserver:fromSyncAnchor:]_block_invoke.444
+ ___69-[FPPendingSetEnumerator enumerateChangesForObserver:fromSyncAnchor:]_block_invoke_2.447
+ ___69-[FPXExtensionContext deleteItemsWithIDs:baseVersions:options:reply:]_block_invoke.504
+ ___69-[FPXExtensionContext deleteItemsWithIDs:baseVersions:options:reply:]_block_invoke.504.cold.1
+ ___69-[FPXExtensionContext deleteItemsWithIDs:baseVersions:options:reply:]_block_invoke.510
+ ___78-[FPXExtensionContext attemptRecoveryFromError:optionIndex:completionHandler:]_block_invoke.555
+ ___80-[FPXExtensionContext startProvidingItemAtURL:readingOptions:completionHandler:]_block_invoke.194
+ ___80-[FPXExtensionContext startProvidingItemAtURL:readingOptions:completionHandler:]_block_invoke.194.cold.1
+ ___80-[FPXExtensionContext startProvidingItemAtURL:readingOptions:completionHandler:]_block_invoke.194.cold.2
+ ___87-[FPXExtensionContext fetchServicesForItemID:allowRestrictedSources:completionHandler:]_block_invoke.468
+ ___93-[FPXExtensionContext startOperation:toFetchThumbnailsWithDictionary:size:completionHandler:]_block_invoke.400
+ ___93-[FPXExtensionContext startOperation:toFetchThumbnailsWithDictionary:size:completionHandler:]_block_invoke.400.cold.1
+ ___93-[FPXExtensionContext startOperation:toFetchThumbnailsWithDictionary:size:completionHandler:]_block_invoke.413
+ ___93-[FPXExtensionContext startOperation:toFetchThumbnailsWithDictionary:size:completionHandler:]_block_invoke.413.cold.1
+ ___93-[FPXExtensionContext startOperation:toFetchThumbnailsWithDictionary:size:completionHandler:]_block_invoke.418
+ ___94-[FPXExtensionContext didUpdateAlternateContentsDocumentForDocumentWithURL:completionHandler:]_block_invoke.312
+ ___95-[FPXExtensionContext fetchAndStartEnumeratingWithSettings:observer:request:completionHandler:]_block_invoke.444
+ ___97-[FPXExtensionContext startOperation:toFetchThumbnailsForItemIdentifiers:size:completionHandler:]_block_invoke.350
+ ___97-[FPXExtensionContext startOperation:toFetchThumbnailsForItemIdentifiers:size:completionHandler:]_block_invoke.369
+ ___97-[FPXExtensionContext startOperation:toFetchThumbnailsForItemIdentifiers:size:completionHandler:]_block_invoke.369.cold.1
+ ___97-[FPXExtensionContext startOperation:toFetchThumbnailsForItemIdentifiers:size:completionHandler:]_block_invoke.374
+ ___97-[FPXExtensionContext startOperation:toFetchThumbnailsForItemIdentifiers:size:completionHandler:]_block_invoke_2.373
+ ___97-[FPXExtensionContext startOperation:toFetchThumbnailsForItemIdentifiers:size:completionHandler:]_block_invoke_2.373.cold.1
+ ___block_descriptor_64_e8_32s40s48bs_e30_v24?0"NSString"8"NSError"16ls32l8s40l8s48l8
+ ___block_literal_global.165
+ ___block_literal_global.170
+ ___block_literal_global.262
+ ___block_literal_global.268
+ ___block_literal_global.353
+ ___block_literal_global.413
+ ___block_literal_global.419
+ ___block_literal_global.421
+ ___block_literal_global.446
+ ___block_literal_global.447
+ ___block_literal_global.449
+ ___block_literal_global.471
+ ___block_literal_global.511
+ ___block_literal_global.600
+ ___block_literal_global.631
+ _fpfs_get_purgeable_stats
+ _fpfs_get_purgeable_stats.cold.1
+ _objc_msgSend$_fp_relationshipToItemAtURL:bothAreRealpaths:
+ _objc_msgSend$fp_fpfsProviderDomainID:skipTypeCheck:error:
+ _objc_msgSend$initWithOverrides:url:noSuitableModuleFoundHandler:
+ _objc_msgSend$newIteratorForURL:withNotFoundHandler:
- ___101-[FPXExtensionContext fetchDefaultContainerForBundleIdentifier:defaultName:inDomainIdentifier:reply:]_block_invoke.526
- ___101-[FPXExtensionContext fetchDefaultContainerForBundleIdentifier:defaultName:inDomainIdentifier:reply:]_block_invoke_2.530
- ___103-[FPXExtensionContext modifyItem:baseVersion:changedFields:contents:options:request:completionHandler:]_block_invoke.277
- ___110-[FPXExtensionContext URLForItemID:creatingPlaceholderIfMissing:ignoreAlternateContentsURL:completionHandler:]_block_invoke.325
- ___110-[FPXExtensionContext URLForItemID:creatingPlaceholderIfMissing:ignoreAlternateContentsURL:completionHandler:]_block_invoke.325.cold.1
- ___120-[FPXExtensionContext _createItemBasedOnTemplate:fields:contents:options:request:bounce:bounceNumber:completionHandler:]_block_invoke.513
- ___120-[FPXExtensionContext _createItemBasedOnTemplate:fields:contents:options:request:bounce:bounceNumber:completionHandler:]_block_invoke.513.cold.1
- ___120-[FPXExtensionContext _createItemBasedOnTemplate:fields:contents:options:request:bounce:bounceNumber:completionHandler:]_block_invoke.513.cold.2
- ___120-[FPXExtensionContext _createItemBasedOnTemplate:fields:contents:options:request:bounce:bounceNumber:completionHandler:]_block_invoke.513.cold.3
- ___120-[FPXExtensionContext _createItemBasedOnTemplate:fields:contents:options:request:bounce:bounceNumber:completionHandler:]_block_invoke.513.cold.4
- ___120-[FPXExtensionContext _createItemBasedOnTemplate:fields:contents:options:request:bounce:bounceNumber:completionHandler:]_block_invoke.513.cold.5
- ___120-[FPXExtensionContext _createItemBasedOnTemplate:fields:contents:options:request:bounce:bounceNumber:completionHandler:]_block_invoke.513.cold.6
- ___120-[FPXExtensionContext _createItemBasedOnTemplate:fields:contents:options:request:bounce:bounceNumber:completionHandler:]_block_invoke.517
- ___137-[FPXExtensionContext fetchContentsForItemWithID:version:request:estimatedItemSize:isSymlink:extent:alignment:options:completionHandler:]_block_invoke.253
- ___137-[FPXExtensionContext fetchContentsForItemWithID:version:request:estimatedItemSize:isSymlink:extent:alignment:options:completionHandler:]_block_invoke_2.261
- ___155-[FPXExtensionContext fetchContentsForItemWithID:version:usingExistingContentsAtURL:existingVersion:request:estimatedItemSize:isSymlink:completionHandler:]_block_invoke.270
- ___155-[FPXExtensionContext fetchContentsForItemWithID:version:usingExistingContentsAtURL:existingVersion:request:estimatedItemSize:isSymlink:completionHandler:]_block_invoke.271
- ___52-[FPXExtensionContext itemForURL:completionHandler:]_block_invoke.320
- ___56-[FPXExtensionContext trashItemAtURL:completionHandler:]_block_invoke.329
- ___56-[FPXExtensionContext trashItemAtURL:completionHandler:]_block_invoke.333
- ___56-[FPXExtensionContext trashItemAtURL:completionHandler:]_block_invoke.334
- ___56-[FPXExtensionContext trashItemAtURL:completionHandler:]_block_invoke.334.cold.1
- ___56-[FPXExtensionContext trashItemAtURL:completionHandler:]_block_invoke.335
- ___63-[FPXExtensionContext preflightTrashItemIDs:completionHandler:]_block_invoke.301
- ___65-[FPXExtensionContext providePlaceholderAtURL:completionHandler:]_block_invoke.307
- ___65-[FPXExtensionContext waitForStabilizationWithCompletionHandler:]_block_invoke.599
- ___66-[FPXExtensionContext fetchTrashIdentifiersWithCompletionHandler:]_block_invoke.586
- ___66-[FPXExtensionContext wakeForSessionIdentifier:completionHandler:]_block_invoke.546
- ___66-[FPXExtensionContext wakeForSessionIdentifier:completionHandler:]_block_invoke.546.cold.1
- ___67-[FPPendingSetEnumerator enumerateItemsForObserver:startingAtPage:]_block_invoke.436
- ___67-[FPXExtensionContext bulkEvictItemsWithItemIDs:completionHandler:]_block_invoke.547
- ___67-[FPXExtensionContext bulkEvictItemsWithItemIDs:completionHandler:]_block_invoke.549
- ___68-[FPXExtensionContext preflightReparentItemIDs:underParentID:reply:]_block_invoke.482
- ___69-[FPPendingSetEnumerator enumerateChangesForObserver:fromSyncAnchor:]_block_invoke.440
- ___69-[FPPendingSetEnumerator enumerateChangesForObserver:fromSyncAnchor:]_block_invoke_2.443
- ___69-[FPXExtensionContext deleteItemsWithIDs:baseVersions:options:reply:]_block_invoke.501
- ___69-[FPXExtensionContext deleteItemsWithIDs:baseVersions:options:reply:]_block_invoke.501.cold.1
- ___69-[FPXExtensionContext deleteItemsWithIDs:baseVersions:options:reply:]_block_invoke.507
- ___78-[FPXExtensionContext attemptRecoveryFromError:optionIndex:completionHandler:]_block_invoke.552
- ___80-[FPXExtensionContext startProvidingItemAtURL:readingOptions:completionHandler:]_block_invoke.191
- ___80-[FPXExtensionContext startProvidingItemAtURL:readingOptions:completionHandler:]_block_invoke.191.cold.1
- ___80-[FPXExtensionContext startProvidingItemAtURL:readingOptions:completionHandler:]_block_invoke.191.cold.2
- ___87-[FPXExtensionContext fetchServicesForItemID:allowRestrictedSources:completionHandler:]_block_invoke.465
- ___93-[FPXExtensionContext startOperation:toFetchThumbnailsWithDictionary:size:completionHandler:]_block_invoke.397
- ___93-[FPXExtensionContext startOperation:toFetchThumbnailsWithDictionary:size:completionHandler:]_block_invoke.397.cold.1
- ___93-[FPXExtensionContext startOperation:toFetchThumbnailsWithDictionary:size:completionHandler:]_block_invoke.410
- ___93-[FPXExtensionContext startOperation:toFetchThumbnailsWithDictionary:size:completionHandler:]_block_invoke.410.cold.1
- ___93-[FPXExtensionContext startOperation:toFetchThumbnailsWithDictionary:size:completionHandler:]_block_invoke.412
- ___94-[FPXExtensionContext didUpdateAlternateContentsDocumentForDocumentWithURL:completionHandler:]_block_invoke.309
- ___95-[FPXExtensionContext fetchAndStartEnumeratingWithSettings:observer:request:completionHandler:]_block_invoke.441
- ___97-[FPXExtensionContext startOperation:toFetchThumbnailsForItemIdentifiers:size:completionHandler:]_block_invoke.347
- ___97-[FPXExtensionContext startOperation:toFetchThumbnailsForItemIdentifiers:size:completionHandler:]_block_invoke.366
- ___97-[FPXExtensionContext startOperation:toFetchThumbnailsForItemIdentifiers:size:completionHandler:]_block_invoke.366.cold.1
- ___97-[FPXExtensionContext startOperation:toFetchThumbnailsForItemIdentifiers:size:completionHandler:]_block_invoke.368
- ___97-[FPXExtensionContext startOperation:toFetchThumbnailsForItemIdentifiers:size:completionHandler:]_block_invoke_2.370
- ___97-[FPXExtensionContext startOperation:toFetchThumbnailsForItemIdentifiers:size:completionHandler:]_block_invoke_2.370.cold.1
- ___block_descriptor_56_e8_32s40bs_e30_v24?0"NSString"8"NSError"16ls32l8s40l8
- ___block_literal_global.152
- ___block_literal_global.157
- ___block_literal_global.258
- ___block_literal_global.264
- ___block_literal_global.350
- ___block_literal_global.409
- ___block_literal_global.415
- ___block_literal_global.417
- ___block_literal_global.438
- ___block_literal_global.444
- ___block_literal_global.445
- ___block_literal_global.468
- ___block_literal_global.493
- ___block_literal_global.597
- ___block_literal_global.627
- _objc_msgSend$initWithOverrides:noSuitableModuleFoundHandler:
CStrings:
+ "\x01\x11\x11"
+ "1835.120.53"
+ "@32@0:8B16B20^@24"
+ "@32@0:8^{__CFURL=}16@?24"
+ "@40@0:8@16^{__CFURL=}24@?32"
+ "A\xc3"
+ "C"
+ "Couldn't get detailed purgeable stats for %llu, errno %{errno}d"
+ "Invalid value for %@: expected %@, actual %@"
+ "Sent to wrong instance, itemID=%@, domainContext.domain=%@"
+ "TQ,N,V_xpcActivityTimeSinceLastAbleToRun"
+ "[CRIT] Called addDomain with an invalid persona; actual persona was %@, expected %@. Caller persona was %@."
+ "[CRIT] Persona transmission failed. Caller persona was %@, fileproviderd received %@."
+ "[DEBUG] New iterator for checked URL (%@in FP)"
+ "_checkURL"
+ "_fp_relationshipToItemAtURL:bothAreRealpaths:"
+ "_mightBeFPURL"
+ "_xpcActivityTimeSinceLastAbleToRun"
+ "actual"
+ "expected"
+ "fp_fpfsProviderDomainID:skipTypeCheck:error:"
+ "fp_realPathRelationshipToItemAtRealPathURL:"
+ "initWithOverrides:url:noSuitableModuleFoundHandler:"
+ "newIteratorForURL:withNotFoundHandler:"
+ "not "
+ "parameter"
+ "q28@0:8@16B24"
+ "setXpcActivityTimeSinceLastAbleToRun:"
+ "xpcActivityTimeSinceLastAbleToRun"
- "1835.102.2"
- "A\xb3"

```
