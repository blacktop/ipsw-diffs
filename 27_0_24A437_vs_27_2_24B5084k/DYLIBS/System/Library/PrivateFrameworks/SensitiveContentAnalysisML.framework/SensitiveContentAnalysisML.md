## SensitiveContentAnalysisML

> `/System/Library/PrivateFrameworks/SensitiveContentAnalysisML.framework/SensitiveContentAnalysisML`

```diff

-165.2.0.0.0
-  __TEXT.__text: 0xef89c
-  __TEXT.__objc_methlist: 0x1e54
-  __TEXT.__const: 0x1156c
-  __TEXT.__gcc_except_tab: 0x4460
-  __TEXT.__cstring: 0x3d76
-  __TEXT.__oslogstring: 0x1ee3
+165.4.0.0.0
+  __TEXT.__text: 0xf0b50
+  __TEXT.__objc_methlist: 0x1ec4
+  __TEXT.__const: 0x1157c
+  __TEXT.__gcc_except_tab: 0x4534
+  __TEXT.__cstring: 0x3e76
+  __TEXT.__oslogstring: 0x1fd3
   __TEXT.__dlopen_cstrs: 0xb0
-  __TEXT.__swift5_typeref: 0x29a7
-  __TEXT.__swift5_fieldmd: 0x2570
+  __TEXT.__swift5_typeref: 0x29cd
+  __TEXT.__swift5_fieldmd: 0x2588
   __TEXT.__constg_swiftt: 0x2bbc
-  __TEXT.__swift5_reflstr: 0x1149
+  __TEXT.__swift5_reflstr: 0x1169
   __TEXT.__swift5_builtin: 0xb4
   __TEXT.__swift5_assocty: 0x4c8
   __TEXT.__swift5_protos: 0x20

   __TEXT.__swift_as_cont: 0x574
   __TEXT.__swift5_capture: 0x43c
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x6478
-  __TEXT.__eh_frame: 0x8cd8
+  __TEXT.__unwind_info: 0x64b0
+  __TEXT.__eh_frame: 0x8ce8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x7c8
-  __DATA_CONST.__objc_classlist: 0x258
+  __DATA_CONST.__objc_classlist: 0x260
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0x1168
+  __DATA_CONST.__objc_selrefs: 0x1190
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x120
+  __DATA_CONST.__objc_superrefs: 0x128
   __DATA_CONST.__objc_arraydata: 0x1f8
-  __DATA_CONST.__got: 0x8e0
-  __AUTH_CONST.__const: 0xa5b8
+  __DATA_CONST.__got: 0x8e8
+  __AUTH_CONST.__const: 0xa5c0
   __AUTH_CONST.__cfstring: 0x1b00
-  __AUTH_CONST.__objc_const: 0x5628
+  __AUTH_CONST.__objc_const: 0x5778
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__objc_intobj: 0x138
   __AUTH_CONST.__objc_arrayobj: 0xf0
-  __AUTH_CONST.__auth_got: 0x19c0
-  __AUTH.__objc_data: 0x2d0
+  __AUTH_CONST.__auth_got: 0x19e8
+  __AUTH.__objc_data: 0x320
   __AUTH.__data: 0x4a8
-  __DATA.__objc_ivar: 0x2f4
-  __DATA.__data: 0x27e0
+  __DATA.__objc_ivar: 0x300
+  __DATA.__data: 0x27e8
   __DATA.__common: 0x98
   __DATA_DIRTY.__objc_data: 0x1740
-  __DATA_DIRTY.__data: 0x1f68
+  __DATA_DIRTY.__data: 0x1f70
   __DATA_DIRTY.__bss: 0x16f0
   __DATA_DIRTY.__common: 0xb0
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 6252
-  Symbols:   4331
-  CStrings:  795
+  Functions: 6265
+  Symbols:   4355
+  CStrings:  803
 
Symbols:
+ -[SCMLImageSanitization forceNonRegionalSafe:]
+ -[SCMLTextSanitization forceNonRegionalSafe:]
+ -[SCMLTextSanitization rawAdapterViolationLabels]
+ -[SCMLTextSanitization setRawAdapterViolationLabels:]
+ -[SCMLTextSanitizationRawLabel .cxx_destruct]
+ -[SCMLTextSanitizationRawLabel category]
+ -[SCMLTextSanitizationRawLabel initWithCategory:severity:]
+ -[SCMLTextSanitizationRawLabel severity]
+ _OBJC_CLASS_$_SCMLTextSanitizationRawLabel
+ _OBJC_IVAR_$_SCMLTextSanitization._rawAdapterViolationLabels
+ _OBJC_IVAR_$_SCMLTextSanitizationRawLabel._category
+ _OBJC_IVAR_$_SCMLTextSanitizationRawLabel._severity
+ _OBJC_METACLASS_$_SCMLTextSanitizationRawLabel
+ __OBJC_$_INSTANCE_METHODS_SCMLTextSanitizationRawLabel
+ __OBJC_$_INSTANCE_VARIABLES_SCMLTextSanitizationRawLabel
+ __OBJC_$_PROP_LIST_SCMLTextSanitizationRawLabel
+ __OBJC_CLASS_RO_$_SCMLTextSanitizationRawLabel
+ __OBJC_METACLASS_RO_$_SCMLTextSanitizationRawLabel
+ ___swift_memcpy42_8
+ _objc_msgSend$forceNonRegionalSafe:
+ _objc_msgSend$initWithCategory:severity:
+ _objc_msgSend$setRawAdapterViolationLabels:
+ _objc_sync_enter
+ _objc_sync_exit
+ _symbolic SaySo28SCMLTextSanitizationRawLabelCG
- ___swift_memcpy34_8
CStrings:
+ "SCMLImageSanitizer result has been overridden to safe=%{bool}d"
+ "SCMLTextSanitizer result has been overridden to safe=%{bool}d"
+ "Safety config useCase=%{public}s matchedPattern=%{public}s label=%{sensitive}s level=%{sensitive}s"
+ "imageSanitizer.override.nonRegional.input.safe"
+ "imageSanitizer.override.nonRegional.output.safe"
+ "nil (no matching entry had this label)"
+ "textSanitizer.override.nonRegional.input.safe"
+ "textSanitizer.override.nonRegional.output.safe"
```
