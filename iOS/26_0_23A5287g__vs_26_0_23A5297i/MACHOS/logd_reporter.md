## logd_reporter

> `/usr/libexec/logd_reporter`

```diff

-1815.0.7.0.0
-  __TEXT.__text: 0x3d84
-  __TEXT.__auth_stubs: 0x500
+1815.0.12.0.0
+  __TEXT.__text: 0x3ec0
+  __TEXT.__auth_stubs: 0x520
   __TEXT.__objc_stubs: 0xc00
   __TEXT.__objc_methlist: 0x118
   __TEXT.__const: 0xa8
   __TEXT.__objc_methname: 0xa82
-  __TEXT.__oslogstring: 0x5ff
+  __TEXT.__oslogstring: 0x633
   __TEXT.__cstring: 0x509
   __TEXT.__objc_classname: 0x21
   __TEXT.__objc_methtype: 0xd5
   __TEXT.__unwind_info: 0xe0
-  __DATA_CONST.__auth_got: 0x288
+  __DATA_CONST.__auth_got: 0x298
   __DATA_CONST.__got: 0xa8
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x1e8
+  __DATA_CONST.__const: 0x208
   __DATA_CONST.__cfstring: 0x700
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA.__objc_selrefs: 0x330
   __DATA.__objc_ivar: 0x48
   __DATA.__objc_data: 0xa0
-  __DATA.__bss: 0x48
+  __DATA.__bss: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics

   - /System/Library/PrivateFrameworks/LoggingSupport.framework/LoggingSupport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3B478BD2-181E-3B32-8D71-7D93662597F2
-  Functions: 47
-  Symbols:   111
-  CStrings:  312
+  UUID: 2DE1643D-FF2D-3079-85A6-81C64290CD6A
+  Functions: 48
+  Symbols:   113
+  CStrings:  314
 
Symbols:
+ _dispatch_activate
+ _dispatch_source_set_cancel_handler
+ _objc_release_x9
+ _objc_retain_x24
- _dispatch_resume
- _objc_retain_x27
Functions:
~ sub_100002764 : 5424 -> 5576
+ sub_100004bd4
CStrings:
+ "Defer timer cancelled"
+ "Failed to create defer timer."

```
