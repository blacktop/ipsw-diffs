## DiagnosticExtensions

> `/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/DiagnosticExtensions`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_intobj`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-147.0.0.0.0
-  __TEXT.__text: 0x17acc
+148.0.0.0.0
+  __TEXT.__text: 0x17dfc
   __TEXT.__objc_methlist: 0x121c
   __TEXT.__const: 0x13a
-  __TEXT.__oslogstring: 0x32b9
-  __TEXT.__cstring: 0x1256
-  __TEXT.__gcc_except_tab: 0x50c
-  __TEXT.__unwind_info: 0x6b0
+  __TEXT.__oslogstring: 0x3348
+  __TEXT.__cstring: 0x1248
+  __TEXT.__gcc_except_tab: 0x518
+  __TEXT.__unwind_info: 0x6b8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __AUTH_CONST.__objc_const: 0x27a0
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH_CONST.__auth_got: 0x590
+  __AUTH_CONST.__auth_got: 0x5a0
   __DATA.__objc_ivar: 0xd0
   __DATA.__data: 0x2a0
   __DATA.__bss: 0x20
   __DATA_DIRTY.__objc_data: 0x730
-  __DATA_DIRTY.__bss: 0xe8
+  __DATA_DIRTY.__bss: 0xe0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/Bom.framework/Bom

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  Functions: 591
-  Symbols:   1315
-  CStrings:  436
+  Functions: 594
+  Symbols:   1313
+  CStrings:  439
 
Symbols:
+ _NSURLIsSymbolicLinkKey
+ _archive_entry_set_symlink
+ _lstat
+ _readlink
- __dispatch_queue_attr_concurrent
- _extendedQueue
- _objc_msgSend$setAfterExtendedBlock:
- _objc_msgSend$setExtendedLoaded:
- _objc_msgSend$setInitialLoadQueue:
- _stat
Functions:
~ -[DEArchive addFile:withPathName:progressHandler:] : 1428 -> 1892
+ _OUTLINED_FUNCTION_0
~ +[DEArchiver archiveDirectoryAt:deleteOriginal:progressHandler:] : 1612 -> 1724
- _OUTLINED_FUNCTION_1
~ ___36+[DEExtensionManager sharedInstance]_block_invoke : 164 -> 60
~ -[DEExtensionManager init] : 56 -> 120
~ +[DEUtils pathComponentsInURL:removingBaseURLComponents:keepingFirstComponent:] : 256 -> 308
~ -[DEArchive addFile:withPathName:progressHandler:].cold.1 : 100 -> 92
~ -[DEArchive addFile:withPathName:progressHandler:].cold.2 : 112 -> 64
~ -[DEArchive addFile:withPathName:progressHandler:].cold.3 : 64 -> 92
+ -[DEArchive addFile:withPathName:progressHandler:].cold.4
+ -[DEArchive addFile:withPathName:progressHandler:].cold.6
+ -[DEArchive archiverForUrl:].cold.2
CStrings:
+ "Error [%@] getting NSURLIsSymbolicLinkKey for url [%@]"
+ "Error reading file"
+ "lstat failed for [%s]: %{errno}d"
+ "readlink failed for [%s]: %{errno}d"
- "extendedQueue"
```
