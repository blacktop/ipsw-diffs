## HearingUtilities

> `/System/Library/PrivateFrameworks/HearingUtilities.framework/HearingUtilities`

```diff

-496.13.0.0.0
-  __TEXT.__text: 0x9cf48
+496.15.0.0.0
+  __TEXT.__text: 0x9d1a8
   __TEXT.__auth_stubs: 0x10d0
-  __TEXT.__objc_methlist: 0x7bd4
+  __TEXT.__objc_methlist: 0x7bdc
   __TEXT.__const: 0x402
   __TEXT.__gcc_except_tab: 0x260c
-  __TEXT.__cstring: 0x4b8a
-  __TEXT.__oslogstring: 0x924a
+  __TEXT.__cstring: 0x4cca
+  __TEXT.__oslogstring: 0x944e
   __TEXT.__dlopen_cstrs: 0x7a7
   __TEXT.__swift5_typeref: 0x46
   __TEXT.__swift5_capture: 0x30

   __TEXT.__unwind_info: 0x29d0
   __TEXT.__eh_frame: 0x70
   __TEXT.__objc_classname: 0x883
-  __TEXT.__objc_methname: 0x140e8
+  __TEXT.__objc_methname: 0x140f4
   __TEXT.__objc_methtype: 0x2275
-  __TEXT.__objc_stubs: 0xeb00
+  __TEXT.__objc_stubs: 0xeb20
   __DATA_CONST.__got: 0x620
   __DATA_CONST.__const: 0x3398
   __DATA_CONST.__objc_classlist: 0x1c0
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0xe8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4908
+  __DATA_CONST.__objc_selrefs: 0x4910
   __DATA_CONST.__objc_superrefs: 0x178
   __DATA_CONST.__objc_arraydata: 0x3d0
   __AUTH_CONST.__auth_got: 0x878

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: A689858F-0A5A-320B-A9F5-9FF5715E8919
-  Functions: 3544
-  Symbols:   11455
-  CStrings:  5915
+  UUID: DC54E26D-B7E9-3AE7-95FC-4680DC4C8826
+  Functions: 3546
+  Symbols:   11460
+  CStrings:  5920
 
Symbols:
+ -[HUComfortSoundsController stopOnQueue]
+ GCC_except_table102
+ GCC_except_table55
+ GCC_except_table85
+ GCC_except_table96
+ ___107-[HUNoiseController checkToSurfaceAnalyticsNotificationForSPL:withDuration:andBuffer:forTime:andThreshold:]_block_invoke.477
+ ___107-[HUNoiseController checkToSurfaceAnalyticsNotificationForSPL:withDuration:andBuffer:forTime:andThreshold:]_block_invoke.481
+ ___107-[HUNoiseController checkToSurfaceAnalyticsNotificationForSPL:withDuration:andBuffer:forTime:andThreshold:]_block_invoke.489
+ ___107-[HUNoiseController checkToSurfaceAnalyticsNotificationForSPL:withDuration:andBuffer:forTime:andThreshold:]_block_invoke.498
+ ___25-[HUNoiseController init]_block_invoke.360
+ ___33-[HUComfortSoundsController init]_block_invoke_5
+ ___37-[HUNoiseController restartADAMTimer]_block_invoke.440
+ ___51-[HUNoiseController subscribeToSharedNotifications]_block_invoke.533
+ ___51-[HUNoiseController subscribeToSharedNotifications]_block_invoke.533.cold.1
+ ___53-[HUNoiseController readEnvironmentalDosimetryLevels]_block_invoke.451
+ ___85-[HUNoiseController checkToSurfaceNotificationForSPL:withDuration:andBuffer:forTime:]_block_invoke.460
+ ___85-[HUNoiseController checkToSurfaceNotificationForSPL:withDuration:andBuffer:forTime:]_block_invoke.465
+ ___block_literal_global.345
+ ___block_literal_global.439
+ ___block_literal_global.483
+ ___block_literal_global.491
+ ___block_literal_global.500
+ ___block_literal_global.509
+ ___block_literal_global.513
+ ___block_literal_global.549
+ _objc_msgSend$stopOnQueue
- GCC_except_table101
- ___107-[HUNoiseController checkToSurfaceAnalyticsNotificationForSPL:withDuration:andBuffer:forTime:andThreshold:]_block_invoke.438
- ___107-[HUNoiseController checkToSurfaceAnalyticsNotificationForSPL:withDuration:andBuffer:forTime:andThreshold:]_block_invoke.442
- ___107-[HUNoiseController checkToSurfaceAnalyticsNotificationForSPL:withDuration:andBuffer:forTime:andThreshold:]_block_invoke.450
- ___107-[HUNoiseController checkToSurfaceAnalyticsNotificationForSPL:withDuration:andBuffer:forTime:andThreshold:]_block_invoke.459
- ___25-[HUNoiseController init]_block_invoke.321
- ___37-[HUNoiseController restartADAMTimer]_block_invoke.401
- ___51-[HUNoiseController subscribeToSharedNotifications]_block_invoke.494
- ___51-[HUNoiseController subscribeToSharedNotifications]_block_invoke.494.cold.1
- ___53-[HUNoiseController readEnvironmentalDosimetryLevels]_block_invoke.412
- ___85-[HUNoiseController checkToSurfaceNotificationForSPL:withDuration:andBuffer:forTime:]_block_invoke.421
- ___85-[HUNoiseController checkToSurfaceNotificationForSPL:withDuration:andBuffer:forTime:]_block_invoke.426
- ___block_literal_global.306
- ___block_literal_global.400
- ___block_literal_global.444
- ___block_literal_global.452
- ___block_literal_global.461
- ___block_literal_global.470
- ___block_literal_global.474
- ___block_literal_global.510
Functions:
~ ___59-[HUAccessoryHearingSyncManager readHearingProtectionState]_block_invoke : 308 -> 288
~ ___33-[HUComfortSoundsController stop]_block_invoke : 292 -> 8
~ -[HUAccessoryHearingSettings activeHearingProtectionEnabledForAddress:] : 176 -> 324
~ -[HUAccessoryHearingSettings setActiveHearingProtectionEnabled:forAddress:] : 312 -> 436
~ ___67-[HUAccessoryHearingSyncManager _registerForAccessoryManagerUpdate]_block_invoke_3 : 396 -> 512
~ ___54-[HUAccessoryHearingSyncManager sendUpdateToAccessory]_block_invoke_2 : 432 -> 440
~ ___33-[HUComfortSoundsController init]_block_invoke_2 : 1148 -> 1232
~ ___33-[HUComfortSoundsController init]_block_invoke_3 : 184 -> 144
~ ___33-[HUComfortSoundsController init]_block_invoke_4 : 588 -> 184
+ ___33-[HUComfortSoundsController init]_block_invoke_5
+ -[HUComfortSoundsController stopOnQueue]
CStrings:
+ "AccessoryHearingSettings: Reading Hearing Protection enabled for %@ = %@"
+ "AccessoryHearingSettings: Reading Hearing Protection is available for %@ = %@"
+ "AccessoryHearingSettings: Saving Hearing Protection enabled for %@ = %d"
+ "AccessoryHearingSyncManager: Reading Hearing Protection for addresses %@"
+ "AccessoryHearingSyncManager: Saving data received from accessory for Hearing Protection Enabled %@ - %@"
+ "AccessoryHearingSyncManager: Sending Hearing Protection Enabled update to %@ - %d - %@"
+ "AccessoryHearingSyncManager: Sending update to accessory as received empty data for Hearing Protection Enabled from %@"
+ "AccessoryManager: Activated BT controller with error %@"
+ "AccessoryManager: Activated BT discovery %@"
+ "AccessoryManager: BT Discovery callback, attributes updated %@ = %@"
+ "AccessoryManager: BT Discovery callback, found audio ownership %@ - %@ = %@"
+ "AccessoryManager: BT Discovery callback, missing address %@"
+ "AccessoryManager: Could not write nil characteristic %@ - %@, %@"
+ "AccessoryManager: Error getting CB controller info"
+ "AccessoryManager: Error turning on Bluetooth %@"
+ "AccessoryManager: Found addresses %@"
+ "AccessoryManager: Found identifiers %@"
+ "AccessoryManager: Resetting aa device manager"
+ "AccessoryManager: Sent listening mode %@ to CBDeviceSettings for %@ with error %@"
+ "AccessoryManager: Skipping write request. Missing value %@, %@ = %@"
+ "AccessoryManager: Skipping write request. No identifier found for %@"
+ "AccessoryManager: Updating BT state %s"
+ "AccessoryManager: Writing %@ to %@ - %@"
+ "stopOnQueue"
- "Activated bluetooth controller with error %@"
- "Activated bluetooth discovery %@"
- "Attributes updated %@ = %@"
- "Checking available for %@ = %@"
- "Error getting controller info"
- "Error turning on Bluetooth %@"
- "Error: Could not write nil characteristic %@ - %@, %@"
- "Found addresses %@"
- "Found discovery audio ownership %@ - %@ = %@"
- "Found identifiers %@"
- "Found value for AHP %@ - %@"
- "Missing address in discovery callback %@"
- "Resetting aa device manager"
- "Sending update to %@ - %@ - %@"
- "Skipping write request. Missing value %@, %@ = %@"
- "Skipping write request. No identifier found for %@"
- "Updated listening mode %@ for %@ with error %@"
- "Updating BT state %s"
- "Writing %@ to %@ - %@"

```
