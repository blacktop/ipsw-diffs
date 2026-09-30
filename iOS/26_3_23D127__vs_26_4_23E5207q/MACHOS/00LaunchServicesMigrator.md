## 00LaunchServicesMigrator

> `/System/Library/DataClassMigrators/00LaunchServicesMigrator.migrator/00LaunchServicesMigrator`

```diff

-1444.3.6.0.0
-  __TEXT.__text: 0x74c
+1444.4.16.0.0
+  __TEXT.__text: 0x78c
   __TEXT.__auth_stubs: 0x100
   __TEXT.__objc_stubs: 0x2e0
   __TEXT.__objc_methlist: 0x68

   - /System/Library/PrivateFrameworks/DataMigration.framework/DataMigration
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2E440EBC-CADF-3BAF-9CDB-4892E53CD6B6
+  UUID: B399AF42-B518-3B7A-A8A9-B4DD8E0A87FA
   Functions: 9
   Symbols:   32
   CStrings:  49
Symbols:
+ _objc_retainAutoreleasedReturnValue
- _objc_claimAutoreleasedReturnValue
Functions:
~ sub_ac4 : 528 -> 548
~ sub_cd4 -> sub_ce8 : 812 -> 844
~ sub_1000 -> sub_1034 : 244 -> 256

```
