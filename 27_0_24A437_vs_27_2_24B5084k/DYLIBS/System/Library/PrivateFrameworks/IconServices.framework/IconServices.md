## IconServices

> `/System/Library/PrivateFrameworks/IconServices.framework/IconServices`

```diff

-792.102.0.0.0
-  __TEXT.__text: 0x64560
+793.1.7.0.0
+  __TEXT.__text: 0x650bc
   __TEXT.__delay_stubs: 0x80
   __TEXT.__delay_helper: 0xa4
-  __TEXT.__objc_methlist: 0x6934
+  __TEXT.__objc_methlist: 0x6994
+  __TEXT.__cstring: 0x463a
   __TEXT.__const: 0x8840
-  __TEXT.__cstring: 0x45e7
-  __TEXT.__oslogstring: 0x3d2c
+  __TEXT.__oslogstring: 0x3f95
   __TEXT.__gcc_except_tab: 0x6b8
-  __TEXT.__unwind_info: 0x1f88
+  __TEXT.__unwind_info: 0x1fe0
   __TEXT.__eh_frame: 0x88
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xa50
+  __DATA_CONST.__const: 0xa80
   __DATA_CONST.__objc_classlist: 0x530
   __DATA_CONST.__objc_catlist: 0xf8
   __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3180
+  __DATA_CONST.__objc_selrefs: 0x31c8
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x408
   __DATA_CONST.__objc_arraydata: 0xb0
   __DATA_CONST.__got: 0x6b0
-  __AUTH_CONST.__const: 0x11a8
-  __AUTH_CONST.__cfstring: 0x4a00
-  __AUTH_CONST.__objc_const: 0x13f98
+  __AUTH_CONST.__const: 0x11c8
+  __AUTH_CONST.__cfstring: 0x4a20
+  __AUTH_CONST.__objc_const: 0x13fe8
   __AUTH_CONST.__objc_intobj: 0x540
   __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH_CONST.__objc_doubleobj: 0x30
   __AUTH_CONST.__auth_got: 0x7f0
   __AUTH.__objc_data: 0x870
-  __DATA.__objc_ivar: 0x6d0
+  __DATA.__objc_ivar: 0x6d4
   __DATA.__data: 0x1cf0
   __DATA_DIRTY.__objc_data: 0x2b70
   __DATA_DIRTY.__data: 0x8
-  __DATA_DIRTY.__bss: 0x1c0
+  __DATA_DIRTY.__bss: 0x220
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2599
-  Symbols:   6201
-  CStrings:  1080
+  Functions: 2621
+  Symbols:   6229
+  CStrings:  1095
 
Symbols:
+ +[ISSymbol _keyPiecesToVariantOptions]
+ +[ISSymbol _orderedVariantOptions]
+ +[ISSymbol _variantOptionsToKeyPieces]
+ +[ISSymbol variantOptionsForKey:]
+ -[ISDefaults isInteriorDebugContentEnabled]
+ -[ISGenericRecipe allowsDebugBackground]
+ -[ISGenericRecipe debugBackgroundEnabled]
+ -[ISGenericRecipe setAllowsDebugBackground:]
+ -[ISGenericRecipe setDebugBackgroundEnabled:]
+ -[ISIconConfigurationMarkupParser symbolVariant]
+ _OBJC_IVAR_$_ISGenericRecipe._allowsDebugBackground
+ _OBJC_IVAR_$_ISGenericRecipe._debugBackgroundEnabled
+ __ISSymbolLog
+ __ISSymbolLog.log
+ __ISSymbolLog.onceToken
+ ___34+[ISSymbol _orderedVariantOptions]_block_invoke
+ ___38+[ISSymbol _keyPiecesToVariantOptions]_block_invoke
+ ___38+[ISSymbol _keyPiecesToVariantOptions]_block_invoke_2
+ ___38+[ISSymbol _variantOptionsToKeyPieces]_block_invoke
+ ____ISSymbolLog_block_invoke
+ ___block_descriptor_40_e8_32s_e35_v32?0"NSNumber"8"NSString"16^B24ls32l8
+ __keyPiecesToVariantOptions.keyPiecesToOptions
+ __keyPiecesToVariantOptions.onceToken
+ __orderedVariantOptions.onceToken
+ __orderedVariantOptions.orderedOptions
+ __variantOptionsToKeyPieces.onceToken
+ __variantOptionsToKeyPieces.optionsToKeyPieces
+ _kISIconConfigurationKeySymbolVariant
+ _objc_msgSend$_keyPiecesToVariantOptions
+ _objc_msgSend$_orderedVariantOptions
+ _objc_msgSend$_variantOptionsToKeyPieces
+ _objc_msgSend$allowsDebugBackground
+ _objc_msgSend$debugBackgroundEnabled
+ _objc_msgSend$enumerateKeysAndObjectsUsingBlock:
+ _objc_msgSend$isInteriorDebugContentEnabled
+ _objc_msgSend$setAllowsDebugBackground:
+ _objc_msgSend$symbolVariant
+ _objc_msgSend$variantOptionsForKey:
- -[ISGenericRecipe isDebugModeEnabled]
- -[ISGenericRecipe setDebugModeEnabled:]
- _OBJC_IVAR_$_ISGenericRecipe._debugModeEnabled
- ___43+[ISSymbol _generateVariantKeyFromOptions:]_block_invoke
- __generateVariantKeyFromOptions:.onceToken
- __generateVariantKeyFromOptions:.optionsToKeyPieces
- __generateVariantKeyFromOptions:.orderedOptions
- _objc_msgSend$isDebugModeEnabled
- _objc_msgSend$setDebugModeEnabled:
- _objc_msgSend$symbolForTypeIdentifier:error:
CStrings:
+ "Attempting to find symbol for type with id `%@` using strategy `%ld` and options `%llu`"
+ "Attempting to find symbol for type with id `%@`. Defaulting to default strategy and no options"
+ "Attempting to find symbol for type with id `%@`. Will use default strategy and no options"
+ "Attempting to find symbol for url: `%@`"
+ "Failed to find symbol for current device type %@. Error: %@"
+ "Found symbol `%@` for type `%@`"
+ "Found symbol `%@` for url `%@`"
+ "Found symbol name `%@` using bundleURL `%@` for url `%@`"
+ "Found type with id `%@` for url `%@`"
+ "ISSymbolVariant"
+ "Lookup for `%@` resolved to symbol name `%@` with url `%@`"
+ "Unknown variant option `%@`"
+ "interior_debug_content"
+ "symbols"
+ "v32@?0@\"NSNumber\"8@\"NSString\"16^B24"
```
