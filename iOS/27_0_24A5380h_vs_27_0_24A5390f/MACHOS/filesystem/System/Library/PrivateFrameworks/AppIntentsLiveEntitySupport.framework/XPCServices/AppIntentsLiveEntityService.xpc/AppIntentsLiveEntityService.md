## AppIntentsLiveEntityService

> `/System/Library/PrivateFrameworks/AppIntentsLiveEntitySupport.framework/XPCServices/AppIntentsLiveEntityService.xpc/AppIntentsLiveEntityService`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_entry`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift5_assocty`
- `__DATA.__objc_data`

```diff

-301.0.43.6.0
-  __TEXT.__text: 0x30f4c
-  __TEXT.__auth_stubs: 0x1450
-  __TEXT.__objc_stubs: 0x380
-  __TEXT.__const: 0x1458
+301.0.45.4.101
+  __TEXT.__text: 0x4a63c
+  __TEXT.__auth_stubs: 0x16f0
+  __TEXT.__objc_stubs: 0x440
+  __TEXT.__const: 0x1a9c
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__oslogstring: 0xac3
-  __TEXT.__swift5_typeref: 0x768
-  __TEXT.__cstring: 0xd59
-  __TEXT.__constg_swiftt: 0x3d4
+  __TEXT.__oslogstring: 0x14c3
+  __TEXT.__swift5_typeref: 0x9cc
+  __TEXT.__cstring: 0x1089
+  __TEXT.__constg_swiftt: 0x4e0
   __TEXT.__swift5_builtin: 0x28
-  __TEXT.__swift5_reflstr: 0x229
-  __TEXT.__swift5_fieldmd: 0x288
-  __TEXT.__swift5_types: 0x38
-  __TEXT.__swift_as_entry: 0x114
-  __TEXT.__swift_as_ret: 0x150
-  __TEXT.__swift_as_cont: 0x1ec
-  __TEXT.__swift5_proto: 0x74
-  __TEXT.__objc_classname: 0x17f
-  __TEXT.__objc_methname: 0x3d3
+  __TEXT.__swift5_reflstr: 0x2ae
+  __TEXT.__swift5_fieldmd: 0x380
+  __TEXT.__swift5_types: 0x4c
+  __TEXT.__swift_as_entry: 0x190
+  __TEXT.__swift_as_ret: 0x1e4
+  __TEXT.__swift_as_cont: 0x2d0
+  __TEXT.__objc_classname: 0x1bf
+  __TEXT.__objc_methname: 0x424
   __TEXT.__objc_methtype: 0x3d
-  __TEXT.__swift5_capture: 0xb78
+  __TEXT.__swift5_capture: 0x1224
   __TEXT.__swift5_mpenum: 0x8
+  __TEXT.__swift5_proto: 0x80
   __TEXT.__swift5_assocty: 0xa8
-  __TEXT.__swift5_acfuncs: 0xb4
-  __TEXT.__unwind_info: 0xdf8
-  __TEXT.__eh_frame: 0x3090
-  __DATA_CONST.__const: 0x2028
-  __DATA_CONST.__objc_classlist: 0x38
+  __TEXT.__swift5_acfuncs: 0x104
+  __TEXT.__unwind_info: 0x1280
+  __TEXT.__eh_frame: 0x4388
+  __DATA_CONST.__const: 0x30c0
+  __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0xa30
-  __DATA_CONST.__got: 0x330
-  __DATA_CONST.__auth_ptr: 0x318
-  __DATA.__objc_const: 0x5b0
-  __DATA.__objc_selrefs: 0xe0
+  __DATA_CONST.__auth_got: 0xb80
+  __DATA_CONST.__got: 0x390
+  __DATA_CONST.__auth_ptr: 0x390
+  __DATA.__objc_const: 0x688
+  __DATA.__objc_selrefs: 0x110
   __DATA.__objc_data: 0xf0
-  __DATA.__data: 0xa70
-  __DATA.__common: 0x50
-  __DATA.__bss: 0xe80
+  __DATA.__data: 0xdc0
+  __DATA.__common: 0x58
+  __DATA.__bss: 0x1000
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/AppIntentsLiveEntitySupport.framework/AppIntentsLiveEntitySupport
   - /System/Library/PrivateFrameworks/LinkMetadata.framework/LinkMetadata
   - /System/Library/PrivateFrameworks/LinkServices.framework/LinkServices
+  - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/XPCDistributed.framework/XPCDistributed
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1295
-  Symbols:   200
-  CStrings:  156
+  Functions: 1848
+  Symbols:   219
+  CStrings:  202
 
Symbols:
+ _OBJC_CLASS_$_NSNumber
+ _OBJC_CLASS_$_RBSProcessHandle
+ __swiftEmptySetSingleton
+ _objc_retain_x22
+ _objc_retain_x24
+ _objc_retain_x26
+ _sqlite3_bind_null
+ _sqlite3_changes
+ _sqlite3_column_type
+ _swift_bridgeObjectRelease_n
+ _swift_cvw_initEnumMetadataMultiPayloadWithLayoutString
+ _swift_cvw_multiPayloadEnumGeneric_destructiveInjectEnumTag
+ _swift_cvw_multiPayloadEnumGeneric_getEnumTag
+ _swift_getDynamicType
+ _swift_getEnumCaseMultiPayload
+ _swift_getObjCClassFromMetadata
+ _swift_release_n
+ _swift_release_x1
+ _swift_storeEnumTagMultiPayload
CStrings:
+ "    CREATE TABLE \"feedMetadata\" (\n        \"feedId\" TEXT PRIMARY KEY NOT NULL,\n        \"lastUpdate\" TEXT NOT NULL\n    );\n    CREATE TABLE \"feedEntries\" (\n        \"feedId\" TEXT NOT NULL,\n        \"bootId\" TEXT NOT NULL,\n        \"bundleId\" TEXT NOT NULL,\n        \"entityId\" TEXT NOT NULL,\n        \"lastUpdate\" TEXT NOT NULL,\n        \"lnValue\" BLOB NOT NULL,\n        \"metadata\" BLOB,\n        PRIMARY KEY (\"feedId\", \"bundleId\", \"entityID\"),\n        FOREIGN KEY (\"feedId\") REFERENCES \"feedMetadata\"(\"feedId\")\n    );\n    CREATE INDEX \"idx_feedEntries_bootId\" ON \"feedEntries\"(\"bootId\");\n    CREATE INDEX \"idx_feedEntries_bundleId\" ON \"feedEntries\"(\"bundleId\");\n    CREATE INDEX \"idx_feedEntries_feedId\" ON \"feedEntries\"(\"feedId\");"
+ " completed with neither output nor error"
+ "%s: fetching feed metadata"
+ "%s: fetching rows for bootId %s"
+ "%s::invalidateDatabaseFilesForTesting()"
+ "%s::setLastUpdateForTesting(feedId: %{public}s, newValue: %{public}fs from now)"
+ "%s::setMetadataForTesting(feedId: %{public}s, bundleId: %{public}s, entityId: %{public}s)"
+ "%s::state() completed for %s: %{public}ld fresh row(s) returned, %{public}ld aged row(s) handed off for rehydration"
+ "DELETE FROM feedEntries WHERE feedId = ? AND lastUpdate < ?"
+ "Deleted row %{public}s::%{public}s::%{sensitive,mask.hash}s"
+ "Dropping row with unknown feedId %{public}s"
+ "Dropping terminally aged row %{public}s::%{public}s from response (age=%{public}fs)"
+ "EntityQuery returned "
+ "Evicted %{public}ld aged entries from %{public}s (threshold: %{public}fs ago)"
+ "Evicted %{public}ld expired entries from %{public}s (olderThan: %{public}s)"
+ "Failed to encode origin metadata for %{public}s: %@"
+ "INSERT INTO feedEntries (\"feedId\", \"bootId\", \"bundleId\", \"entityId\", \"lastUpdate\", \"lnValue\") VALUES ( ?, ?, ?, ?, ?, ? )"
+ "Including aged row %{public}s::%{public}s in response and queueing for rehydration (age=%{public}fs, maxAge=%{public}fs)"
+ "Originating process for: %{public}s::%{public}s origin pid=%{public}d pidversion=%{public}d doesn't exist, evicting entity"
+ "ProcessLivenessCheck: no RunningBoard process for pid=%{public}d (%{public}s)"
+ "REPLACE INTO feedEntries (\"feedId\", \"bootId\", \"bundleId\", \"entityId\", \"lastUpdate\", \"lnValue\", \"metadata\") VALUES (?, ?, ?, ?, ?, ?, ?)"
+ "RehydrationCoordinator: CAS skipped %{public}s::%{public}s — row modified by an external writer since snapshot"
+ "RehydrationCoordinator: all %ld aged rows already in flight"
+ "RehydrationCoordinator: cannot construct identifier for %{public}s::%{public}s — skipping"
+ "RehydrationCoordinator: evicted %{public}s::%{public}s — owning app no longer recognizes this entity"
+ "RehydrationCoordinator: failed to delete missing entity for %{public}s::%{public}s: %@"
+ "RehydrationCoordinator: failed to write resolved entity for %{public}s::%{public}s: %@"
+ "RehydrationCoordinator: leaving %{public}s::%{public}s untouched — %{public}s"
+ "RehydrationCoordinator: refreshed %{public}s::%{public}s (per-row lastUpdate moved %{public}fs forward)"
+ "RehydrationCoordinator: scheduling rehydration for %{public}ld row(s) (skipped %{public}ld already in flight)"
+ "Removed %{public}ld row(s) from PID-pegged feeds"
+ "SELECT feedId, bundleId, entityId, lastUpdate, lnValue, metadata FROM feedEntries WHERE bootId=?"
+ "UPDATE feedEntries SET lastUpdate = ? WHERE feedId = ?"
+ "UPDATE feedEntries SET lnValue = ?, lastUpdate = ? WHERE feedId = ? AND bundleId = ? AND entityId = ? AND lastUpdate = ?"
+ "UPDATE feedEntries SET metadata = ? WHERE feedId = ? AND bundleId = ? AND entityId = ?"
+ "Unable to decode metadata for %s::%s::%s: %@"
+ "Unable to parse per-row lastUpdate for %s::%s::%s"
+ "Unexpected row format in feedEntries table"
+ "_TtC27AppIntentsLiveEntityService22RehydrationCoordinator"
+ "auditToken"
+ "currentProcess"
+ "handleForIdentifier:error:"
+ "hydrateEntitiesKeyed: dropping query result for %{public}s::%{public}s — value is %{public}s (expected LNEntity with localIdentifier)"
+ "hydrateEntitiesKeyed: marking %{public}ld identifier(s) for %{public}s::%{public}s as unavailable: %{public}s"
+ "hydrateEntitiesKeyed: query for %{public}s::%{public}s returned an unsolicited entity for key %{sensitive,mask.hash}s"
+ "inFlight"
+ "initWithInt:"
+ "invalidateDatabaseFilesForTesting()"
+ "livePIDForTesting()"
+ "pid"
+ "runIdentifierQuery(bundleIdentifier:entityType:identifiers:sharedConnection:)"
+ "setLastUpdateForTesting(feedId:newValue:)"
+ "setMetadataForTesting(bundleId:entityId:feedId:metadata:)"
+ "stableIdentifier"
- "    CREATE TABLE \"feedMetadata\" (\n        \"feedId\" TEXT PRIMARY KEY NOT NULL, \n        \"lastUpdate\" TEXT NOT NULL\n    );\n    CREATE TABLE \"feedEntries\" (\n        \"feedId\" TEXT NOT NULL, \n        \"bootId\" TEXT NOT NULL, \n        \"bundleId\" TEXT NOT NULL,\n        \"entityId\" TEXT NOT NULL,\n        \"lnValue\" BLOB NOT NULL,\n        PRIMARY KEY (\"feedId\", \"bundleId\", \"entityID\"),\n        FOREIGN KEY (\"feedId\") REFERENCES \"feedMetadata\"(\"feedId\")\n    );\n    CREATE INDEX \"idx_feedEntries_bootId\" ON \"feedEntries\"(\"bootId\");\n    CREATE INDEX \"idx_feedEntries_bundleId\" ON \"feedEntries\"(\"bundleId\");\n    CREATE INDEX \"idx_feedEntries_feedId\" ON \"feedEntries\"(\"feedId\");"
- "%s: fetching feeds for bootId %s"
- "%s::state() completed for %s"
- "BulkEntityQueryExecutor"
- "INSERT INTO feedEntries (\"feedId\", \"bootId\", \"bundleId\", \"entityId\", \"lnValue\") VALUES ( ?, ?, ?, ?, ? )"
- "REPLACE INTO feedEntries (\"feedId\", \"bootId\", \"bundleId\", \"entityId\", \"lnValue\") VALUES (?, ?, ?, ?, ?)"
- "SELECT feedId, bundleId, lnValue FROM feedEntries WHERE bootId=?"
- "Unexpected row format in feeds table"
```
