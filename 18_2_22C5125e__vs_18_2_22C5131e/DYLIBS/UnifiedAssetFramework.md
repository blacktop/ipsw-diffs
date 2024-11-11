## UnifiedAssetFramework

> `/System/Library/PrivateFrameworks/UnifiedAssetFramework.framework/UnifiedAssetFramework`

```diff

-3402.62.2.1.1
-  __TEXT.__text: 0x6258c
+3402.65.1.0.0
+  __TEXT.__text: 0x62da8
   __TEXT.__auth_stubs: 0xae0
-  __TEXT.__objc_methlist: 0x30e0
+  __TEXT.__objc_methlist: 0x30f0
   __TEXT.__const: 0xf8
-  __TEXT.__gcc_except_tab: 0x1084
-  __TEXT.__cstring: 0x948e
-  __TEXT.__oslogstring: 0xab88
+  __TEXT.__gcc_except_tab: 0x10b0
+  __TEXT.__cstring: 0x95ce
+  __TEXT.__oslogstring: 0xadfa
   __TEXT.__dlopen_cstrs: 0x296
-  __TEXT.__unwind_info: 0x10d8
+  __TEXT.__unwind_info: 0x10e0
   __TEXT.__objc_classname: 0x411
-  __TEXT.__objc_methname: 0x98bb
-  __TEXT.__objc_methtype: 0xeac
-  __TEXT.__objc_stubs: 0x7b20
+  __TEXT.__objc_methname: 0x98de
+  __TEXT.__objc_methtype: 0xeae
+  __TEXT.__objc_stubs: 0x7b60
   __DATA_CONST.__got: 0x4d0
   __DATA_CONST.__const: 0x1a18
   __DATA_CONST.__objc_classlist: 0x158

   __DATA_CONST.__objc_superrefs: 0xe8
   __DATA_CONST.__objc_arraydata: 0xd8
   __AUTH_CONST.__auth_got: 0x580
-  __AUTH_CONST.__const: 0x5e0
+  __AUTH_CONST.__const: 0x600
   __AUTH_CONST.__cfstring: 0x3e60
-  __AUTH_CONST.__objc_const: 0x44b0
+  __AUTH_CONST.__objc_const: 0x44d0
   __AUTH_CONST.__objc_intobj: 0x240
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0x334
+  __DATA.__objc_ivar: 0x338
   __DATA.__data: 0x230
   __DATA.__bss: 0x20
   __DATA_DIRTY.__objc_data: 0xd20

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 1354
-  Symbols:   1939
-  CStrings:  3436
+  Functions: 1356
+  Symbols:   1941
+  CStrings:  3449
 
CStrings:
+ "\x04\x12"
+ "%!s(MISSING) %!{(MISSING)public}@: Checking %!{(MISSING)public}@ with expensive: %!d(MISSING)"
+ "%!s(MISSING) Auto asset set %!{(MISSING)public}@ is configured, has atomic instance %!{(MISSING)public}@, and is available to clients but current OS is not supported"
+ "%!s(MISSING) AutoAssetSet %!{(MISSING)public}@ not previously initialized. Creating a new one for staging."
+ "%!s(MISSING) Could not determine status for set %!{(MISSING)public}@ : %!{(MISSING)public}@"
+ "%!s(MISSING) Downloading assets for subscriber: %!{(MISSING)public}@ and subscription: %!{(MISSING)public}@"
+ "%!s(MISSING) Failed to get all subscriptions due to error: %!@(MISSING). Stopping staging"
+ "%!s(MISSING) Returning asset download status: %!l(MISSING)u for subscriber: %!{(MISSING)public}@ and subscription: %!{(MISSING)public}@"
+ "%!s(MISSING) Returning status: %!l(MISSING)u for subscriber: %!{(MISSING)public}@ and subscription: %!{(MISSING)public}@ as the asset set usages are nil"
+ "%!s(MISSING) Staging assets due to receiving MA notification for platform assets"
+ "+[UAFAutoAssetManager targetForAssetSet:specifiers:version:autoAssetSets:]"
+ "+[UAFManagedSubscriptions _stageAssetsUponPlatformAssetSetUpdate]"
+ "-[UAFAssetSetManager downloadStatusForSubscriber:subscriptionName:]"
+ "-[UAFAssetSetManager downloadStatusForSubscriber:subscriptionName:queue:completion:]"
+ "-[UAFAssetSetManager downloadStatusForSubscriber:subscriptionName:queue:completion:]_block_invoke_2"
+ "_platformAssetSetObserver"
+ "_stageAssetsUponPlatformAssetSetUpdate"
+ "targetForAssetSet:specifiers:version:autoAssetSets:"
- "\x03\x12"
- "%!s(MISSING) %!{(MISSING)public}@: Checking %!{(MISSING)public}@ with cellular: %!d(MISSING)"
- "%!s(MISSING) AutoAssetSet %!{(MISSING)public}@ not previously initialized.  Creating a new one for staging."
- "+[UAFAutoAssetManager targetForAssetSet:specifiers:version:autoAssetSet:]"
- "allowCheckDownloadOverCellular"
- "targetForAssetSet:specifiers:version:autoAssetSet:"

```
