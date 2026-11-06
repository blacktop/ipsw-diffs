## UIKit

> `/System/iOSSupport/System/Library/AccessibilityBundles/UIKit.axbundle/Contents/MacOS/UIKit`

```diff

-3048.0.0.0.0
-  __TEXT.__text: 0x15f9e4
-  __TEXT.__objc_methlist: 0x100f4
+3050.3.6.0.0
+  __TEXT.__text: 0x163f80
+  __TEXT.__objc_methlist: 0x1028c
   __TEXT.__dlopen_cstrs: 0x19c
-  __TEXT.__const: 0x1a8
-  __TEXT.__gcc_except_tab: 0x39dc
-  __TEXT.__cstring: 0x19b73
-  __TEXT.__oslogstring: 0x26ea
+  __TEXT.__const: 0x1b0
+  __TEXT.__gcc_except_tab: 0x3a1c
+  __TEXT.__cstring: 0x19c96
+  __TEXT.__oslogstring: 0x2841
   __TEXT.__ustring: 0x78
-  __TEXT.__unwind_info: 0x4458
+  __TEXT.__unwind_info: 0x44e0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1fb0
-  __DATA_CONST.__objc_classlist: 0x1c20
+  __DATA_CONST.__const: 0x2020
+  __DATA_CONST.__objc_classlist: 0x1c40
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5ea8
+  __DATA_CONST.__objc_selrefs: 0x5f58
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0xad8
+  __DATA_CONST.__objc_superrefs: 0xaf0
   __DATA_CONST.__objc_arraydata: 0x150
-  __DATA_CONST.__got: 0x1038
-  __AUTH_CONST.__const: 0x1760
-  __AUTH_CONST.__cfstring: 0x1e920
-  __AUTH_CONST.__objc_const: 0x21478
+  __DATA_CONST.__got: 0x1040
+  __AUTH_CONST.__const: 0x1780
+  __AUTH_CONST.__cfstring: 0x1ea00
+  __AUTH_CONST.__objc_const: 0x216b8
   __AUTH_CONST.__objc_intobj: 0x1f8
   __AUTH_CONST.__objc_dictobj: 0x140
   __AUTH_CONST.__objc_arrayobj: 0x18

   __AUTH.__objc_data: 0x15e0
   __DATA.__objc_ivar: 0x148
   __DATA.__data: 0x640
-  __DATA.__bss: 0x418
-  __DATA_DIRTY.__objc_data: 0x10360
+  __DATA.__bss: 0x410
+  __DATA_DIRTY.__objc_data: 0x104a0
   __DATA_DIRTY.__common: 0x8
   __DATA_DIRTY.__bss: 0x1e0
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 6110
-  Symbols:   14377
-  CStrings:  4299
+  Functions: 6165
+  Symbols:   14473
+  CStrings:  4309
 
Symbols:
+ +[UIKeyboardModeSwitcherViewAccessibility _accessibilityPerformValidations:]
+ +[UIKeyboardModeSwitcherViewAccessibility(SafeCategory) safeCategoryBaseClass]
+ +[UIKeyboardModeSwitcherViewAccessibility(SafeCategory) safeCategoryTargetClassName]
+ +[_UINavigationItemProxyAccessibility _accessibilityPerformValidations:]
+ +[_UINavigationItemProxyAccessibility(SafeCategory) safeCategoryBaseClass]
+ +[_UINavigationItemProxyAccessibility(SafeCategory) safeCategoryTargetClassName]
+ -[UIAccessibilityElementMockView accessibilitySupportsTextSelection]
+ -[UIApplicationAccessibility _accessibilityElementsForStatusBar:sorted:]
+ -[UIApplicationAccessibility _accessibilityStatusBarElements:sorted:forWindowScene:]
+ -[UIApplicationAccessibility _axFirstVisibleAccessibleElementInContainer:]
+ -[UIApplicationAccessibility _axShouldDeferOffscreenFirstFocusForElement:]
+ -[UICollectionViewAccessibility _accessibilityViewChildrenWithOptions:]
+ -[UICollectionViewCellAccessibilityElement accessibilitySupportsTextSelection]
+ -[UIDropShadowViewAccessibility _axCoversWindow]
+ -[UIDropShadowViewAccessibility _axSheetDimmingViewIsModal]
+ -[UIDropShadowViewAccessibility accessibilityViewIsModal]
+ -[UIIndexBarAccessoryViewAccessibility _axLabelForEntry:lowercaseTitle:]
+ -[UIKeyboardModeSwitcherViewAccessibility accessibilityLabel]
+ -[UIKeyboardModeSwitcherViewAccessibility accessibilityTraits]
+ -[UIKeyboardModeSwitcherViewAccessibility isAccessibilityElement]
+ -[UIResponderAccessibility _axFKAArrowKeysAdjustingValue]
+ -[UIScrollViewAccessibility accessibilityApplyScrollContent:sendScrollStatus:animateWithDuration:animationCurve:allowDelegateTargetRedirect:]
+ -[UIScrollViewAccessibility accessibilityApplyScrollContentOverride:sendScrollStatus:animateWithDuration:animationCurve:allowDelegateTargetRedirect:]
+ -[UISegmentAccessibility accessibilityFrame]
+ -[UITableViewCellAccessibilityElement accessibilitySupportsTextSelection]
+ -[UITextViewAccessibility accessibilitySupportsTextSelection]
+ -[UITransitionViewAccessibility _accessibilityDimmingViewObscuresScreen]
+ -[_AXUITextViewParagraphElement accessibilitySupportsTextSelection]
+ -[_UIButtonBarButtonAccessibility _axHitTestReachesSelfAtPoint:]
+ -[_UIButtonBarButtonAccessibility accessibilityActivationPoint]
+ -[_UIButtonBarButtonAccessibility accessibilityCustomActions]
+ -[_UIContextMenuUIControllerAccessibility _axModalPresentedByMenuActionOwnsFocusForTriggerElement:]
+ -[_UIInterfaceActionCustomViewRepresentationViewAccessibility accessibilityActivate]
+ -[_UIModernBarButtonAccessibility _accessibilityOwningButtonBarButton]
+ -[_UIModernBarButtonAccessibility accessibilityLabel]
+ -[_UINavigationItemProxyAccessibility initWithDestinationNavigationItem:sourceNavigationItem:]
+ -[_UINavigationItemProxyAccessibility navigationItemUpdatedTitleContent:animated:]
+ -[_UIScenePresentationViewAccessibility _accessibilityHitTest:withEvent:]
+ -[_UITabButtonAccessibility _accessibilityUpdatesOnActivationAfterDelay]
+ GCC_except_table1095
+ GCC_except_table1102
+ GCC_except_table1103
+ GCC_except_table1142
+ GCC_except_table1186
+ GCC_except_table1214
+ GCC_except_table1229
+ GCC_except_table1263
+ GCC_except_table1295
+ GCC_except_table1299
+ GCC_except_table1315
+ GCC_except_table1327
+ GCC_except_table1343
+ GCC_except_table1345
+ GCC_except_table1356
+ GCC_except_table136
+ GCC_except_table1369
+ GCC_except_table1395
+ GCC_except_table1510
+ GCC_except_table1539
+ GCC_except_table1541
+ GCC_except_table1548
+ GCC_except_table1558
+ GCC_except_table1586
+ GCC_except_table1589
+ GCC_except_table1593
+ GCC_except_table1614
+ GCC_except_table1667
+ GCC_except_table1696
+ GCC_except_table1697
+ GCC_except_table171
+ GCC_except_table1800
+ GCC_except_table1822
+ GCC_except_table1827
+ GCC_except_table1830
+ GCC_except_table1832
+ GCC_except_table1839
+ GCC_except_table1861
+ GCC_except_table1890
+ GCC_except_table1893
+ GCC_except_table1942
+ GCC_except_table1948
+ GCC_except_table1972
+ GCC_except_table1986
+ GCC_except_table1997
+ GCC_except_table2033
+ GCC_except_table2047
+ GCC_except_table206
+ GCC_except_table2138
+ GCC_except_table2141
+ GCC_except_table2190
+ GCC_except_table2212
+ GCC_except_table2292
+ GCC_except_table2322
+ GCC_except_table2327
+ GCC_except_table2335
+ GCC_except_table2354
+ GCC_except_table2371
+ GCC_except_table2427
+ GCC_except_table2455
+ GCC_except_table2465
+ GCC_except_table2473
+ GCC_except_table2489
+ GCC_except_table2508
+ GCC_except_table2604
+ GCC_except_table262
+ GCC_except_table2688
+ GCC_except_table2714
+ GCC_except_table2748
+ GCC_except_table2812
+ GCC_except_table2816
+ GCC_except_table2841
+ GCC_except_table2860
+ GCC_except_table2886
+ GCC_except_table2980
+ GCC_except_table3013
+ GCC_except_table3060
+ GCC_except_table3118
+ GCC_except_table3204
+ GCC_except_table3210
+ GCC_except_table3264
+ GCC_except_table3277
+ GCC_except_table3410
+ GCC_except_table3411
+ GCC_except_table3467
+ GCC_except_table3527
+ GCC_except_table3670
+ GCC_except_table3741
+ GCC_except_table3751
+ GCC_except_table3770
+ GCC_except_table3895
+ GCC_except_table3909
+ GCC_except_table3930
+ GCC_except_table3949
+ GCC_except_table3970
+ GCC_except_table3973
+ GCC_except_table4008
+ GCC_except_table4010
+ GCC_except_table402
+ GCC_except_table4024
+ GCC_except_table4032
+ GCC_except_table4046
+ GCC_except_table4047
+ GCC_except_table4073
+ GCC_except_table4078
+ GCC_except_table4112
+ GCC_except_table4132
+ GCC_except_table4137
+ GCC_except_table4145
+ GCC_except_table4147
+ GCC_except_table4163
+ GCC_except_table4177
+ GCC_except_table4216
+ GCC_except_table4234
+ GCC_except_table4240
+ GCC_except_table4252
+ GCC_except_table4274
+ GCC_except_table4281
+ GCC_except_table4420
+ GCC_except_table449
+ GCC_except_table4537
+ GCC_except_table461
+ GCC_except_table4689
+ GCC_except_table4696
+ GCC_except_table4749
+ GCC_except_table4773
+ GCC_except_table4774
+ GCC_except_table4796
+ GCC_except_table4830
+ GCC_except_table4835
+ GCC_except_table4837
+ GCC_except_table4846
+ GCC_except_table4850
+ GCC_except_table4851
+ GCC_except_table4852
+ GCC_except_table4858
+ GCC_except_table4859
+ GCC_except_table4862
+ GCC_except_table4868
+ GCC_except_table4884
+ GCC_except_table4900
+ GCC_except_table4917
+ GCC_except_table4987
+ GCC_except_table500
+ GCC_except_table5042
+ GCC_except_table510
+ GCC_except_table5154
+ GCC_except_table5165
+ GCC_except_table5181
+ GCC_except_table5206
+ GCC_except_table5208
+ GCC_except_table5213
+ GCC_except_table522
+ GCC_except_table5392
+ GCC_except_table5536
+ GCC_except_table559
+ GCC_except_table5637
+ GCC_except_table5649
+ GCC_except_table5667
+ GCC_except_table5751
+ GCC_except_table5779
+ GCC_except_table5824
+ GCC_except_table5844
+ GCC_except_table5950
+ GCC_except_table5956
+ GCC_except_table597
+ GCC_except_table5974
+ GCC_except_table5981
+ GCC_except_table6009
+ GCC_except_table6026
+ GCC_except_table609
+ GCC_except_table6108
+ GCC_except_table611
+ GCC_except_table617
+ GCC_except_table621
+ GCC_except_table627
+ GCC_except_table658
+ GCC_except_table665
+ GCC_except_table768
+ GCC_except_table769
+ GCC_except_table771
+ GCC_except_table777
+ GCC_except_table778
+ GCC_except_table780
+ GCC_except_table808
+ GCC_except_table822
+ GCC_except_table844
+ _AXIsHostedScene
+ _AXLocalizationForLocale
+ _AXScrollViewTotalPages
+ _OBJC_CLASS_$_UIKeyboardModeSwitcherViewAccessibility
+ _OBJC_CLASS_$__UINavigationItemProxyAccessibility
+ _OBJC_CLASS_$___UIKeyboardModeSwitcherViewAccessibility_super
+ _OBJC_CLASS_$____UINavigationItemProxyAccessibility_super
+ _OBJC_METACLASS_$_UIKeyboardModeSwitcherViewAccessibility
+ _OBJC_METACLASS_$__UINavigationItemProxyAccessibility
+ _OBJC_METACLASS_$___UIKeyboardModeSwitcherViewAccessibility_super
+ _OBJC_METACLASS_$____UINavigationItemProxyAccessibility_super
+ __AXSBrailleScreenInputEnabled
+ __AXTransferNavigationItemAccessibilityLabel
+ __OBJC_$_CLASS_METHODS_UIKeyboardModeSwitcherViewAccessibility(SafeCategory)
+ __OBJC_$_CLASS_METHODS__UINavigationItemProxyAccessibility(SafeCategory)
+ __OBJC_$_INSTANCE_METHODS_UIKeyboardModeSwitcherViewAccessibility
+ __OBJC_$_INSTANCE_METHODS__UINavigationItemProxyAccessibility
+ __OBJC_CLASS_RO_$_UIKeyboardModeSwitcherViewAccessibility
+ __OBJC_CLASS_RO_$__UINavigationItemProxyAccessibility
+ __OBJC_CLASS_RO_$___UIKeyboardModeSwitcherViewAccessibility_super
+ __OBJC_CLASS_RO_$____UINavigationItemProxyAccessibility_super
+ __OBJC_METACLASS_RO_$_UIKeyboardModeSwitcherViewAccessibility
+ __OBJC_METACLASS_RO_$__UINavigationItemProxyAccessibility
+ __OBJC_METACLASS_RO_$___UIKeyboardModeSwitcherViewAccessibility_super
+ __OBJC_METACLASS_RO_$____UINavigationItemProxyAccessibility_super
+ ___102-[UITableViewAccessibility _accessibilitySortedElementsWithinPreservingFloatingHeader:sortedElements:]_block_invoke_2
+ ___141-[UIScrollViewAccessibility accessibilityApplyScrollContent:sendScrollStatus:animateWithDuration:animationCurve:allowDelegateTargetRedirect:]_block_invoke
+ ___141-[UIScrollViewAccessibility accessibilityApplyScrollContent:sendScrollStatus:animateWithDuration:animationCurve:allowDelegateTargetRedirect:]_block_invoke_2
+ ___141-[UIScrollViewAccessibility accessibilityApplyScrollContent:sendScrollStatus:animateWithDuration:animationCurve:allowDelegateTargetRedirect:]_block_invoke_3
+ ___141-[UIScrollViewAccessibility accessibilityApplyScrollContent:sendScrollStatus:animateWithDuration:animationCurve:allowDelegateTargetRedirect:]_block_invoke_4
+ ___152-[UIKeyboardLayoutStarAccessibility continueFromInternationalActionForTouchUp:withActions:timestamp:interval:didLongPress:prevActions:executionContext:]_block_invoke_2
+ ___71-[UIKeyboardLayoutStarAccessibility _accessibilityCreateElementForKey:]_block_invoke_2
+ ___74-[UIApplicationAccessibility _axFirstVisibleAccessibleElementInContainer:]_block_invoke
+ ___74-[UIApplicationAccessibility _axShouldDeferOffscreenFirstFocusForElement:]_block_invoke
+ ___84-[_UIInterfaceActionCustomViewRepresentationViewAccessibility accessibilityActivate]_block_invoke
+ ___87-[_UINavigationBarTitleControlAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke_2
+ ___block_descriptor_40_e16_B16?0"UIView"8lu32l8
+ ___block_descriptor_40_e8_32r_e12_v24?08^B16lr32l8
+ ___block_descriptor_48_e8_32w40w_e15_"NSString"8?0lw32l8w40l8
+ ___os_log_helper_16_3_2_8_65_8_65
+ _accessibilityLocalizedStringForLanguage
+ _axLanguageOverridingAllContainedElements
+ _fmodf
+ _objc_msgSend$_accessibilityIsScrollAncestor
+ _objc_msgSend$_accessibilityIsVerticalAdjustableElement
+ _objc_msgSend$_accessibilityIterateScrollParentsUsingBlock:
+ _objc_msgSend$_accessibilityOffsetForOpaqueElementDirection:
+ _objc_msgSend$_accessibilityOwningButtonBarButton
+ _objc_msgSend$_accessibilityStatusBarIsVerticalAlongWindowEdge
+ _objc_msgSend$_accessibilityVisiblePoint
+ _objc_msgSend$_axCoversWindow
+ _objc_msgSend$_axFKAArrowKeysAdjustingValue
+ _objc_msgSend$_axSheetDimmingViewIsModal
+ _objc_msgSend$_isEmbeddedScreen
+ _objc_msgSend$accessibilitySupportsTextSelection
+ _objc_msgSend$apportionsSegmentWidthsByContent
+ _objc_msgSend$currentImage
+ _objc_msgSend$currentTitle
+ _objc_msgSend$objectsAtIndexes:
+ _objc_msgSend$sendAction:
- GCC_except_table1089
- GCC_except_table1096
- GCC_except_table1097
- GCC_except_table1136
- GCC_except_table1180
- GCC_except_table1208
- GCC_except_table1223
- GCC_except_table1257
- GCC_except_table1287
- GCC_except_table1300
- GCC_except_table1313
- GCC_except_table1329
- GCC_except_table1331
- GCC_except_table1342
- GCC_except_table135
- GCC_except_table1355
- GCC_except_table1381
- GCC_except_table1496
- GCC_except_table1525
- GCC_except_table1527
- GCC_except_table1534
- GCC_except_table1544
- GCC_except_table1571
- GCC_except_table1574
- GCC_except_table1578
- GCC_except_table1599
- GCC_except_table1652
- GCC_except_table1681
- GCC_except_table1682
- GCC_except_table170
- GCC_except_table1784
- GCC_except_table1795
- GCC_except_table1806
- GCC_except_table1807
- GCC_except_table1814
- GCC_except_table1816
- GCC_except_table1845
- GCC_except_table1874
- GCC_except_table1877
- GCC_except_table1926
- GCC_except_table1932
- GCC_except_table1956
- GCC_except_table1970
- GCC_except_table1980
- GCC_except_table2016
- GCC_except_table2030
- GCC_except_table205
- GCC_except_table2121
- GCC_except_table2124
- GCC_except_table2172
- GCC_except_table2194
- GCC_except_table2274
- GCC_except_table2298
- GCC_except_table2303
- GCC_except_table2311
- GCC_except_table2330
- GCC_except_table2347
- GCC_except_table2403
- GCC_except_table2431
- GCC_except_table2441
- GCC_except_table2448
- GCC_except_table2464
- GCC_except_table2483
- GCC_except_table2576
- GCC_except_table261
- GCC_except_table2660
- GCC_except_table2686
- GCC_except_table2720
- GCC_except_table2778
- GCC_except_table2782
- GCC_except_table2807
- GCC_except_table2826
- GCC_except_table2852
- GCC_except_table2946
- GCC_except_table2978
- GCC_except_table3024
- GCC_except_table3080
- GCC_except_table3165
- GCC_except_table3171
- GCC_except_table3225
- GCC_except_table3238
- GCC_except_table3369
- GCC_except_table3370
- GCC_except_table3426
- GCC_except_table3486
- GCC_except_table3629
- GCC_except_table3700
- GCC_except_table3710
- GCC_except_table3729
- GCC_except_table3854
- GCC_except_table3868
- GCC_except_table3889
- GCC_except_table3908
- GCC_except_table3929
- GCC_except_table3932
- GCC_except_table3966
- GCC_except_table3968
- GCC_except_table3982
- GCC_except_table3990
- GCC_except_table4004
- GCC_except_table4005
- GCC_except_table401
- GCC_except_table4031
- GCC_except_table4036
- GCC_except_table4061
- GCC_except_table4070
- GCC_except_table4090
- GCC_except_table4095
- GCC_except_table4105
- GCC_except_table4121
- GCC_except_table4135
- GCC_except_table4174
- GCC_except_table4192
- GCC_except_table4198
- GCC_except_table4210
- GCC_except_table4232
- GCC_except_table4239
- GCC_except_table4377
- GCC_except_table448
- GCC_except_table4494
- GCC_except_table460
- GCC_except_table4646
- GCC_except_table4653
- GCC_except_table4706
- GCC_except_table4730
- GCC_except_table4731
- GCC_except_table4753
- GCC_except_table4787
- GCC_except_table4792
- GCC_except_table4794
- GCC_except_table4803
- GCC_except_table4807
- GCC_except_table4808
- GCC_except_table4809
- GCC_except_table4815
- GCC_except_table4816
- GCC_except_table4819
- GCC_except_table4825
- GCC_except_table4841
- GCC_except_table4856
- GCC_except_table4873
- GCC_except_table4942
- GCC_except_table496
- GCC_except_table4996
- GCC_except_table506
- GCC_except_table5108
- GCC_except_table5119
- GCC_except_table5135
- GCC_except_table5160
- GCC_except_table5162
- GCC_except_table5167
- GCC_except_table517
- GCC_except_table5346
- GCC_except_table5484
- GCC_except_table554
- GCC_except_table5583
- GCC_except_table5595
- GCC_except_table5613
- GCC_except_table5697
- GCC_except_table5725
- GCC_except_table5770
- GCC_except_table5789
- GCC_except_table5895
- GCC_except_table5901
- GCC_except_table5919
- GCC_except_table592
- GCC_except_table5926
- GCC_except_table5954
- GCC_except_table5971
- GCC_except_table604
- GCC_except_table6053
- GCC_except_table606
- GCC_except_table612
- GCC_except_table616
- GCC_except_table622
- GCC_except_table653
- GCC_except_table660
- GCC_except_table761
- GCC_except_table763
- GCC_except_table764
- GCC_except_table770
- GCC_except_table772
- GCC_except_table773
- GCC_except_table803
- GCC_except_table817
- GCC_except_table839
- ___113-[UIScrollViewAccessibility accessibilityApplyScrollContent:sendScrollStatus:animateWithDuration:animationCurve:]_block_invoke
- ___113-[UIScrollViewAccessibility accessibilityApplyScrollContent:sendScrollStatus:animateWithDuration:animationCurve:]_block_invoke_2
- ___113-[UIScrollViewAccessibility accessibilityApplyScrollContent:sendScrollStatus:animateWithDuration:animationCurve:]_block_invoke_3
- ___113-[UIScrollViewAccessibility accessibilityApplyScrollContent:sendScrollStatus:animateWithDuration:animationCurve:]_block_invoke_4
CStrings:
+ "AXProxyDestinationNavigationItem"
+ "No local children for remote %{private}@, fell back to remote first/last %{private}@"
+ "UIKeyboardModeSwitcherView"
+ "UIKeyboardModeSwitcherViewAccessibility"
+ "_UINavigationItemProxy"
+ "_UINavigationItemProxyAccessibility"
+ "_accessibilityPreferredFocusedWindow"
+ "dimmingView"
+ "initWithDestinationNavigationItem:sourceNavigationItem:"
+ "keyboardModeSwitcherView"
+ "navigationItemUpdatedTitleContent:animated:"
+ "rdar://179296860 First-focus deferred off-screen element %{private}@ to visible %{private}@ in a pre-scrolled container"
+ "rdar://179296860 First-focus resolved to an off-screen element inside a scrolled-away container (expected a visible element): %{private}@"
- "_imageButton"
- "_titleButton"
- "traitCollection"
```
