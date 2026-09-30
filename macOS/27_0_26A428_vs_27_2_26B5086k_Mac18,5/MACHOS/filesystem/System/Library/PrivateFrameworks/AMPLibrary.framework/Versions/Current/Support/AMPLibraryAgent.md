## AMPLibraryAgent

> `/System/Library/PrivateFrameworks/AMPLibrary.framework/Versions/Current/Support/AMPLibraryAgent`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__objc_methlist`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1.7.0.161.2
-  __TEXT.__text: 0x5ddc90
+1.7.1.18.1
+  __TEXT.__text: 0x5e0300
   __TEXT.__auth_stubs: 0x3970
   __TEXT.__objc_stubs: 0x52c0
   __TEXT.__init_offsets: 0xc8
   __TEXT.__objc_methlist: 0x1454
-  __TEXT.__cstring: 0x44573
-  __TEXT.__const: 0x761e0
+  __TEXT.__cstring: 0x4469f
+  __TEXT.__const: 0x763e0
   __TEXT.__objc_classname: 0x3ca
   __TEXT.__objc_methtype: 0x1895
   __TEXT.__constg_swiftt: 0x64
   __TEXT.__swift5_typeref: 0x3a
   __TEXT.__swift5_fieldmd: 0x20
   __TEXT.__swift5_types: 0x8
-  __TEXT.__gcc_except_tab: 0x2fabc
-  __TEXT.__oslogstring: 0x2935f
-  __TEXT.__objc_methname: 0x56d5
-  __TEXT.__unwind_info: 0x16368
+  __TEXT.__gcc_except_tab: 0x2ff1c
+  __TEXT.__oslogstring: 0x299f7
+  __TEXT.__objc_methname: 0x56e7
+  __TEXT.__unwind_info: 0x16448
   __TEXT.__eh_frame: 0xf0
-  __DATA_CONST.__const: 0x42718
-  __DATA_CONST.__cfstring: 0x119a0
+  __DATA_CONST.__const: 0x42948
+  __DATA_CONST.__cfstring: 0x116c0
   __DATA_CONST.__objc_classlist: 0xa8
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x78

   __DATA_CONST.__got: 0xa88
   __DATA_CONST.__auth_ptr: 0x150
   __DATA.__objc_const: 0x1ee0
-  __DATA.__objc_selrefs: 0x1970
+  __DATA.__objc_selrefs: 0x1978
   __DATA.__objc_ivar: 0xe0
   __DATA.__objc_data: 0x750
   __DATA.__data: 0x15c8
-  __DATA.__common: 0x3240
+  __DATA.__common: 0x3250
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts

   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/Versions/A/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreSymbolication.framework/Versions/A/CoreSymbolication
   - /System/Library/PrivateFrameworks/CrashReporterSupport.framework/Versions/A/CrashReporterSupport
+  - /System/Library/PrivateFrameworks/IconServices.framework/Versions/A/IconServices
   - /System/Library/PrivateFrameworks/MusicKitInternal.framework/Versions/A/MusicKitInternal
   - /System/Library/PrivateFrameworks/OnBoardingKit.framework/Versions/A/OnBoardingKit
   - /System/Library/PrivateFrameworks/PhotosFormats.framework/Versions/A/PhotosFormats

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 17698
+  Functions: 17731
   Symbols:   1305
-  CStrings:  13297
+  CStrings:  13316
 
CStrings:
+ "%s/AMPLibraryAgent-1.7.1.18"
+ "(mKind == kRemoteLibraryKind_CloudMusic)"
+ "(mState == eGettingAlbums || mState == eGettingArtists || mState == eQueryAlbum)"
+ "(outChangeDataVar->mValidFields & kAMPLPlaylistChangeDataValidField_Var_ArtworkVariantsInfo) != kAMPLPlaylistChangeDataValidFields_Var_None"
+ "**ERROR**: %{public}s Client> MakeRequest(eDAAPDatabaseGroupsRequest - query) failed with status:%d"
+ "**ERROR**: %{public}s Client> MakeRequest(eDAAPDatabaseItemsRequest - query) failed with status:%d"
+ "**ERROR**: %{public}s Client> ParseDAAPResponse(kDAAPDatabaseSongsResponseCode - query) failed with status:%d"
+ "**ERROR**: %{public}s Client> ParseDAAPResponse(kDAAPGroupAlbumsResponseCode - query) failed with status:%d"
+ "**ERROR**: CEC - CloudDAAPStoreRequest::Setup(%{public}s) failed! status:%d"
+ "**ERROR**: CEC - MakeCollaborationEditBody() failed! type:%{public}s status:%d "
+ "**ERROR**: CEC - MakeEditItemsBody() failed! type:%{public}s  status:%d"
+ "**ERROR**: CEC - SendCloudDAAPStoreRequest(%{public}s) failed! status:%d"
+ "**ERROR**: CEC::SetupRequestParameters(%{public}s) failed! status:%d"
+ "**ERROR**: CPC - CloudDAAPStoreRequest::Setup(%{public}s) failed! status:%d"
+ "**ERROR**: CPC - SendCloudDAAPStoreRequest(%{public}s) failed! status:%d"
+ "**ERROR**: CSC - CloudDAAPStoreRequest::Setup(%{public}s) failed! status:%d"
+ "**ERROR**: CSC - MakeAlbumQueryBody(%{public}s) failed! status:%d"
+ "**ERROR**: CSC - MakeItemsQueryBody(%zu) failed! status:%d"
+ "**ERROR**: CSC - SendCloudDAAPStoreRequest(%{public}s) failed! status:%d"
+ "**ERROR**: CSC::SetupRequestParameters(%{public}s) failed! status:%d"
+ "**ERROR**: CloudClientSyncCommandData::GetSetupData() invalid after setting up! reason: %{public}s "
+ "**ERROR**: Failed INVALID Push: %{public}s for %{public}s"
+ "**ERROR**: Failed to Validate() ClientCommandProcessor::Command supplied to EnqueueCommand()! failure: %{public}s ClientCommandType:%d ccp:%{public}s"
+ "**ERROR**: UNEXPECTED REASON: %{public}s"
+ "**ERROR**: UNKNOWN REQUEST TYPE: %{public}s "
+ "**ERROR**: Unexpected client kind for APNSContentSyncUpdate! kind:%{public}s"
+ "**ERROR**: WaitForLockedCompletion() failed! status:%d client:%{public}s request:%{public}s"
+ "1.7.1"
+ "1.7.1.18"
+ "13.7.1.18"
+ "AMPLibraryAgent version: 1.7.1.18"
+ "DonateLibraryToSpotlight(): Donating all items because DB data version has changed: old = %u, new = %u"
+ "IsFavoritesPlaylist(playlist) || IsCloudMusicEditablePlaylist(playlist)"
+ "Missing mData when requiresData is true"
+ "Signaling clean exit."
+ "artwork-variants-info"
+ "artworkVariantsInfo"
+ "cloud-daap> Starting %{public}s cloud request for %{public}s"
+ "com.apple.AMPLibraryAgent.clientconnection-%S-%u"
+ "dmap.itemid,dmap.containeritemid"
+ "dmap.itemid,dmap.itemname,dmap.persistentid,dmap.parentcontainerid,com.apple.itunes.is-podcast-playlist,com.apple.itunes.special-playlist,com.apple.itunes.playlist-kind,com.apple.itunes.playlist-data,com.apple.itunes.genius-seed-track-id-listing"
+ "eQueryAlbum"
+ "eQueryItems"
+ "groupType"
+ "icml> Updated channel name for album. album:%{public}s existing name:%{public}s new name:%{public}s"
+ "inCommand.Validate(failureReason)"
+ "inDAAPRequest != nullptr"
+ "inRequestParams.isValid()"
+ "inRequestReason != kExtDAAP_CloudRequestReason_APNSContentChannelPush"
+ "inSetupData.valid()"
+ "jojo"
+ "kExtDAAP_CloudRequestReason_APNSContentChannelPush"
+ "kStoreDAAPAlbumTraitsCode"
+ "kStoreDAAPDisplayCountdownTimerCode"
+ "kStoreDAAPItemTraitsCode"
+ "log_sharingclient_daaploading"
+ "log_sharingclient_daapparsing"
+ "mExpectedReleaseDate != 0"
+ "mFireDelayTime < 0"
+ "mType == eUnknownCommandValue"
+ "outBodyData.get()"
+ "outSetupData.valid()"
+ "systemYellowColor"
- "%@=%u"
- "%@databases"
- "%@databases/%u/add-favorite"
- "%@databases/%u/cloud-add"
- "%@databases/%u/collaboration"
- "%@databases/%u/containers"
- "%@databases/%u/containers/%u/items"
- "%@databases/%u/edit"
- "%@databases/%u/groups"
- "%@databases/%u/items"
- "%@databases/%u/pins"
- "%@databases/%u/process"
- "%@databases/%u/subscribed-containers"
- "%@server-info"
- "%@update"
- "%S://%S:%u%S/"
- "%s.clientconnection-%s-%u"
- "%s/AMPLibraryAgent-1.7.0.161"
- "&%@"
- "&%@="
- "&%@=%S"
- "&%@=%u"
- "(mState == eGettingAlbums || mState == eGettingArtists)"
- "**ERROR**: Failed INVALID Push: %{public}s for %s"
- "**ERROR**: Failed to Validate() ClientCommandProcessor::Command supplied to EnqueueCommand()! ClientCommandType:%d ccp:%{public}s"
- "**ERROR**: MakeCollaborationEditBody() failed! type:%u status:%d "
- "**ERROR**: MakeEditItemsBody() failed! type:%u status:%d "
- "**ERROR**: UNEXPECTED REASON: %u"
- "1.7"
- "1.7.0.161"
- "13.7.0.161"
- "AMPLibraryAgent version: 1.7.0.161"
- "DonateLibraryToSpotlight(): Donating all items because DB data versionhas changed: old = %u, new = %u"
- "IsCloudMusicEditablePlaylist(playlist)"
- "groupType=albums&meta=all"
- "groupType=artists&meta=all"
- "inCommand.Validate()"
- "kStoreDAAPCollaborativePlaylistInvitationTokenCode"
- "log-daaploading"
- "log-daapparsing"
- "mBaseURL != nullptr"
- "meta=dmap.itemid,dmap.containeritemid"
- "meta=dmap.itemid,dmap.itemname,dmap.persistentid,dmap.parentcontainerid,com.apple.itunes.is-podcast-playlist,com.apple.itunes.special-playlist,com.apple.itunes.playlist-kind,com.apple.itunes.playlist-data,com.apple.itunes.genius-seed-track-id-listing"
- "type=music&meta="
```
