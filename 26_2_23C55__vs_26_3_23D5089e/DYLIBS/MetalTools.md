## MetalTools

> `/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`

```diff

-370.64.2.0.0
-  __TEXT.__text: 0x12fa44
+371.5.0.0.0
+  __TEXT.__text: 0x12f5d4
   __TEXT.__auth_stubs: 0xc30
-  __TEXT.__objc_methlist: 0x1939c
-  __TEXT.__cstring: 0x32f09
+  __TEXT.__objc_methlist: 0x19354
+  __TEXT.__cstring: 0x32d86
   __TEXT.__const: 0x2f8
-  __TEXT.__gcc_except_tab: 0x2b98
+  __TEXT.__gcc_except_tab: 0x2b8c
   __TEXT.__oslogstring: 0x282e
-  __TEXT.__unwind_info: 0x5170
+  __TEXT.__unwind_info: 0x5160
   __TEXT.__objc_classname: 0x2520
   __TEXT.__objc_methname: 0x1e7fc
   __TEXT.__objc_methtype: 0x17ff5

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x62b8
   __DATA_CONST.__objc_protorefs: 0xa0
-  __DATA_CONST.__objc_superrefs: 0x648
+  __DATA_CONST.__objc_superrefs: 0x640
   __AUTH_CONST.__auth_got: 0x628
   __AUTH_CONST.__const: 0x1d0
-  __AUTH_CONST.__cfstring: 0xe9e0
-  __AUTH_CONST.__objc_const: 0x45f00
+  __AUTH_CONST.__cfstring: 0xe9a0
+  __AUTH_CONST.__objc_const: 0x45eb8
   __AUTH.__thread_vars: 0x18
   __AUTH.__thread_bss: 0x1
-  __DATA.__objc_ivar: 0x1008
+  __DATA.__objc_ivar: 0x1000
   __DATA.__data: 0x3970
   __DATA.__bss: 0x80
   __DATA_DIRTY.__objc_data: 0x48d0

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 766F137B-2F57-3893-B68C-3C0F0854A3B6
-  Functions: 7757
-  Symbols:   24570
-  CStrings:  11101
+  UUID: 0B432742-79E7-3533-9B86-35E6AE79A9F5
+  Functions: 7750
+  Symbols:   24553
+  CStrings:  11090
 
Symbols:
+ -[MTL4ToolsMachineLearningPipelineState device]
+ GCC_except_table151
+ GCC_except_table205
+ GCC_except_table209
- -[MTLDebugDevice tensorSizeAndAlignWithDescriptor:]
- -[MTLDebugTensor initWithBaseObject:buffer:]
- -[MTLDebugTensor initWithBaseObject:parentTensor:]
- -[MTLDebugTensor lockPurgeableState]
- -[MTLDebugTensor purgeableStateValidForRendering]
- -[MTLDebugTensor setPurgeableState:]
- -[MTLDebugTensor unlockPurgeableState]
- GCC_except_table202
- _OBJC_IVAR_$_MTLDebugTensor._purgeableStateHasBeenSet
- _OBJC_IVAR_$_MTLDebugTensor._purgeableStateToken
- __OBJC_$_INSTANCE_VARIABLES_MTLDebugTensor
- __validateRTDescriptorCompatibility
CStrings:
- "-[MTL4DebugComputeCommandEncoder _validateThreadsPerThreadgroupCommon:threadsPerThreadgroup:]"
- "-[MTLDebugDevice tensorSizeAndAlignWithDescriptor:]"
- "-[MTLDebugTensor setPurgeableState:]"
- "Acceleration Structure Descriptor Validation"
- "Tensor Descriptor Validation"
- "Tensor Validation"
- "_validateRTDescriptorCompatibility"
- "strides should not be nil."
- "this device does not support Metal 4 ray tracing."

```
