## XPCAcmeService

> `/System/Library/Frameworks/Security.framework/XPCServices/XPCAcmeService.xpc/XPCAcmeService`

```diff

-61901.0.56.0.1
-  __TEXT.__text: 0x3be0
-  __TEXT.__auth_stubs: 0x9e0
-  __TEXT.__objc_stubs: 0x400
+61901.0.84.0.0
+  __TEXT.__text: 0x3838
+  __TEXT.__auth_stubs: 0x9c0
+  __TEXT.__objc_stubs: 0x3c0
   __TEXT.__objc_methlist: 0x8c
   __TEXT.__const: 0xcc
-  __TEXT.__dlopen_cstrs: 0x66
-  __TEXT.__gcc_except_tab: 0xec
-  __TEXT.__cstring: 0x3ef
-  __TEXT.__objc_methname: 0x31f
-  __TEXT.__objc_classname: 0x10
+  __TEXT.__gcc_except_tab: 0xb4
+  __TEXT.__cstring: 0x356
+  __TEXT.__objc_methname: 0x2db
+  __TEXT.__objc_classname: 0xf
   __TEXT.__objc_methtype: 0x65
   __TEXT.__oslogstring: 0x95
-  __TEXT.__unwind_info: 0x160
-  __DATA_CONST.__auth_got: 0x500
-  __DATA_CONST.__got: 0x100
+  __TEXT.__unwind_info: 0x150
+  __DATA_CONST.__auth_got: 0x4f0
+  __DATA_CONST.__got: 0xf8
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x268
-  __DATA_CONST.__cfstring: 0x2e0
+  __DATA_CONST.__const: 0x220
+  __DATA_CONST.__cfstring: 0x2a0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA.__objc_const: 0x130
-  __DATA.__objc_selrefs: 0x130
+  __DATA.__objc_selrefs: 0x120
   __DATA.__objc_ivar: 0xc
   __DATA.__objc_data: 0x50
-  __DATA.__data: 0x44
-  __DATA.__bss: 0x48
+  __DATA.__data: 0x40
+  __DATA.__bss: 0x38
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/Security.framework/Security
-  - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
+  - /System/Library/PrivateFrameworks/CrashReporterSupport.framework/CrashReporterSupport
+  - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6E4FF7BC-F3FC-3EEC-8F35-D58B5617B9D9
-  Functions: 65
-  Symbols:   203
-  CStrings:  137
+  UUID: BD5F0193-B861-343B-BA7A-33B8CB1F00D7
+  Functions: 61
+  Symbols:   200
+  CStrings:  127
 
Symbols:
+ _SimulateCrash
- _OBJC_CLASS_$_NSAssertionHandler
- __sl_dlopen
- _dlerror
- _dlsym
CStrings:
- "%s"
- "BOOL soft_SimulateCrash(pid_t, mach_exception_data_type_t, NSString *__strong)"
- "SimulateCrash"
- "currentHandler"
- "handleFailureInFunction:file:lineNumber:description:"
- "simulate_crash.m"
- "softlink:o:path:/System/Library/PrivateFrameworks/CrashReporterSupport.framework/CrashReporterSupport"
- "void *CrashReporterSupportLibrary(void)"

```
