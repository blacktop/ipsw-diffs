## RawCamera

> `/System/Library/CoreServices/RawCamera.bundle/RawCamera`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_proto`
- `__TEXT.__dof_RawCamera`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__weak_got`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_floatobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__AUTH.__thread_vars`
- `__DATA_DIRTY.__objc_data`

```diff

-1814.0.0.0.0
-  __TEXT.__text: 0x229210
+1817.0.0.0.0
+  __TEXT.__text: 0x22acb0
   __TEXT.__objc_methlist: 0x2424
-  __TEXT.__const: 0x18164
-  __TEXT.__gcc_except_tab: 0x31568
-  __TEXT.__oslogstring: 0x283b
-  __TEXT.__cstring: 0x122f1
+  __TEXT.__const: 0x18504
+  __TEXT.__gcc_except_tab: 0x31838
+  __TEXT.__oslogstring: 0x2880
+  __TEXT.__cstring: 0x12401
   __TEXT.__ustring: 0x4b6
   __TEXT.__constg_swiftt: 0xa14
   __TEXT.__swift5_typeref: 0x5bf

   __TEXT.__swift5_types: 0xd8
   __TEXT.__swift5_capture: 0x4c
   __TEXT.__dof_RawCamera: 0x8f7
-  __TEXT.__unwind_info: 0xc668
+  __TEXT.__unwind_info: 0xc698
   __TEXT.__eh_frame: 0x13b8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2c10
+  __DATA_CONST.__const: 0x2c30
   __DATA_CONST.__objc_classlist: 0x240
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x10

   __DATA_CONST.__weak_got: 0x10
   __DATA_CONST.__objc_selrefs: 0x16e8
   __DATA_CONST.__objc_superrefs: 0x130
-  __DATA_CONST.__objc_arraydata: 0x3b10
+  __DATA_CONST.__objc_arraydata: 0x3b50
   __DATA_CONST.__got: 0xac8
   __AUTH_CONST.__const: 0x3c5a8
-  __AUTH_CONST.__cfstring: 0x1ac60
-  __AUTH_CONST.__objc_const: 0x6d28
+  __AUTH_CONST.__cfstring: 0x1ae00
+  __AUTH_CONST.__objc_const: 0x6dc8
   __AUTH_CONST.__weak_auth_got: 0x30
   __AUTH_CONST.__objc_arrayobj: 0x5e8
-  __AUTH_CONST.__objc_intobj: 0x3af8
+  __AUTH_CONST.__objc_intobj: 0x3b58
   __AUTH_CONST.__objc_doubleobj: 0x4e0
   __AUTH_CONST.__objc_dictobj: 0x4d58
   __AUTH_CONST.__objc_floatobj: 0xd0

   __AUTH.__data: 0x7a8
   __AUTH.__thread_vars: 0x30
   __AUTH.__thread_bss: 0x18
-  __DATA.__objc_ivar: 0x5d0
-  __DATA.__data: 0x20e60
+  __DATA.__objc_ivar: 0x5e4
+  __DATA.__data: 0x20e68
   __DATA.__bss: 0x72e0
   __DATA.__common: 0x4
   __DATA_DIRTY.__objc_data: 0xf0

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 7740
+  Functions: 7749
   Symbols:   982
-  CStrings:  4212
+  CStrings:  4225
 
CStrings:
+ "%{public}s inputInferenceDevice 'MPSGraph' requires RawCamera built with RAWCAMERA_ENABLE_MPSGRAPH=YES; the MPSGraph backend is not compiled in. Falling back to ANE."
+ "%{public}s model build failed"
+ "+[RAWDemosaicProcessorV9 getModelForCFAPattern:useQuarterRes:useAltModel:useMPSGraph:]"
+ "MPSGraph"
+ "deFujiEXR_v8"
+ "deSuperCCDSR_v8"
+ "inputFujiEXROutputSize"
+ "inputFujiEXRRawCrop"
+ "inputSuperCCDSRLayout"
+ "inputSuperCCDSROutputSize"
+ "inputSuperCCDSRRawCrop"
+ "kCGImageSourceEnableCache"
+ "rsp_FujiEXRCMOS_BG_GR"
+ "rsp_FujiEXRCMOS_GB_RG"
+ "rsp_FujiEXRCMOS_GR_BG"
+ "rsp_FujiEXRCMOS_RG_GB"
- "%{public}s EspressoWrapper build failed"
- "+[RAWDemosaicProcessorV9 getModelForCFAPattern:useQuarterRes:useAltModel:]"
- "DNGLosslessJpegUnpacker: destination pointer out of reasonable range at row %d, col %d"
```
