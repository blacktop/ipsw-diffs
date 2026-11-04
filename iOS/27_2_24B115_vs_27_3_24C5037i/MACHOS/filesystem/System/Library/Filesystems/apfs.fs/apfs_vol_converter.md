## apfs_vol_converter

> `/System/Library/Filesystems/apfs.fs/apfs_vol_converter`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

-3288.42.1.0.0
-  __TEXT.__text: 0x5a3d0
+3288.60.7.0.0
+  __TEXT.__text: 0x5a350
   __TEXT.__auth_stubs: 0xa10
   __TEXT.__init_offsets: 0x4
   __TEXT.__const: 0x750
-  __TEXT.__cstring: 0x1206b
+  __TEXT.__cstring: 0x120bd
   __TEXT.__gcc_except_tab: 0x6a4
-  __TEXT.__unwind_info: 0xf38
+  __TEXT.__unwind_info: 0xf48
   __DATA_CONST.__const: 0xb20
   __DATA_CONST.__cfstring: 0xb80
   __DATA_CONST.__auth_got: 0x510

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libutil.dylib
-  Functions: 908
+  Functions: 911
   Symbols:   187
-  CStrings:  1617
+  CStrings:  1618
 
CStrings:
+ "%s:%d: %s error: chunk info index %u out of range for cib %u chunk info count %u\n"
+ "3288.60.7"
- "3288.42.1"
```
