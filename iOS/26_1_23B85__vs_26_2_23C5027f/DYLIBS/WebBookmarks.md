## WebBookmarks

> `/System/Library/PrivateFrameworks/WebBookmarks.framework/WebBookmarks`

```diff

-622.2.11.10.8
-  __TEXT.__text: 0xa234c
-  __TEXT.__auth_stubs: 0xde0
-  __TEXT.__objc_methlist: 0x840c
+623.1.12.10.4
+  __TEXT.__text: 0xa0598
+  __TEXT.__auth_stubs: 0xec0
+  __TEXT.__objc_methlist: 0x828c
   __TEXT.__const: 0x326
-  __TEXT.__gcc_except_tab: 0xb4b0
-  __TEXT.__cstring: 0xe26c
-  __TEXT.__oslogstring: 0x87c2
+  __TEXT.__gcc_except_tab: 0xb80c
+  __TEXT.__cstring: 0xe24c
+  __TEXT.__oslogstring: 0x8d8d
   __TEXT.__dlopen_cstrs: 0xb2
   __TEXT.__constg_swiftt: 0x60
   __TEXT.__swift5_typeref: 0x9
   __TEXT.__swift5_reflstr: 0x1c
   __TEXT.__swift5_fieldmd: 0x1c
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x4210
-  __TEXT.__objc_classname: 0x9a7
-  __TEXT.__objc_methname: 0x15c77
-  __TEXT.__objc_methtype: 0x26f8
-  __TEXT.__objc_stubs: 0xeb40
-  __DATA_CONST.__got: 0x790
-  __DATA_CONST.__const: 0x2e38
-  __DATA_CONST.__objc_classlist: 0x220
+  __TEXT.__unwind_info: 0x4278
+  __TEXT.__objc_classname: 0x988
+  __TEXT.__objc_methname: 0x15d6f
+  __TEXT.__objc_methtype: 0x2749
+  __TEXT.__objc_stubs: 0xeae0
+  __DATA_CONST.__got: 0x798
+  __DATA_CONST.__const: 0x2e80
+  __DATA_CONST.__objc_classlist: 0x218
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x100
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4c90
+  __DATA_CONST.__objc_selrefs: 0x4ce0
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x1d0
+  __DATA_CONST.__objc_superrefs: 0x1c8
   __DATA_CONST.__objc_arraydata: 0x350
-  __AUTH_CONST.__auth_got: 0x708
-  __AUTH_CONST.__const: 0x11c0
-  __AUTH_CONST.__cfstring: 0x60a0
-  __AUTH_CONST.__objc_const: 0x9a48
+  __AUTH_CONST.__auth_got: 0x778
+  __AUTH_CONST.__const: 0xfe0
+  __AUTH_CONST.__cfstring: 0x5e80
+  __AUTH_CONST.__objc_const: 0x9720
   __AUTH_CONST.__objc_intobj: 0x360
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_arrayobj: 0xd8
   __AUTH.__objc_data: 0x50
   __AUTH.__data: 0xb8
-  __DATA.__objc_ivar: 0x5f4
-  __DATA.__data: 0xf18
-  __DATA.__bss: 0x11c
-  __DATA_DIRTY.__objc_data: 0x14a0
+  __DATA.__objc_ivar: 0x5d4
+  __DATA.__data: 0xf48
+  __DATA.__bss: 0xbc
+  __DATA_DIRTY.__objc_data: 0x1450
   __DATA_DIRTY.__data: 0x10
-  __DATA_DIRTY.__bss: 0x250
+  __DATA_DIRTY.__bss: 0x1d0
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreImage.framework/CoreImage

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 5C9D5510-23EC-365D-8574-F7FE1B886507
-  Functions: 3579
-  Symbols:   12223
-  CStrings:  6347
+  UUID: 3FDE86AD-B5E4-3F5B-A2DE-3247621BEA91
+  Functions: 3503
+  Symbols:   12036
+  CStrings:  6340
 
Symbols:
+ +[WebBookmarkCollection _deviceIdentifierManagerForCloudKitWithCollectionType:]
+ +[WebBookmarkCollection deviceIdentifierManagerForCloudKitWithCollectionType:generateIfNeeded:]
+ -[WBBookmarkDBAccess generateChangesForAllRecordsWithDatabase:]
+ -[WBTabGroupManager _tabWithUUIDIncludingFallbackSearch:]
+ -[WBTabGroupManager _tabWithUUIDIncludingFallbackSearch:].cold.1
+ -[WBTabGroupManager initWithCollection:profileDataManager:]
+ -[WBTabGroupManager profileDataManager]
+ -[WebBookmark isSpecialFolder]
+ -[WebBookmarkCollection _boolForDatabaseProperty:]
+ -[WebBookmarkCollection _dataForDatabaseProperty:]
+ -[WebBookmarkCollection _databasePropertySelectStatementForKey:]
+ -[WebBookmarkCollection _databasePropertyUpdateStatementForKey:]
+ -[WebBookmarkCollection _deviceIdentifierDidChange:]
+ -[WebBookmarkCollection _doubleForDatabaseProperty:]
+ -[WebBookmarkCollection _hasValueForKey:]
+ -[WebBookmarkCollection _insertTombstoneWithServerID:itemType:subtype:orderIndex:syncData:]
+ -[WebBookmarkCollection _integerForDatabaseProperty:]
+ -[WebBookmarkCollection _isBookmarkMarkedAsReadingListItem:]
+ -[WebBookmarkCollection _isSafariVersionAffected]
+ -[WebBookmarkCollection _isVersionInTargetRange:]
+ -[WebBookmarkCollection _markCleanupAsCompleted]
+ -[WebBookmarkCollection _migrateReadingListMarkedFromBookmarksFolder:excludingFolderID:]
+ -[WebBookmarkCollection _migrateSchemaVersion56Or57Or58ToVersion59]
+ -[WebBookmarkCollection _migrateSchemaVersion59Or60ToVersion61]
+ -[WebBookmarkCollection _orderByClauseForArchiveQuery]
+ -[WebBookmarkCollection _performReadingListMigration]
+ -[WebBookmarkCollection _performReadingListMigration].cold.1
+ -[WebBookmarkCollection _removeValueForKey:]
+ -[WebBookmarkCollection _removeValuesForKeyPrefix:]
+ -[WebBookmarkCollection _setBool:forDatabaseProperty:]
+ -[WebBookmarkCollection _setData:forDatabaseProperty:]
+ -[WebBookmarkCollection _setDouble:forDatabaseProperty:]
+ -[WebBookmarkCollection _setInteger:forDatabaseProperty:]
+ -[WebBookmarkCollection _setString:forDatabaseProperty:]
+ -[WebBookmarkCollection _stringForDatabaseProperty:]
+ -[WebBookmarkCollection _whereClauseForArchiveMode:]
+ -[WebBookmarkCollection _whereClauseForArchiveMode:automaticArchivingEnabled:]
+ -[WebBookmarkCollection migrateBookmarksMarkedAsReadingListItemsIfNeeded]
+ GCC_except_table137
+ GCC_except_table207
+ GCC_except_table236
+ GCC_except_table302
+ GCC_except_table306
+ GCC_except_table312
+ GCC_except_table313
+ GCC_except_table318
+ GCC_except_table320
+ GCC_except_table322
+ GCC_except_table323
+ GCC_except_table326
+ GCC_except_table328
+ GCC_except_table329
+ GCC_except_table334
+ GCC_except_table362
+ GCC_except_table365
+ GCC_except_table366
+ GCC_except_table367
+ GCC_except_table369
+ GCC_except_table379
+ GCC_except_table380
+ GCC_except_table383
+ GCC_except_table384
+ GCC_except_table401
+ GCC_except_table410
+ GCC_except_table411
+ GCC_except_table412
+ GCC_except_table413
+ GCC_except_table415
+ GCC_except_table416
+ GCC_except_table418
+ GCC_except_table422
+ GCC_except_table438
+ GCC_except_table440
+ GCC_except_table444
+ GCC_except_table456
+ GCC_except_table459
+ GCC_except_table460
+ GCC_except_table474
+ GCC_except_table493
+ GCC_except_table495
+ GCC_except_table496
+ GCC_except_table501
+ GCC_except_table506
+ GCC_except_table509
+ GCC_except_table519
+ GCC_except_table520
+ GCC_except_table521
+ GCC_except_table522
+ GCC_except_table525
+ GCC_except_table527
+ GCC_except_table528
+ GCC_except_table529
+ GCC_except_table530
+ GCC_except_table533
+ GCC_except_table534
+ GCC_except_table535
+ GCC_except_table536
+ GCC_except_table537
+ GCC_except_table538
+ GCC_except_table539
+ GCC_except_table540
+ GCC_except_table541
+ GCC_except_table548
+ GCC_except_table555
+ GCC_except_table556
+ _OBJC_CLASS_$_WBSAnalyticsLogger
+ _OBJC_CLASS_$_WBSDeviceIdentifierManager
+ _WBSDeviceIdentifierManagerDidChangeNotification
+ _WBSOSLogBookmarkSync
+ _WBSOSLogBookmarks
+ _WBSOSLogCloudBookmarks
+ _WBSOSLogCloudSettings
+ _WBSOSLogCycler
+ _WBSOSLogDataMigration
+ _WBSOSLogDatabaseJournal
+ _WBSOSLogExport
+ _WBSOSLogImport
+ _WBSOSLogProfiles
+ _WBSOSLogReadingList
+ _WBSOSLogReadingListIcons
+ _WBSOSLogTabGroup
+ _WBSOSLogTabs
+ _WBSOSLogWebBookmarkServer
+ _WBSOSLogWebsiteData
+ __OBJC_CLASS_PROTOCOLS_$_WebBookmark
+ __ZGVZL19sqliteTraceCallbackjPvS_S_E11persistLogs
+ __ZGVZL49collectionTypeToDeviceIdentifierManagerDictionaryvE10dictionary
+ __ZL19sqliteTraceCallbackjPvS_S_
+ __ZL19sqliteTraceCallbackjPvS_S_.cold.1
+ __ZL49collectionTypeToDeviceIdentifierManagerDictionaryv
+ __ZZL19sqliteTraceCallbackjPvS_S_E11persistLogs
+ __ZZL49collectionTypeToDeviceIdentifierManagerDictionaryvE10dictionary
+ ___151-[WBTabGroupManager _performCRDTMergeAndMapTabsToParentIdentifiersWithProfilesByIdentifier:devicesByUUID:uninsertedSyncableTabsFromSyncableTabsByUUID:]_block_invoke.56
+ ___32-[WBMutableTabGroup deleteTabs:]_block_invoke.16
+ ___52-[WebBookmarkCollection _deviceIdentifierDidChange:]_block_invoke
+ ___57-[WBTabGroupManager _tabWithUUIDIncludingFallbackSearch:]_block_invoke
+ ___57-[WebBookmarkCollection _updateBookmarks:inFolderWithID:]_block_invoke.417
+ ___57-[WebBookmarkCollection _updateBookmarks:inFolderWithID:]_block_invoke.419
+ ___57-[WebBookmarkCollection _updateBookmarks:inFolderWithID:]_block_invoke.419.cold.1
+ ___57-[WebBookmarkCollection _updateBookmarks:inFolderWithID:]_block_invoke.419.cold.2
+ ___57-[WebBookmarkCollection _updateBookmarks:inFolderWithID:]_block_invoke.419.cold.3
+ ___57-[WebBookmarkCollection _updateBookmarks:inFolderWithID:]_block_invoke.419.cold.4
+ ___57-[WebBookmarkCollection _updateBookmarks:inFolderWithID:]_block_invoke_2.420
+ ___59-[WBTabGroupManager initWithCollection:profileDataManager:]_block_invoke
+ ___68-[WBTabGroupManager _dequeueNextAcceptCloudKitShareMetadataIfNeeded]_block_invoke.156
+ ___69-[WBTabGroupManager updateTabsInTabGroupWithUUID:options:usingBlock:]_block_invoke.147
+ ___80-[WBTabGroupManager _reloadProfilesAndTabGroupsAndNotify:withCompletionHandler:]_block_invoke.50
+ ___95+[WebBookmarkCollection deviceIdentifierManagerForCloudKitWithCollectionType:generateIfNeeded:]_block_invoke
+ ___95+[WebBookmarkCollection deviceIdentifierManagerForCloudKitWithCollectionType:generateIfNeeded:]_block_invoke.cold.1
+ ___95+[WebBookmarkCollection deviceIdentifierManagerForCloudKitWithCollectionType:generateIfNeeded:]_block_invoke_2
+ ___Block_byref_object_copy_.1891
+ ___Block_byref_object_dispose_.1892
+ ____ZL33prefixEndingWithFirstWordOfStringP8NSString_block_invoke.1894
+ ___block_descriptor_40_e8_32s_e22_B16?0"WBMutableTab"8ls32l8
+ ___block_descriptor_40_ea8_32s_e24_B24?0"WebBookmark"8q16ls32l8
+ ___block_descriptor_56_ea8_32s40s48s_e24_B24?0"WebBookmark"8q16ls32l8s40l8s48l8
+ ___block_descriptor_64_ea8_32s40s48s56r_e5_v8?0ls32l8s40l8s48l8r56l8
+ ___block_literal_global.1064
+ ___block_literal_global.108
+ ___block_literal_global.1134
+ ___block_literal_global.1144
+ ___block_literal_global.1146
+ ___block_literal_global.115
+ ___block_literal_global.117
+ ___block_literal_global.124
+ ___block_literal_global.126
+ ___block_literal_global.163
+ ___block_literal_global.18
+ ___block_literal_global.1883
+ ___block_literal_global.1889
+ ___block_literal_global.1896
+ ___block_literal_global.1910
+ ___block_literal_global.239
+ ___block_literal_global.288
+ ___block_literal_global.291
+ ___block_literal_global.293
+ ___block_literal_global.295
+ ___block_literal_global.298
+ ___block_literal_global.303
+ ___block_literal_global.305
+ ___block_literal_global.308
+ ___block_literal_global.313
+ ___block_literal_global.315
+ ___block_literal_global.318
+ ___block_literal_global.462
+ ___block_literal_global.59
+ ___block_literal_global.61
+ ___block_literal_global.68
+ ___block_literal_global.91
+ ___block_literal_global.93
+ ___block_literal_global.96
+ _kWebBookmarksExtensionEnabledKey
+ _kWebBookmarksExtensionIdentifiersKey
+ _kWebBookmarksGetExtensionEnabledState
+ _kWebBookmarksNoExtensionFoundKey
+ _kWebBookmarksOpenSafariWebExtensionsSettings
+ _kWebBookmarksSFSafariSettingsCallingAppBundleIDKey
+ _kWebBookmarksSFSafariSettingsFailedKey
+ _kWebBookmarksSFSafariSettingsMissingEntitlementKey
+ _kWebBookmarksSFSafariSettingsNotRunningForegroundKey
+ _kWebBookmarksSFSafariSettingsTestingModeKey
+ _objc_msgSend$_databasePropertySelectStatementForKey:
+ _objc_msgSend$_databasePropertyUpdateStatementForKey:
+ _objc_msgSend$_deviceIdentifierManagerForCloudKitWithCollectionType:
+ _objc_msgSend$_insertTombstoneWithServerID:itemType:subtype:orderIndex:syncData:
+ _objc_msgSend$_isBookmarkMarkedAsReadingListItem:
+ _objc_msgSend$_isSafariVersionAffected
+ _objc_msgSend$_isVersionInTargetRange:
+ _objc_msgSend$_markCleanupAsCompleted
+ _objc_msgSend$_migrateReadingListMarkedFromBookmarksFolder:excludingFolderID:
+ _objc_msgSend$_migrateSchemaVersion56Or57Or58ToVersion59
+ _objc_msgSend$_migrateSchemaVersion59Or60ToVersion61
+ _objc_msgSend$_orderByClauseForArchiveQuery
+ _objc_msgSend$_performReadingListMigration
+ _objc_msgSend$_tabWithUUIDIncludingFallbackSearch:
+ _objc_msgSend$_whereClauseForArchiveMode:
+ _objc_msgSend$_whereClauseForArchiveMode:automaticArchivingEnabled:
+ _objc_msgSend$clearDeviceIdentifier
+ _objc_msgSend$deviceIdentifierManagerForCloudKitWithCollectionType:generateIfNeeded:
+ _objc_msgSend$didFailToMigratePlist
+ _objc_msgSend$didMigrateDeviceIdentifier
+ _objc_msgSend$fileURLWithPath:isDirectory:
+ _objc_msgSend$initWithCollection:profileDataManager:
+ _objc_msgSend$initWithKey:readOnly:
+ _objc_msgSend$migrateFromPlistAtURLIfNeeded:
+ _objc_msgSend$migrateToBookmarkItem
+ _objc_msgSend$reportUnexpectedTabDeletionWithPreviousTabCount:newTabCount:stackTrace:
+ _objc_msgSend$safari_callStackChunksWithMaxLength:
+ _objc_msgSend$sharedLogger
+ _objc_msgSend$shouldMigrateDeviceIdentifier
+ _objc_msgSend$shouldShowInternalUI
+ _objc_msgSend$startObservingChanges
+ _objc_msgSend$synchronize
+ _sqlite3_expanded_sql
+ _sqlite3_free
+ _sqlite3_get_autocommit
+ _sqlite3_trace_v2
- +[WBBookmarkLabel supportsSecureCoding]
- +[WBBookmarkLocation supportsSecureCoding]
- +[WBBrowserState supportsSecureCoding]
- +[WBLocalTabAttributes supportsSecureCoding]
- +[WBTab supportsSecureCoding]
- +[WBTabGroup supportsSecureCoding]
- +[WBWindowState supportsSecureCoding]
- +[WebBookmark(Internal) supportsSecureCoding]
- +[WebBookmarkChange supportsSecureCoding]
- +[WebBookmarkChangeSet supportsSecureCoding]
- +[WebBookmarkCollection _deviceIdentifierForCloudKitWithCollectionType:]
- +[WebBookmarkCollection deviceIdentifierForCloudKitWithCollectionType:generateIfNeeded:]
- +[WebBookmarkDeviceIdentifier _postWebBookmarkMetaDataChangeDistributedNotification:]
- +[WebBookmarkDeviceIdentifier clearDeviceIdentifierWithPlistURL:]
- -[WBBookmarkDBAccess addItem:underFolderWithServerId:database:].cold.1
- -[WBBookmarkDBAccess beginMergingChangesWithDatabase:]
- -[WBBookmarkDBAccess finishMergingChangesWithDatabase:]
- -[WBBookmarkLabel encodeWithCoder:]
- -[WBBookmarkLabel initWithCoder:]
- -[WBBookmarkLocation encodeWithCoder:]
- -[WBBookmarkLocation initWithCoder:]
- -[WBBrowserState encodeWithCoder:]
- -[WBBrowserState initWithCoder:]
- -[WBLocalTabAttributes encodeWithCoder:]
- -[WBLocalTabAttributes initWithCoder:]
- -[WBTab encodeWithCoder:]
- -[WBTab initWithCoder:]
- -[WBTabGroup encodeWithCoder:]
- -[WBTabGroup initWithCoder:]
- -[WBWindowState encodeWithCoder:]
- -[WBWindowState initWithCoder:]
- -[WebBookmark(Internal) encodeWithCoder:]
- -[WebBookmark(Internal) initWithCoder:]
- -[WebBookmarkChange encodeWithCoder:]
- -[WebBookmarkChange initWithCoder:]
- -[WebBookmarkChangeSet encodeWithCoder:]
- -[WebBookmarkChangeSet initWithCoder:]
- -[WebBookmarkCollection _insertTombstoneWithServerID:itemType:subtype:syncData:]
- -[WebBookmarkCollection _mergeCandidateBookmarkWithTitle:address:parent:mergeMode:]
- -[WebBookmarkCollection _mergeCandidateFolderWithTitle:parent:mergeMode:]
- -[WebBookmarkCollection _mergeMode]
- -[WebBookmarkCollection _metaDataFileChanged:]
- -[WebBookmarkCollection _setMergeMode:]
- -[WebBookmarkCollection isMerging]
- -[WebBookmarkDeviceIdentifier .cxx_destruct]
- -[WebBookmarkDeviceIdentifier UUID]
- -[WebBookmarkDeviceIdentifier _cancelMonitoringMetaDataFile]
- -[WebBookmarkDeviceIdentifier _createOrLoadMetaData]
- -[WebBookmarkDeviceIdentifier _createOrLoadMetaData].cold.1
- -[WebBookmarkDeviceIdentifier _createOrLoadMetaData].cold.2
- -[WebBookmarkDeviceIdentifier _listensForMetaDataChangeNotification]
- -[WebBookmarkDeviceIdentifier _metaDataDidChange:]
- -[WebBookmarkDeviceIdentifier _resumeMonitoringMetaDataFile]
- -[WebBookmarkDeviceIdentifier _setListensForMetaDataChangeNotification:]
- -[WebBookmarkDeviceIdentifier _setUpWithPlistURL:readOnly:queue:]
- -[WebBookmarkDeviceIdentifier dealloc]
- -[WebBookmarkDeviceIdentifier description]
- -[WebBookmarkDeviceIdentifier encounteredErrorWhileObtainingUUID]
- -[WebBookmarkDeviceIdentifier initWithPlistURL:readOnly:]
- -[WebBookmarkDeviceIdentifier isReadOnly]
- -[WebBookmarkDeviceIdentifier setReadOnly:]
- -[WebBookmarkDeviceIdentifier stopObservingChanges]
- GCC_except_table189
- GCC_except_table219
- GCC_except_table240
- GCC_except_table246
- GCC_except_table249
- GCC_except_table25
- GCC_except_table253
- GCC_except_table263
- GCC_except_table277
- GCC_except_table278
- GCC_except_table288
- GCC_except_table293
- GCC_except_table298
- GCC_except_table304
- GCC_except_table309
- GCC_except_table321
- GCC_except_table331
- GCC_except_table332
- GCC_except_table337
- GCC_except_table339
- GCC_except_table341
- GCC_except_table342
- GCC_except_table344
- GCC_except_table345
- GCC_except_table347
- GCC_except_table354
- GCC_except_table382
- GCC_except_table389
- GCC_except_table393
- GCC_except_table399
- GCC_except_table400
- GCC_except_table403
- GCC_except_table404
- GCC_except_table408
- GCC_except_table421
- GCC_except_table425
- GCC_except_table426
- GCC_except_table427
- GCC_except_table430
- GCC_except_table432
- GCC_except_table433
- GCC_except_table435
- GCC_except_table439
- GCC_except_table457
- GCC_except_table472
- GCC_except_table473
- GCC_except_table476
- GCC_except_table477
- GCC_except_table478
- GCC_except_table491
- GCC_except_table510
- GCC_except_table512
- GCC_except_table513
- _OBJC_CLASS_$_WebBookmarkDeviceIdentifier
- _OBJC_IVAR_$_WebBookmarkCollection._mergeMode
- _OBJC_IVAR_$_WebBookmarkDeviceIdentifier._UUID
- _OBJC_IVAR_$_WebBookmarkDeviceIdentifier._encounteredErrorWhileObtainingUUID
- _OBJC_IVAR_$_WebBookmarkDeviceIdentifier._fileMonitor
- _OBJC_IVAR_$_WebBookmarkDeviceIdentifier._listensForMetaDataChangeNotification
- _OBJC_IVAR_$_WebBookmarkDeviceIdentifier._plistURL
- _OBJC_IVAR_$_WebBookmarkDeviceIdentifier._queue
- _OBJC_IVAR_$_WebBookmarkDeviceIdentifier._readOnly
- _OBJC_METACLASS_$_WebBookmarkDeviceIdentifier
- _WBS_LOG_CHANNEL_PREFIXBookmarkSync
- _WBS_LOG_CHANNEL_PREFIXBookmarkSync.cold.1
- _WBS_LOG_CHANNEL_PREFIXBookmarkSync.log
- _WBS_LOG_CHANNEL_PREFIXBookmarkSync.onceToken
- _WBS_LOG_CHANNEL_PREFIXBookmarks
- _WBS_LOG_CHANNEL_PREFIXBookmarks.cold.1
- _WBS_LOG_CHANNEL_PREFIXBookmarks.log
- _WBS_LOG_CHANNEL_PREFIXBookmarks.onceToken
- _WBS_LOG_CHANNEL_PREFIXCloudBookmarks
- _WBS_LOG_CHANNEL_PREFIXCloudBookmarks.cold.1
- _WBS_LOG_CHANNEL_PREFIXCloudBookmarks.log
- _WBS_LOG_CHANNEL_PREFIXCloudBookmarks.onceToken
- _WBS_LOG_CHANNEL_PREFIXCloudSettings
- _WBS_LOG_CHANNEL_PREFIXCloudSettings.cold.1
- _WBS_LOG_CHANNEL_PREFIXCloudSettings.log
- _WBS_LOG_CHANNEL_PREFIXCloudSettings.onceToken
- _WBS_LOG_CHANNEL_PREFIXCycler
- _WBS_LOG_CHANNEL_PREFIXCycler.cold.1
- _WBS_LOG_CHANNEL_PREFIXCycler.log
- _WBS_LOG_CHANNEL_PREFIXCycler.onceToken
- _WBS_LOG_CHANNEL_PREFIXDataMigration
- _WBS_LOG_CHANNEL_PREFIXDataMigration.cold.1
- _WBS_LOG_CHANNEL_PREFIXDataMigration.log
- _WBS_LOG_CHANNEL_PREFIXDataMigration.onceToken
- _WBS_LOG_CHANNEL_PREFIXExport
- _WBS_LOG_CHANNEL_PREFIXExport.cold.1
- _WBS_LOG_CHANNEL_PREFIXExport.log
- _WBS_LOG_CHANNEL_PREFIXExport.onceToken
- _WBS_LOG_CHANNEL_PREFIXImport
- _WBS_LOG_CHANNEL_PREFIXImport.cold.1
- _WBS_LOG_CHANNEL_PREFIXImport.log
- _WBS_LOG_CHANNEL_PREFIXImport.onceToken
- _WBS_LOG_CHANNEL_PREFIXProfiles
- _WBS_LOG_CHANNEL_PREFIXProfiles.cold.1
- _WBS_LOG_CHANNEL_PREFIXProfiles.log
- _WBS_LOG_CHANNEL_PREFIXProfiles.onceToken
- _WBS_LOG_CHANNEL_PREFIXReadingList
- _WBS_LOG_CHANNEL_PREFIXReadingList.cold.1
- _WBS_LOG_CHANNEL_PREFIXReadingList.log
- _WBS_LOG_CHANNEL_PREFIXReadingList.onceToken
- _WBS_LOG_CHANNEL_PREFIXReadingListIcons
- _WBS_LOG_CHANNEL_PREFIXReadingListIcons.cold.1
- _WBS_LOG_CHANNEL_PREFIXReadingListIcons.log
- _WBS_LOG_CHANNEL_PREFIXReadingListIcons.onceToken
- _WBS_LOG_CHANNEL_PREFIXTabGroup
- _WBS_LOG_CHANNEL_PREFIXTabGroup.cold.1
- _WBS_LOG_CHANNEL_PREFIXTabGroup.log
- _WBS_LOG_CHANNEL_PREFIXTabGroup.onceToken
- _WBS_LOG_CHANNEL_PREFIXTabs
- _WBS_LOG_CHANNEL_PREFIXTabs.cold.1
- _WBS_LOG_CHANNEL_PREFIXTabs.log
- _WBS_LOG_CHANNEL_PREFIXTabs.onceToken
- _WBS_LOG_CHANNEL_PREFIXWebBookmarkServer
- _WBS_LOG_CHANNEL_PREFIXWebBookmarkServer.cold.1
- _WBS_LOG_CHANNEL_PREFIXWebBookmarkServer.log
- _WBS_LOG_CHANNEL_PREFIXWebBookmarkServer.onceToken
- _WBS_LOG_CHANNEL_PREFIXWebsiteData
- _WBS_LOG_CHANNEL_PREFIXWebsiteData.cold.1
- _WBS_LOG_CHANNEL_PREFIXWebsiteData.log
- _WBS_LOG_CHANNEL_PREFIXWebsiteData.onceToken
- __OBJC_$_CLASS_METHODS_WBBookmarkLabel
- __OBJC_$_CLASS_METHODS_WBBookmarkLocation
- __OBJC_$_CLASS_METHODS_WBBrowserState
- __OBJC_$_CLASS_METHODS_WBLocalTabAttributes
- __OBJC_$_CLASS_METHODS_WBTabGroup
- __OBJC_$_CLASS_METHODS_WBWindowState
- __OBJC_$_CLASS_METHODS_WebBookmarkChangeSet
- __OBJC_$_CLASS_METHODS_WebBookmarkDeviceIdentifier
- __OBJC_$_CLASS_PROP_LIST_WBBookmarkLabel
- __OBJC_$_CLASS_PROP_LIST_WBBookmarkLocation
- __OBJC_$_CLASS_PROP_LIST_WBBrowserState
- __OBJC_$_CLASS_PROP_LIST_WBLocalTabAttributes
- __OBJC_$_CLASS_PROP_LIST_WBTab
- __OBJC_$_CLASS_PROP_LIST_WBTabGroup
- __OBJC_$_CLASS_PROP_LIST_WBWindowState
- __OBJC_$_CLASS_PROP_LIST_WebBookmarkChange
- __OBJC_$_CLASS_PROP_LIST_WebBookmarkChangeSet
- __OBJC_$_INSTANCE_METHODS_WebBookmarkDeviceIdentifier
- __OBJC_$_INSTANCE_VARIABLES_WebBookmarkDeviceIdentifier
- __OBJC_$_PROP_LIST_WebBookmarkDeviceIdentifier
- __OBJC_CLASS_PROTOCOLS_$_WBBrowserState
- __OBJC_CLASS_PROTOCOLS_$_WebBookmark(Internal|ReadingList|ReadingListArchives|ReadingListInternal)
- __OBJC_CLASS_PROTOCOLS_$_WebBookmarkChangeSet
- __OBJC_CLASS_RO_$_WebBookmarkDeviceIdentifier
- __OBJC_METACLASS_RO_$_WebBookmarkDeviceIdentifier
- __ZGVZL42collectionTypeToDeviceIdentifierDictionaryvE10dictionary
- __ZL42collectionTypeToDeviceIdentifierDictionaryv
- __ZZL42collectionTypeToDeviceIdentifierDictionaryvE10dictionary
- ___151-[WBTabGroupManager _performCRDTMergeAndMapTabsToParentIdentifiersWithProfilesByIdentifier:devicesByUUID:uninsertedSyncableTabsFromSyncableTabsByUUID:]_block_invoke_3
- ___32-[WBMutableTabGroup deleteTabs:]_block_invoke.9
- ___35-[WebBookmarkDeviceIdentifier UUID]_block_invoke
- ___40-[WBTabGroupManager initWithCollection:]_block_invoke
- ___40-[WebBookmarkChangeSet encodeWithCoder:]_block_invoke
- ___46-[WebBookmarkCollection _metaDataFileChanged:]_block_invoke
- ___50-[WebBookmarkDeviceIdentifier _metaDataDidChange:]_block_invoke
- ___51-[WebBookmarkDeviceIdentifier stopObservingChanges]_block_invoke
- ___52-[WebBookmarkDeviceIdentifier _createOrLoadMetaData]_block_invoke
- ___57-[WebBookmarkCollection _updateBookmarks:inFolderWithID:]_block_invoke.404
- ___57-[WebBookmarkCollection _updateBookmarks:inFolderWithID:]_block_invoke.406
- ___57-[WebBookmarkCollection _updateBookmarks:inFolderWithID:]_block_invoke.406.cold.1
- ___57-[WebBookmarkCollection _updateBookmarks:inFolderWithID:]_block_invoke.406.cold.2
- ___57-[WebBookmarkCollection _updateBookmarks:inFolderWithID:]_block_invoke.406.cold.3
- ___57-[WebBookmarkCollection _updateBookmarks:inFolderWithID:]_block_invoke.406.cold.4
- ___57-[WebBookmarkCollection _updateBookmarks:inFolderWithID:]_block_invoke_2.407
- ___60-[WebBookmarkDeviceIdentifier _resumeMonitoringMetaDataFile]_block_invoke
- ___60-[WebBookmarkDeviceIdentifier _resumeMonitoringMetaDataFile]_block_invoke.16
- ___65-[WebBookmarkDeviceIdentifier _setUpWithPlistURL:readOnly:queue:]_block_invoke
- ___65-[WebBookmarkDeviceIdentifier encounteredErrorWhileObtainingUUID]_block_invoke
- ___68-[WBTabGroupManager _dequeueNextAcceptCloudKitShareMetadataIfNeeded]_block_invoke.148
- ___69-[WBTabGroupManager updateTabsInTabGroupWithUUID:options:usingBlock:]_block_invoke_3
- ___80-[WBTabGroupManager _reloadProfilesAndTabGroupsAndNotify:withCompletionHandler:]_block_invoke_3.50
- ___88+[WebBookmarkCollection deviceIdentifierForCloudKitWithCollectionType:generateIfNeeded:]_block_invoke
- ___88+[WebBookmarkCollection deviceIdentifierForCloudKitWithCollectionType:generateIfNeeded:]_block_invoke.cold.1
- ___Block_byref_object_copy_.1855
- ___Block_byref_object_dispose_.1856
- ___WBS_LOG_CHANNEL_PREFIXBookmarkSync_block_invoke
- ___WBS_LOG_CHANNEL_PREFIXBookmarks_block_invoke
- ___WBS_LOG_CHANNEL_PREFIXCloudBookmarks_block_invoke
- ___WBS_LOG_CHANNEL_PREFIXCloudSettings_block_invoke
- ___WBS_LOG_CHANNEL_PREFIXCycler_block_invoke
- ___WBS_LOG_CHANNEL_PREFIXDataMigration_block_invoke
- ___WBS_LOG_CHANNEL_PREFIXExport_block_invoke
- ___WBS_LOG_CHANNEL_PREFIXImport_block_invoke
- ___WBS_LOG_CHANNEL_PREFIXProfiles_block_invoke
- ___WBS_LOG_CHANNEL_PREFIXReadingListIcons_block_invoke
- ___WBS_LOG_CHANNEL_PREFIXReadingList_block_invoke
- ___WBS_LOG_CHANNEL_PREFIXTabGroup_block_invoke
- ___WBS_LOG_CHANNEL_PREFIXTabs_block_invoke
- ___WBS_LOG_CHANNEL_PREFIXWebBookmarkServer_block_invoke
- ___WBS_LOG_CHANNEL_PREFIXWebsiteData_block_invoke
- ____ZL33prefixEndingWithFirstWordOfStringP8NSString_block_invoke.1858
- ___block_descriptor_36_e5_v8?0l
- ___block_descriptor_56_ea8_32s40s48s_e21_B16?0"WebBookmark"8ls32l8s40l8s48l8
- ___block_literal_global.10
- ___block_literal_global.1061
- ___block_literal_global.107
- ___block_literal_global.1131
- ___block_literal_global.114
- ___block_literal_global.1141
- ___block_literal_global.1143
- ___block_literal_global.116
- ___block_literal_global.12
- ___block_literal_global.123
- ___block_literal_global.125
- ___block_literal_global.13
- ___block_literal_global.155
- ___block_literal_global.1850
- ___block_literal_global.1853
- ___block_literal_global.1860
- ___block_literal_global.1868
- ___block_literal_global.233
- ___block_literal_global.26
- ___block_literal_global.28
- ___block_literal_global.294
- ___block_literal_global.297
- ___block_literal_global.299
- ___block_literal_global.304
- ___block_literal_global.307
- ___block_literal_global.309
- ___block_literal_global.31
- ___block_literal_global.314
- ___block_literal_global.317
- ___block_literal_global.319
- ___block_literal_global.324
- ___block_literal_global.327
- ___block_literal_global.37
- ___block_literal_global.4
- ___block_literal_global.40
- ___block_literal_global.452
- ___block_literal_global.52
- ___block_literal_global.57
- ___block_literal_global.60
- ___block_literal_global.67
- ___block_literal_global.7
- ___block_literal_global.70
- ___block_literal_global.73
- ___block_literal_global.90
- ___block_literal_global.92
- ___block_literal_global.95
- __dispatch_source_type_vnode
- _dispatch_resume
- _dispatch_source_cancel
- _dispatch_source_create
- _dispatch_source_set_cancel_handler
- _dispatch_source_set_event_handler
- _kWebBookmarksOpenSafariExportSettingsFailedKey
- _kWebBookmarksOpenSafariExportSettingsMissingEntitlementKey
- _kWebBookmarksOpenSafariExportSettingsNotRunningForegroundKey
- _kWebBookmarksOpenSafariExportSettingsTestingModeKey
- _objc_msgSend$_cancelMonitoringMetaDataFile
- _objc_msgSend$_createOrLoadMetaData
- _objc_msgSend$_deviceIdentifierForCloudKitWithCollectionType:
- _objc_msgSend$_insertTombstoneWithServerID:itemType:subtype:syncData:
- _objc_msgSend$_mergeCandidateBookmarkWithTitle:address:parent:mergeMode:
- _objc_msgSend$_mergeCandidateFolderWithTitle:parent:mergeMode:
- _objc_msgSend$_mergeMode
- _objc_msgSend$_postWebBookmarkMetaDataChangeDistributedNotification:
- _objc_msgSend$_resumeMonitoringMetaDataFile
- _objc_msgSend$_setListensForMetaDataChangeNotification:
- _objc_msgSend$_setMergeMode:
- _objc_msgSend$_setUpWithPlistURL:readOnly:queue:
- _objc_msgSend$addChanges:
- _objc_msgSend$clearDeviceIdentifierWithPlistURL:
- _objc_msgSend$decodeDoubleForKey:
- _objc_msgSend$decodeInt32ForKey:
- _objc_msgSend$decodeIntForKey:
- _objc_msgSend$deviceIdentifierForCloudKitWithCollectionType:generateIfNeeded:
- _objc_msgSend$dictionaryWithContentsOfURL:
- _objc_msgSend$encodeDouble:forKey:
- _objc_msgSend$encodeInt32:forKey:
- _objc_msgSend$encodeInt:forKey:
- _objc_msgSend$encounteredErrorWhileObtainingUUID
- _objc_msgSend$fileSystemRepresentation
- _objc_msgSend$initWithArray:
- _objc_msgSend$initWithPlistURL:readOnly:
- _objc_msgSend$initWithProfileProvider:
- _objc_msgSend$isInternalInstall
- _objc_msgSend$isMerging
- _objc_msgSend$isSafariProfilesEnabled
- _objc_msgSend$removeObserver:name:object:
- _objc_msgSend$setBookmarks:
- _objc_msgSend$setGeneration:
- _objc_msgSend$setSpecialFolderID:
- _objc_msgSend$writeToURL:atomically:
- _os_log_create
- _webBookmarksMetaDataDeviceUUIDKey
- _webBookmarksMetaDataDidChangeNotification
CStrings:
+ "\n%{public}@"
+ " ORDER BY %@"
+ "%zd"
+ "%zu tabs were filtered because they were removed. UUIDS:%{public}@"
+ "%{public}s"
+ "-[WBBookmarkDBAccess generateChangesForAllRecordsWithDatabase:]"
+ "621.1.1"
+ "623.1.12"
+ "About to perform CRDT merge: %zu profiles from DB, %zu syncable tab groups cached, %zu local tab groups cached"
+ "B24@?0@\"WebBookmark\"8q16"
+ "B28@0:8B16@20"
+ "B32@0:8d16@24"
+ "B32@0:8q16@24"
+ "B56@0:8@16q24q32q40@48"
+ "Beginning reload of profiles and tab groups, shouldNotify=%d"
+ "Bookmark (ID: %d) has isReadingListItem = YES"
+ "Bookmark clean up not required, as its not affected version"
+ "Bookmark marked as readinglist clean up completed. Migrated %lu records"
+ "Bookmark marked as readinglist clean up starting"
+ "CRDT merge collected %zu unique tab UUIDs from database"
+ "CRDT merge complete: mapped tabs to %zu parent identifiers"
+ "CRDT merge final result: %zu parent identifiers with tabs"
+ "CREATE INDEX database_properties_key_index ON database_properties (key)"
+ "CREATE TABLE database_properties (key TEXT NOT NULL, value BLOB)"
+ "CallingAppBundleIdentifier"
+ "Checking folder (ID: %d)"
+ "Clearing %zu deleted tabs"
+ "DELETE FROM database_properties WHERE key = ?"
+ "Did reset device identifier, new identifier = \"%{public}@\""
+ "ExtensionEnabled"
+ "ExtensionIdentifiers"
+ "ExtensionNotFound"
+ "FROM bookmarks WHERE deleted = 1 AND server_id IS NOT NULL AND syncable = 1 GROUP BY server_id ORDER BY order_index DESC"
+ "Found misplaced reading list item (ID: %d) in folder (ID: %d)"
+ "Found tab in tab group %{public}@ using fallback search."
+ "GetExtensionEnabledState"
+ "INSERT INTO bookmarks (order_index, type, subtype, deleted, added, parent, server_id, dav_generation, sync_data) VALUES (%zd, %ld, %ld, 1, 0, -1, ?, ?, ?)"
+ "Migration succeeded but save failed for bookmark (ID: %d)"
+ "Need another reload due to %zu missing items, reloading..."
+ "OpenSafariWebExtensionsSettings"
+ "PRAGMA user_version = 59"
+ "PRAGMA user_version = 61"
+ "PersistDatabaseJournaling"
+ "Q28@0:8@16i24"
+ "REPLACE INTO database_properties (value, key) VALUES (?, ?)"
+ "Reload complete: %zu tab groups updated, %zu tab groups removed"
+ "RemoveReadingListFromBookmarksMigration: Bookmark reading list cleanup failed, Could not access root bookmark"
+ "SELECT COUNT(*) FROM database_properties WHERE key = ?"
+ "SELECT COUNT(*) FROM folder_ancestors WHERE folder_id = %d"
+ "SELECT value FROM database_properties WHERE key = ?"
+ "SFSafariSettingsFailed"
+ "SFSafariSettingsMissingEntitlement"
+ "SFSafariSettingsNotRunningForeground"
+ "SFSafariSettingsTestingMode"
+ "Skipping reading list folder (ID: %d)"
+ "Starting CRDT merge: %zu profiles, %zu devices, %zu uninserted syncable tabs"
+ "Starting traversal from root bookmark (ID: %d), excluding reading list folder (ID: %d)"
+ "Successfully migrated and saved bookmark (ID: %d) from reading list format to bookmark format"
+ "Successfully processed %lu bookmarks starting from folder (ID: %d)"
+ "Sync finished successfully, about to reload profiles and tab groups"
+ "Sync reload completed."
+ "T@\"WBSProfileDataManager\",R,N,V_profileDataManager"
+ "TabGroups"
+ "Unable to find a tab in the cache. Using fallback search for the following UUID: %{public}@"
+ "WBSBookmarksWhichAreReadingListCleanupKey"
+ "WBTabGroupManager updateTabsInTabGroupWithUUID: after updateBlock - tabGroup has %zu tabs"
+ "WBTabGroupManager updateTabsInTabGroupWithUUID: before updateBlock - tabGroup has %zu tabs"
+ "Will reset device identifier, old identifier = \"%{public}@\""
+ "_boolForDatabaseProperty:"
+ "_dataForDatabaseProperty:"
+ "_databasePropertySelectStatementForKey:"
+ "_databasePropertyUpdateStatementForKey:"
+ "_deviceIdentifierDidChange:"
+ "_deviceIdentifierManagerForCloudKitWithCollectionType:"
+ "_doubleForDatabaseProperty:"
+ "_hasValueForKey:"
+ "_insertTombstoneWithServerID:itemType:subtype:orderIndex:syncData:"
+ "_integerForDatabaseProperty:"
+ "_isBookmarkMarkedAsReadingListItem:"
+ "_isSafariVersionAffected"
+ "_isVersionInTargetRange:"
+ "_markCleanupAsCompleted"
+ "_migrateReadingListMarkedFromBookmarksFolder:excludingFolderID:"
+ "_migrateSchemaVersion56Or57Or58ToVersion59"
+ "_migrateSchemaVersion59Or60ToVersion61"
+ "_orderByClauseForArchiveQuery"
+ "_performReadingListMigration"
+ "_removeValueForKey:"
+ "_removeValuesForKeyPrefix:"
+ "_setBool:forDatabaseProperty:"
+ "_setData:forDatabaseProperty:"
+ "_setDouble:forDatabaseProperty:"
+ "_setInteger:forDatabaseProperty:"
+ "_setString:forDatabaseProperty:"
+ "_stringForDatabaseProperty:"
+ "_tabWithUUIDIncludingFallbackSearch:"
+ "_whereClauseForArchiveMode:"
+ "_whereClauseForArchiveMode:automaticArchivingEnabled:"
+ "archive_status ASC, read ASC, locally_added DESC, order_index DESC"
+ "archive_status IN (%zd, %zd)"
+ "archive_status IN (%zd, %zd, %zd)"
+ "clearDeviceIdentifier"
+ "d24@0:8@16"
+ "deviceIdentifierManagerForCloudKitWithCollectionType:generateIfNeeded:"
+ "didFailToMigratePlist"
+ "didMigrateDeviceIdentifier"
+ "fileURLWithPath:isDirectory:"
+ "generateChangesForAllRecordsWithDatabase:"
+ "initWithCollection:profileDataManager:"
+ "initWithKey:readOnly:"
+ "isSpecialFolder"
+ "migrateBookmarksMarkedAsReadingListItemsIfNeeded"
+ "migrateFromPlistAtURLIfNeeded:"
+ "profileDataManager"
+ "reportUnexpectedTabDeletionWithPreviousTabCount:newTabCount:stackTrace:"
+ "safari_callStackChunksWithMaxLength:"
+ "setTabs called with %zu tabs on tab group: %{public}@"
+ "sharedLogger"
+ "shouldMigrateDeviceIdentifier"
+ "shouldShowInternalUI"
+ "startObservingChanges"
+ "synchronize"
+ "{BookmarkSQLStatement=^^?^{sqlite3_stmt}BBi}24@0:8@16"
+ "{unique_ptr<WebBookmarks::BookmarkSQLWriteTransaction, std::default_delete<WebBookmarks::BookmarkSQLWriteTransaction>>=\"\"{?=\"__ptr_\"^{BookmarkSQLWriteTransaction}}}"
- " ORDER BY archive_status ASC, read ASC, locally_added DESC, order_index DESC"
- "%lu tabs were filtered because they were removed. UUIDS:%{public}@"
- ", ?"
- ", sync_data"
- "<%@: %p' _UUID = %@"
- "@\"NSObject<OS_dispatch_source>\""
- "AND server_id IS NULL"
- "ArchiveStatus"
- "B48@0:8@16q24q32@40"
- "BADatabaseBeginMergingChanges"
- "BADatabaseFinishMergingChanges"
- "BookmarkSync"
- "Clearing deleted tabs"
- "CloudBookmarks"
- "CloudSettings"
- "Cycler"
- "DataMigration"
- "DeviceUUID"
- "Error reading bookmarks metadata file with code: %zd"
- "Export"
- "FROM bookmarks WHERE deleted = 1 AND server_id IS NOT NULL AND syncable = 1 GROUP BY server_id"
- "Failed to write bookmarks metadata file to %{public}@"
- "FetchedIconData"
- "FileURL"
- "INSERT INTO bookmarks (order_index, type, subtype, deleted, added, parent, server_id, dav_generation%@) VALUES (0, %ld, %ld, 1, 0, -1, ?, ?%@)"
- "Import"
- "Item was merged with %{private}@"
- "OpenSafariExportSettingsFailedKey"
- "OpenSafariExportSettingsMissingEntitlementKey"
- "OpenSafariExportSettingsNotRunningForegroundKey"
- "OpenSafariExportSettingsTestingMode"
- "Pinned"
- "PinnedTabs"
- "PinnedTabsByProfileUUID"
- "Posted bookmarks metadata file changed notification"
- "Posting bookmarks metadata file change distributed notification"
- "PrivatePinnedTabs"
- "Profiles"
- "Read device identifier: %{private}@ from bookmarks metadata file, readonly: %d"
- "ReadingListIcons"
- "Received a vnode event for bookmarks metadata file"
- "Received bookmarks metadata file change distributed notification"
- "ServerID"
- "SyncData"
- "SyncPosition"
- "T@\"NSUUID\",R,N"
- "TB,N,G_listensForMetaDataChangeNotification,S_setListensForMetaDataChangeNotification:,V_listensForMetaDataChangeNotification"
- "TB,N,GisReadOnly,V_readOnly"
- "TB,R,N,GisMerging"
- "TabGroup"
- "WebBookmarkDeviceIdentifier"
- "WebBookmarkServer"
- "WebFilterStatus"
- "WebsiteData"
- "WindowStatesKey"
- "_cancelMonitoringMetaDataFile"
- "_createOrLoadMetaData"
- "_deviceIdentifierForCloudKitWithCollectionType:"
- "_encounteredErrorWhileObtainingUUID"
- "_fileMonitor"
- "_insertTombstoneWithServerID:itemType:subtype:syncData:"
- "_listensForMetaDataChangeNotification"
- "_mergeCandidateBookmarkWithTitle:address:parent:mergeMode:"
- "_mergeCandidateFolderWithTitle:parent:mergeMode:"
- "_mergeMode"
- "_metaDataDidChange:"
- "_metaDataFileChanged:"
- "_plistURL"
- "_postWebBookmarkMetaDataChangeDistributedNotification:"
- "_readOnly"
- "_resumeMonitoringMetaDataFile"
- "_setListensForMetaDataChangeNotification:"
- "_setMergeMode:"
- "_setUpWithPlistURL:readOnly:queue:"
- "archive_status IN (%zd,%zd)"
- "archive_status IN (%zd,%zd,%zd)"
- "beginMergingChangesWithDatabase:"
- "clearDeviceIdentifierWithPlistURL:"
- "com.apple.WebBookmarkDeviceIdentifier.%p"
- "com.apple.WebBookmarks"
- "com.apple.WebBookmarks.MetaDataDidChangeNotification"
- "decodeDoubleForKey:"
- "decodeInt32ForKey:"
- "decodeIntForKey:"
- "deviceIdentifierForCloudKitWithCollectionType:generateIfNeeded:"
- "dictionaryWithContentsOfURL:"
- "encodeDouble:forKey:"
- "encodeInt32:forKey:"
- "encodeInt:forKey:"
- "encounteredErrorWhileObtainingUUID"
- "fileSystemRepresentation"
- "finishMergingChangesWithDatabase:"
- "initWithArray:"
- "initWithPlistURL:readOnly:"
- "initWithProfileProvider:"
- "isInternalInstall"
- "isMerging"
- "isReadOnly"
- "isSafariProfilesEnabled"
- "listensForMetaDataChangeNotification"
- "merging"
- "readOnly"
- "removeObserver:name:object:"
- "setGeneration:"
- "setReadOnly:"
- "type = 0 AND title = ?3 AND url = ?1 AND parent = ?2 AND deleted = 0"
- "type = 0 AND url = ?1 AND parent = ?2 AND deleted = 0 AND server_id IS NULL"
- "type = 1 AND title = ? AND parent = ? AND deleted = 0 %@"
- "v36@0:8@16B24@28"
- "webBookmarksMetaDataDidChangeNotification"
- "writeToURL:atomically:"
- "{unique_ptr<WebBookmarks::BookmarkSQLWriteTransaction, std::default_delete<WebBookmarks::BookmarkSQLWriteTransaction>>=\"__ptr_\"^{BookmarkSQLWriteTransaction}}"

```
