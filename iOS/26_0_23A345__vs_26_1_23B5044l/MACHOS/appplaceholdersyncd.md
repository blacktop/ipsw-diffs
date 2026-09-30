## appplaceholdersyncd

> `/System/Library/CoreServices/appplaceholdersyncd`

```diff

-50.1.0.0.0
-  __TEXT.__text: 0x543c
-  __TEXT.__auth_stubs: 0x800
+52.0.0.0.0
+  __TEXT.__text: 0x5514
+  __TEXT.__auth_stubs: 0x810
   __TEXT.__const: 0x1ac
   __TEXT.__swift5_typeref: 0x8a
-  __TEXT.__oslogstring: 0x370
+  __TEXT.__oslogstring: 0x3a1
   __TEXT.__swift5_capture: 0x30
   __TEXT.__swift5_entry: 0x8
   __TEXT.__swift_as_entry: 0x8
   __TEXT.__swift_as_ret: 0x4
-  __TEXT.__cstring: 0x32e
+  __TEXT.__cstring: 0x33e
   __TEXT.__constg_swiftt: 0xe0
   __TEXT.__swift5_reflstr: 0x34
   __TEXT.__swift5_fieldmd: 0x60

   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_proto: 0x4
   __TEXT.__swift5_types: 0xc
-  __TEXT.__unwind_info: 0x140
+  __TEXT.__unwind_info: 0x168
   __TEXT.__eh_frame: 0x130
-  __DATA_CONST.__auth_got: 0x400
+  __DATA_CONST.__auth_got: 0x408
   __DATA_CONST.__got: 0x78
   __DATA_CONST.__auth_ptr: 0x68
   __DATA_CONST.__const: 0x298

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0x170
   __DATA.__objc_selrefs: 0x20
-  __DATA.__data: 0x1f0
+  __DATA.__data: 0x200
+  __DATA.__common: 0x38
   __DATA.__bss: 0x80
-  __DATA.__common: 0x8
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/AppPlaceholderSync.framework/AppPlaceholderSync
+  - /System/Library/PrivateFrameworks/ScreenContinuityServices.framework/ScreenContinuityServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: A96C490B-3ADD-3845-9B4D-2BA53EDBC514
-  Functions: 80
-  Symbols:   189
-  CStrings:  47
+  UUID: 32A93E31-DD82-3312-93A0-07F14ABDF718
+  Functions: 93
+  Symbols:   190
+  CStrings:  48
 
Symbols:
+ _$s24ScreenContinuityServices0B11EligibilityV25isiPhoneMirroringEligibleSbvgZ
+ _$s2os6LoggerV9subsystem8categoryACSS_SStcfC
+ _objc_release
+ _objc_release_x28
- _$s18AppPlaceholderSync6logger2os6LoggerVvg
- _objc_release_x23
- _os_eligibility_get_domain_answer
CStrings:
+ "Could not fetch iphone mirroring eligibility: %@"

```
