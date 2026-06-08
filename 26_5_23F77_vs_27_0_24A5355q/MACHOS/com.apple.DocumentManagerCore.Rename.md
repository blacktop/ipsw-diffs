## com.apple.DocumentManagerCore.Rename

> `/System/Library/PrivateFrameworks/DocumentManagerCore.framework/XPCServices/com.apple.DocumentManagerCore.Rename.xpc/com.apple.DocumentManagerCore.Rename`

```diff

-367.5.1.0.0
-  __TEXT.__text: 0x9d4
-  __TEXT.__auth_stubs: 0x170
-  __TEXT.__objc_stubs: 0x220
-  __TEXT.__objc_methlist: 0x178
+389.2.0.0.0
+  __TEXT.__text: 0xb00
+  __TEXT.__auth_stubs: 0x190
+  __TEXT.__objc_stubs: 0x280
+  __TEXT.__objc_methlist: 0x188
   __TEXT.__const: 0x80
   __TEXT.__objc_classname: 0x53
-  __TEXT.__objc_methname: 0x39c
+  __TEXT.__objc_methname: 0x3c7
   __TEXT.__objc_methtype: 0x1b5
-  __TEXT.__oslogstring: 0x13a
+  __TEXT.__oslogstring: 0x1bc
   __TEXT.__cstring: 0x85
-  __TEXT.__unwind_info: 0x88
-  __DATA_CONST.__auth_got: 0xc0
-  __DATA_CONST.__got: 0x50
+  __TEXT.__unwind_info: 0x90
   __DATA_CONST.__const: 0x28
   __DATA_CONST.__cfstring: 0x20
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
+  __DATA_CONST.__objc_superrefs: 0x8
+  __DATA_CONST.__auth_got: 0xd0
+  __DATA_CONST.__got: 0x50
   __DATA.__objc_const: 0x2b0
-  __DATA.__objc_selrefs: 0x140
+  __DATA.__objc_selrefs: 0x160
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0x120
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/DocumentManagerExecutables.framework/DocumentManagerExecutables
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: CC860087-2C3F-3AAC-8627-40BA94933BF1
-  Functions: 14
-  Symbols:   47
-  CStrings:  78
+  UUID: D0478C57-EA71-3997-90CF-55B3A3526D8B
+  Functions: 15
+  Symbols:   49
+  CStrings:  85
 
Symbols:
+ _OBJC_CLASS_$_DOCNodeStartupManager
+ __os_log_impl
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSendSuper2
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x8
- ___stack_chk_fail
- ___stack_chk_guard
- _objc_release
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x22
- _objc_retain_x23
CStrings:
+ "[Rename] RenameService.init"
+ "[Rename] importDocumentAtURL failed with error: %@"
+ "[Rename] renameDocumentAtURL failed with error: %@"
+ "doc_xpcSafeError"
+ "init"
+ "shared"
+ "startIfNeeded"

```
