## lskdd

> `/usr/libexec/lskdd`

```diff

 0.0.0.0.0
-  __TEXT.__text: 0x11d81d0
+  __TEXT.__text: 0x11f2274
   __TEXT.__auth_stubs: 0x200
   __TEXT.__objc_stubs: 0x380
   __TEXT.__objc_methlist: 0xb0
   __TEXT.__cstring: 0xea
-  __TEXT.__const: 0x3e7750
+  __TEXT.__const: 0x3e7ab0
   __TEXT.__gcc_except_tab: 0x30
   __TEXT.__objc_methname: 0x345
   __TEXT.__objc_classname: 0x1b
   __TEXT.__objc_methtype: 0x97
-  __TEXT.__unwind_info: 0xb38
-  __TEXT.__eh_frame: 0x2300
+  __TEXT.__unwind_info: 0xb40
+  __TEXT.__eh_frame: 0x23c8
   __DATA_CONST.__auth_got: 0x110
   __DATA_CONST.__got: 0x58
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x468e0
+  __DATA_CONST.__const: 0x47ef0
   __DATA_CONST.__cfstring: 0xc0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA.__objc_selrefs: 0x100
   __DATA.__objc_ivar: 0xc
   __DATA.__objc_data: 0x50
-  __DATA.__data: 0x2360
-  __DATA.__bss: 0x48
-  __DATA.__common: 0x17c8
+  __DATA.__data: 0x2538
+  __DATA.__bss: 0x40
+  __DATA.__common: 0x17b0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices
+  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/MobileActivation.framework/MobileActivation
   - /System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 489
-  Symbols:   158
+  Functions: 488
+  Symbols:   163
   CStrings:  65
 
Symbols:
+ _analytics_send_event_lazy
+ _xpc_dictionary_create_empty
+ _xpc_dictionary_set_data
+ _xpc_dictionary_set_string
+ _xpc_dictionary_set_uint64

```
