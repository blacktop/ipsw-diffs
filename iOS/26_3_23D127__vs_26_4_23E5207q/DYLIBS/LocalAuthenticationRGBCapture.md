## LocalAuthenticationRGBCapture

> `/System/Library/AccessibilityBundles/LocalAuthenticationRGBCapture.axbundle/LocalAuthenticationRGBCapture`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0x9b0
-  __TEXT.__auth_stubs: 0x120
+3005.16.0.0.0
+  __TEXT.__text: 0xa08
+  __TEXT.__auth_stubs: 0x110
   __TEXT.__objc_methlist: 0x1a0
   __TEXT.__cstring: 0x2ef
   __TEXT.__unwind_info: 0x98

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x118
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x98
+  __AUTH_CONST.__auth_got: 0x90
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x3c0
   __AUTH_CONST.__objc_const: 0x510

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: CF1BA449-13E1-3B89-A04B-EC8CE9EB2B7E
+  UUID: D89E9413-1C91-31DD-8C9D-42A6B7629B9F
   Functions: 31
-  Symbols:   169
+  Symbols:   168
   CStrings:  121
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x2
Functions:
~ +[AXLocalAuthenticationRGBCaptureGlue accessibilityInitializeBundle] : 148 -> 152
~ ___68+[AXLocalAuthenticationRGBCaptureGlue accessibilityInitializeBundle]_block_invoke_2 : 96 -> 100
~ ___68+[AXLocalAuthenticationRGBCaptureGlue accessibilityInitializeBundle]_block_invoke_3 : 132 -> 140
~ _accessibilityLocalizedString : 176 -> 184
~ +[LARGBCaptureSelfieVCAccessibility _accessibilityPerformValidations:] : 380 -> 388
~ -[LARGBCaptureSelfieVCAccessibility _toggleFlash:] : 180 -> 184
~ -[LARGBCaptureSelfieVCAccessibility _axAnnounceSuccess] : 188 -> 204
~ -[LARGBCaptureSelfieVCAccessibility _dispatchSkipButtonTimers] : 196 -> 208
~ +[LARGBCaptureInstructionsVCAccessibility _accessibilityPerformValidations:] : 152 -> 164
~ -[LARGBCaptureInstructionsVCAccessibility _accessibilityLoadAccessibilityInformation] : 204 -> 216

```
