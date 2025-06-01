## MediaSetup

> `/System/Library/Frameworks/MediaSetup.framework/MediaSetup`

```diff

-207.40.20.0.0
-  __TEXT.__text: 0x128fc
+207.50.4.0.0
+  __TEXT.__text: 0x12efc
   __TEXT.__auth_stubs: 0x4f0
-  __TEXT.__objc_methlist: 0x184c
+  __TEXT.__objc_methlist: 0x1924
   __TEXT.__const: 0x98
-  __TEXT.__cstring: 0x25eb
+  __TEXT.__cstring: 0x264f
   __TEXT.__gcc_except_tab: 0x190
-  __TEXT.__oslogstring: 0x62e
-  __TEXT.__unwind_info: 0x638
-  __TEXT.__objc_classname: 0x43f
-  __TEXT.__objc_methname: 0x41c5
-  __TEXT.__objc_methtype: 0xa5c
-  __TEXT.__objc_stubs: 0x2b80
+  __TEXT.__oslogstring: 0x65b
+  __TEXT.__unwind_info: 0x660
+  __TEXT.__objc_classname: 0x4ab
+  __TEXT.__objc_methname: 0x4305
+  __TEXT.__objc_methtype: 0xae5
+  __TEXT.__objc_stubs: 0x2be0
   __DATA_CONST.__got: 0x60
   __DATA_CONST.__const: 0x8a0
-  __DATA_CONST.__objc_classlist: 0x110
+  __DATA_CONST.__objc_classlist: 0x120
   __DATA_CONST.__objc_catlist: 0x38
-  __DATA_CONST.__objc_protolist: 0x70
+  __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x4098
-  __DATA_CONST.__objc_selrefs: 0xf88
+  __DATA_CONST.__objc_const: 0x4c00
+  __DATA_CONST.__objc_selrefs: 0xfb8
   __DATA_CONST.__objc_protorefs: 0x38
-  __DATA_CONST.__objc_classrefs: 0x1c8
-  __DATA_CONST.__objc_superrefs: 0xe8
+  __DATA_CONST.__objc_classrefs: 0x1d0
+  __DATA_CONST.__objc_superrefs: 0xf8
   __DATA_CONST.__objc_arraydata: 0x10
   __AUTH_CONST.__cfstring: 0x2260
-  __AUTH_CONST.__objc_const: 0x1018
+  __AUTH_CONST.__objc_const: 0x10a8
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__auth_got: 0x288
-  __AUTH.__objc_data: 0x550
-  __DATA.__objc_ivar: 0x1f0
-  __DATA.__data: 0x548
+  __AUTH.__objc_data: 0x5f0
+  __DATA.__objc_ivar: 0x1fc
+  __DATA.__data: 0x608
   __DATA.__bss: 0x10
   __DATA_DIRTY.__objc_data: 0x550
   __DATA_DIRTY.__bss: 0x30

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A546F9C7-B4DF-3048-B1DA-1FCA93ECD47B
-  Functions: 614
-  Symbols:   2449
-  CStrings:  1550
+  UUID: 1838BF79-CE00-312B-BD32-751ECE6A11BE
+  Functions: 631
+  Symbols:   2528
+  CStrings:  1570
 
Symbols:
+ -[MSServer initWithMediator:]
+ -[MSServer mediator]
+ -[MSServer setMediator:]
+ -[MSServerMediator .cxx_destruct]
+ -[MSServerMediator accountsInterfaceDelegate]
+ -[MSServerMediator activeServiceApplicationInformationForSharedUserID:completionHandler:]
+ -[MSServerMediator addMediaService:usingSetupBundles:completion:]
+ -[MSServerMediator connectionDelegate]
+ -[MSServerMediator getAvailableServices:userIdentifier:completion:]
+ -[MSServerMediator getCachedAvailableServices:userIdentifier:completion:]
+ -[MSServerMediator getCachedServiceInfo:homeUserID:endpointID:completion:]
+ -[MSServerMediator getDefaultMediaService:homeUserID:completion:]
+ -[MSServerMediator getDefaultMediaServiceForAllUsers:]
+ -[MSServerMediator getMediaServiceChoicesForAllUsers:]
+ -[MSServerMediator getMediaServiceChoicesForAllUsers:].cold.1
+ -[MSServerMediator getMediaServiceChoicesForSharedUser:completion:]
+ -[MSServerMediator getMediaServiceChoicesForSharedUser:completion:].cold.1
+ -[MSServerMediator getPublicInfoForBundleID:completion:]
+ -[MSServerMediator getResolvedServiceInfo:completion:]
+ -[MSServerMediator getResolvedServiceInfo:sharedUserID:completion:]
+ -[MSServerMediator getServiceConfigurationInfo:serviceID:completion:]
+ -[MSServerMediator getSupportedThirdPartyMediaServices:]
+ -[MSServerMediator getSupportedThirdPartyMediaServices:].cold.1
+ -[MSServerMediator initWithAccountsDelegate:]
+ -[MSServerMediator openConnection]
+ -[MSServerMediator overrideAppleMusicSubscriptionStatus:homeUserIDS:completion:]
+ -[MSServerMediator removeMediaService:homeID:homeUserID:completion:]
+ -[MSServerMediator requestAuthRenewalForMediaService:homeUserID:parentNetworkActivity:completion:]
+ -[MSServerMediator setAccountsInterfaceDelegate:]
+ -[MSServerMediator setConnectionDelegate:]
+ -[MSServerMediator setVersion:completion:]
+ -[MSServerMediator switchUserAccountInfo:homeID:homeUserID:completion:]
+ -[MSServerMediator thirdPartyMusicAvailable:completion:]
+ -[MSServerMediator updateDefaultMediaService:homeID:homeUserID:completion:]
+ -[MSServerMediator updateProperty:homeID:homeUserID:withOptions:completion:]
+ -[MediaServiceConfiguration mediator]
+ -[MediaServiceConfiguration setMediator:]
+ -[MediaServiceConfigurationMediator .cxx_destruct]
+ -[MediaServiceConfigurationMediator delegate]
+ -[MediaServiceConfigurationMediator initWithServiceDelegate:]
+ -[MediaServiceConfigurationMediator serviceSettingDidUpdate:homeUserID:]
+ -[MediaServiceConfigurationMediator setDelegate:]
+ -[MediaServiceConfigurationMediator userDidRemoveService:homeUserID:]
+ -[MediaServiceConfigurationMediator userDidUpdateDefaultService:homeUserID:]
+ GCC_except_table10
+ GCC_except_table11
+ GCC_except_table7
+ GCC_except_table8
+ _OBJC_CLASS_$_MSServerMediator
+ _OBJC_CLASS_$_MediaServiceConfigurationMediator
+ _OBJC_IVAR_$_MSServer._mediator
+ _OBJC_IVAR_$_MSServerMediator._accountsInterfaceDelegate
+ _OBJC_IVAR_$_MSServerMediator._connectionDelegate
+ _OBJC_IVAR_$_MediaServiceConfiguration._mediator
+ _OBJC_IVAR_$_MediaServiceConfigurationMediator._delegate
+ _OBJC_METACLASS_$_MSServerMediator
+ _OBJC_METACLASS_$_MediaServiceConfigurationMediator
+ _OUTLINED_FUNCTION_2
+ __OBJC_$_INSTANCE_METHODS_MSServerMediator
+ __OBJC_$_INSTANCE_METHODS_MediaServiceConfigurationMediator
+ __OBJC_$_INSTANCE_VARIABLES_MSServerMediator
+ __OBJC_$_INSTANCE_VARIABLES_MediaServiceConfigurationMediator
+ __OBJC_$_PROP_LIST_MSServerMediator
+ __OBJC_$_PROP_LIST_MediaServiceConfigurationMediator
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_MSProxyConnectionDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MSProxyConnectionDelegate
+ __OBJC_$_PROTOCOL_REFS_MSInternalServiceConnectionProtocol
+ __OBJC_CLASS_PROTOCOLS_$_MSServerMediator
+ __OBJC_CLASS_PROTOCOLS_$_MediaServiceConfigurationMediator
+ __OBJC_CLASS_RO_$_MSServerMediator
+ __OBJC_CLASS_RO_$_MediaServiceConfigurationMediator
+ __OBJC_LABEL_PROTOCOL_$_MSInternalServiceConnectionProtocol
+ __OBJC_LABEL_PROTOCOL_$_MSProxyConnectionDelegate
+ __OBJC_METACLASS_RO_$_MSServerMediator
+ __OBJC_METACLASS_RO_$_MediaServiceConfigurationMediator
+ __OBJC_PROTOCOL_$_MSInternalServiceConnectionProtocol
+ __OBJC_PROTOCOL_$_MSProxyConnectionDelegate
+ __OBJC_PROTOCOL_REFERENCE_$_MSInternalServiceConnectionProtocol
+ ___43-[MediaServiceConfiguration initWithQueue:]_block_invoke.126
+ ___43-[MediaServiceConfiguration initWithQueue:]_block_invoke.126.cold.1
+ ___47-[MSServer listener:shouldAcceptNewConnection:]_block_invoke.130
+ ___54-[MediaServiceConfiguration thirdPartyMusicAvailable:]_block_invoke.134
+ ___79-[MediaServiceConfiguration(AppSelection) getSupportedThirdPartyMediaServices:]_block_invoke.199
+ ___79-[MediaServiceConfiguration(AppSelection) getSupportedThirdPartyMediaServices:]_block_invoke.cold.1
+ ___block_literal_global.147
+ _objc_msgSend$connectionDelegate
+ _objc_msgSend$initWithServiceDelegate:
+ _objc_msgSend$setConnectionDelegate:
- -[MSServer accountsInterfaceDelegate]
- -[MSServer activeServiceApplicationInformationForSharedUserID:completionHandler:]
- -[MSServer addMediaService:usingSetupBundles:completion:]
- -[MSServer getAvailableServices:userIdentifier:completion:]
- -[MSServer getCachedAvailableServices:userIdentifier:completion:]
- -[MSServer getCachedServiceInfo:homeUserID:endpointID:completion:]
- -[MSServer getDefaultMediaService:homeUserID:completion:]
- -[MSServer getDefaultMediaServiceForAllUsers:]
- -[MSServer getMediaServiceChoicesForAllUsers:]
- -[MSServer getMediaServiceChoicesForAllUsers:].cold.1
- -[MSServer getMediaServiceChoicesForSharedUser:completion:]
- -[MSServer getMediaServiceChoicesForSharedUser:completion:].cold.1
- -[MSServer getPublicInfoForBundleID:completion:]
- -[MSServer getResolvedServiceInfo:completion:]
- -[MSServer getResolvedServiceInfo:sharedUserID:completion:]
- -[MSServer getServiceConfigurationInfo:serviceID:completion:]
- -[MSServer getSupportedThirdPartyMediaServices:]
- -[MSServer getSupportedThirdPartyMediaServices:].cold.1
- -[MSServer initWithAccountsDelegate:]
- -[MSServer overrideAppleMusicSubscriptionStatus:homeUserIDS:completion:]
- -[MSServer removeMediaService:homeID:homeUserID:completion:]
- -[MSServer requestAuthRenewalForMediaService:homeUserID:parentNetworkActivity:completion:]
- -[MSServer setAccountsInterfaceDelegate:]
- -[MSServer setVersion:completion:]
- -[MSServer switchUserAccountInfo:homeID:homeUserID:completion:]
- -[MSServer thirdPartyMusicAvailable:completion:]
- -[MSServer updateDefaultMediaService:homeID:homeUserID:completion:]
- -[MSServer updateProperty:homeID:homeUserID:withOptions:completion:]
- GCC_except_table27
- GCC_except_table28
- GCC_except_table29
- GCC_except_table32
- GCC_except_table33
- _OBJC_IVAR_$_MSServer._accountsInterfaceDelegate
- _OBJC_IVAR_$_MediaServiceConfiguration._accountsImplementer
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_MSAccountsImplementer
- __OBJC_PROTOCOL_REFERENCE_$_MSAccountsImplementer
- ___43-[MediaServiceConfiguration initWithQueue:]_block_invoke.123
- ___43-[MediaServiceConfiguration initWithQueue:]_block_invoke.123.cold.1
- ___47-[MSServer listener:shouldAcceptNewConnection:]_block_invoke.129
- ___54-[MediaServiceConfiguration thirdPartyMusicAvailable:]_block_invoke.131
- ___79-[MediaServiceConfiguration(AppSelection) getSupportedThirdPartyMediaServices:]_block_invoke_3
- ___block_literal_global.144
CStrings:
+ "!"
+ "-[MSServer initWithMediator:]"
+ "-[MSServerMediator initWithAccountsDelegate:]"
+ "-[MediaServiceConfigurationMediator initWithServiceDelegate:]"
+ "@\"<MSProxyConnectionDelegate>\""
+ "@\"<MediaServiceUpdatedServiceInterfaceDelegate>\""
+ "@\"MSServerMediator\""
+ "@\"MediaServiceConfigurationMediator\""
+ "MSInternalServiceConnectionProtocol"
+ "MSProxyConnectionDelegate"
+ "MSServerMediator"
+ "MediaServiceConfigurationMediator"
+ "T@\"<MSProxyConnectionDelegate>\",W,N,V_connectionDelegate"
+ "T@\"<MediaServiceUpdatedServiceInterfaceDelegate>\",W,N,V_delegate"
+ "T@\"MSServerMediator\",&,N,V_mediator"
+ "T@\"MediaServiceConfigurationMediator\",&,N,V_mediator"
+ "_connectionDelegate"
+ "_mediator"
+ "connectionDelegate"
+ "got an error when working with the proxy: %@"
+ "initWithMediator:"
+ "initWithServiceDelegate:"
+ "mediator"
+ "setConnectionDelegate:"
+ "setMediator:"
- "\x01\x11"
- "\x11"
- "-[MSServer initWithAccountsDelegate:]"
- "1"
- "_accountsImplementer"

```
