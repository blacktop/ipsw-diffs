## UIKit

> `/System/Library/AccessibilityBundles/UIKit.axbundle/UIKit`

```diff

-2999.2.0.0.0
-  __TEXT.__text: 0x193900
-  __TEXT.__auth_stubs: 0x14e0
-  __TEXT.__objc_methlist: 0xf7e4
+3001.4.0.0.0
+  __TEXT.__text: 0x1954e8
+  __TEXT.__auth_stubs: 0x1500
+  __TEXT.__objc_methlist: 0xf88c
   __TEXT.__const: 0xa0
-  __TEXT.__cstring: 0x18bd7
-  __TEXT.__oslogstring: 0x2296
-  __TEXT.__gcc_except_tab: 0x35bc
+  __TEXT.__cstring: 0x18d0f
+  __TEXT.__oslogstring: 0x22ac
+  __TEXT.__gcc_except_tab: 0x3604
   __TEXT.__dlopen_cstrs: 0xb8
   __TEXT.__ustring: 0x78
-  __TEXT.__unwind_info: 0x2ce0
+  __TEXT.__unwind_info: 0x2d00
   __TEXT.__objc_classname: 0x90ad
-  __TEXT.__objc_methname: 0x15d79
+  __TEXT.__objc_methname: 0x15f3d
   __TEXT.__objc_methtype: 0x2159
-  __TEXT.__objc_stubs: 0x10540
+  __TEXT.__objc_stubs: 0x106e0
   __DATA_CONST.__got: 0xf80
-  __DATA_CONST.__const: 0x1e50
+  __DATA_CONST.__const: 0x1e78
   __DATA_CONST.__objc_classlist: 0x1b48
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5b28
+  __DATA_CONST.__objc_selrefs: 0x5ba0
   __DATA_CONST.__objc_protorefs: 0x40
-  __DATA_CONST.__objc_superrefs: 0xa78
+  __DATA_CONST.__objc_superrefs: 0xa80
   __DATA_CONST.__objc_arraydata: 0x190
-  __AUTH_CONST.__auth_got: 0xa80
+  __AUTH_CONST.__auth_got: 0xa90
   __AUTH_CONST.__const: 0x17a0
-  __AUTH_CONST.__cfstring: 0x1db20
+  __AUTH_CONST.__cfstring: 0x1dc60
   __AUTH_CONST.__objc_const: 0x20440
   __AUTH_CONST.__objc_intobj: 0x1f8
   __AUTH_CONST.__objc_dictobj: 0x140

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7C859EA6-1076-3716-BB54-5F42C8ADB67C
-  Functions: 5856
-  Symbols:   19986
-  CStrings:  12170
+  UUID: 851DB077-1122-3F6C-84B9-F4120F4271EE
+  Functions: 5874
+  Symbols:   20040
+  CStrings:  12207
 
Symbols:
+ -[UIApplicationAccessibility _accessibilityConnectedScenes]
+ -[UINavigationBarAccessibility _accessibilityHasSubviewsCountChanged]
+ -[UISheetPresentationControllerAccessibility _axActiveDetent]
+ -[UISheetPresentationControllerAccessibility _axGrabberStatusDescription]
+ -[UISheetPresentationControllerAccessibility _axSheetDetentType]
+ -[UIWindowSceneAccessibility _accessibilityLeadingMultitaskingElements]
+ -[UIWindowSceneAccessibility _accessibilityLeadingRemoteElements]
+ -[UIWindowSceneAccessibility _accessibilityLoadAccessibilityInformation]
+ -[UIWindowSceneAccessibility _accessibilitySetLeadingRemoteElements:]
+ -[UIWindowSceneAccessibility _accessibilitySetTrailingRemoteElements:]
+ -[UIWindowSceneAccessibility _accessibilityTrailingMultitaskingElements]
+ -[UIWindowSceneAccessibility _accessibilityTrailingRemoteElements]
+ -[UIWindowSceneAccessibility _axCreateLeadingRemoteElementsIfNecessary]
+ -[UIWindowSceneAccessibility _axCreateTrailingRemoteElementsIfNecessary]
+ -[UIWindowSceneAccessibility dealloc]
+ GCC_except_table37
+ GCC_except_table41
+ GCC_except_table42
+ _AXDeviceSupportsMultitasking
+ _AXRemoteElementFromObject
+ ___103-[UIApplicationAccessibility _accessibilityElementFirst:last:forFocus:allowScrolling:traversalOptions:]_block_invoke.859
+ ___103-[UIApplicationAccessibility _accessibilityElementFirst:last:forFocus:allowScrolling:traversalOptions:]_block_invoke.860
+ ___103-[UIApplicationAccessibility _accessibilityElementFirst:last:forFocus:allowScrolling:traversalOptions:]_block_invoke.861
+ ___103-[_UIRemoteViewControllerLegacyImplAccessibility _accessibilityLoadAccessibilityInformation:retryTime:]_block_invoke.413
+ ___45-[UITextViewAccessibility automationElements]_block_invoke.640
+ ___60-[UITableViewAccessibility _accessibilityHitTest:withEvent:]_block_invoke.695
+ ___60-[UITableViewAccessibility _accessibilityHitTest:withEvent:]_block_invoke_2.700
+ ___63-[UISheetPresentationControllerAccessibility _axMarkupGrabber:]_block_invoke_4
+ ___64-[UITableViewCellAccessibility _accessibilityHitTest:withEvent:]_block_invoke.698
+ ___68-[UIAccessibilityPickerComponent _accessibilityDateTimePickerValues]_block_invoke.330
+ ___68-[UIAccessibilityPickerComponent _accessibilityDateTimePickerValues]_block_invoke.343
+ ___69-[UIApplicationAccessibility _iosAccessibilitySetValue:forAttribute:]_block_invoke.968
+ ___69-[UIViewAccessibility _accessibilitySortedElementsWithinWithOptions:]_block_invoke.568
+ ___69-[UIViewAccessibility _accessibilitySortedElementsWithinWithOptions:]_block_invoke_2.569
+ ___71-[UIWindowSceneAccessibility _axCreateLeadingRemoteElementsIfNecessary]_block_invoke
+ ___72-[UIScrollViewAccessibility _accessibilityLastOpaqueElementWithOptions:]_block_invoke.442
+ ___72-[UIScrollViewAccessibility _accessibilityLastOpaqueElementWithOptions:]_block_invoke_2.443
+ ___72-[UIWindowSceneAccessibility _axCreateTrailingRemoteElementsIfNecessary]_block_invoke
+ ___73-[UIScrollViewAccessibility _accessibilityFirstOpaqueElementWithOptions:]_block_invoke.430
+ ___73-[UIScrollViewAccessibility _accessibilityFirstOpaqueElementWithOptions:]_block_invoke_2.431
+ ___74-[UITableViewAccessibility _accessibilitySortedElementsWithinWithOptions:]_block_invoke.718
+ ___74-[UITableViewAccessibility _accessibilitySortedElementsWithinWithOptions:]_block_invoke_2.719
+ ___75-[UICollectionViewListCellAccessibility _accessibilityHandleReorderMoveUp:]_block_invoke.512
+ ___76-[UICollectionViewAccessibility accessibilityCreatePrepareCellForIndexPath:]_block_invoke.528
+ ___79-[UICollectionViewAccessibility _accessibilitySortedElementsWithinWithOptions:]_block_invoke.599
+ ___79-[UICollectionViewAccessibility _accessibilitySortedElementsWithinWithOptions:]_block_invoke_2.600
+ ___80-[UITextInputUIResponderAccessibility _accessibilityInsertTextWithAlternatives:]_block_invoke.680
+ ___82-[_UIRemoteDictionaryViewControllerAccessibility tableView:cellForRowAtIndexPath:]_block_invoke.357
+ ___88-[UIKeyboardEmojiCollectionViewAccessibility _accessibilityLocalizedVisibleSectionNames]_block_invoke.369
+ ___89-[UITableViewAccessibility _axFirstLastOpaqueHeaderElementFromSection:options:direction:]_block_invoke.572
+ ___92-[UITableViewAccessibility _axOffScreenOpaqueHeaderElementInDirection:options:childElement:]_block_invoke.583
+ ___98-[UIKeyboardEmojiAndStickerCollectionViewAccessibility _accessibilityLocalizedVisibleSectionNames]_block_invoke.366
+ ___UIWindowSceneAccessibility___accessibilityLeadingRemoteElements
+ ___UIWindowSceneAccessibility___accessibilityTrailingRemoteElements
+ ___block_descriptor_40_e8_32s_e25_B16?0"AXRemoteElement"8ls32l8
+ ___block_literal_global.1007
+ ___block_literal_global.1013
+ ___block_literal_global.1028
+ ___block_literal_global.1031
+ ___block_literal_global.1033
+ ___block_literal_global.1048
+ ___block_literal_global.1053
+ ___block_literal_global.1075
+ ___block_literal_global.1084
+ ___block_literal_global.1120
+ ___block_literal_global.1874
+ ___block_literal_global.1880
+ ___block_literal_global.2527
+ ___block_literal_global.285
+ ___block_literal_global.289
+ ___block_literal_global.294
+ ___block_literal_global.295
+ ___block_literal_global.299
+ ___block_literal_global.3105
+ ___block_literal_global.3107
+ ___block_literal_global.3112
+ ___block_literal_global.3124
+ ___block_literal_global.3126
+ ___block_literal_global.313
+ ___block_literal_global.315
+ ___block_literal_global.3150
+ ___block_literal_global.3158
+ ___block_literal_global.329
+ ___block_literal_global.337
+ ___block_literal_global.339
+ ___block_literal_global.343
+ ___block_literal_global.347
+ ___block_literal_global.367
+ ___block_literal_global.369
+ ___block_literal_global.371
+ ___block_literal_global.373
+ ___block_literal_global.386
+ ___block_literal_global.408
+ ___block_literal_global.424
+ ___block_literal_global.429
+ ___block_literal_global.433
+ ___block_literal_global.437
+ ___block_literal_global.438
+ ___block_literal_global.445
+ ___block_literal_global.449
+ ___block_literal_global.453
+ ___block_literal_global.459
+ ___block_literal_global.460
+ ___block_literal_global.475
+ ___block_literal_global.479
+ ___block_literal_global.519
+ ___block_literal_global.523
+ ___block_literal_global.524
+ ___block_literal_global.532
+ ___block_literal_global.535
+ ___block_literal_global.542
+ ___block_literal_global.546
+ ___block_literal_global.563
+ ___block_literal_global.572
+ ___block_literal_global.581
+ ___block_literal_global.582
+ ___block_literal_global.593
+ ___block_literal_global.594
+ ___block_literal_global.598
+ ___block_literal_global.602
+ ___block_literal_global.612
+ ___block_literal_global.616
+ ___block_literal_global.622
+ ___block_literal_global.624
+ ___block_literal_global.634
+ ___block_literal_global.647
+ ___block_literal_global.652
+ ___block_literal_global.655
+ ___block_literal_global.658
+ ___block_literal_global.660
+ ___block_literal_global.667
+ ___block_literal_global.678
+ ___block_literal_global.682
+ ___block_literal_global.683
+ ___block_literal_global.689
+ ___block_literal_global.704
+ ___block_literal_global.712
+ ___block_literal_global.713
+ ___block_literal_global.717
+ ___block_literal_global.721
+ ___block_literal_global.745
+ ___block_literal_global.749
+ ___block_literal_global.752
+ ___block_literal_global.787
+ ___block_literal_global.817
+ ___block_literal_global.849
+ ___block_literal_global.863
+ ___block_literal_global.869
+ ___block_literal_global.963
+ ___block_literal_global.965
+ ___block_literal_global.967
+ ___block_literal_global.970
+ ___block_literal_global.977
+ _objc_msgSend$_accessibilityConnectedScenes
+ _objc_msgSend$_accessibilityLeadingRemoteElements
+ _objc_msgSend$_accessibilitySetLeadingRemoteElements:
+ _objc_msgSend$_accessibilitySetTrailingRemoteElements:
+ _objc_msgSend$_accessibilityTrailingRemoteElements
+ _objc_msgSend$_axActiveDetent
+ _objc_msgSend$_axCreateLeadingRemoteElementsIfNecessary
+ _objc_msgSend$_axCreateTrailingRemoteElementsIfNecessary
+ _objc_msgSend$_axGrabberStatusDescription
+ _objc_msgSend$_axSheetDetentType
+ _objc_msgSend$auditToken
+ _objc_msgSend$hostHandle
+ _objc_msgSend$remoteElementForBlock:
+ _objc_msgSend$safeSetForKey:
- GCC_except_table19
- GCC_except_table40
- ___103-[UIApplicationAccessibility _accessibilityElementFirst:last:forFocus:allowScrolling:traversalOptions:]_block_invoke.863
- ___103-[UIApplicationAccessibility _accessibilityElementFirst:last:forFocus:allowScrolling:traversalOptions:]_block_invoke.864
- ___103-[UIApplicationAccessibility _accessibilityElementFirst:last:forFocus:allowScrolling:traversalOptions:]_block_invoke.865
- ___103-[_UIRemoteViewControllerLegacyImplAccessibility _accessibilityLoadAccessibilityInformation:retryTime:]_block_invoke.416
- ___45-[UITextViewAccessibility automationElements]_block_invoke.643
- ___60-[UITableViewAccessibility _accessibilityHitTest:withEvent:]_block_invoke.698
- ___60-[UITableViewAccessibility _accessibilityHitTest:withEvent:]_block_invoke_2.703
- ___64-[UITableViewCellAccessibility _accessibilityHitTest:withEvent:]_block_invoke.701
- ___68-[UIAccessibilityPickerComponent _accessibilityDateTimePickerValues]_block_invoke.333
- ___68-[UIAccessibilityPickerComponent _accessibilityDateTimePickerValues]_block_invoke.346
- ___69-[UIApplicationAccessibility _iosAccessibilitySetValue:forAttribute:]_block_invoke.972
- ___69-[UIViewAccessibility _accessibilitySortedElementsWithinWithOptions:]_block_invoke.572
- ___69-[UIViewAccessibility _accessibilitySortedElementsWithinWithOptions:]_block_invoke_2.573
- ___72-[UIScrollViewAccessibility _accessibilityLastOpaqueElementWithOptions:]_block_invoke.445
- ___72-[UIScrollViewAccessibility _accessibilityLastOpaqueElementWithOptions:]_block_invoke_2.446
- ___73-[UIScrollViewAccessibility _accessibilityFirstOpaqueElementWithOptions:]_block_invoke.433
- ___73-[UIScrollViewAccessibility _accessibilityFirstOpaqueElementWithOptions:]_block_invoke_2.434
- ___74-[UITableViewAccessibility _accessibilitySortedElementsWithinWithOptions:]_block_invoke.721
- ___74-[UITableViewAccessibility _accessibilitySortedElementsWithinWithOptions:]_block_invoke_2.722
- ___75-[UICollectionViewListCellAccessibility _accessibilityHandleReorderMoveUp:]_block_invoke.515
- ___76-[UICollectionViewAccessibility accessibilityCreatePrepareCellForIndexPath:]_block_invoke.531
- ___79-[UICollectionViewAccessibility _accessibilitySortedElementsWithinWithOptions:]_block_invoke.602
- ___79-[UICollectionViewAccessibility _accessibilitySortedElementsWithinWithOptions:]_block_invoke_2.603
- ___80-[UITextInputUIResponderAccessibility _accessibilityInsertTextWithAlternatives:]_block_invoke.683
- ___82-[_UIRemoteDictionaryViewControllerAccessibility tableView:cellForRowAtIndexPath:]_block_invoke.360
- ___88-[UIKeyboardEmojiCollectionViewAccessibility _accessibilityLocalizedVisibleSectionNames]_block_invoke.372
- ___89-[UITableViewAccessibility _axFirstLastOpaqueHeaderElementFromSection:options:direction:]_block_invoke.575
- ___92-[UITableViewAccessibility _axOffScreenOpaqueHeaderElementInDirection:options:childElement:]_block_invoke.586
- ___98-[UIKeyboardEmojiAndStickerCollectionViewAccessibility _accessibilityLocalizedVisibleSectionNames]_block_invoke.369
- ___block_literal_global.1011
- ___block_literal_global.1017
- ___block_literal_global.1032
- ___block_literal_global.1035
- ___block_literal_global.1037
- ___block_literal_global.1052
- ___block_literal_global.1057
- ___block_literal_global.1079
- ___block_literal_global.1088
- ___block_literal_global.1124
- ___block_literal_global.1877
- ___block_literal_global.1883
- ___block_literal_global.2530
- ___block_literal_global.288
- ___block_literal_global.292
- ___block_literal_global.297
- ___block_literal_global.298
- ___block_literal_global.302
- ___block_literal_global.3108
- ___block_literal_global.3110
- ___block_literal_global.3115
- ___block_literal_global.3127
- ___block_literal_global.3129
- ___block_literal_global.3153
- ___block_literal_global.316
- ___block_literal_global.3161
- ___block_literal_global.318
- ___block_literal_global.332
- ___block_literal_global.340
- ___block_literal_global.342
- ___block_literal_global.346
- ___block_literal_global.350
- ___block_literal_global.370
- ___block_literal_global.372
- ___block_literal_global.377
- ___block_literal_global.379
- ___block_literal_global.389
- ___block_literal_global.411
- ___block_literal_global.427
- ___block_literal_global.432
- ___block_literal_global.436
- ___block_literal_global.440
- ___block_literal_global.444
- ___block_literal_global.448
- ___block_literal_global.456
- ___block_literal_global.458
- ___block_literal_global.462
- ___block_literal_global.463
- ___block_literal_global.478
- ___block_literal_global.482
- ___block_literal_global.522
- ___block_literal_global.526
- ___block_literal_global.527
- ___block_literal_global.536
- ___block_literal_global.538
- ___block_literal_global.545
- ___block_literal_global.549
- ___block_literal_global.575
- ___block_literal_global.585
- ___block_literal_global.596
- ___block_literal_global.597
- ___block_literal_global.601
- ___block_literal_global.609
- ___block_literal_global.615
- ___block_literal_global.619
- ___block_literal_global.625
- ___block_literal_global.627
- ___block_literal_global.637
- ___block_literal_global.653
- ___block_literal_global.656
- ___block_literal_global.659
- ___block_literal_global.662
- ___block_literal_global.664
- ___block_literal_global.670
- ___block_literal_global.681
- ___block_literal_global.685
- ___block_literal_global.687
- ___block_literal_global.695
- ___block_literal_global.707
- ___block_literal_global.715
- ___block_literal_global.716
- ___block_literal_global.720
- ___block_literal_global.724
- ___block_literal_global.748
- ___block_literal_global.753
- ___block_literal_global.761
- ___block_literal_global.790
- ___block_literal_global.820
- ___block_literal_global.852
- ___block_literal_global.866
- ___block_literal_global.872
- ___block_literal_global.966
- ___block_literal_global.969
- ___block_literal_global.971
- ___block_literal_global.974
- ___block_literal_global.980
- _objc_msgSend$viewControllerForColumn:
CStrings:
+ "%@:%@"
+ "B16@?0@\"AXRemoteElement\"8"
+ "FloatingBarHostingView<FloatingBarContainer>"
+ "NavBar: top most item %{sensitive}@ %@"
+ "NavBar: top most nav item title %{sensitive}@ %@"
+ "_TtC5UIKitP33_2E11A995A04AA6F19429971D06CC321E24FloatingBarContainerView"
+ "_accessibilityConnectedScenes"
+ "_accessibilityLeadingMultitaskingElements"
+ "_accessibilityLeadingRemoteElements"
+ "_accessibilitySetLeadingRemoteElements:"
+ "_accessibilitySetTrailingRemoteElements:"
+ "_accessibilityTrailingMultitaskingElements"
+ "_accessibilityTrailingRemoteElements"
+ "_axActiveDetent"
+ "_axCreateLeadingRemoteElementsIfNecessary"
+ "_axCreateTrailingRemoteElementsIfNecessary"
+ "_axGrabberStatusDescription"
+ "_axSheetDetentType"
+ "_childViewControllerForSpokenContent"
+ "auditToken"
+ "hostHandle"
+ "hostingView"
+ "kAXSubviewCount"
+ "remoteElementForBlock:"
+ "resize-grabber"
+ "safeSetForKey:"
+ "sheet.card.size.full"
+ "sheet.card.size.medium"
+ "sheet.card.size.small"
+ "window-controls"
- "NavBar: top most item %@ %@"
- "NavBar: top most nav item title %@ %@"

```
