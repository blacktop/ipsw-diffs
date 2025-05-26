## WebBookmarks

> `/System/Library/PrivateFrameworks/WebBookmarks.framework/WebBookmarks`

```diff

-616.1.27.10.16
-  __TEXT.__text: 0x92134
+616.2.9.10.10
+  __TEXT.__text: 0x9290c
   __TEXT.__auth_stubs: 0xd10
-  __TEXT.__objc_methlist: 0x70b0
+  __TEXT.__objc_methlist: 0x7110
   __TEXT.__const: 0x1b8
-  __TEXT.__gcc_except_tab: 0x952c
+  __TEXT.__gcc_except_tab: 0x9570
   __TEXT.__cstring: 0xce53
   __TEXT.__oslogstring: 0x6afc
   __TEXT.__dlopen_cstrs: 0xb2
-  __TEXT.__unwind_info: 0x3d34
+  __TEXT.__unwind_info: 0x3d80
   __TEXT.__eh_frame: 0x38
   __TEXT.__objc_classname: 0x9b5
-  __TEXT.__objc_methname: 0x14177
+  __TEXT.__objc_methname: 0x1426d
   __TEXT.__objc_methtype: 0x2525
-  __TEXT.__objc_stubs: 0xdc20
+  __TEXT.__objc_stubs: 0xdce0
   __DATA_CONST.__got: 0x368
   __DATA_CONST.__const: 0x2a38
   __DATA_CONST.__objc_classlist: 0x218
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x108
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x9048
-  __DATA_CONST.__objc_selrefs: 0x46c0
+  __DATA_CONST.__objc_const: 0x9080
+  __DATA_CONST.__objc_selrefs: 0x46f8
   __DATA_CONST.__objc_arraydata: 0x118
   __AUTH_CONST.__cfstring: 0x5420
   __AUTH_CONST.__objc_const: 0x48
   __AUTH_CONST.__objc_intobj: 0x330
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__const: 0x320
+  __AUTH_CONST.__const: 0x300
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_got: 0x6a0
   __AUTH.__objc_data: 0x50

   __DATA.__objc_ivar: 0x5a8
   __DATA.__data: 0xdc0
   __DATA.__bss: 0x108
-  __DATA_DIRTY.__const: 0xd20
+  __DATA_DIRTY.__const: 0xd40
   __DATA_DIRTY.__objc_const: 0x1cd8
   __DATA_DIRTY.__objc_data: 0x14a0
   __DATA_DIRTY.__data: 0x10

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 3349
-  Symbols:   11322
-  CStrings:  5119
+  Functions: 3358
+  Symbols:   11350
+  CStrings:  5126
 
Symbols:
+ -[WBSettingsSyncEngineAccess _attemptUpdatingSavingPerSiteSettingsWithRecord:]
+ -[WBTabCollection _profilesQuery]
+ -[WBTabCollection defaultProfileIdentifier]
+ -[WBTabCollection hasMultipleProfiles]
+ -[WBTabCollection profileWithServerID:]
+ -[WBTabGroupManager _notifySyncDidFinishedForScopedBookmarks]
+ -[WBTabGroupManager registerPinnedTab:]
+ -[WBTabGroupManager unregisterWindowState:]
+ GCC_except_table217
+ GCC_except_table222
+ GCC_except_table250
+ GCC_except_table251
+ GCC_except_table252
+ GCC_except_table263
+ GCC_except_table264
+ GCC_except_table265
+ ___38-[WBTabCollection hasMultipleProfiles]_block_invoke
+ ___39-[WBTabCollection profileWithServerID:]_block_invoke
+ ___60-[WBSettingsSyncEngineAccess deleteBackgroundImageDirectory]_block_invoke.45
+ ___60-[WebBookmarkTabCollection _regenerateSyncPositionsIfNeeded]_block_invoke.156
+ ___60-[WebBookmarkTabCollection _regenerateSyncPositionsIfNeeded]_block_invoke.156.cold.1
+ ___61-[WBTabGroupManager _notifySyncDidFinishedForScopedBookmarks]_block_invoke
+ ___72-[WebBookmarkTabCollection _saveTabGroupRecordsWithMissingCKShareRecord]_block_invoke.160
+ ___78-[WBSettingsSyncEngineAccess _attemptUpdatingSavingPerSiteSettingsWithRecord:]_block_invoke
+ ___78-[WBSettingsSyncEngineAccess _attemptUpdatingSavingPerSiteSettingsWithRecord:]_block_invoke.22
+ ___78-[WBSettingsSyncEngineAccess _attemptUpdatingSavingPerSiteSettingsWithRecord:]_block_invoke.25
+ ___78-[WBSettingsSyncEngineAccess _attemptUpdatingSavingPerSiteSettingsWithRecord:]_block_invoke.cold.1
+ ___78-[WBSettingsSyncEngineAccess _attemptUpdatingSavingPerSiteSettingsWithRecord:]_block_invoke.cold.2
+ ___78-[WBSettingsSyncEngineAccess _attemptUpdatingSavingPerSiteSettingsWithRecord:]_block_invoke.cold.3
+ ___block_descriptor_48_ea8_32s40s_e17_v16?0"NSTimer"8ls32l8s40l8
+ ___block_descriptor_48_ea8_32s40s_e8_v12?0B8ls32l8s40l8
+ ___block_literal_global.151
+ ___block_literal_global.174
+ ___block_literal_global.374
+ ___block_literal_global.398
+ ___block_literal_global.417
+ _objc_msgSend$_attemptUpdatingSavingPerSiteSettingsWithRecord:
+ _objc_msgSend$_notifySyncDidFinishedForScopedBookmarks
+ _objc_msgSend$_profilesQuery
+ _objc_msgSend$scheduledTimerWithTimeInterval:repeats:block:
+ _objc_msgSend$tabGroupManager:didFinishSyncForScopedBookmarkList:
+ _objc_msgSend$unregisterWindowState:
- GCC_except_table213
- GCC_except_table218
- GCC_except_table226
- GCC_except_table234
- GCC_except_table238
- GCC_except_table239
- GCC_except_table256
- ___60-[WBSettingsSyncEngineAccess deleteBackgroundImageDirectory]_block_invoke.43
- ___60-[WebBookmarkTabCollection _regenerateSyncPositionsIfNeeded]_block_invoke.153
- ___60-[WebBookmarkTabCollection _regenerateSyncPositionsIfNeeded]_block_invoke.153.cold.1
- ___63-[WBSettingsSyncEngineAccess _updatePerSiteSettingsWithRecord:]_block_invoke
- ___63-[WBSettingsSyncEngineAccess _updatePerSiteSettingsWithRecord:]_block_invoke.22
- ___63-[WBSettingsSyncEngineAccess _updatePerSiteSettingsWithRecord:]_block_invoke.24
- ___63-[WBSettingsSyncEngineAccess _updatePerSiteSettingsWithRecord:]_block_invoke.cold.1
- ___63-[WBSettingsSyncEngineAccess _updatePerSiteSettingsWithRecord:]_block_invoke.cold.2
- ___63-[WBSettingsSyncEngineAccess _updatePerSiteSettingsWithRecord:]_block_invoke.cold.3
- ___72-[WebBookmarkTabCollection _saveTabGroupRecordsWithMissingCKShareRecord]_block_invoke.157
- ___block_descriptor_56_ea8_32s40s48r_e5_v8?0ls32l8s40l8r48l8
- ___block_descriptor_56_ea8_32s40s48r_e8_v12?0B8ls32l8s40l8r48l8
- ___block_literal_global.145
- ___block_literal_global.160
- ___block_literal_global.171
- ___block_literal_global.371
- ___block_literal_global.395
- ___block_literal_global.414
CStrings:
+ "_attemptUpdatingSavingPerSiteSettingsWithRecord:"
+ "_notifySyncDidFinishedForScopedBookmarks"
+ "_profilesQuery"
+ "registerPinnedTab:"
+ "scheduledTimerWithTimeInterval:repeats:block:"
+ "tabGroupManager:didFinishSyncForScopedBookmarkList:"
+ "unregisterWindowState:"

```
