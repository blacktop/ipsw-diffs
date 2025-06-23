## GenerativeFunctionsInstrumentation

> `/System/Library/PrivateFrameworks/GenerativeFunctionsInstrumentation.framework/GenerativeFunctionsInstrumentation`

```diff

-198.1.102.0.0
-  __TEXT.__text: 0x5233c
-  __TEXT.__auth_stubs: 0x26c0
+202.0.2.0.0
+  __TEXT.__text: 0x50520
+  __TEXT.__auth_stubs: 0x2660
   __TEXT.__objc_methlist: 0x64
-  __TEXT.__cstring: 0x2a3b
-  __TEXT.__swift5_typeref: 0xd2f
-  __TEXT.__swift5_fieldmd: 0xc34
-  __TEXT.__const: 0x14f8
-  __TEXT.__constg_swiftt: 0xb84
+  __TEXT.__cstring: 0x2557
+  __TEXT.__const: 0x14b8
+  __TEXT.__constg_swiftt: 0xb48
+  __TEXT.__swift5_typeref: 0xd11
+  __TEXT.__swift5_fieldmd: 0xb70
   __TEXT.__swift5_builtin: 0x28
-  __TEXT.__swift5_reflstr: 0xfb2
-  __TEXT.__swift5_protos: 0x18
-  __TEXT.__swift5_types: 0xbc
+  __TEXT.__swift5_reflstr: 0xe57
   __TEXT.__swift5_capture: 0x230
+  __TEXT.__swift5_types: 0xb8
+  __TEXT.__oslogstring: 0x20fa
+  __TEXT.__swift5_protos: 0x18
   __TEXT.__swift5_proto: 0xa8
   __TEXT.__swift_as_entry: 0x1c
   __TEXT.__swift_as_ret: 0x14
-  __TEXT.__oslogstring: 0x2296
   __TEXT.__swift5_assocty: 0xb0
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0xef8
-  __TEXT.__eh_frame: 0x13b8
+  __TEXT.__unwind_info: 0xf10
+  __TEXT.__eh_frame: 0x13f0
   __TEXT.__objc_classname: 0x1f
   __TEXT.__objc_methname: 0x469
   __TEXT.__objc_methtype: 0x2e
   __TEXT.__objc_stubs: 0x20
-  __DATA_CONST.__got: 0x6a8
-  __DATA_CONST.__const: 0x110
-  __DATA_CONST.__objc_classlist: 0xb0
+  __DATA_CONST.__got: 0x678
+  __DATA_CONST.__const: 0xf0
+  __DATA_CONST.__objc_classlist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x188
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x1368
+  __AUTH_CONST.__auth_got: 0x1338
   __AUTH_CONST.__const: 0xfc8
-  __AUTH_CONST.__objc_const: 0x1a70
+  __AUTH_CONST.__objc_const: 0x17f8
   __AUTH.__objc_data: 0xf0
-  __AUTH.__data: 0xcd8
+  __AUTH.__data: 0xbc8
   __DATA.__objc_ivar: 0x10
-  __DATA.__data: 0x680
+  __DATA.__data: 0x668
   __DATA.__bss: 0x810
-  __DATA.__common: 0x148
+  __DATA.__common: 0x108
   __DATA_DIRTY.__objc_data: 0xf0
   __DATA_DIRTY.__data: 0xc18
-  __DATA_DIRTY.__bss: 0x700
   __DATA_DIRTY.__common: 0x90
+  __DATA_DIRTY.__bss: 0x700
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CryptoKit.framework/CryptoKit

   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: F2D77AEF-641A-378D-8A9D-1416188063A7
-  Functions: 1729
-  Symbols:   190
-  CStrings:  444
+  UUID: 10584331-8CC9-3132-8D44-AA5ED62ED069
+  Functions: 1705
+  Symbols:   186
+  CStrings:  407
 
Symbols:
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
CStrings:
- "GenerativeFunctionPerformanceProcessor: ill-formed valiator event %s"
- "GenerativeFunctionPerformanceProcessor: missing generativeFunctionIdentifier for %s"
- "GenerativeFunctionPerformanceProcessor: no matching event for %s"
- "GenerativeFunctionPerformanceProcessor: unexpected outcomeType for %s"
- "GenerativeFunctionPerformanceProcessor: unexpected validatorType for %s"
- "_TtCCC34GenerativeFunctionsInstrumentation38GenerativeFunctionPerformanceProcessor24FunctionInvocationEvents22GuardrailOverrideUsage"
- "adapterModelApplied"
- "com.apple.GenerativeModels.GuardrailOverrideUsage"
- "com.apple.generativefunction.languageRecognizerGuardrail"
- "com.apple.generativefunction.languageScriptGuardrail"
- "com.apple.generativefunction.safetyGuardrail"
- "com.apple.generativefunction.safetyGuardrail.rejected"
- "com.apple.generativefunction.safetyOverride"
- "com.apple.generativefunction.safetyOverride.rejected"
- "com.apple.generativefunction.safetyOverride.removed"
- "com.apple.generativefunction.safetyOverride.replaced"
- "denyListApplied"
- "functionIdentifier"
- "inputAdapterModel"
- "inputSafetyMillis"
- "inputUsage"
- "isInputSanitized"
- "isOutputSanitized"
- "languageRecognizerGuardrailBegin"
- "languageScriptGuardrailBegin"
- "latencyInputSanitization"
- "outputAdapterModel"
- "outputRejections"
- "outputSafetyMillis"
- "outputUsage"
- "ovsApplied"
- "rejections"
- "removals"
- "replaces"
- "safetyGuardrailBegin"
- "safetyOverrideBegin"
- "sensitiveContentAnalysisModelApplied"

```
