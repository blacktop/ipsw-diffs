## MMCSServices

> `/System/Library/PrivateFrameworks/MMCSServices.framework/MMCSServices`

```diff

-1491.100.1.2.25
-  __TEXT.__text: 0x8510
-  __TEXT.__objc_methlist: 0x548
+1491.200.63.2.1
+  __TEXT.__text: 0x8808
+  __TEXT.__objc_methlist: 0x578
   __TEXT.__const: 0xd0
-  __TEXT.__gcc_except_tab: 0xa14
-  __TEXT.__cstring: 0x281
-  __TEXT.__oslogstring: 0x126a
-  __TEXT.__unwind_info: 0x3b8
+  __TEXT.__gcc_except_tab: 0xa1c
+  __TEXT.__cstring: 0x28f
+  __TEXT.__oslogstring: 0x12c2
+  __TEXT.__unwind_info: 0x3c0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x3b8
+  __DATA_CONST.__const: 0x3e0
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x568
+  __DATA_CONST.__objc_selrefs: 0x578
   __DATA_CONST.__objc_superrefs: 0x28
-  __DATA_CONST.__got: 0x1b0
+  __DATA_CONST.__got: 0x1b8
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x3e0
-  __AUTH_CONST.__objc_const: 0xa50
+  __AUTH_CONST.__objc_const: 0xab0
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0x98
+  __DATA.__objc_ivar: 0xa0
   __DATA_DIRTY.__objc_data: 0x190
   __DATA_DIRTY.__bss: 0x30
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /System/Library/PrivateFrameworks/Marco.framework/Marco
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 154
-  Symbols:   151
-  CStrings:  138
+  Functions: 159
+  Symbols:   159
+  CStrings:  139
 
Symbols:
+ __dispatch_source_type_timer
+ _dispatch_activate
+ _dispatch_source_cancel
+ _dispatch_source_create
+ _dispatch_source_set_event_handler
+ _dispatch_source_set_timer
+ _dispatch_time
+ _kMMCSRequestOptionPriority
+ _objc_loadWeakRetained
+ _objc_release
- _OBJC_CLASS_$_NSTimer
- _objc_loadWeak
CStrings:
+ "Could not create power assertion timer, assertion will be held until transfers complete"
+ "[%@: guid: %@  item id: %qx  path: %@  fd: %d token: %@   requestor ID: %@  request url: %@ signature: %@  progress: %f file size: %llu priority: %ld]"
- "[%@: guid: %@  item id: %qx  path: %@  fd: %d token: %@   requestor ID: %@  request url: %@ signature: %@  progress: %f file size: %llu]"
```
