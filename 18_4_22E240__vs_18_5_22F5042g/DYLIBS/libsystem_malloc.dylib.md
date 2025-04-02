## libsystem_malloc.dylib

> `/usr/lib/system/libsystem_malloc.dylib`

```diff

-715.102.2.0.0
-  __TEXT.__text: 0x34bdc
+715.120.10.0.0
+  __TEXT.__text: 0x34c5c
   __TEXT.__auth_stubs: 0x6f0
   __TEXT.__const: 0x50c
-  __TEXT.__cstring: 0x8914
+  __TEXT.__cstring: 0x8966
   __TEXT.__dof_magmalloc: 0x912
-  __TEXT.__unwind_info: 0x870
+  __TEXT.__unwind_info: 0x878
   __TEXT.__eh_frame: 0x48
   __DATA_CONST.__got: 0xa8
   __DATA_CONST.__const: 0x6f0

   - /usr/lib/system/libsystem_pthread.dylib
   Functions: 825
   Symbols:   1107
-  CStrings:  783
+  CStrings:  785
 
CStrings:
+ "MallocXzoneEarlyAlloc"
+ "MallocXzoneEarlyAlloc must be 0 or 1.\n"
+ "XZM Config:\n\tData Only: %d\n\tGuards Enabled: %d\n\tScribble: %d\n\tTiny/Small Batch Max: %d\n\tDefer Tiny: %d\n\tDefer Small: %d\n\tDefer Large: %d\n\tHuge Cache Size: %d\n\tReclaim Buffer Count: %u/%u (%s)\n\tRanges (ptr addr/size/data addr/size): 0x%llx/%lu/0x%llx/%lu\n\tEarly Allocator: %s\n\tInitial Slot Config: %s\n\tMax Slot Config: %s\n\tSlot Upgrade Thresholds: %d/%d, %d/%d\n\tTiny Thrash Threshold: %llu ms\n\tSmall Thrash Threshold: %llu ms, %llu bytes\n\tThread Caching: %s (%u allocs, %u contentions, %llu ms)\n\tPointer Bucket Count: %lu\n"
- "XZM Config:\n\tData Only: %d\n\tGuards Enabled: %d\n\tScribble: %d\n\tTiny/Small Batch Max: %d\n\tDefer Tiny: %d\n\tDefer Small: %d\n\tDefer Large: %d\n\tHuge Cache Size: %d\n\tReclaim Buffer Count: %u/%u (%s)\n\tRanges (ptr addr/size/data addr/size): 0x%llx/%lu/0x%llx/%lu\n\tInitial Slot Config: %s\n\tMax Slot Config: %s\n\tSlot Upgrade Thresholds: %d/%d, %d/%d\n\tTiny Thrash Threshold: %llu ms\n\tSmall Thrash Threshold: %llu ms, %llu bytes\n\tThread Caching: %s (%u allocs, %u contentions, %llu ms)\n\tPointer Bucket Count: %lu\n"

```
