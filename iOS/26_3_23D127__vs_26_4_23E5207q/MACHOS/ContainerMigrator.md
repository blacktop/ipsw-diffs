## ContainerMigrator

> `/System/Library/DataClassMigrators/ContainerMigrator.migrator/ContainerMigrator`

```diff

-725.80.5.0.0
-  __TEXT.__text: 0x1b0
+725.100.34.0.0
+  __TEXT.__text: 0x1b4
   __TEXT.__auth_stubs: 0x70
   __TEXT.__objc_methlist: 0x38
-  __TEXT.__const: 0x58
+  __TEXT.__const: 0x60
   __TEXT.__cstring: 0x19
   __TEXT.__oslogstring: 0x71
   __TEXT.__objc_classname: 0x19

   - /System/Library/PrivateFrameworks/DataMigration.framework/DataMigration
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 13D2B715-F337-38A2-B624-ADC6C7469899
+  UUID: 865114AE-8C7F-39DE-9213-D9D6DC6F77AC
   Functions: 4
   Symbols:   14
   CStrings:  11
Symbols:
+ _objc_retainAutoreleasedReturnValue
- _objc_claimAutoreleasedReturnValue
Functions:
~ sub_a18 : 200 -> 204

```
