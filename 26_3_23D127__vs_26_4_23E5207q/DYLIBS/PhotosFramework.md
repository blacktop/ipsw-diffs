## PhotosFramework

> `/System/Library/AccessibilityBundles/PhotosFramework.axbundle/PhotosFramework`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0x1fe0
-  __TEXT.__auth_stubs: 0x350
+3005.16.0.0.0
+  __TEXT.__text: 0x21e8
+  __TEXT.__auth_stubs: 0x320
   __TEXT.__objc_methlist: 0x164
-  __TEXT.__cstring: 0x4dd
+  __TEXT.__cstring: 0x51c
   __TEXT.__const: 0x10
   __TEXT.__gcc_except_tab: 0x14
   __TEXT.__oslogstring: 0x1e

   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x2b0
-  __AUTH_CONST.__auth_got: 0x1b8
+  __AUTH_CONST.__auth_got: 0x1a0
   __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__cfstring: 0x720
   __AUTH_CONST.__objc_const: 0x1b0

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5D182449-1AFB-30D1-8194-CA068671D473
+  UUID: 05CF867C-F972-3E88-BAB7-624BB674B782
   Functions: 36
-  Symbols:   252
+  Symbols:   249
   CStrings:  225
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x21
Functions:
~ _accessibilityCameraUILocalizedString : 184 -> 192
~ _accessibilityPLServicesLocalizedString : 184 -> 192
~ +[PhotosAXGlue accessibilityInitializeBundle] : 100 -> 104
~ ___45+[PhotosAXGlue accessibilityInitializeBundle]_block_invoke_2 : 96 -> 100
~ +[PHAssetAccessibility _accessibilityPerformValidations:] : 644 -> 656
~ -[PHAssetAccessibility shouldMeasureBlurriness] : 68 -> 72
~ -[PHAssetAccessibility _accessibilityCreationTime] : 132 -> 140
~ -[PHAssetAccessibility _accessibilityCreationDate] : 344 -> 376
~ -[PHAssetAccessibility _accessibilityOrientation] : 188 -> 200
~ -[PHAssetAccessibility _accessibilityAssetDuration] : 84 -> 88
~ -[PHAssetAccessibility accessibilityCustomContent] : 1452 -> 1596
~ _AXCombineStringsWithoutDuplicates : 496 -> 516
~ -[PHAssetAccessibility _accessibilityFacesInfo] : 176 -> 188
~ -[PHAssetAccessibility _accessibilityPeopleInPhoto] : 432 -> 452
~ -[PHAssetAccessibility accessibilityURL] : 676 -> 716
~ -[PHAssetAccessibility _accessibilityIsPHAssetLocallyAvailable] : 172 -> 184
~ -[PHAssetAccessibility _accessibilityPhotoLibraryURL] : 164 -> 176
~ -[PHAssetAccessibility accessibilityLabel] : 1040 -> 1148
~ -[PHAssetAccessibility _accessibilityCaptionLabel] : 76 -> 84
~ -[PHAssetAccessibility _accessibilityiCloudPhotoLabel] : 352 -> 380
~ -[PHAssetAccessibility _accessibilitySavePhotoLabel:] : 428 -> 432
~ ___53-[PHAssetAccessibility _accessibilitySavePhotoLabel:]_block_invoke : 92 -> 96
~ ___53-[PHAssetAccessibility _accessibilitySavePhotoLabel:]_block_invoke_2 : 228 -> 232
~ -[PHAssetAccessibility accessibilityApplyValueBlock:] : 132 -> 140
CStrings:
+ "/Library/Caches/com.apple.xbs/D796EB7F-4AEA-4A12-AB49-AB256E569E81/TemporaryDirectory.1bWS40/Sources/AccessibilityBundles/PhotoLibraryAccessibility/Accessibility/PHAssetAccessibility.m"
- "/Library/Caches/com.apple.xbs/Sources/AccessibilityBundles/PhotoLibraryAccessibility/Accessibility/PHAssetAccessibility.m"

```
