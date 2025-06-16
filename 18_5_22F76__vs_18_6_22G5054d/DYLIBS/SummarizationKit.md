## SummarizationKit

> `/System/Library/PrivateFrameworks/SummarizationKit.framework/SummarizationKit`

```diff

-1.5.5.0.0
-  __TEXT.__text: 0x13fc9c
-  __TEXT.__auth_stubs: 0x36d0
-  __TEXT.__const: 0x7788
-  __TEXT.__cstring: 0x600e
-  __TEXT.__constg_swiftt: 0x1e50
-  __TEXT.__swift5_typeref: 0x2188
-  __TEXT.__swift5_reflstr: 0x2f9e
+1.6.3.0.0
+  __TEXT.__text: 0x1446cc
+  __TEXT.__auth_stubs: 0x3730
+  __TEXT.__const: 0x7db8
+  __TEXT.__cstring: 0x5fce
+  __TEXT.__constg_swiftt: 0x1e70
+  __TEXT.__swift5_typeref: 0x21c8
+  __TEXT.__swift5_reflstr: 0x2f4e
   __TEXT.__swift5_fieldmd: 0x232c
   __TEXT.__swift5_builtin: 0x8c
   __TEXT.__swift5_assocty: 0x380
-  __TEXT.__swift5_capture: 0x173c
-  __TEXT.__oslogstring: 0x43f3
+  __TEXT.__swift5_capture: 0x139c
+  __TEXT.__oslogstring: 0x4483
   __TEXT.__swift5_proto: 0x4f8
   __TEXT.__swift5_types: 0x1f0
-  __TEXT.__swift_as_entry: 0x308
-  __TEXT.__swift_as_ret: 0x3a8
+  __TEXT.__swift_as_entry: 0x304
+  __TEXT.__swift_as_ret: 0x3a4
   __TEXT.__swift5_protos: 0x54
   __TEXT.__swift5_mpenum: 0x1c
-  __TEXT.__unwind_info: 0x4690
-  __TEXT.__eh_frame: 0xaa60
+  __TEXT.__unwind_info: 0x4708
+  __TEXT.__eh_frame: 0xaa28
   __TEXT.__objc_methname: 0x438
-  __DATA_CONST.__got: 0xa80
-  __DATA_CONST.__const: 0x2e8
+  __DATA_CONST.__got: 0xa70
+  __DATA_CONST.__const: 0x318
   __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x190
-  __AUTH_CONST.__auth_got: 0x1b68
-  __AUTH_CONST.__const: 0x4f60
-  __AUTH_CONST.__objc_const: 0x1e80
+  __AUTH_CONST.__auth_got: 0x1b98
+  __AUTH_CONST.__const: 0x4e30
+  __AUTH_CONST.__objc_const: 0x1e20
   __AUTH.__objc_data: 0xe8
-  __AUTH.__data: 0x890
-  __DATA.__data: 0x15e0
+  __AUTH.__data: 0x9b8
+  __DATA.__data: 0xeb8
   __DATA.__common: 0x80
-  __DATA.__bss: 0x5200
+  __DATA.__bss: 0x51c0
   __DATA_DIRTY.__objc_data: 0x300
-  __DATA_DIRTY.__data: 0x4008
+  __DATA_DIRTY.__data: 0x3fd0
   __DATA_DIRTY.__bss: 0x3400
   __DATA_DIRTY.__common: 0x398
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 0F13FE3C-7B83-3CFC-8E07-39CD31242D26
+  UUID: C880DEB5-9E1B-3E04-891A-5EC8060AFAE8
   Functions: 5827
-  Symbols:   1381
+  Symbols:   1378
   CStrings:  757
 
Symbols:
+ ___swift_assign_boxed_opaque_existential_0
+ _objectdestroy.179Tm
+ _objectdestroy.192Tm
+ _objectdestroy.23Tm
+ _objectdestroy.36Tm
+ _objectdestroy.73Tm
+ _objectdestroy.83Tm
+ _symbolic _____Sg 10Foundation13URLComponentsV
+ _symbolic _____Sg 10Foundation4UUIDV
+ _symbolic ______pSg 12ModelCatalog19AssetBackedResourceP
+ _symbolic ______pSg 12ModelCatalog21AssetBackedLLMAdapterP
+ _symbolic _____y_____SbG 16SummarizationKit23ErrorContextPropertyKeyV AA014ClassificationC0V
+ _symbolic _____y_____SbG 16SummarizationKit23ErrorContextPropertyKeyV AA0aC0V
+ _symbolic _____y__________G 16SummarizationKit23ErrorContextPropertyKeyV AA014ClassificationC0V 29GenerativeFunctionsFoundation0hC0V06PromptC0V0C4TypeO014SafetyRejectedC4InfoV17ViolationCategoryO
+ _symbolic _____y__________G 16SummarizationKit23ErrorContextPropertyKeyV AA0aC0V 29GenerativeFunctionsFoundation0gC0V06PromptC0V0C4TypeO014SafetyRejectedC4InfoV17ViolationCategoryO
+ _symbolic _____yypG s23_ContiguousArrayStorageC
- ___swift_memcpy52_8
- ___swift_memcpy76_8
- _objectdestroy.191Tm
- _objectdestroy.240Tm
- _objectdestroy.29Tm
- _objectdestroy.43Tm
- _objectdestroy.90Tm
- _objectdestroy.92Tm
- _symbolic SS3key_yp5valuet
- _symbolic ______p 12ModelCatalog0B8ResourceP
- _symbolic ______p 12ModelCatalog19AssetBackedResourceP
- _symbolic ______pSg 12ModelCatalog0B8ResourceP
- _type_layout_string 16SummarizationKit0A14RequestHandlerC0C4InfoV
- _type_layout_string 16SummarizationKit28ClassificationRequestHandlerC0D4InfoV
CStrings:
+ "Error fetching asset for %{public}s: %{public}@"
+ "Error fetching version number for %{public}s: %{public}@"
+ "StringSanitizationUtils.shouldThrowError returning true for [requestIdentifier: %s, useCaseIdentifier: %s]; hasRegionalSource = %{bool}d, shouldThrowErrorIfFinalDecisionUnsafe = %{bool}d"
+ "safetyErrorHasRegionalSource"
+ "safetyErrorViolationCategory"
- ", modelBundleIdentifier: "
- "Will throw safety error for [requestIdentifier: %s, useCaseIdentifier: %s]; hasRegionalSource = %{bool}d, shouldThrowErrorIfFinalDecisionUnsafe = %{bool}d"
- "_isInputSanitized"
- "_isOutputSanitized"
- "_latencyInputSanitization"

```
