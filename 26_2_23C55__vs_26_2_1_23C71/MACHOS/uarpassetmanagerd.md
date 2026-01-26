## uarpassetmanagerd

> `/usr/libexec/uarpassetmanagerd`

```diff

-1338.60.22.0.0
+1338.62.1.0.0
   __TEXT.__text: 0x25908
   __TEXT.__auth_stubs: 0x490
   __TEXT.__objc_stubs: 0x22a0
   __TEXT.__objc_methlist: 0x1124
-  __TEXT.__cstring: 0x2830
+  __TEXT.__cstring: 0x27bc
   __TEXT.__oslogstring: 0x1608
   __TEXT.__objc_methname: 0x28aa
   __TEXT.__objc_classname: 0x2db

   __TEXT.__unwind_info: 0x360
   __DATA_CONST.__auth_got: 0x258
   __DATA_CONST.__got: 0x188
-  __DATA_CONST.__const: 0x1f38
-  __DATA_CONST.__cfstring: 0x27c0
+  __DATA_CONST.__const: 0x1e90
+  __DATA_CONST.__cfstring: 0x2760
   __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x60

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2C98DDA8-3C2B-32C9-A385-723E5798D15E
+  UUID: 7284DCB3-6BC1-3EFF-AB4C-96BE47DC614F
   Functions: 416
-  Symbols:   4926
-  CStrings:  1431
+  Symbols:   4884
+  CStrings:  1425
 
Symbols:
+ __44-[UARPAssetManagerServiceInstance copyCache]_block_invoke.360
+ __46-[UARPAssetManagerServiceInstance primeCache:]_block_invoke.380
+ __46-[UARPAssetManagerServiceInstance queryIsBusy]_block_invoke.366
+ __49-[UARPAssetManagerServiceInstance checkForUpdate]_block_invoke.365
+ __52-[UARPAssetManagerServiceInstance copySubscriptions]_block_invoke.362
+ __59-[UARPAssetManagerServiceInstance registerForSubscription:]_block_invoke.364
+ __60-[UARPAssetManagerServiceInstance clearAssetCacheForDomain:]_block_invoke.375
+ __61-[UARPAssetManagerServiceInstance checkCacheForSubscription:]_block_invoke.357
+ __70-[UARPAssetManagerServiceInstance listener:shouldAcceptNewConnection:]_block_invoke.332
- _INTERNAL_PALLAS_SERVER_URL_V2_AUTH
- _MA_PALLAS_AUDIENCE_CUSTOMER_SEASHIP
- _MA_PALLAS_AUDIENCE_INTERNAL_SEASHIP
- __44-[UARPAssetManagerServiceInstance copyCache]_block_invoke.369
- __46-[UARPAssetManagerServiceInstance primeCache:]_block_invoke.389
- __46-[UARPAssetManagerServiceInstance queryIsBusy]_block_invoke.375
- __49-[UARPAssetManagerServiceInstance checkForUpdate]_block_invoke.374
- __52-[UARPAssetManagerServiceInstance copySubscriptions]_block_invoke.371
- __59-[UARPAssetManagerServiceInstance registerForSubscription:]_block_invoke.373
- __60-[UARPAssetManagerServiceInstance clearAssetCacheForDomain:]_block_invoke.384
- __61-[UARPAssetManagerServiceInstance checkCacheForSubscription:]_block_invoke.366
- __70-[UARPAssetManagerServiceInstance listener:shouldAcceptNewConnection:]_block_invoke.341
CStrings:
- "cd060049-2465-43e3-bbb5-d769a66da2d7"
- "ffc25f86-b83c-4139-b8ad-91131d0e5429"
- "https://gdmf-auth-stg.apple.com/v2/assets"

```
