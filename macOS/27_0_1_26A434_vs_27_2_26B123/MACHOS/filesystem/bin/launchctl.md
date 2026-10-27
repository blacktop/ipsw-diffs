## launchctl

> `/bin/launchctl`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA.__data`

```diff

-3298.1.1.0.0
+3298.40.28.0.0
   __TEXT.__text: 0xe9bc
   __TEXT.__auth_stubs: 0xd80
-  __TEXT.__const: 0x2f0
+  __TEXT.__const: 0x300
   __TEXT.__launchctl: 0x1
-  __TEXT.__info_plist: 0x4e2
-  __TEXT.__cstring: 0x62d8
+  __TEXT.__info_plist: 0x4de
+  __TEXT.__cstring: 0x62de
   __TEXT.__oslogstring: 0x19
   __TEXT.__unwind_info: 0x2c0
   __DATA_CONST.__const: 0x6998
CStrings:
+ "@(#)VERSION:Darwin Bootstrapper Control Interface Version 7.0.0: Sat Oct  3 17:02:55 PDT 2026; root:libxpc_executables-3298.40.28~144/launchctl/RELEASE_ARM64E"
+ "Darwin Bootstrapper Control Interface Version 7.0.0: Sat Oct  3 17:02:55 PDT 2026; root:libxpc_executables-3298.40.28~144/launchctl/RELEASE_ARM64E"
- "@(#)VERSION:Darwin Bootstrapper Control Interface Version 7.0.0: Sat Aug 22 16:54:46 PDT 2026; root:libxpc_executables-3298.1.1~67/launchctl/RELEASE_ARM64E"
- "Darwin Bootstrapper Control Interface Version 7.0.0: Sat Aug 22 16:54:46 PDT 2026; root:libxpc_executables-3298.1.1~67/launchctl/RELEASE_ARM64E"
```
