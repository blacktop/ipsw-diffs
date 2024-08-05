## MobileActivationMigrator

> `/System/Library/DataClassMigrators/MobileActivationMigrator.migrator/MobileActivationMigrator`

```diff

-1004.0.0.0.0
+1006.0.0.0.0
   __TEXT.__text: 0x28c4
   __TEXT.__auth_stubs: 0x270
   __TEXT.__objc_stubs: 0x7a0
   __TEXT.__objc_methlist: 0x8c
-  __TEXT.__cstring: 0x2ead
+  __TEXT.__cstring: 0x2f30
   __TEXT.__objc_classname: 0x47
   __TEXT.__objc_methname: 0xc12
   __TEXT.__objc_methtype: 0x2da

   __DATA_CONST.__auth_got: 0x148
   __DATA_CONST.__got: 0xb8
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0xf30
-  __DATA_CONST.__cfstring: 0x49a0
+  __DATA_CONST.__const: 0xf48
+  __DATA_CONST.__cfstring: 0x4a00
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 53
-  Symbols:   1416
-  CStrings:  758
+  Symbols:   1422
+  CStrings:  761
 
Symbols:
+ _kMADCRTOOBLoadSpreadingActivityID
+ _kMADCRTOOBLoadSpreadingActivityID
+ _kMAOptionsValidateCriticalDcrtOIDs
+ _kMAOptionsValidateCriticalDcrtOIDs
+ _kMASDCRTOOBLoadSpreadingActivityID
+ _kMASDCRTOOBLoadSpreadingActivityID
CStrings:
+ "Enhanced Logging"
+ "ValidateCriticalDcrtOIDs"
+ "com.apple.mobileactivationd.DCRT.OOB.LoadSpreading"
+ "com.apple.mobileactivationd.SDCRT.OOB.LoadSpreading"
- "Log Collector"

```
