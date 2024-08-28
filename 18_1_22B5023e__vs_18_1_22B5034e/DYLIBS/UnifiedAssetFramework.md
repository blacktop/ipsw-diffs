## UnifiedAssetFramework

> `/System/Library/PrivateFrameworks/UnifiedAssetFramework.framework/UnifiedAssetFramework`

```diff

-3401.7.2.0.0
-  __TEXT.__text: 0x5d418
+3401.13.3.0.0
+  __TEXT.__text: 0x5dc44
   __TEXT.__auth_stubs: 0xad0
-  __TEXT.__objc_methlist: 0x2da8
+  __TEXT.__objc_methlist: 0x2db8
   __TEXT.__const: 0xf8
-  __TEXT.__gcc_except_tab: 0xf74
-  __TEXT.__cstring: 0x8c68
-  __TEXT.__oslogstring: 0xa205
+  __TEXT.__gcc_except_tab: 0x1004
+  __TEXT.__cstring: 0x8e24
+  __TEXT.__oslogstring: 0xa2b0
   __TEXT.__dlopen_cstrs: 0x296
-  __TEXT.__unwind_info: 0xf78
+  __TEXT.__unwind_info: 0xf90
   __TEXT.__objc_classname: 0x3f5
-  __TEXT.__objc_methname: 0x91e5
-  __TEXT.__objc_methtype: 0xde8
-  __TEXT.__objc_stubs: 0x76e0
+  __TEXT.__objc_methname: 0x92ab
+  __TEXT.__objc_methtype: 0xe0b
+  __TEXT.__objc_stubs: 0x7740
   __DATA_CONST.__got: 0x4c0
-  __DATA_CONST.__const: 0x1890
+  __DATA_CONST.__const: 0x18b8
   __DATA_CONST.__objc_classlist: 0x150
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2378
+  __DATA_CONST.__objc_selrefs: 0x2390
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xe0
   __DATA_CONST.__objc_arraydata: 0xd8
   __AUTH_CONST.__auth_got: 0x578
   __AUTH_CONST.__const: 0x5c0
-  __AUTH_CONST.__cfstring: 0x3b20
-  __AUTH_CONST.__objc_const: 0x4170
+  __AUTH_CONST.__cfstring: 0x3b80
+  __AUTH_CONST.__objc_const: 0x4190
   __AUTH_CONST.__objc_intobj: 0x240
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0x30c
+  __DATA.__objc_ivar: 0x310
   __DATA.__data: 0x230
   __DATA.__bss: 0x20
   __DATA_DIRTY.__objc_data: 0xcd0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 1277
-  Symbols:   1853
-  CStrings:  3279
+  Functions: 1280
+  Symbols:   1856
+  CStrings:  3294
 
CStrings:
+ "-[UAFSubscriptionStoreManager getAllSubscriptions:]_block_invoke"
+ "getAllSubscriptions:"
+ "%!s(MISSING) Failed to read subscription: %!s(MISSING)"
+ "+[UAFAutoAssetManager manageAssetSet:specifiers:lockIfUnchanged:userInitiated:]"
+ "B52@0:8@16@24@32@40B48"
+ "persistAssetSetInfoConfiguring:entries:isEliminating:reason:"
+ "allValues"
+ "+[UAFAutoAssetManager manageAssetSet:specifiers:lockIfUnchanged:userInitiated:]_block_invoke_2"
+ "%!s(MISSING) Apple Intelligence Assets GMS allowed state: %!{(MISSING)public}@"
+ "+[UAFAutoAssetManager manageAssetSet:specifiers:lockIfUnchanged:userInitiated:]_block_invoke"
+ "manageSubscription:subscriber:assetSets:usageAliases:useHold:userInitiated:"
+ "%!s(MISSING) Checking auto asset set %!{(MISSING)public}@ with cellular: %!d(MISSING) user initiated: %!d(MISSING)"
+ "\xf0R"
+ "+[UAFAutoAssetHistory persistAssetSetInfoConfiguring:entries:isEliminating:reason:]"
+ "+[UAFAssetSetManager unsubscribe:subscriptions:storeManager:configurationManager:userInitiated:]_block_invoke_2"
+ "v32@?0@\"NSArray\"8Q16^B24"
+ "configureAutoAssetsFromAssetSetUsages:subscriptions:configurationManager:lockIfUnchanged:userInitiated:"
+ "dictionaryWithObjects:forKeys:"
+ "SELECT k2, k0 FROM Subscriptions"
+ "Ok to download or serve"
+ "+[UAFManagedSubscriptions manageSubscription:subscriber:assetSets:usageAliases:useHold:userInitiated:]"
+ "v56@0:8@16@24B32@36@44B52"
+ "manageAssetSet:specifiers:lockIfUnchanged:userInitiated:"
+ "v56@0:8@16@24@32@40B48B52"
+ "unsubscribe:subscriptions:storeManager:configurationManager:userInitiated:"
+ "v44@0:8@16@24B32@36"
+ "get all subscriptions"
+ "+[UAFAutoAssetManager configureAutoAssetsFromAssetSetUsages:subscriptions:configurationManager:lockIfUnchanged:userInitiated:]"
+ "_readAllSubscriptionsAndSubscribers"
+ "configureAssetDelivery:configurationManager:lockIfUnchanged:subscriptions:assetSetUsages:userInitiated:"
+ "+[UAFAssetSetManager unsubscribe:subscriptions:storeManager:configurationManager:userInitiated:]_block_invoke"
+ "+[UAFAssetSetManager configureAssetDelivery:configurationManager:lockIfUnchanged:subscriptions:assetSetUsages:userInitiated:]"
+ "+[UAFAssetSetManager subscribe:subscriptions:storeManager:configurationManager:userInitiated:]_block_invoke"
+ "_getAutoAssetSetInfo:entries:includeAssetVersion:"
+ "+[UAFAutoAssetManager configureAutoAssetsFromAssetSetUsages:subscriptions:configurationManager:lockIfUnchanged:userInitiated:]_block_invoke"
+ "%!s(MISSING) Could not read subscriptions from database: %!{(MISSING)public}@"
+ "subscribe:subscriptions:storeManager:configurationManager:userInitiated:"
+ "Should not download or serve"
+ "v48@0:8@16@24@32B40B44"
- "+[UAFAssetSetManager subscribe:subscriptions:storeManager:configurationManager:]_block_invoke"
- "subscribe:subscriptions:storeManager:configurationManager:"
- "manageAssetSet:specifiers:lockIfUnchanged:"
- "configureAssetDelivery:configurationManager:lockIfUnchanged:subscriptions:assetSetUsages:"
- "manageSubscription:subscriber:assetSets:usageAliases:useHold:"
- "v36@0:8@16B24@28"
- "+[UAFAutoAssetHistory persistAssetSetInfoConfiguring:isEliminating:reason:]"
- "+[UAFAutoAssetManager manageAssetSet:specifiers:lockIfUnchanged:]"
- "v44@0:8@16@24@32B40"
- "v52@0:8@16@24@32@40B48"
- "+[UAFAutoAssetManager manageAssetSet:specifiers:lockIfUnchanged:]_block_invoke_2"
- "+[UAFAutoAssetManager configureAutoAssetsFromAssetSetUsages:subscriptions:configurationManager:lockIfUnchanged:]_block_invoke"
- "\xf0B"
- "configureAutoAssetsFromAssetSetUsages:subscriptions:configurationManager:lockIfUnchanged:"
- "_getAutoAssetSetInfo:includeAssetVersion:"
- "+[UAFAssetSetManager configureAssetDelivery:configurationManager:lockIfUnchanged:subscriptions:assetSetUsages:]"
- "v52@0:8@16@24B32@36@44"
- "+[UAFAutoAssetManager manageAssetSet:specifiers:lockIfUnchanged:]_block_invoke"
- "+[UAFAutoAssetManager configureAutoAssetsFromAssetSetUsages:subscriptions:configurationManager:lockIfUnchanged:]"
- "+[UAFAssetSetManager unsubscribe:subscriptions:storeManager:configurationManager:]_block_invoke"
- "persistAssetSetInfoConfiguring:isEliminating:reason:"
- "%!s(MISSING) Checking auto asset set %!{(MISSING)public}@ with cellular: %!d(MISSING)"
- "+[UAFManagedSubscriptions manageSubscription:subscriber:assetSets:usageAliases:useHold:]"
- "unsubscribe:subscriptions:storeManager:configurationManager:"

```
