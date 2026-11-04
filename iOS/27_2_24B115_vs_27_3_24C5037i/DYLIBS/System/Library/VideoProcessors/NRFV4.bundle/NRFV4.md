## NRFV4

> `/System/Library/VideoProcessors/NRFV4.bundle/NRFV4`

```diff

-764.42.8.0.0
-  __TEXT.__text: 0x27b420
-  __TEXT.__objc_methlist: 0x14850
+764.60.7.0.2
+  __TEXT.__text: 0x27b614
+  __TEXT.__objc_methlist: 0x14860
   __TEXT.__const: 0x1032a0
-  __TEXT.__cstring: 0x37051
-  __TEXT.__oslogstring: 0x21e64
+  __TEXT.__cstring: 0x370a6
+  __TEXT.__oslogstring: 0x21ecd
   __TEXT.__gcc_except_tab: 0x1860
   __TEXT.__dlopen_cstrs: 0x10c
-  __TEXT.__unwind_info: 0xb3f0
+  __TEXT.__unwind_info: 0xb3f8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x14f8
+  __DATA_CONST.__const: 0x1500
   __DATA_CONST.__objc_classlist: 0xf28
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x78d0
+  __DATA_CONST.__objc_selrefs: 0x78d8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0xbe8
-  __DATA_CONST.__objc_arraydata: 0xfe0
+  __DATA_CONST.__objc_arraydata: 0x1048
   __DATA_CONST.__got: 0xfa0
-  __AUTH_CONST.__const: 0x9e0
-  __AUTH_CONST.__cfstring: 0x15f40
+  __AUTH_CONST.__const: 0x9c0
+  __AUTH_CONST.__cfstring: 0x15f60
   __AUTH_CONST.__objc_const: 0x40508
   __AUTH_CONST.__objc_floatobj: 0x140
   __AUTH_CONST.__objc_doubleobj: 0xa0
   __AUTH_CONST.__objc_arrayobj: 0xd68
   __AUTH_CONST.__objc_intobj: 0xa38
-  __AUTH_CONST.__objc_dictobj: 0x500
+  __AUTH_CONST.__objc_dictobj: 0x528
   __AUTH_CONST.__auth_got: 0x888
   __AUTH.__objc_data: 0xff0
   __DATA.__objc_ivar: 0x445c

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 15305
-  Symbols:   15796
-  CStrings:  9038
+  Functions: 15306
+  Symbols:   15797
+  CStrings:  9042
 
Symbols:
+ -[RawNightModeInferenceEspresso planSubmitCompletedWithErrorInfo:]
+ ___block_descriptor_40_e8_32s_e15_v16?0^{?=ii*}8ls32l8
- ___block_descriptor_32_e15_v16?0^{?=ii*}8l
Functions:
~ -[H13FastRawScaleConfig(PDC) _fillProcessFocusPixelsConfigWithPDPConfig:args:gainAdj:] : 2520 -> 2588
~ -[H13FastRawScaleStage(PDC) runPDCWithArgs:inputTex:outputTex:] : 5260 -> 5268
~ -[RawNightModeTiledInferenceProvider runInference] : 3188 -> 3276
~ ___50-[RawNightModeTiledInferenceProvider runInference]_block_invoke.86 : 4 -> 12
~ ___48-[RawNightModeTiledInferenceProvider resetState]_block_invoke : 12 -> 16
+ -[RawNightModeInferenceEspresso planSubmitCompletedWithErrorInfo:]
CStrings:
+ "-"
+ "-[RawNightModeInferenceEspresso planSubmitCompletedWithErrorInfo:]"
+ "<<<< RawNightMode >>>> %s: espresso_plan_submit completed with error status=%{public}d, desc=%{private}s"
+ "rbReplaceRobust"
```
