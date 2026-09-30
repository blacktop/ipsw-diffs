## fontservicesd

> `/System/Library/PrivateFrameworks/FontServices.framework/Support/fontservicesd`

```diff

-157.0.0.0.0
-  __TEXT.__text: 0xc2a8
-  __TEXT.__auth_stubs: 0x7a0
-  __TEXT.__objc_stubs: 0x1d80
+157.1.0.1.0
+  __TEXT.__text: 0xc004
+  __TEXT.__auth_stubs: 0x7c0
+  __TEXT.__objc_stubs: 0x1d20
   __TEXT.__objc_methlist: 0x910
   __TEXT.__const: 0x78
-  __TEXT.__cstring: 0x14b8
+  __TEXT.__cstring: 0x14fb
   __TEXT.__gcc_except_tab: 0x338
-  __TEXT.__objc_methname: 0x243f
+  __TEXT.__objc_methname: 0x23f8
   __TEXT.__objc_classname: 0x17e
   __TEXT.__objc_methtype: 0x72f
-  __TEXT.__unwind_info: 0x348
-  __DATA_CONST.__auth_got: 0x3e0
-  __DATA_CONST.__got: 0x228
-  __DATA_CONST.__const: 0x9b8
-  __DATA_CONST.__cfstring: 0x1240
+  __TEXT.__unwind_info: 0x340
+  __DATA_CONST.__auth_got: 0x3f0
+  __DATA_CONST.__got: 0x230
+  __DATA_CONST.__const: 0xa60
+  __DATA_CONST.__cfstring: 0x1200
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x18
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA_CONST.__objc_arraydata: 0x10
-  __DATA_CONST.__objc_arrayobj: 0x18
   __DATA.__objc_const: 0x978
-  __DATA.__objc_selrefs: 0xa10
+  __DATA.__objc_selrefs: 0x9f8
   __DATA.__objc_ivar: 0x54
   __DATA.__objc_data: 0xf0
   __DATA.__data: 0x3c0

   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 430E32DF-E9D3-35A6-BB63-E6E806DCB968
+  UUID: 6F1AD260-439E-3018-9247-9B2441E8D134
   Functions: 217
-  Symbols:   202
-  CStrings:  806
+  Symbols:   204
+  CStrings:  801
 
Symbols:
+ _FSGetMaxSupportedFontAssetCompatibilityVersion
+ _FSRefreshObsoleteAssets
+ _kFSFontAssetCompatibilityVersionKey
- _OBJC_CLASS_$_NSConstantArray
Functions:
~ sub_10000c5bc -> sub_10000c51c : 216 -> 220
~ sub_10000cb30 -> sub_10000ca94 : 412 -> 20
~ sub_10000cccc -> sub_10000caa8 : 336 -> 60
~ sub_10000ce1c -> sub_10000cae4 : 108 -> 60
~ sub_10000ce88 -> sub_10000cb20 : 176 -> 184
~ sub_10000cf38 -> sub_10000cbd8 : 452 -> 468
~ sub_10000d170 -> sub_10000ce20 : 160 -> 172
CStrings:
+ "Downloading font asset %@ (id: %@) result:%d"
+ "purging obsolete asset %@ (id: %@) from %@ result:%d"
+ "refreshObsoleteAssets"
+ "v32@?0q8@\"NSString\"16@\"NSString\"24"
+ "v40@?0q8@\"NSString\"16@\"NSString\"24@\"NSString\"32"
- "_CompatibilityVersion"
- "com.apple.MobileAsset.Font6"
- "com.apple.MobileAsset.Font7"
- "purge:"
- "purging obsolete asset %@ result:%d"
- "removeObsoleteFontAsset"
- "setDoNotBlockBeforeFirstUnlock:"
- "setDoNotBlockOnNetworkStatus:"

```
