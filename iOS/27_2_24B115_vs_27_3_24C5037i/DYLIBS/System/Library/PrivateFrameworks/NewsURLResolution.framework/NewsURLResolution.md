## NewsURLResolution

> `/System/Library/PrivateFrameworks/NewsURLResolution.framework/NewsURLResolution`

```diff

-5971.0.0.0.0
+6006.0.0.0.0
   __TEXT.__text: 0x1b64
   __TEXT.__objc_methlist: 0x37c
   __TEXT.__const: 0x50

   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/NewsCore.framework/NewsCore
+  - /System/Library/PrivateFrameworks/NewsDaemon.framework/NewsDaemon
   - /System/Library/PrivateFrameworks/NewsFoundation.framework/NewsFoundation
   - /System/Library/PrivateFrameworks/NewsTransport.framework/NewsTransport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 65
-  Symbols:   192
+  Symbols:   63
   CStrings:  31
 
Symbols:
- +[NRURLResolutionManager sharedManager]
- -[NRNewsDaemonBloomFilterInfoService .cxx_destruct]
- -[NRNewsDaemonBloomFilterInfoService _fetchBloomFilterInfoWithCompletion:]
- -[NRNewsDaemonBloomFilterInfoService bloomFilterInfo]
- -[NRNewsDaemonBloomFilterInfoService fetchOnceOperation]
- -[NRNewsDaemonBloomFilterInfoService fetchWebURLBloomFilterInfoWithCompletion:]
- -[NRNewsDaemonBloomFilterInfoService init]
- -[NRNewsDaemonBloomFilterInfoService setBloomFilterInfo:]
- -[NRNewsURLResolutionOperation .cxx_destruct]
- -[NRNewsURLResolutionOperation initWithNewsURL:]
- -[NRNewsURLResolutionOperation init]
- -[NRNewsURLResolutionOperation newsURL]
- -[NRNewsURLResolutionOperation operationWillFinishWithError:]
- -[NRNewsURLResolutionOperation performOperation]
- -[NRNewsURLResolutionOperation resolutionCompletion]
- -[NRNewsURLResolutionOperation resultWebURL]
- -[NRNewsURLResolutionOperation setResolutionCompletion:]
- -[NRNewsURLResolutionOperation setResultWebURL:]
- -[NRNewsURLResolutionOperation validateOperation]
- -[NRURLResolutionManager .cxx_destruct]
- -[NRURLResolutionManager bloomFilterInfoService]
- -[NRURLResolutionManager createResolutionOperationForNewsURL:]
- -[NRURLResolutionManager createResolutionOperationForWebURL:]
- -[NRURLResolutionManager init]
- -[NRURLResolutionManager userHasBundleSubscription]
- -[NRWebURLResolutionOperation .cxx_destruct]
- -[NRWebURLResolutionOperation bloomFilterInfoService]
- -[NRWebURLResolutionOperation initWithWebURL:bloomFilterInfoService:]
- -[NRWebURLResolutionOperation init]
- -[NRWebURLResolutionOperation operationWillFinishWithError:]
- -[NRWebURLResolutionOperation performOperation]
- -[NRWebURLResolutionOperation resolutionCompletion]
- -[NRWebURLResolutionOperation resultNewsURL]
- -[NRWebURLResolutionOperation setResolutionCompletion:]
- -[NRWebURLResolutionOperation setResultNewsURL:]
- -[NRWebURLResolutionOperation validateOperation]
- -[NRWebURLResolutionOperation webURL]
- -[NSURL(NRAdditions) nr_isNewsURL]
- -[NSURL(NRAdditions) nr_isWebURL]
- <redacted>
- _OBJC_IVAR_$_NRNewsDaemonBloomFilterInfoService._bloomFilterInfo
- _OBJC_IVAR_$_NRNewsDaemonBloomFilterInfoService._fetchOnceOperation
- _OBJC_IVAR_$_NRNewsURLResolutionOperation._newsURL
- _OBJC_IVAR_$_NRNewsURLResolutionOperation._resolutionCompletion
- _OBJC_IVAR_$_NRNewsURLResolutionOperation._resultWebURL
- _OBJC_IVAR_$_NRURLResolutionManager._bloomFilterInfoService
- _OBJC_IVAR_$_NRWebURLResolutionOperation._bloomFilterInfoService
- _OBJC_IVAR_$_NRWebURLResolutionOperation._resolutionCompletion
- _OBJC_IVAR_$_NRWebURLResolutionOperation._resultNewsURL
- _OBJC_IVAR_$_NRWebURLResolutionOperation._webURL
- _OUTLINED_FUNCTION_0
- _OUTLINED_FUNCTION_1
- _OUTLINED_FUNCTION_2
- _OUTLINED_FUNCTION_3
- _OUTLINED_FUNCTION_4
- __OBJC_$_CATEGORY_INSTANCE_METHODS_NSURL_$_NRAdditions
- __OBJC_$_CATEGORY_NSURL_$_NRAdditions
- __OBJC_$_CLASS_METHODS_NRURLResolutionManager
- __OBJC_$_INSTANCE_METHODS_NRNewsDaemonBloomFilterInfoService
- __OBJC_$_INSTANCE_METHODS_NRNewsURLResolutionOperation
- __OBJC_$_INSTANCE_METHODS_NRURLResolutionManager
- __OBJC_$_INSTANCE_METHODS_NRWebURLResolutionOperation
- __OBJC_$_INSTANCE_VARIABLES_NRNewsDaemonBloomFilterInfoService
- __OBJC_$_INSTANCE_VARIABLES_NRNewsURLResolutionOperation
- __OBJC_$_INSTANCE_VARIABLES_NRURLResolutionManager
- __OBJC_$_INSTANCE_VARIABLES_NRWebURLResolutionOperation
- __OBJC_$_PROP_LIST_NRNewsDaemonBloomFilterInfoService
- __OBJC_$_PROP_LIST_NRNewsURLResolutionOperation
- __OBJC_$_PROP_LIST_NRURLResolutionManager
- __OBJC_$_PROP_LIST_NRURLResolutionOperation
- __OBJC_$_PROP_LIST_NRWebURLResolutionOperation
- __OBJC_$_PROP_LIST_NSObject
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NDURLResolutionService
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NRBloomFilterInfoService
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NRURLResolutionOperation
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject
- __OBJC_$_PROTOCOL_METHOD_TYPES_NDURLResolutionService
- __OBJC_$_PROTOCOL_METHOD_TYPES_NRBloomFilterInfoService
- __OBJC_$_PROTOCOL_METHOD_TYPES_NRURLResolutionOperation
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject
- __OBJC_$_PROTOCOL_REFS_NDURLResolutionService
- __OBJC_$_PROTOCOL_REFS_NRURLResolutionOperation
- __OBJC_CLASS_PROTOCOLS_$_NRNewsDaemonBloomFilterInfoService
- __OBJC_CLASS_PROTOCOLS_$_NRNewsURLResolutionOperation
- __OBJC_CLASS_PROTOCOLS_$_NRWebURLResolutionOperation
- __OBJC_CLASS_RO_$_NRNewsDaemonBloomFilterInfoService
- __OBJC_CLASS_RO_$_NRNewsURLResolutionOperation
- __OBJC_CLASS_RO_$_NRURLResolutionManager
- __OBJC_CLASS_RO_$_NRWebURLResolutionOperation
- __OBJC_LABEL_PROTOCOL_$_NDURLResolutionService
- __OBJC_LABEL_PROTOCOL_$_NRBloomFilterInfoService
- __OBJC_LABEL_PROTOCOL_$_NRURLResolutionOperation
- __OBJC_LABEL_PROTOCOL_$_NSObject
- __OBJC_METACLASS_RO_$_NRNewsDaemonBloomFilterInfoService
- __OBJC_METACLASS_RO_$_NRNewsURLResolutionOperation
- __OBJC_METACLASS_RO_$_NRURLResolutionManager
- __OBJC_METACLASS_RO_$_NRWebURLResolutionOperation
- __OBJC_PROTOCOL_$_NDURLResolutionService
- __OBJC_PROTOCOL_$_NRBloomFilterInfoService
- __OBJC_PROTOCOL_$_NRURLResolutionOperation
- __OBJC_PROTOCOL_$_NSObject
- __OBJC_PROTOCOL_REFERENCE_$_NDURLResolutionService
- ___39+[NRURLResolutionManager sharedManager]_block_invoke
- ___42-[NRNewsDaemonBloomFilterInfoService init]_block_invoke
- ___42-[NRNewsDaemonBloomFilterInfoService init]_block_invoke_2
- ___47-[NRWebURLResolutionOperation performOperation]_block_invoke
- ___47-[NRWebURLResolutionOperation performOperation]_block_invoke_2
- ___47-[NRWebURLResolutionOperation performOperation]_block_invoke_3
- ___47-[NRWebURLResolutionOperation performOperation]_block_invoke_4
- ___47-[NRWebURLResolutionOperation performOperation]_block_invoke_5
- ___48-[NRNewsURLResolutionOperation performOperation]_block_invoke
- ___48-[NRNewsURLResolutionOperation performOperation]_block_invoke_2
- ___48-[NRNewsURLResolutionOperation performOperation]_block_invoke_3
- ___74-[NRNewsDaemonBloomFilterInfoService _fetchBloomFilterInfoWithCompletion:]_block_invoke
- ___74-[NRNewsDaemonBloomFilterInfoService _fetchBloomFilterInfoWithCompletion:]_block_invoke_2
- ___79-[NRNewsDaemonBloomFilterInfoService fetchWebURLBloomFilterInfoWithCompletion:]_block_invoke
- ___block_descriptor_40_e5_v8?0l
- ___block_descriptor_40_e8_32s_e5_v8?0ls32l8
- ___block_descriptor_40_e8_32s_e64_"<FCOperationCanceling><FCOperationPrioritizing>"16?0?<v?B>8ls32l8
- ___block_descriptor_48_e8_32s40bs_e17_v16?0"NSError"8ls40l8s32l8
- ___block_descriptor_48_e8_32s40bs_e41_v24?0"NTPBBloomFilterInfo"8"NSError"16ls32l8s40l8
- ___block_descriptor_48_e8_32s40bs_e41_v24?0"NTPBBloomFilterInfo"8"NSError"16ls40l8s32l8
- ___block_descriptor_48_e8_32s40bs_e5_v8?0ls40l8s32l8
- ___block_descriptor_48_e8_32s40s_e17_v16?0"NSError"8ls32l8s40l8
- ___block_descriptor_48_e8_32s40s_e27_v24?0"NSURL"8"NSError"16ls32l8s40l8
- ___block_descriptor_48_e8_32s40s_e29_v16?0"NTPBBloomFilterInfo"8ls32l8s40l8
- _sharedManager.onceToken
- _sharedManager.result
```
