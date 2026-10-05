## IOMFB_bics_daemon

> `/usr/libexec/IOMFB_bics_daemon`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_assocty`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_proto`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`

```diff

-700.50.104.1.0
-  __TEXT.__text: 0x31770
-  __TEXT.__auth_stubs: 0x1350
+700.50.108.0.0
+  __TEXT.__text: 0x31d38
+  __TEXT.__auth_stubs: 0x1380
   __TEXT.__objc_stubs: 0x160
   __TEXT.__objc_methlist: 0x5c
-  __TEXT.__cstring: 0x587c
+  __TEXT.__cstring: 0x5a1c
   __TEXT.__const: 0x5f44
   __TEXT.__oslogstring: 0x24
-  __TEXT.__gcc_except_tab: 0xaf8
-  __TEXT.__objc_methname: 0xea
-  __TEXT.__objc_classname: 0x2a
-  __TEXT.__objc_methtype: 0xb0
+  __TEXT.__gcc_except_tab: 0xb04
+  __TEXT.__objc_methname: 0xff
+  __TEXT.__objc_classname: 0x1e
+  __TEXT.__objc_methtype: 0x111
   __TEXT.__swift5_typeref: 0x90e
   __TEXT.__swift5_reflstr: 0x278
   __TEXT.__swift5_assocty: 0x360

   __TEXT.__swift5_types: 0x38
   __TEXT.__swift5_protos: 0x50
   __TEXT.__swift5_types2: 0x4
-  __TEXT.__unwind_info: 0xfa0
+  __TEXT.__unwind_info: 0xfd0
   __TEXT.__eh_frame: 0xd40
-  __DATA_CONST.__const: 0xf48
+  __DATA_CONST.__const: 0xf60
   __DATA_CONST.__cfstring: 0x2a0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
-  __DATA_CONST.__auth_got: 0x9c0
-  __DATA_CONST.__got: 0x258
+  __DATA_CONST.__auth_got: 0x9d8
+  __DATA_CONST.__got: 0x290
   __DATA_CONST.__auth_ptr: 0x538
-  __DATA.__objc_const: 0x218
+  __DATA.__objc_const: 0x258
   __DATA.__objc_selrefs: 0x60
-  __DATA.__objc_ivar: 0x18
+  __DATA.__objc_ivar: 0x20
   __DATA.__objc_data: 0xa0
-  __DATA.__data: 0xc40
-  __DATA.__common: 0x28
+  __DATA.__data: 0xc38
+  __DATA.__common: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  Functions: 997
-  Symbols:   506
-  CStrings:  835
+  Functions: 1009
+  Symbols:   515
+  CStrings:  848
 
Symbols:
+ _XPC_ACTIVITY_ALLOW_BATTERY
+ _XPC_ACTIVITY_GRACE_PERIOD
+ _XPC_ACTIVITY_INTERVAL
+ _XPC_ACTIVITY_PRIORITY
+ _XPC_ACTIVITY_PRIORITY_UTILITY
+ _XPC_ACTIVITY_REPEATING
+ _xpc_activity_copy_criteria
+ _xpc_activity_set_criteria
+ _xpc_copy_description
CStrings:
+ "%s %s: drLTH keyed to a different MLB; deferring import to migration"
+ "@\"BICSXpcListener\""
+ "@32@0:8r*16^{bics_command_table_t=^{bics_command_entry_t}i}24"
+ "@40@0:8@16@24^{bics_command_table_t=^{bics_command_entry_t}i}32"
+ "BICS activity criteria: %s\n"
+ "BICSDaemonIntervalSeconds"
+ "BICSXpcClient"
+ "BICSXpcClient::_handleMessage without type"
+ "BICSXpcClient::initWithConnection"
+ "BICSXpcListener"
+ "BICSXpcListener client created %@"
+ "BICSXpcListener client removed %@"
+ "BICSXpcListener::initWithService %s"
+ "FactoryClearAllBICS"
+ "^{bics_command_table_t=^{bics_command_entry_t}i}"
+ "_table"
+ "com.apple.iomfb_bics_daemon.control"
+ "factory_clear_all_bics: armed %s; reboot required to complete"
+ "factory_clear_all_bics: clearing all BICS data for %s"
+ "factory_clear_all_bics: failed to arm %s"
+ "initWithConnection:listener:table:"
+ "initWithService:table:"
+ "overriding BICS daemon interval to %u s\n"
+ "primary"
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
