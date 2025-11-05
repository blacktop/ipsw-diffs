## ScreenReaderCore

> `/System/Library/PrivateFrameworks/ScreenReaderCore.framework/Versions/A/ScreenReaderCore`

```diff

-964.9.2.0.0
-  __TEXT.__text: 0x417b8
+964.12.7.1.0
+  __TEXT.__text: 0x4174c
   __TEXT.__auth_stubs: 0xce0
-  __TEXT.__objc_methlist: 0x375c
+  __TEXT.__objc_methlist: 0x393c
   __TEXT.__cstring: 0x80d3
   __TEXT.__const: 0x7a0
   __TEXT.__gcc_except_tab: 0x4a0

   __TEXT.__oslogstring: 0x42
   __TEXT.__unwind_info: 0xe48
   __TEXT.__objc_classname: 0x8a4
-  __TEXT.__objc_methname: 0x7da0
+  __TEXT.__objc_methname: 0x7db9
   __TEXT.__objc_methtype: 0x1505
   __TEXT.__objc_stubs: 0x6460
   __DATA_CONST.__got: 0x348

   __DATA_CONST.__objc_catlist: 0x90
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x22c0
+  __DATA_CONST.__objc_selrefs: 0x2368
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x170
   __DATA_CONST.__objc_arraydata: 0x238
   __AUTH_CONST.__auth_got: 0x680
   __AUTH_CONST.__const: 0x450
   __AUTH_CONST.__cfstring: 0x8a20
-  __AUTH_CONST.__objc_const: 0x5428
+  __AUTH_CONST.__objc_const: 0x5100
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_intobj: 0x90

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A1AACFE4-97A5-3642-AA38-55CFAA9BF8BA
-  Functions: 1302
-  Symbols:   3806
-  CStrings:  4059
+  UUID: E495775C-E749-3A5E-9523-9490BCACA724
+  Functions: 1317
+  Symbols:   3824
+  CStrings:  4060
 
Symbols:
+ +[NSBundle(SCRCBundleExtras) preferredLocalizationsForLocale:].cold.1
+ +[NSCharacterSet(SCRCCharacterSetExtras) emojiCharacterSet].cold.1
+ +[NSCharacterSet(SCRCCharacterSetExtras) modifierKeyCharacterSet].cold.1
+ +[SCRCPhotoEvaluator sharedInstance].cold.1
+ +[SCRCPhotoEvaluatorBlur detect:inRect:].cold.1
+ +[SCRCUserDefaultsRegistry keysToExcludeFromExport].cold.1
+ +[SCRCWebDateTimeParser sharedInstance].cold.1
+ -[NSString(SCRCStringExtras) hasPlaceholderCharPrefix]
+ -[SCRCMathExpression _scrcBundle].cold.1
+ -[SCRCMathExpression fenceDelimiters].cold.1
+ -[SCRCMathExpression latexIdentifierForIdentifier:].cold.1
+ -[SCRCMathExpression localizedStringForNumber:].cold.1
+ -[SCRCMathOperatorExpression latexFormatStringAsOver].cold.1
+ -[SCRCMathSimpleExpression _functionNames].cold.1
+ -[SCRCThread _processQueue].cold.1
+ -[SCRCUserDefaults(SCRCUserDefaultsImportExport) preferenceDomains].cold.1
+ GCC_except_table27
+ GCC_except_table31
+ SCRCDebugPrint.cold.2
+ SCRCLinkRelationshipStringForType.cold.1
- GCC_except_table26
- GCC_except_table30
CStrings:
+ "hasPlaceholderCharPrefix"

```
