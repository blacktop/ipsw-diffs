## IOMFB_bics_daemon

> `/usr/libexec/IOMFB_bics_daemon`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_assocty`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_proto`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`

```diff

-700.50.97.9.0
-  __TEXT.__text: 0x306ec
-  __TEXT.__auth_stubs: 0x11c0
+700.50.117.0.0
+  __TEXT.__text: 0x3058c
+  __TEXT.__auth_stubs: 0x1220
   __TEXT.__objc_stubs: 0x280
   __TEXT.__objc_methlist: 0x5c
-  __TEXT.__cstring: 0x4e1c
-  __TEXT.__const: 0x5f14
+  __TEXT.__cstring: 0x538c
+  __TEXT.__const: 0x2c74
   __TEXT.__oslogstring: 0x24
-  __TEXT.__gcc_except_tab: 0xb40
-  __TEXT.__objc_methname: 0x1ab
-  __TEXT.__objc_classname: 0x2a
-  __TEXT.__objc_methtype: 0xb0
+  __TEXT.__gcc_except_tab: 0xb68
+  __TEXT.__objc_methname: 0x1c0
+  __TEXT.__objc_classname: 0x1e
+  __TEXT.__objc_methtype: 0x111
   __TEXT.__swift5_typeref: 0x90e
   __TEXT.__swift5_reflstr: 0x278
   __TEXT.__swift5_assocty: 0x360

   __TEXT.__swift5_types: 0x38
   __TEXT.__swift5_protos: 0x50
   __TEXT.__swift5_types2: 0x4
-  __TEXT.__unwind_info: 0xf58
+  __TEXT.__unwind_info: 0xff0
   __TEXT.__eh_frame: 0xd40
-  __DATA_CONST.__const: 0xf60
-  __DATA_CONST.__cfstring: 0x3a0
+  __DATA_CONST.__const: 0xf78
+  __DATA_CONST.__cfstring: 0x3c0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
-  __DATA_CONST.__auth_got: 0x8f8
-  __DATA_CONST.__got: 0x240
-  __DATA_CONST.__auth_ptr: 0x538
-  __DATA.__objc_const: 0x218
+  __DATA_CONST.__auth_got: 0x928
+  __DATA_CONST.__got: 0x280
+  __DATA_CONST.__auth_ptr: 0x590
+  __DATA.__objc_const: 0x258
   __DATA.__objc_selrefs: 0xa8
-  __DATA.__objc_ivar: 0x18
+  __DATA.__objc_ivar: 0x20
   __DATA.__objc_data: 0xa0
-  __DATA.__data: 0xc00
-  __DATA.__bss: 0x16e0
-  __DATA.__common: 0x30
+  __DATA.__data: 0xc38
+  __DATA.__bss: 0x16f0
+  __DATA.__common: 0x28
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  Functions: 959
-  Symbols:   480
-  CStrings:  758
+  Functions: 975
+  Symbols:   492
+  CStrings:  788
 
Symbols:
+ _XPC_ACTIVITY_ALLOW_BATTERY
+ _XPC_ACTIVITY_GRACE_PERIOD
+ _XPC_ACTIVITY_INTERVAL
+ _XPC_ACTIVITY_PRIORITY
+ _XPC_ACTIVITY_PRIORITY_UTILITY
+ _XPC_ACTIVITY_REPEATING
+ ___cxa_atexit
+ ___cxa_guard_acquire
+ ___cxa_guard_release
+ _xpc_activity_copy_criteria
+ _xpc_activity_set_criteria
+ _xpc_copy_description
CStrings:
+ "%s %s: drLTH keyed to a different MLB; deferring import to migration"
+ "%s: DCP rejected imported drLTH (payload CRC or key mismatch)"
+ "%s: Failed to publish migration expiry to ioreg: 0x%x\n"
+ "%s: Failed to update migration record on display nand: %s\n"
+ "@\"BICSXpcListener\""
+ "@32@0:8r*16^{bics_command_table_t=^{bics_command_entry_t}i}24"
+ "@40@0:8@16@24^{bics_command_table_t=^{bics_command_entry_t}i}32"
+ "BICS activity criteria: %s\n"
+ "BICSDaemonIntervalSeconds"
+ "BICSMigrationLastExpiry"
+ "BICSXpcClient"
+ "BICSXpcClient::_handleMessage without type"
+ "BICSXpcClient::initWithConnection"
+ "BICSXpcListener"
+ "BICSXpcListener client created %@"
+ "BICSXpcListener client removed %@"
+ "BICSXpcListener::initWithService %s"
+ "DMIG"
+ "FactoryClearAllBICS"
+ "^{bics_command_table_t=^{bics_command_entry_t}i}"
+ "_table"
+ "com.apple.iomfb_bics_daemon.control"
+ "daemon_shutdown: skipping shutdown processing during userspace reboot"
+ "erase_expired_dstore_data: failed to erase %s from dstore: %s"
+ "factory_clear_all_bics: armed %s; reboot required to complete"
+ "factory_clear_all_bics: clearing all BICS data for %s"
+ "factory_clear_all_bics: failed to arm %s"
+ "initWithConnection:listener:table:"
+ "initWithService:table:"
+ "kern.willuserspacereboot"
+ "migrate_status"
+ "modeInfoUpdate: ICC curve loc %u is tabular (type %u), skipping the ICC cache and saving mode/preset/UA only\n"
+ "modeInfoUpdate: no write, EAN mode caching unsupported by the driver\n"
+ "modeInfoUpdate: no write, EAN storage not present\n"
+ "modeInfoUpdate: no write, throttled: avg interval %llu s < threshold %llu s (%llu updates over %llu s), persisted record stays stale\n"
+ "modeInfoUpdate: no write, v1CRC 0x%x unchanged, validMask 0x%llx\n"
+ "modeInfoUpdate: writing %u bytes to EAN, validMask 0x%llx (mode %d preset %d iccMat %d iccCurve %d ua %d)\n"
+ "overriding BICS daemon interval to %u s\n"
+ "primary"
+ "publish_migration_last_expiry"
+ "store_migration_record"
+ "xpc_factory_clear_bics: refused on non-internal build"
- "@\"BICSMigrationListener\""
- "@24@0:8^{migration_table_t=^{migration_table_entry_t}i}16"
- "@32@0:8@16@24"
- "BICSMigrationClient"
- "BICSMigrationClient::_handleMessage without type"
- "BICSMigrationClient::initWithConnection"
- "BICSMigrationListener"
- "BICSMigrationListener client created %@"
- "BICSMigrationListener client removed %@"
- "BICSMigrationListener::initWithTable"
- "initWithConnection:listener:"
- "initWithTable:"
```
