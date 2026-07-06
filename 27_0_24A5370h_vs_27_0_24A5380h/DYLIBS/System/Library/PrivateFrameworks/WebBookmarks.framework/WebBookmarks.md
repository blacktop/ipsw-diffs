## WebBookmarks

> `/System/Library/PrivateFrameworks/WebBookmarks.framework/WebBookmarks`

```diff

-  __TEXT.__text: 0xa637c
-  __TEXT.__objc_methlist: 0x8884
+  __TEXT.__text: 0xa726c
+  __TEXT.__objc_methlist: 0x893c
   __TEXT.__const: 0x326
-  __TEXT.__gcc_except_tab: 0xc004
-  __TEXT.__cstring: 0xfbf1
-  __TEXT.__oslogstring: 0x9d87
+  __TEXT.__gcc_except_tab: 0xc1e4
+  __TEXT.__cstring: 0xfc87
+  __TEXT.__oslogstring: 0x9e5d
   __TEXT.__dlopen_cstrs: 0xb2
   __TEXT.__constg_swiftt: 0x60
   __TEXT.__swift5_typeref: 0x9
   __TEXT.__swift5_reflstr: 0x1c
   __TEXT.__swift5_fieldmd: 0x1c
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x4690
+  __TEXT.__unwind_info: 0x46f8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x3008
-  __DATA_CONST.__objc_classlist: 0x230
+  __DATA_CONST.__const: 0x3060
+  __DATA_CONST.__objc_classlist: 0x238
   __DATA_CONST.__objc_catlist: 0x20
-  __DATA_CONST.__objc_protolist: 0x108
+  __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5060
+  __DATA_CONST.__objc_selrefs: 0x50a8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x1e0
+  __DATA_CONST.__objc_superrefs: 0x1e8
   __DATA_CONST.__objc_arraydata: 0x370
-  __DATA_CONST.__got: 0x7f8
+  __DATA_CONST.__got: 0x818
   __AUTH_CONST.__const: 0xfe0
   __AUTH_CONST.__cfstring: 0x6440
-  __AUTH_CONST.__objc_const: 0x9d80
+  __AUTH_CONST.__objc_const: 0x9f00
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_intobj: 0x3c0
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_arrayobj: 0xd8
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x140
-  __AUTH.__data: 0xb8
-  __DATA.__objc_ivar: 0x61c
-  __DATA.__data: 0x1070
+  __AUTH.__objc_data: 0x50
+  __DATA.__objc_ivar: 0x624
+  __DATA.__data: 0x10d0
   __DATA.__bss: 0x74
-  __DATA_DIRTY.__objc_data: 0x1450
-  __DATA_DIRTY.__data: 0x10
+  __DATA_DIRTY.__objc_data: 0x1590
+  __DATA_DIRTY.__data: 0xc8
   __DATA_DIRTY.__bss: 0x218
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3692
-  Symbols:   12705
-  CStrings:  2879
+  Functions: 3706
+  Symbols:   12761
+  CStrings:  2884
 
Sections:
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_fieldmd : content changed
~ __TEXT.__swift5_types : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__weak_auth_got : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
Symbols:
+ +[WBProfile profileTitleWithTitle:forProfileIdentifier:]
+ -[WBTab clusterID]
+ -[WebBookmark(ReadingList) featureTextFetchError]
+ -[WebBookmark(ReadingList) setFeatureTextFetchError:]
+ -[WebBookmarkTabCollection _resolveLastSelectedChildOfTabGroup:toInsertedTabWithUUID:]
+ -[WebBookmarkTabCollection _saveTabGroup:childTabs:selectedTabUUID:]
+ -[WebBookmarkTabCollection _saveWindowState:localTabs:localSelectedTabUUID:privateTabs:privateSelectedTabUUID:]
+ -[WebBookmarkTabCollection _saveWindowState:localTabs:localSelectedTabUUID:privateTabs:privateSelectedTabUUID:forApplyingInMemoryChanges:]
+ -[WebBookmarkTabCollection indexableProfiles]
+ -[WebBookmarkTabCollection saveWindowState:localTabs:localSelectedTabUUID:privateTabs:privateSelectedTabUUID:]
+ -[_WBIndexableProfile .cxx_destruct]
+ -[_WBIndexableProfile displayTitle]
+ -[_WBIndexableProfile identifier]
+ -[_WBIndexableProfile initWithIdentifier:displayTitle:]
+ GCC_except_table135
+ _OBJC_CLASS_$__WBIndexableProfile
+ _OBJC_IVAR_$_WebBookmark._featureTextFetchError
+ _OBJC_IVAR_$__WBIndexableProfile._displayTitle
+ _OBJC_IVAR_$__WBIndexableProfile._identifier
+ _OBJC_METACLASS_$__WBIndexableProfile
+ __OBJC_$_INSTANCE_METHODS__WBIndexableProfile
+ __OBJC_$_INSTANCE_VARIABLES__WBIndexableProfile
+ __OBJC_$_PROP_LIST_WBSIndexableProfile
+ __OBJC_$_PROP_LIST__WBIndexableProfile
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_WBSIndexableProfile
+ __OBJC_$_PROTOCOL_METHOD_TYPES_WBSIndexableProfile
+ __OBJC_CLASS_PROTOCOLS_$__WBIndexableProfile
+ __OBJC_CLASS_RO_$__WBIndexableProfile
+ __OBJC_LABEL_PROTOCOL_$_WBSIndexableProfile
+ __OBJC_METACLASS_RO_$__WBIndexableProfile
+ __OBJC_PROTOCOL_$_WBSIndexableProfile
+ ___111-[WebBookmarkTabCollection _saveWindowState:localTabs:localSelectedTabUUID:privateTabs:privateSelectedTabUUID:]_block_invoke
+ ___138-[WebBookmarkTabCollection _saveWindowState:localTabs:localSelectedTabUUID:privateTabs:privateSelectedTabUUID:forApplyingInMemoryChanges:]_block_invoke
+ ___68-[WebBookmarkTabCollection _saveTabGroup:childTabs:selectedTabUUID:]_block_invoke
+ ___block_descriptor_80_ea8_32s40s48s56s64s72s_e5_B8?0ls32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_descriptor_88_ea8_32s40s48s56s64s72s80r_e5_v8?0lr80l8s32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_descriptor_96_ea8_32s40s48s56s64s72s80bs88r_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8r88l8s80l8
+ _objc_msgSend$_resolveLastSelectedChildOfTabGroup:toInsertedTabWithUUID:
+ _objc_msgSend$_saveAndMoveBookmarks:toFolderID:
+ _objc_msgSend$_saveTabGroup:childTabs:selectedTabUUID:
+ _objc_msgSend$_saveWindowState:localTabs:localSelectedTabUUID:privateTabs:privateSelectedTabUUID:
+ _objc_msgSend$_saveWindowState:localTabs:localSelectedTabUUID:privateTabs:privateSelectedTabUUID:forApplyingInMemoryChanges:
+ _objc_msgSend$initWithIdentifier:displayTitle:
+ _objc_msgSend$profileTitleWithTitle:forProfileIdentifier:
+ _objc_msgSend$saveWindowState:localTabs:localSelectedTabUUID:privateTabs:privateSelectedTabUUID:
+ _sqlite3_changes
- -[WebBookmarkTabCollection _saveWindowState:forApplyingInMemoryChanges:]
- -[WebBookmarkTabCollection saveWindowState:]
- GCC_except_table136
- OBJC_IVAR_$_WBProfile._titleProvider
- ___35-[WBProfile initWithBookmark:kind:]_block_invoke
- ___45-[WebBookmarkTabCollection _saveWindowState:]_block_invoke
- ___72-[WebBookmarkTabCollection _saveWindowState:forApplyingInMemoryChanges:]_block_invoke
- ___block_descriptor_32_e15_"NSString"8?0l
- _objc_msgSend$_saveWindowState:forApplyingInMemoryChanges:
CStrings:
+ "Failed to persist %{public}lu tab(s) for tab group %{public}@"
+ "Failed to save localTabGroup %{public}@ for windowState: %{public}@"
+ "Failed to save privateTabGroup %{public}@ for windowState: %{public}@"
+ "Failed to save tab group %{public}@"
+ "Failed to update last selected tab for tab group %{public}@"
+ "SELECT external_uuid, title FROM bookmarks WHERE parent = 0 AND syncable = 1 AND type = 1 AND subtype = 2 AND special_id = 0 ORDER BY order_index ASC"
+ "Tried to update bookmark %{public}@ marked inserted (id=%d) but no row matched — row is missing from the database"
- "Failed to save local tab group %{public}@ while trying to save window state with UUID: %{public}@"
- "Failed to save private tab group %{public}@ while trying to save window state with UUID: %{public}@"

```
