## IconServices

> `/System/Library/PrivateFrameworks/IconServices.framework/IconServices`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__cstring`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__got`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-  __TEXT.__text: 0x66f90
+  __TEXT.__text: 0x678cc
   __TEXT.__auth_stubs: 0xf50
   __TEXT.__delay_helper: 0xdc
   __TEXT.__objc_methlist: 0x6784
-  __TEXT.__const: 0x8800
+  __TEXT.__const: 0x8810
   __TEXT.__gcc_except_tab: 0x440
   __TEXT.__cstring: 0x3f7c
-  __TEXT.__oslogstring: 0x33f8
-  __TEXT.__unwind_info: 0x17d8
+  __TEXT.__oslogstring: 0x3761
+  __TEXT.__unwind_info: 0x17e0
   __TEXT.__eh_frame: 0x88
   __TEXT.__objc_classname: 0x1262
   __TEXT.__objc_methname: 0xc318

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2540
+  Functions: 2542
   Symbols:   6095
-  CStrings:  3602
+  CStrings:  3614
 
CStrings:
+ "00:00:49"
+ "Calculated node offset out of bounds. NodeOffset: %zu, nodeSize: %zu (==%zu), indexSize: %lu"
+ "Failed to add item to index. Attempted to recover by clearing the index, still failed."
+ "Failed to add item to index. Index will be reset! Current capacity: %d, count: %d. Entries offset: %zu, unallocatedOffset: %d, (== %zu), index size: %lu"
+ "Failed to extend the map table data size."
+ "Invalidating previous map table header (capacity: %d, count: %d)"
+ "Invalidating previous store index header (capacity: %d, count: %d)"
+ "Map table extending data region: %zu -> %zu (capacity: %d, count: %d)"
+ "Map table failed to add value. size: %zu, data length: %lu"
+ "Map table removeAll (capacity: %d)"
+ "Map table resizing capacity: %d -> %d, data size: %zu -> %zu, count: %d"
+ "Store index extending capacity: %d -> %d, data size: %zu -> %zu, count: %d"
+ "Store index extending data region: %zu -> %zu (capacity: %d, count: %d)"
+ "Store index removeAll (capacity: %d)"
- "18:51:32"
- "Error: Rcovery from addValue to corrupt index failed."
```
