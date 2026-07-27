## efiupdater

> `/usr/libexec/efiupdater`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-32.0.0.0.0
+34.0.0.0.0
   __TEXT.__text: 0x2c3c
   __TEXT.__auth_stubs: 0x480
   __TEXT.__objc_stubs: 0x420
-  __TEXT.__const: 0x27a
+  __TEXT.__const: 0x272
   __TEXT.__gcc_except_tab: 0x28
-  __TEXT.__cstring: 0x9da
+  __TEXT.__cstring: 0x9d6
   __TEXT.__objc_methname: 0x2ba
   __TEXT.__unwind_info: 0xd8
   __DATA_CONST.__auth_got: 0x250
CStrings:
+ "efiupdater 34~5 (Official), built 2026-07-11T16:46:27-0700"
- "efiupdater 32~13015 (Official), built 2026-06-17T03:15:26-0700"
```
