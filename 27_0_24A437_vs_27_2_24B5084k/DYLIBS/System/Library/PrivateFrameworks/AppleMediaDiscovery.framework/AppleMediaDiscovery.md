## AppleMediaDiscovery

> `/System/Library/PrivateFrameworks/AppleMediaDiscovery.framework/AppleMediaDiscovery`

```diff

-1.5.6.0.0
-  __TEXT.__text: 0xf1258
-  __TEXT.__objc_methlist: 0x3b60
+1.5.7.0.0
+  __TEXT.__text: 0xef1b0
+  __TEXT.__objc_methlist: 0x3af8
   __TEXT.__const: 0xba8
-  __TEXT.__cstring: 0xac68
-  __TEXT.__oslogstring: 0x46f7
-  __TEXT.__gcc_except_tab: 0x28f0
+  __TEXT.__cstring: 0xaa08
+  __TEXT.__oslogstring: 0x4617
+  __TEXT.__gcc_except_tab: 0x28ac
   __TEXT.__dlopen_cstrs: 0xcc
   __TEXT.__swift5_typeref: 0x5a8
   __TEXT.__swift5_capture: 0x75c

   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_assocty: 0xd8
   __TEXT.__swift5_proto: 0x4c
-  __TEXT.__unwind_info: 0x2370
+  __TEXT.__unwind_info: 0x2358
   __TEXT.__eh_frame: 0x798
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xda8
-  __DATA_CONST.__objc_classlist: 0x2e8
+  __DATA_CONST.__const: 0xd80
+  __DATA_CONST.__objc_classlist: 0x2d0
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2808
+  __DATA_CONST.__objc_selrefs: 0x27b8
   __DATA_CONST.__objc_superrefs: 0x110
-  __DATA_CONST.__objc_arraydata: 0x12c0
-  __DATA_CONST.__got: 0x6d8
+  __DATA_CONST.__objc_arraydata: 0x12b0
+  __DATA_CONST.__got: 0x6a8
   __AUTH_CONST.__const: 0x13c0
-  __AUTH_CONST.__cfstring: 0xdaa0
-  __AUTH_CONST.__objc_const: 0x62d0
-  __AUTH_CONST.__objc_intobj: 0xcf0
-  __AUTH_CONST.__objc_dictobj: 0x1068
+  __AUTH_CONST.__cfstring: 0xd760
+  __AUTH_CONST.__objc_const: 0x6120
+  __AUTH_CONST.__objc_intobj: 0xca8
+  __AUTH_CONST.__objc_dictobj: 0x1040
   __AUTH_CONST.__objc_arrayobj: 0x3d8
   __AUTH_CONST.__objc_doubleobj: 0x130
   __AUTH_CONST.__auth_got: 0xc38
-  __AUTH.__objc_data: 0x670
+  __AUTH.__objc_data: 0x580
   __AUTH.__data: 0x78
   __DATA.__objc_ivar: 0x30c
-  __DATA.__data: 0x660
+  __DATA.__data: 0x650
   __DATA.__common: 0x48
   __DATA_DIRTY.__objc_data: 0x1a10
   __DATA_DIRTY.__data: 0x220

   - /System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary
   - /System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams
   - /System/Library/PrivateFrameworks/Bom.framework/Bom
-  - /System/Library/PrivateFrameworks/CipherML.framework/CipherML
   - /System/Library/PrivateFrameworks/DistributedEvaluation.framework/DistributedEvaluation
   - /System/Library/PrivateFrameworks/ServicesIntelligence.framework/ServicesIntelligence
   - /System/Library/PrivateFrameworks/SeymourClient.framework/SeymourClient

   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
+  - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2037
-  Symbols:   3958
-  CStrings:  2394
+  Functions: 2031
+  Symbols:   3920
+  CStrings:  2361
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCoreMIDI
+ __swift_FORCE_LOAD_$_swiftCoreMIDI_$_AppleMediaDiscovery
- +[AMDJSCipherMLQueryHandler triggerPECCall:withError:]
- +[AMDJSCipherMLQueryHandler triggerPIRKVFetch:withError:]
- +[AMDJSPIRResponseHandler persistPIRData:error:]
- +[AMDPirTest testPir:]
- -[AMDClient sendPECSimilarityScores:withCallHandle:andRequestError:error:]
- -[AMDClient sendPIRData:forKeyword:withCallHandle:error:]
- _AMD_CIPHERML_CALL_HANDLE
- _AMD_CIPHERML_REQUEST_ERROR
- _AMD_PEC_SIMILARITY_SCORES_ARRAY
- _AMD_PIR_DATA_ARRAY
- _AMD_PIR_KEYWORD_ARRAY
- _AMD_PIR_MISSING_KEYWORD_ARRAY
- _OBJC_CLASS_$_AMDJSCipherMLQueryHandler
- _OBJC_CLASS_$_AMDJSPIRResponseHandler
- _OBJC_CLASS_$_AMDPirTest
- _OBJC_CLASS_$_CMLClientConfig
- _OBJC_CLASS_$_CMLKeywordPIRClient
- _OBJC_CLASS_$_CMLSimilarityScore
- _OBJC_METACLASS_$_AMDJSCipherMLQueryHandler
- _OBJC_METACLASS_$_AMDJSPIRResponseHandler
- _OBJC_METACLASS_$_AMDPirTest
- _TEST_PEC
- _TEST_PIR
- __OBJC_$_CLASS_METHODS_AMDJSCipherMLQueryHandler
- __OBJC_$_CLASS_METHODS_AMDJSPIRResponseHandler
- __OBJC_$_CLASS_METHODS_AMDPirTest
- __OBJC_CLASS_RO_$_AMDJSCipherMLQueryHandler
- __OBJC_CLASS_RO_$_AMDJSPIRResponseHandler
- __OBJC_CLASS_RO_$_AMDPirTest
- __OBJC_METACLASS_RO_$_AMDJSCipherMLQueryHandler
- __OBJC_METACLASS_RO_$_AMDJSPIRResponseHandler
- __OBJC_METACLASS_RO_$_AMDPirTest
- _objc_msgSend$asyncResponseDataByKeywords:error:
- _objc_msgSend$dataUsingEncoding:
- _objc_msgSend$initWithClientConfig:
- _objc_msgSend$initWithUseCase:
- _objc_msgSend$persistPIRData:error:
- _objc_msgSend$testPir:
- _objc_msgSend$triggerPECCall:withError:
- _objc_msgSend$triggerPIRKVFetch:withError:
CStrings:
+ "score does not respond to identifier, score and metadata"
- "Deprecated method"
- "Error deserializing PIR data for keyword %@: %@"
- "Error deserializing PIR keyword: %@"
- "KVStore cleanup failed: %@"
- "KVStore fetch failed: %@"
- "Keywords absent in PIR query payload"
- "Keywords are not an array"
- "Nil call handle present in PIR response"
- "Nil data present in PIR response"
- "Nil keyword present in PIR response"
- "Non string keyword present in PIR response"
- "PIR Error: Unrecognized call handler"
- "PIR call handle, usecase %@: %@"
- "PIR use case %@ error: %@"
- "PIRQueryPayload is nil"
- "PIRQueryPayload is not a dictionary"
- "Taste profile save failed: %@"
- "This codepath is not being used currently."
- "add_pir_call_handle"
- "callHandle"
- "keywords"
- "pirCallHandleAdd"
- "pirCallHandleAddError"
- "pirTestStatus"
- "run_pec_queries"
- "run_pir_queries"
- "savePIRData"
- "score not an instance of CMLSimilarityScore"
- "testPEC"
- "testPIR"
- "test_call_handle"
- "test_pir"
- "usecase absent in PIR query payload"
- "usecase is not a string"
```
