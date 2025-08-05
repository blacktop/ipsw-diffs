## PosterFoundation

> `/System/Library/PrivateFrameworks/PosterFoundation.framework/PosterFoundation`

```diff

-286.101.0.0.0
-  __TEXT.__text: 0x42658
+289.103.0.0.0
+  __TEXT.__text: 0x43230
   __TEXT.__auth_stubs: 0x1040
-  __TEXT.__objc_methlist: 0x3150
-  __TEXT.__const: 0x18e
-  __TEXT.__cstring: 0x3b43
-  __TEXT.__oslogstring: 0x305a
+  __TEXT.__objc_methlist: 0x3158
+  __TEXT.__const: 0x196
+  __TEXT.__cstring: 0x3cf9
+  __TEXT.__oslogstring: 0x30d1
   __TEXT.__gcc_except_tab: 0x10f8
-  __TEXT.__unwind_info: 0x1248
+  __TEXT.__unwind_info: 0x1258
   __TEXT.__objc_classname: 0x720
-  __TEXT.__objc_methname: 0x7458
+  __TEXT.__objc_methname: 0x7496
   __TEXT.__objc_methtype: 0x1273
-  __TEXT.__objc_stubs: 0x56a0
+  __TEXT.__objc_stubs: 0x56c0
   __DATA_CONST.__got: 0x4e8
-  __DATA_CONST.__const: 0x1350
+  __DATA_CONST.__const: 0x1330
   __DATA_CONST.__objc_classlist: 0x1a0
   __DATA_CONST.__objc_catlist: 0x78
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1d78
+  __DATA_CONST.__objc_selrefs: 0x1d80
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x178
-  __DATA_CONST.__objc_arraydata: 0x120
+  __DATA_CONST.__objc_arraydata: 0x128
   __AUTH_CONST.__auth_got: 0x830
   __AUTH_CONST.__const: 0x920
-  __AUTH_CONST.__cfstring: 0x3a60
-  __AUTH_CONST.__objc_const: 0x80c8
+  __AUTH_CONST.__cfstring: 0x3c20
+  __AUTH_CONST.__objc_const: 0x80f0
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH.__objc_data: 0x4b0
   __DATA.__objc_ivar: 0x2dc
   __DATA.__data: 0x850
-  __DATA.__bss: 0xa8
+  __DATA.__bss: 0x98
   __DATA_DIRTY.__objc_data: 0xb90
-  __DATA_DIRTY.__bss: 0x1e0
+  __DATA_DIRTY.__bss: 0x1f0
   __DATA_DIRTY.__common: 0xc
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: D42D717D-8A48-3704-8448-A23A1C8FF69C
-  Functions: 1584
-  Symbols:   5560
-  CStrings:  2802
+  UUID: 2C10F244-1116-3892-A283-85C054DBFE09
+  Functions: 1587
+  Symbols:   5567
+  CStrings:  2831
 
Symbols:
+ -[PFPosterExtensionProvider _lock_startWithImmediateQueryExecution:]
+ -[PFPosterExtensionProvider startWithImmediateQueryExecution:]
+ GCC_except_table47
+ GCC_except_table58
+ GCC_except_table60
+ GCC_except_table65
+ GCC_except_table67
+ _PFValidateDictionaryForClasses
+ _PFValidateDictionaryForPropertyListTypes
+ _PFValidationUtilitiesErrorDomain
+ __PFValidateDictionaryRecursive
+ __PFValidateObjectForClasses
+ ___block_descriptor_80_e8_32s40s48s56s64s72s_e15_v32?0816^B24ls32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_literal_global.236
+ _objc_msgSend$_lock_startWithImmediateQueryExecution:
+ _objc_msgSend$startWithImmediateQueryExecution:
- -[PFPosterExtensionProvider _lock_start]
- GCC_except_table52
- GCC_except_table59
- GCC_except_table66
- ___87-[NSDictionary(PosterFoundation) pf_sanitizeWithAllowedKeyClasses:allowedValueClasses:]_block_invoke_4
- ___87-[NSDictionary(PosterFoundation) pf_sanitizeWithAllowedKeyClasses:allowedValueClasses:]_block_invoke_5
- ___block_descriptor_40_e8_32s_e8_B16?0#8ls32l8
- ___block_descriptor_56_e8_32s40s48s_e15_v32?0816^B24ls32l8s40l8s48l8
- ___block_literal_global.235
- _objc_msgSend$_lock_start
CStrings:
+ "(%p) _lock_startWithImmediateQueryExecution"
+ "(%p) start with synchronous query execution: %{public}d"
+ "Dictionary validation failed."
+ "Expected an NSDictionary, but received an object of type %@"
+ "Expected types: "
+ "Input is not an NSDictionary."
+ "Invalid class type for key value pair: { %{public}@ : %{public}@ }; dropping from dictionary. Allowed key classes: [ %{public}@ ]. Allowed value classes: [ %{public}@ ]. Detected key class: %{public}@. Detected value class: %{public}@. Validation error: %{public}@"
+ "Invalid dictionary key type."
+ "Invalid dictionary object type."
+ "Invalid keys found: %@. "
+ "Invalid objects found: %@."
+ "No specific types allowed."
+ "Object of type '%@' is not allowed. %{public}@"
+ "PFValidationUtilitiesErrorDomain"
+ "Unknown"
+ "Unknown validation failure."
+ "_lock_startWithImmediateQueryExecution:"
+ "com.apple.transcriptBackgroundPoster.DynamicExtension"
+ "startWithImmediateQueryExecution:"
- "(%p) start"
- "B16@?0#8"
- "Invalid class type for key value pair: { %{public}@ : %{public}@ }; dropping from dictionary. Allowed key classes: [ %{public}@ ]. Allowed value classes: [ %{public}@ ]. Detected key class: %{public}@. Detected value class: %{public}@"
- "_lock_start"

```
