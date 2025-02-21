## fileproviderd

> `/System/Library/Frameworks/FileProvider.framework/Support/fileproviderd`

```diff

-2732.80.49.0.0
-  __TEXT.__text: 0x870
-  __TEXT.__auth_stubs: 0x2d0
+2882.100.384.0.0
+  __TEXT.__text: 0x938
+  __TEXT.__auth_stubs: 0x2c0
   __TEXT.__objc_stubs: 0x200
-  __TEXT.__objc_methlist: 0x44
+  __TEXT.__objc_methlist: 0x164
   __TEXT.__const: 0x86
   __TEXT.__cstring: 0xe1
   __TEXT.__objc_classname: 0x37
   __TEXT.__objc_methname: 0x2a2
   __TEXT.__objc_methtype: 0x102
-  __TEXT.__oslogstring: 0x1c1
+  __TEXT.__oslogstring: 0x204
   __TEXT.__constg_swiftt: 0x38
   __TEXT.__swift5_typeref: 0x14
   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_types: 0x4
   __TEXT.__unwind_info: 0x88
-  __DATA_CONST.__auth_got: 0x170
-  __DATA_CONST.__got: 0x38
+  __DATA_CONST.__auth_got: 0x168
+  __DATA_CONST.__got: 0x50
   __DATA_CONST.__const: 0x70
   __DATA_CONST.__cfstring: 0xa0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_const: 0x478
-  __DATA.__objc_selrefs: 0xa0
+  __DATA.__objc_const: 0x268
+  __DATA.__objc_selrefs: 0x140
   __DATA.__objc_ivar: 0x4
   __DATA.__objc_data: 0x100
   __DATA.__data: 0xe8

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/APFS.framework/APFS
   - /System/Library/PrivateFrameworks/CrashReporterSupport.framework/CrashReporterSupport
-  - /System/Library/PrivateFrameworks/FPFS.framework/FPFS
   - /System/Library/PrivateFrameworks/FileProviderDaemon.framework/FileProviderDaemon
   - /System/Library/PrivateFrameworks/FileProviderTelemetry.framework/FileProviderTelemetry
   - /System/Library/PrivateFrameworks/GenerationalStorage.framework/GenerationalStorage

   - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 16
-  Symbols:   73
-  CStrings:  83
+  Functions: 18
+  Symbols:   75
+  CStrings:  84
 
Symbols:
+ _OBJC_CLASS_$_FPCKTask
+ _OBJC_CLASS_$_FPFSSQLBackupManager
+ _OBJC_CLASS_$_FPFSSQLRestoreManager
+ _fpfs_set_support_long_paths_iopolicy
+ _fpfs_supports_long_paths
- _getFPCKTaskClass
- _getFPFSSQLBackupManagerClass
- _getFPFSSQLRestoreManagerClass
CStrings:
+ "[ERROR] failed to enable support for long paths in VFS: %{errno}d\n"

```
