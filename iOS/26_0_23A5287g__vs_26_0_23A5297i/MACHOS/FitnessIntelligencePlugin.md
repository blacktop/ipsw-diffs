## FitnessIntelligencePlugin

> `/System/Library/Health/Plugins/FitnessIntelligencePlugin.bundle/FitnessIntelligencePlugin`

```diff

-104.0.1.0.0
-  __TEXT.__text: 0x64d50
-  __TEXT.__auth_stubs: 0x17e0
-  __TEXT.__objc_methlist: 0xfdc
-  __TEXT.__cstring: 0x225d
-  __TEXT.__const: 0xfd0
-  __TEXT.__constg_swiftt: 0xa88
-  __TEXT.__swift5_typeref: 0xfe4
+109.0.0.0.0
+  __TEXT.__text: 0x6fc4c
+  __TEXT.__auth_stubs: 0x1a60
+  __TEXT.__objc_methlist: 0x1054
+  __TEXT.__cstring: 0x265d
+  __TEXT.__const: 0x1100
+  __TEXT.__constg_swiftt: 0xb44
+  __TEXT.__swift5_typeref: 0x11a0
   __TEXT.__swift5_builtin: 0x50
-  __TEXT.__swift5_reflstr: 0x6ad
-  __TEXT.__swift5_fieldmd: 0x740
+  __TEXT.__swift5_reflstr: 0x6ed
+  __TEXT.__swift5_fieldmd: 0x7c8
   __TEXT.__swift5_assocty: 0x1f8
-  __TEXT.__swift5_proto: 0xb8
-  __TEXT.__swift5_types: 0x8c
+  __TEXT.__swift5_proto: 0xc8
+  __TEXT.__swift5_types: 0x98
   __TEXT.__objc_classname: 0xcc
-  __TEXT.__objc_methname: 0x1172
+  __TEXT.__objc_methname: 0x119d
   __TEXT.__objc_methtype: 0x65c
-  __TEXT.__swift5_capture: 0xfc4
-  __TEXT.__oslogstring: 0x10d8
-  __TEXT.__swift5_protos: 0x14
-  __TEXT.__unwind_info: 0xf28
-  __TEXT.__eh_frame: 0x1078
-  __DATA_CONST.__auth_got: 0xbf0
-  __DATA_CONST.__got: 0x440
-  __DATA_CONST.__auth_ptr: 0x3e8
-  __DATA_CONST.__const: 0x4038
-  __DATA_CONST.__objc_classlist: 0xa8
-  __DATA_CONST.__objc_protolist: 0xd8
+  __TEXT.__swift5_capture: 0x106c
+  __TEXT.__oslogstring: 0x1128
+  __TEXT.__swift5_protos: 0x18
+  __TEXT.__unwind_info: 0x1030
+  __TEXT.__eh_frame: 0x13b0
+  __DATA_CONST.__auth_got: 0xd30
+  __DATA_CONST.__got: 0x4b8
+  __DATA_CONST.__auth_ptr: 0x458
+  __DATA_CONST.__const: 0x4398
+  __DATA_CONST.__objc_classlist: 0xb0
+  __DATA_CONST.__objc_protolist: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x78
-  __DATA.__objc_const: 0x1378
-  __DATA.__objc_selrefs: 0x488
-  __DATA.__objc_data: 0x1048
-  __DATA.__data: 0x1470
-  __DATA.__common: 0x80
-  __DATA.__bss: 0x1710
+  __DATA_CONST.__objc_protorefs: 0x80
+  __DATA.__objc_const: 0x1480
+  __DATA.__objc_selrefs: 0x490
+  __DATA.__objc_data: 0x1108
+  __DATA.__data: 0x1640
+  __DATA.__common: 0xb0
+  __DATA.__bss: 0x1910
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/HealthKit.framework/HealthKit
   - /System/Library/PrivateFrameworks/FitnessIntelligence.framework/FitnessIntelligence
   - /System/Library/PrivateFrameworks/HealthDaemon.framework/HealthDaemon
   - /System/Library/PrivateFrameworks/HealthDaemonFoundation.framework/HealthDaemonFoundation
+  - /System/Library/PrivateFrameworks/SeymourCore.framework/SeymourCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib

   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
-  - /usr/lib/swift/libswiftCoreMIDI.dylib
-  - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 2FE673AF-7853-354A-946E-9EDF60C8D7CC
-  Functions: 1571
-  Symbols:   194
-  CStrings:  494
+  UUID: 8502F9DA-8080-374E-85EA-E99864EC1F9F
+  Functions: 1674
+  Symbols:   203
+  CStrings:  506
 
Symbols:
+ _HDSQLiteColumnAsDouble
+ _OBJC_CLASS_$__TtC25FitnessIntelligencePlugin16SanityTaskServer
+ _OBJC_METACLASS_$__TtC25FitnessIntelligencePlugin16SanityTaskServer
+ __HKCacheIndexFromDate
+ __swiftEmptyDictionarySingleton
+ _swift_cvw_initStructMetadataWithLayoutString
+ _swift_cvw_initWithTake
+ _swift_getAssociatedConformanceWitness
+ _swift_getAssociatedTypeWitness
+ _swift_getEnumTagSinglePayloadGeneric
+ _swift_storeEnumTagSinglePayloadGeneric
+ _swift_unexpectedError
- __swift_FORCE_LOAD_$_swiftAVFoundation
- __swift_FORCE_LOAD_$_swiftCoreMIDI
- __swift_FORCE_LOAD_$_swiftCoreMedia
CStrings:
+ "  SELECT\n    DISTINCT cache_index\n  FROM\n    activity_caches\n  WHERE\n    cache_index >= 410227200"
+ "  SELECT\n    DISTINCT objects.uuid AS uuid,\n    samples.start_date AS start_date,\n    metadata_values.string_value\n  FROM\n    objects\n  JOIN\n    workout_activities\n  ON\n    objects.data_id = workout_activities.owner_id\n  JOIN\n    samples\n  ON\n    objects.data_id = samples.data_id\n  LEFT JOIN \n      metadata_values\n  ON \n      objects.data_id = metadata_values.object_id\n      AND (metadata_values.key_id = (SELECT ROWID FROM metadata_keys WHERE key = 'HKTimeZone') OR metadata_values.key_id IS NULL)  \n  WHERE\n    samples.data_type = 79\n    AND workout_activities.is_primary_activity = TRUE\n    AND samples.start_date >= 410227200"
+ "Checksum mismatch: %s db = %s ; snapshot = %s"
+ "Duplicate values for key: '"
+ "SELECT DISTINCT objects.uuid AS uuid, activity_type, location_type, swimming_location_type, samples.start_date AS start_date, samples.end_date AS end_date, (SELECT metadata_values.string_value FROM metadata_values JOIN metadata_keys ON metadata_keys.ROWID=metadata_values.key_id WHERE metadata_keys.key='_HKPrivateSeymourCatalogWorkoutIdentifier' AND metadata_values.object_id=objects.data_id)  AS seymour_catalog_identifier FROM objects JOIN workout_activities ON objects.data_id=workout_activities.owner_id JOIN samples ON objects.data_id=samples.data_id WHERE samples.start_date > ? AND samples.end_date < ? AND data_type=79 AND is_primary_activity=true;"
+ "Swift/Dictionary.swift"
+ "Swift/NativeDictionary.swift"
+ "[%s] Querying checksums"
+ "_TtC25FitnessIntelligencePlugin16SanityTaskServer"
+ "_TtP19FitnessIntelligence25SanityTaskServerInterface_"
+ "com.apple.FitnesIntelligence.SanityTaskServer.Synchronization"
+ "queryMismatchingCheckpointsWithCompletion:"
+ "strategy"
- "SELECT DISTINCT objects.uuid AS uuid, activity_type, location_type, swimming_location_type, samples.start_date AS start_date, samples.end_date AS end_date, (SELECT metadata_values.string_value FROM metadata_values WHERE metadata_keys.key='_HKPrivateSeymourCatalogWorkoutIdentifier') AS seymour_catalog_identifier FROM objects JOIN workout_activities ON objects.data_id=workout_activities.owner_id JOIN metadata_values ON objects.data_id=metadata_values.object_id JOIN metadata_keys ON metadata_keys.ROWID=metadata_values.key_id JOIN samples ON objects.data_id=samples.data_id WHERE samples.start_date > ? AND samples.end_date < ? AND data_type=79 AND is_primary_activity=true;"

```
