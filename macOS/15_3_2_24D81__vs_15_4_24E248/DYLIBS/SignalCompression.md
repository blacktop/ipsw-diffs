## SignalCompression

> `/System/Library/PrivateFrameworks/SignalCompression.framework/Versions/A/SignalCompression`

```diff

 18.60.1.0.0
-  __TEXT.__text: 0x9668
-  __TEXT.__auth_stubs: 0x720
+  __TEXT.__text: 0x8718
+  __TEXT.__auth_stubs: 0x6d0
   __TEXT.__objc_methlist: 0xc4
-  __TEXT.__const: 0x15c6
-  __TEXT.__gcc_except_tab: 0x214
-  __TEXT.__cstring: 0x673
+  __TEXT.__const: 0x15e6
+  __TEXT.__gcc_except_tab: 0x220
+  __TEXT.__cstring: 0x2a3
   __TEXT.__oslogstring: 0x249
   __TEXT.__constg_swiftt: 0x20c
   __TEXT.__swift5_typeref: 0x15e

   __TEXT.__swift5_assocty: 0x18
   __TEXT.__swift5_proto: 0x3c
   __TEXT.__swift5_types: 0x2c
-  __TEXT.__unwind_info: 0x3d0
-  __TEXT.__eh_frame: 0x1e8
+  __TEXT.__unwind_info: 0x388
+  __TEXT.__eh_frame: 0x1b4
   __TEXT.__objc_classname: 0x2c
   __TEXT.__objc_methname: 0x257
   __TEXT.__objc_methtype: 0x1a9
   __TEXT.__objc_stubs: 0xc0
-  __DATA_CONST.__got: 0xf8
+  __DATA_CONST.__got: 0xf0
   __DATA_CONST.__const: 0xb0
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x88
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x3a0
+  __AUTH_CONST.__auth_got: 0x378
   __AUTH_CONST.__const: 0x3c8
   __AUTH_CONST.__objc_const: 0x570
   __AUTH.__objc_data: 0x140

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 876B0A6B-4505-3488-A06C-94671815CE73
-  Functions: 264
-  Symbols:   322
-  CStrings:  117
+  UUID: 12C1DDD5-9B64-37DA-866A-4435F14626F8
+  Functions: 246
+  Symbols:   323
+  CStrings:  96
 
Symbols:
+ -[MotionDecoderWrapper motionDecoderWrapperLogSharedInstance].cold.1
+ -[MotionEncoderWrapper motionEncoderWrapperLogSharedInstance].cold.1
+ __ZNKSt3__16vectorIN3gcl17ArithmeticContextENS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIhNS_9allocatorIhEEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIiNS_9allocatorIiEEE20__throw_length_errorB8ne190102Ev
+ __ZNSt12length_errorC1B8ne190102EPKc
+ __ZNSt3__110unique_ptrIN3gcl6motion11DecoderImplENS_14default_deleteIS3_EEE5resetB8ne190102EPS3_
+ __ZNSt3__110unique_ptrIN3gcl6motion11EncoderImplENS_14default_deleteIS3_EEE5resetB8ne190102EPS3_
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN3gcl17ArithmeticContextEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIiEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
+ __ZNSt3__120__throw_length_errorB8ne190102EPKc
+ __ZNSt3__16vectorIhNS_9allocatorIhEEE11__vallocateB8ne190102Em
+ __ZNSt3__16vectorIhNS_9allocatorIhEEE16__init_with_sizeB8ne190102IPhS5_EEvT_T0_m
+ __ZNSt3__16vectorIhNS_9allocatorIhEEEC2B8ne190102Em
+ __ZNSt3__16vectorIiNS_9allocatorIiEEE11__vallocateB8ne190102Em
+ __ZNSt3__16vectorIiNS_9allocatorIiEEE16__init_with_sizeB8ne190102IPKiS6_EEvT_T0_m
+ __ZNSt3__16vectorIiNS_9allocatorIiEEEC2B8ne190102Em
+ __ZNSt3__16vectorIiNS_9allocatorIiEEEC2B8ne190102EmRKi
+ __ZSt28__throw_bad_array_new_lengthB8ne190102v
+ ___swift_destroy_boxed_opaque_existential_0
+ ___swift_destroy_boxed_opaque_existential_0Tm
- __ZNKSt3__16vectorIN3gcl17ArithmeticContextENS_9allocatorIS2_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIhNS_9allocatorIhEEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIiNS_9allocatorIiEEE20__throw_length_errorB8ne180100Ev
- __ZNSt12length_errorC1B8ne180100EPKc
- __ZNSt3__110unique_ptrIN3gcl6motion11DecoderImplENS_14default_deleteIS3_EEE5resetB8ne180100EPS3_
- __ZNSt3__110unique_ptrIN3gcl6motion11EncoderImplENS_14default_deleteIS3_EEE5resetB8ne180100EPS3_
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIN3gcl17ArithmeticContextEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIiEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__120__throw_length_errorB8ne180100EPKc
- __ZNSt3__16vectorIhNS_9allocatorIhEEE11__vallocateB8ne180100Em
- __ZNSt3__16vectorIhNS_9allocatorIhEEE16__init_with_sizeB8ne180100IPhS5_EEvT_T0_m
- __ZNSt3__16vectorIhNS_9allocatorIhEEEC2Em
- __ZNSt3__16vectorIiNS_9allocatorIiEEE11__vallocateB8ne180100Em
- __ZNSt3__16vectorIiNS_9allocatorIiEEE16__init_with_sizeB8ne180100IPKiS6_EEvT_T0_m
- __ZNSt3__16vectorIiNS_9allocatorIiEEEC2Em
- __ZNSt3__16vectorIiNS_9allocatorIiEEEC2EmRKi
- __ZSt28__throw_bad_array_new_lengthB8ne180100v
- ___swift_destroy_boxed_opaque_existential_1Tm
- _memset
- _swift_arrayDestroy
CStrings:
- "Can't construct Array with count < 0"
- "Fatal error"
- "Insufficient space allocated to copy string contents"
- "Negative value is not representable"
- "Not enough bits to represent the passed value"
- "Swift/Array.swift"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/Integers.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawBufferPointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.initialize with negative count"
- "UnsafeMutableRawBufferPointer.copyMemory source has too many elements"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "invalid Collection: less than 'count' elements in collection"

```
