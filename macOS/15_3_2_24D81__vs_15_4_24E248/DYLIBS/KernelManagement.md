## KernelManagement

> `/System/Library/Frameworks/KernelManagement.framework/Versions/A/KernelManagement`

```diff

-463.40.2.0.0
-  __TEXT.__text: 0x3d20
+463.100.7.0.0
+  __TEXT.__text: 0x3cf4
   __TEXT.__auth_stubs: 0x180
-  __TEXT.__objc_methlist: 0x2cc
+  __TEXT.__objc_methlist: 0x3fc
   __TEXT.__const: 0x78
   __TEXT.__gcc_except_tab: 0x10c
   __TEXT.__cstring: 0x1dc
   __TEXT.__oslogstring: 0x292
-  __TEXT.__unwind_info: 0x1b8
+  __TEXT.__unwind_info: 0x1b0
   __TEXT.__objc_classname: 0xa2
   __TEXT.__objc_methname: 0xf31
   __TEXT.__objc_methtype: 0x559

   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2f8
+  __DATA_CONST.__objc_selrefs: 0x320
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x18
   __DATA_CONST.__objc_arraydata: 0x10
   __AUTH_CONST.__auth_got: 0xd0
   __AUTH_CONST.__const: 0x110
   __AUTH_CONST.__cfstring: 0x280
-  __AUTH_CONST.__objc_const: 0x710
+  __AUTH_CONST.__objc_const: 0x4f0
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0x38

   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1C03A159-FB56-3E78-848B-058F1691CBD9
-  Functions: 103
+  UUID: 87306F2D-9D2F-3610-9462-2202DB02B972
+  Functions: 102
   Symbols:   303
   CStrings:  250
 
Functions:
~ -[SimpleKernelExtension initWithBundleIdentifier:fileSystemPath:loaded:kextIsSigned:versionString:lastModifiedDate:signingInfo:infoString:type:displayName:architectures:loadAddress:usageDescription:] : 500 -> 504
~ -[KernelManagementClient unloadExtensionsWithIdentifiers:withClassNames:options:withError:] : 476 -> 472
~ -[KernelManagementClient loadExtensionsWithPaths:withIdentifiers:withPersonalityNames:withDependencyAndFolderPaths:options:withError:] : 540 -> 536
~ -[KernelManagementClient(Private) rebuildAuxiliaryKernelCollectionWithInterface:rebootRequired:withError:] : 512 -> 508
~ -[KernelManagementClient(Private) migrateAuxKCForVolumeGroupUUID:withMigrationSuccess:withRebootRequired:withError:] : 528 -> 524
~ -[KernelManagementClient(Private) triggerAuxKCCleanup:withError:] : 432 -> 428
~ -[KernelManagementClient(Private) triggerPanicMedicInRecoveryWithPath:withError:] : 432 -> 428
~ -[KernelManagementClient(Private) clearAllStagedExtensions:] : 392 -> 388
~ -[KernelManagementClient(Private) checkAllFilesets:] : 392 -> 388
~ _OSKextErrorFromKMError : 128 -> 132
- sub_19981aee0

```
