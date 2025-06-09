## nanoprefsyncd

> `/System/Library/PrivateFrameworks/NanoPreferencesSync.framework/nanoprefsyncd`

```diff

-314.1.0.0.0
-  __TEXT.__text: 0x259ec
-  __TEXT.__auth_stubs: 0xa60
-  __TEXT.__objc_stubs: 0x34a0
-  __TEXT.__objc_methlist: 0x1fe4
-  __TEXT.__cstring: 0x219f
-  __TEXT.__objc_methname: 0x5a75
-  __TEXT.__objc_classname: 0x2ce
-  __TEXT.__objc_methtype: 0xeee
+320.0.0.0.0
+  __TEXT.__text: 0x25a7c
+  __TEXT.__auth_stubs: 0xa70
+  __TEXT.__objc_stubs: 0x3580
+  __TEXT.__objc_methlist: 0x207c
+  __TEXT.__cstring: 0x213b
+  __TEXT.__objc_methname: 0x5b5e
+  __TEXT.__objc_classname: 0x2ec
+  __TEXT.__objc_methtype: 0xfa9
   __TEXT.__const: 0xe0
-  __TEXT.__oslogstring: 0x37cc
-  __TEXT.__gcc_except_tab: 0x6bc
+  __TEXT.__oslogstring: 0x37c0
+  __TEXT.__gcc_except_tab: 0x6c8
   __TEXT.__dlopen_cstrs: 0x52
   __TEXT.__unwind_info: 0x6a0
-  __DATA_CONST.__auth_got: 0x540
-  __DATA_CONST.__got: 0x520
-  __DATA_CONST.__const: 0xb00
-  __DATA_CONST.__cfstring: 0x12e0
+  __DATA_CONST.__auth_got: 0x548
+  __DATA_CONST.__got: 0x490
+  __DATA_CONST.__const: 0xae8
+  __DATA_CONST.__cfstring: 0x12a0
   __DATA_CONST.__objc_classlist: 0xc8
-  __DATA_CONST.__objc_protolist: 0x50
+  __DATA_CONST.__objc_catlist: 0x8
+  __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x70
   __DATA_CONST.__objc_intobj: 0x18
   __DATA_CONST.__objc_arraydata: 0x40
   __DATA_CONST.__objc_arrayobj: 0x30
-  __DATA.__objc_const: 0x2ff8
-  __DATA.__objc_selrefs: 0x1438
+  __DATA.__objc_const: 0x33d0
+  __DATA.__objc_selrefs: 0x14b8
   __DATA.__objc_ivar: 0x234
   __DATA.__objc_data: 0x7d0
-  __DATA.__data: 0x3c0
+  __DATA.__data: 0x420
   __DATA.__bss: 0x80
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /System/Library/PrivateFrameworks/NanoBackup.framework/NanoBackup
   - /System/Library/PrivateFrameworks/NanoPreferencesSync.framework/NanoPreferencesSync
   - /System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry
+  - /System/Library/PrivateFrameworks/PairedDeviceRegistry.framework/PairedDeviceRegistry
   - /System/Library/PrivateFrameworks/PairedSync.framework/PairedSync
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 6AF1641A-CC89-3765-AC55-EFB10DD3DD23
-  Functions: 711
-  Symbols:   343
-  CStrings:  1750
+  UUID: AA2C715D-1FCA-338C-8E32-38295BFC361A
+  Functions: 713
+  Symbols:   327
+  CStrings:  1770
 
Symbols:
+ _OBJC_CLASS_$_NPSPairedDeviceRegistry
+ _OBJC_CLASS_$_PDRDarwinNotifications
+ _OBJC_CLASS_$_PDRDevice
+ _OBJC_CLASS_$_PSYServiceSyncSession
+ _strcmp
- OBJC_IVAR_$_PBDataReader._bytes
- OBJC_IVAR_$_PBDataReader._error
- OBJC_IVAR_$_PBDataReader._length
- OBJC_IVAR_$_PBDataReader._pos
- _NRDevicePropertyIsAltAccount
- _NRDevicePropertyIsArchived
- _NRDevicePropertyIsPaired
- _NRDevicePropertyLastActiveDate
- _NRDevicePropertyLocalPairingDataStorePath
- _NRDevicePropertyPairingID
- _NRDevicePropertySystemBuildVersion
- _NRPairedDeviceRegistryDeviceDidBecomeActive
- _NRPairedDeviceRegistryDeviceDidBecomeInactive
- _NRPairedDeviceRegistryDeviceDidEnterCompatibilityStateNotification
- _NRPairedDeviceRegistryDeviceDidPairNotification
- _NRPairedDeviceRegistryDeviceDidUnpairNotification
- _NRPairedDeviceRegistryDeviceIsSetupNotification
- _NRPairedDeviceRegistryPairedDeviceDidChangeVersionDarwinNotification
- _OBJC_CLASS_$_NRDevice
- _OBJC_CLASS_$_NRPairedDeviceRegistry
- _OBJC_CLASS_$_NSNotificationCenter
CStrings:
+ "@\"PDRDevice\""
+ "B32@?0@\"IDSDevice\"8Q16^B24"
+ "Launching; \"NanoPreferencesSyncDaemon-320\" \"1697\""
+ "PDRDevice"
+ "PDRRegistryDelegate"
+ "Registry changed"
+ "T@\"PDRDevice\",&,N,V_activeDevice"
+ "_setError"
+ "addDelegate:"
+ "bluetoothIdentifier"
+ "deviceForBluetoothID:"
+ "deviceForPairingID:"
+ "getActiveDevice"
+ "getBytes:range:"
+ "hasError"
+ "idsDestinationIDForDevice:withIdsService:"
+ "indexOfObjectPassingTest:"
+ "isAltAccount"
+ "isArchived"
+ "nps_pairedPdrDevice"
+ "nsuuid"
+ "pairedDeviceDidChangeVersion"
+ "pairingStorePath"
+ "pdrDeviceForIDSDevice:"
+ "position"
+ "registry"
+ "registry:added:"
+ "registry:changed:properties:"
+ "registry:compatibilityStateChanged:"
+ "registry:didActivate:"
+ "registry:didDeactivate:"
+ "registry:didPair:"
+ "registry:didSetup:"
+ "registry:didUnpair:"
+ "registry:removed:"
+ "registryChanged:"
+ "setPosition:"
+ "v24@0:8@\"PDRRegistry\"16"
+ "v32@0:8@\"PDRRegistry\"16@\"NSUUID\"24"
+ "v32@0:8@\"PDRRegistry\"16@\"PDRDevice\"24"
+ "v32@0:8@\"PDRRegistry\"16q24"
+ "v32@0:8@16q24"
+ "v40@0:8@\"PDRRegistry\"16@\"PDRDevice\"24@\"NSSet\"32"
- "36A0EB23-E045-4E99-9D71-8FB9A853ADA7"
- "@\"NRDevice\""
- "B44@?0@\"NSBundle\"8@\"NSString\"16B24@\"<NSObject>\"28#36"
- "F4DCA831-3D30-45BC-BDCC-E99D0E482D94"
- "Launching; \"NanoPreferencesSyncDaemon-314.1\" \"596\""
- "Received notification: (%@)"
- "T@\"NRDevice\",&,N,V_activeDevice"
- "_registryChanged:"
- "activeDeviceSelectorBlock"
- "addObserver:selector:name:object:"
- "defaultCenter"
- "deviceForIDSDevice:"
- "deviceForNRDevice:fromIDSDevices:"
- "firstObject"
- "getAllDevicesWithArchivedAltAccountDevicesMatching:"
- "idsDestinationIDForNRDevice:withIdsService:"
- "initWithUUIDString:"
- "name"
- "nrDeviceForIDSDevice:"
- "pairedDevice"
- "valueForProperty:"

```
