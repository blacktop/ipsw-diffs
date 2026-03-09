## libGLVMPlugin.dylib

> `/System/Library/Frameworks/OpenGLES.framework/libGLVMPlugin.dylib`

```diff

 23.1.1.0.0
-  __TEXT.__text: 0x46944
-  __TEXT.__auth_stubs: 0xb30
-  __TEXT.__cstring: 0x3615
+  __TEXT.__text: 0x468f0
+  __TEXT.__auth_stubs: 0xb20
+  __TEXT.__cstring: 0x33a5
   __TEXT.__const: 0x930
   __TEXT.__oslogstring: 0x3
   __TEXT.__unwind_info: 0x610
   __DATA_CONST.__got: 0x18
   __DATA_CONST.__const: 0x1248
-  __AUTH_CONST.__auth_got: 0x598
+  __AUTH_CONST.__auth_got: 0x590
   __AUTH_CONST.__const: 0x150
   __AUTH.__data: 0xe00
   __DATA.__data: 0xcc

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libz.1.dylib
-  UUID: CBDB9647-D182-3D48-BA1D-91A8E89B2935
+  UUID: 7BF34E19-0028-35CC-8E4F-C2ABF8042D66
   Functions: 630
-  Symbols:   1436
-  CStrings:  859
+  Symbols:   1435
+  CStrings:  857
 
Symbols:
+ __ZNSt3__110unique_ptrIN4llvm6ModuleENS_14default_deleteIS2_EEED1B9nqn210106Ev
+ __ZNSt3__119__allocate_at_leastB9nqn210106INS_9allocatorIPN4llvm6MDNodeEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
+ __ZNSt3__16vectorINS_4pairIPN4llvm6MDNodeENS2_9SetVectorIPNS2_8MetadataENS0_IS7_NS_9allocatorIS7_EEEENS2_8DenseSetIS7_NS2_12DenseMapInfoIS7_vEEEEEEEENS8_ISG_EEE16__destroy_vectorclB9nqn210106Ev
+ __ZNSt3__16vectorIPN4llvm6MDNodeENS_9allocatorIS3_EEE20__throw_length_errorB9nqn210106Ev
+ __ZNSt3__19allocatorINS_4pairIPN4llvm6MDNodeENS2_9SetVectorIPNS2_8MetadataENS_6vectorIS7_NS0_IS7_EEEENS2_8DenseSetIS7_NS2_12DenseMapInfoIS7_vEEEEEEEEE7destroyB9nqn210106EPSG_
+ __ZSt28__throw_bad_array_new_lengthB9nqn210106v
- __ZNSt3__110unique_ptrIN4llvm6ModuleENS_14default_deleteIS2_EEED1B9fon210106Ev
- __ZNSt3__119__allocate_at_leastB9fon210106INS_9allocatorIPN4llvm6MDNodeEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
- __ZNSt3__132__internal_log_hardening_failureEPKc
- __ZNSt3__16vectorINS_4pairIPN4llvm6MDNodeENS2_9SetVectorIPNS2_8MetadataENS0_IS7_NS_9allocatorIS7_EEEENS2_8DenseSetIS7_NS2_12DenseMapInfoIS7_vEEEEEEEENS8_ISG_EEE16__destroy_vectorclB9fon210106Ev
- __ZNSt3__16vectorIPN4llvm6MDNodeENS_9allocatorIS3_EEE20__throw_length_errorB9fon210106Ev
- __ZNSt3__19allocatorINS_4pairIPN4llvm6MDNodeENS2_9SetVectorIPNS2_8MetadataENS_6vectorIS7_NS0_IS7_EEEENS2_8DenseSetIS7_NS2_12DenseMapInfoIS7_vEEEEEEEEE7destroyB9fon210106EPSG_
- __ZSt28__throw_bad_array_new_lengthB9fon210106v
Functions:
~ __ZN19GLPDebugInfoContext14createFunctionEPKcPN4llvm8FunctionE : 452 -> 416
~ _glpLLVMGetDebugLocation : 140 -> 92
CStrings:
- "/AppleInternal/Library/BuildRoots/4~CJlFugAVK08U_27PIu6adtk-6VWWsRwfAhPd6JY/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CJlFugAVK08U_27PIu6adtk-6VWWsRwfAhPd6JY/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"

```
