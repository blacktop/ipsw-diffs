## ContainerMigrator

> `/System/Library/DataClassMigrators/ContainerMigrator.migrator/ContainerMigrator`

```diff

-725.120.2.0.0
-  __TEXT.__text: 0x1b4
-  __TEXT.__auth_stubs: 0x70
+826.0.0.0.1
+  __TEXT.__text: 0x138
+  __TEXT.__auth_stubs: 0x10
   __TEXT.__objc_methlist: 0x38
-  __TEXT.__const: 0x60
+  __TEXT.__const: 0x5c
   __TEXT.__cstring: 0x19
-  __TEXT.__oslogstring: 0x71
   __TEXT.__objc_classname: 0x19
   __TEXT.__objc_methname: 0x43
   __TEXT.__objc_methtype: 0x18
-  __TEXT.__unwind_info: 0x60
-  __DATA_CONST.__auth_got: 0x38
-  __DATA_CONST.__got: 0x8
+  __TEXT.__unwind_info: 0x58
   __DATA_CONST.__cfstring: 0x20
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__auth_got: 0x8
+  __DATA_CONST.__got: 0x8
   __DATA.__objc_const: 0x90
   __DATA.__objc_selrefs: 0x20
   __DATA.__objc_data: 0x50

   - /System/Library/PrivateFrameworks/DataMigration.framework/DataMigration
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6C77057D-D89B-3A31-A3EC-A689379F2886
+  UUID: 6B38B37E-85D9-3515-A042-08CD0629B119
   Functions: 4
-  Symbols:   14
-  CStrings:  11
+  Symbols:   8
+  CStrings:  10
 
Symbols:
- __os_log_fault_impl
- _container_log_handle_for_category
- _container_perform_data_migration
- _objc_release_x20
- _objc_retainAutoreleasedReturnValue
- _os_log_type_enabled
Functions:
~ sub_980 -> sub_930 : 76 -> 80
~ sub_a18 -> sub_9cc : 204 -> 80
~ sub_ae4 -> sub_a1c : 80 -> 76
CStrings:
- "Migration failed with error %llu. Please include a sysdiagnose in a bug report for MobileContainerManager | all."

```
