## libRPAC.dylib

> `/usr/lib/libRPAC.dylib`

```diff

-84.0.0.0.0
-  __TEXT.__text: 0x9245c
-  __TEXT.__auth_stubs: 0xad0
+88.0.0.0.0
+  __TEXT.__text: 0x92424
+  __TEXT.__auth_stubs: 0xac0
   __TEXT.__objc_stubs: 0x1a0
   __TEXT.__init_offsets: 0x4
-  __TEXT.__cstring: 0x5190
+  __TEXT.__cstring: 0x5140
   __TEXT.__gcc_except_tab: 0x5c
   __TEXT.__const: 0x1d58
   __TEXT.__objc_methname: 0x13b
   __TEXT.__oslogstring: 0x1d
   __TEXT.__objc_classname: 0x1
-  __TEXT.__unwind_info: 0x320
-  __DATA_CONST.__auth_got: 0x580
-  __DATA_CONST.__got: 0x148
+  __TEXT.__unwind_info: 0x330
+  __DATA_CONST.__auth_got: 0x578
+  __DATA_CONST.__got: 0x140
   __DATA_CONST.__auth_ptr: 0x10
   __DATA_CONST.__const: 0x3f0
   __DATA_CONST.__cfstring: 0x260
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_arraydata: 0x20
   __DATA_CONST.__objc_arrayobj: 0x30
-  __AUTH_CONST.__interpose: 0x230
+  __AUTH_CONST.__interpose: 0x220
   __DATA.__objc_selrefs: 0x88
-  __DATA.__data: 0x7c8
+  __DATA.__data: 0x7c4
   __DATA.__common: 0x800e8
-  __DATA.__bss: 0x5809e0
+  __DATA.__bss: 0x5807d8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/ImageIO.framework/ImageIO

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 277
-  Symbols:   732
-  CStrings:  635
+  Functions: 279
+  Symbols:   730
+  CStrings:  633
 
Symbols:
+ _lockLockInDispatchLockMap
+ _lockLockInNSCondtionLockMap
+ _unlockLockInDispatchLockMap
+ _unlockLockInNSConditionLockMap
- __ZL18max_primitive_maps
- __interpose_dlsym
- _dlsym
- _interposed_dlsym
- deletePrimitiveEntry.cold.1
- interposed_dlsym.dlsym_count
CStrings:
+ "Inversion detection for %s\n"
+ "SemaphoreWaitingAGPCLogType"
+ "semaphorewaitingagpclogtype"
- "DispatchSemaphoreWaitingOnMainThreadAGPCLogType"
- "deletePrimitiveEntry"
- "dispatchsemaphorewaitingonmainthreadagpclogtype"
- "dlsym"
- "libRPAC.dylib: interposed_dlsym invoked\n"

```
