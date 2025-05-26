## PodcastsFoundation

> `/System/Library/PrivateFrameworks/PodcastsFoundation.framework/PodcastsFoundation`

```diff

-4023.110.9.0.0
-  __TEXT.__text: 0x2f954c
+4023.200.21.0.0
+  __TEXT.__text: 0x2fd060
   __TEXT.__auth_stubs: 0x40b0
-  __TEXT.__objc_methlist: 0x8a6c
-  __TEXT.__const: 0x19ae0
-  __TEXT.__oslogstring: 0x2030
-  __TEXT.__cstring: 0x1ae7e
-  __TEXT.__gcc_except_tab: 0x964
+  __TEXT.__objc_methlist: 0x8b04
+  __TEXT.__const: 0x19c20
+  __TEXT.__oslogstring: 0x2088
+  __TEXT.__cstring: 0x1b01e
+  __TEXT.__gcc_except_tab: 0x9b8
   __TEXT.__ustring: 0x54
   __TEXT.__dlopen_cstrs: 0x70
-  __TEXT.__swift5_typeref: 0xca02
-  __TEXT.__constg_swiftt: 0xa090
-  __TEXT.__swift5_reflstr: 0x77b0
-  __TEXT.__swift5_fieldmd: 0x89e8
-  __TEXT.__swift5_builtin: 0x3c0
+  __TEXT.__swift5_typeref: 0xca40
+  __TEXT.__constg_swiftt: 0xa130
+  __TEXT.__swift5_reflstr: 0x78a0
+  __TEXT.__swift5_fieldmd: 0x8a68
+  __TEXT.__swift5_builtin: 0x3e8
   __TEXT.__swift5_assocty: 0xf48
-  __TEXT.__swift5_proto: 0x111c
-  __TEXT.__swift5_types: 0x8f0
-  __TEXT.__swift5_capture: 0x4c3c
+  __TEXT.__swift5_proto: 0x1124
+  __TEXT.__swift5_types: 0x900
+  __TEXT.__swift5_capture: 0x4c5c
   __TEXT.__swift5_protos: 0x100
   __TEXT.__swift5_mpenum: 0xbc
-  __TEXT.__unwind_info: 0xbe18
+  __TEXT.__unwind_info: 0xbd94
   __TEXT.__eh_frame: 0x71c8
-  __TEXT.__objc_classname: 0xd3c
-  __TEXT.__objc_methname: 0x16c8f
-  __TEXT.__objc_methtype: 0x2917
-  __TEXT.__objc_stubs: 0xd3a0
+  __TEXT.__objc_classname: 0xd31
+  __TEXT.__objc_methname: 0x16e11
+  __TEXT.__objc_methtype: 0x2909
+  __TEXT.__objc_stubs: 0xd340
   __DATA_CONST.__got: 0xb58
-  __DATA_CONST.__const: 0x3458
+  __DATA_CONST.__const: 0x34a8
   __DATA_CONST.__objc_classlist: 0x858
-  __DATA_CONST.__objc_catlist: 0xe8
+  __DATA_CONST.__objc_catlist: 0xf0
   __DATA_CONST.__objc_protolist: 0x2e8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1b730
-  __DATA_CONST.__objc_selrefs: 0x59b0
+  __DATA_CONST.__objc_const: 0x1b7a8
+  __DATA_CONST.__objc_selrefs: 0x5a08
   __DATA_CONST.__objc_arraydata: 0x58
-  __AUTH_CONST.__objc_const: 0x34d0
+  __AUTH_CONST.__objc_const: 0x3558
   __AUTH_CONST.__objc_intobj: 0xa68
-  __AUTH_CONST.__cfstring: 0x94c0
-  __AUTH_CONST.__const: 0x1d760
+  __AUTH_CONST.__cfstring: 0x9600
+  __AUTH_CONST.__const: 0x1d8e0
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH_CONST.__objc_doubleobj: 0x50
   __AUTH_CONST.__auth_ptr: 0x720
   __AUTH_CONST.__auth_got: 0x2068
-  __AUTH.__objc_data: 0x3c38
-  __AUTH.__data: 0x2750
+  __AUTH.__objc_data: 0x3cf8
+  __AUTH.__data: 0x2850
   __DATA.__objc_protorefs: 0x190
   __DATA.__objc_classrefs: 0x698
   __DATA.__objc_superrefs: 0x1c8
-  __DATA.__objc_ivar: 0x468
+  __DATA.__objc_ivar: 0x46c
   __DATA.__objc_data: 0x5e8
-  __DATA.__data: 0x61e8
-  __DATA.__bss: 0x183e8
+  __DATA.__data: 0x6238
+  __DATA.__bss: 0x184f8
   __DATA.__common: 0x58
-  __DATA_DIRTY.__objc_data: 0x44e8
-  __DATA_DIRTY.__data: 0x91f0
-  __DATA_DIRTY.__bss: 0x7d28
+  __DATA_DIRTY.__objc_data: 0x4498
+  __DATA_DIRTY.__data: 0x9048
+  __DATA_DIRTY.__bss: 0x7d38
   __DATA_DIRTY.__common: 0x80
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 19901
-  Symbols:   15089
-  CStrings:  7727
+  Functions: 19894
+  Symbols:   15114
+  CStrings:  7763
 
Symbols:
+ +[PFClientUtil isRunningOnVisionOS]
+ +[PFRestrictionsUtil sharedInstance]
+ -[PFRestrictionsUtil beginListeningForChanges]
+ -[PFRestrictionsUtil endListeningForChanges]
+ -[PFRestrictionsUtil profileConnectionDidReceivePasscodeChangedNotification:userInfo:]
+ -[PFRestrictionsUtil profileConnectionDidReceiveRestrictionChangedNotification:userInfo:]
+ _OBJC_CLASS_$__TtC18PodcastsFoundation18SyncKeysRepository
+ _OBJC_IVAR_$_PFRestrictionsUtil._isListening
+ _OBJC_METACLASS_$__TtC18PodcastsFoundation18SyncKeysRepository
+ __CATEGORY__TtC18PodcastsFoundation18SyncKeysRepository_$_PodcastsFoundation
+ __CLASS_PROPERTIES__TtC18PodcastsFoundation18SyncKeysRepository
+ __DATA__TtC18PodcastsFoundation18SyncKeysRepository
+ __DATA__TtC18PodcastsFoundation21SyncKeysInMemoryStore
+ __DATA__TtC18PodcastsFoundation25SyncKeysUserDefaultsStore
+ __IVARS__TtC18PodcastsFoundation18SyncKeysRepository
+ __IVARS__TtC18PodcastsFoundation21SyncKeysInMemoryStore
+ __IVARS__TtC18PodcastsFoundation25SyncKeysUserDefaultsStore
+ __METACLASS_DATA__TtC18PodcastsFoundation18SyncKeysRepository
+ __METACLASS_DATA__TtC18PodcastsFoundation21SyncKeysInMemoryStore
+ __METACLASS_DATA__TtC18PodcastsFoundation25SyncKeysUserDefaultsStore
+ __MTLogCategoryRestrictions
+ __OBJC_$_CLASS_METHODS_NSUserDefaults(MTAdditions|MTTypes|MTUnitTesting|PodcastsFoundation|PodcastsFoundation1|PodcastsFoundation2)
+ __OBJC_$_CLASS_METHODS__TtC18PodcastsFoundation18SyncKeysRepository
+ __OBJC_$_CLASS_METHODS__TtC18PodcastsFoundation18SyncKeysRepository(PodcastsFoundation|PodcastsFoundation1|PodcastsFoundation2)
+ __OBJC_$_CLASS_PROP_LIST_PFRestrictionsUtil
+ __OBJC_$_INSTANCE_METHODS_NSUserDefaults(MTAdditions|MTTypes|MTUnitTesting|PodcastsFoundation|PodcastsFoundation1|PodcastsFoundation2)
+ __OBJC_$_INSTANCE_METHODS_PFRestrictionsUtil
+ __OBJC_$_INSTANCE_METHODS__TtC18PodcastsFoundation18SyncKeysRepository
+ __OBJC_$_INSTANCE_METHODS__TtC18PodcastsFoundation18SyncKeysRepository(PodcastsFoundation|PodcastsFoundation1|PodcastsFoundation2)
+ __OBJC_$_INSTANCE_VARIABLES_PFRestrictionsUtil
+ ___35+[PFClientUtil isRunningOnVisionOS]_block_invoke
+ ___36+[PFRestrictionsUtil sharedInstance]_block_invoke
+ ___block_literal_global.12
+ ___block_literal_global.26
+ _isRunningOnVisionOS.isRunningOnVisionOS
+ _isRunningOnVisionOS.onceToken
+ _kEpisodeEntitledTranscriptIdentifier
+ _kEpisodeEntitledTranscriptProvider
+ _kEpisodeEntitledTranscriptSnippet
+ _kEpisodeFreeTranscriptIdentifier
+ _kEpisodeFreeTranscriptProvider
+ _kEpisodeFreeTranscriptSnippet
+ _kEpisodeTranscriptIdentifier
+ _kLastUnfollowedDate
+ _objc_msgSend$entitledTranscriptIdentifier
+ _objc_msgSend$freeTranscriptIdentifier
+ _objc_msgSend$markSubscriptionSyncDirty:for:
+ _objc_msgSend$registerObserver:
+ _objc_msgSend$setTranscriptIdentifier:
+ _objc_msgSend$shared
+ _objc_msgSend$unregisterObserver:
+ _symbolic $s18PodcastsFoundation13SyncKeysStoreP
+ _symbolic _____ 18PodcastsFoundation18SyncKeysRepositoryC
+ _symbolic _____ 18PodcastsFoundation21SyncKeysInMemoryStoreC
+ _symbolic _____ 18PodcastsFoundation25SyncKeysUserDefaultsStoreC
+ _symbolic _____ SS18PodcastsFoundationE13CloudSyncKeysO
+ _symbolic _____ So19MTBookmarksSyncTypeV
+ _symbolic _____ So22MTSubscriptionSyncTypeV
+ _symbolic _____Sg9playState_t 18PodcastsFoundation16EpisodePlayStateO
+ _symbolic _____XDXMT 18PodcastsFoundation27MusicSubscriptionInfoLoaderC
+ _symbolic ______p 18PodcastsFoundation13SyncKeysStoreP
- +[MTSyncUtil bookmarksSyncDirtyFlagForSyncType:]
- +[MTSyncUtil isNonFollowedShowsSyncDirtyFlag]
- +[MTSyncUtil isSubscriptionSyncEnabled]
- +[MTSyncUtil playlistSyncDirtyFlag]
- +[MTSyncUtil podcastsDomainVersion]
- +[MTSyncUtil setBookmarksSyncDirtyFlag:syncType:]
- +[MTSyncUtil setNonFollowedShowsSyncDirtyFlag:]
- +[MTSyncUtil setPlaylistSyncDirtyFlag:]
- +[MTSyncUtil setPodcastsDomainVersion:]
- +[MTSyncUtil setSubscriptionSyncDirtyFlag:syncType:]
- +[MTSyncUtil subscriptionSyncDirtyFlagForSyncType:]
- +[MTSyncUtil userDefaultsKeyForBookmarksSyncType:]
- +[MTSyncUtil userDefaultsKeyForSubscriptionSyncType:]
- _OBJC_CLASS_$_MTSyncUtil
- _OBJC_METACLASS_$_MTSyncUtil
- __DATA__TtC18PodcastsFoundation12SyncDefaults
- __DATA__TtC18PodcastsFoundation20InMemorySyncDefaults
- __IVARS__TtC18PodcastsFoundation12SyncDefaults
- __IVARS__TtC18PodcastsFoundation20InMemorySyncDefaults
- __METACLASS_DATA__TtC18PodcastsFoundation12SyncDefaults
- __METACLASS_DATA__TtC18PodcastsFoundation20InMemorySyncDefaults
- __OBJC_$_CLASS_METHODS_MTSyncUtil
- __OBJC_$_CLASS_METHODS_NSUserDefaults(MTAdditions|MTTypes|MTUnitTesting|PodcastsFoundation|PodcastsFoundation1|PodcastsFoundation2|PodcastsFoundation3)
- __OBJC_$_CLASS_PROP_LIST_MTSyncUtil
- __OBJC_$_INSTANCE_METHODS_NSUserDefaults(MTAdditions|MTTypes|MTUnitTesting|PodcastsFoundation|PodcastsFoundation1|PodcastsFoundation2|PodcastsFoundation3)
- __OBJC_CLASS_RO_$_MTSyncUtil
- __OBJC_METACLASS_RO_$_MTSyncUtil
- _objc_msgSend$setSubscriptionSyncDirtyFlag:syncType:
- _objc_msgSend$syncKeysBookmarksDRMSyncIsDirty
- _objc_msgSend$syncKeysBookmarksSyncIsDirty
- _objc_msgSend$syncKeysNonFollowedShowsSyncIsDirty
- _objc_msgSend$syncKeysPlaylistSyncIsDirty
- _objc_msgSend$syncKeysPodcastsDomainVersionKey
- _objc_msgSend$syncKeysSubscriptionSyncIsDirty
- _objc_msgSend$syncKeysSubscriptionV3SyncIsDirty
- _objc_msgSend$userDefaultsKeyForBookmarksSyncType:
- _objc_msgSend$userDefaultsKeyForSubscriptionSyncType:
- _symbolic $s18PodcastsFoundation20SyncDefaultsProtocolP
- _symbolic _____ 18PodcastsFoundation12SyncDefaultsC
- _symbolic _____ 18PodcastsFoundation20InMemorySyncDefaultsC
CStrings:
+ "Clean Only"
+ "Explicit Allowed"
+ "FIXME IF YOU SEE THIS IN LOGS"
+ "Fetching Setting: %@"
+ "Initial Setting load: %@"
+ "No subscription info on disk. Not deleting data."
+ "PodcastsFoundation.SyncKeysRepository"
+ "PotentialSyncDataLoss"
+ "ReadOnlyDeviceMakingSyncChanges"
+ "ReadOnlySyncOnHomePods"
+ "RecentlyUnfollowed"
+ "Reloading Settings"
+ "Setting did change: %@"
+ "SyncAuthenticationError"
+ "T@\"PFRestrictionsUtil\",R"
+ "T@\"_TtC18PodcastsFoundation18SyncKeysRepository\",N,R"
+ "Unable to delete Music Subscription Info with error: %@."
+ "_TtC18PodcastsFoundation18SyncKeysRepository"
+ "_TtC18PodcastsFoundation21SyncKeysInMemoryStore"
+ "_TtC18PodcastsFoundation25SyncKeysUserDefaultsStore"
+ "_isListening"
+ "beginListeningForChanges"
+ "endListeningForChanges"
+ "entitledTranscriptIdentifier"
+ "entitledTranscriptProvider"
+ "entitledTranscriptSnippet"
+ "freeTranscriptIdentifier"
+ "freeTranscriptProvider"
+ "freeTranscriptSnippet"
+ "isBookmarksSyncDirtyFor:"
+ "isRunningOnVisionOS"
+ "isSubscriptionSyncDirtyFor:"
+ "lastUnfollowedDate"
+ "markBookmarksSyncDirty:for:"
+ "markSubscriptionSyncDirty:for:"
+ "profileConnectionDidReceivePasscodeChangedNotification:userInfo:"
+ "profileConnectionDidReceiveRestrictionChangedNotification:userInfo:"
+ "registerObserver:"
+ "setIsBookmarksDRMSyncDirty:"
+ "setIsBookmarksSyncDirty:"
+ "setIsNonFollowedShowsSyncDirty:"
+ "setIsPlaylistSyncDirty:"
+ "setIsSubscriptionSyncEnabled:"
+ "setIsSubscriptionSyncV1Dirty:"
+ "setIsSubscriptionSyncV3Dirty:"
+ "setNonFollowedShowsSyncVersion:"
+ "setTranscriptIdentifier:"
+ "shouldSyncInReadOnlyMode"
+ "syncKeysStore"
+ "transcriptIdentifier"
+ "unregisterObserver:"
- "MTSyncUtil"
- "OAUTH_ERROR_LINKING_UNSUCCESSFUL"
- "_TtC18PodcastsFoundation12SyncDefaults"
- "_TtC18PodcastsFoundation20InMemorySyncDefaults"
- "_podcastsDomainVersion"
- "bookmarksSyncDirtyFlagForSyncType:"
- "isNonFollowedShowsSyncDirtyFlag"
- "playlistSyncDirtyFlag"
- "setBookmarksSyncDirtyFlag:syncType:"
- "setNonFollowedShowsSyncDirtyFlag:"
- "setPlaylistSyncDirtyFlag:"
- "setSubscriptionSyncDirtyFlag:syncType:"
- "subscriptionSyncDirtyFlagForSyncType:"
- "syncKeysBookmarksDRMSyncIsDirty"
- "syncKeysBookmarksSyncIsDirty"
- "syncKeysNonFollowedShowsLastSyncTimestamp"
- "syncKeysNonFollowedShowsSynVersion"
- "syncKeysNonFollowedShowsSyncIsDirty"
- "syncKeysPlaylistSyncIsDirty"
- "syncKeysPodcastsDomainVersionKey"
- "syncKeysSubscriptionSyncIsDirty"
- "syncKeysSubscriptionV3SyncIsDirty"
- "userDefaultsKeyForBookmarksSyncType:"
- "userDefaultsKeyForSubscriptionSyncType:"

```
