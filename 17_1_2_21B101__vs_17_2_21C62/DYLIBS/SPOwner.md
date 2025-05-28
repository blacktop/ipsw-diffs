## SPOwner

> `/System/Library/PrivateFrameworks/SPOwner.framework/SPOwner`

```diff

-355.1.6.0.1
-  __TEXT.__text: 0x64d24
-  __TEXT.__auth_stubs: 0xbe0
-  __TEXT.__objc_methlist: 0x8198
-  __TEXT.__cstring: 0x5c07
+356.7.0.0.0
+  __TEXT.__text: 0x64e9c
+  __TEXT.__auth_stubs: 0xc00
+  __TEXT.__objc_methlist: 0x81b0
+  __TEXT.__cstring: 0x5c37
   __TEXT.__const: 0x370
   __TEXT.__gcc_except_tab: 0x1204
-  __TEXT.__oslogstring: 0x61c8
+  __TEXT.__oslogstring: 0x61e9
   __TEXT.__dlopen_cstrs: 0x5a
   __TEXT.__swift5_typeref: 0x122
   __TEXT.__swift5_fieldmd: 0xfc

   __TEXT.__swift5_types: 0x14
   __TEXT.__swift5_assocty: 0x18
   __TEXT.__swift5_capture: 0x38
-  __TEXT.__unwind_info: 0x22e8
+  __TEXT.__unwind_info: 0x22fc
   __TEXT.__eh_frame: 0x240
   __TEXT.__objc_classname: 0xf47
-  __TEXT.__objc_methname: 0x10467
+  __TEXT.__objc_methname: 0x10485
   __TEXT.__objc_methtype: 0x306d
-  __TEXT.__objc_stubs: 0x9760
+  __TEXT.__objc_stubs: 0x9780
   __DATA_CONST.__got: 0x100
-  __DATA_CONST.__const: 0x1e10
+  __DATA_CONST.__const: 0x1e18
   __DATA_CONST.__objc_classlist: 0x370
   __DATA_CONST.__objc_catlist: 0x0
   __DATA_CONST.__objc_protolist: 0x178
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0xf638
-  __DATA_CONST.__objc_selrefs: 0x3200
+  __DATA_CONST.__objc_selrefs: 0x3210
   __DATA_CONST.__objc_arraydata: 0x18
-  __AUTH_CONST.__cfstring: 0x5040
+  __AUTH_CONST.__cfstring: 0x5060
   __AUTH_CONST.__objc_const: 0x37b0
-  __AUTH_CONST.__const: 0xad0
+  __AUTH_CONST.__const: 0xaf0
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_ptr: 0x10
-  __AUTH_CONST.__auth_got: 0x600
+  __AUTH_CONST.__auth_got: 0x610
   __AUTH.__objc_data: 0xe08
   __DATA.__objc_protorefs: 0xa0
   __DATA.__objc_classrefs: 0x488

   __DATA.__objc_ivar: 0xbf0
   __DATA.__objc_data: 0x20
   __DATA.__data: 0x1248
-  __DATA.__bss: 0x5c0
+  __DATA.__bss: 0x5d0
   __DATA_DIRTY.__objc_data: 0x1468
   __DATA_DIRTY.__data: 0x200
   __DATA_DIRTY.__bss: 0x310

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 3536
-  Symbols:   10953
-  CStrings:  4546
+  Functions: 3540
+  Symbols:   10968
+  CStrings:  4551
 
Symbols:
+ -[SPMonitorsWrapper _cpuType]
+ -[SPMonitorsWrapper useLegacyMacBeaconing]
+ _SPAccountRemovedNotification
+ ___29-[SPMonitorsWrapper _cpuType]_block_invoke
+ ___29-[SPMonitorsWrapper _cpuType]_block_invoke.cold.1
+ ___35-[SPBeaconManager repairDataStore:]_block_invoke.280
+ ___44-[SPBeaconManager allBeaconsWithCompletion:]_block_invoke.237
+ ___44-[SPBeaconManager allDuriansWithCompletion:]_block_invoke.256
+ ___44-[SPBeaconManager beaconForUUID:completion:]_block_invoke.232
+ ___47-[SPBeaconManager allBeaconsOfType:completion:]_block_invoke.243
+ ___48-[SPBeaconManager allBeaconsOfTypes:completion:]_block_invoke.238
+ ___48-[SPBeaconManager allBeaconsOfTypes:completion:]_block_invoke.239
+ ___48-[SPBeaconManager roleCategoriesWithCompletion:]_block_invoke.257
+ ___48-[SPBeaconManager setRole:forBeacon:completion:]_block_invoke.258
+ ___51-[SPBeaconManager unacceptedBeaconsWithCompletion:]_block_invoke.253
+ ___51-[SPBeaconManager updateBeacon:updates:completion:]_block_invoke.259
+ ___54-[SPBeaconManager fetchUserStatsForBeacon:completion:]_block_invoke.276
+ ___58-[SPBeaconManager connectedToBeacon:withIndex:completion:]_block_invoke.272
+ ___59-[SPBeaconManager ownedDeviceKeyRecordsForUUID:completion:]_block_invoke.233
+ ___59-[SPBeaconManager setKeyRollInterval:forBeacon:completion:]_block_invoke.268
+ ___60-[SPBeaconManager connectionTokensForBeaconUUID:completion:]_block_invoke.271
+ ___60-[SPBeaconManager fetchFirmwareVersionForBeacon:completion:]_block_invoke.277
+ ___63-[SPBeaconManager setCurrentWildKeyIndex:forBeacon:completion:]_block_invoke.270
+ ___64-[SPBeaconManager beaconingKeysForUUID:dateInterval:completion:]_block_invoke.254
+ ___64-[SPBeaconManager createOwnedDeviceKeyRecordForUUID:completion:]_block_invoke.235
+ ___64-[SPBeaconManager purgeOwnedDeviceKeyRecordsForUUID:completion:]_block_invoke.234
+ ___66-[SPBeaconManager notificationBeaconForSubscriptionId:completion:]_block_invoke.236
+ ___69-[SPBeaconManager connectionTokensForBeaconUUID:criteria:completion:]_block_invoke.264
+ ___73-[SPBeaconManager connectionTokensForBeaconUUID:dateInterval:completion:]_block_invoke.260
+ ___73-[SPBeaconManager setWildKeyBase:interval:fallback:forBeacon:completion:]_block_invoke.269
+ ___75-[SPBeaconManager allBeaconsOfTypes:includeDupes:includeHidden:completion:]_block_invoke.241
+ ___75-[SPBeaconManager allBeaconsOfTypes:includeDupes:includeHidden:completion:]_block_invoke.242
+ ___76-[SPBeaconManager postedLocalNotifyWhenFoundNotificationForUUID:completion:]_block_invoke.255
+ ___77-[SPBeaconManager setAlignmentUncertainty:atIndex:date:forBeacon:completion:]_block_invoke.267
+ ___81-[SPBeaconManager allBeaconingKeysForUUID:dateInterval:forceGenerate:completion:]_block_invoke.266
+ ___block_literal_global.247
+ ___error
+ __cpuType.cachedCPUType
+ __cpuType.onceToken
+ _objc_msgSend$_cpuType
+ _sysctlbyname
- GCC_except_table3
- ___35-[SPBeaconManager repairDataStore:]_block_invoke.277
- ___44-[SPBeaconManager allBeaconsWithCompletion:]_block_invoke.234
- ___44-[SPBeaconManager allDuriansWithCompletion:]_block_invoke.253
- ___44-[SPBeaconManager beaconForUUID:completion:]_block_invoke.229
- ___47-[SPBeaconManager allBeaconsOfType:completion:]_block_invoke.240
- ___48-[SPBeaconManager allBeaconsOfTypes:completion:]_block_invoke.235
- ___48-[SPBeaconManager allBeaconsOfTypes:completion:]_block_invoke.236
- ___48-[SPBeaconManager roleCategoriesWithCompletion:]_block_invoke.254
- ___48-[SPBeaconManager setRole:forBeacon:completion:]_block_invoke.255
- ___51-[SPBeaconManager unacceptedBeaconsWithCompletion:]_block_invoke.250
- ___51-[SPBeaconManager updateBeacon:updates:completion:]_block_invoke.256
- ___54-[SPBeaconManager fetchUserStatsForBeacon:completion:]_block_invoke.273
- ___58-[SPBeaconManager connectedToBeacon:withIndex:completion:]_block_invoke.269
- ___59-[SPBeaconManager ownedDeviceKeyRecordsForUUID:completion:]_block_invoke.230
- ___59-[SPBeaconManager setKeyRollInterval:forBeacon:completion:]_block_invoke.265
- ___60-[SPBeaconManager connectionTokensForBeaconUUID:completion:]_block_invoke.268
- ___60-[SPBeaconManager fetchFirmwareVersionForBeacon:completion:]_block_invoke.274
- ___63-[SPBeaconManager setCurrentWildKeyIndex:forBeacon:completion:]_block_invoke.267
- ___64-[SPBeaconManager beaconingKeysForUUID:dateInterval:completion:]_block_invoke.251
- ___64-[SPBeaconManager createOwnedDeviceKeyRecordForUUID:completion:]_block_invoke.232
- ___64-[SPBeaconManager purgeOwnedDeviceKeyRecordsForUUID:completion:]_block_invoke.231
- ___66-[SPBeaconManager notificationBeaconForSubscriptionId:completion:]_block_invoke.233
- ___69-[SPBeaconManager connectionTokensForBeaconUUID:criteria:completion:]_block_invoke.261
- ___73-[SPBeaconManager connectionTokensForBeaconUUID:dateInterval:completion:]_block_invoke.257
- ___73-[SPBeaconManager setWildKeyBase:interval:fallback:forBeacon:completion:]_block_invoke.266
- ___75-[SPBeaconManager allBeaconsOfTypes:includeDupes:includeHidden:completion:]_block_invoke.238
- ___75-[SPBeaconManager allBeaconsOfTypes:includeDupes:includeHidden:completion:]_block_invoke.239
- ___76-[SPBeaconManager postedLocalNotifyWhenFoundNotificationForUUID:completion:]_block_invoke.252
- ___77-[SPBeaconManager setAlignmentUncertainty:atIndex:date:forBeacon:completion:]_block_invoke.264
- ___81-[SPBeaconManager allBeaconingKeysForUUID:dateInterval:forceGenerate:completion:]_block_invoke.263
- ___block_literal_global.244
- ___block_literal_global.272
CStrings:
+ "SPAccountRemovedNotification"
+ "_cpuType"
+ "hw.cputype"
+ "hw.cputype failed with error: %d"
+ "useLegacyMacBeaconing"

```
