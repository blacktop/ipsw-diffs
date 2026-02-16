## MobileActivationMigrator

> `/System/Library/DataClassMigrators/MobileActivationMigrator.migrator/MobileActivationMigrator`

```diff

-1068.80.3.0.0
-  __TEXT.__text: 0x2868
+1076.100.26.0.0
+  __TEXT.__text: 0x2a68
   __TEXT.__auth_stubs: 0x270
-  __TEXT.__objc_stubs: 0x7a0
+  __TEXT.__objc_stubs: 0x800
   __TEXT.__objc_methlist: 0x334
-  __TEXT.__cstring: 0x316d
+  __TEXT.__cstring: 0x330a
   __TEXT.__objc_classname: 0x47
-  __TEXT.__objc_methname: 0xc3f
+  __TEXT.__objc_methname: 0xc6d
   __TEXT.__objc_methtype: 0x2da
-  __TEXT.__const: 0x30
+  __TEXT.__const: 0x38
   __TEXT.__oslogstring: 0x28
   __TEXT.__gcc_except_tab: 0x40
-  __TEXT.__unwind_info: 0x118
+  __TEXT.__unwind_info: 0x140
   __DATA_CONST.__auth_got: 0x148
-  __DATA_CONST.__got: 0xb8
+  __DATA_CONST.__got: 0xd0
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0xfc8
-  __DATA_CONST.__cfstring: 0x4dc0
+  __DATA_CONST.__const: 0x1020
+  __DATA_CONST.__cfstring: 0x5020
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_arraydata: 0x490
+  __DATA_CONST.__objc_arraydata: 0x4d0
   __DATA_CONST.__objc_arrayobj: 0x60
   __DATA.__objc_const: 0x330
-  __DATA.__objc_selrefs: 0x3b0
+  __DATA.__objc_selrefs: 0x3c8
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0xc0
   __DATA.__bss: 0x64

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C2632FEE-5A2F-3DE8-8BBB-D822AFAFD50D
-  Functions: 59
-  Symbols:   1483
-  CStrings:  1414
+  UUID: B46712DB-ADB8-3EE2-AF9F-CE6865B8D3FD
+  Functions: 68
+  Symbols:   1560
+  CStrings:  1455
 
Symbols:
+ /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/MobileActivationMigrator.build/Objects-normal/arm64e/GestaltHlpr.o
+ /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/MobileActivationMigrator.build/Objects-normal/arm64e/MobileActivationError.o
+ /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/MobileActivationMigrator.build/Objects-normal/arm64e/MobileActivationErrorPrivate.o
+ /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/MobileActivationMigrator.build/Objects-normal/arm64e/MobileActivationMigrator.o
+ /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/MobileActivationMigrator.build/Objects-normal/arm64e/common.o
+ /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/MobileActivationMigrator.build/Objects-normal/arm64e/data_migration_support.o
+ /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/MobileActivationMigrator.build/Objects-normal/arm64e/keylist.o
+ /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/MobileActivationMigrator.build/Objects-normal/arm64e/vm_support.o
+ /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Sources/MobileActivation/MobileActivationMigrator/
+ /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Sources/MobileActivation/shared/
+ _CFPreferencesSynchronize
+ _OBJC_CLASS_$_NSUserDefaults
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
+ _OUTLINED_FUNCTION_2
+ __block_literal_global.413
+ __block_literal_global.445
+ __block_literal_global.453
+ _geteuid
+ _isRunningAsRoot
+ _kCFPreferencesAnyUser
+ _kCFPreferencesCurrentHost
+ _kMACertifySBOverrideURL
+ _kMACertifySessionOverrideURL
+ _kMADeviceRegionCountryCode
+ _kMADeviceRegionRegionInfo
+ _kMADeviceRegionSoftwareBehaviors
+ _kMAIsInPalletUpdateModeOverride
+ _kMAOptionsBAAMatterSubjectDN
+ _kMAOptionsBAAMatterSubjectDNAppleHome
+ _kMAOptionsBAAMatterSubjectDNAppleKeychain
+ _kMAOptionsBAAOIDMatterSubjectDN
+ _kMAOptionsRebootAfterDeactivation
+ _kMAShiptoCountryCode
+ _kMAUCRTSLVGDate
+ _kMAUCRTSLVGState
+ _kMAUCRTSLVGStateKBBSharedSerial
+ _kMAUCRTSLVGStateKBBUniqueSerial
+ _kMAUCRTSLVGStateKGB
+ _kMAUCRTSLVGStateUnavailable
+ _objc_msgSend$initWithSuiteName:
+ _objc_msgSend$objectForKey:
+ _objc_msgSend$setObject:forKey:
+ _readUserDefaults
+ _removeUserDefaults
+ _synchronizeUserDefaults
+ _writeUserDefaults
- /Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/MobileActivationMigrator.build/Objects-normal/arm64e/GestaltHlpr.o
- /Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/MobileActivationMigrator.build/Objects-normal/arm64e/MobileActivationError.o
- /Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/MobileActivationMigrator.build/Objects-normal/arm64e/MobileActivationErrorPrivate.o
- /Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/MobileActivationMigrator.build/Objects-normal/arm64e/MobileActivationMigrator.o
- /Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/MobileActivationMigrator.build/Objects-normal/arm64e/common.o
- /Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/MobileActivationMigrator.build/Objects-normal/arm64e/data_migration_support.o
- /Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/MobileActivationMigrator.build/Objects-normal/arm64e/keylist.o
- /Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/MobileActivationMigrator.build/Objects-normal/arm64e/vm_support.o
- /Library/Caches/com.apple.xbs/Sources/MobileActivation/MobileActivationMigrator/
- /Library/Caches/com.apple.xbs/Sources/MobileActivation/shared/
- __block_literal_global.389
- __block_literal_global.421
- __block_literal_global.429
- _kMAManufacturingData
- _kMAManufacturingDataCountryCode
- _kMARegionDataForGestaltCountryCode
- _kMARegionDataForGestaltRegionInfo
- _kMARegionDataForGestaltSotwareBehaviors
- _objc_retainAutoreleaseReturnValue
- _objc_storeStrong
CStrings:
+ "1.3.6.1.4.1.37244.1.7"
+ "CertifySBOverrideURL"
+ "CertifySessionOverrideURL"
+ "DeviceRegionCountryCode"
+ "DeviceRegionRegionInfo"
+ "DeviceRegionSoftwareBehaviors"
+ "Devices"
+ "MatterSubjectDN"
+ "RebootAfterDeactivation"
+ "SCARemoteView Appex"
+ "ShiptoCountryCode"
+ "UCRTSLVGDate"
+ "UCRTSLVGState"
+ "UCRTSLVGStateKBBSharedSerial"
+ "UCRTSLVGStateKBBUniqueSerial"
+ "UCRTSLVGStateKGB"
+ "UCRTSLVGStateUnavailable"
+ "anomalydetectiond"
+ "com.apple.MobileAsset.DownloadService.Backported"
+ "com.apple.MobileAsset.DownloadService.Builtin"
+ "fmdautomationtool"
+ "getUCRTSalvageStateWithCompletionBlock:"
+ "initWithSuiteName:"
+ "kMAIsInPalletUpdateModeOverride"
+ "objectForKey:"
+ "setObject:forKey:"
+ "triald"
+ "triald_system"
- "CountryCode"
- "ManufacturingData"
- "RegionDataForGestaltCountryCode"
- "RegionDataForGestaltRegionInfo"
- "RegionDataForGestaltSotwareBehaviors"
- "copyRegionDataForGestaltWithCompletionBlock:"

```
