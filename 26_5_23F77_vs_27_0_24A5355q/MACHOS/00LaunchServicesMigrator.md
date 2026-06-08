## 00LaunchServicesMigrator

> `/System/Library/DataClassMigrators/00LaunchServicesMigrator.migrator/00LaunchServicesMigrator`

```diff

-1444.5.2.0.0
-  __TEXT.__text: 0x78c
+1498.0.0.0.0
+  __TEXT.__text: 0x724
   __TEXT.__auth_stubs: 0x100
   __TEXT.__objc_stubs: 0x2e0
   __TEXT.__objc_methlist: 0x68

   __TEXT.__objc_classname: 0x13
   __TEXT.__objc_methtype: 0x18
   __TEXT.__unwind_info: 0x88
-  __DATA_CONST.__auth_got: 0x88
-  __DATA_CONST.__got: 0x28
   __DATA_CONST.__cfstring: 0x80
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
+  __DATA_CONST.__auth_got: 0x88
+  __DATA_CONST.__got: 0x28
   __DATA.__objc_const: 0x90
   __DATA.__objc_selrefs: 0xe8
   __DATA.__objc_data: 0x50

   - /System/Library/PrivateFrameworks/DataMigration.framework/DataMigration
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1A1CDF1E-986F-3A51-B903-C06CDD8F9709
+  UUID: 21DE9582-2CC0-3724-919F-B6CDFDA11D1E
   Functions: 9
   Symbols:   32
   CStrings:  49
Symbols:
+ _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleasedReturnValue
Functions:
~ sub_ac4 : 548 -> 532
~ sub_ce8 -> sub_cd8 : 844 -> 768
~ sub_1034 -> sub_fd8 : 256 -> 244

```
