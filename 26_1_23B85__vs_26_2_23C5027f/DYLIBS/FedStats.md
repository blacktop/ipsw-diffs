## FedStats

> `/System/Library/PrivateFrameworks/FedStats.framework/FedStats`

```diff

-60.0.0.0.0
-  __TEXT.__text: 0x17e20
+62.0.0.0.0
+  __TEXT.__text: 0x17d50
   __TEXT.__auth_stubs: 0x530
-  __TEXT.__objc_methlist: 0x1794
+  __TEXT.__objc_methlist: 0x177c
   __TEXT.__const: 0xd8
-  __TEXT.__cstring: 0x3073
+  __TEXT.__cstring: 0x306d
   __TEXT.__oslogstring: 0x604
   __TEXT.__ustring: 0x1e
   __TEXT.__gcc_except_tab: 0x20
-  __TEXT.__unwind_info: 0x458
-  __TEXT.__objc_classname: 0x62b
-  __TEXT.__objc_methname: 0x3216
-  __TEXT.__objc_methtype: 0x796
+  __TEXT.__unwind_info: 0x460
+  __TEXT.__objc_classname: 0x629
+  __TEXT.__objc_methname: 0x3165
+  __TEXT.__objc_methtype: 0x773
   __TEXT.__objc_stubs: 0x2980
   __DATA_CONST.__got: 0x2a0
   __DATA_CONST.__const: 0x2f0

   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xca8
+  __DATA_CONST.__objc_selrefs: 0xc98
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xe0
   __DATA_CONST.__objc_arraydata: 0x3d0
   __AUTH_CONST.__auth_got: 0x2a8
   __AUTH_CONST.__const: 0xa0
-  __AUTH_CONST.__cfstring: 0x2de0
-  __AUTH_CONST.__objc_const: 0x3180
+  __AUTH_CONST.__cfstring: 0x2dc0
+  __AUTH_CONST.__objc_const: 0x3120
   __AUTH_CONST.__objc_intobj: 0x1b0
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH.__objc_data: 0xc30
-  __DATA.__objc_ivar: 0x14c
+  __DATA.__objc_ivar: 0x144
   __DATA.__data: 0x360
   __DATA.__bss: 0x28
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: D3C4C1E9-E384-36D9-87F6-8F4440E38B19
-  Functions: 436
-  Symbols:   1892
-  CStrings:  1483
+  UUID: 3FE8F387-3FD4-3944-AC2C-0DE18976434C
+  Functions: 434
+  Symbols:   1886
+  CStrings:  1473
 
Symbols:
+ +[FedStatsCategoricalTypeAssetSpecifier assetSpecifierWithKey:error:]
+ +[FedStatsDataEncoder extractAssetNamesFrom:usingFieldValues:error:]
+ +[FedStatsDataEncoder extractRequiredFieldsFrom:error:]
+ -[FedStatsCategoricalTypeAssetSpecifier initWithAssetSpecifierKey:]
+ _objc_msgSend$assetSpecifierWithKey:error:
+ _objc_msgSend$initWithAssetSpecifierKey:
- +[FedStatsCategoricalTypeAssetSpecifier assetSpecifierWithKey:requiredForCollectionKey:error:]
- +[FedStatsDataEncoder extractAssetNamesFrom:usingFieldValues:]
- +[FedStatsDataEncoder extractRequiredFieldsFrom:]
- -[FedStatsCategoricalTypeAssetSpecifier initWithAssetSpecifierKey:dynamic:requiredForCollectionKey:]
- -[FedStatsCategoricalTypeAssetSpecifier isDynamic]
- -[FedStatsCategoricalTypeAssetSpecifier isRequiredForCollectionKey]
- _OBJC_IVAR_$_FedStatsCategoricalTypeAssetSpecifier._isDynamic
- _OBJC_IVAR_$_FedStatsCategoricalTypeAssetSpecifier._isRequiredForCollectionKey
- _objc_msgSend$assetSpecifierWithKey:requiredForCollectionKey:error:
- _objc_msgSend$initWithAssetSpecifierKey:dynamic:requiredForCollectionKey:
CStrings:
+ "assetSpecifierWithKey:error:"
+ "extractAssetNamesFrom:usingFieldValues:error:"
+ "extractRequiredFieldsFrom:error:"
+ "initWithAssetSpecifierKey:"
- "@32@0:8@16B24B28"
- "@36@0:8@16B24^@28"
- "TB,R,N,V_isDynamic"
- "TB,R,N,V_isRequiredForCollectionKey"
- "^%@+$"
- "_isDynamic"
- "_isRequiredForCollectionKey"
- "assetSpecifierWithKey:requiredForCollectionKey:error:"
- "extractAssetNamesFrom:usingFieldValues:"
- "extractRequiredFieldsFrom:"
- "initWithAssetSpecifierKey:dynamic:requiredForCollectionKey:"
- "isDynamic"
- "isRequiredForCollectionKey"

```
