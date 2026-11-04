## apfs_iosd

> `/System/Library/Filesystems/apfs.fs/apfs_iosd`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

-3288.42.1.0.0
-  __TEXT.__text: 0x33d84
+3288.60.7.0.0
+  __TEXT.__text: 0x33dc0
   __TEXT.__auth_stubs: 0xaa0
-  __TEXT.__cstring: 0x67dd
+  __TEXT.__cstring: 0x682f
   __TEXT.__const: 0x350
   __TEXT.__oslogstring: 0x13e0
   __TEXT.__unwind_info: 0x8b0

   - /usr/lib/libutil.dylib
   Functions: 564
   Symbols:   198
-  CStrings:  755
+  CStrings:  756
 
Functions:
~ sub_100016344 : 32 -> 36
~ sub_100017508 -> sub_10001750c : 520 -> 516
~ sub_1000296c4 : 3856 -> 3916
CStrings:
+ "%s:%d: %s error: chunk info index %u out of range for cib %u chunk info count %u\n"
```
