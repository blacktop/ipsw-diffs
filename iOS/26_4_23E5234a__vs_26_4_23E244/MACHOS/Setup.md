## Setup

> `/Applications/Setup.app/Setup`

```diff

 5382.4.7.0.0
-  __TEXT.__text: 0x25d62c
+  __TEXT.__text: 0x25d6b4
   __TEXT.__auth_stubs: 0x27e0
-  __TEXT.__objc_stubs: 0x297e0
+  __TEXT.__objc_stubs: 0x29800
   __TEXT.__objc_methlist: 0x1d6d0
   __TEXT.__dlopen_cstrs: 0x1436
   __TEXT.__objc_classname: 0x58d4
-  __TEXT.__objc_methname: 0x3fd86
+  __TEXT.__objc_methname: 0x3fdb6
   __TEXT.__objc_methtype: 0xc50a
   __TEXT.__const: 0x34d0
   __TEXT.__constg_swiftt: 0x37fc

   __TEXT.__swift5_builtin: 0x154
   __TEXT.__swift5_assocty: 0x180
   __TEXT.__swift5_capture: 0x1320
-  __TEXT.__oslogstring: 0x138e0
+  __TEXT.__oslogstring: 0x138b6
   __TEXT.__swift5_proto: 0x120
   __TEXT.__swift5_types: 0x1bc
   __TEXT.__swift_as_entry: 0x1c0

   __TEXT.__unwind_info: 0x9ce8
   __TEXT.__eh_frame: 0x4700
   __DATA_CONST.__auth_got: 0x1408
-  __DATA_CONST.__got: 0x1f28
+  __DATA_CONST.__got: 0x1f38
   __DATA_CONST.__auth_ptr: 0x568
   __DATA_CONST.__const: 0x8ab8
   __DATA_CONST.__cfstring: 0xb740

   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__objc_floatobj: 0x10
   __DATA.__objc_const: 0x47c38
-  __DATA.__objc_selrefs: 0xcd48
+  __DATA.__objc_selrefs: 0xcd50
   __DATA.__objc_ivar: 0x1d9c
   __DATA.__objc_data: 0xbc88
   __DATA.__data: 0x7378

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 8547E52A-A92E-34E2-B519-AB36A3A4F007
+  UUID: BEC1ABFE-347D-3288-9FE2-75181A192D1B
   Functions: 12251
-  Symbols:   1539
+  Symbols:   1541
   CStrings:  16358
 
Symbols:
+ _BYPrivacySubscriptionBundleIdentifier
+ _OBJC_CLASS_$_AMSAcknowledgePrivacyTask
Functions:
~ sub_10007d3f4 : 24 -> 328
~ sub_100199b64 -> sub_100199c94 : 824 -> 664
~ sub_1001ef624 -> sub_1001ef6b4 : 364 -> 356
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CJlrugAOYcSD1jA0CL_MAe08-rTZ9B1xTfzTH9U/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CJlrugAOYcSD1jA0CL_MAe08-rTZ9B1xTfzTH9U/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:429: libc++ Hardening assertion !empty() failed: front() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CJlrugAOYcSD1jA0CL_MAe08-rTZ9B1xTfzTH9U/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:437: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CJlrugAOYcSD1jA0CL_MAe08-rTZ9B1xTfzTH9U/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:472: libc++ Hardening assertion size() < capacity() failed: We assume that we have enough space to insert an element at the end of the vector\n"
+ "Feb 22 2026"
+ "acknowledgementNeededForPrivacyIdentifier:account:"
+ "ams_isBundleOwner"
- "/AppleInternal/Library/BuildRoots/4~CKHTugDmCaPp_CUql_Kh1tocMlGmIFp4EmTDicQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CKHTugDmCaPp_CUql_Kh1tocMlGmIFp4EmTDicQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:429: libc++ Hardening assertion !empty() failed: front() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CKHTugDmCaPp_CUql_Kh1tocMlGmIFp4EmTDicQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:437: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CKHTugDmCaPp_CUql_Kh1tocMlGmIFp4EmTDicQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:472: libc++ Hardening assertion size() < capacity() failed: We assume that we have enough space to insert an element at the end of the vector\n"
- "Enabling D&U submission for seed build..."
- "Mar  1 2026"
- "setBoolValue:forSetting:"

```
