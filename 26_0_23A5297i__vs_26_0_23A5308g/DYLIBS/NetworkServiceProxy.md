## NetworkServiceProxy

> `/System/Library/PrivateFrameworks/NetworkServiceProxy.framework/NetworkServiceProxy`

```diff

-902.0.0.0.1
-  __TEXT.__text: 0x48c48
-  __TEXT.__auth_stubs: 0xdb0
-  __TEXT.__objc_methlist: 0x4174
+906.0.1.0.0
+  __TEXT.__text: 0x4f278
+  __TEXT.__auth_stubs: 0xdd0
+  __TEXT.__objc_methlist: 0x4aac
   __TEXT.__const: 0x360
   __TEXT.__gcc_except_tab: 0x90
-  __TEXT.__cstring: 0x4fd4
-  __TEXT.__oslogstring: 0x2c53
-  __TEXT.__unwind_info: 0xc68
-  __TEXT.__objc_classname: 0x4e3
-  __TEXT.__objc_methname: 0x8c6a
-  __TEXT.__objc_methtype: 0x1139
-  __TEXT.__objc_stubs: 0x4e20
-  __DATA_CONST.__got: 0x388
-  __DATA_CONST.__const: 0xb40
-  __DATA_CONST.__objc_classlist: 0x148
+  __TEXT.__cstring: 0x5199
+  __TEXT.__oslogstring: 0x2ccc
+  __TEXT.__unwind_info: 0xe38
+  __TEXT.__objc_classname: 0x606
+  __TEXT.__objc_methname: 0x958e
+  __TEXT.__objc_methtype: 0x12d7
+  __TEXT.__objc_stubs: 0x5100
+  __DATA_CONST.__got: 0x3c8
+  __DATA_CONST.__const: 0xba8
+  __DATA_CONST.__objc_classlist: 0x198
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2048
-  __DATA_CONST.__objc_superrefs: 0x128
+  __DATA_CONST.__objc_selrefs: 0x22a8
+  __DATA_CONST.__objc_superrefs: 0x178
   __DATA_CONST.__objc_arraydata: 0x48
-  __AUTH_CONST.__auth_got: 0x6f0
+  __AUTH_CONST.__auth_got: 0x700
   __AUTH_CONST.__const: 0x180
-  __AUTH_CONST.__cfstring: 0x47e0
-  __AUTH_CONST.__objc_const: 0x58f0
+  __AUTH_CONST.__cfstring: 0x4a60
+  __AUTH_CONST.__objc_const: 0x65c8
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH.__objc_data: 0xb40
-  __DATA.__objc_ivar: 0x2b0
+  __AUTH.__objc_data: 0xe60
+  __DATA.__objc_ivar: 0x2c8
   __DATA.__data: 0x268
   __DATA.__common: 0x1
   __DATA.__bss: 0x10
-  __DATA_DIRTY.__objc_ivar: 0x1e4
+  __DATA_DIRTY.__objc_ivar: 0x234
   __DATA_DIRTY.__objc_data: 0x190
   __DATA_DIRTY.__bss: 0xa8
   __DATA_DIRTY.__common: 0x20

   - /usr/lib/libboringssl.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B5B9657C-6602-369F-95E9-6446CA0AA51F
-  Functions: 1479
-  Symbols:   4476
-  CStrings:  3391
+  UUID: D5A14398-990D-3865-8674-6D1CE08248E8
+  Functions: 1677
+  Symbols:   4982
+  CStrings:  3574
 
Symbols:
+ +[NSPPrivacyProxyQuotaInfo quotaServicesType]
+ +[NSPPrivacyProxyQuotaService supportedUseCaseIdentifiersType]
+ -[NSPPrivacyProxyConfiguration hasQuotaInfo]
+ -[NSPPrivacyProxyConfiguration quotaInfo]
+ -[NSPPrivacyProxyConfiguration setQuotaInfo:]
+ -[NSPPrivacyProxyCost copyTo:]
+ -[NSPPrivacyProxyCost copyWithZone:]
+ -[NSPPrivacyProxyCost description]
+ -[NSPPrivacyProxyCost dictionaryRepresentation]
+ -[NSPPrivacyProxyCost hasLimit]
+ -[NSPPrivacyProxyCost hasRemaining]
+ -[NSPPrivacyProxyCost hash]
+ -[NSPPrivacyProxyCost isEqual:]
+ -[NSPPrivacyProxyCost limit]
+ -[NSPPrivacyProxyCost mergeFrom:]
+ -[NSPPrivacyProxyCost readFrom:]
+ -[NSPPrivacyProxyCost remaining]
+ -[NSPPrivacyProxyCost setHasLimit:]
+ -[NSPPrivacyProxyCost setHasRemaining:]
+ -[NSPPrivacyProxyCost setLimit:]
+ -[NSPPrivacyProxyCost setRemaining:]
+ -[NSPPrivacyProxyCost writeTo:]
+ -[NSPPrivacyProxyErrorResponse .cxx_destruct]
+ -[NSPPrivacyProxyErrorResponse copyTo:]
+ -[NSPPrivacyProxyErrorResponse copyWithZone:]
+ -[NSPPrivacyProxyErrorResponse description]
+ -[NSPPrivacyProxyErrorResponse dictionaryRepresentation]
+ -[NSPPrivacyProxyErrorResponse errorReason]
+ -[NSPPrivacyProxyErrorResponse hasErrorReason]
+ -[NSPPrivacyProxyErrorResponse hash]
+ -[NSPPrivacyProxyErrorResponse isEqual:]
+ -[NSPPrivacyProxyErrorResponse mergeFrom:]
+ -[NSPPrivacyProxyErrorResponse readFrom:]
+ -[NSPPrivacyProxyErrorResponse setErrorReason:]
+ -[NSPPrivacyProxyErrorResponse writeTo:]
+ -[NSPPrivacyProxyGetQuotaRequest .cxx_destruct]
+ -[NSPPrivacyProxyGetQuotaRequest copyTo:]
+ -[NSPPrivacyProxyGetQuotaRequest copyWithZone:]
+ -[NSPPrivacyProxyGetQuotaRequest description]
+ -[NSPPrivacyProxyGetQuotaRequest dictionaryRepresentation]
+ -[NSPPrivacyProxyGetQuotaRequest hasUseCaseIdentifier]
+ -[NSPPrivacyProxyGetQuotaRequest hash]
+ -[NSPPrivacyProxyGetQuotaRequest isEqual:]
+ -[NSPPrivacyProxyGetQuotaRequest mergeFrom:]
+ -[NSPPrivacyProxyGetQuotaRequest readFrom:]
+ -[NSPPrivacyProxyGetQuotaRequest setUseCaseIdentifier:]
+ -[NSPPrivacyProxyGetQuotaRequest useCaseIdentifier]
+ -[NSPPrivacyProxyGetQuotaRequest writeTo:]
+ -[NSPPrivacyProxyGetQuotaResponse .cxx_destruct]
+ -[NSPPrivacyProxyGetQuotaResponse StringAsGetQuotaResponseType:]
+ -[NSPPrivacyProxyGetQuotaResponse clearOneofValuesForGetQuotaResponseType]
+ -[NSPPrivacyProxyGetQuotaResponse copyTo:]
+ -[NSPPrivacyProxyGetQuotaResponse copyWithZone:]
+ -[NSPPrivacyProxyGetQuotaResponse description]
+ -[NSPPrivacyProxyGetQuotaResponse dictionaryRepresentation]
+ -[NSPPrivacyProxyGetQuotaResponse genericError]
+ -[NSPPrivacyProxyGetQuotaResponse getQuotaResponseTypeAsString:]
+ -[NSPPrivacyProxyGetQuotaResponse getQuotaResponseType]
+ -[NSPPrivacyProxyGetQuotaResponse hasGenericError]
+ -[NSPPrivacyProxyGetQuotaResponse hasGetQuotaResponseType]
+ -[NSPPrivacyProxyGetQuotaResponse hasSuccess]
+ -[NSPPrivacyProxyGetQuotaResponse hash]
+ -[NSPPrivacyProxyGetQuotaResponse isEqual:]
+ -[NSPPrivacyProxyGetQuotaResponse mergeFrom:]
+ -[NSPPrivacyProxyGetQuotaResponse readFrom:]
+ -[NSPPrivacyProxyGetQuotaResponse setGenericError:]
+ -[NSPPrivacyProxyGetQuotaResponse setGetQuotaResponseType:]
+ -[NSPPrivacyProxyGetQuotaResponse setHasGetQuotaResponseType:]
+ -[NSPPrivacyProxyGetQuotaResponse setSuccess:]
+ -[NSPPrivacyProxyGetQuotaResponse success]
+ -[NSPPrivacyProxyGetQuotaResponse writeTo:]
+ -[NSPPrivacyProxyQuota .cxx_destruct]
+ -[NSPPrivacyProxyQuota copyTo:]
+ -[NSPPrivacyProxyQuota copyWithZone:]
+ -[NSPPrivacyProxyQuota cost]
+ -[NSPPrivacyProxyQuota description]
+ -[NSPPrivacyProxyQuota dictionaryRepresentation]
+ -[NSPPrivacyProxyQuota expiration]
+ -[NSPPrivacyProxyQuota hasCost]
+ -[NSPPrivacyProxyQuota hasExpiration]
+ -[NSPPrivacyProxyQuota hash]
+ -[NSPPrivacyProxyQuota isEqual:]
+ -[NSPPrivacyProxyQuota mergeFrom:]
+ -[NSPPrivacyProxyQuota readFrom:]
+ -[NSPPrivacyProxyQuota setCost:]
+ -[NSPPrivacyProxyQuota setExpiration:]
+ -[NSPPrivacyProxyQuota setHasExpiration:]
+ -[NSPPrivacyProxyQuota writeTo:]
+ -[NSPPrivacyProxyQuotaInfo .cxx_destruct]
+ -[NSPPrivacyProxyQuotaInfo addQuotaServices:]
+ -[NSPPrivacyProxyQuotaInfo clearQuotaServices]
+ -[NSPPrivacyProxyQuotaInfo copyTo:]
+ -[NSPPrivacyProxyQuotaInfo copyWithZone:]
+ -[NSPPrivacyProxyQuotaInfo description]
+ -[NSPPrivacyProxyQuotaInfo dictionaryRepresentation]
+ -[NSPPrivacyProxyQuotaInfo hash]
+ -[NSPPrivacyProxyQuotaInfo isEqual:]
+ -[NSPPrivacyProxyQuotaInfo mergeFrom:]
+ -[NSPPrivacyProxyQuotaInfo quotaServicesAtIndex:]
+ -[NSPPrivacyProxyQuotaInfo quotaServicesCount]
+ -[NSPPrivacyProxyQuotaInfo quotaServices]
+ -[NSPPrivacyProxyQuotaInfo readFrom:]
+ -[NSPPrivacyProxyQuotaInfo setQuotaServices:]
+ -[NSPPrivacyProxyQuotaInfo writeTo:]
+ -[NSPPrivacyProxyQuotaService .cxx_destruct]
+ -[NSPPrivacyProxyQuotaService addSupportedUseCaseIdentifiers:]
+ -[NSPPrivacyProxyQuotaService clearSupportedUseCaseIdentifiers]
+ -[NSPPrivacyProxyQuotaService copyTo:]
+ -[NSPPrivacyProxyQuotaService copyWithZone:]
+ -[NSPPrivacyProxyQuotaService description]
+ -[NSPPrivacyProxyQuotaService dictionaryRepresentation]
+ -[NSPPrivacyProxyQuotaService hasServiceURL]
+ -[NSPPrivacyProxyQuotaService hash]
+ -[NSPPrivacyProxyQuotaService isEqual:]
+ -[NSPPrivacyProxyQuotaService mergeFrom:]
+ -[NSPPrivacyProxyQuotaService readFrom:]
+ -[NSPPrivacyProxyQuotaService serviceURL]
+ -[NSPPrivacyProxyQuotaService setServiceURL:]
+ -[NSPPrivacyProxyQuotaService setSupportedUseCaseIdentifiers:]
+ -[NSPPrivacyProxyQuotaService supportedUseCaseIdentifiersAtIndex:]
+ -[NSPPrivacyProxyQuotaService supportedUseCaseIdentifiersCount]
+ -[NSPPrivacyProxyQuotaService supportedUseCaseIdentifiers]
+ -[NSPPrivacyProxyQuotaService writeTo:]
+ -[NSPPrivacyProxyQuotaServiceRequest .cxx_destruct]
+ -[NSPPrivacyProxyQuotaServiceRequest StringAsRequestType:]
+ -[NSPPrivacyProxyQuotaServiceRequest baa]
+ -[NSPPrivacyProxyQuotaServiceRequest clearOneofValuesForRequestType]
+ -[NSPPrivacyProxyQuotaServiceRequest copyTo:]
+ -[NSPPrivacyProxyQuotaServiceRequest copyWithZone:]
+ -[NSPPrivacyProxyQuotaServiceRequest description]
+ -[NSPPrivacyProxyQuotaServiceRequest dictionaryRepresentation]
+ -[NSPPrivacyProxyQuotaServiceRequest hasBaa]
+ -[NSPPrivacyProxyQuotaServiceRequest hasRequestType]
+ -[NSPPrivacyProxyQuotaServiceRequest hasRequest]
+ -[NSPPrivacyProxyQuotaServiceRequest hash]
+ -[NSPPrivacyProxyQuotaServiceRequest isEqual:]
+ -[NSPPrivacyProxyQuotaServiceRequest mergeFrom:]
+ -[NSPPrivacyProxyQuotaServiceRequest readFrom:]
+ -[NSPPrivacyProxyQuotaServiceRequest requestTypeAsString:]
+ -[NSPPrivacyProxyQuotaServiceRequest requestType]
+ -[NSPPrivacyProxyQuotaServiceRequest request]
+ -[NSPPrivacyProxyQuotaServiceRequest setBaa:]
+ -[NSPPrivacyProxyQuotaServiceRequest setHasRequestType:]
+ -[NSPPrivacyProxyQuotaServiceRequest setRequest:]
+ -[NSPPrivacyProxyQuotaServiceRequest setRequestType:]
+ -[NSPPrivacyProxyQuotaServiceRequest writeTo:]
+ -[NSPPrivacyProxyQuotaServiceResponse .cxx_destruct]
+ -[NSPPrivacyProxyQuotaServiceResponse StringAsRequestType:]
+ -[NSPPrivacyProxyQuotaServiceResponse clearOneofValuesForRequestType]
+ -[NSPPrivacyProxyQuotaServiceResponse copyTo:]
+ -[NSPPrivacyProxyQuotaServiceResponse copyWithZone:]
+ -[NSPPrivacyProxyQuotaServiceResponse description]
+ -[NSPPrivacyProxyQuotaServiceResponse dictionaryRepresentation]
+ -[NSPPrivacyProxyQuotaServiceResponse hasRequestType]
+ -[NSPPrivacyProxyQuotaServiceResponse hasResponse]
+ -[NSPPrivacyProxyQuotaServiceResponse hash]
+ -[NSPPrivacyProxyQuotaServiceResponse isEqual:]
+ -[NSPPrivacyProxyQuotaServiceResponse mergeFrom:]
+ -[NSPPrivacyProxyQuotaServiceResponse readFrom:]
+ -[NSPPrivacyProxyQuotaServiceResponse requestTypeAsString:]
+ -[NSPPrivacyProxyQuotaServiceResponse requestType]
+ -[NSPPrivacyProxyQuotaServiceResponse response]
+ -[NSPPrivacyProxyQuotaServiceResponse setHasRequestType:]
+ -[NSPPrivacyProxyQuotaServiceResponse setRequestType:]
+ -[NSPPrivacyProxyQuotaServiceResponse setResponse:]
+ -[NSPPrivacyProxyQuotaServiceResponse writeTo:]
+ -[NSPPrivacyProxySuccessResponse .cxx_destruct]
+ -[NSPPrivacyProxySuccessResponse copyTo:]
+ -[NSPPrivacyProxySuccessResponse copyWithZone:]
+ -[NSPPrivacyProxySuccessResponse description]
+ -[NSPPrivacyProxySuccessResponse dictionaryRepresentation]
+ -[NSPPrivacyProxySuccessResponse hasQuota]
+ -[NSPPrivacyProxySuccessResponse hash]
+ -[NSPPrivacyProxySuccessResponse isEqual:]
+ -[NSPPrivacyProxySuccessResponse mergeFrom:]
+ -[NSPPrivacyProxySuccessResponse quota]
+ -[NSPPrivacyProxySuccessResponse readFrom:]
+ -[NSPPrivacyProxySuccessResponse setQuota:]
+ -[NSPPrivacyProxySuccessResponse writeTo:]
+ -[NSPPrivacyProxyTokenIssuer hasSupportsTokenUsageFeedback]
+ -[NSPPrivacyProxyTokenIssuer setHasSupportsTokenUsageFeedback:]
+ -[NSPPrivacyProxyTokenIssuer setSupportsTokenUsageFeedback:]
+ -[NSPPrivacyProxyTokenIssuer supportsTokenUsageFeedback]
+ -[NSPPrivateAccessTokenFetcher checkRemainingCostQuotaWithQueue:completionHandler:]
+ -[NSPServerClient checkRemainingCostQuotaWithFetcher:allowRetry:completionHandler:]
+ _NSPPrivacyProxyCostReadFrom
+ _NSPPrivacyProxyErrorResponseReadFrom
+ _NSPPrivacyProxyGetQuotaRequestReadFrom
+ _NSPPrivacyProxyGetQuotaResponseReadFrom
+ _NSPPrivacyProxyQuotaInfoReadFrom
+ _NSPPrivacyProxyQuotaReadFrom
+ _NSPPrivacyProxyQuotaServiceReadFrom
+ _NSPPrivacyProxyQuotaServiceRequestReadFrom
+ _NSPPrivacyProxyQuotaServiceResponseReadFrom
+ _NSPPrivacyProxySuccessResponseReadFrom
+ _OBJC_CLASS_$_NSPPrivacyProxyCost
+ _OBJC_CLASS_$_NSPPrivacyProxyErrorResponse
+ _OBJC_CLASS_$_NSPPrivacyProxyGetQuotaRequest
+ _OBJC_CLASS_$_NSPPrivacyProxyGetQuotaResponse
+ _OBJC_CLASS_$_NSPPrivacyProxyQuota
+ _OBJC_CLASS_$_NSPPrivacyProxyQuotaInfo
+ _OBJC_CLASS_$_NSPPrivacyProxyQuotaService
+ _OBJC_CLASS_$_NSPPrivacyProxyQuotaServiceRequest
+ _OBJC_CLASS_$_NSPPrivacyProxyQuotaServiceResponse
+ _OBJC_CLASS_$_NSPPrivacyProxySuccessResponse
+ _OBJC_IVAR_$_NSPPrivacyProxyErrorResponse._errorReason
+ _OBJC_IVAR_$_NSPPrivacyProxyGetQuotaRequest._useCaseIdentifier
+ _OBJC_IVAR_$_NSPPrivacyProxyQuotaInfo._quotaServices
+ _OBJC_IVAR_$_NSPPrivacyProxyQuotaService._serviceURL
+ _OBJC_IVAR_$_NSPPrivacyProxyQuotaService._supportedUseCaseIdentifiers
+ _OBJC_IVAR_$_NSPPrivacyProxySuccessResponse._quota
+ _OBJC_METACLASS_$_NSPPrivacyProxyCost
+ _OBJC_METACLASS_$_NSPPrivacyProxyErrorResponse
+ _OBJC_METACLASS_$_NSPPrivacyProxyGetQuotaRequest
+ _OBJC_METACLASS_$_NSPPrivacyProxyGetQuotaResponse
+ _OBJC_METACLASS_$_NSPPrivacyProxyQuota
+ _OBJC_METACLASS_$_NSPPrivacyProxyQuotaInfo
+ _OBJC_METACLASS_$_NSPPrivacyProxyQuotaService
+ _OBJC_METACLASS_$_NSPPrivacyProxyQuotaServiceRequest
+ _OBJC_METACLASS_$_NSPPrivacyProxyQuotaServiceResponse
+ _OBJC_METACLASS_$_NSPPrivacyProxySuccessResponse
+ _PBDataWriterWriteDoubleField
+ __OBJC_$_CLASS_METHODS_NSPPrivacyProxyQuotaInfo
+ __OBJC_$_CLASS_METHODS_NSPPrivacyProxyQuotaService
+ __OBJC_$_INSTANCE_METHODS_NSPPrivacyProxyCost
+ __OBJC_$_INSTANCE_METHODS_NSPPrivacyProxyErrorResponse
+ __OBJC_$_INSTANCE_METHODS_NSPPrivacyProxyGetQuotaRequest
+ __OBJC_$_INSTANCE_METHODS_NSPPrivacyProxyGetQuotaResponse
+ __OBJC_$_INSTANCE_METHODS_NSPPrivacyProxyQuota
+ __OBJC_$_INSTANCE_METHODS_NSPPrivacyProxyQuotaInfo
+ __OBJC_$_INSTANCE_METHODS_NSPPrivacyProxyQuotaService
+ __OBJC_$_INSTANCE_METHODS_NSPPrivacyProxyQuotaServiceRequest
+ __OBJC_$_INSTANCE_METHODS_NSPPrivacyProxyQuotaServiceResponse
+ __OBJC_$_INSTANCE_METHODS_NSPPrivacyProxySuccessResponse
+ __OBJC_$_INSTANCE_VARIABLES_NSPPrivacyProxyCost
+ __OBJC_$_INSTANCE_VARIABLES_NSPPrivacyProxyErrorResponse
+ __OBJC_$_INSTANCE_VARIABLES_NSPPrivacyProxyGetQuotaRequest
+ __OBJC_$_INSTANCE_VARIABLES_NSPPrivacyProxyGetQuotaResponse
+ __OBJC_$_INSTANCE_VARIABLES_NSPPrivacyProxyQuota
+ __OBJC_$_INSTANCE_VARIABLES_NSPPrivacyProxyQuotaInfo
+ __OBJC_$_INSTANCE_VARIABLES_NSPPrivacyProxyQuotaService
+ __OBJC_$_INSTANCE_VARIABLES_NSPPrivacyProxyQuotaServiceRequest
+ __OBJC_$_INSTANCE_VARIABLES_NSPPrivacyProxyQuotaServiceResponse
+ __OBJC_$_INSTANCE_VARIABLES_NSPPrivacyProxySuccessResponse
+ __OBJC_$_PROP_LIST_NSPPrivacyProxyCost
+ __OBJC_$_PROP_LIST_NSPPrivacyProxyErrorResponse
+ __OBJC_$_PROP_LIST_NSPPrivacyProxyGetQuotaRequest
+ __OBJC_$_PROP_LIST_NSPPrivacyProxyGetQuotaResponse
+ __OBJC_$_PROP_LIST_NSPPrivacyProxyQuota
+ __OBJC_$_PROP_LIST_NSPPrivacyProxyQuotaInfo
+ __OBJC_$_PROP_LIST_NSPPrivacyProxyQuotaService
+ __OBJC_$_PROP_LIST_NSPPrivacyProxyQuotaServiceRequest
+ __OBJC_$_PROP_LIST_NSPPrivacyProxyQuotaServiceResponse
+ __OBJC_$_PROP_LIST_NSPPrivacyProxySuccessResponse
+ __OBJC_CLASS_PROTOCOLS_$_NSPPrivacyProxyCost
+ __OBJC_CLASS_PROTOCOLS_$_NSPPrivacyProxyErrorResponse
+ __OBJC_CLASS_PROTOCOLS_$_NSPPrivacyProxyGetQuotaRequest
+ __OBJC_CLASS_PROTOCOLS_$_NSPPrivacyProxyGetQuotaResponse
+ __OBJC_CLASS_PROTOCOLS_$_NSPPrivacyProxyQuota
+ __OBJC_CLASS_PROTOCOLS_$_NSPPrivacyProxyQuotaInfo
+ __OBJC_CLASS_PROTOCOLS_$_NSPPrivacyProxyQuotaService
+ __OBJC_CLASS_PROTOCOLS_$_NSPPrivacyProxyQuotaServiceRequest
+ __OBJC_CLASS_PROTOCOLS_$_NSPPrivacyProxyQuotaServiceResponse
+ __OBJC_CLASS_PROTOCOLS_$_NSPPrivacyProxySuccessResponse
+ __OBJC_CLASS_RO_$_NSPPrivacyProxyCost
+ __OBJC_CLASS_RO_$_NSPPrivacyProxyErrorResponse
+ __OBJC_CLASS_RO_$_NSPPrivacyProxyGetQuotaRequest
+ __OBJC_CLASS_RO_$_NSPPrivacyProxyGetQuotaResponse
+ __OBJC_CLASS_RO_$_NSPPrivacyProxyQuota
+ __OBJC_CLASS_RO_$_NSPPrivacyProxyQuotaInfo
+ __OBJC_CLASS_RO_$_NSPPrivacyProxyQuotaService
+ __OBJC_CLASS_RO_$_NSPPrivacyProxyQuotaServiceRequest
+ __OBJC_CLASS_RO_$_NSPPrivacyProxyQuotaServiceResponse
+ __OBJC_CLASS_RO_$_NSPPrivacyProxySuccessResponse
+ __OBJC_METACLASS_RO_$_NSPPrivacyProxyCost
+ __OBJC_METACLASS_RO_$_NSPPrivacyProxyErrorResponse
+ __OBJC_METACLASS_RO_$_NSPPrivacyProxyGetQuotaRequest
+ __OBJC_METACLASS_RO_$_NSPPrivacyProxyGetQuotaResponse
+ __OBJC_METACLASS_RO_$_NSPPrivacyProxyQuota
+ __OBJC_METACLASS_RO_$_NSPPrivacyProxyQuotaInfo
+ __OBJC_METACLASS_RO_$_NSPPrivacyProxyQuotaService
+ __OBJC_METACLASS_RO_$_NSPPrivacyProxyQuotaServiceRequest
+ __OBJC_METACLASS_RO_$_NSPPrivacyProxyQuotaServiceResponse
+ __OBJC_METACLASS_RO_$_NSPPrivacyProxySuccessResponse
+ ___83-[NSPPrivateAccessTokenFetcher checkRemainingCostQuotaWithQueue:completionHandler:]_block_invoke
+ ___83-[NSPPrivateAccessTokenFetcher checkRemainingCostQuotaWithQueue:completionHandler:]_block_invoke.203
+ ___83-[NSPServerClient checkRemainingCostQuotaWithFetcher:allowRetry:completionHandler:]_block_invoke
+ ___block_descriptor_48_e8_32s40bs_e34_v40?0d8d16"NSDate"24"NSError"32ls32l8s40l8
+ ___block_descriptor_72_e8_32s40s48bs_e5_v8?0ls48l8s32l8s40l8
+ _objc_msgSend$addQuotaServices:
+ _objc_msgSend$addSupportedUseCaseIdentifiers:
+ _objc_msgSend$checkRemainingCostQuotaWithFetcher:allowRetry:completionHandler:
+ _objc_msgSend$clearOneofValuesForGetQuotaResponseType
+ _objc_msgSend$clearOneofValuesForRequestType
+ _objc_msgSend$clearQuotaServices
+ _objc_msgSend$clearSupportedUseCaseIdentifiers
+ _objc_msgSend$dateWithTimeIntervalSince1970:
+ _objc_msgSend$quotaServicesAtIndex:
+ _objc_msgSend$quotaServicesCount
+ _objc_msgSend$setBaa:
+ _objc_msgSend$setCost:
+ _objc_msgSend$setErrorReason:
+ _objc_msgSend$setGenericError:
+ _objc_msgSend$setQuota:
+ _objc_msgSend$setQuotaInfo:
+ _objc_msgSend$setRequest:
+ _objc_msgSend$setResponse:
+ _objc_msgSend$setServiceURL:
+ _objc_msgSend$setSuccess:
+ _objc_msgSend$setUseCaseIdentifier:
+ _objc_msgSend$supportedUseCaseIdentifiersAtIndex:
+ _objc_msgSend$supportedUseCaseIdentifiersCount
+ _xpc_dictionary_get_double
CStrings:
+ "-[NSPPrivateAccessTokenFetcher checkRemainingCostQuotaWithQueue:completionHandler:]"
+ "@\"NSPPrivacyProxyCost\""
+ "@\"NSPPrivacyProxyErrorResponse\""
+ "@\"NSPPrivacyProxyGetQuotaRequest\""
+ "@\"NSPPrivacyProxyGetQuotaResponse\""
+ "@\"NSPPrivacyProxyQuota\""
+ "@\"NSPPrivacyProxyQuotaInfo\""
+ "@\"NSPPrivacyProxySuccessResponse\""
+ "Check cost quota got invalid connection, retrying"
+ "Checking remaining cost quota"
+ "Failed to check remaining cost quota: %@"
+ "GetQuotaResponseType"
+ "NSPPrivacyProxyCost"
+ "NSPPrivacyProxyErrorResponse"
+ "NSPPrivacyProxyGetQuotaRequest"
+ "NSPPrivacyProxyGetQuotaResponse"
+ "NSPPrivacyProxyQuota"
+ "NSPPrivacyProxyQuotaInfo"
+ "NSPPrivacyProxyQuotaService"
+ "NSPPrivacyProxyQuotaServiceRequest"
+ "NSPPrivacyProxyQuotaServiceResponse"
+ "NSPPrivacyProxySuccessResponse"
+ "NSPServerErrorRequestUUID"
+ "NSPServerQuotaCostLimit"
+ "NSPServerQuotaCostRemaining"
+ "NSPServerQuotaExpiration"
+ "PBUNSET"
+ "RequestType"
+ "StringAsGetQuotaResponseType:"
+ "StringAsRequestType:"
+ "T@\"NSMutableArray\",&,N,V_quotaServices"
+ "T@\"NSMutableArray\",&,N,V_supportedUseCaseIdentifiers"
+ "T@\"NSPPrivacyProxyBAAValidation\",&,N,V_baa"
+ "T@\"NSPPrivacyProxyCost\",&,N,V_cost"
+ "T@\"NSPPrivacyProxyErrorResponse\",&,N,V_genericError"
+ "T@\"NSPPrivacyProxyGetQuotaRequest\",&,N,V_request"
+ "T@\"NSPPrivacyProxyGetQuotaResponse\",&,N,V_response"
+ "T@\"NSPPrivacyProxyQuota\",&,N,V_quota"
+ "T@\"NSPPrivacyProxyQuotaInfo\",&,N,V_quotaInfo"
+ "T@\"NSPPrivacyProxySuccessResponse\",&,N,V_success"
+ "T@\"NSString\",&,N,V_errorReason"
+ "T@\"NSString\",&,N,V_serviceURL"
+ "T@\"NSString\",&,N,V_useCaseIdentifier"
+ "TB,N,V_supportsTokenUsageFeedback"
+ "Td,N,V_limit"
+ "Td,N,V_remaining"
+ "Ti,N,V_getQuotaResponseType"
+ "Ti,N,V_requestType"
+ "_baa"
+ "_cost"
+ "_errorReason"
+ "_genericError"
+ "_getQuotaResponseType"
+ "_limit"
+ "_quota"
+ "_quotaInfo"
+ "_quotaServices"
+ "_remaining"
+ "_request"
+ "_requestType"
+ "_response"
+ "_serviceURL"
+ "_success"
+ "_supportedUseCaseIdentifiers"
+ "_supportsTokenUsageFeedback"
+ "_useCaseIdentifier"
+ "addQuotaServices:"
+ "addSupportedUseCaseIdentifiers:"
+ "baa"
+ "checkRemainingCostQuotaWithFetcher:allowRetry:completionHandler:"
+ "checkRemainingCostQuotaWithQueue:completionHandler:"
+ "clearOneofValuesForGetQuotaResponseType"
+ "clearOneofValuesForRequestType"
+ "clearQuotaServices"
+ "clearSupportedUseCaseIdentifiers"
+ "cost"
+ "dateWithTimeIntervalSince1970:"
+ "errorReason"
+ "genericError"
+ "generic_error"
+ "getQuotaResponseType"
+ "getQuotaResponseTypeAsString:"
+ "hasBaa"
+ "hasCost"
+ "hasErrorReason"
+ "hasGenericError"
+ "hasGetQuotaResponseType"
+ "hasLimit"
+ "hasQuota"
+ "hasQuotaInfo"
+ "hasRemaining"
+ "hasRequest"
+ "hasRequestType"
+ "hasResponse"
+ "hasServiceURL"
+ "hasSuccess"
+ "hasSupportsTokenUsageFeedback"
+ "hasUseCaseIdentifier"
+ "limit"
+ "quota"
+ "quotaInfo"
+ "quotaServices"
+ "quotaServicesAtIndex:"
+ "quotaServicesCount"
+ "quotaServicesType"
+ "remaining"
+ "request"
+ "requestType"
+ "requestTypeAsString:"
+ "response"
+ "serviceURL"
+ "setBaa:"
+ "setCost:"
+ "setErrorReason:"
+ "setGenericError:"
+ "setGetQuotaResponseType:"
+ "setHasGetQuotaResponseType:"
+ "setHasLimit:"
+ "setHasRemaining:"
+ "setHasRequestType:"
+ "setHasSupportsTokenUsageFeedback:"
+ "setLimit:"
+ "setQuota:"
+ "setQuotaInfo:"
+ "setQuotaServices:"
+ "setRemaining:"
+ "setRequest:"
+ "setRequestType:"
+ "setResponse:"
+ "setServiceURL:"
+ "setSuccess:"
+ "setSupportedUseCaseIdentifiers:"
+ "setSupportsTokenUsageFeedback:"
+ "setUseCaseIdentifier:"
+ "success"
+ "supportedUseCaseIdentifiers"
+ "supportedUseCaseIdentifiersAtIndex:"
+ "supportedUseCaseIdentifiersCount"
+ "supportedUseCaseIdentifiersType"
+ "supportsTokenUsageFeedback"
+ "useCaseIdentifier"
+ "v36@0:8@\"NSPPrivateAccessTokenFetcher\"16B24@?<v@?dd@\"NSDate\"@\"NSError\">28"
+ "v40@?0d8d16@\"NSDate\"24@\"NSError\"32"
+ "{?=\"expiration\"b1}"
+ "{?=\"getQuotaResponseType\"b1}"
+ "{?=\"limit\"b1\"remaining\"b1}"
+ "{?=\"requestType\"b1}"
+ "{?=\"supportsTokenUsageFeedback\"b1}"

```
