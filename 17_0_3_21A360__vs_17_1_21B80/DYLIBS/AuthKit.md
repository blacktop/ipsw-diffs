## AuthKit

> `/System/Library/PrivateFrameworks/AuthKit.framework/AuthKit`

```diff

-458.1.1.7.0
-  __TEXT.__text: 0xab808
+464.5.0.0.0
+  __TEXT.__text: 0xabf48
   __TEXT.__auth_stubs: 0xd20
-  __TEXT.__objc_methlist: 0x9540
+  __TEXT.__objc_methlist: 0x9650
   __TEXT.__const: 0x1760
-  __TEXT.__cstring: 0xb3ac
-  __TEXT.__oslogstring: 0xca8a
-  __TEXT.__gcc_except_tab: 0x3c5c
+  __TEXT.__cstring: 0xb3de
+  __TEXT.__oslogstring: 0xc9d2
+  __TEXT.__gcc_except_tab: 0x3c88
   __TEXT.__ustring: 0x1b8
-  __TEXT.__unwind_info: 0x316c
-  __TEXT.__objc_classname: 0x1413
-  __TEXT.__objc_methname: 0x19537
-  __TEXT.__objc_methtype: 0x3467
-  __TEXT.__objc_stubs: 0xbb00
+  __TEXT.__unwind_info: 0x319c
+  __TEXT.__objc_classname: 0x14c6
+  __TEXT.__objc_methname: 0x197a5
+  __TEXT.__objc_methtype: 0x3606
+  __TEXT.__objc_stubs: 0xbba0
   __DATA_CONST.__got: 0x2e8
-  __DATA_CONST.__const: 0x4578
-  __DATA_CONST.__objc_classlist: 0x468
-  __DATA_CONST.__objc_catlist: 0x78
-  __DATA_CONST.__objc_protolist: 0x180
+  __DATA_CONST.__const: 0x45b8
+  __DATA_CONST.__objc_classlist: 0x470
+  __DATA_CONST.__objc_catlist: 0x80
+  __DATA_CONST.__objc_protolist: 0x190
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1a490
-  __DATA_CONST.__objc_selrefs: 0x5428
+  __DATA_CONST.__objc_const: 0x1a6e8
+  __DATA_CONST.__objc_selrefs: 0x54b0
   __DATA_CONST.__objc_arraydata: 0x128
-  __AUTH_CONST.__cfstring: 0xb8e0
-  __AUTH_CONST.__objc_const: 0x40c8
-  __AUTH_CONST.__const: 0xef0
+  __AUTH_CONST.__cfstring: 0xb9e0
+  __AUTH_CONST.__objc_const: 0x4198
+  __AUTH_CONST.__const: 0xf30
   __AUTH_CONST.__objc_intobj: 0x1c8
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_dictobj: 0x168
   __AUTH_CONST.__auth_got: 0x6a0
-  __AUTH.__objc_data: 0x19f0
-  __DATA.__objc_protorefs: 0xc0
-  __DATA.__objc_classrefs: 0x560
-  __DATA.__objc_superrefs: 0x2a0
-  __DATA.__objc_ivar: 0xc78
-  __DATA.__data: 0x1440
-  __DATA.__bss: 0x338
+  __AUTH.__objc_data: 0x1a40
+  __DATA.__objc_protorefs: 0xd0
+  __DATA.__objc_classrefs: 0x578
+  __DATA.__objc_superrefs: 0x2a8
+  __DATA.__objc_ivar: 0xc7c
+  __DATA.__data: 0x1500
+  __DATA.__bss: 0x358
   __DATA_DIRTY.__objc_data: 0x1220
   __DATA_DIRTY.__bss: 0x1f8
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: AE84E63B-0139-3DD0-93F3-14B2FAE70C0C
-  Functions: 5064
-  Symbols:   16439
-  CStrings:  8766
+  UUID: 3862F148-551B-3E51-ABF9-99FA26526610
+  Functions: 5085
+  Symbols:   16534
+  CStrings:  8808
 
Symbols:
+ +[AKRemoteViewServiceConfiguration configurationForHostWithBundleID:sceneID:]
+ +[AKRemoteViewServiceConfiguration defaultConfiguration]
+ +[AKRemoteViewServiceConfiguration supportsSecureCoding]
+ +[NSError(AuthKit) ak_deviceListErrorWithCode:]
+ +[NSXPCInterface(NSXPCInterface_AKRemoteViewServiceInterface) remoteViewServiceInterface]
+ +[NSXPCInterface(NSXPCInterface_AKRemoteViewSessionInterface) remoteViewSessionInterface]
+ -[AKAccountManager _isSilentEscrowRecordRepairEnabledForAccountV2:]
+ -[AKAccountManager _isSilentEscrowRecordRepairEnabledForAccountV2:].cold.1
+ -[AKAccountManager isSilentEscrowRecordRepairEnabledForAccountV2:]
+ -[AKAccountManager isSilentEscrowRecordRepairEnabledForAccountV2:].cold.1
+ -[AKAccountManager isSilentEscrowRecordRepairEnabledForAccountV2:].cold.2
+ -[AKAccountManager setSilentEscrowRecordRepairEnabledV2:forAccount:]
+ -[AKAccountManager setSilentEscrowRecordRepairEnabledV2:forAccount:].cold.1
+ -[AKAdaptiveService activate]
+ -[AKAdaptiveService invalidate]
+ -[AKAdaptiveService remoteObjectInterface]
+ -[AKAdaptiveService setRemoteObjectInterface:]
+ -[AKAppleIDAuthenticationController performCheckInForAccountWithAltDSID:event:completion:]
+ -[AKConfiguration contactKeyVerification]
+ -[AKConfiguration forceSilentEscrowRecordRepairEnabledV2]
+ -[AKConfiguration setContactKeyVerification:]
+ -[AKConfiguration setForceSilentEscrowRecordRepairEnabledV2:]
+ -[AKRemoteViewServiceConfiguration .cxx_destruct]
+ -[AKRemoteViewServiceConfiguration encodeWithCoder:]
+ -[AKRemoteViewServiceConfiguration hostBundleID]
+ -[AKRemoteViewServiceConfiguration hostSceneID]
+ -[AKRemoteViewServiceConfiguration initWithCoder:]
+ -[AKRemoteViewServiceConfiguration setHostBundleID:]
+ -[AKRemoteViewServiceConfiguration setHostSceneID:]
+ -[AKURLBag isFirstPartyURLEntitlementCheckDisabled]
+ GCC_except_table101
+ GCC_except_table105
+ GCC_except_table109
+ GCC_except_table124
+ GCC_except_table127
+ GCC_except_table138
+ GCC_except_table142
+ GCC_except_table146
+ GCC_except_table150
+ GCC_except_table175
+ GCC_except_table213
+ GCC_except_table214
+ GCC_except_table215
+ GCC_except_table237
+ GCC_except_table249
+ GCC_except_table250
+ GCC_except_table251
+ _AKAllConfigsKey
+ _AKAppleIDAuthenticationServerErrorDomain
+ _AKLivenessErrorDomain
+ _AKPostDataEventFinalSignOut
+ _AKPostDataEventLiveness
+ _AKPostDataEventServiceSignOut
+ _AKPostDataEventUpdateDeviceState
+ _AKSilentEscrowRecordRepairEnabledKeyV2
+ _AKUserNotificationCreate
+ _OBJC_CLASS_$_AKRemoteViewServiceConfiguration
+ _OBJC_IVAR_$_AKAdaptiveService._remoteObjectInterface
+ _OBJC_IVAR_$_AKRemoteViewServiceConfiguration._hostBundleID
+ _OBJC_IVAR_$_AKRemoteViewServiceConfiguration._hostSceneID
+ _OBJC_METACLASS_$_AKRemoteViewServiceConfiguration
+ __AKHTTPHeaderClientTime
+ __OBJC_$_CATEGORY_NSXPCInterface_$_NSXPCInterface_AKRemoteViewServiceInterface
+ __OBJC_$_CLASS_METHODS_AKRemoteViewServiceConfiguration
+ __OBJC_$_CLASS_METHODS_NSXPCInterface(NSXPCInterface_AKRemoteViewServiceInterface|NSXPCInterface_AKRemoteViewSessionInterface)
+ __OBJC_$_CLASS_PROP_LIST_AKRemoteViewServiceConfiguration
+ __OBJC_$_INSTANCE_METHODS_AKRemoteViewServiceConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_AKRemoteViewServiceConfiguration
+ __OBJC_$_PROP_LIST_AKRemoteViewServiceConfiguration
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AKRemoteViewServiceInterface
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AKRemoteViewSessionInterface
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AKRemoteViewServiceInterface
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AKRemoteViewSessionInterface
+ __OBJC_$_PROTOCOL_REFS_AKRemoteViewSessionInterface
+ __OBJC_CLASS_PROTOCOLS_$_AKRemoteViewServiceConfiguration
+ __OBJC_CLASS_RO_$_AKRemoteViewServiceConfiguration
+ __OBJC_LABEL_PROTOCOL_$_AKRemoteViewServiceInterface
+ __OBJC_LABEL_PROTOCOL_$_AKRemoteViewSessionInterface
+ __OBJC_METACLASS_RO_$_AKRemoteViewServiceConfiguration
+ __OBJC_PROTOCOL_$_AKRemoteViewServiceInterface
+ __OBJC_PROTOCOL_$_AKRemoteViewSessionInterface
+ __OBJC_PROTOCOL_REFERENCE_$_AKRemoteViewServiceInterface
+ __OBJC_PROTOCOL_REFERENCE_$_AKRemoteViewSessionInterface
+ ___73-[AKAppleIDSession _generateAppleIDHeadersForSessionTask:withCompletion:]_block_invoke.60.cold.1
+ ___73-[AKAppleIDSession _generateAppleIDHeadersForSessionTask:withCompletion:]_block_invoke.61
+ ___74-[AKAppleIDSession _handleAnissetteURLResponse:forRequest:withCompletion:]_block_invoke.77
+ ___74-[AKAppleIDSession _handleAnissetteURLResponse:forRequest:withCompletion:]_block_invoke.77.cold.1
+ ___74-[AKAppleIDSession _handleAnissetteURLResponse:forRequest:withCompletion:]_block_invoke.77.cold.2
+ ___89+[NSXPCInterface(NSXPCInterface_AKRemoteViewServiceInterface) remoteViewServiceInterface]_block_invoke
+ ___89+[NSXPCInterface(NSXPCInterface_AKRemoteViewSessionInterface) remoteViewSessionInterface]_block_invoke
+ ___90-[AKAppleIDAuthenticationController performCheckInForAccountWithAltDSID:event:completion:]_block_invoke
+ ___90-[AKAppleIDAuthenticationController performCheckInForAccountWithAltDSID:event:completion:]_block_invoke.292
+ ___90-[AKAppleIDAuthenticationController performCheckInForAccountWithAltDSID:event:completion:]_block_invoke.292.cold.1
+ ___90-[AKAppleIDAuthenticationController performCheckInForAccountWithAltDSID:event:completion:]_block_invoke_2
+ ___90-[AKAppleIDAuthenticationController performCheckInForAccountWithAltDSID:event:completion:]_block_invoke_2.cold.1
+ ___block_literal_global.310
+ _objc_msgSend$_isSilentEscrowRecordRepairEnabledForAccountV2:
+ _objc_msgSend$contactKeyVerification
+ _objc_msgSend$defaultConfiguration
+ _objc_msgSend$forceSilentEscrowRecordRepairEnabledV2
+ _objc_msgSend$performCheckInForAccountWithAltDSID:event:completion:
+ _objc_msgSend$setHostBundleID:
+ _objc_msgSend$setHostSceneID:
+ _objc_msgSend$setInterface:forSelector:argumentIndex:ofReply:
+ _remoteViewServiceInterface.interface
+ _remoteViewServiceInterface.once
+ _remoteViewSessionInterface.interface
+ _remoteViewSessionInterface.once
- +[AKLoginCodeNotificationBuilder iconURL]
- -[AKAccountManager hasSOSActiveDeviceForAccount:].cold.2
- -[AKAccountManager hasSOSActiveDeviceForAccount:].cold.3
- -[AKAccountManager isSOSNeededForAccount:].cold.2
- -[AKAccountManager isSOSNeededForAccount:].cold.3
- -[AKAppleIDSession _handleAnissetteURLResponse:forRequest:withCompletion:].cold.7
- -[AKFeatureManager init].cold.8
- -[AKFeatureManager isFamilyAccountEnabled]
- -[AKURLBag isAidProxAdvertisementDisableSupportedConfig]
- -[AKURLBag isAidProxAdvertisementDisabledConfig]
- GCC_except_table100
- GCC_except_table104
- GCC_except_table108
- GCC_except_table112
- GCC_except_table120
- GCC_except_table123
- GCC_except_table126
- GCC_except_table130
- GCC_except_table134
- GCC_except_table137
- GCC_except_table145
- GCC_except_table149
- GCC_except_table163
- GCC_except_table174
- GCC_except_table211
- GCC_except_table224
- GCC_except_table225
- GCC_except_table226
- GCC_except_table240
- _OBJC_IVAR_$_AKFeatureManager._cachedIsFamilyAccountEnabled
- _OBJC_IVAR_$_AKURLBag._isAidProxAdvertisementDisableSupportedConfig
- ___73-[AKAppleIDSession _generateAppleIDHeadersForSessionTask:withCompletion:]_block_invoke.59
- ___73-[AKAppleIDSession _generateAppleIDHeadersForSessionTask:withCompletion:]_block_invoke.59.cold.1
- ___74-[AKAppleIDSession _handleAnissetteURLResponse:forRequest:withCompletion:]_block_invoke.75
- ___74-[AKAppleIDSession _handleAnissetteURLResponse:forRequest:withCompletion:]_block_invoke.75.cold.1
- ___74-[AKAppleIDSession _handleAnissetteURLResponse:forRequest:withCompletion:]_block_invoke.75.cold.2
- ___84-[AKAppleIDAuthenticationController performCheckInForAccountWithAltDSID:completion:]_block_invoke
- ___84-[AKAppleIDAuthenticationController performCheckInForAccountWithAltDSID:completion:]_block_invoke.292
- ___84-[AKAppleIDAuthenticationController performCheckInForAccountWithAltDSID:completion:]_block_invoke.292.cold.1
- ___84-[AKAppleIDAuthenticationController performCheckInForAccountWithAltDSID:completion:]_block_invoke_2
- ___84-[AKAppleIDAuthenticationController performCheckInForAccountWithAltDSID:completion:]_block_invoke_2.cold.1
- ___block_literal_global.307
- _objc_msgSend$URLForResource:withExtension:
- _objc_msgSend$bundleWithPath:
- _objc_msgSend$performCheckInForAccountWithAltDSID:completion:
CStrings:
+ "AKAuthenticationServerError"
+ "AKForceSilentEscrowRecordRepairEnabledV2"
+ "AKLivenessError"
+ "AKRemoteViewServiceConfiguration"
+ "AKRemoteViewServiceInterface"
+ "AKRemoteViewSessionInterface"
+ "Exception caught when fetching silentEscrowRecordRepairEnabledV2 property: %@"
+ "Exception caught when setting silentEscrowRecordRepairEnabledV2 property: %@"
+ "NSXPCInterface_AKRemoteViewServiceInterface"
+ "NSXPCInterface_AKRemoteViewSessionInterface"
+ "Silent escrow record repair V2 is force disabled"
+ "Silent escrow record repair V2 is force enabled"
+ "T@\"NSString\",C,N,V_hostBundleID"
+ "T@\"NSString\",C,N,V_hostSceneID"
+ "T@\"NSXPCInterface\",&,N,V_remoteObjectInterface"
+ "Vv24@0:8@?<v@?@\"AKRemoteViewServiceConfiguration\"@\"NSError\">16"
+ "Vv32@0:8@\"NSUUID\"16@?<v@?@\"NSError\">24"
+ "Vv40@0:8@\"AKAuthorizationPresentationContext\"16@\"<AKAuthorizationPresenterHostProtocol>\"24@?<v@?@\"AKAuthorization\"@\"NSError\">32"
+ "Vv40@0:8@\"AKPrivateEmailContext\"16@\"<AKPrivateEmailPresenterHostProtocol>\"24@?<v@?@\"AKPrivateEmail\"@\"NSError\">32"
+ "Vv40@0:8@16@24@?32"
+ "_AKContactKeyVerification"
+ "_hostBundleID"
+ "_hostSceneID"
+ "_isSilentEscrowRecordRepairEnabledForAccountV2:"
+ "_remoteObjectInterface"
+ "activateWithCompletionHandler:"
+ "ak_deviceListErrorWithCode:"
+ "configurationForHostWithBundleID:sceneID:"
+ "contactKeyVerification"
+ "continueAuthenticationWithSurrogateID:completionHandler:"
+ "defaultConfiguration"
+ "firstPartyURLEntitlementCheckDisabled"
+ "forceSilentEscrowRecordRepairEnabledV2"
+ "hostBundleID"
+ "hostSceneID"
+ "isFirstPartyURLEntitlementCheckDisabled"
+ "isSilentEscrowRecordRepairEnabledForAccountV2:"
+ "liveness"
+ "performCheckInForAccountWithAltDSID:event:completion:"
+ "presentAuthorizationWithContext:usingHost:completionHandler:"
+ "presentPrivateEmailWithContext:usingHost:completionHandler:"
+ "remoteObjectInterface"
+ "remoteViewServiceInterface"
+ "remoteViewSessionInterface"
+ "setContactKeyVerification:"
+ "setForceSilentEscrowRecordRepairEnabledV2:"
+ "setHostBundleID:"
+ "setHostSceneID:"
+ "setInterface:forSelector:argumentIndex:ofReply:"
+ "setSilentEscrowRecordRepairEnabledV2:forAccount:"
+ "signout-"
+ "signout-all"
+ "silentEscrowRecordRepairEnabledV2"
+ "update-device-state"
+ "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"NSError\">32"
- "%@:%s send RTC midInvalidated event since kAKHTTPStatusCodeReprovision"
- "-[AKAppleIDSession _handleAnissetteURLResponse:forRequest:withCompletion:]"
- "/System/Library/PrivateFrameworks/AuthKitUI.framework"
- "FamilyAccount"
- "Feature FamilyAccount is supported. Is FamilyAccount enabled - %@"
- "TB,R,N,GisAidProxAdvertisementDisableSupportedConfig,V_isAidProxAdvertisementDisableSupportedConfig"
- "TB,R,N,GisFamilyAccountEnabled"
- "URLForResource:withExtension:"
- "_cachedIsFamilyAccountEnabled"
- "_isAidProxAdvertisementDisableSupportedConfig"
- "aidProxAdvertisementDisabled"
- "appleaccount_mono_icon-60-dark@2x"
- "bundleWithPath:"
- "enableFamilyAccount"
- "forceHasSOSActiveDevice was not set; use normal implementation"
- "forceHasSOSActiveDevice was set to %@; returning for AKAccountManager hasSOSActiveDeviceForAccount"
- "forceSOSNeeded was not set; use normal implementation"
- "forceSOSNeeded was set to %@; returning for AKAccountManager isSOSNeededForAccount"
- "iconURL"
- "isAidProxAdvertisementDisableSupportedConfig"
- "isAidProxAdvertisementDisabledConfig"
- "isFamilyAccountEnabled"
- "png"

```
