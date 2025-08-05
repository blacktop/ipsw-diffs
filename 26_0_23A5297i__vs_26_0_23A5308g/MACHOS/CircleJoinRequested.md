## CircleJoinRequested

> `/System/Library/Frameworks/Security.framework/CircleJoinRequested/CircleJoinRequested`

```diff

-61901.0.56.0.1
-  __TEXT.__text: 0x58d8
-  __TEXT.__auth_stubs: 0x5e0
-  __TEXT.__objc_stubs: 0xa20
+61901.0.84.0.0
+  __TEXT.__text: 0x550c
+  __TEXT.__auth_stubs: 0x5a0
+  __TEXT.__objc_stubs: 0x9c0
   __TEXT.__objc_methlist: 0x1a0
-  __TEXT.__const: 0xb8
-  __TEXT.__dlopen_cstrs: 0x66
-  __TEXT.__gcc_except_tab: 0x2c
+  __TEXT.__const: 0xa8
   __TEXT.__objc_classname: 0x21
-  __TEXT.__objc_methname: 0x8f9
+  __TEXT.__objc_methname: 0x89f
   __TEXT.__objc_methtype: 0xf4
-  __TEXT.__cstring: 0x9c7
+  __TEXT.__cstring: 0x92e
   __TEXT.__oslogstring: 0xb0c
   __TEXT.__ustring: 0x424
-  __TEXT.__unwind_info: 0x110
-  __DATA_CONST.__auth_got: 0x300
-  __DATA_CONST.__got: 0x178
-  __DATA_CONST.__const: 0x358
-  __DATA_CONST.__cfstring: 0xa00
+  __TEXT.__unwind_info: 0xf8
+  __DATA_CONST.__auth_got: 0x2d8
+  __DATA_CONST.__got: 0x170
+  __DATA_CONST.__const: 0x310
+  __DATA_CONST.__cfstring: 0x9c0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA.__objc_const: 0x370
-  __DATA.__objc_selrefs: 0x2b0
+  __DATA.__objc_selrefs: 0x298
   __DATA.__objc_ivar: 0x24
   __DATA.__objc_data: 0xa0
-  __DATA.__data: 0xc
-  __DATA.__bss: 0x50
+  __DATA.__data: 0x8
+  __DATA.__bss: 0x39
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount
   - /System/Library/PrivateFrameworks/CloudServices.framework/CloudServices
   - /System/Library/PrivateFrameworks/CoreCDP.framework/CoreCDP
+  - /System/Library/PrivateFrameworks/CrashReporterSupport.framework/CrashReporterSupport
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/ProtectedCloudStorage.framework/ProtectedCloudStorage
-  - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C3794FD4-9928-34ED-91B0-3B8477E28E78
-  Functions: 64
-  Symbols:   151
-  CStrings:  389
+  UUID: 69720DF5-38E8-340A-BA96-39EAB49D31D2
+  Functions: 60
+  Symbols:   145
+  CStrings:  378
 
Symbols:
+ _SimulateCrash
- _OBJC_CLASS_$_NSAssertionHandler
- __Block_object_dispose
- __Unwind_Resume
- ___objc_personality_v0
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
- "stringWithUTF8String:"
- "void *CrashReporterSupportLibrary(void)"

```
