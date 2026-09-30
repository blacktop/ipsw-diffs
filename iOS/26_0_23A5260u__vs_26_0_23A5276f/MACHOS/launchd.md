## launchd

> `/sbin/launchd`

```diff

-3070.0.0.0.2
-  __TEXT.__text: 0x54218
+3088.0.0.0.0
+  __TEXT.__text: 0x542d8
   __TEXT.__auth_stubs: 0x21f0
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0x20c
-  __TEXT.__const: 0x350
-  __TEXT.__cstring: 0x158c9
+  __TEXT.__const: 0x340
+  __TEXT.__cstring: 0x157ea
   __TEXT.__launchd: 0x1
   __TEXT.__objc_methname: 0x8
   __TEXT.__objc_classname: 0x1d5

   __DATA_CONST.__auth_got: 0x10f8
   __DATA_CONST.__got: 0x198
   __DATA_CONST.__auth_ptr: 0x38
-  __DATA_CONST.__const: 0x5658
+  __DATA_CONST.__const: 0x55c8
   __DATA_CONST.__objc_classlist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0xb0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsandbox.1.dylib
-  UUID: 1DF26BE9-A01B-3D53-825F-DDFBE3D3477A
-  Functions: 1712
+  UUID: 5903B1CC-6D97-302B-A7BB-CF6D3C79833C
+  Functions: 1714
   Symbols:   598
-  CStrings:  2706
+  CStrings:  2700
 
CStrings:
+ "@(#)VERSION:Darwin Bootstrapper Version 7.0.0: Fri Jun 13 07:15:26 PDT 2025; root:libxpc_executables-3088~40/launchd/RELEASE_ARM64E"
+ "Darwin Bootstrapper Version 7.0.0: Fri Jun 13 07:15:26 PDT 2025; root:libxpc_executables-3088~40/launchd/RELEASE_ARM64E"
+ "Executable not in bundle"
+ "leader-pid"
+ "perform reboot failed: %d"
+ "v16@?0^{_launch_coalition_s={_launch_obj_header_s=^vB}CiQQi**^{coalition_resource_usage}^?}8"
- "@(#)VERSION:Darwin Bootstrapper Version 7.0.0: Sat May 24 04:24:41 PDT 2025; root:libxpc_executables-3070.0.0.0.2~30/launchd/RELEASE_ARM64E"
- "Darwin Bootstrapper Version 7.0.0: Sat May 24 04:24:41 PDT 2025; root:libxpc_executables-3070.0.0.0.2~30/launchd/RELEASE_ARM64E"
- "kGUARD_EXC_DEALLOC_GAP"
- "kGUARD_EXC_RECLAIM_COPYIO_FAILURE"
- "kGUARD_EXC_RECLAIM_DEALLOCATE_FAILURE"
- "kGUARD_EXC_RECLAIM_INDEX_FAILURE"
- "kGUARD_EXC_SEC_ACCESS_FAULT"
- "kGUARD_EXC_SEC_COPY_DENIED"
- "kGUARD_EXC_SEC_LOOKUP_DENIED"
- "kGUARD_EXC_SEC_RANGE_DENIED"
- "kGUARD_EXC_SEC_SHARING_DENIED"
- "v16@?0^{_launch_coalition_s={_launch_obj_header_s=^vB}CiQQ**^{coalition_resource_usage}^?}8"

```
