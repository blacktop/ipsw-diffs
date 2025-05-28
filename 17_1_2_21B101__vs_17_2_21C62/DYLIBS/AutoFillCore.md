## AutoFillCore

> `/System/Library/PrivateFrameworks/AutoFillCore.framework/AutoFillCore`

```diff

-27.150.0.0.0
-  __TEXT.__text: 0x9bb8
+27.202.0.0.0
+  __TEXT.__text: 0xa0e0
   __TEXT.__auth_stubs: 0x4f0
   __TEXT.__objc_methlist: 0x384
   __TEXT.__const: 0x68
-  __TEXT.__cstring: 0x1676
-  __TEXT.__gcc_except_tab: 0x378
+  __TEXT.__cstring: 0x16c7
+  __TEXT.__gcc_except_tab: 0x390
   __TEXT.__oslogstring: 0x3
-  __TEXT.__dlopen_cstrs: 0x354
-  __TEXT.__unwind_info: 0x2b8
+  __TEXT.__dlopen_cstrs: 0x3aa
+  __TEXT.__unwind_info: 0x2c8
   __TEXT.__objc_classname: 0xa4
   __TEXT.__objc_methname: 0x1a09
   __TEXT.__objc_methtype: 0x3ae
   __TEXT.__objc_stubs: 0x13a0
   __DATA_CONST.__got: 0x28
-  __DATA_CONST.__const: 0x6e8
+  __DATA_CONST.__const: 0x700
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA.__objc_superrefs: 0x20
   __DATA.__objc_ivar: 0x54
   __DATA.__data: 0xd0
-  __DATA.__bss: 0x168
+  __DATA.__bss: 0x180
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Security.framework/Security

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 203
-  Symbols:   915
-  CStrings:  485
+  Functions: 209
+  Symbols:   931
+  CStrings:  488
 
Symbols:
+ -[AFSuggestionGenerationManager generateCreditCardAutoFillWithCompletionHandler:].cold.3
+ -[AFSuggestionGenerationManager generateCreditCardAutoFillWithCompletionHandler:].cold.4
+ _SafariSharedLibrary
+ _SafariSharedLibraryCore.frameworkLibrary
+ ___SafariSharedLibraryCore_block_invoke
+ ___getWBSCreditCardTypeFromNumberSymbolLoc_block_invoke
+ ___getWBSCreditCardTypeLocalizedNameForGeneratingCardNamesSymbolLoc_block_invoke
+ _audit_stringSafariShared
+ _getWBSCreditCardTypeFromNumberSymbolLoc.ptr
+ _getWBSCreditCardTypeLocalizedNameForGeneratingCardNamesSymbolLoc.ptr
CStrings:
+ "WBSCreditCardTypeFromNumber"
+ "WBSCreditCardTypeLocalizedNameForGeneratingCardNames"
+ "softlink:r:path:/System/Library/PrivateFrameworks/SafariShared.framework/SafariShared"

```
