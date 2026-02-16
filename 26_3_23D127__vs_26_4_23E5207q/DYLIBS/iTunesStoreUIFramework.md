## iTunesStoreUIFramework

> `/System/Library/AccessibilityBundles/iTunesStoreUIFramework.axbundle/iTunesStoreUIFramework`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0x40c0
-  __TEXT.__auth_stubs: 0x320
+3005.16.0.0.0
+  __TEXT.__text: 0x4394
+  __TEXT.__auth_stubs: 0x2f0
   __TEXT.__objc_methlist: 0xa44
   __TEXT.__cstring: 0x119f
   __TEXT.__const: 0x10

   __DATA_CONST.__objc_selrefs: 0x398
   __DATA_CONST.__objc_superrefs: 0xa0
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__auth_got: 0x198
+  __AUTH_CONST.__auth_got: 0x180
   __AUTH_CONST.__const: 0x120
   __AUTH_CONST.__cfstring: 0x1820
   __AUTH_CONST.__objc_const: 0x2b90

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6083415C-B557-3AED-9D7C-EC9A540876D3
+  UUID: 08ABC0EC-BC84-323E-BF0A-71BF1508766F
   Functions: 170
-  Symbols:   906
+  Symbols:   903
   CStrings:  604
 
Symbols:
+ _objc_retain_x22
+ _objc_retain_x26
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x8
Functions:
~ +[AXiTunesStoreUIGlue accessibilityInitializeBundle] : 296 -> 304
~ ___52+[AXiTunesStoreUIGlue accessibilityInitializeBundle]_block_invoke : 2068 -> 2072
~ ___52+[AXiTunesStoreUIGlue accessibilityInitializeBundle]_block_invoke_2 : 84 -> 88
~ ___52+[AXiTunesStoreUIGlue accessibilityInitializeBundle]_block_invoke_3 : 732 -> 740
~ ___41+[AXiTunesStoreUIGlue _webKitInitialized]_block_invoke : 100 -> 104
~ ___41+[AXiTunesStoreUIGlue _webKitInitialized]_block_invoke_2 : 100 -> 104
~ ___41+[AXiTunesStoreUIGlue _webKitInitialized]_block_invoke_3 : 84 -> 88
~ ___41+[AXiTunesStoreUIGlue _webKitInitialized]_block_invoke_4 : 132 -> 140
~ -[SUApplicationAccessibility _accessibilityContentLanguage] : 104 -> 112
~ -[SUBannerCellAccessibility _reloadButtons] : 580 -> 624
~ -[SUBannerCellConfigurationAccessibility accessibilityTableViewCellText] : 140 -> 152
~ -[SUButtonCellConfigurationAccessibility accessibilityLabel] : 88 -> 104
~ -[SUCellConfigurationCacheAccessibility configurationForRow:] : 216 -> 220
~ -[SUCompletionCellConfigurationAccessibility accessibilityLabel] : 88 -> 104
~ -[SUItemCellConfigurationAccessibility _accessibilityVideoIconString] : 128 -> 136
~ -[SUItemOfferButtonAccessibility accessibilityLabel] : 240 -> 260
~ -[SULoadMoreCellConfigurationAccessibility accessibilityLabel] : 88 -> 104
~ -[SULoadMoreMediaCellConfigurationAccessibility accessibilityLabel] : 132 -> 140
~ -[SUMaskedViewAccessibility accessibilityElementsHidden] : 192 -> 196
~ -[SUNavigationButtonAccessibility accessibilityLabel] : 232 -> 248
~ -[SUReviewCellConfigurationAccessibility accessibilityLabel] : 284 -> 308
~ -[SUReviewsButtonAccessibility accessibilityLabel] : 252 -> 272
~ -[SUReviewsHeaderCellConfigurationAccessibility accessibilityLabel] : 280 -> 304
~ -[SUShortLinkCellConfigurationAccessibility accessibilityLabel] : 168 -> 172
~ -[SUStorePageViewControllerAccessibility reloadForSectionsWithGroup:] : 160 -> 168
~ -[SUStorePageViewControllerAccessibility _setActiveChildViewController:shouldTearDown:] : 196 -> 200
~ -[SUSubtitledButtonAccessibility accessibilityLabel] : 164 -> 176
~ -[SUTableCellAccessibility accessibilityTableViewCellText] : 84 -> 92
~ -[SUTableCellAccessibility accessibilityHint] : 84 -> 92
~ -[SUTableCellAccessibility accessibilityValue] : 84 -> 92
~ -[SUTableCellAccessibility accessibilityTraits] : 200 -> 208
~ -[SUTableCellAccessibility description] : 172 -> 184
~ +[SURedeemCameraViewControllerAccessibility _accessibilityPerformValidations:] : 128 -> 140
~ -[SURedeemCameraViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 132 -> 140
~ -[SUTableCellContentViewAccessibility accessibilityTraits] : 64 -> 68
~ -[SUTableCellContentViewAccessibility accessibilityHint] : 84 -> 92
~ -[SUTableCellContentViewAccessibility accessibilityLabel] : 84 -> 92
~ -[SUTableCellContentViewAccessibility accessibilityValue] : 84 -> 92
~ -[SUTableCellContentViewAccessibility description] : 128 -> 136
~ -[SUTableHeaderViewAccessibility accessibilityLabel] : 204 -> 216
~ -[SUTableViewAccessibility _accessibilityScrollStatus] : 200 -> 212
~ -[SUTallLinkCellConfigurationAccessibility accessibilityLabel] : 364 -> 384
~ -[SUTermsAndConditionsViewAccessibility _termsAndConditionsControl] : 144 -> 152
~ +[SUTextContentViewAccessibility _accessibilityPerformValidations:] : 156 -> 168
~ -[SUTextContentViewAccessibility _accessibilityPlaceholderValue:] : 324 -> 344
~ -[SUTextContentViewAccessibility _accessibilityLoadAccessibilityInformation] : 104 -> 108
~ -[SUTextContentViewAccessibility accessibilityValue] : 140 -> 152
~ -[SUTouchCaptureViewAccessibility _accessibilityHitTest:withEvent:] : 632 -> 652
~ -[SUTwoLineTrackCellConfigurationAccessibility accessibilityLabel] : 308 -> 316
~ -[SUUIScrollViewAccessibility setTopExtensionViewColor:] : 100 -> 104
~ -[SUUIWebDocumentViewAccessibility accessibilityScrollRightPage] : 600 -> 644
~ -[SUiBooksOverrideWebViewAccessibility _accessibilityIsScrollAncestor] : 224 -> 228
~ ___70-[SUiBooksOverrideWebViewAccessibility _accessibilityIsScrollAncestor]_block_invoke : 244 -> 264
~ -[SUWebViewAccessibility _accessibilitySUWebViewIsScrollAncestor] : 292 -> 308
~ -[SUWebViewAccessibility accessibilityScroll:] : 244 -> 256
~ -[SUWebViewAccessibility accessibilityPerformEscape] : 80 -> 84
~ -[SUWebViewAccessibility accessibilityScrollRightPage] : 532 -> 572
~ _accessibilityLocalizedString : 156 -> 164
~ _starStringForStarCount : 208 -> 220
~ ___69-[SUScriptNotificationObserverAccessibility _axActionOccurredForWeb:]_block_invoke : 264 -> 280
~ -[SUScriptNotificationObserverAccessibility dealloc] : 112 -> 116

```
