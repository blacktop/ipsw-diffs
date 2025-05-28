## SignalCompression

> `/System/Library/PrivateFrameworks/SignalCompression.framework/SignalCompression`

```diff

 12.0.0.0.0
-  __TEXT.__text: 0x8da4
-  __TEXT.__auth_stubs: 0x780
+  __TEXT.__text: 0x978c
+  __TEXT.__auth_stubs: 0x7b0
   __TEXT.__objc_methlist: 0xc8
   __TEXT.__const: 0x15a6
-  __TEXT.__gcc_except_tab: 0x198
-  __TEXT.__cstring: 0x443
+  __TEXT.__gcc_except_tab: 0x19c
+  __TEXT.__cstring: 0x863
   __TEXT.__oslogstring: 0xfe
   __TEXT.__constg_swiftt: 0x20c
   __TEXT.__swift5_typeref: 0x15e

   __TEXT.__swift5_assocty: 0x18
   __TEXT.__swift5_proto: 0x3c
   __TEXT.__swift5_types: 0x2c
-  __TEXT.__unwind_info: 0x3e4
+  __TEXT.__unwind_info: 0x3f0
   __TEXT.__eh_frame: 0x260
   __TEXT.__objc_classname: 0x2c
   __TEXT.__objc_methname: 0x259

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x4e0
   __DATA_CONST.__objc_selrefs: 0x88
+  __DATA_CONST.__objc_classrefs: 0x18
+  __DATA_CONST.__objc_superrefs: 0x10
   __AUTH_CONST.__const: 0x570
   __AUTH_CONST.__objc_const: 0x90
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__auth_got: 0x3d0
+  __AUTH_CONST.__auth_got: 0x3e8
   __AUTH.__objc_data: 0x140
   __AUTH.__data: 0x200
-  __DATA.__objc_classrefs: 0x18
-  __DATA.__objc_superrefs: 0x10
   __DATA.__objc_ivar: 0x38
   __DATA.__data: 0x760
   __DATA.__bss: 0x7a0

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 278
-  Symbols:   381
-  CStrings:  98
+  Functions: 289
+  Symbols:   382
+  CStrings:  120
 
Symbols:
+ __ZNKSt3__16vectorIN3gcl17ArithmeticContextENS_9allocatorIS2_EEE20__throw_length_errorB8ue170006Ev
+ __ZNKSt3__16vectorIhNS_9allocatorIhEEE20__throw_length_errorB8ue170006Ev
+ __ZNKSt3__16vectorIiNS_9allocatorIiEEE20__throw_length_errorB8ue170006Ev
+ __ZNSt12length_errorC1B8ue170006EPKc
+ __ZNSt3__110unique_ptrIN3gcl6motion11DecoderImplENS_14default_deleteIS3_EEE5resetB8ue170006EPS3_
+ __ZNSt3__110unique_ptrIN3gcl6motion11EncoderImplENS_14default_deleteIS3_EEE5resetB8ue170006EPS3_
+ __ZNSt3__119__allocate_at_leastB8ue170006INS_9allocatorIN3gcl17ArithmeticContextEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119__allocate_at_leastB8ue170006INS_9allocatorIiEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
+ __ZNSt3__120__throw_length_errorB8ue170006EPKc
+ __ZNSt3__16vectorIhNS_9allocatorIhEEE11__vallocateB8ue170006Em
+ __ZNSt3__16vectorIhNS_9allocatorIhEEE16__init_with_sizeB8ue170006IPhS5_EEvT_T0_m
+ __ZNSt3__16vectorIiNS_9allocatorIiEEE11__vallocateB8ue170006Em
+ __ZNSt3__16vectorIiNS_9allocatorIiEEE16__init_with_sizeB8ue170006IPKiS6_EEvT_T0_m
+ __ZSt28__throw_bad_array_new_lengthB8ue170006v
+ _memset
+ _objc_release_x21
- __ZNKSt3__16vectorIN3gcl17ArithmeticContextENS_9allocatorIS2_EEE20__throw_length_errorB7v160006Ev
- __ZNKSt3__16vectorIhNS_9allocatorIhEEE20__throw_length_errorB7v160006Ev
- __ZNKSt3__16vectorIiNS_9allocatorIiEEE20__throw_length_errorB7v160006Ev
- __ZNSt12length_errorC1B7v160006EPKc
- __ZNSt3__110unique_ptrIN3gcl6motion11DecoderImplENS_14default_deleteIS3_EEE5resetB7v160006EPS3_
- __ZNSt3__110unique_ptrIN3gcl6motion11EncoderImplENS_14default_deleteIS3_EEE5resetB7v160006EPS3_
- __ZNSt3__119__allocate_at_leastB7v160006INS_9allocatorIN3gcl17ArithmeticContextEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB7v160006INS_9allocatorIiEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__120__throw_length_errorB7v160006EPKc
- __ZNSt3__16vectorIhNS_9allocatorIhEEE11__vallocateB7v160006Em
- __ZNSt3__16vectorIhNS_9allocatorIhEEEC2IPhLi0EEET_S6_
- __ZNSt3__16vectorIiNS_9allocatorIiEEE11__vallocateB7v160006Em
- __ZNSt3__16vectorIiNS_9allocatorIiEEEC2IPKiLi0EEET_S7_
- __ZSt28__throw_bad_array_new_lengthB7v160006v
- _swift_bridgeObjectRetain_n
CStrings:
+ "Can't construct Array with count < 0"
+ "Fatal error"
+ "Insufficient space allocated to copy string contents"
+ "Negative value is not representable"
+ "Not enough bits to represent the passed value"
+ "Swift/Array.swift"
+ "Swift/ContiguousArrayBuffer.swift"
+ "Swift/Integers.swift"
+ "Swift/StringTesting.swift"
+ "Swift/StringUTF8View.swift"
+ "Swift/UnsafeBufferPointer.swift"
+ "Swift/UnsafePointer.swift"
+ "Swift/UnsafeRawBufferPointer.swift"
+ "Swift/UnsafeRawPointer.swift"
+ "Unexpectedly found nil while unwrapping an Optional value"
+ "UnsafeMutableBufferPointer with negative count"
+ "UnsafeMutablePointer.initialize overlapping range"
+ "UnsafeMutablePointer.initialize with negative count"
+ "UnsafeMutablePointer.moveInitialize with negative count"
+ "UnsafeMutableRawBufferPointer.copyMemory source has too many elements"
+ "UnsafeMutableRawPointer.initializeMemory overlapping range"
+ "invalid Collection: less than 'count' elements in collection"

```
