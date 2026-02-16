## ExposureNotificationSettingsUI

> `/System/Library/AccessibilityBundles/ExposureNotificationSettingsUI.axbundle/ExposureNotificationSettingsUI`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0xa7c
-  __TEXT.__auth_stubs: 0x110
+3005.16.0.0.0
+  __TEXT.__text: 0xb14
+  __TEXT.__auth_stubs: 0x100
   __TEXT.__objc_methlist: 0x1b0
   __TEXT.__cstring: 0x36f
   __TEXT.__const: 0x8

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xf0
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x90
+  __AUTH_CONST.__auth_got: 0x88
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x480
   __AUTH_CONST.__objc_const: 0x630

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A581E883-4DDF-32ED-AE71-F8AD24C02824
+  UUID: 59A3D9D0-7A65-379A-B4AA-966CC88EEB50
   Functions: 31
-  Symbols:   176
+  Symbols:   175
   CStrings:  122
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x2
Functions:
~ +[AXExposureNotificationSettingsUIGlue accessibilityInitializeBundle] : 148 -> 152
~ ___69+[AXExposureNotificationSettingsUIGlue accessibilityInitializeBundle]_block_invoke_2 : 96 -> 100
~ ___69+[AXExposureNotificationSettingsUIGlue accessibilityInitializeBundle]_block_invoke_3 : 152 -> 160
~ _accessibilityLocalizedString : 176 -> 184
~ +[ENUIExposureCheckCellAccessibility _accessibilityPerformValidations:] : 156 -> 168
~ +[ENUIRegionalDetailsHeaderCellAccessibility _accessibilityPerformValidations:] : 264 -> 276
~ -[ENUIRegionalDetailsHeaderCellAccessibility accessibilityElements] : 144 -> 156
~ -[ENUIRegionalDetailsHeaderCellAccessibility _accessibilityLoadAccessibilityInformation] : 184 -> 196
~ +[ENUILegalDocumentViewControllerAccessibility _accessibilityPerformValidations:] : 120 -> 128
~ -[ENUILegalDocumentViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 176 -> 180
~ ___90-[ENUILegalDocumentViewControllerAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke : 116 -> 124
~ +[ENUILoggingStatusCellAccessibility _accessibilityPerformValidations:] : 156 -> 168
~ -[ENUILoggingStatusCellAccessibility accessibilityLabel] : 84 -> 92
~ +[ENUIRegionCellAccessibility _accessibilityPerformValidations:] : 188 -> 200
~ -[ENUIRegionCellAccessibility accessibilityLabel] : 84 -> 92
~ -[ENUIRegionCellAccessibility accessibilityValue] : 200 -> 220

```
