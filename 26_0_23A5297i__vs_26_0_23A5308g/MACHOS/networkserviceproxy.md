## networkserviceproxy

> `/usr/libexec/networkserviceproxy`

```diff

-902.0.0.0.1
-  __TEXT.__text: 0xb5114
-  __TEXT.__auth_stubs: 0x18c0
-  __TEXT.__objc_stubs: 0xc000
-  __TEXT.__objc_methlist: 0x4d84
+906.0.1.0.0
+  __TEXT.__text: 0xb7770
+  __TEXT.__auth_stubs: 0x18d0
+  __TEXT.__objc_stubs: 0xc280
+  __TEXT.__objc_methlist: 0x4dec
   __TEXT.__const: 0x321
   __TEXT.__dlopen_cstrs: 0x64
-  __TEXT.__gcc_except_tab: 0x3ee4
-  __TEXT.__oslogstring: 0xfca2
-  __TEXT.__cstring: 0xccdf
-  __TEXT.__objc_methname: 0xf1e8
+  __TEXT.__gcc_except_tab: 0x3f6c
+  __TEXT.__oslogstring: 0xfe9e
+  __TEXT.__cstring: 0xcf62
+  __TEXT.__objc_methname: 0xf3f8
   __TEXT.__objc_classname: 0xc7b
-  __TEXT.__objc_methtype: 0x27ee
-  __TEXT.__unwind_info: 0x1850
-  __DATA_CONST.__auth_got: 0xc70
-  __DATA_CONST.__got: 0x6c8
-  __DATA_CONST.__const: 0x1f50
-  __DATA_CONST.__cfstring: 0x8100
+  __TEXT.__objc_methtype: 0x28db
+  __TEXT.__unwind_info: 0x1880
+  __DATA_CONST.__auth_got: 0xc78
+  __DATA_CONST.__got: 0x6e0
+  __DATA_CONST.__auth_ptr: 0x8
+  __DATA_CONST.__const: 0x2040
+  __DATA_CONST.__cfstring: 0x81a0
   __DATA_CONST.__objc_classlist: 0x2c8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xf0

   __DATA_CONST.__objc_arrayobj: 0xf0
   __DATA_CONST.__objc_intobj: 0x648
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0xad50
-  __DATA.__objc_selrefs: 0x3668
+  __DATA.__objc_const: 0xad60
+  __DATA.__objc_selrefs: 0x3710
   __DATA.__objc_ivar: 0x9bc
   __DATA.__objc_data: 0x1bd0
   __DATA.__data: 0xb48

   - /usr/lib/libmrc.dylib
   - /usr/lib/libnetworkextension.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B9099B21-5B66-3DB2-A49D-878948E67E4F
-  Functions: 2062
-  Symbols:   627
-  CStrings:  6946
+  UUID: DDC8B552-CB15-3689-9533-15FD9565C0B2
+  Functions: 2078
+  Symbols:   632
+  CStrings:  7000
 
Symbols:
+ _OBJC_CLASS_$_NSPPrivacyProxyGetQuotaRequest
+ _OBJC_CLASS_$_NSPPrivacyProxyQuotaServiceRequest
+ _OBJC_CLASS_$_NSPPrivacyProxyQuotaServiceResponse
+ ___chkstk_darwin
+ _objc_release_x10
CStrings:
+ "%s called with null quotaServiceRequest"
+ "%s called with null serviceURLComponents"
+ "%s called with null urlSession"
+ "+[NSPBAA_Anisette sendRequestForQuota:urlSession:quotaServiceRequest:completionHandler:]"
+ "+[NSPPrivateAccessTokenCache copyTokenFromCacheForChallenge:tokenKeys:tokensRemaining:]"
+ "-[NSPPrivacyTokenManager checkCostQuotaForIssuerName:quotaService:auditToken:bundleID:accessToken:completionHandler:]"
+ "-[NSPPrivacyTokenManager fetchPrivateAccessTokenForChallenge:overrideAttester:supportsTokenUsageFeedback:customAttester:customAttesterHeaders:tokenKey:originNameKey:selectedOrigin:auxiliaryAuthInfoCacheKey:rateLimit:auditToken:bundleID:allowTools:systemTokenClient:accessToken:completionHandler:]"
+ "-[NSPPrivateAccessTokenFetcher checkRemainingCostQuotaWithQueue:completionHandler:]"
+ "Cached long-lived token from keychain for \"%@\" has non-matching challenge, flushing tokens"
+ "Cached one-time token from keychain for \"%@\" has non-matching challenge, flushing tokens"
+ "Cached token from keychain for \"%@\" has non-matching challenge, flushing tokens"
+ "Checking cost quota for %@"
+ "CostQuotaFetch"
+ "Failed to check remaining cost quota: %@"
+ "Failed to find known quota service for challenge (issuer name: %@)"
+ "Failed to parse service URL for quota service: %@"
+ "NSPServerErrorRequestUUID"
+ "NSPServerQuotaCostLimit"
+ "NSPServerQuotaCostRemaining"
+ "NSPServerQuotaExpiration"
+ "No matching quota service"
+ "No quota service URL"
+ "Quota service server error"
+ "Received %f/%f cost quota from %@, expiring at %llu"
+ "Received check quota error %@ for %@"
+ "System client entitlement missing, cannot check cost quota"
+ "Unknown error"
+ "checkCostQuotaForIssuerName:quotaService:auditToken:bundleID:accessToken:completionHandler:"
+ "checkRemainingCostQuotaWithFetcher:allowRetry:completionHandler:"
+ "checkRemainingCostQuotaWithQueue:completionHandler:"
+ "cost"
+ "errorReason"
+ "failed to cost quota due to missing delegation entitlement for %s"
+ "fetchPrivateAccessTokenForChallenge:overrideAttester:supportsTokenUsageFeedback:customAttester:customAttesterHeaders:tokenKey:originNameKey:selectedOrigin:auxiliaryAuthInfoCacheKey:rateLimit:auditToken:bundleID:allowTools:systemTokenClient:accessToken:completionHandler:"
+ "genericError"
+ "hasGenericError"
+ "hasSuccess"
+ "quota"
+ "quotaInfo"
+ "quotaServices"
+ "remaining"
+ "request"
+ "response"
+ "sendRequestForQuota:urlSession:quotaServiceRequest:completionHandler:"
+ "serviceURL"
+ "setBaa:"
+ "setRequest:"
+ "setUseCaseIdentifier:"
+ "supportedUseCaseIdentifiers"
+ "supportsTokenUsageFeedback"
+ "v128@0:8@16@24B32@36@44@52@60@68@76I84@88@96B104B108@112@?120"
+ "v36@0:8@\"NSPPrivateAccessTokenFetcher\"16B24@?<v@?dd@\"NSDate\"@\"NSError\">28"
+ "v40@?0@\"NSData\"8q16@\"NSString\"24@\"NSString\"32"
+ "v40@?0d8d16@\"NSDate\"24@\"NSError\"32"
+ "v48@0:8@\"NSMutableURLRequest\"16@\"NSURLSession\"24@\"NSPPrivacyProxyQuotaServiceRequest\"32@?<v@?i@\"NSData\"@\"NSURLResponse\"@\"NSError\">40"
+ "v56@?0@\"NSData\"8@\"NSData\"16@\"NSData\"24q32@\"NSString\"40@\"NSString\"48"
+ "v56@?0d8d16Q24q32@\"NSString\"40@\"NSString\"48"
+ "v64@0:8@16@24@32@40@48@?56"
+ "v64@?0@\"NSArray\"8@\"NSArray\"16@\"NSDate\"24@\"NSDictionary\"32q40@\"NSString\"48@\"NSString\"56"
- "+[NSPPrivateAccessTokenCache copyTokenFromCacheForChallenge:tokenKey:tokensRemaining:]"
- "-[NSPPrivacyTokenManager fetchPrivateAccessTokenForChallenge:overrideAttester:customAttester:customAttesterHeaders:tokenKey:originNameKey:selectedOrigin:auxiliaryAuthInfoCacheKey:rateLimit:auditToken:bundleID:allowTools:systemTokenClient:accessToken:completionHandler:]"
- "Cached long-lived token from keychain for \"%@\" has non-matching challenege, flushing tokens"
- "Cached one-time token from keychain for \"%@\" has non-matching challenege, flushing tokens"
- "Cached token from keychain for \"%@\" has non-matching challenege, flushing tokens"
- "fetchPrivateAccessTokenForChallenge:overrideAttester:customAttester:customAttesterHeaders:tokenKey:originNameKey:selectedOrigin:auxiliaryAuthInfoCacheKey:rateLimit:auditToken:bundleID:allowTools:systemTokenClient:accessToken:completionHandler:"
- "v124@0:8@16@24@32@40@48@56@64@72I80@84@92B100B104@108@?116"
- "v32@?0@\"NSData\"8q16@\"NSString\"24"
- "v48@?0@\"NSData\"8@\"NSData\"16@\"NSData\"24q32@\"NSString\"40"
- "v56@?0@\"NSArray\"8@\"NSArray\"16@\"NSDate\"24@\"NSDictionary\"32q40@\"NSString\"48"

```
