## fileproviderd

> `/System/Library/Frameworks/FileProvider.framework/Support/fileproviderd`

```diff

-2732.81.1.0.0
-  __TEXT.__text: 0xcdc
-  __TEXT.__auth_stubs: 0x2c0
+2882.101.2.0.0
+  __TEXT.__text: 0xda0
+  __TEXT.__auth_stubs: 0x2b0
   __TEXT.__objc_stubs: 0x2e0
-  __TEXT.__objc_methlist: 0x44
+  __TEXT.__objc_methlist: 0x164
   __TEXT.__const: 0x8e
   __TEXT.__cstring: 0x111
   __TEXT.__objc_classname: 0x37
   __TEXT.__objc_methname: 0x32e
   __TEXT.__objc_methtype: 0x102
-  __TEXT.__oslogstring: 0x26a
+  __TEXT.__oslogstring: 0x2ad
   __TEXT.__constg_swiftt: 0x38
   __TEXT.__swift5_typeref: 0x14
   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_types: 0x4
   __TEXT.__unwind_info: 0x90
-  __DATA_CONST.__auth_got: 0x168
-  __DATA_CONST.__got: 0x50
+  __DATA_CONST.__auth_got: 0x160
+  __DATA_CONST.__got: 0x68
   __DATA_CONST.__const: 0x78
   __DATA_CONST.__cfstring: 0xa0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_const: 0x478
-  __DATA.__objc_selrefs: 0xd8
+  __DATA.__objc_const: 0x268
+  __DATA.__objc_selrefs: 0x178
   __DATA.__objc_ivar: 0x4
   __DATA.__objc_data: 0x100
   __DATA.__data: 0xe8

   - /System/Library/PrivateFrameworks/APFS.framework/Versions/A/APFS
   - /System/Library/PrivateFrameworks/CrashReporterSupport.framework/Versions/A/CrashReporterSupport
   - /System/Library/PrivateFrameworks/DesktopServicesPriv.framework/Versions/A/DesktopServicesPriv
-  - /System/Library/PrivateFrameworks/FPFS.framework/Versions/A/FPFS
   - /System/Library/PrivateFrameworks/FileProviderDaemon.framework/Versions/A/FileProviderDaemon
   - /System/Library/PrivateFrameworks/FileProviderTelemetry.framework/Versions/A/FileProviderTelemetry
   - /System/Library/PrivateFrameworks/GenerationalStorage.framework/Versions/A/GenerationalStorage

   - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: C1F3D02F-F68B-3EC9-908A-3FDEAFE890B2
-  Functions: 20
-  Symbols:   76
-  CStrings:  101
+  UUID: 3C5C0958-C64F-34B9-A2A1-E5A1EC375995
+  Functions: 21
+  Symbols:   78
+  CStrings:  102
 
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
