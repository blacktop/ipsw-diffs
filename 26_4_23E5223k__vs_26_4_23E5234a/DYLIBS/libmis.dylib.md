## libmis.dylib

> `/usr/lib/libmis.dylib`

```diff

-463.100.15.0.0
-  __TEXT.__text: 0x3ba8c
-  __TEXT.__auth_stubs: 0x1ce0
-  __TEXT.__objc_methlist: 0xcdc
-  __TEXT.__const: 0x6e60
-  __TEXT.__swift5_typeref: 0x448
-  __TEXT.__swift5_capture: 0x8bc
-  __TEXT.__cstring: 0x506a
+463.100.17.0.0
+  __TEXT.__text: 0x3c8c8
+  __TEXT.__auth_stubs: 0x1d00
+  __TEXT.__objc_methlist: 0xd0c
+  __TEXT.__const: 0x6e80
+  __TEXT.__swift5_typeref: 0x474
+  __TEXT.__swift5_capture: 0x944
+  __TEXT.__cstring: 0x528e
   __TEXT.__constg_swiftt: 0x4b8
   __TEXT.__swift5_builtin: 0x64
   __TEXT.__swift5_mpenum: 0x18

   __TEXT.__swift5_fieldmd: 0x35c
   __TEXT.__swift5_proto: 0x68
   __TEXT.__swift5_types: 0x6c
-  __TEXT.__oslogstring: 0x3319
+  __TEXT.__oslogstring: 0x3401
   __TEXT.__swift5_assocty: 0xa8
   __TEXT.__gcc_except_tab: 0x36c
-  __TEXT.__unwind_info: 0xde8
-  __TEXT.__eh_frame: 0xfd4
+  __TEXT.__unwind_info: 0xe18
+  __TEXT.__eh_frame: 0x1024
   __TEXT.__objc_classname: 0x252
-  __TEXT.__objc_methname: 0x1c69
-  __TEXT.__objc_methtype: 0x509
-  __TEXT.__objc_stubs: 0x1520
+  __TEXT.__objc_methname: 0x1d18
+  __TEXT.__objc_methtype: 0x519
+  __TEXT.__objc_stubs: 0x1560
   __DATA_CONST.__got: 0x2f8
   __DATA_CONST.__const: 0x40d8
   __DATA_CONST.__objc_classlist: 0xb0
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x840
+  __DATA_CONST.__objc_selrefs: 0x860
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x58
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__auth_got: 0xe80
-  __AUTH_CONST.__const: 0x13b0
-  __AUTH_CONST.__cfstring: 0x1ca0
+  __AUTH_CONST.__auth_got: 0xe90
+  __AUTH_CONST.__const: 0x1450
+  __AUTH_CONST.__cfstring: 0x1ce0
   __AUTH_CONST.__objc_const: 0x1528
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0x1b0
   __AUTH.__data: 0x198
   __DATA.__objc_ivar: 0xac
-  __DATA.__data: 0x2d0
+  __DATA.__data: 0x2f0
   __DATA.__bss: 0xc48
   __DATA.__common: 0x70
   __DATA_DIRTY.__objc_data: 0x648

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: CF8700B9-BADF-31F5-B6FC-87CB41C0A7D5
-  Functions: 1183
-  Symbols:   969
-  CStrings:  1367
+  UUID: C3C94363-D313-3F56-961A-F03EEC735F33
+  Functions: 1201
+  Symbols:   971
+  CStrings:  1384
 
Symbols:
+ _swift_initStackObject
+ _swift_setDeallocating
CStrings:
+ "10"
+ "CREATE TABLE IF NOT EXISTS legacy_profile_grace_periods (  uuid TEXT NOT NULL PRIMARY KEY,  grace_period INT NOT NULL,  CONSTRAINT fk_legacy_profile_grace_period_uuid    FOREIGN KEY (uuid)    REFERENCES profiles(uuid)    ON DELETE CASCADE )"
+ "Couldn't create the legacy profile grace periods table: %s"
+ "Error getting legacy profile grace period for %{public}s"
+ "Error getting legacy profile grace periods: %{public}@"
+ "INSERT INTO legacy_profile_grace_periods (uuid, grace_period)\nVALUES (?1, ?2)\nON CONFLICT(uuid) DO UPDATE SET grace_period = ?2"
+ "MISQL: performing database migration 9 -> 10"
+ "SELECT grace_period FROM legacy_profile_grace_periods WHERE uuid = ?1"
+ "SELECT uuid, grace_period FROM legacy_profile_grace_periods"
+ "getLegacyProfileGracePeriodNoThrowWithProfileUUID:"
+ "getLegacyProfileGracePeriodsNoThrow"
+ "i24@0:8@16"
+ "legacyProfileGracePeriods"
+ "legacy_profile_grace_periods"
+ "setLegacyProfileGracePeriodWithProfileUUID:gracePeriod:error:"

```
