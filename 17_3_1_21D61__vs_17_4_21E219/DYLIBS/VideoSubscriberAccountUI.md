## VideoSubscriberAccountUI

> `/System/Library/PrivateFrameworks/VideoSubscriberAccountUI.framework/VideoSubscriberAccountUI`

```diff

-511.20.5.0.0
-  __TEXT.__text: 0x556c4
-  __TEXT.__auth_stubs: 0x870
-  __TEXT.__objc_methlist: 0x6be0
+511.41.2.0.0
+  __TEXT.__text: 0x57494
+  __TEXT.__auth_stubs: 0x8b0
+  __TEXT.__objc_methlist: 0x6e30
   __TEXT.__const: 0x150
-  __TEXT.__cstring: 0x4fe3
-  __TEXT.__gcc_except_tab: 0xdec
-  __TEXT.__oslogstring: 0x337f
+  __TEXT.__cstring: 0x51cd
+  __TEXT.__gcc_except_tab: 0xda8
+  __TEXT.__oslogstring: 0x33bf
   __TEXT.__ustring: 0x10
-  __TEXT.__unwind_info: 0x14ec
-  __TEXT.__objc_classname: 0x13b0
-  __TEXT.__objc_methname: 0x1425c
-  __TEXT.__objc_methtype: 0x32bd
-  __TEXT.__objc_stubs: 0xda80
-  __DATA_CONST.__got: 0x3a0
-  __DATA_CONST.__const: 0x17b8
-  __DATA_CONST.__objc_classlist: 0x3f0
+  __TEXT.__unwind_info: 0x1578
+  __TEXT.__objc_classname: 0x13ca
+  __TEXT.__objc_methname: 0x148a2
+  __TEXT.__objc_methtype: 0x336b
+  __TEXT.__objc_stubs: 0xde20
+  __DATA_CONST.__got: 0x3b0
+  __DATA_CONST.__const: 0x1828
+  __DATA_CONST.__objc_classlist: 0x400
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x1f0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x148b0
-  __DATA_CONST.__objc_selrefs: 0x4400
+  __DATA_CONST.__objc_const: 0x14d70
+  __DATA_CONST.__objc_selrefs: 0x44e8
+  __DATA_CONST.__objc_protorefs: 0x30
+  __DATA_CONST.__objc_classrefs: 0x878
+  __DATA_CONST.__objc_superrefs: 0x318
   __DATA_CONST.__objc_arraydata: 0x60
-  __AUTH_CONST.__objc_const: 0x2bf0
-  __AUTH_CONST.__cfstring: 0x42e0
-  __AUTH_CONST.__const: 0x580
+  __AUTH_CONST.__objc_const: 0x2c80
+  __AUTH_CONST.__cfstring: 0x4480
+  __AUTH_CONST.__const: 0x560
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_floatobj: 0x30
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH_CONST.__auth_got: 0x448
-  __AUTH.__objc_data: 0x24e0
-  __DATA.__objc_protorefs: 0x30
-  __DATA.__objc_classrefs: 0x848
-  __DATA.__objc_superrefs: 0x308
-  __DATA.__objc_ivar: 0x948
+  __AUTH_CONST.__auth_got: 0x468
+  __AUTH.__objc_data: 0x2580
+  __DATA.__objc_ivar: 0x99c
   __DATA.__data: 0x17c0
   __DATA.__bss: 0xc0
   __DATA_DIRTY.__objc_data: 0x280

   - /System/Library/PrivateFrameworks/WatchListKit.framework/WatchListKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2634
-  Symbols:   9825
-  CStrings:  4841
+  Functions: 2695
+  Symbols:   10031
+  CStrings:  4924
 
Symbols:
+ -[UIViewController(VSAdditions) _forceViewReload]
+ -[UIViewController(VSAdditions) vs_updateNavigationItemAndForceViewReloadWithSearchController:]
+ -[UIViewController(VSAdditions) vs_updateNavigationItemAndForceViewReloadWithSearchController:rightBarButtonItem:]
+ -[VSAppDescription isVisionOSCompatible]
+ -[VSAppDescription setVisionOSCompatible:]
+ -[VSAppSettingsFacade appsOperationClass]
+ -[VSAppSettingsFacade initWithStorage:restrictionsCenter:accountChannelsCenter:appsOperationClass:]
+ -[VSAppSettingsFacade initWithStorage:restrictionsCenter:accountChannelsCenter:appsOperationClass:].cold.1
+ -[VSAppSettingsFacade setAppsOperationClass:]
+ -[VSAppSettingsFacade shouldShowMVPDAppInstallPrompt].cold.1
+ -[VSApplicationControllerResponse applicationUserAccounts]
+ -[VSApplicationControllerResponse setApplicationUserAccounts:]
+ -[VSApps .cxx_destruct]
+ -[VSApps availableApps]
+ -[VSApps description]
+ -[VSApps hasChannelApps]
+ -[VSApps hasUserChannelList]
+ -[VSApps init]
+ -[VSApps nonChannelApps]
+ -[VSApps setAvailableApps:]
+ -[VSApps setHasChannelApps:]
+ -[VSApps setHasUserChannelList:]
+ -[VSApps setNonChannelApps:]
+ -[VSApps setSubscribedApps:]
+ -[VSApps subscribedApps]
+ -[VSAppsOperation .cxx_destruct]
+ -[VSAppsOperation accountChannelsCenter]
+ -[VSAppsOperation accountChannels]
+ -[VSAppsOperation channelAppsFailable]
+ -[VSAppsOperation createAppsResult]
+ -[VSAppsOperation createAppsResult].cold.1
+ -[VSAppsOperation dispatchGroup]
+ -[VSAppsOperation executionDidBegin]
+ -[VSAppsOperation fetchChannelAppsWithCompletion:]
+ -[VSAppsOperation filterVisionOSCompatibleApps:]
+ -[VSAppsOperation identityProvider]
+ -[VSAppsOperation initWithIdentityProvider:]
+ -[VSAppsOperation initWithIdentityProvider:accountChannels:]
+ -[VSAppsOperation nonChannelApps]
+ -[VSAppsOperation result]
+ -[VSAppsOperation setAccountChannels:]
+ -[VSAppsOperation setAccountChannelsCenter:]
+ -[VSAppsOperation setChannelAppsFailable:]
+ -[VSAppsOperation setDispatchGroup:]
+ -[VSAppsOperation setIdentityProvider:]
+ -[VSAppsOperation setNonChannelApps:]
+ -[VSAppsOperation setResult:]
+ -[VSAutoAuthenticationViewController_iOS setTraitChangeRegistration:]
+ -[VSAutoAuthenticationViewController_iOS traitChangeRegistration]
+ -[VSCircularProgressView setTraitChangeRegistration:]
+ -[VSCircularProgressView traitChangeRegistration]
+ -[VSCredentialEntryViewController_iOS setTraitChangeRegistration:]
+ -[VSCredentialEntryViewController_iOS traitChangeRegistration]
+ -[VSErrorViewController setTraitChangeRegistration:]
+ -[VSErrorViewController traitChangeRegistration]
+ -[VSFooterMessageView setTraitChangeRegistration:]
+ -[VSFooterMessageView traitChangeRegistration]
+ -[VSIdentityProviderPickerViewController_iOS dealloc]
+ -[VSIdentityProviderPickerViewController_iOS setTraitChangeRegistration:]
+ -[VSIdentityProviderPickerViewController_iOS traitChangeRegistration]
+ -[VSSetupView setTraitChangeRegistration:]
+ -[VSSetupView traitChangeRegistration]
+ -[VSTwoFactorEntryViewController_iOS setTraitChangeRegistration:]
+ -[VSTwoFactorEntryViewController_iOS traitChangeRegistration]
+ GCC_except_table11
+ GCC_except_table17
+ GCC_except_table22
+ GCC_except_table4
+ _OBJC_CLASS_$_LSBundleRecord
+ _OBJC_CLASS_$_NSNull
+ _OBJC_CLASS_$_NSPredicate
+ _OBJC_CLASS_$_UITraitUserInterfaceStyle
+ _OBJC_CLASS_$_VSApplicationAppleSubscription
+ _OBJC_CLASS_$_VSApps
+ _OBJC_CLASS_$_VSAppsOperation
+ _OBJC_IVAR_$_VSAppDescription._visionOSCompatible
+ _OBJC_IVAR_$_VSAppSettingsFacade._appsOperationClass
+ _OBJC_IVAR_$_VSApplicationControllerResponse._applicationUserAccounts
+ _OBJC_IVAR_$_VSApps._availableApps
+ _OBJC_IVAR_$_VSApps._hasChannelApps
+ _OBJC_IVAR_$_VSApps._hasUserChannelList
+ _OBJC_IVAR_$_VSApps._nonChannelApps
+ _OBJC_IVAR_$_VSApps._subscribedApps
+ _OBJC_IVAR_$_VSAppsOperation._accountChannels
+ _OBJC_IVAR_$_VSAppsOperation._accountChannelsCenter
+ _OBJC_IVAR_$_VSAppsOperation._channelAppsFailable
+ _OBJC_IVAR_$_VSAppsOperation._dispatchGroup
+ _OBJC_IVAR_$_VSAppsOperation._identityProvider
+ _OBJC_IVAR_$_VSAppsOperation._nonChannelApps
+ _OBJC_IVAR_$_VSAppsOperation._result
+ _OBJC_IVAR_$_VSAutoAuthenticationViewController_iOS._traitChangeRegistration
+ _OBJC_IVAR_$_VSCircularProgressView._traitChangeRegistration
+ _OBJC_IVAR_$_VSCredentialEntryViewController_iOS._traitChangeRegistration
+ _OBJC_IVAR_$_VSErrorViewController._traitChangeRegistration
+ _OBJC_IVAR_$_VSFooterMessageView._traitChangeRegistration
+ _OBJC_IVAR_$_VSIdentityProviderPickerViewController_iOS._traitChangeRegistration
+ _OBJC_IVAR_$_VSSetupView._traitChangeRegistration
+ _OBJC_IVAR_$_VSTwoFactorEntryViewController_iOS._traitChangeRegistration
+ _OBJC_METACLASS_$_VSApps
+ _OBJC_METACLASS_$_VSAppsOperation
+ _VSMetricClickTargetIdentityProvider
+ _VSMetricPageSettingsPicker
+ __OBJC_$_INSTANCE_METHODS_VSApps
+ __OBJC_$_INSTANCE_METHODS_VSAppsOperation
+ __OBJC_$_INSTANCE_VARIABLES_VSApps
+ __OBJC_$_INSTANCE_VARIABLES_VSAppsOperation
+ __OBJC_$_PROP_LIST_VSApps
+ __OBJC_$_PROP_LIST_VSAppsOperation
+ __OBJC_$_PROP_LIST_VSWebAuthenticationViewController.212
+ __OBJC_CLASS_RO_$_VSApps
+ __OBJC_CLASS_RO_$_VSAppsOperation
+ __OBJC_METACLASS_RO_$_VSApps
+ __OBJC_METACLASS_RO_$_VSAppsOperation
+ ___102-[VSViewServiceViewController identityProviderPickerViewControllerDidPickAdditionalIdentityProviders:]_block_invoke.166
+ ___126-[VSViewServiceViewController _performRequestInternal:withID:identityProviders:accounts:currentStorefrontCode:allStorefronts:]_block_invoke.114
+ ___160-[VSViewControllerFactory viewControllerForPlaybackActivityReportingFromAppsWithBundleIDs:grantingVouchers:appleAccountName:identityProvider:completionHandler:]_block_invoke.132
+ ___34-[VSAppSettingsFacade _updateApps]_block_invoke.65
+ ___35-[VSAppsOperation createAppsResult]_block_invoke
+ ___35-[VSAppsOperation createAppsResult]_block_invoke_2
+ ___35-[VSAppsOperation createAppsResult]_block_invoke_2.cold.1
+ ___36-[VSAppsOperation executionDidBegin]_block_invoke
+ ___36-[VSAppsOperation executionDidBegin]_block_invoke_2
+ ___36-[VSAppsOperation executionDidBegin]_block_invoke_3
+ ___40-[VSCircularProgressView initWithFrame:]_block_invoke
+ ___40-[VSCircularProgressView initWithFrame:]_block_invoke_2
+ ___41-[VSFooterMessageView initWithSpecifier:]_block_invoke
+ ___44-[VSApplicationController _presentDocument:]_block_invoke.235
+ ___44-[VSApplicationController _presentDocument:]_block_invoke.235.cold.1
+ ___44-[VSApplicationController _presentDocument:]_block_invoke.235.cold.2
+ ___47-[VSLoadAllAppIconsOperation executionDidBegin]_block_invoke.11
+ ___48-[VSAppsOperation filterVisionOSCompatibleApps:]_block_invoke
+ ___48-[VSErrorViewController initWithNibName:bundle:]_block_invoke
+ ___48-[VSViewServiceViewController _didCancelRequest]_block_invoke.161
+ ___49-[VSTwoFactorEntryViewController_iOS viewDidLoad]_block_invoke
+ ___50-[VSAppsOperation fetchChannelAppsWithCompletion:]_block_invoke
+ ___55-[VSApplicationController _completeRequest:withResult:]_block_invoke.265
+ ___60-[VSIdentityProviderPickerViewController_iOS initWithStyle:]_block_invoke
+ ___61-[VSApplicationController transitionToWaitingForBootUrlState]_block_invoke.147
+ ___61-[VSApplicationController transitionToWaitingForBootUrlState]_block_invoke.147.cold.1
+ ___62-[VSCredentialEntryViewController_iOS initWithNibName:bundle:]_block_invoke_6
+ ___62-[VSViewServiceViewController _performRequest:withIdentifier:]_block_invoke.82
+ ___62-[VSViewServiceViewController _performRequest:withIdentifier:]_block_invoke.92
+ ___62-[VSViewServiceViewController _performRequest:withIdentifier:]_block_invoke_2.84
+ ___62-[VSViewServiceViewController _performRequest:withIdentifier:]_block_invoke_2.93
+ ___62-[VSViewServiceViewController _performRequest:withIdentifier:]_block_invoke_3.89
+ ___73-[VSApplicationController transitionToWaitingForBothLaunchCallbacksState]_block_invoke.170
+ ___75-[VSViewServiceViewController _performRequestWithIdentityProvider:account:]_block_invoke.135
+ ___75-[VSViewServiceViewController _performRequestWithIdentityProvider:account:]_block_invoke.143
+ ___75-[VSViewServiceViewController _performRequestWithIdentityProvider:account:]_block_invoke.143.cold.1
+ ___75-[VSViewServiceViewController _performRequestWithIdentityProvider:account:]_block_invoke_2.139
+ ___77-[VSApplicationController _applicationReadyWithSuccess:javascriptErrorValue:]_block_invoke.257
+ ___77-[VSApplicationController _applicationReadyWithSuccess:javascriptErrorValue:]_block_invoke.260
+ ___78-[VSViewServiceViewController identityProviderViewControllerDidFinishLoading:]_block_invoke.181
+ ___78-[VSViewServiceViewController identityProviderViewControllerDidFinishLoading:]_block_invoke.181.cold.1
+ ___82-[VSApplicationController showAuthenticationUserInterfaceWithAuthenticationToken:]_block_invoke.196
+ ___83-[VSIdentityProviderRequestManager applicationController:request:didFailWithError:]_block_invoke.162
+ ___83-[VSIdentityProviderRequestManager applicationController:request:didFailWithError:]_block_invoke.162.cold.1
+ ___84-[VSApplicationController _submitJavascriptRequest:forApplicationControllerRequest:]_block_invoke.252
+ ___86-[VSViewServiceViewController _didDetermineIdentityProvider:withPickerViewController:]_block_invoke.152
+ ___86-[VSViewServiceViewController _didDetermineIdentityProvider:withPickerViewController:]_block_invoke.153
+ ___86-[VSViewServiceViewController _didDetermineIdentityProvider:withPickerViewController:]_block_invoke_2.151
+ ___86-[VSViewServiceViewController _didDetermineIdentityProvider:withPickerViewController:]_block_invoke_2.155
+ ___90-[VSIdentityProviderRequestManager applicationController:request:didCompleteWithResponse:]_block_invoke.174
+ ___90-[VSIdentityProviderRequestManager applicationController:request:didCompleteWithResponse:]_block_invoke.176
+ ___90-[VSIdentityProviderRequestManager applicationController:request:didCompleteWithResponse:]_block_invoke.181
+ ___90-[VSIdentityProviderRequestManager applicationController:request:didCompleteWithResponse:]_block_invoke.183
+ ___90-[VSIdentityProviderRequestManager applicationController:request:didCompleteWithResponse:]_block_invoke.183.cold.1
+ ___90-[VSIdentityProviderRequestManager applicationController:request:didCompleteWithResponse:]_block_invoke_2.182
+ ___90-[VSViewServiceViewController identityProviderViewController:didFinishRequest:withResult:]_block_invoke.173.cold.1
+ ___90-[VSViewServiceViewController identityProviderViewController:didFinishRequest:withResult:]_block_invoke.174
+ ___99-[VSAppSettingsFacade initWithStorage:restrictionsCenter:accountChannelsCenter:appsOperationClass:]_block_invoke
+ ___block_descriptor_32_e43_B24?0"VSAppDescription"8"NSDictionary"16l
+ ___block_descriptor_40_e8_32w_e20_v16?0"VSFailable"8lw32l8
+ ___block_descriptor_40_e8_32w_e52_v24?0"<UITraitEnvironment>"8"UITraitCollection"16lw32l8
+ ___block_descriptor_48_e8_32bs40w_e5_v8?0ls32l8w40l8
+ ___block_descriptor_72_e8_32r40r48r56w64w_e5_v8?0lw56l8w64l8r32l8r40l8r48l8
+ ___block_descriptor_88_e8_32s40r48r56r64w72w80w_e5_v8?0lw64l8w72l8w80l8r40l8s32l8r48l8r56l8
+ ___block_literal_global.141
+ ___block_literal_global.145
+ ___block_literal_global.148
+ ___block_literal_global.157
+ ___block_literal_global.160
+ ___block_literal_global.163
+ ___block_literal_global.165
+ ___block_literal_global.168
+ ___block_literal_global.171
+ ___block_literal_global.183
+ ___block_literal_global.211
+ ___block_literal_global.263
+ ___block_literal_global.287
+ ___commonInit_block_invoke_2
+ __unnamed_array_storage.233
+ _dispatch_group_create
+ _dispatch_group_enter
+ _dispatch_group_leave
+ _dispatch_group_notify
+ _objc_msgSend$_deviceLanguage
+ _objc_msgSend$_forceViewReload
+ _objc_msgSend$addExecutionBlock:
+ _objc_msgSend$applicationUserAccounts
+ _objc_msgSend$applicationUserAccountsFromUserAccounts:
+ _objc_msgSend$appsOperationClass
+ _objc_msgSend$availableApps
+ _objc_msgSend$bundleRecordWithBundleIdentifier:allowPlaceholder:error:
+ _objc_msgSend$channelAppsFailable
+ _objc_msgSend$createAppsResult
+ _objc_msgSend$description
+ _objc_msgSend$dispatchGroup
+ _objc_msgSend$fetchChannelAppsWithCompletion:
+ _objc_msgSend$hasChannelApps
+ _objc_msgSend$hasUserChannelList
+ _objc_msgSend$initWithIdentityProvider:accountChannels:
+ _objc_msgSend$initWithStorage:restrictionsCenter:accountChannelsCenter:appsOperationClass:
+ _objc_msgSend$isVisionOSCompatible
+ _objc_msgSend$nonChannelApps
+ _objc_msgSend$null
+ _objc_msgSend$predicateWithBlock:
+ _objc_msgSend$recordClickEventWithPage:pageType:target:
+ _objc_msgSend$registerForTraitChanges:withHandler:
+ _objc_msgSend$setApplicationUserAccounts:
+ _objc_msgSend$setAvailableApps:
+ _objc_msgSend$setChannelAppsFailable:
+ _objc_msgSend$setHasUserChannelList:
+ _objc_msgSend$setNonChannelApps:
+ _objc_msgSend$setSubscribedApps:
+ _objc_msgSend$setTraitChangeRegistration:
+ _objc_msgSend$setVisionOSCompatible:
+ _objc_msgSend$subscribedApps
+ _objc_msgSend$traitChangeRegistration
+ _objc_msgSend$unregisterForTraitChanges:
+ _objc_msgSend$userAccountsFromApplicationUserAccounts:ForProviderID:allowedBundleIDs:
+ _objc_msgSend$vs_updateNavigationItemAndForceViewReloadWithSearchController:
+ _setDisplayNameIfAvailable
- -[VSAppSettingsFacade channelAppsOperationClass]
- -[VSAppSettingsFacade initWithStorage:restrictionsCenter:accountChannelsCenter:channelAppsOperationClass:]
- -[VSAppSettingsFacade initWithStorage:restrictionsCenter:accountChannelsCenter:channelAppsOperationClass:].cold.1
- -[VSAppSettingsFacade setChannelAppsOperationClass:]
- -[VSApplicationControllerResponse setUserAccounts:]
- -[VSApplicationControllerResponse userAccounts]
- -[VSAutoAuthenticationViewController_iOS traitCollectionDidChange:]
- -[VSCircularProgressView traitCollectionDidChange:]
- -[VSCredentialEntryViewController_iOS traitCollectionDidChange:]
- -[VSErrorViewController traitCollectionDidChange:]
- -[VSFooterMessageView traitCollectionDidChange:]
- -[VSIdentityProviderPickerViewController_iOS traitCollectionDidChange:]
- -[VSSetupView traitCollectionDidChange:]
- -[VSTwoFactorEntryViewController_iOS traitCollectionDidChange:]
- GCC_except_table25
- GCC_except_table86
- _OBJC_CLASS_$_LSBundleProxy
- _OBJC_IVAR_$_VSAppSettingsFacade._channelAppsOperationClass
- _OBJC_IVAR_$_VSApplicationControllerResponse._userAccounts
- __OBJC_$_PROP_LIST_VSWebAuthenticationViewController.211
- ___102-[VSViewServiceViewController identityProviderPickerViewControllerDidPickAdditionalIdentityProviders:]_block_invoke.165
- ___106-[VSAppSettingsFacade initWithStorage:restrictionsCenter:accountChannelsCenter:channelAppsOperationClass:]_block_invoke
- ___126-[VSViewServiceViewController _performRequestInternal:withID:identityProviders:accounts:currentStorefrontCode:allStorefronts:]_block_invoke.113
- ___160-[VSViewControllerFactory viewControllerForPlaybackActivityReportingFromAppsWithBundleIDs:grantingVouchers:appleAccountName:identityProvider:completionHandler:]_block_invoke.131
- ___34-[VSAppSettingsFacade _updateApps]_block_invoke.64
- ___34-[VSAppSettingsFacade _updateApps]_block_invoke.71
- ___34-[VSAppSettingsFacade _updateApps]_block_invoke.71.cold.1
- ___34-[VSAppSettingsFacade _updateApps]_block_invoke_3
- ___34-[VSAppSettingsFacade _updateApps]_block_invoke_4
- ___34-[VSAppSettingsFacade _updateApps]_block_invoke_4.cold.1
- ___44-[VSApplicationController _presentDocument:]_block_invoke.231
- ___44-[VSApplicationController _presentDocument:]_block_invoke.231.cold.1
- ___44-[VSApplicationController _presentDocument:]_block_invoke.231.cold.2
- ___47-[VSLoadAllAppIconsOperation executionDidBegin]_block_invoke.8
- ___48-[VSViewServiceViewController _didCancelRequest]_block_invoke.160
- ___51-[VSCircularProgressView traitCollectionDidChange:]_block_invoke
- ___55-[VSApplicationController _completeRequest:withResult:]_block_invoke.261
- ___61-[VSApplicationController transitionToWaitingForBootUrlState]_block_invoke.144
- ___61-[VSApplicationController transitionToWaitingForBootUrlState]_block_invoke.144.cold.1
- ___62-[VSViewServiceViewController _performRequest:withIdentifier:]_block_invoke.81
- ___62-[VSViewServiceViewController _performRequest:withIdentifier:]_block_invoke.91
- ___62-[VSViewServiceViewController _performRequest:withIdentifier:]_block_invoke_2.83
- ___62-[VSViewServiceViewController _performRequest:withIdentifier:]_block_invoke_2.92
- ___62-[VSViewServiceViewController _performRequest:withIdentifier:]_block_invoke_3.88
- ___73-[VSApplicationController transitionToWaitingForBothLaunchCallbacksState]_block_invoke.167
- ___75-[VSViewServiceViewController _performRequestWithIdentityProvider:account:]_block_invoke.133
- ___75-[VSViewServiceViewController _performRequestWithIdentityProvider:account:]_block_invoke.141
- ___75-[VSViewServiceViewController _performRequestWithIdentityProvider:account:]_block_invoke.141.cold.1
- ___75-[VSViewServiceViewController _performRequestWithIdentityProvider:account:]_block_invoke_2.137
- ___77-[VSApplicationController _applicationReadyWithSuccess:javascriptErrorValue:]_block_invoke.253
- ___77-[VSApplicationController _applicationReadyWithSuccess:javascriptErrorValue:]_block_invoke.256
- ___78-[VSViewServiceViewController identityProviderViewControllerDidFinishLoading:]_block_invoke.180
- ___78-[VSViewServiceViewController identityProviderViewControllerDidFinishLoading:]_block_invoke.180.cold.1
- ___82-[VSApplicationController showAuthenticationUserInterfaceWithAuthenticationToken:]_block_invoke.193
- ___83-[VSIdentityProviderRequestManager applicationController:request:didFailWithError:]_block_invoke.153
- ___83-[VSIdentityProviderRequestManager applicationController:request:didFailWithError:]_block_invoke.153.cold.1
- ___84-[VSApplicationController _submitJavascriptRequest:forApplicationControllerRequest:]_block_invoke.248
- ___86-[VSViewServiceViewController _didDetermineIdentityProvider:withPickerViewController:]_block_invoke.148
- ___86-[VSViewServiceViewController _didDetermineIdentityProvider:withPickerViewController:]_block_invoke.151
- ___86-[VSViewServiceViewController _didDetermineIdentityProvider:withPickerViewController:]_block_invoke_2.149
- ___86-[VSViewServiceViewController _didDetermineIdentityProvider:withPickerViewController:]_block_invoke_2.153
- ___90-[VSIdentityProviderRequestManager applicationController:request:didCompleteWithResponse:]_block_invoke.165
- ___90-[VSIdentityProviderRequestManager applicationController:request:didCompleteWithResponse:]_block_invoke.171
- ___90-[VSIdentityProviderRequestManager applicationController:request:didCompleteWithResponse:]_block_invoke.171.cold.1
- ___90-[VSIdentityProviderRequestManager applicationController:request:didCompleteWithResponse:]_block_invoke.175
- ___90-[VSIdentityProviderRequestManager applicationController:request:didCompleteWithResponse:]_block_invoke.180
- ___90-[VSIdentityProviderRequestManager applicationController:request:didCompleteWithResponse:]_block_invoke.182
- ___90-[VSIdentityProviderRequestManager applicationController:request:didCompleteWithResponse:]_block_invoke.182.cold.1
- ___90-[VSIdentityProviderRequestManager applicationController:request:didCompleteWithResponse:]_block_invoke_2.169
- ___90-[VSIdentityProviderRequestManager applicationController:request:didCompleteWithResponse:]_block_invoke_2.181
- ___90-[VSViewServiceViewController identityProviderViewController:didFinishRequest:withResult:]_block_invoke.172
- ___90-[VSViewServiceViewController identityProviderViewController:didFinishRequest:withResult:]_block_invoke.172.cold.1
- ___block_descriptor_40_e8_32r_e20_v16?0"VSFailable"8lr32l8
- ___block_descriptor_72_e8_32r40r48r56r64w_e5_v8?0lw64l8r32l8r40l8r48l8r56l8
- ___block_descriptor_88_e8_32s40r48r56r64r72w80w_e5_v8?0lw72l8w80l8r40l8s32l8r48l8r56l8r64l8
- ___block_literal_global.139
- ___block_literal_global.143
- ___block_literal_global.146
- ___block_literal_global.155
- ___block_literal_global.159
- ___block_literal_global.162
- ___block_literal_global.164
- ___block_literal_global.167
- ___block_literal_global.170
- ___block_literal_global.173
- ___block_literal_global.182
- ___block_literal_global.208
- ___block_literal_global.255
- ___block_literal_global.283
- ___block_literal_global.73
- __unnamed_array_storage.229
- _objc_msgSend$applicationIdentifier
- _objc_msgSend$bundleProxyForIdentifier:
- _objc_msgSend$channelAppsOperationClass
- _objc_msgSend$deviceLanguage
- _objc_msgSend$initWithStorage:restrictionsCenter:accountChannelsCenter:channelAppsOperationClass:
- _objc_msgSend$removeAllVouchers
- _objc_msgSend$userAccountsWithNativeUserAccounts:
CStrings:
+ "\a"
+ "\x11\x15E"
+ "\x15$\x12\x11"
+ "\x1b\x15"
+ "!\x1f\x05"
+ "\"$\x11"
+ "("
+ ","
+ "-[VSAppsOperation executionDidBegin]"
+ "/\x15"
+ "<%@ %p %@=%@, %@=%@, %@=%@, %@=%@, %@=%@>"
+ "@\"<UITraitChangeRegistration>\""
+ "@\"NSObject<OS_dispatch_group>\""
+ "@\"VSApps\""
+ "@\"VSFailable\""
+ "AppleSubscription"
+ "B24@?0@\"VSAppDescription\"8@\"NSDictionary\"16"
+ "No ChannelAppsOperation result -- returning no apps."
+ "T#,&,N,V_appsOperationClass"
+ "T@\"<UITraitChangeRegistration>\",&,N,V_traitChangeRegistration"
+ "T@\"NSArray\",&,N,V_availableApps"
+ "T@\"NSArray\",&,N,V_nonChannelApps"
+ "T@\"NSArray\",&,N,V_subscribedApps"
+ "T@\"NSArray\",C,N,V_applicationUserAccounts"
+ "T@\"NSNumber\",&,N,GisVisionOSCompatible,V_visionOSCompatible"
+ "T@\"NSObject<OS_dispatch_group>\",&,N,V_dispatchGroup"
+ "T@\"NSString\",?,C,N"
+ "T@\"NSString\",?,C,N,V_textContentType"
+ "T@\"NSString\",?,R,C"
+ "T@\"UISearchController\",?,R,N"
+ "T@\"UITextInputPasswordRules\",?,C,N"
+ "T@\"UIView\",?,R,N"
+ "T@\"VSApps\",&,N,V_result"
+ "T@\"VSFailable\",&,N,V_channelAppsFailable"
+ "T@,?,R,N"
+ "TB,?,N"
+ "TB,?,N,GisSecureTextEntry"
+ "TB,N,V_hasUserChannelList"
+ "The [appDescription bundleID] parameter must not be nil."
+ "The [response applicationUserAccounts] parameter must not be nil."
+ "The strongPresentationOperation parameter must not be nil."
+ "The textOrNil parameter must not be nil."
+ "Tq,?,N"
+ "Tq,?,N,V_autocapitalizationType"
+ "Tq,?,N,V_keyboardType"
+ "Tq,?,N,V_returnKeyType"
+ "T{CGSize=dd},?,R,N"
+ "VSApps"
+ "VSAppsOperation"
+ "_applicationUserAccounts"
+ "_appsOperationClass"
+ "_availableApps"
+ "_channelAppsFailable"
+ "_deviceLanguage"
+ "_dispatchGroup"
+ "_forceViewReload"
+ "_hasUserChannelList"
+ "_nonChannelApps"
+ "_subscribedApps"
+ "_traitChangeRegistration"
+ "_visionOSCompatible"
+ "addExecutionBlock:"
+ "applicationUserAccounts"
+ "applicationUserAccountsFromUserAccounts:"
+ "appsOperationClass"
+ "availableApps"
+ "bundleRecordWithBundleIdentifier:allowPlaceholder:error:"
+ "caretTransformForPosition:"
+ "channelAppsFailable"
+ "createAppsResult"
+ "dispatchGroup"
+ "fetchChannelAppsWithCompletion:"
+ "filterVisionOSCompatibleApps:"
+ "hasUserChannelList"
+ "initWithIdentityProvider:accountChannels:"
+ "initWithStorage:restrictionsCenter:accountChannelsCenter:appsOperationClass:"
+ "isVisionOSCompatible"
+ "isXROSCompatible"
+ "nonChannelApps"
+ "null"
+ "predicateWithBlock:"
+ "recordClickEventWithPage:pageType:target:"
+ "registerForTraitChanges:withHandler:"
+ "setApplicationUserAccounts:"
+ "setAppsOperationClass:"
+ "setAvailableApps:"
+ "setChannelAppsFailable:"
+ "setDispatchGroup:"
+ "setHasUserChannelList:"
+ "setNonChannelApps:"
+ "setSubscribedApps:"
+ "setTraitChangeRegistration:"
+ "setVisionOSCompatible:"
+ "shouldShowMVPDAppInstallPrompt - Error finding bundle record for bundleID %@ : %@"
+ "subscribedApps"
+ "traitChangeRegistration"
+ "unregisterForTraitChanges:"
+ "userAccountsFromApplicationUserAccounts:ForProviderID:allowedBundleIDs:"
+ "v24@?0@\"<UITraitEnvironment>\"8@\"UITraitCollection\"16"
+ "visionOSCompatible"
+ "vs_updateNavigationItemAndForceViewReloadWithSearchController:"
+ "vs_updateNavigationItemAndForceViewReloadWithSearchController:rightBarButtonItem:"
+ "{CGAffineTransform=dddddd}24@0:8@\"UITextPosition\"16"
+ "{CGAffineTransform=dddddd}24@0:8@16"
- "\x11\x15D"
- "\x15#\x13\x11"
- "\x1b\x14"
- "!\x1f\x04"
- "\"$"
- "%s: channelAppsResponse %@"
- "+"
- "/\x14"
- "Error fetching ChannelAppsOperation result."
- "T#,&,N,V_channelAppsOperationClass"
- "T@\"NSString\",C,N,V_textContentType"
- "T@\"UISearchController\",R,N"
- "T@\"UITextInputPasswordRules\",C,N"
- "T@\"UIView\",R,N"
- "T@,R,N"
- "TB,N,GisSecureTextEntry"
- "The [accountChannelsOrNil channelIDs] parameter must not be nil."
- "_channelAppsOperationClass"
- "applicationIdentifier"
- "bundleProxyForIdentifier:"
- "channelAppsOperationClass"
- "deviceLanguage"
- "initWithStorage:restrictionsCenter:accountChannelsCenter:channelAppsOperationClass:"
- "removeAllVouchers"
- "setChannelAppsOperationClass:"
- "traitCollectionDidChange:"
- "userAccountsWithNativeUserAccounts:"

```
