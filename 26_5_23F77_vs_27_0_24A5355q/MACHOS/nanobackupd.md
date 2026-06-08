## nanobackupd

> `/System/Library/PrivateFrameworks/NanoBackup.framework/nanobackupd`

```diff

-130.0.0.0.0
-  __TEXT.__text: 0x1d538
-  __TEXT.__auth_stubs: 0x720
-  __TEXT.__objc_stubs: 0x34e0
-  __TEXT.__objc_methlist: 0x192c
+134.0.0.0.0
+  __TEXT.__text: 0x1bf68
+  __TEXT.__auth_stubs: 0x780
+  __TEXT.__objc_stubs: 0x34c0
+  __TEXT.__objc_methlist: 0x1914
   __TEXT.__const: 0xc0
-  __TEXT.__gcc_except_tab: 0x394
-  __TEXT.__oslogstring: 0x1c03
-  __TEXT.__objc_methname: 0x45ff
-  __TEXT.__cstring: 0x11c9
-  __TEXT.__objc_classname: 0x25c
+  __TEXT.__gcc_except_tab: 0x2cc
+  __TEXT.__oslogstring: 0x1c0a
+  __TEXT.__objc_methname: 0x45d3
+  __TEXT.__cstring: 0x11bb
+  __TEXT.__objc_classname: 0x245
   __TEXT.__objc_methtype: 0x1098
-  __TEXT.__unwind_info: 0x788
-  __DATA_CONST.__auth_got: 0x3a0
-  __DATA_CONST.__got: 0x340
+  __TEXT.__unwind_info: 0x638
   __DATA_CONST.__const: 0xd98
-  __DATA_CONST.__cfstring: 0x11a0
+  __DATA_CONST.__cfstring: 0x1180
   __DATA_CONST.__objc_classlist: 0x98
-  __DATA_CONST.__objc_catlist: 0x10
+  __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x80
   __DATA_CONST.__objc_intobj: 0x90
-  __DATA.__objc_const: 0x2e58
-  __DATA.__objc_selrefs: 0x1248
+  __DATA_CONST.__auth_got: 0x3d0
+  __DATA_CONST.__got: 0x348
+  __DATA.__objc_const: 0x2e18
+  __DATA.__objc_selrefs: 0x1238
   __DATA.__objc_ivar: 0x130
   __DATA.__objc_data: 0x5f0
   __DATA.__data: 0x300

   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/NanoBackup.framework/NanoBackup
   - /System/Library/PrivateFrameworks/NanoPreferencesSync.framework/NanoPreferencesSync
-  - /System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry
   - /System/Library/PrivateFrameworks/NanoTimeKitCompanion.framework/NanoTimeKitCompanion
+  - /System/Library/PrivateFrameworks/PairedDeviceRegistry.framework/PairedDeviceRegistry
   - /System/Library/PrivateFrameworks/PersistentConnection.framework/PersistentConnection
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4B1D5CB6-BC02-3598-B719-19F87B287E31
-  Functions: 604
-  Symbols:   235
-  CStrings:  1399
+  UUID: 2F118577-0412-3040-BFE8-BAF5F6D06D64
+  Functions: 603
+  Symbols:   241
+  CStrings:  1395
 
Symbols:
+ _OBJC_CLASS_$_PDRRegistry
+ _PDRDevicePropertyKeyCSN
+ _PDRDevicePropertyKeyColor
+ _PDRDevicePropertyKeyDeviceBackingColor
+ _PDRDevicePropertyKeyDeviceCoverGlassColor
+ _PDRDevicePropertyKeyDeviceHousingColor
+ _PDRDevicePropertyKeyDmin
+ _PDRDevicePropertyKeyEnclosureColor
+ _PDRDevicePropertyKeyIsActive
+ _PDRDevicePropertyKeyIsAltAccount
+ _PDRDevicePropertyKeyIsPaired
+ _PDRDevicePropertyKeyLocalPairingDataStorePath
+ _PDRDevicePropertyKeyMarketingVersion
+ _PDRDevicePropertyKeyName
+ _PDRDevicePropertyKeyPairingID
+ _PDRDevicePropertyKeyProductType
+ _PDRDevicePropertyKeySystemBuildVersion
+ _PDRDevicePropertyKeySystemName
+ _PDRDevicePropertyKeySystemVersion
+ _PDRDidPairNotification
+ _PDRDidUnpairNotification
+ _PDRVersionIsGreaterThanOrEqual
+ _PDRWatchOSVersion
+ _PDRWatchOSVersionForRemoteDevice
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x5
+ _objc_retain_x9
- _NRDevicePropertyCSN
- _NRDevicePropertyColor
- _NRDevicePropertyDeviceBackingColor
- _NRDevicePropertyDeviceCoverGlassColor
- _NRDevicePropertyDeviceHousingColor
- _NRDevicePropertyDmin
- _NRDevicePropertyEnclosureColor
- _NRDevicePropertyIsActive
- _NRDevicePropertyIsAltAccount
- _NRDevicePropertyIsPaired
- _NRDevicePropertyLocalPairingDataStorePath
- _NRDevicePropertyMarketingVersion
- _NRDevicePropertyName
- _NRDevicePropertyPairingID
- _NRDevicePropertyProductType
- _NRDevicePropertySystemBuildVersion
- _NRDevicePropertySystemName
- _NRDevicePropertySystemVersion
- _NRPairedDeviceRegistryDeviceDidUnpairNotification
- _NRVersionIsGreaterThanOrEqual
- _NRWatchOSVersion
- _NRWatchOSVersionForRemoteDevice
- _OBJC_CLASS_$_IDSDevice
- _OBJC_CLASS_$_NRPairedDeviceRegistry
CStrings:
+ "B16@?0@\"PDRDevice\"8"
+ "Launching; \"NanoBackupDaemon-134\" \"1105\""
+ "PairedDeviceRegistry returned matching device (%p) for pairingID (%@)"
+ "initWithDomain:pdrDevice:"
- "2a51e7b3-1b80-4981-9f09-f725bc3a8065"
- "B16@?0@\"NRDevice\"8"
- "Launching; \"NanoBackupDaemon-130\" \"24033\""
- "NanoRegistry returned matching device (%p) for pairingID (%@)"
- "initWithDomain:pairedDevice:"
- "nb_nrDevice"
- "nonActiveDeviceForIDSDevice:"

```
