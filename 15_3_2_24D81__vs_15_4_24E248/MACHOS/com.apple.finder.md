## com.apple.finder

> `/System/Library/Accessibility/BundlesBase/com.apple.finder.axbundle/Versions/A/com.apple.finder`

```diff

-287.6.0.0.0
-  __TEXT.__text: 0x823c
-  __TEXT.__auth_stubs: 0x340
+287.6.4.0.0
+  __TEXT.__text: 0x8344
+  __TEXT.__auth_stubs: 0x330
   __TEXT.__objc_stubs: 0x15a0
   __TEXT.__objc_methlist: 0xcf4
   __TEXT.__objc_classname: 0xa7d

   __TEXT.__gcc_except_tab: 0x80
   __TEXT.__oslogstring: 0x71
   __TEXT.__unwind_info: 0x300
-  __DATA_CONST.__auth_got: 0x1b0
+  __DATA_CONST.__auth_got: 0x1a8
   __DATA_CONST.__got: 0x1d8
   __DATA_CONST.__const: 0x438
   __DATA_CONST.__cfstring: 0x1e80

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A8696525-96E0-3039-8023-9902CCB0C1DA
-  Functions: 253
-  Symbols:   953
+  UUID: 4692C25F-2C6D-3F5C-817A-2CE56E1A6111
+  Functions: 256
+  Symbols:   956
   CStrings:  819
 
Symbols:
+ +[TDesktopWidgetViewAccessibility _accessibilitySharedDispatchQueue].cold.1
+ -[TApplicationAccessibility _axFontSizeForCategory:].cold.1
+ __59+[AXFinderGlue accessibilityPrincipalClassInitializeBundle]_block_invoke_3.cold.1
+ accessibilityIsThingamajigEnabled.cold.1
- _fmod
Functions:
~ -[TGoToResultTableCellViewAccessibility prepareForReuse] : 196 -> 200
~ -[TGoToResultTableCellViewAccessibility setObjectValue:] : 516 -> 524
~ -[TContextMenuItemAccessibility accessibilityAttributeValue:] : 280 -> 284
~ -[TTouchBarAddTagsViewControllerAccessibility updateTag:button:tags:] : 276 -> 280
~ -[TListViewControllerAccessibility iconSize] : 200 -> 220
~ -[TTaggingSuggestionsViewControllerAccessibility configureView] : 228 -> 232
~ -[TIconViewAccessibility setTitleFont:] : 280 -> 284
~ -[TDesktopMultiWindowControllerAccessibility accessibilitySetValue:forAttribute:] : 372 -> 376
~ -[TListHeaderRowViewAccessibility performLayout] : 408 -> 412
~ -[TReturnToSenderPillViewAccessibility accessibilityTitle] : 196 -> 200
~ +[TDesktopWidgetViewAccessibility _accessibilitySharedDispatchQueue] : 84 -> 68
~ -[TDesktopWidgetViewAccessibility _accessibilityFetchWidgetElement] : 408 -> 404
~ ___67-[TDesktopWidgetViewAccessibility _accessibilityFetchWidgetElement]_block_invoke : 616 -> 620
~ -[TDesktopWidgetViewAccessibility _accessibilityNotificationCenterProcess] : 360 -> 364
~ -[TIconCollectionViewControllerAccessibility loadView] : 504 -> 516
~ -[TNodeViewSettingsAccessibility axUpdateViewSettingsToCurrentFontSize] : 856 -> 868
~ __71-[TNodeViewSettingsAccessibility axUpdateViewSettingsToCurrentFontSize]_block_invoke.331 : 140 -> 148
~ +[TNodeViewSettingsAccessibility textSizeFromSettings:] : 232 -> 236
~ -[TTitleViewBadgeAccessibility accessibilityTitle] : 140 -> 144
~ -[TColumnViewControllerAccessibility loadView] : 504 -> 516
~ -[TColumnViewControllerAccessibility calculateIconSize] : 136 -> 148
~ -[TGoToWindowAccessibility _accessibilityLoadAccessibilityInformation] : 428 -> 432
~ -[TSidebarItemCellAccessibility _accessibilityLoadAccessibilityInformation] : 980 -> 988
~ ___59+[AXFinderGlue accessibilityPrincipalClassInitializeBundle]_block_invoke_3 : 844 -> 832
~ _accessibilityIsThingamajigEnabled : 68 -> 56
~ +[TApplicationAccessibility axApplication] : 152 -> 156
~ -[TApplicationAccessibility _axFontSizeForCategory:] : 148 -> 132
~ -[TApplicationAccessibility _axUpdateOpenViewsToCurrentFontSize] : 828 -> 840
~ -[TApplicationAccessibility accessibilitySetValue:forAttribute:] : 256 -> 260
~ -[TIconViewSettingsAccessibility setTextSize:] : 372 -> 376
~ -[TIconViewSettingsAccessibility textSize] : 240 -> 244
~ -[TDesktopViewControllerAccessibility accessibilityAttributeValue:] : 576 -> 584
~ -[TListViewAccessibility accessibilityPerformAction:] : 816 -> 824
~ -[TColumnViewAccessibility accessibilityFrame] : 280 -> 284
~ -[TGalleryCollectionViewControllerAccessibility loadView] : 528 -> 540
~ -[TGalleryCollectionViewControllerAccessibility iconSize] : 220 -> 240
~ -[TBrowserContainerControllerAccessibility nodeViewSettings] : 180 -> 184
~ -[TBrowserContainerControllerAccessibility _axcBrowserWindow] : 464 -> 472
~ -[TBrowserContainerControllerAccessibility _axcSidebarView] : 304 -> 312
~ -[TDesktopMultiViewControllerAccessibility rotor:resultForSearchParameters:] : 828 -> 832
~ -[TListViewSettingsAccessibility setTextSize:] : 372 -> 376
~ -[TListViewSettingsAccessibility textSize] : 240 -> 244
~ -[TListHeaderCellViewAccessibility accessibilityLabel] : 508 -> 516
~ -[TListHeaderCellViewAccessibility _axcSelfAsTableCell] : 108 -> 112
~ -[TSplitViewAccessibility accessibilityChildrenInNavigationOrder] : 528 -> 524

```
