## MobileActivationMigrator

> `/System/Library/DataClassMigrators/MobileActivationMigrator.migrator/MobileActivationMigrator`

```diff

-1062.0.0.0.0
+1065.0.0.0.0
   __TEXT.__text: 0x2868
   __TEXT.__auth_stubs: 0x270
   __TEXT.__objc_stubs: 0x7a0
   __TEXT.__objc_methlist: 0x334
-  __TEXT.__cstring: 0x3085
+  __TEXT.__cstring: 0x310a
   __TEXT.__objc_classname: 0x47
   __TEXT.__objc_methname: 0xc3f
   __TEXT.__objc_methtype: 0x2da

   __DATA_CONST.__auth_got: 0x148
   __DATA_CONST.__got: 0xb8
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0xf80
-  __DATA_CONST.__cfstring: 0x4ca0
+  __DATA_CONST.__const: 0xfa8
+  __DATA_CONST.__cfstring: 0x4d40
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 273AA4AC-B1B8-32D0-9813-3264A4889EA7
+  UUID: DE8EBDA1-5336-3422-8784-583112352B00
   Functions: 59
-  Symbols:   1465
-  CStrings:  1396
+  Symbols:   1475
+  CStrings:  1406
 
Symbols:
+ _kMASkipActivationRandomnessCheck
+ _kMASkipUCRTValidation
+ _kMASplunkStatsActivationRecordContainsUCRT
+ _kMASplunkStatsActivationRecordProductTypeValid
+ _kMASplunkStatsActivationRecordValid
CStrings:
+ "SkipActivationRandomnessCheck"
+ "SkipUCRTValidation"
+ "activationRecordContainsUCRT"
+ "activationRecordProductTypeValid"
+ "activationRecordValid"

```
