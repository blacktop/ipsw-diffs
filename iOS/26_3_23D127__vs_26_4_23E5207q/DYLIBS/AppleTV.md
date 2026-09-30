## AppleTV

> `/System/Library/AccessibilityBundles/AppleTV.axbundle/AppleTV`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0x1ac
-  __TEXT.__auth_stubs: 0xa0
+3005.16.0.0.0
+  __TEXT.__text: 0x1bc
+  __TEXT.__auth_stubs: 0x90
   __TEXT.__objc_methlist: 0x20
   __TEXT.__cstring: 0x9a
   __TEXT.__unwind_info: 0x70

   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x50
-  __AUTH_CONST.__auth_got: 0x58
+  __AUTH_CONST.__auth_got: 0x50
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0xa0
   __AUTH_CONST.__objc_const: 0x90

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 540E2FE1-2F19-348B-AFFB-66E6FAF11762
+  UUID: 7B5BF35F-4DC7-3A27-A3D0-A62B6A9ED27D
   Functions: 6
-  Symbols:   48
+  Symbols:   47
   CStrings:  24
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
- _objc_claimAutoreleasedReturnValue
- _objc_retain
- _objc_retain_x1
Functions:
~ +[AXAppleTVGlue accessibilityInitializeBundle] : 148 -> 152
~ ___46+[AXAppleTVGlue accessibilityInitializeBundle]_block_invoke_2 : 84 -> 88
~ _accessibilityLocalizedString : 160 -> 168

```
