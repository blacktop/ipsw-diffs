## MediaToolbox

> `/System/Library/Frameworks/MediaToolbox.framework/Versions/A/MediaToolbox`

```diff

-3350.77.5.6.0
-  __TEXT.__text: 0xa285b8
+3385.14.5.2.0
+  __TEXT.__text: 0xa2bee0
   __TEXT.__lazy_helpers: 0x2a0
-  __TEXT.__objc_methlist: 0x22cc
-  __TEXT.__cstring: 0x64754
-  __TEXT.__const: 0x1d750
-  __TEXT.__gcc_except_tab: 0x1428
-  __TEXT.__oslogstring: 0x60776
+  __TEXT.__objc_methlist: 0x22d4
+  __TEXT.__cstring: 0x649c4
+  __TEXT.__const: 0x1d830
+  __TEXT.__gcc_except_tab: 0x1460
+  __TEXT.__oslogstring: 0x60a8a
   __TEXT.__ustring: 0x24e
   __TEXT.__dlopen_cstrs: 0x21c
   __TEXT.__constg_swiftt: 0x234

   __TEXT.__swift_as_ret: 0x10
   __TEXT.__swift_as_cont: 0x30
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x12908
+  __TEXT.__unwind_info: 0x12950
   __TEXT.__eh_frame: 0x408
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1eae8
+  __DATA_CONST.__const: 0x1ebe8
   __DATA_CONST.__objc_classlist: 0x1e0
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1cb8
+  __DATA_CONST.__objc_selrefs: 0x1cc0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x1a8
   __DATA_CONST.__objc_arraydata: 0x30
-  __DATA_CONST.__got: 0x42c0
-  __AUTH_CONST.__const: 0x3ca60
-  __AUTH_CONST.__cfstring: 0x4db80
+  __DATA_CONST.__got: 0x42c8
+  __AUTH_CONST.__const: 0x3cb80
+  __AUTH_CONST.__cfstring: 0x4dde0
   __AUTH_CONST.__objc_const: 0x47a8
   __AUTH_CONST.__weak_auth_got: 0x20
   __AUTH_CONST.__lazy_load_got: 0x38
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_arrayobj: 0x48
-  __AUTH_CONST.__auth_got: 0x5590
+  __AUTH_CONST.__auth_got: 0x55a0
   __AUTH_CONST.__auth_ptr: 0x4f8
-  __AUTH.__objc_data: 0xd20
+  __AUTH.__objc_data: 0xc30
   __AUTH.__data: 0x6c0
   __DATA.__objc_ivar: 0x2b4
   __DATA.__data: 0x2858
   __DATA.__common: 0x1890
-  __DATA.__bss: 0x4860
-  __DATA_DIRTY.__objc_data: 0x5a0
+  __DATA.__bss: 0x48a0
+  __DATA_DIRTY.__objc_data: 0x690
   __DATA_DIRTY.__data: 0x878
   __DATA_DIRTY.__common: 0x5e0
-  __DATA_DIRTY.__bss: 0x1b18
+  __DATA_DIRTY.__bss: 0x1ae8
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate
   - /System/Library/Frameworks/ApplicationServices.framework/Versions/A/ApplicationServices
   - /System/Library/Frameworks/AudioToolbox.framework/Versions/A/AudioToolbox

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 39738
-  Symbols:   11908
-  CStrings:  18932
+  Functions: 39799
+  Symbols:   11915
+  CStrings:  18964
 
Symbols:
+ _FigCFSetCreateFromArray
+ _FigCFSetGetCount
+ _kFigAssetOptionKey_DeferFailuresForCreationTimeAccessCheck
+ _kFigHTTPRequestCreateOption_ConnectionCachePurgeTimeout
+ _kFigMutableMovieCreationOption_DeferFailuresForCreationTimeAccessCheck
+ _kFigVideoCompositorProperty_MaximumPendingVideoCompositionRequests
+ _kFigXPCRemoteClientOption_DoNotMonitorConnection
CStrings:
+ "!"
+ "<<<< FAQ Offline Mixer >>>> %s: [%p] %{public}s called. connected=%ld, FAQs connected=%ld"
+ "<<<< FAQ Offline Mixer >>>> %s: [%p] %{public}s faq: %p aqMixer: %p audioQueue: %p current_connected: %ld FAQs connected: %ld"
+ "<<<< FigCaptionRenderPipeline >>>> %s: %{public}s (%p) non-forced subtitles turned off with non-forced text on display: clearing it"
+ "<<<< FigCaptionRenderPipeline >>>> %s: %{public}s (%p) sbuf PTS: %f duration: %f PlayFormat = %c%c%c%c/%c%c%c%c extendedLanguageTag: %@ %{public}s %{public}s DisplayNonForcedSubtitles: %{public}s WillBeDropped: %{public}s"
+ "<<<< FigStreamPlayer >>>> %s: [%p|%{public}s] <%p|%{public}s>: Video rendition is now the %s rendition"
+ "<<<< FigStreamPlayer >>>> %s: [%p|%{public}s]: gapless-continuation caption auxiliary shares fanOut %p with another item and item is fully cached; seeding from this item's cache and bounding to EndOfItem"
+ "<<<< FigVideoQueue >>>> %s: (%p) not creating layerSync: configuration has no layers to synchronize"
+ "<FigCPECryptorPKD %p (invalidated)>"
+ "<SEGPUMP> %s: %{public}@: defer recovery switch at sequence number %lld to next index file update; current one ends at %lld"
+ "ALT_RENDITION"
+ "AudioQueueOfflineMixerProperty_ConnectedFigAudioQueueCount"
+ "DeferFailuresForCreationTimeAccessCheck"
+ "FHRP_ConnectionCachePurgeTimeout"
+ "IsRendChange"
+ "MaximumPendingVideoCompositionRequests"
+ "PlayTimeAltRendition"
+ "PlayTimeDefault"
+ "VidRendChangeIsClient"
+ "VidRendChangeTime"
+ "VidRendMediaRndrDelay"
+ "VidRendType"
+ "VideoRendChg"
+ "VideoRenditionSwitchCnt"
+ "VideoRenditionSwitchTime"
+ "assetOption_DeferFailuresForCreationTimeAccessCheck"
+ "commandData"
+ "connectionCachePurgeTimeout"
+ "empty"
+ "figCaptionRenderPipelineSetProperty"
+ "fpfsi_RTCReportingUpdateVideoRendition"
+ "isAltVidRend"
+ "manifest default"
+ "non-default alternate"
+ "non-empty"
+ "non-forced"
+ "useNWLoader"
+ "vq_setupLayerSynchronizer"
- "<<<< FAQ Offline Mixer >>>> %s: [%p] %{public}s called.  connected=%ld"
- "<<<< FAQ Offline Mixer >>>> %s: [%p] %{public}s faq: %p aqMixer: %p audioQueue: %p current_connected: %ld"
- "<<<< FigCaptionRenderPipeline >>>> %s: %{public}s (%p) sbuf PTS: %f duration: %f PlayFormat = %c%c%c%c/%c%c%c%c extendedLanguageTag: %@"
- "All"
- "AudioQueueOfflineMixer_ConnectedAudioQueueCount"
- "ClientProcessName"
```
