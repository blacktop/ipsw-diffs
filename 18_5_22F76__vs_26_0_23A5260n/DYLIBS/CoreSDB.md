## CoreSDB

> `/System/Library/PrivateFrameworks/CoreSDB.framework/CoreSDB`

```diff

-205.100.22.0.0
-  __TEXT.__text: 0xef98
-  __TEXT.__auth_stubs: 0xbf0
-  __TEXT.__objc_methlist: 0xe8
+209.100.1.0.0
+  __TEXT.__text: 0xeca4
+  __TEXT.__auth_stubs: 0xb90
+  __TEXT.__objc_methlist: 0xec
   __TEXT.__const: 0x128
-  __TEXT.__cstring: 0x1454
-  __TEXT.__gcc_except_tab: 0x8c4
-  __TEXT.__oslogstring: 0x15b6
-  __TEXT.__unwind_info: 0x568
+  __TEXT.__cstring: 0x131f
+  __TEXT.__gcc_except_tab: 0x868
+  __TEXT.__oslogstring: 0x159a
+  __TEXT.__unwind_info: 0x558
   __TEXT.__objc_classname: 0x2a
   __TEXT.__objc_methname: 0x51a
-  __TEXT.__objc_methtype: 0x29e
+  __TEXT.__objc_methtype: 0x292
   __TEXT.__objc_stubs: 0x540
-  __DATA_CONST.__got: 0xa8
+  __DATA_CONST.__got: 0x98
   __DATA_CONST.__const: 0x130
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x170
+  __DATA_CONST.__objc_selrefs: 0x160
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x608
+  __AUTH_CONST.__auth_got: 0x5d8
   __AUTH_CONST.__const: 0x1a8
-  __AUTH_CONST.__cfstring: 0xc80
-  __AUTH_CONST.__objc_const: 0x2b0
-  __DATA.__objc_ivar: 0x30
+  __AUTH_CONST.__cfstring: 0xb20
+  __AUTH_CONST.__objc_const: 0x2c0
+  __DATA.__objc_ivar: 0x2c
   __DATA.__data: 0x40
   __DATA.__bss: 0x34
   __DATA_DIRTY.__objc_data: 0xa0
   __DATA_DIRTY.__data: 0x84
-  __DATA_DIRTY.__bss: 0x4c
+  __DATA_DIRTY.__bss: 0x54
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/IMFoundation.framework/IMFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 1329B78E-4F8F-3F97-9775-BBF3D3755947
-  Functions: 356
-  Symbols:   431
-  CStrings:  480
+  UUID: E6E9176B-FF8B-39D0-9E4A-A38BBA98CF98
+  Functions: 358
+  Symbols:   424
+  CStrings:  456
 
Symbols:
+ _CFAllocatorAllocateTyped
+ _CSDBThreadedRecordStoreGetQueue
+ _OBJC_CLASS_$_IMRGLog
+ __os_log_error_impl
- _CFAllocatorAllocate
- _CFRunLoopAddSource
- _CFRunLoopGetCurrent
- _CFRunLoopRun
- _CFRunLoopSourceCreate
- _OBJC_CLASS_$_NSRunLoop
- _OBJC_CLASS_$_NSThread
- __IMAlwaysLog
- __IMWillLog
- _kCFRunLoopDefaultMode
- _objc_retain
CStrings:
+ "T@\"NSObject<OS_dispatch_queue>\",R,N"
+ "queue"
+ "warning"
- "@\"NSThread\""
- "Free page count: %lld"
- "Initializing database on thread: %@"
- "Initializing database."
- "Load factor: %f"
- "Max Free Pages: %lld"
- "Not doing incremental vacuum we are either a) above a load factor of 0.85 or the free list is less than max free."
- "Page count: %lld"
- "Pages in use: %lld"
- "Starting up database thread"
- "Using DB path %@"
- "_threadedMain"
- "currentRunLoop"
- "currentThread"
- "thread"

```
