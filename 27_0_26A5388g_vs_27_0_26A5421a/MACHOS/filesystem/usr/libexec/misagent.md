## misagent

> `/usr/libexec/misagent`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift5_proto`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_ivar`

```diff

-487.0.0.0.0
-  __TEXT.__text: 0x197b8
-  __TEXT.__auth_stubs: 0x10c0
-  __TEXT.__objc_stubs: 0x11e0
-  __TEXT.__objc_methlist: 0x83c
-  __TEXT.__const: 0x442
-  __TEXT.__oslogstring: 0x1eb7
-  __TEXT.__cstring: 0x345e
-  __TEXT.__objc_classname: 0x141
-  __TEXT.__objc_methname: 0x14e5
-  __TEXT.__objc_methtype: 0x3ac
-  __TEXT.__gcc_except_tab: 0x534
-  __TEXT.__swift5_typeref: 0x266
-  __TEXT.__swift5_capture: 0x870
-  __TEXT.__constg_swiftt: 0x1ac
+487.0.2.0.0
+  __TEXT.__text: 0x1bc70
+  __TEXT.__auth_stubs: 0x10f0
+  __TEXT.__objc_stubs: 0x12e0
+  __TEXT.__objc_methlist: 0x90c
+  __TEXT.__const: 0x4c8
+  __TEXT.__oslogstring: 0x206d
+  __TEXT.__cstring: 0x3929
+  __TEXT.__gcc_except_tab: 0x574
+  __TEXT.__objc_methname: 0x1894
+  __TEXT.__objc_classname: 0x199
+  __TEXT.__objc_methtype: 0x42f
+  __TEXT.__swift5_typeref: 0x2b9
+  __TEXT.__constg_swiftt: 0x22c
+  __TEXT.__swift5_fieldmd: 0x12c
+  __TEXT.__swift5_types: 0x24
+  __TEXT.__swift5_capture: 0x930
+  __TEXT.__swift5_reflstr: 0xc9
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__swift5_reflstr: 0x80
-  __TEXT.__swift5_fieldmd: 0xe8
   __TEXT.__swift5_proto: 0x8
-  __TEXT.__swift5_types: 0x1c
-  __TEXT.__unwind_info: 0x758
-  __TEXT.__eh_frame: 0x504
-  __DATA_CONST.__const: 0xed8
-  __DATA_CONST.__cfstring: 0x1360
-  __DATA_CONST.__objc_classlist: 0x68
+  __TEXT.__unwind_info: 0x7e8
+  __TEXT.__eh_frame: 0x52c
+  __DATA_CONST.__const: 0x10f0
+  __DATA_CONST.__cfstring: 0x13e0
+  __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x48
+  __DATA_CONST.__objc_intobj: 0x18
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA_CONST.__objc_intobj: 0x18
-  __DATA_CONST.__auth_got: 0x870
-  __DATA_CONST.__got: 0x148
-  __DATA_CONST.__auth_ptr: 0xb0
-  __DATA.__objc_const: 0xd90
-  __DATA.__objc_selrefs: 0x5b8
+  __DATA_CONST.__auth_got: 0x888
+  __DATA_CONST.__got: 0x150
+  __DATA_CONST.__auth_ptr: 0xa8
+  __DATA.__objc_const: 0xed8
+  __DATA.__objc_selrefs: 0x610
   __DATA.__objc_ivar: 0x80
-  __DATA.__objc_data: 0x4a0
-  __DATA.__data: 0x2d8
-  __DATA.__bss: 0x190
-  __DATA.__common: 0x20
+  __DATA.__objc_data: 0x630
+  __DATA.__data: 0x360
+  __DATA.__bss: 0x1a0
+  __DATA.__common: 0x28
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/Security.framework/Versions/A/Security
+  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/Versions/A/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreTime.framework/Versions/A/CoreTime
   - /usr/lib/libCoreEntitlements.dylib
   - /usr/lib/libMobileGestalt.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 667
-  Symbols:   301
-  CStrings:  717
+  Functions: 739
+  Symbols:   304
+  CStrings:  764
 
Symbols:
+ _AnalyticsSendEventLazy
+ _OBJC_CLASS_$_OnlineAuthMetrics
+ _OBJC_METACLASS_$_OnlineAuthMetrics
CStrings:
+ ""
+ "11"
+ "?"
+ "@\"NSDictionary\"8@?0"
+ "B36@0:8q16i24^@28"
+ "BuildVersion"
+ "CREATE TABLE IF NOT EXISTS online_auth_migration_state (  id INTEGER NOT NULL PRIMARY KEY CHECK (id = 1),  last_migration_monotonic_time INTEGER NOT NULL,  last_migration_sources_bitmask INTEGER NOT NULL,  last_seen_os_build TEXT NOT NULL )"
+ "Couldn't create the online auth migration state table: %s"
+ "Error getting online auth migration state: %{public}@"
+ "Error setting last seen OS build: %{public}@"
+ "Error setting online auth migration state: %{public}@"
+ "INSERT INTO online_auth_migration_state (\n    id, last_migration_monotonic_time, last_migration_sources_bitmask, last_seen_os_build\n)\nVALUES (1, -1, 0, ?1)\nON CONFLICT(id) DO UPDATE SET last_seen_os_build = ?1"
+ "INSERT INTO online_auth_migration_state (\n    id, last_migration_monotonic_time, last_migration_sources_bitmask, last_seen_os_build\n)\nVALUES (1, ?1, ?2, \"\")\nON CONFLICT(id) DO UPDATE SET\n    last_migration_monotonic_time = ?1,\n    last_migration_sources_bitmask = ?2"
+ "MISOnlineAuthMigrationState"
+ "MISQL: performing database migration 10 -> 11"
+ "Migration: indeterminate entry for profile %{public}@ has no cdHash, skipping"
+ "Migration: rejection entry for profile %{public}@ has no cdHash, skipping"
+ "OnlineAuthMetrics"
+ "SELECT last_migration_monotonic_time, last_migration_sources_bitmask, last_seen_os_build\nFROM online_auth_migration_state\nWHERE id = 1"
+ "T@\"NSString\",N,R"
+ "T@\"OnlineAuthMetrics\",N,R"
+ "Ti,N,R,VlastMigrationSourcesBitmask"
+ "Tq,N,R,VlastMigrationMonotonicTime"
+ "com.apple.mis.onlineauth.indeterminate_detected"
+ "com.apple.mis.onlineauth.migration_completed"
+ "droppedProfileUninstalled"
+ "getOnlineAuthMigrationStateNoThrow"
+ "hoursSinceLastMigration"
+ "hoursSinceLastSuccess"
+ "lastMigrationMonotonicTime"
+ "lastMigrationSource"
+ "lastMigrationSourcesBitmask"
+ "lastSeenOSBuild"
+ "minutesSinceBoot"
+ "misagent.MISOnlineAuthMigrationState"
+ "misagent2"
+ "profileCountOnDevice"
+ "reportIndeterminateDetectedWithReason:gracePeriodDays:hoursSinceLastSuccess:profileCountOnDevice:minutesSinceBoot:hoursSinceLastMigration:lastMigrationSource:profileType:"
+ "reportMigrationCompletedWithSourcesBitmask:droppedNoCDHash:droppedProfileUninstalled:droppedOther:fromOsBuild:"
+ "setLastSeenOSBuild:error:"
+ "setLastSeenOSBuildNoThrow:"
+ "setOnlineAuthMigrationStateNoThrowWithLastMigrationMonotonicTime:lastMigrationSourcesBitmask:"
+ "setOnlineAuthMigrationStateWithLastMigrationMonotonicTime:lastMigrationSourcesBitmask:error:"
+ "shared"
+ "v28@0:8q16i24"
+ "v56@0:8q16q24q32q40@48"
+ "v80@0:8q16q24q32q40q48q56q64q72"
```
