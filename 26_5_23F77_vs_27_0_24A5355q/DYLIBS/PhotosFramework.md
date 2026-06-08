## PhotosFramework

> `/System/Library/AccessibilityBundles/PhotosFramework.axbundle/PhotosFramework`

```diff

-3005.28.0.0.0
-  __TEXT.__text: 0x21e8
-  __TEXT.__auth_stubs: 0x320
+3036.2.0.0.0
+  __TEXT.__text: 0x1ff8
   __TEXT.__objc_methlist: 0x164
-  __TEXT.__cstring: 0x51c
   __TEXT.__const: 0x10
   __TEXT.__gcc_except_tab: 0x14
+  __TEXT.__cstring: 0x51c
   __TEXT.__oslogstring: 0x1e
   __TEXT.__unwind_info: 0xe0
-  __TEXT.__objc_classname: 0x4c
-  __TEXT.__objc_methname: 0x7e3
-  __TEXT.__objc_methtype: 0x5e
-  __TEXT.__objc_stubs: 0x8c0
-  __DATA_CONST.__got: 0xb0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0xb0
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x2b0
-  __AUTH_CONST.__auth_got: 0x1a0
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__cfstring: 0x720
   __AUTH_CONST.__objc_const: 0x1b0
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__bss: 0x12
   __DATA_DIRTY.__objc_data: 0xf0
   - /System/Library/Frameworks/Accessibility.framework/Accessibility

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C22BBB25-A31A-38C8-973E-AD6698F3B806
+  UUID: 6D11540F-1A70-3922-8F2D-DC81468E0A31
   Functions: 36
-  Symbols:   249
-  CStrings:  225
+  Symbols:   252
+  CStrings:  125
 
Symbols:
+ GCC_except_table9
+ ___block_literal_global.5
+ ___block_literal_global.577
+ ___block_literal_global.586
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x21
- GCC_except_table24
- ___block_literal_global.535
- ___block_literal_global.544
- _objc_retainAutoreleasedReturnValue
Functions:
~ _accessibilityCameraUILocalizedString : 192 -> 184
~ _accessibilityPLServicesLocalizedString : 192 -> 184
~ +[PhotosAXGlue accessibilityInitializeBundle] : 104 -> 100
~ ___45+[PhotosAXGlue accessibilityInitializeBundle]_block_invoke_2 : 100 -> 96
~ +[PHAssetAccessibility _accessibilityPerformValidations:] : 656 -> 644
~ -[PHAssetAccessibility shouldMeasureBlurriness] : 72 -> 68
~ -[PHAssetAccessibility _accessibilityCreationTime] : 140 -> 132
~ -[PHAssetAccessibility _accessibilityCreationDate] : 376 -> 344
~ -[PHAssetAccessibility _accessibilityOrientation] : 200 -> 188
~ -[PHAssetAccessibility _accessibilityAssetDuration] : 88 -> 84
~ -[PHAssetAccessibility accessibilityCustomContent] : 1596 -> 1452
~ _AXCombineStringsWithoutDuplicates : 516 -> 512
~ -[PHAssetAccessibility _accessibilityFacesInfo] : 188 -> 176
~ -[PHAssetAccessibility _accessibilityPeopleInPhoto] : 452 -> 444
~ -[PHAssetAccessibility accessibilityURL] : 716 -> 692
~ -[PHAssetAccessibility _accessibilityIsPHAssetLocallyAvailable] : 184 -> 172
~ -[PHAssetAccessibility _accessibilityPhotoLibraryURL] : 176 -> 164
~ -[PHAssetAccessibility accessibilityLabel] : 1148 -> 1056
~ -[PHAssetAccessibility _accessibilityCaptionLabel] : 84 -> 76
~ -[PHAssetAccessibility _accessibilityiCloudPhotoLabel] : 380 -> 360
~ -[PHAssetAccessibility _accessibilitySavePhotoLabel:] : 432 -> 428
~ ___53-[PHAssetAccessibility _accessibilitySavePhotoLabel:]_block_invoke : 96 -> 92
~ ___53-[PHAssetAccessibility _accessibilitySavePhotoLabel:]_block_invoke_2 : 232 -> 184
~ -[PHAssetAccessibility accessibilityApplyValueBlock:] : 140 -> 132
CStrings:
- "#16@0:8"
- "@16@0:8"
- "@?16@0:8"
- "B16@0:8"
- "B24@0:8@16"
- "PhotosAXGlue"
- "Q16@0:8"
- "SafeCategory"
- "__PHAssetAccessibility_super"
- "_accessibilityAssetDuration"
- "_accessibilityCaptionLabel"
- "_accessibilityCreationDate"
- "_accessibilityCreationTime"
- "_accessibilityFacesInfo"
- "_accessibilityIsPHAssetLocallyAvailable"
- "_accessibilityOrientation"
- "_accessibilityPHAssetLocalIdentifier"
- "_accessibilityPeopleInPhoto"
- "_accessibilityPerformValidations:"
- "_accessibilityPhotoDescription"
- "_accessibilityPhotoLibraryURL"
- "_accessibilitySavePhotoLabel:"
- "_accessibilityiCloudPhotoLabel"
- "_axICloudLabelWasSet"
- "_axSetICloudLabelWasSet:"
- "_axValueCallback"
- "_setAXValueCallback:"
- "accessibilityApplyValueBlock:"
- "accessibilityCustomContent"
- "accessibilityDescription"
- "accessibilityInitializeBundle"
- "accessibilityLabel"
- "accessibilityTraits"
- "accessibilityURL"
- "accessibilityUserDefinedLabel"
- "accessibilityValue"
- "addObject:"
- "array"
- "arrayWithObjects:count:"
- "assetDescription"
- "assetResourcesForAsset:includeDerivatives:"
- "axArrayByIgnoringNilElementsWithCount:"
- "axFilterObjectsUsingBlock:"
- "boolValue"
- "bundleWithPath:"
- "changeRequestForAsset:"
- "components:fromDate:"
- "componentsJoinedByString:"
- "containsObject:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "currentCalendar"
- "customContentWithLabel:value:"
- "date"
- "day"
- "descriptionProperties"
- "fetchAssetsWithLocalIdentifiers:options:"
- "fetchFacesInAsset:options:"
- "fetchPersonsInAsset:options:"
- "firstObject"
- "identifier"
- "installSafeCategory:canInteractWithTargetClass:"
- "integerValue"
- "isEqualToString:"
- "isLocallyAvailable"
- "length"
- "localizedStringForKey:value:table:"
- "localizedStringWithFormat:"
- "month"
- "name"
- "performChanges:completionHandler:"
- "performValidations:withPreValidationHandler:postValidationHandler:safeCategoryInstallationHandler:"
- "privateFileURL"
- "safeBoolForKey:"
- "safeCategoryBaseClass"
- "safeCategoryTargetClassName"
- "safeFloatForKey:"
- "safeStringForKey:"
- "safeValueForKey:"
- "set"
- "setAccessibilityDescription:"
- "setAccessibilityLabel:"
- "setDebugBuild:"
- "setImportance:"
- "setOverrideProcessName:"
- "setValidationTargetName:"
- "sharedInstance"
- "shouldMeasureBlurriness"
- "uniformTypeIdentifier"
- "unsignedIntegerValue"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "validateClass:hasInstanceMethod:withFullSignature:"
- "validateClass:isKindOfClass:"
- "year"

```
