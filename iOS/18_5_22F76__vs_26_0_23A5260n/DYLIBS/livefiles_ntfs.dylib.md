## livefiles_ntfs.dylib

> `/System/Library/PrivateFrameworks/UserFS.framework/PlugIns/livefiles_ntfs.dylib`

```diff

-161.100.2.0.0
-  __TEXT.__text: 0x431d0
-  __TEXT.__auth_stubs: 0x470
-  __TEXT.__const: 0xdd8
+166.0.0.0.0
+  __TEXT.__text: 0x43a04
+  __TEXT.__auth_stubs: 0x4a0
+  __TEXT.__const: 0xde8
   __TEXT.__cstring: 0x13953
-  __TEXT.__oslogstring: 0xe4b
-  __TEXT.__unwind_info: 0x570
-  __DATA_CONST.__got: 0x28
-  __AUTH_CONST.__auth_got: 0x238
+  __TEXT.__oslogstring: 0xf3d
+  __TEXT.__unwind_info: 0x578
+  __TEXT.__objc_methname: 0x6e
+  __TEXT.__objc_stubs: 0x80
+  __DATA_CONST.__got: 0x30
+  __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_selrefs: 0x20
+  __AUTH_CONST.__auth_got: 0x258
   __AUTH_CONST.__const: 0x38
   __AUTH.__data: 0x488
   __DATA.__data: 0xd8
   __DATA.__common: 0x108
   __DATA.__bss: 0x608
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
+  - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/LiveFS.framework/LiveFS
   - /System/Library/PrivateFrameworks/UserFS.framework/UserFS
   - /usr/lib/libSystem.B.dylib
-  UUID: 1D073DF2-2026-3B8F-8B12-3BF8A11CE271
-  Functions: 1026
-  Symbols:   2930
-  CStrings:  1645
+  - /usr/lib/libobjc.A.dylib
+  UUID: EA859240-9903-340C-AA46-276498B62E8A
+  Functions: 1037
+  Symbols:   2960
+  CStrings:  1655
 
Symbols:
+ _OBJC_CLASS_$_LiveFSServiceUserClient
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend
+ _objc_msgSend$closeFileDescriptorForKernel:
+ _objc_msgSend$defaultClient
+ _objc_msgSend$openFileDescriptorForKernel:flags:
+ _objc_msgSend$readMeta:buffer:offset:length:
+ _objc_release_x21
+ _objc_release_x23
+ _xpl_buf_meta_read
+ _xpl_buf_meta_read.cold.1
+ _xpl_grant_kernel_access_to_fd
+ _xpl_grant_kernel_access_to_fd.cold.1
+ _xpl_grant_kernel_access_to_fd.cold.2
+ _xpl_revoke_kernel_access_to_fd
+ _xpl_revoke_kernel_access_to_fd.cold.1
+ _xpl_revoke_kernel_access_to_fd.cold.2
+ _xpl_revoke_kernel_access_to_fd.cold.3
+ _xpl_revoke_kernel_access_to_fd.cold.4
+ _xpl_vfs_mount_alloc_init.cold.2
- _ntfs_inode_hash_list_find
CStrings:
+ "buf_meta_read:error:0x%x"
+ "closeFileDescriptorForKernel:"
+ "could not enable metadata io kernel assist"
+ "defaultClient"
+ "grant:kernel:access:to:fd:%d:flags:0x%x:finish:%d"
+ "grant:kernel:access:to:fd:%d:flags:0x%x:start"
+ "openFileDescriptorForKernel:flags:"
+ "readMeta:buffer:offset:length:"
+ "revoke:kernel:access:to:fd:%d:finish:0x%x"
+ "revoke:kernel:access:to:fd:%d:start"

```
