## AMPDevicesAgent

> `/System/Library/PrivateFrameworks/AMPDevices.framework/Versions/A/Support/AMPDevicesAgent`

```diff

-1.5.2.56.0
-  __TEXT.__text: 0x68b99c
-  __TEXT.__auth_stubs: 0x5840
-  __TEXT.__objc_stubs: 0x81c0
-  __TEXT.__init_offsets: 0xa4
-  __TEXT.__objc_methlist: 0x14f0
-  __TEXT.__const: 0x832c0
-  __TEXT.__gcc_except_tab: 0x2d2ec
-  __TEXT.__cstring: 0x60d23
-  __TEXT.__oslogstring: 0x1ac68
+1.5.4.70.0
+  __TEXT.__text: 0x686c0c
+  __TEXT.__auth_stubs: 0x56b0
+  __TEXT.__objc_stubs: 0x8220
+  __TEXT.__init_offsets: 0x9c
+  __TEXT.__objc_methlist: 0x1e1c
+  __TEXT.__const: 0x83568
+  __TEXT.__gcc_except_tab: 0x2d5a0
+  __TEXT.__cstring: 0x5fa54
+  __TEXT.__oslogstring: 0x1ad3f
   __TEXT.__objc_classname: 0x355
-  __TEXT.__objc_methname: 0x8beb
+  __TEXT.__objc_methname: 0x8c13
   __TEXT.__objc_methtype: 0x2a67
-  __TEXT.__unwind_info: 0x11df0
+  __TEXT.__unwind_info: 0x11c10
   __TEXT.__eh_frame: 0x1ec
-  __DATA_CONST.__auth_got: 0x2c38
+  __DATA_CONST.__auth_got: 0x2b70
   __DATA_CONST.__got: 0xe28
-  __DATA_CONST.__auth_ptr: 0x190
-  __DATA_CONST.__const: 0x55e98
-  __DATA_CONST.__cfstring: 0x13f80
+  __DATA_CONST.__auth_ptr: 0x188
+  __DATA_CONST.__const: 0x579f0
+  __DATA_CONST.__cfstring: 0x13820
   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x60

   __DATA_CONST.__objc_classrefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x68
   __DATA_CONST.__objc_intobj: 0x48
-  __DATA.__objc_const: 0x3260
-  __DATA.__objc_selrefs: 0x2630
+  __DATA.__objc_const: 0x20c8
+  __DATA.__objc_selrefs: 0x2720
   __DATA.__objc_ivar: 0x100
   __DATA.__objc_data: 0x5a0
-  __DATA.__data: 0x1438
-  __DATA.__common: 0x3b10
-  __DATA.__bss: 0x33ea0
+  __DATA.__data: 0x1428
+  __DATA.__common: 0x3ae8
+  __DATA.__bss: 0x33bd0
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts

   - /System/Library/PrivateFrameworks/PhotosFormats.framework/Versions/A/PhotosFormats
   - /System/Library/PrivateFrameworks/SoftwareUpdate.framework/Versions/A/SoftwareUpdate
   - /System/Library/PrivateFrameworks/StoreFoundation.framework/Versions/A/StoreFoundation
-  - /System/Library/PrivateFrameworks/iPod.framework/Versions/A/iPod
   - /System/Library/PrivateFrameworks/iPodUpdater.framework/Versions/A/iPodUpdater
   - /System/Library/PrivateFrameworks/iTunesCloud.framework/Versions/A/iTunesCloud
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 04EDFA4B-DACC-3AFF-BBEC-68F2EC3161FA
-  Functions: 17679
-  Symbols:   1917
-  CStrings:  22261
+  UUID: 2C7E7D00-5364-333F-AD95-776FDD3DAC3A
+  Functions: 17541
+  Symbols:   1889
+  CStrings:  22125
 
Symbols:
+ __ZNKSt3__119__shared_weak_count13__get_deleterERKSt9type_info
+ __ZNSt3__117bad_function_callD1Ev
+ __ZTINSt3__117bad_function_callE
+ __ZTVNSt3__117bad_function_callE
- _AVCFInitializeProtectedContentPlaybackSupportAudioKey
- _AVCFInitializeProtectedContentPlaybackSupportVideoKey
- _AVCFProtectedContentProviderCommon
- _AVCFProtectedContentProviderFairPlay
- _CFURLCreateStringByReplacingPercentEscapes
- _CGDataProviderCreateDirect
- _CGImageSourceCreateWithDataProvider
- __AVCFInitializeRetainedProtectedContentPlaybackSupportSessionAsynchronouslyForProviderWithOptions
- __ZNKSt9exception4whatEv
- __ZNSt9exceptionD2Ev
- __ZTISt9exception
- _cache_get_and_retain
- _cache_release_value
- _cache_remove
- _cache_set_and_retain
- _iPodAquireLock
- _iPodCopyConnected
- _iPodCopyMountpoint
- _iPodCopyName
- _iPodCopyPreferences
- _iPodCopyRevision
- _iPodGetUniqueID
- _iPodPreferenceGetValue
- _iPodPreferenceSetValue
- _iPodRegisterWithServer
- _iPodReleaseLock
- _iPodSetPreferences
- _iPodUnregisterFromServer
- _malloc_default_purgeable_zone
- _malloc_size
- _malloc_type_malloc
- _malloc_zone_malloc
CStrings:
+ "!this->HasPendingRequests()"
+ "%26"
+ "( ((downloadManager) != __null) && (((downloadManager)->magic == 'down') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"(downloadManager)->magic == 'down'\", \"/AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Sources/Devices/iTunes/Application/DownloadManager.cpp\", 10500, true)) )"
+ "( ((downloadManager) != __null) && (((downloadManager)->magic == 'down') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"(downloadManager)->magic == 'down'\", \"/AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Sources/Devices/iTunes/Application/DownloadManager.cpp\", 11320, true)) )"
+ "( ((inDM) != __null) && (((inDM)->magic == 'down') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"(inDM)->magic == 'down'\", \"/AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Sources/Devices/iTunes/Application/DownloadManager.cpp\", 15665, true)) )"
+ "( ((inDM) != __null) && (((inDM)->magic == 'down') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"(inDM)->magic == 'down'\", \"/AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Sources/Devices/iTunes/Application/DownloadManager.cpp\", 15723, true)) )"
+ "( ((inDM) != __null) && (((inDM)->magic == 'down') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"(inDM)->magic == 'down'\", \"/AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Sources/Devices/iTunes/Application/DownloadManager.cpp\", 18048, true)) )"
+ "( ((inWorkTaskInfo) != __null) && (((inWorkTaskInfo)->magic == 'dwti') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"(inWorkTaskInfo)->magic == 'dwti'\", \"/AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Sources/Devices/iTunes/Application/DownloadManager.cpp\", 8446, true)) )"
+ "((databaseData->magic == 'db  ') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"databaseData->magic == 'db  '\", \"/AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Sources/Devices/iTunes/Application/Plugins.cpp\", 699, true))"
+ "((plugin->magic == 'db  ') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"plugin->magic == 'db  '\", \"/AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Sources/Devices/iTunes/Application/Plugins.cpp\", 120, true))"
+ "((plugin->magic == 'encd') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"plugin->magic == 'encd'\", \"/AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Sources/Devices/iTunes/Application/Plugins.cpp\", 103, true))"
+ "((plugin->magic == 'plug') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"plugin->magic == 'plug'\", \"/AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Sources/Devices/iTunes/Application/Plugins.cpp\", 84, true))"
+ "((stream->magic == 'strm') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"stream->magic == 'strm'\", \"/AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Sources/Devices/Utilities/StreamUtilities.cpp\", 21, true))"
+ "(msg->trackKind == kITFileKind) || (msg->trackKind == kITMemoryFileKind)"
+ "***ERROR*** ProcessRequest could not find a request again after prepare, assuming the request has been cancelled."
+ "***ERROR*** ProcessRequest could not find a request, assuming the request has been cancelled."
+ "1.5.4"
+ "1.5.4.70"
+ "13.5.4"
+ "13.5.4.70"
+ "AMPDevicesAgent: 1.5.4.70"
+ "AMPErrorDomainHRESULT"
+ "AppleWebKit"
+ "Automatically Add to TV"
+ "Automatically Add to TV.localized"
+ "Automatically Add to Videos"
+ "Automatically Add to Videos.localized"
+ "Cancelling all requests with reason %s, except those marked non-cancellable."
+ "Could not create notification center connection!"
+ "Could not register StoreServices un-initialization proc. Not initialized."
+ "DMAPTagged requests have to be POST."
+ "Destroying request scheduler."
+ "EditingSessionID"
+ "ExplicitContentBadgeTreatment"
+ "Found request scheduler with pending requests at StoreServices un-initialization time."
+ "IsSoftwareRestoreOnlyDeviceClass(deviceClass) == false"
+ "IsSoftwareRestoreOnlyDeviceClass(handlerData->deviceClass) == false"
+ "IsSoftwareUpdateRestoreDeviceClass(deviceClass)"
+ "IsSoftwareUpdateRestoreDeviceClass(mDeviceClass)"
+ "Left %lu requests uncancelled."
+ "NSMissingImage"
+ "No clientId to fetch API token."
+ "No token service! Cannot get JWT for Request %{public}s(%d)"
+ "No token service.."
+ "Notification arrived after shutdown has begun. Ignoring."
+ "Pref 'log-request-to-har-path' is not present or empty."
+ "Registering for notification action '%{public}@:%{public}@'"
+ "Scheduler was destroyed. Cannot continue request %{public}s(%d) after custom requirements were satisfied."
+ "Scheduler was destroyed. Cannot set JWT in request %{public}s(%d)"
+ "Scheduler was destroyed. Cannot set Mescal session in request %{public}s(%d)"
+ "Scheduler was destroyed. Cannot set StoreBag in request %{public}s(%d)"
+ "Stopping accepting requests."
+ "StoreServices::IsInitialized()"
+ "application/x-dmap-tagged"
+ "clientRef != nullptr && ((clientRef->magic == 'clie') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"clientRef->magic == 'clie'\", \"/AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Sources/Devices/iTunes/iPod/iPodSupport.cpp\", 1304, true))"
+ "currentField != __null"
+ "inArtworkFileURL.IsValid()"
+ "info != nullptr && ((info->magic == 'srai') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"info->magic == 'srai'\", \"/AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Sources/Devices/Utilities/StreamUtilities.cpp\", 2453, true))"
+ "info != nullptr && ((info->magic == 'srai') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"info->magic == 'srai'\", \"/AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Sources/Devices/Utilities/StreamUtilities.cpp\", 752, true))"
+ "initWithContentsOfURL:"
+ "isExplicitContentAgeVerificationRequired"
+ "korea"
+ "mHostToUse != nullptr"
+ "notificationRegistration"
+ "params->u.getLocationString.locationString != nullptr"
+ "request_scheduler"
+ "setCacheMode:"
+ "setObject:forKey:cost:"
+ "skynet> (receive only)"
+ "skynet> URL: %{public}@, stripLegacyVersionXML: %{BOOL}d"
+ "skynet> device returned empty URL list"
+ "skynet> existing instance already running"
+ "skynet> file size zero for %{public}@"
+ "skynet> getting URL list"
+ "skynet> incomplete file send; %d bytes remaining"
+ "skynet> reading request %d"
+ "skynet> received dictionary message %@"
+ "skynet> starting carrier bundle update service"
+ "skynet> starting file transfer of %d bytes from %{public}@ with status %d"
+ "urlRequest.IsValid() || error.IsValid()"
- " AppleWebKit/"
- "%0.2f"
- "%s()%s(receive only)"
- "%s()%sURL: %@, stripLegacyVersionXML: %s"
- "%s()%sdevice returned empty URL list"
- "%s()%sexisting instance already running"
- "%s()%sfile size zero for %@"
- "%s()%sgetting URL list"
- "%s()%sincomplete file send; %d bytes remaining"
- "%s()%sreading request %d"
- "%s()%sreceived dictionary message %@"
- "%s()%sstarting carrier bundle update service"
- "%s()%sstarting file transfer of %d bytes from %@ with status %d"
- "( ((downloadManager) != __null) && (((downloadManager)->magic == 'down') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"(downloadManager)->magic == 'down'\", \"/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/Devices/iTunes/Application/DownloadManager.cpp\", 10501, true)) )"
- "( ((downloadManager) != __null) && (((downloadManager)->magic == 'down') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"(downloadManager)->magic == 'down'\", \"/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/Devices/iTunes/Application/DownloadManager.cpp\", 11321, true)) )"
- "( ((inDM) != __null) && (((inDM)->magic == 'down') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"(inDM)->magic == 'down'\", \"/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/Devices/iTunes/Application/DownloadManager.cpp\", 15686, true)) )"
- "( ((inDM) != __null) && (((inDM)->magic == 'down') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"(inDM)->magic == 'down'\", \"/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/Devices/iTunes/Application/DownloadManager.cpp\", 15744, true)) )"
- "( ((inDM) != __null) && (((inDM)->magic == 'down') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"(inDM)->magic == 'down'\", \"/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/Devices/iTunes/Application/DownloadManager.cpp\", 18069, true)) )"
- "( ((inWorkTaskInfo) != __null) && (((inWorkTaskInfo)->magic == 'dwti') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"(inWorkTaskInfo)->magic == 'dwti'\", \"/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/Devices/iTunes/Application/DownloadManager.cpp\", 8447, true)) )"
- "((databaseData->magic == 'db  ') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"databaseData->magic == 'db  '\", \"/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/Devices/iTunes/Application/Plugins.cpp\", 699, true))"
- "((plugin->magic == 'db  ') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"plugin->magic == 'db  '\", \"/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/Devices/iTunes/Application/Plugins.cpp\", 120, true))"
- "((plugin->magic == 'encd') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"plugin->magic == 'encd'\", \"/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/Devices/iTunes/Application/Plugins.cpp\", 103, true))"
- "((plugin->magic == 'plug') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"plugin->magic == 'plug'\", \"/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/Devices/iTunes/Application/Plugins.cpp\", 84, true))"
- "((stream->magic == 'strm') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"stream->magic == 'strm'\", \"/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/Devices/Utilities/StreamUtilities.cpp\", 21, true))"
- "(deviceClass == kITIPodDeviceClassAppleIPod) || (deviceClass == kITIPodDeviceClassAppleIPodTouch) || (deviceClass == kITIPodDeviceClassAppleIPhone) || (deviceClass == kITIPodDeviceClassAppleIPad)"
- "(deviceClass == kITIPodDeviceClassAppleIPod) || (deviceClass == kITIPodDeviceClassAppleIPodTouch) || (deviceClass == kITIPodDeviceClassAppleIPhone) || (deviceClass == kITIPodDeviceClassAppleIPad) || (deviceClass == kITIPodDeviceClassAppleTV) || (deviceClass == kITIPodDeviceClassAppleWatch) || (deviceClass == kITIPodDeviceClassAppleHomePod) || (deviceClass == kITIPodDeviceClassAppleMac) || (deviceClass == kITIPodDeviceClassAppleIBridge)"
- "(deviceClass == kITIPodDeviceClassAppleIPodTouch) || (deviceClass == kITIPodDeviceClassAppleIPhone) || (deviceClass == kITIPodDeviceClassAppleIPad) || (deviceClass == kITIPodDeviceClassAppleWatch) || (deviceClass == kITIPodDeviceClassAppleHomePod) || (deviceClass == kITIPodDeviceClassAppleMac) || (deviceClass == kITIPodDeviceClassAppleIBridge)"
- "(deviceUpdaterFamilyInfo.deviceClass == kITIPodDeviceClassAppleIPod) || (deviceUpdaterFamilyInfo.deviceClass == kITIPodDeviceClassAppleIPodTouch) || (deviceUpdaterFamilyInfo.deviceClass == kITIPodDeviceClassAppleIPhone) || (deviceUpdaterFamilyInfo.deviceClass == kITIPodDeviceClassAppleIPad) || (deviceUpdaterFamilyInfo.deviceClass == kITIPodDeviceClassAppleTV) || (deviceUpdaterFamilyInfo.deviceClass == kITIPodDeviceClassAppleWatch) || (deviceUpdaterFamilyInfo.deviceClass == kITIPodDeviceClassAppleHomePod) || (deviceUpdaterFamilyInfo.deviceClass == kITIPodDeviceClassAppleMac) || (deviceUpdaterFamilyInfo.deviceClass == kITIPodDeviceClassAppleIBridge)"
- "(mDeviceClass == kITIPodDeviceClassAppleIPod) || (mDeviceClass == kITIPodDeviceClassAppleIPodTouch) || (mDeviceClass == kITIPodDeviceClassAppleIPhone) || (mDeviceClass == kITIPodDeviceClassAppleIPad) || (mDeviceClass == kITIPodDeviceClassAppleTV) || (mDeviceClass == kITIPodDeviceClassAppleWatch) || (mDeviceClass == kITIPodDeviceClassAppleHomePod) || (mDeviceClass == kITIPodDeviceClassAppleMac) || (mDeviceClass == kITIPodDeviceClassAppleIBridge)"
- "***ERROR*** Could not find a request again after prepare, assuming the request has been cancelled."
- "***ERROR*** Could not find a request, assuming the request has been cancelled."
- "1.5.2"
- "1.5.2.56"
- "13.5.2"
- "13.5.2.56"
- ": "
- "AMPDevicesAgent: 1.5.2.56"
- "AVCFContentKeyRequest_RequiresValidationDataInSecureTokenKey"
- "AVCFContentKeySessionServerPlaybackContextOption_ServerChallenge"
- "AVCFContentKeySession_InvalidatePersistableKey"
- "AVCFPlayerAllowsAirPlayVideoWhileExternalScreenIsActive"
- "AVCFPlayerAudioSessionModeDefault"
- "AVCFPlayerAudioSessionModeMoviePlayback"
- "AVCFPlayerGetAirPlayLocalPlaybackVolume"
- "AVCFPlayerGetAudioSessionPlaybackMode"
- "AVCFPlayerIsAirPlayLocalPlaybackEnabled"
- "AVCFPlayerIsAirPlayVideoAllowed"
- "AVCFPlayerIsAirPlayVideoAllowedWhileExternalScreenIsActive"
- "AVCFPlayerIsExclusiveAudioDevicePassthroughActive"
- "AVCFPlayerIsExternalPlaybackActive"
- "AVCFPlayerItemDurationParameter"
- "AVCFPlayerItemDurationProperty"
- "AVCFPlayerItemFailedToPlayToEndTimeErrorKey"
- "AVCFPlayerItemFailedToPlayToEndTimeNotification"
- "AVCFPlayerItemMakeReadyForInspection"
- "AVCFPlayerItemPlayerAttachedNotification"
- "AVCFPlayerItemPresentationSizeParameter"
- "AVCFPlayerItemPresentationSizeProperty"
- "AVCFPlayerItemTracksParameter"
- "AVCFPlayerItemTracksProperty"
- "AVCFPlayerMediaSelectionCriteriaPrincipalCharacteristicsKey"
- "AVCFPlayerPlaybackCoordinator_CopyPlaybackCoordinator"
- "AVCFPlayerPlaybackCoordinator_SetCallbacks"
- "AVCFPlayerRateDidChangeOriginatingParticipantKey"
- "AVCFPlayerSetAirPlayLocalPlaybackEnabled"
- "AVCFPlayerSetAirPlayLocalPlaybackVolume"
- "AVCFPlayerSetAllowsAirPlayVideo"
- "AVCFPlayerSetAudioSessionPlaybackMode"
- "AVCFPlayerSetExternalPlaybackRoutingContext"
- "AVCFQueuePlayerAdvanceToNextItem"
- "AVCFQueuePlayerCanInsertItem"
- "AVCFQueuePlayerCopyCurrentItems"
- "AVCFQueuePlayerCreateWithPlayerItemsAndOptions"
- "AVCFQueuePlayerGetTypeID"
- "AVCFQueuePlayerInsertItem"
- "AVCFQueuePlayerRemoveAllItems"
- "AVCFQueuePlayerRemoveItem"
- "AVCFURLAssetiTunesStoreContentAlternateContentInfoAssetURLStringKey"
- "AVCFURLAssetiTunesStoreContentAlternateContentInfoKey"
- "AVCFURLAssetiTunesStoreContentDSIDKey"
- "AVCFURLAssetiTunesStoreContentDownloadParametersKey"
- "AVCFURLAssetiTunesStoreContentHLSAssetURLStringKey"
- "AVCFURLAssetiTunesStoreContentIDKey"
- "AVCFURLAssetiTunesStoreContentInfoKey"
- "AVCFURLAssetiTunesStoreContentPurchasedMediaKindKey"
- "AVCFURLAssetiTunesStoreContentRentalIDKey"
- "AVCFURLAssetiTunesStoreContentTypeKey"
- "AVCFURLAssetiTunesStoreContentUserAgentKey"
- "AVCF_Uninitialize"
- "AVFoundationCF.framework"
- "AVFoundationCFSupport.plist"
- "AssetPlayabilityValidationPropertyList"
- "Cancelled all requests."
- "Cancelling any and all pending requests because too much time has passed while quitting process."
- "Cannot get JWT. No token service!!!"
- "CoreMediaPrewarm"
- "GMT"
- "GetTrackInfoCanHavePrice(trackInfo)"
- "JRCFURLGetJRFileSpec( url, volumeSpec, &status )"
- "Left %u requests uncancelled, possibly because process quitting and request allowed to continue during quit."
- "Pref 'log-request-to-har-path' is not present"
- "Releasing empty unmountable iPod record"
- "RequireOneRecognized"
- "Scheduler was destroyed. Cannot continue after custom requirements were satisfied."
- "Scheduler was destroyed. Cannot set JWT."
- "Scheduler was destroyed. Cannot set Mescal session."
- "Scheduler was destroyed. Cannot set StoreBag."
- "Simulating kiPodRemoved"
- "UTC"
- "ValidationType"
- "bundleResourcesURL != __null"
- "clientRef != nullptr && ((clientRef->magic == 'clie') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"clientRef->magic == 'clie'\", \"/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/Devices/iTunes/iPod/iPodSupport.cpp\", 1305, true))"
- "columnInfo->sortable"
- "componentsToDisplayForPath:"
- "functionName != nullptr"
- "functionSignature != nullptr"
- "handlerData->deviceClass == kITIPodDeviceClassAppleIPod || handlerData->deviceClass == kITIPodDeviceClassAppleIPodTouch || handlerData->deviceClass == kITIPodDeviceClassAppleIPhone || handlerData->deviceClass == kITIPodDeviceClassAppleIPad"
- "iPod path is \"%{public}s\""
- "iPod->haveOSFrameworkSupport == false"
- "iPod->macOSIPodRef != nullptr"
- "iPodDevice != nullptr"
- "iPodDevice == nullptr"
- "iPodDevice->hasNotBeenInitializedYet == true"
- "iPodDevice->macOSIPodRef == nullptr"
- "ignoring kiPodMounted message from SystemUIServer"
- "inArtworkUUID != nullptr"
- "inKey != nullptr"
- "info != nullptr && ((info->magic == 'srai') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"info->magic == 'srai'\", \"/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/Devices/Utilities/StreamUtilities.cpp\", 2453, true))"
- "info != nullptr && ((info->magic == 'srai') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"info->magic == 'srai'\", \"/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/Devices/Utilities/StreamUtilities.cpp\", 752, true))"
- "ioIsDone != nullptr"
- "ioStatus != nullptr"
- "isSupportedDeviceClass"
- "kiPodAttached"
- "kiPodMounted"
- "kiPodNameChanged"
- "kiPodPrefsChanged"
- "kiPodRemoved"
- "kiPodServerAlive"
- "kiPodServerDied"
- "kiPodUnmounted"
- "locationStr != nullptr"
- "mIPodLogFileSpecIsValid || mIPhoneLogFileSpecIsValid || mIPadLogFileSpecIsValid || mAppleTVLogFileSpecIsValid || mAppleWatchLogFileSpecIsValid || mHomePodLogFileSpecIsValid || (otaUpdateFailureLogFileSpec != nullptr)"
- "msg->trackKind == kITFileKind"
- "mutableDict != __null"
- "ok"
- "price"
- "priceDisplay"
- "priceStr != nullptr"
- "provider != nullptr"
- "relativeTo == nullptr"
- "requestscheduler"
- "result == noErr || result == 2"
- "sAVCFFrameworkBundle != __null"
- "sPrewarmDRMTimer == nullptr"
- "symbolAddresses != __null"
- "symbolNames != __null"
- "this->IsSuccessful()"
- "trackInfo->mediaKindPrivate != kTrackInfoMediaKind_Unknown"

```
