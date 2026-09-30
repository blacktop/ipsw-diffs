## SpotlightServices

> `/System/Library/PrivateFrameworks/SpotlightServices.framework/SpotlightServices`

```diff

-2400.19.0.0.0
-  __TEXT.__text: 0x158bfc
-  __TEXT.__auth_stubs: 0x1ce0
+2400.22.0.0.0
+  __TEXT.__text: 0x158d0c
+  __TEXT.__auth_stubs: 0x1d20
   __TEXT.__objc_methlist: 0xf200
-  __TEXT.__const: 0x2af8
-  __TEXT.__cstring: 0x3116f
+  __TEXT.__const: 0x2ae8
+  __TEXT.__cstring: 0x311aa
   __TEXT.__gcc_except_tab: 0x4d04
   __TEXT.__oslogstring: 0x9c7b
   __TEXT.__ustring: 0x8c2

   __TEXT.__swift5_proto: 0xc
   __TEXT.__swift5_types: 0x18
   __TEXT.__swift5_capture: 0x94
-  __TEXT.__unwind_info: 0x3458
+  __TEXT.__unwind_info: 0x3468
   __TEXT.__objc_classname: 0x1521
   __TEXT.__objc_methname: 0x2be12
   __TEXT.__objc_methtype: 0x314a

   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x560
   __DATA_CONST.__objc_arraydata: 0x1248
-  __AUTH_CONST.__auth_got: 0xe80
-  __AUTH_CONST.__const: 0x2930
-  __AUTH_CONST.__cfstring: 0x2b6a0
+  __AUTH_CONST.__auth_got: 0xea0
+  __AUTH_CONST.__const: 0x2950
+  __AUTH_CONST.__cfstring: 0x2b6c0
   __AUTH_CONST.__objc_const: 0x188d8
   __AUTH_CONST.__objc_intobj: 0x32d0
-  __AUTH_CONST.__objc_doubleobj: 0x2a0
-  __AUTH_CONST.__objc_floatobj: 0x20
   __AUTH_CONST.__objc_arrayobj: 0x828
+  __AUTH_CONST.__objc_doubleobj: 0x2a0
   __AUTH_CONST.__objc_dictobj: 0x258
+  __AUTH_CONST.__objc_floatobj: 0x20
   __AUTH.__objc_data: 0x2228
   __AUTH.__data: 0x118
   __DATA.__objc_ivar: 0x1558
   __DATA.__data: 0x1240
-  __DATA.__bss: 0xc88
+  __DATA.__bss: 0xc98
   __DATA.__common: 0x28
   __DATA_DIRTY.__objc_data: 0x23f0
   __DATA_DIRTY.__data: 0x298
-  __DATA_DIRTY.__bss: 0x4cc0
+  __DATA_DIRTY.__bss: 0x4cb8
   __DATA_DIRTY.__common: 0x30
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /System/Library/Frameworks/Intents.framework/Intents
   - /System/Library/Frameworks/MarketplaceKit.framework/MarketplaceKit
   - /System/Library/Frameworks/NaturalLanguage.framework/NaturalLanguage
+  - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers
   - /System/Library/PrivateFrameworks/AeroML.framework/AeroML
   - /System/Library/PrivateFrameworks/AggregateDictionary.framework/AggregateDictionary

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 1BEE933A-D85C-3A19-929F-F9404F9844AD
-  Functions: 6457
-  Symbols:   22340
-  CStrings:  19626
+  UUID: CCAA0460-255B-37C1-9E54-B07FC6399B13
+  Functions: 6459
+  Symbols:   22341
+  CStrings:  19628
 
Symbols:
+ +[SSLocalCEP getCEPValuesForCurrentLocale].cold.2
+ _CFBooleanGetTypeID
+ _CFBooleanGetValue
+ _SecTaskCopyValueForEntitlement
+ _SecTaskCreateFromSelf
+ __OBJC_$_CATEGORY_NSArray_$_Tokenize
+ __OBJC_$_CATEGORY_NSString_$_TokenMatch
+ __OBJC_$_INSTANCE_METHODS_NSArray(Tokenize|PRSRankingItemAdditions|QueryUtils)
+ __OBJC_$_INSTANCE_METHODS_NSString(TokenMatch|MatchScore|ParsecExtras|QueryParser|SSQueryUtils)
+ ___42+[SSLocalCEP getCEPValuesForCurrentLocale]_block_invoke_3
+ ___block_literal_global.11
+ ___block_literal_global.19
+ _getCEPValuesForCurrentLocale.sEntitlementCheckToken
+ _getCEPValuesForCurrentLocale.sHasEngagementDataEntitlement
- __OBJC_$_CATEGORY_NSArray_$_QueryUtils
- __OBJC_$_CATEGORY_NSString_$_QueryParser
- __OBJC_$_INSTANCE_METHODS_NSArray(QueryUtils|Tokenize|PRSRankingItemAdditions)
- __OBJC_$_INSTANCE_METHODS_NSString(QueryParser|MatchScore|SSQueryUtils|TokenMatch|ParsecExtras)
- ___block_literal_global.14
CStrings:
+ "com.apple.private.spotlight.cep-engagement-data"

```
