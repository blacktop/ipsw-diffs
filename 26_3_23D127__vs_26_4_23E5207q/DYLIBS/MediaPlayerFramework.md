## MediaPlayerFramework

> `/System/Library/AccessibilityBundles/MediaPlayerFramework.axbundle/MediaPlayerFramework`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0x3028
-  __TEXT.__auth_stubs: 0x2e0
+3005.16.0.0.0
+  __TEXT.__text: 0x3240
+  __TEXT.__auth_stubs: 0x2c0
   __TEXT.__objc_methlist: 0x5f4
   __TEXT.__cstring: 0xb54
   __TEXT.__const: 0x18

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x398
   __DATA_CONST.__objc_superrefs: 0x60
-  __AUTH_CONST.__auth_got: 0x180
+  __AUTH_CONST.__auth_got: 0x170
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x1080
   __AUTH_CONST.__objc_const: 0x1290

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: FB670CB7-FE9C-3866-A7B8-E2B1E1D7E454
+  UUID: E5C0FBAD-A137-3213-9493-3615AAB56789
   Functions: 113
-  Symbols:   572
+  Symbols:   570
   CStrings:  442
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
+ _objc_retain_x20
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x3
- _objc_retain_x8
Functions:
~ +[AXMediaPlayerFrameworkGlue accessibilityInitializeBundle] : 148 -> 152
~ ___59+[AXMediaPlayerFrameworkGlue accessibilityInitializeBundle]_block_invoke : 424 -> 428
~ ___59+[AXMediaPlayerFrameworkGlue accessibilityInitializeBundle]_block_invoke_2 : 84 -> 88
~ ___59+[AXMediaPlayerFrameworkGlue accessibilityInitializeBundle]_block_invoke_3 : 332 -> 340
~ _accessibilityMPLocalizedString : 176 -> 184
~ +[MPAVRoutingControllerAccessibility _iconImageForRoute:] : 152 -> 160
~ +[MPAVRoutingSheetAccessibility _accessibilityPerformValidations:] : 196 -> 204
~ -[MPAVRoutingSheetAccessibility _accessibilityLoadAccessibilityInformation] : 140 -> 148
~ +[MPAVRoutingTableViewCellAccessibility _accessibilityPerformValidations:] : 332 -> 340
~ -[MPAVRoutingTableViewCellAccessibility _axIsVolumeSliderVisible] : 80 -> 84
~ -[MPAVRoutingTableViewCellAccessibility accessibilityActivationPoint] : 208 -> 216
~ -[MPAVRoutingTableViewCellAccessibility accessibilityLabel] : 244 -> 264
~ -[MPAVRoutingTableViewCellAccessibility accessibilityValue] : 564 -> 584
~ ___59-[MPAVRoutingTableViewCellAccessibility accessibilityValue]_block_invoke : 836 -> 952
~ -[MPAVRoutingTableViewCellAccessibility updateForEndpoint:routeItem:inferLocalizedModelName:] : 180 -> 184
~ +[MPAddKeepLocalControlAccessibility _accessibilityPerformValidations:] : 148 -> 156
~ -[MPAddKeepLocalControlAccessibility isAccessibilityElement] : 108 -> 116
~ -[MPAddKeepLocalControlAccessibility _accessibilityLabelForStatusType:] : 100 -> 104
~ -[MPAddKeepLocalControlAccessibility _accessibilityValueForStatusType:andDownloadProgress:] : 204 -> 220
~ -[MPAddKeepLocalControlAccessibility _accessibilityCustomActionLabelForControlStatus:] : 88 -> 92
~ -[MPAddKeepLocalControlAccessibility setControlStatus:animated:] : 108 -> 112
~ +[MPDetailSliderAccessibility _accessibilityPerformValidations:] : 224 -> 236
~ -[MPDetailSliderAccessibility _accessibilityLoadAccessibilityInformation] : 264 -> 280
~ -[MPDetailSliderAccessibility _accessibilityCommitPositionChange] : 232 -> 240
~ -[MPDetailSliderAccessibility accessibilityIncrement] : 292 -> 300
~ -[MPDetailSliderAccessibility accessibilityDecrement] : 292 -> 300
~ -[MPDetailSliderAccessibility _axPostUpdate] : 92 -> 96
~ -[MPDetailSliderAccessibility continueTrackingWithTouch:withEvent:] : 216 -> 220
~ -[MPDetailSliderAccessibility accessibilityValue] : 584 -> 608
~ -[MPRouteButtonAccessibility accessibilityValue] : 84 -> 92
~ -[MPRouteLabelAccessibility isAccessibilityElement] : 124 -> 128
~ -[MPRouteLabelAccessibility accessibilityLabel] : 124 -> 136
~ +[MPVolumeSliderAccessibility _accessibilityPerformValidations:] : 196 -> 204
~ -[MPVolumeSliderAccessibility accessibilityLabel] : 100 -> 112
~ -[MPVolumeSliderAccessibility accessibilityIncrement] : 184 -> 192
~ -[MPVolumeSliderAccessibility accessibilityDecrement] : 184 -> 192
~ -[MPVolumeSliderAccessibility _accessibilityHitTest:withEvent:] : 168 -> 172
~ -[MPVolumeSliderAccessibility _layoutVolumeWarningView] : 704 -> 748
~ -[MPVolumeViewAccessibility _createSubviews] : 132 -> 140
~ _AXLabelForMediaRoute : 320 -> 328
~ _accessibilityLocalizedString : 156 -> 164
~ -[UINavigationButtonAccessibility__MediaPlayer__UIKit accessibilityLabel] : 148 -> 160
~ -[UINavigationButtonAccessibility__MediaPlayer__UIKit accessibilityValue] : 300 -> 320
~ -[UITableViewCellAccessibility__MediaPlayer__UIKit accessibilityTraits] : 428 -> 436
~ ___71-[UITableViewCellAccessibility__MediaPlayer__UIKit accessibilityTraits]_block_invoke : 80 -> 84

```
