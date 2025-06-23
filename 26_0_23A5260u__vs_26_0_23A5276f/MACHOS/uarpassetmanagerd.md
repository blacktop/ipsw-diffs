## uarpassetmanagerd

> `/usr/libexec/uarpassetmanagerd`

```diff

-1338.0.21.0.2
-  __TEXT.__text: 0x24d1c
+1338.0.37.0.0
+  __TEXT.__text: 0x24d9c
   __TEXT.__auth_stubs: 0x450
   __TEXT.__objc_stubs: 0x2260
-  __TEXT.__objc_methlist: 0x111c
-  __TEXT.__cstring: 0x2755
+  __TEXT.__objc_methlist: 0x1124
+  __TEXT.__cstring: 0x276e
   __TEXT.__oslogstring: 0x15a9
   __TEXT.__objc_methname: 0x2846
   __TEXT.__objc_classname: 0x2db

   __TEXT.__unwind_info: 0x360
   __DATA_CONST.__auth_got: 0x238
   __DATA_CONST.__got: 0x180
-  __DATA_CONST.__const: 0x1e48
-  __DATA_CONST.__cfstring: 0x26e0
+  __DATA_CONST.__const: 0x1e80
+  __DATA_CONST.__cfstring: 0x2720
   __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x60

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 634D04ED-1D08-3BFB-AE7D-74ABF04C5375
-  Functions: 415
-  Symbols:   4853
-  CStrings:  1412
+  UUID: AB838180-9665-3093-AE5F-C17710856E85
+  Functions: 416
+  Symbols:   4872
+  CStrings:  1416
 
Symbols:
+ -[UARPSettingsAccessory description]
+ _MA_ASSET_PROPERTY_ALLOW_USER_INTERACTION
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
Functions:
+ -[UARPSettingsAccessory description]
~ _getPallasSettingForAccessory : 264 -> 236
CStrings:
+ "%@"
+ "_AllowUserInteraction"

```
