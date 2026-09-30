## misagent

> `/usr/libexec/misagent`

```diff

-463.100.15.0.0
-  __TEXT.__text: 0x18b7c
-  __TEXT.__auth_stubs: 0x12e0
-  __TEXT.__objc_stubs: 0x11e0
-  __TEXT.__objc_methlist: 0x814
-  __TEXT.__const: 0x412
-  __TEXT.__oslogstring: 0x1d3c
-  __TEXT.__cstring: 0x324e
+463.100.17.0.0
+  __TEXT.__text: 0x19dbc
+  __TEXT.__auth_stubs: 0x1350
+  __TEXT.__objc_stubs: 0x1200
+  __TEXT.__objc_methlist: 0x83c
+  __TEXT.__const: 0x452
+  __TEXT.__oslogstring: 0x1f07
+  __TEXT.__cstring: 0x344e
   __TEXT.__objc_classname: 0x151
-  __TEXT.__objc_methname: 0x1450
-  __TEXT.__objc_methtype: 0x3a1
-  __TEXT.__gcc_except_tab: 0x4ac
-  __TEXT.__swift5_typeref: 0x21c
-  __TEXT.__swift5_capture: 0x7e8
+  __TEXT.__objc_methname: 0x14e5
+  __TEXT.__objc_methtype: 0x3ac
+  __TEXT.__gcc_except_tab: 0x520
+  __TEXT.__swift5_typeref: 0x266
+  __TEXT.__swift5_capture: 0x870
   __TEXT.__constg_swiftt: 0x1ac
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_mpenum: 0x10

   __TEXT.__swift5_fieldmd: 0xe8
   __TEXT.__swift5_proto: 0x8
   __TEXT.__swift5_types: 0x1c
-  __TEXT.__unwind_info: 0x6e8
-  __TEXT.__eh_frame: 0x4b4
-  __DATA_CONST.__auth_got: 0x980
-  __DATA_CONST.__got: 0x158
-  __DATA_CONST.__auth_ptr: 0xb8
-  __DATA_CONST.__const: 0xd98
-  __DATA_CONST.__cfstring: 0x1440
+  __TEXT.__unwind_info: 0x720
+  __TEXT.__eh_frame: 0x504
+  __DATA_CONST.__auth_got: 0x9b8
+  __DATA_CONST.__got: 0x168
+  __DATA_CONST.__auth_ptr: 0xc0
+  __DATA_CONST.__const: 0xe38
+  __DATA_CONST.__cfstring: 0x1480
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_intobj: 0x18
   __DATA.__objc_const: 0xd90
-  __DATA.__objc_selrefs: 0x5a0
+  __DATA.__objc_selrefs: 0x5b8
   __DATA.__objc_ivar: 0x80
   __DATA.__objc_data: 0x4a0
-  __DATA.__data: 0x2b0
+  __DATA.__data: 0x2d8
   __DATA.__bss: 0x170
   __DATA.__common: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: FAD22176-8FE5-39E7-8890-F2B1C0B70A7E
-  Functions: 647
-  Symbols:   341
-  CStrings:  880
+  UUID: 0385E13C-A4C4-3562-8C59-BD600A0C1E4B
+  Functions: 669
+  Symbols:   344
+  CStrings:  898
 
Symbols:
+ __swiftEmptyDictionarySingleton
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
+ "Migration: Error setting legacy profile grace period for %{public}@: %{public}@"
+ "Migration: Starting migration of legacy profile grace periods from %{public}@"
+ "Profile %{public}@ has grace period but is not installed, skipping"
+ "SELECT grace_period FROM legacy_profile_grace_periods WHERE uuid = ?1"
+ "SELECT uuid, grace_period FROM legacy_profile_grace_periods"
+ "getLegacyProfileGracePeriodNoThrowWithProfileUUID:"
+ "getLegacyProfileGracePeriodsNoThrow"
+ "i24@0:8@16"
+ "setLegacyProfileGracePeriodWithProfileUUID:gracePeriod:error:"

```
