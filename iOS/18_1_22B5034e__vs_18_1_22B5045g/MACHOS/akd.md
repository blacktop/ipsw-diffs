## akd

> `/System/Library/PrivateFrameworks/AuthKit.framework/akd`

```diff

-491.1.0.0.0
-  __TEXT.__text: 0x17f710
-  __TEXT.__auth_stubs: 0x1cf0
-  __TEXT.__objc_stubs: 0x17080
-  __TEXT.__objc_methlist: 0x88cc
+493.100.2.0.0
+  __TEXT.__text: 0x17dad0
+  __TEXT.__auth_stubs: 0x1d00
+  __TEXT.__objc_stubs: 0x17060
+  __TEXT.__objc_methlist: 0x88f4
   __TEXT.__const: 0x2ce0
-  __TEXT.__cstring: 0xab53
-  __TEXT.__objc_classname: 0x181d
-  __TEXT.__objc_methname: 0x20744
-  __TEXT.__objc_methtype: 0x5882
+  __TEXT.__cstring: 0xab73
+  __TEXT.__objc_classname: 0x1817
+  __TEXT.__objc_methname: 0x207f8
+  __TEXT.__objc_methtype: 0x5873
   __TEXT.__gcc_except_tab: 0x2270
-  __TEXT.__oslogstring: 0x1f1e8
+  __TEXT.__oslogstring: 0x1f0d8
   __TEXT.__dlopen_cstrs: 0x5a
   __TEXT.__swift5_typeref: 0x1580
   __TEXT.__swift5_fieldmd: 0xb6c

   __TEXT.__swift5_proto: 0x118
   __TEXT.__swift5_types: 0xec
   __TEXT.__swift5_protos: 0x34
-  __TEXT.__unwind_info: 0x5530
-  __TEXT.__eh_frame: 0x76f0
-  __DATA_CONST.__auth_got: 0xe88
+  __TEXT.__unwind_info: 0x4ef0
+  __TEXT.__eh_frame: 0x6df0
+  __DATA_CONST.__auth_got: 0xe90
   __DATA_CONST.__got: 0x15b0
-  __DATA_CONST.__auth_ptr: 0x4e8
-  __DATA_CONST.__const: 0xbb58
+  __DATA_CONST.__auth_ptr: 0x510
+  __DATA_CONST.__const: 0xbbd8
   __DATA_CONST.__cfstring: 0x6ae0
   __DATA_CONST.__objc_classlist: 0x6d0
   __DATA_CONST.__objc_catlist: 0x38

   __DATA_CONST.__objc_arrayobj: 0x48
   __DATA_CONST.__linkguard: 0x3e
   __DATA_CONST.__objc_dictobj: 0x118
-  __DATA.__objc_const: 0x24b70
-  __DATA.__objc_selrefs: 0x6ca8
-  __DATA.__objc_ivar: 0x9a8
+  __DATA.__objc_const: 0x24b90
+  __DATA.__objc_selrefs: 0x6cb0
+  __DATA.__objc_ivar: 0x9ac
   __DATA.__objc_data: 0x5330
   __DATA.__data: 0x3c28
   __DATA.__bss: 0x2170

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 6653
-  Symbols:   1298
-  CStrings:  9232
+  Functions: 6613
+  Symbols:   1299
+  CStrings:  9233
 
Symbols:
+ _AKURLBagKeyStoreModernRecovery
+ _$s10Foundation3URLV19_bridgeToObjectiveCSo5NSURLCyF
- _AKAuthenticationTelemetryDeviceSessionID
CStrings:
+ "setRequestBodyType:"
+ "_requestingControllerWithServerResponse:"
+ "Updating auth results for context: %!@(MISSING)"
+ "setShouldSendIdentityToken:"
+ "_requestURLOverride"
+ "T@\"NSURL\",R,C,N,V_requestURLOverride"
+ "requestURLOverride"
+ "_requestBodyType"
+ "requestURLWithCompletion:"
+ "AuthKit account exists and is consented to telemetry collection, deviceSessionID: %!@(MISSING)"
+ "T@\"NSString\",C,N,V_urlBagKey"
+ "setUrlBagKey:"
+ "initWithContext:url:"
+ "allowAuthenticationBeforeFirstUnlock"
+ "v24@?0@\"NSURLRequest\"8@\"NSError\"16"
+ "_updateHeadersWithProxiedDeviceAnisetteData:clientProvidedData:completion:"
+ "Device Session ID: AuthKit account exists and is consented to telemetry collection, updating context... %!@(MISSING)"
+ "v24@0:8@?<v@?@\"NSURLRequest\"@\"NSError\">16"
+ "appendRequestUrl:queryParameterNamed:value:"
+ "Unable to get proxied Anisette data for %!@(MISSING)! Error: %!@(MISSING)"
+ "Failed to append %!@(MISSING):%!@(MISSING) to %!@(MISSING)"
+ "AuthKit account exists and is consented to telemetry collection, but is missing a deviceSessionID, creating a new one... %!@(MISSING)"
+ "_shouldSendIdentityToken"
+ "AKPrivateEmailRequestProvider"
+ "buildRequestWithCompletion:"
+ "initWithUrlBagKey:"
+ "TQ,N,V_requestBodyType"
+ "TB,N,V_shouldSendIdentityToken"
+ "Attempting to build request without a URL (urlBagKey: %!@(MISSING)), bad things to come..."
+ "shouldSendIdentityToken"
- "AKPersistRecoveryKeyRequestProvider"
- "@\"NSURLRequest\"24@0:8^@16"
- "isEasyDependentSignInEnabled"
- "setRequestURL:"
- "_recoveryKeyContext"
- "Attempting to build request without a URL, bad things to come..."
- "osAttestationURL"
- "recoveryKeyContext"
- "AuthKit account exists and is consented to telemetry collection, but is missing a deviceSessionID!"
- "storeModernRecoveryURL"
- "setRecoveryKeyContext:"
- "appendRequestUrlQueryParameterNamed:value:"
- "buildRequest:"
- "@\"AKPersistRecoveryKeyContext\""
- "initWithRecoveryKeyContext:authContext:"
- "circleURL"
- "Got a bad private-email fetch URL from the bag: %!@(MISSING)"
- "fetchFollowUps"
- "Storing the context device session ID for the account %!@(MISSING)"
- "_setRequestURL"
- "Device session ID mismatch detected, account and context differ, fatal data quality error"
- "telemetryDeviceSessionID does not exist for account or user has not opted-in, creating a new telemetryDeviceSessionID: %!@(MISSING)"
- "T@\"NSString\",R,C,N,V_urlBagKey"
- "T@\"AKPersistRecoveryKeyContext\",C,N,V_recoveryKeyContext"
- "Device should be unlocked after boot to continue provisioning."
- "Unable to fetch private email. The URL is missing from the URL bag"
- "AuthKit account exists and is consented to telemetry collection, populating deviceSessionID: %!@(MISSING)"
- "T@\"NSURL\",C,N,V_requestURL"
- "Device session ID was not detected on context, fatal data quality error"

```
