## launchd

> `/sbin/launchd`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_capture`
- `__TEXT.__dof_launchd`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`
- `__DATA.__os_assumes_log`

```diff

-3298.0.21.0.0
-  __TEXT.__text: 0x5ad00
-  __TEXT.__auth_stubs: 0x2390
+3298.1.1.0.0
+  __TEXT.__text: 0x5be58
+  __TEXT.__auth_stubs: 0x23b0
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0x20c
   __TEXT.__const: 0x4a0

   __TEXT.__swift5_fieldmd: 0x60
   __TEXT.__swift5_proto: 0x8
   __TEXT.__swift5_types: 0xc
-  __TEXT.__cstring: 0x16b82
+  __TEXT.__cstring: 0x16f51
   __TEXT.__swift5_capture: 0x14
   __TEXT.__objc_methtype: 0xf
   __TEXT.__objc_classname: 0x212

   __TEXT.__oslogstring: 0xd5
   __TEXT.__config: 0x3b2f
   __TEXT.__dof_launchd: 0x81d
-  __TEXT.__unwind_info: 0x10f0
+  __TEXT.__unwind_info: 0x1128
   __TEXT.__eh_frame: 0x210
-  __DATA_CONST.__const: 0x58d0
+  __DATA_CONST.__const: 0x59d8
   __DATA_CONST.__objc_classlist: 0xc0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0xb0
-  __DATA_CONST.__auth_got: 0x11d0
+  __DATA_CONST.__auth_got: 0x11e0
   __DATA_CONST.__got: 0x210
-  __DATA_CONST.__auth_ptr: 0x80
+  __DATA_CONST.__auth_ptr: 0x88
   __DATA.__objc_const: 0xdf0
   __DATA.__objc_selrefs: 0x8
   __DATA.__objc_data: 0x6e0

   __DATA.__os_assumes_log: 0x8
   __DATA.__crash_info: 0x148
   __DATA.__bss: 0xda8
-  __DATA.__common: 0x800
+  __DATA.__common: 0x808
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libauditd.0.dylib
   - /usr/lib/libbsm.0.dylib

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  Functions: 1466
-  Symbols:   656
-  CStrings:  2852
+  Functions: 1479
+  Symbols:   658
+  CStrings:  2871
 
Symbols:
+ _mkdirat
+ _renameatx_np
CStrings:
+ "@(#)VERSION:Darwin Bootstrapper Version 7.0.0: Mon Aug 10 01:06:09 PDT 2026; root:libxpc_executables-3298.1.1~29/launchd/RELEASE_ARM64E"
+ "Cannot rename secure socket; UIDs mismatch: socket owner=%d, path=%d"
+ "Darwin Bootstrapper Version 7.0.0: Mon Aug 10 01:06:09 PDT 2026; root:libxpc_executables-3298.1.1~29/launchd/RELEASE_ARM64E"
+ "Failed to basename_r() socket directory path: path=%s, error=%s (%d)"
+ "Failed to dirname_r() socket directory path: path=%s, error=%s (%d)"
+ "Failed to dirname_r() socket path: path=%s, error=%s (%d)"
+ "Failed to fstatat() secure socket path: path=%s, error=%s (%d)"
+ "Failed to fstatat() socket path: path=%s, error=%s (%d)"
+ "Failed to open() socket parent directory: path=%s, error=%s (%d)"
+ "Failed to renameat() passive socket from secure path to known path: secure path=%s, known path=%s, error=%s (%d)"
+ "Failed to stat() socket directory path: path=%s, error=%s (%d)"
+ "Invalid socket name: %s"
+ "No hidden path for socket: path=%s"
+ "Secure socket path is not a socket; path=%s"
+ "caller failed %s sandbox check on parent directory %s"
+ "caller failed %s sandbox check on path %s"
+ "caller failed file-write-create sandbox check on grand parent directory %s"
+ "file-write-create"
+ "file-write-unlink"
+ "needs_rename = %s"
+ "setup unix domain socket"
- "@(#)VERSION:Darwin Bootstrapper Version 7.0.0: Mon Jul 13 21:46:13 PDT 2026; root:libxpc_executables-3298.0.21~90/launchd/RELEASE_ARM64E"
- "Darwin Bootstrapper Version 7.0.0: Mon Jul 13 21:46:13 PDT 2026; root:libxpc_executables-3298.0.21~90/launchd/RELEASE_ARM64E"
```
