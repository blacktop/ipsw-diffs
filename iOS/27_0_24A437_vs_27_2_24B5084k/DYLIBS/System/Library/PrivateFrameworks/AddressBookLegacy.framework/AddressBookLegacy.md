## AddressBookLegacy

> `/System/Library/PrivateFrameworks/AddressBookLegacy.framework/AddressBookLegacy`

```diff

-12877.100.1.0.0
-  __TEXT.__text: 0x766d4
+12880.200.11.0.0
+  __TEXT.__text: 0x76c20
   __TEXT.__objc_methlist: 0x307c
   __TEXT.__const: 0x371
-  __TEXT.__cstring: 0x26ff0
-  __TEXT.__oslogstring: 0x2eff
+  __TEXT.__cstring: 0x2708d
+  __TEXT.__oslogstring: 0x306b
   __TEXT.__gcc_except_tab: 0x644
   __TEXT.__dlopen_cstrs: 0xb8
   __TEXT.__ustring: 0x24c
-  __TEXT.__unwind_info: 0x23f8
+  __TEXT.__unwind_info: 0x2428
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_superrefs: 0x100
   __DATA_CONST.__objc_arraydata: 0x48
   __DATA_CONST.__got: 0x5d8
-  __AUTH_CONST.__const: 0xf00
-  __AUTH_CONST.__cfstring: 0xde40
+  __AUTH_CONST.__const: 0xf20
+  __AUTH_CONST.__cfstring: 0xde80
   __AUTH_CONST.__objc_const: 0x4cb0
   __AUTH_CONST.__objc_doubleobj: 0x60
   __AUTH_CONST.__objc_intobj: 0x120
   __AUTH_CONST.__objc_arrayobj: 0x48
-  __AUTH_CONST.__auth_got: 0x1148
+  __AUTH_CONST.__auth_got: 0x1170
   __AUTH.__objc_data: 0xbe0
   __DATA.__objc_ivar: 0x400
-  __DATA.__data: 0x2c8
+  __DATA.__data: 0x2d0
   __DATA.__common: 0x4
   __DATA_DIRTY.__objc_data: 0x410
   __DATA_DIRTY.__data: 0x168

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 2633
-  Symbols:   5451
-  CStrings:  2552
+  Functions: 2645
+  Symbols:   5468
+  CStrings:  2562
 
Symbols:
+ _ABMigrationGateBegin
+ _ABMigrationGateEnd
+ _ABMigrationGateRenew
+ _ABMigrationGateTimeNow
+ _ABMigrationGateTimeNow.timebase_info
+ _ABMigrationGateWaitIfNeeded
+ __ABMigrationGateIsActive
+ __ABMigrationGateSetExpiry
+ __ABMigrationGateToken.once
+ __ABMigrationGateToken.token
+ ___ABIsMigratorProcess
+ ____ABMigrationGateToken_block_invoke
+ _mach_continuous_time
+ _mach_timebase_info
+ _notify_post
+ _notify_register_check
+ _notify_set_state
CStrings:
+ " ), all_person_ids(rowid, PersonLink%@) AS MATERIALIZED (SELECT pm.rowid, pm.PersonLink%@ FROM preferredmatched pm WHERE pm.PersonLink = -1 UNION ALL SELECT abp.rowid, abp.PersonLink%@ FROM preferredmatched pm JOIN ABPerson abp ON abp.PersonLink = pm.PersonLink WHERE pm.PersonLink != -1 %@) "
+ "AB Migration - claimed database gate; clients will wait"
+ "AB Migration - database gate cleared after %llus"
+ "AB Migration - deferring database access until migration completes"
+ "AB Migration - failed to get database gate token"
+ "AB Migration - gate wait timed out after %.0fs; proceeding"
+ "AB Migration - released database gate"
+ "AB Migration - renewed claim on database gate"
+ "ORDER BY 2, 1 "
+ "ORDER BY 3, 4, 5, 2, 1 "
+ "all_person_ids.PersonLink, all_person_ids.rowid "
+ "com.apple.AddressBook.migration-in-progress"
- " ), all_person_ids(rowid%@) AS NOT MATERIALIZED (SELECT pm.rowid%@ FROM preferredmatched pm WHERE pm.PersonLink = -1 UNION ALL SELECT abp.rowid%@ FROM preferredmatched pm JOIN ABPerson abp ON abp.PersonLink = pm.PersonLink WHERE pm.PersonLink != -1 ) "
- "abp.PersonLink "
```
