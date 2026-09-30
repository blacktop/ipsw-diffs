## securityuploadd

> `/usr/libexec/securityuploadd`

```diff

-61901.0.56.0.1
-  __TEXT.__text: 0x138d8
-  __TEXT.__auth_stubs: 0xe80
-  __TEXT.__objc_stubs: 0x1de0
+61901.0.84.0.0
+  __TEXT.__text: 0x13500
+  __TEXT.__auth_stubs: 0xe60
+  __TEXT.__objc_stubs: 0x1d80
   __TEXT.__objc_methlist: 0x8f8
   __TEXT.__const: 0x2d0
-  __TEXT.__cstring: 0x11b6
-  __TEXT.__objc_methname: 0x232a
+  __TEXT.__cstring: 0x1119
+  __TEXT.__objc_methname: 0x22d0
   __TEXT.__constg_swiftt: 0x1a0
   __TEXT.__swift5_typeref: 0x18f
   __TEXT.__swift5_reflstr: 0xa2

   __TEXT.__swift5_capture: 0xf0
   __TEXT.__swift5_proto: 0x10
   __TEXT.__swift5_types: 0xc
-  __TEXT.__dlopen_cstrs: 0x66
-  __TEXT.__gcc_except_tab: 0x38c
-  __TEXT.__objc_classname: 0xd7
+  __TEXT.__gcc_except_tab: 0x348
+  __TEXT.__objc_classname: 0xd6
   __TEXT.__objc_methtype: 0x55d
-  __TEXT.__unwind_info: 0x440
+  __TEXT.__unwind_info: 0x430
   __TEXT.__eh_frame: 0x178
-  __DATA_CONST.__auth_got: 0x750
-  __DATA_CONST.__got: 0x318
+  __DATA_CONST.__auth_got: 0x740
+  __DATA_CONST.__got: 0x310
   __DATA_CONST.__auth_ptr: 0xe0
-  __DATA_CONST.__const: 0xc68
-  __DATA_CONST.__cfstring: 0x1500
+  __DATA_CONST.__const: 0xc20
+  __DATA_CONST.__cfstring: 0x14c0
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x28

   __DATA_CONST.__objc_superrefs: 0x18
   __DATA_CONST.__objc_intobj: 0x30
   __DATA.__objc_const: 0xe40
-  __DATA.__objc_selrefs: 0xa38
+  __DATA.__objc_selrefs: 0xa20
   __DATA.__objc_ivar: 0x6c
   __DATA.__objc_data: 0x330
-  __DATA.__data: 0x4a4
-  __DATA.__bss: 0x2a8
+  __DATA.__data: 0x4a0
+  __DATA.__bss: 0x298
   __DATA.__common: 0x68
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount
   - /System/Library/PrivateFrameworks/AuthKit.framework/AuthKit
   - /System/Library/PrivateFrameworks/CrashReporterSupport.framework/CrashReporterSupport
+  - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/OSAnalytics.framework/OSAnalytics
-  - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 786928C2-9297-3CE9-A201-C62F7A2C0535
-  Functions: 335
-  Symbols:   381
-  CStrings:  953
+  UUID: D40384CB-D1DB-3D69-ACC0-1096B4557615
+  Functions: 331
+  Symbols:   378
+  CStrings:  942
 
Symbols:
+ _SimulateCrash
- _OBJC_CLASS_$_NSAssertionHandler
- __sl_dlopen
- _dlerror
- _dlsym
CStrings:
+ "61901.0.84"
- "%s"
- "61901.0.56.0.1"
- "BOOL soft_SimulateCrash(pid_t, mach_exception_data_type_t, NSString *__strong)"
- "SimulateCrash"
- "currentHandler"
- "handleFailureInFunction:file:lineNumber:description:"
- "simulate_crash.m"
- "softlink:o:path:/System/Library/PrivateFrameworks/CrashReporterSupport.framework/CrashReporterSupport"
- "stringWithUTF8String:"
- "void *CrashReporterSupportLibrary(void)"

```
