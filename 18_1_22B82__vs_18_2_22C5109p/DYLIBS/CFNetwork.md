## CFNetwork

> `/System/Library/Frameworks/CFNetwork.framework/CFNetwork`

```diff

-1568.200.51.0.0
-  __TEXT.__text: 0x26e808
-  __TEXT.__auth_stubs: 0x5550
+1568.300.61.0.0
+  __TEXT.__text: 0x26f6bc
+  __TEXT.__auth_stubs: 0x5560
   __TEXT.__delay_stubs: 0x7e8
   __TEXT.__delay_helper: 0x1728
-  __TEXT.__objc_methlist: 0x8df8
-  __TEXT.__const: 0xc9b8c
-  __TEXT.__gcc_except_tab: 0x14ec4
-  __TEXT.__cstring: 0x18d45
-  __TEXT.__oslogstring: 0xf7ab
+  __TEXT.__objc_methlist: 0x8e30
+  __TEXT.__const: 0xc9bcc
+  __TEXT.__gcc_except_tab: 0x14ffc
+  __TEXT.__cstring: 0x18d35
+  __TEXT.__oslogstring: 0xf7f4
   __TEXT.__dof_CFNetwork: 0xf3b
-  __TEXT.__unwind_info: 0xbfa0
+  __TEXT.__unwind_info: 0xbfb8
   __TEXT.__objc_classname: 0x1514
-  __TEXT.__objc_methname: 0x17917
-  __TEXT.__objc_methtype: 0x6c8c
-  __TEXT.__objc_stubs: 0xe620
-  __DATA_CONST.__got: 0xc28
-  __DATA_CONST.__const: 0x9380
+  __TEXT.__objc_methname: 0x179bd
+  __TEXT.__objc_methtype: 0x6cc6
+  __TEXT.__objc_stubs: 0xe640
+  __DATA_CONST.__got: 0xc30
+  __DATA_CONST.__const: 0x9390
   __DATA_CONST.__objc_classlist: 0x4d8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x128
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4b30
+  __DATA_CONST.__objc_selrefs: 0x4b48
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x3e0
   __DATA_CONST.__objc_arraydata: 0x68
-  __AUTH_CONST.__auth_got: 0x2c30
+  __AUTH_CONST.__auth_got: 0x2c38
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__const: 0x13750
+  __AUTH_CONST.__const: 0x13758
   __AUTH_CONST.__cfstring: 0xf2a0
-  __AUTH_CONST.__objc_const: 0x155c0
+  __AUTH_CONST.__objc_const: 0x15600
   __AUTH_CONST.__objc_intobj: 0x180
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH.__objc_data: 0x1630
   __AUTH.__data: 0x2f8
-  __AUTH.__cfstring_CFN: 0x7c40
-  __DATA.__objc_ivar: 0x1390
+  __AUTH.__cfstring_CFN: 0x7cb0
+  __DATA.__objc_ivar: 0x1394
   __DATA.__data: 0x11b0
   __DATA.__crash_info: 0x40
   __DATA.__bss: 0xd50

   - /usr/lib/libsp.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 12842
-  Symbols:   14995
-  CStrings:  9374
+  Functions: 12856
+  Symbols:   15012
+  CStrings:  9381
 
Symbols:
+ _NSHTTPCookieSetByJavaScript
+ _NSURLVolumeIsLocalKey
+ __ZNSt3__16__sortIRNS_6__lessIjjEEPjEEvT0_S5_T_
CStrings:
+ "<CompactCookieHeader@%!p(MISSING)> { domain: %!s(MISSING), partition: %!s(MISSING), name: %!s(MISSING), path: %!s(MISSING), value: %!s(MISSING), session: %!c(MISSING), secure: %!c(MISSING), httponly? %!c(MISSING), expires: %!@(MISSING), created: %!@(MISSING), accessed: %!@(MISSING) }"
+ "@40@0:8@16@24d32"
+ "SetInJavaScript"
+ "T@\"NSString\",R,C,V_cookiePartitionIdentifier"
+ "Volume of %!@(MISSING) is not local, falling back to in memory alt-svc storage: %!@(MISSING)"
+ "_cookiePartitionIdentifier"
+ "_initWithCookie:partition:accessTime:"
+ "cookiePartitionIdentifier"
+ "setCookiePartitionIdentifier:"
+ "{URLRequest=\"_vptr$CoreLoggable\"^^?\"fURL\"^{__CFURL}\"fCachePolicy\"Q\"fTimeout\"d\"fMainDocumentURL\"^{__CFURL}\"fProtocolProperties\"^{__CFDictionary}\"fProxyDict\"^{__CFDictionary}\"fHTTPRequest\"^{HTTPRequest}\"fFlags\"{Flags=\"_flag_SHOULD_HANDLE_HTTP_COOKIES\"b1\"_flag_IS_MUTABLE\"b1\"_flag_SHOULD_START_SYNCHRONOUSLY\"b1\"_flag_ALLOW_CELLULAR\"b1\"_flag_PREVENTSIDLESYSTEMSLEEP\"b1\"_flag_SET_EXPLICIT_SHOULD_HANDLE_COOKIES\"b1\"_flag_SET_EXPLICIT_NETWORK_SERVICE_TYPE\"b1\"_flag_SET_EXPLICIT_ALLOWS_CELLULAR\"b1\"_flag_SET_EXPLICIT_PREVENTS_IDLE_SYSTEM_SLEEP\"b1\"_flag_SET_EXPLICIT_SHOULD_PIPELINE\"b1\"_flag_SET_EXPLICIT_CACHE_POLICY\"b1\"_flag_SET_EXPLICIT_TIMEOUT\"b1\"_flag_SET_EXPLICIT_PROXY_DICT\"b1\"_flag_SET_EXPLICIT_SSL_PROPERTIES\"b1\"_flag_SET_EXPLICIT_SHOULD_START_SYNCHRONOUSLY\"b1}\"fSSLProps\"^{__CFDictionary}\"fContentDispositionHeaderEncodingFallbackArray\"^{__CFArray}\"fRequestPriority\"q\"fAllowedProtocolTypes\"Q\"fNetworkServiceType\"i\"fBoundInterfaceIdentifier\"^{__CFString}\"fTrackerContext\"^{__CFString}\"fCookiePartitionIdentifier\"^{__CFString}\"fTimeWindowDelay\"d\"fTimeWindowDuration\"d\"fStartTimeoutTime\"d\"fRequiresShortConnectionTimeout\"C\"fPreventHSTSStorage\"C\"fIgnoreHSTS\"C\"fSchemeWasUpgradedDueToDynamicHSTS\"C\"fAssumesHTTP3Capable\"C\"fKnownTracker\"C\"fPrivacyProxyFailClosed\"C\"fPrivacyProxyFailClosedForUnreachableNonMainHosts\"C\"fPrivacyProxyFailClosedForUnreachableHosts\"C\"fProhibitPrivacyProxy\"C\"fAllowPrivateAccessTokensForThirdParty\"C\"fUseEnhancedPrivacyMode\"C\"fBlockTrackers\"C\"fFailInsecureLoadWithHTTPSDNSRecord\"C\"fIsWebSearchContent\"C\"fRequiresDNSSECValidation\"i\"fAllowsPersistentDNS\"C\"fAttribution\"Q\"fPayloadTransmissionTimeout\"d\"fATSOverrides\"^{__CFDictionary}\"fHSTSPolicy\"{unique_ptr<_CFHSTSPolicy, Deleter_CFRelease>=\"__ptr_\"{__compressed_pair<_CFHSTSPolicy *, Deleter_CFRelease>=\"__value_\"^{_CFHSTSPolicy}}}\"fAllowsExpensiveNetworkAccess\"i\"fAllowsConstrainedNetworkAccess\"i\"fAllowsUCA\"i\"_explicitStorageSession\"^{__CFURLStorageSession}}"
- "<CompactCookieHeader@%!p(MISSING)> { domain: %!s(MISSING), partition: %!s(MISSING), name: %!s(MISSING), path: %!s(MISSING), value: %!s(MISSING), session: %!c(MISSING), secure: %!c(MISSING), httponly? %!c(MISSING), expires: %!@(MISSING), created: %!@(MISSING) }"
- "NOTE: we're creating a COOKIE clone for %!@(MISSING)"
- "NSCFPrivateCookieStorage<%!p(MISSING)>"
- "{URLRequest=\"_vptr$CoreLoggable\"^^?\"fURL\"^{__CFURL}\"fCachePolicy\"Q\"fTimeout\"d\"fMainDocumentURL\"^{__CFURL}\"fProtocolProperties\"^{__CFDictionary}\"fProxyDict\"^{__CFDictionary}\"fHTTPRequest\"^{HTTPRequest}\"fFlags\"{Flags=\"_flag_SHOULD_HANDLE_HTTP_COOKIES\"b1\"_flag_IS_MUTABLE\"b1\"_flag_SHOULD_START_SYNCHRONOUSLY\"b1\"_flag_ALLOW_CELLULAR\"b1\"_flag_PREVENTSIDLESYSTEMSLEEP\"b1\"_flag_SET_EXPLICIT_SHOULD_HANDLE_COOKIES\"b1\"_flag_SET_EXPLICIT_NETWORK_SERVICE_TYPE\"b1\"_flag_SET_EXPLICIT_ALLOWS_CELLULAR\"b1\"_flag_SET_EXPLICIT_PREVENTS_IDLE_SYSTEM_SLEEP\"b1\"_flag_SET_EXPLICIT_SHOULD_PIPELINE\"b1\"_flag_SET_EXPLICIT_CACHE_POLICY\"b1\"_flag_SET_EXPLICIT_TIMEOUT\"b1\"_flag_SET_EXPLICIT_PROXY_DICT\"b1\"_flag_SET_EXPLICIT_SSL_PROPERTIES\"b1\"_flag_SET_EXPLICIT_SHOULD_START_SYNCHRONOUSLY\"b1}\"fSSLProps\"^{__CFDictionary}\"fContentDispositionHeaderEncodingFallbackArray\"^{__CFArray}\"fRequestPriority\"q\"fAllowedProtocolTypes\"Q\"fNetworkServiceType\"i\"fBoundInterfaceIdentifier\"^{__CFString}\"fTrackerContext\"^{__CFString}\"fTimeWindowDelay\"d\"fTimeWindowDuration\"d\"fStartTimeoutTime\"d\"fRequiresShortConnectionTimeout\"C\"fPreventHSTSStorage\"C\"fIgnoreHSTS\"C\"fSchemeWasUpgradedDueToDynamicHSTS\"C\"fAssumesHTTP3Capable\"C\"fKnownTracker\"C\"fPrivacyProxyFailClosed\"C\"fPrivacyProxyFailClosedForUnreachableNonMainHosts\"C\"fPrivacyProxyFailClosedForUnreachableHosts\"C\"fProhibitPrivacyProxy\"C\"fAllowPrivateAccessTokensForThirdParty\"C\"fUseEnhancedPrivacyMode\"C\"fBlockTrackers\"C\"fFailInsecureLoadWithHTTPSDNSRecord\"C\"fIsWebSearchContent\"C\"fRequiresDNSSECValidation\"i\"fAllowsPersistentDNS\"C\"fAttribution\"Q\"fPayloadTransmissionTimeout\"d\"fATSOverrides\"^{__CFDictionary}\"fHSTSPolicy\"{unique_ptr<_CFHSTSPolicy, Deleter_CFRelease>=\"__ptr_\"{__compressed_pair<_CFHSTSPolicy *, Deleter_CFRelease>=\"__value_\"^{_CFHSTSPolicy}}}\"fAllowsExpensiveNetworkAccess\"i\"fAllowsConstrainedNetworkAccess\"i\"fAllowsUCA\"i\"_explicitStorageSession\"^{__CFURLStorageSession}}"

```
