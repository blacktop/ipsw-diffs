## DataDeliveryServices

> `/System/Library/PrivateFrameworks/DataDeliveryServices.framework/Versions/A/DataDeliveryServices`

```diff

-115.0.0.0.0
-  __TEXT.__text: 0x2c9ec
-  __TEXT.__objc_methlist: 0x2a7c
+117.0.0.0.0
+  __TEXT.__text: 0x2cc64
+  __TEXT.__objc_methlist: 0x2ac4
   __TEXT.__const: 0x188
   __TEXT.__gcc_except_tab: 0x620
-  __TEXT.__cstring: 0x1690
-  __TEXT.__oslogstring: 0x3dfe
-  __TEXT.__unwind_info: 0xf78
+  __TEXT.__cstring: 0x16a2
+  __TEXT.__oslogstring: 0x3e0a
+  __TEXT.__unwind_info: 0xf88
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xf8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1618
+  __DATA_CONST.__objc_selrefs: 0x1620
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x118
   __DATA_CONST.__objc_arraydata: 0x70
   __DATA_CONST.__got: 0x338
   __AUTH_CONST.__const: 0x1200
   __AUTH_CONST.__cfstring: 0x1960
-  __AUTH_CONST.__objc_const: 0x8e18
+  __AUTH_CONST.__objc_const: 0x8e70
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x1e0
-  __DATA.__objc_ivar: 0x22c
+  __DATA.__objc_ivar: 0x230
   __DATA.__data: 0xbd0
   __DATA_DIRTY.__objc_data: 0xc30
   __DATA_DIRTY.__data: 0x8

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1084
-  Symbols:   2633
+  Functions: 1089
+  Symbols:   2640
   CStrings:  560
 
Symbols:
+ -[DDSUAFManager _assetsFromUAFForQuery:]
+ -[DDSUAFManager assetQueryResultsCache]
+ -[DDSUAFManager serverDidUpdateAssetsWithType:]
+ -[DDSUAFManagerStub serverDidUpdateAssetsWithType:]
+ GCC_except_table22
+ GCC_except_table25
+ GCC_except_table34
+ OBJC_IVAR_$_DDSUAFManager._assetQueryResultsCache
+ __40-[DDSUAFManager _assetsFromUAFForQuery:]_block_invoke
+ ___40-[DDSUAFManager _assetsFromUAFForQuery:]_block_invoke
+ _objc_msgSend$_assetsFromUAFForQuery:
- GCC_except_table23
- GCC_except_table32
- __32-[DDSUAFManager assetsForQuery:]_block_invoke
- ___32-[DDSUAFManager assetsForQuery:]_block_invoke
CStrings:
+ "DDSUAFManagerStub: serverDidUpdateAssetsWithType called (no-op)"
+ "UAFAssetAccess"
+ "com.apple.UnifiedAssetFramework"
- "FinishTaskNow"
- "assetsForQuery: %{public}@ final result: %{public}@"
- "com.apple.common"
```
