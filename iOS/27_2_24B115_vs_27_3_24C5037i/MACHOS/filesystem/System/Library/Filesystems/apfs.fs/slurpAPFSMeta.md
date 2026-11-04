## slurpAPFSMeta

> `/System/Library/Filesystems/apfs.fs/slurpAPFSMeta`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

-3288.42.1.0.0
-  __TEXT.__text: 0x37e48
+3288.60.7.0.0
+  __TEXT.__text: 0x37e88
   __TEXT.__auth_stubs: 0x830
-  __TEXT.__cstring: 0x9148
+  __TEXT.__cstring: 0x919a
   __TEXT.__const: 0x1b0
   __TEXT.__unwind_info: 0x850
   __DATA_CONST.__const: 0x470

   - /usr/lib/libSystem.B.dylib
   Functions: 536
   Symbols:   144
-  CStrings:  781
+  CStrings:  782
 
Functions:
~ sub_100016430 : 32 -> 36
~ sub_100020a44 -> sub_100020a48 : 3856 -> 3916
CStrings:
+ "%s:%d: %s error: chunk info index %u out of range for cib %u chunk info count %u\n"
```
