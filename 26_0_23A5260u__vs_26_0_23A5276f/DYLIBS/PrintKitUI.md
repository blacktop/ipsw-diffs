## PrintKitUI

> `/System/Library/PrivateFrameworks/PrintKitUI.framework/PrintKitUI`

```diff

-71.0.0.0.0
-  __TEXT.__text: 0x5dedc
+74.0.0.0.0
+  __TEXT.__text: 0x5ed50
   __TEXT.__auth_stubs: 0xf10
-  __TEXT.__objc_methlist: 0x6d6c
-  __TEXT.__const: 0x310
-  __TEXT.__cstring: 0x2655
+  __TEXT.__objc_methlist: 0x6e24
+  __TEXT.__const: 0x320
+  __TEXT.__cstring: 0x269b
   __TEXT.__ustring: 0x182
-  __TEXT.__gcc_except_tab: 0x12d4
+  __TEXT.__gcc_except_tab: 0x1398
   __TEXT.__dlopen_cstrs: 0x95
-  __TEXT.__unwind_info: 0x14f0
-  __TEXT.__objc_classname: 0xc21
-  __TEXT.__objc_methname: 0x13a5d
-  __TEXT.__objc_methtype: 0x3a4f
-  __TEXT.__objc_stubs: 0xe440
+  __TEXT.__unwind_info: 0x1540
+  __TEXT.__objc_classname: 0xc1f
+  __TEXT.__objc_methname: 0x13bee
+  __TEXT.__objc_methtype: 0x3a6b
+  __TEXT.__objc_stubs: 0xe5e0
   __DATA_CONST.__got: 0x8f0
-  __DATA_CONST.__const: 0xec0
+  __DATA_CONST.__const: 0xf08
   __DATA_CONST.__objc_classlist: 0x298
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x46d0
+  __DATA_CONST.__objc_selrefs: 0x4738
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x238
   __DATA_CONST.__objc_arraydata: 0x88
   __AUTH_CONST.__auth_got: 0x798
-  __AUTH_CONST.__const: 0x160
-  __AUTH_CONST.__cfstring: 0x3480
-  __AUTH_CONST.__objc_const: 0xa558
+  __AUTH_CONST.__const: 0x1a0
+  __AUTH_CONST.__cfstring: 0x34a0
+  __AUTH_CONST.__objc_const: 0xa5d8
   __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0x2d0
-  __DATA.__objc_ivar: 0x7b8
+  __DATA.__objc_ivar: 0x7c4
   __DATA.__data: 0xcc8
   __DATA.__bss: 0x98
   __DATA_DIRTY.__objc_data: 0x1720

   - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8C154D25-B97B-3AF5-847A-81BE667A788D
-  Functions: 2179
-  Symbols:   8143
-  CStrings:  4589
+  UUID: 10215A5A-C50A-3BF3-A10A-A999CC721221
+  Functions: 2200
+  Symbols:   8208
+  CStrings:  4612
 
Symbols:
+ -[UIPrintAppOptionsSection previewDidChangeSize:]
+ -[UIPrintOptionCell previewDidChangeSize:]
+ -[UIPrintOptionListCell previewDidChangeSize:]
+ -[UIPrintOptionPopupCell _updateConstraints]
+ -[UIPrintOptionPopupCell constraints]
+ -[UIPrintOptionPopupCell setConstraints:]
+ -[UIPrintOptionPopupCell textLabel]
+ -[UIPrintOptionPopupCell usingLargeTextLayout]
+ -[UIPrintOptionSection dealloc]
+ -[UIPrintOptionSection previewDidChangeSize:]
+ -[UIPrintOptionViewCell previewDidChangeSize:]
+ -[UIPrintPanelViewController contentInsetForPreviewWithHeight:]
+ -[UIPrintPanelViewController controlTintColor]
+ -[UIPrintPanelViewController preferredContentSizeCategoryChanged]
+ -[UIPrintPanelViewController previewSidebarNavigationController]
+ -[UIPrintPanelViewController setPreviewSidebarNavigationController:]
+ -[UIPrintPanelViewController splitViewController:didHideColumn:]
+ -[UIPrintPanelViewController splitViewController:didShowColumn:]
+ -[UIPrintPreviewPageCell invalidateThumbnailImage]
+ -[UIPrintPreviewPageCell invalidated]
+ -[UIPrintPreviewPageCell setInvalidated:]
+ -[UIPrintPreviewPageCell setThumbnailSize:]
+ -[UIPrintPreviewPageCell thumbnailSize]
+ -[UIPrintPreviewPageCell updatePageLabelAndImageViewWithIndex:pageCount:allowSelection:thumbnailSize:]
+ -[UIPrintPreviewViewController collectionView:contextMenuConfigurationForItemsAtIndexPaths:point:]
+ -[UIPrintPreviewViewController collectionViewContainerTopConstraint]
+ -[UIPrintPreviewViewController previewDocumentInteractionControllerRefCount]
+ -[UIPrintPreviewViewController scrollToBeginning]
+ -[UIPrintPreviewViewController scrollToEnd]
+ -[UIPrintPreviewViewController setCollectionViewContainerTopConstraint:]
+ -[UIPrintPreviewViewController setPreviewDocumentInteractionControllerRefCount:]
+ -[UIPrintPreviewViewController showingPreviewDocumentInteractionController]
+ GCC_except_table44
+ GCC_except_table51
+ GCC_except_table68
+ GCC_except_table76
+ GCC_except_table88
+ _OBJC_IVAR_$_UIPrintOptionPopupCell._constraints
+ _OBJC_IVAR_$_UIPrintOptionPopupCell._textLabel
+ _OBJC_IVAR_$_UIPrintPanelViewController._previewSidebarNavigationController
+ _OBJC_IVAR_$_UIPrintPreviewPageCell._invalidated
+ _OBJC_IVAR_$_UIPrintPreviewPageCell._thumbnailSize
+ _OBJC_IVAR_$_UIPrintPreviewViewController._collectionViewContainerTopConstraint
+ _OBJC_IVAR_$_UIPrintPreviewViewController._previewDocumentInteractionControllerRefCount
+ _UIContentSizeCategoryIsAccessibilityCategory
+ ___53-[UIPrinterBrowserViewController startPrinterBrowser]_block_invoke_3
+ ___56-[UIPrintOptionPopupCell initWithStyle:reuseIdentifier:]_block_invoke
+ ___56-[UIPrintOptionPopupCell initWithStyle:reuseIdentifier:]_block_invoke_2
+ ___79-[UIPrintPreviewViewController fetchThumnailImageInBackground:previewPageCell:]_block_invoke_3
+ ___79-[UIPrintPreviewViewController fetchThumnailImageInBackground:previewPageCell:]_block_invoke_4
+ ___98-[UIPrintPanelViewController initWithPrintInterationController:inParentController:usingSplitView:]_block_invoke_2
+ ___98-[UIPrintPreviewViewController collectionView:contextMenuConfigurationForItemsAtIndexPaths:point:]_block_invoke
+ ___98-[UIPrintPreviewViewController collectionView:contextMenuConfigurationForItemsAtIndexPaths:point:]_block_invoke_2
+ ___block_descriptor_32_e18_v16?0"UIAction"8l
+ ___block_descriptor_40_e8_32w_e52_v24?0"<UITraitEnvironment>"8"UITraitCollection"16lw32l8
+ ___block_descriptor_64_e8_32s40s48w_e5_v8?0lw48l8s32l8s40l8
+ ___block_descriptor_72_e8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
+ _objc_msgSend$_updateConstraints
+ _objc_msgSend$collectionViewContainerTopConstraint
+ _objc_msgSend$contentInsetForPreviewWithHeight:
+ _objc_msgSend$controlTintColor
+ _objc_msgSend$invalidateThumbnailImage
+ _objc_msgSend$invalidated
+ _objc_msgSend$isShowingColumn:
+ _objc_msgSend$performBatchUpdates:completion:
+ _objc_msgSend$preferredContentSizeCategoryChanged
+ _objc_msgSend$previewDocumentInteractionControllerRefCount
+ _objc_msgSend$previewSidebarNavigationController
+ _objc_msgSend$registerForTraitChanges:withHandler:
+ _objc_msgSend$safeAreaInsets
+ _objc_msgSend$setAdditionalSafeAreaInsets:
+ _objc_msgSend$setCollectionViewContainerTopConstraint:
+ _objc_msgSend$setConstraints:
+ _objc_msgSend$setInvalidated:
+ _objc_msgSend$setPreviewDocumentInteractionControllerRefCount:
+ _objc_msgSend$setPreviewSidebarNavigationController:
+ _objc_msgSend$setThumbnailSize:
+ _objc_msgSend$showThumbnailProgressSpinner
+ _objc_msgSend$showingPreviewDocumentInteractionController
+ _objc_msgSend$thumbnailSize
+ _objc_msgSend$updatePageLabelAndImageViewWithIndex:pageCount:allowSelection:thumbnailSize:
+ _objc_msgSend$usingLargeTextLayout
- -[UIPrintOptionCell previewDidChangeSize]
- -[UIPrintOptionListCell previewDidChangeSize]
- -[UIPrintOptionPopupCell prepareForReuse]
- -[UIPrintPanelViewController contentInsetForPreview]
- -[UIPrintPanelViewController setSplitViewDisplayMode:]
- -[UIPrintPanelViewController splitViewController:willChangeToDisplayMode:]
- -[UIPrintPanelViewController splitViewDisplayMode]
- -[UIPrintPreviewPageCell addPageLabelAndImageView:]
- -[UIPrintPreviewViewController collectionView:contextMenuConfigurationForItemAtIndexPath:point:]
- -[UIPrintPreviewViewController collectionViewTopConstraint]
- -[UIPrintPreviewViewController presentingDocumentInteractionController]
- -[UIPrintPreviewViewController setCollectionViewTopConstraint:]
- -[UIPrintPreviewViewController setPresentingDocumentInteractionController:]
- -[UIPrintPreviewViewController setTraitPreferredContentSizeChangeRegistration:]
- -[UIPrintPreviewViewController traitCollectionDidChange:previousTraitCollection:]
- -[UIPrintPreviewViewController traitPreferredContentSizeChangeRegistration]
- -[UIPrintPreviewViewController viewWillTransitionToSize:withTransitionCoordinator:]
- GCC_except_table38
- GCC_except_table43
- GCC_except_table47
- GCC_except_table79
- GCC_except_table92
- _OBJC_IVAR_$_UIPrintPanelViewController._splitViewDisplayMode
- _OBJC_IVAR_$_UIPrintPreviewViewController._collectionViewTopConstraint
- _OBJC_IVAR_$_UIPrintPreviewViewController._presentingDocumentInteractionController
- _OBJC_IVAR_$_UIPrintPreviewViewController._traitPreferredContentSizeChangeRegistration
- ___96-[UIPrintPreviewViewController collectionView:contextMenuConfigurationForItemAtIndexPath:point:]_block_invoke
- ___96-[UIPrintPreviewViewController collectionView:contextMenuConfigurationForItemAtIndexPath:point:]_block_invoke_2
- ___block_descriptor_56_e8_32s40w_e5_v8?0lw40l8s32l8
- ___block_descriptor_64_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
- _objc_msgSend$addPageLabelAndImageView:
- _objc_msgSend$collectionViewTopConstraint
- _objc_msgSend$contentInsetForPreview
- _objc_msgSend$presentingDocumentInteractionController
- _objc_msgSend$registerForTraitChanges:withAction:
- _objc_msgSend$setCollectionViewTopConstraint:
- _objc_msgSend$setPresentingDocumentInteractionController:
- _objc_msgSend$setSplitViewDisplayMode:
- _objc_msgSend$setTraitPreferredContentSizeChangeRegistration:
- _objc_msgSend$splitViewDisplayMode
- _objc_msgSend$traitPreferredContentSizeChangeRegistration
- _objc_msgSend$unregisterForTraitChanges:
- _objc_opt_self
CStrings:
+ "!)"
+ "T@\"NSArray\",&,N,V_constraints"
+ "T@\"NSLayoutConstraint\",&,V_collectionViewContainerTopConstraint"
+ "T@\"UINavigationController\",&,N,V_previewSidebarNavigationController"
+ "TB,N,V_invalidated"
+ "Tq,V_pageIndex"
+ "Tq,V_previewDocumentInteractionControllerRefCount"
+ "T{CGSize=dd},V_thumbnailSize"
+ "_collectionViewContainerTopConstraint"
+ "_constraints"
+ "_invalidated"
+ "_previewDocumentInteractionControllerRefCount"
+ "_previewSidebarNavigationController"
+ "_textLabel"
+ "_thumbnailSize"
+ "_updateConstraints"
+ "collectionViewContainerTopConstraint"
+ "com.apple.iBooks"
+ "contentInsetForPreviewWithHeight:"
+ "controlTintColor"
+ "invalidateThumbnailImage"
+ "invalidated"
+ "isShowingColumn:"
+ "performBatchUpdates:completion:"
+ "preferredContentSizeCategoryChanged"
+ "previewDocumentInteractionControllerRefCount"
+ "previewSidebarNavigationController"
+ "safeAreaInsets"
+ "scrollToBeginning"
+ "scrollToEnd"
+ "setAdditionalSafeAreaInsets:"
+ "setCollectionViewContainerTopConstraint:"
+ "setConstraints:"
+ "setInvalidated:"
+ "setPreviewDocumentInteractionControllerRefCount:"
+ "setPreviewSidebarNavigationController:"
+ "setThumbnailSize:"
+ "showingPreviewDocumentInteractionController"
+ "thumbnailSize"
+ "updatePageLabelAndImageViewWithIndex:pageCount:allowSelection:thumbnailSize:"
+ "usingLargeTextLayout"
+ "v24@?0@\"<UITraitEnvironment>\"8@\"UITraitCollection\"16"
+ "v52@0:8q16q24B32{CGSize=dd}36"
+ "{UIEdgeInsets=dddd}24@0:8d16"
- "@\"<UITraitChangeRegistration>\""
- "T@\"<UITraitChangeRegistration>\",&,V_traitPreferredContentSizeChangeRegistration"
- "T@\"NSLayoutConstraint\",&,V_collectionViewTopConstraint"
- "TB,V_presentingDocumentInteractionController"
- "Tq,N,V_pageIndex"
- "Tq,N,V_splitViewDisplayMode"
- "_collectionViewTopConstraint"
- "_presentingDocumentInteractionController"
- "_splitViewDisplayMode"
- "_traitPreferredContentSizeChangeRegistration"
- "addPageLabelAndImageView:"
- "collectionViewTopConstraint"
- "contentInsetForPreview"
- "presentingDocumentInteractionController"
- "previewDidChangeSize"
- "setCollectionViewTopConstraint:"
- "setPresentingDocumentInteractionController:"
- "setSplitViewDisplayMode:"
- "setTraitPreferredContentSizeChangeRegistration:"
- "splitViewDisplayMode"
- "traitCollectionDidChange:previousTraitCollection:"
- "traitPreferredContentSizeChangeRegistration"

```
