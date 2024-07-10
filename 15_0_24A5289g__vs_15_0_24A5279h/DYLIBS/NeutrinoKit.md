## NeutrinoKit

> `/System/Library/PrivateFrameworks/NeutrinoKit.framework/Versions/A/NeutrinoKit`

```diff

-700.27.103.0.0
-  __TEXT.__text: 0x15fb0
+700.21.101.0.0
+  __TEXT.__text: 0x16700
   __TEXT.__auth_stubs: 0x6c0
-  __TEXT.__objc_methlist: 0x1714
+  __TEXT.__objc_methlist: 0x170c
   __TEXT.__const: 0x100
-  __TEXT.__gcc_except_tab: 0x214
+  __TEXT.__gcc_except_tab: 0x210
   __TEXT.__cstring: 0x1093
-  __TEXT.__oslogstring: 0x3f7
-  __TEXT.__unwind_info: 0x688
-  __TEXT.__objc_classname: 0x1f6
-  __TEXT.__objc_methname: 0x4a91
-  __TEXT.__objc_methtype: 0x102c
-  __TEXT.__objc_stubs: 0x4380
-  __DATA_CONST.__got: 0x350
+  __TEXT.__oslogstring: 0x489
+  __TEXT.__unwind_info: 0x690
+  __TEXT.__objc_classname: 0x1f5
+  __TEXT.__objc_methname: 0x4ad5
+  __TEXT.__objc_methtype: 0x105c
+  __TEXT.__objc_stubs: 0x4420
+  __DATA_CONST.__got: 0x348
   __DATA_CONST.__const: 0x100
   __DATA_CONST.__objc_classlist: 0x98
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x14d8
+  __DATA_CONST.__objc_selrefs: 0x14f0
   __DATA_CONST.__objc_superrefs: 0x70
   __AUTH_CONST.__auth_got: 0x370
   __AUTH_CONST.__const: 0x650
   __AUTH_CONST.__cfstring: 0xaa0
-  __AUTH_CONST.__objc_const: 0x2d30
+  __AUTH_CONST.__objc_const: 0x2d10
   __AUTH.__objc_data: 0x5f0
-  __DATA.__objc_ivar: 0x204
+  __DATA.__objc_ivar: 0x200
   __DATA.__data: 0x270
   __DATA.__bss: 0x10
-  - /System/Library/Frameworks/AVFAudio.framework/Versions/A/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /System/Library/PrivateFrameworks/PhotoFoundation.framework/Versions/A/PhotoFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 568
-  Symbols:   1689
+  Functions: 567
+  Symbols:   1691
   CStrings:  130
 
Symbols:
+ -[NUAVPlayerController _effectiveTimeForTime:]
+ -[NUAVPlayerController _loopingPlayerItemWithVideoAsset:videoComposition:audioMix:]
+ -[NUAVPlayerController _playerItemWithVideoAsset:videoComposition:audioMix:]
+ -[NUAVPlayerController _playerItemsWithVideoAsset:videoComposition:audioMix:loopsVideo:]
+ -[NUAVPlayerController prepareWithAVAsset:videoComposition:audioMix:loopsVideo:seekToTime:]
+ -[NUMediaView loopsVideoPlayback]
+ -[NUMediaView setLoopsVideoPlayback:]
+ GCC_except_table149
+ GCC_except_table155
+ GCC_except_table254
+ GCC_except_table281
+ GCC_except_table285
+ GCC_except_table300
+ GCC_except_table305
+ GCC_except_table313
+ GCC_except_table319
+ GCC_except_table32
+ GCC_except_table77
+ NUAssertLogger.310
+ NUAssertLogger.859
+ __Block_byref_object_copy_.337
+ __Block_byref_object_dispose_.338
+ __NUAssertLogger_block_invoke.316
+ __NUAssertLogger_block_invoke.848
+ __NULogger_block_invoke.818
+ __NUUILogger_block_invoke.318
+ ___88-[NUAVPlayerController _playerItemsWithVideoAsset:videoComposition:audioMix:loopsVideo:]_block_invoke
+ ___91-[NUAVPlayerController prepareWithAVAsset:videoComposition:audioMix:loopsVideo:seekToTime:]_block_invoke
+ __block_literal_global.184
+ __block_literal_global.195
+ __block_literal_global.323
+ __block_literal_global.367
+ __block_literal_global.369
+ __block_literal_global.470
+ __block_literal_global.472
+ __block_literal_global.825
+ _objc_msgSend$_effectiveTimeForTime:
+ _objc_msgSend$_loopingPlayerItemWithVideoAsset:videoComposition:audioMix:
+ _objc_msgSend$_playerItemWithVideoAsset:videoComposition:audioMix:
+ _objc_msgSend$_playerItemsWithVideoAsset:videoComposition:audioMix:loopsVideo:
+ _objc_msgSend$_removePlayerItemKVO:
+ _objc_msgSend$loopsVideoPlayback
+ _objc_msgSend$prepareWithAVAsset:videoComposition:audioMix:loopsVideo:seekToTime:
+ _objc_msgSend$removeAllItems
+ _objc_msgSend$repeatAudio:count:error:
+ _objc_msgSend$repeatVideo:count:error:
+ _objc_msgSend$repeatVideoComposition:count:error:
+ _objc_msgSend$setPlaybackMode:
- -[NUAVPlayerController _clearNextItemCache]
- -[NUAVPlayerController _playerItemsWithVideoAsset:videoComposition:audioMix:]
- -[NUAVPlayerController _updatePlayerActionAtItemEnd]
- -[NUAVPlayerController _updatePlayerAudioSession]
- -[NUAVPlayerController audioSessionCategory]
- -[NUAVPlayerController prepareWithAVAsset:videoComposition:audioMix:seekToTime:]
- -[NUAVPlayerController setAudioSessionCategory:]
- -[NUMediaViewRenderer _configurePlayerControllerForSelectedPlaybackMode]
- GCC_except_table151
- GCC_except_table157
- GCC_except_table257
- GCC_except_table284
- GCC_except_table288
- GCC_except_table303
- GCC_except_table308
- GCC_except_table316
- GCC_except_table322
- GCC_except_table35
- GCC_except_table79
- NUAssertLogger.322
- NUAssertLogger.858
- OBJC_IVAR_$_NUAVPlayerController._audioSessionCategory
- _AVAudioSessionCategoryPlayback
- __Block_byref_object_copy_.345
- __Block_byref_object_dispose_.346
- __NUAssertLogger_block_invoke.328
- __NUAssertLogger_block_invoke.847
- __NULogger_block_invoke.816
- __NUUILogger_block_invoke.330
- ___77-[NUAVPlayerController _playerItemsWithVideoAsset:videoComposition:audioMix:]_block_invoke
- ___80-[NUAVPlayerController prepareWithAVAsset:videoComposition:audioMix:seekToTime:]_block_invoke
- __block_literal_global.196
- __block_literal_global.202
- __block_literal_global.334
- __block_literal_global.363
- __block_literal_global.365
- __block_literal_global.471
- __block_literal_global.473
- __block_literal_global.823
- _objc_msgSend$_clearNextItemCache
- _objc_msgSend$_configurePlayerControllerForSelectedPlaybackMode
- _objc_msgSend$_playerItemsWithVideoAsset:videoComposition:audioMix:
- _objc_msgSend$_updatePlayerActionAtItemEnd
- _objc_msgSend$_updatePlayerAudioSession
- _objc_msgSend$prepareWithAVAsset:videoComposition:audioMix:seekToTime:
- _objc_msgSend$setAudioSessionCategory:
CStrings:
+ "/AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/Kit/Common/NUMaskTransformer.m"
+ "/AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/Kit/Common/NUMediaViewRenderer.m"
+ "/AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/Kit/Common/NUViewport.m"
+ "/AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/Kit/Common/NUViewportRegionPolicy.m"
+ "/AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/Kit/macOS/NUMediaView.m"
- "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/Kit/Common/NUMaskTransformer.m"
- "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/Kit/Common/NUMediaViewRenderer.m"
- "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/Kit/Common/NUViewport.m"
- "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/Kit/Common/NUViewportRegionPolicy.m"
- "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/Kit/macOS/NUMediaView.m"

```
