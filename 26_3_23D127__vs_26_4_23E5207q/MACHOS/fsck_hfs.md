## fsck_hfs

> `/System/Library/Filesystems/hfs.fs/fsck_hfs`

```diff

-704.60.4.0.0
-  __TEXT.__text: 0x30268
-  __TEXT.__auth_stubs: 0x7b0
-  __TEXT.__const: 0x112c
-  __TEXT.__cstring: 0x6e13
-  __TEXT.__unwind_info: 0x508
-  __DATA_CONST.__auth_got: 0x3d8
+715.100.9.0.0
+  __TEXT.__text: 0x3dcf4
+  __TEXT.__auth_stubs: 0x850
+  __TEXT.__const: 0x4c2e
+  __TEXT.__cstring: 0x803b
+  __TEXT.__unwind_info: 0x588
+  __DATA_CONST.__auth_got: 0x428
   __DATA_CONST.__got: 0x50
   __DATA_CONST.__auth_ptr: 0x20
   __DATA_CONST.__const: 0x370
   __DATA_CONST.__cfstring: 0x40
-  __DATA.__data: 0x33e8
+  __DATA.__data: 0x10958
   __DATA.__common: 0x50e8
   __DATA.__bss: 0x186
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/FSKit.framework/FSKit
   - /usr/lib/libSystem.B.dylib
-  UUID: 22C2217B-667C-3EA3-ABFD-108E65AC0216
-  Functions: 471
-  Symbols:   138
-  CStrings:  787
+  - @rpath/libclang_rt.ubsan_ios_dynamic.dylib
+  UUID: 1CBC17C8-433F-3242-BE8D-3D042D3FDB02
+  Functions: 923
+  Symbols:   148
+  CStrings:  821
 
Symbols:
+ ___ubsan_handle_add_overflow_abort
+ ___ubsan_handle_builtin_unreachable
+ ___ubsan_handle_divrem_overflow_abort
+ ___ubsan_handle_mul_overflow_abort
+ ___ubsan_handle_negate_overflow_abort
+ ___ubsan_handle_out_of_bounds_abort
+ ___ubsan_handle_pointer_overflow_abort
+ ___ubsan_handle_shift_out_of_bounds_abort
+ ___ubsan_handle_sub_overflow_abort
+ ___ubsan_handle_type_mismatch_v1_abort
+ ___ubsan_handle_vla_bound_not_positive_abort
- _memset
CStrings:
+ "\t%s - volume header total allocation blocks is too small to be valid \n"
+ "\tvolume allocation block count %d \n"
+ "/AppleInternal/Library/BuildRoots/4~CIU0ugDDCg8CEhpBxpsYl1ItP1jaAgS3U5yjZxY/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/_ctype.h"
+ "/Library/Caches/com.apple.xbs/20022CBB-7987-4277-B5C3-995958015464/TemporaryDirectory.VvPQcD/Sources/hfs/fsck_hfs/fsck_hfs.c"
+ "/Library/Caches/com.apple.xbs/20022CBB-7987-4277-B5C3-995958015464/TemporaryDirectory.VvPQcD/Sources/hfs/fsck_hfs/fsck_messages.c"
+ "/Library/Caches/com.apple.xbs/20022CBB-7987-4277-B5C3-995958015464/TemporaryDirectory.VvPQcD/Sources/hfs/fsck_hfs/utilities.c"
+ "/Library/Caches/com.apple.xbs/20022CBB-7987-4277-B5C3-995958015464/TemporaryDirectory.VvPQcD/Sources/hfs/lib_fsck_hfs/cache.c"
+ "/Library/Caches/com.apple.xbs/20022CBB-7987-4277-B5C3-995958015464/TemporaryDirectory.VvPQcD/Sources/hfs/lib_fsck_hfs/check.c"
+ "/Library/Caches/com.apple.xbs/20022CBB-7987-4277-B5C3-995958015464/TemporaryDirectory.VvPQcD/Sources/hfs/lib_fsck_hfs/dfalib/BTree.c"
+ "/Library/Caches/com.apple.xbs/20022CBB-7987-4277-B5C3-995958015464/TemporaryDirectory.VvPQcD/Sources/hfs/lib_fsck_hfs/dfalib/BTreeAllocate.c"
+ "/Library/Caches/com.apple.xbs/20022CBB-7987-4277-B5C3-995958015464/TemporaryDirectory.VvPQcD/Sources/hfs/lib_fsck_hfs/dfalib/BTreeMiscOps.c"
+ "/Library/Caches/com.apple.xbs/20022CBB-7987-4277-B5C3-995958015464/TemporaryDirectory.VvPQcD/Sources/hfs/lib_fsck_hfs/dfalib/BTreeNodeOps.c"
+ "/Library/Caches/com.apple.xbs/20022CBB-7987-4277-B5C3-995958015464/TemporaryDirectory.VvPQcD/Sources/hfs/lib_fsck_hfs/dfalib/BTreeScanner.c"
+ "/Library/Caches/com.apple.xbs/20022CBB-7987-4277-B5C3-995958015464/TemporaryDirectory.VvPQcD/Sources/hfs/lib_fsck_hfs/dfalib/BTreeTreeOps.c"
+ "/Library/Caches/com.apple.xbs/20022CBB-7987-4277-B5C3-995958015464/TemporaryDirectory.VvPQcD/Sources/hfs/lib_fsck_hfs/dfalib/BlockCache.c"
+ "/Library/Caches/com.apple.xbs/20022CBB-7987-4277-B5C3-995958015464/TemporaryDirectory.VvPQcD/Sources/hfs/lib_fsck_hfs/dfalib/CatalogCheck.c"
+ "/Library/Caches/com.apple.xbs/20022CBB-7987-4277-B5C3-995958015464/TemporaryDirectory.VvPQcD/Sources/hfs/lib_fsck_hfs/dfalib/HardLinkCheck.c"
+ "/Library/Caches/com.apple.xbs/20022CBB-7987-4277-B5C3-995958015464/TemporaryDirectory.VvPQcD/Sources/hfs/lib_fsck_hfs/dfalib/SAllocate.c"
+ "/Library/Caches/com.apple.xbs/20022CBB-7987-4277-B5C3-995958015464/TemporaryDirectory.VvPQcD/Sources/hfs/lib_fsck_hfs/dfalib/SBTree.c"
+ "/Library/Caches/com.apple.xbs/20022CBB-7987-4277-B5C3-995958015464/TemporaryDirectory.VvPQcD/Sources/hfs/lib_fsck_hfs/dfalib/SCatalog.c"
+ "/Library/Caches/com.apple.xbs/20022CBB-7987-4277-B5C3-995958015464/TemporaryDirectory.VvPQcD/Sources/hfs/lib_fsck_hfs/dfalib/SControl.c"
+ "/Library/Caches/com.apple.xbs/20022CBB-7987-4277-B5C3-995958015464/TemporaryDirectory.VvPQcD/Sources/hfs/lib_fsck_hfs/dfalib/SDevice.c"
+ "/Library/Caches/com.apple.xbs/20022CBB-7987-4277-B5C3-995958015464/TemporaryDirectory.VvPQcD/Sources/hfs/lib_fsck_hfs/dfalib/SExtents.c"
+ "/Library/Caches/com.apple.xbs/20022CBB-7987-4277-B5C3-995958015464/TemporaryDirectory.VvPQcD/Sources/hfs/lib_fsck_hfs/dfalib/SKeyCompare.c"
+ "/Library/Caches/com.apple.xbs/20022CBB-7987-4277-B5C3-995958015464/TemporaryDirectory.VvPQcD/Sources/hfs/lib_fsck_hfs/dfalib/SRebuildBTree.c"
+ "/Library/Caches/com.apple.xbs/20022CBB-7987-4277-B5C3-995958015464/TemporaryDirectory.VvPQcD/Sources/hfs/lib_fsck_hfs/dfalib/SRepair.c"
+ "/Library/Caches/com.apple.xbs/20022CBB-7987-4277-B5C3-995958015464/TemporaryDirectory.VvPQcD/Sources/hfs/lib_fsck_hfs/dfalib/SStubs.c"
+ "/Library/Caches/com.apple.xbs/20022CBB-7987-4277-B5C3-995958015464/TemporaryDirectory.VvPQcD/Sources/hfs/lib_fsck_hfs/dfalib/SUtils.c"
+ "/Library/Caches/com.apple.xbs/20022CBB-7987-4277-B5C3-995958015464/TemporaryDirectory.VvPQcD/Sources/hfs/lib_fsck_hfs/dfalib/SVerify1.c"
+ "/Library/Caches/com.apple.xbs/20022CBB-7987-4277-B5C3-995958015464/TemporaryDirectory.VvPQcD/Sources/hfs/lib_fsck_hfs/dfalib/SVerify2.c"
+ "/Library/Caches/com.apple.xbs/20022CBB-7987-4277-B5C3-995958015464/TemporaryDirectory.VvPQcD/Sources/hfs/lib_fsck_hfs/dfalib/VolumeBitmapCheck.c"
+ "/Library/Caches/com.apple.xbs/20022CBB-7987-4277-B5C3-995958015464/TemporaryDirectory.VvPQcD/Sources/hfs/lib_fsck_hfs/dfalib/dirhardlink.c"
+ "/Library/Caches/com.apple.xbs/20022CBB-7987-4277-B5C3-995958015464/TemporaryDirectory.VvPQcD/Sources/hfs/lib_fsck_hfs/dfalib/hfs_endian.c"
+ "/Library/Caches/com.apple.xbs/20022CBB-7987-4277-B5C3-995958015464/TemporaryDirectory.VvPQcD/Sources/hfs/lib_fsck_hfs/fsck_debug.c"
+ "/Library/Caches/com.apple.xbs/20022CBB-7987-4277-B5C3-995958015464/TemporaryDirectory.VvPQcD/Sources/hfs/lib_fsck_hfs/fsck_journal.c"
- "dotdot\r"

```
