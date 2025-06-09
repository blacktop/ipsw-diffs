## WebBookmarks

> `/System/Library/PrivateFrameworks/WebBookmarks.framework/WebBookmarks`

```diff

-621.2.5.10.10
-  __TEXT.__text: 0x9e0e8
+622.1.14.10.4
+  __TEXT.__text: 0x9f074
   __TEXT.__auth_stubs: 0xda0
-  __TEXT.__objc_methlist: 0x8304
+  __TEXT.__objc_methlist: 0x833c
   __TEXT.__const: 0x306
-  __TEXT.__gcc_except_tab: 0xae64
-  __TEXT.__cstring: 0xde9c
-  __TEXT.__oslogstring: 0x7aff
+  __TEXT.__gcc_except_tab: 0xb034
+  __TEXT.__cstring: 0xe06c
+  __TEXT.__oslogstring: 0x7faf
   __TEXT.__dlopen_cstrs: 0xb2
   __TEXT.__constg_swiftt: 0x60
   __TEXT.__swift5_typeref: 0x9
   __TEXT.__swift5_reflstr: 0x1c
   __TEXT.__swift5_fieldmd: 0x1c
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x4068
+  __TEXT.__unwind_info: 0x40a0
   __TEXT.__objc_classname: 0x9a7
-  __TEXT.__objc_methname: 0x159c4
-  __TEXT.__objc_methtype: 0x2780
-  __TEXT.__objc_stubs: 0xea00
+  __TEXT.__objc_methname: 0x15ab2
+  __TEXT.__objc_methtype: 0x26f5
+  __TEXT.__objc_stubs: 0xea40
   __DATA_CONST.__got: 0x790
-  __DATA_CONST.__const: 0x2dd0
+  __DATA_CONST.__const: 0x2e48
   __DATA_CONST.__objc_classlist: 0x220
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x100
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4be8
+  __DATA_CONST.__objc_selrefs: 0x4c18
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x1d0
   __DATA_CONST.__objc_arraydata: 0x350
   __AUTH_CONST.__auth_got: 0x6e8
-  __AUTH_CONST.__const: 0x1140
-  __AUTH_CONST.__cfstring: 0x6000
-  __AUTH_CONST.__objc_const: 0x99b8
+  __AUTH_CONST.__const: 0x1180
+  __AUTH_CONST.__cfstring: 0x6060
+  __AUTH_CONST.__objc_const: 0x9a10
   __AUTH_CONST.__objc_intobj: 0x360
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_arrayobj: 0xd8
+  __AUTH.__objc_data: 0x50
   __AUTH.__data: 0xb8
-  __DATA.__objc_ivar: 0x5ec
-  __DATA.__data: 0xef0
+  __DATA.__objc_ivar: 0x5f0
+  __DATA.__data: 0xf18
   __DATA.__bss: 0x10c
-  __DATA_DIRTY.__objc_data: 0x14f0
+  __DATA_DIRTY.__objc_data: 0x14a0
   __DATA_DIRTY.__data: 0x10
   __DATA_DIRTY.__bss: 0x260
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
+  - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_errno.dylib
-  - /usr/lib/swift/libswift_math.dylib
-  - /usr/lib/swift/libswift_signal.dylib
-  - /usr/lib/swift/libswift_stdio.dylib
-  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  - /usr/lib/swift/libswiftsys_time.dylib
-  - /usr/lib/swift/libswiftunistd.dylib
-  UUID: E373996C-1E1C-3370-AD00-E29CAF099E11
-  Functions: 3516
-  Symbols:   12068
-  CStrings:  6258
+  UUID: 6D6550E6-43A6-30E8-8BFF-5C1B50837C4E
+  Functions: 3540
+  Symbols:   12128
+  CStrings:  6294
 
Symbols:
+ -[WBTab initWithBookmarkStorage:].cold.2
+ -[WebBookmark initManagedBookmarkFolderWithTitle:uuid:]
+ -[WebBookmark initManagedBookmarkWithTitle:address:uuid:]
+ -[WebBookmark managedBookmarkUUID]
+ -[WebBookmarkCollection _saveBookmark:withSpecialID:updateGenerationIfNeeded:].cold.10
+ -[WebBookmarkCollection _saveBookmark:withSpecialID:updateGenerationIfNeeded:].cold.11
+ -[WebBookmarkCollection _saveBookmark:withSpecialID:updateGenerationIfNeeded:].cold.12
+ -[WebBookmarkCollection _saveBookmark:withSpecialID:updateGenerationIfNeeded:].cold.13
+ -[WebBookmarkCollection _saveBookmark:withSpecialID:updateGenerationIfNeeded:].cold.14
+ -[WebBookmarkCollection _saveBookmark:withSpecialID:updateGenerationIfNeeded:].cold.15
+ -[WebBookmarkCollection _saveBookmark:withSpecialID:updateGenerationIfNeeded:].cold.3
+ -[WebBookmarkCollection _saveBookmark:withSpecialID:updateGenerationIfNeeded:].cold.4
+ -[WebBookmarkCollection _saveBookmark:withSpecialID:updateGenerationIfNeeded:].cold.5
+ -[WebBookmarkCollection _saveBookmark:withSpecialID:updateGenerationIfNeeded:].cold.6
+ -[WebBookmarkCollection _saveBookmark:withSpecialID:updateGenerationIfNeeded:].cold.7
+ -[WebBookmarkCollection _saveBookmark:withSpecialID:updateGenerationIfNeeded:].cold.8
+ -[WebBookmarkCollection _saveBookmark:withSpecialID:updateGenerationIfNeeded:].cold.9
+ -[WebBookmarkCollection allBookmarkFolders]
+ -[WebBookmarkCollection bookmarksByDateAdded]
+ -[WebBookmarkCollection folderContents:]
+ GCC_except_table134
+ GCC_except_table510
+ GCC_except_table511
+ GCC_except_table512
+ GCC_except_table513
+ GCC_except_table514
+ GCC_except_table521
+ GCC_except_table528
+ GCC_except_table529
+ _OBJC_IVAR_$_WebBookmark._managedBookmarkUUID
+ _WebBookmarksDidReloadDistributedNotification
+ ___45-[WebBookmarkCollection bookmarksByDateAdded]_block_invoke
+ ___45-[WebBookmarkCollection bookmarksByDateAdded]_block_invoke_2
+ ___57-[WebBookmarkCollection _updateBookmarks:inFolderWithID:]_block_invoke.404
+ ___57-[WebBookmarkCollection _updateBookmarks:inFolderWithID:]_block_invoke.406
+ ___57-[WebBookmarkCollection _updateBookmarks:inFolderWithID:]_block_invoke.406.cold.1
+ ___57-[WebBookmarkCollection _updateBookmarks:inFolderWithID:]_block_invoke.406.cold.2
+ ___57-[WebBookmarkCollection _updateBookmarks:inFolderWithID:]_block_invoke.406.cold.3
+ ___57-[WebBookmarkCollection _updateBookmarks:inFolderWithID:]_block_invoke.406.cold.4
+ ___57-[WebBookmarkCollection _updateBookmarks:inFolderWithID:]_block_invoke_2.407
+ ___78-[WebBookmarkCollection _saveBookmark:withSpecialID:updateGenerationIfNeeded:]_block_invoke.830
+ ___Block_byref_object_copy_.1843
+ ___Block_byref_object_dispose_.1844
+ ____ZL33prefixEndingWithFirstWordOfStringP8NSString_block_invoke.1846
+ ___block_descriptor_56_ea8_32s40r_e25_B32?0"NSString"8Q16^B24lr40l8s32l8
+ ___block_descriptor_56_ea8_32s40s48s_e25_v32?0"NSString"8Q16^B24ls32l8s40l8s48l8
+ ___block_descriptor_60_ea8_32s40s48r_e35_v32?0"NSString"8"NSString"16^B24ls32l8s40l8r48l8
+ ___block_literal_global.1018
+ ___block_literal_global.1053
+ ___block_literal_global.1123
+ ___block_literal_global.1133
+ ___block_literal_global.1135
+ ___block_literal_global.1838
+ ___block_literal_global.1841
+ ___block_literal_global.1848
+ ___block_literal_global.1856
+ ___block_literal_global.233
+ ___block_literal_global.452
+ ___block_literal_global.460
+ __swift_FORCE_LOAD_$_swiftAccelerate
+ __swift_FORCE_LOAD_$_swiftAccelerate_$_WebBookmarks
+ __swift_FORCE_LOAD_$_swiftCompression
+ __swift_FORCE_LOAD_$_swiftCompression_$_WebBookmarks
+ __swift_FORCE_LOAD_$_swiftCoreImage
+ __swift_FORCE_LOAD_$_swiftCoreImage_$_WebBookmarks
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_WebBookmarks
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_WebBookmarks
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_WebBookmarks
+ _kWebBookmarksOpenSafariExportSettings
+ _kWebBookmarksOpenSafariExportSettingsFailedKey
+ _kWebBookmarksOpenSafariExportSettingsMissingEntitlementKey
+ _kWebBookmarksOpenSafariExportSettingsNotRunningForegroundKey
+ _kWebBookmarksOpenSafariExportSettingsTestingModeKey
+ _objc_msgSend$isBuiltinBookmark
+ _objc_msgSend$preferredVisiblePositionForNewSectionWithIdentifier:
+ _objc_msgSend$reorderSectionsToMatchOrderedIdentifiers:
- -[WebBookmarkTabCollection _createSpecialFolderWithIDIfNeeded:]
- GCC_except_table516
- GCC_except_table523
- GCC_except_table524
- ___57-[WebBookmarkCollection _updateBookmarks:inFolderWithID:]_block_invoke.401
- ___57-[WebBookmarkCollection _updateBookmarks:inFolderWithID:]_block_invoke.403
- ___57-[WebBookmarkCollection _updateBookmarks:inFolderWithID:]_block_invoke.403.cold.1
- ___57-[WebBookmarkCollection _updateBookmarks:inFolderWithID:]_block_invoke.403.cold.2
- ___57-[WebBookmarkCollection _updateBookmarks:inFolderWithID:]_block_invoke.403.cold.3
- ___57-[WebBookmarkCollection _updateBookmarks:inFolderWithID:]_block_invoke.403.cold.4
- ___57-[WebBookmarkCollection _updateBookmarks:inFolderWithID:]_block_invoke_2.404
- ___78-[WebBookmarkCollection _saveBookmark:withSpecialID:updateGenerationIfNeeded:]_block_invoke_2
- ___Block_byref_object_copy_.1820
- ___Block_byref_object_dispose_.1821
- ____ZL33prefixEndingWithFirstWordOfStringP8NSString_block_invoke.1823
- ___block_literal_global.1014
- ___block_literal_global.1049
- ___block_literal_global.1119
- ___block_literal_global.1815
- ___block_literal_global.1818
- ___block_literal_global.1825
- ___block_literal_global.1833
- ___block_literal_global.230
- ___block_literal_global.449
- ___block_literal_global.463
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_errno_$_WebBookmarks
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_math_$_WebBookmarks
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_signal_$_WebBookmarks
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_stdio_$_WebBookmarks
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swift_time_$_WebBookmarks
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftsys_time_$_WebBookmarks
- __swift_FORCE_LOAD_$_swiftunistd
- __swift_FORCE_LOAD_$_swiftunistd_$_WebBookmarks
- _objc_msgSend$setSectionsIdentifiers:enabledIndexes:
CStrings:
+ "## %s(value: %{private}@)"
+ "(%@ %@) %@ %@ %@ %@"
+ "<%@: %p; activeTabGroupUUID = %@; identifier = %d; sceneID = %@; uuid = %@; restoration_archive = %lu; localTabGroup = %@<%d> with %ld tab(s), selectedTabGroup = %@>"
+ "Background task will expire soon. Block performing saving bookmarks. %{public}@"
+ "Error converting in-memory changes into plist data: %{public}@"
+ "Failed to add bookmark %{public}@"
+ "Failed to save active tab (%{public}@) in tabgroup with ID: (%{public}@) and windowID: (%{public}@)"
+ "Failed to save local tab group %{public}@ while trying to save window state with UUID: %{public}@"
+ "Failed to save private tab group %{public}@ while trying to save window state with UUID: %{public}@"
+ "Failed to save unnamed tab group (%{public}@) in window with UUID: (%{public}@)"
+ "Failed to save window state %{public}@."
+ "Failed to update bookmark, could add extraAttributes %{public}@"
+ "Failed to update bookmark, could not add localAttributes %{public}@"
+ "Failed to update bookmark, could not finalize sqlite statement %{public}@"
+ "Failed to update bookmark, could not increment generation for bookmark: %{public}@"
+ "Failed to update bookmark, could not mark bookmark %{public}@ with special ID: <%d>"
+ "Failed to update bookmark, could not prepare sqlite statement %{public}@"
+ "Failed to update bookmark, could not update child count for parent <%d> and bookmark: %{public}@"
+ "Failed to update bookmark, could not update hidden ancestor count for folder: %{public}@"
+ "Failed to update bookmark, could not update reading list item: %{public}@"
+ "Failed to update bookmark, could update hidden flag %{public}@"
+ "Failed to update bookmark, failed to reindex bookmark: %{public}@"
+ "Failed to update bookmark, failed to update sync data for bookmark: %{public}@"
+ "OpenSafariExportSettings"
+ "OpenSafariExportSettingsFailedKey"
+ "OpenSafariExportSettingsMissingEntitlementKey"
+ "OpenSafariExportSettingsNotRunningForegroundKey"
+ "OpenSafariExportSettingsTestingMode"
+ "T@\"NSUUID\",R,N,V_managedBookmarkUUID"
+ "UPDATE bookmarks SET title = ?1, url = ?2, extra_attributes = ?3, local_attributes = ?11, fetched_icon = ?4, icon = ?5, locally_added = ?10, archive_status = ?8, web_filter_status = ?12,last_selected_child = ?14%@%@ WHERE id = ?6"
+ "WBTab initialized with a malformed UUID %{public}@"
+ "WBTab must be backed by a bookmark %{public}@"
+ "WBTab must have a UUID %{public}@"
+ "_managedBookmarkUUID"
+ "allBookmarkFolders"
+ "bookmarksByDateAdded"
+ "com.apple.WebBookmarks.WebBookmarksDidReloadNotification"
+ "folderContents:"
+ "id DESC"
+ "initManagedBookmarkFolderWithTitle:uuid:"
+ "initManagedBookmarkWithTitle:address:uuid:"
+ "managedBookmarkUUID"
+ "preferredVisiblePositionForNewSectionWithIdentifier:"
+ "reorderSectionsToMatchOrderedIdentifiers:"
+ "type = 0 AND syncable = 1 AND deleted = 0 AND editable = 1 AND deletable = 1"
+ "type = 1 AND syncable = 1 AND deleted = 0 AND editable = 1 AND deletable = 1"
+ "{unique_ptr<WebBookmarks::BookmarkSQLWriteTransaction, std::default_delete<WebBookmarks::BookmarkSQLWriteTransaction>>=\"__ptr_\"^{BookmarkSQLWriteTransaction}}"
- "(%@ %@) %@ %@ %@"
- "<%@: %p; activeTabGroupUUID = %@; identifier = %d; sceneID = %@; uuid = %@; restoration_archive = %lu>"
- "Background task will expire soon. Block performing saving bookmarks. %@{public}"
- "Error converting in-memory changes into plist data: %@{public}"
- "Failed to save active tab (%{public}@) in tabgroup with ID: (%{public}@) and windowID: (%d)"
- "Failed to save local tab group while trying to save window state"
- "Failed to save private tab group while trying to save window state"
- "Failed to save unnamed tab group (%{public}@) in window with ID: (%d)"
- "Failed to save window state."
- "UPDATE bookmarks SET title = ?1, url = ?2, extra_attributes = ?3, local_attributes = ?11, fetched_icon = ?4, icon = ?5, locally_added = ?10, archive_status = ?8, web_filter_status = ?12, last_selected_child = ?14%@%@ WHERE id = ?6"
- "Windows"
- "_createSpecialFolderWithIDIfNeeded:"
- "setSectionsIdentifiers:enabledIndexes:"
- "{unique_ptr<WebBookmarks::BookmarkSQLWriteTransaction, std::default_delete<WebBookmarks::BookmarkSQLWriteTransaction>>=\"__ptr_\"{__compressed_pair<WebBookmarks::BookmarkSQLWriteTransaction *, std::default_delete<WebBookmarks::BookmarkSQLWriteTransaction>>=\"__value_\"^{BookmarkSQLWriteTransaction}}}"

```
