## CloudKeychainProxy

> `/System/Library/Frameworks/Security.framework/CloudKeychainProxy.bundle/CloudKeychainProxy`

```diff

-61439.82.1.0.0
-  __TEXT.__text: 0xd1d8
-  __TEXT.__auth_stubs: 0xca0
+61439.100.301.0.0
+  __TEXT.__text: 0xce64
+  __TEXT.__auth_stubs: 0xc20
   __TEXT.__objc_stubs: 0x1840
-  __TEXT.__objc_methlist: 0x9dc
+  __TEXT.__objc_methlist: 0xc1c
   __TEXT.__const: 0xfc
-  __TEXT.__cstring: 0x9b0
+  __TEXT.__dlopen_cstrs: 0x66
   __TEXT.__gcc_except_tab: 0x10c
   __TEXT.__objc_methname: 0x1ce6
+  __TEXT.__cstring: 0x903
   __TEXT.__oslogstring: 0xb89
   __TEXT.__objc_classname: 0x163
   __TEXT.__objc_methtype: 0x4cf
-  __TEXT.__dlopen_cstrs: 0x66
-  __TEXT.__unwind_info: 0x3f0
-  __DATA_CONST.__auth_got: 0x660
-  __DATA_CONST.__got: 0x1e8
+  __TEXT.__unwind_info: 0x3d8
+  __DATA_CONST.__auth_got: 0x620
+  __DATA_CONST.__got: 0x1d0
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x8e0
+  __DATA_CONST.__const: 0x848
   __DATA_CONST.__cfstring: 0x4e0
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x28
-  __DATA.__objc_const: 0x14e8
-  __DATA.__objc_selrefs: 0x7d0
+  __DATA.__objc_const: 0x10c0
+  __DATA.__objc_selrefs: 0x860
   __DATA.__objc_ivar: 0xac
   __DATA.__objc_data: 0x1e0
   __DATA.__data: 0x284
-  __DATA.__bss: 0x78
+  __DATA.__bss: 0x60
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/Security.framework/Security
+  - /System/Library/PrivateFrameworks/AppleKeyStore.framework/AppleKeyStore
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/SymptomDiagnosticReporter.framework/SymptomDiagnosticReporter
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 310
-  Symbols:   277
-  CStrings:  684
+  Functions: 304
+  Symbols:   266
+  CStrings:  677
 
Symbols:
+ _aks_get_lock_state
- _IOConnectCallMethod
- _IOObjectRelease
- _IORegistryEntryFromPath
- _IOServiceClose
- _IOServiceGetMatchingService
- _IOServiceMatching
- _IOServiceOpen
- ___stdoutp
- _fprintf
- _kIOMasterPortDefault
- _mach_task_self_
- _syslog
CStrings:
- "%s%s:%s%s%s%s%u:%s%u:%s aks connection failed%s\n"
- "AppleKeyStore"
- "IOService:/IOResources/AppleKeyStore"
- "aks"
- "aks-client-queue"
- "aks_get_lock_state"
- "failed to open connection to %s\n"

```
