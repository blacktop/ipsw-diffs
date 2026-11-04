## sm_stats

> `/System/Library/Filesystems/apfs.fs/sm_stats`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

-3288.42.1.0.0
-  __TEXT.__text: 0x43f88
+3288.60.7.0.0
+  __TEXT.__text: 0x43fc8
   __TEXT.__auth_stubs: 0x730
-  __TEXT.__cstring: 0xce46
+  __TEXT.__cstring: 0xce98
   __TEXT.__const: 0x1c8
   __TEXT.__unwind_info: 0x8f8
   __DATA_CONST.__const: 0x6f8

   - /usr/lib/libutil.dylib
   Functions: 597
   Symbols:   130
-  CStrings:  1054
+  CStrings:  1055
 
Functions:
~ sub_10000b7b0 : 3856 -> 3916
~ sub_10001fc84 -> sub_10001fcc0 : 32 -> 36
CStrings:
+ "%s:%d: %s error: chunk info index %u out of range for cib %u chunk info count %u\n"
```
