## DMCEnrollmentLibrary

> `/System/Library/PrivateFrameworks/DMCEnrollmentLibrary.framework/DMCEnrollmentLibrary`

```diff

-55.80.2.0.0
-  __TEXT.__text: 0x2a288
-  __TEXT.__auth_stubs: 0x590
-  __TEXT.__objc_methlist: 0x1abc
+55.80.4.0.0
+  __TEXT.__text: 0x2a340
+  __TEXT.__auth_stubs: 0x5a0
+  __TEXT.__objc_methlist: 0x1acc
   __TEXT.__const: 0xf0
-  __TEXT.__oslogstring: 0x3ee4
+  __TEXT.__oslogstring: 0x3f11
   __TEXT.__cstring: 0x24b8
   __TEXT.__gcc_except_tab: 0x9ec
   __TEXT.__dlopen_cstrs: 0xae
-  __TEXT.__unwind_info: 0x8e0
+  __TEXT.__unwind_info: 0x8e8
   __TEXT.__objc_classname: 0x21b
-  __TEXT.__objc_methname: 0x8707
+  __TEXT.__objc_methname: 0x872a
   __TEXT.__objc_methtype: 0x9ae
-  __TEXT.__objc_stubs: 0x6380
+  __TEXT.__objc_stubs: 0x63a0
   __DATA_CONST.__got: 0x498
   __DATA_CONST.__const: 0x1320
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1b28
+  __DATA_CONST.__objc_selrefs: 0x1b30
   __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_arraydata: 0x480
-  __AUTH_CONST.__auth_got: 0x2d8
+  __AUTH_CONST.__auth_got: 0x2e0
   __AUTH_CONST.__const: 0x120
   __AUTH_CONST.__cfstring: 0x17c0
   __AUTH_CONST.__objc_const: 0x1dc0
   __AUTH_CONST.__objc_intobj: 0x9c0
-  __AUTH_CONST.__objc_arrayobj: 0x438
+  __AUTH_CONST.__objc_arrayobj: 0x450
   __AUTH_CONST.__objc_dictobj: 0x28
   __DATA.__objc_ivar: 0x170
   __DATA.__data: 0x1e0

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D731E69B-6831-3513-B3EE-4C5EA5967625
-  Functions: 783
-  Symbols:   3036
-  CStrings:  1940
+  UUID: D49C5EE9-7B31-332B-8EF3-E6307848F642
+  Functions: 784
+  Symbols:   3040
+  CStrings:  1942
 
Symbols:
+ -[DMCMigrationFlowController(Sequence) _migration_cleanupCloudConfigSteps]
+ _DMCIsSetupBuddyRunning
+ _objc_msgSend$_migration_cleanupCloudConfigSteps
Functions:
~ -[DMCMigrationFlowController _preflightMigration] : 808 -> 892
+ -[DMCMigrationFlowController(Sequence) _migration_enrollmentSteps]
~ +[DMCMigrationHelper launchMigrationApplicationWithError:] : 440 -> 528
CStrings:
+ "DMCMigrationHelper: Buddy is running already"
+ "_migration_cleanupCloudConfigSteps"

```
