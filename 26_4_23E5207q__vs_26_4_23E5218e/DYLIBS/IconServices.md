## IconServices

> `/System/Library/PrivateFrameworks/IconServices.framework/IconServices`

```diff

-742.106.100.0.0
-  __TEXT.__text: 0x66968
+742.108.0.0.0
+  __TEXT.__text: 0x67320
   __TEXT.__auth_stubs: 0xf50
   __TEXT.__delay_helper: 0xdc
-  __TEXT.__objc_methlist: 0x670c
-  __TEXT.__const: 0x87d0
+  __TEXT.__objc_methlist: 0x678c
+  __TEXT.__const: 0x8800
   __TEXT.__gcc_except_tab: 0x458
   __TEXT.__cstring: 0x3f9a
-  __TEXT.__oslogstring: 0x32dd
-  __TEXT.__unwind_info: 0x17e8
+  __TEXT.__oslogstring: 0x33f8
+  __TEXT.__unwind_info: 0x17f0
   __TEXT.__eh_frame: 0x88
-  __TEXT.__objc_classname: 0x1260
-  __TEXT.__objc_methname: 0xc146
-  __TEXT.__objc_methtype: 0x18d9
-  __TEXT.__objc_stubs: 0x97a0
-  __DATA_CONST.__got: 0x638
+  __TEXT.__objc_classname: 0x1262
+  __TEXT.__objc_methname: 0xc30c
+  __TEXT.__objc_methtype: 0x18f5
+  __TEXT.__objc_stubs: 0x9820
+  __DATA_CONST.__got: 0x658
   __DATA_CONST.__const: 0xa30
   __DATA_CONST.__objc_classlist: 0x528
   __DATA_CONST.__objc_catlist: 0xf8
   __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3050
+  __DATA_CONST.__objc_selrefs: 0x3098
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x400
   __DATA_CONST.__objc_arraydata: 0xb0
   __AUTH_CONST.__auth_got: 0x7c0
-  __AUTH_CONST.__const: 0x1188
+  __AUTH_CONST.__const: 0x1168
   __AUTH_CONST.__cfstring: 0x4360
-  __AUTH_CONST.__objc_const: 0x13cb8
+  __AUTH_CONST.__objc_const: 0x13d48
   __AUTH_CONST.__objc_intobj: 0x528
   __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH_CONST.__objc_doubleobj: 0x30
   __AUTH.__objc_data: 0x7d0
-  __DATA.__objc_ivar: 0x6a0
+  __DATA.__objc_ivar: 0x6ac
   __DATA.__data: 0x1ce8
-  __DATA.__bss: 0x650
+  __DATA.__bss: 0x640
   __DATA_DIRTY.__objc_data: 0x2bc0
   __DATA_DIRTY.__data: 0xc
   __DATA_DIRTY.__bss: 0x1f8

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 8BA10C1B-1D6C-333D-A1C7-83A812283067
-  Functions: 2534
-  Symbols:   9556
-  CStrings:  4216
+  UUID: CAF3A2EC-0A0E-3F24-A13A-3A1DA4849EF8
+  Functions: 2543
+  Symbols:   9586
+  CStrings:  4238
 
Symbols:
+ +[IFColor(IconServicesAdditions) systemColorFromTagColorIndex:]
+ +[ISAliasIcon(Factory) _iconForValues:].cold.7
+ +[ISIconFactory _iconForURL:iconConfiguration:]
+ +[ISIconFactory _iconForURL:options:iconConfiguration:]
+ +[ISIconFactory _iconForURL:options:iconConfiguration:].cold.1
+ +[ISIconFactory _iconForURL:options:iconConfiguration:].cold.10
+ +[ISIconFactory _iconForURL:options:iconConfiguration:].cold.11
+ +[ISIconFactory _iconForURL:options:iconConfiguration:].cold.12
+ +[ISIconFactory _iconForURL:options:iconConfiguration:].cold.2
+ +[ISIconFactory _iconForURL:options:iconConfiguration:].cold.3
+ +[ISIconFactory _iconForURL:options:iconConfiguration:].cold.4
+ +[ISIconFactory _iconForURL:options:iconConfiguration:].cold.5
+ +[ISIconFactory _iconForURL:options:iconConfiguration:].cold.6
+ +[ISIconFactory _iconForURL:options:iconConfiguration:].cold.7
+ +[ISIconFactory _iconForURL:options:iconConfiguration:].cold.8
+ +[ISIconFactory _iconForURL:options:iconConfiguration:].cold.9
+ -[ISAliasIcon additionalURLProperties]
+ -[ISAliasIcon setAdditionalURLProperties:]
+ -[ISAssetInspector catalogAssetName]
+ -[ISAssetInspector setCatalogAssetName:]
+ -[ISFolderIconConfiguration initWithURL:]
+ -[ISFolderIconConfiguration initWithURL:].cold.1
+ -[ISFolderIconConfiguration initWithURLProperties:]
+ -[ISIconFactory initWithURL:iconConfiguration:]
+ -[ISURLResourcePropertySpecification folderConfigurationProperties]
+ _OBJC_IVAR_$_ISAliasIcon._additionalURLProperties
+ _OBJC_IVAR_$_ISAssetInspector._catalogAssetName
+ _OBJC_IVAR_$_ISURLResourcePropertySpecification._folderConfigurationProperties
+ ___block_literal_global.35
+ ___block_literal_global.76
+ ___block_literal_global.86
+ __kCFURLDirectoryHasVisibleContentKey
+ __kCFURLIconEmojiKey
+ __kCFURLIconSymbolNameKey
+ __kCFURLTagColorIndexKey
+ _objc_msgSend$_IF_numberForKey:
+ _objc_msgSend$_iconForURL:options:iconConfiguration:
+ _objc_msgSend$additionalURLProperties
+ _objc_msgSend$folderConfigurationProperties
+ _objc_msgSend$initWithURLProperties:
+ _objc_msgSend$systemColorFromTagColorIndex:
- +[ISIconFactory _iconForURL:options:].cold.1
- +[ISIconFactory _iconForURL:options:].cold.10
- +[ISIconFactory _iconForURL:options:].cold.11
- +[ISIconFactory _iconForURL:options:].cold.12
- +[ISIconFactory _iconForURL:options:].cold.2
- +[ISIconFactory _iconForURL:options:].cold.3
- +[ISIconFactory _iconForURL:options:].cold.4
- +[ISIconFactory _iconForURL:options:].cold.5
- +[ISIconFactory _iconForURL:options:].cold.6
- +[ISIconFactory _iconForURL:options:].cold.7
- +[ISIconFactory _iconForURL:options:].cold.8
- +[ISIconFactory _iconForURL:options:].cold.9
- -[ISDefaults forceSymbolEmbossment]
- -[ISDefaults forceSymbolEmbossment].cold.1
- ___35-[ISDefaults forceSymbolEmbossment]_block_invoke
- ___block_literal_global.33
- ___block_literal_global.36
- ___block_literal_global.70
- _forceSymbolEmbossment.once
- _forceSymbolEmbossment.symbolName
- _objc_msgSend$forceSymbolEmbossment
- _objc_msgSend$initWithSymbolName:tintColor:
CStrings:
+ "-[ISIcon initWithURL:iconConfiguration:]"
+ "04:06:02"
+ "@40@0:8@16Q24@32"
+ "Creating Folder icon for bookmark"
+ "Failed to retrieve folder configuration url properties from url: %@. Error: %@"
+ "Identified configurable folder for URL: %@. Config: %@"
+ "Identified configurable folder for alias URL: %@. Config: %@"
+ "Identified custom folder type %@ for alias URL: %@"
+ "No catalog icon asset referenced in Info.plist"
+ "T@\"NSArray\",R,V_folderConfigurationProperties"
+ "T@\"NSDictionary\",&,V_additionalURLProperties"
+ "T@\"NSString\",&,N,V_catalogAssetName"
+ "_IF_numberForKey:"
+ "_additionalURLProperties"
+ "_catalogAssetName"
+ "_folderConfigurationProperties"
+ "_iconForURL:iconConfiguration:"
+ "_iconForURL:options:iconConfiguration:"
+ "additionalURLProperties"
+ "folderConfigurationProperties"
+ "initWithURL:iconConfiguration:"
+ "initWithURLProperties:"
+ "q20@0:8i16"
+ "setAdditionalURLProperties:"
+ "setCatalogAssetName:"
+ "systemColorFromTagColorIndex:"
- "23:57:25"
- "Creating Folder icon  for bookmark"
- "ISForceSymbolEmbossment"
- "Overriding tint/embossing with config content: %@"
- "forceSymbolEmbossment"

```
