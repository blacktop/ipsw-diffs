## launchctl

> `/bin/launchctl`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA.__data`

```diff

-3298.0.21.0.0
+3298.1.1.0.0
   __TEXT.__text: 0xea64
   __TEXT.__auth_stubs: 0xd80
-  __TEXT.__const: 0x300
+  __TEXT.__const: 0x2f0
   __TEXT.__launchctl: 0x1
-  __TEXT.__cstring: 0x62da
+  __TEXT.__cstring: 0x62d8
   __TEXT.__oslogstring: 0x19
   __TEXT.__unwind_info: 0x1d0
   __DATA_CONST.__const: 0x6998
CStrings:
+ "@(#)VERSION:Darwin Bootstrapper Control Interface Version 7.0.0: Mon Aug 10 01:08:45 PDT 2026; root:libxpc_executables-3298.1.1~29/launchctl/RELEASE_ARM64E"
+ "Darwin Bootstrapper Control Interface Version 7.0.0: Mon Aug 10 01:08:45 PDT 2026; root:libxpc_executables-3298.1.1~29/launchctl/RELEASE_ARM64E"
- "@(#)VERSION:Darwin Bootstrapper Control Interface Version 7.0.0: Mon Jul 13 21:49:35 PDT 2026; root:libxpc_executables-3298.0.21~90/launchctl/RELEASE_ARM64E"
- "Darwin Bootstrapper Control Interface Version 7.0.0: Mon Jul 13 21:49:35 PDT 2026; root:libxpc_executables-3298.0.21~90/launchctl/RELEASE_ARM64E"
```
