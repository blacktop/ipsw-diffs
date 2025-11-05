## AMPLibraryAgent

> `/System/Library/PrivateFrameworks/AMPLibrary.framework/Versions/A/Support/AMPLibraryAgent`

```diff

-1.5.2.56.0
-  __TEXT.__text: 0x5c7abc
-  __TEXT.__auth_stubs: 0x3700
-  __TEXT.__objc_stubs: 0x4860
-  __TEXT.__init_offsets: 0xd4
-  __TEXT.__objc_methlist: 0xd60
-  __TEXT.__const: 0x70d58
-  __TEXT.__gcc_except_tab: 0x2f6d0
-  __TEXT.__oslogstring: 0x22c09
-  __TEXT.__cstring: 0x41677
+1.5.4.70.0
+  __TEXT.__text: 0x5c5ce0
+  __TEXT.__auth_stubs: 0x3660
+  __TEXT.__objc_stubs: 0x48e0
+  __TEXT.__init_offsets: 0xd0
+  __TEXT.__objc_methlist: 0x13dc
+  __TEXT.__cstring: 0x41567
+  __TEXT.__const: 0x71098
+  __TEXT.__gcc_except_tab: 0x2f9bc
+  __TEXT.__oslogstring: 0x22faa
   __TEXT.__objc_classname: 0x38e
-  __TEXT.__objc_methname: 0x4f14
+  __TEXT.__objc_methname: 0x4f50
   __TEXT.__objc_methtype: 0x19f8
-  __TEXT.__unwind_info: 0x11748
+  __TEXT.__unwind_info: 0x11468
   __TEXT.__eh_frame: 0xcc
-  __DATA_CONST.__auth_got: 0x1b90
-  __DATA_CONST.__got: 0x8a8
-  __DATA_CONST.__auth_ptr: 0x120
-  __DATA_CONST.__const: 0x42300
-  __DATA_CONST.__cfstring: 0x11240
+  __DATA_CONST.__auth_got: 0x1b40
+  __DATA_CONST.__got: 0x8c8
+  __DATA_CONST.__auth_ptr: 0x110
+  __DATA_CONST.__const: 0x440e8
+  __DATA_CONST.__cfstring: 0x110a0
   __DATA_CONST.__objc_classlist: 0xa0
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x78

   __DATA_CONST.__objc_classrefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x40
   __DATA_CONST.__objc_intobj: 0x60
-  __DATA.__objc_const: 0x2ab0
-  __DATA.__objc_selrefs: 0x15f0
+  __DATA.__objc_const: 0x1eb0
+  __DATA.__objc_selrefs: 0x1700
   __DATA.__objc_ivar: 0xdc
   __DATA.__objc_data: 0x640
-  __DATA.__data: 0xfc8
-  __DATA.__common: 0x31f0
-  __DATA.__bss: 0x334d0
+  __DATA.__data: 0xfd8
+  __DATA.__bss: 0x33490
+  __DATA.__common: 0x31b0
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 1085C5CA-2D7D-304A-B1E7-3F7956A142AF
-  Functions: 16821
-  Symbols:   1207
-  CStrings:  14906
+  UUID: 7E33A4C2-090B-3DDF-A5FA-028193CB5BDE
+  Functions: 16622
+  Symbols:   1198
+  CStrings:  14895
 
Symbols:
+ __ZNKSt3__119__shared_weak_count13__get_deleterERKSt9type_info
+ __ZNSt3__117bad_function_callD1Ev
+ __ZTINSt3__117bad_function_callE
+ __ZTVNSt3__117bad_function_callE
- _CGDataProviderCreateDirect
- _CGImageSourceCreateWithDataProvider
- __ZNKSt9exception4whatEv
- __ZNSt9exceptionD2Ev
- __ZTISt9exception
- _cache_get_and_retain
- _cache_release_value
- _cache_remove
- _cache_set_and_retain
- _malloc_default_purgeable_zone
- _malloc_size
- _malloc_type_malloc
- _malloc_zone_malloc
CStrings:
+ "!this->HasPendingRequests()"
+ "%26"
+ "%s/AMPLibraryAgent-1.5.4.70"
+ "%{public}s unknown tag in response %{public}s size:%u "
+ "( ((downloadManager) != __null) && (((downloadManager)->magic == 'down') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"(downloadManager)->magic == 'down'\", \"/AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Sources/AMPLibrary/iTunes/Application/DownloadManager.cpp\", 10500, true)) )"
+ "( ((downloadManager) != __null) && (((downloadManager)->magic == 'down') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"(downloadManager)->magic == 'down'\", \"/AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Sources/AMPLibrary/iTunes/Application/DownloadManager.cpp\", 11320, true)) )"
+ "( ((inDM) != __null) && (((inDM)->magic == 'down') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"(inDM)->magic == 'down'\", \"/AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Sources/AMPLibrary/iTunes/Application/DownloadManager.cpp\", 15723, true)) )"
+ "( ((inDM) != __null) && (((inDM)->magic == 'down') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"(inDM)->magic == 'down'\", \"/AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Sources/AMPLibrary/iTunes/Application/DownloadManager.cpp\", 18048, true)) )"
+ "( ((inWorkTaskInfo) != __null) && (((inWorkTaskInfo)->magic == 'dwti') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"(inWorkTaskInfo)->magic == 'dwti'\", \"/AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Sources/AMPLibrary/iTunes/Application/DownloadManager.cpp\", 8446, true)) )"
+ "((databaseData->magic == 'db  ') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"databaseData->magic == 'db  '\", \"/AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Sources/AMPLibrary/iTunes/Application/Plugins.cpp\", 699, true))"
+ "((plugin->magic == 'db  ') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"plugin->magic == 'db  '\", \"/AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Sources/AMPLibrary/iTunes/Application/Plugins.cpp\", 120, true))"
+ "((plugin->magic == 'encd') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"plugin->magic == 'encd'\", \"/AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Sources/AMPLibrary/iTunes/Application/Plugins.cpp\", 103, true))"
+ "((plugin->magic == 'plug') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"plugin->magic == 'plug'\", \"/AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Sources/AMPLibrary/iTunes/Application/Plugins.cpp\", 84, true))"
+ "((stream->magic == 'strm') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"stream->magic == 'strm'\", \"/AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Sources/AMPLibrary/Utilities/StreamUtilities.cpp\", 21, true))"
+ "(msg->trackKind == kITFileKind) || (msg->trackKind == kITMemoryFileKind)"
+ "***ERROR*** ProcessRequest could not find a request again after prepare, assuming the request has been cancelled."
+ "***ERROR*** ProcessRequest could not find a request, assuming the request has been cancelled."
+ "**WARNING**: Unimplemented function \"%s\" at /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Sources/AMPLibrary/Core/amplibraryd/amplibrarydStubs.cpp:%d"
+ "1.5.4"
+ "1.5.4.70"
+ "13.5.4.70"
+ "AMPErrorDomainHRESULT"
+ "AMPLibraryAgent version: 1.5.4.70"
+ "AppleWebKit"
+ "Automatically Add to TV"
+ "Automatically Add to TV.localized"
+ "Automatically Add to Videos"
+ "Automatically Add to Videos.localized"
+ "Cancelling all requests with reason %s, except those marked non-cancellable."
+ "Could not register StoreServices un-initialization proc. Not initialized."
+ "DMAPTagged requests have to be POST."
+ "Destroying request scheduler."
+ "FixMediaLibraryBundlePermissions(): File \"%{public}s\" is locked"
+ "FixMediaLibraryBundlePermissions(): File \"%{public}s\" is not writeable"
+ "FixMediaLibraryBundlePermissions(): JRCreateDirectoryIterator() failed! status = %d"
+ "FixMediaLibraryBundlePermissions(): JRFileSpecSetPermissions() failed for file \"%{public}s\". status = %d"
+ "FixMediaLibraryBundlePermissions(): JRFileSpecSetPermissions() failed for library bundle folder. status = %d"
+ "FixMediaLibraryBundlePermissions(): JRFileSpecUnlock() failed for file \"%{public}s\". status = %d"
+ "FixMediaLibraryBundlePermissions(): JRIterateDirectory() failed! status =  %d"
+ "FixMediaLibraryBundlePermissions(): Library bundle folder is not writeable!"
+ "Found request scheduler with pending requests at StoreServices un-initialization time."
+ "Left %lu requests uncancelled."
+ "NSMissingImage"
+ "No clientId to fetch API token."
+ "No token service! Cannot get JWT for Request %{public}s(%d)"
+ "No token service.."
+ "Notification arrived after shutdown has begun. Ignoring."
+ "Pref 'log-request-to-har-path' is not present or empty."
+ "Scheduler was destroyed. Cannot continue request %{public}s(%d) after custom requirements were satisfied."
+ "Scheduler was destroyed. Cannot set JWT in request %{public}s(%d)"
+ "Scheduler was destroyed. Cannot set Mescal session in request %{public}s(%d)"
+ "Scheduler was destroyed. Cannot set StoreBag in request %{public}s(%d)"
+ "Stopping accepting requests."
+ "editing-session-id"
+ "inArtworkFileURL.IsValid()"
+ "info != nullptr && ((info->magic == 'srai') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"info->magic == 'srai'\", \"/AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Sources/AMPLibrary/Utilities/StreamUtilities.cpp\", 2453, true))"
+ "info != nullptr && ((info->magic == 'srai') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"info->magic == 'srai'\", \"/AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Sources/AMPLibrary/Utilities/StreamUtilities.cpp\", 752, true))"
+ "initWithContentsOfURL:"
+ "kDMAPMaxTotalCountCode"
+ "kStoreDAAPAppendPinCode"
+ "kStoreDAAPDeletePinCode"
+ "kStoreDAAPEditPinsRequestCode"
+ "kStoreDAAPEditPinsResponseCode"
+ "kStoreDAAPGetPinsRequestCode"
+ "kStoreDAAPGetPinsResponseCode"
+ "kStoreDAAPInsertAfterPinLocationUUIDCode"
+ "kStoreDAAPMovePinCode"
+ "kStoreDAAPPinActionCode"
+ "kStoreDAAPPinLocationTypeCode"
+ "kStoreDAAPPinLocationUUIDCode"
+ "kStoreDAAPPlaylistEditSessionIDCode"
+ "kStoreDAAPUpdatePinCode"
+ "nullptr != assetFileSpec"
+ "params->u.getLocationString.locationString != nullptr"
+ "removeObjectForKey:"
+ "request_scheduler"
+ "setCacheMode:"
+ "setObject:forKey:cost:"
+ "urlRequest.IsValid() || error.IsValid()"
- " AppleWebKit/"
- "%0.2f"
- "%s/AMPLibraryAgent-1.5.2.56"
- "( ((downloadManager) != __null) && (((downloadManager)->magic == 'down') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"(downloadManager)->magic == 'down'\", \"/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AMPLibrary/iTunes/Application/DownloadManager.cpp\", 10501, true)) )"
- "( ((downloadManager) != __null) && (((downloadManager)->magic == 'down') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"(downloadManager)->magic == 'down'\", \"/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AMPLibrary/iTunes/Application/DownloadManager.cpp\", 11321, true)) )"
- "( ((inDM) != __null) && (((inDM)->magic == 'down') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"(inDM)->magic == 'down'\", \"/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AMPLibrary/iTunes/Application/DownloadManager.cpp\", 15744, true)) )"
- "( ((inDM) != __null) && (((inDM)->magic == 'down') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"(inDM)->magic == 'down'\", \"/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AMPLibrary/iTunes/Application/DownloadManager.cpp\", 18069, true)) )"
- "( ((inWorkTaskInfo) != __null) && (((inWorkTaskInfo)->magic == 'dwti') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"(inWorkTaskInfo)->magic == 'dwti'\", \"/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AMPLibrary/iTunes/Application/DownloadManager.cpp\", 8447, true)) )"
- "((databaseData->magic == 'db  ') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"databaseData->magic == 'db  '\", \"/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AMPLibrary/iTunes/Application/Plugins.cpp\", 699, true))"
- "((plugin->magic == 'db  ') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"plugin->magic == 'db  '\", \"/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AMPLibrary/iTunes/Application/Plugins.cpp\", 120, true))"
- "((plugin->magic == 'encd') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"plugin->magic == 'encd'\", \"/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AMPLibrary/iTunes/Application/Plugins.cpp\", 103, true))"
- "((plugin->magic == 'plug') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"plugin->magic == 'plug'\", \"/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AMPLibrary/iTunes/Application/Plugins.cpp\", 84, true))"
- "((stream->magic == 'strm') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"stream->magic == 'strm'\", \"/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AMPLibrary/Utilities/StreamUtilities.cpp\", 21, true))"
- "(isLatitude == false && integralComponentsStringLength == 3) || (isLatitude && integralComponentsStringLength == 2)"
- "(isLatitude == false && integralComponentsStringLength == 5) || (isLatitude && integralComponentsStringLength == 4)"
- "(isLatitude == false && integralComponentsStringLength == 7) || (isLatitude && integralComponentsStringLength == 6)"
- "***ERROR*** Could not find a request again after prepare, assuming the request has been cancelled."
- "***ERROR*** Could not find a request, assuming the request has been cancelled."
- "**ERROR**: IsCloudMusicLibraryClientLoaded() is FALSE! command:%{public}s cmdID:%llu"
- "**ERROR**: ItemIDKind() failed! status:%d"
- "**WARNING**: Unimplemented function \"%s\" at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AMPLibrary/Core/amplibraryd/amplibrarydStubs.cpp:%d"
- "+-"
- "+-C/"
- ".."
- "1.0"
- "1.5.2"
- "1.5.2.56"
- "13.5.2.56"
- "AMPLibraryAgent version: 1.5.2.56"
- "Cancelled all requests."
- "Cancelling any and all pending requests because too much time has passed while quitting process."
- "Cannot get JWT. No token service!!!"
- "GMT"
- "GetLatitudeAndLongitudeFromISO6709String(iso6709String, &workItem->latitude, &workItem->longitude)"
- "GetTrackInfoCanHavePrice(trackInfo)"
- "ITCMGetMetaDataValue"
- "JRCFStringGetLength(signString) == 1"
- "Left %u requests uncancelled, possibly because process quitting and request allowed to continue during quit."
- "ParseLatitudeOrLongitude(scanner, &latitude, true)"
- "ParseLatitudeOrLongitude(scanner, &longitude, false)"
- "Pref 'log-request-to-har-path' is not present"
- "Scheduler was destroyed. Cannot continue after custom requirements were satisfied."
- "Scheduler was destroyed. Cannot set JWT."
- "Scheduler was destroyed. Cannot set Mescal session."
- "Scheduler was destroyed. Cannot set StoreBag."
- "UTC"
- "appVersion"
- "columnInfo->sortable"
- "columns"
- "componentsToDisplayForPath:"
- "degreesString != nullptr"
- "deliveryVersion"
- "eventType"
- "events"
- "inArtworkUUID != nullptr"
- "info != nullptr && ((info->magic == 'srai') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"info->magic == 'srai'\", \"/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AMPLibrary/Utilities/StreamUtilities.cpp\", 2453, true))"
- "info != nullptr && ((info->magic == 'srai') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"info->magic == 'srai'\", \"/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AMPLibrary/Utilities/StreamUtilities.cpp\", 752, true))"
- "isSignedIn"
- "location"
- "locationStr != nullptr"
- "minutesString != nullptr"
- "msg->trackKind == kITFileKind"
- "pixelRatio"
- "postTime"
- "priceDisplay"
- "priceStr != nullptr"
- "provider != nullptr"
- "relativeTo == nullptr"
- "requestscheduler"
- "result == noErr || result == 2"
- "screenHeight"
- "screenWidth"
- "secondsString != nullptr"
- "set != nullptr"
- "this->IsSuccessful()"
- "topic"
- "trackInfo->mediaKindPrivate != kTrackInfoMediaKind_Unknown"
- "validURL"

```
