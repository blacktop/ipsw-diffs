## Bom

> `/System/Library/PrivateFrameworks/Bom.framework/Bom`

```diff

-265.0.0.0.0
-  __TEXT.__text: 0x557e8
+269.0.0.0.0
+  __TEXT.__text: 0x56494
   __TEXT.__auth_stubs: 0x1840
-  __TEXT.__cstring: 0x11550
-  __TEXT.__const: 0x1518
-  __TEXT.__oslogstring: 0xfbb
+  __TEXT.__cstring: 0x119ea
+  __TEXT.__const: 0x1508
+  __TEXT.__oslogstring: 0x1011
   __TEXT.__unwind_info: 0xa80
   __DATA_CONST.__got: 0x70
   __DATA_CONST.__const: 0x9a8
   __AUTH_CONST.__auth_got: 0xc20
   __AUTH_CONST.__const: 0x180
-  __AUTH_CONST.__cfstring: 0x11a0
-  __DATA.__data: 0x20
+  __AUTH_CONST.__cfstring: 0x11c0
+  __DATA.__data: 0x168
   __DATA.__bss: 0x8dc
   __DATA_DIRTY.__data: 0x160
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libbz2.1.0.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 195A15E2-074B-32B1-B8BB-3DBDF06420B9
-  Functions: 1048
-  Symbols:   2054
-  CStrings:  2405
+  UUID: 250D0264-20F5-3746-A3DB-0726C4A25F39
+  Functions: 1051
+  Symbols:   2062
+  CStrings:  2434
 
Symbols:
+ _BOMFilePreallocate
+ _inject_apple_double_bytes
+ _next_source_entry
+ _pop_replay_stack
+ _populate_sequester_stack
- _BOMBufferDeallocate
CStrings:
+ "%s/._%s"
+ "Could not allocate last path component buffer: %s\n"
+ "Could not allocate parent path buffer: %s\n"
+ "Could not construct insert entry path: %s\n"
+ "Could not convert kBOMCopierSourceOptionSegmentFileSizeKey to kCFNumberLongLongType"
+ "Could not create AppleDouble injection entry"
+ "Could not create insert entry path"
+ "Could not create last path component"
+ "Could not create parent path"
+ "Could not get basename of %s: %s\n"
+ "Could not get dirname of %s: %s\n"
+ "Could not get last path component"
+ "Could not get parent path"
+ "Could not preallocate regular file at %s for %llu: %s"
+ "Could not push source entry onto the preempty stack"
+ "Could not read from source entry\n"
+ "Could not set insert entry path"
+ "Injecting AppleDouble between segmented files"
+ "May 18 2025"
+ "Previous split file path is NULL"
+ "Read 0 bytes from deterministic source."
+ "injectAppleDouble requires creating a CPIO"
+ "injectAppleDouble requires segment large files"
+ "injectAppleDoubleBetweenSegmentedFiles"
+ "kBOMCopierOptionInjectAppleDoubleBetweenSegmentedFilesKey is not a CFBooleanRef"
+ "kBOMCopierOptionInjectAppleDoubleBetweenSegmentedFilesKey must be a CFBooleanRef"
+ "kBOMCopierSourceOptionInjectAppleDoubleBetweenSegmentedFilesKey must be a CFBooleanRef"
+ "kBOMCopierSourceOptionSegmentFileSizeKey must be a CFNumberRef"
+ "synthesize_inject_apple_double"
- "Apr 19 2025"

```
