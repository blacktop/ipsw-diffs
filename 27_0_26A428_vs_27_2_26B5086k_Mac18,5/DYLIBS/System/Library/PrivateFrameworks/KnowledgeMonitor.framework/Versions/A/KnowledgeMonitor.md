## KnowledgeMonitor

> `/System/Library/PrivateFrameworks/KnowledgeMonitor.framework/Versions/A/KnowledgeMonitor`

```diff

-477.0.1.0.0
-  __TEXT.__text: 0x1b7f4
-  __TEXT.__objc_methlist: 0x1f14
-  __TEXT.__const: 0x110
-  __TEXT.__gcc_except_tab: 0x45c
-  __TEXT.__cstring: 0x16ab
-  __TEXT.__oslogstring: 0x1a4f
-  __TEXT.__unwind_info: 0x918
+480.0.0.0.0
+  __TEXT.__text: 0x1be84
+  __TEXT.__objc_methlist: 0x1f1c
+  __TEXT.__const: 0x108
+  __TEXT.__gcc_except_tab: 0x460
+  __TEXT.__cstring: 0x16b5
+  __TEXT.__oslogstring: 0x1b2d
+  __TEXT.__unwind_info: 0x928
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0xe0
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x16c0
+  __DATA_CONST.__objc_selrefs: 0x16c8
   __DATA_CONST.__objc_superrefs: 0xb8
   __DATA_CONST.__objc_arraydata: 0x40
-  __DATA_CONST.__got: 0x3d0
+  __DATA_CONST.__got: 0x428
   __AUTH_CONST.__const: 0x730
-  __AUTH_CONST.__cfstring: 0xd80
+  __AUTH_CONST.__cfstring: 0xdc0
   __AUTH_CONST.__objc_const: 0x2ff8
   __AUTH_CONST.__objc_intobj: 0x108
   __AUTH_CONST.__objc_arrayobj: 0x90

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 759
-  Symbols:   1946
-  CStrings:  313
+  Functions: 762
+  Symbols:   1960
+  CStrings:  317
 
Symbols:
+ -[_DKApplicationMonitorBase updateBiomeAppInFocusWithStopEventAtTimestamp:reason:transitionReason:]
+ -[_DKNowPlayingMonitor saveBMEventWithCurrent:outputDevices:artistStoreIdentifier:albumStoreIdentifier:strictMediaType:contentType:excludeFromSuggestions:]
+ _MRNowPlayingInfoContentTypeBook
+ _MRNowPlayingInfoContentTypeGeneric
+ _MRNowPlayingInfoContentTypeHomeMedia
+ _MRNowPlayingInfoContentTypeMovie
+ _MRNowPlayingInfoContentTypeMusic
+ _MRNowPlayingInfoContentTypePodcast
+ _MRNowPlayingInfoContentTypeRadio
+ _MRNowPlayingInfoContentTypeTVShow
+ _MRNowPlayingInfoMediaTypeAudio
+ _MRNowPlayingInfoMediaTypeVideo
+ _OUTLINED_FUNCTION_4
+ ___block_descriptor_112_e8_32s40s48s56s64r72r80r88r96r104r_e29_v24?0^{__CFDictionary=}8^v16l
+ ___block_descriptor_120_e8_32s40s48s56r64r72r80r88r96r104r112r_e5_v8?0l
+ ___block_descriptor_40_e8_32w_e5_v8?0l
+ ___copy_helper_block_e8_32s40s48s56r64r72r80r88r96r104r112r
+ ___copy_helper_block_e8_32s40s48s56s64r72r80r88r96r104r
+ ___destroy_helper_block_e8_32s40s48s56r64r72r80r88r96r104r112r
+ ___destroy_helper_block_e8_32s40s48s56s64r72r80r88r96r104r
+ _kMRMediaRemoteNowPlayingInfoContentType
+ _kMRMediaRemoteNowPlayingInfoStrictMediaType
+ _objc_msgSend$initWithLaunchReason:type:starting:absoluteTimestamp:bundleID:parentBundleID:extensionHostID:shortVersionString:exactVersionString:dyldPlatform:isNativeArchitecture:displayType:transitionReason:
+ _objc_msgSend$saveBMEventWithCurrent:outputDevices:artistStoreIdentifier:albumStoreIdentifier:strictMediaType:contentType:excludeFromSuggestions:
+ _objc_msgSend$updateBiomeAppInFocusWithStopEventAtTimestamp:reason:transitionReason:
- -[_DKNowPlayingMonitor saveBMEventWithCurrent:outputDevices:artistStoreIdentifier:albumStoreIdentifier:excludeFromSuggestions:]
- _OBJC_CLASS_$_NSTimer
- ___block_descriptor_104_e8_32s40s48s56r64r72r80r88r96r_e5_v8?0l
- ___block_descriptor_40_e8_32w_e17_v16?0"NSTimer"8l
- ___block_descriptor_96_e8_32s40s48s56s64r72r80r88r_e29_v24?0^{__CFDictionary=}8^v16l
- ___copy_helper_block_e8_32s40s48s56r64r72r80r88r96r
- ___copy_helper_block_e8_32s40s48s56s64r72r80r88r
- ___destroy_helper_block_e8_32s40s48s56r64r72r80r88r96r
- ___destroy_helper_block_e8_32s40s48s56s64r72r80r88r
- _objc_msgSend$saveBMEventWithCurrent:outputDevices:artistStoreIdentifier:albumStoreIdentifier:excludeFromSuggestions:
- _objc_msgSend$scheduledTimerWithTimeInterval:repeats:block:
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/DuetKnowledgeCollector/KnowledgeMonitor/KnowledgeMonitor/Monitors/_DKBacklightMonitor.m:200"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/DuetKnowledgeCollector/KnowledgeMonitor/KnowledgeMonitor/Monitors/_DKNowPlayingMonitor.m:502"
+ "BMMediaNowPlayingMediaSubtype: Unrecognized value for contentType: %{public}@"
+ "BMMediaNowPlayingMediaType: Unrecognized value for strictMediaType: %{public}@"
+ "Last alive date %{public}@ predates boot %{public}@; ignoring it"
+ "contentType"
+ "strictMediaType"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/DuetKnowledgeCollector/KnowledgeMonitor/KnowledgeMonitor/Monitors/_DKBacklightMonitor.m:193"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/DuetKnowledgeCollector/KnowledgeMonitor/KnowledgeMonitor/Monitors/_DKNowPlayingMonitor.m:494"
- "v16@?0@\"NSTimer\"8"
```
