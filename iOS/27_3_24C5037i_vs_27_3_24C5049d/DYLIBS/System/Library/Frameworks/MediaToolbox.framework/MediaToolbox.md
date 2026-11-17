## MediaToolbox

> `/System/Library/Frameworks/MediaToolbox.framework/MediaToolbox`

```diff

-3395.5.1.0.0
-  __TEXT.__text: 0xbe1d14
+3395.8.1.0.0
+  __TEXT.__text: 0xbe317c
   __TEXT.__lazy_helpers: 0x3618
   __TEXT.__objc_methlist: 0x2b7c
   __TEXT.__const: 0x297f0
-  __TEXT.__cstring: 0x71c77
-  __TEXT.__oslogstring: 0x67ad4
+  __TEXT.__cstring: 0x71d47
+  __TEXT.__oslogstring: 0x67c68
   __TEXT.__gcc_except_tab: 0x1648
   __TEXT.__dlopen_cstrs: 0x32e
   __TEXT.__ustring: 0x24e

   __TEXT.__swift_as_entry: 0x10
   __TEXT.__swift_as_ret: 0x10
   __TEXT.__swift_as_cont: 0x30
-  __TEXT.__unwind_info: 0x22030
+  __TEXT.__unwind_info: 0x220a8
   __TEXT.__eh_frame: 0x478
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x24d18
+  __DATA_CONST.__const: 0x24d70
   __DATA_CONST.__objc_classlist: 0x228
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x24a8
+  __DATA_CONST.__objc_selrefs: 0x24b0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x1f0
   __DATA_CONST.__objc_arraydata: 0x50
   __DATA_CONST.__got: 0x4970
   __AUTH_CONST.__const: 0x47f08
-  __AUTH_CONST.__cfstring: 0x50b40
+  __AUTH_CONST.__cfstring: 0x50ba0
   __AUTH_CONST.__objc_const: 0x59c8
   __AUTH_CONST.__weak_auth_got: 0x20
   __AUTH_CONST.__lazy_load_got: 0x4e0

   __DATA.__common: 0x20d8
   __DATA_DIRTY.__objc_data: 0x640
   __DATA_DIRTY.__data: 0x50c
-  __DATA_DIRTY.__bss: 0x1b90
+  __DATA_DIRTY.__bss: 0x1b98
   __DATA_DIRTY.__common: 0x220
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 43839
-  Symbols:   44409
-  CStrings:  21039
+  Functions: 43864
+  Symbols:   44430
+  CStrings:  21048
 
Symbols:
+ GCC_except_table71
+ _FigCFHTTPGetHTTPRequestFlagsFromAssetCreationOptions
+ _FigRemakerQueueMarkInvalidationPending
+ _URLAssetCreateURLStorageSessionOptionsFromAssetCreationOptions
+ ___figAssetSetUpConnectionForURLAsyncCompleteWithError_block_invoke
+ ___frs_invalidateClientAsync_block_invoke
+ ___frs_mediaServicesDeathListener_block_invoke
+ _assetReader_copyChannelByExtractionID
+ _assetWriter_copyChannelByWriterTrackID
+ _assetXPCServer_checkNetworkAccountingDelegationPermitted
+ _assetXPCServer_setDerivedClientBundleIdentifierIfMissing
+ _frs_clientListHasSharedSessionClientForPid
+ _frs_invalidateClientAsync
+ _frs_markClientInvalidationPending
+ _frs_mediaServicesDeathListener
+ _frs_postDeathNotificationToClient
+ _frs_recordMediaServicesDeathInRunningStats
+ _frs_sharedSessionAddClient
+ _frs_sharedSessionRemoveSession
+ _kFigHTTPRequestCreateOption_ResourceTimeout
+ _kFigPlayerInterstitialNotification_EventItemIntegratedTimelineOffsetsChanged
+ _kFigTrialFactor_MediaRequestTimeoutForDownload
+ _queuedRemaker_appendPendingTrack
+ _queuedRemaker_applyPendingFormatWriterTrackProperty
+ _remakerFamily_copyChannelBySourceTrackID
+ _remakerFamily_trackArrayGetAndRetainTrackByIndex
+ _remakerFamily_trackArrayGetCount
+ _saig_OpenOrRestartPump
- GCC_except_table70
- ___FigAssetSetUpConnectionForURLAsync_block_invoke
- _assetReader_getChannelByExtractionID
- _assetWriter_getChannelByWriterTrackID
- _frs_invalidateSubObject
- _queuedRemaker_setPendingFormatWriterTrackProperty
- _remakerFamily_getChannelBySourceTrackID
CStrings:
+ "<<<< RemakerQueue >>>> %s: [%p]:[EXP]:Marking invalidation pending"
+ "<<<< RemakerServer >>>> %s: [EXP]:Create client [%p] %{public}s subObject [%p] PID [%d]"
+ "<<<< RemakerServer >>>> %s: [EXP]:Finalize Client [%p] %{public}s Releasing subObject [%p]"
+ "<<<< RemakerServer >>>> %s: [EXP]:NoInterruptions client [%p] %{public}s could not attach to shared session for death notification, err %d"
+ "<<<< RemakerServer >>>> %s: [EXP]:Stop and Fail Client [%p] %{public}s, err = %d subObject %{public}s:[%p]"
+ "<<<< RemakerServer >>>> %s: [EXP]:media services died, will invalidate client [%p] %{public}s pid [%d] subObject %{public}s:[%p]"
+ "<<<< RemakerServer >>>> %s: [EXP]:task pid [%u] client %{public}s terminated"
+ "<<<< RemakerServer >>>> %s: [EXP]:task pid [%u] client %{public}s unexpected app state %u %{public}s"
+ "FHRP_ResourceTimeout"
+ "FigRemakerQueueMarkInvalidationPending"
+ "com.apple.coremedia.remakerserver.invalidationQueue"
+ "fpiEventItemOffsetsChanged"
+ "frs_mediaServicesDeathListener"
+ "frs_sharedSessionRemoveSession"
+ "mediaRequestTimeoutForDownload"
- "<<<< RemakerServer >>>> %s: [EXP]:Create client [%p] subObject [%p] PID [%d]"
- "<<<< RemakerServer >>>> %s: [EXP]:Finalize Client [%p] Releasing subObject [%p]"
- "<<<< RemakerServer >>>> %s: [EXP]:Stop and Fail Client [%p], err = %d subObject %{public}s:[%p]"
- "<<<< RemakerServer >>>> %s: [EXP]:task pid [%u] terminated"
- "<<<< RemakerServer >>>> %s: [EXP]:task pid [%u] unexpected app state %u %{public}s"
- "frs_sharedSessionRemoveClient"
```
