## MobileSoftwareUpdate

> `/System/Library/PrivateFrameworks/MobileSoftwareUpdate.framework/MobileSoftwareUpdate`

```diff

-2422.0.71.0.1
-  __TEXT.__text: 0xc980
+2422.0.80.0.0
+  __TEXT.__text: 0xcc24
   __TEXT.__auth_stubs: 0x6a0
   __TEXT.__objc_methlist: 0x100
   __TEXT.__const: 0x470
-  __TEXT.__cstring: 0x1dda
-  __TEXT.__oslogstring: 0x1cc9
+  __TEXT.__cstring: 0x1e16
+  __TEXT.__oslogstring: 0x1d6f
   __TEXT.__gcc_except_tab: 0xc8
   __TEXT.__unwind_info: 0x238
   __TEXT.__objc_classname: 0x30
-  __TEXT.__objc_methname: 0x518
+  __TEXT.__objc_methname: 0x548
   __TEXT.__objc_methtype: 0x7a
-  __TEXT.__objc_stubs: 0x6a0
+  __TEXT.__objc_stubs: 0x6e0
   __DATA_CONST.__got: 0xf0
   __DATA_CONST.__const: 0x780
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x210
+  __DATA_CONST.__objc_selrefs: 0x220
   __DATA_CONST.__objc_superrefs: 0x10
   __AUTH_CONST.__auth_got: 0x360
   __AUTH_CONST.__const: 0x338
-  __AUTH_CONST.__cfstring: 0x2620
+  __AUTH_CONST.__cfstring: 0x2640
   __AUTH_CONST.__objc_const: 0x1a0
   __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0x8
-  __DATA.__bss: 0x28
-  __DATA_DIRTY.__bss: 0x28
+  __DATA.__bss: 0x20
+  __DATA_DIRTY.__bss: 0x30
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 615EE53B-A332-3855-B35D-BB6359D163DE
-  Functions: 202
-  Symbols:   774
-  CStrings:  872
+  UUID: E89D2C40-1706-30B4-90D9-9118FCBC7741
+  Functions: 204
+  Symbols:   779
+  CStrings:  880
 
Symbols:
+ _MSUCopyStashedAccessibilityPrefs
+ _MSUCopyStashedAccessibilityPrefs.cold.1
+ _objc_msgSend$firstObject
+ _objc_msgSend$languageIdentifier
+ _objc_msgSend$localeWithLocaleIdentifier:
+ _objc_msgSend$preferredLanguages
- _objc_msgSend$_deviceLanguage
- _objc_msgSend$currentLocale
Functions:
~ _MSUApplyUpdate : 1128 -> 1160
+ _MSUCopyStashedAccessibilityPrefs
+ _MSUCopyStashedAccessibilityPrefs.cold.1
CStrings:
+ "AccessibilityDomains.plist"
+ "MSUCopyStashedAccessibilityPrefs"
+ "[SPI] %@ | Attempting to load accessibility domains from %@"
+ "[SPI] %@ | Current LanguageCode: %@ ExpandedLanguageCode: %@"
+ "[SPI] %@ | FAILURE | unable to load accessibility domains"
+ "[SPI] %@ | SUCCESS | accessibilityDict:%@"
+ "firstObject"
+ "languageIdentifier"
+ "localeWithLocaleIdentifier:"
+ "preferredLanguages"
- "[SPI] %@ | Current Locale: %@ ExpandedLanguageCode: %@"
- "_deviceLanguage"
- "currentLocale"

```
