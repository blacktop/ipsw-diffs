## PhotoLibraryFramework

> `/System/Library/AccessibilityBundles/PhotoLibraryFramework.axbundle/PhotoLibraryFramework`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0x4b90
-  __TEXT.__auth_stubs: 0x370
+3005.16.0.0.0
+  __TEXT.__text: 0x4efc
+  __TEXT.__auth_stubs: 0x350
   __TEXT.__objc_methlist: 0x908
-  __TEXT.__cstring: 0xe51
+  __TEXT.__cstring: 0xe90
   __TEXT.__const: 0x8
   __TEXT.__unwind_info: 0x238
   __TEXT.__objc_classname: 0x7b1

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x488
   __DATA_CONST.__objc_superrefs: 0x78
-  __AUTH_CONST.__auth_got: 0x1c0
+  __AUTH_CONST.__auth_got: 0x1b0
   __AUTH_CONST.__const: 0x120
   __AUTH_CONST.__cfstring: 0x13e0
   __AUTH_CONST.__objc_const: 0x1b60

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: DB735331-83E6-387C-A705-66533936B9D8
+  UUID: A180F530-1337-3123-9451-2EC6431E2067
   Functions: 167
-  Symbols:   787
+  Symbols:   785
   CStrings:  569
 
Symbols:
+ _objc_retain_x21
+ _objc_retain_x22
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x3
Functions:
~ +[AXPhotoLibraryFrameworkGlue accessibilityInitializeBundle] : 208 -> 216
~ ___60+[AXPhotoLibraryFrameworkGlue accessibilityInitializeBundle]_block_invoke : 1148 -> 1152
~ ___60+[AXPhotoLibraryFrameworkGlue accessibilityInitializeBundle]_block_invoke_2 : 96 -> 100
~ ___60+[AXPhotoLibraryFrameworkGlue accessibilityInitializeBundle]_block_invoke_3 : 432 -> 440
~ ___60+[AXPhotoLibraryFrameworkGlue accessibilityInitializeBundle]_block_invoke_5 : 104 -> 108
~ ___60+[AXPhotoLibraryFrameworkGlue accessibilityInitializeBundle]_block_invoke_7 : 80 -> 84
~ ___60+[AXPhotoLibraryFrameworkGlue accessibilityInitializeBundle]_block_invoke_9 : 92 -> 96
~ -[PLImageAccessibilityElement delegate] : 204 -> 208
~ -[PLImageAccessibilityElement dataSource] : 124 -> 136
~ -[PLImageAccessibilityElement accessibilityFrame] : 192 -> 200
~ -[PLImageAccessibilityElement _albumPhotoIndex] : 284 -> 312
~ -[PLImageAccessibilityElement _axMainAssetURL] : 156 -> 168
~ -[PLImageAccessibilityElement _accessibilityPhotoDescription] : 156 -> 168
~ -[PLImageAccessibilityElement _accessibilityElementStoredUserLabel] : 104 -> 112
~ -[PLImageAccessibilityElement albumView] : 96 -> 104
~ -[PLImageAccessibilityElement accessibilityLabel] : 236 -> 252
~ -[PLImageAccessibilityElement accessibilityTraits] : 220 -> 232
~ +[MFComposeRecipientViewAccessibility__PhotoLibrary__MessageUI _accessibilityPerformValidations:] : 196 -> 204
~ -[MFComposeRecipientViewAccessibility__PhotoLibrary__MessageUI _accessibilityLoadAccessibilityInformation] : 180 -> 192
~ -[PLCropOverlayAccessibility _accessibilityHitTest:withEvent:] : 364 -> 376
~ +[PLCropOverlayBottomBarAccessibility _accessibilityPerformValidations:] : 224 -> 232
~ -[PLCropOverlayBottomBarAccessibility _axUpdatePlayPauseButtonWithImage] : 172 -> 184
~ -[UIImage(UIAXNormalizedImage) normalizedImageWithScale:] : 184 -> 188
~ -[PLExpandableImageViewAccessibility _axMainAssetURL] : 128 -> 140
~ -[PLExpandableImageViewAccessibility _axExifLabel] : 76 -> 84
~ -[PLExpandableImageViewAccessibility _accessibilityElementStoredUserLabel] : 88 -> 92
~ -[PLExpandableImageViewAccessibility _accessibilityHitTest:withEvent:] : 620 -> 636
~ -[PLExpandableImageViewAccessibility _axSourceObject] : 140 -> 152
~ -[PLExpandableImageViewAccessibility accessibilityValue] : 76 -> 84
~ -[PLExpandableImageViewAccessibility accessibilityLabel] : 76 -> 84
~ -[PLExpandableImageViewAccessibility accessibilityTraits] : 56 -> 60
~ +[PLHighFidelityVideoOverlayButtonAccessibility _accessibilityPerformValidations:] : 172 -> 180
~ -[PLHighFidelityVideoOverlayButtonAccessibility _accessibilityLoadAccessibilityInformation] : 104 -> 108
~ -[PLIndexTitleViewAccessibility accessibilityLabel] : 204 -> 216
~ -[PLPhotoSmilesCommentCellAccessibility accessibilityLabel] : 84 -> 92
~ -[PLPhotoSmilesCommentCellAccessibility accessibilityActivationPoint] : 80 -> 84
~ -[PLPhotoTileViewControllerAccessibility _setPhoto:] : 172 -> 180
~ -[PLPhotoTileViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 216 -> 220
~ ___84-[PLPhotoTileViewControllerAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke : 92 -> 96
~ -[PLProgressViewAccessibility isAccessibilityElement] : 68 -> 72
~ -[PLProgressViewAccessibility accessibilityLabel] : 84 -> 92
~ -[PLProgressViewAccessibility _axUpdateValueBasedOnPercentComplete:] : 176 -> 184
~ -[PLProgressViewAccessibility setPercentComplete:] : 188 -> 196
~ -[PLProgressViewAccessibility _accessibilityLoadAccessibilityInformation] : 108 -> 112
~ -[PLUIAccessibilityMockSlider setView:] : 148 -> 152
~ -[PLUIAccessibilityMockSlider accessibilityFrame] : 168 -> 172
~ -[UITableViewCellAccessibility__PhotoLibrary__UIKit _accessibilityIgnoreInternalLabels] : 64 -> 68
~ -[UITextFieldAccessibility__PhotoLibrary__UIKit accessibilityPlaceholderValue] : 244 -> 264
~ +[PLVideoEditingOverlayViewAccessibility _accessibilityPerformValidations:] : 124 -> 132
~ -[PLVideoEditingOverlayViewAccessibility accessibilityLabel] : 188 -> 208
~ +[PLVideoViewAccessibility _accessibilityPerformValidations:] : 224 -> 232
~ -[PLVideoViewAccessibility _showVideoOverlay] : 216 -> 228
~ -[PLVideoViewAccessibility _videoOverlayFadeOutDidFinish] : 144 -> 148
~ -[PLVideoViewAccessibility viewDidDisappear] : 164 -> 172
~ -[PLVideoViewAccessibility _createScrubberIfNeeded] : 164 -> 172
~ -[PLVideoViewAccessibility isAccessibilityElement] : 156 -> 168
~ -[PLVideoViewAccessibility accessibilityLabel] : 84 -> 92
~ -[PLVideoViewAccessibility accessibilityElements] : 432 -> 460
~ -[PLVideoViewAccessibility _accessibilityLoadAccessibilityInformation] : 132 -> 140
~ -[PLVideoViewAccessibility accessibilityURL] : 192 -> 204
~ -[PLVideoViewAccessibility _accessibilityElementStoredUserLabel] : 76 -> 84
~ _accessibilityLocalizedStringFromBundleWithTable : 120 -> 128
~ _accessibilityLocalizedString : 176 -> 184
~ -[UINavigationButtonAccessibility__PhotoLibrary__UIKit accessibilityLabel] : 248 -> 260
~ -[UIToolbarButtonAccessibility__PhotoLibrary__UIKit isAccessibilityElement] : 120 -> 132
~ -[UIToolbarButtonAccessibility__PhotoLibrary__UIKit accessibilityLabel] : 192 -> 212
~ +[PLSlalomRegionEditorAccessibility _accessibilityPerformValidations:] : 380 -> 388
~ -[PLSlalomRegionEditorAccessibility setStartValue:notify:] : 336 -> 364
~ __createFormatDurationString : 368 -> 380
~ -[PLSlalomRegionEditorAccessibility setEndValue:notify:] : 336 -> 364
~ -[PLSlalomRegionEditorAccessibility continueTrackingWithTouch:withEvent:] : 488 -> 524
~ -[PLSlalomRegionEditorAccessibility layoutSubviews] : 456 -> 480
~ -[PLSlalomRegionEditorAccessibility accessibilityElements] : 776 -> 828
~ -[PLSlalomRegionEditorAccessibility _accessibilitySliderDeltaForFrame:] : 160 -> 172
~ -[PLSlalomRegionEditorAccessibility _accessibilityIncrementMockSlider:largeStep:] : 628 -> 664
~ -[PLSlalomRegionEditorAccessibility _accessibilityDecrementMockSlider:largeStep:] : 628 -> 664
CStrings:
+ "/Library/Caches/com.apple.xbs/D796EB7F-4AEA-4A12-AB49-AB256E569E81/TemporaryDirectory.1bWS40/Sources/AccessibilityBundles/PhotoLibraryAccessibility/Accessibility/PLAlbumViewCellAccessibility.m"
- "/Library/Caches/com.apple.xbs/Sources/AccessibilityBundles/PhotoLibraryAccessibility/Accessibility/PLAlbumViewCellAccessibility.m"

```
