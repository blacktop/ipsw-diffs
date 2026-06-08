## ExposureNotificationSettingsUI

> `/System/Library/AccessibilityBundles/ExposureNotificationSettingsUI.axbundle/ExposureNotificationSettingsUI`

```diff

-3005.28.0.0.0
-  __TEXT.__text: 0xb14
-  __TEXT.__auth_stubs: 0x100
+3036.2.0.0.0
+  __TEXT.__text: 0xa7c
   __TEXT.__objc_methlist: 0x1b0
-  __TEXT.__cstring: 0x36f
   __TEXT.__const: 0x8
+  __TEXT.__cstring: 0x36f
   __TEXT.__unwind_info: 0xa8
-  __TEXT.__objc_classname: 0x1ce
-  __TEXT.__objc_methname: 0x350
-  __TEXT.__objc_methtype: 0x23
-  __TEXT.__objc_stubs: 0x2e0
-  __DATA_CONST.__got: 0x30
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x68
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xf0
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x88
+  __DATA_CONST.__got: 0x30
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x480
   __AUTH_CONST.__objc_const: 0x630
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x370
   __DATA.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: CA6A285A-9697-3F29-BD82-68A25188AB8A
+  UUID: C173D9A2-23FA-37E9-B63E-97294DB7442A
   Functions: 31
-  Symbols:   175
-  CStrings:  122
+  Symbols:   176
+  CStrings:  76
 
Symbols:
+ ___block_literal_global.351
+ ___block_literal_global.360
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
- ___block_literal_global.330
- ___block_literal_global.339
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
Functions:
~ +[AXExposureNotificationSettingsUIGlue accessibilityInitializeBundle] : 152 -> 148
~ ___69+[AXExposureNotificationSettingsUIGlue accessibilityInitializeBundle]_block_invoke_2 : 100 -> 96
~ ___69+[AXExposureNotificationSettingsUIGlue accessibilityInitializeBundle]_block_invoke_3 : 160 -> 152
~ _accessibilityLocalizedString : 184 -> 176
~ +[ENUIExposureCheckCellAccessibility _accessibilityPerformValidations:] : 168 -> 156
~ +[ENUIRegionalDetailsHeaderCellAccessibility _accessibilityPerformValidations:] : 276 -> 264
~ -[ENUIRegionalDetailsHeaderCellAccessibility accessibilityElements] : 156 -> 144
~ -[ENUIRegionalDetailsHeaderCellAccessibility _accessibilityLoadAccessibilityInformation] : 196 -> 184
~ +[ENUILegalDocumentViewControllerAccessibility _accessibilityPerformValidations:] : 128 -> 120
~ -[ENUILegalDocumentViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 180 -> 176
~ ___90-[ENUILegalDocumentViewControllerAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke : 124 -> 116
~ +[ENUILoggingStatusCellAccessibility _accessibilityPerformValidations:] : 168 -> 156
~ -[ENUILoggingStatusCellAccessibility accessibilityLabel] : 92 -> 84
~ +[ENUIRegionCellAccessibility _accessibilityPerformValidations:] : 200 -> 188
~ -[ENUIRegionCellAccessibility accessibilityLabel] : 92 -> 84
~ -[ENUIRegionCellAccessibility accessibilityValue] : 220 -> 200
CStrings:
- "#16@0:8"
- "@16@0:8"
- "AXExposureNotificationSettingsUIGlue"
- "SafeCategory"
- "__ENUIExposureCheckCellAccessibility_super"
- "__ENUILegalDocumentViewControllerAccessibility_super"
- "__ENUILoggingStatusCellAccessibility_super"
- "__ENUIRegionCellAccessibility_super"
- "__ENUIRegionalDetailsHeaderCellAccessibility_super"
- "_accessibilityImageView"
- "_accessibilityLoadAccessibilityInformation"
- "_accessibilityPerformValidations:"
- "_accessibilityStringForLabelKeyValues:"
- "_setAccessibilityElementsBlock:"
- "accessibilityElements"
- "accessibilityInitializeBundle"
- "accessibilityLabel"
- "accessibilityValue"
- "axArrayByIgnoringNilElementsWithCount:"
- "bundleForClass:"
- "init"
- "installSafeCategory:canInteractWithTargetClass:"
- "localizedStringForKey:value:table:"
- "performValidations:withPreValidationHandler:postValidationHandler:safeCategoryInstallationHandler:"
- "safeCategoryBaseClass"
- "safeCategoryTargetClassName"
- "safeStringForKey:"
- "safeUIViewForKey:"
- "safeValueForKey:"
- "safeValueForKeyPath:"
- "setAccessibilityLabel:"
- "setDebugBuild:"
- "setIsAccessibilityElement:"
- "setOverrideProcessName:"
- "setValidationTargetName:"
- "sharedInstance"
- "v16@0:8"
- "v24@0:8@16"
- "validateClass:hasInstanceMethod:withFullSignature:"
- "validateClass:isKindOfClass:"

```
