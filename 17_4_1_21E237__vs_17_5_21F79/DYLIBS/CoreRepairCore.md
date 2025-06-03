## CoreRepairCore

> `/System/Library/PrivateFrameworks/CoreRepairCore.framework/CoreRepairCore`

```diff

-397.100.12.0.0
-  __TEXT.__text: 0x4e274
-  __TEXT.__auth_stubs: 0x12d0
-  __TEXT.__objc_methlist: 0x1fc4
+397.120.5.0.0
+  __TEXT.__text: 0x4fc08
+  __TEXT.__auth_stubs: 0x1320
+  __TEXT.__objc_methlist: 0x2054
   __TEXT.__const: 0x1200
-  __TEXT.__oslogstring: 0x5daf
-  __TEXT.__cstring: 0x3064
-  __TEXT.__gcc_except_tab: 0xb38
-  __TEXT.__unwind_info: 0xa08
-  __TEXT.__objc_classname: 0x55e
-  __TEXT.__objc_methname: 0x4f88
-  __TEXT.__objc_methtype: 0xe61
-  __TEXT.__objc_stubs: 0x3be0
-  __DATA_CONST.__got: 0x1b8
+  __TEXT.__oslogstring: 0x5fe0
+  __TEXT.__cstring: 0x3160
+  __TEXT.__gcc_except_tab: 0xb4c
+  __TEXT.__unwind_info: 0xa30
+  __TEXT.__objc_classname: 0x576
+  __TEXT.__objc_methname: 0x500c
+  __TEXT.__objc_methtype: 0xe80
+  __TEXT.__objc_stubs: 0x3c80
+  __DATA_CONST.__got: 0x1c0
   __DATA_CONST.__const: 0x1480
-  __DATA_CONST.__objc_classlist: 0x1c8
+  __DATA_CONST.__objc_classlist: 0x1d0
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x2358
-  __DATA_CONST.__objc_selrefs: 0x12f0
+  __DATA_CONST.__objc_selrefs: 0x1318
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_classrefs: 0x298
-  __DATA_CONST.__objc_superrefs: 0x150
-  __DATA_CONST.__objc_arraydata: 0x428
-  __AUTH_CONST.__cfstring: 0x3fc0
-  __AUTH_CONST.__objc_const: 0x1978
+  __DATA_CONST.__objc_classrefs: 0x2a0
+  __DATA_CONST.__objc_superrefs: 0x158
+  __DATA_CONST.__objc_arraydata: 0x4a8
+  __AUTH_CONST.__cfstring: 0x4100
+  __AUTH_CONST.__objc_const: 0x1a08
   __AUTH_CONST.__const: 0x280
   __AUTH_CONST.__objc_intobj: 0xd8
-  __AUTH_CONST.__objc_arrayobj: 0x240
-  __AUTH_CONST.__objc_dictobj: 0xa0
-  __AUTH_CONST.__auth_got: 0x978
-  __AUTH.__objc_data: 0x10e0
+  __AUTH_CONST.__objc_arrayobj: 0x2a0
+  __AUTH_CONST.__objc_dictobj: 0xf0
+  __AUTH_CONST.__auth_got: 0x9a0
+  __AUTH.__objc_data: 0x1090
   __DATA.__objc_ivar: 0x1c8
   __DATA.__data: 0x480
   __DATA.__common: 0x8
   __DATA.__bss: 0xb0
-  __DATA_DIRTY.__objc_data: 0xf0
+  __DATA_DIRTY.__objc_data: 0x190
   __DATA_DIRTY.__bss: 0x28
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/ServiceManagement.framework/ServiceManagement
   - /System/Library/PrivateFrameworks/Symptoms.framework/Frameworks/SymptomAnalytics.framework/SymptomAnalytics
   - /System/Library/PrivateFrameworks/Symptoms.framework/Frameworks/SymptomPresentationFeed.framework/SymptomPresentationFeed
+  - /System/Library/PrivateFrameworks/ZhuGeSupport.framework/ZhuGeSupport
   - /usr/lib/libFDR.dylib
   - /usr/lib/libIOAccessoryManager.dylib
   - /usr/lib/libMobileGestalt.dylib

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/updaters/libSavageRestoreInfo_iOS.dylib
   - /usr/lib/updaters/libT200Updater.dylib
-  UUID: 7A097CBB-A6FE-3E7C-823B-3AB76481070B
-  Functions: 1537
-  Symbols:   436
-  CStrings:  2869
+  UUID: 83185E93-2DC8-3332-9567-BB57B1638327
+  Functions: 1557
+  Symbols:   442
+  CStrings:  2908
 
Symbols:
+ _AMFDRSealingMapCreateLocalMultiDataBlobForClass
+ _AMFDRSealingMapEntryHasAttribute
+ _AMFDRSealingMapGetEntry
+ _ZhuGeCopyValueWithCFError
+ _kAMFDRSealingMapAttributeEarlyAccessMultiData
+ _objc_unsafeClaimAutoreleasedReturnValue
CStrings:
+ "AmbientLightSensorFrontLandSerialNumber"
+ "AmbientLightSensorFrontPortSerialNumber"
+ "AmbientLightSensorRearSerialNumber"
+ "B48@0:8^{__AMFDR=}16@24@32^@40"
+ "CRFDRiPad1DeviceHandler"
+ "Copying multi data: %@"
+ "DeviceClassNumber"
+ "Failed to copy sealed dataclasses and instances: %@"
+ "Failed to read live serial number of %@ failed, error: %@"
+ "Found unsealed non-repairable instance: %@. Seal with instance: %@"
+ "IPAD COMP DISPLAY"
+ "IPAD FRONT CAMERA"
+ "IPAD REAR CAMERA"
+ "Live ALS instances: %@"
+ "MTUB combo repair not supported"
+ "Missing ALS instances: %@"
+ "No candidate instance to use"
+ "RCSn"
+ "Sealed ALS instances: %@"
+ "The device doesn't support class %@, so the class won't be claimed"
+ "The device doesn't support class %@, so the class won't be updated"
+ "The device doesn't support property %@, so the property won't be added"
+ "Unable to _addDataClassAndInstanceToMutableArray:%@"
+ "Unable to get property %@: %@"
+ "_addHmCAToMutableArrayWithFdrRemote:dataClasses:dataInstances:error:"
+ "_hasRearALS"
+ "isSupportedIPad"
+ "isiPad1ProductType:"
+ "removeObject:"

```
