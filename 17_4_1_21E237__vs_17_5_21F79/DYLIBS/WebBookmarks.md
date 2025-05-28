## WebBookmarks

> `/System/Library/PrivateFrameworks/WebBookmarks.framework/WebBookmarks`

```diff

-618.1.15.10.15
-  __TEXT.__text: 0x949dc
+618.2.12.10.9
+  __TEXT.__text: 0x950b0
   __TEXT.__auth_stubs: 0xcf0
-  __TEXT.__objc_methlist: 0x70a8
+  __TEXT.__objc_methlist: 0x70e0
   __TEXT.__const: 0x1b8
-  __TEXT.__gcc_except_tab: 0x9878
-  __TEXT.__cstring: 0xd225
-  __TEXT.__oslogstring: 0x6b36
+  __TEXT.__gcc_except_tab: 0x9918
+  __TEXT.__cstring: 0xd296
+  __TEXT.__oslogstring: 0x6bc2
   __TEXT.__dlopen_cstrs: 0xb2
-  __TEXT.__unwind_info: 0x3e60
+  __TEXT.__unwind_info: 0x3f1c
   __TEXT.__eh_frame: 0x38
   __TEXT.__objc_classname: 0x991
-  __TEXT.__objc_methname: 0x14815
+  __TEXT.__objc_methname: 0x148fd
   __TEXT.__objc_methtype: 0x2636
-  __TEXT.__objc_stubs: 0xe060
+  __TEXT.__objc_stubs: 0xe0e0
   __DATA_CONST.__got: 0x378
-  __DATA_CONST.__const: 0x2b08
+  __DATA_CONST.__const: 0x2b30
   __DATA_CONST.__objc_classlist: 0x210
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x100
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x8fc0
-  __DATA_CONST.__objc_selrefs: 0x4848
+  __DATA_CONST.__objc_const: 0x8ff0
+  __DATA_CONST.__objc_selrefs: 0x4868
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_classrefs: 0x428
   __DATA_CONST.__objc_superrefs: 0x1d0
   __DATA_CONST.__objc_arraydata: 0x128
-  __AUTH_CONST.__cfstring: 0x5800
-  __AUTH_CONST.__objc_const: 0x48
-  __AUTH_CONST.__const: 0x560
+  __AUTH_CONST.__cfstring: 0x5840
+  __AUTH_CONST.__objc_const: 0x0
+  __AUTH_CONST.__const: 0x440
   __AUTH_CONST.__objc_intobj: 0x360
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_got: 0x690
-  __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0x5a4
+  __DATA.__objc_ivar: 0x5a8
   __DATA.__data: 0xd60
   __DATA.__bss: 0xf8
-  __DATA_DIRTY.__const: 0xae0
-  __DATA_DIRTY.__objc_const: 0x1c90
-  __DATA_DIRTY.__objc_data: 0x1450
+  __DATA_DIRTY.__const: 0xc00
+  __DATA_DIRTY.__objc_const: 0x1cd8
+  __DATA_DIRTY.__objc_data: 0x14a0
   __DATA_DIRTY.__data: 0x10
   __DATA_DIRTY.__bss: 0x248
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 3357
-  Symbols:   11390
-  CStrings:  5205
+  Functions: 3365
+  Symbols:   11414
+  CStrings:  5214
 
Symbols:
+ -[WBTabGroupManager _allSyncedTabGroupsExceptRemoteUnnamedTabGroups]
+ -[WBTabGroupManager _cacheTabGroup:creatorDeviceUUID:]
+ -[WBTabGroupManager _didLocallyCreateUnnamedTabGroup:]
+ -[WBTabGroupManager _updateTabsAndCacheTabGroup:withTabsByParentIdentifiers:creatorDeviceUUID:]
+ -[WBTabGroupManager allSyncedTabGroupsExceptRemoteUnnamedTabGroups]
+ -[WebBookmark dealloc]
+ -[WebBookmarkCollection _performSafariVersionUpgradesOutsideSafariProcessFromPreviousVersion:]
+ -[WebBookmarkCollection _updateDatabaseOutsideSafariProcessIfNewerSafariVersionWasLaunched]
+ -[WebBookmarkTabCollection _allUnnamedTabGroupUUIDsFromCurrentWindowStates]
+ -[WebBookmarkTabCollection _performSafariVersionUpgradesOutsideSafariProcessFromPreviousVersion:]
+ -[WebBookmarkTabCollection _performSafariVersionUpgradesOutsideSafariProcessFromPreviousVersion:].cold.1
+ -[WebBookmarkTabCollection _removeClosedLocallyCreatedUnnamedTabGroups]
+ GCC_except_table108
+ _OBJC_IVAR_$_WBTabGroupManager._deviceUUIDByTabGroupUUID
+ ___22-[WebBookmark dealloc]_block_invoke
+ ___60-[WebBookmarkTabCollection _regenerateSyncPositionsIfNeeded]_block_invoke.175
+ ___60-[WebBookmarkTabCollection _regenerateSyncPositionsIfNeeded]_block_invoke.175.cold.1
+ ___68-[WBTabGroupManager _allSyncedTabGroupsExceptRemoteUnnamedTabGroups]_block_invoke
+ ___72-[WebBookmarkTabCollection _saveTabGroupRecordsWithMissingCKShareRecord]_block_invoke.179
+ ___block_descriptor_41_e8_32s_e8_v12?0B8ls32l8
+ ___block_literal_global.167
+ ___block_literal_global.170
+ ___block_literal_global.182
+ ___block_literal_global.193
+ ___block_literal_global.393
+ ___block_literal_global.417
+ ___block_literal_global.436
+ ___block_literal_global.77
+ ___block_literal_global.79
+ _objc_msgSend$_allSyncedTabGroupsExceptRemoteUnnamedTabGroups
+ _objc_msgSend$_allUnnamedTabGroupUUIDsFromCurrentWindowStates
+ _objc_msgSend$_cacheTabGroup:creatorDeviceUUID:
+ _objc_msgSend$_didLocallyCreateUnnamedTabGroup:
+ _objc_msgSend$_removeClosedLocallyCreatedUnnamedTabGroups
+ _objc_msgSend$_updateDatabaseOutsideSafariProcessIfNewerSafariVersionWasLaunched
+ _objc_msgSend$_updateTabsAndCacheTabGroup:withTabsByParentIdentifiers:creatorDeviceUUID:
+ _objc_msgSend$allSyncedTabGroupsExceptRemoteUnnamedTabGroups
+ _objc_msgSend$safari_isInSyncAgent
- -[WBTabGroupManager _cacheTabGroup:]
- -[WBTabGroupManager _updateTabsAndCacheTabGroup:withTabsByParentIdentifiers:]
- -[WebBookmarkCollection _performSafariVersionUpgradesInSafariProcessFromPreviousVersion:]
- -[WebBookmarkCollection _updateDatabaseFromSafariProcessIfNewerSafariVersionWasLaunched]
- -[WebBookmarkTabCollection _allTabsThatExceededLocalAttributesSizeLimit]
- -[WebBookmarkTabCollection _performSafariVersionUpgradesInSafariProcessFromPreviousVersion:]
- GCC_except_table133
- GCC_except_table230
- ___60-[WebBookmarkTabCollection _regenerateSyncPositionsIfNeeded]_block_invoke.169
- ___60-[WebBookmarkTabCollection _regenerateSyncPositionsIfNeeded]_block_invoke.169.cold.1
- ___72-[WebBookmarkTabCollection _saveTabGroupRecordsWithMissingCKShareRecord]_block_invoke.173
- ___block_literal_global.161
- ___block_literal_global.164
- ___block_literal_global.176
- ___block_literal_global.187
- ___block_literal_global.386
- ___block_literal_global.410
- ___block_literal_global.429
- ___block_literal_global.76
- ___block_literal_global.78
- _objc_msgSend$_allTabsThatExceededLocalAttributesSizeLimit
- _objc_msgSend$_cacheTabGroup:
- _objc_msgSend$_updateDatabaseFromSafariProcessIfNewerSafariVersionWasLaunched
- _objc_msgSend$_updateTabsAndCacheTabGroup:withTabsByParentIdentifiers:
- _objc_msgSend$safari_isSafariApplicationPlatform
CStrings:
+ "\x0f\x03\x14\x14\x12"
+ "618.2.3"
+ "Failed to remove unnamed tab groups from windows that were already closed."
+ "NewestLaunchedSafariVersionOutsideApplicationProcess"
+ "Removed unnamed tab groups from windows that were already closed"
+ "_allSyncedTabGroupsExceptRemoteUnnamedTabGroups"
+ "_allUnnamedTabGroupUUIDsFromCurrentWindowStates"
+ "_cacheTabGroup:creatorDeviceUUID:"
+ "_deviceUUIDByTabGroupUUID"
+ "_didLocallyCreateUnnamedTabGroup:"
+ "_performSafariVersionUpgradesOutsideSafariProcessFromPreviousVersion:"
+ "_removeClosedLocallyCreatedUnnamedTabGroups"
+ "_updateDatabaseOutsideSafariProcessIfNewerSafariVersionWasLaunched"
+ "_updateTabsAndCacheTabGroup:withTabsByParentIdentifiers:creatorDeviceUUID:"
+ "allSyncedTabGroupsExceptRemoteUnnamedTabGroups"
+ "newestLaunchedSafariOutsideSafariProcessVersion"
+ "safari_isInSyncAgent"
+ "type = 1 AND subtype = 0 AND parent in (SELECT id FROM bookmarks WHERE type = 1 AND subtype = 3)"
+ "v40@0:8@16B24B28@?32"
- "\x0f\x02\x14\x14\x12"
- "@40@0:8@16B24B28@?32"
- "NewestLaunchedSafariVersionInApplicationProcess"
- "_allTabsThatExceededLocalAttributesSizeLimit"
- "_cacheTabGroup:"
- "_performSafariVersionUpgradesInSafariProcessFromPreviousVersion:"
- "_updateDatabaseFromSafariProcessIfNewerSafariVersionWasLaunched"
- "_updateTabsAndCacheTabGroup:withTabsByParentIdentifiers:"
- "newestLaunchedSafariFromSafariProcessVersion"
- "safari_isSafariApplicationPlatform"

```
