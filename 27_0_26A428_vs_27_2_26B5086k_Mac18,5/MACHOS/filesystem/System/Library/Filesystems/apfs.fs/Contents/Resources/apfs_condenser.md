## apfs_condenser

> `/System/Library/Filesystems/apfs.fs/Contents/Resources/apfs_condenser`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

-3288.1.3.0.0
-  __TEXT.__text: 0x4d37c
+3288.40.13.0.0
+  __TEXT.__text: 0x4d574
   __TEXT.__auth_stubs: 0x820
-  __TEXT.__cstring: 0xfb6b
+  __TEXT.__cstring: 0xfbc6
   __TEXT.__const: 0x220
-  __TEXT.__unwind_info: 0xa58
+  __TEXT.__unwind_info: 0xa60
   __DATA_CONST.__const: 0x8f8
   __DATA_CONST.__cfstring: 0x140
   __DATA_CONST.__auth_got: 0x410
   __DATA_CONST.__got: 0x48
   __DATA_CONST.__auth_ptr: 0x28
   __DATA.__data: 0x358
-  __DATA.__common: 0x51c
+  __DATA.__common: 0x520
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/DiskArbitration.framework/Versions/A/DiskArbitration
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libutil.dylib
-  Functions: 688
+  Functions: 689
   Symbols:   144
-  CStrings:  1292
+  CStrings:  1294
 
CStrings:
+ "%s:%d: Temp checkpoint protection: refusing regular checkpoint mount\n"
+ "3288.40.13"
+ "btree_node_compact"
- "3288.1.3"
```
