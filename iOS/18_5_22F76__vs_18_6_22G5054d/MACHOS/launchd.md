## launchd

> `/sbin/launchd`

```diff

-2894.122.1.0.0
-  __TEXT.__text: 0x51ab0
+2894.140.10.0.0
+  __TEXT.__text: 0x51a94
   __TEXT.__auth_stubs: 0x2120
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0x1f4
-  __TEXT.__const: 0x2e0
-  __TEXT.__cstring: 0x1505b
+  __TEXT.__const: 0x2f0
+  __TEXT.__cstring: 0x14f6a
   __TEXT.__launchd: 0x1
   __TEXT.__objc_methname: 0x8
   __TEXT.__objc_classname: 0x1ba

   __DATA_CONST.__auth_got: 0x1090
   __DATA_CONST.__got: 0x180
   __DATA_CONST.__auth_ptr: 0x30
-  __DATA_CONST.__const: 0x5340
+  __DATA_CONST.__const: 0x52b0
   __DATA_CONST.__objc_classlist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0xa8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsandbox.1.dylib
-  UUID: FEBB544E-F4DA-3F20-BE33-F8C3B3206218
+  UUID: 70EEDC08-E795-33E9-8D7C-5426BBFEE515
   Functions: 1644
   Symbols:   583
-  CStrings:  2632
+  CStrings:  2624
 
Functions:
~ sub_100004c54 : 1716 -> 1740
~ sub_100048064 -> sub_10004807c : 308 -> 256
CStrings:
+ "@(#)VERSION:Darwin Bootstrapper Version 7.0.0: Tue Jun  3 09:28:22 PDT 2025; root:libxpc_executables-2894.140.10~72/launchd/RELEASE_ARM64E"
+ "Darwin Bootstrapper Version 7.0.0: Tue Jun  3 09:28:22 PDT 2025; root:libxpc_executables-2894.140.10~72/launchd/RELEASE_ARM64E"
+ "Executable not in bundle"
- "@(#)VERSION:Darwin Bootstrapper Version 7.0.0: Tue Apr 22 20:33:03 PDT 2025; root:libxpc_executables-2894.122.1~1/launchd/RELEASE_ARM64E"
- "Darwin Bootstrapper Version 7.0.0: Tue Apr 22 20:33:03 PDT 2025; root:libxpc_executables-2894.122.1~1/launchd/RELEASE_ARM64E"
- "kGUARD_EXC_DEALLOC_GAP"
- "kGUARD_EXC_RECLAIM_COPYIO_FAILURE"
- "kGUARD_EXC_RECLAIM_DEALLOCATE_FAILURE"
- "kGUARD_EXC_RECLAIM_INDEX_FAILURE"
- "kGUARD_EXC_SEC_ACCESS_FAULT"
- "kGUARD_EXC_SEC_COPY_DENIED"
- "kGUARD_EXC_SEC_LOOKUP_DENIED"
- "kGUARD_EXC_SEC_RANGE_DENIED"
- "kGUARD_EXC_SEC_SHARING_DENIED"

```
