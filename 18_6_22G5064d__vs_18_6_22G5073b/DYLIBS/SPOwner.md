## SPOwner

> `/System/Library/PrivateFrameworks/SPOwner.framework/SPOwner`

```diff

-396.36.4.2.5
-  __TEXT.__text: 0x728c4
+396.36.4.2.8
+  __TEXT.__text: 0x7294c
   __TEXT.__auth_stubs: 0xc60
-  __TEXT.__objc_methlist: 0xacb4
+  __TEXT.__objc_methlist: 0xaccc
   __TEXT.__cstring: 0x6527
   __TEXT.__const: 0x448
   __TEXT.__gcc_except_tab: 0x1bc0

   __TEXT.__unwind_info: 0x2518
   __TEXT.__eh_frame: 0x278
   __TEXT.__objc_classname: 0x124e
-  __TEXT.__objc_methname: 0x12538
+  __TEXT.__objc_methname: 0x12559
   __TEXT.__objc_methtype: 0x3825
   __TEXT.__objc_stubs: 0xa780
   __DATA_CONST.__got: 0x590

   __AUTH_CONST.__auth_got: 0x640
   __AUTH_CONST.__const: 0xb50
   __AUTH_CONST.__cfstring: 0x5960
-  __AUTH_CONST.__objc_const: 0x126f0
+  __AUTH_CONST.__objc_const: 0x12720
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x230
-  __DATA.__objc_ivar: 0xd80
+  __DATA.__objc_ivar: 0xd84
   __DATA.__data: 0x1478
   __DATA.__bss: 0x5e0
   __DATA_DIRTY.__objc_data: 0x2590

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 4801638B-C564-32BA-A374-4362D922B282
-  Functions: 4035
-  Symbols:   12543
-  CStrings:  5750
+  UUID: 83733946-C9C9-3116-B3BA-3A254F996BD2
+  Functions: 4037
+  Symbols:   12548
+  CStrings:  5751
 
Symbols:
+ -[SPDiscoveredAccessoryMetadata findMyVersion]
+ -[SPDiscoveredAccessoryMetadata setFindMyVersion:]
+ _OBJC_IVAR_$_SPDiscoveredAccessoryMetadata._findMyVersion
+ ___29-[SPLocalBeaconManager start]_block_invoke.132
+ ___34-[SPLocalBeaconManager timerFired]_block_invoke.155
+ ___39-[SPLocalBeaconManager beaconsChanged:]_block_invoke.141
+ ___44-[SPLocalBeaconManager updateStateFromNVRAM]_block_invoke.130
+ ___46-[SPLocalBeaconManager beaconingStateChanged:]_block_invoke.142
+ ___46-[SPLocalBeaconManager beaconingStateChanged:]_block_invoke.144
+ ___58-[SPLocalBeaconManager beaconingStateChangedNotification:]_block_invoke.140
+ ___70-[SPLocalBeaconManager notifyBeaconingKeysChangedBlockWithCompletion:]_block_invoke.170
+ ___70-[SPLocalBeaconManager notifyBeaconingKeysChangedBlockWithCompletion:]_block_invoke.172
+ ___70-[SPLocalBeaconManager notifyBeaconingKeysChangedBlockWithCompletion:]_block_invoke.173
+ ___83-[SPLocalBeaconManager(KeyGeneration) generateOfflineAdvertisingKeysForReason:now:]_block_invoke.412
+ ___block_literal_global.176
+ ___block_literal_global.181
+ ___block_literal_global.421
- ___29-[SPLocalBeaconManager start]_block_invoke.126
- ___34-[SPLocalBeaconManager timerFired]_block_invoke.149
- ___39-[SPLocalBeaconManager beaconsChanged:]_block_invoke.135
- ___44-[SPLocalBeaconManager updateStateFromNVRAM]_block_invoke.124
- ___46-[SPLocalBeaconManager beaconingStateChanged:]_block_invoke.136
- ___46-[SPLocalBeaconManager beaconingStateChanged:]_block_invoke.138
- ___58-[SPLocalBeaconManager beaconingStateChangedNotification:]_block_invoke.134
- ___70-[SPLocalBeaconManager notifyBeaconingKeysChangedBlockWithCompletion:]_block_invoke.164
- ___70-[SPLocalBeaconManager notifyBeaconingKeysChangedBlockWithCompletion:]_block_invoke.166
- ___70-[SPLocalBeaconManager notifyBeaconingKeysChangedBlockWithCompletion:]_block_invoke.167
- ___83-[SPLocalBeaconManager(KeyGeneration) generateOfflineAdvertisingKeysForReason:now:]_block_invoke.406
- ___block_literal_global.170
- ___block_literal_global.175
- ___block_literal_global.415
Functions (modified):
~ -[SPDiscoveredAccessoryMetadata copyWithZone:] : 412 -> 456
~ -[SPDiscoveredAccessoryMetadata encodeWithCoder:] : 316 -> 336
~ -[SPDiscoveredAccessoryMetadata initWithCoder:] : 472 -> 516
~ -[SPDiscoveredAccessoryMetadata .cxx_destruct] : 116 -> 128

Functions (added):
+ -[SPDiscoveredAccessoryMetadata findMyVersion]
+ -[SPDiscoveredAccessoryMetadata setFindMyVersion:]
CStrings:
+ "T@\"NSString\",C,N,V_findMyVersion"

```
