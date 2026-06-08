## PhotoLibraryFramework

> `/System/Library/AccessibilityBundles/PhotoLibraryFramework.axbundle/PhotoLibraryFramework`

```diff

-3005.28.0.0.0
-  __TEXT.__text: 0x4efc
-  __TEXT.__auth_stubs: 0x350
+3036.2.0.0.0
+  __TEXT.__text: 0x4c1c
   __TEXT.__objc_methlist: 0x908
-  __TEXT.__cstring: 0xe90
   __TEXT.__const: 0x8
-  __TEXT.__unwind_info: 0x238
-  __TEXT.__objc_classname: 0x7b1
-  __TEXT.__objc_methname: 0xd67
-  __TEXT.__objc_methtype: 0x172
-  __TEXT.__objc_stubs: 0xce0
-  __DATA_CONST.__got: 0xf0
+  __TEXT.__cstring: 0xe94
+  __TEXT.__unwind_info: 0x230
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0xa8
   __DATA_CONST.__objc_classlist: 0x178
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x488
   __DATA_CONST.__objc_superrefs: 0x78
-  __AUTH_CONST.__auth_got: 0x1b0
+  __DATA_CONST.__got: 0xf0
   __AUTH_CONST.__const: 0x120
   __AUTH_CONST.__cfstring: 0x13e0
   __AUTH_CONST.__objc_const: 0x1b60
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x1e0
   __DATA.__objc_ivar: 0xc
   __DATA.__bss: 0x8

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 992B2FFE-6080-36F0-8438-4FE430148596
+  UUID: 19B1AFE3-16C0-358D-88BF-3C1C472421A5
   Functions: 167
-  Symbols:   785
-  CStrings:  569
+  Symbols:   787
+  CStrings:  343
 
Symbols:
+ ___block_literal_global.701
+ ___block_literal_global.710
+ ___block_literal_global.772
+ ___block_literal_global.774
+ ___block_literal_global.776
+ ___block_literal_global.778
+ ___block_literal_global.784
+ ___block_literal_global.786
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x3
- ___block_literal_global.659
- ___block_literal_global.668
- ___block_literal_global.730
- ___block_literal_global.732
- ___block_literal_global.734
- ___block_literal_global.736
- ___block_literal_global.742
- ___block_literal_global.744
- _objc_retain_x21
- _objc_retain_x22
Functions:
~ +[AXPhotoLibraryFrameworkGlue accessibilityInitializeBundle] : 216 -> 208
~ ___60+[AXPhotoLibraryFrameworkGlue accessibilityInitializeBundle]_block_invoke : 1152 -> 1148
~ ___60+[AXPhotoLibraryFrameworkGlue accessibilityInitializeBundle]_block_invoke_2 : 100 -> 96
~ ___60+[AXPhotoLibraryFrameworkGlue accessibilityInitializeBundle]_block_invoke_3 : 440 -> 432
~ ___60+[AXPhotoLibraryFrameworkGlue accessibilityInitializeBundle]_block_invoke_5 : 108 -> 104
~ ___60+[AXPhotoLibraryFrameworkGlue accessibilityInitializeBundle]_block_invoke_7 : 84 -> 80
~ ___60+[AXPhotoLibraryFrameworkGlue accessibilityInitializeBundle]_block_invoke_9 : 96 -> 92
~ -[PLImageAccessibilityElement delegate] : 208 -> 204
~ -[PLImageAccessibilityElement dataSource] : 136 -> 124
~ -[PLImageAccessibilityElement accessibilityFrame] : 200 -> 192
~ -[PLImageAccessibilityElement _albumPhotoIndex] : 312 -> 284
~ -[PLImageAccessibilityElement _axMainAssetURL] : 168 -> 156
~ -[PLImageAccessibilityElement _accessibilityPhotoDescription] : 168 -> 156
~ -[PLImageAccessibilityElement _accessibilityElementStoredUserLabel] : 112 -> 104
~ -[PLImageAccessibilityElement albumView] : 104 -> 96
~ -[PLImageAccessibilityElement accessibilityLabel] : 252 -> 236
~ -[PLImageAccessibilityElement accessibilityTraits] : 232 -> 220
~ -[PLImageAccessibilityElement index] : 16 -> 20
~ -[PLImageAccessibilityElement setIndex:] : 16 -> 20
~ +[MFComposeRecipientViewAccessibility__PhotoLibrary__MessageUI _accessibilityPerformValidations:] : 204 -> 196
~ -[MFComposeRecipientViewAccessibility__PhotoLibrary__MessageUI _accessibilityLoadAccessibilityInformation] : 192 -> 180
~ -[PLCropOverlayAccessibility _accessibilityHitTest:withEvent:] : 376 -> 368
~ +[PLCropOverlayBottomBarAccessibility _accessibilityPerformValidations:] : 232 -> 224
~ -[PLCropOverlayBottomBarAccessibility _axUpdatePlayPauseButtonWithImage] : 184 -> 172
~ -[UIImage(UIAXNormalizedImage) normalizedImageWithScale:] : 188 -> 184
~ -[PLExpandableImageViewAccessibility _axMainAssetURL] : 140 -> 128
~ -[PLExpandableImageViewAccessibility _axExifLabel] : 84 -> 76
~ -[PLExpandableImageViewAccessibility _accessibilityElementStoredUserLabel] : 92 -> 88
~ -[PLExpandableImageViewAccessibility _accessibilityHitTest:withEvent:] : 636 -> 624
~ -[PLExpandableImageViewAccessibility _axSourceObject] : 152 -> 140
~ -[PLExpandableImageViewAccessibility accessibilityValue] : 84 -> 76
~ -[PLExpandableImageViewAccessibility accessibilityLabel] : 84 -> 76
~ -[PLExpandableImageViewAccessibility accessibilityTraits] : 60 -> 56
~ +[PLHighFidelityVideoOverlayButtonAccessibility _accessibilityPerformValidations:] : 180 -> 172
~ -[PLHighFidelityVideoOverlayButtonAccessibility _accessibilityLoadAccessibilityInformation] : 108 -> 104
~ -[PLIndexTitleViewAccessibility accessibilityLabel] : 216 -> 204
~ -[PLPhotoSmilesCommentCellAccessibility accessibilityLabel] : 92 -> 84
~ -[PLPhotoSmilesCommentCellAccessibility accessibilityActivationPoint] : 84 -> 80
~ -[PLPhotoTileViewControllerAccessibility _setPhoto:] : 180 -> 172
~ -[PLPhotoTileViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 220 -> 216
~ ___84-[PLPhotoTileViewControllerAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke : 96 -> 92
~ -[PLProgressViewAccessibility isAccessibilityElement] : 72 -> 68
~ -[PLProgressViewAccessibility accessibilityLabel] : 92 -> 84
~ -[PLProgressViewAccessibility _axUpdateValueBasedOnPercentComplete:] : 184 -> 176
~ -[PLProgressViewAccessibility setPercentComplete:] : 196 -> 188
~ -[PLProgressViewAccessibility _accessibilityLoadAccessibilityInformation] : 112 -> 108
~ -[PLUIAccessibilityMockSlider accessibilityTraits] : 176 -> 180
~ -[PLUIAccessibilityMockSlider view] : 16 -> 20
~ -[UITableViewCellAccessibility__PhotoLibrary__UIKit _accessibilityIgnoreInternalLabels] : 68 -> 64
~ -[UITextFieldAccessibility__PhotoLibrary__UIKit accessibilityPlaceholderValue] : 264 -> 244
~ +[PLVideoEditingOverlayViewAccessibility _accessibilityPerformValidations:] : 132 -> 124
~ -[PLVideoEditingOverlayViewAccessibility accessibilityLabel] : 208 -> 188
~ +[PLVideoViewAccessibility _accessibilityPerformValidations:] : 232 -> 224
~ -[PLVideoViewAccessibility _showVideoOverlay] : 228 -> 216
~ -[PLVideoViewAccessibility _videoOverlayFadeOutDidFinish] : 148 -> 144
~ -[PLVideoViewAccessibility viewDidDisappear] : 172 -> 164
~ -[PLVideoViewAccessibility _createScrubberIfNeeded] : 172 -> 164
~ -[PLVideoViewAccessibility isAccessibilityElement] : 168 -> 156
~ -[PLVideoViewAccessibility accessibilityLabel] : 92 -> 84
~ -[PLVideoViewAccessibility accessibilityElements] : 460 -> 432
~ -[PLVideoViewAccessibility _accessibilityLoadAccessibilityInformation] : 140 -> 132
~ -[PLVideoViewAccessibility accessibilityURL] : 204 -> 192
~ -[PLVideoViewAccessibility _accessibilityElementStoredUserLabel] : 84 -> 76
~ _accessibilityLocalizedStringFromBundle : 12 -> 120
~ _accessibilityLocalizedStringFromBundleWithTable : 128 -> 120
~ _accessibilityLocalizedString : 184 -> 176
~ -[UINavigationButtonAccessibility__PhotoLibrary__UIKit accessibilityLabel] : 260 -> 248
~ -[UIToolbarButtonAccessibility__PhotoLibrary__UIKit isAccessibilityElement] : 132 -> 120
~ -[UIToolbarButtonAccessibility__PhotoLibrary__UIKit accessibilityLabel] : 212 -> 192
~ +[PLSlalomRegionEditorAccessibility _accessibilityPerformValidations:] : 388 -> 380
~ -[PLSlalomRegionEditorAccessibility setStartValue:notify:] : 364 -> 336
~ __createFormatDurationString : 380 -> 368
~ -[PLSlalomRegionEditorAccessibility setEndValue:notify:] : 364 -> 336
~ -[PLSlalomRegionEditorAccessibility continueTrackingWithTouch:withEvent:] : 524 -> 488
~ -[PLSlalomRegionEditorAccessibility layoutSubviews] : 480 -> 456
~ -[PLSlalomRegionEditorAccessibility accessibilityElements] : 828 -> 776
~ -[PLSlalomRegionEditorAccessibility _accessibilitySliderDeltaForFrame:] : 172 -> 160
~ -[PLSlalomRegionEditorAccessibility _accessibilityIncrementMockSlider:largeStep:] : 664 -> 628
~ -[PLSlalomRegionEditorAccessibility _accessibilityDecrementMockSlider:largeStep:] : 664 -> 628
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"UIView\""
- "@16@0:8"
- "@20@0:8f16"
- "@24@0:8q16"
- "@40@0:8{CGPoint=dd}16@32"
- "@48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
- "AXPhotoLibraryFrameworkGlue"
- "B16@0:8"
- "B24@0:8q16"
- "B32@0:8@16@24"
- "PLImageAccessibilityElement"
- "PLIndexTitleViewAccessibility"
- "PLPhotoSmilesCommentCellAccessibility"
- "PLUIAccessibilityMockSlider"
- "Q16@0:8"
- "SafeCategory"
- "T@\"UIView\",&,N,V_view"
- "T@,W,N,V_mockSliderDelegate"
- "Ti,N,V_index"
- "UIAXNormalizedImage"
- "__MFComposeRecipientViewAccessibility__PhotoLibrary__MessageUI_super"
- "__PLContactPhotoOverlayAccessibility_super"
- "__PLCropOverlayAccessibility_super"
- "__PLCropOverlayBottomBarAccessibility_super"
- "__PLExpandableImageViewAccessibility_super"
- "__PLExpandableViewAccessibility_super"
- "__PLFlatVideoOverlayButtonAccessibility_super"
- "__PLHighFidelityVideoOverlayButtonAccessibility_super"
- "__PLImageScrollViewAccessibility_super"
- "__PLIndexTitleViewAccessibility_super"
- "__PLPhotoSmilesCommentCellAccessibility_super"
- "__PLPhotoTileViewControllerAccessibility_super"
- "__PLProgressViewAccessibility_super"
- "__PLSlalomRegionEditorAccessibility_super"
- "__PLUIImageViewControllerAccessibility_super"
- "__PLVideoEditingOverlayViewAccessibility_super"
- "__PLVideoRemakerAccessibility_super"
- "__PLVideoViewAccessibility_super"
- "__UINavigationButtonAccessibility__PhotoLibrary__UIKit_super"
- "__UITableViewCellAccessibility__PhotoLibrary__UIKit_super"
- "__UITextFieldAccessibility__PhotoLibrary__UIKit_super"
- "__UIToolbarButtonAccessibility__PhotoLibrary__UIKit_super"
- "_accessibilityAllowsSiblingsWhenOvergrown"
- "_accessibilityAncestorIsKindOf:"
- "_accessibilityClearChildren"
- "_accessibilityDecrementMockSlider:largeStep:"
- "_accessibilityDefaultFocusGroupIdentifier"
- "_accessibilityElementStoredUserLabel"
- "_accessibilityHitTest:withEvent:"
- "_accessibilityIgnoreInternalLabels"
- "_accessibilityIncrementMockSlider:largeStep:"
- "_accessibilityIsScrollAncestor"
- "_accessibilityLoadAccessibilityInformation"
- "_accessibilityPerformValidations:"
- "_accessibilityPhotoDescription"
- "_accessibilityRemoveValueForKey:"
- "_accessibilityScrollToVisible"
- "_accessibilitySetRetainedValue:forKey:"
- "_accessibilitySliderDeltaForFrame:"
- "_accessibilityValueForKey:"
- "_albumPhotoIndex"
- "_axExifLabel"
- "_axMainAssetURL"
- "_axSourceObject"
- "_axUpdatePlayPauseButtonWithImage"
- "_axUpdateValueBasedOnPercentComplete:"
- "_index"
- "_mockSliderDelegate"
- "_setPhoto:"
- "_view"
- "accessibilityActivationPoint"
- "accessibilityContainer"
- "accessibilityDecrement"
- "accessibilityElementCount"
- "accessibilityElements"
- "accessibilityFrame"
- "accessibilityIdentification"
- "accessibilityIdentifier"
- "accessibilityIncrement"
- "accessibilityInitializeBundle"
- "accessibilityLabel"
- "accessibilityPlaceholderValue"
- "accessibilityScroll:"
- "accessibilityTraits"
- "accessibilityURL"
- "accessibilityUserDefinedLabel"
- "accessibilityValue"
- "addHandler:forFramework:"
- "addObject:"
- "addObjectsFromArray:"
- "albumView"
- "albumView:accessibilityLabelForPhotoAtIndex:"
- "albumView:accessibilityPhotoDescription:"
- "albumView:accessibilityPhotoURL:"
- "albumView:accessibilityTraitsForPhotoAtIndex:"
- "appendFormat:"
- "array"
- "boolValue"
- "bounds"
- "bundleForClass:"
- "continueTrackingWithTouch:withEvent:"
- "convertPoint:toView:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "d48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
- "dictionary"
- "doubleValue"
- "drawInRect:"
- "fileURLWithPath:isDirectory:"
- "firstObject"
- "floatValue"
- "frame"
- "hasPrefix:"
- "i16@0:8"
- "index"
- "indexPathForCell:"
- "init"
- "initWithAccessibilityContainer:"
- "initWithFormat:"
- "initWithFrame:"
- "initWithString:"
- "installSafeCategory:canInteractWithTargetClass:"
- "integerValue"
- "isAccessibilityElement"
- "isAccessibilityUserDefinedElement"
- "isEqualToString:"
- "layoutSubviews"
- "length"
- "localizedStringForKey:value:table:"
- "mockSliderDelegate"
- "normalizedImageWithScale:"
- "objectForKey:"
- "performValidations:withPreValidationHandler:postValidationHandler:safeCategoryInstallationHandler:"
- "q16@0:8"
- "rangeOfString:"
- "rangeOfString:options:"
- "rectValue"
- "row"
- "safeBoolForKey:"
- "safeCategoryBaseClass"
- "safeCategoryTargetClassName"
- "safeValueForKey:"
- "scale"
- "setAccessibilityContainer:"
- "setAccessibilityLabel:"
- "setAccessibilityValue:"
- "setAttribute:forKey:withRange:"
- "setDebugBuild:"
- "setEndValue:notify:"
- "setIndex:"
- "setIsAccessibilityElement:"
- "setMockSliderDelegate:"
- "setNeedsLoadAccessibilityInformation"
- "setObject:forKey:"
- "setOverrideProcessName:"
- "setStartValue:notify:"
- "setState:withDuration:"
- "setValidationTargetName:"
- "setView:"
- "sharedInstance"
- "size"
- "sizeValue"
- "slalomRegionEditorDidBeginEditing:withStartHandle:"
- "slalomRegionEditorDidEndEditing:"
- "string"
- "v16@0:8"
- "v20@0:8f16"
- "v20@0:8i16"
- "v24@0:8@16"
- "v24@0:8d16"
- "v28@0:8@16B24"
- "v28@0:8d16B24"
- "v28@0:8i16d20"
- "validateClass:"
- "validateClass:hasInstanceMethod:withFullSignature:"
- "validateClass:hasInstanceVariable:withType:"
- "validateClass:isKindOfClass:"
- "valueForKey:"
- "valueWithRect:"
- "{CGPoint=dd}16@0:8"
- "{CGRect={CGPoint=dd}{CGSize=dd}}16@0:8"

```
