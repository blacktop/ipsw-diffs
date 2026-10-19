## EventKit

> `/System/Library/Frameworks/EventKit.framework/EventKit`

```diff

 1976.2.2.0.0
-  __TEXT.__text: 0x199730
-  __TEXT.__objc_methlist: 0x15bcc
+  __TEXT.__text: 0x199d6c
+  __TEXT.__objc_methlist: 0x15bfc
   __TEXT.__cstring: 0xbdbf
   __TEXT.__const: 0x4870
-  __TEXT.__oslogstring: 0xf234
-  __TEXT.__gcc_except_tab: 0x3950
+  __TEXT.__oslogstring: 0xf294
+  __TEXT.__gcc_except_tab: 0x397c
   __TEXT.__dlopen_cstrs: 0x400
   __TEXT.__ustring: 0x1a0
   __TEXT.__swift5_typeref: 0x1988

   __TEXT.__swift_as_ret: 0xec
   __TEXT.__swift_as_cont: 0x1a8
   __TEXT.__swift5_mpenum: 0x60
-  __TEXT.__unwind_info: 0x83b8
+  __TEXT.__unwind_info: 0x83e8
   __TEXT.__eh_frame: 0x261c
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0xa0
   __DATA_CONST.__objc_protolist: 0x258
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xaef8
+  __DATA_CONST.__objc_selrefs: 0xaf28
   __DATA_CONST.__objc_protorefs: 0x70
   __DATA_CONST.__objc_superrefs: 0x538
   __DATA_CONST.__objc_arraydata: 0x5d8
-  __DATA_CONST.__got: 0x1a50
-  __AUTH_CONST.__const: 0x4500
+  __DATA_CONST.__got: 0x1a58
+  __AUTH_CONST.__const: 0x4520
   __AUTH_CONST.__cfstring: 0x9ec0
-  __AUTH_CONST.__objc_const: 0x187c8
+  __AUTH_CONST.__objc_const: 0x187d8
   __AUTH_CONST.__objc_intobj: 0x6d8
   __AUTH_CONST.__objc_arrayobj: 0x1f8
   __AUTH_CONST.__objc_dictobj: 0x1b8
   __AUTH_CONST.__objc_doubleobj: 0x100
-  __AUTH_CONST.__auth_got: 0x1430
+  __AUTH_CONST.__auth_got: 0x1438
   __AUTH.__objc_data: 0x1db8
   __AUTH.__data: 0x610
   __DATA.__objc_ivar: 0xd88

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 10709
-  Symbols:   13291
-  CStrings:  2673
+  Functions: 10717
+  Symbols:   13300
+  CStrings:  2675
 
Symbols:
+ +[EKAttachment _expandedArchiveTemporaryDirectoryRootForURL:]
+ +[EKAttachment _volumeIdentifierForURL:]
+ -[EKAttachment _mirroredTemporaryURLForExpandedArchiveContentsOfArchiveAtURL:]
+ -[EKAttachment localURLExpandingArchiveIfNeeded]
+ _NSURLVolumeIdentifierKey
+ _UnzipArchive
+ ___61+[EKAttachment _expandedArchiveTemporaryDirectoryRootForURL:]_block_invoke
+ __expandedArchiveTemporaryDirectoryRootForURL:.cachedRootsByVolume
+ __expandedArchiveTemporaryDirectoryRootForURL:.onceToken
CStrings:
+ "Unable to determine volume identifier for %@: %@"
+ "Unable to expand attachment archive %@"
```
