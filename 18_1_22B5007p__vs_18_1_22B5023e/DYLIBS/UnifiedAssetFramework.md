## UnifiedAssetFramework

> `/System/Library/PrivateFrameworks/UnifiedAssetFramework.framework/UnifiedAssetFramework`

```diff

-3400.107.1.0.0
-  __TEXT.__text: 0x5c2e4
-  __TEXT.__auth_stubs: 0xaa0
-  __TEXT.__objc_methlist: 0x2d38
+3401.7.2.0.0
+  __TEXT.__text: 0x5d418
+  __TEXT.__auth_stubs: 0xad0
+  __TEXT.__objc_methlist: 0x2da8
   __TEXT.__const: 0xf8
-  __TEXT.__gcc_except_tab: 0xf14
-  __TEXT.__cstring: 0x8b53
-  __TEXT.__oslogstring: 0xa0ed
+  __TEXT.__gcc_except_tab: 0xf74
+  __TEXT.__cstring: 0x8c68
+  __TEXT.__oslogstring: 0xa205
   __TEXT.__dlopen_cstrs: 0x296
-  __TEXT.__unwind_info: 0xf20
+  __TEXT.__unwind_info: 0xf78
   __TEXT.__objc_classname: 0x3f5
-  __TEXT.__objc_methname: 0x8fd6
-  __TEXT.__objc_methtype: 0xdaf
-  __TEXT.__objc_stubs: 0x75e0
+  __TEXT.__objc_methname: 0x91e5
+  __TEXT.__objc_methtype: 0xde8
+  __TEXT.__objc_stubs: 0x76e0
   __DATA_CONST.__got: 0x4c0
-  __DATA_CONST.__const: 0x1808
+  __DATA_CONST.__const: 0x1890
   __DATA_CONST.__objc_classlist: 0x150
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2320
+  __DATA_CONST.__objc_selrefs: 0x2378
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xe0
   __DATA_CONST.__objc_arraydata: 0xd8
-  __AUTH_CONST.__auth_got: 0x560
+  __AUTH_CONST.__auth_got: 0x578
   __AUTH_CONST.__const: 0x5c0
-  __AUTH_CONST.__cfstring: 0x3a80
-  __AUTH_CONST.__objc_const: 0x4140
+  __AUTH_CONST.__cfstring: 0x3b20
+  __AUTH_CONST.__objc_const: 0x4170
   __AUTH_CONST.__objc_intobj: 0x240
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH.__objc_data: 0x190
-  __DATA.__objc_ivar: 0x308
+  __AUTH.__objc_data: 0x50
+  __DATA.__objc_ivar: 0x30c
   __DATA.__data: 0x230
-  __DATA.__bss: 0x18
-  __DATA_DIRTY.__objc_data: 0xb90
+  __DATA.__bss: 0x20
+  __DATA_DIRTY.__objc_data: 0xcd0
   __DATA_DIRTY.__bss: 0x2f0
   __DATA_DIRTY.__common: 0x60
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 1260
-  Symbols:   1831
-  CStrings:  3251
+  Functions: 1277
+  Symbols:   1853
+  CStrings:  3279
 
Symbols:
+ _kUAFStorageErrorDomain
+ _kUAFSubjectToAppleIntelligenceWaitlist
+ _notify_get_state
+ _notify_register_check
+ _sqlite3_errstr
CStrings:
+ "%!s(MISSING) Asset set %!{(MISSING)public}@ is not allowed on this device"
+ "%!s(MISSING) Could not load asset set %!{(MISSING)public}@ from URL %!{(MISSING)public}@: %!{(MISSING)public}@"
+ "%!s(MISSING) Could not read system usages from database: %!@(MISSING)"
+ "%!s(MISSING) Failed to determine if Apple Intelligence Assets allowed: %!{(MISSING)public}@"
+ "%!s(MISSING) Inexpensive network available and game mode disabled, skipping on-boot activity registration"
+ "%!s(MISSING) Scheduling on-boot activity for next opportunity: Inexpensive network availability: %!d(MISSING), GameMode: %!d(MISSING)"
+ "+[UAFAssetSetManager configureAssetDelivery:configurationManager:lockIfUnchanged:subscriptions:assetSetUsages:]"
+ "+[UAFAssetSetManager subscribe:subscriptions:storeManager:configurationManager:]_block_invoke"
+ "+[UAFAssetSetManager unsubscribe:subscriptions:storeManager:configurationManager:]_block_invoke"
+ "+[UAFCommonUtilities gmsAllowsAssets]_block_invoke"
+ "-[UAFSubscriptionStoreManager _updateSystemAssetSetUsages:assetSetUsages:configurationManager:]"
+ "-[UAFSubscriptionStoreManager doDatabaseOperation:useTransaction:logDescription:error:]_block_invoke"
+ "-[UAFSubscriptionStoreManager getAllSystemAssetSetUsages:]_block_invoke"
+ "B20@0:8I16"
+ "B8@?0"
+ "CH"
+ "RegionCode"
+ "SubjectToAppleIntelligenceWaitlist"
+ "TB,N,V_subjectToAppleIntelligenceWaitlist"
+ "_subjectToAppleIntelligenceWaitlist"
+ "_updateSystemAssetSetUsages:assetSetUsages:configurationManager:"
+ "arrayWithArray:"
+ "com.apple.UnifiedAssetFramework.Storage"
+ "com.apple.siri.assistant.xr"
+ "com.apple.system.console_mode_changed"
+ "configureAssetDelivery:configurationManager:lockIfUnchanged:subscriptions:assetSetUsages:"
+ "doDatabaseOperation:useTransaction:logDescription:error:"
+ "getAllSystemAssetSetUsages:"
+ "getShouldNotDownloadOrServeAppleIntelligenceAssetsWithCompletionHandler:"
+ "gmsAllowsAssets"
+ "i40@0:8^@16^@24@32"
+ "i44@0:8@?16B24@28^@36"
+ "isChinaDeviceRegionCode"
+ "isGameModeEnabled"
+ "manageXRSubscription:subscribe:"
+ "setSubjectToAppleIntelligenceWaitlist:"
+ "subjectToAppleIntelligenceWaitlist"
+ "userIsValidForAssetSetManagement:"
+ "v52@0:8@16@24B32@36@44"
- "%!s(MISSING) Inexpensive network available, skipping on-boot activity registration"
- "%!s(MISSING) Inexpensive network unavailable, scheduling on-boot activity for when it becomes available"
- "+[UAFAssetSetManager configureAssetDelivery:configurationManager:lockIfUnchanged:]"
- "+[UAFAssetSetManager subscribe:subscriptions:storeManager:configurationManager:]"
- "+[UAFAssetSetManager unsubscribe:subscriptions:storeManager:configurationManager:]"
- "-[UAFSubscriptionStoreManager doDatabaseOperation:useTransaction:logDescription:]_block_invoke"
- "-[UAFSubscriptionStoreManager getAllSystemAssetSetUsages]_block_invoke"
- "-[UAFSubscriptionStoreManager updateSystemAssetSetUsages:configurationManager:]_block_invoke"
- "doDatabaseOperation:useTransaction:logDescription:"
- "getAllSystemAssetSetUsages"
- "i36@0:8@?16B24@28"

```
