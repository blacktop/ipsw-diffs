## MediaToolbox

> `/System/Library/Frameworks/MediaToolbox.framework/MediaToolbox`

```diff

-3210.14.1.11.3
-  __TEXT.__text: 0xf2533c
-  __TEXT.__auth_stubs: 0xbbe0
+3210.17.1.11.1
+  __TEXT.__text: 0xf290d8
+  __TEXT.__auth_stubs: 0xbbf0
   __TEXT.__objc_methlist: 0x225c
-  __TEXT.__cstring: 0x118eaf
-  __TEXT.__const: 0x54fa0
-  __TEXT.__oslogstring: 0x12c7ad
+  __TEXT.__cstring: 0x11949d
+  __TEXT.__const: 0x54fc0
+  __TEXT.__oslogstring: 0x12cdb1
   __TEXT.__ustring: 0x1f8
   __TEXT.__gcc_except_tab: 0x1358
   __TEXT.__dlopen_cstrs: 0x166
-  __TEXT.__unwind_info: 0x137c0
+  __TEXT.__unwind_info: 0x13830
   __TEXT.__eh_frame: 0x44f8
   __TEXT.__objc_classname: 0x850
   __TEXT.__objc_methname: 0x601b
   __TEXT.__objc_methtype: 0x2501
   __TEXT.__objc_stubs: 0x5a20
-  __DATA_CONST.__got: 0x3548
-  __DATA_CONST.__const: 0x220c0
+  __DATA_CONST.__got: 0x3550
+  __DATA_CONST.__const: 0x22280
   __DATA_CONST.__objc_classlist: 0x218
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x1d8
   __DATA_CONST.__objc_arraydata: 0x30
-  __AUTH_CONST.__auth_got: 0x5e08
+  __AUTH_CONST.__auth_got: 0x5e10
   __AUTH_CONST.__auth_ptr: 0x50
-  __AUTH_CONST.__const: 0x3e450
-  __AUTH_CONST.__cfstring: 0x50760
+  __AUTH_CONST.__const: 0x3e510
+  __AUTH_CONST.__cfstring: 0x50900
   __AUTH_CONST.__objc_const: 0x4c90
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_doubleobj: 0x10

   __AUTH.__data: 0x9c8
   __DATA.__objc_ivar: 0x2e4
   __DATA.__data: 0x183b8
-  __DATA.__bss: 0x23d8
-  __DATA.__common: 0x2ee0
+  __DATA.__bss: 0x23e8
+  __DATA.__common: 0x2ef0
   __DATA_DIRTY.__objc_data: 0x4b0
   __DATA_DIRTY.__data: 0x430
   __DATA_DIRTY.__common: 0x360
-  __DATA_DIRTY.__bss: 0x18c8
+  __DATA_DIRTY.__bss: 0x1940
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 41827
-  Symbols:   58193
-  CStrings:  53135
+  Functions: 41868
+  Symbols:   58246
+  CStrings:  53199
 
Symbols:
+ _FigXPCServerRetainNeighborObjectFromIDWithProcessID
+ _kFigAssetDownloaderProperty_MediaSelectionArray
+ _kFigAudioQueueProperty_IgnoreAudioDeviceLatencyInStartupSync
+ _kFigAudioRenderPipelineProperty_IgnoreAudioDeviceLatencyInStartupSync
+ _kFigPlaybackItemOptionKey_IntegratedSessionID
+ _kFigPlayerProperty_IgnoreAudioDeviceLatencyInStartupSync
+ _kFigXPCServerOption_AllowSecondaryConnections
CStrings:
+ "    "
+ " enableTelemetry=YES item=%s, itemRef=%llu"
+ "! memoryOrigin"
+ "! outByteStream"
+ "! outByteStreamDetails"
+ "<<<< FAQ >>>> %s: [%p:%p] %{public}s ignoreAudioDeviceLatencyInStartupSync is true, so skipping to query for device latency"
+ "<<<< FigFilePlayer >>>> %s: [%p] %{public}s ignoreAudioDeviceLatencyInStartupSync changing to %s."
+ "<<<< FigItemIntegratedTimeline >>>> %s: %p: %f"
+ "<<<< FigItemIntegratedTimeline >>>> %s: %p: seeking to target time %1.5g from %1.5g, source time %1.5g, source segment %@, minSnapTime %1.5g, maxSnapTime %1.5g, seekID %d"
+ "<<<< FigPlayerInterstitial >>>> %s: %p: primary was gated to %f and received a time jump to %f, proceed to regate"
+ "<<<< FigPlayer_AP >>>> %s: [%p] %{public}s Before latch airplayShadowMovieTimebase at %f"
+ "<<<< FigStreamPlayer >>>> %s: [%p|%{public}s]: auto-selection defaults changed, will re-apply auto-selection to play queue items"
+ "<<<< FigStreamPlayer >>>> %s: [QE Critical][%p|%{public}s]: <%p|%{public}s>: Couldn't obtain audio stream description for media type [%c%c%c%c]"
+ "<<<< FigStreamPlayer >>>> %s: [QE Critical][%p|%{public}s]: <%p|%{public}s>: [AudioFormat %c%c%c%c is %s decodable] [AudioChannels %d] [Spatialization Eligible %s] [Client permits multi: %s, stereo: %s] [Spatialization %s] [StereoSpatialization %s] [Rendition %@] [SampleRate %d] [BitDepth %d]"
+ "<<<< HLSPersistentStore >>>> %s: %@"
+ "<<<< HLSPersistentStore >>>> %s: %s: [%0.6f] [%p]: [fileFork:pathnum] %p:%@ %{private}@ [HOLDTIME = %0.6f] (%d/%d/%d acq/blk/err) [acquireTime = %0.6f] [unlockTime = %0.6f]"
+ "<<<< HLSPersistentStore >>>> %s: Inconsistency: no record of flock() attempt. unlockrace with lock?"
+ "<<<< HLSPersistentStore >>>> %s: LOG STATE: empty, stopping timer"
+ "<<<< HLSPersistentStore >>>> %s: LOG STATE: hlspersistent_flock_logging_trace >= 5: force log dump"
+ "<<<< HLSPersistentStore >>>> %s: LOG STATE: will fire again in %0.3f seconds"
+ "<<<< HLSPersistentStore >>>> %s: [%p] Unexpected NULL logRecord"
+ "<<<< HLSPersistentStore >>>> %s: flock() HISTORY"
+ "<<<< HLSPersistentStore >>>> %s: flock() HISTORY DONE"
+ "<<<< HLSPersistentStore >>>> %s: flock() IN PROGRESS"
+ "<<<< HLSPersistentStore >>>> %s: flock() IN PROGRESS DONE"
+ "<unknown>"
+ "AssetDownloaderProperty_MediaSelectionArray"
+ "Could not obtain FigByteStreamServer MemoryPool"
+ "Couldn't allocate FigServedByteStreamState"
+ "CreateServedByteStreamState"
+ "Expected a valid FigServedByteStreamState"
+ "FigByteStreamServer"
+ "FigByteStreamServerCopyByteStreamForID"
+ "FigHLSPersistentStore held flock to root.xml for too long"
+ "FigServedByteStreamState"
+ "FigServedByteStreamState %p"
+ "HELD"
+ "IgnoreAudioDeviceLatencyInStartupSync"
+ "IgnoreAudioDeviceLatencyInStartupSync changed"
+ "IgnoreAudioDeviceLatencyInStartupSync not a CFBoolean"
+ "IntegratedSessionID"
+ "InterCnt"
+ "Media playback or download encountered a potential hang state"
+ "NULL eventsWithOfflineURLsOut"
+ "Not a FigByteStream"
+ "PlayerPerformance_ItemLikelyToKeepUp"
+ "While accessing FigHLSPersistentStore, held flock to root.xml for too long. Should have been unlocked quickly"
+ "cannot update media selection array after alternate has been set"
+ "com.apple.coremedia.logging.flock"
+ "compositionTableTrack_createAvailableMetadataReaderPropertiesArray"
+ "compositionTable_createAvailableMetadataReaderPropertiesArray"
+ "fl_logLockAcquisition"
+ "fl_logUnlock"
+ "flockLoggerTimerCallback"
+ "flockLogger_Log"
+ "flockLogger_LogAll"
+ "flockLogger_logBacktraceArrayApplierFunc"
+ "fpic_CopyEventsWithOfflineURLsIfNecessary"
+ "fpic_ensurePrimaryPlaybackGateForTimeJumpDuringIntendedSeek"
+ "hlspersistent_flock_logging_trace"
+ "invalid processPID"
+ "item=%s, itemRef=%llu"
+ "kRTCReportingSessionInfoSamplingUUIID"
+ "not CFArray for metadata"
+ "object is not the expected CMByteStream type"
+ "sad_setMediaSelectionArray"
+ "tfac2IPauseBufSet"
+ "tfac2IPauseBufUnset"
- "<<<< FigItemIntegratedTimeline >>>> %s: %p: seeking to target time %1.5g, source time %1.5g, source segment %@, minSnapTime %1.5g, maxSnapTime %1.5g, seekID %d"
- "<<<< FigStreamPlayer >>>> %s: [%p|%{public}s] <%p|%{public}s>: auto-selection defaults changed, will re-apply auto-selection to current item"
- "<<<< FigStreamPlayer >>>> %s: [QE Critical][%p|%{public}s]: <%p|%{public}s>: [AudioFormat %c%c%c%c] [AudioChannels %d] [Spatialization Eligible %s] [Client permits multi: %s, stereo: %s] [Spatialization %s] [StereoSpatialization %s] [Rendition %@] [SampleRate %d] [BitDepth %d]"
- "Could not obtain CommonMemoryPool"

```
