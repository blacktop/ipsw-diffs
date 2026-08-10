## online-auth-agent

> `/usr/libexec/online-auth-agent`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_assocty`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__got`
- `__DATA.__objc_ivar`
- `__DATA.__bss`
- `__DATA.__common`

```diff

-487.0.0.0.0
-  __TEXT.__text: 0x3ca2c
+487.0.2.0.0
+  __TEXT.__text: 0x3d9d4
   __TEXT.__auth_stubs: 0x1e20
-  __TEXT.__objc_stubs: 0x1c40
-  __TEXT.__objc_methlist: 0x7ac
-  __TEXT.__const: 0x23fc
-  __TEXT.__cstring: 0x3c4b
+  __TEXT.__objc_stubs: 0x1c80
+  __TEXT.__objc_methlist: 0x82c
+  __TEXT.__const: 0x2458
+  __TEXT.__oslogstring: 0x2ee5
+  __TEXT.__cstring: 0x4045
+  __TEXT.__objc_methname: 0x1f55
+  __TEXT.__objc_classname: 0x378
+  __TEXT.__objc_methtype: 0x554
   __TEXT.__gcc_except_tab: 0x384
-  __TEXT.__objc_methname: 0x1d25
-  __TEXT.__oslogstring: 0x2ddb
-  __TEXT.__objc_classname: 0x358
-  __TEXT.__objc_methtype: 0x534
   __TEXT.__dlopen_cstrs: 0x5e
-  __TEXT.__swift5_typeref: 0x949
-  __TEXT.__swift5_capture: 0x670
-  __TEXT.__constg_swiftt: 0xbfc
+  __TEXT.__swift5_typeref: 0x958
+  __TEXT.__constg_swiftt: 0xc38
+  __TEXT.__swift5_reflstr: 0x7d4
+  __TEXT.__swift5_fieldmd: 0xa1c
+  __TEXT.__swift5_proto: 0x198
+  __TEXT.__swift5_types: 0xf4
+  __TEXT.__swift5_capture: 0x688
   __TEXT.__swift5_builtin: 0x8c
   __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__swift5_reflstr: 0x795
-  __TEXT.__swift5_fieldmd: 0x9e8
-  __TEXT.__swift5_proto: 0x198
-  __TEXT.__swift5_types: 0xf0
   __TEXT.__swift5_protos: 0xc
   __TEXT.__swift5_assocty: 0x168
-  __TEXT.__unwind_info: 0xec0
-  __TEXT.__eh_frame: 0x1290
-  __DATA_CONST.__const: 0x2488
-  __DATA_CONST.__cfstring: 0x14a0
-  __DATA_CONST.__objc_classlist: 0xa0
+  __TEXT.__unwind_info: 0xee8
+  __TEXT.__eh_frame: 0x12b8
+  __DATA_CONST.__const: 0x2510
+  __DATA_CONST.__cfstring: 0x14e0
+  __DATA_CONST.__objc_classlist: 0xa8
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10

   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__auth_got: 0xf20
   __DATA_CONST.__got: 0x458
-  __DATA_CONST.__auth_ptr: 0x468
-  __DATA.__objc_const: 0x1420
-  __DATA.__objc_selrefs: 0x8c0
+  __DATA_CONST.__auth_ptr: 0x480
+  __DATA.__objc_const: 0x1508
+  __DATA.__objc_selrefs: 0x900
   __DATA.__objc_ivar: 0x60
-  __DATA.__objc_data: 0x4c0
-  __DATA.__data: 0x16b8
+  __DATA.__objc_data: 0x590
+  __DATA.__data: 0x16e0
   __DATA.__bss: 0x3050
   __DATA.__common: 0x118
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /System/Library/PrivateFrameworks/DeviceIdentity.framework/DeviceIdentity
   - /System/Library/PrivateFrameworks/InstalledContentLibrary.framework/InstalledContentLibrary
   - /System/Library/PrivateFrameworks/MessageSecurity.framework/MessageSecurity
-  - /System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset
   - /System/Library/PrivateFrameworks/MobileInstallation.framework/MobileInstallation
   - /System/Library/PrivateFrameworks/ProfileValidatedAppIdentity.framework/ProfileValidatedAppIdentity
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 1265
+  Functions: 1292
   Symbols:   434
-  CStrings:  1017
+  CStrings:  1045
 
CStrings:
+ "11"
+ "2f319679-66b9-44cf-9cf0-723471de0db9"
+ "?"
+ "B36@0:8q16i24^@28"
+ "CREATE TABLE IF NOT EXISTS online_auth_migration_state (  id INTEGER NOT NULL PRIMARY KEY CHECK (id = 1),  last_migration_monotonic_time INTEGER NOT NULL,  last_migration_sources_bitmask INTEGER NOT NULL,  last_seen_os_build TEXT NOT NULL )"
+ "Couldn't create the online auth migration state table: %s"
+ "Error getting online auth migration state: %{public}@"
+ "Error setting last seen OS build: %{public}@"
+ "Error setting online auth migration state: %{public}@"
+ "INSERT INTO online_auth_migration_state (\n    id, last_migration_monotonic_time, last_migration_sources_bitmask, last_seen_os_build\n)\nVALUES (1, -1, 0, ?1)\nON CONFLICT(id) DO UPDATE SET last_seen_os_build = ?1"
+ "INSERT INTO online_auth_migration_state (\n    id, last_migration_monotonic_time, last_migration_sources_bitmask, last_seen_os_build\n)\nVALUES (1, ?1, ?2, \"\")\nON CONFLICT(id) DO UPDATE SET\n    last_migration_monotonic_time = ?1,\n    last_migration_sources_bitmask = ?2"
+ "MISOnlineAuthMigrationState"
+ "MISQL: performing database migration 10 -> 11"
+ "SELECT last_migration_monotonic_time, last_migration_sources_bitmask, last_seen_os_build\nFROM online_auth_migration_state\nWHERE id = 1"
+ "T@\"NSString\",N,R"
+ "Ti,N,R,VlastMigrationSourcesBitmask"
+ "Tq,N,R,VlastMigrationMonotonicTime"
+ "adaea588-c074-4b87-b8ea-26cb685b3443"
+ "getOnlineAuthMigrationStateNoThrow"
+ "lastMigrationMonotonicTime"
+ "lastMigrationSourcesBitmask"
+ "lastSeenOSBuild"
+ "online_auth_agent.MISOnlineAuthMigrationState"
+ "setLastSeenOSBuild:error:"
+ "setLastSeenOSBuildNoThrow:"
+ "setOnlineAuthMigrationStateNoThrowWithLastMigrationMonotonicTime:lastMigrationSourcesBitmask:"
+ "setOnlineAuthMigrationStateWithLastMigrationMonotonicTime:lastMigrationSourcesBitmask:error:"
+ "v28@0:8q16i24"
```
