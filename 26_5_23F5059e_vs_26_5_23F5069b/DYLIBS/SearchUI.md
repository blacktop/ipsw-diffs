## SearchUI

> `/System/Library/PrivateFrameworks/SearchUI.framework/SearchUI`

```diff

-634.4.7.0.0
-  __TEXT.__text: 0xfc690
+634.5.1.0.0
+  __TEXT.__text: 0xfcb00
   __TEXT.__auth_stubs: 0x2e40
-  __TEXT.__objc_methlist: 0x121e0
+  __TEXT.__objc_methlist: 0x12200
   __TEXT.__const: 0x3754
   __TEXT.__cstring: 0x38d8
-  __TEXT.__oslogstring: 0x272f
+  __TEXT.__oslogstring: 0x277f
   __TEXT.__gcc_except_tab: 0x9d8
   __TEXT.__ustring: 0x9c
   __TEXT.__dlopen_cstrs: 0x160

   __TEXT.__swift_as_ret: 0x110
   __TEXT.__swift5_protos: 0x24
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x4f50
+  __TEXT.__unwind_info: 0x4f68
   __TEXT.__eh_frame: 0x21e4
   __TEXT.__objc_classname: 0x36c7
-  __TEXT.__objc_methname: 0x2ad41
+  __TEXT.__objc_methname: 0x2ada1
   __TEXT.__objc_methtype: 0x7df8
-  __TEXT.__objc_stubs: 0x21140
-  __DATA_CONST.__got: 0x24a0
+  __TEXT.__objc_stubs: 0x211e0
+  __DATA_CONST.__got: 0x24c0
   __DATA_CONST.__const: 0x2868
   __DATA_CONST.__objc_classlist: 0xad0
   __DATA_CONST.__objc_catlist: 0x408
   __DATA_CONST.__objc_protolist: 0x368
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9f98
+  __DATA_CONST.__objc_selrefs: 0x9fc0
   __DATA_CONST.__objc_protorefs: 0x68
   __DATA_CONST.__objc_superrefs: 0x6f0
   __DATA_CONST.__objc_arraydata: 0x38

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: DBCCA658-0207-3FD2-A14F-7610334A5AB2
-  Functions: 6857
-  Symbols:   21310
-  CStrings:  9153
+  UUID: 63194CAC-364E-312A-8877-AADD3B9EA3CD
+  Functions: 6862
+  Symbols:   21332
+  CStrings:  9160
 
Symbols:
+ +[SearchUIShareItemHandler isSymlinkForURL:]
+ +[SearchUIShareItemHandler isSymlinkForURL:].cold.1
+ -[SearchUIShareItemHandler showFailAlertForURL:]
+ _NSCocoaErrorDomain
+ _NSFilePathErrorKey
+ _NSURLIsSymbolicLinkKey
+ _OBJC_CLASS_$_NSError
+ __OBJC_$_CLASS_METHODS_SearchUIShareItemHandler
+ ___48-[SearchUIShareItemHandler showFailAlertForURL:]_block_invoke
+ ___68-[SearchUIShareItemHandler performCommand:triggerEvent:environment:]_block_invoke.cold.2
+ _objc_msgSend$errorWithDomain:code:userInfo:
+ _objc_msgSend$getResourceValue:forKey:error:
+ _objc_msgSend$isSymlinkForURL:
+ _objc_msgSend$path
+ _objc_msgSend$showFailAlertForURL:
CStrings:
+ "Failed to check if URL is symlink %@: %@"
+ "Prevented sharing of symlink: %@"
+ "errorWithDomain:code:userInfo:"
+ "getResourceValue:forKey:error:"
+ "isSymlinkForURL:"
+ "path"
+ "showFailAlertForURL:"

```
