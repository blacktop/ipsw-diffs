## shared_cache_page_prewarming

> `/System/Library/PrivateFrameworks/shared_cache_page_prewarming.framework/shared_cache_page_prewarming`

```diff

-8.2.0.0.0
-  __TEXT.__text: 0xa62c
-  __TEXT.__auth_stubs: 0x4d0
+9.1.0.0.0
+  __TEXT.__text: 0xa99c
+  __TEXT.__auth_stubs: 0x470
   __TEXT.__const: 0x2ed0
-  __TEXT.__gcc_except_tab: 0x4b4
-  __TEXT.__cstring: 0x7b6
-  __TEXT.__oslogstring: 0x16f
-  __TEXT.__unwind_info: 0x360
-  __TEXT.__objc_methname: 0x8f
-  __TEXT.__objc_stubs: 0x120
-  __DATA_CONST.__got: 0x38
+  __TEXT.__gcc_except_tab: 0x428
+  __TEXT.__cstring: 0x7fe
+  __TEXT.__oslogstring: 0x246
+  __TEXT.__unwind_info: 0x370
+  __TEXT.__objc_methname: 0x61
+  __TEXT.__objc_stubs: 0xe0
+  __DATA_CONST.__got: 0x40
+  __DATA_CONST.__const: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x48
-  __AUTH_CONST.__auth_got: 0x278
-  __AUTH_CONST.__cfstring: 0x60
-  __DATA.__data: 0x1
-  __DATA.__bss: 0x471
+  __DATA_CONST.__objc_selrefs: 0x38
+  __AUTH_CONST.__auth_got: 0x248
+  __AUTH_CONST.__cfstring: 0x40
+  __DATA.__bss: 0x4e0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 168
-  Symbols:   253
-  CStrings:  87
+  Functions: 176
+  Symbols:   256
+  CStrings:  91
 
Symbols:
+ _OBJC_CLASS_$_NSProcessInfo
+ __dispatch_queue_attr_concurrent
+ __os_log_debug_impl
+ _dispatch_apply_f
+ _memcmp
+ _memcpy
- _OBJC_CLASS_$_RBSDomainAttribute
- _objc_enumerationMutation
- _objc_opt_class
- _objc_opt_isKindOfClass
- _objc_release_x22
- _objc_release_x23
- _objc_release_x24
- _objc_release_x25
- _objc_retain_x19
- _objc_retain_x20
- _objc_retain_x23
CStrings:
+ "(null)"
+ "Error: Failed to create parallel dispatch queue."
+ "Error: Failed to create serial dispatch queue."
+ "Executed 'defaults read %@ %@' and recieved value: nil, enabling prewarming by default"
+ "PerfBoard"
+ "Prewarming disabled due to prior error. Check earlier logs for reason"
+ "Prewarming for launch of %{public}s"
+ "Process %{public}s is not eligible for prewarming."
+ "SpringBoard"
+ "com.apple.shared_cache_page_prewarming_concurrent_queue"
+ "prewarming_enable_2"
+ "processInfo"
+ "processName"
- "Failed to create serial dispatch queue."
- "Prewarming for launch of %s"
- "Prewarming short circuted. Check earlier logs for reason"
- "attributes"
- "com.apple.dasd"
- "countByEnumeratingWithState:objects:count:"
- "domain"
- "isEqual:"
- "prewarming_enable"

```
