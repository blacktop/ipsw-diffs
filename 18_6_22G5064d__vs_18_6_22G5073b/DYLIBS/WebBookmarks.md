## WebBookmarks

> `/System/Library/PrivateFrameworks/WebBookmarks.framework/WebBookmarks`

```diff

-621.3.7.10.1
-  __TEXT.__text: 0x9e92c
+621.3.8.0.0
+  __TEXT.__text: 0x9f364
   __TEXT.__auth_stubs: 0xda0
-  __TEXT.__objc_methlist: 0x8304
+  __TEXT.__objc_methlist: 0x8344
   __TEXT.__const: 0x306
-  __TEXT.__gcc_except_tab: 0xaf90
-  __TEXT.__cstring: 0xde7c
-  __TEXT.__oslogstring: 0x7c09
+  __TEXT.__gcc_except_tab: 0xb0b8
+  __TEXT.__cstring: 0xdecc
+  __TEXT.__oslogstring: 0x7e5c
   __TEXT.__dlopen_cstrs: 0xb2
   __TEXT.__constg_swiftt: 0x60
   __TEXT.__swift5_typeref: 0x9
   __TEXT.__swift5_reflstr: 0x1c
   __TEXT.__swift5_fieldmd: 0x1c
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x4070
+  __TEXT.__unwind_info: 0x40b0
   __TEXT.__objc_classname: 0x9a7
-  __TEXT.__objc_methname: 0x159c4
+  __TEXT.__objc_methname: 0x15a0f
   __TEXT.__objc_methtype: 0x2780
-  __TEXT.__objc_stubs: 0xea00
+  __TEXT.__objc_stubs: 0xea60
   __DATA_CONST.__got: 0x790
   __DATA_CONST.__const: 0x2dc8
   __DATA_CONST.__objc_classlist: 0x220
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x100
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4be8
+  __DATA_CONST.__objc_selrefs: 0x4c00
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x1d0
   __DATA_CONST.__objc_arraydata: 0x350

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 97457DE2-A209-319C-8725-C1BB99BA511A
-  Functions: 3518
-  Symbols:   12072
-  CStrings:  6261
+  UUID: AA84531E-EEE3-3E7E-94C1-6FE16C8988C9
+  Functions: 3532
+  Symbols:   12107
+  CStrings:  6272
 
Symbols:
+ -[WBTabCollection deleteWindowsNotInLastSession]
+ -[WBTabCollection tabCountForTabGroupWithUUID:]
+ -[WBTabGroupManager deleteWindowsNotInLastSession]
+ -[WBTabGroupManager tabCountForTabGroupWithUUID:]
+ -[WBWindowState copyForRecovery]
+ -[WebBookmarkCollection _deleteBookmark:leaveTombstone:insertTombstoneBlock:].cold.1
+ -[WebBookmarkCollection _reindexBookmarkID:title:].cold.1
+ -[WebBookmarkCollection _reindexBookmarkID:title:].cold.2
+ -[WebBookmarkCollection _saveBookmark:withSpecialID:updateGenerationIfNeeded:].cold.3
+ -[WebBookmarkCollection _saveBookmark:withSpecialID:updateGenerationIfNeeded:].cold.4
+ -[WebBookmarkTabCollection tabCountForTabGroupWithUUID:]
+ GCC_except_table134
+ GCC_except_table177
+ GCC_except_table201
+ GCC_except_table211
+ GCC_except_table215
+ GCC_except_table216
+ GCC_except_table220
+ GCC_except_table231
+ GCC_except_table232
+ GCC_except_table242
+ GCC_except_table270
+ GCC_except_table271
+ GCC_except_table288
+ _OUTLINED_FUNCTION_12
+ ___47-[WBTabCollection tabCountForTabGroupWithUUID:]_block_invoke
+ ___48-[WBTabCollection deleteWindowsNotInLastSession]_block_invoke
+ ___78-[WebBookmarkCollection _saveBookmark:withSpecialID:updateGenerationIfNeeded:]_block_invoke.827
+ ___Block_byref_object_copy_.1821
+ ___Block_byref_object_dispose_.1822
+ ____ZL33prefixEndingWithFirstWordOfStringP8NSString_block_invoke.1824
+ ___block_literal_global.1015
+ ___block_literal_global.1050
+ ___block_literal_global.1120
+ ___block_literal_global.1816
+ ___block_literal_global.1819
+ ___block_literal_global.1826
+ ___block_literal_global.1834
+ _objc_msgSend$deleteWindowsNotInLastSession
+ _objc_msgSend$initWithUUID:
+ _objc_msgSend$tabCountForTabGroupWithUUID:
- GCC_except_table116
- GCC_except_table135
- GCC_except_table205
- GCC_except_table213
- GCC_except_table218
- GCC_except_table222
- GCC_except_table233
- GCC_except_table234
- GCC_except_table239
- GCC_except_table272
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
CStrings:
+ "<%@: %p; activeTabGroupUUID = %@; identifier = %d; sceneID = %@; uuid = %@; restoration_archive = %lu; localTabGroup = %@<%d> with %ld tab(s), selectedTabGroup = %@, isPrivate = %d>"
+ "Cannot save bookmark: failed to get hidden ancestor count (%i) with error: %{public}@"
+ "Cannot save bookmark: failed to update order index of bookmarks during insertion (%i) with error: %{public}@"
+ "Could not reorder bookmarks in parent: %d, error: %{public}@"
+ "Deleting windowState with UUID: %{public}@"
+ "Failed to clear title words for bookmark with ID: %d"
+ "Failed to index bookmark with ID: %d"
+ "Failed to index for bookmark with ID: (%d), word_index: (%d) and error: %{public}@"
+ "Failed to save bookmark %{public}@ isFolder: %d Invalid parentID %d"
+ "Failed to update bookmark, could not add extraAttributes %{public}@"
+ "Failed to update bookmark, could not finalize sqlite statement %{public}@ with error %{public}@"
+ "Failed to update bookmark, could not prepare sqlite statement %{public}@ with error: %{public}@"
+ "copyForRecovery"
+ "deleteWindowsNotInLastSession"
+ "tabCountForTabGroupWithUUID:"
- "<%@: %p; activeTabGroupUUID = %@; identifier = %d; sceneID = %@; uuid = %@; restoration_archive = %lu>"
- "Cannot save bookmark: failed to get hidden ancestor count (%i)"
- "Cannot save bookmark: failed to update order index of bookmarks during insertion (%i)"
- "Failed to save bookmark %{public}@: Invalid parentID %d"

```
