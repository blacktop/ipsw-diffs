## Diagnostic-8268

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8268.appex/Diagnostic-8268`

```diff

-645.40.12.0.0
-  __TEXT.__text: 0xb5c
-  __TEXT.__auth_stubs: 0x1a0
-  __TEXT.__objc_stubs: 0x220
-  __TEXT.__objc_methlist: 0xbc
-  __TEXT.__const: 0x20
-  __TEXT.__cstring: 0x170
-  __TEXT.__oslogstring: 0xbb
+645.40.18.0.0
+  __TEXT.__text: 0x293c
+  __TEXT.__auth_stubs: 0x250
+  __TEXT.__objc_stubs: 0x300
+  __TEXT.__objc_methlist: 0x10c
+  __TEXT.__const: 0x38
+  __TEXT.__cstring: 0x31e
+  __TEXT.__oslogstring: 0x2c0
   __TEXT.__objc_classname: 0x3c
-  __TEXT.__objc_methname: 0x437
-  __TEXT.__objc_methtype: 0x11b
-  __TEXT.__unwind_info: 0x88
-  __DATA_CONST.__auth_got: 0xd8
-  __DATA_CONST.__got: 0x30
-  __DATA_CONST.__cfstring: 0x1c0
+  __TEXT.__objc_methname: 0x57a
+  __TEXT.__objc_methtype: 0x13e
+  __TEXT.__unwind_info: 0xb0
+  __DATA_CONST.__auth_got: 0x130
+  __DATA_CONST.__got: 0x60
+  __DATA_CONST.__const: 0x80
+  __DATA_CONST.__cfstring: 0x280
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_intobj: 0x30
-  __DATA.__objc_const: 0x5e0
-  __DATA.__objc_selrefs: 0xd8
-  __DATA.__objc_ivar: 0x14
+  __DATA.__objc_const: 0x670
+  __DATA.__objc_selrefs: 0x128
+  __DATA.__objc_ivar: 0x20
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0xc0
+  __DATA.__bss: 0x18
+  __DATA.__common: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/CoreRepairCore.framework/CoreRepairCore
   - /System/Library/PrivateFrameworks/DiagnosticsKit.framework/DiagnosticsKit
   - /usr/lib/libFDR.dylib

   - /usr/lib/libamsupport.dylib
   - /usr/lib/libauthinstall.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 15
-  Symbols:   46
-  CStrings:  121
+  Functions: 35
+  Symbols:   64
+  CStrings:  176
 
Symbols:
+ _mach_task_self_
+ ___kCFBooleanTrue
+ _os_log_create
+ _IOConnectCallStructMethod
+ __os_log_default
+ _OBJC_CLASS_$_NSMutableDictionary
+ __NSConcreteGlobalBlock
+ _IOServiceGetMatchingService
+ ___kCFBooleanFalse
+ _IOServiceOpen
+ _free
+ _dispatch_once
+ _IOServiceMatching
+ _IOServiceClose
+ _memmove
+ _IOObjectRelease
+ _kIOMasterPortDefault
+ _malloc_type_malloc
CStrings:
+ "_trustObjectURL"
+ "err == 0 "
+ "setPhysicalPresence control:%!d(MISSING) state:%!p(MISSING)\n"
+ "AMFDR options: %!@(MISSING)"
+ "mesaPhysicalPresenceAsserted"
+ "AppleBiometricServices"
+ "service"
+ "v8@?0"
+ "Library-MesaFactory"
+ "i16@0:8"
+ "setObject:forKeyedSubscript:"
+ "/Library/Caches/com.apple.xbs/Sources/Mesa/AppleBiometricServices/MesaFactoryC/MesaFactoryC.c"
+ "FDR DS URL: %!@(MISSING)"
+ "v32@0:8@16^B24"
+ "T@\"NSString\",R,N,V_FDRDSURL"
+ "getSensorType -> %!{(MISSING)errno}d %!d(MISSING)\n"
+ "control < kMesaFactoryPhysicalPresenceCount"
+ "FDRDSURL"
+ "@\"NSString\""
+ "getSensorType %!p(MISSING)\n"
+ "FDR Trust Object URL: %!@(MISSING)"
+ "_FDRDSURL"
+ "Get PhysicalPresenceAsserted failed: 0x%!x(MISSING)\n"
+ "createFDROptions"
+ "CAURL"
+ "Mesa sensor type: 0x%!x(MISSING)"
+ "URL: %!@(MISSING) is invalid"
+ "cmd"
+ "control != kMesaFactoryPhysicalPresenceGetState || state"
+ "size == sizeof(sensorInfo)"
+ "VerifyData"
+ "dictionary"
+ "mesaProtocolVersion"
+ "com.apple.BiometricKit"
+ "StripImg4"
+ "Couldn't create OS Log for 'com.apple.BiometricKit.Library-MesaFactory'!\n"
+ "URL: %!@(MISSING) scheme is invalid"
+ "FDR CA URL: %!@(MISSING)"
+ "FDRCAURL"
+ "NSStringFromKey:defaultValue:failed:"
+ "T@\"NSString\",R,N,V_trustObjectURL"
+ "DSURL"
+ "TrustObjectURL"
+ "size == sizeof(state)"
+ "\x16"
+ "AssertMacros: %!s(MISSING) (value = 0x%!l(MISSING)x), %!s(MISSING) file: %!s(MISSING), line: %!d(MISSING)\n\n"
+ "_FDRCAURL"
+ "-[MesaPairer createFDROptions]"
+ "setPhysicalPresence -> 0x%!x(MISSING)\n"
+ "GetCombined"
+ "Failed to get sensor type: 0x%!x(MISSING)"
+ "trustObjectURL"
+ "Mesa protocol version %!d(MISSING)"
+ "T@\"NSString\",R,N,V_FDRCAURL"
+ "_validateURL:failed:"
+ "Physical Presence -> %!d(MISSING)\n"
- "\x13"

```
