## PhotosPlayer

> `/System/Library/PrivateFrameworks/PhotosPlayer.framework/PhotosPlayer`

```diff

-760.6.150.0.0
-  __TEXT.__text: 0x29be0
-  __TEXT.__auth_stubs: 0x7f0
-  __TEXT.__objc_methlist: 0x410c
-  __TEXT.__const: 0x1e8
-  __TEXT.__gcc_except_tab: 0x8e0
-  __TEXT.__cstring: 0xfb3
-  __TEXT.__oslogstring: 0x81c
-  __TEXT.__ustring: 0x22
-  __TEXT.__unwind_info: 0x1288
-  __TEXT.__objc_classname: 0x64c
-  __TEXT.__objc_methname: 0xb086
-  __TEXT.__objc_methtype: 0x198e
-  __TEXT.__objc_stubs: 0x7ce0
-  __DATA_CONST.__got: 0x3a8
-  __DATA_CONST.__const: 0xde0
-  __DATA_CONST.__objc_classlist: 0x1c8
+800.14.111.0.0
+  __TEXT.__text: 0x2b1a8
+  __TEXT.__auth_stubs: 0x810
+  __TEXT.__objc_methlist: 0x426c
+  __TEXT.__const: 0x1c0
+  __TEXT.__gcc_except_tab: 0x9d8
+  __TEXT.__cstring: 0x102c
+  __TEXT.__oslogstring: 0x91f
+  __TEXT.__ustring: 0x62
+  __TEXT.__unwind_info: 0x12c8
+  __TEXT.__objc_classname: 0x671
+  __TEXT.__objc_methname: 0xb5b1
+  __TEXT.__objc_methtype: 0x1a09
+  __TEXT.__objc_stubs: 0x8040
+  __DATA_CONST.__got: 0x3d0
+  __DATA_CONST.__const: 0xe58
+  __DATA_CONST.__objc_classlist: 0x1d0
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x25c0
-  __DATA_CONST.__objc_superrefs: 0x180
+  __DATA_CONST.__objc_selrefs: 0x26c0
+  __DATA_CONST.__objc_superrefs: 0x188
   __DATA_CONST.__objc_arraydata: 0x168
-  __AUTH_CONST.__auth_got: 0x408
+  __AUTH_CONST.__auth_got: 0x418
   __AUTH_CONST.__const: 0x380
-  __AUTH_CONST.__cfstring: 0x1480
-  __AUTH_CONST.__objc_const: 0x7330
+  __AUTH_CONST.__cfstring: 0x14c0
+  __AUTH_CONST.__objc_const: 0x75a0
   __AUTH_CONST.__objc_intobj: 0x108
   __AUTH_CONST.__objc_arrayobj: 0x168
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __DATA.__objc_ivar: 0x630
+  __DATA.__objc_ivar: 0x658
   __DATA.__data: 0x600
-  __DATA.__bss: 0x30
-  __DATA_DIRTY.__objc_data: 0x11d0
+  __DATA.__bss: 0x28
+  __DATA_DIRTY.__objc_data: 0x1220
   __DATA_DIRTY.__bss: 0x110
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/MediaAccessibility.framework/MediaAccessibility
+  - /System/Library/Frameworks/MediaPlayer.framework/MediaPlayer
   - /System/Library/Frameworks/MediaToolbox.framework/MediaToolbox
   - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
   - /System/Library/Frameworks/UIKit.framework/UIKit

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: BBBC48BB-67C9-35D8-B308-57323AA1C7BA
-  Functions: 1571
-  Symbols:   5540
-  CStrings:  2576
+  UUID: D9E49BBD-6ECC-3C51-8CCF-43266B52F40F
+  Functions: 1610
+  Symbols:   5676
+  CStrings:  2641
 
Symbols:
+ +[ISWrappedMemoriesAppleMusicPlayer isFeatureEnabled]
+ -[ISPlayerSettings playAppleMusicWithMemoriesExports]
+ -[ISPlayerSettings setPlayAppleMusicWithMemoriesExports:]
+ -[ISWrappedAVAudioSession mode]
+ -[ISWrappedMemoriesAppleMusicPlayer .cxx_destruct]
+ -[ISWrappedMemoriesAppleMusicPlayer _modifyAudioSessionToMixWithOthers]
+ -[ISWrappedMemoriesAppleMusicPlayer _waitForAssetLoadingIfNeccesary]
+ -[ISWrappedMemoriesAppleMusicPlayer adamID]
+ -[ISWrappedMemoriesAppleMusicPlayer appleMusicPlayerError]
+ -[ISWrappedMemoriesAppleMusicPlayer appleMusicPlayerQueue]
+ -[ISWrappedMemoriesAppleMusicPlayer appleMusicPlayer]
+ -[ISWrappedMemoriesAppleMusicPlayer cachedAVMediaSelectionGroup]
+ -[ISWrappedMemoriesAppleMusicPlayer dealloc]
+ -[ISWrappedMemoriesAppleMusicPlayer initWithPlayerItem:queue:]
+ -[ISWrappedMemoriesAppleMusicPlayer isLoadingAssetSemaphore]
+ -[ISWrappedMemoriesAppleMusicPlayer isLoadingAsset]
+ -[ISWrappedMemoriesAppleMusicPlayer pause]
+ -[ISWrappedMemoriesAppleMusicPlayer playWithCompletionHandler:]
+ -[ISWrappedMemoriesAppleMusicPlayer prepareWithCompletionHandler:]
+ -[ISWrappedMemoriesAppleMusicPlayer setAdamID:]
+ -[ISWrappedMemoriesAppleMusicPlayer setAppleMusicPlayerError:]
+ -[ISWrappedMemoriesAppleMusicPlayer setAppleMusicPlayerQueue:]
+ -[ISWrappedMemoriesAppleMusicPlayer setIsLoadingAsset:]
+ -[ISWrappedMemoriesAppleMusicPlayer setIsLoadingAssetSemaphore:]
+ -[ISWrappedMemoriesAppleMusicPlayer setWithoutMusicMediaOption:]
+ -[ISWrappedMemoriesAppleMusicPlayer stop]
+ -[ISWrappedMemoriesAppleMusicPlayer withoutMusicMediaOption]
+ GCC_except_table1167
+ GCC_except_table1217
+ GCC_except_table1224
+ GCC_except_table1227
+ GCC_except_table1231
+ GCC_except_table1235
+ GCC_except_table14
+ GCC_except_table1482
+ GCC_except_table1484
+ GCC_except_table1486
+ GCC_except_table1489
+ GCC_except_table1491
+ GCC_except_table1493
+ GCC_except_table1495
+ GCC_except_table1499
+ GCC_except_table150
+ GCC_except_table1501
+ GCC_except_table1503
+ GCC_except_table1505
+ GCC_except_table1507
+ GCC_except_table1509
+ GCC_except_table1511
+ GCC_except_table1513
+ GCC_except_table1515
+ GCC_except_table1517
+ GCC_except_table1519
+ GCC_except_table1521
+ GCC_except_table1564
+ GCC_except_table1585
+ GCC_except_table175
+ GCC_except_table176
+ GCC_except_table179
+ GCC_except_table18
+ GCC_except_table180
+ GCC_except_table189
+ GCC_except_table194
+ GCC_except_table215
+ GCC_except_table264
+ GCC_except_table283
+ GCC_except_table30
+ GCC_except_table410
+ GCC_except_table413
+ GCC_except_table420
+ GCC_except_table488
+ GCC_except_table490
+ GCC_except_table527
+ GCC_except_table549
+ GCC_except_table557
+ GCC_except_table59
+ GCC_except_table614
+ GCC_except_table658
+ GCC_except_table659
+ GCC_except_table661
+ GCC_except_table662
+ GCC_except_table666
+ GCC_except_table690
+ GCC_except_table726
+ GCC_except_table736
+ GCC_except_table792
+ GCC_except_table797
+ GCC_except_table802
+ GCC_except_table810
+ GCC_except_table821
+ GCC_except_table829
+ GCC_except_table839
+ GCC_except_table842
+ GCC_except_table847
+ GCC_except_table852
+ GCC_except_table859
+ GCC_except_table864
+ GCC_except_table868
+ GCC_except_table870
+ GCC_except_table878
+ GCC_except_table883
+ GCC_except_table891
+ GCC_except_table898
+ GCC_except_table909
+ GCC_except_table915
+ GCC_except_table920
+ GCC_except_table958
+ _AVMetadataQuickTimeMetadataKeyDescription
+ _AVMetadataQuickTimeMetadataKeyDisplayName
+ _MPErrorDomain
+ _OBJC_CLASS_$_ISWrappedMemoriesAppleMusicPlayer
+ _OBJC_CLASS_$_MPMusicPlayerApplicationController
+ _OBJC_IVAR_$_ISPlayerSettings._playAppleMusicWithMemoriesExports
+ _OBJC_IVAR_$_ISWrappedAVAudioSession._expectedMode
+ _OBJC_IVAR_$_ISWrappedAVPlayer._memoriesAppleMusicPlayer
+ _OBJC_IVAR_$_ISWrappedMemoriesAppleMusicPlayer._adamID
+ _OBJC_IVAR_$_ISWrappedMemoriesAppleMusicPlayer._appleMusicPlayerError
+ _OBJC_IVAR_$_ISWrappedMemoriesAppleMusicPlayer._appleMusicPlayerQueue
+ _OBJC_IVAR_$_ISWrappedMemoriesAppleMusicPlayer._cachedAVMediaSelectionGroup
+ _OBJC_IVAR_$_ISWrappedMemoriesAppleMusicPlayer._isLoadingAsset
+ _OBJC_IVAR_$_ISWrappedMemoriesAppleMusicPlayer._isLoadingAssetSemaphore
+ _OBJC_IVAR_$_ISWrappedMemoriesAppleMusicPlayer._withoutMusicMediaOption
+ _OBJC_METACLASS_$_ISWrappedMemoriesAppleMusicPlayer
+ _QueueIdentifierContext.4110
+ __OBJC_$_CLASS_METHODS_ISWrappedMemoriesAppleMusicPlayer
+ __OBJC_$_INSTANCE_METHODS_ISWrappedMemoriesAppleMusicPlayer
+ __OBJC_$_INSTANCE_VARIABLES_ISWrappedMemoriesAppleMusicPlayer
+ __OBJC_$_PROP_LIST_ISWrappedMemoriesAppleMusicPlayer
+ __OBJC_CLASS_RO_$_ISWrappedMemoriesAppleMusicPlayer
+ __OBJC_METACLASS_RO_$_ISWrappedMemoriesAppleMusicPlayer
+ ___41-[ISWrappedMemoriesAppleMusicPlayer stop]_block_invoke
+ ___42-[ISWrappedMemoriesAppleMusicPlayer pause]_block_invoke
+ ___62-[ISWrappedMemoriesAppleMusicPlayer initWithPlayerItem:queue:]_block_invoke
+ ___62-[ISWrappedMemoriesAppleMusicPlayer initWithPlayerItem:queue:]_block_invoke_2
+ ___63-[ISWrappedMemoriesAppleMusicPlayer playWithCompletionHandler:]_block_invoke
+ ___63-[ISWrappedMemoriesAppleMusicPlayer playWithCompletionHandler:]_block_invoke.13
+ ___63-[ISWrappedMemoriesAppleMusicPlayer playWithCompletionHandler:]_block_invoke_2
+ ___66-[ISWrappedMemoriesAppleMusicPlayer prepareWithCompletionHandler:]_block_invoke
+ ___66-[ISWrappedMemoriesAppleMusicPlayer prepareWithCompletionHandler:]_block_invoke_2
+ ___71-[ISWrappedAVPlayer observeChangeforKVOProxyIdentifier:keyPath:change:]_block_invoke_31
+ ___71-[ISWrappedAVPlayer observeChangeforKVOProxyIdentifier:keyPath:change:]_block_invoke_32
+ ___71-[ISWrappedAVPlayer observeChangeforKVOProxyIdentifier:keyPath:change:]_block_invoke_33
+ ___Block_byref_object_copy_.1992
+ ___Block_byref_object_copy_.4062
+ ___Block_byref_object_dispose_.1993
+ ___Block_byref_object_dispose_.4063
+ ___block_descriptor_40_e8_32bs_e17_v16?0"NSError"8ls32l8
+ ___block_descriptor_40_e8_32s_e43_v24?0"AVMediaSelectionGroup"8"NSError"16ls32l8
+ ___block_descriptor_56_e8_32s40bs48w_e17_v16?0"NSError"8ls32l8w48l8s40l8
+ ___block_descriptor_56_e8_32s40s48bs_e27_v16?0"ISWrappedAVPlayer"8ls32l8s40l8s48l8
+ ___block_literal_global.10.3912
+ ___block_literal_global.1357
+ ___block_literal_global.1561
+ ___block_literal_global.2007
+ ___block_literal_global.2123
+ ___block_literal_global.2757
+ ___block_literal_global.2987
+ ___block_literal_global.3.3921
+ ___block_literal_global.3114
+ ___block_literal_global.351
+ ___block_literal_global.3918
+ ___block_literal_global.4105
+ ___block_literal_global.492
+ ___block_literal_global.655
+ ___block_literal_global.74
+ ___block_literal_global.77
+ ___block_literal_global.992
+ __os_feature_enabled_impl
+ _objc_getProperty
+ _objc_msgSend$_modifyAudioSessionToMixWithOthers
+ _objc_msgSend$_waitForAssetLoadingIfNeccesary
+ _objc_msgSend$adamID
+ _objc_msgSend$appleMusicPlayer
+ _objc_msgSend$appleMusicPlayerError
+ _objc_msgSend$appleMusicPlayerQueue
+ _objc_msgSend$applicationQueuePlayer
+ _objc_msgSend$cachedAVMediaSelectionGroup
+ _objc_msgSend$category
+ _objc_msgSend$commonMetadata
+ _objc_msgSend$initWithPlayerItem:queue:
+ _objc_msgSend$isFeatureEnabled
+ _objc_msgSend$isLoadingAsset
+ _objc_msgSend$isLoadingAssetSemaphore
+ _objc_msgSend$key
+ _objc_msgSend$length
+ _objc_msgSend$livePhotoView:canBeginInteractivePlaybackAtPoint:
+ _objc_msgSend$loadMediaSelectionGroupForMediaCharacteristic:completionHandler:
+ _objc_msgSend$mode
+ _objc_msgSend$play
+ _objc_msgSend$playAppleMusicWithMemoriesExports
+ _objc_msgSend$playWithCompletionHandler:
+ _objc_msgSend$prepareToPlayWithCompletionHandler:
+ _objc_msgSend$prepareWithCompletionHandler:
+ _objc_msgSend$setPlayAppleMusicWithMemoriesExports:
+ _objc_msgSend$setQueueWithStoreIDs:
+ _objc_msgSend$setRepeatMode:
+ _objc_msgSend$withoutMusicMediaOption
+ _objc_setProperty_atomic
+ _sharedInstance.onceToken.2669
- GCC_except_table1132
- GCC_except_table117
- GCC_except_table1182
- GCC_except_table1189
- GCC_except_table1192
- GCC_except_table1196
- GCC_except_table1200
- GCC_except_table142
- GCC_except_table143
- GCC_except_table1446
- GCC_except_table1448
- GCC_except_table1450
- GCC_except_table1453
- GCC_except_table1455
- GCC_except_table1457
- GCC_except_table1459
- GCC_except_table146
- GCC_except_table1463
- GCC_except_table1465
- GCC_except_table1467
- GCC_except_table1469
- GCC_except_table147
- GCC_except_table1471
- GCC_except_table1473
- GCC_except_table1475
- GCC_except_table1477
- GCC_except_table1479
- GCC_except_table1481
- GCC_except_table1483
- GCC_except_table1485
- GCC_except_table1546
- GCC_except_table156
- GCC_except_table161
- GCC_except_table182
- GCC_except_table231
- GCC_except_table250
- GCC_except_table26
- GCC_except_table377
- GCC_except_table380
- GCC_except_table387
- GCC_except_table455
- GCC_except_table457
- GCC_except_table494
- GCC_except_table516
- GCC_except_table524
- GCC_except_table581
- GCC_except_table592
- GCC_except_table595
- GCC_except_table596
- GCC_except_table626
- GCC_except_table633
- GCC_except_table657
- GCC_except_table693
- GCC_except_table703
- GCC_except_table759
- GCC_except_table764
- GCC_except_table769
- GCC_except_table777
- GCC_except_table786
- GCC_except_table788
- GCC_except_table793
- GCC_except_table796
- GCC_except_table804
- GCC_except_table806
- GCC_except_table809
- GCC_except_table814
- GCC_except_table831
- GCC_except_table835
- GCC_except_table845
- GCC_except_table850
- GCC_except_table854
- GCC_except_table858
- GCC_except_table865
- GCC_except_table876
- GCC_except_table882
- GCC_except_table925
- _MGIsDeviceOneOfType
- _QueueIdentifierContext.4057
- ___Block_byref_object_copy_.1896
- ___Block_byref_object_copy_.4009
- ___Block_byref_object_dispose_.1897
- ___Block_byref_object_dispose_.4010
- ___block_descriptor_48_e8_32s40bs_e27_v16?0"ISWrappedAVPlayer"8ls32l8s40l8
- ___block_literal_global.10.3869
- ___block_literal_global.1261
- ___block_literal_global.1464
- ___block_literal_global.1912
- ___block_literal_global.2030
- ___block_literal_global.265
- ___block_literal_global.2674
- ___block_literal_global.2904
- ___block_literal_global.3.3878
- ___block_literal_global.3031
- ___block_literal_global.3875
- ___block_literal_global.402
- ___block_literal_global.4052
- ___block_literal_global.562
- ___block_literal_global.73
- ___block_literal_global.76
- ___block_literal_global.898
- _objc_msgSend$livePhotoViewCanBeginInteractivePlayback:
- _sharedInstance.onceToken.2587
CStrings:
+ "@\"AVMediaSelectionGroup\""
+ "@\"AVMediaSelectionOption\""
+ "@\"ISWrappedMemoriesAppleMusicPlayer\""
+ "@\"NSObject<OS_dispatch_semaphore>\""
+ "Apple Music Stopped prepareWithCompletionHandler failed. error=%@"
+ "AppleMusicSharing"
+ "ISWrappedMemoriesAppleMusicPlayer"
+ "ISWrappedMemoriesAppleMusicPlayer  loadMediaSelectionGroupForMediaCharacteristic. error=%@"
+ "ISWrappedMemoriesAppleMusicPlayer Failed to set MixWithOthers video playback audio session option. %@"
+ "Photos"
+ "T@\"AVMediaSelectionGroup\",R,V_cachedAVMediaSelectionGroup"
+ "T@\"AVMediaSelectionOption\",&,V_withoutMusicMediaOption"
+ "T@\"NSError\",&,V_appleMusicPlayerError"
+ "T@\"NSObject<OS_dispatch_queue>\",&,V_appleMusicPlayerQueue"
+ "T@\"NSObject<OS_dispatch_semaphore>\",&,V_isLoadingAssetSemaphore"
+ "T@\"NSString\",&,V_adamID"
+ "TB,N,V_playAppleMusicWithMemoriesExports"
+ "TB,V_isLoadingAsset"
+ "_adamID"
+ "_appleMusicPlayerError"
+ "_appleMusicPlayerQueue"
+ "_cachedAVMediaSelectionGroup"
+ "_expectedMode"
+ "_isLoadingAsset"
+ "_isLoadingAssetSemaphore"
+ "_memoriesAppleMusicPlayer"
+ "_modifyAudioSessionToMixWithOthers"
+ "_playAppleMusicWithMemoriesExports"
+ "_waitForAssetLoadingIfNeccesary"
+ "_withoutMusicMediaOption"
+ "adamID"
+ "appleMusicPlayer"
+ "appleMusicPlayerError"
+ "appleMusicPlayerQueue"
+ "applicationQueuePlayer"
+ "cachedAVMediaSelectionGroup"
+ "commonMetadata"
+ "initWithPlayerItem:queue:"
+ "isFeatureEnabled"
+ "isLoadingAsset"
+ "isLoadingAssetSemaphore"
+ "key"
+ "length"
+ "livePhotoView:canBeginInteractivePlaybackAtPoint:"
+ "loadMediaSelectionGroupForMediaCharacteristic:completionHandler:"
+ "mode"
+ "play"
+ "playAppleMusicWithMemoriesExports"
+ "playWithCompletionHandler:"
+ "prepareToPlayWithCompletionHandler:"
+ "prepareWithCompletionHandler:"
+ "setAdamID:"
+ "setAppleMusicPlayerError:"
+ "setAppleMusicPlayerQueue:"
+ "setIsLoadingAsset:"
+ "setIsLoadingAssetSemaphore:"
+ "setPlayAppleMusicWithMemoriesExports:"
+ "setQueueWithStoreIDs:"
+ "setRepeatMode:"
+ "setWithoutMusicMediaOption:"
+ "v16@?0@\"NSError\"8"
+ "v24@?0@\"AVMediaSelectionGroup\"8@\"NSError\"16"
+ "withoutMusicMediaOption"
- "livePhotoViewCanBeginInteractivePlayback:"

```
