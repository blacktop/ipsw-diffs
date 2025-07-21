## MobileActivationMigrator

> `/System/Library/DataClassMigrators/MobileActivationMigrator.migrator/MobileActivationMigrator`

```diff

-1017.120.3.0.0
+1017.142.1.0.0
   __TEXT.__text: 0x2868
   __TEXT.__auth_stubs: 0x270
   __TEXT.__objc_stubs: 0x7a0
   __TEXT.__objc_methlist: 0x32c
-  __TEXT.__cstring: 0x2f9a
+  __TEXT.__cstring: 0x301f
   __TEXT.__objc_classname: 0x47
   __TEXT.__objc_methname: 0xc12
   __TEXT.__objc_methtype: 0x2da

   __DATA_CONST.__auth_got: 0x148
   __DATA_CONST.__got: 0xb8
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0xf58
-  __DATA_CONST.__cfstring: 0x4ae0
+  __DATA_CONST.__const: 0xf80
+  __DATA_CONST.__cfstring: 0x4b80
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 256F0F1B-B7E5-33A2-8C1C-07E084753A17
+  UUID: DCCE67B9-6659-3236-BA21-7FBCB8A0CAF9
   Functions: 59
-  Symbols:   1455
-  CStrings:  1367
+  Symbols:   1465
+  CStrings:  1377
 
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
