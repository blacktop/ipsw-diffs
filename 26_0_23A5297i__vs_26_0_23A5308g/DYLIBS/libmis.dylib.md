## libmis.dylib

> `/usr/lib/libmis.dylib`

```diff

-463.0.4.0.0
-  __TEXT.__text: 0x3b394
-  __TEXT.__auth_stubs: 0x1d10
-  __TEXT.__objc_methlist: 0xccc
+463.0.8.0.0
+  __TEXT.__text: 0x3ab98
+  __TEXT.__auth_stubs: 0x1d20
+  __TEXT.__objc_methlist: 0xcd4
   __TEXT.__const: 0x6d50
   __TEXT.__swift5_typeref: 0x448
   __TEXT.__swift5_capture: 0x8bc
-  __TEXT.__cstring: 0x552b
+  __TEXT.__cstring: 0x538e
   __TEXT.__constg_swiftt: 0x4b8
   __TEXT.__swift5_builtin: 0x64
   __TEXT.__swift5_mpenum: 0x18

   __TEXT.__swift5_fieldmd: 0x350
   __TEXT.__swift5_proto: 0x68
   __TEXT.__swift5_types: 0x6c
-  __TEXT.__oslogstring: 0x3441
+  __TEXT.__oslogstring: 0x333d
   __TEXT.__swift5_assocty: 0xa8
-  __TEXT.__gcc_except_tab: 0x3d4
-  __TEXT.__unwind_info: 0xe18
+  __TEXT.__gcc_except_tab: 0x398
+  __TEXT.__unwind_info: 0xdf0
   __TEXT.__eh_frame: 0x109c
   __TEXT.__objc_classname: 0x125
-  __TEXT.__objc_methname: 0x1c48
+  __TEXT.__objc_methname: 0x1c5e
   __TEXT.__objc_methtype: 0x398
-  __TEXT.__objc_stubs: 0x13c0
-  __DATA_CONST.__got: 0x310
-  __DATA_CONST.__const: 0x4148
+  __TEXT.__objc_stubs: 0x1380
+  __DATA_CONST.__got: 0x2f8
+  __DATA_CONST.__const: 0x40d0
   __DATA_CONST.__objc_classlist: 0xb0
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x850
+  __DATA_CONST.__objc_selrefs: 0x848
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x58
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__auth_got: 0xe98
+  __AUTH_CONST.__auth_got: 0xea0
   __AUTH_CONST.__const: 0x13b0
-  __AUTH_CONST.__cfstring: 0x1cc0
-  __AUTH_CONST.__objc_const: 0x1518
+  __AUTH_CONST.__cfstring: 0x1c80
+  __AUTH_CONST.__objc_const: 0x1528
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH.__objc_data: 0x570
-  __AUTH.__data: 0x1e8
+  __AUTH.__objc_data: 0x568
+  __AUTH.__data: 0x2f8
   __DATA.__objc_ivar: 0xac
-  __DATA.__data: 0x2d8
-  __DATA.__bss: 0xc60
-  __DATA.__common: 0x88
-  __DATA_DIRTY.__objc_data: 0x288
-  __DATA_DIRTY.__data: 0x348
+  __DATA.__data: 0x2c8
+  __DATA.__bss: 0xc48
+  __DATA.__common: 0x70
+  __DATA_DIRTY.__objc_data: 0x290
+  __DATA_DIRTY.__data: 0x238
   __DATA_DIRTY.__bss: 0x1a0
+  __DATA_DIRTY.__common: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/Security.framework/Security
+  - /System/Library/PrivateFrameworks/CoreTime.framework/CoreTime
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libCoreEntitlements.dylib
   - /usr/lib/libMobileGestalt.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: A90A7B7A-0A35-30C5-878E-A6692087DCFD
-  Functions: 1180
-  Symbols:   976
-  CStrings:  1392
+  UUID: 3EA7D9EB-5B88-376E-A997-1A258DFC1A5A
+  Functions: 1177
+  Symbols:   972
+  CStrings:  1374
 
Symbols:
+ _TMGetKernelMonotonicClock
+ _TMGetRTCResetCount
- _OBJC_CLASS_$_NSAssertionHandler
- __sl_dlopen
- _dlerror
- _dlsym
- _kSecCodeInfoCdHashes
- _kSecCodeInfoDigestAlgorithms
CStrings:
+ "SELECT DISTINCT profiles.uuid\nFROM profiles\nLEFT JOIN signing_identities ON signing_identities.uuid = profiles.uuid\nWHERE signing_identity = ?1"
+ "SELECT DISTINCT signing_identities.signing_identity\nFROM signing_identities\nLEFT JOIN profiles ON profiles.uuid = signing_identities.uuid\nWHERE profiles.uuid = ?1"
+ "SELECT DISTINCT signing_identities.signing_identity\nFROM signing_identities\nLEFT JOIN profiles ON profiles.uuid = signing_identities.uuid\nWHERE team_id = ?1"
+ "SELECT DISTINCT team_id\nFROM profiles\nLEFT JOIN signing_identities ON signing_identities.uuid = profiles.uuid\nWHERE signing_identity = ?1"
+ "T@\"NSObject<OS_dispatch_semaphore>\",R,N,V_transactionSemaphore"
+ "_transactionSemaphore"
+ "transactionSemaphore"
- "%s"
- "/AppleInternal/Library/Frameworks/CoreTime.framework/CoreTime"
- "/System/AppleInternal/Library/Frameworks/CoreTime.framework/CoreTime"
- "/System/Library/Frameworks/CoreTime.framework/CoreTime"
- "/System/Library/PrivateFrameworks/CoreTime.framework/CoreTime"
- "Algorithm at index %ld is not a number, but %{public}@!"
- "Algorithms are not an array, but %{public}@!"
- "CFTimeInterval TMGetKernelMonotonicClockSoft(void)"
- "CdHashes are not an array, but %{public}@!"
- "CdHashes count (%ld) != Algorithms count (%ld)!\n"
- "Could not get numeric value for algorithm at index %ld: %{public}@"
- "MISDeviceUtilities.m"
- "SELECT profiles.uuid\nFROM profiles\nLEFT JOIN signing_identities ON signing_identities.uuid = profiles.uuid\nWHERE signing_identity = ?1"
- "SELECT signing_identities.signing_identity\nFROM signing_identities\nLEFT JOIN profiles ON profiles.uuid = signing_identities.uuid\nWHERE profiles.uuid = ?1"
- "SELECT signing_identities.signing_identity\nFROM signing_identities\nLEFT JOIN profiles ON profiles.uuid = signing_identities.uuid\nWHERE team_id = ?1"
- "SELECT team_id\nFROM profiles\nLEFT JOIN signing_identities ON signing_identities.uuid = profiles.uuid\nWHERE signing_identity = ?1"
- "TMGetKernelMonotonicClock"
- "TMGetRTCResetCount"
- "_transactionSem"
- "currentHandler"
- "handleFailureInFunction:file:lineNumber:description:"
- "int TMGetRTCResetCountSoft(void)"
- "void *CoreTimeLibrary(void)"

```
