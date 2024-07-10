## UnifiedAssetFramework

> `/System/Library/PrivateFrameworks/UnifiedAssetFramework.framework/Versions/A/UnifiedAssetFramework`

```diff

-3400.102.1.0.0
-  __TEXT.__text: 0x64830
+3400.96.3.4.1
+  __TEXT.__text: 0x62aa8
   __TEXT.__auth_stubs: 0x8d0
-  __TEXT.__objc_methlist: 0x2cc8
+  __TEXT.__objc_methlist: 0x2c64
   __TEXT.__const: 0xf0
-  __TEXT.__gcc_except_tab: 0xea8
-  __TEXT.__cstring: 0x8a67
-  __TEXT.__oslogstring: 0x9ef1
-  __TEXT.__dlopen_cstrs: 0x296
-  __TEXT.__unwind_info: 0xf48
+  __TEXT.__gcc_except_tab: 0xdfc
+  __TEXT.__cstring: 0x8777
+  __TEXT.__oslogstring: 0x9d73
+  __TEXT.__dlopen_cstrs: 0x238
+  __TEXT.__unwind_info: 0xed8
   __TEXT.__objc_classname: 0x3e1
-  __TEXT.__objc_methname: 0x8f7f
-  __TEXT.__objc_methtype: 0xdc0
-  __TEXT.__objc_stubs: 0x7580
+  __TEXT.__objc_methname: 0x8ea9
+  __TEXT.__objc_methtype: 0xdca
+  __TEXT.__objc_stubs: 0x73c0
   __DATA_CONST.__got: 0x4b0
-  __DATA_CONST.__const: 0x7c0
+  __DATA_CONST.__const: 0x798
   __DATA_CONST.__objc_classlist: 0x148
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2308
+  __DATA_CONST.__objc_selrefs: 0x22b0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xd8
   __DATA_CONST.__objc_arraydata: 0xd8
   __AUTH_CONST.__auth_got: 0x478
-  __AUTH_CONST.__const: 0x1860
-  __AUTH_CONST.__cfstring: 0x3a80
-  __AUTH_CONST.__objc_const: 0x4000
+  __AUTH_CONST.__const: 0x1750
+  __AUTH_CONST.__cfstring: 0x3a00
+  __AUTH_CONST.__objc_const: 0x4060
   __AUTH_CONST.__objc_intobj: 0x240
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0xcd0
-  __DATA.__objc_ivar: 0x2f8
+  __DATA.__objc_ivar: 0x300
   __DATA.__data: 0x230
-  __DATA.__bss: 0x308
+  __DATA.__bss: 0x2e8
   __DATA.__common: 0x60
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 1307
-  Symbols:   3492
-  CStrings:  924
+  Functions: 1288
+  Symbols:   3447
+  CStrings:  908
 
Symbols:
+ +[UAFAssetSetManager downloadStatus:subscription:storeManager:configurationManager:]
+ +[UAFManagedSubscriptions manageSubscription:subscriber:assetSets:usageAliases:]
+ -[UAFAssetSetManager configurationManager]
+ -[UAFAssetSetManager setConfigurationManager:]
+ -[UAFAssetSetManager setSubscriptionStoreManager:]
+ -[UAFAssetSetManager subscriptionStoreManager]
+ GCC_except_table21
+ GCC_except_table39
+ GCC_except_table61
+ OBJC_IVAR_$_UAFAssetSetManager._configurationManager
+ OBJC_IVAR_$_UAFAssetSetManager._subscriptionStoreManager
+ __151-[UAFAssetSetManager updateAssetsForSubscriber:subscriptionName:policies:queue:progress:detailedProgress:completion:storeManager:configurationManager:]_block_invoke.290
+ __151-[UAFAssetSetManager updateAssetsForSubscriber:subscriptionName:policies:queue:progress:detailedProgress:completion:storeManager:configurationManager:]_block_invoke.293
+ __151-[UAFAssetSetManager updateAssetsForSubscriber:subscriptionName:policies:queue:progress:detailedProgress:completion:storeManager:configurationManager:]_block_invoke.298
+ __151-[UAFAssetSetManager updateAssetsForSubscriber:subscriptionName:policies:queue:progress:detailedProgress:completion:storeManager:configurationManager:]_block_invoke_2.294
+ __151-[UAFAssetSetManager updateAssetsForSubscriber:subscriptionName:policies:queue:progress:detailedProgress:completion:storeManager:configurationManager:]_block_invoke_2.299
+ __27-[UAFXPCService runUpdates]_block_invoke.289
+ __43+[UAFAssetSetManager getSystemUsageAssets:]_block_invoke.311
+ __43+[UAFAssetSetManager getSystemUsageAssets:]_block_invoke.315
+ __88-[UAFAssetSetManager disableCacheDelete:forAssetNamed:assetSet:usages:queue:completion:]_block_invoke.384
+ __block_literal_global.318
+ __block_literal_global.366
+ __block_literal_global.369
+ _objc_msgSend$downloadStatus:subscription:storeManager:configurationManager:
+ _objc_msgSend$manageSubscription:subscriber:assetSets:usageAliases:
- +[UAFAssetSetManager getComparableUsages:]
- +[UAFAssetSetManager shouldConfigure:newUsages:]
- +[UAFAutoAssetManager assetSetNamesFromUsages:configurationManager:]
- +[UAFAutoAssetManager autoAssetSetForStatus:]
- +[UAFAutoAssetManager getDownloadStatusFromAssetSetUsages:configurationManager:queue:completion:]
- +[UAFAutoAssetManager getDownloadStatusFromMAAutoAssetSetStatus:]
- +[UAFCommonUtilities gmsWantsAssets]
- +[UAFInstrumentationProvider defaultDeviceId]
- +[UAFInstrumentationProvider getPersistedDeviceId]
- +[UAFManagedSubscriptions manageGMSSiriLanguageSubscription:language:]
- +[UAFManagedSubscriptions manageSubscription:subscriber:assetSets:usageAliases:useHold:]
- -[UAFAssetSetManager assetSetUsagesForStatusForSubscriber:subscriptionName:status:]
- -[UAFAssetSetManager downloadStatusForSubscriber:subscriptionName:queue:completion:]
- -[UAFXPCService _assistantGMSAvailabilityUpdate]
- GCC_except_table22
- GCC_except_table59
- GCC_except_table63
- GCC_except_table72
- GCC_except_table74
- __151-[UAFAssetSetManager updateAssetsForSubscriber:subscriptionName:policies:queue:progress:detailedProgress:completion:storeManager:configurationManager:]_block_invoke.295
- __151-[UAFAssetSetManager updateAssetsForSubscriber:subscriptionName:policies:queue:progress:detailedProgress:completion:storeManager:configurationManager:]_block_invoke.299
- __151-[UAFAssetSetManager updateAssetsForSubscriber:subscriptionName:policies:queue:progress:detailedProgress:completion:storeManager:configurationManager:]_block_invoke.304
- __151-[UAFAssetSetManager updateAssetsForSubscriber:subscriptionName:policies:queue:progress:detailedProgress:completion:storeManager:configurationManager:]_block_invoke_2.300
- __151-[UAFAssetSetManager updateAssetsForSubscriber:subscriptionName:policies:queue:progress:detailedProgress:completion:storeManager:configurationManager:]_block_invoke_2.305
- __27-[UAFXPCService runUpdates]_block_invoke.292
- __43+[UAFAssetSetManager getSystemUsageAssets:]_block_invoke.317
- __43+[UAFAssetSetManager getSystemUsageAssets:]_block_invoke.321
- __84-[UAFAssetSetManager downloadStatusForSubscriber:subscriptionName:queue:completion:]_block_invoke.365
- __88-[UAFAssetSetManager disableCacheDelete:forAssetNamed:assetSet:usages:queue:completion:]_block_invoke.392
- __97+[UAFAutoAssetManager getDownloadStatusFromAssetSetUsages:configurationManager:queue:completion:]_block_invoke.425
- __GMSAvailabilityDidChangeCallback
- ___42+[UAFAssetSetManager getComparableUsages:]_block_invoke
- ___45+[UAFInstrumentationProvider defaultDeviceId]_block_invoke
- ___48+[UAFAssetSetManager shouldConfigure:newUsages:]_block_invoke
- ___84-[UAFAssetSetManager downloadStatusForSubscriber:subscriptionName:queue:completion:]_block_invoke
- ___97+[UAFAutoAssetManager getDownloadStatusFromAssetSetUsages:configurationManager:queue:completion:]_block_invoke
- ___GenerativeModelsLibraryCore_block_invoke
- ___block_descriptor_40_e8_32s_e34_v32?0"NSString"8"NSArray"16^B24l
- ___block_descriptor_48_e8_32bs40r_e5_v8?0l
- ___block_descriptor_56_e8_32bs40r_e8_v16?0Q8l
- ___block_descriptor_56_e8_32s40s48r_e32_v32?0"NSString"8"NSSet"16^B24l
- ___block_descriptor_56_e8_32s40s48s_e42_v24?0"MAAutoAssetSetStatus"8"NSError"16l
- ___copy_helper_block_e8_32b40r
- ___getGMAvailabilityWrapperClass_block_invoke
- __block_literal_global.290
- __block_literal_global.321
- __block_literal_global.363
- __block_literal_global.377
- _audit_stringGenerativeModels
- _kUAFGMSSiriSubscriber
- _kUAFGMSSiriSubscription
- _objc_msgSend$UUIDString
- _objc_msgSend$_assistantGMSAvailabilityUpdate
- _objc_msgSend$assetSetNamesFromUsages:configurationManager:
- _objc_msgSend$assetSetUsagesForStatusForSubscriber:subscriptionName:status:
- _objc_msgSend$autoAssetSetForStatus:
- _objc_msgSend$defaultDeviceId
- _objc_msgSend$getComparableUsages:
- _objc_msgSend$getDownloadStatusFromAssetSetUsages:configurationManager:queue:completion:
- _objc_msgSend$getDownloadStatusFromMAAutoAssetSetStatus:
- _objc_msgSend$getPersistedDeviceId
- _objc_msgSend$gmsWantsAssets
- _objc_msgSend$isOkayToHaveAsset
- _objc_msgSend$manageGMSSiriLanguageSubscription:language:
- _objc_msgSend$manageSubscription:subscriber:assetSets:usageAliases:useHold:
- _objc_msgSend$shouldConfigure:newUsages:
- _objc_msgSend$stringForKey:
CStrings:
+ "+[UAFAssetSetManager downloadStatus:subscription:storeManager:configurationManager:]"
+ "+[UAFManagedSubscriptions manageSubscription:subscriber:assetSets:usageAliases:]"
- "+[UAFAssetSetManager shouldConfigure:newUsages:]"
- "+[UAFAssetSetManager shouldConfigure:newUsages:]_block_invoke"
- "+[UAFAutoAssetManager assetSetNamesFromUsages:configurationManager:]"
- "+[UAFAutoAssetManager autoAssetSetForStatus:]"
- "+[UAFAutoAssetManager getDownloadStatusFromAssetSetUsages:configurationManager:queue:completion:]_block_invoke"
- "+[UAFAutoAssetManager getDownloadStatusFromMAAutoAssetSetStatus:]"
- "+[UAFManagedSubscriptions manageSubscription:subscriber:assetSets:usageAliases:useHold:]"
- "+[UAFPlatform configurationManagers:]"
- "-[UAFAssetSetManager assetSetUsagesForStatusForSubscriber:subscriptionName:status:]"
- "-[UAFXPCService _assistantGMSAvailabilityUpdate]"
- "/System/Library/PrivateFrameworks/GenerativeModels.framework/Contents/MacOS/GenerativeModels"
- "GMAvailabilityWrapper"
- "PersistedDeviceId"
- "com.apple.gms.availability.notification"
- "com.apple.siri.intelligenceengine"
- "en-US"
- "v16@?0Q8"
- "v32@?0@\"NSString\"8@\"NSSet\"16^B24"

```
