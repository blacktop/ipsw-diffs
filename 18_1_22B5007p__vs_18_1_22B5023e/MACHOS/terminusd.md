## terminusd

> `/usr/libexec/terminusd`

```diff

-563.0.0.0.0
-  __TEXT.__text: 0x1572d4
+563.0.3.0.0
+  __TEXT.__text: 0x156568
   __TEXT.__auth_stubs: 0x26d0
   __TEXT.__objc_stubs: 0x7ee0
   __TEXT.__objc_methlist: 0x45cc
   __TEXT.__const: 0x250
   __TEXT.__gcc_except_tab: 0x3824
-  __TEXT.__objc_methname: 0x104fd
-  __TEXT.__cstring: 0x3b070
-  __TEXT.__oslogstring: 0x2cd1
+  __TEXT.__objc_methname: 0x10555
+  __TEXT.__cstring: 0x3a8a2
+  __TEXT.__oslogstring: 0x2568
   __TEXT.__objc_classname: 0xd90
   __TEXT.__objc_methtype: 0x30ba
-  __TEXT.__info_plist: 0x439
-  __TEXT.__unwind_info: 0x2150
+  __TEXT.__info_plist: 0x42f
+  __TEXT.__unwind_info: 0x2148
   __DATA_CONST.__auth_got: 0x1378
-  __DATA_CONST.__got: 0x958
+  __DATA_CONST.__got: 0x960
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x2e68
   __DATA_CONST.__cfstring: 0xb260

   __DATA_CONST.__objc_arraydata: 0x78
   __DATA_CONST.__objc_arrayobj: 0xf0
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA.__objc_const: 0x15198
+  __DATA.__objc_const: 0x151f8
   __DATA.__objc_selrefs: 0x2720
-  __DATA.__objc_ivar: 0x1864
+  __DATA.__objc_ivar: 0x1870
   __DATA.__objc_data: 0x2760
   __DATA.__data: 0xbc8
   __DATA.__bss: 0x678

   - /usr/lib/libmrc.dylib
   - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2944
-  Symbols:   931
-  CStrings:  9361
+  Functions: 2945
+  Symbols:   932
+  CStrings:  9324
 
Symbols:
+ _nrXPCKeyDeviceMonitorStatusPluggedIn
CStrings:
+ "%!s(MISSING) called with null remoteClassAKeys.length == sizeof(ccec25519pubkey) + sizeof(ccec25519pubkey)"
+ "%!s(MISSING) called with null remoteClassCKeys.length == sizeof(ccec25519pubkey) + sizeof(ccec25519pubkey)"
+ "%!s(MISSING) called with null remoteClassDKeys.length == sizeof(ccec25519pubkey) + sizeof(ccec25519pubkey)"
+ "%!s(MISSING) called with null remoteDeviceIdentityData.length == sizeof(uuid_t) + sizeof(ccec25519pubkey)"
+ "%!s(MISSING)%!s(MISSING):%!d(MISSING) Bad localPublicClassAKeys.length %!l(MISSING)lu"
+ "%!s(MISSING)%!s(MISSING):%!d(MISSING) Bad localPublicClassCKeys.length %!l(MISSING)lu"
+ "%!s(MISSING)%!s(MISSING):%!d(MISSING) Bad localPublicClassDKeys.length %!l(MISSING)lu"
+ "%!s(MISSING)%!s(MISSING):%!d(MISSING) deferring sending device state update"
+ "+[NRDDeviceConductor createDeviceMonitorDictWithNRUUID:isNearby:isConnected:isCloudConnected:isAsleep:isClassCConnected:hasUnpairedBluetooth:linkType:linkSubtype:proxySvcIntfName:thermalPressure:pluggedIn:replyDict:]"
+ "-[NRDDeviceConductor sendDeviceStateUpdateOnLink:]"
+ "17:07:25"
+ "563.0.3"
+ "DevicePluggedIn"
+ "Jul 31 2024"
+ "_lastReportedPluggedInState"
+ "_lastSeenPeerPluggedInState"
+ "_sendDeviceStateUpdateWhenAwake"
- "%!s(MISSING) called with null localPublicClassDKeys"
- "%!s(MISSING) called with null remoteClassAKeys"
- "%!s(MISSING) called with null remoteClassCKeys"
- "%!s(MISSING) called with null remoteClassDKeys"
- "%!s(MISSING) called with null remoteDeviceIdentityData"
- "%!s(MISSING)%!s(MISSING):%!d(MISSING) ABORTING: Assertion Failed: (localDevice.classAKeychainItemsLegacyOnly.remotePublicKey) != ((void *)0)"
- "%!s(MISSING)%!s(MISSING):%!d(MISSING) ABORTING: Assertion Failed: (localDevice.classAKeychainItemsLegacyOnly.sharedSecret) != ((void *)0)"
- "%!s(MISSING)%!s(MISSING):%!d(MISSING) ABORTING: Assertion Failed: (localDevice.classCKeychainItems.remotePublicKey) != ((void *)0)"
- "%!s(MISSING)%!s(MISSING):%!d(MISSING) ABORTING: Assertion Failed: (localDevice.classCKeychainItems.sharedSecret) != ((void *)0)"
- "%!s(MISSING)%!s(MISSING):%!d(MISSING) ABORTING: Assertion Failed: (localDevice.classDKeychainItems.dhLocalPrivateKey) != ((void *)0)"
- "%!s(MISSING)%!s(MISSING):%!d(MISSING) ABORTING: Assertion Failed: (localDevice.classDKeychainItems.localPrivateKey) != ((void *)0)"
- "%!s(MISSING)%!s(MISSING):%!d(MISSING) ABORTING: Assertion Failed: (localDevice.classDKeychainItems.remotePublicKey) != ((void *)0)"
- "%!s(MISSING)%!s(MISSING):%!d(MISSING) ABORTING: Assertion Failed: (localDevice.classDKeychainItems.sharedSecret) != ((void *)0)"
- "%!s(MISSING)%!s(MISSING):%!d(MISSING) ABORTING: Assertion Failed: (localPublicClassAKeys) != ((void *)0)"
- "%!s(MISSING)%!s(MISSING):%!d(MISSING) ABORTING: Assertion Failed: (localPublicClassCKeys) != ((void *)0)"
- "%!s(MISSING)%!s(MISSING):%!d(MISSING) ABORTING: Assertion Failed: (localPublicClassDKeys) != ((void *)0)"
- "%!s(MISSING)%!s(MISSING):%!d(MISSING) ABORTING: Assertion Failed: localDevice.classAKeychainItemsLegacyOnly.sharedSecret.secretData.length == sizeof(ccec25519key)"
- "%!s(MISSING)%!s(MISSING):%!d(MISSING) ABORTING: Assertion Failed: localDevice.classCKeychainItems.sharedSecret.secretData.length == sizeof(ccec25519key)"
- "%!s(MISSING)%!s(MISSING):%!d(MISSING) ABORTING: Assertion Failed: localDevice.classDKeychainItems.sharedSecret.secretData.length == sizeof(ccec25519key)"
- "%!s(MISSING)%!s(MISSING):%!d(MISSING) ABORTING: Assertion Failed: remoteClassAKeys.length == sizeof(ccec25519pubkey) + sizeof(ccec25519pubkey)"
- "%!s(MISSING)%!s(MISSING):%!d(MISSING) ABORTING: Assertion Failed: remoteClassCKeys.length == sizeof(ccec25519pubkey) + sizeof(ccec25519pubkey)"
- "%!s(MISSING)%!s(MISSING):%!d(MISSING) ABORTING: Assertion Failed: remoteClassDKeys.length == sizeof(ccec25519pubkey) + sizeof(ccec25519pubkey)"
- "%!s(MISSING)%!s(MISSING):%!d(MISSING) ABORTING: Assertion Failed: remoteDeviceIdentityData.length == sizeof(uuid_t) + sizeof(ccec25519pubkey)"
- "%!s(MISSING)%!s(MISSING):%!d(MISSING) ABORTING: Bad localPublicClassAKeys.length %!l(MISSING)lu"
- "%!s(MISSING)%!s(MISSING):%!d(MISSING) ABORTING: Bad localPublicClassCKeys.length %!l(MISSING)lu"
- "%!s(MISSING)%!s(MISSING):%!d(MISSING) ABORTING: Bad localPublicClassDKeys.length %!l(MISSING)lu"
- "%!{(MISSING)public}s Assertion Failed: (localDevice.classAKeychainItemsLegacyOnly.remotePublicKey) != ((void *)0)"
- "%!{(MISSING)public}s Assertion Failed: (localDevice.classAKeychainItemsLegacyOnly.sharedSecret) != ((void *)0)"
- "%!{(MISSING)public}s Assertion Failed: (localDevice.classCKeychainItems.remotePublicKey) != ((void *)0)"
- "%!{(MISSING)public}s Assertion Failed: (localDevice.classCKeychainItems.sharedSecret) != ((void *)0)"
- "%!{(MISSING)public}s Assertion Failed: (localDevice.classDKeychainItems.dhLocalPrivateKey) != ((void *)0)"
- "%!{(MISSING)public}s Assertion Failed: (localDevice.classDKeychainItems.localPrivateKey) != ((void *)0)"
- "%!{(MISSING)public}s Assertion Failed: (localDevice.classDKeychainItems.remotePublicKey) != ((void *)0)"
- "%!{(MISSING)public}s Assertion Failed: (localDevice.classDKeychainItems.sharedSecret) != ((void *)0)"
- "%!{(MISSING)public}s Assertion Failed: (localPublicClassAKeys) != ((void *)0)"
- "%!{(MISSING)public}s Assertion Failed: (localPublicClassCKeys) != ((void *)0)"
- "%!{(MISSING)public}s Assertion Failed: (localPublicClassDKeys) != ((void *)0)"
- "%!{(MISSING)public}s Assertion Failed: localDevice.classAKeychainItemsLegacyOnly.sharedSecret.secretData.length == sizeof(ccec25519key)"
- "%!{(MISSING)public}s Assertion Failed: localDevice.classCKeychainItems.sharedSecret.secretData.length == sizeof(ccec25519key)"
- "%!{(MISSING)public}s Assertion Failed: localDevice.classDKeychainItems.sharedSecret.secretData.length == sizeof(ccec25519key)"
- "%!{(MISSING)public}s Assertion Failed: remoteClassAKeys.length == sizeof(ccec25519pubkey) + sizeof(ccec25519pubkey)"
- "%!{(MISSING)public}s Assertion Failed: remoteClassCKeys.length == sizeof(ccec25519pubkey) + sizeof(ccec25519pubkey)"
- "%!{(MISSING)public}s Assertion Failed: remoteClassDKeys.length == sizeof(ccec25519pubkey) + sizeof(ccec25519pubkey)"
- "%!{(MISSING)public}s Assertion Failed: remoteDeviceIdentityData.length == sizeof(uuid_t) + sizeof(ccec25519pubkey)"
- "%!{(MISSING)public}s Bad localPublicClassAKeys.length %!l(MISSING)lu"
- "%!{(MISSING)public}s Bad localPublicClassCKeys.length %!l(MISSING)lu"
- "%!{(MISSING)public}s Bad localPublicClassDKeys.length %!l(MISSING)lu"
- "+[NRDDeviceConductor createDeviceMonitorDictWithNRUUID:isNearby:isConnected:isCloudConnected:isAsleep:isClassCConnected:hasUnpairedBluetooth:linkType:linkSubtype:proxySvcIntfName:thermalPressure:replyDict:]"
- "+[NRDLocalDevice ingestRemoteClassAKeys:nrUUID:deviceCompletionBlock:]_block_invoke"
- "+[NRDLocalDevice ingestRemoteClassCKeys:nrUUID:deviceCompletionBlock:]_block_invoke"
- "-[NRDIDSKeyManager queryIDSKeysForBluetoothUUID:minDataProtectionClass:localPublicClassDKeys:localPublicClassCKeys:localPublicClassAKeys:completionBlock:]"
- "00:50:36"
- "563"
- "Jul 12 2024"

```
