## BusinessChatService

> `/System/Library/PrivateFrameworks/BusinessChatService.framework/Versions/A/BusinessChatService`

```diff

-30095.22.9.7.15
-  __TEXT.__text: 0x81654
-  __TEXT.__auth_stubs: 0x8f0
-  __TEXT.__objc_methlist: 0x8504
-  __TEXT.__const: 0x258
-  __TEXT.__cstring: 0x7d5c
-  __TEXT.__oslogstring: 0x47a0
-  __TEXT.__gcc_except_tab: 0xa64
+30095.24.10.23.15
+  __TEXT.__text: 0x8159c
+  __TEXT.__auth_stubs: 0x8e0
+  __TEXT.__objc_methlist: 0x9594
+  __TEXT.__const: 0x260
+  __TEXT.__cstring: 0x7d96
+  __TEXT.__oslogstring: 0x4804
+  __TEXT.__gcc_except_tab: 0xa54
   __TEXT.__ustring: 0x5b0
-  __TEXT.__unwind_info: 0x19f0
-  __TEXT.__objc_classname: 0x16b2
-  __TEXT.__objc_methname: 0x11a38
-  __TEXT.__objc_methtype: 0x31ff
-  __TEXT.__objc_stubs: 0xb840
+  __TEXT.__unwind_info: 0x18b8
+  __TEXT.__objc_classname: 0x16c5
+  __TEXT.__objc_methname: 0x11aa5
+  __TEXT.__objc_methtype: 0x31fa
+  __TEXT.__objc_stubs: 0xb8c0
   __DATA_CONST.__got: 0x418
-  __DATA_CONST.__const: 0x6d0
-  __DATA_CONST.__objc_classlist: 0x4b8
+  __DATA_CONST.__const: 0x718
+  __DATA_CONST.__objc_classlist: 0x4c0
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x2e0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3b48
+  __DATA_CONST.__objc_selrefs: 0x3be0
   __DATA_CONST.__objc_protorefs: 0x40
-  __DATA_CONST.__objc_superrefs: 0x398
+  __DATA_CONST.__objc_superrefs: 0x3a0
   __DATA_CONST.__objc_arraydata: 0x18
-  __AUTH_CONST.__auth_got: 0x488
-  __AUTH_CONST.__const: 0x19e0
-  __AUTH_CONST.__cfstring: 0x5e00
-  __AUTH_CONST.__objc_const: 0x12920
+  __AUTH_CONST.__auth_got: 0x480
+  __AUTH_CONST.__const: 0x1a10
+  __AUTH_CONST.__cfstring: 0x5e20
+  __AUTH_CONST.__objc_const: 0x10e60
   __AUTH_CONST.__objc_intobj: 0xf0
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH.__objc_data: 0x2f30
-  __DATA.__objc_ivar: 0x8a0
+  __AUTH.__objc_data: 0x2f80
+  __DATA.__objc_ivar: 0x8a8
   __DATA.__data: 0xda70
   __DATA.__bss: 0x1a8
   __DATA.__common: 0x10

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 88698003-DFC1-3930-96A2-634C9EB35FE6
-  Functions: 3007
-  Symbols:   7125
-  CStrings:  5486
+  UUID: B7AB20F1-6062-38BA-B6DD-672CD2F19C3E
+  Functions: 2941
+  Symbols:   7144
+  CStrings:  5497
 
Symbols:
+ -[BCSPIRBatchRequest .cxx_destruct]
+ -[BCSPIRBatchRequest identifiersByPIRKey]
+ -[BCSPIRBatchRequest initWithQuery:]
+ -[BCSPIRBatchRequest invalidIdentifiers]
+ -[BCSPIRBatchRequest pirKeysToFetch]
+ -[BCSRemoteFetchPIR decompressData:error:]
+ -[BCSRemoteFetchPIR initWithEnvironment:metricFactory:queue:pirClient:]
+ OBJC_IVAR_$_BCSPIRBatchRequest._invalidIdentifiers
+ OBJC_IVAR_$_BCSPIRBatchRequest._storage
+ _BCSErrorMultipleFailuresCode
+ _BCSErrorSubErrorsKey
+ _OBJC_CLASS_$_BCSPIRBatchRequest
+ _OBJC_METACLASS_$_BCSPIRBatchRequest
+ __58-[BCSRemoteFetchPIR fetchDataMatching:timeout:completion:]_block_invoke.89
+ __76-[BCSRemoteFetchPIR fetchDataMatchingBatch:timeout:perItemBlock:completion:]_block_invoke.22
+ __76-[BCSRemoteFetchPIR fetchDataMatchingBatch:timeout:perItemBlock:completion:]_block_invoke.23
+ __76-[BCSRemoteFetchPIR fetchDataMatchingBatch:timeout:perItemBlock:completion:]_block_invoke.36
+ __77-[BCSBusinessEmailResolver _metadataMatching:metric:perItemBlock:completion:]_block_invoke.88
+ __OBJC_$_INSTANCE_METHODS_BCSPIRBatchRequest
+ __OBJC_$_INSTANCE_VARIABLES_BCSPIRBatchRequest
+ __OBJC_$_PROP_LIST_BCSPIRBatchRequest
+ __OBJC_CLASS_RO_$_BCSPIRBatchRequest
+ __OBJC_METACLASS_RO_$_BCSPIRBatchRequest
+ ___block_descriptor_104_e8_32s40s48s56s64s72s80bs88bs96r_e29_v24?0"NSArray"8"NSError"16l
+ ___block_descriptor_64_e8_32s40s48bs_e43_B24?0"<BCSItemIdentifying>"8"NSObject"16l
+ _objc_msgSend$decompressData:error:
+ _objc_msgSend$identifiersByPIRKey
+ _objc_msgSend$initWithEnvironment:metricFactory:queue:pirClient:
+ _objc_msgSend$initWithQuery:
+ _objc_msgSend$invalidIdentifiers
+ _objc_msgSend$pirKeysToFetch
- -[BCSRemoteFetchPIR decompressData:]
- -[BCSRemoteFetchPIR initWithEnvironment:metricFactory:queue:]
- __58-[BCSRemoteFetchPIR fetchDataMatching:timeout:completion:]_block_invoke.88
- __76-[BCSRemoteFetchPIR fetchDataMatchingBatch:timeout:perItemBlock:completion:]_block_invoke.69
- __76-[BCSRemoteFetchPIR fetchDataMatchingBatch:timeout:perItemBlock:completion:]_block_invoke.85
- __77-[BCSBusinessEmailResolver _metadataMatching:metric:perItemBlock:completion:]_block_invoke.25
- ___block_descriptor_96_e8_32s40s48s56s64s72bs80bs88r_e29_v24?0"NSArray"8"NSError"16l
- ___copy_helper_block_e8_32s40s48s56s64s72b80b88r
- ___destroy_helper_block_e8_32s40s48s56s64s72s80s88r
- _fmod
- _objc_msgSend$decompressData:
- _objc_msgSend$initWithEnvironment:metricFactory:queue:
CStrings:
+ "%s - Unexpectedly invalid identifiers for key (%@{private}) in query item identifiers (%@{private})"
+ "-[BCSRemoteFetchPIR decompressData:error:]"
+ "@\"<BCSPIRClient>\""
+ "B24@?0@\"<BCSItemIdentifying>\"8@\"NSObject\"16"
+ "BCSPIRBatchRequest"
+ "BCSSubErrors"
+ "Failed to unzip data"
+ "T@\"<BCSPIRClient>\",&,N,V_pirClient"
+ "_invalidIdentifiers"
+ "_storage"
+ "decompressData:error:"
+ "identifiersByPIRKey"
+ "initWithEnvironment:metricFactory:queue:pirClient:"
+ "initWithQuery:"
+ "invalidIdentifiers"
+ "pirKeysToFetch"
- "-[BCSRemoteFetchPIR decompressData:]"
- "@\"CMLKeywordPIRClient\""
- "Failed to decompress data"
- "T@\"CMLKeywordPIRClient\",&,N,V_pirClient"
- "decompressData:"
- "initWithEnvironment:metricFactory:queue:"

```
