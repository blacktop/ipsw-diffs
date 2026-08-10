## efiupdater

> `/usr/libexec/efiupdater`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__objc_selrefs`

```diff

   __TEXT.__objc_stubs: 0x420
   __TEXT.__const: 0x272
   __TEXT.__gcc_except_tab: 0x28
-  __TEXT.__cstring: 0x9d6
+  __TEXT.__cstring: 0x9d7
   __TEXT.__objc_methname: 0x2ba
   __TEXT.__unwind_info: 0xd8
   __DATA_CONST.__auth_got: 0x250
CStrings:
+ "efiupdater 34~11 (Official), built 2026-07-31T20:23:20-0700"
- "efiupdater 34~5 (Official), built 2026-07-11T16:46:27-0700"
```
