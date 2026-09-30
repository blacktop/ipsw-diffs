## libGPUCompilerImplLazy.dylib

> `/System/Library/PrivateFrameworks/GPUCompiler.framework/Versions/32023/Libraries/libGPUCompilerImplLazy.dylib`

```diff

 32023.921.6.0.0
-  __TEXT.__text: 0x117e480
+  __TEXT.__text: 0x1187120
   __TEXT.__init_offsets: 0x14
-  __TEXT.__const: 0xd5fd0
-  __TEXT.__cstring: 0x13a4c7
-  __TEXT.__unwind_info: 0x18b60
+  __TEXT.__const: 0xd6420
+  __TEXT.__cstring: 0x13a8b3
+  __TEXT.__unwind_info: 0x18bd0
   __TEXT.__auth_stubs: 0x0
-  __DATA_CONST.__const: 0x192f30
+  __DATA_CONST.__const: 0x193158
   __DATA_CONST.__weak_got: 0x8
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0xf4a20
+  __AUTH_CONST.__const: 0xf4bb8
   __AUTH_CONST.__weak_auth_got: 0xb8
-  __AUTH_CONST.__auth_got: 0x35a8
-  __AUTH.__data: 0x4b40
+  __AUTH_CONST.__auth_got: 0x35b8
+  __AUTH.__data: 0x4bd0
   __AUTH.__thread_vars: 0x18
   __AUTH.__thread_bss: 0x8
-  __DATA.__data: 0x16e8
+  __DATA.__data: 0x1700
   __DATA.__common: 0x20
   __DATA_DIRTY.__data: 0x1130
   __DATA_DIRTY.__bss: 0x15a8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 37894
-  Symbols:   1842
-  CStrings:  56845
+  Functions: 37935
+  Symbols:   1844
+  CStrings:  56883
 
Symbols:
+ __ZN4llvm3air12AIPersistent7getImplERNS_11LLVMContextEbNS_8Metadata11StorageTypeEb
+ __ZN4llvm3air16AIKernelFunction7getImplERNS_11LLVMContextEPNS_8FunctionENS_24MDTupleTypedArrayWrapperINS0_12AIReturnTypeEEENS6_INS0_10AIArgumentEEEPNS0_13AIVecTypeHintEPNS0_15AIWorkgroupSizeEPNS0_19AIWorkgroupSizeHintEPNS0_18AIWorkgroupMaxSizeEPNS0_16AIUserAnnotationEPNS0_12AIPersistentEPNS0_22AIForwardProgressUsageENS_8Metadata11StorageTypeEb
+ __ZN4llvm3air22AIForwardProgressUsage7getImplERNS_11LLVMContextENS0_26AIForwardProgressUsageKindENS_8Metadata11StorageTypeEb
- __ZN4llvm3air16AIKernelFunction7getImplERNS_11LLVMContextEPNS_8FunctionENS_24MDTupleTypedArrayWrapperINS0_12AIReturnTypeEEENS6_INS0_10AIArgumentEEEPNS0_13AIVecTypeHintEPNS0_15AIWorkgroupSizeEPNS0_19AIWorkgroupSizeHintEPNS0_18AIWorkgroupMaxSizeEPNS0_16AIUserAnnotationENS_8Metadata11StorageTypeEb
CStrings:
+ " Automatic"
+ " SIMDGroupParallel"
+ " Weak"
+ " [[forward_progress_usage"
+ " [[gnu::contention_relief"
+ " [[persistent"
+ " __attribute__((contention_relief"
+ "#pragma METAL contention_relief"
+ "'default', 'automatic' or 'none'"
+ "ContentionReliefKind"
+ "METAL contention_relief"
+ "METAL::contention_relief"
+ "Metal: support for contention relief"
+ "Metal: support for the forward progress usage attribute"
+ "Metal: support for the persistent attribute"
+ "MetalContentionRelief"
+ "MetalContentionReliefAttr"
+ "MetalForwardProgressUsage"
+ "MetalForwardProgressUsageAttr"
+ "MetalPersistent"
+ "MetalPersistentAttr"
+ "Usage"
+ "__metal_atomic_notify_all_simdgroup"
+ "__metal_atomic_notify_one_simdgroup"
+ "__metal_atomic_wait_explicit_simdgroup"
+ "__metal_atomic_wait_with_predicate_explicit_simdgroup"
+ "__metal_critical_section"
+ "__metal_yield_simdgroup"
+ "annot_pragma_metal_contention_relief"
+ "contention-relief"
+ "contention_relief"
+ "forward_progress_usage"
+ "gnu::contention_relief"
+ "persistent"
+ "simdgroup_parallel"
+ "uuuuiii"
+ "vu"
+ "vuuuu"
```
