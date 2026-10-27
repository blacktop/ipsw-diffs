## AVFCore

> `/System/Library/PrivateFrameworks/AVFCore.framework/Versions/A/AVFCore`

```diff

-2450.77.5.1.0
-  __TEXT.__text: 0x1c1868
-  __TEXT.__objc_methlist: 0x1beb4
-  __TEXT.__gcc_except_tab: 0x98e0
+2475.13.5.1.0
+  __TEXT.__text: 0x1c229c
+  __TEXT.__objc_methlist: 0x1bf94
+  __TEXT.__gcc_except_tab: 0x98d8
   __TEXT.__const: 0x1f2c
-  __TEXT.__cstring: 0x270fb
-  __TEXT.__oslogstring: 0x4a3b
+  __TEXT.__cstring: 0x2713b
+  __TEXT.__oslogstring: 0x4ab6
   __TEXT.__ustring: 0x18
   __TEXT.__swift5_typeref: 0x41a
   __TEXT.__constg_swiftt: 0x290

   __TEXT.__swift5_proto: 0x6c
   __TEXT.__swift5_types: 0x48
   __TEXT.__swift5_capture: 0x60
-  __TEXT.__unwind_info: 0xa328
+  __TEXT.__unwind_info: 0xa370
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x3520
+  __DATA_CONST.__const: 0x3528
   __DATA_CONST.__objc_classlist: 0x1258
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x1c0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb1b0
+  __DATA_CONST.__objc_selrefs: 0xb1f8
   __DATA_CONST.__objc_protorefs: 0x50
   __DATA_CONST.__objc_superrefs: 0xd88
   __DATA_CONST.__objc_arraydata: 0x308
-  __DATA_CONST.__got: 0x46b0
+  __DATA_CONST.__got: 0x46b8
   __AUTH_CONST.__const: 0x3c70
-  __AUTH_CONST.__cfstring: 0x1abc0
-  __AUTH_CONST.__objc_const: 0x32870
+  __AUTH_CONST.__cfstring: 0x1abe0
+  __AUTH_CONST.__objc_const: 0x328e0
   __AUTH_CONST.__objc_intobj: 0x240
   __AUTH_CONST.__objc_doubleobj: 0x30
   __AUTH_CONST.__objc_arrayobj: 0x360
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__auth_got: 0x1e20
   __AUTH_CONST.__auth_ptr: 0x120
-  __AUTH.__objc_data: 0x8f50
-  __AUTH.__data: 0x1e8
-  __DATA.__objc_ivar: 0x27b0
+  __AUTH.__objc_data: 0x82d0
+  __AUTH.__data: 0x1d8
+  __DATA.__objc_ivar: 0x27bc
   __DATA.__data: 0x16b0
   __DATA.__crash_info: 0x148
   __DATA.__common: 0x1c0
   __DATA.__bss: 0x1380
-  __DATA_DIRTY.__objc_data: 0x28a0
+  __DATA_DIRTY.__objc_data: 0x3520
+  __DATA_DIRTY.__data: 0x8
   __DATA_DIRTY.__common: 0x1c0
   __DATA_DIRTY.__bss: 0x1a0
   - /System/Library/Frameworks/AVFAudio.framework/Versions/A/AVFAudio

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 11985
-  Symbols:   28057
-  CStrings:  4283
+  Functions: 12003
+  Symbols:   28094
+  CStrings:  4285
 
Symbols:
+ -[AVAsset _availableMediaCharacteristicsFromMediaSelectionGroupDictionaries:]
+ -[AVAsset _mediaSelectionGroupDictionariesIncludingExtendedOptions:]
+ -[AVAsset _mediaSelectionGroupForMediaCharacteristic:inMediaSelectionGroupDictionaries:]
+ -[AVAssetTrackPlan hash]
+ -[AVAssetVideoTrackPlan hash]
+ -[AVAssetWriterInput _readyForMoreMediaDataMayHaveChanged]
+ -[AVAssetWriterInput(SwiftOverlay_Internal) _canBecomeReadyForMoreMediaDataAndReturnError:]
+ -[AVAssetWriterInput(SwiftOverlay_Internal) _errorForNotReadyForMoreMediaData]
+ -[AVAssetWriterInput(SwiftOverlay_Internal) _invokeWhenReadyForMoreMediaDataUsingBlock:]
+ -[AVAssetWriterInputHelper canBecomeReadyForMoreMediaDataAndReturnError:]
+ -[AVAssetWriterInputInterPassAnalysisHelper canBecomeReadyForMoreMediaDataAndReturnError:]
+ -[AVAssetWriterInputNoMorePassesHelper canBecomeReadyForMoreMediaDataAndReturnError:]
+ -[AVAssetWriterInputUnknownHelper canBecomeReadyForMoreMediaDataAndReturnError:]
+ -[AVAssetWriterInputWritingHelper canBecomeReadyForMoreMediaDataAndReturnError:]
+ -[AVFigAssetWriterTrack setWeakReferenceToAssetWriterInput:]
+ -[AVFigAssetWriterTrack weakReferenceToAssetWriterInput]
+ -[AVMediaSelection(AVMediaSelection_Local) _initWithAsset:mediaSelectionGroupDictionaries:selectedMediaArray:]
+ -[AVPlannedSegmentConfiguration hash]
+ -[AVPlannedVideoSegmentConfiguration hash]
+ -[AVSampleBufferVideoRenderer _isReadyForMoreMediaDataOnSerialQueue]
+ GCC_except_table107
+ GCC_except_table111
+ GCC_except_table122
+ GCC_except_table143
+ GCC_except_table154
+ GCC_except_table163
+ GCC_except_table165
+ GCC_except_table172
+ GCC_except_table175
+ GCC_except_table181
+ GCC_except_table183
+ GCC_except_table209
+ GCC_except_table217
+ GCC_except_table231
+ GCC_except_table235
+ GCC_except_table237
+ GCC_except_table92
+ OBJC_IVAR_$_AVAssetWriterInputInternal.readyForMoreMediaDataWaiters
+ OBJC_IVAR_$_AVAssetWriterInputInternal.readyForMoreMediaDataWaitersMutex
+ OBJC_IVAR_$_AVFigAssetWriterTrack._weakReferenceToAssetWriterInput
+ _AVMediaCharacteristicSignLanguageInterpretationForAccessibility
+ _kFigVideoCompositorProperty_MaximumPendingVideoCompositionRequests
+ _objc_msgSend$_availableMediaCharacteristicsFromMediaSelectionGroupDictionaries:
+ _objc_msgSend$_canBecomeReadyForMoreMediaDataAndReturnError:
+ _objc_msgSend$_initWithAsset:mediaSelectionGroupDictionaries:selectedMediaArray:
+ _objc_msgSend$_isReadyForMoreMediaDataOnSerialQueue
+ _objc_msgSend$_mediaSelectionGroupDictionariesIncludingExtendedOptions:
+ _objc_msgSend$_mediaSelectionGroupForMediaCharacteristic:inMediaSelectionGroupDictionaries:
+ _objc_msgSend$_readyForMoreMediaDataMayHaveChanged
+ _objc_msgSend$canBecomeReadyForMoreMediaDataAndReturnError:
+ _objc_msgSend$maximumPendingVideoCompositionRequests
- -[AVAssetDownloadSession _registerWithLiveActivityManager]
- -[AVAssetDownloadSession cancelFromLiveActivity]
- GCC_except_table110
- GCC_except_table119
- GCC_except_table162
- GCC_except_table166
- GCC_except_table168
- GCC_except_table174
- GCC_except_table180
- GCC_except_table210
- GCC_except_table253
- GCC_except_table458
- _objc_msgSend$_registerWithLiveActivityManager
- _objc_msgSend$_stopUnderlyingDownload
CStrings:
+ "<<<< AVSampleBufferVideoRenderer >>>> %s: <%{public}@|%p> Waking a suspended Swift enqueue because a flush is now required"
+ "FVQSetProperty(VideoDestinationArray/DisplayLayer)"
+ "public.accessibility.sign-language-interpretation"
- "FVQSetProperty(DisplayLayer)"
```
