## UIKit

> `/System/Library/AccessibilityBundles/UIKit.axbundle/UIKit`

```diff

-3001.4.0.0.0
-  __TEXT.__text: 0x1954e8
-  __TEXT.__auth_stubs: 0x1500
-  __TEXT.__objc_methlist: 0xf88c
+3003.1.0.0.0
+  __TEXT.__text: 0x197474
+  __TEXT.__auth_stubs: 0x1510
+  __TEXT.__objc_methlist: 0xf8ac
   __TEXT.__const: 0xa0
-  __TEXT.__cstring: 0x18d0f
-  __TEXT.__oslogstring: 0x22ac
-  __TEXT.__gcc_except_tab: 0x3604
+  __TEXT.__cstring: 0x18e91
+  __TEXT.__oslogstring: 0x2311
+  __TEXT.__gcc_except_tab: 0x36ac
   __TEXT.__dlopen_cstrs: 0xb8
   __TEXT.__ustring: 0x78
-  __TEXT.__unwind_info: 0x2d00
+  __TEXT.__unwind_info: 0x2d30
   __TEXT.__objc_classname: 0x90ad
-  __TEXT.__objc_methname: 0x15f3d
-  __TEXT.__objc_methtype: 0x2159
-  __TEXT.__objc_stubs: 0x106e0
-  __DATA_CONST.__got: 0xf80
-  __DATA_CONST.__const: 0x1e78
+  __TEXT.__objc_methname: 0x15fc5
+  __TEXT.__objc_methtype: 0x214d
+  __TEXT.__objc_stubs: 0x10740
+  __DATA_CONST.__got: 0xfa0
+  __DATA_CONST.__const: 0x1ea8
   __DATA_CONST.__objc_classlist: 0x1b48
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5ba0
+  __DATA_CONST.__objc_selrefs: 0x5bb8
   __DATA_CONST.__objc_protorefs: 0x40
-  __DATA_CONST.__objc_superrefs: 0xa80
+  __DATA_CONST.__objc_superrefs: 0xa88
   __DATA_CONST.__objc_arraydata: 0x190
-  __AUTH_CONST.__auth_got: 0xa90
+  __AUTH_CONST.__auth_got: 0xa98
   __AUTH_CONST.__const: 0x17a0
-  __AUTH_CONST.__cfstring: 0x1dc60
+  __AUTH_CONST.__cfstring: 0x1de40
   __AUTH_CONST.__objc_const: 0x20440
   __AUTH_CONST.__objc_intobj: 0x1f8
   __AUTH_CONST.__objc_dictobj: 0x140

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 851DB077-1122-3F6C-84B9-F4120F4271EE
-  Functions: 5874
-  Symbols:   20040
-  CStrings:  12207
+  UUID: D3F8C6C1-E2F7-358B-A6FE-2A3AF74E3535
+  Functions: 5884
+  Symbols:   20072
+  CStrings:  12246
 
Symbols:
+ -[UINavigationBarAccessibility _accessibilityHasSubtitleViewChanged]
+ -[UINavigationBarAccessibility _axSubtitleLabel]
+ -[UISearchTextFieldAccessibility _delegateShouldChangeCharactersInTextStorageRanges:replacementString:delegateCares:]
+ -[UIWindowSceneAccessibility accessibilityFrame]
+ -[_UIFloatingTabBarItemCellAccessibility _accessibilityRetainsFocusOnScreenChange]
+ -[_UISplitViewControllerAdaptiveImplAccessibility _accessibilityLoadAccessibilityInformation]
+ GCC_except_table148
+ GCC_except_table151
+ GCC_except_table156
+ GCC_except_table219
+ _NSStringFromCGSize
+ _OBJC_CLASS_$_FBSceneLayer
+ _OBJC_CLASS_$_UIImageSymbolConfiguration
+ _OBJC_CLASS_$_UIScene
+ _OBJC_CLASS_$__UINavigationBarVisualProvider
+ __AXUIKit_UIKeyboardCurrentInputModeIsMultiscript
+ ___103-[UIApplicationAccessibility _accessibilityElementFirst:last:forFocus:allowScrolling:traversalOptions:]_block_invoke.862
+ ___103-[UIApplicationAccessibility _accessibilityElementFirst:last:forFocus:allowScrolling:traversalOptions:]_block_invoke.863
+ ___103-[UIApplicationAccessibility _accessibilityElementFirst:last:forFocus:allowScrolling:traversalOptions:]_block_invoke.864
+ ___103-[_UIRemoteViewControllerLegacyImplAccessibility _accessibilityLoadAccessibilityInformation:retryTime:]_block_invoke.416
+ ___45-[UITextViewAccessibility automationElements]_block_invoke.643
+ ___48-[UIWindowSceneAccessibility accessibilityFrame]_block_invoke
+ ___60-[UITableViewAccessibility _accessibilityHitTest:withEvent:]_block_invoke.698
+ ___60-[UITableViewAccessibility _accessibilityHitTest:withEvent:]_block_invoke_2.703
+ ___64-[UITableViewCellAccessibility _accessibilityHitTest:withEvent:]_block_invoke.701
+ ___68-[UIAccessibilityPickerComponent _accessibilityDateTimePickerValues]_block_invoke.333
+ ___68-[UIAccessibilityPickerComponent _accessibilityDateTimePickerValues]_block_invoke.346
+ ___69-[UIApplicationAccessibility _iosAccessibilitySetValue:forAttribute:]_block_invoke.974
+ ___69-[UIViewAccessibility _accessibilitySortedElementsWithinWithOptions:]_block_invoke.571
+ ___69-[UIViewAccessibility _accessibilitySortedElementsWithinWithOptions:]_block_invoke_2.572
+ ___72-[UIScrollViewAccessibility _accessibilityLastOpaqueElementWithOptions:]_block_invoke.445
+ ___72-[UIScrollViewAccessibility _accessibilityLastOpaqueElementWithOptions:]_block_invoke_2.446
+ ___73-[UIScrollViewAccessibility _accessibilityFirstOpaqueElementWithOptions:]_block_invoke.433
+ ___73-[UIScrollViewAccessibility _accessibilityFirstOpaqueElementWithOptions:]_block_invoke_2.434
+ ___74-[UITableViewAccessibility _accessibilitySortedElementsWithinWithOptions:]_block_invoke.721
+ ___74-[UITableViewAccessibility _accessibilitySortedElementsWithinWithOptions:]_block_invoke_2.722
+ ___75-[UIApplicationAccessibility _iosAccessibilityAttributeValue:forParameter:]_block_invoke
+ ___75-[UIApplicationAccessibility _iosAccessibilityAttributeValue:forParameter:]_block_invoke_2
+ ___75-[UICollectionViewListCellAccessibility _accessibilityHandleReorderMoveUp:]_block_invoke.515
+ ___76-[UICollectionViewAccessibility accessibilityCreatePrepareCellForIndexPath:]_block_invoke.531
+ ___79-[UICollectionViewAccessibility _accessibilitySortedElementsWithinWithOptions:]_block_invoke.602
+ ___79-[UICollectionViewAccessibility _accessibilitySortedElementsWithinWithOptions:]_block_invoke_2.603
+ ___80-[UITextInputUIResponderAccessibility _accessibilityInsertTextWithAlternatives:]_block_invoke.683
+ ___82-[_UIRemoteDictionaryViewControllerAccessibility tableView:cellForRowAtIndexPath:]_block_invoke.360
+ ___88-[UIKeyboardEmojiCollectionViewAccessibility _accessibilityLocalizedVisibleSectionNames]_block_invoke.372
+ ___89-[UITableViewAccessibility _axFirstLastOpaqueHeaderElementFromSection:options:direction:]_block_invoke.575
+ ___92-[UITableViewAccessibility _axOffScreenOpaqueHeaderElementInDirection:options:childElement:]_block_invoke.586
+ ___93-[_UISplitViewControllerAdaptiveImplAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke
+ ___98-[UIKeyboardEmojiAndStickerCollectionViewAccessibility _accessibilityLocalizedVisibleSectionNames]_block_invoke.369
+ ___block_descriptor_42_e8_32s_e12_v24?08^B16ls32l8
+ ___block_literal_global.1018
+ ___block_literal_global.1036
+ ___block_literal_global.1038
+ ___block_literal_global.1058
+ ___block_literal_global.1080
+ ___block_literal_global.1089
+ ___block_literal_global.1125
+ ___block_literal_global.1886
+ ___block_literal_global.2533
+ ___block_literal_global.288
+ ___block_literal_global.292
+ ___block_literal_global.297
+ ___block_literal_global.298
+ ___block_literal_global.302
+ ___block_literal_global.3111
+ ___block_literal_global.3113
+ ___block_literal_global.3118
+ ___block_literal_global.3130
+ ___block_literal_global.3132
+ ___block_literal_global.3156
+ ___block_literal_global.316
+ ___block_literal_global.3164
+ ___block_literal_global.318
+ ___block_literal_global.332
+ ___block_literal_global.340
+ ___block_literal_global.342
+ ___block_literal_global.346
+ ___block_literal_global.350
+ ___block_literal_global.370
+ ___block_literal_global.372
+ ___block_literal_global.377
+ ___block_literal_global.379
+ ___block_literal_global.389
+ ___block_literal_global.411
+ ___block_literal_global.427
+ ___block_literal_global.432
+ ___block_literal_global.436
+ ___block_literal_global.440
+ ___block_literal_global.444
+ ___block_literal_global.448
+ ___block_literal_global.456
+ ___block_literal_global.458
+ ___block_literal_global.462
+ ___block_literal_global.463
+ ___block_literal_global.478
+ ___block_literal_global.482
+ ___block_literal_global.486
+ ___block_literal_global.506
+ ___block_literal_global.509
+ ___block_literal_global.522
+ ___block_literal_global.526
+ ___block_literal_global.527
+ ___block_literal_global.538
+ ___block_literal_global.545
+ ___block_literal_global.549
+ ___block_literal_global.566
+ ___block_literal_global.568
+ ___block_literal_global.570
+ ___block_literal_global.574
+ ___block_literal_global.575
+ ___block_literal_global.584
+ ___block_literal_global.585
+ ___block_literal_global.596
+ ___block_literal_global.597
+ ___block_literal_global.601
+ ___block_literal_global.608
+ ___block_literal_global.615
+ ___block_literal_global.619
+ ___block_literal_global.625
+ ___block_literal_global.627
+ ___block_literal_global.637
+ ___block_literal_global.653
+ ___block_literal_global.661
+ ___block_literal_global.663
+ ___block_literal_global.670
+ ___block_literal_global.681
+ ___block_literal_global.685
+ ___block_literal_global.686
+ ___block_literal_global.695
+ ___block_literal_global.707
+ ___block_literal_global.715
+ ___block_literal_global.716
+ ___block_literal_global.720
+ ___block_literal_global.724
+ ___block_literal_global.748
+ ___block_literal_global.761
+ ___block_literal_global.793
+ ___block_literal_global.820
+ ___block_literal_global.852
+ ___block_literal_global.866
+ ___block_literal_global.872
+ ___block_literal_global.966
+ ___block_literal_global.971
+ ___block_literal_global.973
+ ___block_literal_global.976
+ ___block_literal_global.980
+ _kAXRemoteAlertWorkspaceIdentifier
+ _objc_msgSend$_accessibilityScannerElementsGrouped:shouldIncludeNonScannerElements:
+ _objc_msgSend$_axPageSize
+ _objc_msgSend$ax_filteredSetUsingBlock:
+ _objc_msgSend$multilingualLanguages
+ _objc_msgSend$wantsLargeTitleDisplayed
- -[UISearchTextFieldAccessibility _delegateShouldChangeCharactersInTextStorageRange:replacementString:delegateCares:]
- GCC_except_table149
- GCC_except_table154
- GCC_except_table169
- GCC_except_table217
- GCC_except_table42
- ___103-[UIApplicationAccessibility _accessibilityElementFirst:last:forFocus:allowScrolling:traversalOptions:]_block_invoke.859
- ___103-[UIApplicationAccessibility _accessibilityElementFirst:last:forFocus:allowScrolling:traversalOptions:]_block_invoke.860
- ___103-[UIApplicationAccessibility _accessibilityElementFirst:last:forFocus:allowScrolling:traversalOptions:]_block_invoke.861
- ___103-[_UIRemoteViewControllerLegacyImplAccessibility _accessibilityLoadAccessibilityInformation:retryTime:]_block_invoke.413
- ___45-[UITextViewAccessibility automationElements]_block_invoke.640
- ___60-[UITableViewAccessibility _accessibilityHitTest:withEvent:]_block_invoke.695
- ___60-[UITableViewAccessibility _accessibilityHitTest:withEvent:]_block_invoke_2.700
- ___64-[UITableViewCellAccessibility _accessibilityHitTest:withEvent:]_block_invoke.698
- ___68-[UIAccessibilityPickerComponent _accessibilityDateTimePickerValues]_block_invoke.330
- ___68-[UIAccessibilityPickerComponent _accessibilityDateTimePickerValues]_block_invoke.343
- ___69-[UIApplicationAccessibility _iosAccessibilitySetValue:forAttribute:]_block_invoke.968
- ___69-[UIViewAccessibility _accessibilitySortedElementsWithinWithOptions:]_block_invoke.568
- ___69-[UIViewAccessibility _accessibilitySortedElementsWithinWithOptions:]_block_invoke_2.569
- ___72-[UIScrollViewAccessibility _accessibilityLastOpaqueElementWithOptions:]_block_invoke.442
- ___72-[UIScrollViewAccessibility _accessibilityLastOpaqueElementWithOptions:]_block_invoke_2.443
- ___73-[UIScrollViewAccessibility _accessibilityFirstOpaqueElementWithOptions:]_block_invoke.430
- ___73-[UIScrollViewAccessibility _accessibilityFirstOpaqueElementWithOptions:]_block_invoke_2.431
- ___74-[UITableViewAccessibility _accessibilitySortedElementsWithinWithOptions:]_block_invoke.718
- ___74-[UITableViewAccessibility _accessibilitySortedElementsWithinWithOptions:]_block_invoke_2.719
- ___75-[UICollectionViewListCellAccessibility _accessibilityHandleReorderMoveUp:]_block_invoke.512
- ___76-[UICollectionViewAccessibility accessibilityCreatePrepareCellForIndexPath:]_block_invoke.528
- ___79-[UICollectionViewAccessibility _accessibilitySortedElementsWithinWithOptions:]_block_invoke.599
- ___79-[UICollectionViewAccessibility _accessibilitySortedElementsWithinWithOptions:]_block_invoke_2.600
- ___80-[UITextInputUIResponderAccessibility _accessibilityInsertTextWithAlternatives:]_block_invoke.680
- ___82-[_UIRemoteDictionaryViewControllerAccessibility tableView:cellForRowAtIndexPath:]_block_invoke.357
- ___88-[UIKeyboardEmojiCollectionViewAccessibility _accessibilityLocalizedVisibleSectionNames]_block_invoke.369
- ___89-[UITableViewAccessibility _axFirstLastOpaqueHeaderElementFromSection:options:direction:]_block_invoke.572
- ___92-[UITableViewAccessibility _axOffScreenOpaqueHeaderElementInDirection:options:childElement:]_block_invoke.583
- ___98-[UIKeyboardEmojiAndStickerCollectionViewAccessibility _accessibilityLocalizedVisibleSectionNames]_block_invoke.366
- ___block_literal_global.1007
- ___block_literal_global.1028
- ___block_literal_global.1031
- ___block_literal_global.1048
- ___block_literal_global.1075
- ___block_literal_global.1084
- ___block_literal_global.1120
- ___block_literal_global.1874
- ___block_literal_global.2527
- ___block_literal_global.285
- ___block_literal_global.289
- ___block_literal_global.294
- ___block_literal_global.295
- ___block_literal_global.299
- ___block_literal_global.3105
- ___block_literal_global.3107
- ___block_literal_global.3112
- ___block_literal_global.3124
- ___block_literal_global.3126
- ___block_literal_global.313
- ___block_literal_global.315
- ___block_literal_global.3150
- ___block_literal_global.3158
- ___block_literal_global.329
- ___block_literal_global.337
- ___block_literal_global.339
- ___block_literal_global.343
- ___block_literal_global.347
- ___block_literal_global.367
- ___block_literal_global.369
- ___block_literal_global.371
- ___block_literal_global.373
- ___block_literal_global.386
- ___block_literal_global.408
- ___block_literal_global.424
- ___block_literal_global.429
- ___block_literal_global.433
- ___block_literal_global.437
- ___block_literal_global.438
- ___block_literal_global.439
- ___block_literal_global.445
- ___block_literal_global.449
- ___block_literal_global.450
- ___block_literal_global.453
- ___block_literal_global.459
- ___block_literal_global.460
- ___block_literal_global.470
- ___block_literal_global.473
- ___block_literal_global.479
- ___block_literal_global.519
- ___block_literal_global.523
- ___block_literal_global.524
- ___block_literal_global.532
- ___block_literal_global.533
- ___block_literal_global.542
- ___block_literal_global.546
- ___block_literal_global.563
- ___block_literal_global.567
- ___block_literal_global.571
- ___block_literal_global.572
- ___block_literal_global.581
- ___block_literal_global.582
- ___block_literal_global.593
- ___block_literal_global.594
- ___block_literal_global.598
- ___block_literal_global.602
- ___block_literal_global.612
- ___block_literal_global.616
- ___block_literal_global.622
- ___block_literal_global.624
- ___block_literal_global.634
- ___block_literal_global.647
- ___block_literal_global.652
- ___block_literal_global.660
- ___block_literal_global.667
- ___block_literal_global.678
- ___block_literal_global.682
- ___block_literal_global.683
- ___block_literal_global.689
- ___block_literal_global.704
- ___block_literal_global.712
- ___block_literal_global.713
- ___block_literal_global.717
- ___block_literal_global.721
- ___block_literal_global.745
- ___block_literal_global.749
- ___block_literal_global.787
- ___block_literal_global.817
- ___block_literal_global.849
- ___block_literal_global.863
- ___block_literal_global.869
- ___block_literal_global.963
- ___block_literal_global.965
- ___block_literal_global.967
- ___block_literal_global.970
- ___block_literal_global.977
- _objc_msgSend$layerManager
- _objc_msgSend$layers
CStrings:
+ "-With-"
+ "AXSubtitleView"
+ "B40@0:8@16@24^B32"
+ "Bounds: %@, interpage spacing: %@"
+ "Label"
+ "Multiscript multilingualLanguages %@"
+ "Optional<NavigationBarLargeTitleView>"
+ "PUPickerNavigationBarPalette"
+ "Paging origin: %@"
+ "UIKit.NavigationBarLargeTitleView"
+ "UIKit._UINavigationBarVisualProviderModernIOSSwift"
+ "_UISplitViewControllerAdaptiveColumn"
+ "_accessibilityScannerElementsGrouped:shouldIncludeNonScannerElements:"
+ "_axPageSize"
+ "_columns"
+ "_delegateShouldChangeCharactersInTextStorageRanges: replacementString: delegateCares:"
+ "_delegateShouldChangeCharactersInTextStorageRanges:replacementString:delegateCares:"
+ "_subtitleLabel"
+ "ax_filteredSetUsingBlock:"
+ "com.apple.SpringBoard.SceneWorkspace.RemoteAlert"
+ "doneButton"
+ "hostContainerView"
+ "hostedLayers"
+ "language %@"
+ "layout"
+ "multilingualLanguages"
+ "togglePrimaryEdgeBarButtonItem"
+ "wantsLargeTitleDisplayed"
- "B48@0:8{_NSRange=QQ}16@32^B40"
- "_delegateShouldChangeCharactersInTextStorageRange: replacementString: delegateCares:"
- "_delegateShouldChangeCharactersInTextStorageRange:replacementString:delegateCares:"
- "layerManager"
- "layers"

```
