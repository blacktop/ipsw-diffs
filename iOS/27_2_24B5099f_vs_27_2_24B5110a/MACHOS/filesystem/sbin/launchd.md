## launchd

> `/sbin/launchd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_capture`
- `__TEXT.__dof_launchd`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-3298.40.28.0.0
-  __TEXT.__text: 0x5abc8
+3298.42.1.0.0
+  __TEXT.__text: 0x5abac
   __TEXT.__auth_stubs: 0x2720
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0x20c

   __TEXT.__swift5_fieldmd: 0x60
   __TEXT.__swift5_proto: 0x8
   __TEXT.__swift5_types: 0xc
-  __TEXT.__cstring: 0x169a6
+  __TEXT.__cstring: 0x16984
   __TEXT.__swift5_capture: 0x14
   __TEXT.__objc_methtype: 0xf
   __TEXT.__objc_classname: 0x212
   __TEXT.__objc_methname: 0x1c
   __TEXT.__gcc_except_tab: 0xf8
   __TEXT.__oslogstring: 0xd5
-  __TEXT.__config: 0x2a71
+  __TEXT.__config: 0x2a50
   __TEXT.__dof_launchd: 0x67c
   __TEXT.__unwind_info: 0x1778
   __TEXT.__eh_frame: 0x210

   __DATA.__data: 0xac0
   __DATA.__os_assumes_log: 0x8
   __DATA.__crash_info: 0x148
-  __DATA.__common: 0x7f0
+  __DATA.__common: 0x7f8
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   Functions: 1484
   Symbols:   712
-  CStrings:  2836
+  CStrings:  2834
 
Functions:
~ sub_100049470 : 2980 -> 2952
CStrings:
+ "@(#)VERSION:Darwin Bootstrapper Version 7.0.0: Sat Oct  3 23:05:26 PDT 2026; root:libxpc_executables-3298.42.1~6/launchd/RELEASE_ARM64E"
+ "Darwin Bootstrapper Version 7.0.0: Sat Oct  3 23:05:26 PDT 2026; root:libxpc_executables-3298.42.1~6/launchd/RELEASE_ARM64E"
- "@(#)VERSION:Darwin Bootstrapper Version 7.0.0: Sat Sep 26 06:06:59 PDT 2026; root:libxpc_executables-3298.40.28~39/launchd/RELEASE_ARM64E"
- "Darwin Bootstrapper Version 7.0.0: Sat Sep 26 06:06:59 PDT 2026; root:libxpc_executables-3298.40.28~39/launchd/RELEASE_ARM64E"
- "IgnoreCache"
- "launchd_no_cache="
```
