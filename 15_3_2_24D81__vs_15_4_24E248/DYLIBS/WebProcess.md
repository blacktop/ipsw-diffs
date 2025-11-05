## WebProcess

> `/System/iOSSupport/System/Library/AccessibilityBundles/WebProcess.axbundle/Versions/A/WebProcess`

```diff

-2963.3.13.1.0
-  __TEXT.__text: 0x2690
+2963.10.10.0.0
+  __TEXT.__text: 0x2698
   __TEXT.__auth_stubs: 0x370
   __TEXT.__objc_methlist: 0x248
   __TEXT.__const: 0x20

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: DA7FBEA2-6714-3FDD-B1F1-3D4EC3563709
-  Functions: 78
-  Symbols:   323
+  UUID: 9D0E2226-8EDD-3820-BE80-3718C035FA7A
+  Functions: 79
+  Symbols:   324
   CStrings:  232
 
Symbols:
+ +[AXWebProcessGlue accessibilityInitializeBundle].cold.1
Functions:
~ +[AXWebProcessGlue accessibilityInitializeBundle] : 92 -> 76
~ __40+[AXWebProcessGlue _initializeAXRuntime]_block_invoke_2.347 : 172 -> 168
~ -[WKAccessibilityWebPageObjectAccessibility _accessibilityTextViewTextOperationResponder] : 160 -> 164
~ -[WKAccessibilityWebPageObjectAccessibility _axRemoteElementRegistered:] : 416 -> 420
+ +[AXWebProcessGlue accessibilityInitializeBundle].cold.1
~ __getAXPMacPlatformElementClass_block_invoke.cold.1 : 128 -> 124
~ __getAXPMacPlatformElementClass_block_invoke.cold.2 : 124 -> 128
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AccessibilityBundles_Alias2/WebKitAccessibility/Accessibility/WKAccessibilityWebPageObjectAccessibility.m"
- "/AppleInternal/Library/BuildRoots/423aabcf-bd7b-11ef-ae7d-aabfac210453/Library/Caches/com.apple.xbs/Sources/AccessibilityBundles_Alias2/WebKitAccessibility/Accessibility/WKAccessibilityWebPageObjectAccessibility.m"

```
