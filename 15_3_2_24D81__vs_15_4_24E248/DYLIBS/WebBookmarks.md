## WebBookmarks

> `/System/Library/PrivateFrameworks/WebBookmarks.framework/Versions/A/WebBookmarks`

```diff

-620.2.4.11.6
-  __TEXT.__text: 0xa57e0
-  __TEXT.__auth_stubs: 0xb00
-  __TEXT.__objc_methlist: 0x72ac
-  __TEXT.__const: 0x2b8
-  __TEXT.__gcc_except_tab: 0xa70c
-  __TEXT.__cstring: 0xd76d
-  __TEXT.__oslogstring: 0x764d
+621.1.15.11.10
+  __TEXT.__text: 0xaaf88
+  __TEXT.__auth_stubs: 0xb40
+  __TEXT.__objc_methlist: 0x80ec
+  __TEXT.__const: 0x306
+  __TEXT.__gcc_except_tab: 0xa9f0
+  __TEXT.__cstring: 0xd93c
+  __TEXT.__oslogstring: 0x7806
   __TEXT.__dlopen_cstrs: 0x50
-  __TEXT.__unwind_info: 0x3e58
+  __TEXT.__constg_swiftt: 0x60
+  __TEXT.__swift5_typeref: 0x9
+  __TEXT.__swift5_reflstr: 0x1c
+  __TEXT.__swift5_fieldmd: 0x1c
+  __TEXT.__swift5_types: 0x4
+  __TEXT.__unwind_info: 0x4240
   __TEXT.__objc_classname: 0xa21
-  __TEXT.__objc_methname: 0x14ec1
+  __TEXT.__objc_methname: 0x1512d
   __TEXT.__objc_methtype: 0x272b
-  __TEXT.__objc_stubs: 0xe040
-  __DATA_CONST.__got: 0x740
-  __DATA_CONST.__const: 0xb40
-  __DATA_CONST.__objc_classlist: 0x218
+  __TEXT.__objc_stubs: 0xe1e0
+  __DATA_CONST.__got: 0x748
+  __DATA_CONST.__const: 0xc38
+  __DATA_CONST.__objc_classlist: 0x220
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x100
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4900
+  __DATA_CONST.__objc_selrefs: 0x4a28
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x1c0
   __DATA_CONST.__objc_arraydata: 0x358
-  __AUTH_CONST.__auth_got: 0x598
-  __AUTH_CONST.__const: 0x35b0
-  __AUTH_CONST.__cfstring: 0x5cc0
-  __AUTH_CONST.__objc_const: 0xaef8
+  __AUTH_CONST.__auth_got: 0x5b8
+  __AUTH_CONST.__const: 0x36a0
+  __AUTH_CONST.__cfstring: 0x5d20
+  __AUTH_CONST.__objc_const: 0x96d0
   __AUTH_CONST.__objc_arrayobj: 0xf0
   __AUTH_CONST.__objc_intobj: 0x360
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH.__objc_data: 0x14f0
-  __DATA.__objc_ivar: 0x5a4
+  __AUTH.__data: 0xb8
+  __DATA.__objc_ivar: 0x5a8
   __DATA.__data: 0xf00
   __DATA.__bss: 0x314
   - /System/Library/Frameworks/CloudKit.framework/Versions/A/CloudKit

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 3C61BA05-315D-3F1A-A933-EAB2531B62BE
-  Functions: 3426
-  Symbols:   8160
-  CStrings:  6079
+  - /usr/lib/swift/libswiftAVFoundation.dylib
+  - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreAudio.dylib
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreLocation.dylib
+  - /usr/lib/swift/libswiftCoreMIDI.dylib
+  - /usr/lib/swift/libswiftCoreMedia.dylib
+  - /usr/lib/swift/libswiftDarwin.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftIOKit.dylib
+  - /usr/lib/swift/libswiftIntents.dylib
+  - /usr/lib/swift/libswiftMetal.dylib
+  - /usr/lib/swift/libswiftOSLog.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswiftos.dylib
+  - /usr/lib/swift/libswiftsimd.dylib
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  UUID: 91B83A89-4FAA-3B26-AE9D-AE8695D07E9D
+  Functions: 3645
+  Symbols:   8494
+  CStrings:  6111
 
Symbols:
+ +[WBFeatureManager sharedFeatureManager].cold.1
+ +[WBTabGroupSyncAgentProxy sharedProxy].cold.1
+ +[WebBookmark(Internal) modifiedAttributesToFieldNames].cold.1
+ +[WebBookmarkCollection readingListArchivesDirectoryPath].cold.1
+ +[WebBookmarkCollection safariBookmarkCollection].cold.2
+ +[WebBookmarkCollection(Sync) _syncFlags].cold.1
+ -[WBMutableTabGroup duplicateTabs:]
+ -[WBProfile _defaultSettingForKey:].cold.1
+ -[WBReusableTabEntry setReusableTab:]
+ -[WBSettingsSyncEngineAccess _isKnownPerSiteSetting:].cold.1
+ -[WBSettingsSyncEngineAccess _perSitePreferencesStore].cold.1
+ -[WBTab duplicatePreservingUUID]
+ -[WBTabCollection _deleteItems:leaveTombstones:cleanBookmarks:]
+ -[WBTabCollection deleteItems:leaveTombstones:cleanBookmarks:]
+ -[WBTabCollection saveWindowRestorationArchiveData:forWindowUUIDString:completionHandler:]
+ -[WBTabGroupManager deletePrivateWindowState:]
+ -[WBTabGroupManager saveWindowRestorationArchiveData:forWindowUUIDString:completionHandler:]
+ -[WBWindowState setWindowRestorationArchiveData:]
+ -[WBWindowState windowRestorationArchiveData]
+ -[WebBookmarkCollection _createSchema].cold.1
+ -[WebBookmarkCollection _deleteBookmarks:leaveTombstone:cleanBookmarks:]
+ -[WebBookmarkCollection _migrateSchemaVersion55ToVersion56]
+ -[WebBookmarkCollection _trackChangesInMemoryIfDatabaseWriteIsNotAllowed].cold.1
+ -[WebBookmarkCollection didExpireBackgroundTask]
+ -[WebBookmarkListQuery _preparePrefixesFromNormalizedString:].cold.1
+ -[WebBookmarkTabCollection _migrateSchemaVersion55ToVersion56]
+ -[WebBookmarkTabCollection _saveWindowRestorationArchiveData:forWindowUUIDString:]
+ -[WebBookmarkTabCollection _windowStatesWithFilter:].cold.1
+ -[WebBookmarkTabCollection saveWindowRestorationArchiveData:forWindowUUIDString:]
+ -[WebBookmarkTitleWordTokenizer advanceToNextToken].cold.1
+ BookmarkInFolderWithoutIconColumnsSelectQuery.cold.1
+ BookmarkInFolderWithoutIconColumnsSelectQueryWithOptions.cold.1
+ BookmarkSQLiteColumnNames.cold.1
+ BookmarkSQLiteColumns.cold.1
+ GCC_except_table105
+ GCC_except_table189
+ GCC_except_table196
+ GCC_except_table201
+ GCC_except_table203
+ GCC_except_table204
+ GCC_except_table230
+ GCC_except_table238
+ GCC_except_table241
+ GCC_except_table256
+ GCC_except_table257
+ GCC_except_table258
+ GCC_except_table270
+ GCC_except_table288
+ GCC_except_table306
+ GCC_except_table312
+ GCC_except_table313
+ GCC_except_table318
+ GCC_except_table320
+ GCC_except_table322
+ GCC_except_table323
+ GCC_except_table326
+ GCC_except_table329
+ GCC_except_table334
+ GCC_except_table335
+ GCC_except_table336
+ GCC_except_table350
+ GCC_except_table355
+ GCC_except_table364
+ GCC_except_table367
+ GCC_except_table368
+ GCC_except_table369
+ GCC_except_table370
+ GCC_except_table371
+ GCC_except_table375
+ GCC_except_table381
+ GCC_except_table382
+ GCC_except_table385
+ GCC_except_table386
+ GCC_except_table388
+ GCC_except_table399
+ GCC_except_table402
+ GCC_except_table406
+ GCC_except_table407
+ GCC_except_table408
+ GCC_except_table411
+ GCC_except_table412
+ GCC_except_table413
+ GCC_except_table416
+ GCC_except_table417
+ GCC_except_table423
+ GCC_except_table439
+ GCC_except_table441
+ GCC_except_table444
+ GCC_except_table445
+ GCC_except_table456
+ GCC_except_table457
+ GCC_except_table460
+ GCC_except_table461
+ GCC_except_table462
+ GCC_except_table475
+ GCC_except_table481
+ GCC_except_table495
+ GCC_except_table496
+ GCC_except_table499
+ GCC_except_table505
+ GCC_except_table510
+ GCC_except_table513
+ GCC_except_table516
+ GCC_except_table517
+ GCC_except_table518
+ GCC_except_table528
+ GCC_except_table529
+ OBJC_IVAR_$_WBWindowState._windowRestorationArchiveData
+ WBBookmarkSyncModifiedAttributesForKey.cold.1
+ WBCurrentProcessContainerPath.cold.1
+ WBS_LOG_CHANNEL_PREFIXBookmarkSync.cold.1
+ WBS_LOG_CHANNEL_PREFIXBookmarks.cold.1
+ WBS_LOG_CHANNEL_PREFIXCloudBookmarks.cold.1
+ WBS_LOG_CHANNEL_PREFIXCloudSettings.cold.1
+ WBS_LOG_CHANNEL_PREFIXCycler.cold.1
+ WBS_LOG_CHANNEL_PREFIXDataMigration.cold.1
+ WBS_LOG_CHANNEL_PREFIXExport.cold.1
+ WBS_LOG_CHANNEL_PREFIXImport.cold.1
+ WBS_LOG_CHANNEL_PREFIXProfiles.cold.1
+ WBS_LOG_CHANNEL_PREFIXReadingList.cold.1
+ WBS_LOG_CHANNEL_PREFIXReadingListIcons.cold.1
+ WBS_LOG_CHANNEL_PREFIXTabGroup.cold.1
+ WBS_LOG_CHANNEL_PREFIXTabs.cold.1
+ WBS_LOG_CHANNEL_PREFIXWebBookmarkServer.cold.1
+ WBS_LOG_CHANNEL_PREFIXWebsiteData.cold.1
+ WBSafariContainerPath.cold.1
+ WBSafariDirectoryPath.cold.1
+ WBSafariPreferencesDomain.cold.1
+ _OBJC_CLASS_$__TtCs12_SwiftObject
+ _OBJC_METACLASS_$__TtCs12_SwiftObject
+ _WBSWindowRestorationArchiveDataKey
+ _ZL13syncLockQueuev.cold.1
+ _ZL21bookmarkMatchesFilterP11WebBookmarkP7NSArrayIP8NSStringE.cold.1
+ _ZL23performBlockExclusivelyU13block_pointerFvvE.cold.1
+ _ZL24bookmarksCollectionQueuev.cold.1
+ __24-[WBTabCollection error]_block_invoke.34
+ __32-[WBMutableTabGroup deleteTabs:]_block_invoke.9
+ __40-[WBTabCollection hasCompletedMigration]_block_invoke.28
+ __42-[WBTabCollection scopedBookmarkWithUUID:]_block_invoke_4.cold.1
+ __42-[WBTabGroupManager closeAllTabsOnDevice:]_block_invoke.166
+ __43-[WBTabGroupManager insertUnnamedTabGroup:]_block_invoke.154
+ __44-[WBTabCollection scopedBookmarkListWithID:]_block_invoke_4.cold.1
+ __45-[WebBookmarkTabCollection _saveWindowState:]_block_invoke.410
+ __45-[WebBookmarkTabCollection _saveWindowState:]_block_invoke.410.cold.1
+ __46-[WBTabGroupManager deletePrivateWindowState:]_block_invoke.92
+ __46-[WBTabGroupManager deletePrivateWindowState:]_block_invoke_2.93
+ __56-[WBTabCollection _updatePinnedTabsByProfileIdentifier:]_block_invoke.99
+ __56-[WBTabCollection _updatePinnedTabsByProfileIdentifier:]_block_invoke_2.100
+ __58-[WBTabCollection updateTabsInTabGroup:completionHandler:]_block_invoke.149
+ __60-[WebBookmarkCollection updateBookmarkSyncPositionIfNeeded:]_block_invoke.1106
+ __60-[WebBookmarkCollection updateBookmarkSyncPositionIfNeeded:]_block_invoke_2.1110
+ __60-[WebBookmarkTabCollection _regenerateSyncPositionsIfNeeded]_block_invoke.181
+ __60-[WebBookmarkTabCollection _regenerateSyncPositionsIfNeeded]_block_invoke.181.cold.1
+ __61-[WBTabGroupManager _notifySyncDidFinishedForScopedBookmarks]_block_invoke.238
+ __64-[WBTabCollection getActiveParticipantsInTab:completionHandler:]_block_invoke.187
+ __64-[WBTabCollection scopedBookmarkListWithID:filteredUsingString:]_block_invoke_4.cold.1
+ __68-[WBTabGroupManager _dequeueNextAcceptCloudKitShareMetadataIfNeeded]_block_invoke.208
+ __72-[WebBookmarkTabCollection _saveTabGroupRecordsWithMissingCKShareRecord]_block_invoke.187
+ __78-[WebBookmarkCollection _saveBookmark:withSpecialID:updateGenerationIfNeeded:]_block_invoke.810
+ __86-[WBTabGroupManager updateProfileWithIdentifier:persist:usingBlock:completionHandler:]_block_invoke.141
+ __92-[WBTabGroupManager moveTabs:toTabGroup:afterTab:withoutPersistingTabGroupsWithUUIDStrings:]_block_invoke.189
+ __DATA__TtC12WebBookmarks35SymbolOfNewBeginningsInWebBookmarks
+ __IVARS__TtC12WebBookmarks35SymbolOfNewBeginningsInWebBookmarks
+ __METACLASS_DATA__TtC12WebBookmarks35SymbolOfNewBeginningsInWebBookmarks
+ __ZN12SafariShared25SuddenTerminationDisablerC1EP8NSStringU13block_pointerFvvE
+ ___24-[WBTabCollection error]_block_invoke_2
+ ___28-[WBTabCollection saveItem:]_block_invoke_2
+ ___28-[WBTabCollection saveItem:]_block_invoke_3
+ ___30-[WBTabCollection deleteTabs:]_block_invoke_4
+ ___30-[WBTabCollection deleteTabs:]_block_invoke_5
+ ___31-[WBTabCollection browserState]_block_invoke_2
+ ___31-[WBTabCollection browserState]_block_invoke_3
+ ___31-[WBTabCollection windowStates]_block_invoke_2
+ ___31-[WBTabCollection windowStates]_block_invoke_3
+ ___32-[WBTabCollection saveTabGroup:]_block_invoke_3
+ ___32-[WBTabCollection saveTabGroup:]_block_invoke_4
+ ___34-[WBTabCollection deleteTabGroup:]_block_invoke_2
+ ___34-[WBTabCollection deleteTabGroup:]_block_invoke_3
+ ___34-[WBTabCollection mutableProfiles]_block_invoke_2
+ ___34-[WBTabCollection mutableProfiles]_block_invoke_3
+ ___34-[WBTabCollection recordIDForTab:]_block_invoke_3
+ ___34-[WBTabCollection recordIDForTab:]_block_invoke_4
+ ___35-[WBMutableTabGroup duplicateTabs:]_block_invoke
+ ___35-[WBTabCollection databaseSyncData]_block_invoke_2
+ ___35-[WBTabCollection databaseSyncData]_block_invoke_3
+ ___35-[WBTabCollection saveWindowState:]_block_invoke_2
+ ___35-[WBTabCollection saveWindowState:]_block_invoke_3
+ ___35-[WBTabCollection syncDataForItem:]_block_invoke_2
+ ___35-[WBTabCollection syncDataForItem:]_block_invoke_3
+ ___36-[WBTabCollection closeWindowState:]_block_invoke_2
+ ___36-[WBTabCollection closeWindowState:]_block_invoke_3
+ ___36-[WBTabCollection saveBrowserState:]_block_invoke_2
+ ___36-[WBTabCollection saveBrowserState:]_block_invoke_3
+ ___37-[WBTabCollection deleteWindowState:]_block_invoke_2
+ ___37-[WBTabCollection deleteWindowState:]_block_invoke_3
+ ___37-[WBTabCollection devicesForProfile:]_block_invoke_2
+ ___37-[WBTabCollection devicesForProfile:]_block_invoke_3
+ ___37-[WBTabCollection performMaintenance]_block_invoke_2
+ ___37-[WBTabCollection performMaintenance]_block_invoke_3
+ ___37-[WBTabCollection pinnedTabsFolderID]_block_invoke_2
+ ___37-[WBTabCollection pinnedTabsFolderID]_block_invoke_3
+ ___38-[WBTabCollection deleteWindowStates:]_block_invoke_2
+ ___38-[WBTabCollection deleteWindowStates:]_block_invoke_3
+ ___38-[WBTabCollection hasMultipleProfiles]_block_invoke_2
+ ___38-[WBTabCollection hasMultipleProfiles]_block_invoke_3
+ ___38-[WBTabCollection mutableTabWithUUID:]_block_invoke_3
+ ___38-[WBTabCollection mutableTabWithUUID:]_block_invoke_4
+ ___38-[WBTabCollection tabUUIDForServerID:]_block_invoke_3
+ ___38-[WBTabCollection tabUUIDForServerID:]_block_invoke_4
+ ___39-[WBTabCollection profileWithServerID:]_block_invoke_2
+ ___39-[WBTabCollection profileWithServerID:]_block_invoke_3
+ ___39-[WBTabCollection windowStateWithUUID:]_block_invoke_2
+ ___39-[WBTabCollection windowStateWithUUID:]_block_invoke_3
+ ___40-[WBTabCollection deleteAllWindowStates]_block_invoke_2
+ ___40-[WBTabCollection deleteAllWindowStates]_block_invoke_3
+ ___40-[WBTabCollection hasCompletedMigration]_block_invoke_2
+ ___41-[WBTabCollection reorderItem:afterItem:]_block_invoke_2
+ ___41-[WBTabCollection reorderItem:afterItem:]_block_invoke_3
+ ___41-[WBTabCollection setCompletedMigration:]_block_invoke_2
+ ___41-[WBTabCollection setCompletedMigration:]_block_invoke_3
+ ___41-[WBTabCollection syncDataForItemWithID:]_block_invoke_2
+ ___41-[WBTabCollection syncDataForItemWithID:]_block_invoke_3
+ ___41-[WBTabCollection updateTabs:inTabGroup:]_block_invoke_2
+ ___41-[WBTabCollection updateTabs:inTabGroup:]_block_invoke_3
+ ___42-[WBTabCollection lastSessionBrowserState]_block_invoke_2
+ ___42-[WBTabCollection lastSessionBrowserState]_block_invoke_3
+ ___42-[WBTabCollection mutableTabsForTabGroup:]_block_invoke_2
+ ___42-[WBTabCollection mutableTabsForTabGroup:]_block_invoke_3
+ ___42-[WBTabCollection scopedBookmarkWithUUID:]_block_invoke_3
+ ___42-[WBTabCollection scopedBookmarkWithUUID:]_block_invoke_4
+ ___42-[WBTabCollection shareRecordForTabGroup:]_block_invoke_2
+ ___42-[WBTabCollection shareRecordForTabGroup:]_block_invoke_3
+ ___43-[WBTabCollection activeParticipantsInTab:]_block_invoke_2
+ ___43-[WBTabCollection activeParticipantsInTab:]_block_invoke_3
+ ___43-[WBTabCollection deleteAllLocalSavedState]_block_invoke_3
+ ___43-[WBTabCollection deleteAllLocalSavedState]_block_invoke_4
+ ___43-[WBTabCollection mutableTabGroupWithUUID:]_block_invoke_2
+ ___43-[WBTabCollection mutableTabGroupWithUUID:]_block_invoke_3
+ ___43-[WBTabCollection tabGroupUUIDForServerID:]_block_invoke_3
+ ___43-[WBTabCollection tabGroupUUIDForServerID:]_block_invoke_4
+ ___44-[WBTabCollection privatePinnedTabsFolderID]_block_invoke_2
+ ___44-[WBTabCollection privatePinnedTabsFolderID]_block_invoke_3
+ ___44-[WBTabCollection scopedBookmarkListWithID:]_block_invoke_3
+ ___44-[WBTabCollection scopedBookmarkListWithID:]_block_invoke_4
+ ___46-[WBReusableTabManager cache:willEvictObject:]_block_invoke
+ ___46-[WBTabCollection itemsInParentWithID:ofType:]_block_invoke_4
+ ___46-[WBTabCollection itemsInParentWithID:ofType:]_block_invoke_5
+ ___46-[WBTabCollection numberOfLocalTabsToBeClosed]_block_invoke_2
+ ___46-[WBTabCollection numberOfLocalTabsToBeClosed]_block_invoke_3
+ ___46-[WBTabCollection saveItem:completionHandler:]_block_invoke_2
+ ___46-[WBTabCollection saveItem:completionHandler:]_block_invoke_3
+ ___46-[WBTabCollection updateItems:inParentWithID:]_block_invoke_2
+ ___46-[WBTabCollection updateItems:inParentWithID:]_block_invoke_3
+ ___46-[WBTabGroupManager deletePrivateWindowState:]_block_invoke
+ ___46-[WBTabGroupManager deletePrivateWindowState:]_block_invoke_2
+ ___47-[WBTabCollection deleteItems:leaveTombstones:]_block_invoke_2
+ ___47-[WBTabCollection deleteItems:leaveTombstones:]_block_invoke_3
+ ___47-[WBTabCollection saveItems:completionHandler:]_block_invoke_2
+ ___47-[WBTabCollection saveItems:completionHandler:]_block_invoke_3
+ ___48-[WBTabCollection activeParticipantsInTabGroup:]_block_invoke_2
+ ___48-[WBTabCollection activeParticipantsInTabGroup:]_block_invoke_3
+ ___48-[WBTabCollection insertTabGroup:afterTabGroup:]_block_invoke_3
+ ___48-[WBTabCollection insertTabGroup:afterTabGroup:]_block_invoke_4
+ ___48-[WBTabCollection mutableProfileWithIdentifier:]_block_invoke_2
+ ___48-[WBTabCollection mutableProfileWithIdentifier:]_block_invoke_3
+ ___49-[WBTabCollection insertTab:inTabGroup:afterTab:]_block_invoke_3
+ ___49-[WBTabCollection insertTab:inTabGroup:afterTab:]_block_invoke_4
+ ___50-[WBTabCollection insertTabs:inTabGroup:afterTab:]_block_invoke_4
+ ___50-[WBTabCollection insertTabs:inTabGroup:afterTab:]_block_invoke_5
+ ___51-[WBTabCollection allMutableNamedTabGroupsUnsorted]_block_invoke_2
+ ___51-[WBTabCollection allMutableNamedTabGroupsUnsorted]_block_invoke_3
+ ___53-[WBTabCollection saveWindowState:completionHandler:]_block_invoke_2
+ ___53-[WBTabCollection saveWindowState:completionHandler:]_block_invoke_3
+ ___54-[WBTabCollection pinnedTabsForProfileWithIdentifier:]_block_invoke_2
+ ___54-[WBTabCollection pinnedTabsForProfileWithIdentifier:]_block_invoke_3
+ ___54-[WBTabCollection saveBrowserState:completionHandler:]_block_invoke_2
+ ___54-[WBTabCollection saveBrowserState:completionHandler:]_block_invoke_3
+ ___56-[WBTabCollection deleteWindowStates:completionHandler:]_block_invoke_2
+ ___56-[WBTabCollection deleteWindowStates:completionHandler:]_block_invoke_3
+ ___56-[WBTabCollection insertItems:inParentWithID:afterItem:]_block_invoke_2
+ ___56-[WBTabCollection insertItems:inParentWithID:afterItem:]_block_invoke_3
+ ___56-[WBTabCollection mutableNamedTabGroupsInDefaultProfile]_block_invoke_2
+ ___56-[WBTabCollection mutableNamedTabGroupsInDefaultProfile]_block_invoke_3
+ ___58-[WBTabCollection reorderItemIntoPlace:completionHandler:]_block_invoke_2
+ ___58-[WBTabCollection reorderItemIntoPlace:completionHandler:]_block_invoke_3
+ ___59-[WBTabCollection reorderItem:afterItem:completionHandler:]_block_invoke_2
+ ___59-[WBTabCollection reorderItem:afterItem:completionHandler:]_block_invoke_3
+ ___60-[WBTabCollection disableSuddenTerminationForPendingChanges]_block_invoke_2
+ ___60-[WBTabCollection disableSuddenTerminationForPendingChanges]_block_invoke_3
+ ___60-[WBTabCollection shareRecordForTabGroup:completionHandler:]_block_invoke_2
+ ___60-[WBTabCollection shareRecordForTabGroup:completionHandler:]_block_invoke_3
+ ___62-[WBTabCollection deleteItems:leaveTombstones:cleanBookmarks:]_block_invoke
+ ___62-[WBTabCollection deleteItems:leaveTombstones:cleanBookmarks:]_block_invoke_2
+ ___62-[WBTabCollection deleteItems:leaveTombstones:cleanBookmarks:]_block_invoke_3
+ ___62-[WBTabCollection pinnedTabsFolderIDForProfileWithIdentifier:]_block_invoke_2
+ ___62-[WBTabCollection pinnedTabsFolderIDForProfileWithIdentifier:]_block_invoke_3
+ ___62-[WBTabCollection setHasSharedTabGroupsWithCompletionHandler:]_block_invoke_2
+ ___62-[WBTabCollection setHasSharedTabGroupsWithCompletionHandler:]_block_invoke_3
+ ___63-[WBTabCollection _deleteItems:leaveTombstones:cleanBookmarks:]_block_invoke
+ ___63-[WBTabCollection _deleteItems:leaveTombstones:cleanBookmarks:]_block_invoke_2
+ ___63-[WBTabCollection enumerateDescendantsOfItemWithID:usingBlock:]_block_invoke_3
+ ___63-[WBTabCollection enumerateDescendantsOfItemWithID:usingBlock:]_block_invoke_4
+ ___64-[WBTabCollection getActiveParticipantsInTab:completionHandler:]_block_invoke_3
+ ___64-[WBTabCollection getActiveParticipantsInTab:completionHandler:]_block_invoke_4
+ ___64-[WBTabCollection scopedBookmarkListWithID:filteredUsingString:]_block_invoke_3
+ ___64-[WBTabCollection scopedBookmarkListWithID:filteredUsingString:]_block_invoke_4
+ ___64-[WBTabCollection updateItems:inParentWithID:completionHandler:]_block_invoke_2
+ ___64-[WBTabCollection updateItems:inParentWithID:completionHandler:]_block_invoke_3
+ ___65-[WBTabCollection deleteItems:leaveTombstones:completionHandler:]_block_invoke_2
+ ___65-[WBTabCollection deleteItems:leaveTombstones:completionHandler:]_block_invoke_3
+ ___66-[WBReusableTabManager tabGroupManager:didRemoveTabGroupWithUUID:]_block_invoke
+ ___67-[WBTabCollection insertItemsIntoPlace:inParent:completionHandler:]_block_invoke_2
+ ___67-[WBTabCollection insertItemsIntoPlace:inParent:completionHandler:]_block_invoke_3
+ ___68-[WBTabCollection insertItems:inParent:afterItem:completionHandler:]_block_invoke_2
+ ___68-[WBTabCollection insertItems:inParent:afterItem:completionHandler:]_block_invoke_3
+ ___70-[WBTabCollection presenceTabUUIDForParticipantIdentifier:inTabGroup:]_block_invoke_2
+ ___70-[WBTabCollection presenceTabUUIDForParticipantIdentifier:inTabGroup:]_block_invoke_3
+ ___70-[WBTabGroupManager numberOfTabsToBeClosedForProfilesWithIdentifiers:]_block_invoke
+ ___73-[WBTabCollection insertItemsIntoPlace:inParentWithID:completionHandler:]_block_invoke_2
+ ___73-[WBTabCollection insertItemsIntoPlace:inParentWithID:completionHandler:]_block_invoke_3
+ ___74-[WBTabCollection frequentlyVisitedSitesFolderIDForProfileWithIdentifier:]_block_invoke_2
+ ___74-[WBTabCollection frequentlyVisitedSitesFolderIDForProfileWithIdentifier:]_block_invoke_3
+ ___74-[WBTabCollection insertItems:inParentWithID:afterItem:completionHandler:]_block_invoke_2
+ ___74-[WBTabCollection insertItems:inParentWithID:afterItem:completionHandler:]_block_invoke_3
+ ___81-[WebBookmarkTabCollection saveWindowRestorationArchiveData:forWindowUUIDString:]_block_invoke
+ ___88-[WBTabCollection setFrequentlyVisitedSites:forProfileWithIdentifier:completionHandler:]_block_invoke_2
+ ___88-[WBTabCollection setFrequentlyVisitedSites:forProfileWithIdentifier:completionHandler:]_block_invoke_3
+ ___90-[WBTabCollection saveWindowRestorationArchiveData:forWindowUUIDString:completionHandler:]_block_invoke
+ ___90-[WBTabCollection saveWindowRestorationArchiveData:forWindowUUIDString:completionHandler:]_block_invoke_2
+ ___90-[WBTabCollection saveWindowRestorationArchiveData:forWindowUUIDString:completionHandler:]_block_invoke_3
+ ___block_descriptor_32_e22_16?0"WBMutableTab"8l
+ ___block_descriptor_40_ea8_32r_e5_v8?0l
+ ___block_descriptor_50_ea8_32s40s_e5_B8?0l
+ ___block_descriptor_58_ea8_32s40s48r_e5_v8?0l
+ ___swift_reflection_version
+ __block_literal_global.1027
+ __block_literal_global.103
+ __block_literal_global.1109
+ __block_literal_global.122
+ __block_literal_global.124
+ __block_literal_global.127
+ __block_literal_global.139
+ __block_literal_global.14
+ __block_literal_global.142
+ __block_literal_global.146
+ __block_literal_global.157
+ __block_literal_global.159
+ __block_literal_global.173
+ __block_literal_global.175
+ __block_literal_global.176
+ __block_literal_global.1806
+ __block_literal_global.1809
+ __block_literal_global.1817
+ __block_literal_global.192
+ __block_literal_global.203
+ __block_literal_global.205
+ __block_literal_global.221
+ __block_literal_global.438
+ __block_literal_global.46
+ __block_literal_global.483
+ __block_literal_global.56
+ __block_literal_global.58
+ __block_literal_global.61
+ __block_literal_global.71
+ __block_literal_global.74
+ __block_literal_global.95
+ __block_literal_global.988
+ __swift_FORCE_LOAD_$_swiftAVFoundation
+ __swift_FORCE_LOAD_$_swiftAVFoundation_$_WebBookmarks
+ __swift_FORCE_LOAD_$_swiftCoreAudio
+ __swift_FORCE_LOAD_$_swiftCoreAudio_$_WebBookmarks
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftCoreFoundation_$_WebBookmarks
+ __swift_FORCE_LOAD_$_swiftCoreLocation
+ __swift_FORCE_LOAD_$_swiftCoreLocation_$_WebBookmarks
+ __swift_FORCE_LOAD_$_swiftCoreMIDI
+ __swift_FORCE_LOAD_$_swiftCoreMIDI_$_WebBookmarks
+ __swift_FORCE_LOAD_$_swiftCoreMedia
+ __swift_FORCE_LOAD_$_swiftCoreMedia_$_WebBookmarks
+ __swift_FORCE_LOAD_$_swiftDarwin
+ __swift_FORCE_LOAD_$_swiftDarwin_$_WebBookmarks
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftDispatch_$_WebBookmarks
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftFoundation_$_WebBookmarks
+ __swift_FORCE_LOAD_$_swiftIOKit
+ __swift_FORCE_LOAD_$_swiftIOKit_$_WebBookmarks
+ __swift_FORCE_LOAD_$_swiftIntents
+ __swift_FORCE_LOAD_$_swiftIntents_$_WebBookmarks
+ __swift_FORCE_LOAD_$_swiftMetal
+ __swift_FORCE_LOAD_$_swiftMetal_$_WebBookmarks
+ __swift_FORCE_LOAD_$_swiftOSLog
+ __swift_FORCE_LOAD_$_swiftOSLog_$_WebBookmarks
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftObjectiveC_$_WebBookmarks
+ __swift_FORCE_LOAD_$_swiftQuartzCore
+ __swift_FORCE_LOAD_$_swiftQuartzCore_$_WebBookmarks
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers_$_WebBookmarks
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swiftXPC_$_WebBookmarks
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_Builtin_float_$_WebBookmarks
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_errno_$_WebBookmarks
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_math_$_WebBookmarks
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_signal_$_WebBookmarks
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_stdio_$_WebBookmarks
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swift_time_$_WebBookmarks
+ __swift_FORCE_LOAD_$_swiftos
+ __swift_FORCE_LOAD_$_swiftos_$_WebBookmarks
+ __swift_FORCE_LOAD_$_swiftsimd
+ __swift_FORCE_LOAD_$_swiftsimd_$_WebBookmarks
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftsys_time_$_WebBookmarks
+ __swift_FORCE_LOAD_$_swiftunistd
+ __swift_FORCE_LOAD_$_swiftunistd_$_WebBookmarks
+ _objc_msgSend$_deleteBookmarks:leaveTombstone:cleanBookmarks:
+ _objc_msgSend$_deleteItems:leaveTombstones:cleanBookmarks:
+ _objc_msgSend$_migrateSchemaVersion55ToVersion56
+ _objc_msgSend$_saveWindowRestorationArchiveData:forWindowUUIDString:
+ _objc_msgSend$deleteItems:leaveTombstones:cleanBookmarks:
+ _objc_msgSend$didExpireBackgroundTask
+ _objc_msgSend$isMainThread
+ _objc_msgSend$isPrivateWindow
+ _objc_msgSend$mutableDuplicate
+ _objc_msgSend$safari_replaceItemAtURL:withItemFromURL:error:
+ _objc_msgSend$saveWindowRestorationArchiveData:forWindowUUIDString:
+ _objc_msgSend$saveWindowRestorationArchiveData:forWindowUUIDString:completionHandler:
+ _objc_msgSend$setReusableTab:
+ _objc_msgSend$setWindowRestorationArchiveData:
+ _objc_msgSend$stringByAppendingFormat:
+ _objc_msgSend$windowRestorationArchiveData
+ _objc_opt_self
+ _sqlite3_bind_blob64
+ _swift_bridgeObjectRelease
+ _swift_deallocClassInstance
+ _swift_deletedMethodError
+ _symbolic SS
+ _symbolic _____ 12WebBookmarks023SymbolOfNewBeginningsInaB0C
- GCC_except_table116
- GCC_except_table144
- GCC_except_table145
- GCC_except_table154
- GCC_except_table177
- GCC_except_table190
- GCC_except_table194
- GCC_except_table195
- GCC_except_table198
- GCC_except_table199
- GCC_except_table205
- GCC_except_table213
- GCC_except_table214
- GCC_except_table219
- GCC_except_table221
- GCC_except_table224
- GCC_except_table225
- GCC_except_table226
- GCC_except_table227
- GCC_except_table233
- GCC_except_table234
- GCC_except_table243
- GCC_except_table259
- GCC_except_table260
- GCC_except_table264
- GCC_except_table272
- GCC_except_table285
- GCC_except_table290
- GCC_except_table295
- GCC_except_table304
- GCC_except_table308
- GCC_except_table314
- GCC_except_table324
- GCC_except_table337
- GCC_except_table338
- GCC_except_table352
- GCC_except_table357
- GCC_except_table366
- GCC_except_table384
- GCC_except_table387
- GCC_except_table410
- GCC_except_table415
- GCC_except_table418
- GCC_except_table446
- GCC_except_table447
- GCC_except_table459
- GCC_except_table477
- GCC_except_table483
- GCC_except_table497
- GCC_except_table501
- GCC_except_table502
- GCC_except_table507
- GCC_except_table512
- GCC_except_table515
- GCC_except_table522
- GCC_except_table526
- GCC_except_table60
- GCC_except_table99
- _OUTLINED_FUNCTION_12
- _OUTLINED_FUNCTION_13
- _OUTLINED_FUNCTION_14
- __32-[WBMutableTabGroup deleteTabs:]_block_invoke.8
- __42-[WBTabCollection scopedBookmarkWithUUID:]_block_invoke_2.cold.1
- __42-[WBTabGroupManager closeAllTabsOnDevice:]_block_invoke.156
- __43-[WBTabGroupManager insertUnnamedTabGroup:]_block_invoke.144
- __44-[WBTabCollection scopedBookmarkListWithID:]_block_invoke_2.cold.1
- __45-[WebBookmarkTabCollection _saveWindowState:]_block_invoke.405
- __45-[WebBookmarkTabCollection _saveWindowState:]_block_invoke.405.cold.1
- __56-[WBTabCollection _updatePinnedTabsByProfileIdentifier:]_block_invoke.95
- __56-[WBTabCollection _updatePinnedTabsByProfileIdentifier:]_block_invoke_2.96
- __58-[WBSettingsSyncEngineAccess didDeleteRemoteRecordWithID:]_block_invoke.cold.2
- __58-[WBTabCollection updateTabsInTabGroup:completionHandler:]_block_invoke.143
- __60-[WBSettingsSyncEngineAccess deleteBackgroundImageDirectory]_block_invoke.cold.2
- __60-[WebBookmarkCollection updateBookmarkSyncPositionIfNeeded:]_block_invoke.1105
- __60-[WebBookmarkCollection updateBookmarkSyncPositionIfNeeded:]_block_invoke_2.1109
- __60-[WebBookmarkTabCollection _regenerateSyncPositionsIfNeeded]_block_invoke.179
- __60-[WebBookmarkTabCollection _regenerateSyncPositionsIfNeeded]_block_invoke.179.cold.1
- __61-[WBTabGroupManager _notifySyncDidFinishedForScopedBookmarks]_block_invoke.226
- __64-[WBTabCollection getActiveParticipantsInTab:completionHandler:]_block_invoke.181
- __64-[WBTabCollection scopedBookmarkListWithID:filteredUsingString:]_block_invoke_2.cold.1
- __68-[WBTabGroupManager _dequeueNextAcceptCloudKitShareMetadataIfNeeded]_block_invoke.196
- __72-[WebBookmarkTabCollection _saveTabGroupRecordsWithMissingCKShareRecord]_block_invoke.185
- __78-[WebBookmarkCollection _saveBookmark:withSpecialID:updateGenerationIfNeeded:]_block_invoke.809
- __86-[WBTabGroupManager updateProfileWithIdentifier:persist:usingBlock:completionHandler:]_block_invoke.131
- __92-[WBTabGroupManager moveTabs:toTabGroup:afterTab:withoutPersistingTabGroupsWithUUIDStrings:]_block_invoke.179
- __ZN12WebBookmarks22BookmarkSQLTransaction8rollbackEv
- ___48-[WBTabCollection _deleteItems:leaveTombstones:]_block_invoke
- ___48-[WBTabCollection _deleteItems:leaveTombstones:]_block_invoke_2
- __block_literal_global.1026
- __block_literal_global.1108
- __block_literal_global.112
- __block_literal_global.114
- __block_literal_global.117
- __block_literal_global.120
- __block_literal_global.133
- __block_literal_global.136
- __block_literal_global.147
- __block_literal_global.163
- __block_literal_global.171
- __block_literal_global.174
- __block_literal_global.1802
- __block_literal_global.1805
- __block_literal_global.1813
- __block_literal_global.190
- __block_literal_global.201
- __block_literal_global.209
- __block_literal_global.36
- __block_literal_global.38
- __block_literal_global.427
- __block_literal_global.45
- __block_literal_global.472
- __block_literal_global.55
- __block_literal_global.59
- __block_literal_global.70
- __block_literal_global.91
- __block_literal_global.987
- __block_literal_global.99
- _objc_msgSend$URLByDeletingLastPathComponent
- _objc_msgSend$numberOfLocalTabsToBeClosed
- _objc_msgSend$safari_ensureDirectoryExists:
- _strncmp
CStrings:
+ " FROM windows INNER JOIN bookmarks AS tab_group_bookmarks ON windows.active_tab_group_id = tab_group_bookmarks.id LEFT JOIN bookmarks AS profile_bookmarks ON windows.active_profile_id = profile_bookmarks.id %@"
+ "<%@: %p; activeTabGroupUUID = %@; identifier = %d; sceneID = %@; uuid = %@; restoration_archive = %lu>"
+ "@16@?0@\"WBMutableTab\"8"
+ "ALTER TABLE windows ADD COLUMN restoration_archive BLOB"
+ "Background task expired. transactionIsActive: %d, database name: %@"
+ "CREATE TABLE IF NOT EXISTS windows (id INTEGER PRIMARY KEY,active_tab_group_id INTEGER DEFAULT NULL,active_profile_id INTEGER DEFAULT NULL,date_closed REAL DEFAULT NULL,extra_attributes BLOB DEFAULT NULL,is_last_session INTEGER DEFAULT 0,local_tab_group_id INTEGER DEFAULT NULL,private_tab_group_id INTEGER DEFAULT NULL,scene_id TEXT DEFAULT NULL,uuid TEXT NOT NULL UNIQUE,restoration_archive BLOB DEFAULT NULL,FOREIGN KEY (active_tab_group_id) REFERENCES bookmarks (id) ON UPDATE CASCADE ON DELETE SET NULL,FOREIGN KEY (active_profile_id) REFERENCES bookmarks (id) ON UPDATE CASCADE ON DELETE SET NULL,FOREIGN KEY (local_tab_group_id) REFERENCES bookmarks (id) ON UPDATE CASCADE ON DELETE CASCADE,FOREIGN KEY (private_tab_group_id) REFERENCES bookmarks (id) ON UPDATE CASCADE ON DELETE CASCADE)"
+ "Duplicating %zu tabs"
+ "FROM bookmarks WHERE dav_generation = %zd AND deleted = 0 AND added = 0 AND id != 0 AND syncable = 1 AND ((modified_attributes & %llu) != %llu OR type = 0)"
+ "FROM bookmarks WHERE dav_generation > %zd AND deleted = 0 AND added = 0 AND id != 0 AND syncable = 1 AND modified_attributes != 0 AND ((modified_attributes & %llu) != %llu OR type = 0)"
+ "FROM folder_ancestors LEFT OUTER JOIN bookmarks ON folder_id = bookmarks.id WHERE dav_generation = %zd AND deleted = 0 AND added = 0 AND bookmarks.id != 0 AND syncable = 1 AND (modified_attributes & %llu) == %llu GROUP BY folder_id ORDER BY count(ancestor_id) ASC"
+ "FROM folder_ancestors LEFT OUTER JOIN bookmarks ON folder_id = bookmarks.id WHERE dav_generation > %zd AND deleted = 0 AND added = 0 AND bookmarks.id != 0 AND syncable = 1 AND (modified_attributes & %llu) == %llu GROUP BY folder_id ORDER BY count(ancestor_id) ASC"
+ "Failed to add restoration archive"
+ "INSERT INTO windows (active_tab_group_id, active_profile_id, date_closed, extra_attributes, is_last_session, local_tab_group_id, private_tab_group_id, scene_id, uuid, restoration_archive) VALUES (?, ?, ?, ?, 1, ?, ?, ?, ?, ?) ON CONFLICT (uuid) DO UPDATE SET active_tab_group_id = excluded.active_tab_group_id, active_profile_id = excluded.active_profile_id, date_closed = excluded.date_closed, extra_attributes = excluded.extra_attributes, local_tab_group_id = excluded.local_tab_group_id, private_tab_group_id = excluded.private_tab_group_id, is_last_session = 1, restoration_archive = excluded.restoration_archive, scene_id = excluded.scene_id"
+ "PRAGMA user_version = 56"
+ "Postponing unlockSync. The process %{public}@ has requested to hold the lock."
+ "Queueing save operation for Window(%{public}@) restoration archive(%p)."
+ "SELECT tab_group_bookmarks.external_uuid, profile_bookmarks.external_uuid, windows.local_tab_group_id, windows.private_tab_group_id, windows.scene_id, windows.uuid, windows.id, windows.extra_attributes, windows.restoration_archive"
+ "T@\"<WBReusableTab>\",&,N,V_reusableTab"
+ "T@\"NSData\",C,N,V_windowRestorationArchiveData"
+ "UPDATE windows SET restoration_archive = ? WHERE uuid = ?"
+ "Window(%{public}@) has no restoration archive. Window position may reset."
+ "WindowState (%{public}@) saved with restoration archive(%p)."
+ "[StartPageBackground] %{public}@ was removed in Default Profile successfully."
+ "[StartPageBackground] Dispatching Asyc Task to Delete image directory."
+ "[StartPageBackground] Failed to remove image directory (%{public}@). Error: %{public}@."
+ "[StartPageBackground] FileManager could not install mobile asset image. %{public}@"
+ "[StartPageBackground] FileManager could not update image with record for Default Profile. %{public}@"
+ "[StartPageBackground] Removed image directory successfully."
+ "[StartPageBackground] Removing %{public}@ in Default Profile failed with error: %{public}@."
+ "_TtC12WebBookmarks35SymbolOfNewBeginningsInWebBookmarks"
+ "_deleteBookmarks:leaveTombstone:cleanBookmarks:"
+ "_deleteItems:leaveTombstones:cleanBookmarks:"
+ "_migrateSchemaVersion55ToVersion56"
+ "_saveWindowRestorationArchiveData:forWindowUUIDString:"
+ "_windowRestorationArchiveData"
+ "deleteItems:leaveTombstones:cleanBookmarks:"
+ "deletePrivateWindowState:"
+ "didExpireBackgroundTask"
+ "duplicatePreservingUUID"
+ "duplicateTabs:"
+ "isMainThread"
+ "safari_replaceItemAtURL:withItemFromURL:error:"
+ "saveWindowRestorationArchiveData:forWindowUUIDString:"
+ "saveWindowRestorationArchiveData:forWindowUUIDString:completionHandler:"
+ "setReusableTab:"
+ "setWindowRestorationArchiveData:"
+ "stringByAppendingFormat:"
+ "welcomeToTheWorldOfTomorrow"
+ "windowRestorationArchiveData"
- "<%@: %p; activeTabGroupUUID = %@; identifier = %d; sceneID = %@; uuid = %@>"
- "Attempting to remove Safari's background image directory."
- "CREATE TABLE IF NOT EXISTS windows (id INTEGER PRIMARY KEY,active_tab_group_id INTEGER DEFAULT NULL,active_profile_id INTEGER DEFAULT NULL,date_closed REAL DEFAULT NULL,extra_attributes BLOB DEFAULT NULL,is_last_session INTEGER DEFAULT 0,local_tab_group_id INTEGER DEFAULT NULL,private_tab_group_id INTEGER DEFAULT NULL,scene_id TEXT DEFAULT NULL,uuid TEXT NOT NULL UNIQUE,FOREIGN KEY (active_tab_group_id) REFERENCES bookmarks (id) ON UPDATE CASCADE ON DELETE SET NULL,FOREIGN KEY (active_profile_id) REFERENCES bookmarks (id) ON UPDATE CASCADE ON DELETE SET NULL,FOREIGN KEY (local_tab_group_id) REFERENCES bookmarks (id) ON UPDATE CASCADE ON DELETE CASCADE,FOREIGN KEY (private_tab_group_id) REFERENCES bookmarks (id) ON UPDATE CASCADE ON DELETE CASCADE)"
- "FROM bookmarks WHERE dav_generation = %ld AND deleted = 0 AND added = 0 AND id != 0 AND syncable = 1 AND ((modified_attributes & %llu) != %llu OR type = 0)"
- "FROM bookmarks WHERE dav_generation > %ld AND deleted = 0 AND added = 0 AND id != 0 AND syncable = 1 AND modified_attributes != 0 AND ((modified_attributes & %llu) != %llu OR type = 0)"
- "FROM folder_ancestors LEFT OUTER JOIN bookmarks ON folder_id = bookmarks.id WHERE dav_generation = %ld AND deleted = 0 AND added = 0 AND bookmarks.id != 0 AND syncable = 1 AND (modified_attributes & %llu) == %llu GROUP BY folder_id ORDER BY count(ancestor_id) ASC"
- "FROM folder_ancestors LEFT OUTER JOIN bookmarks ON folder_id = bookmarks.id WHERE dav_generation > %ld AND deleted = 0 AND added = 0 AND bookmarks.id != 0 AND syncable = 1 AND (modified_attributes & %llu) == %llu GROUP BY folder_id ORDER BY count(ancestor_id) ASC"
- "Failed to copy the background image over. Error: %{public}@"
- "Failed to copy the mobile asset background image over. Error: %{public}@"
- "INSERT INTO windows (active_tab_group_id, active_profile_id, date_closed, extra_attributes, is_last_session, local_tab_group_id, private_tab_group_id, scene_id, uuid) VALUES (?, ?, ?, ?, 1, ?, ?, ?, ?) ON CONFLICT (uuid) DO UPDATE SET active_tab_group_id = excluded.active_tab_group_id, active_profile_id = excluded.active_profile_id, date_closed = excluded.date_closed, extra_attributes = excluded.extra_attributes, local_tab_group_id = excluded.local_tab_group_id, private_tab_group_id = excluded.private_tab_group_id, is_last_session = 1, scene_id = excluded.scene_id"
- "Postponing unlockSync. The process %{public}@ has requested to hold the lock"
- "Removing Safari's background image directory failed with error: %@."
- "Removing Safari's background image directory was successful."
- "Removing Safari's background image failed with error: %@."
- "Removing Safari's background image was successful."
- "SELECT tab_group_bookmarks.external_uuid, profile_bookmarks.external_uuid, windows.local_tab_group_id, windows.private_tab_group_id, windows.scene_id, windows.uuid, windows.id, windows.extra_attributes FROM windows INNER JOIN bookmarks AS tab_group_bookmarks ON windows.active_tab_group_id = tab_group_bookmarks.id LEFT JOIN bookmarks AS profile_bookmarks ON windows.active_profile_id = profile_bookmarks.id %@"
- "T@\"<WBReusableTab>\",R,N,V_reusableTab"
- "URLByDeletingLastPathComponent"
- "ok"
- "safari_ensureDirectoryExists:"

```
