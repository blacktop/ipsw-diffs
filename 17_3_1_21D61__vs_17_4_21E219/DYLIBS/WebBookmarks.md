## WebBookmarks

> `/System/Library/PrivateFrameworks/WebBookmarks.framework/WebBookmarks`

```diff

-617.2.4.10.8
-  __TEXT.__text: 0x93f20
-  __TEXT.__auth_stubs: 0xd10
-  __TEXT.__objc_methlist: 0x71b8
+618.1.15.10.11
+  __TEXT.__text: 0x949dc
+  __TEXT.__auth_stubs: 0xcf0
+  __TEXT.__objc_methlist: 0x70a8
   __TEXT.__const: 0x1b8
-  __TEXT.__gcc_except_tab: 0x9844
-  __TEXT.__cstring: 0xd106
-  __TEXT.__oslogstring: 0x6a60
+  __TEXT.__gcc_except_tab: 0x9878
+  __TEXT.__cstring: 0xd225
+  __TEXT.__oslogstring: 0x6b36
   __TEXT.__dlopen_cstrs: 0xb2
-  __TEXT.__unwind_info: 0x3df8
+  __TEXT.__unwind_info: 0x3e60
   __TEXT.__eh_frame: 0x38
-  __TEXT.__objc_classname: 0x9b6
-  __TEXT.__objc_methname: 0x144ed
-  __TEXT.__objc_methtype: 0x259f
-  __TEXT.__objc_stubs: 0xdf20
-  __DATA_CONST.__got: 0x368
-  __DATA_CONST.__const: 0x2ad8
-  __DATA_CONST.__objc_classlist: 0x218
+  __TEXT.__objc_classname: 0x991
+  __TEXT.__objc_methname: 0x14815
+  __TEXT.__objc_methtype: 0x2636
+  __TEXT.__objc_stubs: 0xe060
+  __DATA_CONST.__got: 0x378
+  __DATA_CONST.__const: 0x2b08
+  __DATA_CONST.__objc_classlist: 0x210
   __DATA_CONST.__objc_catlist: 0x20
-  __DATA_CONST.__objc_protolist: 0x108
+  __DATA_CONST.__objc_protolist: 0x100
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x9120
-  __DATA_CONST.__objc_selrefs: 0x4798
-  __DATA_CONST.__objc_arraydata: 0x118
-  __AUTH_CONST.__cfstring: 0x56a0
+  __DATA_CONST.__objc_const: 0x8fc0
+  __DATA_CONST.__objc_selrefs: 0x4848
+  __DATA_CONST.__objc_protorefs: 0x10
+  __DATA_CONST.__objc_classrefs: 0x428
+  __DATA_CONST.__objc_superrefs: 0x1d0
+  __DATA_CONST.__objc_arraydata: 0x128
+  __AUTH_CONST.__cfstring: 0x5800
   __AUTH_CONST.__objc_const: 0x48
-  __AUTH_CONST.__objc_intobj: 0x330
+  __AUTH_CONST.__const: 0x560
+  __AUTH_CONST.__objc_intobj: 0x360
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__const: 0x320
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__auth_got: 0x6a0
+  __AUTH_CONST.__auth_got: 0x690
   __AUTH.__objc_data: 0x50
-  __DATA.__objc_protorefs: 0x10
-  __DATA.__objc_classrefs: 0x428
-  __DATA.__objc_superrefs: 0x1d8
-  __DATA.__objc_ivar: 0x5ac
-  __DATA.__data: 0xdc0
-  __DATA.__bss: 0x108
-  __DATA_DIRTY.__const: 0xd20
-  __DATA_DIRTY.__objc_const: 0x1cd8
-  __DATA_DIRTY.__objc_data: 0x14a0
+  __DATA.__objc_ivar: 0x5a4
+  __DATA.__data: 0xd60
+  __DATA.__bss: 0xf8
+  __DATA_DIRTY.__const: 0xae0
+  __DATA_DIRTY.__objc_const: 0x1c90
+  __DATA_DIRTY.__objc_data: 0x1450
   __DATA_DIRTY.__data: 0x10
   __DATA_DIRTY.__bss: 0x248
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 3375
-  Symbols:   11417
-  CStrings:  5167
+  Functions: 3357
+  Symbols:   11390
+  CStrings:  5205
 
Symbols:
+ +[WBCollectionConfiguration sharedInMemoryTabCollectionConfigurationWithIdentifier:]
+ +[WBCollectionConfiguration sharedInMemoryTabCollectionConfiguration]
+ +[WBDevice localDeviceWithTitle:creationDeviceIdentifier:deviceIdentifier:unnamedTabGroups:profileIdentifier:]
+ +[WBDevice remoteDeviceWithTitle:deviceIdentifier:unnamedTabGroups:profileIdentifier:]
+ +[WBTabCollection deviceIdentifier]
+ -[WBCollectionConfiguration device]
+ -[WBCollectionConfiguration identifier]
+ -[WBCollectionConfiguration setDevice:]
+ -[WBCollectionConfiguration setIdentifier:]
+ -[WBDevice serverID]
+ -[WBLocalTabAttributes localAttributesWithLastVisitTime:queuedNavigation:]
+ -[WBLocalTabAttributes setSessionStateData:]
+ -[WBMutableTabGroup initWithBookmark:tabs:lastSelectedTabUUID:kind:]
+ -[WBProfile isDefault]
+ -[WBProfileWindow existingUnnamedTabGroupForProfileWithIdentifier:]
+ -[WBProfileWindow initWithWindowState:tabGroupManager:]
+ -[WBProfileWindow initWithWindowState:tabGroupManager:preferredProfileIdentifier:]
+ -[WBSettingsSyncEngineAccess _didUpdateIOSDefaultBrowserWithRecord:]
+ -[WBTab _determineURL]
+ -[WBTab initWithUUID:title:url:deviceIdentifier:isPrivateBrowsing:]
+ -[WBTabCollection currentDeviceIdentifier]
+ -[WBTabCollection databaseSyncData]
+ -[WBTabCollection enumerateDescendantsOfItemWithID:usingBlock:]
+ -[WBTabCollection serverIDForItemWithID:]
+ -[WBTabCollection syncDataForItem:]
+ -[WBTabCollection syncDataForItemWithID:]
+ -[WBTabGroup firstUnpinnedTab]
+ -[WBTabGroup serverID]
+ -[WBTabGroupManager _findOrCreateLocalDeviceForProfileWithIdentifier:]
+ -[WBTabGroupManager _loadDatabase]
+ -[WBTabGroupManager dealloc]
+ -[WBTabGroupManager deviceIdentifier]
+ -[WBTabGroupManager insertUnnamedTabGroup:]
+ -[WBTabGroupManager observeValueForKeyPath:ofObject:change:context:]
+ -[WBTabGroupManager removedTabGroupWithUUID:]
+ -[WBTabGroupManager tabGroupWithServerID:]
+ -[WebBookmark setShowIconOnly:]
+ -[WebBookmark showIconOnly]
+ -[WebBookmark(Internal) showIconOnlyProvider]
+ -[WebBookmark(Internal) showIconOnlyUpdater]
+ -[WebBookmarkCollection _descendantIDsOfBookmarkFolderID:]
+ -[WebBookmarkCollection _performSafariVersionUpgradesInSafariProcessFromPreviousVersion:]
+ -[WebBookmarkCollection _updateDatabaseFromSafariProcessIfNewerSafariVersionWasLaunched]
+ -[WebBookmarkCollection resetDeviceIdentifier]
+ -[WebBookmarkTabCollection _allTabsThatExceededLocalAttributesSizeLimit]
+ -[WebBookmarkTabCollection _deleteDefaultProfileIfSavedAsTabGroup]
+ -[WebBookmarkTabCollection _deleteDefaultProfileIfSavedAsTabGroup].cold.1
+ -[WebBookmarkTabCollection _migrateWindowBookmark:]
+ -[WebBookmarkTabCollection _performSafariVersionUpgradesFromPreviousVersion:].cold.5
+ -[WebBookmarkTabCollection _performSafariVersionUpgradesFromPreviousVersion:].cold.6
+ -[WebBookmarkTabCollection _performSafariVersionUpgradesInSafariProcessFromPreviousVersion:]
+ -[WebBookmarkTabCollection _reEncodeSessionStateDataIfNeeded]
+ -[WebBookmarkTabCollection _tabGroupForBookmark:kind:]
+ -[WebBookmarkTabCollection _tabGroupWithID:kind:]
+ -[WebBookmarkTabCollection devicesForProfile:]
+ -[WebBookmarkTabCollection initWithConfiguration:checkIntegrity:]
+ -[WebBookmarkTabCollection remoteDevicesForProfileBookmark:]
+ GCC_except_table197
+ GCC_except_table215
+ GCC_except_table218
+ GCC_except_table219
+ GCC_except_table220
+ GCC_except_table228
+ GCC_except_table230
+ GCC_except_table236
+ GCC_except_table237
+ GCC_except_table250
+ GCC_except_table259
+ GCC_except_table277
+ GCC_except_table282
+ GCC_except_table294
+ GCC_except_table298
+ GCC_except_table304
+ GCC_except_table305
+ GCC_except_table310
+ GCC_except_table312
+ GCC_except_table324
+ GCC_except_table337
+ GCC_except_table342
+ GCC_except_table351
+ GCC_except_table354
+ GCC_except_table356
+ GCC_except_table357
+ GCC_except_table368
+ GCC_except_table369
+ GCC_except_table375
+ GCC_except_table390
+ GCC_except_table395
+ GCC_except_table396
+ GCC_except_table401
+ GCC_except_table402
+ GCC_except_table407
+ GCC_except_table427
+ GCC_except_table429
+ GCC_except_table444
+ GCC_except_table445
+ GCC_except_table462
+ GCC_except_table481
+ GCC_except_table483
+ GCC_except_table484
+ GCC_except_table489
+ GCC_except_table494
+ GCC_except_table497
+ GCC_except_table500
+ GCC_except_table502
+ GCC_except_table503
+ GCC_except_table510
+ GCC_except_table517
+ GCC_except_table518
+ _NSKeyValueChangeNewKey
+ _OBJC_CLASS_$_WBSDevice
+ _OBJC_IVAR_$_WBCollectionConfiguration._device
+ _OBJC_IVAR_$_WBCollectionConfiguration._identifier
+ _OBJC_IVAR_$_WBTab._cachedURL
+ _OBJC_IVAR_$_WBTabGroupManager._device
+ _OBJC_IVAR_$_WebBookmark._showIconOnlyField
+ _WBLocalTabGroupTitle
+ _WBPrivateTabGroupTitle
+ _WBSIOSDefaultBrowserSelectionStateKey
+ _WBSPerSitePreferenceNameProfile
+ _WebBookmarksShowIconOnlyAttributeKey
+ ___31-[WebBookmark setShowIconOnly:]_block_invoke
+ ___32-[WBMutableTabGroup deleteTabs:]_block_invoke.12
+ ___34-[WBTabGroupManager _loadDatabase]_block_invoke
+ ___34-[WBTabGroupManager _loadDatabase]_block_invoke.42
+ ___34-[WBTabGroupManager _loadDatabase]_block_invoke_2
+ ___34-[WBTabGroupManager _loadDatabase]_block_invoke_2.43
+ ___34-[WBTabGroupManager _loadDatabase]_block_invoke_2.cold.1
+ ___34-[WBTabGroupManager _loadDatabase]_block_invoke_3
+ ___34-[WBTabGroupManager _loadDatabase]_block_invoke_4
+ ___35-[WBTabCollection databaseSyncData]_block_invoke
+ ___35-[WBTabCollection syncDataForItem:]_block_invoke
+ ___40-[WBTabGroupManager initWithCollection:]_block_invoke
+ ___41-[WBTabCollection syncDataForItemWithID:]_block_invoke
+ ___42-[WBTabGroupManager tabGroupWithServerID:]_block_invoke
+ ___43-[WBTabGroupManager insertUnnamedTabGroup:]_block_invoke
+ ___43-[WBTabGroupManager insertUnnamedTabGroup:]_block_invoke_2
+ ___43-[WBTabGroupManager insertUnnamedTabGroup:]_block_invoke_3
+ ___44-[WBTabGroupSyncAgentProxy _setUpConnection]_block_invoke.68
+ ___44-[WBTabGroupSyncAgentProxy _setUpConnection]_block_invoke.68.cold.1
+ ___44-[WebBookmark(Internal) showIconOnlyUpdater]_block_invoke
+ ___45-[WBTabGroupManager syncDidFinishWithResult:]_block_invoke_2
+ ___45-[WebBookmark(Internal) showIconOnlyProvider]_block_invoke
+ ___46-[WebBookmarkTabCollection devicesForProfile:]_block_invoke
+ ___51-[WBTabGroupManager _unsafeTabGroupUUIDsToCKShares]_block_invoke_2
+ ___54-[WBTabGroupSyncAgentProxy _setUpSyncObserverIfNeeded]_block_invoke.75
+ ___54-[WBTabGroupSyncAgentProxy _setUpSyncObserverIfNeeded]_block_invoke.75.cold.1
+ ___54-[WebBookmarkTabCollection _tabGroupForBookmark:kind:]_block_invoke
+ ___57-[WebBookmarkCollection _updateBookmarks:inFolderWithID:]_block_invoke.391
+ ___57-[WebBookmarkCollection _updateBookmarks:inFolderWithID:]_block_invoke.393
+ ___57-[WebBookmarkCollection _updateBookmarks:inFolderWithID:]_block_invoke.393.cold.1
+ ___57-[WebBookmarkCollection _updateBookmarks:inFolderWithID:]_block_invoke.393.cold.2
+ ___57-[WebBookmarkCollection _updateBookmarks:inFolderWithID:]_block_invoke.393.cold.3
+ ___57-[WebBookmarkCollection _updateBookmarks:inFolderWithID:]_block_invoke.393.cold.4
+ ___57-[WebBookmarkCollection _updateBookmarks:inFolderWithID:]_block_invoke_2.394
+ ___60-[WBSettingsSyncEngineAccess deleteBackgroundImageDirectory]_block_invoke.43
+ ___60-[WebBookmarkTabCollection _regenerateSyncPositionsIfNeeded]_block_invoke.169
+ ___60-[WebBookmarkTabCollection _regenerateSyncPositionsIfNeeded]_block_invoke.169.cold.1
+ ___60-[WebBookmarkTabCollection remoteDevicesForProfileBookmark:]_block_invoke
+ ___63-[WBTabCollection enumerateDescendantsOfItemWithID:usingBlock:]_block_invoke
+ ___63-[WBTabCollection enumerateDescendantsOfItemWithID:usingBlock:]_block_invoke_2
+ ___67-[WBProfileWindow existingUnnamedTabGroupForProfileWithIdentifier:]_block_invoke
+ ___68-[WBTabGroupManager _dequeueNextAcceptCloudKitShareMetadataIfNeeded]_block_invoke.129
+ ___72-[WebBookmarkTabCollection _saveTabGroupRecordsWithMissingCKShareRecord]_block_invoke.173
+ ___77-[WBTabCyclerCommandHandler _startMonitoringSyncStatusWithCompletionHandler:]_block_invoke.36
+ ___81-[WBTabCyclerCommandHandler _moveTabGroup:toProfileWithIdentifier:atIndex:reply:]_block_invoke_2
+ ___Block_byref_object_copy_.1794
+ ___Block_byref_object_dispose_.1795
+ ____ZL33prefixEndingWithFirstWordOfStringP8NSString_block_invoke.1797
+ ___block_descriptor_40_e8_32r_e43_v32?0"NSString"8"WBMutableProfile"16^B24lr32l8
+ ___block_descriptor_40_e8_32s_e35_v32?0"NSString"8"WBDevice"16^B24ls32l8
+ ___block_descriptor_40_e8_32s_e44_B32?0"NSString"8"WBMutableTabGroup"16^B24ls32l8
+ ___block_descriptor_48_e8_32s40s_e28_v16?0"WBBookmarkSyncData"8ls32l8s40l8
+ ___block_descriptor_52_ea8_32s40bs_e5_v8?0ls32l8s40l8
+ ___block_descriptor_80_ea8_32s40s48s56s_e5_B8?0ls32l8s40l8s48l8s56l8
+ ___block_literal_global.1000
+ ___block_literal_global.101
+ ___block_literal_global.1035
+ ___block_literal_global.107
+ ___block_literal_global.109
+ ___block_literal_global.1102
+ ___block_literal_global.136
+ ___block_literal_global.154
+ ___block_literal_global.161
+ ___block_literal_global.164
+ ___block_literal_global.176
+ ___block_literal_global.1789
+ ___block_literal_global.1792
+ ___block_literal_global.1799
+ ___block_literal_global.1807
+ ___block_literal_global.187
+ ___block_literal_global.220
+ ___block_literal_global.294
+ ___block_literal_global.298
+ ___block_literal_global.300
+ ___block_literal_global.302
+ ___block_literal_global.305
+ ___block_literal_global.308
+ ___block_literal_global.310
+ ___block_literal_global.312
+ ___block_literal_global.315
+ ___block_literal_global.318
+ ___block_literal_global.386
+ ___block_literal_global.410
+ ___block_literal_global.429
+ ___block_literal_global.439
+ ___block_literal_global.60
+ ___block_literal_global.71
+ ___block_literal_global.74
+ ___block_literal_global.76
+ ___block_literal_global.78
+ ___block_literal_global.9
+ ___block_literal_global.94
+ __unnamed_array_storage.114
+ _deviceNameObserverContext
+ _objc_msgSend$_allTabsThatExceededLocalAttributesSizeLimit
+ _objc_msgSend$_deleteDefaultProfileIfSavedAsTabGroup
+ _objc_msgSend$_descendantIDsOfBookmarkFolderID:
+ _objc_msgSend$_determineURL
+ _objc_msgSend$_didUpdateIOSDefaultBrowserWithRecord:
+ _objc_msgSend$_findOrCreateLocalDeviceForProfileWithIdentifier:
+ _objc_msgSend$_loadDatabase
+ _objc_msgSend$_migrateWindowBookmark:
+ _objc_msgSend$_reEncodeSessionStateDataIfNeeded
+ _objc_msgSend$_tabGroupForBookmark:kind:
+ _objc_msgSend$_tabGroupWithID:kind:
+ _objc_msgSend$_updateDatabaseFromSafariProcessIfNewerSafariVersionWasLaunched
+ _objc_msgSend$addObserver:forKeyPath:options:context:
+ _objc_msgSend$containsString:
+ _objc_msgSend$currentDevice
+ _objc_msgSend$device
+ _objc_msgSend$deviceClass
+ _objc_msgSend$existingUnnamedTabGroupForProfileWithIdentifier:
+ _objc_msgSend$initWithBookmark:tabs:lastSelectedTabUUID:kind:
+ _objc_msgSend$initWithWindowState:tabGroupManager:preferredProfileIdentifier:
+ _objc_msgSend$insertUnnamedTabGroup:
+ _objc_msgSend$localDeviceWithTitle:creationDeviceIdentifier:deviceIdentifier:unnamedTabGroups:profileIdentifier:
+ _objc_msgSend$removeObserver:forKeyPath:context:
+ _objc_msgSend$removedTabGroupWithUUID:
+ _objc_msgSend$resetDeviceIdentifier
+ _objc_msgSend$safari_isSafariApplicationPlatform
+ _objc_msgSend$setByAddingObjectsFromSet:
+ _objc_msgSend$setDevice:
+ _objc_msgSend$setInteger:forKey:
+ _objc_msgSend$setSessionStateData:
+ _objc_msgSend$setShowIconOnly:
+ _objc_msgSend$sf_safariSharedDefaults
+ _objc_msgSend$sharedInMemoryTabCollectionConfigurationWithIdentifier:
+ _objc_msgSend$showIconOnly
+ _objc_msgSend$showIconOnlyProvider
+ _objc_msgSend$showIconOnlyUpdater
+ _objc_msgSend$tabGroupManager:didReloadAferSyncWithResult:
+ _objc_msgSend$userUniqueDeviceIdentifier
- +[WBDevice currentDeviceIdentifier]
- +[WBTabCollection currentDeviceIdentifier]
- -[WBBrowserState initWithPinnedTabs:privatePinnedTabs:windows:]
- -[WBBrowserState setWindows:]
- -[WBBrowserState windows]
- -[WBDevice initWithTitle:deviceIdentifier:remote:unnamedTabGroups:profileIdentifier:]
- -[WBMutableTabGroup initWithBookmark:tabs:lastSelectedTabUUID:]
- -[WBProfileWindow _existingUnnamedTabGroupForProfileWithIdentifier:]
- -[WBProfileWindow deviceName]
- -[WBProfileWindow initWithWindowState:tabGroupManager:deviceName:]
- -[WBProfileWindow initWithWindowState:tabGroupManager:preferredProfileIdentifier:deviceName:]
- -[WBProfileWindow setDeviceName:]
- -[WBReadonlyTabCollection windowWithUUID:]
- -[WBReadonlyTabCollection windowsFolderSpecialID]
- -[WBReadonlyTabCollection windows]
- -[WBTabCollection saveWindow:]
- -[WBTabCollection windowWithUUID:]
- -[WBTabCollection windowsFolderSpecialID]
- -[WBTabCollection windows]
- -[WBTabGroupManager _commonInit]
- -[WBTabGroupManager _findOrCreateLocalDeviceWithName:forProfileWithIdentifier:]
- -[WBTabGroupManager _unsafeCreateDefaultProfileIfNecessary]
- -[WBTabGroupManager _unsafeMutableDefaultProfile]
- -[WBTabGroupManager insertUnnamedTabGroup:deviceName:]
- -[WBTabGroupManager windowWithUUID:]
- -[WBTabGroupManager windowsFolderSpecialID]
- -[WBTabGroupManager windows]
- -[WBTabGroupSyncAgent deviceIdentifier]
- -[WBWindow .cxx_destruct]
- -[WBWindow _updateExtraAttributesUsingBlock:]
- -[WBWindow activeTabGroup]
- -[WBWindow activeTabUUIDForTabGroupWithUUID:]
- -[WBWindow bookmark]
- -[WBWindow customUnifiedFieldText]
- -[WBWindow dateClosed]
- -[WBWindow description]
- -[WBWindow extraAttributes]
- -[WBWindow hash]
- -[WBWindow identifier]
- -[WBWindow initWithBookmark:]
- -[WBWindow initWithBookmark:activeTabGroup:localTabGroup:privateTabGroup:]
- -[WBWindow initWithDictionaryRepresentation:localTabGroup:privateTabGroup:]
- -[WBWindow initWithUUID:]
- -[WBWindow initWithUUID:activeTabGroup:localTabGroup:privateTabGroup:sceneID:]
- -[WBWindow initWithUUID:sceneID:]
- -[WBWindow isEqual:]
- -[WBWindow isFavoritesBarHidden]
- -[WBWindow isMinimized]
- -[WBWindow isPopupWindow]
- -[WBWindow isPrivateWindow]
- -[WBWindow isTabBarHidden]
- -[WBWindow localTabGroup]
- -[WBWindow prefersSidebarVisible]
- -[WBWindow privateTabGroup]
- -[WBWindow removeActiveTabUUIDForTabGroupWithUUID:]
- -[WBWindow removeAllActiveTabUUIDs]
- -[WBWindow sceneID]
- -[WBWindow setActiveTabGroup:]
- -[WBWindow setActiveTabUUID:forTabGroupWithUUID:]
- -[WBWindow setDateClosed:]
- -[WBWindow setExtraAttributes:]
- -[WBWindow setSceneID:]
- -[WBWindow tabGroupsToActiveTabs]
- -[WBWindow updateActiveTabGroup]
- -[WBWindow uuid]
- -[WebBookmarkTabCollection _migrateWindow:]
- -[WebBookmarkTabCollection _migrateWindowState:]
- -[WebBookmarkTabCollection _tabGroupWithID:]
- -[WebBookmarkTabCollection _windowWithBookmark:]
- -[WebBookmarkTabCollection deleteAllWindows]
- -[WebBookmarkTabCollection devicesForProfileBookmark:]
- -[WebBookmarkTabCollection saveWindow:]
- -[WebBookmarkTabCollection windowWithUUID:]
- -[WebBookmarkTabCollection windowsFolderSpecialID]
- -[WebBookmarkTabCollection windows]
- GCC_except_table108
- GCC_except_table198
- GCC_except_table200
- GCC_except_table214
- GCC_except_table226
- GCC_except_table229
- GCC_except_table239
- GCC_except_table244
- GCC_except_table253
- GCC_except_table262
- GCC_except_table280
- GCC_except_table285
- GCC_except_table297
- GCC_except_table301
- GCC_except_table307
- GCC_except_table308
- GCC_except_table321
- GCC_except_table322
- GCC_except_table327
- GCC_except_table341
- GCC_except_table346
- GCC_except_table359
- GCC_except_table360
- GCC_except_table361
- GCC_except_table366
- GCC_except_table379
- GCC_except_table380
- GCC_except_table381
- GCC_except_table398
- GCC_except_table403
- GCC_except_table406
- GCC_except_table408
- GCC_except_table409
- GCC_except_table415
- GCC_except_table431
- GCC_except_table437
- GCC_except_table452
- GCC_except_table453
- GCC_except_table466
- GCC_except_table485
- GCC_except_table487
- GCC_except_table488
- GCC_except_table493
- GCC_except_table498
- GCC_except_table506
- GCC_except_table513
- GCC_except_table514
- _MGGetSInt32Answer
- _OBJC_CLASS_$_WBWindow
- _OBJC_IVAR_$_WBBrowserState._windows
- _OBJC_IVAR_$_WBProfileWindow._deviceName
- _OBJC_IVAR_$_WBWindow._activeTabGroup
- _OBJC_IVAR_$_WBWindow._bookmark
- _OBJC_IVAR_$_WBWindow._dateClosed
- _OBJC_IVAR_$_WBWindow._localTabGroup
- _OBJC_IVAR_$_WBWindow._privateTabGroup
- _OBJC_METACLASS_$_WBWindow
- _WBSDeviceUDID
- _WBSWindowActiveTabGroupKey
- __OBJC_$_CLASS_PROP_LIST_WBDevice
- __OBJC_$_INSTANCE_METHODS_WBWindow
- __OBJC_$_INSTANCE_VARIABLES_WBWindow
- __OBJC_$_PROP_LIST_WBWindow
- __OBJC_$_PROTOCOL_REFS_WBTabGroupSyncAgentProxyProtocol
- __OBJC_CLASS_RO_$_WBWindow
- __OBJC_LABEL_PROTOCOL_$_WBTabGroupSyncAgentProxyProtocol
- __OBJC_METACLASS_RO_$_WBWindow
- __OBJC_PROTOCOL_$_WBTabGroupSyncAgentProxyProtocol
- ___23-[WBWindow setSceneID:]_block_invoke
- ___26-[WBTabCollection windows]_block_invoke
- ___30-[WBTabCollection saveWindow:]_block_invoke
- ___32-[WBMutableTabGroup deleteTabs:]_block_invoke.18
- ___32-[WBTabGroupManager _commonInit]_block_invoke
- ___34-[WBTabCollection windowWithUUID:]_block_invoke
- ___35+[WBDevice currentDeviceIdentifier]_block_invoke
- ___35-[WBWindow removeAllActiveTabUUIDs]_block_invoke
- ___35-[WebBookmarkTabCollection windows]_block_invoke
- ___39-[WebBookmarkTabCollection saveWindow:]_block_invoke
- ___39-[WebBookmarkTabCollection saveWindow:]_block_invoke.cold.1
- ___39-[WebBookmarkTabCollection saveWindow:]_block_invoke.cold.2
- ___39-[WebBookmarkTabCollection saveWindow:]_block_invoke_2
- ___39-[WebBookmarkTabCollection saveWindow:]_block_invoke_2.cold.1
- ___41-[WBTabCollection windowsFolderSpecialID]_block_invoke
- ___44-[WBTabGroupSyncAgentProxy _setUpConnection]_block_invoke.67
- ___44-[WBTabGroupSyncAgentProxy _setUpConnection]_block_invoke.67.cold.1
- ___44-[WebBookmarkTabCollection deleteAllWindows]_block_invoke
- ___48-[WebBookmarkTabCollection _migrateWindowState:]_block_invoke
- ___48-[WebBookmarkTabCollection tabGroupForBookmark:]_block_invoke
- ___49-[WBWindow setActiveTabUUID:forTabGroupWithUUID:]_block_invoke
- ___51-[WBTabGroupManager _unsafeTabGroupUUIDsToCKShares]_block_invoke.126
- ___54-[WBTabGroupManager insertUnnamedTabGroup:deviceName:]_block_invoke
- ___54-[WBTabGroupManager insertUnnamedTabGroup:deviceName:]_block_invoke_2
- ___54-[WBTabGroupManager insertUnnamedTabGroup:deviceName:]_block_invoke_3
- ___54-[WBTabGroupSyncAgentProxy _setUpSyncObserverIfNeeded]_block_invoke.74
- ___54-[WBTabGroupSyncAgentProxy _setUpSyncObserverIfNeeded]_block_invoke.74.cold.1
- ___54-[WebBookmarkTabCollection devicesForProfileBookmark:]_block_invoke
- ___57-[WebBookmarkCollection _updateBookmarks:inFolderWithID:]_block_invoke.385
- ___57-[WebBookmarkCollection _updateBookmarks:inFolderWithID:]_block_invoke.387
- ___57-[WebBookmarkCollection _updateBookmarks:inFolderWithID:]_block_invoke.387.cold.1
- ___57-[WebBookmarkCollection _updateBookmarks:inFolderWithID:]_block_invoke.387.cold.2
- ___57-[WebBookmarkCollection _updateBookmarks:inFolderWithID:]_block_invoke.387.cold.3
- ___57-[WebBookmarkCollection _updateBookmarks:inFolderWithID:]_block_invoke.387.cold.4
- ___57-[WebBookmarkCollection _updateBookmarks:inFolderWithID:]_block_invoke_2.388
- ___59-[WBTabGroupManager _unsafeCreateDefaultProfileIfNecessary]_block_invoke
- ___59-[WBTabGroupManager _unsafeCreateDefaultProfileIfNecessary]_block_invoke.cold.1
- ___60-[WBSettingsSyncEngineAccess deleteBackgroundImageDirectory]_block_invoke.45
- ___60-[WebBookmarkTabCollection _regenerateSyncPositionsIfNeeded]_block_invoke.156
- ___60-[WebBookmarkTabCollection _regenerateSyncPositionsIfNeeded]_block_invoke.156.cold.1
- ___68-[WBProfileWindow _existingUnnamedTabGroupForProfileWithIdentifier:]_block_invoke
- ___68-[WBTabGroupManager _dequeueNextAcceptCloudKitShareMetadataIfNeeded]_block_invoke.118
- ___72-[WebBookmarkTabCollection _saveTabGroupRecordsWithMissingCKShareRecord]_block_invoke.160
- ___77-[WBTabCyclerCommandHandler _startMonitoringSyncStatusWithCompletionHandler:]_block_invoke.35
- ___79-[WBTabGroupManager _findOrCreateLocalDeviceWithName:forProfileWithIdentifier:]_block_invoke
- ___Block_byref_object_copy_.1769
- ___Block_byref_object_dispose_.1770
- ____ZL33prefixEndingWithFirstWordOfStringP8NSString_block_invoke.1772
- ___block_descriptor_40_ea8_32s_e31_"WBWindow"16?0"WebBookmark"8ls32l8
- ___block_descriptor_40_ea8_32s_e36_"NSArray"16?0"WBMutableTabGroup"8ls32l8
- ___block_descriptor_44_ea8_32s_e20_B16?0"WBTabGroup"8ls32l8
- ___block_descriptor_48_e8_32s40s_e29_v16?0"NSMutableDictionary"8ls32l8s40l8
- ___block_descriptor_72_ea8_32s40s48s_e5_B8?0ls32l8s40l8s48l8
- ___block_literal_global.1017
- ___block_literal_global.1081
- ___block_literal_global.125
- ___block_literal_global.146
- ___block_literal_global.148
- ___block_literal_global.149
- ___block_literal_global.174
- ___block_literal_global.1764
- ___block_literal_global.1767
- ___block_literal_global.1774
- ___block_literal_global.1782
- ___block_literal_global.21
- ___block_literal_global.214
- ___block_literal_global.286
- ___block_literal_global.289
- ___block_literal_global.293
- ___block_literal_global.299
- ___block_literal_global.301
- ___block_literal_global.303
- ___block_literal_global.306
- ___block_literal_global.309
- ___block_literal_global.380
- ___block_literal_global.404
- ___block_literal_global.423
- ___block_literal_global.433
- ___block_literal_global.5
- ___block_literal_global.57
- ___block_literal_global.61
- ___block_literal_global.64
- ___block_literal_global.67
- ___block_literal_global.70
- ___block_literal_global.73
- ___block_literal_global.90
- ___block_literal_global.96
- ___block_literal_global.98
- ___block_literal_global.982
- __unnamed_array_storage.109
- _currentDeviceIdentifier.currentDeviceIdentifier
- _currentDeviceIdentifier.onceToken
- _objc_msgSend$_cacheProfile:
- _objc_msgSend$_commonInit
- _objc_msgSend$_existingUnnamedTabGroupForProfileWithIdentifier:
- _objc_msgSend$_findOrCreateLocalDeviceWithName:forProfileWithIdentifier:
- _objc_msgSend$_migrateWindow:
- _objc_msgSend$_resetBookmark:
- _objc_msgSend$_tabGroupWithID:
- _objc_msgSend$_unsafeCreateDefaultProfileIfNecessary
- _objc_msgSend$_unsafeMutableDefaultProfile
- _objc_msgSend$_updateExtraAttributesUsingBlock:
- _objc_msgSend$_windowWithBookmark:
- _objc_msgSend$activeTabGroup
- _objc_msgSend$activeTabUUIDForTabGroupWithUUID:
- _objc_msgSend$devicesForProfileBookmark:
- _objc_msgSend$initWithBookmark:activeTabGroup:localTabGroup:privateTabGroup:
- _objc_msgSend$initWithBookmark:tabs:lastSelectedTabUUID:
- _objc_msgSend$initWithPinnedTabs:privatePinnedTabs:windows:
- _objc_msgSend$initWithTitle:deviceIdentifier:remote:unnamedTabGroups:profileIdentifier:
- _objc_msgSend$initWithUUID:activeTabGroup:localTabGroup:privateTabGroup:sceneID:
- _objc_msgSend$initWithWindowState:tabGroupManager:preferredProfileIdentifier:deviceName:
- _objc_msgSend$insertUnnamedTabGroup:deviceName:
- _objc_msgSend$mutableProfileWithIdentifier:
- _objc_msgSend$saveWindow:
- _objc_msgSend$setActiveTabGroup:
- _objc_msgSend$updateActiveTabGroup
- _objc_msgSend$windowWithUUID:
- _objc_msgSend$windows
- _objc_msgSend$windowsFolderSpecialID
CStrings:
+ "\x02\x11\x15"
+ "\x02\x12\x11"
+ "\x0f\x02\x14\x14\x12"
+ "!\""
+ "%\x112\x7f\x01"
+ "618.1.13"
+ "618.1.16"
+ "@\"NSArray\"24@0:8@\"<WBSProfileMetadataProviding>\"16"
+ "@\"WBSCRDTPosition\"16@0:8"
+ "@\"WBSDevice\""
+ "@\"WBSNamedColorOption\"16@0:8"
+ "@24@0:8@\"NSString\"16"
+ "@48@0:8@16@24@32q40"
+ "@52@0:8@16@24@32@40B48"
+ "@@ %s: Set showIconOnly to value: %@"
+ "@@ %s: Set showIconOnly to value: 0"
+ "B32@?0@\"NSString\"8@\"WBMutableTabGroup\"16^B24"
+ "Deleted personal profile which was mistakenly saved as a Tab Group."
+ "Failed to delete personal profile that was saved as a Tab Group"
+ "Failed to delete personal profile which was saved as a Tab Group."
+ "Failed to re-encode session state data to truncate large HTTP bodies."
+ "INSERT INTO bookmarks (id, type, order_index, num_children, title, external_uuid) VALUES (0, 1, 0, 0, 'Root', '%@')"
+ "NewestLaunchedSafariVersionInApplicationProcess"
+ "Re-encoded session state data to truncate large HTTP bodies."
+ "Root"
+ "ShowIconOnly"
+ "T@\"NSData\",C,N,V_sessionStateData"
+ "T@\"NSDictionary\",?,R,C,N"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",C,N,V_identifier"
+ "T@\"WBSDevice\",&,N,V_device"
+ "UPDATE bookmarks SET title = 'Root', external_uuid = '%@' WHERE id = 0"
+ "_allTabsThatExceededLocalAttributesSizeLimit"
+ "_cachedURL"
+ "_deleteDefaultProfileIfSavedAsTabGroup"
+ "_descendantIDsOfBookmarkFolderID:"
+ "_determineURL"
+ "_device"
+ "_didUpdateIOSDefaultBrowserWithRecord:"
+ "_findOrCreateLocalDeviceForProfileWithIdentifier:"
+ "_loadDatabase"
+ "_migrateWindowBookmark:"
+ "_performSafariVersionUpgradesInSafariProcessFromPreviousVersion:"
+ "_reEncodeSessionStateDataIfNeeded"
+ "_showIconOnlyField"
+ "_tabGroupForBookmark:kind:"
+ "_tabGroupWithID:kind:"
+ "_updateDatabaseFromSafariProcessIfNewerSafariVersionWasLaunched"
+ "addObserver:forKeyPath:options:context:"
+ "containsString:"
+ "currentDevice"
+ "device"
+ "deviceClass"
+ "enumerateDescendantsOfItemWithID:usingBlock:"
+ "existingUnnamedTabGroupForProfileWithIdentifier:"
+ "file:%@?mode=memory&cache=shared"
+ "firstUnpinnedTab"
+ "initWithBookmark:tabs:lastSelectedTabUUID:kind:"
+ "initWithUUID:title:url:deviceIdentifier:isPrivateBrowsing:"
+ "initWithWindowState:tabGroupManager:"
+ "initWithWindowState:tabGroupManager:preferredProfileIdentifier:"
+ "insertUnnamedTabGroup:"
+ "isDefault"
+ "localAttributesWithLastVisitTime:queuedNavigation:"
+ "localDeviceWithTitle:creationDeviceIdentifier:deviceIdentifier:unnamedTabGroups:profileIdentifier:"
+ "mode=memory"
+ "newestLaunchedSafariFromSafariProcessVersion"
+ "observeValueForKeyPath:ofObject:change:context:"
+ "remoteDeviceWithTitle:deviceIdentifier:unnamedTabGroups:profileIdentifier:"
+ "remoteDevicesForProfileBookmark:"
+ "removeObserver:forKeyPath:context:"
+ "removedTabGroupWithUUID:"
+ "safari_isSafariApplicationPlatform"
+ "serverIDForItemWithID:"
+ "server_id = 'DefaultProfile' AND parent = 0 AND syncable = 1 AND type = 1 AND subtype = 0"
+ "setByAddingObjectsFromSet:"
+ "setDevice:"
+ "setInteger:forKey:"
+ "setSessionStateData:"
+ "setShowIconOnly:"
+ "sf_safariSharedDefaults"
+ "sharedInMemoryTabCollectionConfiguration"
+ "sharedInMemoryTabCollectionConfigurationWithIdentifier:"
+ "showIconOnly"
+ "showIconOnlyProvider"
+ "showIconOnlyUpdater"
+ "syncDataForItem:"
+ "syncDataForItemWithID:"
+ "tabGroupManager:didReloadAferSyncWithResult:"
+ "tabGroupWithServerID:"
+ "type = 0 AND subtype = 0 AND LENGTH(local_attributes) > %d"
+ "userAssignedName"
+ "userUniqueDeviceIdentifier"
+ "v32@0:8@\"WBTabGroupManager\"16q24"
+ "v32@0:8@16q24"
+ "v48@0:8@16@24@32^v40"
- "\x02\x12\x12"
- "\x02\x15"
- "\x0f\x01\x14\x14\x12"
- "%\x112\x7f"
- "@\"NSArray\"16@?0@\"WBMutableTabGroup\"8"
- "@\"NSArray\"24@0:8@\"WBProfile\"16"
- "@\"WBTabGroup\""
- "@\"WBWindow\"16@?0@\"WebBookmark\"8"
- "@\"WBWindow\"24@0:8@\"NSString\"16"
- "@52@0:8@16@24B32@36@44"
- "Could not save window state as bookmark"
- "DeviceClassNumber"
- "INSERT INTO bookmarks (id, type, order_index, num_children, title, external_uuid) VALUES (0, 1, 0, 0, 'Root', 'Root')"
- "Saving window state as bookmark"
- "T@\"NSArray\",C,N,V_windows"
- "T@\"NSData\",R,C,N,V_sessionStateData"
- "T@\"NSString\",C,N,V_deviceName"
- "T@\"WBTabGroup\",&,N,V_activeTabGroup"
- "UPDATE bookmarks SET title = 'Root', external_uuid = 'Root' WHERE id = 0"
- "Unable to move tab group to window folder"
- "Unable to save local tab group when saving window"
- "WBTabGroupSyncAgentProxyProtocol"
- "WBWindow"
- "Window"
- "_activeTabGroup"
- "_commonInit"
- "_deviceName"
- "_existingUnnamedTabGroupForProfileWithIdentifier:"
- "_findOrCreateLocalDeviceWithName:forProfileWithIdentifier:"
- "_migrateWindow:"
- "_migrateWindowState:"
- "_tabGroupWithID:"
- "_unsafeCreateDefaultProfileIfNecessary"
- "_unsafeMutableDefaultProfile"
- "_updateExtraAttributesUsingBlock:"
- "_windowWithBookmark:"
- "_windows"
- "activeTabGroup"
- "deleteAllWindows"
- "deviceName"
- "devicesForProfileBookmark:"
- "initWithBookmark:activeTabGroup:localTabGroup:privateTabGroup:"
- "initWithBookmark:tabs:lastSelectedTabUUID:"
- "initWithPinnedTabs:privatePinnedTabs:windows:"
- "initWithTitle:deviceIdentifier:remote:unnamedTabGroups:profileIdentifier:"
- "initWithUUID:activeTabGroup:localTabGroup:privateTabGroup:sceneID:"
- "initWithWindowState:tabGroupManager:deviceName:"
- "initWithWindowState:tabGroupManager:preferredProfileIdentifier:deviceName:"
- "insertUnnamedTabGroup:deviceName:"
- "saveWindow:"
- "setActiveTabGroup:"
- "setDeviceName:"
- "setWindows:"
- "tabBookmarks count: %zu"
- "updateActiveTabGroup"
- "windowWithUUID:"
- "windows"
- "windowsFolderSpecialID"

```
