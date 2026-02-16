## WebBookmarks

> `/System/Library/PrivateFrameworks/WebBookmarks.framework/WebBookmarks`

```diff

-623.2.7.10.4
-  __TEXT.__text: 0x9f84c
-  __TEXT.__auth_stubs: 0xed0
-  __TEXT.__objc_methlist: 0x8214
+624.1.11.10.3
+  __TEXT.__text: 0xa62f4
+  __TEXT.__auth_stubs: 0xe80
+  __TEXT.__objc_methlist: 0x830c
   __TEXT.__const: 0x326
-  __TEXT.__gcc_except_tab: 0xb6a4
-  __TEXT.__cstring: 0xe22c
-  __TEXT.__oslogstring: 0x8d8d
+  __TEXT.__gcc_except_tab: 0xbacc
+  __TEXT.__cstring: 0xe76d
+  __TEXT.__oslogstring: 0x94d7
   __TEXT.__dlopen_cstrs: 0xb2
   __TEXT.__constg_swiftt: 0x60
   __TEXT.__swift5_typeref: 0x9
   __TEXT.__swift5_reflstr: 0x1c
   __TEXT.__swift5_fieldmd: 0x1c
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x4260
-  __TEXT.__objc_classname: 0x988
-  __TEXT.__objc_methname: 0x15ab1
-  __TEXT.__objc_methtype: 0x26ca
-  __TEXT.__objc_stubs: 0xea40
+  __TEXT.__unwind_info: 0x42c0
+  __TEXT.__objc_classname: 0x9c8
+  __TEXT.__objc_methname: 0x1617e
+  __TEXT.__objc_methtype: 0x2734
+  __TEXT.__objc_stubs: 0xec00
   __DATA_CONST.__got: 0x798
-  __DATA_CONST.__const: 0x2e80
+  __DATA_CONST.__const: 0x2ed0
   __DATA_CONST.__objc_classlist: 0x218
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x100
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4cb8
+  __DATA_CONST.__objc_selrefs: 0x4d68
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x1c8
   __DATA_CONST.__objc_arraydata: 0x350
-  __AUTH_CONST.__auth_got: 0x780
+  __AUTH_CONST.__auth_got: 0x758
   __AUTH_CONST.__const: 0x1000
-  __AUTH_CONST.__cfstring: 0x5e60
-  __AUTH_CONST.__objc_const: 0x9690
+  __AUTH_CONST.__cfstring: 0x5ee0
+  __AUTH_CONST.__objc_const: 0x9820
   __AUTH_CONST.__objc_intobj: 0x360
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_arrayobj: 0xd8
   __AUTH.__objc_data: 0x50
   __AUTH.__data: 0xb8
-  __DATA.__objc_ivar: 0x5cc
-  __DATA.__data: 0xf48
-  __DATA.__bss: 0xbc
+  __DATA.__objc_ivar: 0x5f4
+  __DATA.__data: 0x1010
+  __DATA.__bss: 0x8c
   __DATA_DIRTY.__objc_data: 0x1450
   __DATA_DIRTY.__data: 0x10
-  __DATA_DIRTY.__bss: 0x1d0
+  __DATA_DIRTY.__bss: 0x200
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreImage.framework/CoreImage

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 89BDB078-4197-32AD-8B92-A1A72B3A370C
-  Functions: 3492
-  Symbols:   12007
-  CStrings:  6326
+  UUID: C622D185-E84A-393A-ACDF-EDD63A191118
+  Functions: 3540
+  Symbols:   12209
+  CStrings:  6426
 
Symbols:
+ +[WBDeviceParameters localDeviceWithTitle:creationDeviceIdentifier:deviceIdentifier:]
+ +[WBDeviceParameters remoteDeviceWithTitle:deviceIdentifier:]
+ +[WBMutableTabGroup unnamedTabGroupWithDeviceIdentifier:]
+ +[WBMutableTabGroup unnamedTabGroupWithUUID:profileIdentifier:deviceIdentifier:]
+ +[WBTab pinnedTabWithTitle:url:deviceIdentifier:]
+ +[WBTab startPageTabWithDeviceIdentifier:]
+ +[WebBookmarkCollection maintainsSyncMetadata]
+ +[WebBookmarkTabCollection maintainsSyncMetadata]
+ +[WebBookmarkTitleWordTokenizer test_cjkIdeographCharacterSet]
+ -[WBDeviceParameters deviceIdentifier]
+ -[WBDeviceParameters setDeviceIdentifier:]
+ -[WBMutableTabGroup initWithTitle:deviceIdentifier:profileIdentifier:]
+ -[WBProfile deviceIdentifier]
+ -[WBProfile initWithTitle:deviceIdentifier:]
+ -[WBProfile initWithTitle:symbolImageName:favoritesFolderServerID:deviceIdentifier:]
+ -[WBTab deviceIdentifier]
+ -[WBTab initWithTitle:url:deviceIdentifier:]
+ -[WBTab initWithUUID:deviceIdentifier:]
+ -[WBTab initWithUUID:deviceIdentifier:lastVisitTime:]
+ -[WBTab initWithUUID:title:url:deviceIdentifier:]
+ -[WBTab initWithUUID:title:url:deviceIdentifier:isPrivateBrowsing:]
+ -[WBTab initWithUUID:title:url:deviceIdentifier:lastVisitTime:]
+ -[WBTab initWithUUID:title:url:pinned:pinnedTitle:pinnedURL:localAttributes:deviceIdentifier:]
+ -[WBTabGroup deviceIdentifier]
+ -[WBTabGroup initWithDeviceIdentifier:]
+ -[WBTabGroup initWithTitle:deviceIdentifier:]
+ -[WBTabGroup initWithTitle:uuid:deviceIdentifier:]
+ -[WBTabGroupManager uncacheTabGroup:]
+ -[WBWindowState localOrUnnamedTabGroupForRestoration:inProfileWithIdentifier:deviceIdentifier:]
+ -[WebBookmark deviceIdentifier]
+ -[WebBookmark initFolderWithParentID:deviceIdentifier:collectionType:]
+ -[WebBookmark initFolderWithParentID:subtype:deviceIdentifier:collectionType:]
+ -[WebBookmark initWithTitle:address:parentID:deviceIdentifier:collectionType:]
+ -[WebBookmark initWithTitle:address:parentID:folder:deviceIdentifier:collectionType:]
+ -[WebBookmark initWithTitle:address:parentID:subtype:deviceIdentifier:collectionType:]
+ -[WebBookmark initWithTitle:address:parentID:subtype:deviceIdentifier:collectionType:score:]
+ -[WebBookmark setDeviceIdentifier:]
+ -[WebBookmark syncStateGeneration]
+ -[WebBookmark(Internal) initWithSQLiteStatement:deviceIdentifier:collectionType:]
+ -[WebBookmark(Internal) initWithSQLiteStatement:deviceIdentifier:collectionType:skipDecodingSyncData:]
+ -[WebBookmark(Internal) initWithSQLiteStatement:deviceIdentifier:hasIcon:collectionType:skipDecodingSyncData:]
+ -[WebBookmark(Internal) initWithSQLiteStatement:deviceIdentifier:hasIcon:collectionType:skipDecodingSyncData:].cold.1
+ -[WebBookmark(Internal) initWithSQLiteStatement:deviceIdentifier:hasIcon:collectionType:skipDecodingSyncData:].cold.2
+ -[WebBookmarkCollection _archivedDataWithRootObject:]
+ -[WebBookmarkCollection _enumerateContentsOfBookmarkFolder:includingSubfolders:includeHidden:usingBlock:]
+ -[WebBookmarkCollection _migrateSchemaVersion61ToVersion62]
+ -[WebBookmarkCollection _privacyPreservingDescriptionForMostRecentSQLiteError]
+ -[WebBookmarkCollection _saveAndMoveBookmark:toFolderID:].cold.1
+ -[WebBookmarkCollection _unarchivedObjectOfClass:fromData:]
+ -[WebBookmarkCollection enumerateDescendantsOfBookmarkID:includeHidden:usingBlock:]
+ -[WebBookmarkCollection expectedOrderIndexOfSpecialID:]
+ -[WebBookmarkCollection interruptDatabase]
+ -[WebBookmarkCollection interruptDatabase].cold.1
+ -[WebBookmarkCollection performDatabaseUpdatesWithTransaction:applyInMemoryChanges:secureDelete:].cold.1
+ -[WebBookmarkCollection(Sync) clearAllLocalBookmarksForAutomatedTesting]
+ -[WebBookmarkCollection(Sync) performDeduplicationWithMode:]
+ -[WebBookmarksSettingsGateway _exportBookmarkWithMessage:connection:]
+ -[WebBookmarksSettingsGateway _exportHistoryWithMessage:connection:]
+ -[WebBookmarksSettingsGateway _exportReadingListWithMessage:connection:]
+ -[WebBookmarksSettingsGateway _finishedBookmarksExportWithMessage:connection:]
+ -[WebBookmarksSettingsGateway _finishedHistoryExportWithMessage:connection:]
+ -[WebBookmarksSettingsGateway _finishedReadingListExportWithMessage:connection:]
+ -[WebBookmarksSettingsGateway exportBookmarksWithBlock:completionHandler:]
+ -[WebBookmarksSettingsGateway exportHistoryWithBlock:completionHandler:]
+ -[WebBookmarksSettingsGateway exportReadingListToURL:sandboxExtension:completionHandler:]
+ -[WebBookmarksSettingsGateway exportReadingListWithBlock:completionHandler:]
+ -[WebBookmarksSettingsGateway importBookmarksFromURL:completionHandler:]
+ -[WebBookmarksSettingsGateway importBookmarksFromURL:completionHandler:].cold.1
+ GCC_except_table189
+ GCC_except_table215
+ GCC_except_table235
+ GCC_except_table249
+ GCC_except_table25
+ GCC_except_table278
+ GCC_except_table279
+ GCC_except_table293
+ GCC_except_table298
+ GCC_except_table304
+ GCC_except_table321
+ GCC_except_table325
+ GCC_except_table331
+ GCC_except_table332
+ GCC_except_table337
+ GCC_except_table339
+ GCC_except_table341
+ GCC_except_table342
+ GCC_except_table345
+ GCC_except_table347
+ GCC_except_table348
+ GCC_except_table368
+ GCC_except_table373
+ GCC_except_table382
+ GCC_except_table386
+ GCC_except_table387
+ GCC_except_table388
+ GCC_except_table389
+ GCC_except_table393
+ GCC_except_table403
+ GCC_except_table404
+ GCC_except_table406
+ GCC_except_table407
+ GCC_except_table408
+ GCC_except_table421
+ GCC_except_table425
+ GCC_except_table426
+ GCC_except_table427
+ GCC_except_table430
+ GCC_except_table432
+ GCC_except_table435
+ GCC_except_table455
+ GCC_except_table457
+ GCC_except_table461
+ GCC_except_table472
+ GCC_except_table476
+ GCC_except_table477
+ GCC_except_table478
+ GCC_except_table491
+ GCC_except_table510
+ GCC_except_table512
+ GCC_except_table513
+ GCC_except_table518
+ GCC_except_table523
+ GCC_except_table542
+ GCC_except_table543
+ GCC_except_table544
+ GCC_except_table545
+ GCC_except_table546
+ GCC_except_table547
+ GCC_except_table549
+ GCC_except_table550
+ GCC_except_table551
+ GCC_except_table552
+ GCC_except_table559
+ GCC_except_table566
+ GCC_except_table567
+ _OBJC_IVAR_$_WBDeviceParameters._deviceIdentifier
+ _OBJC_IVAR_$_WebBookmark._deviceIdentifier
+ _OBJC_IVAR_$_WebBookmarkCollection._transactionRevertBlocks
+ _OBJC_IVAR_$_WebBookmarksSettingsGateway._exportBookmarksBlock
+ _OBJC_IVAR_$_WebBookmarksSettingsGateway._exportBookmarksCompletionHandler
+ _OBJC_IVAR_$_WebBookmarksSettingsGateway._exportHistoryBlock
+ _OBJC_IVAR_$_WebBookmarksSettingsGateway._exportHistoryCompletionHandler
+ _OBJC_IVAR_$_WebBookmarksSettingsGateway._exportReadingListBlock
+ _OBJC_IVAR_$_WebBookmarksSettingsGateway._exportReadingListCompletionHandler
+ _OBJC_IVAR_$_WebBookmarksXPCConnection._connectionLock
+ _OUTLINED_FUNCTION_13
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_15
+ _OUTLINED_FUNCTION_16
+ _OUTLINED_FUNCTION_17
+ __ZL36deviceIdentifierKeyForCollectionType16WBCollectionType
+ ___139-[WebBookmarkCollection _moveBookmark:toFolderWithID:orderIndex:detectCycles:incrementGeneration:shouldMerge:generateSyncPositionIfNeeded:]_block_invoke
+ ___182-[WebBookmarkCollection _addBookmarkWithTitle:address:parentID:orderIndex:isFolder:externalUUID:associatedBookmark:updateParentChildCount:updateAncestorEntries:incrementGenerations:]_block_invoke
+ ___35-[WebBookmark setDeviceIdentifier:]_block_invoke
+ ___47-[WebBookmarksSettingsGateway _setupConnection]_block_invoke_10
+ ___47-[WebBookmarksSettingsGateway _setupConnection]_block_invoke_5
+ ___47-[WebBookmarksSettingsGateway _setupConnection]_block_invoke_6
+ ___47-[WebBookmarksSettingsGateway _setupConnection]_block_invoke_7
+ ___47-[WebBookmarksSettingsGateway _setupConnection]_block_invoke_8
+ ___47-[WebBookmarksSettingsGateway _setupConnection]_block_invoke_9
+ ___57-[WebBookmarkCollection _updateBookmarks:inFolderWithID:]_block_invoke.428
+ ___57-[WebBookmarkCollection _updateBookmarks:inFolderWithID:]_block_invoke.430
+ ___57-[WebBookmarkCollection _updateBookmarks:inFolderWithID:]_block_invoke.430.cold.1
+ ___57-[WebBookmarkCollection _updateBookmarks:inFolderWithID:]_block_invoke.430.cold.2
+ ___57-[WebBookmarkCollection _updateBookmarks:inFolderWithID:]_block_invoke.430.cold.3
+ ___57-[WebBookmarkCollection _updateBookmarks:inFolderWithID:]_block_invoke.430.cold.4
+ ___57-[WebBookmarkCollection _updateBookmarks:inFolderWithID:]_block_invoke.432
+ ___57-[WebBookmarkCollection _updateBookmarks:inFolderWithID:]_block_invoke_2.431
+ ___59-[WebBookmarkCollection _migrateSchemaVersion61ToVersion62]_block_invoke
+ ___62-[WebBookmarkCollection updateSyncDataForBookmark:usingBlock:]_block_invoke
+ ___64-[WBTabCyclerCommandHandler syncBookmarksWithCompletionHandler:]_block_invoke.40
+ ___70-[WBTabCyclerCommandHandler _clearLocalProfilesWithCompletionHandler:]_block_invoke_2
+ ___71-[WBTabCyclerCommandHandler _clearRemoteProfilesWithCompletionHandler:]_block_invoke.26
+ ___72-[WebBookmarksSettingsGateway importBookmarksFromURL:completionHandler:]_block_invoke
+ ___72-[WebBookmarksSettingsGateway importBookmarksFromURL:completionHandler:]_block_invoke.cold.1
+ ___77-[WBTabCyclerCommandHandler _startMonitoringSyncStatusWithCompletionHandler:]_block_invoke.43
+ ___78-[WebBookmarkCollection _saveBookmark:withSpecialID:updateGenerationIfNeeded:]_block_invoke.848
+ ___79-[WebBookmarkCollection _reorderBookmark:toIndex:generateSyncPositionIfNeeded:]_block_invoke
+ ___89-[WebBookmarksSettingsGateway exportReadingListToURL:sandboxExtension:completionHandler:]_block_invoke
+ ___89-[WebBookmarksSettingsGateway exportReadingListToURL:sandboxExtension:completionHandler:]_block_invoke.cold.1
+ ___97-[WebBookmarkCollection performDatabaseUpdatesWithTransaction:applyInMemoryChanges:secureDelete:]_block_invoke
+ ___Block_byref_object_copy_.1914
+ ___Block_byref_object_dispose_.1915
+ ____ZL33prefixEndingWithFirstWordOfStringP8NSString_block_invoke.1917
+ ___block_descriptor_32_e21_v32?0?<v?>8Q16^B24l
+ ___block_descriptor_52_ea8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_56_ea8_32s40r_e5_v8?0ls32l8r40l8
+ ___block_descriptor_56_ea8_32s40s48bs_e5_B8?0ls48l8s32l8s40l8
+ ___block_descriptor_56_ea8_32s40s48s_e24_B24?0"WebBookmark"8q16ls32l8s40l8s48l8
+ ___block_descriptor_65_ea8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ ___block_literal_global.1036
+ ___block_literal_global.1082
+ ___block_literal_global.1157
+ ___block_literal_global.1159
+ ___block_literal_global.168
+ ___block_literal_global.1906
+ ___block_literal_global.1919
+ ___block_literal_global.1933
+ ___block_literal_global.201
+ ___block_literal_global.215
+ ___block_literal_global.291
+ ___block_literal_global.293
+ ___block_literal_global.301
+ ___block_literal_global.303
+ ___block_literal_global.307
+ ___block_literal_global.311
+ ___block_literal_global.313
+ ___block_literal_global.321
+ ___block_literal_global.474
+ _cjkIdeographCharacterSet
+ _cjkIdeographCharacterSet.cold.1
+ _kWebBookmarksBrowserDataExchangeBookmarksExportFinishedMessageName
+ _kWebBookmarksBrowserDataExchangeExportBookmarksFolderIdentifierKey
+ _kWebBookmarksBrowserDataExchangeExportBookmarksIdentifierKey
+ _kWebBookmarksBrowserDataExchangeExportBookmarksIsFolderKey
+ _kWebBookmarksBrowserDataExchangeExportBookmarksMessageName
+ _kWebBookmarksBrowserDataExchangeExportBookmarksTitleKey
+ _kWebBookmarksBrowserDataExchangeExportBookmarksURLStringKey
+ _kWebBookmarksBrowserDataExchangeExportHistoryHttpGetKey
+ _kWebBookmarksBrowserDataExchangeExportHistoryLoadSuccessfulKey
+ _kWebBookmarksBrowserDataExchangeExportHistoryMessageName
+ _kWebBookmarksBrowserDataExchangeExportHistoryRedirectDestinationURLStringKey
+ _kWebBookmarksBrowserDataExchangeExportHistoryRedirectDestinationVisitTimeKey
+ _kWebBookmarksBrowserDataExchangeExportHistoryRedirectSourceURLStringKey
+ _kWebBookmarksBrowserDataExchangeExportHistoryRedirectSourceVisitTimeKey
+ _kWebBookmarksBrowserDataExchangeExportHistoryTitleKey
+ _kWebBookmarksBrowserDataExchangeExportHistoryURLStringKey
+ _kWebBookmarksBrowserDataExchangeExportHistoryVisitCountKey
+ _kWebBookmarksBrowserDataExchangeExportHistoryVisitTimeKey
+ _kWebBookmarksBrowserDataExchangeExportReadingListDateOfLastVisitKey
+ _kWebBookmarksBrowserDataExchangeExportReadingListMessageName
+ _kWebBookmarksBrowserDataExchangeExportReadingListTitleKey
+ _kWebBookmarksBrowserDataExchangeExportReadingListURLStringKey
+ _kWebBookmarksBrowserDataExchangeHistoryExportFinishedMessageName
+ _kWebBookmarksBrowserDataExchangeReadingListExportFinishedMessageName
+ _kWebBookmarksExportReadingListMessageName
+ _kWebBookmarksExportReadingListSandboxExtensionKey
+ _kWebBookmarksExportReadingListURLKey
+ _objc_msgSend$_enumerateContentsOfBookmarkFolder:includingSubfolders:includeHidden:usingBlock:
+ _objc_msgSend$_exportBookmarkWithMessage:connection:
+ _objc_msgSend$_exportHistoryWithMessage:connection:
+ _objc_msgSend$_exportReadingListWithMessage:connection:
+ _objc_msgSend$_finishedBookmarksExportWithMessage:connection:
+ _objc_msgSend$_finishedHistoryExportWithMessage:connection:
+ _objc_msgSend$_finishedReadingListExportWithMessage:connection:
+ _objc_msgSend$_migrateSchemaVersion61ToVersion62
+ _objc_msgSend$_privacyPreservingDescriptionForMostRecentSQLiteError
+ _objc_msgSend$clearAllLocalBookmarksForAutomatedTesting
+ _objc_msgSend$enumerateDescendantsOfBookmarkID:includeHidden:usingBlock:
+ _objc_msgSend$enumerateObjectsWithOptions:usingBlock:
+ _objc_msgSend$initFolderWithParentID:deviceIdentifier:collectionType:
+ _objc_msgSend$initFolderWithParentID:subtype:deviceIdentifier:collectionType:
+ _objc_msgSend$initWithDeviceIdentifier:
+ _objc_msgSend$initWithSQLiteStatement:deviceIdentifier:collectionType:
+ _objc_msgSend$initWithSQLiteStatement:deviceIdentifier:collectionType:skipDecodingSyncData:
+ _objc_msgSend$initWithSQLiteStatement:deviceIdentifier:hasIcon:collectionType:skipDecodingSyncData:
+ _objc_msgSend$initWithTitle:address:parentID:deviceIdentifier:collectionType:
+ _objc_msgSend$initWithTitle:address:parentID:folder:deviceIdentifier:collectionType:
+ _objc_msgSend$initWithTitle:address:parentID:subtype:deviceIdentifier:collectionType:
+ _objc_msgSend$initWithTitle:deviceIdentifier:
+ _objc_msgSend$initWithTitle:symbolImageName:favoritesFolderServerID:deviceIdentifier:
+ _objc_msgSend$initWithTitle:url:deviceIdentifier:
+ _objc_msgSend$initWithTitle:uuid:deviceIdentifier:
+ _objc_msgSend$initWithUUID:deviceIdentifier:
+ _objc_msgSend$initWithUUID:title:url:deviceIdentifier:
+ _objc_msgSend$initWithUUID:title:url:deviceIdentifier:lastVisitTime:
+ _objc_msgSend$initWithUUID:title:url:pinned:pinnedTitle:pinnedURL:localAttributes:deviceIdentifier:
+ _objc_msgSend$initWithValue:generation:deviceIdentifier:
+ _objc_msgSend$initWithValueSource:valueProvider:valueUpdater:generation:deviceIdentifier:
+ _objc_msgSend$interruptDatabase
+ _objc_msgSend$localDeviceWithTitle:creationDeviceIdentifier:deviceIdentifier:
+ _objc_msgSend$localOrUnnamedTabGroupForRestoration:inProfileWithIdentifier:deviceIdentifier:
+ _objc_msgSend$performDeduplicationWithMode:
+ _objc_msgSend$positionBetweenPosition:andPosition:
+ _objc_msgSend$processName
+ _objc_msgSend$reportDatabaseTransactionFailureWithProcessName:revertedChangesCount:stacktrace:sqliteError:
+ _objc_msgSend$safari_safariApplicationPlatformBundleIdentifier
+ _objc_msgSend$setDeviceIdentifier:
+ _objc_msgSend$startPageTabWithDeviceIdentifier:
+ _objc_msgSend$unarchivedObjectOfClass:fromData:error:
+ _objc_msgSend$uncacheTabGroup:
+ _objc_msgSend$unnamedTabGroupWithUUID:profileIdentifier:deviceIdentifier:
- +[WBDeviceParameters localDeviceWithTitle:creationDeviceIdentifier:]
- +[WBDeviceParameters remoteDeviceWithTitle:]
- +[WBMutableTabGroup unnamedTabGroupWithUUID:profileIdentifier:]
- +[WBMutableTabGroup unnamedTabGroup]
- +[WBTab pinnedTabWithTitle:url:]
- +[WBTab startPageTab]
- +[WebBookmarkTabCollection isLockedSync]
- +[WebBookmarkTabCollection lockSync]
- +[WebBookmarkTabCollection unlockSync]
- -[WBMutableTabGroup initWithTitle:profileIdentifier:]
- -[WBProfile initWithTitle:]
- -[WBProfile initWithTitle:symbolImageName:favoritesFolderServerID:]
- -[WBTab initWithTitle:url:]
- -[WBTab initWithUUID:]
- -[WBTab initWithUUID:lastVisitTime:]
- -[WBTab initWithUUID:title:url:]
- -[WBTab initWithUUID:title:url:isPrivateBrowsing:]
- -[WBTab initWithUUID:title:url:lastVisitTime:]
- -[WBTab initWithUUID:title:url:pinned:pinnedTitle:pinnedURL:localAttributes:]
- -[WBTabGroup initWithTitle:]
- -[WBTabGroup initWithTitle:uuid:]
- -[WBTabGroupManager _nextInMemoryPositionChangeID]
- -[WBTabGroupManager _uncacheTabGroup:]
- -[WBTabGroupManager deviceIdentifierForPositionGenerator:]
- -[WBTabGroupManager nextChangeIDForPositionInPositionGenerator:]
- -[WBWindowState localOrUnnamedTabGroupForRestoration:inProfileWithIdentifier:]
- -[WebBookmark initFolderWithParentID:subtype:collectionType:]
- -[WebBookmark initWithTitle:address:parentID:folder:collectionType:]
- -[WebBookmark initWithTitle:address:parentID:subtype:collectionType:]
- -[WebBookmark initWithTitle:address:parentID:subtype:collectionType:score:]
- -[WebBookmark(Internal) initWithSQLiteStatement:collectionType:]
- -[WebBookmark(Internal) initWithSQLiteStatement:collectionType:skipDecodingSyncData:]
- -[WebBookmark(Internal) initWithSQLiteStatement:hasIcon:collectionType:skipDecodingSyncData:]
- -[WebBookmark(Internal) initWithSQLiteStatement:hasIcon:collectionType:skipDecodingSyncData:].cold.1
- -[WebBookmark(Internal) initWithSQLiteStatement:hasIcon:collectionType:skipDecodingSyncData:].cold.2
- -[WebBookmarkCollection _enumerateContentsOfBookmarkFolder:includingSubfolders:usingBlock:]
- -[WebBookmarkCollection _interruptDatabase]
- -[WebBookmarkCollection _interruptDatabase].cold.1
- -[WebBookmarkCollection nextDatabaseSyncChangeID]
- -[WebBookmarkTabCollection _saveWindowState:].cold.6
- -[WebBookmarkTabCollection _windowStatesWithFilter:].cold.1
- -[WebBookmarkTabCollection _windowStatesWithFilter:].cold.2
- -[WebBookmarkTabCollection maintainsSyncMetadata]
- -[WebBookmarkTitleWordTokenizer advanceToNextToken].cold.1
- -[WebBookmarksSettingsGateway importBookmarksFromURL:inFolderWithSuggestedName:completionHandler:]
- -[WebBookmarksSettingsGateway importBookmarksFromURL:inFolderWithSuggestedName:completionHandler:].cold.1
- GCC_except_table113
- GCC_except_table135
- GCC_except_table161
- GCC_except_table254
- GCC_except_table265
- GCC_except_table297
- GCC_except_table300
- GCC_except_table301
- GCC_except_table302
- GCC_except_table303
- GCC_except_table315
- GCC_except_table320
- GCC_except_table333
- GCC_except_table343
- GCC_except_table349
- GCC_except_table351
- GCC_except_table356
- GCC_except_table357
- GCC_except_table359
- GCC_except_table360
- GCC_except_table365
- GCC_except_table366
- GCC_except_table380
- GCC_except_table394
- GCC_except_table397
- GCC_except_table398
- GCC_except_table401
- GCC_except_table411
- GCC_except_table412
- GCC_except_table415
- GCC_except_table416
- GCC_except_table417
- GCC_except_table418
- GCC_except_table419
- GCC_except_table420
- GCC_except_table437
- GCC_except_table438
- GCC_except_table442
- GCC_except_table444
- GCC_except_table445
- GCC_except_table447
- GCC_except_table451
- GCC_except_table467
- GCC_except_table469
- GCC_except_table484
- GCC_except_table485
- GCC_except_table488
- GCC_except_table489
- GCC_except_table490
- GCC_except_table504
- GCC_except_table522
- GCC_except_table524
- GCC_except_table525
- GCC_except_table534
- GCC_except_table537
- GCC_except_table555
- GCC_except_table556
- ___49-[WebBookmarkCollection nextDatabaseSyncChangeID]_block_invoke
- ___57-[WebBookmarkCollection _updateBookmarks:inFolderWithID:]_block_invoke.417
- ___57-[WebBookmarkCollection _updateBookmarks:inFolderWithID:]_block_invoke.419
- ___57-[WebBookmarkCollection _updateBookmarks:inFolderWithID:]_block_invoke.419.cold.1
- ___57-[WebBookmarkCollection _updateBookmarks:inFolderWithID:]_block_invoke.419.cold.2
- ___57-[WebBookmarkCollection _updateBookmarks:inFolderWithID:]_block_invoke.419.cold.3
- ___57-[WebBookmarkCollection _updateBookmarks:inFolderWithID:]_block_invoke.419.cold.4
- ___57-[WebBookmarkCollection _updateBookmarks:inFolderWithID:]_block_invoke_2.420
- ___60-[WebBookmarkCollection updateBookmarkSyncPositionIfNeeded:]_block_invoke_3
- ___60-[WebBookmarkCollection updateBookmarkSyncPositionIfNeeded:]_block_invoke_4
- ___64-[WBTabCyclerCommandHandler syncBookmarksWithCompletionHandler:]_block_invoke_2
- ___71-[WBTabCyclerCommandHandler _clearRemoteProfilesWithCompletionHandler:]_block_invoke_2
- ___77-[WBTabCyclerCommandHandler _startMonitoringSyncStatusWithCompletionHandler:]_block_invoke.40
- ___78-[WebBookmarkCollection _saveBookmark:withSpecialID:updateGenerationIfNeeded:]_block_invoke.835
- ___98-[WebBookmarksSettingsGateway importBookmarksFromURL:inFolderWithSuggestedName:completionHandler:]_block_invoke
- ___98-[WebBookmarksSettingsGateway importBookmarksFromURL:inFolderWithSuggestedName:completionHandler:]_block_invoke.cold.1
- ___Block_byref_object_copy_.1893
- ___Block_byref_object_dispose_.1894
- ____ZL33prefixEndingWithFirstWordOfStringP8NSString_block_invoke.1896
- ___block_descriptor_32_e34_B16?0"WBSCRDTPositionSortValue"8l
- ___block_descriptor_40_ea8_32r_e64_"WBBookmarkDatabaseSyncData"16?0"WBBookmarkDatabaseSyncData"8lr32l8
- ___block_descriptor_40_ea8_32s_e60_"WBSCRDTPositionSortValue"16?0"WBSCRDTPositionSortValue"8ls32l8
- ___block_descriptor_48_ea8_32s40s_e24_B24?0"WebBookmark"8q16ls32l8s40l8
- ___block_literal_global.1023
- ___block_literal_global.1066
- ___block_literal_global.1136
- ___block_literal_global.1146
- ___block_literal_global.1148
- ___block_literal_global.165
- ___block_literal_global.1885
- ___block_literal_global.1891
- ___block_literal_global.1898
- ___block_literal_global.199
- ___block_literal_global.212
- ___block_literal_global.285
- ___block_literal_global.290
- ___block_literal_global.292
- ___block_literal_global.300
- ___block_literal_global.302
- ___block_literal_global.310
- ___block_literal_global.312
- ___block_literal_global.462
- ___block_literal_global.684
- _inMemoryChangeIDLock
- _kWebBookmarksImportBookmarksSuggestedNameKey
- _nextInMemoryPositionChangeID
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$_enumerateContentsOfBookmarkFolder:includingSubfolders:usingBlock:
- _objc_msgSend$_interruptDatabase
- _objc_msgSend$_nextInMemoryPositionChangeID
- _objc_msgSend$_uncacheTabGroup:
- _objc_msgSend$changeID
- _objc_msgSend$initFolderWithParentID:subtype:collectionType:
- _objc_msgSend$initWithSQLiteStatement:collectionType:
- _objc_msgSend$initWithSQLiteStatement:collectionType:skipDecodingSyncData:
- _objc_msgSend$initWithSQLiteStatement:hasIcon:collectionType:skipDecodingSyncData:
- _objc_msgSend$initWithSortValues:
- _objc_msgSend$initWithTitle:
- _objc_msgSend$initWithTitle:address:parentID:folder:collectionType:
- _objc_msgSend$initWithTitle:address:parentID:subtype:collectionType:
- _objc_msgSend$initWithTitle:symbolImageName:favoritesFolderServerID:
- _objc_msgSend$initWithTitle:url:
- _objc_msgSend$initWithTitle:uuid:
- _objc_msgSend$initWithUUID:title:url:
- _objc_msgSend$initWithUUID:title:url:lastVisitTime:
- _objc_msgSend$initWithUUID:title:url:pinned:pinnedTitle:pinnedURL:localAttributes:
- _objc_msgSend$initWithValue:generation:
- _objc_msgSend$initWithValueSource:valueProvider:valueUpdater:generation:
- _objc_msgSend$localDeviceWithTitle:creationDeviceIdentifier:
- _objc_msgSend$localOrUnnamedTabGroupForRestoration:inProfileWithIdentifier:
- _objc_msgSend$nextChangeID
- _objc_msgSend$nextDatabaseSyncChangeID
- _objc_msgSend$positionBetweenPosition:andPosition:withDeviceIdentifier:changeID:
- _objc_msgSend$positionSortValueWithChangeID:
- _objc_msgSend$sortValues
- _objc_msgSend$startPageTab
- _objc_msgSend$unnamedTabGroupWithUUID:profileIdentifier:
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x5
- _objc_retain_x6
- _objc_retain_x7
CStrings:
+ "%@.Bookmarks"
+ "%@.TabGroups"
+ "(%@ %@) %@ %@ %@ %@ %@"
+ "@32@0:8#16@24"
+ "@36@0:8B16@20@28"
+ "@36@0:8i16@20q28"
+ "@40@0:8^{sqlite3_stmt=}16@24q32"
+ "@44@0:8^{sqlite3_stmt=}16@24q32B40"
+ "@44@0:8i16q20@28q36"
+ "@48@0:8^{sqlite3_stmt=}16@24B32q36B44"
+ "@52@0:8@16@24@32@40B48"
+ "@52@0:8@16@24i32@36q44"
+ "@56@0:8@16@24@32@40@48"
+ "@56@0:8@16@24i32B36@40q48"
+ "@60@0:8@16@24i32q36@44q52"
+ "@68@0:8@16@24i32q36@44q52@60"
+ "@76@0:8@16@24@32B40@44@52@60@68"
+ "AND deleted = 0"
+ "BrowserDataExchangeBookmarksExportFinished"
+ "BrowserDataExchangeExportBookmarks"
+ "BrowserDataExchangeExportBookmarksFolderIdentifier"
+ "BrowserDataExchangeExportBookmarksIdentifier"
+ "BrowserDataExchangeExportBookmarksIsFolder"
+ "BrowserDataExchangeExportBookmarksTitle"
+ "BrowserDataExchangeExportBookmarksURLString"
+ "BrowserDataExchangeExportHistory"
+ "BrowserDataExchangeExportHistoryHttpGet"
+ "BrowserDataExchangeExportHistoryLoadSuccessful"
+ "BrowserDataExchangeExportHistoryRedirectDestinationURLString"
+ "BrowserDataExchangeExportHistoryRedirectDestinationVisitTime"
+ "BrowserDataExchangeExportHistoryRedirectSourceURLString"
+ "BrowserDataExchangeExportHistoryRedirectSourceVisitTime"
+ "BrowserDataExchangeExportHistoryTitle"
+ "BrowserDataExchangeExportHistoryURLString"
+ "BrowserDataExchangeExportHistoryVisitCount"
+ "BrowserDataExchangeExportHistoryVisitTime"
+ "BrowserDataExchangeExportReadingList"
+ "BrowserDataExchangeExportReadingListDateOfLastVisit"
+ "BrowserDataExchangeExportReadingListTitle"
+ "BrowserDataExchangeExportReadingListURLString"
+ "BrowserDataExchangeHistoryExportFinished"
+ "BrowserDataExchangeReadingListExportFinished"
+ "CREATE UNIQUE INDEX database_properties_key_index ON database_properties (key)"
+ "Clearing local profiles and tab groups: %lu profiles, %lu tab groups"
+ "Clearing remote profiles and tab groups for validation"
+ "Could not save windowState: %{public}@ activeTabGroupID: <%d> localTabGroupID: <%d> privateTabGroupID: <%d> activeProfileID: <%d>"
+ "DELETE FROM database_properties WHERE rowid NOT IN (SELECT MIN(rowid) FROM database_properties GROUP BY key)"
+ "DROP INDEX database_properties_key_index"
+ "Error encountered while delivering XPC message to export reading list. Error: %{public}@"
+ "ExportReadingList"
+ "ExportReadingListSandboxExtension"
+ "ExportReadingListURL"
+ "Failed to move bookmark %d to folder %d (before save). SQLite error: %{public}@"
+ "Failed to move bookmark %d to folder %d at order index %d. SQLite error: %{public}@"
+ "Failed to save bookmark %d (specialID: %d). SQLite error: %{public}@"
+ "Failed to save bookmark %d after move (specialID: %d)"
+ "Fetching scoped bookmarks for tab group %{public}@ (%{public}@): found %zu scoped bookmarks"
+ "Has tab groups, starting tab group sync monitoring and triggering sync"
+ "I20@0:8i16"
+ "Initial tab group sync completed, starting migration monitoring"
+ "Inserting scoped bookmark %{public}@ (%{public}@) in tab group %{public}@ (%{public}@) at parent folder ID %d"
+ "No profiles or tab groups to clear, calling completion immediately"
+ "No tab groups found, clearing tab sync data and starting migration"
+ "PRAGMA user_version = 62"
+ "Received acknowledgement that XPC message was delivered to export reading list"
+ "Removing tab group: %@"
+ "Removing tab profile: %@"
+ "Reverting _addBookmarkWithTitle state for bookmark %{public}@: ID %d -> %d, orderIndex %d -> %d, isInserted %d -> %d"
+ "Reverting _moveBookmark state for bookmark %{public}@: parentID %d -> %d, orderIndex %d -> %d"
+ "Reverting _reorderBookmark state for bookmark %{public}@: orderIndex %d -> %d"
+ "Reverting _updateBookmarks state for bookmark %{public}@: orderIndex %d -> %d, anchor %{public}@: orderIndex %d -> %d"
+ "SELECT COUNT(*) FROM bookmarks WHERE special_id != 0 AND special_id < %u"
+ "Scoped bookmark: %{public}@ (%{public}@)"
+ "Skipped window state from DB due to missing tab group. windowID: %d, UUID: %{public}@"
+ "Starting tab group sync status monitoring with timeout: %.0f seconds"
+ "T@\"NSString\",C,N,V_deviceIdentifier"
+ "Tab group sync agent finished syncing with result %ld"
+ "Tab group sync agent reset sync data. Triggering another sync."
+ "Tab group sync finished but local migration has not completed. Waiting for migration to complete."
+ "Tab group sync monitoring completed with result: %lu"
+ "Timed out waiting for tab group sync agent to finish syncing after %.0f seconds"
+ "Transaction failed, reverting %zu bookmark state changes"
+ "Update %zu pinned tabs"
+ "_archivedDataWithRootObject:"
+ "_connectionLock"
+ "_deviceIdentifier"
+ "_enumerateContentsOfBookmarkFolder:includingSubfolders:includeHidden:usingBlock:"
+ "_exportBookmarkWithMessage:connection:"
+ "_exportBookmarksBlock"
+ "_exportBookmarksCompletionHandler"
+ "_exportHistoryBlock"
+ "_exportHistoryCompletionHandler"
+ "_exportHistoryWithMessage:connection:"
+ "_exportReadingListBlock"
+ "_exportReadingListCompletionHandler"
+ "_exportReadingListWithMessage:connection:"
+ "_finishedBookmarksExportWithMessage:connection:"
+ "_finishedHistoryExportWithMessage:connection:"
+ "_finishedReadingListExportWithMessage:connection:"
+ "_migrateSchemaVersion61ToVersion62"
+ "_privacyPreservingDescriptionForMostRecentSQLiteError"
+ "_transactionRevertBlocks"
+ "_unarchivedObjectOfClass:fromData:"
+ "clearAllLocalBookmarksForAutomatedTesting"
+ "enumerateDescendantsOfBookmarkID:includeHidden:usingBlock:"
+ "enumerateObjectsWithOptions:usingBlock:"
+ "expectedOrderIndexOfSpecialID:"
+ "exportBookmarksWithBlock:completionHandler:"
+ "exportHistoryWithBlock:completionHandler:"
+ "exportReadingListToURL:sandboxExtension:completionHandler:"
+ "exportReadingListWithBlock:completionHandler:"
+ "importBookmarksFromURL:completionHandler:"
+ "initFolderWithParentID:deviceIdentifier:collectionType:"
+ "initFolderWithParentID:subtype:deviceIdentifier:collectionType:"
+ "initWithDeviceIdentifier:"
+ "initWithSQLiteStatement:deviceIdentifier:collectionType:"
+ "initWithSQLiteStatement:deviceIdentifier:collectionType:skipDecodingSyncData:"
+ "initWithSQLiteStatement:deviceIdentifier:hasIcon:collectionType:skipDecodingSyncData:"
+ "initWithTitle:address:parentID:deviceIdentifier:collectionType:"
+ "initWithTitle:address:parentID:folder:deviceIdentifier:collectionType:"
+ "initWithTitle:address:parentID:subtype:deviceIdentifier:collectionType:"
+ "initWithTitle:address:parentID:subtype:deviceIdentifier:collectionType:score:"
+ "initWithTitle:deviceIdentifier:"
+ "initWithTitle:deviceIdentifier:profileIdentifier:"
+ "initWithTitle:symbolImageName:favoritesFolderServerID:deviceIdentifier:"
+ "initWithTitle:url:deviceIdentifier:"
+ "initWithTitle:uuid:deviceIdentifier:"
+ "initWithUUID:deviceIdentifier:"
+ "initWithUUID:deviceIdentifier:lastVisitTime:"
+ "initWithUUID:title:url:deviceIdentifier:"
+ "initWithUUID:title:url:deviceIdentifier:isPrivateBrowsing:"
+ "initWithUUID:title:url:deviceIdentifier:lastVisitTime:"
+ "initWithUUID:title:url:pinned:pinnedTitle:pinnedURL:localAttributes:deviceIdentifier:"
+ "initWithValue:generation:deviceIdentifier:"
+ "initWithValueSource:valueProvider:valueUpdater:generation:deviceIdentifier:"
+ "interruptDatabase"
+ "localDeviceWithTitle:creationDeviceIdentifier:deviceIdentifier:"
+ "localOrUnnamedTabGroupForRestoration:inProfileWithIdentifier:deviceIdentifier:"
+ "performDeduplicationWithMode:"
+ "pinnedTabWithTitle:url:deviceIdentifier:"
+ "positionBetweenPosition:andPosition:"
+ "processName"
+ "r"
+ "remoteDeviceWithTitle:deviceIdentifier:"
+ "reportDatabaseTransactionFailureWithProcessName:revertedChangesCount:stacktrace:sqliteError:"
+ "safari_safariApplicationPlatformBundleIdentifier"
+ "setDeviceIdentifier:"
+ "startPageTabWithDeviceIdentifier:"
+ "syncStateGeneration"
+ "test_cjkIdeographCharacterSet"
+ "unarchivedObjectOfClass:fromData:error:"
+ "uncacheTabGroup:"
+ "unnamedTabGroupWithDeviceIdentifier:"
+ "unnamedTabGroupWithUUID:profileIdentifier:deviceIdentifier:"
+ "v32@0:8@?16@?24"
+ "v32@?0@?<v@?>8Q16^B24"
+ "v36@0:8i16B20B24@?28"
+ "~DefaultProfileDeviceIdentifier-%@"
- "(%@ %@) %@ %@ %@ %@"
- "@\"NSString\"24@0:8@\"WBSCRDTPositionGenerator\"16"
- "@\"WBSCRDTPositionSortValue\"16@?0@\"WBSCRDTPositionSortValue\"8"
- "@32@0:8^{sqlite3_stmt=}16q24"
- "@36@0:8^{sqlite3_stmt=}16q24B32"
- "@36@0:8i16q20q28"
- "@40@0:8^{sqlite3_stmt=}16B24q28B36"
- "@48@0:8@16@24i32B36q40"
- "@52@0:8@16@24i32q36q44"
- "@60@0:8@16@24i32q36q44@52"
- "@68@0:8@16@24@32B40@44@52@60"
- "A"
- "B16@?0@\"WBSCRDTPositionSortValue\"8"
- "ImportBookmarksSuggestedName"
- "Local tab group %{public}@ is getting saved to disk with no tabs"
- "Skipped window state from DB due to missing tab group."
- "Sync agent finished syncing"
- "Sync agent reset sync data. Triggering another sync."
- "Sync finished but local migration has not completed. Waiting for migration to complete."
- "TabGroups"
- "Timed out waiting for sync agent to finish syncing"
- "Window state local tab group has no tabs: %{public}@"
- "_enumerateContentsOfBookmarkFolder:includingSubfolders:usingBlock:"
- "_interruptDatabase"
- "_nextInMemoryPositionChangeID"
- "_uncacheTabGroup:"
- "changeID"
- "deviceIdentifierForPositionGenerator:"
- "importBookmarksFromURL:inFolderWithSuggestedName:completionHandler:"
- "initFolderWithParentID:subtype:collectionType:"
- "initWithSQLiteStatement:collectionType:"
- "initWithSQLiteStatement:collectionType:skipDecodingSyncData:"
- "initWithSQLiteStatement:hasIcon:collectionType:skipDecodingSyncData:"
- "initWithSortValues:"
- "initWithTitle:"
- "initWithTitle:address:parentID:folder:collectionType:"
- "initWithTitle:address:parentID:subtype:collectionType:"
- "initWithTitle:address:parentID:subtype:collectionType:score:"
- "initWithTitle:profileIdentifier:"
- "initWithTitle:symbolImageName:favoritesFolderServerID:"
- "initWithTitle:url:"
- "initWithTitle:uuid:"
- "initWithUUID:lastVisitTime:"
- "initWithUUID:title:url:"
- "initWithUUID:title:url:isPrivateBrowsing:"
- "initWithUUID:title:url:lastVisitTime:"
- "initWithUUID:title:url:pinned:pinnedTitle:pinnedURL:localAttributes:"
- "initWithValue:generation:"
- "initWithValueSource:valueProvider:valueUpdater:generation:"
- "localDeviceWithTitle:creationDeviceIdentifier:"
- "localOrUnnamedTabGroupForRestoration:inProfileWithIdentifier:"
- "nextChangeIDForPositionInPositionGenerator:"
- "nextDatabaseSyncChangeID"
- "pinnedTabWithTitle:url:"
- "positionBetweenPosition:andPosition:withDeviceIdentifier:changeID:"
- "positionSortValueWithChangeID:"
- "q24@0:8@\"WBSCRDTPositionGenerator\"16"
- "remoteDeviceWithTitle:"
- "sortValues"
- "startPageTab"
- "unnamedTabGroup"
- "unnamedTabGroupWithUUID:profileIdentifier:"

```
