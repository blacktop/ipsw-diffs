## NetworkServiceProxy

> `/System/Library/PrivateFrameworks/NetworkServiceProxy.framework/Versions/A/NetworkServiceProxy`

```diff

-985.0.0.0.0
-  __TEXT.__text: 0x66c34
-  __TEXT.__objc_methlist: 0x601c
+990.0.0.0.0
+  __TEXT.__text: 0x6aa40
+  __TEXT.__objc_methlist: 0x654c
   __TEXT.__const: 0x378
   __TEXT.__gcc_except_tab: 0xb4
-  __TEXT.__cstring: 0x5ae0
+  __TEXT.__cstring: 0x5b9a
   __TEXT.__oslogstring: 0x336e
-  __TEXT.__unwind_info: 0x14f8
+  __TEXT.__unwind_info: 0x1608
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x628
-  __DATA_CONST.__objc_classlist: 0x220
+  __DATA_CONST.__const: 0x668
+  __DATA_CONST.__objc_classlist: 0x240
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2a00
-  __DATA_CONST.__objc_superrefs: 0x208
+  __DATA_CONST.__objc_selrefs: 0x2b28
+  __DATA_CONST.__objc_superrefs: 0x228
   __DATA_CONST.__objc_arraydata: 0x48
-  __DATA_CONST.__got: 0x480
+  __DATA_CONST.__got: 0x490
   __AUTH_CONST.__const: 0x8e0
-  __AUTH_CONST.__cfstring: 0x5160
-  __AUTH_CONST.__objc_const: 0x80e0
+  __AUTH_CONST.__cfstring: 0x52e0
+  __AUTH_CONST.__objc_const: 0x8660
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__auth_got: 0x628
-  __AUTH.__objc_data: 0x1400
+  __AUTH_CONST.__auth_got: 0x620
+  __AUTH.__objc_data: 0x1540
   __DATA.__objc_ivar: 0x334
   __DATA.__data: 0x268
   __DATA.__common: 0x1
-  __DATA_DIRTY.__objc_ivar: 0x2dc
+  __DATA_DIRTY.__objc_ivar: 0x310
   __DATA_DIRTY.__objc_data: 0x140
   __DATA_DIRTY.__bss: 0x98
   __DATA_DIRTY.__common: 0x20

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2143
-  Symbols:   4071
-  CStrings:  1224
+  Functions: 2251
+  Symbols:   4232
+  CStrings:  1236
 
Symbols:
+ +[NSPPrivacyProxyDenominationResult tokenResponsesType]
+ +[NSPPrivacyProxyFailedExpiringTokens privacyPassTokensType]
+ +[NSPPrivacyProxyTokenRefundRequest denominationRequestsType]
+ +[NSPPrivacyProxyTokenRefundRequest privacyPassTokensType]
+ +[NSPPrivacyProxyTokenRefundResponse failedType]
+ +[NSPPrivacyProxyTokenRefundResponse resultsType]
+ -[NSPPrivacyProxyDenominationResult .cxx_destruct]
+ -[NSPPrivacyProxyDenominationResult StringAsStatus:]
+ -[NSPPrivacyProxyDenominationResult addTokenResponses:]
+ -[NSPPrivacyProxyDenominationResult clearTokenResponses]
+ -[NSPPrivacyProxyDenominationResult copyTo:]
+ -[NSPPrivacyProxyDenominationResult copyWithZone:]
+ -[NSPPrivacyProxyDenominationResult denominationIssuer]
+ -[NSPPrivacyProxyDenominationResult description]
+ -[NSPPrivacyProxyDenominationResult dictionaryRepresentation]
+ -[NSPPrivacyProxyDenominationResult hasDenominationIssuer]
+ -[NSPPrivacyProxyDenominationResult hasStatus]
+ -[NSPPrivacyProxyDenominationResult hash]
+ -[NSPPrivacyProxyDenominationResult isEqual:]
+ -[NSPPrivacyProxyDenominationResult mergeFrom:]
+ -[NSPPrivacyProxyDenominationResult readFrom:]
+ -[NSPPrivacyProxyDenominationResult setDenominationIssuer:]
+ -[NSPPrivacyProxyDenominationResult setHasStatus:]
+ -[NSPPrivacyProxyDenominationResult setStatus:]
+ -[NSPPrivacyProxyDenominationResult setTokenResponses:]
+ -[NSPPrivacyProxyDenominationResult statusAsString:]
+ -[NSPPrivacyProxyDenominationResult status]
+ -[NSPPrivacyProxyDenominationResult tokenResponsesAtIndex:]
+ -[NSPPrivacyProxyDenominationResult tokenResponsesCount]
+ -[NSPPrivacyProxyDenominationResult tokenResponses]
+ -[NSPPrivacyProxyDenominationResult writeTo:]
+ -[NSPPrivacyProxyFailedExpiringTokens .cxx_destruct]
+ -[NSPPrivacyProxyFailedExpiringTokens StringAsReason:]
+ -[NSPPrivacyProxyFailedExpiringTokens addPrivacyPassTokens:]
+ -[NSPPrivacyProxyFailedExpiringTokens clearPrivacyPassTokens]
+ -[NSPPrivacyProxyFailedExpiringTokens copyTo:]
+ -[NSPPrivacyProxyFailedExpiringTokens copyWithZone:]
+ -[NSPPrivacyProxyFailedExpiringTokens description]
+ -[NSPPrivacyProxyFailedExpiringTokens dictionaryRepresentation]
+ -[NSPPrivacyProxyFailedExpiringTokens hasReason]
+ -[NSPPrivacyProxyFailedExpiringTokens hasReusable]
+ -[NSPPrivacyProxyFailedExpiringTokens hash]
+ -[NSPPrivacyProxyFailedExpiringTokens isEqual:]
+ -[NSPPrivacyProxyFailedExpiringTokens mergeFrom:]
+ -[NSPPrivacyProxyFailedExpiringTokens privacyPassTokensAtIndex:]
+ -[NSPPrivacyProxyFailedExpiringTokens privacyPassTokensCount]
+ -[NSPPrivacyProxyFailedExpiringTokens privacyPassTokens]
+ -[NSPPrivacyProxyFailedExpiringTokens readFrom:]
+ -[NSPPrivacyProxyFailedExpiringTokens reasonAsString:]
+ -[NSPPrivacyProxyFailedExpiringTokens reason]
+ -[NSPPrivacyProxyFailedExpiringTokens reusable]
+ -[NSPPrivacyProxyFailedExpiringTokens setHasReason:]
+ -[NSPPrivacyProxyFailedExpiringTokens setHasReusable:]
+ -[NSPPrivacyProxyFailedExpiringTokens setPrivacyPassTokens:]
+ -[NSPPrivacyProxyFailedExpiringTokens setReason:]
+ -[NSPPrivacyProxyFailedExpiringTokens setReusable:]
+ -[NSPPrivacyProxyFailedExpiringTokens writeTo:]
+ -[NSPPrivacyProxyTokenRefundRequest .cxx_destruct]
+ -[NSPPrivacyProxyTokenRefundRequest addDenominationRequests:]
+ -[NSPPrivacyProxyTokenRefundRequest addPrivacyPassTokens:]
+ -[NSPPrivacyProxyTokenRefundRequest clearDenominationRequests]
+ -[NSPPrivacyProxyTokenRefundRequest clearPrivacyPassTokens]
+ -[NSPPrivacyProxyTokenRefundRequest copyTo:]
+ -[NSPPrivacyProxyTokenRefundRequest copyWithZone:]
+ -[NSPPrivacyProxyTokenRefundRequest denominationRequestsAtIndex:]
+ -[NSPPrivacyProxyTokenRefundRequest denominationRequestsCount]
+ -[NSPPrivacyProxyTokenRefundRequest denominationRequests]
+ -[NSPPrivacyProxyTokenRefundRequest description]
+ -[NSPPrivacyProxyTokenRefundRequest dictionaryRepresentation]
+ -[NSPPrivacyProxyTokenRefundRequest expiringTokenIssuerName]
+ -[NSPPrivacyProxyTokenRefundRequest hasExpiringTokenIssuerName]
+ -[NSPPrivacyProxyTokenRefundRequest hash]
+ -[NSPPrivacyProxyTokenRefundRequest isEqual:]
+ -[NSPPrivacyProxyTokenRefundRequest mergeFrom:]
+ -[NSPPrivacyProxyTokenRefundRequest privacyPassTokensAtIndex:]
+ -[NSPPrivacyProxyTokenRefundRequest privacyPassTokensCount]
+ -[NSPPrivacyProxyTokenRefundRequest privacyPassTokens]
+ -[NSPPrivacyProxyTokenRefundRequest readFrom:]
+ -[NSPPrivacyProxyTokenRefundRequest setDenominationRequests:]
+ -[NSPPrivacyProxyTokenRefundRequest setExpiringTokenIssuerName:]
+ -[NSPPrivacyProxyTokenRefundRequest setPrivacyPassTokens:]
+ -[NSPPrivacyProxyTokenRefundRequest writeTo:]
+ -[NSPPrivacyProxyTokenRefundResponse .cxx_destruct]
+ -[NSPPrivacyProxyTokenRefundResponse addFailed:]
+ -[NSPPrivacyProxyTokenRefundResponse addResults:]
+ -[NSPPrivacyProxyTokenRefundResponse clearFaileds]
+ -[NSPPrivacyProxyTokenRefundResponse clearResults]
+ -[NSPPrivacyProxyTokenRefundResponse copyTo:]
+ -[NSPPrivacyProxyTokenRefundResponse copyWithZone:]
+ -[NSPPrivacyProxyTokenRefundResponse description]
+ -[NSPPrivacyProxyTokenRefundResponse dictionaryRepresentation]
+ -[NSPPrivacyProxyTokenRefundResponse failedAtIndex:]
+ -[NSPPrivacyProxyTokenRefundResponse failedsCount]
+ -[NSPPrivacyProxyTokenRefundResponse faileds]
+ -[NSPPrivacyProxyTokenRefundResponse hash]
+ -[NSPPrivacyProxyTokenRefundResponse isEqual:]
+ -[NSPPrivacyProxyTokenRefundResponse mergeFrom:]
+ -[NSPPrivacyProxyTokenRefundResponse readFrom:]
+ -[NSPPrivacyProxyTokenRefundResponse resultsAtIndex:]
+ -[NSPPrivacyProxyTokenRefundResponse resultsCount]
+ -[NSPPrivacyProxyTokenRefundResponse results]
+ -[NSPPrivacyProxyTokenRefundResponse setFaileds:]
+ -[NSPPrivacyProxyTokenRefundResponse setResults:]
+ -[NSPPrivacyProxyTokenRefundResponse writeTo:]
+ _NSPPrivacyProxyDenominationResultReadFrom
+ _NSPPrivacyProxyFailedExpiringTokensReadFrom
+ _NSPPrivacyProxyTokenRefundRequestReadFrom
+ _NSPPrivacyProxyTokenRefundResponseReadFrom
+ _OBJC_CLASS_$_NSPPrivacyProxyDenominationResult
+ _OBJC_CLASS_$_NSPPrivacyProxyFailedExpiringTokens
+ _OBJC_CLASS_$_NSPPrivacyProxyTokenRefundRequest
+ _OBJC_CLASS_$_NSPPrivacyProxyTokenRefundResponse
+ _OBJC_METACLASS_$_NSPPrivacyProxyDenominationResult
+ _OBJC_METACLASS_$_NSPPrivacyProxyFailedExpiringTokens
+ _OBJC_METACLASS_$_NSPPrivacyProxyTokenRefundRequest
+ _OBJC_METACLASS_$_NSPPrivacyProxyTokenRefundResponse
+ __OBJC_$_CLASS_METHODS_NSPPrivacyProxyDenominationResult
+ __OBJC_$_CLASS_METHODS_NSPPrivacyProxyFailedExpiringTokens
+ __OBJC_$_CLASS_METHODS_NSPPrivacyProxyTokenRefundRequest
+ __OBJC_$_CLASS_METHODS_NSPPrivacyProxyTokenRefundResponse
+ __OBJC_$_INSTANCE_METHODS_NSPPrivacyProxyDenominationResult
+ __OBJC_$_INSTANCE_METHODS_NSPPrivacyProxyFailedExpiringTokens
+ __OBJC_$_INSTANCE_METHODS_NSPPrivacyProxyTokenRefundRequest
+ __OBJC_$_INSTANCE_METHODS_NSPPrivacyProxyTokenRefundResponse
+ __OBJC_$_INSTANCE_VARIABLES_NSPPrivacyProxyDenominationResult
+ __OBJC_$_INSTANCE_VARIABLES_NSPPrivacyProxyFailedExpiringTokens
+ __OBJC_$_INSTANCE_VARIABLES_NSPPrivacyProxyTokenRefundRequest
+ __OBJC_$_INSTANCE_VARIABLES_NSPPrivacyProxyTokenRefundResponse
+ __OBJC_$_PROP_LIST_NSPPrivacyProxyDenominationResult
+ __OBJC_$_PROP_LIST_NSPPrivacyProxyFailedExpiringTokens
+ __OBJC_$_PROP_LIST_NSPPrivacyProxyTokenRefundRequest
+ __OBJC_$_PROP_LIST_NSPPrivacyProxyTokenRefundResponse
+ __OBJC_CLASS_PROTOCOLS_$_NSPPrivacyProxyDenominationResult
+ __OBJC_CLASS_PROTOCOLS_$_NSPPrivacyProxyFailedExpiringTokens
+ __OBJC_CLASS_PROTOCOLS_$_NSPPrivacyProxyTokenRefundRequest
+ __OBJC_CLASS_PROTOCOLS_$_NSPPrivacyProxyTokenRefundResponse
+ __OBJC_CLASS_RO_$_NSPPrivacyProxyDenominationResult
+ __OBJC_CLASS_RO_$_NSPPrivacyProxyFailedExpiringTokens
+ __OBJC_CLASS_RO_$_NSPPrivacyProxyTokenRefundRequest
+ __OBJC_CLASS_RO_$_NSPPrivacyProxyTokenRefundResponse
+ __OBJC_METACLASS_RO_$_NSPPrivacyProxyDenominationResult
+ __OBJC_METACLASS_RO_$_NSPPrivacyProxyFailedExpiringTokens
+ __OBJC_METACLASS_RO_$_NSPPrivacyProxyTokenRefundRequest
+ __OBJC_METACLASS_RO_$_NSPPrivacyProxyTokenRefundResponse
+ _objc_msgSend$addDenominationRequests:
+ _objc_msgSend$addFailed:
+ _objc_msgSend$addPrivacyPassTokens:
+ _objc_msgSend$addResults:
+ _objc_msgSend$clearDenominationRequests
+ _objc_msgSend$clearFaileds
+ _objc_msgSend$clearPrivacyPassTokens
+ _objc_msgSend$clearResults
+ _objc_msgSend$denominationRequestsAtIndex:
+ _objc_msgSend$denominationRequestsCount
+ _objc_msgSend$failedAtIndex:
+ _objc_msgSend$failedsCount
+ _objc_msgSend$privacyPassTokensAtIndex:
+ _objc_msgSend$privacyPassTokensCount
+ _objc_msgSend$resultsAtIndex:
+ _objc_msgSend$resultsCount
+ _objc_msgSend$setDenominationIssuer:
+ _objc_msgSend$setExpiringTokenIssuerName:
- _os_variant_has_internal_content
CStrings:
+ "DENOMINATION_TOO_SMALL"
+ "FULFILLED"
+ "INSUFFICIENT_VALUE"
+ "INVALID_KEY"
+ "KEY_EXPIRED"
+ "SERVER_ERROR"
+ "denominationIssuer"
+ "denominationRequests"
+ "expiringTokenIssuerName"
+ "failed"
+ "privacyPassTokens"
+ "results"
```
