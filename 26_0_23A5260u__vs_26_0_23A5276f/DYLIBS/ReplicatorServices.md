## ReplicatorServices

> `/System/Library/PrivateFrameworks/ReplicatorServices.framework/ReplicatorServices`

```diff

-108.0.0.0.0
-  __TEXT.__text: 0xfd03c
-  __TEXT.__auth_stubs: 0x1ef0
+113.0.0.0.0
+  __TEXT.__text: 0xfea20
+  __TEXT.__auth_stubs: 0x1f00
   __TEXT.__objc_methlist: 0x900
-  __TEXT.__const: 0xae54
-  __TEXT.__cstring: 0x3783
-  __TEXT.__swift5_typeref: 0x3261
-  __TEXT.__swift5_reflstr: 0x18c3
+  __TEXT.__const: 0xaee4
+  __TEXT.__cstring: 0x3793
+  __TEXT.__swift5_typeref: 0x3277
+  __TEXT.__swift5_reflstr: 0x18d3
   __TEXT.__swift5_assocty: 0x828
-  __TEXT.__constg_swiftt: 0x3358
-  __TEXT.__swift5_fieldmd: 0x27dc
+  __TEXT.__constg_swiftt: 0x337c
+  __TEXT.__swift5_fieldmd: 0x2804
   __TEXT.__swift5_builtin: 0x78
-  __TEXT.__swift5_proto: 0xb1c
-  __TEXT.__swift5_types: 0x37c
-  __TEXT.__oslogstring: 0x3030
+  __TEXT.__swift5_proto: 0xb24
+  __TEXT.__swift5_types: 0x380
+  __TEXT.__oslogstring: 0x3240
   __TEXT.__swift5_capture: 0x954
   __TEXT.__swift5_protos: 0x80
   __TEXT.__swift_as_entry: 0x10
   __TEXT.__swift_as_ret: 0x10
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x39c8
-  __TEXT.__eh_frame: 0x711c
+  __TEXT.__unwind_info: 0x3a10
+  __TEXT.__eh_frame: 0x715c
   __TEXT.__objc_classname: 0xec
   __TEXT.__objc_methname: 0xe4d
   __TEXT.__objc_methtype: 0x2fb
   __TEXT.__objc_stubs: 0x1a0
   __DATA_CONST.__got: 0x4f8
-  __DATA_CONST.__const: 0x218
+  __DATA_CONST.__const: 0x1f8
   __DATA_CONST.__objc_classlist: 0x188
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xc0

   __DATA_CONST.__objc_selrefs: 0x4b0
   __DATA_CONST.__objc_protorefs: 0x80
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0xf80
-  __AUTH_CONST.__const: 0x6dd8
+  __AUTH_CONST.__auth_got: 0xf88
+  __AUTH_CONST.__const: 0x6e68
   __AUTH_CONST.__cfstring: 0x100
   __AUTH_CONST.__objc_const: 0x36f8
   __AUTH.__objc_data: 0x9d0
-  __AUTH.__data: 0x2798
+  __AUTH.__data: 0x27a8
   __DATA.__objc_ivar: 0x18
-  __DATA.__data: 0x21b0
-  __DATA.__bss: 0x10080
+  __DATA.__data: 0x2140
+  __DATA.__bss: 0x10180
   __DATA.__common: 0x78
   __DATA_DIRTY.__objc_data: 0x670
   __DATA_DIRTY.__data: 0x14a8

   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: D7F09CEF-21E2-3E4F-9B39-94BF4193C0E2
-  Functions: 5192
-  Symbols:   2012
-  CStrings:  845
+  UUID: 5AB70EB6-C657-3FA4-B4AF-7DAFF7BB1037
+  Functions: 5201
+  Symbols:   2007
+  CStrings:  851
 
Symbols:
+ _associated conformance 18ReplicatorServices0A6ClientC23InvalidRecordResolutionOSHAASQ
+ _symbolic _____ 18ReplicatorServices0A6ClientC23InvalidRecordResolutionO
+ _symbolic _____Sg 18ReplicatorServices0A8ScheduleO
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swiftDarwin_$_ReplicatorServices
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_ReplicatorServices
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_ReplicatorServices
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_ReplicatorServices
CStrings:
+ "\n    WHERE\n        "
+ "Database sync already scheduled; priority %s"
+ "Local record for destination collection does not exist in replicator but has no valid destinations; deleting local copy of %{public}s"
+ "Local record has expired; deleting local copy of: %{public}s"
+ "Local record is outdated in replicator but we have no eligbile destinations; deleting local copy of %{public}s"
+ "No eligible destinations for record %{public}s"
+ "Record ID is too long: %{public}s (max %llu; requested %ld)"
+ "Record exceeds maximum size: %{public}s (max %llu; requested %ld)"
+ "Relationship %{public}s does not exist for record %{public}s"
+ "Remote zone does not exist for record %{public}s"
+ "Remote zone is incompatible with record %{public}s"
+ "SELECT EXISTS(\n    SELECT\n        1\n    FROM\n        "
+ "Scheduling database sync with priority %s"
+ "lock_scheduledDatabaseSyncSchedule"
+ "queue_internalRecordIDToClientDefinedID"
- "Database sync already scheduled"
- "Local record does not exist in replicator and has no valid destinations; deleting local copy of %{public}s"
- "Record ID is too long: %{public}s"
- "Record exceeds maximum size: %{public}s"
- "ReplicatorServices/ReplicatorClientWithPersistence.swift"
- "Scheduling database sync"
- "Unexpected destination"
- "lock_hasScheduledDatabaseSync"
- "queue_clientDefinedIDToInternalRecordID"

```
