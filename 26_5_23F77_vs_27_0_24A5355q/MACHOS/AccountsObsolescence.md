## AccountsObsolescence

> `/System/Library/DataClassMigrators/AccountsObsolescence.migrator/AccountsObsolescence`

```diff

-1036.0.0.0.0
+1116.0.0.0.0
   __TEXT.__text: 0x118
   __TEXT.__auth_stubs: 0x90
   __TEXT.__objc_stubs: 0x40

   __TEXT.__objc_methname: 0x7c
   __TEXT.__objc_methtype: 0x23
   __TEXT.__unwind_info: 0x60
-  __DATA_CONST.__auth_got: 0x50
-  __DATA_CONST.__got: 0x10
   __DATA_CONST.__const: 0x28
   __DATA_CONST.__cfstring: 0x20
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__auth_got: 0x50
+  __DATA_CONST.__got: 0x10
   __DATA.__objc_const: 0x90
   __DATA.__objc_selrefs: 0x30
   __DATA.__objc_data: 0x50

   - /System/Library/PrivateFrameworks/DataMigration.framework/DataMigration
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D6BC4ABC-DCDE-37BA-8A8A-CE8D502380AF
+  UUID: 4000E602-87DA-3C42-9AF5-06146EC173DC
   Functions: 6
   Symbols:   20
   CStrings:  14
Symbols:
+ _objc_retain
+ _objc_retain_x2
- _objc_retain_x19
- _objc_retain_x20

```
