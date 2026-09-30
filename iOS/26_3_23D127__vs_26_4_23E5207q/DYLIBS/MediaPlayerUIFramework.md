## MediaPlayerUIFramework

> `/System/Library/AccessibilityBundles/MediaPlayerUIFramework.axbundle/MediaPlayerUIFramework`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0x890
-  __TEXT.__auth_stubs: 0x150
+3005.16.0.0.0
+  __TEXT.__text: 0x8d8
+  __TEXT.__auth_stubs: 0x140
   __TEXT.__objc_methlist: 0x194
   __TEXT.__cstring: 0x1d5
   __TEXT.__const: 0x18

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x100
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0xb0
+  __AUTH_CONST.__auth_got: 0xa8
   __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__cfstring: 0x2e0
   __AUTH_CONST.__objc_const: 0x510

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: BC25677E-D586-3D33-96DF-706FBAA7C759
+  UUID: 14B26D42-D226-3A8C-B275-A07FEE82EB05
   Functions: 32
-  Symbols:   174
+  Symbols:   173
   CStrings:  102
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x2
Functions:
~ ___52+[AXMediaPlayerUIGlue accessibilityInitializeBundle]_block_invoke : 100 -> 104
~ ___52+[AXMediaPlayerUIGlue accessibilityInitializeBundle]_block_invoke_3 : 84 -> 88
~ ___52+[AXMediaPlayerUIGlue accessibilityInitializeBundle]_block_invoke_4 : 132 -> 140
~ _accessibilityMPUILocalizedString : 176 -> 184
~ -[MPUMarqueeViewAccessibility isAccessibilityElement] : 112 -> 120
~ -[MPUMarqueeViewAccessibility accessibilityLabel] : 396 -> 412
~ -[MPUNowPlayingIndicatorViewAccessibility setPlaybackState:] : 120 -> 124
~ +[MPURatingControlAccessibility _accessibilityPerformValidations:] : 168 -> 176
~ -[MPURatingControlAccessibility _accessibilityChangeValue:] : 220 -> 224
~ ___59-[MPURatingControlAccessibility _accessibilityChangeValue:]_block_invoke : 96 -> 100
~ -[MPURatingControlAccessibility accessibilityValue] : 92 -> 96

```
