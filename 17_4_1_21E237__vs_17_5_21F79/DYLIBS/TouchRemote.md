## TouchRemote

> `/System/Library/PrivateFrameworks/TouchRemote.framework/TouchRemote`

```diff

-180.40.4.0.0
-  __TEXT.__text: 0x2623c
-  __TEXT.__auth_stubs: 0x820
-  __TEXT.__objc_methlist: 0x2770
+180.50.10.0.0
+  __TEXT.__text: 0x284a0
+  __TEXT.__auth_stubs: 0x830
+  __TEXT.__objc_methlist: 0x2a10
   __TEXT.__const: 0x18
-  __TEXT.__cstring: 0x299f
-  __TEXT.__oslogstring: 0x2357
-  __TEXT.__gcc_except_tab: 0x4c8
-  __TEXT.__unwind_info: 0x9d4
-  __TEXT.__objc_classname: 0x8da
-  __TEXT.__objc_methname: 0x5440
-  __TEXT.__objc_methtype: 0x9ef
-  __TEXT.__objc_stubs: 0x3d00
-  __DATA_CONST.__got: 0x120
-  __DATA_CONST.__const: 0xdd0
-  __DATA_CONST.__objc_classlist: 0x2a0
+  __TEXT.__cstring: 0x2b82
+  __TEXT.__oslogstring: 0x26b5
+  __TEXT.__gcc_except_tab: 0x4e8
+  __TEXT.__unwind_info: 0xa4c
+  __TEXT.__objc_classname: 0x92a
+  __TEXT.__objc_methname: 0x5b30
+  __TEXT.__objc_methtype: 0xae8
+  __TEXT.__objc_stubs: 0x40a0
+  __DATA_CONST.__got: 0x138
+  __DATA_CONST.__const: 0xe60
+  __DATA_CONST.__objc_classlist: 0x2b0
   __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x48
+  __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x6660
-  __DATA_CONST.__objc_selrefs: 0x12b8
-  __DATA_CONST.__objc_classrefs: 0x360
-  __DATA_CONST.__objc_superrefs: 0x1b8
+  __DATA_CONST.__objc_const: 0x6e80
+  __DATA_CONST.__objc_selrefs: 0x1410
+  __DATA_CONST.__objc_classrefs: 0x378
+  __DATA_CONST.__objc_superrefs: 0x1c8
   __DATA_CONST.__objc_arraydata: 0xb0
-  __AUTH_CONST.__objc_const: 0x1e08
-  __AUTH_CONST.__cfstring: 0x1ee0
-  __AUTH_CONST.__const: 0x100
-  __AUTH_CONST.__objc_intobj: 0x198
+  __AUTH_CONST.__objc_const: 0x1ee0
+  __AUTH_CONST.__cfstring: 0x1f80
+  __AUTH_CONST.__const: 0x140
+  __AUTH_CONST.__objc_intobj: 0x1b0
   __AUTH_CONST.__objc_arrayobj: 0xf0
-  __AUTH_CONST.__auth_got: 0x420
-  __AUTH.__objc_data: 0x19a0
-  __AUTH.__data: 0x10
-  __DATA.__objc_ivar: 0x2ac
-  __DATA.__data: 0x368
-  __DATA.__bss: 0x48
+  __AUTH_CONST.__auth_got: 0x428
+  __AUTH.__objc_data: 0x1a40
+  __AUTH.__data: 0x18
+  __DATA.__objc_ivar: 0x310
+  __DATA.__data: 0x3c8
+  __DATA.__bss: 0x70
   __DATA_DIRTY.__objc_data: 0xa0
   __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: D1C660E4-B149-3012-8DF4-3F6EF9C2A7DE
-  Functions: 964
-  Symbols:   3675
-  CStrings:  1909
+  UUID: AA32FDF8-38E6-3D3D-902E-EB173B04599A
+  Functions: 1031
+  Symbols:   3909
+  CStrings:  2032
 
Symbols:
+ +[TRDefaults forceProxyAuth]
+ +[TRDefaults getBoolForKey:defaultValue:]
+ +[TRDefaults getDoubleForKey:defaultValue:]
+ +[TRDefaults getIntegerForKey:defaultValue:]
+ +[TRDefaults setBoolForKey:newValue:]
+ +[TRDefaults sharedDefaults]
+ +[TRDefaults sharedInstance]
+ -[TRAuthenticationOperation authType]
+ -[TRAuthenticationOperation canDoTermsAndConditions]
+ -[TRAuthenticationOperation forceFail]
+ -[TRAuthenticationOperation presentingChildViewController]
+ -[TRAuthenticationOperation setAuthType:]
+ -[TRAuthenticationOperation setCanDoTermsAndConditions:]
+ -[TRAuthenticationOperation setForceFail:]
+ -[TRAuthenticationOperation setPresentingChildViewController:]
+ -[TRCompanionAuthOperation _handleProxyDeviceResponse:]
+ -[TRCompanionAuthOperation _handleResponse:proxiedDevice:]
+ -[TRCompanionAuthOperation _performCompanionAuthenticationWithProxiedDevice:]
+ -[TRCompanionAuthOperation _sendProxyDeviceRequest]
+ -[TRCompanionAuthOperation canDoTermsAndConditions]
+ -[TRCompanionAuthOperation forceFail]
+ -[TRCompanionAuthOperation isForHomePod]
+ -[TRCompanionAuthOperation presentingChildViewController]
+ -[TRCompanionAuthOperation presentingViewController]
+ -[TRCompanionAuthOperation setCanDoTermsAndConditions:]
+ -[TRCompanionAuthOperation setForceFail:]
+ -[TRCompanionAuthOperation setIsForHomePod:]
+ -[TRCompanionAuthOperation setPresentingChildViewController:]
+ -[TRCompanionAuthOperation setPresentingViewController:]
+ -[TRDefaults .cxx_destruct]
+ -[TRDefaults defaults]
+ -[TRDefaults init]
+ -[TRDefaults setDefaults:]
+ -[TRProxyAuthOperation _handleProxyAuthenticationResponse:proxiedDevice:]
+ -[TRProxyAuthOperation canDoTermsAndConditions]
+ -[TRProxyAuthOperation forceFail]
+ -[TRProxyAuthOperation isForHomePod]
+ -[TRProxyAuthOperation presentingChildViewController]
+ -[TRProxyAuthOperation setCanDoTermsAndConditions:]
+ -[TRProxyAuthOperation setForceFail:]
+ -[TRProxyAuthOperation setIsForHomePod:]
+ -[TRProxyAuthOperation setPresentingChildViewController:]
+ -[TRSetupAuthenticationResponse authenticationResults]
+ -[TRSetupAuthenticationResponse setAuthenticationResults:]
+ -[TRTermsAndConditionsManager .cxx_destruct]
+ -[TRTermsAndConditionsManager genericTermsRemoteUI:acceptedTermsInfo:]
+ -[TRTermsAndConditionsManager genericTermsRemoteUI:didFinishWithSuccess:]
+ -[TRTermsAndConditionsManager handleAccept]
+ -[TRTermsAndConditionsManager handleDecline]
+ -[TRTermsAndConditionsManager initWithAuthResultsBlock:presentingViewController:]
+ -[TRTermsAndConditionsManager invalidate]
+ -[TRTermsAndConditionsManager loadProxiedTerms:anisetteDataProvider:appProvidedContext:acceptAction:declineAction:]
+ -[TRTermsAndConditionsManager presentProxiedTermsRemoteUI]
+ -[TRTermsAndConditionsManager proxiedTermsRemoteUI]
+ -[TRTermsAndConditionsManager setAcceptedTermsInfo:]
+ -[TRTermsAndConditionsManager setProxiedTermsRemoteUI:]
+ GCC_except_table4
+ _AATermsEntryPrivacy
+ _AATermsEntryWarranty
+ _AATermsEntryiCloud
+ _AAUIProxiedTermsRemoteUIFunction
+ _AppleAccountUILibrary.sLib
+ _AppleAccountUILibrary.sOnce
+ _OBJC_CLASS_$_NSUserDefaults
+ _OBJC_CLASS_$_TRDefaults
+ _OBJC_CLASS_$_TRTermsAndConditionsManager
+ _OBJC_IVAR_$_TRAuthenticationOperation._authType
+ _OBJC_IVAR_$_TRAuthenticationOperation._canDoTermsAndConditions
+ _OBJC_IVAR_$_TRAuthenticationOperation._forceFail
+ _OBJC_IVAR_$_TRAuthenticationOperation._presentingChildViewController
+ _OBJC_IVAR_$_TRCompanionAuthOperation._canDoTermsAndConditions
+ _OBJC_IVAR_$_TRCompanionAuthOperation._forceFail
+ _OBJC_IVAR_$_TRCompanionAuthOperation._isForHomePod
+ _OBJC_IVAR_$_TRCompanionAuthOperation._presentingChildViewController
+ _OBJC_IVAR_$_TRCompanionAuthOperation._presentingViewController
+ _OBJC_IVAR_$_TRCompanionAuthOperation._termsManager
+ _OBJC_IVAR_$_TRDefaults._defaults
+ _OBJC_IVAR_$_TRProxyAuthOperation._canDoTermsAndConditions
+ _OBJC_IVAR_$_TRProxyAuthOperation._forceFail
+ _OBJC_IVAR_$_TRProxyAuthOperation._isForHomePod
+ _OBJC_IVAR_$_TRProxyAuthOperation._presentingChildViewController
+ _OBJC_IVAR_$_TRProxyAuthOperation._termsManager
+ _OBJC_IVAR_$_TRSetupAuthenticationResponse._authenticationResults
+ _OBJC_IVAR_$_TRTermsAndConditionsManager._acceptAction
+ _OBJC_IVAR_$_TRTermsAndConditionsManager._acceptedTermsInfo
+ _OBJC_IVAR_$_TRTermsAndConditionsManager._authResult
+ _OBJC_IVAR_$_TRTermsAndConditionsManager._declineAction
+ _OBJC_IVAR_$_TRTermsAndConditionsManager._didAccept
+ _OBJC_IVAR_$_TRTermsAndConditionsManager._presentingViewController
+ _OBJC_IVAR_$_TRTermsAndConditionsManager._proxiedDevice
+ _OBJC_IVAR_$_TRTermsAndConditionsManager._proxiedTermsRemoteUI
+ _OBJC_METACLASS_$_TRDefaults
+ _OBJC_METACLASS_$_TRTermsAndConditionsManager
+ _TROperationErrorDomain
+ __OBJC_$_CLASS_METHODS_TRDefaults
+ __OBJC_$_INSTANCE_METHODS_TRDefaults
+ __OBJC_$_INSTANCE_METHODS_TRTermsAndConditionsManager
+ __OBJC_$_INSTANCE_VARIABLES_TRDefaults
+ __OBJC_$_INSTANCE_VARIABLES_TRTermsAndConditionsManager
+ __OBJC_$_PROP_LIST_TRDefaults
+ __OBJC_$_PROP_LIST_TRTermsAndConditionsManager
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AAUIGenericTermsRemoteUIDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_AAUIGenericTermsRemoteUIDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AAUIGenericTermsRemoteUIDelegate
+ __OBJC_$_PROTOCOL_REFS_AAUIGenericTermsRemoteUIDelegate
+ __OBJC_CLASS_PROTOCOLS_$_TRTermsAndConditionsManager
+ __OBJC_CLASS_RO_$_TRDefaults
+ __OBJC_CLASS_RO_$_TRTermsAndConditionsManager
+ __OBJC_LABEL_PROTOCOL_$_AAUIGenericTermsRemoteUIDelegate
+ __OBJC_METACLASS_RO_$_TRDefaults
+ __OBJC_METACLASS_RO_$_TRTermsAndConditionsManager
+ __OBJC_PROTOCOL_$_AAUIGenericTermsRemoteUIDelegate
+ ___28+[TRDefaults sharedInstance]_block_invoke
+ ___51-[TRCompanionAuthOperation _sendProxyDeviceRequest]_block_invoke
+ ___58-[TRCompanionAuthOperation _handleResponse:proxiedDevice:]_block_invoke
+ ___58-[TRCompanionAuthOperation _handleResponse:proxiedDevice:]_block_invoke_2
+ ___58-[TRCompanionAuthOperation _handleResponse:proxiedDevice:]_block_invoke_3
+ ___58-[TRCompanionAuthOperation _handleResponse:proxiedDevice:]_block_invoke_4
+ ___72-[TRSetupHandler _handleProxyAuthenticationRequest:withResponseHandler:]_block_invoke_3
+ ___73-[TRProxyAuthOperation _handleProxyAuthenticationResponse:proxiedDevice:]_block_invoke
+ ___73-[TRProxyAuthOperation _handleProxyAuthenticationResponse:proxiedDevice:]_block_invoke_2
+ ___76-[TRSetupHandler _handleCompanionAuthenticationRequest:withResponseHandler:]_block_invoke_3
+ ___77-[TRCompanionAuthOperation _performCompanionAuthenticationWithProxiedDevice:]_block_invoke
+ ___AppleAccountUILibrary_block_invoke
+ ___block_descriptor_40_e8_32bs_e44_v32?0"NSSet"8"NSError"16"NSDictionary"24ls32l8
+ ___block_descriptor_48_e8_32s40s_e22_v16?0"NSDictionary"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40w_e39_v24?0"NSError"8"TRResponseMessage"16lw40l8s32l8
+ ___block_descriptor_56_e8_32s40s48s_e34_v24?0"NSDictionary"8"NSError"16ls32l8s40l8s48l8
+ __os_feature_enabled_impl
+ _classAAUIProxiedTermsRemoteUI
+ _getAAUIProxiedTermsRemoteUIClass
+ _initAAUIProxiedTermsRemoteUI
+ _kDefaultsDomain
+ _kDefaultsKey_ForceProxyAuth
+ _objc_msgSend$_handleProxyAuthenticationResponse:proxiedDevice:
+ _objc_msgSend$_handleResponse:proxiedDevice:
+ _objc_msgSend$_performCompanionAuthenticationWithProxiedDevice:
+ _objc_msgSend$authenticationResults
+ _objc_msgSend$boolForKey:
+ _objc_msgSend$decodeObjectForKey:
+ _objc_msgSend$defaults
+ _objc_msgSend$doubleForKey:
+ _objc_msgSend$forceProxyAuth
+ _objc_msgSend$getBoolForKey:defaultValue:
+ _objc_msgSend$handleAccept
+ _objc_msgSend$handleDecline
+ _objc_msgSend$initWithArray:
+ _objc_msgSend$initWithAuthResults:proxiedDevice:anisetteDataProvider:appProvidedContext:termsEntries:
+ _objc_msgSend$initWithAuthResultsBlock:presentingViewController:
+ _objc_msgSend$initWithSuiteName:
+ _objc_msgSend$integerForKey:
+ _objc_msgSend$loadProxiedTerms:anisetteDataProvider:appProvidedContext:acceptAction:declineAction:
+ _objc_msgSend$presentFromViewController:modal:
+ _objc_msgSend$presentProxiedTermsRemoteUI
+ _objc_msgSend$setAcceptedTermsInfo:
+ _objc_msgSend$setAuthenticationResults:
+ _objc_msgSend$setBool:forKey:
+ _objc_msgSend$setCanDoTermsAndConditions:
+ _objc_msgSend$setForceFail:
+ _objc_msgSend$setIsForHomePod:
+ _objc_msgSend$setPresentingChildViewController:
+ _objc_msgSend$setupHandler:performCompanionAuthenticationWithParams:completionWithErrorAuthResults:
+ _objc_msgSend$setupHandler:performProxyAuthenticationWithParamsAuthResult:completionWithErrorAuthResults:
+ _objc_msgSend$sharedDefaults
+ _sharedInstance.instance
- -[TRCompanionAuthOperation _handleResponse:]
- -[TRProxyAuthOperation _handleProxyAuthenticationResponse:]
- ___35-[TRCompanionAuthOperation execute]_block_invoke
- ___block_descriptor_48_e8_32s40s_e34_v24?0"NSDictionary"8"NSError"16ls32l8s40l8
- _objc_msgSend$_handleProxyAuthenticationResponse:
CStrings:
+ "\x01\x15"
+ "\x03"
+ "\x05\x12"
+ "$"
+ "%s Terms Done"
+ "%s Terms Done Presenting"
+ "%s response class is not TRSetupAuthenticationResponse: %@"
+ "%s: Force Proxy Auth Default enabled"
+ "-[TRCompanionAuthOperation _handleProxyDeviceResponse:]"
+ "-[TRCompanionAuthOperation _handleResponse:proxiedDevice:]"
+ "-[TRCompanionAuthOperation _performCompanionAuthenticationWithProxiedDevice:]"
+ "-[TRCompanionAuthOperation _sendProxyDeviceRequest]"
+ "-[TRProxyAuthOperation _handleProxyAuthenticationResponse:proxiedDevice:]"
+ "/System/Library/PrivateFrameworks/AppleAccountUI.framework/AppleAccountUI"
+ "@\"AAUIProxiedTermsRemoteUI\""
+ "@\"NSUserDefaults\""
+ "@\"TRTermsAndConditionsManager\""
+ "AAUIGenericTermsRemoteUIDelegate"
+ "AAUIProxiedTermsRemoteUI"
+ "Companion Auth Skipping terms"
+ "Error in response"
+ "HomePodSLA"
+ "HomePodSetup"
+ "Proxy Auth Skipping terms"
+ "Reason: Presenting VC Nil"
+ "Reason: Proxy Terms Nil"
+ "Showing Terms for Companion Auth"
+ "Showing Terms for Proxy Auth"
+ "T@\"AAUIProxiedTermsRemoteUI\",&,N,V_proxiedTermsRemoteUI"
+ "T@\"NSDictionary\",&,N,V_authenticationResults"
+ "T@\"NSUserDefaults\",&,N,V_defaults"
+ "T@\"UIViewController\",&,N,V_presentingChildViewController"
+ "TB,N,V_canDoTermsAndConditions"
+ "TB,N,V_forceFail"
+ "TB,N,V_isForHomePod"
+ "TRDefaults"
+ "TROperationErrorDomain"
+ "TRSetupAuthenticationMessages_ar"
+ "TRTermsAndConditionsManager"
+ "TRTermsAndConditionsManager Could not present"
+ "TRTermsAndConditionsManager Presenting Terms"
+ "TRTermsAndConditionsManager Terms Info not empty %@"
+ "TRTermsAndConditionsManager acceptedTerms undefined"
+ "TRTermsAndConditionsManager acceptedTermsInfo %@"
+ "TRTermsAndConditionsManager decline action undefined"
+ "TRTermsAndConditionsManager didFinishWithSuccess %s"
+ "TRTermsAndConditionsManager handleAccept"
+ "TRTermsAndConditionsManager handleAccept entered multiple times"
+ "TRTermsAndConditionsManager handleDecline"
+ "TRTermsAndConditionsManager loadProxiedTerms"
+ "Ti,N,V_authType"
+ "_acceptAction"
+ "_acceptedTermsInfo"
+ "_authResult"
+ "_authType"
+ "_authenticationResults"
+ "_canDoTermsAndConditions"
+ "_declineAction"
+ "_defaults"
+ "_didAccept"
+ "_forceFail"
+ "_handleProxyAuthenticationResponse:proxiedDevice:"
+ "_handleResponse:proxiedDevice:"
+ "_isForHomePod"
+ "_performCompanionAuthenticationWithProxiedDevice:"
+ "_presentingChildViewController"
+ "_proxiedDevice"
+ "_proxiedTermsRemoteUI"
+ "_termsManager"
+ "authType"
+ "authenticationResults"
+ "boolForKey:"
+ "canDoTermsAndConditions"
+ "d32@0:8@16d24"
+ "decodeObjectForKey:"
+ "defaults"
+ "doubleForKey:"
+ "forceFail"
+ "forceProxyAuth"
+ "genericTermsRemoteUI:acceptedTermsInfo:"
+ "genericTermsRemoteUI:didFinishWithSuccess:"
+ "getBoolForKey:defaultValue:"
+ "getDoubleForKey:defaultValue:"
+ "getIntegerForKey:defaultValue:"
+ "handleAccept"
+ "handleDecline"
+ "initWithArray:"
+ "initWithAuthResults:proxiedDevice:anisetteDataProvider:appProvidedContext:termsEntries:"
+ "initWithAuthResultsBlock:presentingViewController:"
+ "initWithSuiteName:"
+ "integerForKey:"
+ "isForHomePod"
+ "loadProxiedTerms:anisetteDataProvider:appProvidedContext:acceptAction:declineAction:"
+ "no"
+ "presentFromViewController:modal:"
+ "presentProxiedTermsRemoteUI"
+ "presentingChildViewController"
+ "proxiedTermsRemoteUI"
+ "q28@0:8@16B24"
+ "q32@0:8@16q24"
+ "setAcceptedTermsInfo:"
+ "setAuthType:"
+ "setAuthenticationResults:"
+ "setBool:forKey:"
+ "setBoolForKey:newValue:"
+ "setCanDoTermsAndConditions:"
+ "setDefaults:"
+ "setForceFail:"
+ "setIsForHomePod:"
+ "setPresentingChildViewController:"
+ "setProxiedTermsRemoteUI:"
+ "setupHandler:performCompanionAuthenticationWithParams:completionWithErrorAuthResults:"
+ "setupHandler:performProxyAuthenticationWithParamsAuthResult:completionWithErrorAuthResults:"
+ "sharedDefaults"
+ "termsandconditionsv2"
+ "unauthenticatedAccountServices:%@ error:%@ authResults:%@"
+ "v16@?0@\"NSDictionary\"8"
+ "v20@0:8i16"
+ "v28@0:8@\"AAUIGenericTermsRemoteUI\"16B24"
+ "v32@0:8@\"AAUIGenericTermsRemoteUI\"16@\"NSDictionary\"24"
+ "v32@?0@\"NSSet\"8@\"NSError\"16@\"NSDictionary\"24"
+ "v56@0:8@16@24@32@?40@?48"
+ "yes"
- "\x14"
- "-[TRCompanionAuthOperation _handleResponse:]"
- "-[TRCompanionAuthOperation execute]"
- "-[TRProxyAuthOperation _handleProxyAuthenticationResponse:]"
- "_handleProxyAuthenticationResponse:"
- "unauthenticatedAccountServices:%@ error:%@"

```
