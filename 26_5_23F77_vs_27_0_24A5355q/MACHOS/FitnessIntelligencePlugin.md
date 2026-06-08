## FitnessIntelligencePlugin

> `/System/Library/Health/Plugins/FitnessIntelligencePlugin.bundle/FitnessIntelligencePlugin`

```diff

-2026.5.2.0.0
-  __TEXT.__text: 0x72704
-  __TEXT.__auth_stubs: 0x1b00
+2027.0.59.0.2
+  __TEXT.__text: 0x7d0b4
+  __TEXT.__auth_stubs: 0x1e20
   __TEXT.__objc_stubs: 0x760
-  __TEXT.__objc_methlist: 0x1054
-  __TEXT.__cstring: 0x173d
-  __TEXT.__const: 0x1580
-  __TEXT.__constg_swiftt: 0xb04
-  __TEXT.__swift5_typeref: 0x11f6
+  __TEXT.__objc_methlist: 0x1154
+  __TEXT.__const: 0x15a8
+  __TEXT.__cstring: 0x19cf
+  __TEXT.__constg_swiftt: 0xbb4
+  __TEXT.__swift5_typeref: 0x12ea
   __TEXT.__swift5_builtin: 0x50
-  __TEXT.__swift5_reflstr: 0x6ed
-  __TEXT.__swift5_fieldmd: 0x77c
+  __TEXT.__swift5_reflstr: 0x76f
+  __TEXT.__swift5_fieldmd: 0x7e4
+  __TEXT.__swift5_capture: 0x1078
+  __TEXT.__objc_methtype: 0xb6b
+  __TEXT.__oslogstring: 0x125f
   __TEXT.__swift5_assocty: 0x1e0
   __TEXT.__swift5_proto: 0xbc
-  __TEXT.__swift5_types: 0x94
-  __TEXT.__objc_methtype: 0xbbd
-  __TEXT.__swift5_capture: 0xe48
-  __TEXT.__oslogstring: 0x1298
-  __TEXT.__objc_methname: 0x1609
-  __TEXT.__objc_classname: 0x859
+  __TEXT.__swift5_types: 0x9c
+  __TEXT.__objc_classname: 0x936
+  __TEXT.__objc_methname: 0x16a9
   __TEXT.__swift5_protos: 0x18
-  __TEXT.__unwind_info: 0x1060
-  __TEXT.__eh_frame: 0x16d8
-  __DATA_CONST.__auth_got: 0xd88
-  __DATA_CONST.__got: 0x4d0
-  __DATA_CONST.__auth_ptr: 0x448
-  __DATA_CONST.__const: 0x3c98
-  __DATA_CONST.__objc_classlist: 0xb0
+  __TEXT.__unwind_info: 0x1290
+  __TEXT.__eh_frame: 0x1ad8
+  __DATA_CONST.__const: 0x40a8
+  __DATA_CONST.__objc_classlist: 0xc0
   __DATA_CONST.__objc_protolist: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x80
-  __DATA.__objc_const: 0x1460
-  __DATA.__objc_selrefs: 0x490
-  __DATA.__objc_data: 0x10e8
-  __DATA.__data: 0x1658
-  __DATA.__common: 0x80
+  __DATA_CONST.__auth_got: 0xf18
+  __DATA_CONST.__got: 0x530
+  __DATA_CONST.__auth_ptr: 0x468
+  __DATA.__objc_const: 0x15e0
+  __DATA.__objc_selrefs: 0x4b8
+  __DATA.__objc_data: 0x12a0
+  __DATA.__data: 0x16f8
   __DATA.__bss: 0x1790
+  __DATA.__common: 0x98
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/HealthKit.framework/HealthKit
   - /System/Library/PrivateFrameworks/FitnessIntelligence.framework/FitnessIntelligence
   - /System/Library/PrivateFrameworks/HealthDaemon.framework/HealthDaemon
   - /System/Library/PrivateFrameworks/HealthDaemonFoundation.framework/HealthDaemonFoundation
-  - /System/Library/PrivateFrameworks/SeymourCore.framework/SeymourCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 9A9BD033-6587-3397-8282-2DD4A0E00986
-  Functions: 1608
-  Symbols:   204
-  CStrings:  493
+  UUID: DCF79FFF-51DE-3CE6-9459-A8D6AFC85C61
+  Functions: 1763
+  Symbols:   232
+  CStrings:  503
 
Symbols:
+ __swift_isClassOrObjCExistentialType
+ _swift_checkMetadataState
+ _swift_getTupleTypeMetadata2
+ _swift_isClassType
+ _swift_release_x1
+ _swift_release_x19
+ _swift_release_x20
+ _swift_release_x21
+ _swift_release_x22
+ _swift_release_x23
+ _swift_release_x24
+ _swift_release_x25
+ _swift_release_x26
+ _swift_release_x27
+ _swift_release_x28
+ _swift_release_x8
+ _swift_retain_n
+ _swift_retain_x19
+ _swift_retain_x2
+ _swift_retain_x20
+ _swift_retain_x21
+ _swift_retain_x22
+ _swift_retain_x23
+ _swift_retain_x24
+ _swift_retain_x25
+ _swift_retain_x26
+ _swift_retain_x27
+ _swift_retain_x28
+ _swift_retain_x8
- _swift_unexpectedError
CStrings:
+ "B24@0:8@\"_HKBehavior\"16"
+ "CREATE TABLE IF NOT EXISTS FitnessIntelligencePlugin_fitnessPlusPropertyRecords ("
+ "CREATE TABLE IF NOT EXISTS FitnessIntelligencePlugin_inferenceEntries ("
+ "CREATE TABLE IF NOT EXISTS FitnessIntelligencePlugin_propertyRecordCheckpoints ("
+ "CREATE TABLE IF NOT EXISTS FitnessIntelligencePlugin_ringsPropertyRecords ("
+ "CREATE TABLE IF NOT EXISTS FitnessIntelligencePlugin_workoutPropertyRecords ("
+ "DELETE FROM FitnessIntelligencePlugin_propertyRecordCheckpoints WHERE endCacheIndex >= ?"
+ "Executing %s Properties Query: %s"
+ "Failed to decode InferenceRecord from row: %ld, ignoring."
+ "FitnessIntelligencePlugin.LegacyInferenceRecordContainerJournalEntry"
+ "FitnessIntelligencePlugin.LegacyInferenceRecordContainerWrapper"
+ "Saved %ld records for %s %s"
+ "Starting migration to v10"
+ "Unknown type to execute for, skipping."
+ "_TtC25FitnessIntelligencePlugin42LegacyInferenceRecordContainerJournalEntry"
+ "_TtCC25FitnessIntelligencePlugin30InferenceRecordContainerEntityP33_E9B91BEFD4C6875DD06DB40FDD81357037LegacyInferenceRecordContainerWrapper"
+ "handlePostInstall:"
+ "key value "
+ "legacyListRecordsWithAdapter:interval:completion:"
+ "legacyRetrieveWith:completion:"
+ "legacySaveInference:completion:"
+ "legacySetFeedbackId:for:completion:"
+ "shouldLoadPluginForBehavior:"
+ "v32@0:8@\"HDWorkoutManager\"16@\"HDWorkoutSessionSnapshot\"24"
+ "workoutManager:didChangeStateForCurrentSession:"
+ "workoutManager:didUpdateCurrentSession:"
- "B24@0:8@\"<HDHealthDaemon>\"16"
- "CREATE TABLE IF NOT EXISTS "
- "Executing FitnessPlus Properties Query: %s"
- "Executing Rings Properties Query"
- "Executing Workout Properties Query"
- "Saved %ld records for %s F+ properties"
- "Saved %ld records for %s rings properties"
- "Saved %ld records for %s workout properties"
- "Swift/Dictionary.swift"
- "shouldLoadPluginForDaemon:"
- "v40@0:8@\"HDWorkoutManager\"16@\"HDWorkoutSessionServer\"24@\"<HDWorkoutDataAccumulator>\"32"
- "v40@0:8@\"HDWorkoutManager\"16@\"HDWorkoutSessionServer\"24q32"
- "v40@0:8@16@24@32"
- "v40@0:8@16@24q32"
- "workoutManager:currentWorkout:didChangeToState:"
- "workoutManager:currentWorkout:didUpdateDataAccumulator:"

```
