## AuthKit

> `/System/Library/PrivateFrameworks/AuthKit.framework/AuthKit`

```diff

-525.475.18.0.0
-  __TEXT.__text: 0x197484
+525.475.19.0.0
+  __TEXT.__text: 0x1978ec
   __TEXT.__auth_stubs: 0xc80
-  __TEXT.__objc_methlist: 0xefec
+  __TEXT.__objc_methlist: 0xf00c
   __TEXT.__const: 0x6a48
-  __TEXT.__cstring: 0x107a2
-  __TEXT.__gcc_except_tab: 0xa798
-  __TEXT.__oslogstring: 0x13e2c
+  __TEXT.__cstring: 0x107db
+  __TEXT.__gcc_except_tab: 0xa7f4
+  __TEXT.__oslogstring: 0x13e9f
   __TEXT.__dlopen_cstrs: 0x305
   __TEXT.__ustring: 0x300
-  __TEXT.__unwind_info: 0x4548
+  __TEXT.__unwind_info: 0x4558
   __TEXT.__objc_classname: 0x1e34
-  __TEXT.__objc_methname: 0x251c9
+  __TEXT.__objc_methname: 0x2528b
   __TEXT.__objc_methtype: 0x49aa
   __TEXT.__objc_stubs: 0x10bc0
   __DATA_CONST.__got: 0xad0
-  __DATA_CONST.__const: 0xa6b8
+  __DATA_CONST.__const: 0xa6e8
   __DATA_CONST.__objc_classlist: 0x6b8
   __DATA_CONST.__objc_catlist: 0x88
   __DATA_CONST.__objc_protolist: 0x208
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x78e0
+  __DATA_CONST.__objc_selrefs: 0x78f8
   __DATA_CONST.__objc_protorefs: 0xe0
   __DATA_CONST.__objc_superrefs: 0x438
   __DATA_CONST.__objc_arraydata: 0x2e8
   __AUTH_CONST.__auth_got: 0x650
   __AUTH_CONST.__const: 0x1410
-  __AUTH_CONST.__cfstring: 0x11580
-  __AUTH_CONST.__objc_const: 0x282b0
+  __AUTH_CONST.__cfstring: 0x115a0
+  __AUTH_CONST.__objc_const: 0x282e0
   __AUTH_CONST.__objc_intobj: 0x300
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_dictobj: 0x410
   __AUTH.__objc_data: 0x2ad0
-  __DATA.__objc_ivar: 0x115c
+  __DATA.__objc_ivar: 0x1160
   __DATA.__data: 0x1900
   __DATA.__bss: 0x6f8
   __DATA_DIRTY.__objc_data: 0x1860

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 56DD3F45-AE93-3F78-8C6F-5B6955210607
-  Functions: 5774
-  Symbols:   21843
-  CStrings:  12832
+  UUID: 26E74B0C-8D28-3BF3-9C57-CC2562C8BD75
+  Functions: 5777
+  Symbols:   21858
+  CStrings:  12843
 
Symbols:
+ -[AKAccountManager enforceLivenessNonce:]
+ -[AKAccountManager setEnforceLivenessNonce:success:]
+ -[AKFeatureManager isPasskeyValidationFixesEnabled]
+ GCC_except_table237
+ GCC_except_table281
+ GCC_except_table282
+ GCC_except_table300
+ GCC_except_table303
+ GCC_except_table306
+ GCC_except_table314
+ GCC_except_table315
+ GCC_except_table355
+ GCC_except_table361
+ GCC_except_table362
+ GCC_except_table377
+ GCC_except_table378
+ _AKEnforceLivenessNonce
+ _AKUserAgeRangeHeaderKey
+ _OBJC_IVAR_$_AKFeatureManager._cachedPasskeyValidationFixesEnabled
+ ___block_literal_global.219
+ ___block_literal_global.254
+ ___block_literal_global.279
- GCC_except_table257
- GCC_except_table263
- GCC_except_table283
- GCC_except_table284
- GCC_except_table302
- GCC_except_table305
- GCC_except_table308
- GCC_except_table326
- GCC_except_table327
- GCC_except_table357
- GCC_except_table363
- GCC_except_table364
- ___block_literal_global.216
- ___block_literal_global.251
- ___block_literal_global.276
- _kAKAnalyticsEscapeOffer
CStrings:
+ "Call completion with authentication finished with results additionalData :%@ and error: %@"
+ "Exception caught when fetching enforceLivenessNonce: %@"
+ "Feature PasskeyValidationFixes enabled - %@"
+ "PasskeyValidationFixes"
+ "TB,R,N,GisPasskeyValidationFixesEnabled"
+ "X-Apple-I-User-Age-Range"
+ "_cachedPasskeyValidationFixesEnabled"
+ "enforceLivenessNonce"
+ "enforceLivenessNonce:"
+ "isPasskeyValidationFixesEnabled"
+ "passkeyValidationFixesEnabled"
+ "setEnforceLivenessNonce:success:"
- "Call completion with authentication result with presentation completion: %@"
- "escapeOffer"

```
