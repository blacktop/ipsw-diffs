## WebBookmarks

> `/System/Library/PrivateFrameworks/WebBookmarks.framework/WebBookmarks`

```diff

-622.1.21.10.3
-  __TEXT.__text: 0xa0ddc
+622.1.22.10.4
+  __TEXT.__text: 0xa1a50
   __TEXT.__auth_stubs: 0xdc0
-  __TEXT.__objc_methlist: 0x83b4
-  __TEXT.__const: 0x316
-  __TEXT.__gcc_except_tab: 0xb2d8
+  __TEXT.__objc_methlist: 0x83c4
+  __TEXT.__const: 0x326
+  __TEXT.__gcc_except_tab: 0xb414
   __TEXT.__cstring: 0xe06c
-  __TEXT.__oslogstring: 0x840c
+  __TEXT.__oslogstring: 0x876f
   __TEXT.__dlopen_cstrs: 0xb2
   __TEXT.__constg_swiftt: 0x60
   __TEXT.__swift5_typeref: 0x9
   __TEXT.__swift5_reflstr: 0x1c
   __TEXT.__swift5_fieldmd: 0x1c
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x41c0
+  __TEXT.__unwind_info: 0x41c8
   __TEXT.__objc_classname: 0x9a7
-  __TEXT.__objc_methname: 0x15b8c
+  __TEXT.__objc_methname: 0x15b98
   __TEXT.__objc_methtype: 0x26f5
-  __TEXT.__objc_stubs: 0xeae0
+  __TEXT.__objc_stubs: 0xeb00
   __DATA_CONST.__got: 0x790
   __DATA_CONST.__const: 0x2e08
   __DATA_CONST.__objc_classlist: 0x220
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x100
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4c50
+  __DATA_CONST.__objc_selrefs: 0x4c58
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x1d0
   __DATA_CONST.__objc_arraydata: 0x350

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 1FEF045C-B1A2-3EDA-B344-3882AD66C927
-  Functions: 3561
-  Symbols:   12173
-  CStrings:  6317
+  UUID: 6125708C-D7BA-35A5-A00B-53B641C8BB99
+  Functions: 3569
+  Symbols:   12192
+  CStrings:  6331
 
Symbols:
+ -[WBTabCollection _commonInit]
+ -[WBTabGroupManager _cacheTabGroup:creatorDeviceUUID:].cold.1
+ -[WBTabGroupManager _reorderTabGroup:afterTabGroup:].cold.1
+ -[WBTabGroupManager updateTabWithUUID:persist:notify:usingBlock:].cold.1
+ -[WebBookmarkTabCollection _saveWindowState:].cold.6
+ -[WebBookmarkTabCollection _windowStatesWithFilter:].cold.2
+ -[WebBookmarkTabCollection tabGroupsChildrenForBookmark:].cold.1
+ -[WebBookmarkTabCollection tabsForTabGroupBookmark:].cold.1
+ GCC_except_table116
+ GCC_except_table205
+ GCC_except_table213
+ GCC_except_table222
+ GCC_except_table233
+ GCC_except_table237
+ GCC_except_table272
+ ___151-[WBTabGroupManager _performCRDTMergeAndMapTabsToParentIdentifiersWithProfilesByIdentifier:devicesByUUID:uninsertedSyncableTabsFromSyncableTabsByUUID:]_block_invoke.52
+ ___68-[WBTabGroupManager _dequeueNextAcceptCloudKitShareMetadataIfNeeded]_block_invoke.145
+ ___block_descriptor_64_e8_32s40s48s56s_e39_v32?0"NSString"8"WBMutableTab"16^B24ls32l8s40l8s48l8s56l8
+ ___block_literal_global.107
+ ___block_literal_global.114
+ ___block_literal_global.116
+ ___block_literal_global.123
+ ___block_literal_global.125
+ ___block_literal_global.152
+ ___block_literal_global.55
+ ___block_literal_global.67
+ ___block_literal_global.70
+ ___block_literal_global.73
+ ___block_literal_global.90
+ ___block_literal_global.92
+ ___block_literal_global.95
+ _objc_msgSend$_commonInit
- GCC_except_table137
- GCC_except_table168
- GCC_except_table204
- GCC_except_table214
- GCC_except_table219
- GCC_except_table223
- GCC_except_table240
- GCC_except_table262
- ___151-[WBTabGroupManager _performCRDTMergeAndMapTabsToParentIdentifiersWithProfilesByIdentifier:devicesByUUID:uninsertedSyncableTabsFromSyncableTabsByUUID:]_block_invoke_4
- ___68-[WBTabGroupManager _dequeueNextAcceptCloudKitShareMetadataIfNeeded]_block_invoke.144
- ___block_descriptor_56_e8_32s40s48s_e39_v32?0"NSString"8"WBMutableTab"16^B24ls32l8s40l8s48l8
- ___block_literal_global.106
- ___block_literal_global.113
- ___block_literal_global.115
- ___block_literal_global.124
- ___block_literal_global.59
- ___block_literal_global.66
- ___block_literal_global.69
- ___block_literal_global.72
- ___block_literal_global.89
- ___block_literal_global.91
- ___block_literal_global.94
CStrings:
+ "%lu tabs were filtered because they were removed. UUIDS:%{public}@"
+ "Add tabs in tab group to the parent identifier dictionary %{public}@"
+ "Couldn't find profile in the cache %@"
+ "Did not cache %lu tabs in tab group %{public}@ because the tab group was removed"
+ "Local tab group %{public}@ is getting saved to disk with no tabs"
+ "Merging profile in database %@ with profile in the cache %@"
+ "No tab groups found for profile: %{public}@"
+ "No tabs found for tab group bookmark: %{public}@"
+ "Not moving tab group %{public}@ because it does not exist."
+ "Removing unnamed tab group bookmark because it wasn't in the current tab state %{public}@."
+ "Saving tab group %{public}@ with %{public}lu tabs into the cache."
+ "Setup with path failed for path %{public}@."
+ "Tab %{public}@ has invalid parent identifier and moved under %{public}@"
+ "Tab group cache is updated from %{public}lu to %{public}lu"
+ "Updating the web bookmarks from version: %{public}@ to the current version: %{public}@."
+ "Window state local tab group has no tabs: %{public}@"
+ "_commonInit"
- "Filtering tab group %{public}@ because it was removed"
- "Not moving tab group %{public}@ because it no longer exists"
- "Setup with path failed."

```
