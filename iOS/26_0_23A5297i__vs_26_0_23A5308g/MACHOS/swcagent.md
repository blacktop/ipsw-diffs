## swcagent

> `/System/Library/Frameworks/Security.framework/swcagent`

```diff

-61901.0.56.0.1
-  __TEXT.__text: 0x55a0
-  __TEXT.__auth_stubs: 0x9a0
-  __TEXT.__objc_stubs: 0x320
+61901.0.84.0.0
+  __TEXT.__text: 0x51f0
+  __TEXT.__auth_stubs: 0x980
+  __TEXT.__objc_stubs: 0x2e0
   __TEXT.__objc_methlist: 0x8c
-  __TEXT.__const: 0xf4
-  __TEXT.__dlopen_cstrs: 0x66
-  __TEXT.__gcc_except_tab: 0x2c
-  __TEXT.__cstring: 0x980
-  __TEXT.__objc_classname: 0xa
-  __TEXT.__objc_methname: 0x26b
+  __TEXT.__const: 0xe4
+  __TEXT.__cstring: 0x8e7
+  __TEXT.__objc_classname: 0x9
+  __TEXT.__objc_methname: 0x227
   __TEXT.__objc_methtype: 0x48
   __TEXT.__oslogstring: 0x1a5
-  __TEXT.__unwind_info: 0x148
-  __DATA_CONST.__auth_got: 0x4e0
-  __DATA_CONST.__got: 0xf8
+  __TEXT.__unwind_info: 0x130
+  __DATA_CONST.__auth_got: 0x4c8
+  __DATA_CONST.__got: 0xf0
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x300
-  __DATA_CONST.__cfstring: 0x940
+  __DATA_CONST.__const: 0x2b8
+  __DATA_CONST.__cfstring: 0x900
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0x190
-  __DATA.__objc_selrefs: 0xd8
+  __DATA.__objc_selrefs: 0xc8
   __DATA.__objc_ivar: 0x14
   __DATA.__objc_data: 0x50
-  __DATA.__data: 0x44
-  __DATA.__bss: 0x88
+  __DATA.__data: 0x40
+  __DATA.__bss: 0x78
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
+  - /System/Library/PrivateFrameworks/CrashReporterSupport.framework/CrashReporterSupport
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
-  - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
+  - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 122AB7E6-7289-3CA4-83F6-A804DDB3AA75
-  Functions: 75
-  Symbols:   195
-  CStrings:  242
+  UUID: 9E54DD9A-9930-3AA1-B166-9904D02A38DC
+  Functions: 71
+  Symbols:   191
+  CStrings:  232
 
Symbols:
+ _SimulateCrash
- _OBJC_CLASS_$_NSAssertionHandler
- __Unwind_Resume
- ___objc_personality_v0
- __sl_dlopen
- _dlerror
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
