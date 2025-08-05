## trustd

> `/usr/libexec/trustd`

```diff

-61901.0.56.0.1
-  __TEXT.__text: 0x5f998
-  __TEXT.__auth_stubs: 0x23e0
-  __TEXT.__objc_stubs: 0x2d40
+61901.0.84.0.0
+  __TEXT.__text: 0x5f498
+  __TEXT.__auth_stubs: 0x23c0
+  __TEXT.__objc_stubs: 0x2d00
   __TEXT.__objc_methlist: 0xc0c
   __TEXT.__const: 0x59a1
-  __TEXT.__dlopen_cstrs: 0x66
-  __TEXT.__gcc_except_tab: 0xcfc
-  __TEXT.__cstring: 0x67c1
+  __TEXT.__gcc_except_tab: 0xd48
+  __TEXT.__cstring: 0x674b
   __TEXT.__oslogstring: 0x5a8e
   __TEXT.__objc_classname: 0x194
-  __TEXT.__objc_methname: 0x2ccd
+  __TEXT.__objc_methname: 0x2c89
   __TEXT.__objc_methtype: 0xae6
-  __TEXT.__unwind_info: 0x10b0
-  __DATA_CONST.__auth_got: 0x1200
-  __DATA_CONST.__got: 0x798
+  __TEXT.__unwind_info: 0x1088
+  __DATA_CONST.__auth_got: 0x11f0
+  __DATA_CONST.__got: 0x790
   __DATA_CONST.__auth_ptr: 0x18
   __DATA_CONST.__const: 0x4a38
-  __DATA_CONST.__cfstring: 0x5e40
+  __DATA_CONST.__cfstring: 0x5e20
   __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x28

   __DATA_CONST.__objc_arraydata: 0x40
   __DATA_CONST.__objc_arrayobj: 0x48
   __DATA.__objc_const: 0x1450
-  __DATA.__objc_selrefs: 0xd20
+  __DATA.__objc_selrefs: 0xd10
   __DATA.__objc_ivar: 0xb4
   __DATA.__objc_data: 0x460
-  __DATA.__data: 0x3b0
-  __DATA.__bss: 0x500
+  __DATA.__data: 0x3a8
+  __DATA.__bss: 0x4f0
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/Network.framework/Network
   - /System/Library/Frameworks/Security.framework/Security
+  - /System/Library/PrivateFrameworks/CrashReporterSupport.framework/CrashReporterSupport
   - /System/Library/PrivateFrameworks/MSUDataAccessor.framework/MSUDataAccessor
   - /System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset
+  - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: C6A99D3B-7C8A-3694-8FFE-31EAAB0162F7
-  Functions: 1255
-  Symbols:   833
-  CStrings:  2923
+  UUID: C67E5449-23AB-34A3-AD87-65EAE9C6004B
+  Functions: 1245
+  Symbols:   830
+  CStrings:  2916
 
Symbols:
+ _CFRunLoopRun
+ _SimulateCrash
- _OBJC_CLASS_$_NSAssertionHandler
- __sl_dlopen
- _dispatch_main
- _dlerror
- _dlsym
CStrings:
+ "com.apple.trustd.initialization"
- "BOOL soft_SimulateCrash(pid_t, mach_exception_data_type_t, NSString *__strong)"
- "SimulateCrash"
- "currentHandler"
- "handleFailureInFunction:file:lineNumber:description:"
- "simulate_crash.m"
- "softlink:o:path:/System/Library/PrivateFrameworks/CrashReporterSupport.framework/CrashReporterSupport"
- "void *CrashReporterSupportLibrary(void)"

```
