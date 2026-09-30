## CloudKeychainProxy

> `/System/Library/Frameworks/Security.framework/CloudKeychainProxy.bundle/CloudKeychainProxy`

```diff

-61901.0.56.0.1
-  __TEXT.__text: 0xce5c
-  __TEXT.__auth_stubs: 0xc20
+61901.0.84.0.0
+  __TEXT.__text: 0xcb70
+  __TEXT.__auth_stubs: 0xc10
   __TEXT.__objc_stubs: 0x1840
   __TEXT.__objc_methlist: 0xc1c
-  __TEXT.__const: 0x104
-  __TEXT.__dlopen_cstrs: 0x66
-  __TEXT.__gcc_except_tab: 0x10c
-  __TEXT.__objc_methname: 0x1ce6
-  __TEXT.__cstring: 0x903
-  __TEXT.__oslogstring: 0xb89
+  __TEXT.__const: 0xfc
+  __TEXT.__gcc_except_tab: 0xfc
+  __TEXT.__objc_methname: 0x1ccc
+  __TEXT.__cstring: 0x947
+  __TEXT.__oslogstring: 0xbaf
   __TEXT.__objc_classname: 0x163
   __TEXT.__objc_methtype: 0x4cf
-  __TEXT.__unwind_info: 0x3d8
-  __DATA_CONST.__auth_got: 0x620
+  __TEXT.__unwind_info: 0x3c0
+  __DATA_CONST.__auth_got: 0x618
   __DATA_CONST.__got: 0x1d0
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x848
-  __DATA_CONST.__cfstring: 0x4e0
+  __DATA_CONST.__const: 0x800
+  __DATA_CONST.__cfstring: 0x500
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x30

   __DATA.__objc_selrefs: 0x860
   __DATA.__objc_ivar: 0xac
   __DATA.__objc_data: 0x1e0
-  __DATA.__data: 0x284
-  __DATA.__bss: 0x60
+  __DATA.__data: 0x280
+  __DATA.__bss: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/PrivateFrameworks/AppleKeyStore.framework/AppleKeyStore
+  - /System/Library/PrivateFrameworks/CrashReporterSupport.framework/CrashReporterSupport
+  - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/SymptomDiagnosticReporter.framework/SymptomDiagnosticReporter
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: DA1A5528-0589-3F25-A846-692BD0C15D17
-  Functions: 304
-  Symbols:   266
-  CStrings:  710
+  UUID: 2DB23954-7D59-32C2-AC41-53A0D964921B
+  Functions: 300
+  Symbols:   265
+  CStrings:  709
 
Symbols:
+ _OBJC_CLASS_$_SecTapToRadar
+ _SecIsInternalRelease
+ _SimulateCrash
- _OBJC_CLASS_$_NSAssertionHandler
- __sl_dlopen
- _dlerror
- _dlsym
CStrings:
+ "153038246"
+ "Please TTR! CloudKeychainProxy is attempting to synchronize with syncdefaultsd however syncdefaultsd has not responded within 60 seconds of issuing the request."
+ "fresh: failed to synchronize with KVS"
+ "initTapToRadar:description:radar:"
+ "syncdefaultsd failed to respond within 60 seconds"
+ "trigger"
- "%s"
- "BOOL soft_SimulateCrash(pid_t, mach_exception_data_type_t, NSString *__strong)"
- "SimulateCrash"
- "currentHandler"
- "handleFailureInFunction:file:lineNumber:description:"
- "simulate_crash.m"
- "softlink:o:path:/System/Library/PrivateFrameworks/CrashReporterSupport.framework/CrashReporterSupport"
- "void *CrashReporterSupportLibrary(void)"

```
