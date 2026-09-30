## Restaurants-Assistant

> `/System/Library/AccessibilityBundles/Restaurants-Assistant.axbundle/Restaurants-Assistant`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0x11b8
-  __TEXT.__auth_stubs: 0x220
+3005.16.0.0.0
+  __TEXT.__text: 0x12b8
+  __TEXT.__auth_stubs: 0x1f0
   __TEXT.__objc_methlist: 0x16c
   __TEXT.__cstring: 0x429
   __TEXT.__const: 0x20

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x128
   __DATA_CONST.__objc_superrefs: 0x18
-  __AUTH_CONST.__auth_got: 0x120
+  __AUTH_CONST.__auth_got: 0x108
   __AUTH_CONST.__const: 0xc0
   __AUTH_CONST.__cfstring: 0x4e0
   __AUTH_CONST.__objc_const: 0x630

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2DA7E327-C16E-3C3A-9250-A73724A6D74D
+  UUID: 45786548-BC7C-36D0-8435-F6B0DD15A278
   Functions: 33
-  Symbols:   215
+  Symbols:   212
   CStrings:  143
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x8
Functions:
~ _restaurantAccessibilityLocalizedString : 176 -> 184
~ ___59+[AXRestaurantsAssistantGlue accessibilityInitializeBundle]_block_invoke : 100 -> 104
~ ___59+[AXRestaurantsAssistantGlue accessibilityInitializeBundle]_block_invoke_2 : 380 -> 384
~ ___59+[AXRestaurantsAssistantGlue accessibilityInitializeBundle]_block_invoke_3 : 84 -> 88
~ ___59+[AXRestaurantsAssistantGlue accessibilityInitializeBundle]_block_invoke_4 : 152 -> 160
~ -[SiriRestaurantsDetailDescriptionCellAccessibility _setPriceInfoWithRestaurant:] : 540 -> 568
~ -[SiriRestaurantsDetailViewControllerAccessibility _configurePhoneCell:forItem:] : 184 -> 196
~ -[SiriRestaurantsDetailViewControllerAccessibility _configureURLCell:forItem:] : 184 -> 196
~ -[SiriRestaurantsDetailViewControllerAccessibility _configureReviewsCell:forItem:] : 268 -> 292
~ +[SiriRestaurantsListItemCellAccessibility _accessibilityPerformValidations:] : 272 -> 280
~ -[SiriRestaurantsListItemCellAccessibility accessibilityLabel] : 804 -> 880
~ -[SiriRestaurantsOpenHoursCellAccessibility configureWithParsedOpenHoursInfo:] : 280 -> 288
~ ___78-[SiriRestaurantsOpenHoursCellAccessibility configureWithParsedOpenHoursInfo:]_block_invoke_2 : 356 -> 392
~ +[SiriRestaurantsLogoButtonAccessibility _accessibilityPerformValidations:] : 128 -> 140
~ -[SiriRestaurantsLogoButtonAccessibility accessibilityLabel] : 160 -> 172

```
