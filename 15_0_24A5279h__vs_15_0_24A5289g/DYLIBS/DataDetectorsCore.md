## DataDetectorsCore

> `/System/Library/PrivateFrameworks/DataDetectorsCore.framework/Versions/A/DataDetectorsCore`

```diff

-786.0.0.0.0
-  __TEXT.__text: 0x3c2ac
+789.0.0.0.0
+  __TEXT.__text: 0x3c858
   __TEXT.__auth_stubs: 0x13b0
   __TEXT.__delay_stubs: 0xdc
   __TEXT.__delay_helper: 0x2e8
-  __TEXT.__objc_methlist: 0xa88
+  __TEXT.__objc_methlist: 0xaa8
   __TEXT.__const: 0x3c4
-  __TEXT.__gcc_except_tab: 0x598
+  __TEXT.__gcc_except_tab: 0x5d4
   __TEXT.__oslogstring: 0x2070
-  __TEXT.__cstring: 0x5b99
+  __TEXT.__cstring: 0x5bd6
   __TEXT.__ustring: 0xc
   __TEXT.__unwind_info: 0xa98
   __TEXT.__objc_classname: 0x1c6
-  __TEXT.__objc_methname: 0x24b6
-  __TEXT.__objc_methtype: 0xca4
-  __TEXT.__objc_stubs: 0x24a0
+  __TEXT.__objc_methname: 0x25c6
+  __TEXT.__objc_methtype: 0xdc4
+  __TEXT.__objc_stubs: 0x2540
   __DATA_CONST.__got: 0x280
   __DATA_CONST.__const: 0xb00
   __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xae8
+  __DATA_CONST.__objc_selrefs: 0xb20
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x50
+  __DATA_CONST.__objc_superrefs: 0x58
   __DATA_CONST.__objc_arraydata: 0x540
   __AUTH_CONST.__auth_got: 0xa10
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__const: 0x12b0
-  __AUTH_CONST.__cfstring: 0x8100
-  __AUTH_CONST.__objc_const: 0x1930
+  __AUTH_CONST.__cfstring: 0x8120
+  __AUTH_CONST.__objc_const: 0x1990
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0x550
   __AUTH.__data: 0x8
-  __DATA.__objc_ivar: 0x138
+  __DATA.__objc_ivar: 0x140
   __DATA.__data: 0x1044
   __DATA.__bss: 0x30c
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxml2.2.dylib
-  Functions: 840
-  Symbols:   2171
-  CStrings:  1287
+  Functions: 844
+  Symbols:   2183
+  CStrings:  1288
 
Symbols:
+ +[DDMLTaggerModel _buildTokenToLabelMap:supportedTypes:]
+ -[DDMLTaggerModel supportedTypes]
+ -[DDMLTokenType initWithClassification:beginning:]
+ -[DDResultCluster resolvedDDResultFromOriginalQuery:mlSupportedTypes:]
+ -[DDScannerServiceConfiguration setSupportedMLResults:]
+ -[DDScannerServiceConfiguration supportedMLResults]
+ GCC_except_table114
+ GCC_except_table134
+ GCC_except_table138
+ GCC_except_table141
+ GCC_except_table212
+ GCC_except_table221
+ GCC_except_table232
+ GCC_except_table236
+ GCC_except_table261
+ GCC_except_table433
+ GCC_except_table566
+ GCC_except_table817
+ GCC_except_table92
+ GCC_except_table96
+ OBJC_IVAR_$_DDMLTaggerModel._supportedTypes
+ OBJC_IVAR_$_DDScannerServiceConfiguration._supportedMLResults
+ _DDMLClassificationForType
+ _DDResultTypeIsMLSupported
+ _DDScannerSetMLSupportedTypes
+ _NLNaturalLanguageErrorDomain
+ __58-[DDScanServerDispatcher scannerConf:sync:string:runTask:]_block_invoke.635
+ __60-[DDScanServerDispatcher recycleScanner:fromList:sameQueue:]_block_invoke.638
+ __67+[DDScannerService scanString:range:configuration:completionBlock:]_block_invoke.677
+ __72-[DDScannerObject scanString:range:query:configuration:completionBlock:]_block_invoke.183
+ __Block_byref_object_copy_.1117
+ __Block_byref_object_copy_.189
+ __Block_byref_object_copy_.247
+ __Block_byref_object_copy_.3318
+ __Block_byref_object_dispose_.1118
+ __Block_byref_object_dispose_.190
+ __Block_byref_object_dispose_.248
+ __Block_byref_object_dispose_.3319
+ __DDMLScannerGetEmbeddingAndAssetsForScriptWithCompletionHandler_block_invoke.189
+ ___56+[DDMLTaggerModel _buildTokenToLabelMap:supportedTypes:]_block_invoke
+ ___block_descriptor_48_e8_32s40s_e15_v32?0816^B24l
+ __block_descriptor_tmp.1217
+ __block_descriptor_tmp.1435
+ __block_descriptor_tmp.1638
+ __block_descriptor_tmp.1664
+ __block_descriptor_tmp.2396
+ __block_descriptor_tmp.2839
+ __block_descriptor_tmp.2934
+ __block_descriptor_tmp.364
+ __block_descriptor_tmp.663
+ __block_descriptor_tmp.839
+ __block_literal_global.1137
+ __block_literal_global.1206
+ __block_literal_global.1430
+ __block_literal_global.1569
+ __block_literal_global.1636
+ __block_literal_global.1662
+ __block_literal_global.1733
+ __block_literal_global.196.3095
+ __block_literal_global.212
+ __block_literal_global.214.3367
+ __block_literal_global.217
+ __block_literal_global.2392
+ __block_literal_global.247
+ __block_literal_global.2932
+ __block_literal_global.3311
+ __block_literal_global.332
+ __block_literal_global.340
+ __block_literal_global.362
+ __block_literal_global.42.2790
+ __block_literal_global.657
+ __block_literal_global.701
+ _gotLoadHelper_x8$_NLNaturalLanguageErrorDomain
+ _objc_msgSend$_buildTokenToLabelMap:supportedTypes:
+ _objc_msgSend$allObjects
+ _objc_msgSend$code
+ _objc_msgSend$contextualEmbeddingWithModelIdentifier:
+ _objc_msgSend$domain
+ _objc_msgSend$initWithClassification:beginning:
+ _objc_msgSend$numberWithUnsignedInt:
+ _objc_msgSend$resolvedDDResultFromOriginalQuery:mlSupportedTypes:
+ _objc_msgSend$supportedMLResults
+ _objc_msgSend$supportedTypes
- +[DDMLTaggerModel _buildTokenToLabelMap:]
- -[DDMLTokenType setBeginning:]
- -[DDMLTokenType setClassification:]
- -[DDResultCluster resolvedDDResultFromOriginalQuery:]
- GCC_except_table112
- GCC_except_table132
- GCC_except_table136
- GCC_except_table139
- GCC_except_table208
- GCC_except_table219
- GCC_except_table230
- GCC_except_table234
- GCC_except_table259
- GCC_except_table430
- GCC_except_table561
- GCC_except_table807
- GCC_except_table90
- GCC_except_table94
- _NLScriptLatin
- __58-[DDScanServerDispatcher scannerConf:sync:string:runTask:]_block_invoke.630
- __60-[DDScanServerDispatcher recycleScanner:fromList:sameQueue:]_block_invoke.633
- __67+[DDScannerService scanString:range:configuration:completionBlock:]_block_invoke.667
- __72-[DDScannerObject scanString:range:query:configuration:completionBlock:]_block_invoke.178
- __Block_byref_object_copy_.1102
- __Block_byref_object_copy_.185
- __Block_byref_object_copy_.244
- __Block_byref_object_copy_.3312
- __Block_byref_object_dispose_.1103
- __Block_byref_object_dispose_.186
- __Block_byref_object_dispose_.245
- __Block_byref_object_dispose_.3313
- __DDMLScannerGetEmbeddingAndAssetsForScriptWithCompletionHandler_block_invoke.182
- ___41+[DDMLTaggerModel _buildTokenToLabelMap:]_block_invoke
- ___block_descriptor_40_e8_32s_e15_v32?0816^B24l
- __block_descriptor_tmp.1202
- __block_descriptor_tmp.1420
- __block_descriptor_tmp.1624
- __block_descriptor_tmp.1650
- __block_descriptor_tmp.2382
- __block_descriptor_tmp.2842
- __block_descriptor_tmp.2938
- __block_descriptor_tmp.359
- __block_descriptor_tmp.656
- __block_descriptor_tmp.830
- __block_literal_global.1122
- __block_literal_global.1191
- __block_literal_global.1415
- __block_literal_global.1555
- __block_literal_global.1622
- __block_literal_global.1648
- __block_literal_global.1719
- __block_literal_global.192.2935
- __block_literal_global.206
- __block_literal_global.208.3354
- __block_literal_global.211.3359
- __block_literal_global.2378
- __block_literal_global.242
- __block_literal_global.2936
- __block_literal_global.327
- __block_literal_global.3305
- __block_literal_global.335
- __block_literal_global.357
- __block_literal_global.42.2793
- __block_literal_global.650
- __block_literal_global.696
- _gotLoadHelper_x8$_NLScriptLatin
- _objc_msgSend$_buildTokenToLabelMap:
- _objc_msgSend$contextualEmbeddingWithScript:
- _objc_msgSend$resolvedDDResultFromOriginalQuery:
- _objc_msgSend$setBeginning:
- _objc_msgSend$setClassification:
CStrings:
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/DataDetectorsCore/Sources/Automaton Compiler/DDDFAScanner.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/DataDetectorsCore/Sources/DDCache.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/DataDetectorsCore/Sources/DDScannerLoader.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/DataDetectorsCore/Sources/DDScannerResult.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/DataDetectorsCore/Sources/ICU-Patch/DDLexer.cpp"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/DataDetectorsCore/Sources/ICU-Patch/rbclass.cpp"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/DataDetectorsCore/Sources/Lookup/DDCachingStringTokenizer.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/DataDetectorsCore/Sources/Lookup/DDLookupTable.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/DataDetectorsCore/Sources/Lookup/DDStaticTrie.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/DataDetectorsCore/Sources/Lookup/DDTrie.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/DataDetectorsCore/Sources/PushDown/DDLRDispatchTable_sparse.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/DataDetectorsCore/Sources/PushDown/DDLRLightResult.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/DataDetectorsCore/Sources/PushDown/DDLexemCache.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/DataDetectorsCore/Sources/PushDown/DDPushDownAutomaton.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/DataDetectorsCore/Sources/PushDown/DDResult.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/DataDetectorsCore/Sources/PushDown/DDResultFiltering.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/DataDetectorsCore/Sources/PushDown/DDScanQuery.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/DataDetectorsCore/Sources/PushDown/DDScanner.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/DataDetectorsCore/Sources/PushDown/DDTokenCache.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/DataDetectorsCore/Sources/Utilities/DDDebugUtils.c"
+ "8075FCEB-2588-4FBD-9804-8507C9DB31E4"
+ "C44@?0^{__DDResult={__CFRuntimeBase=QAQ}{__DDQueryRange={__DDQueryOffset=b16b16b32}{__DDQueryOffset=b16b16b32}}{?=qq}q^{__CFArray}^{__CFString}^{__CFString}^v^{__CFDictionary}qCf}8^{__CFString=}16^{__DDScanner={__CFRuntimeBase=QAQ}^{__DDLRTable}^{__DDLexer}^{__DDCache}^{__DDTokenCache}^{__DDLexemCache}^{__DDScanQuery}^{__DDScanQuery}[7^{__DDLookupTable}]^{__CFString}d^{__CFData}^{DDSourceMatchCache}^{__CFArray}^{__CFArray}qqqq*@?db1b1CSC^{__CFLocale}iiC^{__CFArray}^{__CFArray}}24^{__CFString=}32C40"
+ "v24@?0^{__CFArray=}8^{__DDScanner={__CFRuntimeBase=QAQ}^{__DDLRTable}^{__DDLexer}^{__DDCache}^{__DDTokenCache}^{__DDLexemCache}^{__DDScanQuery}^{__DDScanQuery}[7^{__DDLookupTable}]^{__CFString}d^{__CFData}^{DDSourceMatchCache}^{__CFArray}^{__CFArray}qqqq*@?db1b1CSC^{__CFLocale}iiC^{__CFArray}^{__CFArray}}16"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/DataDetectorsCore/Sources/Automaton Compiler/DDDFAScanner.c"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/DataDetectorsCore/Sources/DDCache.c"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/DataDetectorsCore/Sources/DDScannerLoader.c"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/DataDetectorsCore/Sources/DDScannerResult.m"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/DataDetectorsCore/Sources/ICU-Patch/DDLexer.cpp"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/DataDetectorsCore/Sources/ICU-Patch/rbclass.cpp"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/DataDetectorsCore/Sources/Lookup/DDCachingStringTokenizer.c"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/DataDetectorsCore/Sources/Lookup/DDLookupTable.c"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/DataDetectorsCore/Sources/Lookup/DDStaticTrie.c"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/DataDetectorsCore/Sources/Lookup/DDTrie.c"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/DataDetectorsCore/Sources/PushDown/DDLRDispatchTable_sparse.c"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/DataDetectorsCore/Sources/PushDown/DDLRLightResult.c"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/DataDetectorsCore/Sources/PushDown/DDLexemCache.c"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/DataDetectorsCore/Sources/PushDown/DDPushDownAutomaton.c"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/DataDetectorsCore/Sources/PushDown/DDResult.c"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/DataDetectorsCore/Sources/PushDown/DDResultFiltering.c"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/DataDetectorsCore/Sources/PushDown/DDScanQuery.c"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/DataDetectorsCore/Sources/PushDown/DDScanner.c"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/DataDetectorsCore/Sources/PushDown/DDTokenCache.c"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/DataDetectorsCore/Sources/Utilities/DDDebugUtils.c"
- "C44@?0^{__DDResult={__CFRuntimeBase=QAQ}{__DDQueryRange={__DDQueryOffset=b16b16b32}{__DDQueryOffset=b16b16b32}}{?=qq}q^{__CFArray}^{__CFString}^{__CFString}^v^{__CFDictionary}qCf}8^{__CFString=}16^{__DDScanner={__CFRuntimeBase=QAQ}^{__DDLRTable}^{__DDLexer}^{__DDCache}^{__DDTokenCache}^{__DDLexemCache}^{__DDScanQuery}^{__DDScanQuery}[7^{__DDLookupTable}]^{__CFString}d^{__CFData}^{DDSourceMatchCache}^{__CFArray}^{__CFArray}qqqq*@?db1b1CSC^{__CFLocale}iiC^{__CFArray}}24^{__CFString=}32C40"
- "v24@?0^{__CFArray=}8^{__DDScanner={__CFRuntimeBase=QAQ}^{__DDLRTable}^{__DDLexer}^{__DDCache}^{__DDTokenCache}^{__DDLexemCache}^{__DDScanQuery}^{__DDScanQuery}[7^{__DDLookupTable}]^{__CFString}d^{__CFData}^{DDSourceMatchCache}^{__CFArray}^{__CFArray}qqqq*@?db1b1CSC^{__CFLocale}iiC^{__CFArray}}16"

```
