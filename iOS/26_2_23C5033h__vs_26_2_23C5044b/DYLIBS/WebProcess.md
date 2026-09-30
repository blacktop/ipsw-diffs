## WebProcess

> `/System/Library/AccessibilityBundles/WebProcess.axbundle/WebProcess`

```diff

-3005.4.9.0.0
-  __TEXT.__text: 0x1c78
-  __TEXT.__auth_stubs: 0x2f0
-  __TEXT.__objc_methlist: 0x230
+3005.4.13.0.0
+  __TEXT.__text: 0x1d88
+  __TEXT.__auth_stubs: 0x2e0
+  __TEXT.__objc_methlist: 0x238
   __TEXT.__const: 0x8
-  __TEXT.__cstring: 0x45b
+  __TEXT.__cstring: 0x477
   __TEXT.__oslogstring: 0x48
   __TEXT.__unwind_info: 0x130
   __TEXT.__objc_classname: 0xd1
-  __TEXT.__objc_methname: 0xb17
+  __TEXT.__objc_methname: 0xb47
   __TEXT.__objc_methtype: 0xca
   __TEXT.__objc_stubs: 0xa20
   __DATA_CONST.__got: 0x80
   __DATA_CONST.__const: 0x1a0
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x338
+  __DATA_CONST.__objc_selrefs: 0x348
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x180
+  __AUTH_CONST.__auth_got: 0x178
   __AUTH_CONST.__const: 0x1c0
-  __AUTH_CONST.__cfstring: 0x3c0
+  __AUTH_CONST.__cfstring: 0x3e0
   __AUTH_CONST.__objc_const: 0x360
   __DATA.__common: 0x8
   __DATA.__bss: 0x8

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: AF03DDBA-3A56-36D3-A8AA-18D9A8F26025
-  Functions: 60
-  Symbols:   331
-  CStrings:  205
+  UUID: D17C44C5-968E-3546-A8CA-95886A550315
+  Functions: 61
+  Symbols:   332
+  CStrings:  209
 
Symbols:
+ -[WKAccessibilityWebPageObjectAccessibility setRemoteTokenDictionary:]
+ _objc_msgSend$safeDictionaryForKey:
- _objc_msgSend$remoteTokenData
- _objc_release_x25
Functions:
~ -[WKAccessibilityWebPageObjectAccessibility _axRemoteElementRegistered:] : 420 -> 468
~ -[WKAccessibilityWebPageObjectAccessibility _accessibilityLoadAccessibilityInformation] : 152 -> 268
+ -[WKAccessibilityWebPageObjectAccessibility setRemoteTokenDictionary:]
CStrings:
+ "remoteTokenDictionary"
+ "safeDictionaryForKey:"
+ "setRemoteTokenDictionary:"

```
