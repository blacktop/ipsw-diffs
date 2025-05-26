## VideoSubscriberAccount

> `/System/Library/Frameworks/VideoSubscriberAccount.framework/VideoSubscriberAccount`

```diff

-511.20.5.0.0
-  __TEXT.__text: 0xafb58
-  __TEXT.__auth_stubs: 0xf50
-  __TEXT.__objc_methlist: 0x7af4
-  __TEXT.__const: 0xe2f0
-  __TEXT.__cstring: 0x9976
-  __TEXT.__oslogstring: 0x59d0
-  __TEXT.__gcc_except_tab: 0x1224
+511.41.2.0.0
+  __TEXT.__text: 0xbbfdc
+  __TEXT.__auth_stubs: 0xef0
+  __TEXT.__objc_methlist: 0x7d84
+  __TEXT.__const: 0xfbe0
+  __TEXT.__cstring: 0x9c36
+  __TEXT.__oslogstring: 0x5a2f
+  __TEXT.__gcc_except_tab: 0x11fc
   __TEXT.__ustring: 0x178
-  __TEXT.__swift5_typeref: 0xe0
+  __TEXT.__swift5_typeref: 0xe2
+  __TEXT.__constg_swiftt: 0xdc
+  __TEXT.__swift5_reflstr: 0x63
+  __TEXT.__swift5_fieldmd: 0xd8
+  __TEXT.__swift5_proto: 0x34
+  __TEXT.__swift5_types: 0x18
   __TEXT.__swift5_capture: 0x20
-  __TEXT.__swift5_reflstr: 0x1a9
   __TEXT.__swift5_assocty: 0x48
-  __TEXT.__constg_swiftt: 0xcc
-  __TEXT.__swift5_fieldmd: 0x17c
-  __TEXT.__swift5_proto: 0x2c
-  __TEXT.__swift5_types: 0x14
-  __TEXT.__unwind_info: 0x23c0
-  __TEXT.__eh_frame: 0x178
-  __TEXT.__objc_classname: 0x12c7
-  __TEXT.__objc_methname: 0x122ba
-  __TEXT.__objc_methtype: 0x1b19
-  __TEXT.__objc_stubs: 0xbdc0
-  __DATA_CONST.__got: 0x360
-  __DATA_CONST.__const: 0x2980
-  __DATA_CONST.__objc_classlist: 0x510
+  __TEXT.__unwind_info: 0x32a4
+  __TEXT.__eh_frame: 0xe18
+  __TEXT.__objc_classname: 0x1334
+  __TEXT.__objc_methname: 0x1268c
+  __TEXT.__objc_methtype: 0x1be5
+  __TEXT.__objc_stubs: 0xbf60
+  __DATA_CONST.__got: 0x368
+  __DATA_CONST.__const: 0x24f0
+  __DATA_CONST.__objc_classlist: 0x530
   __DATA_CONST.__objc_catlist: 0x98
-  __DATA_CONST.__objc_protolist: 0x120
+  __DATA_CONST.__objc_protolist: 0x130
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x13660
-  __DATA_CONST.__objc_selrefs: 0x3f58
-  __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__cfstring: 0x80e0
+  __DATA_CONST.__objc_const: 0x13bb0
+  __DATA_CONST.__objc_selrefs: 0x3fd0
+  __DATA_CONST.__objc_protorefs: 0x50
+  __DATA_CONST.__objc_classrefs: 0x6c0
+  __DATA_CONST.__objc_superrefs: 0x3f0
+  __DATA_CONST.__objc_arraydata: 0x18
+  __AUTH_CONST.__cfstring: 0x82e0
   __AUTH_CONST.__objc_intobj: 0x1f8
-  __AUTH_CONST.__objc_const: 0x0
-  __AUTH_CONST.__const: 0x4bd0
-  __AUTH_CONST.__objc_arrayobj: 0x18
+  __AUTH_CONST.__objc_const: 0x240
+  __AUTH_CONST.__const: 0x5618
+  __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__auth_ptr: 0x18
-  __AUTH_CONST.__auth_got: 0x7b8
+  __AUTH_CONST.__auth_got: 0x788
+  __AUTH.__objc_data: 0x140
   __AUTH.__data: 0x98
-  __DATA.__objc_protorefs: 0x50
-  __DATA.__objc_classrefs: 0x6a0
-  __DATA.__objc_superrefs: 0x3d8
-  __DATA.__objc_ivar: 0x8f4
-  __DATA.__data: 0x1a78
-  __DATA.__bss: 0x800
-  __DATA.__common: 0x44
-  __DATA_DIRTY.__const: 0xd00
+  __DATA.__objc_ivar: 0x91c
+  __DATA.__data: 0x1b68
+  __DATA.__bss: 0x8c0
+  __DATA.__common: 0x60
+  __DATA_DIRTY.__const: 0xd18
   __DATA_DIRTY.__objc_const: 0x4410
   __DATA_DIRTY.__objc_data: 0x3250
-  __DATA_DIRTY.__data: 0xc0
-  __DATA_DIRTY.__bss: 0x190
+  __DATA_DIRTY.__bss: 0x170
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreData.framework/CoreData

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  Functions: 3704
-  Symbols:   11818
-  CStrings:  5265
+  Functions: 3823
+  Symbols:   11957
+  CStrings:  5325
 
Symbols:
+ +[VSAppleSubscription new]
+ +[VSAppleSubscription supportsSecureCoding]
+ +[VSAppleSubscriptionValueTransformer allowsReverseTransformation]
+ +[VSAppleSubscriptionValueTransformer transformedValueClass]
+ +[VSApplicationAppleSubscription appleSubscriptionsFromApplicationAppleSubscriptions:]
+ +[VSApplicationAppleSubscription applicationAppleSubscriptionsFromAppleSubscriptions:]
+ +[VSApplicationUserAccount applicationUserAccountsFromUserAccounts:]
+ +[VSApplicationUserAccount userAccountsFromApplicationUserAccounts:ForProviderID:allowedBundleIDs:]
+ +[VSJSAppleSubscription appleSubscriptionsFromJSAppleSubscriptions:]
+ +[VSJSAppleSubscription jsAppleSubscriptionsFromAppleSubscriptions:]
+ +[VSJSUserAccount jsUserAccountsFromUserAccounts:]
+ +[VSJSUserAccount userAccountsFromJSUserAccounts:]
+ -[NSDictionary(VSAdditions) vs_boolForKey:]
+ -[VSAppleSubscription .cxx_destruct]
+ -[VSAppleSubscription componentsForPrinting:]
+ -[VSAppleSubscription copyWithZone:]
+ -[VSAppleSubscription customerID]
+ -[VSAppleSubscription description]
+ -[VSAppleSubscription encodeWithCoder:]
+ -[VSAppleSubscription hash]
+ -[VSAppleSubscription initWithCoder:]
+ -[VSAppleSubscription initWithCustomerID:productCodes:]
+ -[VSAppleSubscription init]
+ -[VSAppleSubscription isEqual:]
+ -[VSAppleSubscription prettyPrint]
+ -[VSAppleSubscription productCodes]
+ -[VSAppleSubscription setCustomerID:]
+ -[VSAppleSubscription setProductCodes:]
+ -[VSAppleSubscriptionValueTransformer reverseTransformedValue:]
+ -[VSAppleSubscriptionValueTransformer reverseTransformedValue:].cold.1
+ -[VSAppleSubscriptionValueTransformer transformedValue:]
+ -[VSAppleSubscriptionValueTransformer transformedValue:].cold.1
+ -[VSApplicationAppleSubscription .cxx_destruct]
+ -[VSApplicationAppleSubscription appleSubscription]
+ -[VSApplicationAppleSubscription customerID]
+ -[VSApplicationAppleSubscription initWithAppleSubscription:]
+ -[VSApplicationAppleSubscription init]
+ -[VSApplicationAppleSubscription productCodes]
+ -[VSApplicationAppleSubscription setCustomerID:]
+ -[VSApplicationAppleSubscription setProductCodes:]
+ -[VSApplicationUserAccount appleSubscription]
+ -[VSApplicationUserAccount initWithUserAccount:]
+ -[VSApplicationUserAccount init]
+ -[VSApplicationUserAccount setAppleSubscription:]
+ -[VSApplicationUserAccount userAccountForProviderID:allowedBundleIDs:]
+ -[VSApplicationUserAccount userAccountForProviderID:allowedBundleIDs:].cold.1
+ -[VSDevice _stringForKey:copyAnswer:]
+ -[VSDevice deviceNameString]
+ -[VSDevice propertyFetchQueue]
+ -[VSDevice setDeviceNameString:]
+ -[VSDevice setPropertyFetchQueue:]
+ -[VSJSAppleSubscription .cxx_destruct]
+ -[VSJSAppleSubscription appleSubscription]
+ -[VSJSAppleSubscription customerID]
+ -[VSJSAppleSubscription initWithAppleSubscription:]
+ -[VSJSAppleSubscription init]
+ -[VSJSAppleSubscription productCodes]
+ -[VSJSAppleSubscription setCustomerID:]
+ -[VSJSAppleSubscription setProductCodes:]
+ -[VSJSUserAccount appleSubscription]
+ -[VSJSUserAccount setAppleSubscription:]
+ -[VSJSUserAccount userAccountForProviderID:allowedBundleIDs:]
+ -[VSJSUserAccount userAccountForProviderID:allowedBundleIDs:].cold.1
+ -[VSJSUserAccount userAccount]
+ -[VSJSUserAccount userAccount].cold.1
+ -[VSJSUserAccount userAccount].cold.2
+ -[VSPrivacyVoucherLockbox issueVouchersForAppDescriptions:providerID:]
+ -[VSUserAccount appleSubscription]
+ -[VSUserAccount copyWithZone:]
+ -[VSUserAccount hash]
+ -[VSUserAccount initWithAccountType:updateURL:sourceType:sourceIdentifier:]
+ -[VSUserAccount isEqual:]
+ -[VSUserAccount setAppleSubscription:]
+ -[VSUserAccountPersistentContainer configureDescriptonInMemory:]
+ -[VSUserAccountPersistentContainer initInMemory:]
+ -[VSUserAccountUpdateManager transitionToWaitingForAppStopState]
+ GCC_except_table46
+ GCC_except_table51
+ GCC_except_table52
+ _NSInMemoryStoreType
+ _OBJC_CLASS_$_LSBundleRecord
+ _OBJC_CLASS_$_MTStoreAMSBagDelegatePackage
+ _OBJC_CLASS_$_NSMutableCharacterSet
+ _OBJC_CLASS_$_VSAppleSubscription
+ _OBJC_CLASS_$_VSAppleSubscriptionValueTransformer
+ _OBJC_CLASS_$_VSApplicationAppleSubscription
+ _OBJC_CLASS_$_VSJSAppleSubscription
+ _OBJC_IVAR_$_VSAppleSubscription._customerID
+ _OBJC_IVAR_$_VSAppleSubscription._productCodes
+ _OBJC_IVAR_$_VSApplicationAppleSubscription._customerID
+ _OBJC_IVAR_$_VSApplicationAppleSubscription._productCodes
+ _OBJC_IVAR_$_VSApplicationUserAccount._appleSubscription
+ _OBJC_IVAR_$_VSDevice._deviceNameString
+ _OBJC_IVAR_$_VSDevice._propertyFetchQueue
+ _OBJC_IVAR_$_VSJSAppleSubscription._customerID
+ _OBJC_IVAR_$_VSJSAppleSubscription._productCodes
+ _OBJC_IVAR_$_VSJSUserAccount._appleSubscription
+ _OBJC_IVAR_$_VSUserAccount._appleSubscription
+ _OBJC_METACLASS_$_VSAppleSubscription
+ _OBJC_METACLASS_$_VSAppleSubscriptionValueTransformer
+ _OBJC_METACLASS_$_VSApplicationAppleSubscription
+ _OBJC_METACLASS_$_VSJSAppleSubscription
+ _VSAppleSubscriptionValueTransformerName
+ _VSDisplayNameForBundleWithIdentifier.cold.1
+ __OBJC_$_CLASS_METHODS_VSAppleSubscription
+ __OBJC_$_CLASS_METHODS_VSAppleSubscriptionValueTransformer
+ __OBJC_$_CLASS_METHODS_VSApplicationAppleSubscription
+ __OBJC_$_CLASS_METHODS_VSJSAppleSubscription
+ __OBJC_$_CLASS_PROP_LIST_VSAppleSubscription
+ __OBJC_$_INSTANCE_METHODS_VSAppleSubscription
+ __OBJC_$_INSTANCE_METHODS_VSAppleSubscriptionValueTransformer
+ __OBJC_$_INSTANCE_METHODS_VSApplicationAppleSubscription
+ __OBJC_$_INSTANCE_METHODS_VSJSAppleSubscription
+ __OBJC_$_INSTANCE_VARIABLES_VSAppleSubscription
+ __OBJC_$_INSTANCE_VARIABLES_VSApplicationAppleSubscription
+ __OBJC_$_INSTANCE_VARIABLES_VSJSAppleSubscription
+ __OBJC_$_PROP_LIST_VSAppleSubscription
+ __OBJC_$_PROP_LIST_VSApplicationAppleSubscription
+ __OBJC_$_PROP_LIST_VSApplicationAppleSubscription.34
+ __OBJC_$_PROP_LIST_VSApplicationUserAccount.114
+ __OBJC_$_PROP_LIST_VSJSAppleSubscription
+ __OBJC_$_PROP_LIST_VSJSAppleSubscription.29
+ __OBJC_$_PROP_LIST_VSJSUserAccount.110
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_VSApplicationAppleSubscription
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_VSJSAppleSubscription
+ __OBJC_$_PROTOCOL_METHOD_TYPES_VSApplicationAppleSubscription
+ __OBJC_$_PROTOCOL_METHOD_TYPES_VSJSAppleSubscription
+ __OBJC_$_PROTOCOL_REFS_VSApplicationAppleSubscription
+ __OBJC_$_PROTOCOL_REFS_VSJSAppleSubscription
+ __OBJC_CLASS_PROTOCOLS_$_VSAppleSubscription
+ __OBJC_CLASS_PROTOCOLS_$_VSApplicationAppleSubscription
+ __OBJC_CLASS_PROTOCOLS_$_VSJSAppleSubscription
+ __OBJC_CLASS_RO_$_VSAppleSubscription
+ __OBJC_CLASS_RO_$_VSAppleSubscriptionValueTransformer
+ __OBJC_CLASS_RO_$_VSApplicationAppleSubscription
+ __OBJC_CLASS_RO_$_VSJSAppleSubscription
+ __OBJC_LABEL_PROTOCOL_$_VSApplicationAppleSubscription
+ __OBJC_LABEL_PROTOCOL_$_VSJSAppleSubscription
+ __OBJC_METACLASS_RO_$_VSAppleSubscription
+ __OBJC_METACLASS_RO_$_VSAppleSubscriptionValueTransformer
+ __OBJC_METACLASS_RO_$_VSApplicationAppleSubscription
+ __OBJC_METACLASS_RO_$_VSJSAppleSubscription
+ __OBJC_PROTOCOL_$_VSApplicationAppleSubscription
+ __OBJC_PROTOCOL_$_VSJSAppleSubscription
+ ___22-[VSAccountStore init]_block_invoke.47
+ ___26-[VSDevice productVersion]_block_invoke
+ ___37-[VSDevice _stringForKey:copyAnswer:]_block_invoke
+ ___38-[VSDevice setIgnoreSetTopBoxProfile:]_block_invoke.138
+ ___38-[VSDevice setIgnoreSetTopBoxProfile:]_block_invoke.139
+ ___38-[VSDevice setIgnoreSetTopBoxProfile:]_block_invoke.139.cold.1
+ ___38-[VSDevice setIgnoreSetTopBoxProfile:]_block_invoke.143
+ ___38-[VSDevice setIgnoreSetTopBoxProfile:]_block_invoke.143.cold.1
+ ___40-[VSMetricsCenter accountStoreDidChange]_block_invoke.226
+ ___40-[VSMetricsCenter accountStoreDidChange]_block_invoke_2.227
+ ___40-[VSMetricsCenter accountStoreDidChange]_block_invoke_3.229
+ ___40-[VSMetricsCenter accountStoreDidChange]_block_invoke_3.229.cold.1
+ ___43-[VSAccountStore _updateCachedFirstAccount]_block_invoke.175
+ ___43-[VSAccountStore _updateCachedFirstAccount]_block_invoke.180
+ ___43-[VSAccountStore _updateCachedFirstAccount]_block_invoke.180.cold.1
+ ___43-[VSAccountStore _updateCachedFirstAccount]_block_invoke.182
+ ___43-[VSAccountStore _updateCachedFirstAccount]_block_invoke_2.177
+ ___43-[VSAccountStore _updateCachedFirstAccount]_block_invoke_2.177.cold.1
+ ___65-[VSAccountSerializationCenter importData:withCompletionHandler:]_block_invoke.82
+ ___65-[VSAccountSerializationCenter importData:withCompletionHandler:]_block_invoke.82.cold.1
+ ___67-[VSAccountManager checkAccessStatusWithOptions:completionHandler:]_block_invoke.78
+ ___67-[VSAccountManager checkAccessStatusWithOptions:completionHandler:]_block_invoke.85
+ ___67-[VSAccountManager checkAccessStatusWithOptions:completionHandler:]_block_invoke_2.79
+ ___68-[VSAccountManager enqueueAccountMetadataRequest:completionHandler:]_block_invoke.93
+ ___68-[VSAccountManager enqueueAccountMetadataRequest:completionHandler:]_block_invoke.95
+ ___80-[VSSubscriptionRegistry fetchActiveSubscriptionsWithOptions:completionHandler:]_block_invoke_2.cold.3
+ ___81-[VSAccountStore _fetchAccountsSimulatingExpiredToken:forProviderIDs:completion:]_block_invoke.100
+ ___81-[VSAccountStore _fetchAccountsSimulatingExpiredToken:forProviderIDs:completion:]_block_invoke.111
+ ___81-[VSAccountStore _fetchAccountsSimulatingExpiredToken:forProviderIDs:completion:]_block_invoke.120
+ ___81-[VSAccountStore _fetchAccountsSimulatingExpiredToken:forProviderIDs:completion:]_block_invoke.93
+ ___81-[VSAccountStore _fetchAccountsSimulatingExpiredToken:forProviderIDs:completion:]_block_invoke_2.98
+ ___block_descriptor_64_e8_32s40r_e5_v8?0lr40l8s32l8
+ ___block_literal_global.137
+ ___block_literal_global.141
+ ___block_literal_global.145
+ ___block_literal_global.179
+ ___block_literal_global.197
+ ___block_literal_global.225
+ ___block_literal_global.231
+ ___block_literal_global.236
+ ___block_literal_global.238
+ ___block_literal_global.240
+ ___block_literal_global.242
+ ___block_literal_global.55
+ ___swift_memcpy16_8
+ _associated conformance 22VideoSubscriberAccount19VSAppleSubscriptionVSHAASQ
+ _block_copy_helper.12
+ _block_descriptor.14
+ _block_destroy_helper.13
+ _malloc
+ _memmove
+ _objc_msgSend$appleSubscription
+ _objc_msgSend$availableApps
+ _objc_msgSend$bundleRecordWithBundleIdentifier:allowPlaceholder:error:
+ _objc_msgSend$configureDescriptonInMemory:
+ _objc_msgSend$customerID
+ _objc_msgSend$deviceNameString
+ _objc_msgSend$enumeratorWithOptions:
+ _objc_msgSend$hasUserChannelList
+ _objc_msgSend$initWithAccountType:updateURL:sourceType:sourceIdentifier:
+ _objc_msgSend$initWithAppleSubscription:
+ _objc_msgSend$initWithCustomerID:productCodes:
+ _objc_msgSend$isEqualToArray:
+ _objc_msgSend$issueVouchersForAppDescriptions:providerID:
+ _objc_msgSend$jsUserAccountsFromUserAccounts:
+ _objc_msgSend$mergedModelFromBundles:
+ _objc_msgSend$nonChannelApps
+ _objc_msgSend$persistentStoreDescriptions
+ _objc_msgSend$productCodes
+ _objc_msgSend$propertyFetchQueue
+ _objc_msgSend$serialNumberString
+ _objc_msgSend$setAppleSubscription:
+ _objc_msgSend$setCustomerID:
+ _objc_msgSend$setDeviceNameString:
+ _objc_msgSend$setProductCodes:
+ _objc_msgSend$setSerialNumberString:
+ _objc_msgSend$subscribedApps
+ _objc_msgSend$unarchivedObjectOfClasses:fromData:error:
+ _objc_msgSend$userAccountForProviderID:allowedBundleIDs:
+ _objc_msgSend$userAccountsFromJSUserAccounts:
+ _objc_msgSend$vs_numberForKey:
+ _swift_dynamicCast
+ _swift_unknownObjectRelease
+ _symbolic So13VSUserAccountC
+ _symbolic So19VSAppleSubscriptionC
+ _symbolic _____ 22VideoSubscriberAccount19VSAppleSubscriptionV
+ _symbolic _____Sg 22VideoSubscriberAccount19VSAppleSubscriptionV
- +[NSBundle(VSAdditions) vs_bundleForClassWithName:]
- +[NSDate(VSAdditions) vs_dateAccessQueue]
- +[NSDate(VSAdditions) vs_recordedDates]
- +[NSDate(VSAdditions) vs_startRecordingDates]
- +[NSDate(VSAdditions) vs_stopRecordingDates]
- +[VSApplicationUserAccount nativeUserAccountsForJSUserAccounts:ForProviderID:allowedBundleIDs:]
- +[VSApplicationUserAccount userAccountsWithNativeUserAccounts:]
- +[VSDevice _stringForKey:copyAnswer:]
- +[VSJSUserAccount nativeUserAccountsForJSUserAccounts:]
- +[VSJSUserAccount userAccountsWithNativeUserAccounts:]
- -[VSApplicationUserAccount initWithUserAcount:]
- -[VSApplicationUserAccount nativeUserAccountForProviderID:allowedBundleIDs:]
- -[VSApplicationUserAccount nativeUserAccountForProviderID:allowedBundleIDs:].cold.1
- -[VSIdentityProviderUserAccountUpdateOperation _userAccountsForJSUserAccounts]
- -[VSJSUserAccount nativeUserAccount]
- -[VSJSUserAccount nativeUserAccount].cold.1
- -[VSJSUserAccount nativeUserAccount].cold.2
- -[VSUserAccount initWithAccountType:updateURL:sourceType:sourceIdentifier:deviceIdentifier:]
- -[VSUserAccount initWithCoder:].cold.2
- -[VSUserAccount sourceTypeForFiltering]
- -[VSUserAccountPersistentContainer init]
- -[VSVersionMapping mapping]
- -[VSVersionMapping setMapping:]
- GCC_except_table37
- GCC_except_table48
- GCC_except_table49
- GCC_except_table53
- _OBJC_CLASS_$_LSBundleProxy
- _OBJC_CLASS_$_MTUIKitStoreAMSBagDelegatePackage
- _OBJC_IVAR_$_VSVersionMapping._mapping
- _OSAtomicCompareAndSwapIntBarrier
- _SimulateCrash
- _VSMetricFlexibleFieldSuccess
- __OBJC_$_PROP_LIST_VSApplicationUserAccount.103
- __OBJC_$_PROP_LIST_VSJSUserAccount.97
- ___22-[VSAccountStore init]_block_invoke.46
- ___22-[VSAccountStore init]_block_invoke.48
- ___22-[VSAccountStore init]_block_invoke_3
- ___24-[VSDevice serialNumber]_block_invoke.149
- ___24-[VSDevice serialNumber]_block_invoke_2
- ___37+[NSDate(VSAdditions) vs_currentDate]_block_invoke
- ___38-[VSDevice setIgnoreSetTopBoxProfile:]_block_invoke.135
- ___38-[VSDevice setIgnoreSetTopBoxProfile:]_block_invoke.136
- ___38-[VSDevice setIgnoreSetTopBoxProfile:]_block_invoke.136.cold.1
- ___38-[VSDevice setIgnoreSetTopBoxProfile:]_block_invoke.140
- ___38-[VSDevice setIgnoreSetTopBoxProfile:]_block_invoke.140.cold.1
- ___39+[NSDate(VSAdditions) vs_recordedDates]_block_invoke
- ___40-[VSMetricsCenter accountStoreDidChange]_block_invoke.229
- ___40-[VSMetricsCenter accountStoreDidChange]_block_invoke_2.230
- ___40-[VSMetricsCenter accountStoreDidChange]_block_invoke_3.232
- ___40-[VSMetricsCenter accountStoreDidChange]_block_invoke_3.232.cold.1
- ___41+[NSDate(VSAdditions) vs_dateAccessQueue]_block_invoke
- ___43-[VSAccountStore _updateCachedFirstAccount]_block_invoke.176
- ___43-[VSAccountStore _updateCachedFirstAccount]_block_invoke.181
- ___43-[VSAccountStore _updateCachedFirstAccount]_block_invoke.181.cold.1
- ___43-[VSAccountStore _updateCachedFirstAccount]_block_invoke_2.178
- ___43-[VSAccountStore _updateCachedFirstAccount]_block_invoke_2.178.cold.1
- ___44+[NSDate(VSAdditions) vs_stopRecordingDates]_block_invoke
- ___45+[NSDate(VSAdditions) vs_startRecordingDates]_block_invoke
- ___51+[NSBundle(VSAdditions) vs_bundleForClassWithName:]_block_invoke
- ___52-[VSAppInstallationInfoCenter installedAppBundleIDs]_block_invoke
- ___65-[VSAccountSerializationCenter importData:withCompletionHandler:]_block_invoke.81
- ___65-[VSAccountSerializationCenter importData:withCompletionHandler:]_block_invoke.81.cold.1
- ___67-[VSAccountManager checkAccessStatusWithOptions:completionHandler:]_block_invoke.77
- ___67-[VSAccountManager checkAccessStatusWithOptions:completionHandler:]_block_invoke.83
- ___67-[VSAccountManager checkAccessStatusWithOptions:completionHandler:]_block_invoke_2.78
- ___68-[VSAccountManager enqueueAccountMetadataRequest:completionHandler:]_block_invoke.92
- ___68-[VSAccountManager enqueueAccountMetadataRequest:completionHandler:]_block_invoke.94
- ___74-[VSAccountStore remoteNotifier:didReceiveRemoteNotificationWithUserInfo:]_block_invoke_2
- ___78-[VSIdentityProviderUserAccountUpdateOperation _userAccountsForJSUserAccounts]_block_invoke
- ___81-[VSAccountStore _fetchAccountsSimulatingExpiredToken:forProviderIDs:completion:]_block_invoke.101
- ___81-[VSAccountStore _fetchAccountsSimulatingExpiredToken:forProviderIDs:completion:]_block_invoke.113
- ___81-[VSAccountStore _fetchAccountsSimulatingExpiredToken:forProviderIDs:completion:]_block_invoke.121
- ___81-[VSAccountStore _fetchAccountsSimulatingExpiredToken:forProviderIDs:completion:]_block_invoke.94
- ___81-[VSAccountStore _fetchAccountsSimulatingExpiredToken:forProviderIDs:completion:]_block_invoke_2.99
- ___block_descriptor_40_e8_32s_e15_"NSString"8?0ls32l8
- ___block_descriptor_40_e8_32s_e27_v24?0"LSBundleProxy"8^B16ls32l8
- ___block_descriptor_48_e8_32r_e5_v8?0lr32l8
- ___block_literal_global.116
- ___block_literal_global.134
- ___block_literal_global.138
- ___block_literal_global.142
- ___block_literal_global.180
- ___block_literal_global.200
- ___block_literal_global.228
- ___block_literal_global.234
- ___block_literal_global.239
- ___block_literal_global.241
- ___block_literal_global.243
- ___block_literal_global.245
- ___block_literal_global.5
- ___block_literal_global.8
- _block_copy_helper.11
- _block_descriptor.13
- _block_destroy_helper.12
- _getpid
- _isRecording
- _name.__vs_lazy_init_predicate
- _name.__vs_lazy_init_variable
- _objc_msgSend$URLForResource:withExtension:
- _objc_msgSend$_allowedBundleIDs
- _objc_msgSend$_userAccountsForJSUserAccounts
- _objc_msgSend$addOperations:waitUntilFinished:
- _objc_msgSend$bundleProxyForIdentifier:
- _objc_msgSend$enumerateBundlesOfType:block:
- _objc_msgSend$initWithAccountType:updateURL:sourceType:sourceIdentifier:deviceIdentifier:
- _objc_msgSend$initWithContentsOfURL:
- _objc_msgSend$initWithUserAcount:
- _objc_msgSend$nativeUserAccount
- _objc_msgSend$nativeUserAccountForProviderID:allowedBundleIDs:
- _objc_msgSend$nativeUserAccountsForJSUserAccounts:
- _objc_msgSend$persistentStoreDescriptionWithURL:
- _objc_msgSend$serialNumber
- _objc_msgSend$userAccountsWithNativeUserAccounts:
- _objc_msgSend$vs_dateAccessQueue
- _objc_msgSend$vs_recordedDates
- _serialNumber.__vs_lazy_init_predicate
- _serialNumber.__vs_lazy_init_variable
- _swift_arrayInitWithTakeBackToFront
- _swift_arrayInitWithTakeFrontToBack
- _swift_getEnumTagSinglePayloadGeneric
- _swift_getSingletonMetadata
- _swift_initStructMetadata
- _swift_storeEnumTagSinglePayloadGeneric
- _symbolic SS
- _symbolic SSSg
- _symbolic SaySSGSg
- _symbolic Sb
- _symbolic Su
- _symbolic _____ 10Foundation4DateV
- _symbolic _____Sg 22VideoSubscriberAccount06VSUserC0V
- _symbolic _____Sg_ABt 10Foundation3URLV
- _symbolic _____Sg_ABt 10Foundation4DateV
- _vs_bundleForClassWithName:.__vs_lazy_init_predicate
- _vs_bundleForClassWithName:.__vs_lazy_init_variable
- _vs_dateAccessQueue.__vs_lazy_init_predicate
- _vs_dateAccessQueue.__vs_lazy_init_variable
- _vs_recordedDates.__vs_lazy_init_predicate
- _vs_recordedDates.__vs_lazy_init_variable
CStrings:
+ "\x06\x16"
+ "\x13\x14\x13\x13"
+ "#\x16"
+ "/dev/null"
+ "@\"VSAppleSubscription\""
+ "@\"VSApplicationAppleSubscription\""
+ "@\"VSApplicationAppleSubscription\"16@0:8"
+ "@\"VSJSAppleSubscription\""
+ "@\"VSJSAppleSubscription\"16@0:8"
+ "@48@0:8q16@24q32@40"
+ "Ai"
+ "AppleSubscription"
+ "At least one product code is required."
+ "Error archiving VSAppleSubscription value: %@"
+ "Error finding bundle record for bundleID %@ : %@"
+ "Error unarchiving VSAppleSubscription value: %@"
+ "Invalid product code was provided."
+ "T@\"NSArray\",&,N"
+ "T@\"NSArray\",&,N,V_productCodes"
+ "T@\"NSArray\",C,N,V_productCodes"
+ "T@\"NSOperationQueue\",&,N,V_propertyFetchQueue"
+ "T@\"NSString\",&,N,V_customerID"
+ "T@\"NSString\",&,V_deviceNameString"
+ "T@\"NSString\",&,V_productVersionString"
+ "T@\"NSString\",&,V_serialNumberString"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",C,N,V_customerID"
+ "T@\"VSAppleSubscription\",&,D,N"
+ "T@\"VSAppleSubscription\",&,N,V_appleSubscription"
+ "T@\"VSApplicationAppleSubscription\",&,N"
+ "T@\"VSApplicationAppleSubscription\",&,N,V_appleSubscription"
+ "T@\"VSJSAppleSubscription\",&,N"
+ "T@\"VSJSAppleSubscription\",&,N,V_appleSubscription"
+ "The [[self persistentStoreDescriptions] firstObject] parameter must not be nil."
+ "The [coder decodeArrayOfObjectsOfClass:[NSString class] forKey:kVSAppleSubscriptionTypeProductCodesKey] parameter must not be nil."
+ "The [coder decodeObjectOfClass:[NSString class] forKey:kVSAppleSubscriptionTypeCustomerIDKey] parameter must not be nil."
+ "The [self customerID] parameter must not be nil."
+ "The [self productCodes] parameter must not be nil."
+ "The [userAccount appleSubscription] parameter must not be nil."
+ "Unexpectedly, object was %@, instead of VSAppleSubscription."
+ "Unexpectedly, object was %@, instead of VSUserAccount."
+ "VSAppleSubscription"
+ "VSAppleSubscriptionValueTransformer"
+ "VSApplicationAppleSubscription"
+ "VSDevice - PropertyFetch"
+ "VSJSAppleSubscription"
+ "_appleSubscription"
+ "_customerID"
+ "_deviceNameString"
+ "_productCodes"
+ "_propertyFetchQueue"
+ "appleSubscription"
+ "appleSubscriptionsFromApplicationAppleSubscriptions:"
+ "appleSubscriptionsFromJSAppleSubscriptions:"
+ "applicationAppleSubscriptionsFromAppleSubscriptions:"
+ "applicationUserAccountsFromUserAccounts:"
+ "availableApps"
+ "bundleRecordWithBundleIdentifier:allowPlaceholder:error:"
+ "configureDescriptonInMemory:"
+ "customerID"
+ "customerID is required."
+ "deviceNameString"
+ "enumeratorWithOptions:"
+ "hasUserChannelList"
+ "initInMemory:"
+ "initWithAccountType:updateURL:sourceType:sourceIdentifier:"
+ "initWithAppleSubscription:"
+ "initWithCustomerID:productCodes:"
+ "isEqualToArray:"
+ "issueVouchersForAppDescriptions:providerID:"
+ "jsAppleSubscriptionsFromAppleSubscriptions:"
+ "jsUserAccountsFromUserAccounts:"
+ "mergedModelFromBundles:"
+ "nonChannelApps"
+ "persistentStoreDescriptions"
+ "productCodes"
+ "propertyFetchQueue"
+ "sampleCID"
+ "samplePID"
+ "setAppleSubscription:"
+ "setCustomerID:"
+ "setDeviceNameString:"
+ "setProductCodes:"
+ "setPropertyFetchQueue:"
+ "subscribedApps"
+ "transitionToWaitingForAppStopState"
+ "unarchivedObjectOfClasses:fromData:error:"
+ "userAccountForProviderID:allowedBundleIDs:"
+ "userAccountsFromApplicationUserAccounts:ForProviderID:allowedBundleIDs:"
+ "userAccountsFromJSUserAccounts:"
+ "v24@0:8@\"VSApplicationAppleSubscription\"16"
+ "v24@0:8@\"VSJSAppleSubscription\"16"
+ "vs_boolForKey:"
- "\x04\x16"
- "\x13\x14\x12\x13"
- "#\x15"
- "@\"NSString\"8@?0"
- "@24@0:8@\"VSUserAccount\"16"
- "@56@0:8q16@24q32@40@48"
- "Every VSUserAccount should have a deviceIdentifier"
- "T@\"NSDictionary\",&,N,V_mapping"
- "T@\"NSString\",&,N,V_productVersionString"
- "T@\"NSString\",&,N,V_serialNumberString"
- "The copiedDates parameter must not be nil."
- "The productVersion parameter must not be nil."
- "URLForResource:withExtension:"
- "_mapping"
- "_userAccountsForJSUserAccounts"
- "addOperations:waitUntilFinished:"
- "bundleProxyForIdentifier:"
- "enumerateBundlesOfType:block:"
- "initWithAccountType:updateURL:sourceType:sourceIdentifier:deviceIdentifier:"
- "initWithContentsOfURL:"
- "initWithUserAcount:"
- "mapping"
- "momd"
- "nativeUserAccount"
- "nativeUserAccountForProviderID:allowedBundleIDs:"
- "nativeUserAccountsForJSUserAccounts:"
- "nativeUserAccountsForJSUserAccounts:ForProviderID:allowedBundleIDs:"
- "persistentStoreDescriptionWithURL:"
- "setMapping:"
- "sourceTypeForFiltering"
- "success"
- "userAccountsWithNativeUserAccounts:"
- "v24@?0@\"LSBundleProxy\"8^B16"
- "vs_bundleForClassWithName:"
- "vs_dateAccessQueue"
- "vs_recordedDates"
- "vs_startRecordingDates"
- "vs_stopRecordingDates"

```
