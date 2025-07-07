## TrialArchivingService

> `/System/Library/PrivateFrameworks/TrialServer.framework/XPCServices/TrialArchivingService.xpc/TrialArchivingService`

```diff

-466.0.0.0.0
-  __TEXT.__text: 0x6cf0
-  __TEXT.__auth_stubs: 0x820
+468.0.0.0.0
+  __TEXT.__text: 0x64d0
+  __TEXT.__auth_stubs: 0x7f0
+  __TEXT.__delay_stubs: 0xb0
+  __TEXT.__delay_helper: 0xa4
   __TEXT.__objc_stubs: 0xae0
   __TEXT.__objc_methlist: 0x358
   __TEXT.__const: 0xb8
-  __TEXT.__dlopen_cstrs: 0x4e
+  __TEXT.__oslogstring: 0x1368
+  __TEXT.__cstring: 0x5f1
   __TEXT.__objc_classname: 0xdf
-  __TEXT.__oslogstring: 0x1397
-  __TEXT.__cstring: 0x791
-  __TEXT.__objc_methname: 0xd84
   __TEXT.__objc_methtype: 0x44d
-  __TEXT.__gcc_except_tab: 0x524
-  __TEXT.__unwind_info: 0x170
-  __DATA_CONST.__auth_got: 0x420
+  __TEXT.__objc_methname: 0xd84
+  __TEXT.__gcc_except_tab: 0x49c
+  __TEXT.__unwind_info: 0x160
+  __DATA_CONST.__auth_got: 0x428
   __DATA_CONST.__got: 0xc8
-  __DATA_CONST.__const: 0x2b0
-  __DATA_CONST.__cfstring: 0x420
+  __DATA_CONST.__const: 0x250
+  __DATA_CONST.__cfstring: 0x3e0
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA.__objc_selrefs: 0x3a8
   __DATA.__objc_ivar: 0x8
   __DATA.__objc_data: 0x230
-  __DATA.__data: 0x180
-  __DATA.__bss: 0x38
+  __DATA.__data: 0x184
   __DATA.__common: 0x20
+  __DATA.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/PrivateFrameworks/Espresso.framework/Espresso
   - /System/Library/PrivateFrameworks/ProactiveSupport.framework/ProactiveSupport
-  - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/Trial.framework/Trial
   - /System/Library/PrivateFrameworks/TrialProto.framework/TrialProto
   - /usr/lib/libAppleArchive.dylib

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1C5EF8D1-B712-34F3-BA77-D69B9608AE25
-  Functions: 62
-  Symbols:   175
-  CStrings:  372
+  UUID: 9BDE772B-7F1B-3F00-9976-203A0D715B3A
+  Functions: 55
+  Symbols:   176
+  CStrings:  358
 
Symbols:
+ _dlopen
+ _espresso_ane_cache_has_network
+ _espresso_ane_cache_purge_network
+ _espresso_context_destroy
+ _espresso_create_context
- __sl_dlopen
- _dlerror
- _dlsym
- _free
CStrings:
+ "/System/Library/PrivateFrameworks/Espresso.framework/Espresso"
- "%s"
- "Skipping purge, Espresso runtime not available"
- "TrialArchivingService.m"
- "espresso_ane_cache_has_network"
- "espresso_ane_cache_purge_network"
- "espresso_context_destroy"
- "espresso_context_ref_t tri_espresso_create_context(espresso_engine_t, int)"
- "espresso_create_context"
- "espresso_return_status_t tri_espresso_ane_cache_has_network(const char *, int *)"
- "espresso_return_status_t tri_espresso_ane_cache_purge_network(const char *)"
- "espresso_return_status_t tri_espresso_context_destroy(espresso_context_ref_t)"
- "softlink:o:path:/System/Library/PrivateFrameworks/Espresso.framework/Espresso"
- "void *EspressoLibrary(void)"

```
