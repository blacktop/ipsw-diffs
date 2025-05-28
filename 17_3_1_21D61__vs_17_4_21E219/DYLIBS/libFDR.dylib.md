## libFDR.dylib

> `/usr/lib/libFDR.dylib`

```diff

-1113.80.2.0.0
-  __TEXT.__text: 0x6d260
-  __TEXT.__auth_stubs: 0x12d0
-  __TEXT.__const: 0x1f03
-  __TEXT.__cstring: 0x1e172
+1117.100.60.0.0
+  __TEXT.__text: 0x6e358
+  __TEXT.__auth_stubs: 0x12a0
+  __TEXT.__const: 0x1f0b
+  __TEXT.__cstring: 0x1e58f
   __TEXT.__ustring: 0x38
-  __TEXT.__unwind_info: 0x9c8
-  __TEXT.__objc_methname: 0x22
-  __TEXT.__objc_stubs: 0x20
+  __TEXT.__unwind_info: 0x9cc
   __DATA_CONST.__got: 0xe8
-  __DATA_CONST.__const: 0x8f8
+  __DATA_CONST.__const: 0x900
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8
-  __AUTH_CONST.__const: 0x920
-  __AUTH_CONST.__cfstring: 0xd7a0
+  __DATA_CONST.__objc_classrefs: 0x8
+  __AUTH_CONST.__const: 0x8f8
+  __AUTH_CONST.__cfstring: 0xd900
   __AUTH_CONST.__auth_ptr: 0x38
-  __AUTH_CONST.__auth_got: 0x970
-  __DATA.__objc_classrefs: 0x8
+  __AUTH_CONST.__auth_got: 0x950
   __DATA.__data: 0x158
-  __DATA.__bss: 0xe8
+  __DATA.__bss: 0xd8
   __DATA_DIRTY.__data: 0x20
-  __DATA_DIRTY.__bss: 0xc0
+  __DATA_DIRTY.__bss: 0xd0
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libamsupport.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 802
-  Symbols:   2052
-  CStrings:  3628
+  Symbols:   2045
+  CStrings:  3653
 
Symbols:
+ _AMFDRDataCreateMultiDataAsMultiResponse
+ _AMFDRDataMultiCopyDataForPatch
+ _AMFDRDataMultiPatchWithOptions
+ _AMFDREncodeMultiResponseAddRecord
+ _AMFDREncodeMultiResponseBegin
+ _AMFDREncodeMultiResponseDestroy
+ _AMFDREncodeMultiResponseEnd
+ _AMFDRSealingMapCreateLocalMultiDataBlobForClass
+ ___block_descriptor_tmp.1022
+ ___block_descriptor_tmp.1083
+ ___block_descriptor_tmp.1087
+ ___block_descriptor_tmp.1098
+ ___block_descriptor_tmp.1170
+ ___block_descriptor_tmp.1172
+ ___block_descriptor_tmp.1232
+ ___block_descriptor_tmp.1235
+ ___block_descriptor_tmp.1383
+ ___block_descriptor_tmp.840
+ ___block_descriptor_tmp.907
+ ___block_literal_global.1085
+ ___block_literal_global.1089
+ ___block_literal_global.1100
+ ___block_literal_global.1172
+ ___block_literal_global.1234
+ ___block_literal_global.1237
+ ___block_literal_global.842
+ ___block_literal_global.909
+ _calloc
+ _kAMFDRSealingMapAttributeEarlyAccessMultiData
- _AMFDRJSONCreateDictFromJson
- __AMFDRDataCheckGrammarItems
- __AMFDRDataCheckSubGrammarItems
- __AMFDRHttpMultiCopyAsidMetadataCallback
- __AMFDRHttpMultiCopyCallback
- __AMFDRHttpMultiCopyCallbackInternal
- __AMFDRHttpMultiCopyDigestCallback
- __AMFDRHttpMultiCopyManifestCallback
- ___block_descriptor_tmp.1004
- ___block_descriptor_tmp.1054
- ___block_descriptor_tmp.1058
- ___block_descriptor_tmp.1069
- ___block_descriptor_tmp.1143
- ___block_descriptor_tmp.1148
- ___block_descriptor_tmp.1203
- ___block_descriptor_tmp.1206
- ___block_descriptor_tmp.1354
- ___block_descriptor_tmp.824
- ___block_descriptor_tmp.891
- ___block_literal_global.1056
- ___block_literal_global.1060
- ___block_literal_global.1071
- ___block_literal_global.1150
- ___block_literal_global.1205
- ___block_literal_global.1208
- ___block_literal_global.826
- ___block_literal_global.893
- _kAMFDRSealingMapMaxSize
- _objc_autoreleasePoolPop
- _objc_autoreleasePoolPush
- _objc_msgSend$JSONObjectWithData:options:error:
- _objc_retain
- _objc_retain_x8
CStrings:
+ " UUID=%@"
+ "%@ has been specified in override data class, skipping this entry"
+ "%@%@%@%@%@%@"
+ "AMFDRDataCreateMultiDataAsMultiResponse"
+ "AMFDRDataMultiCopy local data missing %@"
+ "AMFDRDataMultiCopyDataForPatch"
+ "AMFDRDataMultiCopyDataForPatch failed for %@: %@"
+ "AMFDRDataMultiPatchWithOptions"
+ "AMFDREncodeMultiResponseAddRecord"
+ "AMFDREncodeMultiResponseBegin"
+ "AMFDREncodeMultiResponseEnd"
+ "AMFDRSealingMapCopyLocalData returned error: %@"
+ "AMFDRSealingMapCreateLocalMultiDataBlobForClass"
+ "CFUUIDCreate failed"
+ "CFUUIDCreateString failed for uuid: %@"
+ "DEREncoderAddDataFromEncoder failed"
+ "EarlyAccessMultiData"
+ "LocalValidation"
+ "No data found for %@"
+ "UUID"
+ "_AMFDRDecodeMultiSealingResposeRecords failed with error 0x%llX"
+ "_HttpRequestStatisticCreateString failed"
+ "action is %d"
+ "cannot get data instances for %@, skip creating data blobs..."
+ "cannot get multiResponseErrors"
+ "dataClassInstanceArray is NULL"
+ "dataInstanceEntries count mismatch"
+ "errorLength is 0"
+ "errorLength is not 0"
+ "failed to add error value"
+ "failed to add metadata value"
+ "failed to allocate mutable copy of override data class/instance array"
+ "failed to copy data for %@-%@, but data is allowed to be missing since skip sealing is enabled"
+ "failed to copy matching sealing properties"
+ "failed to create an encoded data blob for %@"
+ "failed to create currDataClassInstance string"
+ "failed to create data class instance data"
+ "failed to create data for %@-%@"
+ "multiResponseContext is NULL"
+ "optionsArray isn't supported!!"
+ "optionsFDR is NULL"
+ "recordSetEncoder is NULL"
+ "uuidStr is NULL"
+ "validation has invalid type"
- "%@%@%@%@%@"
- "JSONObjectWithData:options:error:"
- "MaxSize"
- "No subCCs key in json dict, error json file"
- "_AMFDRCheckSubCCValid"
- "_AMFDRDataCheckGrammarItems"
- "_AMFDRDataCheckSubGrammarItems"
- "_AMFDRHttpMultiCopyCallbackInternal"
- "_HttpRequestStatisticCreateString is NULL"
- "checkDict is not CFDictionary"
- "itemValue is not CFData"
- "jsonData is not CFData"
- "jsonDict is NULL"
- "keyValue is not CFNumber"
- "len:%d is not equal to lenInGrammar:%d"
- "patchDict is not CFDictionary"
- "size"
- "subCCs"
- "subCCsDict is NULL or not dictionary type"

```
