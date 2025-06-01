## PlatformSSO

> `/System/Library/PrivateFrameworks/PlatformSSO.framework/PlatformSSO`

```diff

-384.120.7.0.0
-  __TEXT.__text: 0xb02c0
+384.140.6.0.0
+  __TEXT.__text: 0xb0c18
   __TEXT.__auth_stubs: 0x1540
-  __TEXT.__objc_methlist: 0x6604
+  __TEXT.__objc_methlist: 0x6614
   __TEXT.__const: 0xfc4
-  __TEXT.__cstring: 0xda26
-  __TEXT.__oslogstring: 0x2a8c
+  __TEXT.__cstring: 0xda87
+  __TEXT.__oslogstring: 0x2af4
   __TEXT.__gcc_except_tab: 0xecc
   __TEXT.__dlopen_cstrs: 0x162
-  __TEXT.__unwind_info: 0x2514
+  __TEXT.__unwind_info: 0x251c
   __TEXT.__objc_classname: 0xdfc
-  __TEXT.__objc_methname: 0xe868
-  __TEXT.__objc_methtype: 0x294b
-  __TEXT.__objc_stubs: 0x9c60
+  __TEXT.__objc_methname: 0xe864
+  __TEXT.__objc_methtype: 0x295c
+  __TEXT.__objc_stubs: 0x9c40
   __DATA_CONST.__got: 0x2d0
   __DATA_CONST.__const: 0x2a48
   __DATA_CONST.__objc_classlist: 0x4a0

   __DATA_CONST.__objc_superrefs: 0x218
   __DATA_CONST.__objc_arraydata: 0x88
   __AUTH_CONST.__objc_const: 0x37e8
-  __AUTH_CONST.__cfstring: 0x9040
+  __AUTH_CONST.__cfstring: 0x9080
   __AUTH_CONST.__const: 0xb60
-  __AUTH_CONST.__objc_intobj: 0x168
+  __AUTH_CONST.__objc_intobj: 0x138
   __AUTH_CONST.__objc_doubleobj: 0x30
   __AUTH_CONST.__objc_arrayobj: 0xf0
   __AUTH_CONST.__objc_dictobj: 0x50

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxml2.2.dylib
-  UUID: 132C947E-00E2-3A01-ACF0-DAACB27F8EE0
-  Functions: 4716
-  Symbols:   14058
-  CStrings:  5983
+  UUID: 180A8E88-E431-3EF9-B2A2-E89A1439A185
+  Functions: 4723
+  Symbols:   14071
+  CStrings:  5991
 
Symbols:
+ +[POSecKeyHelper verifyKey:]
+ -[POAgentAuthenticationProcess _doLoginWithPasswordContext:tokenId:].cold.8
+ -[POAgentProcess screenDidUnlockWithCredentialContext:smartCardContext:biometricContext:tokenId:atLogin:tokenUnlock:completion:]
+ -[POAgentProcess screenDidUnlockWithCredentialContext:smartCardContext:biometricContext:tokenId:atLogin:tokenUnlock:completion:].cold.1
+ -[POAgentProcess screenDidUnlockWithCredentialContext:smartCardContext:biometricContext:tokenId:atLogin:tokenUnlock:completion:].cold.2
+ -[POAuthPluginProcess screenDidUnlockWithCredentialContext:smartCardContext:biometricContext:tokenId:atLogin:tokenUnlock:]
+ -[POServiceConnection screenDidUnlockWithCredentialContext:smartCardContext:biometricContext:tokenId:atLogin:tokenUnlock:completion:]
+ GCC_except_table15
+ GCC_except_table156
+ GCC_except_table160
+ GCC_except_table204
+ GCC_except_table27
+ GCC_except_table36
+ GCC_except_table38
+ GCC_except_table81
+ ___100-[POAgentAuthenticationProcess handleScreenUnlockWithCredentialContext:tokenId:atLogin:tokenUnlock:]_block_invoke.66
+ ___100-[POAgentAuthenticationProcess handleScreenUnlockWithCredentialContext:tokenId:atLogin:tokenUnlock:]_block_invoke.cold.1
+ ___122-[POAuthPluginProcess screenDidUnlockWithCredentialContext:smartCardContext:biometricContext:tokenId:atLogin:tokenUnlock:]_block_invoke
+ ___122-[POAuthPluginProcess screenDidUnlockWithCredentialContext:smartCardContext:biometricContext:tokenId:atLogin:tokenUnlock:]_block_invoke_2
+ ___128-[POAgentProcess screenDidUnlockWithCredentialContext:smartCardContext:biometricContext:tokenId:atLogin:tokenUnlock:completion:]_block_invoke
+ ___128-[POAgentProcess screenDidUnlockWithCredentialContext:smartCardContext:biometricContext:tokenId:atLogin:tokenUnlock:completion:]_block_invoke.cold.1
+ ___133-[POServiceConnection screenDidUnlockWithCredentialContext:smartCardContext:biometricContext:tokenId:atLogin:tokenUnlock:completion:]_block_invoke
+ ___133-[POServiceConnection screenDidUnlockWithCredentialContext:smartCardContext:biometricContext:tokenId:atLogin:tokenUnlock:completion:]_block_invoke.cold.1
+ ___28+[POSecKeyHelper verifyKey:]_block_invoke
+ ___28+[POSecKeyHelper verifyKey:]_block_invoke.cold.1
+ ___51-[POAgentAuthenticationProcess handleNetworkChange]_block_invoke.101
+ ___51-[POAgentAuthenticationProcess handleNetworkChange]_block_invoke.101.cold.1
+ ___51-[POAgentAuthenticationProcess handleNetworkChange]_block_invoke.101.cold.2
+ ___51-[POAgentAuthenticationProcess handleNetworkChange]_block_invoke.101.cold.3
+ ___64+[POSecKeyHelper evaluateTrustForCertificates:rootCertificates:]_block_invoke.62
+ ___64+[POSecKeyHelper evaluateTrustForCertificates:rootCertificates:]_block_invoke.62.cold.1
+ ___64+[POSecKeyHelper evaluateTrustForCertificates:rootCertificates:]_block_invoke.66
+ ___64+[POSecKeyHelper evaluateTrustForCertificates:rootCertificates:]_block_invoke.66.cold.1
+ ___64+[POSecKeyHelper evaluateTrustForCertificates:rootCertificates:]_block_invoke.70
+ ___64+[POSecKeyHelper evaluateTrustForCertificates:rootCertificates:]_block_invoke.70.cold.1
+ ___65+[POSecKeyHelper createSEPKeyForKeyType:userPresence:currentSet:]_block_invoke.27
+ ___65+[POSecKeyHelper createSEPKeyForKeyType:userPresence:currentSet:]_block_invoke.27.cold.1
+ ___65+[POSecKeyHelper createSEPKeyForKeyType:userPresence:currentSet:]_block_invoke.32
+ ___65+[POSecKeyHelper createSEPKeyForKeyType:userPresence:currentSet:]_block_invoke.32.cold.1
+ ___68-[POAgentAuthenticationProcess _doLoginWithPasswordContext:tokenId:]_block_invoke.149.cold.1
+ ___68-[POAgentAuthenticationProcess _doLoginWithPasswordContext:tokenId:]_block_invoke.153
+ ___70-[POAgentAuthenticationProcess _doRefreshWithPasswordContext:tokenId:]_block_invoke.122
+ ___70-[POAgentAuthenticationProcess _doRefreshWithPasswordContext:tokenId:]_block_invoke.122.cold.1
+ ___70-[POAgentAuthenticationProcess _doRefreshWithPasswordContext:tokenId:]_block_invoke.128
+ ___70-[POAgentAuthenticationProcess _doRefreshWithPasswordContext:tokenId:]_block_invoke.128.cold.1
+ ___70-[POAgentAuthenticationProcess _doRefreshWithPasswordContext:tokenId:]_block_invoke.136
+ ___70-[POAgentAuthenticationProcess doUnlockForTokenWithCredentialContext:]_block_invoke.85
+ ___70-[POAgentAuthenticationProcess doUnlockForTokenWithCredentialContext:]_block_invoke.85.cold.1
+ ___73-[POAgentAuthenticationProcess doUnlockForPasswordWithCredentialContext:]_block_invoke.73
+ ___73-[POAgentAuthenticationProcess doUnlockForPasswordWithCredentialContext:]_block_invoke.73.cold.1
+ ___86-[POAgentAuthenticationProcess performLoginForCurrentUserWithPasswordContext:tokenId:]_block_invoke.113
+ ___86-[POAgentAuthenticationProcess performLoginForCurrentUserWithPasswordContext:tokenId:]_block_invoke.113.cold.1
+ ___block_descriptor_74_e8_32s40s48s56s64s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
+ ___block_literal_global.134
+ _aks_get_seconds_since_passcode_change
+ _objc_msgSend$screenDidUnlockWithCredentialContext:smartCardContext:biometricContext:tokenId:atLogin:tokenUnlock:completion:
+ _objc_msgSend$verifyKey:
- -[POAgentProcess screenDidUnlockWithCredentialContext:smartCardContext:tokenId:atLogin:tokenUnlock:completion:]
- -[POAgentProcess screenDidUnlockWithCredentialContext:smartCardContext:tokenId:atLogin:tokenUnlock:completion:].cold.1
- -[POAgentProcess screenDidUnlockWithCredentialContext:smartCardContext:tokenId:atLogin:tokenUnlock:completion:].cold.2
- -[POAuthPluginProcess screenDidUnlockWithCredentialContext:smartCardContext:tokenId:atLogin:tokenUnlock:]
- -[POServiceConnection screenDidUnlockWithCredentialContext:smartCardContext:tokenId:atLogin:tokenUnlock:completion:]
- GCC_except_table155
- GCC_except_table159
- GCC_except_table203
- GCC_except_table33
- GCC_except_table64
- ___105-[POAuthPluginProcess screenDidUnlockWithCredentialContext:smartCardContext:tokenId:atLogin:tokenUnlock:]_block_invoke
- ___105-[POAuthPluginProcess screenDidUnlockWithCredentialContext:smartCardContext:tokenId:atLogin:tokenUnlock:]_block_invoke_2
- ___111-[POAgentProcess screenDidUnlockWithCredentialContext:smartCardContext:tokenId:atLogin:tokenUnlock:completion:]_block_invoke
- ___111-[POAgentProcess screenDidUnlockWithCredentialContext:smartCardContext:tokenId:atLogin:tokenUnlock:completion:]_block_invoke.cold.1
- ___116-[POServiceConnection screenDidUnlockWithCredentialContext:smartCardContext:tokenId:atLogin:tokenUnlock:completion:]_block_invoke
- ___116-[POServiceConnection screenDidUnlockWithCredentialContext:smartCardContext:tokenId:atLogin:tokenUnlock:completion:]_block_invoke.cold.1
- ___51-[POAgentAuthenticationProcess handleNetworkChange]_block_invoke.97
- ___51-[POAgentAuthenticationProcess handleNetworkChange]_block_invoke.97.cold.1
- ___51-[POAgentAuthenticationProcess handleNetworkChange]_block_invoke.97.cold.2
- ___51-[POAgentAuthenticationProcess handleNetworkChange]_block_invoke.97.cold.3
- ___64+[POSecKeyHelper evaluateTrustForCertificates:rootCertificates:]_block_invoke.63
- ___64+[POSecKeyHelper evaluateTrustForCertificates:rootCertificates:]_block_invoke.63.cold.1
- ___64+[POSecKeyHelper evaluateTrustForCertificates:rootCertificates:]_block_invoke.67
- ___64+[POSecKeyHelper evaluateTrustForCertificates:rootCertificates:]_block_invoke.67.cold.1
- ___64+[POSecKeyHelper evaluateTrustForCertificates:rootCertificates:]_block_invoke.71
- ___64+[POSecKeyHelper evaluateTrustForCertificates:rootCertificates:]_block_invoke.71.cold.1
- ___65+[POSecKeyHelper createSEPKeyForKeyType:userPresence:currentSet:]_block_invoke.28
- ___65+[POSecKeyHelper createSEPKeyForKeyType:userPresence:currentSet:]_block_invoke.28.cold.1
- ___65+[POSecKeyHelper createSEPKeyForKeyType:userPresence:currentSet:]_block_invoke.33
- ___65+[POSecKeyHelper createSEPKeyForKeyType:userPresence:currentSet:]_block_invoke.33.cold.1
- ___68-[POAgentAuthenticationProcess _doLoginWithPasswordContext:tokenId:]_block_invoke.137
- ___68-[POAgentAuthenticationProcess _doLoginWithPasswordContext:tokenId:]_block_invoke.137.cold.1
- ___70-[POAgentAuthenticationProcess _doRefreshWithPasswordContext:tokenId:]_block_invoke.118
- ___70-[POAgentAuthenticationProcess _doRefreshWithPasswordContext:tokenId:]_block_invoke.118.cold.1
- ___70-[POAgentAuthenticationProcess _doRefreshWithPasswordContext:tokenId:]_block_invoke.124
- ___70-[POAgentAuthenticationProcess _doRefreshWithPasswordContext:tokenId:]_block_invoke.124.cold.1
- ___70-[POAgentAuthenticationProcess _doRefreshWithPasswordContext:tokenId:]_block_invoke.132
- ___70-[POAgentAuthenticationProcess doUnlockForTokenWithCredentialContext:]_block_invoke.81
- ___70-[POAgentAuthenticationProcess doUnlockForTokenWithCredentialContext:]_block_invoke.81.cold.1
- ___73-[POAgentAuthenticationProcess doUnlockForPasswordWithCredentialContext:]_block_invoke.69
- ___73-[POAgentAuthenticationProcess doUnlockForPasswordWithCredentialContext:]_block_invoke.69.cold.1
- ___86-[POAgentAuthenticationProcess performLoginForCurrentUserWithPasswordContext:tokenId:]_block_invoke.101
- ___86-[POAgentAuthenticationProcess performLoginForCurrentUserWithPasswordContext:tokenId:]_block_invoke.101.cold.1
- ___block_descriptor_66_e8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
- ___block_literal_global.131
- _objc_msgSend$screenDidUnlockWithCredentialContext:smartCardContext:tokenId:atLogin:tokenUnlock:completion:
- _objc_msgSend$sendPasswordChangedNotification
- _objc_msgSend$setTouchIDAuthenticationAllowableReuseDuration:
CStrings:
+ "%s context = %{public}@, sccontext = %{public}@, bcontext = %{public}@ on %@"
+ "-[POAgentProcess screenDidUnlockWithCredentialContext:smartCardContext:biometricContext:tokenId:atLogin:tokenUnlock:completion:]"
+ "-[POAuthPluginProcess screenDidUnlockWithCredentialContext:smartCardContext:biometricContext:tokenId:atLogin:tokenUnlock:]"
+ "Failed to clear SSO tokens after login."
+ "Failed to validate key"
+ "Using context from unlock."
+ "Verifying device keys"
+ "Verifying user key"
+ "key is valid"
+ "screenDidUnlockWithCredentialContext:smartCardContext:biometricContext:tokenId:atLogin:tokenUnlock:"
+ "screenDidUnlockWithCredentialContext:smartCardContext:biometricContext:tokenId:atLogin:tokenUnlock:completion:"
+ "v56@0:8@16@24@32@40B48B52"
+ "v64@0:8@\"NSData\"16@\"NSData\"24@\"NSData\"32@\"NSString\"40B48B52@?<v@?@\"NSError\">56"
+ "v64@0:8@16@24@32@40B48B52@?56"
+ "verifyKey:"
- "%s context = %{public}@, sccontext = %{public}@ on %@"
- "-[POAgentProcess screenDidUnlockWithCredentialContext:smartCardContext:tokenId:atLogin:tokenUnlock:completion:]"
- "-[POAuthPluginProcess screenDidUnlockWithCredentialContext:smartCardContext:tokenId:atLogin:tokenUnlock:]"
- "screenDidUnlockWithCredentialContext:smartCardContext:tokenId:atLogin:tokenUnlock:"
- "screenDidUnlockWithCredentialContext:smartCardContext:tokenId:atLogin:tokenUnlock:completion:"
- "setTouchIDAuthenticationAllowableReuseDuration:"
- "v48@0:8@16@24@32B40B44"
- "v56@0:8@\"NSData\"16@\"NSData\"24@\"NSString\"32B40B44@?<v@?@\"NSError\">48"
- "v56@0:8@16@24@32B40B44@?48"

```
