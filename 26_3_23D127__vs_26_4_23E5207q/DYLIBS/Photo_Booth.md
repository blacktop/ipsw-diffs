## Photo Booth

> `/System/Library/AccessibilityBundles/Photo Booth.axbundle/Photo Booth`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0x13c0
-  __TEXT.__auth_stubs: 0x1c0
+3005.16.0.0.0
+  __TEXT.__text: 0x1470
+  __TEXT.__auth_stubs: 0x190
   __TEXT.__objc_methlist: 0x1e4
-  __TEXT.__cstring: 0x650
+  __TEXT.__cstring: 0x6ce
   __TEXT.__const: 0x8
   __TEXT.__unwind_info: 0xe0
   __TEXT.__objc_classname: 0x127

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x1c8
   __DATA_CONST.__objc_superrefs: 0x18
-  __AUTH_CONST.__auth_got: 0xe8
+  __AUTH_CONST.__auth_got: 0xd0
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x720
   __AUTH_CONST.__objc_const: 0x550

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8E3184A8-1885-35A4-ABA5-06C2F41AFEC4
+  UUID: C9FB740B-3E3C-3785-8960-BE9258902F87
   Functions: 37
-  Symbols:   212
+  Symbols:   209
   CStrings:  205
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x2
Functions:
~ _axLocalizedString : 176 -> 184
~ +[AXPhotoBoothGlue accessibilityInitializeBundle] : 148 -> 152
~ ___49+[AXPhotoBoothGlue accessibilityInitializeBundle]_block_invoke : 480 -> 484
~ ___49+[AXPhotoBoothGlue accessibilityInitializeBundle]_block_invoke_2 : 96 -> 100
~ ___49+[AXPhotoBoothGlue accessibilityInitializeBundle]_block_invoke_3 : 132 -> 140
~ -[UIApplication(PhotoBoothCategory) accessibilityStartStopToggle] : 112 -> 120
~ +[PBControllerAccessibility _accessibilityPerformValidations:] : 312 -> 320
~ -[PBControllerAccessibility _accessibilityLoadAccessibilityInformation] : 168 -> 180
~ -[PBControllerAccessibility _addTilesForPhotos:animated:] : 112 -> 116
~ -[PBControllerAccessibility _accessibilityApplyLabels:] : 324 -> 332
~ -[PBControllerAccessibility _reviewModeFooter] : 176 -> 180
~ -[PBControllerAccessibility toggleCamera:] : 120 -> 124
~ +[PBEffectsViewAccessibility _accessibilityPerformValidations:] : 296 -> 304
~ -[PBEffectsViewAccessibility accessibilityLabel] : 204 -> 212
~ -[PBEffectsViewAccessibility isAccessibilityElement] : 68 -> 72
~ -[PBEffectsViewAccessibility accessibilityElements] : 272 -> 292
~ -[PBEffectsViewAccessibility _accessibilityShouldHitTestLayers] : 68 -> 72
~ -[PBEffectsViewAccessibility dealloc] : 280 -> 284
~ -[PBEffectsViewAccessibility _accessibilityLoadAccessibilityInformation] : 296 -> 304
~ ___72-[PBEffectsViewAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke : 168 -> 176
~ -[PBShelfTileAccessibility accessibilityLabel] : 428 -> 444
~ -[PBShelfTileAccessibility accessibilityTraits] : 104 -> 108
~ -[PBContainerViewAccessibility _accessibilityHitTest:withEvent:] : 100 -> 116
CStrings:
+ "/Library/Caches/com.apple.xbs/68E6B9E5-C901-462C-A76A-34D56E9A7404/TemporaryDirectory.RaWz7g/Sources/AccessibilityBundles_Alias7/PhotoBoothAccessibility/Accessibility/PBControllerAccessibility.m"
+ "/Library/Caches/com.apple.xbs/68E6B9E5-C901-462C-A76A-34D56E9A7404/TemporaryDirectory.RaWz7g/Sources/AccessibilityBundles_Alias7/PhotoBoothAccessibility/Accessibility/PBEffectsViewAccessibility.m"
- "/Library/Caches/com.apple.xbs/Sources/AccessibilityBundles_Alias7/PhotoBoothAccessibility/Accessibility/PBControllerAccessibility.m"
- "/Library/Caches/com.apple.xbs/Sources/AccessibilityBundles_Alias7/PhotoBoothAccessibility/Accessibility/PBEffectsViewAccessibility.m"

```
