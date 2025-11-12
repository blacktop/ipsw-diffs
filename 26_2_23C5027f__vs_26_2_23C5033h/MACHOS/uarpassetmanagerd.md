## uarpassetmanagerd

> `/usr/libexec/uarpassetmanagerd`

```diff

-1338.60.16.0.0
-  __TEXT.__text: 0x24d9c
-  __TEXT.__auth_stubs: 0x450
-  __TEXT.__objc_stubs: 0x2260
+1338.60.22.0.0
+  __TEXT.__text: 0x25904
+  __TEXT.__auth_stubs: 0x490
+  __TEXT.__objc_stubs: 0x22a0
   __TEXT.__objc_methlist: 0x1124
-  __TEXT.__cstring: 0x27c0
-  __TEXT.__oslogstring: 0x15a9
-  __TEXT.__objc_methname: 0x2846
+  __TEXT.__cstring: 0x2834
+  __TEXT.__oslogstring: 0x1608
+  __TEXT.__objc_methname: 0x28aa
   __TEXT.__objc_classname: 0x2db
-  __TEXT.__objc_methtype: 0x800
+  __TEXT.__objc_methtype: 0x80f
   __TEXT.__gcc_except_tab: 0x1a0
   __TEXT.__unwind_info: 0x360
-  __DATA_CONST.__auth_got: 0x238
-  __DATA_CONST.__got: 0x180
-  __DATA_CONST.__const: 0x1e90
-  __DATA_CONST.__cfstring: 0x2760
+  __DATA_CONST.__auth_got: 0x258
+  __DATA_CONST.__got: 0x188
+  __DATA_CONST.__const: 0x1f38
+  __DATA_CONST.__cfstring: 0x27c0
   __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x60

   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x70
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0x2b30
-  __DATA.__objc_selrefs: 0xad0
-  __DATA.__objc_ivar: 0x15c
+  __DATA.__objc_const: 0x2b50
+  __DATA.__objc_selrefs: 0xae0
+  __DATA.__objc_ivar: 0x160
   __DATA.__objc_data: 0x4b0
   __DATA.__data: 0x480
   __DATA.__bss: 0x40

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E02FE6EC-5597-3171-88F2-928A3BFFF637
+  UUID: FF4AF8C3-B46B-3AB0-8E96-3E3DA94326F4
   Functions: 416
-  Symbols:   4876
-  CStrings:  1420
+  Symbols:   4926
+  CStrings:  1431
 
Symbols:
+ -[UARPAssetManagerController assetAvailabilityUpdateForPersonality:serialNumbers:assetVersion:creationDate:status:]
+ -[UARPAssetManagerServiceInstanceMobileAsset assetAvailabilityUpdateForPersonality:serialNumbers:assetVersion:creationDate:status:]
+ OBJC_IVAR_$_UARPAssetManagerController._lastSettingsPaneTriggeredCacheRefreshDate
+ _INTERNAL_PALLAS_SERVER_URL_V2_AUTH
+ _MA_PALLAS_AUDIENCE_CUSTOMER_SEASHIP
+ _MA_PALLAS_AUDIENCE_INTERNAL_SEASHIP
+ __44-[UARPAssetManagerServiceInstance copyCache]_block_invoke.369
+ __46-[UARPAssetManagerServiceInstance primeCache:]_block_invoke.389
+ __46-[UARPAssetManagerServiceInstance queryIsBusy]_block_invoke.375
+ __49-[UARPAssetManagerServiceInstance checkForUpdate]_block_invoke.374
+ __52-[UARPAssetManagerServiceInstance copySubscriptions]_block_invoke.371
+ __59-[UARPAssetManagerServiceInstance registerForSubscription:]_block_invoke.373
+ __60-[UARPAssetManagerServiceInstance clearAssetCacheForDomain:]_block_invoke.384
+ __61-[UARPAssetManagerServiceInstance checkCacheForSubscription:]_block_invoke.366
+ __70-[UARPAssetManagerServiceInstance listener:shouldAcceptNewConnection:]_block_invoke.341
+ _kUARPAssetAvailabilityXPCEventSerialNumbersKey
+ _objc_msgSend$assetAvailabilityUpdateForPersonality:serialNumbers:assetVersion:creationDate:status:
+ _objc_msgSend$isPersonalityMatch:
+ _objc_msgSend$timeIntervalSinceDate:
+ _xpc_array_append_value
+ _xpc_array_create
+ _xpc_dictionary_set_value
+ _xpc_string_create
- -[UARPAssetManagerController assetAvailabilityUpdateForPersonality:assetVersion:creationDate:status:]
- -[UARPAssetManagerServiceInstanceMobileAsset assetAvailabilityUpdateForPersonality:assetVersion:creationDate:status:]
- __44-[UARPAssetManagerServiceInstance copyCache]_block_invoke.360
- __46-[UARPAssetManagerServiceInstance primeCache:]_block_invoke.380
- __46-[UARPAssetManagerServiceInstance queryIsBusy]_block_invoke.366
- __49-[UARPAssetManagerServiceInstance checkForUpdate]_block_invoke.365
- __52-[UARPAssetManagerServiceInstance copySubscriptions]_block_invoke.362
- __59-[UARPAssetManagerServiceInstance registerForSubscription:]_block_invoke.364
- __60-[UARPAssetManagerServiceInstance clearAssetCacheForDomain:]_block_invoke.375
- __61-[UARPAssetManagerServiceInstance checkCacheForSubscription:]_block_invoke.357
- __70-[UARPAssetManagerServiceInstance listener:shouldAcceptNewConnection:]_block_invoke.332
- _objc_msgSend$assetAvailabilityUpdateForPersonality:assetVersion:creationDate:status:
Functions:
~ -[UARPAssetManagerServiceInstanceMobileAsset subscribeForPersonality:] : 1880 -> 1892
~ -[UARPAssetManagerServiceInstanceMobileAsset assetAvailabilityUpdateForSubscription:cacheRecord:asyncUpdate:] : 2084 -> 4084
~ -[UARPAssetManagerServiceInstanceMobileAsset assetAvailabilityUpdateForPersonality:assetVersion:creationDate:status:] -> -[UARPAssetManagerServiceInstanceMobileAsset assetAvailabilityUpdateForPersonality:serialNumbers:assetVersion:creationDate:status:] : 228 -> 268
~ -[UARPAssetManagerController assetAvailabilityUpdateForPersonality:assetVersion:creationDate:status:] -> -[UARPAssetManagerController assetAvailabilityUpdateForPersonality:serialNumbers:assetVersion:creationDate:status:] : 1504 -> 2076
~ -[UARPAssetManagerController settingsChangedForSerialNumber:] : 280 -> 560
~ -[UARPAssetManagerController .cxx_destruct] : 172 -> 188
CStrings:
+ "%s Comparing %@ with test subscription %@"
+ "Attempting periodic cache refresh since last time %@"
+ "_lastSettingsPaneTriggeredCacheRefreshDate"
+ "assetAvailabilityUpdateForPersonality:serialNumbers:assetVersion:creationDate:status:"
+ "cd060049-2465-43e3-bbb5-d769a66da2d7"
+ "ffc25f86-b83c-4139-b8ad-91131d0e5429"
+ "https://gdmf-auth-stg.apple.com/v2/assets"
+ "isPersonalityMatch:"
+ "timeIntervalSinceDate:"
+ "v56@0:8@\"UARPEndpointPersonality\"16@\"NSArray\"24@\"UARPAssetVersionBase\"32@\"NSDate\"40q48"
+ "v56@0:8@16@24@32@40q48"
- "assetAvailabilityUpdateForPersonality:assetVersion:creationDate:status:"
- "v48@0:8@\"UARPEndpointPersonality\"16@\"UARPAssetVersionBase\"24@\"NSDate\"32q40"
- "v48@0:8@16@24@32q40"

```
