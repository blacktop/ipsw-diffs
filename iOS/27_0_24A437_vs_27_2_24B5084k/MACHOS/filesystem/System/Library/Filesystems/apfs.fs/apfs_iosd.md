## apfs_iosd

> `/System/Library/Filesystems/apfs.fs/apfs_iosd`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__data`

```diff

-3288.2.1.0.0
-  __TEXT.__text: 0x33a54
-  __TEXT.__auth_stubs: 0xa90
-  __TEXT.__cstring: 0x67af
+3288.40.13.0.0
+  __TEXT.__text: 0x33c88
+  __TEXT.__auth_stubs: 0xaa0
+  __TEXT.__cstring: 0x67dd
   __TEXT.__const: 0x350
   __TEXT.__oslogstring: 0x13e0
-  __TEXT.__unwind_info: 0x8a8
+  __TEXT.__unwind_info: 0x8b0
   __DATA_CONST.__const: 0x708
-  __DATA_CONST.__cfstring: 0xc80
-  __DATA_CONST.__auth_got: 0x548
+  __DATA_CONST.__cfstring: 0xcc0
+  __DATA_CONST.__auth_got: 0x550
   __DATA_CONST.__got: 0xb8
   __DATA_CONST.__auth_ptr: 0x20
   __DATA.__data: 0x9c

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libutil.dylib
-  Functions: 562
-  Symbols:   197
-  CStrings:  752
+  Functions: 564
+  Symbols:   198
+  CStrings:  755
 
Symbols:
+ _CFEqual
CStrings:
+ "IOMatchCategory"
+ "btree_node_compact"
+ "mount_apfs"
```
