## MobileActivationMigrator

> `/System/Library/DataClassMigrators/MobileActivationMigrator.migrator/MobileActivationMigrator`

```diff

-1017.120.3.0.0
+1055.0.0.0.0
   __TEXT.__text: 0x2868
   __TEXT.__auth_stubs: 0x270
   __TEXT.__objc_stubs: 0x7a0
-  __TEXT.__objc_methlist: 0x32c
-  __TEXT.__cstring: 0x2f9a
+  __TEXT.__objc_methlist: 0x334
+  __TEXT.__cstring: 0x3074
   __TEXT.__objc_classname: 0x47
-  __TEXT.__objc_methname: 0xc12
+  __TEXT.__objc_methname: 0xc3f
   __TEXT.__objc_methtype: 0x2da
   __TEXT.__const: 0x30
   __TEXT.__oslogstring: 0x28

   __DATA_CONST.__auth_got: 0x148
   __DATA_CONST.__got: 0xb8
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0xf58
-  __DATA_CONST.__cfstring: 0x4ae0
+  __DATA_CONST.__const: 0xf80
+  __DATA_CONST.__cfstring: 0x4c60
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_arraydata: 0x448
+  __DATA_CONST.__objc_arraydata: 0x480
   __DATA_CONST.__objc_arrayobj: 0x60
-  __DATA.__objc_const: 0x328
-  __DATA.__objc_selrefs: 0x3a8
+  __DATA.__objc_const: 0x330
+  __DATA.__objc_selrefs: 0x3b0
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0xc0
   __DATA.__bss: 0x64

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 472AE825-18D0-3B48-87DE-DA5973FEBE03
+  UUID: 4E01A28D-0EC5-3C07-8897-BEA7C99BC9FD
   Functions: 59
-  Symbols:   1455
-  CStrings:  1367
+  Symbols:   1465
+  CStrings:  1392
 
Symbols:
+ __44-[MobileActivationMigrator performMigration]_block_invoke.93
+ __block_literal_global.383
+ __block_literal_global.415
+ __block_literal_global.423
+ _kMAManufacturingData
+ _kMAManufacturingDataCountryCode
+ _kMAManufacturingDataOverride
+ _kMARegionDataForGestaltCountryCode
+ _kMARegionDataForGestaltRegionInfo
+ _kMARegionDataForGestaltSotwareBehaviors
- __44-[MobileActivationMigrator performMigration]_block_invoke.92
- __block_literal_global.362
- __block_literal_global.394
- __block_literal_global.402
- _kMAOptionsAllowInvalidNetworkCertificates
CStrings:
+ "CountryCode"
+ "DemoLoop"
+ "FeatureAccessAgent"
+ "ManufacturingData"
+ "ManufacturingDataOverride"
+ "RegionDataForGestaltCountryCode"
+ "RegionDataForGestaltRegionInfo"
+ "RegionDataForGestaltSotwareBehaviors"
+ "RepairApp"
+ "SupportFlow"
+ "copyRegionDataForGestaltWithCompletionBlock:"
+ "featureaccessd"
+ "frauddefensed"
+ "managedassetsd"
- "AllowInvalidNetworkCertificates"

```
