## MobileActivationMigrator

> `/System/Library/DataClassMigrators/MobileActivationMigrator.migrator/MobileActivationMigrator`

```diff

   __TEXT.__auth_stubs: 0x2f0
   __TEXT.__objc_stubs: 0x860
   __TEXT.__objc_methlist: 0x334
-  __TEXT.__cstring: 0x3451
+  __TEXT.__cstring: 0x34c3
   __TEXT.__objc_classname: 0x47
   __TEXT.__objc_methname: 0xcad
   __TEXT.__objc_methtype: 0x2da

   __TEXT.__oslogstring: 0x53
   __TEXT.__gcc_except_tab: 0x2c
   __TEXT.__unwind_info: 0x140
-  __DATA_CONST.__const: 0x1030
-  __DATA_CONST.__cfstring: 0x5220
+  __DATA_CONST.__const: 0x1088
+  __DATA_CONST.__cfstring: 0x5340
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 70
-  Symbols:   1596
-  CStrings:  1491
+  Symbols:   1618
+  CStrings:  1509
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__objc_arrayobj : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_selrefs : content changed
~ __DATA.__data : content changed
Symbols:
+ _kMAOptionsBAABoardId
+ _kMAOptionsBAAChipID
+ _kMAOptionsBAADeviceLocalPolicyCertificate
+ _kMAOptionsBAARequestVersion
+ _kMAOptionsBAASCRT
+ _kMAOptionsBAASecurityDomain
+ _kMAOptionsBAASerialNumber
+ _kMAOptionsBAAUCRT
+ _kMAOptionsBAAUniqueChipID
+ _kMAOptionsBAAUseIM4C
+ _kMAOptionsBAAVMIdentityAttestation
CStrings:
+ "BoardId"
+ "ChipID"
+ "DeviceLocalPolicyCertificate"
+ "RequestVersion"
+ "SecurityDomain"
+ "UseIM4C"
+ "VMIdentityAttestation"
+ "scrt"
+ "ucrt"

```
