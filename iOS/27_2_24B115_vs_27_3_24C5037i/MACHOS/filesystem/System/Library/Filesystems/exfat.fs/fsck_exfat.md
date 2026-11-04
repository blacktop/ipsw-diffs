## fsck_exfat

> `/System/Library/Filesystems/exfat.fs/fsck_exfat`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

-561.40.5.0.0
-  __TEXT.__text: 0xce64
+561.60.2.0.0
+  __TEXT.__text: 0xceb0
   __TEXT.__auth_stubs: 0x610
   __TEXT.__const: 0x280
-  __TEXT.__cstring: 0x35af
+  __TEXT.__cstring: 0x35da
   __TEXT.__oslogstring: 0x18
   __TEXT.__unwind_info: 0x320
   __DATA_CONST.__const: 0x3e8

   - /usr/lib/libSystem.B.dylib
   Functions: 193
   Symbols:   115
-  CStrings:  375
+  CStrings:  376
 
Functions:
~ sub_10000717c : 1816 -> 1892
CStrings:
+ "FAT (%u sectors) too small for %u clusters"
```
