## AppleCVHWA

> `/System/Library/PrivateFrameworks/AppleCVHWA.framework/AppleCVHWA`

```diff

-4.4.10.0.0
-  __TEXT.__text: 0xb5a34
-  __TEXT.__const: 0x2ed0
-  __TEXT.__gcc_except_tab: 0x5560
+4.4.12.0.0
+  __TEXT.__text: 0xb5ea8
+  __TEXT.__const: 0x2f90
+  __TEXT.__gcc_except_tab: 0x555c
   __TEXT.__oslogstring: 0x3b9
-  __TEXT.__cstring: 0x9001
-  __TEXT.__unwind_info: 0x17a8
+  __TEXT.__cstring: 0x8ef8
+  __TEXT.__unwind_info: 0x17b8
   __TEXT.__eh_frame: 0x50
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__weak_got: 0x18
   __DATA_CONST.__objc_selrefs: 0x8
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x1558
+  __AUTH_CONST.__const: 0x15a8
   __AUTH_CONST.__cfstring: 0x220
   __AUTH_CONST.__weak_auth_got: 0x50
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH_CONST.__auth_got: 0x5e0
+  __AUTH_CONST.__auth_got: 0x5e8
   __AUTH.__data: 0x20
   __DATA.__data: 0x7f98
   __DATA.__crash_info: 0x148
   __DATA.__bss: 0x3c8
-  __DATA.__common: 0x20
+  __DATA.__common: 0x10
   __DATA_DIRTY.__data: 0x1e18
-  __DATA_DIRTY.__bss: 0x1b0
+  __DATA_DIRTY.__bss: 0x1d0
   __DATA_DIRTY.__common: 0x10
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1143
-  Symbols:   444
-  CStrings:  586
+  Functions: 1147
+  Symbols:   448
+  CStrings:  583
 
Symbols:
+ __ZNSt3__19to_stringEj
+ __xpc_error_connection_interrupted
+ __xpc_error_connection_invalid
+ __xpc_error_termination_imminent
CStrings:
+ " GPAPI Logger uses level "
+ " Logger uses level "
+ "AppleCVHWA version "
+ "CVPixelBufferGetBaseAddress(*buf) && \"NULL base address\""
- "(*counterpart_ptr != *dma_ptr) && \"Shouldn't be in this branch if dma_in_ptr_ == dma_out_ptr_\""
- "(base != buf) && \"Unnecessary memcpy, source == destination.\""
- "(needs_alloc || tracked_cvpb != nullptr) && \"No CVPixelBuffer backing available\""
- "AppleCVHWA GPAPI Logger uses level "
- "AppleCVHWA Logger uses level "
- "base_address && \"NULL pointer\""
- "needs_memcpy && \"needs_memcpy is false unexpectedly\""
```
