## MCCleanup

> `/System/Library/DataClassMigrators/MCCleanup.migrator/MCCleanup`

```diff

-2343.0.0.0.0
-  __TEXT.__text: 0x118
-  __TEXT.__auth_stubs: 0x30
-  __TEXT.__objc_stubs: 0xa0
-  __TEXT.__objc_methlist: 0x38
-  __TEXT.__cstring: 0x103
+2347.0.0.0.0
+  __TEXT.__text: 0x28c
+  __TEXT.__auth_stubs: 0x60
+  __TEXT.__objc_stubs: 0xc0
+  __TEXT.__objc_methlist: 0x44
+  __TEXT.__const: 0x10
+  __TEXT.__gcc_except_tab: 0x10
+  __TEXT.__cstring: 0x18d
   __TEXT.__objc_classname: 0x12
-  __TEXT.__objc_methname: 0xc6
-  __TEXT.__objc_methtype: 0x18
-  __TEXT.__unwind_info: 0x60
-  __DATA_CONST.__auth_got: 0x20
-  __DATA_CONST.__got: 0x8
-  __DATA_CONST.__cfstring: 0x100
+  __TEXT.__objc_methname: 0xe4
+  __TEXT.__objc_methtype: 0x23
+  __TEXT.__unwind_info: 0x80
+  __DATA_CONST.__auth_got: 0x40
+  __DATA_CONST.__got: 0x10
+  __DATA_CONST.__const: 0x28
+  __DATA_CONST.__cfstring: 0x140
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0x90
-  __DATA.__objc_selrefs: 0x48
+  __DATA.__objc_selrefs: 0x50
   __DATA.__objc_data: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 4
-  Symbols:   13
-  CStrings:  21
+  Functions: 6
+  Symbols:   18
+  CStrings:  26
 
Symbols:
+ __Block_object_dispose
+ __NSConcreteStackBlock
+ __Unwind_Resume
+ ___objc_personality_v0
+ _objc_release_x20
+ _sleep
- _objc_release_x21
CStrings:
+ "B20@0:8i16"
+ "MCCleanupMigrator: migrateCleanupMigratorWithContext failed. Error: %!@(MISSING)"
+ "MCCleanupMigrator: migration failed, context: %!@(MISSING)"
+ "_triggerMigrationWithContext:"
+ "v16@?0@\"NSError\"8"

```
