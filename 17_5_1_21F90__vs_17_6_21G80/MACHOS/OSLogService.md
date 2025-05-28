## OSLogService

> `/System/Library/Frameworks/OSLog.framework/XPCServices/OSLogService.xpc/OSLogService`

```diff

-1510.122.1.0.0
-  __TEXT.__text: 0xc38
-  __TEXT.__auth_stubs: 0x300
-  __TEXT.__objc_stubs: 0x3c0
-  __TEXT.__objc_methlist: 0x8c
+1510.140.4.0.0
+  __TEXT.__text: 0x10c0
+  __TEXT.__auth_stubs: 0x380
+  __TEXT.__objc_stubs: 0x400
+  __TEXT.__objc_methlist: 0xa4
   __TEXT.__const: 0x50
-  __TEXT.__gcc_except_tab: 0xac
-  __TEXT.__objc_methname: 0x4fe
-  __TEXT.__cstring: 0xf1
+  __TEXT.__gcc_except_tab: 0xcc
+  __TEXT.__objc_methname: 0x550
+  __TEXT.__cstring: 0x13d
   __TEXT.__oslogstring: 0x8a
   __TEXT.__objc_classname: 0x53
-  __TEXT.__objc_methtype: 0x1d5
-  __TEXT.__unwind_info: 0x9c
-  __DATA_CONST.__auth_got: 0x190
+  __TEXT.__objc_methtype: 0x200
+  __TEXT.__unwind_info: 0xc8
+  __DATA_CONST.__auth_got: 0x1d0
   __DATA_CONST.__got: 0x30
-  __DATA_CONST.__const: 0xa0
+  __DATA_CONST.__const: 0x140
   __DATA_CONST.__cfstring: 0x60
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x18

   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_classrefs: 0x68
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA.__objc_const: 0x608
-  __DATA.__objc_selrefs: 0x128
-  __DATA.__objc_ivar: 0x1c
+  __DATA.__objc_const: 0x628
+  __DATA.__objc_selrefs: 0x138
+  __DATA.__objc_ivar: 0x20
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0x120
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 17
-  Symbols:   73
-  CStrings:  120
+  Functions: 24
+  Symbols:   81
+  CStrings:  127
 
Symbols:
+ _dispatch_assert_queue$V2
+ _dispatch_queue_attr_make_with_autorelease_frequency
+ _dispatch_queue_create
+ _dispatch_sync
+ _objc_autoreleaseReturnValue
+ _objc_release_x1
+ _objc_retain
+ _objc_retain_x21
CStrings:
+ "\x05"
+ "@\"NSObject<OS_dispatch_queue>\""
+ "@24@0:8@?16"
+ "_queue_getNextOSLogEntryWithReply:"
+ "_queue_setupWithPredicate:reply:"
+ "_serial_queue"
+ "com.apple.OSLogService.OSLogEventStream"
+ "com.apple.OSLogService.serial_queue"
- "\x04"

```
