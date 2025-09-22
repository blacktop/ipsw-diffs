## SearchUI

> `/System/Library/PrivateFrameworks/SearchUI.framework/SearchUI`

```diff

-634.0.0.0.0
-  __TEXT.__text: 0xecb88
-  __TEXT.__auth_stubs: 0x2d40
-  __TEXT.__objc_methlist: 0x12098
+634.1.4.0.0
+  __TEXT.__text: 0xed39c
+  __TEXT.__auth_stubs: 0x2d50
+  __TEXT.__objc_methlist: 0x12078
   __TEXT.__const: 0x2f04
   __TEXT.__gcc_except_tab: 0xa1c
-  __TEXT.__cstring: 0x45b7
+  __TEXT.__cstring: 0x4607
   __TEXT.__oslogstring: 0x25e8
   __TEXT.__ustring: 0x9c
   __TEXT.__dlopen_cstrs: 0x160

   __TEXT.__swift_as_entry: 0x120
   __TEXT.__swift_as_ret: 0x108
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x46f0
+  __TEXT.__unwind_info: 0x4720
   __TEXT.__eh_frame: 0x1ef0
-  __TEXT.__objc_classname: 0x30e3
-  __TEXT.__objc_methname: 0x2a2e4
-  __TEXT.__objc_methtype: 0x76ed
-  __TEXT.__objc_stubs: 0x20440
+  __TEXT.__objc_classname: 0x30c7
+  __TEXT.__objc_methname: 0x2a318
+  __TEXT.__objc_methtype: 0x7722
+  __TEXT.__objc_stubs: 0x204e0
   __DATA_CONST.__got: 0x2470
   __DATA_CONST.__const: 0x27c0
   __DATA_CONST.__objc_classlist: 0xab8
   __DATA_CONST.__objc_catlist: 0x400
-  __DATA_CONST.__objc_protolist: 0x368
+  __DATA_CONST.__objc_protolist: 0x360
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9eb0
+  __DATA_CONST.__objc_selrefs: 0x9eb8
   __DATA_CONST.__objc_protorefs: 0x68
   __DATA_CONST.__objc_superrefs: 0x6e8
   __DATA_CONST.__objc_arraydata: 0x38
-  __AUTH_CONST.__auth_got: 0x16b0
-  __AUTH_CONST.__const: 0x2728
-  __AUTH_CONST.__cfstring: 0x3100
-  __AUTH_CONST.__objc_const: 0x1dc40
+  __AUTH_CONST.__auth_got: 0x16b8
+  __AUTH_CONST.__const: 0x2748
+  __AUTH_CONST.__cfstring: 0x3140
+  __AUTH_CONST.__objc_const: 0x1dc18
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0x40f8
   __AUTH.__data: 0x7a0
-  __DATA.__objc_ivar: 0xca0
-  __DATA.__data: 0x3228
-  __DATA.__bss: 0x1ac0
+  __DATA.__objc_ivar: 0xca4
+  __DATA.__data: 0x31c8
+  __DATA.__bss: 0x1ad0
   __DATA.__common: 0xd8
   __DATA_DIRTY.__objc_data: 0x36f0
   __DATA_DIRTY.__data: 0x4d0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: D70F551C-62B9-3690-8C55-BDFF9932C906
-  Functions: 6763
-  Symbols:   21012
-  CStrings:  9102
+  UUID: 14521C92-C308-3AE5-A2FE-DD5086A9A67A
+  Functions: 6775
+  Symbols:   21042
+  CStrings:  9110
 
Symbols:
+ -[SearchUICollectionViewController collectionView:didHighlightItemAtIndexPath:]
+ -[SearchUICollectionViewController collectionView:didUnhighlightItemAtIndexPath:]
+ -[SearchUICollectionViewController focusedIndexPath]
+ -[SearchUICollectionViewController setAdjacentSeparatorVisibility:indexPath:]
+ -[SearchUICollectionViewController setFocusedIndexPath:]
+ -[SearchUICommandHandler supportsDrag]
+ -[SearchUIHomeScreenAppIconViewContextMenuController shouldActivateApplicationShortcutItem:atIndex:forIconView:]
+ -[SearchUIPerformIntentHandler supportsDrag]
+ -[SearchUIPhotosImage imageQueue]
+ -[SearchUIPhotosImage imageQueue].cold.1
+ -[SearchUIRowModel hasGridStyling]
+ -[SearchUIRunShortcutHandler supportsDrag]
+ GCC_except_table100
+ _OBJC_IVAR_$_SearchUICollectionViewController._focusedIndexPath
+ _SearchUIAppIconHighlightFrameInset
+ _UIRoundToScale
+ ___33-[SearchUIPhotosImage imageQueue]_block_invoke
+ ___block_descriptor_65_e8_32s40s48s56r_e84_"UIListSeparatorConfiguration"24?0"NSIndexPath"8"UIListSeparatorConfiguration"16ls32l8s40l8s48l8r56l8
+ ___block_descriptor_89_e8_32s40bs_e17_v16?0"PHAsset"8ls32l8s40l8
+ _imageQueue.onceToken
+ _imageQueue.queue
+ _objc_msgSend$focusedIndexPath
+ _objc_msgSend$imageQueue
+ _objc_msgSend$sectionBottomSeparatorKind
+ _objc_msgSend$setAdjacentSeparatorVisibility:indexPath:
+ _objc_msgSend$shouldActivateApplicationShortcutItem:atIndex:forIconView:
+ _objc_msgSend$supportsDrag
- -[SearchUIHomeScreenAppIconView shouldActivateApplicationShortcutItem:atIndex:]
- GCC_except_table97
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_SBIconViewShortcutsDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_SBIconViewShortcutsDelegate
- __OBJC_$_PROTOCOL_REFS_SBIconViewShortcutsDelegate
- __OBJC_LABEL_PROTOCOL_$_SBIconViewShortcutsDelegate
- __OBJC_PROTOCOL_$_SBIconViewShortcutsDelegate
- ___block_descriptor_66_e8_32s40s48s56r_e84_"UIListSeparatorConfiguration"24?0"NSIndexPath"8"UIListSeparatorConfiguration"16ls32l8s40l8s48l8r56l8
- ___block_descriptor_89_e8_32s40bs_e17_v16?0"PHAsset"8ls40l8s32l8
- _objc_msgSend$shouldActivateApplicationShortcutItem:atIndex:
CStrings:
+ "@\"NSArray\"32@0:8@\"SBHIconViewContextMenuManager\"16@\"SBIconView\"24"
+ "@\"UIViewController\"24@0:8@\"SBIconView\"16"
+ "B40@0:8@16Q24@32"
+ "T@\"NSIndexPath\",&,N,V_focusedIndexPath"
+ "_focusedIndexPath"
+ "com.apple.email.SearchIndexer"
+ "com.apple.searchui.SearchUIPhotosImage"
+ "contextMenuManager:orderedActionContextMenuProvidersForIconView:"
+ "contextMenuManager:preferredMenuElementOrderForIconView:"
+ "focusedIndexPath"
+ "hasGridStyling"
+ "imageQueue"
+ "kCSItemBundle"
+ "parentViewControllerForCustomIconImageViewControllerForIconView:"
+ "q32@0:8@\"SBHIconViewContextMenuManager\"16@\"SBIconView\"24"
+ "setAdjacentSeparatorVisibility:indexPath:"
+ "setFocusedIndexPath:"
+ "shouldActivateApplicationShortcutItem:atIndex:forIconView:"
+ "supportsDrag"
- "@\"<SBIconViewShortcutsDelegate>\"24@0:8@\"SBIconView\"16"
- "@\"SBHRecentsDocumentExtensionProvider\"24@0:8@\"SBIconView\"16"
- "B32@0:8@16Q24"
- "SBIconViewShortcutsDelegate"
- "applicationBundleURLForShortcutsWithIconView:"
- "iconViewShortcutsPresentationDidCancel:"
- "iconViewShortcutsPresentationDidFinish:"
- "iconViewShortcutsPresentationWillBegin:"
- "iconViewShortcutsPresentationWillFinish:"
- "iconViewShouldBeginShortcutsPresentation:"
- "recentDocumentExtensionProviderForIconView:"
- "shortcutsDelegateForIconView:"
- "shouldActivateApplicationShortcutItem:atIndex:"

```
