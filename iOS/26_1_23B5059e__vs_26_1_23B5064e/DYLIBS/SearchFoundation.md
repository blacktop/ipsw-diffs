## SearchFoundation

> `/System/Library/PrivateFrameworks/SearchFoundation.framework/SearchFoundation`

```diff

-3505.10.1.0.0
-  __TEXT.__text: 0x38ce90
-  __TEXT.__auth_stubs: 0x640
-  __TEXT.__objc_methlist: 0x55594
+3505.12.2.0.0
+  __TEXT.__text: 0x38d12c
+  __TEXT.__auth_stubs: 0x630
+  __TEXT.__objc_methlist: 0x555c4
   __TEXT.__const: 0x80
   __TEXT.__dlopen_cstrs: 0x52
   __TEXT.__gcc_except_tab: 0x94
-  __TEXT.__cstring: 0x6ded
+  __TEXT.__cstring: 0x6dbf
   __TEXT.__oslogstring: 0x19a
-  __TEXT.__unwind_info: 0x83b8
-  __TEXT.__objc_classname: 0x4767
-  __TEXT.__objc_methname: 0x2f712
-  __TEXT.__objc_methtype: 0xfa42
-  __TEXT.__objc_stubs: 0x19700
+  __TEXT.__unwind_info: 0x83d0
+  __TEXT.__objc_classname: 0x4765
+  __TEXT.__objc_methname: 0x2f7e9
+  __TEXT.__objc_methtype: 0xfa59
+  __TEXT.__objc_stubs: 0x19720
   __DATA_CONST.__got: 0x1760
   __DATA_CONST.__const: 0xad0
   __DATA_CONST.__objc_classlist: 0x1798
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x1650
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x76a0
+  __DATA_CONST.__objc_selrefs: 0x76c0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x1e88
-  __AUTH_CONST.__auth_got: 0x330
+  __AUTH_CONST.__auth_got: 0x328
   __AUTH_CONST.__const: 0xe0
-  __AUTH_CONST.__cfstring: 0xcfe0
-  __AUTH_CONST.__objc_const: 0xaa098
+  __AUTH_CONST.__cfstring: 0xcfa0
+  __AUTH_CONST.__objc_const: 0xaa0f8
   __AUTH.__objc_data: 0xc080
-  __DATA.__objc_ivar: 0x43f8
+  __DATA.__objc_ivar: 0x4400
   __DATA.__data: 0x10bd8
   __DATA.__bss: 0xc8
   __DATA_DIRTY.__objc_data: 0x2b70

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B93E6D43-8D27-3EEC-B19A-2E2FE811D928
-  Functions: 17334
-  Symbols:   53435
-  CStrings:  13781
+  UUID: 4F9AE61F-58CC-3D32-9AC8-D586E721012F
+  Functions: 17338
+  Symbols:   53445
+  CStrings:  13785
 
Symbols:
+ -[SFEndNetworkSearchFeedback edge]
+ -[SFEndNetworkSearchFeedback initWithStartSearch:responseSize:statusCode:networkTimingData:edge:]
+ -[SFVisibleResultsFeedback inputToResultShownMs]
+ -[SFVisibleResultsFeedback setInputToResultShownMs:]
+ GCC_except_table6416
+ GCC_except_table7974
+ _OBJC_IVAR_$_SFEndNetworkSearchFeedback._edge
+ _OBJC_IVAR_$_SFVisibleResultsFeedback._inputToResultShownMs
+ _PARLogHandleForCategory.logHandles.0.70635
+ _PARLogHandleForCategory.logHandles.1.70632
+ _PARLogHandleForCategory.logHandles.2.70637
+ _PARLogHandleForCategory.logHandles.3.70638
+ _PARLogHandleForCategory.logHandles.4.70640
+ _PARLogHandleForCategory.logHandles.5.70641
+ _PARLogHandleForCategory.onceToken.70631
+ ___PARLogHandleForCategory_block_invoke.70634
+ ___block_literal_global.70647
+ ___getDispatchQueue_block_invoke.70651
+ _getDispatchQueue.70645
+ _getDispatchQueue.onceToken.70646
+ _getDispatchQueue.queue.70648
+ _objc_msgSend$inputToResultShownMs
- GCC_except_table6412
- GCC_except_table7970
- _PARLogHandleForCategory.logHandles.0.70620
- _PARLogHandleForCategory.logHandles.1.70617
- _PARLogHandleForCategory.logHandles.2.70622
- _PARLogHandleForCategory.logHandles.3.70623
- _PARLogHandleForCategory.logHandles.4.70625
- _PARLogHandleForCategory.logHandles.5.70626
- _PARLogHandleForCategory.onceToken.70616
- ___PARLogHandleForCategory_block_invoke.70619
- ___block_literal_global.70632
- ___getDispatchQueue_block_invoke.70636
- _getDispatchQueue.70630
- _getDispatchQueue.onceToken.70631
- _getDispatchQueue.queue.70633
- _objc_unsafeClaimAutoreleasedReturnValue
Functions:
~ -[SFEndLocalSearchFeedback .cxx_destruct] : 84 -> 104
~ -[SFVisibleResultsFeedback .cxx_destruct] : 124 -> 144
~ -[SFEndNetworkSearchFeedback .cxx_destruct] : 20 -> 84
+ -[SFEndNetworkSearchFeedback edge]
~ -[SFEndNetworkSearchFeedback encodeWithCoder:] : 180 -> 208
~ -[SFEndNetworkSearchFeedback initWithCoder:] : 296 -> 336
+ -[SFEndNetworkSearchFeedback initWithStartSearch:responseSize:statusCode:networkTimingData:edge:]
~ -[SFStartLocalSearchFeedback encodeWithCoder:] : 308 -> 292
~ -[SFEndLocalSearchFeedback setEmbeddingState:] : 16 -> 20
~ -[SFEndLocalSearchFeedback initWithCoder:] : 316 -> 320
~ -[SFEndLocalSearchFeedback initWithStartSearch:queryUnderstandingParse:l1ToL2ResultCount:coreSpotlightIndexCount:embeddingState:] : 52 -> 144
+ -[SFVisibleResultsFeedback setInputToResultShownMs:]
+ -[SFVisibleResultsFeedback isFilterBarShown]
~ -[SFVisibleResultsFeedback description] : 308 -> 336
~ -[SFVisibleResultsFeedback encodeWithCoder:] : 236 -> 264
~ -[SFVisibleResultsFeedback initWithCoder:] : 380 -> 432
~ -[SFVisibleResultsFeedback copyWithZone:] : 300 -> 332
CStrings:
+ "%@ - result: %@ - buttons: %@ - card sections: %@ - isFilterBarShown: %@ - inputToResultShownMs: %@"
+ "@56@0:8@16q24q32@40@48"
+ "T@\"NSNumber\",&,N,V_inputToResultShownMs"
+ "T@\"NSString\",R,C,N,V_edge"
+ "T@\"SFEmbeddingState\",&,N,V_embeddingState"
+ "_edge"
+ "_inputToResultShownMs"
+ "edge"
+ "initWithStartSearch:responseSize:statusCode:networkTimingData:edge:"
+ "inputToResultShownMs"
+ "setInputToResultShownMs:"
- "%@ - result: %@ - buttons: %@ - card sections: %@ - isFilterBarShown: %@"
- "A"
- "T@\"SFEmbeddingState\",N,V_embeddingState"

```
