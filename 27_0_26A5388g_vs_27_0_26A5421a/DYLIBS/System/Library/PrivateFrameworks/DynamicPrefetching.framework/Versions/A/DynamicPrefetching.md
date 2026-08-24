## DynamicPrefetching

> `/System/Library/PrivateFrameworks/DynamicPrefetching.framework/Versions/A/DynamicPrefetching`

```diff

-3.5.8.0.0
-  __TEXT.__text: 0x3508
+3.6.0.0.0
+  __TEXT.__text: 0x402c
   __TEXT.__objc_methlist: 0x29c
-  __TEXT.__const: 0x10a
-  __TEXT.__gcc_except_tab: 0x364
-  __TEXT.__cstring: 0x23d
-  __TEXT.__oslogstring: 0x508
-  __TEXT.__unwind_info: 0x270
+  __TEXT.__const: 0x12b
+  __TEXT.__gcc_except_tab: 0x438
+  __TEXT.__cstring: 0x321
+  __TEXT.__oslogstring: 0x639
+  __TEXT.__unwind_info: 0x2e0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x88
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x1f0
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA_CONST.__got: 0x40
-  __AUTH_CONST.__const: 0x88
-  __AUTH_CONST.__cfstring: 0x80
+  __DATA_CONST.__got: 0x78
+  __AUTH_CONST.__const: 0xe8
+  __AUTH_CONST.__cfstring: 0xc0
   __AUTH_CONST.__objc_const: 0x310
-  __AUTH_CONST.__weak_auth_got: 0x10
+  __AUTH_CONST.__weak_auth_got: 0x18
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x8
   __DATA.__data: 0xd0
-  __DATA.__bss: 0x20
+  __DATA.__bss: 0xb0
   __DATA_DIRTY.__data: 0x10
   __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
+  - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/Versions/A/CoreAnalytics
   - /System/Library/PrivateFrameworks/PowerLog.framework/Versions/A/PowerLog
   - /System/Library/PrivateFrameworks/Trial.framework/Versions/A/Trial
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 104
-  Symbols:   83
-  CStrings:  42
+  Functions: 126
+  Symbols:   105
+  CStrings:  61
 
Symbols:
+ _CFDictionaryCreateMutable
+ _CFDictionarySetValue
+ _CFRelease
+ _IOIteratorNext
+ _IOObjectConformsTo
+ _IOObjectGetClass
+ _IOObjectRelease
+ _IORegistryEntryCreateIterator
+ _IOServiceGetMatchingServices
+ __ZN11Prefetching26storage_controller_is_ans2Ev
+ __ZN11Prefetching32detected_storage_controller_nameEv
+ __ZN11Prefetching38detected_storage_controller_class_nameEv
+ __ZNSt3__117bad_function_callD1Ev
+ __ZTVNSt3__117bad_function_callE
+ __ZdlPvSt19__type_descriptor_t
+ ___cxa_guard_abort
+ _kCFAllocatorDefault
+ _kCFBooleanTrue
+ _kCFTypeDictionaryKeyCallBacks
+ _kCFTypeDictionaryValueCallBacks
+ _kIOMainPortDefault
+ _memcmp
CStrings:
+ "ANS2"
+ "ANS3"
+ "AppleANS2CGv2Controller"
+ "AppleANS2Controller"
+ "AppleANS2NVMeController"
+ "AppleANS3CGv2Controller"
+ "AppleANS3NVMeController"
+ "AppleS3ELabController"
+ "AppleS3XController"
+ "IOPropertyMatch"
+ "IOService"
+ "NVMe SMART Capable"
+ "S3E"
+ "S3X"
+ "storage_controller: detected generation=%{public}s"
+ "storage_controller: exception in detect_generation_uncached: %{public}s"
+ "storage_controller: no known NVMe controller generation matched; defaulting to unknown (Tier-1 prefetch disabled)"
+ "storage_controller: unknown exception in detect_generation_uncached"
+ "unknown"
```
