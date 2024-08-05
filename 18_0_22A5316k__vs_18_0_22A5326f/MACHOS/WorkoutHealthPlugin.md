## WorkoutHealthPlugin

> `/System/Library/Health/Plugins/WorkoutHealthPlugin.bundle/WorkoutHealthPlugin`

```diff

-889.0.0.0.0
-  __TEXT.__text: 0x9244
+897.0.0.0.0
+  __TEXT.__text: 0x9490
   __TEXT.__auth_stubs: 0x530
-  __TEXT.__objc_stubs: 0x17a0
-  __TEXT.__objc_methlist: 0x6e8
-  __TEXT.__cstring: 0x211f
+  __TEXT.__objc_stubs: 0x17e0
+  __TEXT.__objc_methlist: 0x700
+  __TEXT.__cstring: 0x2174
   __TEXT.__objc_classname: 0x20e
-  __TEXT.__objc_methname: 0x20dc
+  __TEXT.__objc_methname: 0x2137
   __TEXT.__objc_methtype: 0x97e
   __TEXT.__const: 0x68
-  __TEXT.__oslogstring: 0xd77
+  __TEXT.__oslogstring: 0xe30
   __TEXT.__gcc_except_tab: 0x240
-  __TEXT.__unwind_info: 0x2b8
+  __TEXT.__unwind_info: 0x2c8
   __DATA_CONST.__auth_got: 0x2a8
   __DATA_CONST.__got: 0x190
-  __DATA_CONST.__const: 0xac0
-  __DATA_CONST.__cfstring: 0x880
+  __DATA_CONST.__const: 0xb00
+  __DATA_CONST.__cfstring: 0x8a0
   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x30
-  __DATA_CONST.__objc_arraydata: 0x80
-  __DATA_CONST.__objc_arrayobj: 0x48
+  __DATA_CONST.__objc_arraydata: 0x88
+  __DATA_CONST.__objc_arrayobj: 0x60
   __DATA_CONST.__objc_intobj: 0x78
   __DATA.__objc_const: 0x17e0
-  __DATA.__objc_selrefs: 0x740
+  __DATA.__objc_selrefs: 0x750
   __DATA.__objc_ivar: 0x18
   __DATA.__objc_data: 0x320
   __DATA.__data: 0x420

   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/HealthKit.framework/HealthKit
-  - /System/Library/PrivateFrameworks/FitnessUI.framework/FitnessUI
+  - /System/Library/PrivateFrameworks/Fitness.framework/Fitness
   - /System/Library/PrivateFrameworks/HealthDaemon.framework/HealthDaemon
   - /System/Library/PrivateFrameworks/HealthDaemonFoundation.framework/HealthDaemonFoundation
   - /System/Library/PrivateFrameworks/WorkoutHealthBridge.framework/WorkoutHealthBridge

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 201
+  Functions: 205
   Symbols:   165
-  CStrings:  562
+  CStrings:  567
 
Symbols:
+ _FIIsWorkoutNFCAllDayEnabled
+ _FISetWorkoutNFCAllDayEnabled
- _FIUIIsWorkoutNFCAllDayEnabled
- _FIUISetWorkoutNFCAllDayEnabled
CStrings:
+ "DELETE FROM WorkoutHealthPlugin_workout_configurations WHERE configuration_type = 3;"
+ "[%!@(MISSING)] migration step _deleteRaceWorkoutConfigurationsWithMigrator, toVersion: %!l(MISSING)d, success: %!@(MISSING), error: %!@(MISSING)"
+ "[%!@(MISSING)] migration step _emptyMigrationToSchemaVersion8WithMigrator, toVersion: %!l(MISSING)d"
+ "_deleteRaceWorkoutConfigurationsWithMigrator:"
+ "_emptyMigrationToSchemaVersion8WithMigrator:"

```
