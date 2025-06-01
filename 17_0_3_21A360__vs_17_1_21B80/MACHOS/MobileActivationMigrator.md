## MobileActivationMigrator

> `/System/Library/DataClassMigrators/MobileActivationMigrator.migrator/MobileActivationMigrator`

```diff

-898.0.10.0.0
+898.42.1.0.0
   __TEXT.__text: 0x2974
   __TEXT.__auth_stubs: 0x270
   __TEXT.__objc_stubs: 0x7c0
   __TEXT.__objc_methlist: 0x8c
-  __TEXT.__cstring: 0x2c3c
+  __TEXT.__cstring: 0x2c82
   __TEXT.__objc_classname: 0x47
   __TEXT.__objc_methname: 0xc0c
   __TEXT.__objc_methtype: 0x2da

   __DATA_CONST.__auth_got: 0x148
   __DATA_CONST.__got: 0x30
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0xeb8
-  __DATA_CONST.__cfstring: 0x4500
+  __DATA_CONST.__const: 0xed8
+  __DATA_CONST.__cfstring: 0x45a0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_arraydata: 0x320
+  __DATA_CONST.__objc_arraydata: 0x328
   __DATA_CONST.__objc_arrayobj: 0x48
   __DATA.__objc_const: 0x818
   __DATA.__objc_selrefs: 0x218

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3CBAF733-9843-301C-BAB9-906BD0806495
+  UUID: 2AC1F272-1077-3B26-87FA-BC4F50EB7EBD
   Functions: 56
-  Symbols:   1410
-  CStrings:  1274
+  Symbols:   1418
+  CStrings:  1284
 
Symbols:
+ __block_literal_global.275
+ __block_literal_global.307
+ __block_literal_global.315
+ _kMAActivationExpired
+ _kMADSPExpirationDate
+ _kMADSPList
+ _kMASplunkStatsDSPDevice
+ _unnamed_array_storage.304
+ _unnamed_array_storage.309
- __block_literal_global.272
- __block_literal_global.304
- __block_literal_global.312
- _unnamed_array_storage.301
- _unnamed_array_storage.306
CStrings:
+ "ActivationExpired"
+ "DSPDevice"
+ "DSPExpirationDate"
+ "DSPList"
+ "icloudmailagent"

```
