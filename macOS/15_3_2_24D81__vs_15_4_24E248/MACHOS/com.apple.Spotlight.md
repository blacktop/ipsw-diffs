## com.apple.Spotlight

> `/System/Library/Accessibility/BundlesBase/com.apple.Spotlight.axbundle/Versions/A/com.apple.Spotlight`

```diff

-287.6.0.0.0
-  __TEXT.__text: 0x12c0
+287.6.4.0.0
+  __TEXT.__text: 0x12f8
   __TEXT.__auth_stubs: 0x100
   __TEXT.__objc_stubs: 0x400
   __TEXT.__objc_methlist: 0x1ec

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8572C96C-7835-3906-ACAB-1FF0BB0194B5
+  UUID: 37D2794F-B681-3AC3-8FFB-6088CFE0B474
   Functions: 38
   Symbols:   181
   CStrings:  165
Functions:
~ -[SearchFieldCellAccessibility accessibilityFrame] : 300 -> 308
~ -[SearchFieldCellAccessibility accessibilitySharedFocusElements] : 292 -> 296
~ -[SPSpotlightPanelAccessibility accessibilityPerformCancel] : 352 -> 360
~ -[SearchViewControllerAccessibility expandWindow] : 180 -> 184
~ +[SPAppDelegateAccessibility accessibilitySetupExistingObjects] : 316 -> 320
~ -[SPAppDelegateAccessibility _axbSearchResultCollectionView] : 272 -> 280
~ -[SPAppDelegateAccessibility _axbResultsViewDidChange] : 224 -> 228
~ -[SPResultWithoutSubitemsHelperAccessibility setupForObject:appIsScreenTimeRestricted:] : 536 -> 552

```
