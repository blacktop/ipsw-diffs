## AccountsObsolescence

> `/System/Library/DataClassMigrators/AccountsObsolescence.migrator/AccountsObsolescence`

```diff

-956.0.0.0.0
+962.2.0.0.0
   __TEXT.__text: 0x118
   __TEXT.__auth_stubs: 0x90
   __TEXT.__objc_stubs: 0x40

   __DATA_CONST.__cfstring: 0x20
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_classrefs: 0x8
   __DATA.__objc_const: 0x90
   __DATA.__objc_selrefs: 0x30
-  __DATA.__objc_classrefs: 0x8
   __DATA.__objc_data: 0x50
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/DataMigration.framework/DataMigration
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8DD80909-111D-33B3-BEE5-6ADB15C49CCC
+  UUID: 2E09B679-6E09-3840-B5BD-CF62A693DD4C
   Functions: 6
   Symbols:   20
   CStrings:  14

```
