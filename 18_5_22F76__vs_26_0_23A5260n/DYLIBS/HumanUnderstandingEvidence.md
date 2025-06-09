## HumanUnderstandingEvidence

> `/System/Library/PrivateFrameworks/HumanUnderstandingEvidence.framework/HumanUnderstandingEvidence`

```diff

-124.19.0.1.0
-  __TEXT.__text: 0x49ec
-  __TEXT.__auth_stubs: 0x850
+146.101.0.0.0
+  __TEXT.__text: 0x481c
+  __TEXT.__auth_stubs: 0x860
   __TEXT.__objc_methlist: 0x2fc
-  __TEXT.__const: 0x500
+  __TEXT.__const: 0x4f8
   __TEXT.__constg_swiftt: 0x11c
   __TEXT.__swift5_typeref: 0xd9
   __TEXT.__swift5_builtin: 0x3c

   __TEXT.__cstring: 0x242
   __TEXT.__oslogstring: 0x4b
   __TEXT.__gcc_except_tab: 0x34c
-  __TEXT.__unwind_info: 0x2f8
+  __TEXT.__unwind_info: 0x2d8
   __TEXT.__eh_frame: 0x1a0
   __TEXT.__objc_classname: 0x3e
   __TEXT.__objc_methname: 0x516
-  __TEXT.__objc_methtype: 0x746
+  __TEXT.__objc_methtype: 0x4e3
   __TEXT.__objc_stubs: 0x200
   __DATA_CONST.__got: 0xb8
-  __DATA_CONST.__const: 0xc0
+  __DATA_CONST.__const: 0xc8
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x230
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x438
+  __AUTH_CONST.__auth_got: 0x440
   __AUTH_CONST.__const: 0x1d8
   __AUTH_CONST.__cfstring: 0x120
   __AUTH_CONST.__objc_const: 0x358

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
+  - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_errno.dylib
-  - /usr/lib/swift/libswift_math.dylib
-  - /usr/lib/swift/libswift_signal.dylib
-  - /usr/lib/swift/libswift_stdio.dylib
-  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
-  - /usr/lib/swift/libswiftsys_time.dylib
-  - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 47FAF277-654F-3069-B154-359D3F8007CB
-  Functions: 165
+  - /usr/lib/swift/libswiftsimd.dylib
+  UUID: 1DE62AA2-0F97-3AF1-ABDF-053CC4A14CD0
+  Functions: 163
   Symbols:   140
   CStrings:  153
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftAccelerate
+ __swift_FORCE_LOAD_$_swiftCoreImage
+ __swift_FORCE_LOAD_$_swiftOSLog
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ __swift_FORCE_LOAD_$_swiftsimd
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftunistd
- _objc_retain_x26
CStrings:
+ "{HDGuardedData=\"scores\"{SimdVector<float __attribute__((ext_vector_type(8))), float>=\"chunks\"{vector<float __attribute__((ext_vector_type(8))), (anonymous namespace)::SimdAlignedAllocator<float __attribute__((ext_vector_type(8)))>>=\"__begin_\"^\"__end_\"^\"__cap_\"^}\"count\"Q}\"abs\"{SimdVector<int __attribute__((ext_vector_type(8))), unsigned int>=\"chunks\"{vector<int __attribute__((ext_vector_type(8))), (anonymous namespace)::SimdAlignedAllocator<int __attribute__((ext_vector_type(8)))>>=\"__begin_\"^\"__end_\"^\"__cap_\"^}\"count\"Q}\"enumerationInProgress\"B}"
+ "{unique_ptr<proactive::pas::SynchronizedObject<(anonymous namespace)::HDGuardedData, proactive::pas::detail::RecursiveMutex>, std::default_delete<proactive::pas::SynchronizedObject<(anonymous namespace)::HDGuardedData, proactive::pas::detail::RecursiveMutex>>>=\"__ptr_\"^v}"
- "{HDGuardedData=\"scores\"{SimdVector<float __attribute__((ext_vector_type(8))), float>=\"chunks\"{vector<float __attribute__((ext_vector_type(8))), (anonymous namespace)::SimdAlignedAllocator<float __attribute__((ext_vector_type(8)))>>=\"__begin_\"^\"__end_\"^\"__end_cap_\"{__compressed_pair<float * __attribute__((ext_vector_type(8))), (anonymous namespace)::SimdAlignedAllocator<float __attribute__((ext_vector_type(8)))>>=\"__value_\"^}}\"count\"Q}\"abs\"{SimdVector<int __attribute__((ext_vector_type(8))), unsigned int>=\"chunks\"{vector<int __attribute__((ext_vector_type(8))), (anonymous namespace)::SimdAlignedAllocator<int __attribute__((ext_vector_type(8)))>>=\"__begin_\"^\"__end_\"^\"__end_cap_\"{__compressed_pair<int * __attribute__((ext_vector_type(8))), (anonymous namespace)::SimdAlignedAllocator<int __attribute__((ext_vector_type(8)))>>=\"__value_\"^}}\"count\"Q}\"enumerationInProgress\"B}"
- "{unique_ptr<proactive::pas::SynchronizedObject<(anonymous namespace)::HDGuardedData, proactive::pas::detail::RecursiveMutex>, std::default_delete<proactive::pas::SynchronizedObject<(anonymous namespace)::HDGuardedData, proactive::pas::detail::RecursiveMutex>>>=\"__ptr_\"{__compressed_pair<proactive::pas::SynchronizedObject<(anonymous namespace)::HDGuardedData, proactive::pas::detail::RecursiveMutex> *, std::default_delete<proactive::pas::SynchronizedObject<(anonymous namespace)::HDGuardedData, proactive::pas::detail::RecursiveMutex>>>=\"__value_\"^v}}"

```
