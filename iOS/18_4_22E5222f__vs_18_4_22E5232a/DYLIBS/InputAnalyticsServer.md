## InputAnalyticsServer

> `/System/Library/PrivateFrameworks/InputAnalyticsServer.framework/InputAnalyticsServer`

```diff

-64.314.0.0.0
-  __TEXT.__text: 0x31aa8
-  __TEXT.__auth_stubs: 0xb40
-  __TEXT.__objc_methlist: 0x2784
+64.315.0.0.0
+  __TEXT.__text: 0x336a8
+  __TEXT.__auth_stubs: 0xbb0
+  __TEXT.__objc_methlist: 0x282c
   __TEXT.__const: 0x1e0
-  __TEXT.__cstring: 0x2669
-  __TEXT.__oslogstring: 0x3b36
+  __TEXT.__cstring: 0x2699
+  __TEXT.__oslogstring: 0x3c26
   __TEXT.__gcc_except_tab: 0x2a8
   __TEXT.__swift5_typeref: 0xf5
   __TEXT.__swift5_capture: 0x88

   __TEXT.__swift5_types: 0x8
   __TEXT.__swift_as_entry: 0x1c
   __TEXT.__swift_as_ret: 0x1c
-  __TEXT.__unwind_info: 0x9c8
+  __TEXT.__unwind_info: 0x9e8
   __TEXT.__eh_frame: 0x2e8
-  __TEXT.__objc_classname: 0x544
-  __TEXT.__objc_methname: 0x60b2
+  __TEXT.__objc_classname: 0x545
+  __TEXT.__objc_methname: 0x6309
   __TEXT.__objc_methtype: 0x852
-  __TEXT.__objc_stubs: 0x4aa0
-  __DATA_CONST.__got: 0xb38
-  __DATA_CONST.__const: 0xa18
+  __TEXT.__objc_stubs: 0x4c60
+  __DATA_CONST.__got: 0xb68
+  __DATA_CONST.__const: 0xa70
   __DATA_CONST.__objc_classlist: 0x178
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1500
+  __DATA_CONST.__objc_selrefs: 0x1580
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xf8
   __DATA_CONST.__objc_arraydata: 0xb8
-  __AUTH_CONST.__auth_got: 0x5b0
+  __AUTH_CONST.__auth_got: 0x5e8
   __AUTH_CONST.__auth_ptr: 0xb8
   __AUTH_CONST.__const: 0x9b8
-  __AUTH_CONST.__cfstring: 0x29a0
-  __AUTH_CONST.__objc_const: 0x4640
+  __AUTH_CONST.__cfstring: 0x2a80
+  __AUTH_CONST.__objc_const: 0x4760
   __AUTH_CONST.__objc_arrayobj: 0xf0
-  __AUTH_CONST.__objc_intobj: 0x708
+  __AUTH_CONST.__objc_intobj: 0x720
   __AUTH.__objc_data: 0x4a0
   __AUTH.__data: 0x50
-  __DATA.__objc_ivar: 0x338
-  __DATA.__data: 0x3b0
+  __DATA.__objc_ivar: 0x34c
+  __DATA.__data: 0x3b8
   __DATA.__bss: 0x120
   __DATA_DIRTY.__objc_data: 0xa50
   __DATA_DIRTY.__bss: 0x1b0

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 1172
-  Symbols:   480
-  CStrings:  1832
+  Functions: 1193
+  Symbols:   489
+  CStrings:  1865
 
Symbols:
+ _IAPayloadKeySmartRepliesInputTokenCount
+ _IAPayloadKeySmartRepliesOutputTokenCount
+ _IAPayloadKeyWritingToolsInputTextTokenCount
+ _IAPayloadKeyWritingToolsOutputTextTokenCount
+ _OBJC_CLASS_$_NSCharacterSet
+ _OBJC_CLASS_$_NSJSONSerialization
+ _bzero
+ _objc_retain_x28
+ _swift_arrayInitWithCopy
CStrings:
+ "\t\x11"
+ "\x14\x13\x15\x11\x11\x12"
+ "\x17\x11\x135U"
+ "1"
+ "@80@0:8q16@24@32q40@48@56@64@72"
+ "Feedback initiated - model language: %s"
+ "T@\"NSNumber\",C,N,V_inputTokenCount"
+ "T@\"NSNumber\",C,N,V_outputTokenCount"
+ "T@\"NSString\",C,N,V_cachedDetectedModelLanguage"
+ "[%{private}@] cacheDetectedModelLanguageForPayload: Unexpected nil payload"
+ "[%{private}@] cacheDetectedModelLanguageForPayload: cachedDetectedModelLanguage '%{sensitive}@ -> %{sensitive}@"
+ "_cachedDetectedModelLanguage"
+ "_inputTokenCount"
+ "_outputTokenCount"
+ "answer"
+ "base reply"
+ "cacheDetectedModelLanguageForPayload:"
+ "cachedDetectedModelLanguage"
+ "dataWithJSONObject:options:error:"
+ "detectedModelLanguage"
+ "final reply"
+ "initWithData:encoding:"
+ "initWithFeatureDomain:bundleId:sceneId:action:originalContent:generatedContent:modelInfo:detectedModelLanguage:"
+ "inputTokenCount"
+ "integerValue"
+ "mutableCopy"
+ "options"
+ "outputTokenCount"
+ "outputTokenLength"
+ "outputTokenLengthRaw"
+ "question"
+ "questionnaire"
+ "selected"
+ "serializeDictionaryToJSON:"
+ "setCachedDetectedModelLanguage:"
+ "setDetectedModelLanguage:"
+ "setInputTokenCount:"
+ "setOutputTokenCount:"
+ "shown"
+ "stringByTrimmingCharactersInSet:"
+ "version"
+ "whitespaceAndNewlineCharacterSet"
+ "{}"
- "\b\x11"
- "\x14\x13\x15\x11\x11"
- "\x17\x11\x135S"
- "- Question: %@ Options: %@ Answer: %@"
- "@72@0:8q16@24@32q40@48@56@64"
- "Base reply: %@"
- "Final reply: %@"
- "Selected: %@"
- "Shown: %@"
- "com.apple.Emporda"
- "initWithFeatureDomain:bundleId:sceneId:action:originalContent:generatedContent:modelInfo:"

```
