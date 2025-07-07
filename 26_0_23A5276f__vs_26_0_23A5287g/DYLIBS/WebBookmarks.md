## WebBookmarks

> `/System/Library/PrivateFrameworks/WebBookmarks.framework/WebBookmarks`

```diff

-622.1.16.10.3
-  __TEXT.__text: 0x9fd94
+622.1.18.10.3
+  __TEXT.__text: 0xa06e0
   __TEXT.__auth_stubs: 0xda0
-  __TEXT.__objc_methlist: 0x833c
+  __TEXT.__objc_methlist: 0x8384
   __TEXT.__const: 0x316
-  __TEXT.__gcc_except_tab: 0xb1a0
-  __TEXT.__cstring: 0xe04c
-  __TEXT.__oslogstring: 0x8157
+  __TEXT.__gcc_except_tab: 0xb280
+  __TEXT.__cstring: 0xe05c
+  __TEXT.__oslogstring: 0x82d7
   __TEXT.__dlopen_cstrs: 0xb2
   __TEXT.__constg_swiftt: 0x60
   __TEXT.__swift5_typeref: 0x9
   __TEXT.__swift5_reflstr: 0x1c
   __TEXT.__swift5_fieldmd: 0x1c
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x40b0
+  __TEXT.__unwind_info: 0x41a8
   __TEXT.__objc_classname: 0x9a7
-  __TEXT.__objc_methname: 0x15ab2
+  __TEXT.__objc_methname: 0x15afd
   __TEXT.__objc_methtype: 0x26f5
-  __TEXT.__objc_stubs: 0xea40
+  __TEXT.__objc_stubs: 0xeaa0
   __DATA_CONST.__got: 0x790
   __DATA_CONST.__const: 0x2e20
   __DATA_CONST.__objc_classlist: 0x220
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x100
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4c18
+  __DATA_CONST.__objc_selrefs: 0x4c30
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x1d0
   __DATA_CONST.__objc_arraydata: 0x350

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 1BC90EE4-AB24-3FF1-BDC9-51D78A4BBD2F
-  Functions: 3543
-  Symbols:   12126
-  CStrings:  6299
+  UUID: D9C820C0-1230-3B28-8F00-B79D591E644D
+  Functions: 3554
+  Symbols:   12157
+  CStrings:  6307
 
Symbols:
+ -[WBBookmarkDBAccess copyValueForKey:item:].cold.8
+ -[WBTabCollection deleteWindowsNotInLastSession]
+ -[WBTabCollection tabCountForTabGroupWithUUID:]
+ -[WBTabGroupManager deleteWindowsNotInLastSession]
+ -[WBTabGroupManager tabCountForTabGroupWithUUID:]
+ -[WBWindowState copyForRecovery]
+ -[WebBookmarkCollection _deleteBookmark:leaveTombstone:insertTombstoneBlock:].cold.1
+ -[WebBookmarkCollection _reindexBookmarkID:title:].cold.1
+ -[WebBookmarkCollection _reindexBookmarkID:title:].cold.2
+ -[WebBookmarkTabCollection tabCountForTabGroupWithUUID:]
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
+ _objc_msgSend$deleteWindowsNotInLastSession
+ _objc_msgSend$initWithUUID:
+ _objc_msgSend$tabCountForTabGroupWithUUID:
- -[WebBookmarkCollection _saveBookmark:withSpecialID:updateGenerationIfNeeded:].cold.15
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
- "<%@: %p; activeTabGroupUUID = %@; identifier = %d; sceneID = %@; uuid = %@; restoration_archive = %lu; localTabGroup = %@<%d> with %ld tab(s), selectedTabGroup = %@>"
- "Cannot save bookmark: failed to get hidden ancestor count (%i)"
- "Cannot save bookmark: failed to update order index of bookmarks during insertion (%i)"
- "Failed to save bookmark %{public}@: Invalid parentID %d"
- "Failed to update bookmark, could add extraAttributes %{public}@"
- "Failed to update bookmark, could not finalize sqlite statement %{public}@"
- "Failed to update bookmark, could not prepare sqlite statement %{public}@"

```
