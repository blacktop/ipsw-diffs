## HelpKit

> `/System/Library/PrivateFrameworks/HelpKit.framework/HelpKit`

```diff

-192.0.0.0.0
-  __TEXT.__text: 0x28a90
-  __TEXT.__auth_stubs: 0x6f0
-  __TEXT.__objc_methlist: 0x342c
-  __TEXT.__const: 0xe8
-  __TEXT.__gcc_except_tab: 0xc70
-  __TEXT.__cstring: 0x18ce
+195.0.0.0.0
+  __TEXT.__text: 0x27b0c
+  __TEXT.__auth_stubs: 0x6b0
+  __TEXT.__objc_methlist: 0x33fc
+  __TEXT.__const: 0xe0
+  __TEXT.__gcc_except_tab: 0xc04
+  __TEXT.__cstring: 0x1847
   __TEXT.__oslogstring: 0x329
-  __TEXT.__dlopen_cstrs: 0x10e
   __TEXT.__ustring: 0x82
-  __TEXT.__unwind_info: 0xa60
-  __TEXT.__objc_classname: 0x5cb
-  __TEXT.__objc_methname: 0x97c1
-  __TEXT.__objc_methtype: 0x1d4d
-  __TEXT.__objc_stubs: 0x73e0
+  __TEXT.__unwind_info: 0xa18
+  __TEXT.__objc_classname: 0x5b1
+  __TEXT.__objc_methname: 0x9715
+  __TEXT.__objc_methtype: 0x1d37
+  __TEXT.__objc_stubs: 0x72c0
   __DATA_CONST.__got: 0x498
-  __DATA_CONST.__const: 0xea0
+  __DATA_CONST.__const: 0xe28
   __DATA_CONST.__objc_classlist: 0x130
-  __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2558
+  __DATA_CONST.__objc_selrefs: 0x2528
   __DATA_CONST.__objc_superrefs: 0xf0
   __DATA_CONST.__objc_arraydata: 0x88
-  __AUTH_CONST.__auth_got: 0x388
+  __AUTH_CONST.__auth_got: 0x368
   __AUTH_CONST.__const: 0x320
-  __AUTH_CONST.__cfstring: 0x2b60
-  __AUTH_CONST.__objc_const: 0x5080
+  __AUTH_CONST.__cfstring: 0x2ba0
+  __AUTH_CONST.__objc_const: 0x4f90
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH.__objc_data: 0xb90
-  __DATA.__objc_ivar: 0x410
+  __DATA.__objc_ivar: 0x40c
   __DATA.__data: 0x858
-  __DATA.__bss: 0x1b0
+  __DATA.__bss: 0x170
   __DATA_DIRTY.__objc_data: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: FEAD7E32-DD0A-3147-9766-42B7FFDB4021
-  Functions: 1101
-  Symbols:   4269
-  CStrings:  2693
+  UUID: 244E3509-6EC7-3A27-B1A8-F40C770C4CC3
+  Functions: 1083
+  Symbols:   4195
+  CStrings:  2677
 
Symbols:
+ +[HLPCommonDefines HLPBundle]
+ +[HLPCommonDefines removeHLPBundle]
+ +[HLPLoadInfo infoWithTopicItem:accessType:searchTerms:anchor:]
+ -[HLPHelpItem decodedNameString]
+ -[HLPHelpSearchIndexController hpd_compressedDataUsingAlgorithm:data:]
+ -[HLPHelpSearchIndexController hpd_dataUsingCompressionAlgorithm:operation:data:]
+ -[HLPHelpSearchIndexController hpd_decompressedDataUsingAlgorithm:data:]
+ -[HLPHelpTopicViewController loadHelpTopicItem:accessType:searchTerms:anchor:]
+ -[HLPHelpViewController accessType]
+ -[HLPHelpViewController closeBarButtonSystemItem]
+ -[HLPHelpViewController setAccessType:]
+ GCC_except_table53
+ GCC_except_table55
+ GCC_except_table68
+ _HLPAnalyticsViewSourceTypeDESiri
+ _HLPAnalyticsViewSourceTypeLearnMore
+ _OBJC_IVAR_$_HLPHelpViewController._accessType
+ __UISolariumEnabled
+ ___98-[HLPURLSessionManager newURLSessionItemWithRequest:identifier:networkDelegate:completionHandler:]_block_invoke.22
+ _objc_msgSend$closeBarButtonSystemItem
+ _objc_msgSend$decodedNameString
+ _objc_msgSend$hpd_dataUsingCompressionAlgorithm:operation:data:
+ _objc_msgSend$hpd_decompressedDataUsingAlgorithm:data:
+ _objc_msgSend$infoWithTopicItem:accessType:searchTerms:anchor:
+ _objc_msgSend$loadHelpTopicItem:accessType:searchTerms:anchor:
- +[HLPLoadInfo infoWithTopicItem:accesstype:searchTerms:anchor:]
- +[NSBundle(HLPAdditions) HLPBundle]
- +[NSBundle(HLPAdditions) removeHLPBundle]
- -[HLPHelpTopicViewController loadHelpTopicItem:searchTerms:anchor:]
- -[HLPURLSessionACAuthHandler setSsoAuthenticator:]
- -[HLPURLSessionACAuthHandler ssoAuthenticator]
- -[HLPURLSessionManager setUrlRedirector:]
- -[HLPURLSessionManager urlRedirector]
- -[NSData(HPDAdditions) hpd_compressedDataUsingAlgorithm:]
- -[NSData(HPDAdditions) hpd_dataUsingCompressionAlgorithm:operation:]
- -[NSData(HPDAdditions) hpd_decompressedDataUsingAlgorithm:]
- -[NSString(HLPAdditions) htmlDecodedString]
- GCC_except_table52
- GCC_except_table54
- GCC_except_table67
- _OBJC_IVAR_$_HLPURLSessionACAuthHandler._ssoAuthenticator
- _OBJC_IVAR_$_HLPURLSessionManager._urlRedirector
- _PingPongClientLibrary
- _PingPongClientLibraryCore
- _PingPongClientLibraryCore.frameworkLibrary
- __OBJC_$_CATEGORY_CLASS_METHODS_NSBundle_$_HLPAdditions
- __OBJC_$_CATEGORY_INSTANCE_METHODS_NSData_$_HPDAdditions
- __OBJC_$_CATEGORY_INSTANCE_METHODS_NSString_$_HLPAdditions
- __OBJC_$_CATEGORY_NSBundle_$_HLPAdditions
- __OBJC_$_CATEGORY_NSData_$_HPDAdditions
- __OBJC_$_CATEGORY_NSString_$_HLPAdditions
- ___57-[HLPURLSessionACAuthHandler authenticateWithCompletion:]_block_invoke
- ___57-[HLPURLSessionACAuthHandler authenticateWithCompletion:]_block_invoke_2
- ___57-[HLPURLSessionACAuthHandler authenticateWithCompletion:]_block_invoke_2.cold.1
- ___57-[HLPURLSessionACAuthHandler authenticateWithCompletion:]_block_invoke_2.cold.2
- ___98-[HLPURLSessionManager newURLSessionItemWithRequest:identifier:networkDelegate:completionHandler:]_block_invoke.24
- ___PingPongClientLibraryCore_block_invoke
- ___block_descriptor_40_e8_32r_e5_v8?0lr32l8
- ___block_descriptor_48_e8_32s40bs_e34_v24?0"NSDictionary"8"NSError"16ls32l8s40l8
- ___block_literal_global.3
- ___getPPCExtensibleSSOAuthenticatorClass_block_invoke
- ___getPPCExtensibleSSOAuthenticatorClass_block_invoke.cold.1
- ___getPPCRedirectClass_block_invoke
- ___getPPCRedirectClass_block_invoke.cold.1
- ___getkExtensibleSSOTokenKeySymbolLoc_block_invoke
- ___getkExtensibleSSOUsernameKeySymbolLoc_block_invoke
- __sl_dlopen
- _abort_report_np
- _audit_stringPingPongClient
- _dlerror
- _dlsym
- _getPPCExtensibleSSOAuthenticatorClass.softClass
- _getPPCRedirectClass.softClass
- _getkExtensibleSSOTokenKeySymbolLoc.ptr
- _getkExtensibleSSOUsernameKeySymbolLoc.ptr
- _objc_getClass
- _objc_msgSend$customHeaderFields
- _objc_msgSend$hostMappings
- _objc_msgSend$hpd_dataUsingCompressionAlgorithm:operation:
- _objc_msgSend$hpd_decompressedDataUsingAlgorithm:
- _objc_msgSend$htmlDecodedString
- _objc_msgSend$infoWithTopicItem:accesstype:searchTerms:anchor:
- _objc_msgSend$loadHelpTopicItem:searchTerms:anchor:
- _objc_msgSend$mappedURL:
- _objc_msgSend$setEnvIdentifier:
- _objc_msgSend$setInteractivity:
- _objc_msgSend$setSsoAuthenticator:
- _objc_msgSend$setUrlRedirector:
- _objc_msgSend$ssoAuthenticator
- _objc_msgSend$syncQueue
- _objc_msgSend$urlRedirector
CStrings:
+ "@28@0:8i16@20"
+ "@32@0:8i16i20@24"
+ "Tq,N,V_accessType"
+ "closeBarButtonSystemItem"
+ "de_siri"
+ "decodedNameString"
+ "hpd_compressedDataUsingAlgorithm:data:"
+ "hpd_dataUsingCompressionAlgorithm:operation:data:"
+ "hpd_decompressedDataUsingAlgorithm:data:"
+ "infoWithTopicItem:accessType:searchTerms:anchor:"
+ "learnmore"
+ "loadHelpTopicItem:accessType:searchTerms:anchor:"
+ "setAccessType:"
+ "v48@0:8@16q24@32@40"
- "%s"
- "@\"PPCExtensibleSSOAuthenticator\""
- "@\"PPCRedirect\""
- "@20@0:8i16"
- "@24@0:8i16i20"
- "HLPAdditions"
- "HPDAdditions"
- "PPCExtensibleSSOAuthenticator"
- "PPCRedirect"
- "T@\"PPCExtensibleSSOAuthenticator\",&,N,V_ssoAuthenticator"
- "T@\"PPCRedirect\",&,N,V_urlRedirector"
- "Unable to find class %s"
- "_ssoAuthenticator"
- "_urlRedirector"
- "hostMappings"
- "hpd_compressedDataUsingAlgorithm:"
- "hpd_dataUsingCompressionAlgorithm:operation:"
- "hpd_decompressedDataUsingAlgorithm:"
- "htmlDecodedString"
- "infoWithTopicItem:accesstype:searchTerms:anchor:"
- "kExtensibleSSOTokenKey"
- "kExtensibleSSOUsernameKey"
- "loadHelpTopicItem:searchTerms:anchor:"
- "mappedURL:"
- "setEnvIdentifier:"
- "setInteractivity:"
- "setSsoAuthenticator:"
- "setUrlRedirector:"
- "softlink:o:path:/System/Library/PrivateFrameworks/PingPongClient.framework/PingPongClient"
- "ssoAuthenticator"
- "urlRedirector"
- "v24@?0@\"NSDictionary\"8@\"NSError\"16"

```
