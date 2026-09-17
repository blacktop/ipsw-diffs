## MMCSServices

> `/System/Library/PrivateFrameworks/MMCSServices.framework/Versions/A/MMCSServices`

```diff

-1491.100.1.1.11
-  __TEXT.__text: 0x87dc
-  __TEXT.__objc_methlist: 0x548
-  __TEXT.__const: 0xd0
-  __TEXT.__gcc_except_tab: 0x980
-  __TEXT.__cstring: 0x23f
-  __TEXT.__oslogstring: 0x1178
-  __TEXT.__unwind_info: 0x3e0
+1491.200.63.0.0
+  __TEXT.__text: 0x8d4c
+  __TEXT.__objc_methlist: 0x578
+  __TEXT.__const: 0xd8
+  __TEXT.__gcc_except_tab: 0x9e8
+  __TEXT.__cstring: 0x24d
+  __TEXT.__oslogstring: 0x1254
+  __TEXT.__unwind_info: 0x410
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__const: 0xc0
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x538
+  __DATA_CONST.__objc_selrefs: 0x558
   __DATA_CONST.__objc_superrefs: 0x28
-  __DATA_CONST.__got: 0x170
-  __AUTH_CONST.__const: 0x390
+  __DATA_CONST.__got: 0x180
+  __AUTH_CONST.__const: 0x3c0
   __AUTH_CONST.__cfstring: 0x380
-  __AUTH_CONST.__objc_const: 0xa50
+  __AUTH_CONST.__objc_const: 0xab0
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0x98
+  __DATA.__objc_ivar: 0xa0
   __DATA_DIRTY.__objc_data: 0x190
   __DATA_DIRTY.__bss: 0x30
   - /System/Library/Frameworks/CFNetwork.framework/Versions/A/CFNetwork

   - /System/Library/PrivateFrameworks/Marco.framework/Versions/A/Marco
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 178
-  Symbols:   133
-  CStrings:  130
+  Functions: 185
+  Symbols:   141
+  CStrings:  134
 
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
- _objc_loadWeak
CStrings:
+ "Clearing power assertion, we have %d transfers (%@)"
+ "Could not create power assertion timer, assertion will be held until transfers complete"
+ "Extending power assertion timer by %f seconds"
+ "Power Assertion Timer invalidated"
+ "[%@: guid: %@  item id: %qx  path: %@  fd: %d token: %@   requestor ID: %@  request url: %@ signature: %@  progress: %f file size: %llu priority: %ld]"
- "[%@: guid: %@  item id: %qx  path: %@  fd: %d token: %@   requestor ID: %@  request url: %@ signature: %@  progress: %f file size: %llu]"
```
