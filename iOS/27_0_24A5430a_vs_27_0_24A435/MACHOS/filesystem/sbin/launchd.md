## launchd

> `/sbin/launchd`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__cstring`
- `__TEXT.__dof_launchd`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`
- `__DATA.__os_assumes_log`

```diff

 3298.2.1.0.0
-  __TEXT.__text: 0x5b820
+  __TEXT.__text: 0x5b82c
   __TEXT.__auth_stubs: 0x2700
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0x20c
Functions:
~ sub_100017d48 : 476 -> 480
~ sub_10004eb70 -> sub_10004eb74 : 220 -> 224
~ sub_10004ec4c -> sub_10004ec54 : 608 -> 612
CStrings:
+ "@(#)VERSION:Darwin Bootstrapper Version 7.0.0: Sat Aug  8 16:38:05 PDT 2026; root:libxpc_executables-3298.2.1~23/launchd/RELEASE_ARM64E"
+ "Darwin Bootstrapper Version 7.0.0: Sat Aug  8 16:38:05 PDT 2026; root:libxpc_executables-3298.2.1~23/launchd/RELEASE_ARM64E"
- "@(#)VERSION:Darwin Bootstrapper Version 7.0.0: Sat Aug  8 19:38:49 PDT 2026; root:libxpc_executables-3298.2.1~26/launchd/RELEASE_ARM64E"
- "Darwin Bootstrapper Version 7.0.0: Sat Aug  8 19:38:49 PDT 2026; root:libxpc_executables-3298.2.1~26/launchd/RELEASE_ARM64E"
```
