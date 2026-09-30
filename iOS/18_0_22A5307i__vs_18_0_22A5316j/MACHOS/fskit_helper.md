## fskit_helper

> `/usr/libexec/fskit_helper`

```diff

-437.0.0.0.1
-  __TEXT.__text: 0x10b8
-  __TEXT.__auth_stubs: 0x290
-  __TEXT.__objc_stubs: 0x220
-  __TEXT.__objc_methlist: 0x44
-  __TEXT.__cstring: 0xce
+445.0.0.0.0
+  __TEXT.__text: 0x192c
+  __TEXT.__auth_stubs: 0x320
+  __TEXT.__objc_stubs: 0x320
+  __TEXT.__objc_methlist: 0x5c
+  __TEXT.__cstring: 0x1ba
   __TEXT.__objc_classname: 0x53
-  __TEXT.__objc_methname: 0x31a
-  __TEXT.__objc_methtype: 0x20e
-  __TEXT.__oslogstring: 0x291
-  __TEXT.__const: 0x48
-  __TEXT.__gcc_except_tab: 0xbc
-  __TEXT.__unwind_info: 0x98
-  __DATA_CONST.__auth_got: 0x158
-  __DATA_CONST.__got: 0x38
-  __DATA_CONST.__const: 0x28
-  __DATA_CONST.__cfstring: 0x40
+  __TEXT.__objc_methname: 0x39f
+  __TEXT.__objc_methtype: 0x219
+  __TEXT.__oslogstring: 0x3c3
+  __TEXT.__gcc_except_tab: 0x104
+  __TEXT.__const: 0x50
+  __TEXT.__unwind_info: 0xd8
+  __DATA_CONST.__auth_got: 0x1a0
+  __DATA_CONST.__got: 0x48
+  __DATA_CONST.__const: 0xa0
+  __DATA_CONST.__cfstring: 0x60
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA.__objc_const: 0x518
-  __DATA.__objc_selrefs: 0xa8
+  __DATA.__objc_selrefs: 0xe8
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0x120
+  __DATA.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/FSKit.framework/FSKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  Functions: 24
-  Symbols:   56
-  CStrings:  97
+  Functions: 34
+  Symbols:   67
+  CStrings:  115
 
Symbols:
+ _OBJC_CLASS_$_NSMutableDictionary
+ _OBJC_CLASS_$_NSString
+ _dispatch_queue_create
+ _dispatch_sync
+ _objc_autoreleaseReturnValue
+ _objc_release_x8
+ _objc_release_x9
+ _objc_retain_x19
+ _objc_retain_x24
+ _objc_retain_x25
+ _objc_retain_x8
+ _objc_sync_enter
+ _objc_sync_exit
- _objc_release_x26
- _objc_release_x27
CStrings:
+ "%!s(MISSING):reply(EBADF): BSD name (%!@(MISSING)) resource was revoked already, can't wipeFS"
+ "%!s(MISSING):reply(EBADF): Can't find queue for BSD name (%!@(MISSING)), resource was revoked already, can't wipeFS"
+ "%!s(MISSING):reply(EINVAL): Can't find queue for BSD name (%!@(MISSING)), resouce wasn't opened or was revoked already"
+ "%!s(MISSING):start:resource(%!p(MISSING)):resourceID(%!@(MISSING))"
+ "-[FSKitHelper revoke:replyHandler:]_block_invoke"
+ "-[FSKitHelper wipeFS:includingRanges:excludingRanges:replyHandler:]"
+ "-[FSKitHelper wipeFS:includingRanges:excludingRanges:replyHandler:]_block_invoke"
+ "@24@0:8@16"
+ "bsdName"
+ "com.apple.fskit_helper.queue.%!@(MISSING)"
+ "createQueue:"
+ "getResourceID"
+ "getResourceQueue:"
+ "objectForKeyedSubscript:"
+ "revoked"
+ "setObject:forKeyedSubscript:"
+ "stringWithFormat:"
+ "v8@?0"

```
