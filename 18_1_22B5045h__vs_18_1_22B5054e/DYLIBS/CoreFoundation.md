## CoreFoundation

> `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation`

```diff

-3103.0.0.0.0
-  __TEXT.__text: 0x1b8834
+3105.0.0.0.0
+  __TEXT.__text: 0x1b89f4
   __TEXT.__auth_stubs: 0x3160
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0x76cc
   __TEXT.__const: 0x18c150
-  __TEXT.__oslogstring: 0x57e7
-  __TEXT.__cstring: 0x14ad81
+  __TEXT.__oslogstring: 0x570c
+  __TEXT.__cstring: 0x14ab9b
   __TEXT.__gcc_except_tab: 0x4468
   __TEXT.__ustring: 0x484
   __TEXT.__dof_CFRunLoop: 0x964
   __TEXT.__dof_Cocoa_Aut: 0x486
-  __TEXT.__unwind_info: 0x5cf4
+  __TEXT.__unwind_info: 0x5cec
   __TEXT.__eh_frame: 0x59c
   __TEXT.__objc_classname: 0xa7c
   __TEXT.__objc_methname: 0x7eb2

   __DATA_CONST.__got: 0x380
   __DATA_CONST.__objc_arraydata: 0x1520
   __AUTH_CONST.__const_cfobj2: 0x40
-  __AUTH_CONST.__const: 0x4878
-  __AUTH_CONST.__cfstring: 0x140d80
+  __AUTH_CONST.__const: 0x4818
+  __AUTH_CONST.__cfstring: 0x140d20
   __AUTH_CONST.__objc_const: 0x3a88
   __AUTH_CONST.__auth_ptr: 0x1e8
   __AUTH_CONST.__objc_dictobj: 0x7f8

   __AUTH.__objc_data: 0xa00
   __AUTH.__data: 0x58
   __DATA.__objc_ivar: 0x4f8
-  __DATA.__data: 0xaf0
+  __DATA.__data: 0xac0
   __DATA.__thread_vars: 0x18
   __DATA.__cf_except_bt: 0x2000
   __DATA.__cf_except_pack: 0x410

   __DATA_DIRTY.__objc_data: 0x21c0
   __DATA_DIRTY.__data: 0x138
   __DATA_DIRTY.__got: 0x8
-  __DATA_DIRTY.__bss: 0xe40
+  __DATA_DIRTY.__bss: 0xe60
   __DATA_DIRTY.__common: 0x380
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/CoreServicesInternal.framework/CoreServicesInternal
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 7593
-  Symbols:   9331
-  CStrings:  56693
+  Functions: 7589
+  Symbols:   9327
+  CStrings:  56689
 
CStrings:
+ "Attempting to use the main runloop, but the main thread has exited. This message will only log once."
- "Attempting to perform block on main runloop, but the main thread has exited. This message will only log once. Break on _CFRunLoopError_MainThreadHasExited to debug."
- "Attempting to add source to main runloop, but the main thread has exited. This message will only log once. Break on _CFRunLoopError_MainThreadHasExited to debug."
- "Attempting to add observer to main runloop, but the main thread has exited. This message will only log once. Break on _CFRunLoopError_MainThreadHasExited to debug."
- "Attempting to wake up main runloop, but the main thread as exited. This message will only log once. Break on _CFRunLoopError_MainThreadHasExited to debug."
- "Attempting to add timer to main runloop, but the main thread as exited. This message will only log once. Break on _CFRunLoopError_MainThreadHasExited to debug."

```
