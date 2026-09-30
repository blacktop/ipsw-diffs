## inputanalyticsd

> `/usr/libexec/inputanalyticsd`

```diff

-64.104.0.0.0
-  __TEXT.__text: 0x42c
-  __TEXT.__auth_stubs: 0x150
+64.106.0.0.0
+  __TEXT.__text: 0x4a4
+  __TEXT.__auth_stubs: 0x190
+  __TEXT.__objc_stubs: 0x40
   __TEXT.__const: 0x50
-  __TEXT.__cstring: 0x59
+  __TEXT.__cstring: 0x7d
   __TEXT.__oslogstring: 0x101
+  __TEXT.__objc_methname: 0x15
   __TEXT.__unwind_info: 0x70
-  __DATA_CONST.__auth_got: 0xa8
-  __DATA_CONST.__got: 0x20
-  __DATA_CONST.__cfstring: 0x40
+  __DATA_CONST.__auth_got: 0xd0
+  __DATA_CONST.__got: 0x38
+  __DATA_CONST.__const: 0x40
+  __DATA_CONST.__cfstring: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA.__objc_selrefs: 0x10
   __DATA.__bss: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/InputAnalyticsServer.framework/InputAnalyticsServer
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 8
-  Symbols:   28
-  CStrings:  9
+  Functions: 9
+  Symbols:   37
+  CStrings:  13
 
Symbols:
+ _dispatch_resume
+ _objc_msgSend
+ __dispatch_main_q
+ _dispatch_source_create
+ _OBJC_CLASS_$_IAServerStats
+ __dispatch_source_type_signal
+ _signal
+ _dispatch_source_set_event_handler
+ __NSConcreteGlobalBlock
CStrings:
+ "logShutdown"
+ "logStart"
+ "inputanalyticsd shutting down"
+ "v8@?0"

```
