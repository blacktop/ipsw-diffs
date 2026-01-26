## uarpassetmanagerd

> `/usr/libexec/uarpassetmanagerd`

```diff

-1338.80.32.0.0
-  __TEXT.__text: 0x28ac4
+1338.80.37.0.0
+  __TEXT.__text: 0x294b8
   __TEXT.__auth_stubs: 0x4c0
-  __TEXT.__objc_stubs: 0x2480
-  __TEXT.__objc_methlist: 0x1284
-  __TEXT.__cstring: 0x29c7
-  __TEXT.__oslogstring: 0x1788
-  __TEXT.__objc_methname: 0x2b79
+  __TEXT.__objc_stubs: 0x24e0
+  __TEXT.__objc_methlist: 0x129c
+  __TEXT.__cstring: 0x2a68
+  __TEXT.__oslogstring: 0x1822
+  __TEXT.__objc_methname: 0x2be3
   __TEXT.__objc_classname: 0x2fe
   __TEXT.__objc_methtype: 0x829
   __TEXT.__gcc_except_tab: 0x1ac
-  __TEXT.__unwind_info: 0x388
+  __TEXT.__unwind_info: 0x398
   __DATA_CONST.__auth_got: 0x270
-  __DATA_CONST.__got: 0x190
-  __DATA_CONST.__const: 0x21f8
-  __DATA_CONST.__cfstring: 0x2860
+  __DATA_CONST.__got: 0x198
+  __DATA_CONST.__const: 0x22c8
+  __DATA_CONST.__cfstring: 0x2940
   __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x60

   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x78
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0x2d18
-  __DATA.__objc_selrefs: 0xb68
-  __DATA.__objc_ivar: 0x178
+  __DATA.__objc_const: 0x2d48
+  __DATA.__objc_selrefs: 0xb80
+  __DATA.__objc_ivar: 0x17c
   __DATA.__objc_data: 0x500
   __DATA.__data: 0x480
   __DATA.__bss: 0x40

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 94C5FFFF-59DA-33F4-B573-850D8EFAD156
-  Functions: 448
-  Symbols:   5297
-  CStrings:  1484
+  UUID: E3C9A91F-6FEE-33CE-AD88-9D70B1D1F4EC
+  Functions: 451
+  Symbols:   5369
+  CStrings:  1505
 
Symbols:
+ -[UARPAssetSubscriptionMobileAsset pallasServerURL]
+ -[UARPAssetSubscriptionMobileAsset setPallasServerURL:]
+ OBJC_IVAR_$_UARPAssetSubscriptionMobileAsset._pallasServerURL
+ _INTERNAL_PALLAS_SERVER_URL_V2_AUTH
+ _MA_PALLAS_AUDIENCE_CUSTOMER_SEASHIP
+ _MA_PALLAS_AUDIENCE_INTERNAL_SEASHIP
+ _OBJC_CLASS_$_NSUUID
+ __44-[UARPAssetManagerServiceInstance copyCache]_block_invoke.370
+ __46-[UARPAssetManagerServiceInstance primeCache:]_block_invoke.387
+ __46-[UARPAssetManagerServiceInstance queryIsBusy]_block_invoke.376
+ __50-[UARPAssetManagerServiceInstance checkForUpdate:]_block_invoke.375
+ __52-[UARPAssetManagerServiceInstance copySubscriptions]_block_invoke.372
+ __59-[UARPAssetManagerServiceInstance registerForSubscription:]_block_invoke.374
+ __60-[UARPAssetManagerServiceInstance clearAssetCacheForDomain:]_block_invoke.385
+ __61-[UARPAssetManagerServiceInstance checkCacheForSubscription:]_block_invoke.367
+ __70-[UARPAssetManagerServiceInstance listener:shouldAcceptNewConnection:]_block_invoke.341
+ _kAUDeveloperSettingsPallasURLOverrideKey
+ _kUARPAssetSubscriptionMobileAssetEncoderKeyPallasServerURL
+ _loadProfilePallasURLOverrideSetting
+ _objc_msgSend$initWithUUIDString:
+ _objc_msgSend$pallasServerURL
+ _objc_msgSend$setPallasServerURL:
- __44-[UARPAssetManagerServiceInstance copyCache]_block_invoke.361
- __46-[UARPAssetManagerServiceInstance primeCache:]_block_invoke.378
- __46-[UARPAssetManagerServiceInstance queryIsBusy]_block_invoke.367
- __50-[UARPAssetManagerServiceInstance checkForUpdate:]_block_invoke.366
- __52-[UARPAssetManagerServiceInstance copySubscriptions]_block_invoke.363
- __59-[UARPAssetManagerServiceInstance registerForSubscription:]_block_invoke.365
- __60-[UARPAssetManagerServiceInstance clearAssetCacheForDomain:]_block_invoke.376
- __61-[UARPAssetManagerServiceInstance checkCacheForSubscription:]_block_invoke.358
- __70-[UARPAssetManagerServiceInstance listener:shouldAcceptNewConnection:]_block_invoke.332
CStrings:
+ "<%@: modelNumber=%@, hwFusing=%@ assetLocation=%@ url=%@ domain=%@>"
+ "<%@: modelNumber=%@, hwFusing=%@ assetLocation=%@/%u activeVersion=%@/%u variant=%u force=%u url=%@ domain=%@>"
+ "Failed to read profile with error %{public}@"
+ "Invalid profile asset URL override %{public}@"
+ "T@\"NSString\",C,V_pallasServerURL"
+ "Using profile settings for asset %{public}@ and url %{public}@"
+ "_pallasServerURL"
+ "cd060049-2465-43e3-bbb5-d769a66da2d7"
+ "ffc25f86-b83c-4139-b8ad-91131d0e5429"
+ "http"
+ "https://gdmf-auth-stg.apple.com/v2/assets"
+ "initWithUUIDString:"
+ "pallasServerURL"
+ "pallasURL"
+ "setPallasServerURL:"
- "<%@: modelNumber=%@, hwFusing=%@ assetLocation=%@ domain=%@>"
- "<%@: modelNumber=%@, hwFusing=%@ assetLocation=%@/%u activeVersion=%@/%u variant=%u force=%u domain=%@>"

```
