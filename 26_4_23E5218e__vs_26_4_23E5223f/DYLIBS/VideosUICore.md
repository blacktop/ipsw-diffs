## VideosUICore

> `/System/Library/PrivateFrameworks/VideosUICore.framework/VideosUICore`

```diff

-1061.40.55.0.1
-  __TEXT.__text: 0x30d8c
+1061.40.57.0.1
+  __TEXT.__text: 0x30da8
   __TEXT.__auth_stubs: 0xbc0
   __TEXT.__objc_methlist: 0x4e5c
   __TEXT.__const: 0x1e0
-  __TEXT.__cstring: 0x2d35
+  __TEXT.__cstring: 0x2d44
   __TEXT.__oslogstring: 0xda7
   __TEXT.__gcc_except_tab: 0x7d8
   __TEXT.__ustring: 0x6a

   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x198
   __AUTH_CONST.__auth_got: 0x5f0
-  __AUTH_CONST.__const: 0x560
-  __AUTH_CONST.__cfstring: 0x58e0
+  __AUTH_CONST.__const: 0x580
+  __AUTH_CONST.__cfstring: 0x5900
   __AUTH_CONST.__objc_const: 0x7ea0
   __AUTH_CONST.__objc_intobj: 0x300
   __AUTH_CONST.__objc_doubleobj: 0xc0
   __AUTH.__objc_data: 0x780
   __DATA.__objc_ivar: 0x530
   __DATA.__data: 0x858
-  __DATA.__bss: 0x80
+  __DATA.__bss: 0x90
   __DATA_DIRTY.__objc_data: 0xe60
   __DATA_DIRTY.__data: 0x8
   __DATA_DIRTY.__bss: 0x210

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6301B757-C42F-3629-9C0F-443BE76AA469
-  Functions: 1676
-  Symbols:   6170
-  CStrings:  4247
+  UUID: CC5825B4-06E0-3635-B178-EA09C3CFB3E7
+  Functions: 1678
+  Symbols:   6177
+  CStrings:  4249
 
Symbols:
+ -[VUIFeatureManager osFeatureFlagsJSON].cold.1
+ ___39-[VUIFeatureManager osFeatureFlagsJSON]_block_invoke
+ ___block_descriptor_49_e8_32s40w_e24_v16?0"NSNotification"8lw40l8s32l8
+ ___block_literal_global.78
+ _osFeatureFlagsJSON.sparkleEnabledDefaultsValue
+ _osFeatureFlagsJSON.sparkleOnceToken
- ___block_descriptor_41_e8_32w_e24_v16?0"NSNotification"8lw32l8
Functions:
~ -[VUIFeatureManager osFeatureFlagsJSON] : 2692 -> 2584
+ ___39-[VUIFeatureManager osFeatureFlagsJSON]_block_invoke
~ -[VUIImageProxy _completeImageLoadWithImage:imagePath:error:assetKey:expiryDate:tags:] : 776 -> 780
~ ___86-[VUIImageProxy _completeImageLoadWithImage:imagePath:error:assetKey:expiryDate:tags:]_block_invoke : 488 -> 508
+ +[VUICoreUtilities _vuiCoreResourceMap].cold.1
CStrings:
+ "sparkleEnabled"

```
