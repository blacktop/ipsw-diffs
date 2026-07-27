## IconServices

> `/System/Library/PrivateFrameworks/IconServices.framework/Versions/A/IconServices`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
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
- `__AUTH_CONST.__auth_got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-743.5.2.400.0
-  __TEXT.__text: 0x8383c
+743.5.2.401.0
+  __TEXT.__text: 0x841bc
   __TEXT.__auth_stubs: 0x1640
   __TEXT.__delay_helper: 0xdc
   __TEXT.__objc_methlist: 0x7714
-  __TEXT.__const: 0x9540
+  __TEXT.__const: 0x9550
   __TEXT.__gcc_except_tab: 0x6f0
   __TEXT.__cstring: 0x4f27
-  __TEXT.__oslogstring: 0x346d
-  __TEXT.__unwind_info: 0x1c60
+  __TEXT.__oslogstring: 0x37d6
+  __TEXT.__unwind_info: 0x1c68
   __TEXT.__eh_frame: 0x88
   __TEXT.__objc_classname: 0x14ef
   __TEXT.__objc_methname: 0xda95

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2978
+  Functions: 2980
   Symbols:   7216
-  CStrings:  4163
+  CStrings:  4175
 
CStrings:
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
- "Error: Rcovery from addValue to corrupt index failed."
```
