## UnifiedAssetFramework

> `/System/Library/PrivateFrameworks/UnifiedAssetFramework.framework/UnifiedAssetFramework`

```diff

-3605.17.1.0.0
-  __TEXT.__text: 0x75828
-  __TEXT.__objc_methlist: 0x3690
+3610.10.1.0.0
+  __TEXT.__text: 0x76060
+  __TEXT.__objc_methlist: 0x36f0
   __TEXT.__const: 0x198
   __TEXT.__constg_swiftt: 0x48
   __TEXT.__swift5_typeref: 0x67
   __TEXT.__swift5_reflstr: 0x9
   __TEXT.__swift5_fieldmd: 0x1c
-  __TEXT.__cstring: 0xb7c6
-  __TEXT.__oslogstring: 0xf0c7
+  __TEXT.__cstring: 0xb8b9
+  __TEXT.__oslogstring: 0xf1bb
   __TEXT.__swift5_types: 0x4
   __TEXT.__gcc_except_tab: 0xe0c
-  __TEXT.__unwind_info: 0x15b0
+  __TEXT.__unwind_info: 0x15e0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1d10
+  __DATA_CONST.__const: 0x1d38
   __DATA_CONST.__objc_classlist: 0x1b0
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2630
+  __DATA_CONST.__objc_selrefs: 0x2670
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xf0
   __DATA_CONST.__objc_arraydata: 0x128
   __DATA_CONST.__got: 0x550
   __AUTH_CONST.__const: 0x608
-  __AUTH_CONST.__cfstring: 0x5520
-  __AUTH_CONST.__objc_const: 0x4630
+  __AUTH_CONST.__cfstring: 0x56a0
+  __AUTH_CONST.__objc_const: 0x4660
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_intobj: 0x1f8
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__auth_got: 0x8a0
   __AUTH.__objc_data: 0x98
-  __DATA.__objc_ivar: 0x320
+  __DATA.__objc_ivar: 0x324
   __DATA.__data: 0x298
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x1018

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 1457
-  Symbols:   2750
-  CStrings:  2146
+  Functions: 1467
+  Symbols:   2761
+  CStrings:  2164
 
Symbols:
+ +[UAFSubscriptionStoreManager _reportsDatabaseFailuresInProcess:]
+ +[UAFSubscriptionStoreManager _reportsDatabaseFailures]
+ -[UAFOSEligibility isMainlandChina]
+ -[UAFSubscriptionStoreManager _enumerateSubscriptionsByName:user:usingBlock:]
+ -[UAFSubscriptionStoreManager _reportCorruption:]
+ -[UAFSubscriptionStoreManager _reportFailedReset:error:]
+ -[UAFSubscriptionStoreManager _reportFailedWrite:]
+ -[UAFSubscriptionStoreManager _reportFailureToABC:context:]
+ -[UAFSubscriptionStoreManager _reportSkippedRows:]
+ GCC_except_table104
+ GCC_except_table112
+ GCC_except_table44
+ GCC_except_table48
+ GCC_except_table62
+ GCC_except_table64
+ GCC_except_table67
+ GCC_except_table74
+ GCC_except_table81
+ GCC_except_table85
+ GCC_except_table87
+ _OBJC_IVAR_$_UAFOSEligibility._isMainlandChina
+ ___54-[UAFSubscriptionStoreManager _getSubscriptions:user:]_block_invoke
+ ___66-[UAFSubscriptionStoreManager _getSubscriptionsAsDictionary:user:]_block_invoke
+ ___block_descriptor_40_e8_32s_e33_v16?0"UAFAssetSetSubscription"8ls32l8
+ _gReportedFailures
- -[UAFSubscriptionStoreManager _getSubscriptionsAsDictionary:subscriptionsFor:]
- GCC_except_table101
- GCC_except_table103
- GCC_except_table109
- GCC_except_table37
- GCC_except_table41
- GCC_except_table46
- GCC_except_table49
- GCC_except_table53
- GCC_except_table65
- GCC_except_table72
- GCC_except_table76
- GCC_except_table88
- GCC_except_table95
CStrings:
+ "%@ %@"
+ "%@ %ld"
+ "%s Could not enable fullfsync SQLite error: %d (%s, Extended: %d)"
+ "%s Failed to read subscription '%{public}@' for %{public}@"
+ "%s No country policy value found"
+ "%s Reading db version from DbVersion table failed SQLite error: %d (%s, Extended: %d)"
+ "%s Skipped %lu rows of Subscriptions that don't read while reading all subscriptions"
+ "-[UAFOSEligibility _updateCountryPolicy:]"
+ "-[UAFSubscriptionStoreManager _enumerateSubscriptionsByName:user:usingBlock:]"
+ "-[UAFSubscriptionStoreManager _reportSkippedRows:]"
+ "EligibleAppleIntelligenceIsMainlandChina"
+ "OS_ELIGIBILITY_CONTEXT_COUNTRY_POLICY"
+ "PRAGMA fullfsync = ON"
+ "SELECT k1 FROM Subscriptions WHERE k0 = ? AND k4 = ?"
+ "Subscriptions:%lu"
+ "assetsubscriptiond"
+ "com.apple.MobileAsset.CN.Guardrail"
+ "corruption"
+ "move"
+ "open"
+ "prepare"
+ "reset"
+ "reset failed"
+ "skipped rows"
+ "v16@?0@\"UAFAssetSetSubscription\"8"
- "%s Failed to read subscription: %s"
- "%s Reading db version from DbVersion table failed"
- "-[UAFSubscriptionStoreManager _getAllSubscriptions:]"
- "-[UAFSubscriptionStoreManager _getAllSubscriptionsFlat:]"
- "-[UAFSubscriptionStoreManager _getSubscriptionsAsDictionary:subscriptionsFor:]"
- "CAReportingAssetSet"
- "SELECT k2 FROM Subscriptions WHERE k0 = ? AND k4 = ?"
```
