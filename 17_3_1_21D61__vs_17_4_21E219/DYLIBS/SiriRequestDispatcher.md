## SiriRequestDispatcher

> `/System/Library/PrivateFrameworks/SiriRequestDispatcher.framework/SiriRequestDispatcher`

```diff

-3302.11.1.0.0
-  __TEXT.__text: 0x1cd40
-  __TEXT.__auth_stubs: 0xe80
+3304.73.1.0.0
+  __TEXT.__text: 0x1e48c
+  __TEXT.__auth_stubs: 0xec0
   __TEXT.__objc_methlist: 0x38
-  __TEXT.__const: 0xa7a
-  __TEXT.__cstring: 0x2203
-  __TEXT.__swift5_typeref: 0x660
-  __TEXT.__constg_swiftt: 0xa14
-  __TEXT.__swift5_fieldmd: 0x3d8
-  __TEXT.__swift5_types: 0x60
+  __TEXT.__const: 0xaba
+  __TEXT.__cstring: 0x25c3
+  __TEXT.__swift5_typeref: 0x694
+  __TEXT.__constg_swiftt: 0xa30
+  __TEXT.__swift5_fieldmd: 0x3e8
+  __TEXT.__swift5_types: 0x64
   __TEXT.__swift5_reflstr: 0x44b
   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_proto: 0x2c
-  __TEXT.__swift5_capture: 0x230
+  __TEXT.__swift5_capture: 0x250
   __TEXT.__swift5_protos: 0xc
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x660
-  __TEXT.__eh_frame: 0x1b0
+  __TEXT.__unwind_info: 0x654
+  __TEXT.__eh_frame: 0x190
   __TEXT.__objc_classname: 0x96
-  __TEXT.__objc_methname: 0xf75
-  __TEXT.__objc_methtype: 0x5e7
-  __DATA_CONST.__got: 0x160
+  __TEXT.__objc_methname: 0xfe6
+  __TEXT.__objc_methtype: 0x625
+  __DATA_CONST.__got: 0x158
   __DATA_CONST.__const: 0x1e8
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x10f8
-  __DATA_CONST.__objc_selrefs: 0x290
-  __AUTH_CONST.__const: 0xf38
+  __DATA_CONST.__objc_const: 0x1118
+  __DATA_CONST.__objc_selrefs: 0x2d8
+  __DATA_CONST.__objc_protorefs: 0x50
+  __DATA_CONST.__objc_classrefs: 0x100
+  __AUTH_CONST.__const: 0xfd8
   __AUTH_CONST.__auth_ptr: 0x58
-  __AUTH_CONST.__auth_got: 0x740
-  __AUTH.__data: 0x138
+  __AUTH_CONST.__auth_got: 0x760
+  __AUTH.__data: 0x50
   __AUTH.__objc_data: 0xb0
-  __DATA.__objc_protorefs: 0x50
-  __DATA.__objc_classrefs: 0xf0
-  __DATA.__data: 0x608
+  __DATA.__data: 0x780
   __DATA.__bss: 0x300
+  __DATA.__common: 0x10
   __DATA_DIRTY.__objc_data: 0x50
-  __DATA_DIRTY.__data: 0x7e0
+  __DATA_DIRTY.__data: 0x910
   __DATA_DIRTY.__common: 0x68
   __DATA_DIRTY.__bss: 0x180
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 873
-  Symbols:   840
-  CStrings:  375
+  Functions: 919
+  Symbols:   873
+  CStrings:  405
 
Symbols:
+ _OBJC_CLASS_$_NSError
+ _OBJC_CLASS_$_NSJSONSerialization
+ _OUTLINED_FUNCTION_44
+ _OUTLINED_FUNCTION_45
+ _OUTLINED_FUNCTION_46
+ _OUTLINED_FUNCTION_47
+ _OUTLINED_FUNCTION_48
+ _OUTLINED_FUNCTION_49
+ _symbolic So18SAConfidenceScoresC
+ _symbolic So26AFVoiceIdScoreCardMutating_pSgIgg_
+ _symbolic _____ 21SiriRequestDispatcher24ResultCandidateConstantsO
- _objectdestroy.30Tm
- _swift_arrayInitWithCopy
- _symbolic SaySSG
- _symbolic _____ySSG s23_ContiguousArrayStorageC
CStrings:
+ "Fatal error"
+ "Insufficient space allocated to copy string contents"
+ "Not sending VoiceIdentificationSignal in case of server fallback"
+ "Swift/ContiguousArrayBuffer.swift"
+ "Swift/StringTesting.swift"
+ "Swift/StringUTF8View.swift"
+ "Swift/UnsafeBufferPointer.swift"
+ "Swift/UnsafePointer.swift"
+ "Swift/UnsafeRawPointer.swift"
+ "T@\"NSString\",?,R,C"
+ "Unexpectedly found nil while unwrapping an Optional value"
+ "UnsafeMutableBufferPointer with negative count"
+ "UnsafeMutablePointer.initialize overlapping range"
+ "UnsafeMutablePointer.initialize with negative count"
+ "UnsafeMutablePointer.moveInitialize with negative count"
+ "UnsafeMutableRawPointer.initializeMemory overlapping range"
+ "UnsafeMutableRawPointer.initializeMemory with negative count"
+ "[ServerFallbackUtils] shouldDisableServerFallback returns %{bool}d with disabledByFeatureFlag = %{bool}d and disabledByABExperiment = %{bool}d for requestId: %s and locale %{public}s"
+ "dataWithJSONObject:options:error:"
+ "dispatch command %s to the handle method"
+ "fetchDeviceAndUserIdsForSharedUserId:withCallback:"
+ "initWithBuilder:"
+ "invalid Collection: less than 'count' elements in collection"
+ "setSpIdAssetVersion:"
+ "setSpIdAudioProcessedDuration:"
+ "setSpIdKnownUserScores:"
+ "setSpIdScoreThresholdingType:"
+ "setSpIdUnknownUserScore:"
+ "setSpIdUserScoresVersion:"
+ "setUserClassified:"
+ "v16@?0@\"<AFVoiceIdScoreCardMutating>\"8"
+ "v32@0:8@\"NSString\"16@?<v@?@\"<AFAnalyticsDeviceAndUserIds>\">24"
+ "{\"result\":\"Error in converting JSON "
+ "{\"result\":\"json serialization return nil object for params "
- "Not sending VoiceIdenfiticationSignal in case of server fallback"
- "[ServerFallbackUtils] shouldDisableServerFallback returns %{bool}d with disabledByFeatureFlag = %{bool}d and disabledByABExperiment = %{bool}d for requestId: %s and locale %s"
- "dispatch commnad %s to the handle method"
- "initWithSpIdAudioProcessedDuration:spIdUnknownUserScore:spIdKnownUserScores:spIdUserScoresVersion:spIdScoreThresholdingType:spIdAssetVersion:userClassified:userIdentityClassification:"

```
