## IconServices

> `/System/Library/PrivateFrameworks/IconServices.framework/Versions/A/IconServices`

```diff

-792.100.0.0.0
-  __TEXT.__text: 0x7f818
+793.1.7.0.0
+  __TEXT.__text: 0x808ec
   __TEXT.__delay_stubs: 0x80
   __TEXT.__delay_helper: 0xa4
-  __TEXT.__objc_methlist: 0x78c4
+  __TEXT.__objc_methlist: 0x7924
+  __TEXT.__cstring: 0x55e6
   __TEXT.__const: 0x9570
-  __TEXT.__cstring: 0x5591
-  __TEXT.__oslogstring: 0x3cc1
-  __TEXT.__gcc_except_tab: 0x904
-  __TEXT.__unwind_info: 0x2518
+  __TEXT.__oslogstring: 0x4030
+  __TEXT.__gcc_except_tab: 0x96c
+  __TEXT.__unwind_info: 0x2580
   __TEXT.__eh_frame: 0x88
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x6e8
+  __DATA_CONST.__const: 0x6f0
   __DATA_CONST.__objc_classlist: 0x5c8
   __DATA_CONST.__objc_catlist: 0xe8
   __DATA_CONST.__objc_protolist: 0x148
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x37d0
+  __DATA_CONST.__objc_selrefs: 0x3818
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x488
   __DATA_CONST.__objc_arraydata: 0xb0
   __DATA_CONST.__got: 0x848
-  __AUTH_CONST.__const: 0x1b18
-  __AUTH_CONST.__cfstring: 0x5f40
-  __AUTH_CONST.__objc_const: 0x16b48
+  __AUTH_CONST.__const: 0x1b68
+  __AUTH_CONST.__cfstring: 0x5fa0
+  __AUTH_CONST.__objc_const: 0x16b98
   __AUTH_CONST.__weak_auth_got: 0x10
-  __AUTH_CONST.__objc_intobj: 0x690
+  __AUTH_CONST.__objc_intobj: 0x6a8
   __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH_CONST.__objc_doubleobj: 0x30
   __AUTH_CONST.__auth_got: 0xb48
   __AUTH.__objc_data: 0xcd0
   __AUTH.__data: 0x8
-  __DATA.__objc_ivar: 0x798
+  __DATA.__objc_ivar: 0x79c
   __DATA.__data: 0x211c
   __DATA_DIRTY.__objc_data: 0x2d00
-  __DATA_DIRTY.__bss: 0x220
+  __DATA_DIRTY.__bss: 0x270
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate
   - /System/Library/Frameworks/ApplicationServices.framework/Versions/A/Frameworks/HIServices.framework/Versions/A/HIServices
   - /System/Library/Frameworks/ApplicationServices.framework/Versions/A/Frameworks/QD.framework/Versions/A/QD

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3034
-  Symbols:   7315
-  CStrings:  1281
+  Functions: 3058
+  Symbols:   7348
+  CStrings:  1301
 
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
+ GCC_except_table37
+ OBJC_IVAR_$_ISGenericRecipe._allowsDebugBackground
+ OBJC_IVAR_$_ISGenericRecipe._debugBackgroundEnabled
+ _ISSymbolLog
+ _ISSymbolLog.log
+ _ISSymbolLog.onceToken
+ __ISSymbolLog
+ ___34+[ISSymbol _orderedVariantOptions]_block_invoke
+ ___38+[ISSymbol _keyPiecesToVariantOptions]_block_invoke
+ ___38+[ISSymbol _keyPiecesToVariantOptions]_block_invoke_2
+ ___38+[ISSymbol _variantOptionsToKeyPieces]_block_invoke
+ ____ISSymbolLog_block_invoke
+ ___block_descriptor_40_e8_32s_e35_v32?0"NSNumber"8"NSString"16^B24l
+ ___block_descriptor_80_e8_32s40s48s56bs64bs72r_e14_"NSError"8?0l
+ ___copy_helper_block_e8_32s40s48s56b64b72r
+ ___destroy_helper_block_e8_32s40s48s56s64s72r
+ _kISIconConfigurationKeySymbolVariant
+ _keyPiecesToVariantOptions.keyPiecesToOptions
+ _keyPiecesToVariantOptions.onceToken
+ _objc_msgSend$_applyTreatmentsAndCacheResultForResource:fallbackTypeID:descriptor:description:
+ _objc_msgSend$_keyPiecesToVariantOptions
+ _objc_msgSend$_orderedVariantOptions
+ _objc_msgSend$_variantOptionsToKeyPieces
+ _objc_msgSend$allowsDebugBackground
+ _objc_msgSend$debugBackgroundEnabled
+ _objc_msgSend$debugGenericAppIconResource
+ _objc_msgSend$enumerateKeysAndObjectsUsingBlock:
+ _objc_msgSend$isInteriorDebugContentEnabled
+ _objc_msgSend$setAllowsDebugBackground:
+ _objc_msgSend$symbolVariant
+ _objc_msgSend$variantOptionsForKey:
+ _orderedVariantOptions.onceToken
+ _orderedVariantOptions.orderedOptions
+ _variantOptionsToKeyPieces.onceToken
+ _variantOptionsToKeyPieces.optionsToKeyPieces
- -[ISGenericRecipe isDebugModeEnabled]
- -[ISGenericRecipe setDebugModeEnabled:]
- OBJC_IVAR_$_ISGenericRecipe._debugModeEnabled
- ___43+[ISSymbol _generateVariantKeyFromOptions:]_block_invoke
- ___block_descriptor_72_e8_32s40s48s56bs64r_e14_"NSError"8?0l
- ___copy_helper_block_e8_32s40s48s56b64r
- _generateVariantKeyFromOptions:.onceToken
- _generateVariantKeyFromOptions:.optionsToKeyPieces
- _generateVariantKeyFromOptions:.orderedOptions
- _objc_msgSend$isDebugModeEnabled
- _objc_msgSend$setDebugModeEnabled:
- _objc_msgSend$symbolForTypeIdentifier:error:
CStrings:
+ "Attempting to find symbol for type with id `%@` using strategy `%ld` and options `%llu`"
+ "Attempting to find symbol for type with id `%@`. Defaulting to default strategy and no options"
+ "Attempting to find symbol for type with id `%@`. Will use default strategy and no options"
+ "Attempting to find symbol for url: `%@`"
+ "Exception encoding generation request for %@ - %@: %@"
+ "Exception encoding generation request for %@ - %@: %@. Request: %@"
+ "Failed to create debug placeholder image. Image: %@. Fallback type: %@. Descriptor: %@. Icon: %@"
+ "Failed to create debug placeholder resource"
+ "Failed to find symbol for current device type %@. Error: %@"
+ "Found symbol `%@` for type `%@`"
+ "Found symbol `%@` for url `%@`"
+ "Found symbol name `%@` using bundleURL `%@` for url `%@`"
+ "Found type with id `%@` for url `%@`"
+ "ISSymbolVariant"
+ "Lookup for `%@` resolved to symbol name `%@` with url `%@`"
+ "Unknown variant option `%@`"
+ "debug_placeholder"
+ "interior_debug_content"
+ "state_b"
+ "symbols"
+ "v32@?0@\"NSNumber\"8@\"NSString\"16^B24"
- "debug_placeholder_icons"
```
