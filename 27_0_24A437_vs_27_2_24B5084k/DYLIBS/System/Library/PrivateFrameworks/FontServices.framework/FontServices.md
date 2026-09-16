## FontServices

> `/System/Library/PrivateFrameworks/FontServices.framework/FontServices`

```diff

-169.0.0.0.0
-  __TEXT.__text: 0xbdc0
+173.0.0.0.0
+  __TEXT.__text: 0xcf38
   __TEXT.__delay_helper: 0x308
-  __TEXT.__objc_methlist: 0xdfc
+  __TEXT.__objc_methlist: 0xe2c
   __TEXT.__const: 0x68
-  __TEXT.__cstring: 0x1a5b
-  __TEXT.__gcc_except_tab: 0x6d4
+  __TEXT.__cstring: 0x1d17
+  __TEXT.__gcc_except_tab: 0x724
   __TEXT.__oslogstring: 0x3
-  __TEXT.__unwind_info: 0x680
+  __TEXT.__unwind_info: 0x6c0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x6e8
+  __DATA_CONST.__const: 0x738
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x900
+  __DATA_CONST.__objc_selrefs: 0x928
   __DATA_CONST.__objc_protorefs: 0x60
   __DATA_CONST.__objc_superrefs: 0x40
   __DATA_CONST.__objc_arraydata: 0x48
   __DATA_CONST.__got: 0x1a0
   __AUTH_CONST.__const: 0x820
-  __AUTH_CONST.__cfstring: 0xe80
-  __AUTH_CONST.__objc_const: 0x10d8
+  __AUTH_CONST.__cfstring: 0xfa0
+  __AUTH_CONST.__objc_const: 0x10e8
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x2d0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 355
-  Symbols:   1035
-  CStrings:  188
+  Functions: 366
+  Symbols:   1054
+  CStrings:  199
 
Symbols:
+ +[FSUserFontManager replaceFontDataFromIdentifier:toIdentifier:]
+ -[FontServicesDaemonManager migrateIssuedFontsForIdentifier:toIdentifier:]
+ GCC_except_table37
+ GCC_except_table77
+ _AppReplacementDictionaryByRemovingIdentifier
+ _AppReplacementDictionaryByRenamingIdentifier
+ _AppReplacementIdentifierIsWellFormed
+ _FontProviderAppInfoIsWellFormed
+ _FontProviderFontsInfoIsWellFormed
+ ___64+[FSUserFontManager replaceFontDataFromIdentifier:toIdentifier:]_block_invoke
+ ___64+[FSUserFontManager replaceFontDataFromIdentifier:toIdentifier:]_block_invoke_2
+ ___74-[FontServicesDaemonManager migrateIssuedFontsForIdentifier:toIdentifier:]_block_invoke
+ ___74-[FontServicesDaemonManager migrateIssuedFontsForIdentifier:toIdentifier:]_block_invoke_2
+ ___block_descriptor_40_e8_32r_e17_v16?0"NSError"8lr32l8
+ ___block_descriptor_40_e8_32r_e8_v12?0B8lr32l8
+ _memchr
+ _objc_msgSend$containsString:
+ _objc_msgSend$isEqual:
+ _objc_msgSend$migrateIssuedFontsForIdentifier:toIdentifier:reply:
+ _objc_msgSend$replaceFontDataFromIdentifier:toIdentifier:completionHandler:
- GCC_except_table34
CStrings:
+ "+[FSUserFontManager replaceFontDataFromIdentifier:toIdentifier:]_block_invoke"
+ "-[FontServicesDaemonManager migrateIssuedFontsForIdentifier:toIdentifier:]_block_invoke"
+ ".."
+ "App Replacement: -> UserFontManager replaceFontData \"%@\" -> \"%@\""
+ "App Replacement: -> fontservicesd migrateIssuedFonts \"%@\" -> \"%@\""
+ "App Replacement: <- UserFontManager replaceFontData (xpcError %@, migrationError %@)"
+ "App Replacement: <- fontservicesd migrateIssuedFonts (success %d, xpcFailed %d)"
+ "UIFont is unavailable in this process; no system font names"
+ "UIWindow is unavailable in this process; continuing without a scene identifier"
+ "UIWindow is unavailable in this process; requesting fonts without a scene identifier"
+ "actualPath"
```
