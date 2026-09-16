## PrivacyAccounting

> `/System/Library/PrivateFrameworks/PrivacyAccounting.framework/PrivacyAccounting`

```diff

-149.0.0.0.0
-  __TEXT.__text: 0x1b9d0
+150.0.0.0.0
+  __TEXT.__text: 0x1c830
   __TEXT.__objc_methlist: 0x2114
-  __TEXT.__const: 0x690
-  __TEXT.__cstring: 0x10fc
-  __TEXT.__oslogstring: 0x9dc
+  __TEXT.__const: 0x6b0
+  __TEXT.__cstring: 0x113c
+  __TEXT.__oslogstring: 0xa3f
   __TEXT.__gcc_except_tab: 0x574
   __TEXT.__constg_swiftt: 0x26c
-  __TEXT.__swift5_typeref: 0x1fd
+  __TEXT.__swift5_typeref: 0x213
   __TEXT.__swift5_fieldmd: 0x14c
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_reflstr: 0xbd

   __TEXT.__swift5_types: 0x28
   __TEXT.__swift5_capture: 0x10
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0xcb0
+  __TEXT.__unwind_info: 0xce8
   __TEXT.__eh_frame: 0x1f8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_selrefs: 0xe10
   __DATA_CONST.__objc_protorefs: 0x40
   __DATA_CONST.__objc_superrefs: 0x140
-  __DATA_CONST.__got: 0x308
-  __AUTH_CONST.__const: 0x600
+  __DATA_CONST.__got: 0x330
+  __AUTH_CONST.__const: 0x628
   __AUTH_CONST.__cfstring: 0xe00
   __AUTH_CONST.__objc_const: 0x4640
   __AUTH_CONST.__objc_intobj: 0x78
-  __AUTH_CONST.__auth_got: 0x760
+  __AUTH_CONST.__auth_got: 0x7f0
   __AUTH.__objc_data: 0xc00
   __AUTH.__data: 0x188
   __DATA.__objc_ivar: 0x228
-  __DATA.__data: 0xa50
+  __DATA.__data: 0xa60
+  __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0x430
-  __DATA_DIRTY.__data: 0x30
+  __DATA_DIRTY.__data: 0x28
   __DATA_DIRTY.__bss: 0xd8
-  __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/BiomePubSub.framework/BiomePubSub
   - /System/Library/PrivateFrameworks/BiomeStorage.framework/BiomeStorage
   - /System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams
+  - /System/Library/PrivateFrameworks/OSEligibility.framework/OSEligibility
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/TCC.framework/TCC

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 873
-  Symbols:   2079
-  CStrings:  206
+  Functions: 884
+  Symbols:   2088
+  CStrings:  210
 
Symbols:
+ ___swift_allocate_value_buffer
+ ___swift_destroy_boxed_opaque_existential_0
+ ___swift_project_value_buffer
+ __swiftImmortalRefCount
+ _swift_arrayDestroy
+ _swift_errorRetain
+ _swift_getObjectType
+ _swift_slowAlloc
+ _swift_slowDealloc
+ _symbolic ______p s5ErrorP
+ _symbolic _____y_____G s23_ContiguousArrayStorageC s5UInt8V
- _MobileGestalt_get_current_device
- _MobileGestalt_get_greenTeaDeviceCapability
CStrings:
+ "Failed to read eligibility for %{public}s: %{public}s"
+ "OSEligibility result%{public}s"
+ "OSEligibilityClient"
+ "com.apple.privacyaccounting"
```
