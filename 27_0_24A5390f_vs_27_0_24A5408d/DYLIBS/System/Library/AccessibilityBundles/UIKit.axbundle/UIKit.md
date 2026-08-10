## UIKit

> `/System/Library/AccessibilityBundles/UIKit.axbundle/UIKit`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__DATA_DIRTY.__objc_data`

```diff

-3045.0.0.0.0
-  __TEXT.__text: 0x15951c
-  __TEXT.__objc_methlist: 0xfb5c
+3048.0.0.0.0
+  __TEXT.__text: 0x15b3b8
+  __TEXT.__objc_methlist: 0xfc24
   __TEXT.__dlopen_cstrs: 0xb8
-  __TEXT.__const: 0x1a8
-  __TEXT.__gcc_except_tab: 0x35c4
-  __TEXT.__cstring: 0x19341
-  __TEXT.__oslogstring: 0x24cb
+  __TEXT.__const: 0x1c0
+  __TEXT.__gcc_except_tab: 0x35c8
+  __TEXT.__cstring: 0x19451
+  __TEXT.__oslogstring: 0x2712
   __TEXT.__ustring: 0x78
-  __TEXT.__unwind_info: 0x42b8
+  __TEXT.__unwind_info: 0x4308
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1ee0
-  __DATA_CONST.__objc_classlist: 0x1b50
+  __DATA_CONST.__const: 0x1ee8
+  __DATA_CONST.__objc_classlist: 0x1b70
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5d80
+  __DATA_CONST.__objc_selrefs: 0x5d88
   __DATA_CONST.__objc_protorefs: 0x48
-  __DATA_CONST.__objc_superrefs: 0xa80
+  __DATA_CONST.__objc_superrefs: 0xa90
   __DATA_CONST.__objc_arraydata: 0x160
-  __DATA_CONST.__got: 0xfd0
+  __DATA_CONST.__got: 0xfd8
   __AUTH_CONST.__const: 0x17c0
-  __AUTH_CONST.__cfstring: 0x1dfc0
-  __AUTH_CONST.__objc_const: 0x20740
+  __AUTH_CONST.__cfstring: 0x1e0e0
+  __AUTH_CONST.__objc_const: 0x20980
   __AUTH_CONST.__objc_intobj: 0x210
   __AUTH_CONST.__objc_dictobj: 0x140
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0xb40
+  __AUTH.__objc_data: 0xc80
   __DATA.__objc_ivar: 0x130
-  __DATA.__data: 0x698
-  __DATA.__bss: 0x400
+  __DATA.__data: 0x6a0
+  __DATA.__bss: 0x408
   __DATA_DIRTY.__objc_data: 0x105e0
   __DATA_DIRTY.__common: 0x8
-  __DATA_DIRTY.__bss: 0x1e9
+  __DATA_DIRTY.__bss: 0x1ea
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 5978
-  Symbols:   14039
-  CStrings:  4203
+  Functions: 5998
+  Symbols:   14086
+  CStrings:  4215
 
Symbols:
+ +[UIPlatformGlassInteractionViewAccessibility _accessibilityPerformValidations:]
+ +[UIPlatformGlassInteractionViewAccessibility(SafeCategory) safeCategoryBaseClass]
+ +[UIPlatformGlassInteractionViewAccessibility(SafeCategory) safeCategoryTargetClassName]
+ +[_UIModernBarButtonAccessibility _accessibilityPerformValidations:]
+ +[_UIModernBarButtonAccessibility(SafeCategory) safeCategoryBaseClass]
+ +[_UIModernBarButtonAccessibility(SafeCategory) safeCategoryTargetClassName]
+ -[UIPlatformGlassInteractionViewAccessibility accessibilityElementsHidden]
+ -[UISegmentAccessibility accessibilityActivate]
+ -[UITextViewAccessibility _axPresentsAsSingleElement]
+ -[UITextViewAccessibility _axShouldExposeLinksForMotorControlFeatures]
+ -[_UIFloatingBarContainerViewAccessibility _accessibilityHitTest:withEvent:]
+ -[_UIFloatingBarContainerViewAccessibility _accessibilityHitTestShouldFallbackToNearestChild]
+ -[_UIFloatingBarContainerViewAccessibility _accessibilitySortPriority]
+ -[_UIModernBarButtonAccessibility accessibilityTraits]
+ GCC_except_table1109
+ GCC_except_table1116
+ GCC_except_table1117
+ GCC_except_table1156
+ GCC_except_table1201
+ GCC_except_table1229
+ GCC_except_table1244
+ GCC_except_table1278
+ GCC_except_table1308
+ GCC_except_table1321
+ GCC_except_table1334
+ GCC_except_table1350
+ GCC_except_table1352
+ GCC_except_table1363
+ GCC_except_table1500
+ GCC_except_table1520
+ GCC_except_table1522
+ GCC_except_table1536
+ GCC_except_table1563
+ GCC_except_table1566
+ GCC_except_table1569
+ GCC_except_table1590
+ GCC_except_table1639
+ GCC_except_table1668
+ GCC_except_table1669
+ GCC_except_table1764
+ GCC_except_table1775
+ GCC_except_table1786
+ GCC_except_table1791
+ GCC_except_table1794
+ GCC_except_table1796
+ GCC_except_table1803
+ GCC_except_table1825
+ GCC_except_table1854
+ GCC_except_table1857
+ GCC_except_table1906
+ GCC_except_table1912
+ GCC_except_table1932
+ GCC_except_table1946
+ GCC_except_table1956
+ GCC_except_table2002
+ GCC_except_table2096
+ GCC_except_table2099
+ GCC_except_table2147
+ GCC_except_table2169
+ GCC_except_table2253
+ GCC_except_table2277
+ GCC_except_table2282
+ GCC_except_table2290
+ GCC_except_table2309
+ GCC_except_table2326
+ GCC_except_table2382
+ GCC_except_table2410
+ GCC_except_table2420
+ GCC_except_table2427
+ GCC_except_table2443
+ GCC_except_table2462
+ GCC_except_table2555
+ GCC_except_table261
+ GCC_except_table2639
+ GCC_except_table2695
+ GCC_except_table2763
+ GCC_except_table2767
+ GCC_except_table2785
+ GCC_except_table2804
+ GCC_except_table2921
+ GCC_except_table2954
+ GCC_except_table3005
+ GCC_except_table3028
+ GCC_except_table3080
+ GCC_except_table3164
+ GCC_except_table3170
+ GCC_except_table3223
+ GCC_except_table3236
+ GCC_except_table3365
+ GCC_except_table3366
+ GCC_except_table3422
+ GCC_except_table3482
+ GCC_except_table3619
+ GCC_except_table3692
+ GCC_except_table3711
+ GCC_except_table3730
+ GCC_except_table3846
+ GCC_except_table3877
+ GCC_except_table3914
+ GCC_except_table3916
+ GCC_except_table3949
+ GCC_except_table3951
+ GCC_except_table3965
+ GCC_except_table3987
+ GCC_except_table3988
+ GCC_except_table401
+ GCC_except_table4014
+ GCC_except_table4019
+ GCC_except_table4040
+ GCC_except_table4049
+ GCC_except_table4074
+ GCC_except_table4082
+ GCC_except_table4084
+ GCC_except_table4100
+ GCC_except_table4114
+ GCC_except_table4153
+ GCC_except_table4171
+ GCC_except_table4177
+ GCC_except_table4189
+ GCC_except_table4211
+ GCC_except_table4218
+ GCC_except_table4356
+ GCC_except_table446
+ GCC_except_table4472
+ GCC_except_table458
+ GCC_except_table4661
+ GCC_except_table4664
+ GCC_except_table4665
+ GCC_except_table4687
+ GCC_except_table4721
+ GCC_except_table4728
+ GCC_except_table4737
+ GCC_except_table4741
+ GCC_except_table4743
+ GCC_except_table4749
+ GCC_except_table4750
+ GCC_except_table4753
+ GCC_except_table4759
+ GCC_except_table4775
+ GCC_except_table4807
+ GCC_except_table4876
+ GCC_except_table4934
+ GCC_except_table494
+ GCC_except_table504
+ GCC_except_table5047
+ GCC_except_table5074
+ GCC_except_table5099
+ GCC_except_table5101
+ GCC_except_table5106
+ GCC_except_table515
+ GCC_except_table5273
+ GCC_except_table5401
+ GCC_except_table5496
+ GCC_except_table552
+ GCC_except_table5592
+ GCC_except_table5620
+ GCC_except_table5665
+ GCC_except_table5684
+ GCC_except_table5790
+ GCC_except_table5796
+ GCC_except_table5811
+ GCC_except_table5827
+ GCC_except_table5848
+ GCC_except_table5860
+ GCC_except_table5877
+ GCC_except_table590
+ GCC_except_table602
+ GCC_except_table604
+ GCC_except_table614
+ GCC_except_table620
+ GCC_except_table651
+ GCC_except_table658
+ GCC_except_table759
+ GCC_except_table761
+ GCC_except_table762
+ GCC_except_table768
+ GCC_except_table770
+ GCC_except_table771
+ GCC_except_table773
+ GCC_except_table801
+ GCC_except_table815
+ GCC_except_table837
+ GCC_except_table910
+ _AXAIWhiteGloveLoggingEnabled
+ _AXKeyboardConsideredShown
+ _OBJC_CLASS_$_UIPlatformGlassInteractionViewAccessibility
+ _OBJC_CLASS_$__UIModernBarButtonAccessibility
+ _OBJC_CLASS_$___UIPlatformGlassInteractionViewAccessibility_super
+ _OBJC_CLASS_$____UIModernBarButtonAccessibility_super
+ _OBJC_METACLASS_$_UIPlatformGlassInteractionViewAccessibility
+ _OBJC_METACLASS_$__UIModernBarButtonAccessibility
+ _OBJC_METACLASS_$___UIPlatformGlassInteractionViewAccessibility_super
+ _OBJC_METACLASS_$____UIModernBarButtonAccessibility_super
+ _UIAccessibilityAutoCorrectCandidate
+ __AXContextMenuDismissStartPostCountStorage
+ __OBJC_$_CLASS_METHODS_UIPlatformGlassInteractionViewAccessibility(SafeCategory)
+ __OBJC_$_CLASS_METHODS__UIModernBarButtonAccessibility(SafeCategory)
+ __OBJC_$_INSTANCE_METHODS_UIPlatformGlassInteractionViewAccessibility
+ __OBJC_$_INSTANCE_METHODS__UIModernBarButtonAccessibility
+ __OBJC_CLASS_RO_$_UIPlatformGlassInteractionViewAccessibility
+ __OBJC_CLASS_RO_$__UIModernBarButtonAccessibility
+ __OBJC_CLASS_RO_$___UIPlatformGlassInteractionViewAccessibility_super
+ __OBJC_CLASS_RO_$____UIModernBarButtonAccessibility_super
+ __OBJC_METACLASS_RO_$_UIPlatformGlassInteractionViewAccessibility
+ __OBJC_METACLASS_RO_$__UIModernBarButtonAccessibility
+ __OBJC_METACLASS_RO_$___UIPlatformGlassInteractionViewAccessibility_super
+ __OBJC_METACLASS_RO_$____UIModernBarButtonAccessibility_super
+ __UIAccessibilityElementBearingScreenChangePostCount
+ ___47-[UISegmentAccessibility accessibilityActivate]_block_invoke
+ ___76-[_UIContextMenuUIControllerAccessibility contextMenuView:didSelectElement:]_block_invoke
+ ___os_log_helper_16_0_3_8_0_8_0_8_0
+ ___os_log_helper_16_2_4_8_0_8_66_8_66_8_66
+ ___os_log_helper_16_3_4_8_0_8_66_8_66_8_65
+ __collectAccessibleDescendantFrames
+ _kAXAppRestrictionsPreflightWorkspaceIdentifier
+ _objc_msgSend$setSelectedSegmentIndex:
+ _objc_msgSend$voiceOverOptions
+ _objc_release_x27
- -[UITextViewAccessibility _axShouldExposeLinksForCommandClient]
- GCC_except_table1105
- GCC_except_table1112
- GCC_except_table1113
- GCC_except_table1152
- GCC_except_table1197
- GCC_except_table1225
- GCC_except_table1240
- GCC_except_table1274
- GCC_except_table1304
- GCC_except_table1317
- GCC_except_table1330
- GCC_except_table1346
- GCC_except_table1348
- GCC_except_table1359
- GCC_except_table1496
- GCC_except_table1516
- GCC_except_table1518
- GCC_except_table1532
- GCC_except_table1559
- GCC_except_table1562
- GCC_except_table1565
- GCC_except_table1586
- GCC_except_table1635
- GCC_except_table1664
- GCC_except_table1665
- GCC_except_table1760
- GCC_except_table1771
- GCC_except_table1782
- GCC_except_table1783
- GCC_except_table1790
- GCC_except_table1792
- GCC_except_table1799
- GCC_except_table1821
- GCC_except_table1850
- GCC_except_table1853
- GCC_except_table1902
- GCC_except_table1908
- GCC_except_table1928
- GCC_except_table1941
- GCC_except_table1951
- GCC_except_table1997
- GCC_except_table2091
- GCC_except_table2094
- GCC_except_table2142
- GCC_except_table2164
- GCC_except_table2248
- GCC_except_table2271
- GCC_except_table2276
- GCC_except_table2284
- GCC_except_table2303
- GCC_except_table2320
- GCC_except_table2375
- GCC_except_table2402
- GCC_except_table2412
- GCC_except_table2419
- GCC_except_table2435
- GCC_except_table2453
- GCC_except_table2546
- GCC_except_table257
- GCC_except_table2630
- GCC_except_table2686
- GCC_except_table2754
- GCC_except_table2758
- GCC_except_table2776
- GCC_except_table2795
- GCC_except_table2912
- GCC_except_table2945
- GCC_except_table2996
- GCC_except_table3019
- GCC_except_table3071
- GCC_except_table3155
- GCC_except_table3161
- GCC_except_table3214
- GCC_except_table3227
- GCC_except_table3350
- GCC_except_table3351
- GCC_except_table3407
- GCC_except_table3467
- GCC_except_table3604
- GCC_except_table3677
- GCC_except_table3696
- GCC_except_table3715
- GCC_except_table3831
- GCC_except_table3862
- GCC_except_table3899
- GCC_except_table3901
- GCC_except_table3934
- GCC_except_table3936
- GCC_except_table3950
- GCC_except_table3958
- GCC_except_table397
- GCC_except_table3972
- GCC_except_table3999
- GCC_except_table4004
- GCC_except_table4025
- GCC_except_table4034
- GCC_except_table4054
- GCC_except_table4059
- GCC_except_table4067
- GCC_except_table4085
- GCC_except_table4099
- GCC_except_table4138
- GCC_except_table4156
- GCC_except_table4162
- GCC_except_table4174
- GCC_except_table4196
- GCC_except_table4203
- GCC_except_table4341
- GCC_except_table442
- GCC_except_table4457
- GCC_except_table454
- GCC_except_table4646
- GCC_except_table4649
- GCC_except_table4650
- GCC_except_table4672
- GCC_except_table4701
- GCC_except_table4706
- GCC_except_table4711
- GCC_except_table4720
- GCC_except_table4724
- GCC_except_table4725
- GCC_except_table4732
- GCC_except_table4733
- GCC_except_table4736
- GCC_except_table4758
- GCC_except_table4773
- GCC_except_table4860
- GCC_except_table490
- GCC_except_table4918
- GCC_except_table500
- GCC_except_table5031
- GCC_except_table5042
- GCC_except_table5083
- GCC_except_table5085
- GCC_except_table5090
- GCC_except_table511
- GCC_except_table5257
- GCC_except_table5381
- GCC_except_table5476
- GCC_except_table548
- GCC_except_table5572
- GCC_except_table5600
- GCC_except_table5645
- GCC_except_table5664
- GCC_except_table5770
- GCC_except_table5776
- GCC_except_table5791
- GCC_except_table5807
- GCC_except_table5828
- GCC_except_table5840
- GCC_except_table5857
- GCC_except_table586
- GCC_except_table598
- GCC_except_table600
- GCC_except_table606
- GCC_except_table616
- GCC_except_table647
- GCC_except_table654
- GCC_except_table755
- GCC_except_table757
- GCC_except_table758
- GCC_except_table760
- GCC_except_table766
- GCC_except_table767
- GCC_except_table769
- GCC_except_table797
- GCC_except_table811
- GCC_except_table833
- GCC_except_table906
- _objc_msgSend$_accessibilityGetContextID
CStrings:
+ "AXRemoteElement"
+ "FloatingBarItemsFrame-%p"
+ "UIPlatformGlassInteractionViewAccessibility"
+ "_TtC5UIKitP33_F83AB3ECBB2C378B4FCEB681A4D7DB7430UIPlatformGlassInteractionView"
+ "_UIModernBarButtonAccessibility"
+ "_isBackgroundSuppressed"
+ "com.apple.apprestrictions.preflight"
+ "rdar://166368898 UIKeyboardDockView supplementaryFooterViews count=%lu rightDockItemClass=%{public}@ firstFooterClass=%{public}@ firstFooterLabel=%{private}@"
+ "rdar://166368898 UIKeyboardDockView supplementaryHeaderViews count=%lu leftDockItemClass=%{public}@ firstHeaderClass=%{public}@ firstHeaderLabel=%{private}@"
+ "rdar://166368898 UIKeyboardLayoutStar iOSGetOrderedRows result orderedRowsCount=%lu sortedRowsCount=%lu inputKeyboardRowCount=%ld"
+ "rdar://166368898 UIKeyboardLayoutStar sortedUnstoredKeys count=%lu firstKeyName=%{public}@ lastKeyName=%{public}@ keyplaneName=%{public}@"
+ "traitCollection"
```
