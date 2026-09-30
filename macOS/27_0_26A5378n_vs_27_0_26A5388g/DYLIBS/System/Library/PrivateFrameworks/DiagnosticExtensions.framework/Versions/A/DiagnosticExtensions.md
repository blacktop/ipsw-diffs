## DiagnosticExtensions

> `/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/Versions/A/DiagnosticExtensions`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
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
-  __TEXT.__text: 0x2a51c
+148.0.0.0.0
+  __TEXT.__text: 0x2aa10
   __TEXT.__objc_methlist: 0x121c
   __TEXT.__const: 0x66
-  __TEXT.__oslogstring: 0x327a
-  __TEXT.__cstring: 0x13ce
+  __TEXT.__oslogstring: 0x3309
+  __TEXT.__cstring: 0x13c0
   __TEXT.__gcc_except_tab: 0x734
   __TEXT.__unwind_info: 0x588
   __TEXT.__objc_stubs: 0x0

   __AUTH_CONST.__objc_const: 0x27a0
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH_CONST.__auth_got: 0x490
+  __AUTH_CONST.__auth_got: 0x4a0
   __DATA.__objc_ivar: 0xd0
   __DATA.__data: 0x2a0
-  __DATA.__bss: 0x28
+  __DATA.__bss: 0x20
   __DATA_DIRTY.__objc_data: 0x730
-  __DATA_DIRTY.__bss: 0xe8
+  __DATA_DIRTY.__bss: 0xe0
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/PrivateFrameworks/Bom.framework/Versions/A/Bom

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   Functions: 482
-  Symbols:   1384
-  CStrings:  447
+  Symbols:   1381
+  CStrings:  450
 
Symbols:
+ _NSURLIsSymbolicLinkKey
+ _archive_entry_set_symlink
+ _lstat
+ _readlink
- __dispatch_queue_attr_concurrent
- _extendedQueue
- _initialLoadQueue
- _objc_msgSend$setAfterExtendedBlock:
- _objc_msgSend$setExtendedLoaded:
- _objc_msgSend$setInitialLoadQueue:
- _stat
Functions:
~ -[DEArchive addFile:withPathName:progressHandler:] : 2800 -> 3888
~ +[DEArchiver archiveDirectoryAt:deleteOriginal:progressHandler:] : 3168 -> 3336
~ ___36+[DEExtensionManager sharedInstance]_block_invoke : 236 -> 80
~ -[DEExtensionManager init] : 168 -> 244
~ +[DEUtils pathComponentsInURL:removingBaseURLComponents:keepingFirstComponent:] : 840 -> 932
CStrings:
+ "Error [%@] getting NSURLIsSymbolicLinkKey for url [%@]"
+ "Error reading file"
+ "lstat failed for [%s]: %{errno}d"
+ "readlink failed for [%s]: %{errno}d"
- "extendedQueue"
```
