## online-auth-agent

> `/usr/libexec/online-auth-agent`

```diff

-463.100.15.0.0
-  __TEXT.__text: 0x4296c
+463.100.17.0.0
+  __TEXT.__text: 0x4384c
   __TEXT.__auth_stubs: 0x1e60
-  __TEXT.__objc_stubs: 0x1f00
-  __TEXT.__objc_methlist: 0x784
-  __TEXT.__const: 0x244c
-  __TEXT.__cstring: 0x3b4c
+  __TEXT.__objc_stubs: 0x1f20
+  __TEXT.__objc_methlist: 0x7ac
+  __TEXT.__const: 0x246c
+  __TEXT.__cstring: 0x3d4c
   __TEXT.__gcc_except_tab: 0x414
-  __TEXT.__objc_methname: 0x1e35
-  __TEXT.__oslogstring: 0x382b
+  __TEXT.__objc_methname: 0x1ed5
+  __TEXT.__oslogstring: 0x399b
   __TEXT.__objc_classname: 0x358
-  __TEXT.__objc_methtype: 0x524
+  __TEXT.__objc_methtype: 0x534
   __TEXT.__dlopen_cstrs: 0x5e
-  __TEXT.__swift5_typeref: 0x913
-  __TEXT.__swift5_capture: 0x5e8
+  __TEXT.__swift5_typeref: 0x949
+  __TEXT.__swift5_capture: 0x670
   __TEXT.__constg_swiftt: 0xbfc
   __TEXT.__swift5_builtin: 0x8c
   __TEXT.__swift5_mpenum: 0x18

   __TEXT.__swift5_types: 0xf0
   __TEXT.__swift5_protos: 0xc
   __TEXT.__swift5_assocty: 0x168
-  __TEXT.__unwind_info: 0xf60
-  __TEXT.__eh_frame: 0x1310
+  __TEXT.__unwind_info: 0xf88
+  __TEXT.__eh_frame: 0x1360
   __DATA_CONST.__auth_got: 0xf40
-  __DATA_CONST.__got: 0x498
+  __DATA_CONST.__got: 0x4a0
   __DATA_CONST.__auth_ptr: 0x470
-  __DATA_CONST.__const: 0x2558
-  __DATA_CONST.__cfstring: 0x1500
+  __DATA_CONST.__const: 0x25f8
+  __DATA_CONST.__cfstring: 0x1540
   __DATA_CONST.__objc_classlist: 0xa0
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA.__objc_const: 0x1420
-  __DATA.__objc_selrefs: 0x958
+  __DATA.__objc_selrefs: 0x970
   __DATA.__objc_ivar: 0x60
   __DATA.__objc_data: 0x4c0
-  __DATA.__data: 0x1698
+  __DATA.__data: 0x16b8
   __DATA.__bss: 0x3050
   __DATA.__common: 0x118
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 053F7132-8BEF-3AAD-AE5A-8E5971F6B2D8
-  Functions: 1334
+  UUID: 5518743C-3606-3A28-A871-D9874814C6F9
+  Functions: 1352
   Symbols:   445
-  CStrings:  1292
+  CStrings:  1309
 
CStrings:
+ "10"
+ "Applying legacy grace period %d for %{public}@, %{public}@"
+ "CREATE TABLE IF NOT EXISTS legacy_profile_grace_periods (  uuid TEXT NOT NULL PRIMARY KEY,  grace_period INT NOT NULL,  CONSTRAINT fk_legacy_profile_grace_period_uuid    FOREIGN KEY (uuid)    REFERENCES profiles(uuid)    ON DELETE CASCADE )"
+ "Couldn't create the legacy profile grace periods table: %s"
+ "Error applying legacy grace period for %{public}@, %{public}@: %{public}@"
+ "Error getting legacy profile grace period for %{public}s"
+ "Error getting legacy profile grace periods: %{public}@"
+ "INSERT INTO legacy_profile_grace_periods (uuid, grace_period)\nVALUES (?1, ?2)\nON CONFLICT(uuid) DO UPDATE SET grace_period = ?2"
+ "MISQL: performing database migration 9 -> 10"
+ "SELECT grace_period FROM legacy_profile_grace_periods WHERE uuid = ?1"
+ "SELECT uuid, grace_period FROM legacy_profile_grace_periods"
+ "getLegacyProfileGracePeriodNoThrowWithProfileUUID:"
+ "getLegacyProfileGracePeriodsNoThrow"
+ "i24@0:8@16"
+ "setLegacyProfileGracePeriodWithProfileUUID:gracePeriod:error:"

```
