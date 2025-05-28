## libusd_ms.dylib

> `/usr/lib/usd/libusd_ms.dylib`

```diff

-21.1.17.0.0
-  __TEXT.__text: 0xaee828
-  __TEXT.__auth_stubs: 0x4f80
-  __TEXT.__gcc_except_tab: 0xe3030
+21.2.4.0.0
+  __TEXT.__text: 0xaeed24
+  __TEXT.__auth_stubs: 0x4f90
+  __TEXT.__gcc_except_tab: 0xe3064
   __TEXT.__const: 0x12c683
-  __TEXT.__cstring: 0xf7062
-  __TEXT.__oslogstring: 0x3
-  __TEXT.__unwind_info: 0x4ccf0
+  __TEXT.__cstring: 0xf70e2
+  __TEXT.__oslogstring: 0x7b
+  __TEXT.__unwind_info: 0x4cd14
   __TEXT.__eh_frame: 0x38
   __TEXT.__objc_methname: 0x180
   __TEXT.__objc_stubs: 0x220
   __DATA_CONST.__got: 0x268
-  __DATA_CONST.__const: 0x830
+  __DATA_CONST.__const: 0x870
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x88
-  __AUTH_CONST.__const: 0x41910
+  __AUTH_CONST.__const: 0x41950
   __AUTH_CONST.__auth_ptr: 0x90
   __AUTH_CONST.__objc_intobj: 0x1f8
   __AUTH_CONST.__cfstring: 0x40
-  __AUTH_CONST.__auth_got: 0xc58
+  __AUTH_CONST.__auth_got: 0xc60
   __AUTH.__data: 0x20
   __AUTH.__const_weak: 0xe270
   __AUTH.pxrctor: 0x40

   __DATA.__data: 0x3840
   __DATA.__thread_vars: 0x258
   __DATA.__thread_bss: 0x44120
-  __DATA.__bss: 0x20c928
-  __DATA.__common: 0x6e0
+  __DATA.__bss: 0x20c948
+  __DATA.__common: 0x6e8
   __DATA_DIRTY.__tf_func: 0x0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 55257
-  Symbols:   20475
-  CStrings:  12262
+  Functions: 55261
+  Symbols:   20477
+  CStrings:  12269
 
Symbols:
+ __ZN38pxrInternal_v0_22__aapl__pxrReserved__19__usdlibInitFailureE
+ __os_log_error_impl
CStrings:
+ "13:40:50)"
+ "Could not find expected prefix:\"anon:%%p\" in anonymous layer identifier."
+ "Sep 30 2023"
+ "TBB Global TLS count is not == 1, instead it is: %d"
+ "TBB failed to acquire key from pthread_key_create. Error Code: %d\n "
+ "anon:%p"
+ "com.apple.usdlib"
+ "tbbgovernor"
+ "tbbmain"
+ "vertex index out of range index: %d numFaceIndices: %d"
- "02:55:41)"
- "Aug  6 2023"
- "TBB failed to initialize task scheduler TLS\n"

```
