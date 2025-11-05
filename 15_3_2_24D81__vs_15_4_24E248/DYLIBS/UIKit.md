## UIKit

> `/System/iOSSupport/System/Library/AccessibilityBundles/UIKit.axbundle/Contents/MacOS/UIKit`

```diff

-2963.3.13.1.0
-  __TEXT.__text: 0x184dd8
-  __TEXT.__auth_stubs: 0x13d0
-  __TEXT.__objc_methlist: 0xea84
-  __TEXT.__const: 0x108
-  __TEXT.__cstring: 0x18645
+2963.10.10.0.0
+  __TEXT.__text: 0x18d97c
+  __TEXT.__auth_stubs: 0x13c0
+  __TEXT.__objc_methlist: 0xf614
+  __TEXT.__cstring: 0x1886b
   __TEXT.__oslogstring: 0x2218
-  __TEXT.__gcc_except_tab: 0x3520
+  __TEXT.__gcc_except_tab: 0x35ac
   __TEXT.__dlopen_cstrs: 0x19c
   __TEXT.__ustring: 0x78
-  __TEXT.__unwind_info: 0x2ca0
+  __TEXT.__const: 0x18
+  __TEXT.__unwind_info: 0x2c60
   __TEXT.__objc_classname: 0x8e00
-  __TEXT.__objc_methname: 0x15ae9
-  __TEXT.__objc_methtype: 0x213c
-  __TEXT.__objc_stubs: 0x100e0
-  __DATA_CONST.__got: 0xfa0
-  __DATA_CONST.__const: 0x1e50
+  __TEXT.__objc_methname: 0x15cb4
+  __TEXT.__objc_methtype: 0x21ac
+  __TEXT.__objc_stubs: 0x10240
+  __DATA_CONST.__got: 0xfb8
+  __DATA_CONST.__const: 0x1ea8
   __DATA_CONST.__objc_classlist: 0x1ae8
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5660
+  __DATA_CONST.__objc_selrefs: 0x5b80
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0xa38
+  __DATA_CONST.__objc_superrefs: 0xa40
   __DATA_CONST.__objc_arraydata: 0x180
-  __AUTH_CONST.__auth_got: 0x9f8
-  __AUTH_CONST.__const: 0x15a0
-  __AUTH_CONST.__cfstring: 0x1d340
-  __AUTH_CONST.__objc_const: 0x212d0
+  __AUTH_CONST.__auth_got: 0x9f0
+  __AUTH_CONST.__const: 0x1600
+  __AUTH_CONST.__cfstring: 0x1d600
+  __AUTH_CONST.__objc_const: 0x1fe98
   __AUTH_CONST.__objc_intobj: 0x1e0
   __AUTH_CONST.__objc_dictobj: 0x140
   __AUTH_CONST.__objc_arrayobj: 0x48

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7003FF04-36B0-3949-BF06-5577D2A93D41
-  Functions: 5773
-  Symbols:   13921
-  CStrings:  12045
+  UUID: D042B197-3155-3776-B17D-76B68B6BD1D6
+  Functions: 5784
+  Symbols:   13974
+  CStrings:  12111
 
Symbols:
+ +[UILayoutContainerViewAccessibility _accessibilityPerformValidations:]
+ -[UICollectionViewListCellAccessibility _accessibilityHandleReorderMoveDown]
+ -[UICollectionViewListCellAccessibility _accessibilityHandleReorderMoveUp:]
+ -[UICollectionViewListCellAccessibility _accessibilityHandleReorderMoveUp]
+ -[UICollectionViewListCellAccessibility _accessibilityHasReorderActions]
+ -[UICollectionViewListCellAccessibility _accessibilityNextIndexPath]
+ -[UICollectionViewListCellAccessibility _accessibilityParentCollectionView]
+ -[UICollectionViewListCellAccessibility _accessibilityPreviousIndexPath]
+ -[UIIndexBarAccessoryViewAccessibility _axDidSelectEntry:]
+ -[UIIndexBarAccessoryViewAccessibility _axDidSelectEntry]
+ -[UIIndexBarAccessoryViewAccessibility _axMoveToFirstVisibleIndex:]
+ -[UIIndexBarAccessoryViewAccessibility accessibilityElementDidBecomeFocused]
+ -[UINavigationControllerAccessibility _axHandleTransitionEndFromView:toView:]
+ -[UINavigationControllerAccessibility transitionConductor:didEndCustomTransitionWithContext:didComplete:]
+ -[_UIContextMenuUIControllerAccessibility contextMenuView:didSelectElement:]
+ -[_UIKeyboardStateManagerAccessibility performKeyboardOutput:userInfo:]
+ -[_UITabContainerViewAccessibility accessibilityViewIsModal]
+ -[_UITabContainerViewAccessibility updateEditModeAppearanceAnimated:]
+ -[_UITabOutlineViewAccessibility _accessibilitySortPriority]
+ -[_UITabOutlineViewAccessibility willMoveToSuperview:]
+ -[_UITabSidebarCellAccessibility accessibilityDragSourceDescriptors]
+ GCC_except_table23
+ _AXLabelAndValueForElements
+ _UIKBTIKeyboardOutputShouldForwardToRemoteInputSource
+ __45-[UITextViewAccessibility automationElements]_block_invoke.617
+ __72-[UIScrollViewAccessibility _accessibilityLastOpaqueElementWithOptions:]_block_invoke.419
+ __72-[UIScrollViewAccessibility _accessibilityLastOpaqueElementWithOptions:]_block_invoke_2.420
+ __73-[UIScrollViewAccessibility _accessibilityFirstOpaqueElementWithOptions:]_block_invoke.407
+ __73-[UIScrollViewAccessibility _accessibilityFirstOpaqueElementWithOptions:]_block_invoke_2.408
+ __75-[UICollectionViewListCellAccessibility _accessibilityHandleReorderMoveUp:]_block_invoke.506
+ __80-[UITextInputUIResponderAccessibility _accessibilityInsertTextWithAlternatives:]_block_invoke.649
+ ___54-[_UITabOutlineViewAccessibility willMoveToSuperview:]_block_invoke
+ ___63-[_UIFloatingTabBarItemViewAccessibility accessibilityRowRange]_block_invoke_2
+ ___65-[UICollectionViewListCellAccessibility _accessibilityBriefLabel]_block_invoke
+ ___68-[_UITabSidebarCellAccessibility accessibilityDragSourceDescriptors]_block_invoke
+ ___69-[_UITabContainerViewAccessibility updateEditModeAppearanceAnimated:]_block_invoke
+ ___71-[UINavigationBarAccessibility _accessibilityFetchCachedNavBarElements]_block_invoke_4
+ ___71-[_UIKeyboardStateManagerAccessibility performKeyboardOutput:userInfo:]_block_invoke
+ ___72-[UICollectionViewListCellAccessibility _accessibilityHasReorderActions]_block_invoke
+ ___75-[UICollectionViewListCellAccessibility _accessibilityHandleReorderMoveUp:]_block_invoke
+ ___75-[UICollectionViewListCellAccessibility _accessibilityHandleReorderMoveUp:]_block_invoke_2
+ ___75-[UICollectionViewListCellAccessibility _privateAccessibilityCustomActions]_block_invoke_9
+ ___UIIndexBarAccessoryViewAccessibility___axDidSelectEntry
+ ___block_descriptor_40_e8_32bs_e8_v16?0Q8ls32l8
+ ___block_descriptor_80_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_88_e8_32s40r_e5_v8?0lr40l8s32l8
+ __block_literal_global.1015
+ __block_literal_global.1024
+ __block_literal_global.1061
+ __block_literal_global.406
+ __block_literal_global.410
+ __block_literal_global.414
+ __block_literal_global.418
+ __block_literal_global.422
+ __block_literal_global.439
+ __block_literal_global.462
+ __block_literal_global.511
+ __block_literal_global.518
+ __block_literal_global.522
+ __block_literal_global.947
+ __block_literal_global.953
+ __block_literal_global.968
+ __block_literal_global.973
+ __block_literal_global.988
+ __block_literal_global.993
+ _objc_msgSend$_abbreviatedBackButtonTitles
+ _objc_msgSend$_axDidSelectEntry
+ _objc_msgSend$_axDidSelectEntry:
+ _objc_msgSend$_axHandleTransitionEndFromView:toView:
+ _objc_msgSend$_axMoveToFirstVisibleIndex:
+ _objc_msgSend$_canReorderItemAtIndexPath:
+ _objc_msgSend$_fromView
+ _objc_msgSend$_indexInDataSourceForItemAtIndexPath:
+ _objc_msgSend$_toView
+ _objc_msgSend$beginInteractiveMovementForItemAtIndexPath:
+ _objc_msgSend$endInteractiveMovement
+ _objc_msgSend$updateInteractiveMovementTargetPosition:
- -[_UIKeyboardStateManagerAccessibility performKeyboardOutput:checkingDelegate:forwardToRemoteInputSource:]
- GCC_except_table19
- __45-[UITextViewAccessibility automationElements]_block_invoke.614
- __72-[UIScrollViewAccessibility _accessibilityLastOpaqueElementWithOptions:]_block_invoke.416
- __72-[UIScrollViewAccessibility _accessibilityLastOpaqueElementWithOptions:]_block_invoke_2.417
- __73-[UIScrollViewAccessibility _accessibilityFirstOpaqueElementWithOptions:]_block_invoke.404
- __73-[UIScrollViewAccessibility _accessibilityFirstOpaqueElementWithOptions:]_block_invoke_2.405
- __80-[UITextInputUIResponderAccessibility _accessibilityInsertTextWithAlternatives:]_block_invoke.641
- ___106-[_UIKeyboardStateManagerAccessibility performKeyboardOutput:checkingDelegate:forwardToRemoteInputSource:]_block_invoke
- ___78-[_UIContextMenuViewAccessibility displayMenu:updateType:alongsideAnimations:]_block_invoke_2
- ___block_descriptor_48_e8_32bs40w_e8_v16?0Q8ls32l8w40l8
- __block_literal_global.1013
- __block_literal_global.1022
- __block_literal_global.1059
- __block_literal_global.403
- __block_literal_global.407
- __block_literal_global.409
- __block_literal_global.415
- __block_literal_global.419
- __block_literal_global.456
- __block_literal_global.508
- __block_literal_global.515
- __block_literal_global.517
- __block_literal_global.693
- __block_literal_global.945
- __block_literal_global.951
- __block_literal_global.966
- __block_literal_global.969
- __block_literal_global.986
- __block_literal_global.991
- _objc_msgSend$preferredPlacement
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AccessibilityBundles_Alias2/UIKitAccessibility/CollectionViews/UICollectionViewAccessibility.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AccessibilityBundles_Alias2/UIKitAccessibility/CollectionViews/UICollectionViewCellAccessibility.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AccessibilityBundles_Alias2/UIKitAccessibility/Keyboards/UIKeyboardLayoutStarAccessibility.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AccessibilityBundles_Alias2/UIKitAccessibility/Pickers/UIAccessibilityPickerComponent.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AccessibilityBundles_Alias2/UIKitAccessibility/RemoteViews/_UIRemoteViewAccessibility.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AccessibilityBundles_Alias2/UIKitAccessibility/StatusBar/UIStatusBarDataNetworkItemViewAccessibility.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AccessibilityBundles_Alias2/UIKitAccessibility/Tables/UICollectionViewTableCellAccessibility.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AccessibilityBundles_Alias2/UIKitAccessibility/Tables/UITableViewAccessibility.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AccessibilityBundles_Alias2/UIKitAccessibility/Tables/UITableViewCellAccessibility.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AccessibilityBundles_Alias2/UIKitAccessibility/Text/UITextAccessibilityUtilities.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AccessibilityBundles_Alias2/UIKitAccessibility/Text/UITextInputUIResponderAccessibility.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AccessibilityBundles_Alias2/UIKitAccessibility/UIApplicationAccessibility.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AccessibilityBundles_Alias2/UIKitAccessibility/UIIndexBarAccessoryViewAccessibility.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AccessibilityBundles_Alias2/UIKitAccessibility/UIInputSwitcherSegmentControlAccessibility.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AccessibilityBundles_Alias2/UIKitAccessibility/UISplitViewControllerClassicImplAccessibility.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AccessibilityBundles_Alias2/UIKitAccessibility/UIWindowAccessibility.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AccessibilityBundles_Alias2/UIKitAccessibility/_UIRemoteDictionaryViewControllerAccessibility.m"
+ "@\"UIConversationContext\"16@0:8"
+ "NSDiffableDataSourceSnapshot"
+ "T@\"UIConversationContext\",?,&,N"
+ "UIMenuElement"
+ "UITextLinkInteraction"
+ "_UIContextMenuPresentation"
+ "_UIFloatingTabBarCustomizationProxy"
+ "_UIFloatingTabBarPinnedItemsView"
+ "_UINavigationPalette"
+ "_UITableViewHeaderFooterViewLabel"
+ "_abbreviatedBackButtonTitles"
+ "_axDidSelectEntry"
+ "_axDidSelectEntry:"
+ "_axHandleTransitionEndFromView:toView:"
+ "_axMoveToFirstVisibleIndex:"
+ "_canReorderItemAtIndexPath:"
+ "_detailLabel"
+ "_detailText"
+ "_focusTargetOffset"
+ "_fromView"
+ "_indexInDataSourceForItemAtIndexPath:"
+ "_isLeaf"
+ "_isShowingSidebar"
+ "_toView"
+ "contextMenuView:didSelectElement:"
+ "conversationContext"
+ "delegate.delegate"
+ "insertInputSuggestion:"
+ "performKeyboardOutput:userInfo:"
+ "setConversationContext:"
+ "shouldForwardToRemoteInputSource"
+ "space"
+ "transitionConductor:didEndCustomTransitionWithContext:didComplete:"
+ "updateEditModeAppearanceAnimated:"
+ "updateInteractiveMovementTargetPosition:"
+ "v24@0:8@\"UIConversationContext\"16"
+ "v24@0:8@\"UIInputSuggestion\"16"
+ "v36@0:8@16@24B32"
+ "willMoveToSuperview:"
- "/AppleInternal/Library/BuildRoots/423aabcf-bd7b-11ef-ae7d-aabfac210453/Library/Caches/com.apple.xbs/Sources/AccessibilityBundles_Alias2/UIKitAccessibility/CollectionViews/UICollectionViewAccessibility.m"
- "/AppleInternal/Library/BuildRoots/423aabcf-bd7b-11ef-ae7d-aabfac210453/Library/Caches/com.apple.xbs/Sources/AccessibilityBundles_Alias2/UIKitAccessibility/CollectionViews/UICollectionViewCellAccessibility.m"
- "/AppleInternal/Library/BuildRoots/423aabcf-bd7b-11ef-ae7d-aabfac210453/Library/Caches/com.apple.xbs/Sources/AccessibilityBundles_Alias2/UIKitAccessibility/Keyboards/UIKeyboardLayoutStarAccessibility.m"
- "/AppleInternal/Library/BuildRoots/423aabcf-bd7b-11ef-ae7d-aabfac210453/Library/Caches/com.apple.xbs/Sources/AccessibilityBundles_Alias2/UIKitAccessibility/Pickers/UIAccessibilityPickerComponent.m"
- "/AppleInternal/Library/BuildRoots/423aabcf-bd7b-11ef-ae7d-aabfac210453/Library/Caches/com.apple.xbs/Sources/AccessibilityBundles_Alias2/UIKitAccessibility/RemoteViews/_UIRemoteViewAccessibility.m"
- "/AppleInternal/Library/BuildRoots/423aabcf-bd7b-11ef-ae7d-aabfac210453/Library/Caches/com.apple.xbs/Sources/AccessibilityBundles_Alias2/UIKitAccessibility/StatusBar/UIStatusBarDataNetworkItemViewAccessibility.m"
- "/AppleInternal/Library/BuildRoots/423aabcf-bd7b-11ef-ae7d-aabfac210453/Library/Caches/com.apple.xbs/Sources/AccessibilityBundles_Alias2/UIKitAccessibility/Tables/UICollectionViewTableCellAccessibility.m"
- "/AppleInternal/Library/BuildRoots/423aabcf-bd7b-11ef-ae7d-aabfac210453/Library/Caches/com.apple.xbs/Sources/AccessibilityBundles_Alias2/UIKitAccessibility/Tables/UITableViewAccessibility.m"
- "/AppleInternal/Library/BuildRoots/423aabcf-bd7b-11ef-ae7d-aabfac210453/Library/Caches/com.apple.xbs/Sources/AccessibilityBundles_Alias2/UIKitAccessibility/Tables/UITableViewCellAccessibility.m"
- "/AppleInternal/Library/BuildRoots/423aabcf-bd7b-11ef-ae7d-aabfac210453/Library/Caches/com.apple.xbs/Sources/AccessibilityBundles_Alias2/UIKitAccessibility/Text/UITextAccessibilityUtilities.m"
- "/AppleInternal/Library/BuildRoots/423aabcf-bd7b-11ef-ae7d-aabfac210453/Library/Caches/com.apple.xbs/Sources/AccessibilityBundles_Alias2/UIKitAccessibility/Text/UITextInputUIResponderAccessibility.m"
- "/AppleInternal/Library/BuildRoots/423aabcf-bd7b-11ef-ae7d-aabfac210453/Library/Caches/com.apple.xbs/Sources/AccessibilityBundles_Alias2/UIKitAccessibility/UIApplicationAccessibility.m"
- "/AppleInternal/Library/BuildRoots/423aabcf-bd7b-11ef-ae7d-aabfac210453/Library/Caches/com.apple.xbs/Sources/AccessibilityBundles_Alias2/UIKitAccessibility/UIIndexBarAccessoryViewAccessibility.m"
- "/AppleInternal/Library/BuildRoots/423aabcf-bd7b-11ef-ae7d-aabfac210453/Library/Caches/com.apple.xbs/Sources/AccessibilityBundles_Alias2/UIKitAccessibility/UIInputSwitcherSegmentControlAccessibility.m"
- "/AppleInternal/Library/BuildRoots/423aabcf-bd7b-11ef-ae7d-aabfac210453/Library/Caches/com.apple.xbs/Sources/AccessibilityBundles_Alias2/UIKitAccessibility/UISplitViewControllerClassicImplAccessibility.m"
- "/AppleInternal/Library/BuildRoots/423aabcf-bd7b-11ef-ae7d-aabfac210453/Library/Caches/com.apple.xbs/Sources/AccessibilityBundles_Alias2/UIKitAccessibility/UIWindowAccessibility.m"
- "/AppleInternal/Library/BuildRoots/423aabcf-bd7b-11ef-ae7d-aabfac210453/Library/Caches/com.apple.xbs/Sources/AccessibilityBundles_Alias2/UIKitAccessibility/_UIRemoteDictionaryViewControllerAccessibility.m"
- "performKeyboardOutput:checkingDelegate:forwardToRemoteInputSource:"
- "preferredPlacement"

```
