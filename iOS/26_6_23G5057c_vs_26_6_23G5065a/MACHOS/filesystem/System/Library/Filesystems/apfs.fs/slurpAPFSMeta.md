## slurpAPFSMeta

> `/System/Library/Filesystems/apfs.fs/slurpAPFSMeta`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

-  __TEXT.__text: 0x36b24
+  __TEXT.__text: 0x36cdc
   __TEXT.__auth_stubs: 0x830
-  __TEXT.__cstring: 0x8f52
+  __TEXT.__cstring: 0x901b
   __TEXT.__const: 0x1b0
   __TEXT.__unwind_info: 0x680
   __DATA_CONST.__auth_got: 0x418

   - /usr/lib/libSystem.B.dylib
   Functions: 521
   Symbols:   144
-  CStrings:  772
+  CStrings:  775
 
Functions:
~ sub_100019634 : 632 -> 636
~ sub_1000258a4 -> sub_1000258a8 : 172 -> 168
~ sub_1000317ec : 1192 -> 1632
CStrings:
+ "%s:%d: %s Invalid reap list free entry %d\n"
+ "%s:%d: %s reap list object expected %u entries, max %u, but we walked %u\n"
+ "%s:%d: %s reap list object expected %u entries, max %u, but we walked %u + %u = %u\n"
```
