## ShareSheet

> `/System/Library/PrivateFrameworks/ShareSheet.framework/ShareSheet`

```diff

-2084.10.7.2.5
-  __TEXT.__text: 0xc2138
-  __TEXT.__auth_stubs: 0xec0
-  __TEXT.__objc_methlist: 0x10e1c
+2086.10.3.2.2
+  __TEXT.__text: 0xc41cc
+  __TEXT.__auth_stubs: 0xef0
+  __TEXT.__objc_methlist: 0x110e4
   __TEXT.__const: 0x620
-  __TEXT.__gcc_except_tab: 0x2280
-  __TEXT.__oslogstring: 0x690d
-  __TEXT.__cstring: 0x6b4a
-  __TEXT.__dlopen_cstrs: 0x9ba
+  __TEXT.__gcc_except_tab: 0x22a8
+  __TEXT.__oslogstring: 0x69ef
+  __TEXT.__cstring: 0x6b7e
+  __TEXT.__dlopen_cstrs: 0xa0a
   __TEXT.__ustring: 0xca
-  __TEXT.__unwind_info: 0x3218
-  __TEXT.__objc_classname: 0x240f
-  __TEXT.__objc_methname: 0x2cbc2
-  __TEXT.__objc_methtype: 0x740b
-  __TEXT.__objc_stubs: 0x1bea0
-  __DATA_CONST.__got: 0xf98
-  __DATA_CONST.__const: 0x2700
-  __DATA_CONST.__objc_classlist: 0x620
+  __TEXT.__unwind_info: 0x3270
+  __TEXT.__objc_classname: 0x249c
+  __TEXT.__objc_methname: 0x2d41c
+  __TEXT.__objc_methtype: 0x762b
+  __TEXT.__objc_stubs: 0x1c260
+  __DATA_CONST.__got: 0xfb8
+  __DATA_CONST.__const: 0x2740
+  __DATA_CONST.__objc_classlist: 0x638
   __DATA_CONST.__objc_catlist: 0x18
-  __DATA_CONST.__objc_protolist: 0x3a0
+  __DATA_CONST.__objc_protolist: 0x3a8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8958
+  __DATA_CONST.__objc_selrefs: 0x8ab0
   __DATA_CONST.__objc_protorefs: 0x58
-  __DATA_CONST.__objc_superrefs: 0x3f0
+  __DATA_CONST.__objc_superrefs: 0x400
   __DATA_CONST.__objc_arraydata: 0x678
-  __AUTH_CONST.__auth_got: 0x770
-  __AUTH_CONST.__const: 0x1060
-  __AUTH_CONST.__cfstring: 0x5720
-  __AUTH_CONST.__objc_const: 0x29a38
+  __AUTH_CONST.__auth_got: 0x788
+  __AUTH_CONST.__const: 0x10a0
+  __AUTH_CONST.__cfstring: 0x5740
+  __AUTH_CONST.__objc_const: 0x2a218
   __AUTH_CONST.__objc_arrayobj: 0x510
   __AUTH_CONST.__objc_dictobj: 0x730
   __AUTH_CONST.__objc_intobj: 0x78
-  __AUTH.__objc_data: 0x2210
+  __AUTH.__objc_data: 0x2300
   __AUTH.__data: 0x128
-  __DATA.__objc_ivar: 0x1474
-  __DATA.__data: 0x2b88
-  __DATA.__bss: 0x7c8
+  __DATA.__objc_ivar: 0x14a0
+  __DATA.__data: 0x2be8
+  __DATA.__bss: 0x7e8
   __DATA_DIRTY.__objc_data: 0x1b30
   __DATA_DIRTY.__data: 0x68
   __DATA_DIRTY.__bss: 0x278

   - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 74F45909-AC55-35CC-9C01-52316A12C097
-  Functions: 5746
-  Symbols:   20535
-  CStrings:  9535
+  UUID: 752FF7A8-0F35-3B1C-8F2E-C4913F825B2C
+  Functions: 5796
+  Symbols:   20723
+  CStrings:  9618
 
Symbols:
+ +[SHSheetFactory createCustomRemoteViewControllerWithSession:]
+ +[SHSheetFactory createNavigationControllerWithRootViewController:delegate:accessibilityIdentifier:]
+ -[SHSheetContentLayoutSection .cxx_destruct]
+ -[SHSheetContentLayoutSection cellSideInset]
+ -[SHSheetContentLayoutSection initWithLayoutSection:]
+ -[SHSheetContentLayoutSection layoutSection]
+ -[SHSheetContentLayoutSection setCellSideInset:]
+ -[SHSheetContentLayoutSpec peopleSectionTopInset]
+ -[SHSheetPresenter handleRemoteCustomDismissal]
+ -[SHSheetPresenter handleRemoteCustomPresentation]
+ -[SHSheetPresenter presentationControllerDidDismiss:]
+ -[SHSheetRemoteCustomSceneSpecification uiSceneSessionRole]
+ -[SHSheetRemoteCustomViewController .cxx_destruct]
+ -[SHSheetRemoteCustomViewController clientIsReady]
+ -[SHSheetRemoteCustomViewController didInstallHostingView]
+ -[SHSheetRemoteCustomViewController hostingController]
+ -[SHSheetRemoteCustomViewController initWithSessionIdentifier:]
+ -[SHSheetRemoteCustomViewController installSceneHostingView]
+ -[SHSheetRemoteCustomViewController sessionIdentifier]
+ -[SHSheetRemoteCustomViewController setDidInstallHostingView:]
+ -[SHSheetRemoteScene presentationDirectionType]
+ -[SHSheetRouter _createUserDefaultsNavigationControllerWithRootViewController:]
+ -[SHSheetRouter dismissRemoteCustomViewControllerIfNeeded]
+ -[SHSheetRouter presentRemoteCustomViewController:]
+ -[SHSheetRouter remoteCustomViewController]
+ -[SHSheetRouter setRemoteCustomViewController:]
+ -[UIActivityActionGroupCell _preferredSeparatorInsetsForProposedInsets:]
+ -[UIActivityContentViewController _updateHeaderContentInsets]
+ -[UIActivityContentViewController cachedHorizontalLayoutSection]
+ -[UIActivityContentViewController hostPresentationDirectionType]
+ -[UIActivityContentViewController isAtScrollBoundary]
+ -[UIActivityContentViewController isPresentedFromBottom]
+ -[UIActivityContentViewController presentationDirectionType]
+ -[UIActivityContentViewController setCachedHorizontalLayoutSection:]
+ -[UIActivityContentViewController setHostPresentationDirectionType:]
+ -[UIActivityContentViewController setIsAtScrollBoundary:]
+ -[_UIActivityUserDefaultsViewController _provideCellForTableView:indexPath:itemIdentifier:]
+ -[_UIActivityViewControllerPresentationController .cxx_destruct]
+ -[_UIActivityViewControllerPresentationController _updatePresentationDirection]
+ -[_UIActivityViewControllerPresentationController _update]
+ -[_UIActivityViewControllerPresentationController popoverBackgroundColor]
+ -[_UIActivityViewControllerPresentationController presentationDirectionType]
+ -[_UIActivityViewControllerPresentationController setPopoverBackgroundColor:]
+ -[_UIActivityViewControllerPresentationController setPresentationDirectionType:]
+ -[_UIActivityViewControllerPresentationController setSourceItem:]
+ -[_UIActivityViewControllerPresentationController setSourceView:]
+ -[_UIActivityViewControllerPresentationController updateWithCompactSize:applyImmediately:]
+ GCC_except_table111
+ GCC_except_table121
+ GCC_except_table124
+ GCC_except_table125
+ GCC_except_table176
+ _OBJC_CLASS_$_SHSheetContentLayoutSection
+ _OBJC_CLASS_$_SHSheetRemoteCustomSceneSpecification
+ _OBJC_CLASS_$_SHSheetRemoteCustomViewController
+ _OBJC_IVAR_$_SHSheetContentLayoutSection._cellSideInset
+ _OBJC_IVAR_$_SHSheetContentLayoutSection._layoutSection
+ _OBJC_IVAR_$_SHSheetContentLayoutSpec._peopleSectionTopInset
+ _OBJC_IVAR_$_SHSheetRemoteCustomViewController._didInstallHostingView
+ _OBJC_IVAR_$_SHSheetRemoteCustomViewController._hostingController
+ _OBJC_IVAR_$_SHSheetRemoteCustomViewController._sessionIdentifier
+ _OBJC_IVAR_$_SHSheetRouter._remoteCustomViewController
+ _OBJC_IVAR_$_UIActivityContentViewController._cachedHorizontalLayoutSection
+ _OBJC_IVAR_$_UIActivityContentViewController._hostPresentationDirectionType
+ _OBJC_IVAR_$_UIActivityContentViewController._isAtScrollBoundary
+ _OBJC_IVAR_$__UIActivityViewControllerPresentationController._popoverBackgroundColor
+ _OBJC_IVAR_$__UIActivityViewControllerPresentationController._presentationDirectionType
+ _OBJC_METACLASS_$_SHSheetContentLayoutSection
+ _OBJC_METACLASS_$_SHSheetRemoteCustomSceneSpecification
+ _OBJC_METACLASS_$_SHSheetRemoteCustomViewController
+ _SHLPLinkView_intrinsicContentSize
+ _UISceneSessionRoleCustom
+ _UIViewNoIntrinsicMetric
+ __OBJC_$_INSTANCE_METHODS_SHSheetContentLayoutSection
+ __OBJC_$_INSTANCE_METHODS_SHSheetRemoteCustomSceneSpecification
+ __OBJC_$_INSTANCE_METHODS_SHSheetRemoteCustomViewController
+ __OBJC_$_INSTANCE_VARIABLES_SHSheetContentLayoutSection
+ __OBJC_$_INSTANCE_VARIABLES_SHSheetRemoteCustomViewController
+ __OBJC_$_PROP_LIST_SHSheetContentLayoutSection
+ __OBJC_$_PROP_LIST_SHSheetPresenter.645
+ __OBJC_$_PROP_LIST_SHSheetRemoteCustomViewController
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_UIAdaptivePresentationControllerDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT__UIActivityUserDefaultsViewControllerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_UIAdaptivePresentationControllerDelegate
+ __OBJC_$_PROTOCOL_REFS_UIAdaptivePresentationControllerDelegate
+ __OBJC_CLASS_PROTOCOLS_$_SHSheetRemoteCustomViewController
+ __OBJC_CLASS_RO_$_SHSheetContentLayoutSection
+ __OBJC_CLASS_RO_$_SHSheetRemoteCustomSceneSpecification
+ __OBJC_CLASS_RO_$_SHSheetRemoteCustomViewController
+ __OBJC_LABEL_PROTOCOL_$_UIAdaptivePresentationControllerDelegate
+ __OBJC_METACLASS_RO_$_SHSheetContentLayoutSection
+ __OBJC_METACLASS_RO_$_SHSheetRemoteCustomSceneSpecification
+ __OBJC_METACLASS_RO_$_SHSheetRemoteCustomViewController
+ __OBJC_PROTOCOL_$_UIAdaptivePresentationControllerDelegate
+ ___60-[SHSheetRemoteCustomViewController installSceneHostingView]_block_invoke
+ ___77-[SHSheetRouter activityPerformer:preparePresentationWithContext:completion:]_block_invoke.148
+ ___77-[SHSheetRouter activityPerformer:preparePresentationWithContext:completion:]_block_invoke.149
+ ___91-[_UIActivityUserDefaultsViewController _provideCellForTableView:indexPath:itemIdentifier:]_block_invoke
+ ___91-[_UIActivityUserDefaultsViewController _provideCellForTableView:indexPath:itemIdentifier:]_block_invoke_2
+ ___91-[_UIActivityUserDefaultsViewController _provideCellForTableView:indexPath:itemIdentifier:]_block_invoke_3
+ ___94-[SHSheetRouter dismissForActivityPerformerResult:didPresentFromShareSheet:completionHandler:]_block_invoke.143
+ ___allocSHLPLinkViewInstance_block_invoke
+ ___block_descriptor_32_e8_B12?0B8l
+ ___block_descriptor_40_e8_32w_e65_"UITableViewCell"32?0"UITableView"8"NSIndexPath"16"NSUUID"24lw32l8
+ ___block_literal_global.1021
+ ___block_literal_global.1028
+ ___block_literal_global.1032
+ ___block_literal_global.1038
+ ___block_literal_global.361
+ _allocSHLPLinkViewInstance
+ _allocSHLPLinkViewInstance.cold.1
+ _allocSHLPLinkViewInstance.onceToken
+ _allocSHLPLinkViewInstance.theClass
+ _class_addMethod
+ _objc_allocateClassPair
+ _objc_msgSend$_createUserDefaultsNavigationControllerWithRootViewController:
+ _objc_msgSend$_provideCellForTableView:indexPath:itemIdentifier:
+ _objc_msgSend$_update
+ _objc_msgSend$_updateHeaderContentInsets
+ _objc_msgSend$_updatePresentationDirection
+ _objc_msgSend$cachedHorizontalLayoutSection
+ _objc_msgSend$cellSideInset
+ _objc_msgSend$createCustomRemoteViewControllerWithSession:
+ _objc_msgSend$createNavigationControllerWithRootViewController:delegate:accessibilityIdentifier:
+ _objc_msgSend$dismissRemoteCustomViewControllerIfNeeded
+ _objc_msgSend$frameInView:
+ _objc_msgSend$handleRemoteCustomDismissal
+ _objc_msgSend$handleRemoteCustomPresentation
+ _objc_msgSend$hostPresentationDirectionType
+ _objc_msgSend$initWithLayoutSection:
+ _objc_msgSend$isAtScrollBoundary
+ _objc_msgSend$isPresentedFromBottom
+ _objc_msgSend$layoutSection
+ _objc_msgSend$peopleSectionTopInset
+ _objc_msgSend$popoverBackgroundColor
+ _objc_msgSend$presentRemoteCustomViewController:
+ _objc_msgSend$presentationDirectionType
+ _objc_msgSend$remoteCustomViewController
+ _objc_msgSend$setBackgroundEffects:
+ _objc_msgSend$setCachedHorizontalLayoutSection:
+ _objc_msgSend$setCellSideInset:
+ _objc_msgSend$setIsAtScrollBoundary:
+ _objc_msgSend$setPopoverBackgroundColor:
+ _objc_msgSend$setPresentationDirectionType:
+ _objc_msgSend$setRemoteCustomViewController:
+ _objc_msgSend$setSourceItem:
+ _objc_msgSend$systemBackgroundColor
+ _objc_msgSend$updateHostingController:sessionIdentifier:
+ _objc_msgSend$updateHostingController:withContext:hostProcessType:hostPresentationStyle:optionGroups:collaborationOptionsData:cloudShareRequest:isSLMEnabled:presentationDirectionType:
+ _objc_msgSend$updateWithCompactSize:applyImmediately:
+ _objc_msgSend$userDefaultsViewControllerDidRequestDismissal:
+ _objc_registerClassPair
- -[UIActivityActionGroupCell needsLeftIconLayout]
- -[UIActivityContentViewController isDraggingFromInitialPosition]
- -[UIActivityContentViewController setIsDraggingFromInitialPosition:]
- -[_UIActivityViewControllerPresentationController updateWithCompactSize:]
- GCC_except_table106
- GCC_except_table116
- GCC_except_table119
- GCC_except_table122
- GCC_except_table173
- _OBJC_IVAR_$_UIActivityContentViewController._isDraggingFromInitialPosition
- __OBJC_$_PROP_LIST_SHSheetPresenter.621
- ___52-[_UIActivityUserDefaultsViewController viewDidLoad]_block_invoke_2
- ___52-[_UIActivityUserDefaultsViewController viewDidLoad]_block_invoke_3
- ___52-[_UIActivityUserDefaultsViewController viewDidLoad]_block_invoke_4
- ___77-[SHSheetRouter activityPerformer:preparePresentationWithContext:completion:]_block_invoke.146
- ___77-[SHSheetRouter activityPerformer:preparePresentationWithContext:completion:]_block_invoke.147
- ___94-[SHSheetRouter dismissForActivityPerformerResult:didPresentFromShareSheet:completionHandler:]_block_invoke.141
- ___block_descriptor_56_e8_32s40s48w_e65_"UITableViewCell"32?0"UITableView"8"NSIndexPath"16"NSUUID"24lw48l8s32l8s40l8
- ___block_literal_global.1002
- ___block_literal_global.1007
- ___block_literal_global.1011
- ___block_literal_global.360
- _objc_msgSend$isDraggingFromInitialPosition
- _objc_msgSend$linkViewHeaderInsets
- _objc_msgSend$needsLeftIconLayout
- _objc_msgSend$setIsDraggingFromInitialPosition:
- _objc_msgSend$updateHostingController:withContext:hostProcessType:hostPresentationStyle:optionGroups:collaborationOptionsData:cloudShareRequest:isSLMEnabled:
- _objc_msgSend$updateWithCompactSize:
CStrings:
+ "%@: setHostPresentationDirectionType:%@"
+ "@\"NSCollectionLayoutSection\""
+ "@\"SHSheetContentLayoutSection\""
+ "@\"SHSheetRemoteCustomViewController\""
+ "@\"UIViewController\"32@0:8@\"UIPresentationController\"16q24"
+ "B24@0:8@\"UIPresentationController\"16"
+ "SHLPLinkView"
+ "SHSheetContentLayoutSection"
+ "SHSheetRemoteCustomSceneSpecification"
+ "SHSheetRemoteCustomViewController"
+ "T@\"NSCollectionLayoutSection\",R,N,V_layoutSection"
+ "T@\"NSNumber\",&,N,V_hostPresentationDirectionType"
+ "T@\"SHSheetContentLayoutSection\",&,N,V_cachedHorizontalLayoutSection"
+ "T@\"SHSheetRemoteCustomViewController\",&,N,V_remoteCustomViewController"
+ "T@\"UIColor\",&,N,V_popoverBackgroundColor"
+ "T@\"_UISceneHostingController\",R,N,V_hostingController"
+ "TB,N,V_isAtScrollBoundary"
+ "Td,N,V_cellSideInset"
+ "Td,R,N,V_peopleSectionTopInset"
+ "Tq,N,V_presentationDirectionType"
+ "UIAdaptivePresentationControllerDelegate"
+ "UISceneSessionRoleCustom"
+ "_cachedHorizontalLayoutSection"
+ "_cellSideInset"
+ "_createUserDefaultsNavigationControllerWithRootViewController:"
+ "_hostPresentationDirectionType"
+ "_isAtScrollBoundary"
+ "_layoutSection"
+ "_peopleSectionTopInset"
+ "_popoverBackgroundColor"
+ "_preferredSeparatorInsetsForProposedInsets:"
+ "_presentationDirectionType"
+ "_provideCellForTableView:indexPath:itemIdentifier:"
+ "_remoteCustomViewController"
+ "_update"
+ "_updateHeaderContentInsets"
+ "_updatePresentationDirection"
+ "adaptivePresentationStyleForPresentationController:"
+ "adaptivePresentationStyleForPresentationController:traitCollection:"
+ "cachedHorizontalLayoutSection"
+ "cellSideInset"
+ "createCustomRemoteViewControllerWithSession:"
+ "createNavigationControllerWithRootViewController:delegate:accessibilityIdentifier:"
+ "dismissRemoteCustomViewControllerIfNeeded"
+ "frameInView:"
+ "handleRemoteCustomDismissal"
+ "handleRemoteCustomPresentation"
+ "handleResizeGesture - isPresentedFromBottom:%@"
+ "hostPresentationDirectionType"
+ "initWithLayoutSection:"
+ "intrinsicContentSize"
+ "isAtScrollBoundary"
+ "isPresentedFromBottom"
+ "layoutSection"
+ "peopleSectionTopInset"
+ "popoverBackgroundColor"
+ "presentRemoteCustomViewController:"
+ "presentationController:prepareAdaptivePresentationController:"
+ "presentationController:viewControllerForAdaptivePresentationStyle:"
+ "presentationController:willPresentWithAdaptiveStyle:transitionCoordinator:"
+ "presentationControllerDidAttemptToDismiss:"
+ "presentationControllerDidDismiss:"
+ "presentationControllerShouldDismiss:"
+ "presentationControllerWillDismiss:"
+ "presentationDirectionType"
+ "q24@0:8@\"UIPresentationController\"16"
+ "q32@0:8@\"UIPresentationController\"16@\"UITraitCollection\"24"
+ "remoteCustomViewController"
+ "scrollViewWillBeginDragging - isPresentedFromBottom:%@"
+ "setBackgroundEffects:"
+ "setCachedHorizontalLayoutSection:"
+ "setCellSideInset:"
+ "setHostPresentationDirectionType:"
+ "setIsAtScrollBoundary:"
+ "setPopoverBackgroundColor:"
+ "setPresentationDirectionType:"
+ "setRemoteCustomViewController:"
+ "setSourceItem:"
+ "skipping anchor source:%@ noOverlap:%@ bothOverlap:%@ for presentationController:%@"
+ "systemBackgroundColor"
+ "updateHostingController:sessionIdentifier:"
+ "updateHostingController:withContext:hostProcessType:hostPresentationStyle:optionGroups:collaborationOptionsData:cloudShareRequest:isSLMEnabled:presentationDirectionType:"
+ "updateWithCompactSize:applyImmediately:"
+ "userDefaultsViewControllerDidRequestDismissal:"
+ "v24@0:8@\"UIPresentationController\"16"
+ "v32@0:8@\"UIPresentationController\"16@\"UIPresentationController\"24"
+ "v40@0:8@\"UIPresentationController\"16q24@\"<UIViewControllerTransitionCoordinator>\"32"
+ "{CGSize=ff}@:"
+ "{NSDirectionalEdgeInsets=dddd}48@0:8{NSDirectionalEdgeInsets=dddd}16"
- "TB,N,V_isDraggingFromInitialPosition"
- "_isDraggingFromInitialPosition"
- "isDraggingFromInitialPosition"
- "needsLeftIconLayout"
- "setIsDraggingFromInitialPosition:"
- "updateHostingController:withContext:hostProcessType:hostPresentationStyle:optionGroups:collaborationOptionsData:cloudShareRequest:isSLMEnabled:"
- "updateWithCompactSize:"

```
