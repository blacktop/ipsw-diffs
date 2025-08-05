## uarpassetmanagerd

> `/usr/libexec/uarpassetmanagerd`

```diff

-1338.0.62.0.1
+1338.0.72.0.0
   __TEXT.__text: 0x24d9c
   __TEXT.__auth_stubs: 0x450
   __TEXT.__objc_stubs: 0x2260
   __TEXT.__objc_methlist: 0x1124
-  __TEXT.__cstring: 0x27b6
+  __TEXT.__cstring: 0x27bf
   __TEXT.__oslogstring: 0x15a9
   __TEXT.__objc_methname: 0x2846
   __TEXT.__objc_classname: 0x2db

   __TEXT.__unwind_info: 0x360
   __DATA_CONST.__auth_got: 0x238
   __DATA_CONST.__got: 0x180
-  __DATA_CONST.__const: 0x1e58
-  __DATA_CONST.__cfstring: 0x2740
+  __DATA_CONST.__const: 0x1e90
+  __DATA_CONST.__cfstring: 0x2760
   __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x60

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 004C08B3-CD4C-30B3-91F8-F0AD2A749993
+  UUID: A544315E-6F26-3BA3-8E91-C90F2FA96039
   Functions: 416
-  Symbols:   4862
-  CStrings:  1418
+  Symbols:   4876
+  CStrings:  1420
 
Symbols:
+ _MA_AUTO_ASSET_SHORT_TERM_LOCK_FILESYSTEM_SPECIFIC
+ __44-[UARPAssetManagerServiceInstance copyCache]_block_invoke.360
+ __46-[UARPAssetManagerServiceInstance primeCache:]_block_invoke.380
+ __46-[UARPAssetManagerServiceInstance queryIsBusy]_block_invoke.366
+ __49-[UARPAssetManagerServiceInstance checkForUpdate]_block_invoke.365
+ __52-[UARPAssetManagerServiceInstance copySubscriptions]_block_invoke.362
+ __59-[UARPAssetManagerServiceInstance registerForSubscription:]_block_invoke.364
+ __60-[UARPAssetManagerServiceInstance clearAssetCacheForDomain:]_block_invoke.375
+ __61-[UARPAssetManagerServiceInstance checkCacheForSubscription:]_block_invoke.357
+ __70-[UARPAssetManagerServiceInstance listener:shouldAcceptNewConnection:]_block_invoke.332
- __44-[UARPAssetManagerServiceInstance copyCache]_block_invoke.357
- __46-[UARPAssetManagerServiceInstance primeCache:]_block_invoke.377
- __46-[UARPAssetManagerServiceInstance queryIsBusy]_block_invoke.363
- __49-[UARPAssetManagerServiceInstance checkForUpdate]_block_invoke.362
- __52-[UARPAssetManagerServiceInstance copySubscriptions]_block_invoke.359
- __59-[UARPAssetManagerServiceInstance registerForSubscription:]_block_invoke.361
- __60-[UARPAssetManagerServiceInstance clearAssetCacheForDomain:]_block_invoke.372
- __61-[UARPAssetManagerServiceInstance checkCacheForSubscription:]_block_invoke.354
- __70-[UARPAssetManagerServiceInstance listener:shouldAcceptNewConnection:]_block_invoke.329
CStrings:
+ "specific"

```
