## iCloudQuota

> `/System/Library/PrivateFrameworks/iCloudQuota.framework/iCloudQuota`

```diff

-301.23.3.2.0
-  __TEXT.__text: 0x785e4
-  __TEXT.__auth_stubs: 0x1680
-  __TEXT.__objc_methlist: 0x581c
-  __TEXT.__const: 0x1288
-  __TEXT.__cstring: 0x6771
-  __TEXT.__oslogstring: 0x8129
-  __TEXT.__gcc_except_tab: 0x6b8
-  __TEXT.__dlopen_cstrs: 0x2f1
+301.23.4.7.0
+  __TEXT.__text: 0x7e534
+  __TEXT.__auth_stubs: 0x15f0
+  __TEXT.__objc_methlist: 0x5924
+  __TEXT.__const: 0x12c8
+  __TEXT.__cstring: 0x6390
+  __TEXT.__oslogstring: 0x8629
+  __TEXT.__gcc_except_tab: 0x740
+  __TEXT.__dlopen_cstrs: 0x3b5
   __TEXT.__ustring: 0x152
-  __TEXT.__swift5_typeref: 0x712
+  __TEXT.__swift5_typeref: 0x724
   __TEXT.__swift5_capture: 0x2f8
   __TEXT.__swift5_reflstr: 0x2c1
   __TEXT.__swift5_assocty: 0xa8
   __TEXT.__constg_swiftt: 0x6b0
   __TEXT.__swift5_fieldmd: 0x348
-  __TEXT.__swift5_proto: 0xa4
+  __TEXT.__swift5_proto: 0xa8
   __TEXT.__swift5_types: 0x50
   __TEXT.__swift_as_entry: 0x60
   __TEXT.__swift_as_ret: 0x68
   __TEXT.__swift5_protos: 0x14
   __TEXT.__swift5_builtin: 0x28
-  __TEXT.__unwind_info: 0x1cd0
-  __TEXT.__eh_frame: 0x11d8
-  __TEXT.__objc_classname: 0xa79
-  __TEXT.__objc_methname: 0xd560
-  __TEXT.__objc_methtype: 0xfd7
-  __TEXT.__objc_stubs: 0x8fa0
-  __DATA_CONST.__got: 0x7e8
-  __DATA_CONST.__const: 0x1d00
-  __DATA_CONST.__objc_classlist: 0x388
+  __TEXT.__unwind_info: 0x21d8
+  __TEXT.__eh_frame: 0x1158
+  __TEXT.__objc_classname: 0xc67
+  __TEXT.__objc_methname: 0xdc80
+  __TEXT.__objc_methtype: 0x121d
+  __TEXT.__objc_stubs: 0x9620
+  __DATA_CONST.__got: 0x808
+  __DATA_CONST.__const: 0x1de8
+  __DATA_CONST.__objc_classlist: 0x398
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2f40
+  __DATA_CONST.__objc_selrefs: 0x3028
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x280
-  __DATA_CONST.__objc_arraydata: 0x2328
-  __AUTH_CONST.__auth_got: 0xb50
-  __AUTH_CONST.__const: 0x13c8
-  __AUTH_CONST.__cfstring: 0x7360
-  __AUTH_CONST.__objc_const: 0xb010
-  __AUTH_CONST.__objc_intobj: 0xaf8
+  __DATA_CONST.__objc_superrefs: 0x290
+  __DATA_CONST.__objc_arraydata: 0x2338
+  __AUTH_CONST.__auth_got: 0xb08
+  __AUTH_CONST.__const: 0x1448
+  __AUTH_CONST.__cfstring: 0x7600
+  __AUTH_CONST.__objc_const: 0xb220
+  __AUTH_CONST.__objc_intobj: 0xb10
   __AUTH_CONST.__objc_dictobj: 0x15e0
   __AUTH_CONST.__objc_arrayobj: 0x588
-  __AUTH.__objc_data: 0x14b0
+  __AUTH.__objc_data: 0x1500
   __AUTH.__data: 0x460
-  __DATA.__objc_ivar: 0x680
-  __DATA.__data: 0x5c8
-  __DATA.__bss: 0x1510
+  __DATA.__objc_ivar: 0x69c
+  __DATA.__data: 0x578
+  __DATA.__bss: 0x15b0
   __DATA.__common: 0x10
-  __DATA_DIRTY.__objc_data: 0x1080
-  __DATA_DIRTY.__data: 0x228
-  __DATA_DIRTY.__bss: 0x248
+  __DATA_DIRTY.__objc_data: 0x10d0
+  __DATA_DIRTY.__data: 0x278
+  __DATA_DIRTY.__bss: 0x268
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 6965B747-9BEC-353B-83A7-13B21A59395E
-  Functions: 2898
-  Symbols:   8049
-  CStrings:  5179
+  UUID: B7E8D420-B993-3181-9FA5-F1F7D2F330F9
+  Functions: 2951
+  Symbols:   8286
+  CStrings:  5270
 
Symbols:
+ +[ICQAMSEngagementPresenter sharedPresenter]
+ +[ICQAMSEngagementPresenter sharedPresenter].cold.1
+ +[ICQAMSFlowManager sharedManager]
+ +[ICQAMSFlowManager sharedManager].cold.1
+ +[ICQDaemonOfferConditions getPhotoLibraryQuotaSize]
+ +[ICQDaemonOfferConditions getPhotoLibraryQuotaSize].cold.1
+ +[ICQDaemonOfferConditions getPhotoLibraryQuotaSize].cold.2
+ +[_ICQPhotosInfo canUsePhotoLibrary]
+ +[_ICQPhotosInfo getInfoWithCompletion:].cold.1
+ -[ICQAMSEngagementPresenter .cxx_destruct]
+ -[ICQAMSEngagementPresenter _clientDataFromActParams:]
+ -[ICQAMSEngagementPresenter _launchAMSEngagementWithURL:params:originatorBundleId:bag:completion:]
+ -[ICQAMSEngagementPresenter _metricsOverlayFromActParams:account:]
+ -[ICQAMSEngagementPresenter _performPostPurchaseTeardown]
+ -[ICQAMSEngagementPresenter clearPendingEngagement]
+ -[ICQAMSEngagementPresenter init]
+ -[ICQAMSEngagementPresenter performAMSEngagementWithParameters:completion:]
+ -[ICQAMSEngagementPresenter performAMSEngagementWithParameters:completion:].cold.1
+ -[ICQAMSEngagementPresenter performAMSEngagementWithParameters:completion:].cold.2
+ -[ICQAMSEngagementPresenter performAMSEngagementWithParameters:completion:].cold.3
+ -[ICQAMSEngagementPresenter reactivatePendingEngagementWithCompletion:]
+ -[ICQAMSFlowManager .cxx_destruct]
+ -[ICQAMSFlowManager _enrichedParametersFromParameters:bundleId:isICQ:]
+ -[ICQAMSFlowManager _handleFlowCompletionWithSuccess:error:userCompletion:]
+ -[ICQAMSFlowManager _handleFlowCompletionWithSuccess:error:userCompletion:].cold.1
+ -[ICQAMSFlowManager _tryStartFlowWithCompletion:]
+ -[ICQAMSFlowManager beginFlowWithParameters:completion:]
+ -[ICQAMSFlowManager init]
+ GCC_except_table11
+ _ICQAMSActParamsKey
+ _ICQAMSOriginatorBundleIdentifierKey
+ _ICQAMSUserAgentSuffixKey
+ _OBJC_CLASS_$_AMSEngagementRequest
+ _OBJC_CLASS_$_AMSProcessInfo
+ _OBJC_CLASS_$_AMSSystemEngagementTask
+ _OBJC_CLASS_$_ICQAMSEngagementPresenter
+ _OBJC_CLASS_$_ICQAMSFlowManager
+ _OBJC_IVAR_$_ICQAMSEngagementPresenter._pendingTask
+ _OBJC_IVAR_$_ICQAMSEngagementPresenter._taskLock
+ _OBJC_IVAR_$_ICQAMSFlowManager._activeDaemonConnection
+ _OBJC_IVAR_$_ICQAMSFlowManager._flowLock
+ _OBJC_IVAR_$_ICQAMSFlowManager._flowStartTime
+ _OBJC_IVAR_$_ICQAMSFlowManager._foregroundObserverToken
+ _OBJC_IVAR_$_ICQAMSFlowManager._isFlowPresented
+ _OBJC_METACLASS_$_ICQAMSEngagementPresenter
+ _OBJC_METACLASS_$_ICQAMSFlowManager
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ __OBJC_$_CLASS_METHODS_ICQAMSEngagementPresenter
+ __OBJC_$_CLASS_METHODS_ICQAMSFlowManager
+ __OBJC_$_INSTANCE_METHODS_ICQAMSEngagementPresenter
+ __OBJC_$_INSTANCE_METHODS_ICQAMSFlowManager
+ __OBJC_$_INSTANCE_VARIABLES_ICQAMSEngagementPresenter
+ __OBJC_$_INSTANCE_VARIABLES_ICQAMSFlowManager
+ __OBJC_CLASS_RO_$_ICQAMSEngagementPresenter
+ __OBJC_CLASS_RO_$_ICQAMSFlowManager
+ __OBJC_METACLASS_RO_$_ICQAMSEngagementPresenter
+ __OBJC_METACLASS_RO_$_ICQAMSFlowManager
+ ___34+[ICQAMSFlowManager sharedManager]_block_invoke
+ ___44+[ICQAMSEngagementPresenter sharedPresenter]_block_invoke
+ ___44+[ICQLink performAction:parameters:options:]_block_invoke
+ ___44+[ICQLink performAction:parameters:options:]_block_invoke.cold.1
+ ___56-[ICQAMSFlowManager beginFlowWithParameters:completion:]_block_invoke
+ ___56-[ICQAMSFlowManager beginFlowWithParameters:completion:]_block_invoke_2
+ ___56-[ICQAMSFlowManager beginFlowWithParameters:completion:]_block_invoke_3
+ ___56-[ICQAMSFlowManager beginFlowWithParameters:completion:]_block_invoke_3.cold.1
+ ___57-[ICQAMSEngagementPresenter _performPostPurchaseTeardown]_block_invoke
+ ___57-[ICQAMSEngagementPresenter _performPostPurchaseTeardown]_block_invoke.cold.1
+ ___75-[ICQAMSEngagementPresenter performAMSEngagementWithParameters:completion:]_block_invoke
+ ___75-[ICQAMSEngagementPresenter performAMSEngagementWithParameters:completion:]_block_invoke.cold.1
+ ___98-[ICQAMSEngagementPresenter _launchAMSEngagementWithURL:params:originatorBundleId:bag:completion:]_block_invoke
+ ___98-[ICQAMSEngagementPresenter _launchAMSEngagementWithURL:params:originatorBundleId:bag:completion:]_block_invoke.cold.1
+ ___block_descriptor_40_e8_32s_e20_v20?0B8"NSError"12ls32l8
+ ___block_descriptor_48_e8_32bs40w_e20_v20?0B8"NSError"12lw40l8s32l8
+ ___block_descriptor_48_e8_32bs40w_e41_v24?0"AMSEngagementResult"8"NSError"16lw40l8s32l8
+ ___block_descriptor_72_e8_32s40s48s56s64bs_e30_v28?0"NSURL"8B16"NSError"20ls64l8s32l8s40l8s48l8s56l8
+ ___block_literal_global.25
+ ___block_literal_global.60
+ _block_copy_helper.5
+ _block_descriptor.7
+ _block_destroy_helper.6
+ _objc_msgSend$URLForDirectory:inDomain:appropriateForURL:create:error:
+ _objc_msgSend$URLForKey:
+ _objc_msgSend$_activateIfWithError:
+ _objc_msgSend$_clientDataFromActParams:
+ _objc_msgSend$_enrichedParametersFromParameters:bundleId:isICQ:
+ _objc_msgSend$_handleFlowCompletionWithSuccess:error:userCompletion:
+ _objc_msgSend$_launchAMSEngagementWithURL:params:originatorBundleId:bag:completion:
+ _objc_msgSend$_metricsOverlayFromActParams:account:
+ _objc_msgSend$_performPostPurchaseTeardown
+ _objc_msgSend$_tryStartFlowWithCompletion:
+ _objc_msgSend$aa_addClientInfoHeaders
+ _objc_msgSend$aa_addContentTypeHeaders:
+ _objc_msgSend$aa_addDeviceIDHeader
+ _objc_msgSend$aa_addMultiUserDeviceHeaderIfEnabled
+ _objc_msgSend$aa_primaryAppleAccountWithCompletion:
+ _objc_msgSend$apps
+ _objc_msgSend$beginFlowWithParameters:completion:
+ _objc_msgSend$boolForEntitlement:
+ _objc_msgSend$bundleIds
+ _objc_msgSend$clearPendingEngagement
+ _objc_msgSend$createDirectoryAtURL:withIntermediateDirectories:attributes:error:
+ _objc_msgSend$currentProcess
+ _objc_msgSend$fetchStorageAppsWithCompletion:
+ _objc_msgSend$fetchStorageSummaryWithCompletion:
+ _objc_msgSend$fileDescriptor
+ _objc_msgSend$fileExistsAtPath:
+ _objc_msgSend$fileHandleForReadingFromURL:error:
+ _objc_msgSend$getPhotoLibraryQuotaSize
+ _objc_msgSend$initWithBase64EncodedString:options:
+ _objc_msgSend$initWithDomain:code:userInfo:
+ _objc_msgSend$initWithRequest:
+ _objc_msgSend$initWithURL:cachePolicy:timeoutInterval:
+ _objc_msgSend$invalidateAndCancel
+ _objc_msgSend$notifyAMSEngagementAppDidBecomeActiveWithCompletion:
+ _objc_msgSend$operatingSystemVersion
+ _objc_msgSend$performAMSEngagementWithParameters:completion:
+ _objc_msgSend$performPostPurchaseTeardownWithCompletion:
+ _objc_msgSend$present
+ _objc_msgSend$processInfo
+ _objc_msgSend$quotaBag
+ _objc_msgSend$renewCredentialsForAccount:completion:
+ _objc_msgSend$sessionWithConfiguration:delegate:delegateQueue:
+ _objc_msgSend$setBag:
+ _objc_msgSend$setBundleIdentifier:
+ _objc_msgSend$setClientData:
+ _objc_msgSend$setClientInfo:
+ _objc_msgSend$setMetricsOverlay:
+ _objc_msgSend$setShouldIgnoreCache:
+ _objc_msgSend$setURL:
+ _objc_msgSend$setUserAgentSuffix:
+ _objc_msgSend$sharedManager
+ _objc_msgSend$sharedPresenter
+ _objc_msgSend$sizeOfLocallyAvailableiCloudQuotaResourcesWithError:
+ _objc_msgSend$valueWithCompletion:
+ _sharedManager.onceToken
+ _sharedManager.sCoordinator
+ _sharedPresenter.onceToken
+ _sharedPresenter.sPresenter
+ _swift_release_n
+ _symbolic SS3key_yp5valuet
- +[ICQDaemonOfferConditions getLibrarySizesFromDB:]
- +[ICQDaemonOfferConditions getLibrarySizesFromDB:].cold.1
- +[ICQDaemonOfferConditions getLibrarySizesFromDB:].cold.2
- +[ICQDaemonOfferConditions getPhotosLibraryUploadSizeWithCompletion:].cold.1
- _block_copy_helper.6
- _block_descriptor.8
- _block_destroy_helper.7
- _malloc
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$getLibrarySizesFromDB:
- _objc_msgSend$getLibrarySizesFromDB:error:
- _objc_retain_x1
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x6
- _objc_retain_x7
- _objc_retain_x9
- _swift_bridgeObjectRelease_n
CStrings:
+ "%@/%@ MBF/1.0 CastleSettings/1.0"
+ "@\"<NSObject>\""
+ "@\"AMSSystemEngagementTask\""
+ "@\"INDaemonConnection\""
+ "@36@0:8@16@24B32"
+ "AMSBag unavailable"
+ "DSID"
+ "Flow already in progress"
+ "ICQAMSEngagementPresenter"
+ "ICQAMSEngagementPresenter: AMSSystemEngagementTask completed"
+ "ICQAMSEngagementPresenter: AMSSystemEngagementTask failed (code=%{public}ld): %{public}@"
+ "ICQAMSEngagementPresenter: CRITICAL - AMSBag.quotaBag is nil!"
+ "ICQAMSEngagementPresenter: Failed to get URL from bag: %@"
+ "ICQAMSEngagementPresenter: Launching engagement (URL=%{public}@, serviceType=%{public}@, placement=%{public}@)"
+ "ICQAMSEngagementPresenter: Missing required serviceType or placement"
+ "ICQAMSEngagementPresenter: Post-purchase teardown failed: %@"
+ "ICQAMSEngagementPresenter: Post-purchase teardown succeeded"
+ "ICQAMSEngagementPresenter: Server-provided URL is malformed: %@, falling back to bag"
+ "ICQAMSEngagementPresenter: Starting engagement flow"
+ "ICQAMSFlowManager"
+ "ICQAMSFlowManager: Failed to reactivate engagement: %@"
+ "ICQAMSFlowManager: Flow already in progress, rejecting to prevent button spam"
+ "ICQAMSFlowManager: Flow completed successfully"
+ "ICQAMSFlowManager: Flow completed with error: %@"
+ "ICQAMSFlowManager: Previous flow timed out, allowing new flow"
+ "ICQAMSFlowManager: beginFlowWithParameters (isRemoteFlow=%{public}d, params=%{public}@)"
+ "ICQActionLaunchAMSEngagementTask"
+ "ICQLink: AMSEngagement flow failed: %@"
+ "ICQLink: launching AMSSystemEngagementTask via flow manager"
+ "Missing serviceType or placement"
+ "No pending engagement task"
+ "Photo library unavailable before device unlock"
+ "UIApplicationWillEnterForegroundNotification"
+ "URLForKey:"
+ "_activateIfWithError:"
+ "_activeDaemonConnection"
+ "_clientDataFromActParams:"
+ "_enrichedParametersFromParameters:bundleId:isICQ:"
+ "_flowLock"
+ "_flowStartTime"
+ "_foregroundObserverToken"
+ "_handleFlowCompletionWithSuccess:error:userCompletion:"
+ "_isFlowPresented"
+ "_launchAMSEngagementWithURL:params:originatorBundleId:bag:completion:"
+ "_metricsOverlayFromActParams:account:"
+ "_originatorBundleIdentifier"
+ "_pendingTask"
+ "_performPostPurchaseTeardown"
+ "_taskLock"
+ "_tryStartFlowWithCompletion:"
+ "app"
+ "beginFlowWithParameters:completion:"
+ "boolForEntitlement:"
+ "clearPendingEngagement"
+ "clientIdentifier"
+ "com.apple.springboard.remote-alert"
+ "currentProcess"
+ "getInfoWithCompletion: photo library usage is not available before first unlock."
+ "getPhotoLibraryQuotaSize"
+ "getPhotoLibraryQuotaSize: Error from sizeOfLocallyAvailableiCloudQuotaResourcesWithError: %@"
+ "getPhotoLibraryQuotaSize: photo libary usage is not available."
+ "getPhotoLibraryQuotaSize: returning size: %lld"
+ "icloud"
+ "initWithBase64EncodedString:options:"
+ "initWithRequest:"
+ "marketingItemDynamicUIUrl"
+ "mediaClientIdentifier"
+ "metricsOverlay"
+ "notifyAMSEngagementAppDidBecomeActiveWithCompletion:"
+ "performAMSEngagementWithParameters:completion:"
+ "performPostPurchaseTeardownWithCompletion:"
+ "placement"
+ "present"
+ "reactivatePendingEngagementWithCompletion:"
+ "serviceType"
+ "setBag:"
+ "setClientData:"
+ "setClientInfo:"
+ "setMetricsOverlay:"
+ "setURL:"
+ "setUserAgentSuffix:"
+ "sharedManager"
+ "sharedPresenter"
+ "shouldUseiCloudAccount"
+ "sizeOfLocallyAvailableiCloudQuotaResourcesWithError:"
+ "topic"
+ "v24@?0@\"AMSEngagementResult\"8@\"NSError\"16"
+ "v28@?0@\"NSURL\"8B16@\"NSError\"20"
+ "v36@0:8B16@20@?28"
+ "valueWithCompletion:"
+ "xp_its_main"
- "%lu"
- "Error from getLibrarySizesFromDB: %@"
- "Requesting library size from PHPhotoLibrary"
- "Requesting library size from PHPhotoLibrary using DB"
- "com.apple.ind.getPHPhotoLibrarySizes"
- "com.apple.ind.getPHPhotoLibrarySizesWithDB"
- "getLibrarySizesFromDB:"
- "getLibrarySizesFromDB: photo libary usage is not available."
- "getLibrarySizesFromDB:error:"

```
