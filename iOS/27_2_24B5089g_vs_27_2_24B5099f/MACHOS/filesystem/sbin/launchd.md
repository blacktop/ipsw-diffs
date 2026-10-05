## launchd

> `/sbin/launchd`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_capture`
- `__TEXT.__dof_launchd`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`
- `__DATA.__os_assumes_log`

```diff

-3298.40.20.0.0
-  __TEXT.__text: 0x5a93c
-  __TEXT.__auth_stubs: 0x2710
+3298.40.28.0.0
+  __TEXT.__text: 0x5abc8
+  __TEXT.__auth_stubs: 0x2720
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0x20c
   __TEXT.__const: 0x500

   __TEXT.__swift5_fieldmd: 0x60
   __TEXT.__swift5_proto: 0x8
   __TEXT.__swift5_types: 0xc
-  __TEXT.__cstring: 0x168c6
+  __TEXT.__cstring: 0x169a6
   __TEXT.__swift5_capture: 0x14
   __TEXT.__objc_methtype: 0xf
   __TEXT.__objc_classname: 0x212

   __TEXT.__dof_launchd: 0x67c
   __TEXT.__unwind_info: 0x1778
   __TEXT.__eh_frame: 0x210
-  __DATA_CONST.__const: 0x59e0
+  __DATA_CONST.__const: 0x59e8
   __DATA_CONST.__objc_classlist: 0xc0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0xb0
-  __DATA_CONST.__auth_got: 0x1390
+  __DATA_CONST.__auth_got: 0x1398
   __DATA_CONST.__got: 0x210
   __DATA_CONST.__auth_ptr: 0xa0
   __DATA.__objc_const: 0xdf0

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   Functions: 1484
-  Symbols:   711
-  CStrings:  2830
+  Symbols:   712
+  CStrings:  2836
 
Symbols:
+ _fstatfs
+ _objc_retain_x23
- _objc_retain_x22
CStrings:
+ "@(#)VERSION:Darwin Bootstrapper Version 7.0.0: Sat Sep 26 06:06:59 PDT 2026; root:libxpc_executables-3298.40.28~39/launchd/RELEASE_ARM64E"
+ "Darwin Bootstrapper Version 7.0.0: Sat Sep 26 06:06:59 PDT 2026; root:libxpc_executables-3298.40.28~39/launchd/RELEASE_ARM64E"
+ "Failed to resolve BundlePath: error=%s: %d, caller=%s"
+ "_BundlePath"
+ "bundle path = %s"
+ "com.apple.private.xpc.launchd.allow-set-bundle-path"
+ "fstatfs failed, treating ownership as untrusted: %d: %s"
+ "v20@?0^{_launch_io_s={_launch_object_s=^vB}{?={_xpc_token_s=IIIIIiii}Q}{?=C*^{dispatch_data_s}^{_xpc_bundle_s}^v{stat=iSSQIIi{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}qqiIIi[2q]}i^{dispatch_queue_s}@?b1b1b1b1b1b1}}8i16"
+ "v28@?0^{_launch_domain_io_s={_launch_object_s=^vB}{?=*{_xpc_token_s=IIIIIiii}Q^{dispatch_queue_s}@?@?^{_launch_array_s}ICb1}}8^{_launch_io_s={_launch_object_s=^vB}{?={_xpc_token_s=IIIIIiii}Q}{?=C*^{dispatch_data_s}^{_xpc_bundle_s}^v{stat=iSSQIIi{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}qqiIIi[2q]}i^{dispatch_queue_s}@?b1b1b1b1b1b1}}16i24"
+ "vproc not allowed by caller %s"
- "@(#)VERSION:Darwin Bootstrapper Version 7.0.0: Sun Sep 13 20:53:38 PDT 2026; root:libxpc_executables-3298.40.20~223/launchd/RELEASE_ARM64E"
- "Darwin Bootstrapper Version 7.0.0: Sun Sep 13 20:53:38 PDT 2026; root:libxpc_executables-3298.40.20~223/launchd/RELEASE_ARM64E"
- "v20@?0^{_launch_io_s={_launch_object_s=^vB}{?={_xpc_token_s=IIIIIiii}Q}{?=C*^{dispatch_data_s}^{_xpc_bundle_s}^v{stat=iSSQIIi{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}qqiIIi[2q]}i^{dispatch_queue_s}@?b1b1b1b1b1}}8i16"
- "v28@?0^{_launch_domain_io_s={_launch_object_s=^vB}{?=*{_xpc_token_s=IIIIIiii}Q^{dispatch_queue_s}@?@?^{_launch_array_s}ICb1}}8^{_launch_io_s={_launch_object_s=^vB}{?={_xpc_token_s=IIIIIiii}Q}{?=C*^{dispatch_data_s}^{_xpc_bundle_s}^v{stat=iSSQIIi{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}qqiIIi[2q]}i^{dispatch_queue_s}@?b1b1b1b1b1}}16i24"
```
