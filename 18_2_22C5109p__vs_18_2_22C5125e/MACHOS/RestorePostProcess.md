## RestorePostProcess

> `/System/Library/DataClassMigrators/RestorePostProcess.migrator/RestorePostProcess`

```diff

-2349.60.69.0.1
-  __TEXT.__text: 0x144b8
+2349.60.109.0.0
+  __TEXT.__text: 0x1465c
   __TEXT.__auth_stubs: 0xcd0
-  __TEXT.__objc_stubs: 0x2480
-  __TEXT.__objc_methlist: 0xa48
+  __TEXT.__objc_stubs: 0x24e0
+  __TEXT.__objc_methlist: 0xa68
   __TEXT.__const: 0x420
-  __TEXT.__cstring: 0x3935
-  __TEXT.__objc_methname: 0x2cb9
+  __TEXT.__cstring: 0x3985
+  __TEXT.__objc_methname: 0x2d45
   __TEXT.__objc_classname: 0xf2
-  __TEXT.__objc_methtype: 0x597
-  __TEXT.__oslogstring: 0x25d0
-  __TEXT.__gcc_except_tab: 0x384
+  __TEXT.__objc_methtype: 0x5b3
+  __TEXT.__oslogstring: 0x261d
+  __TEXT.__gcc_except_tab: 0x38c
   __TEXT.__constg_swiftt: 0x18c
   __TEXT.__swift5_typeref: 0xe4
   __TEXT.__swift5_reflstr: 0x8c

   __TEXT.__swift5_proto: 0x28
   __TEXT.__swift5_types: 0x1c
   __TEXT.__swift5_assocty: 0x18
-  __TEXT.__unwind_info: 0x470
+  __TEXT.__unwind_info: 0x478
   __TEXT.__eh_frame: 0x158
   __DATA_CONST.__auth_got: 0x678
-  __DATA_CONST.__got: 0x2b0
+  __DATA_CONST.__got: 0x2b8
   __DATA_CONST.__auth_ptr: 0x128
   __DATA_CONST.__const: 0x828
   __DATA_CONST.__cfstring: 0xe40

   __DATA_CONST.__objc_intobj: 0x48
   __DATA_CONST.__objc_arraydata: 0x50
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0x1618
-  __DATA.__objc_selrefs: 0xb88
+  __DATA.__objc_const: 0x1628
+  __DATA.__objc_selrefs: 0xbb0
   __DATA.__objc_ivar: 0x6c
   __DATA.__objc_data: 0x4c0
   __DATA.__data: 0x360

   - /System/Library/PrivateFrameworks/AuthKit.framework/AuthKit
   - /System/Library/PrivateFrameworks/DataMigration.framework/DataMigration
   - /System/Library/PrivateFrameworks/InstallCoordination.framework/InstallCoordination
+  - /System/Library/PrivateFrameworks/MDMClientLibrary.framework/MDMClientLibrary
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/MobileBackup.framework/MobileBackup
   - /System/Library/PrivateFrameworks/MobileDeviceLink.framework/MobileDeviceLink

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 364
-  Symbols:   296
-  CStrings:  1118
+  Functions: 367
+  Symbols:   297
+  CStrings:  1127
 
Symbols:
+ _OBJC_CLASS_$_MDMClient
CStrings:
+ "@20@0:8B16"
+ "Not updating bundleID to personaID mapping because it was already set by MDM"
+ "_addContainer:toArray:visited:"
+ "_visitContainerDependenciesAndFilterDuplicates:"
+ "hasSetPersonaMappingForRestore"
+ "sharedClient"
+ "uniqueContainers"
+ "v40@0:8@16@24@32"

```
