## shared_cache_page_prewarming

> `/System/Library/PrivateFrameworks/shared_cache_page_prewarming.framework/shared_cache_page_prewarming`

```diff

-9.1.0.0.0
-  __TEXT.__text: 0xa99c
+9.3.0.0.0
+  __TEXT.__text: 0xa9a0
   __TEXT.__auth_stubs: 0x470
-  __TEXT.__const: 0x2ed0
-  __TEXT.__gcc_except_tab: 0x428
+  __TEXT.__const: 0x2ec0
+  __TEXT.__gcc_except_tab: 0x41c
   __TEXT.__cstring: 0x7fe
-  __TEXT.__oslogstring: 0x246
+  __TEXT.__oslogstring: 0x22a
   __TEXT.__unwind_info: 0x370
   __TEXT.__objc_methname: 0x61
   __TEXT.__objc_stubs: 0xe0

   __DATA_CONST.__objc_selrefs: 0x38
   __AUTH_CONST.__auth_got: 0x248
   __AUTH_CONST.__cfstring: 0x40
+  __DATA.__data: 0x1
   __DATA.__bss: 0x4e0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 176
-  Symbols:   256
-  CStrings:  91
+  Functions: 178
+  Symbols:   258
+  CStrings:  92
 
CStrings:
+ "User default not set, enabling prewarming"
+ "User default set to 0, disabling prewarming"
+ "User default set to 1, enabling prewarming"
- "Executed 'defaults read %@ %@' and recieved value: %d (previously %d)"
- "Executed 'defaults read %@ %@' and recieved value: nil, enabling prewarming by default"

```
