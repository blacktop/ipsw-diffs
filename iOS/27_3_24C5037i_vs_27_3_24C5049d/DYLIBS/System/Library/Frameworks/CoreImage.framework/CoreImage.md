## CoreImage

> `/System/Library/Frameworks/CoreImage.framework/CoreImage`

```diff

-1667.60.2.0.0
-  __TEXT.__text: 0x3442c8
-  __TEXT.__objc_methlist: 0x159f0
+1667.60.3.0.0
+  __TEXT.__text: 0x346508
+  __TEXT.__objc_methlist: 0x15a10
   __TEXT.__const: 0xe198
-  __TEXT.__gcc_except_tab: 0xa8d4
-  __TEXT.__cstring: 0x104b7d
-  __TEXT.__oslogstring: 0xb37e
+  __TEXT.__gcc_except_tab: 0xa934
+  __TEXT.__cstring: 0x104c88
+  __TEXT.__oslogstring: 0xb51f
   __TEXT.__dlopen_cstrs: 0x445
   __TEXT.__runtimeheader: 0x15aa4
   __TEXT.__cikl2metal_pre: 0x54b
   __TEXT.__grain: 0x105040
-  __TEXT.__unwind_info: 0xc868
+  __TEXT.__unwind_info: 0xc8b8
   __TEXT.__eh_frame: 0x350
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8e78
+  __DATA_CONST.__objc_selrefs: 0x8ea0
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x360
   __DATA_CONST.__objc_arraydata: 0x1488
   __DATA_CONST.__got: 0xb28
   __AUTH_CONST.__const: 0xde40
-  __AUTH_CONST.__cfstring: 0x1dcc0
-  __AUTH_CONST.__objc_const: 0x2b4e0
+  __AUTH_CONST.__cfstring: 0x1dd00
+  __AUTH_CONST.__objc_const: 0x2b500
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__objc_intobj: 0xdc8
   __AUTH_CONST.__objc_dictobj: 0x410

   __AUTH_CONST.__auth_got: 0x1898
   __AUTH.__objc_data: 0x9a88
   __AUTH.__data: 0x278a0
-  __DATA.__objc_ivar: 0x1fc0
+  __DATA.__objc_ivar: 0x1fc4
   __DATA.__data: 0x67a8
   __DATA.__common: 0x38
   __DATA_DIRTY.__objc_data: 0xa28

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 15194
-  Symbols:   26378
-  CStrings:  8898
+  Functions: 15208
+  Symbols:   26396
+  CStrings:  8904
 
Symbols:
+ -[CIKernelLibrary fallbackLibraryForFunctionName:]
+ -[CIKernelLibrary sliceLibraries]
+ -[CIKernelLibrary stitchableLibraryForFunctionName:]
+ GCC_except_table144
+ GCC_except_table147
+ GCC_except_table198
+ GCC_except_table211
+ GCC_except_table221
+ GCC_except_table228
+ GCC_except_table400
+ GCC_except_table409
+ GCC_except_table486
+ _CIMetalDeviceSupportsDynamicLibraries
+ _CIMetalFunctionImportsCoreImageDylib
+ _CI_SIMULATE_NO_METAL_DYLIB_SUPPORT
+ _OBJC_IVAR_$_CIKernelLibrary._slice_libraries
+ __ZGVZ34CI_SIMULATE_NO_METAL_DYLIB_SUPPORTE1v
+ __ZL25applyMetalUserAnnotationsP15CIKernelLibraryPKcRjRN2CI11PixelFormatE
+ __ZN18CIKernelReflection38reflectLegacyWithStitchableAnnotationsEP15CIKernelLibraryS1_PKcPP7NSError
+ __ZNSt3__111__introsortINS_17_ClassicAlgPolicyERZL21fatMetalLibrarySlicesP6NSDataE3$_0P20FatMetalLibrarySliceLb0EEEvT1_S8_T0_NS_15iterator_traitsIS8_E15difference_typeEb
+ __ZNSt3__119__allocate_at_leastB9fqn220106INS_9allocatorI20FatMetalLibrarySliceEENS_16allocator_traitsIS3_EEEENS_19__allocation_resultINT0_7pointerENS7_9size_typeEEERT_m
+ __ZNSt3__127__insertion_sort_incompleteB9fqn220106INS_17_ClassicAlgPolicyERZL21fatMetalLibrarySlicesP6NSDataE3$_0P20FatMetalLibrarySliceEEbT1_S8_T0_
+ __ZNSt3__16vectorI20FatMetalLibrarySliceNS_9allocatorIS1_EEE20__throw_length_errorB9fqn220106Ev
+ __ZNSt3__16vectorI20FatMetalLibrarySliceNS_9allocatorIS1_EEE24__emplace_back_slow_pathIJRKS1_EEEPS1_DpOT_
+ __ZNSt3__17__sort5B9fqn220106INS_17_ClassicAlgPolicyERZL21fatMetalLibrarySlicesP6NSDataE3$_0P20FatMetalLibrarySliceLi0EEEvT1_S8_S8_S8_S8_T0_
+ __ZZ34CI_SIMULATE_NO_METAL_DYLIB_SUPPORTE1v
- GCC_except_table187
- GCC_except_table203
- GCC_except_table213
- GCC_except_table219
- GCC_except_table223
- GCC_except_table398
- GCC_except_table407
- GCC_except_table484
CStrings:
+ "1667.60.3"
+ "CI_SIMULATE_NO_METAL_DYLIB_SUPPORT"
+ "Kernel '%{public}s' links CoreImage.metallib but this device does not support dynamic libraries."
+ "Kernel '%{public}s' links CoreImage.metallib which this device does not support. Using the non-stitchable version of the function from another slice of the library."
+ "Kernel '%{public}s': the non-stitchable version in another slice of the library does not have the same signature as the stitchable one, so it is not used."
+ "Kernel links the Core Image Metal dynamic library, which is not supported on this GPU, and its non-stitchable version has a different signature."
+ "Kernel links the Core Image Metal dynamic library, which is not supported on this GPU."
- "1667.60.2"
```
