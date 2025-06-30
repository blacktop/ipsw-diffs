## HealthRecordServices

> `/System/Library/PrivateFrameworks/HealthRecordServices.framework/HealthRecordServices`

```diff

-4146.3.2.0.0
-  __TEXT.__text: 0x38150
-  __TEXT.__auth_stubs: 0x570
-  __TEXT.__objc_methlist: 0x4780
+4146.4.18.0.0
+  __TEXT.__text: 0x38e28
+  __TEXT.__auth_stubs: 0x5a0
+  __TEXT.__objc_methlist: 0x4870
   __TEXT.__const: 0xd8
-  __TEXT.__cstring: 0x2f9c
+  __TEXT.__cstring: 0x2fe0
   __TEXT.__ustring: 0x78
-  __TEXT.__oslogstring: 0xa5d
+  __TEXT.__oslogstring: 0xac0
   __TEXT.__gcc_except_tab: 0x104
-  __TEXT.__unwind_info: 0x1260
-  __TEXT.__objc_classname: 0xf05
-  __TEXT.__objc_methname: 0xad46
-  __TEXT.__objc_methtype: 0x21f1
-  __TEXT.__objc_stubs: 0x5720
-  __DATA_CONST.__got: 0x180
+  __TEXT.__unwind_info: 0x1288
+  __TEXT.__objc_classname: 0xf2e
+  __TEXT.__objc_methname: 0xaf3e
+  __TEXT.__objc_methtype: 0x2210
+  __TEXT.__objc_stubs: 0x5880
+  __DATA_CONST.__got: 0x188
   __DATA_CONST.__const: 0x1330
-  __DATA_CONST.__objc_classlist: 0x2f0
+  __DATA_CONST.__objc_classlist: 0x2f8
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0xd0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x7420
-  __DATA_CONST.__objc_selrefs: 0x1d68
-  __AUTH_CONST.__cfstring: 0x40c0
-  __AUTH_CONST.__objc_const: 0x32a8
+  __DATA_CONST.__objc_const: 0x7558
+  __DATA_CONST.__objc_selrefs: 0x1dd8
+  __DATA_CONST.__objc_protorefs: 0x88
+  __DATA_CONST.__objc_classrefs: 0x350
+  __DATA_CONST.__objc_superrefs: 0x2b0
+  __AUTH_CONST.__cfstring: 0x4180
+  __AUTH_CONST.__objc_const: 0x3338
   __AUTH_CONST.__const: 0x2a0
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH_CONST.__auth_got: 0x2c8
-  __AUTH.__objc_data: 0x12c0
-  __DATA.__objc_protorefs: 0x88
-  __DATA.__objc_classrefs: 0x340
-  __DATA.__objc_superrefs: 0x2a8
-  __DATA.__objc_ivar: 0x550
+  __AUTH_CONST.__auth_got: 0x2e0
+  __AUTH.__objc_data: 0x1220
+  __DATA.__objc_ivar: 0x564
   __DATA.__data: 0x9d0
-  __DATA_DIRTY.__objc_data: 0xaa0
+  __DATA_DIRTY.__objc_data: 0xb90
   __DATA_DIRTY.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 4206CD68-E438-3C69-BB5D-AC1C3270680E
-  Functions: 1741
-  Symbols:   5872
-  CStrings:  2981
+  UUID: B2828C3B-282F-37D5-BCEB-C0A241E9E095
+  Functions: 1760
+  Symbols:   5941
+  CStrings:  3016
 
Symbols:
+ +[HKOAuth2LoginSession generatePKCEChallengeFromVerifier:algorithm:error:]
+ +[HKOAuth2LoginSession generatePKCEVerifierWithAlgorithm:]
+ +[HKOAuth2LoginSession generatePKCEVerifierWithAlgorithm:].cold.1
+ +[HKOAuth2LoginSession new]
+ +[HKOAuth2LoginSession supportsSecureCoding]
+ -[HKOAuth2LoginSession .cxx_destruct]
+ -[HKOAuth2LoginSession callbackURLComponents]
+ -[HKOAuth2LoginSession copyWithZone:]
+ -[HKOAuth2LoginSession encodeWithCoder:]
+ -[HKOAuth2LoginSession hash]
+ -[HKOAuth2LoginSession initWithCoder:]
+ -[HKOAuth2LoginSession initWithState:loginURL:callbackURLComponents:requestedScope:pkceVerifier:]
+ -[HKOAuth2LoginSession init]
+ -[HKOAuth2LoginSession isEqual:]
+ -[HKOAuth2LoginSession loginURL]
+ -[HKOAuth2LoginSession pkceVerifier]
+ -[HKOAuth2LoginSession requestedScope]
+ -[HKOAuth2LoginSession state]
+ -[NSData(HKBase64URLEncoding) hk_base64URLEncodedString]
+ _OBJC_CLASS_$_HKOAuth2LoginSession
+ _OBJC_CLASS_$_NSURLComponents
+ _OBJC_IVAR_$_HKOAuth2LoginSession._callbackURLComponents
+ _OBJC_IVAR_$_HKOAuth2LoginSession._loginURL
+ _OBJC_IVAR_$_HKOAuth2LoginSession._pkceVerifier
+ _OBJC_IVAR_$_HKOAuth2LoginSession._requestedScope
+ _OBJC_IVAR_$_HKOAuth2LoginSession._state
+ _OBJC_METACLASS_$_HKOAuth2LoginSession
+ _SecRandomCopyBytes
+ __OBJC_$_CLASS_METHODS_HKOAuth2LoginSession
+ __OBJC_$_CLASS_PROP_LIST_HKOAuth2LoginSession
+ __OBJC_$_INSTANCE_METHODS_HKOAuth2LoginSession
+ __OBJC_$_INSTANCE_METHODS_NSData(HealthRecordServices|HKBase64URLEncoding)
+ __OBJC_$_INSTANCE_VARIABLES_HKOAuth2LoginSession
+ __OBJC_$_PROP_LIST_HKOAuth2LoginSession
+ __OBJC_CLASS_PROTOCOLS_$_HKOAuth2LoginSession
+ __OBJC_CLASS_RO_$_HKOAuth2LoginSession
+ __OBJC_METACLASS_RO_$_HKOAuth2LoginSession
+ ___49-[HKClinicalAccountStore supportsClinicalSharing]_block_invoke.253
+ ___49-[HKClinicalAccountStore supportsClinicalSharing]_block_invoke.253.cold.1
+ ___52-[HKClinicalDocumentStore _establishProxyConnection]_block_invoke.246
+ ___52-[HKClinicalDocumentStore _establishProxyConnection]_block_invoke.246.cold.1
+ ___54-[HKClinicalSharingSyncObserver resumeWithCompletion:]_block_invoke.254
+ ___54-[HKClinicalSharingSyncObserver resumeWithCompletion:]_block_invoke.254.cold.1
+ ___54-[HKClinicalSharingSyncObserver resumeWithCompletion:]_block_invoke.256
+ ___54-[HKClinicalSharingSyncObserver resumeWithCompletion:]_block_invoke_2.260
+ ___54-[HKClinicalSharingSyncObserver resumeWithCompletion:]_block_invoke_2.260.cold.1
+ ___67-[HKClinicalAccountStore hasAnyHealthRecordsAccountWithCompletion:]_block_invoke.249
+ ___67-[HKClinicalAccountStore hasAnyHealthRecordsAccountWithCompletion:]_block_invoke.249.cold.1
+ ___71-[HKClinicalAccountStore shouldShowHealthRecordsSectionWithCompletion:]_block_invoke.252
+ ___71-[HKClinicalAccountStore shouldShowHealthRecordsSectionWithCompletion:]_block_invoke.252.cold.1
+ ___77-[HKClinicalAccountStore hasGatewayBackedHealthRecordsAccountWithCompletion:]_block_invoke.250
+ ___77-[HKClinicalAccountStore hasGatewayBackedHealthRecordsAccountWithCompletion:]_block_invoke.250.cold.1
+ ___block_literal_global.244
+ ___block_literal_global.247
+ ___block_literal_global.250
+ ___block_literal_global.253
+ ___block_literal_global.259
+ ___block_literal_global.260
+ ___block_literal_global.262
+ ___error
+ __os_log_fault_impl
+ _kSecRandomDefault
+ _objc_msgSend$base64EncodedStringWithOptions:
+ _objc_msgSend$callbackURLComponents
+ _objc_msgSend$componentsWithString:
+ _objc_msgSend$dataWithLength:
+ _objc_msgSend$hk_SHA256
+ _objc_msgSend$hk_base64URLEncodedString
+ _objc_msgSend$initWithState:loginURL:callbackURLComponents:requestedScope:pkceVerifier:
+ _objc_msgSend$loginURL
+ _objc_msgSend$mutableBytes
+ _objc_msgSend$string
+ _objc_msgSend$stringByReplacingOccurrencesOfString:withString:
- __OBJC_$_INSTANCE_METHODS_NSData(HealthRecordServices)
- ___49-[HKClinicalAccountStore supportsClinicalSharing]_block_invoke.229
- ___49-[HKClinicalAccountStore supportsClinicalSharing]_block_invoke.229.cold.1
- ___52-[HKClinicalDocumentStore _establishProxyConnection]_block_invoke.222
- ___52-[HKClinicalDocumentStore _establishProxyConnection]_block_invoke.222.cold.1
- ___54-[HKClinicalSharingSyncObserver resumeWithCompletion:]_block_invoke.230
- ___54-[HKClinicalSharingSyncObserver resumeWithCompletion:]_block_invoke.230.cold.1
- ___54-[HKClinicalSharingSyncObserver resumeWithCompletion:]_block_invoke.232
- ___54-[HKClinicalSharingSyncObserver resumeWithCompletion:]_block_invoke_2.236
- ___54-[HKClinicalSharingSyncObserver resumeWithCompletion:]_block_invoke_2.236.cold.1
- ___67-[HKClinicalAccountStore hasAnyHealthRecordsAccountWithCompletion:]_block_invoke.225
- ___67-[HKClinicalAccountStore hasAnyHealthRecordsAccountWithCompletion:]_block_invoke.225.cold.1
- ___71-[HKClinicalAccountStore shouldShowHealthRecordsSectionWithCompletion:]_block_invoke.228
- ___71-[HKClinicalAccountStore shouldShowHealthRecordsSectionWithCompletion:]_block_invoke.228.cold.1
- ___77-[HKClinicalAccountStore hasGatewayBackedHealthRecordsAccountWithCompletion:]_block_invoke.226
- ___77-[HKClinicalAccountStore hasGatewayBackedHealthRecordsAccountWithCompletion:]_block_invoke.226.cold.1
- ___block_literal_global.220
- ___block_literal_global.223
- ___block_literal_global.226
- ___block_literal_global.229
- ___block_literal_global.235
- ___block_literal_global.236
- ___block_literal_global.238
CStrings:
+ "+"
+ "-"
+ "@\"NSURLComponents\""
+ "HKBase64URLEncoding"
+ "HKOAuth2LoginSession"
+ "HKOAuth2LoginSession.generatePKCEVerifierWithAlgorithm failed, will fall back to NSUUID. Error: %d"
+ "PKCE algorithm %lu not implemented"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSURL\",R,C,N,V_loginURL"
+ "T@\"NSURLComponents\",R,C,N,V_callbackURLComponents"
+ "_"
+ "_callbackURLComponents"
+ "_loginURL"
+ "base64EncodedStringWithOptions:"
+ "callbackURLComponents"
+ "callbackURLString"
+ "componentsWithString:"
+ "dataWithLength:"
+ "generatePKCEChallengeFromVerifier:algorithm:error:"
+ "generatePKCEVerifierWithAlgorithm:"
+ "hk_SHA256"
+ "hk_base64URLEncodedString"
+ "initWithState:loginURL:callbackURLComponents:requestedScope:pkceVerifier:"
+ "loginURL"
+ "mutableBytes"
+ "new"
+ "string"
+ "stringByReplacingOccurrencesOfString:withString:"
+ "v32@0:8@\"NSString\"16@?<v@?@\"HKOAuth2LoginSession\"@\"NSError\">24"
+ "v32@0:8@\"NSUUID\"16@?<v@?@\"HKOAuth2LoginSession\"@\"NSError\">24"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSURL\"@\"NSUUID\"@\"NSError\">24"
- "v32@0:8@\"NSUUID\"16@?<v@?@\"NSURL\"@\"NSUUID\"@\"NSError\">24"

```
