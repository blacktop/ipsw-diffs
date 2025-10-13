## HearingUtilities

> `/System/Library/PrivateFrameworks/HearingUtilities.framework/HearingUtilities`

```diff

-496.4.1.0.0
-  __TEXT.__text: 0x99984
+496.4.3.0.0
+  __TEXT.__text: 0x9a09c
   __TEXT.__auth_stubs: 0x1140
-  __TEXT.__objc_methlist: 0x7d84
+  __TEXT.__objc_methlist: 0x7d9c
   __TEXT.__const: 0x40a
-  __TEXT.__gcc_except_tab: 0x290c
-  __TEXT.__cstring: 0x4edb
-  __TEXT.__oslogstring: 0x9bc7
+  __TEXT.__gcc_except_tab: 0x2930
+  __TEXT.__cstring: 0x4efb
+  __TEXT.__oslogstring: 0xa2d3
   __TEXT.__dlopen_cstrs: 0x7a7
   __TEXT.__swift5_typeref: 0x46
   __TEXT.__swift5_capture: 0x30

   __TEXT.__swift5_reflstr: 0xb
   __TEXT.__swift5_fieldmd: 0x38
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x25d0
+  __TEXT.__unwind_info: 0x25e8
   __TEXT.__eh_frame: 0x48
   __TEXT.__objc_classname: 0x843
-  __TEXT.__objc_methname: 0x142ac
-  __TEXT.__objc_methtype: 0x2197
-  __TEXT.__objc_stubs: 0xed80
+  __TEXT.__objc_methname: 0x14300
+  __TEXT.__objc_methtype: 0x21e3
+  __TEXT.__objc_stubs: 0xeda0
   __DATA_CONST.__got: 0x620
-  __DATA_CONST.__const: 0x3420
+  __DATA_CONST.__const: 0x3470
   __DATA_CONST.__objc_classlist: 0x1c0
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0xe8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4988
+  __DATA_CONST.__objc_selrefs: 0x4998
   __DATA_CONST.__objc_superrefs: 0x180
   __DATA_CONST.__objc_arraydata: 0x430
   __AUTH_CONST.__auth_got: 0x8b0
   __AUTH_CONST.__const: 0xd98
-  __AUTH_CONST.__cfstring: 0x5200
-  __AUTH_CONST.__objc_const: 0xa608
+  __AUTH_CONST.__cfstring: 0x5220
+  __AUTH_CONST.__objc_const: 0xa610
   __AUTH_CONST.__objc_intobj: 0xa80
   __AUTH_CONST.__objc_arrayobj: 0x1f8
   __AUTH_CONST.__objc_dictobj: 0x410

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 42D91E66-F097-3976-85B4-82B526AB5265
-  Functions: 3585
-  Symbols:   11540
-  CStrings:  6050
+  UUID: D90C51F2-2D2A-32EE-8D1A-203EE2693733
+  Functions: 3589
+  Symbols:   11552
+  CStrings:  6069
 
Symbols:
+ -[AXHearingAidDeviceController addFakeHearingAidsWithType:]
+ GCC_except_table112
+ GCC_except_table116
+ GCC_except_table119
+ GCC_except_table123
+ GCC_except_table130
+ GCC_except_table133
+ GCC_except_table138
+ GCC_except_table143
+ GCC_except_table148
+ GCC_except_table154
+ GCC_except_table163
+ GCC_except_table167
+ GCC_except_table173
+ GCC_except_table175
+ ___58-[AXHearingAidDeviceController pairedHearingAidsDidChange]_block_invoke.102
+ ___58-[AXHearingAidDeviceController pairedHearingAidsDidChange]_block_invoke.103
+ ___63-[HUAccessoryManager getCBDeviceForCurrentRouteWithCompletion:]_block_invoke.88
+ ___63-[HUAccessoryManager getCBDeviceForCurrentRouteWithCompletion:]_block_invoke.88.cold.1
+ ___63-[HUAccessoryManager getCBDeviceForCurrentRouteWithCompletion:]_block_invoke.89
+ ___63-[HUAccessoryManager getCBDeviceForCurrentRouteWithCompletion:]_block_invoke.cold.1
+ ___66-[HUAccessoryManager getSSLSupportStateForAddress:withCompletion:]_block_invoke_2
+ ___block_descriptor_56_e8_32s40bs48r_e11_v16?0B8B12ls32l8r48l8s40l8
+ ___block_descriptor_56_e8_32s40bs48r_e5_v8?0lr48l8s32l8s40l8
+ ___block_descriptor_56_e8_32s40s48r_e25_v32?0"CBDevice"8Q16^B24ls32l8s40l8r48l8
+ ___block_literal_global.61
+ ___block_literal_global.81
+ ___block_literal_global.91
+ _objc_msgSend$addFakeHearingAidsWithType:
- GCC_except_table111
- GCC_except_table115
- GCC_except_table122
- GCC_except_table129
- GCC_except_table131
- GCC_except_table137
- GCC_except_table142
- GCC_except_table147
- GCC_except_table153
- GCC_except_table162
- GCC_except_table166
- GCC_except_table172
- GCC_except_table174
- GCC_except_table83
- ___58-[AXHearingAidDeviceController pairedHearingAidsDidChange]_block_invoke.96
- ___58-[AXHearingAidDeviceController pairedHearingAidsDidChange]_block_invoke.97
- ___63-[HUAccessoryManager getCBDeviceForCurrentRouteWithCompletion:]_block_invoke_2
- ___63-[HUAccessoryManager getCBDeviceForCurrentRouteWithCompletion:]_block_invoke_3
- ___block_descriptor_64_e8_32s40s48bs56r_e11_v16?0B8B12ls32l8r56l8s40l8s48l8
- ___block_literal_global.55
- ___block_literal_global.70
- ___block_literal_global.85
CStrings:
+ "%@ [%@] %@, state: %@"
+ "AXHAServer: Hearing Device reachability state %@"
+ "AccessoryManager: Checking PSE version for address %@"
+ "AccessoryManager: Couldn't find SSL state for address %@"
+ "AccessoryManager: Couldn't get current route information"
+ "AccessoryManager: Current route: %@"
+ "AccessoryManager: Found CB device: %@ for current route: %@"
+ "AccessoryManager: Found PSE version %@ for address %@"
+ "AccessoryManager: Found SSL Enabled %d for address %@"
+ "AccessoryManager: Found device: %@ for current route: %@, listening mode %@"
+ "AccessoryManager: Found devices %@ - %@"
+ "AccessoryManager: Paired device with supported and enabled HP %@"
+ "AccessoryManager: SSL is not supported for nil address"
+ "AccessoryManager: SSL is supported %d for %@ address"
+ "AccessoryManager: Updated SSL mode %@ for %@ with error %@"
+ "CentralManager: OFF, Clearing Devices, restarting scanning %d"
+ "CentralManager: ON, Updating Paired Hearing Aids, Connecting to persistent device"
+ "CentralManager: Retrieved peripheral, Did add %d to device\n%@"
+ "CentralManager: centralManagerDidUpdateState, Central state %@ (%@), new = %d, old = %d"
+ "HAController: New device updates client. Updated available controllers"
+ "HAController: update nearby state with connectedPeer: %@, Reachable HA: %@, isConnected: %@, audioReachable: %@"
+ "Hearing test started. Background Sounds is already off."
+ "Hearing test started. Stopping Background Sounds."
+ "HearingAidDevice Connect\n%@"
+ "HearingAidDevice: Resetting connection to disable streaming %@"
+ "HearingAidDevice: Updated Input tags, resetting connection"
+ "HearingAidDevice: Updated shouldStreamToLeftAid, Resetting connection"
+ "HearingAidDevice: Updated shouldStreamToRightAid, Resetting connection"
+ "HearingAidDevice: connectionDidChange, Confirmed Paired and BT paired: \nRepresentation %@\nDevice %@"
+ "HearingAidDevice: disconnectAndUnpair %d\n%@"
+ "HearingAidDeviceController: checkPartiallyPaired, Paired devices count %@, Loaded devices\n%@"
+ "HearingAidDeviceController: checkPartiallyPaired, Partial pair %d\n%@"
+ "HearingAidDeviceController: connectToPeripheral, Failed, no peripheral"
+ "HearingAidDeviceController: pairedHearingAidsDidChange, No peripheral identifiers %@, unpairing persistent device\n%@"
+ "HearingAidDeviceController: pairedHearingAidsDidChange, No persistent Hearing Aids, Clearing Paired Hearing Devices"
+ "HearingAidDeviceController: pairedHearingAidsDidChange, Persistent properties weren't loaded, Disconnecting and Unpairing device\n%@"
+ "HearingAidDeviceController: pairedHearingAidsDidChange, Saving iCloud paired device\n%@"
+ "HearingAidDeviceController: pairedHearingAidsDidChange, Updating Persistent/Loaded/Available with device\n%@"
+ "HearingAidDeviceController: pairedHearingAidsDidChange, persistent Hearing Aids: %@"
+ "HearingAidSettings, iCloudAccountDidChange (using=%d)"
+ "HearingAidSettings: iCloud Account: %d"
+ "HearingAidSettings: init iCloud, Paired Hearing Aids from local plist %@"
+ "HearingAidSettings: pushLocalHearingAidsToiCloud, Using iCloud: %d, will push local Hearing Aids: %d, fake: %d"
+ "NearbyHearingAidController shouldConnect: %d, state: %@"
+ "NearbyHearingAidController shouldDisconnect: %d, state: %@"
+ "NearbyHearingAidController: Cancel and Destroy peerTimer, is pending %d"
+ "NearbyHearingAidController: Connect to %@, Connected peer: %@, Connecting Peer: %@"
+ "NearbyHearingAidController: Disconnect from paired hearing device"
+ "NearbyHearingAidController: Disconnect, Connected peer: %@, Connecting Peer: %@"
+ "No"
+ "addFakeHearingAidsWithType:"
+ "iCloud: Account credential has changed: %@"
+ "iCloud: Account was added: %@"
+ "iCloud: Account was modified: %@"
+ "iCloud: Account was removed: %@"
+ "iCloud: Pushing local aids to iCloud %@"
+ "iCloud: Removing Hearing Aids from iCloud"
+ "service:account:inviteDroppedForSessionID:fromID:error:"
+ "v56@0:8@\"IDSService\"16@\"IDSAccount\"24@\"NSString\"32@\"NSString\"40@\"NSError\"48"
- "%@ [%@] %@ - %@"
- "AXHAServer: Availability %@"
- "Account credential has changed: %@"
- "Account was added: %@"
- "Account was modified: %@"
- "Account was removed: %@"
- "Account: %d"
- "Cancel and Destroy peerTimer, is pending %d"
- "CentralManager: OFF"
- "CentralManager: ON"
- "CentralManager: centralManagerDidUpdateState, Central state (%ld) %d = %d"
- "Checking address %@"
- "Connect to %@, Connected peer: %@, Connecting Peer: %@"
- "Couldn't find SSL state for address %@"
- "Couldn't get current route information"
- "Disconnect from paired hearing device"
- "Disconnect, Connected peer: %@, Connecting Peer: %@"
- "Found SSL Enabled %d for address %@"
- "Found device: %@ for current route: %@"
- "Found devices %@ - %@"
- "Found pse version %@ for address %@"
- "HP is enabled for %@"
- "Hearing test started. Stopping Background Sounds"
- "HearingAidDevice Connect"
- "HearingAidDevice: connectionDidChange, Confirmed Paired and BT paired: %@ - %@"
- "HearingAidDevice: disconnectAndUnpair %d"
- "HearingAidDeviceController: checkPartiallyPaired, Partial pair %d = %@"
- "HearingAidDeviceController: pairedHearingAidsDidChange, Adding peripheral to device [%d] %@"
- "HearingAidDeviceController: pairedHearingAidsDidChange, New aids: %@"
- "HearingAidDeviceController: pairedHearingAidsDidChange, No peripheral identifiers %@, unpairing rep %@"
- "Nearby controller shouldConnect: %d, state: %@"
- "Nearby controller shouldDisconnect: %d, state: %@"
- "New device updates client. Updated available controllers"
- "New iCloud %d"
- "Paired Hearing Aids from local %@"
- "Pushing local aids to iCloud %@"
- "Removing from iCloud"
- "Resetting connection to disable streaming %@"
- "Should we push local aids to cloud? should use cloud: %d, should local aids be pushed: %d, fake hearing aids %d"
- "Updated SSL mode %@ for %@ with error %@"
- "connectedPeer: %@, Reachable HA: %@, isConnected: %@, audioReachable: %@"

```
