## DAAccount

> `/System/Library/DataClassMigrators/DAAccount.migrator/DAAccount`

```diff

-2691.2.2.0.0
-  __TEXT.__text: 0xe0
+2691.4.5.0.0
+  __TEXT.__text: 0xe4
   __TEXT.__auth_stubs: 0x50
   __TEXT.__objc_methlist: 0x38
   __TEXT.__const: 0x4

   - /System/Library/PrivateFrameworks/DataMigration.framework/DataMigration
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 753DC081-AC7C-3C0A-AAA6-AE01172D516F
+  UUID: BC3D9181-1566-3981-AD69-22CF3F34E24A
   Functions: 4
   Symbols:   30
   CStrings:  15
Symbols:
+ _objc_retainAutoreleasedReturnValue
- _objc_claimAutoreleasedReturnValue
Functions:
~ -[DAAccountMigrator performMigration] : 192 -> 196

```
