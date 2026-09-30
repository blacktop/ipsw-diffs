## DocumentUnderstanding

> `/System/Library/PrivateFrameworks/DocumentUnderstanding.framework/DocumentUnderstanding`

```diff

-116.0.1.0.0
-  __TEXT.__text: 0x1d6570
+116.3.0.0.0
+  __TEXT.__text: 0x1d6750
   __TEXT.__auth_stubs: 0x31e0
   __TEXT.__objc_methlist: 0x8f7c
   __TEXT.__const: 0xb718
   __TEXT.__dlopen_cstrs: 0xed
-  __TEXT.__cstring: 0xe515
-  __TEXT.__constg_swiftt: 0x5dcc
+  __TEXT.__cstring: 0xe835
+  __TEXT.__constg_swiftt: 0x5dc4
   __TEXT.__swift5_typeref: 0x2be2
   __TEXT.__swift5_reflstr: 0x44d9
   __TEXT.__swift5_fieldmd: 0x4078

   __TEXT.__swift5_assocty: 0xa38
   __TEXT.__swift5_proto: 0x7ac
   __TEXT.__swift5_types: 0x3a4
-  __TEXT.__oslogstring: 0x5bd3
+  __TEXT.__oslogstring: 0x6243
   __TEXT.__swift5_capture: 0x7b0
   __TEXT.__swift_as_entry: 0x234
   __TEXT.__swift_as_ret: 0x278
   __TEXT.__swift5_protos: 0x24
   __TEXT.__swift5_mpenum: 0x10
   __TEXT.__gcc_except_tab: 0x4238
-  __TEXT.__unwind_info: 0x79e0
-  __TEXT.__eh_frame: 0xa654
+  __TEXT.__unwind_info: 0x79d0
+  __TEXT.__eh_frame: 0xa624
   __TEXT.__objc_classname: 0x3b3
   __TEXT.__objc_methname: 0x8058
   __TEXT.__objc_methtype: 0xd87

   __AUTH_CONST.__cfstring: 0x2c0
   __AUTH_CONST.__objc_const: 0x9c18
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH.__objc_data: 0x3908
-  __AUTH.__data: 0x3958
+  __AUTH.__objc_data: 0x38b8
+  __AUTH.__data: 0x3758
   __AUTH.__thread_vars: 0x30
   __AUTH.__thread_bss: 0x9d0
   __DATA.__objc_ivar: 0x9c
-  __DATA.__data: 0x2710
-  __DATA.__bss: 0xcff8
-  __DATA.__common: 0x991
-  __DATA_DIRTY.__objc_data: 0x19e8
-  __DATA_DIRTY.__data: 0x2e60
-  __DATA_DIRTY.__bss: 0x728
-  __DATA_DIRTY.__common: 0xf0
+  __DATA.__data: 0x23b8
+  __DATA.__bss: 0xbf78
+  __DATA.__common: 0x811
+  __DATA_DIRTY.__objc_data: 0x1a38
+  __DATA_DIRTY.__data: 0x3390
+  __DATA_DIRTY.__bss: 0x17a8
+  __DATA_DIRTY.__common: 0x240
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 5F60D213-5324-3813-B6E6-7E207834EFF5
-  Functions: 13045
+  UUID: C443636C-947A-36D2-A5A3-9A4B4684677A
+  Functions: 13048
   Symbols:   872
-  CStrings:  4858
+  CStrings:  4886
 
CStrings:
+ "?"
+ "@\"NSError\""
+ "@\"NSNumber\""
+ "@\"_TtC21DocumentUnderstanding20DUFoundInEventResult\""
+ "@\"_TtC21DocumentUnderstanding21DUDocumentMessageData\""
+ "@\"_TtC21DocumentUnderstanding36DUUserInterfaceUnderstandingResponse\""
+ "DUFoundInEventClassificationImplementation: Data Detectors did not obtain Required Fields."
+ "DUFoundInEventClassificationImplementation: Document length (%ld) is less than threshold %ld."
+ "DUFoundInEventClassificationImplementation: Dominant Language is %s, not supported in %s"
+ "DUFoundInEventClassificationImplementation: Error loading NLModel: %@"
+ "DUFoundInEventClassificationImplementation: Error loading mlModel as NLModel: %@"
+ "DUFoundInEventClassificationImplementation: Language from language detector is nil, skipping model loading"
+ "DUFoundInEventClassificationImplementation: LinguisticData bundle found, loading model"
+ "DUFoundInEventClassificationImplementation: LinguisticData bundle not found, requesting download of NLAsset"
+ "DUFoundInEventClassificationImplementation: Loading classifier model from OTA for %s"
+ "DUFoundInEventClassificationImplementation: Locale not found for %s"
+ "DUFoundInEventClassificationImplementation: OTA model is already loaded and locale %s matches currently loaded model, early return."
+ "DUFoundInEventClassificationImplementation: Probability for predicting %s, Value: %s"
+ "DUFoundInEventClassificationImplementation: Successfully loaded model. Description %s"
+ "DUFoundInEventClassificationImplementation: Successfully loaded model. Model description %s"
+ "DUFoundInEventClassificationImplementation: Unable to find model URL from DocumentUnderstanding bundle."
+ "DUFoundInEventClassificationImplementation: empty emailHeadersDictionary"
+ "DUFoundInEventClassificationImplementation: empty senderEmail"
+ "DUFoundInEventClassificationImplementation: gating logic failed: %@"
+ "DUFoundInEventClassificationImplementation:isCandidateForEventExtraction"
+ "DUIDClassificationImplementation: Data Detectors detected %s"
+ "DUIDClassificationImplementation: Embedding not found for %s"
+ "DUIDClassificationImplementation: Error loading NLModel: %@"
+ "DUIDClassificationImplementation: Error loading mlModel as NLModel: %@"
+ "DUIDClassificationImplementation: LanguageRecognizer failed, skipping multilingual model loading"
+ "DUIDClassificationImplementation: LinguisticData bundle found, loading model"
+ "DUIDClassificationImplementation: LinguisticData bundle not found, requesting download of NLAsset"
+ "DUIDClassificationImplementation: OTA model is already loaded and locale %s matches currently loaded model, early return."
+ "DUIDClassificationImplementation: Probability for predicting %s, Value: %s"
+ "DUIDClassificationImplementation: Unable to find model URL from DocumentUnderstanding bundle."
+ "DUIDClassificationImplementation: isFoundInUseLLMExtendedLanguagesEnabled is disabled. loading english OTA by default"
+ "DUIDClassificationImplementation: isFoundInUseLLMExtendedLanguagesEnabled is enabled, Loading OTA asset"
+ "d"
+ "f"
+ "q"
+ "{CGPoint=dd}"
+ "{CGRect={CGPoint=dd}{CGSize=dd}}"
- "DUFoundInEventClassificationImplementation"
- "DUFoundInEventClassificationImplementation: unknown document type received"
- "DUFoundInEventClassificationImplementation:isMailOrMessageCandidateForEventExtraction"
- "DUIDClassificationImplementation"
- "Data Detectors detected %s"
- "Data Detectors did not obtain Required Fields."
- "Document length (%ld) is less than threshold %ld."
- "DocumentUnderstanding/DUFoundInEventClassificationImplementation.swift"
- "Dominant Language is %s, not supported in %s"
- "Embedding not found for %s"
- "Error loading NLModel: %@"
- "Error loading mlModel as NLModel: %@"
- "Language from language detector is nil, skipping model loading"
- "LanguageRecognizer failed, skipping multilingual model loading"
- "LinguisticData bundle found, loading model"
- "LinguisticData bundle not found, requesting download of NLAsset"
- "Loading classifier model from OTA for %s"
- "Locale not found for %s"
- "OTA model is already loaded and locale %s matches currently loaded model, early return."
- "Probability for predicting %s, Value: %s"
- "Successfully loaded model. Description %s"
- "Successfully loaded model. Model description %s"
- "Unable to find model URL from DocumentUnderstanding bundle."
- "empty emailHeadersDictionary"
- "empty senderEmail"
- "gating logic failed: %@"
- "isFoundInUseLLMExtendedLanguagesEnabled is disabled. loading english OTA by default"
- "isFoundInUseLLMExtendedLanguagesEnabled is enabled, Loading OTA asset"

```
