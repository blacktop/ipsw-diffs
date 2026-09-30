## MediaToolbox

> `/System/Library/Frameworks/MediaToolbox.framework/MediaToolbox`

```diff

-3210.18.2.11.3
-  __TEXT.__text: 0xa280e0
+3210.19.1.1.3
+  __TEXT.__text: 0xa27b20
   __TEXT.__auth_stubs: 0xbab0
   __TEXT.__objc_methlist: 0x225c
-  __TEXT.__cstring: 0x5ebf6
-  __TEXT.__const: 0x54da0
-  __TEXT.__oslogstring: 0x43945
+  __TEXT.__cstring: 0x5eb48
+  __TEXT.__const: 0x54d90
+  __TEXT.__oslogstring: 0x43837
   __TEXT.__ustring: 0x1f8
   __TEXT.__gcc_except_tab: 0xcd4
   __TEXT.__dlopen_cstrs: 0x166
-  __TEXT.__unwind_info: 0x127e0
+  __TEXT.__unwind_info: 0x127b8
   __TEXT.__eh_frame: 0x44e0
   __TEXT.__objc_classname: 0x850
-  __TEXT.__objc_methname: 0x5fb1
+  __TEXT.__objc_methname: 0x5fd5
   __TEXT.__objc_methtype: 0x2501
-  __TEXT.__objc_stubs: 0x5940
+  __TEXT.__objc_stubs: 0x5960
   __DATA_CONST.__got: 0x3558
-  __DATA_CONST.__const: 0x22020
+  __DATA_CONST.__const: 0x21f88
   __DATA_CONST.__objc_classlist: 0x218
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1d48
+  __DATA_CONST.__objc_selrefs: 0x1d50
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x1d8
   __DATA_CONST.__objc_arraydata: 0x30
   __AUTH_CONST.__auth_got: 0x5d70
   __AUTH_CONST.__auth_ptr: 0x58
-  __AUTH_CONST.__const: 0x3e5b0
-  __AUTH_CONST.__cfstring: 0x4d7a0
+  __AUTH_CONST.__const: 0x3e590
+  __AUTH_CONST.__cfstring: 0x4d780
   __AUTH_CONST.__objc_const: 0x4c90
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_doubleobj: 0x10

   __AUTH.__data: 0x9c8
   __DATA.__objc_ivar: 0x2e4
   __DATA.__data: 0x18378
-  __DATA.__bss: 0x2248
+  __DATA.__bss: 0x2238
   __DATA.__common: 0x1998
   __DATA_DIRTY.__objc_data: 0x4b0
   __DATA_DIRTY.__data: 0x460
-  __DATA_DIRTY.__bss: 0x19d8
+  __DATA_DIRTY.__bss: 0x1990
   __DATA_DIRTY.__common: 0x130
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 30240
-  Symbols:   49664
-  CStrings:  19409
+  Functions: 30225
+  Symbols:   49649
+  CStrings:  19402
 
Symbols:
+ _FigAlternateCopyStreamBitrateCurve
+ _FigAlternateSetStreamBitrateCurve
+ _kFigAlternateMonitorForPlaybackBitrateProperty_AudioStreamPlaylist
+ _kFigAssetDownloaderCreateOption_InterstitialMediaSelectionCriteria
- _FigAlternateCopyMainStreamBitrateCurve
- _FigAlternateSetMainStreamBitrateCurve
- _kFigAssetDownloadConfig_DownloadsInterstitialAssets
CStrings:
+ "1.1"
+ "<<<< FigStreamPlayer >>>> %s: [%p|%{public}s]  %@ unknown"
+ "<<<< FigStreamPlayer >>>> %s: [%p|%{public}s] <%p|%{public}s>: Setting PriorImageQueueGauge %p"
+ "AfmfpbProperty_AudioStreamPlaylist"
+ "AssetDownloaderCreateOption_InterstitialMediaSelectionCriteria"
+ "compressedDataUsingAlgorithm:error:"
+ "compression"
+ "fpfs_deferredSeekableTimeRangeChanged"
+ "fpfs_deferredSuggestedAlternateNote"
+ "fpfsi_pumpNotificationHandler"
+ "fpfsi_updatePriorImageQueueGaugeOnVideoRenderPipelines"
+ "zlib"
- "    "
- "<<<< HLSPersistentStore >>>> %s: %@"
- "<<<< HLSPersistentStore >>>> %s: %s: [%0.6f] [%p]: [fileFork:pathnum] %p:%@ %{private}@ [HOLDTIME = %0.6f] (%d/%d/%d acq/blk/err) [acquireTime = %0.6f] [unlockTime = %0.6f]"
- "<<<< HLSPersistentStore >>>> %s: flock() HISTORY"
- "<<<< HLSPersistentStore >>>> %s: flock() HISTORY DONE"
- "<<<< HLSPersistentStore >>>> %s: flock() IN PROGRESS"
- "<<<< HLSPersistentStore >>>> %s: flock() IN PROGRESS DONE"
- "<unknown>"
- "FigHLSPersistentStore held flock to root.xml for too long"
- "HELD"
- "Media playback or download encountered a potential hang state"
- "While accessing FigHLSPersistentStore, held flock to root.xml for too long. Should have been unlocked quickly"
- "com.apple.coremedia.logging.flock"
- "flockLogger_Log"
- "flockLogger_LogAll"
- "flockLogger_logBacktraceArrayApplierFunc"
- "fpfs_SeekableTimeRangeChanged"
- "fpfs_SuggestedAlternateNote"
- "hlspersistent_flock_logging_trace"

```
