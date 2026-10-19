## CalendarFoundation

> `/System/Library/PrivateFrameworks/CalendarFoundation.framework/CalendarFoundation`

```diff

 1636.2.2.0.0
-  __TEXT.__text: 0x61bf8
-  __TEXT.__objc_methlist: 0x5db4
-  __TEXT.__cstring: 0x6602
+  __TEXT.__text: 0x6319c
+  __TEXT.__objc_methlist: 0x5dcc
+  __TEXT.__cstring: 0x6662
   __TEXT.__const: 0x8f4
-  __TEXT.__gcc_except_tab: 0xaf8
-  __TEXT.__oslogstring: 0x39a5
+  __TEXT.__gcc_except_tab: 0xbcc
+  __TEXT.__oslogstring: 0x3d55
   __TEXT.__ustring: 0x2e8
   __TEXT.__dlopen_cstrs: 0x5a
   __TEXT.__swift5_typeref: 0x2cc

   __TEXT.__swift_as_entry: 0x8
   __TEXT.__swift_as_ret: 0x8
   __TEXT.__swift_as_cont: 0x8
-  __TEXT.__unwind_info: 0x2758
+  __TEXT.__unwind_info: 0x27a8
   __TEXT.__eh_frame: 0x130
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1790
+  __DATA_CONST.__const: 0x17b8
   __DATA_CONST.__objc_classlist: 0x358
   __DATA_CONST.__objc_catlist: 0xb0
   __DATA_CONST.__objc_protolist: 0xc0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x41d8
+  __DATA_CONST.__objc_selrefs: 0x4200
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x180
   __DATA_CONST.__objc_arraydata: 0x100
-  __DATA_CONST.__got: 0x910
+  __DATA_CONST.__got: 0x918
   __AUTH_CONST.__const: 0x11a8
-  __AUTH_CONST.__cfstring: 0x9580
+  __AUTH_CONST.__cfstring: 0x95e0
   __AUTH_CONST.__objc_const: 0x79b0
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH_CONST.__auth_got: 0xcb8
+  __AUTH_CONST.__auth_got: 0xd08
   __AUTH.__objc_data: 0xdf0
   __AUTH.__data: 0x178
   __DATA.__objc_ivar: 0x354

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2753
-  Symbols:   4480
-  CStrings:  1567
+  Functions: 2774
+  Symbols:   4502
+  CStrings:  1585
 
Symbols:
+ +[CalAttachmentUtils URL:isContainedInDirectory:]
+ +[CalAttachmentUtils isSymbolicLinkAtURL:]
+ GCC_except_table10
+ _BOMCopierCancelCopy
+ _BOMCopierSetCopyFileFinishedHandler
+ _BOMCopierSetCopyFileStartedHandler
+ _BOMCopierSetCopyFileUpdateHandler
+ _BOMCopierUserData
+ _UnzipArchiveWithLimits
+ __CalUnzipCopyFileFinished
+ __CalUnzipCopyFileStarted
+ __CalUnzipCopyFileUpdate
+ __CalUnzipEntryDestinationPath
+ __CalUnzipParentIsContained
+ __CalUnzipTrackTopLevelPath
+ ____CalUnzipRemoveEscapingSymlinks_block_invoke
+ ___block_descriptor_40_e8_32r_e27_B24?0"NSURL"8"NSError"16lr32l8
+ _lstat
+ _realpath$DARWIN_EXTSN
+ _strcmp
+ _strncmp
+ _unlink
CStrings:
+ ".."
+ "Archive contains a symlink pointing outside destination; removing it. entry = %@"
+ "Archive entry exceeds total size limit (%llu bytes); canceling extraction."
+ "Archive entry resolves outside destination; canceling extraction. entry = %s"
+ "Archive entry's parent directory escapes destination (likely via an earlier symlink entry); canceling extraction. entry = %s"
+ "Archive exceeds item count limit (%lu); canceling extraction."
+ "Archive exceeds total size limit (%llu bytes) while writing an entry; canceling extraction."
+ "Archive exceeds total size limit (%llu bytes); canceling extraction."
+ "B24@?0@\"NSURL\"8@\"NSError\"16"
+ "Could not lstat %@: %d"
+ "Could not resolve %@ or %@: %d"
+ "Could not resolve destination %@: %d; refusing to extract."
+ "Failed to enumerate extracted archive contents at %@: %@; treating as unsafe."
+ "Failed to remove debris left by a failed extraction at %@: %@"
+ "Failed to remove escaping symlink: %d"
+ "Refusing to remove %@: its parent directory is not contained in destination."
+ "enforceDestinationEncapsulation"
+ "enforceDestinationLocation"
```
