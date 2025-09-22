## AppPlaceholderSync

> `/System/Library/PrivateFrameworks/AppPlaceholderSync.framework/AppPlaceholderSync`

```diff

-50.1.0.0.0
-  __TEXT.__text: 0x25e4c
-  __TEXT.__auth_stubs: 0x15d0
+52.0.0.0.0
+  __TEXT.__text: 0x26984
+  __TEXT.__auth_stubs: 0x15b0
   __TEXT.__objc_methlist: 0x2c
   __TEXT.__const: 0x1100
-  __TEXT.__cstring: 0x946
   __TEXT.__swift5_typeref: 0x6d6
-  __TEXT.__oslogstring: 0xbbf
+  __TEXT.__oslogstring: 0xcbf
+  __TEXT.__cstring: 0x906
   __TEXT.__constg_swiftt: 0x61c
   __TEXT.__swift5_reflstr: 0x37f
   __TEXT.__swift5_fieldmd: 0x398

   __TEXT.__swift5_capture: 0x98
   __TEXT.__swift_as_entry: 0x8
   __TEXT.__swift_as_ret: 0x8
-  __TEXT.__unwind_info: 0x5e8
-  __TEXT.__eh_frame: 0x800
-  __TEXT.__objc_methname: 0x365
+  __TEXT.__unwind_info: 0x5f0
+  __TEXT.__eh_frame: 0x850
+  __TEXT.__objc_methname: 0x37f
   __TEXT.__objc_stubs: 0x20
   __DATA_CONST.__got: 0x398
   __DATA_CONST.__const: 0x120
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x140
-  __AUTH_CONST.__auth_got: 0xaf0
+  __DATA_CONST.__objc_selrefs: 0x148
+  __AUTH_CONST.__auth_got: 0xae0
   __AUTH_CONST.__const: 0x5b0
-  __AUTH_CONST.__cfstring: 0x20
   __AUTH_CONST.__objc_const: 0x5b0
   __AUTH.__objc_data: 0x70
   __AUTH.__data: 0x28
-  __DATA.__data: 0x1c8
+  __DATA.__data: 0x1d8
   __DATA.__bss: 0xaa0
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x140

   - /System/Library/PrivateFrameworks/IconServices.framework/IconServices
   - /System/Library/PrivateFrameworks/MobileInstallation.framework/MobileInstallation
   - /System/Library/PrivateFrameworks/ReplicatorServices.framework/ReplicatorServices
+  - /System/Library/PrivateFrameworks/ScreenContinuityServices.framework/ScreenContinuityServices
   - /System/Library/PrivateFrameworks/Sharing.framework/Sharing
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 535B8B41-99FC-36BB-8F7F-7E5F8307E40D
-  Functions: 560
-  Symbols:   424
-  CStrings:  176
+  UUID: 1FDE0A8A-D7A1-3A7F-8F16-B59F60443813
+  Functions: 562
+  Symbols:   419
+  CStrings:  178
 
Symbols:
+ _container_query_free
- _IsEligibleForOneness
- _NSLog
- ___CFConstantStringClassReference
- ___error
- _objc_retain_x28
- _os_eligibility_get_domain_answer
CStrings:
+ "Could not fetch iphone mirroring eligibility: %@"
+ "Got cached placeholder at: %s"
+ "Not adding bundle identifier: %s because there are no paired mirroring devices"
+ "Not adding bundles because there are no paired mirroring devices"
+ "serializedPlaceholderPath"
- "%s: error fetching eligibility: %s (%d)"
- "IsEligibleForOneness"

```
