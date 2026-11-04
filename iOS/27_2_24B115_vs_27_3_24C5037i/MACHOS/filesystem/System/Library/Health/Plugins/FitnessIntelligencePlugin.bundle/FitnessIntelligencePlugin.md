## FitnessIntelligencePlugin

> `/System/Library/Health/Plugins/FitnessIntelligencePlugin.bundle/FitnessIntelligencePlugin`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`

```diff

-2027.1.35.0.0
-  __TEXT.__text: 0x811ac
-  __TEXT.__auth_stubs: 0x1fa0
-  __TEXT.__objc_stubs: 0x780
-  __TEXT.__objc_methlist: 0x119c
-  __TEXT.__const: 0x1648
-  __TEXT.__cstring: 0x1c6f
-  __TEXT.__constg_swiftt: 0xbf8
-  __TEXT.__swift5_typeref: 0x1354
+2027.2.12.0.0
+  __TEXT.__text: 0x95934
+  __TEXT.__auth_stubs: 0x22d0
+  __TEXT.__objc_stubs: 0x7a0
+  __TEXT.__objc_methlist: 0x1374
+  __TEXT.__cstring: 0x1fa4
+  __TEXT.__swift5_typeref: 0x15d0
+  __TEXT.__swift5_fieldmd: 0xa5c
+  __TEXT.__const: 0x1948
+  __TEXT.__constg_swiftt: 0xce0
   __TEXT.__swift5_builtin: 0x50
-  __TEXT.__swift5_reflstr: 0x7bf
-  __TEXT.__swift5_fieldmd: 0x8d8
-  __TEXT.__swift5_capture: 0x1210
-  __TEXT.__objc_methtype: 0xb6b
-  __TEXT.__oslogstring: 0x171f
-  __TEXT.__swift5_assocty: 0x1e0
-  __TEXT.__swift5_proto: 0xbc
-  __TEXT.__swift5_types: 0x9c
-  __TEXT.__objc_classname: 0x936
-  __TEXT.__objc_methname: 0x16c9
+  __TEXT.__swift5_reflstr: 0x934
+  __TEXT.__swift5_assocty: 0x260
   __TEXT.__swift5_protos: 0x18
+  __TEXT.__swift5_proto: 0xe0
+  __TEXT.__swift5_types: 0xac
+  __TEXT.__swift5_capture: 0x135c
+  __TEXT.__objc_methtype: 0xbab
+  __TEXT.__oslogstring: 0x185d
+  __TEXT.__objc_classname: 0xa13
+  __TEXT.__objc_methname: 0x1699
   __TEXT.__swift_as_entry: 0xc
   __TEXT.__swift_as_ret: 0xc
   __TEXT.__swift_as_cont: 0x18
-  __TEXT.__unwind_info: 0x1798
-  __TEXT.__eh_frame: 0x1e78
-  __DATA_CONST.__const: 0x48e8
-  __DATA_CONST.__objc_classlist: 0xc0
+  __TEXT.__unwind_info: 0x1a58
+  __TEXT.__eh_frame: 0x2268
+  __DATA_CONST.__const: 0x4f18
+  __DATA_CONST.__objc_classlist: 0xd8
   __DATA_CONST.__objc_protolist: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x80
-  __DATA_CONST.__auth_got: 0xfd8
-  __DATA_CONST.__got: 0x580
-  __DATA_CONST.__auth_ptr: 0x470
-  __DATA.__objc_const: 0x15f8
-  __DATA.__objc_selrefs: 0x4d0
-  __DATA.__objc_data: 0x12c8
-  __DATA.__data: 0x1748
-  __DATA.__common: 0x98
+  __DATA_CONST.__auth_got: 0x1170
+  __DATA_CONST.__got: 0x6c8
+  __DATA_CONST.__auth_ptr: 0x508
+  __DATA.__objc_const: 0x17d0
+  __DATA.__objc_selrefs: 0x4d8
+  __DATA.__objc_data: 0x1528
+  __DATA.__data: 0x1a60
+  __DATA.__common: 0xa0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/HealthKit.framework/HealthKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1875
-  Symbols:   236
-  CStrings:  542
+  Functions: 2088
+  Symbols:   241
+  CStrings:  564
 
Symbols:
+ _OBJC_CLASS_$__TtC25FitnessIntelligencePlugin43StrengthWorkoutExercisePropertyRecordEntity
+ _OBJC_METACLASS_$__TtC25FitnessIntelligencePlugin43StrengthWorkoutExercisePropertyRecordEntity
+ _swift_getAtKeyPath
+ _swift_getKeyPath
+ _swift_release_x12
CStrings:
+ ", 'unixepoch') AS INTEGER);"
+ "ALTER TABLE FitnessIntelligencePlugin_strengthWorkoutExercisePropertyRecords ADD COLUMN year INTEGER;"
+ "CREATE INDEX IF NOT EXISTS FitnessIntelligencePlugin_strengthWorkoutExercisePropertyRecords_index ON FitnessIntelligencePlugin_strengthWorkoutExercisePropertyRecords(startCacheIndex, endCacheIndex, propertyKind);"
+ "CREATE TABLE IF NOT EXISTS FitnessIntelligencePlugin_strengthWorkoutExercisePropertyRecords ("
+ "Compounded predicate: %s"
+ "Failed to decode InferenceRecord from row: %ld, skipping"
+ "Failed to initialize StrengthWorkoutExercisePropertyRecordEntity from row: %@"
+ "Failed to initialize StrengthWorkoutExercisePropertyRecordEntity from row: no propertyData"
+ "FitnessIntelligencePlugin.StrengthWorkoutExercisePropertyRecordJournalEntry"
+ "FitnessIntelligencePlugin/StrengthWorkoutExercisePropertyRecordJournalEntry.swift"
+ "FitnessIntelligencePlugin_strengthWorkoutExercisePropertyRecords"
+ "Starting migration to v16"
+ "Starting migration to v17"
+ "Starting migration to v18"
+ "StrengthWorkoutExerciseEntityWrapper"
+ "StrengthWorkoutExercisePropertyRecordEntity"
+ "_TtC25FitnessIntelligencePlugin43StrengthWorkoutExercisePropertyRecordEntity"
+ "_TtC25FitnessIntelligencePlugin49StrengthWorkoutExercisePropertyRecordJournalEntry"
+ "equipments"
+ "exercise"
+ "muscleGroups"
+ "phase"
+ "side"
- "Failed to decode InferenceRecord from row: %ld"
```
