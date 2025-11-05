## CloudKeychainProxy

> `/System/Library/Frameworks/Security.framework/Versions/A/Resources/CloudKeychainProxy.bundle/Contents/MacOS/CloudKeychainProxy`

```diff

-61439.81.1.0.0
-  __TEXT.__text: 0xe430
-  __TEXT.__auth_stubs: 0xb00
+61439.101.1.0.0
+  __TEXT.__text: 0xe0d8
+  __TEXT.__auth_stubs: 0xa80
   __TEXT.__objc_stubs: 0x1840
-  __TEXT.__objc_methlist: 0x9dc
+  __TEXT.__objc_methlist: 0xc1c
   __TEXT.__const: 0x10c
-  __TEXT.__cstring: 0xa33
+  __TEXT.__dlopen_cstrs: 0x66
   __TEXT.__gcc_except_tab: 0x10c
   __TEXT.__objc_methname: 0x1ce6
+  __TEXT.__cstring: 0x986
   __TEXT.__oslogstring: 0xbaf
   __TEXT.__objc_classname: 0x163
   __TEXT.__objc_methtype: 0x4cf
-  __TEXT.__dlopen_cstrs: 0x66
-  __TEXT.__unwind_info: 0x410
-  __DATA_CONST.__auth_got: 0x590
-  __DATA_CONST.__got: 0x1e8
+  __TEXT.__unwind_info: 0x3f8
+  __DATA_CONST.__auth_got: 0x550
+  __DATA_CONST.__got: 0x1d0
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0xa28
+  __DATA_CONST.__const: 0x990
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
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/Security.framework/Versions/A/Security
+  - /System/Library/PrivateFrameworks/AppleKeyStore.framework/Versions/A/AppleKeyStore
   - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking
   - /System/Library/PrivateFrameworks/SymptomDiagnosticReporter.framework/Versions/A/SymptomDiagnosticReporter
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 406FE78E-9C0C-3013-BA54-62BEE31D0DF2
-  Functions: 334
-  Symbols:   251
-  CStrings:  720
+  UUID: 05089FAB-B3C7-33DE-A873-480442DE955E
+  Functions: 328
+  Symbols:   240
+  CStrings:  713
 
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
- _syslog$DARWIN_EXTSN
CStrings:
- "%s%s:%s%s%s%s%u:%s%u:%s aks connection failed%s\n"
- "AppleKeyStore"
- "IOService:/IOResources/AppleKeyStore"
- "aks"
- "aks-client-queue"
- "aks_get_lock_state"
- "failed to open connection to %s\n"

```
