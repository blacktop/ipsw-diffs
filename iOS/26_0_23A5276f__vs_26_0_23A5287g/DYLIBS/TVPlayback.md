## TVPlayback

> `/System/Library/PrivateFrameworks/TVPlayback.framework/TVPlayback`

```diff

-594.0.0.0.0
-  __TEXT.__text: 0x66b0c
+595.0.0.0.0
+  __TEXT.__text: 0x6742c
   __TEXT.__auth_stubs: 0x820
-  __TEXT.__objc_methlist: 0x5e30
+  __TEXT.__objc_methlist: 0x5e70
   __TEXT.__const: 0x270
-  __TEXT.__cstring: 0x67c6
-  __TEXT.__oslogstring: 0x63eb
-  __TEXT.__gcc_except_tab: 0x26dc
-  __TEXT.__unwind_info: 0x16a8
+  __TEXT.__cstring: 0x6878
+  __TEXT.__oslogstring: 0x65b2
+  __TEXT.__gcc_except_tab: 0x2730
+  __TEXT.__unwind_info: 0x16b0
   __TEXT.__objc_classname: 0x843
-  __TEXT.__objc_methname: 0x12d44
+  __TEXT.__objc_methname: 0x12e40
   __TEXT.__objc_methtype: 0x2507
-  __TEXT.__objc_stubs: 0xb3a0
-  __DATA_CONST.__got: 0x898
-  __DATA_CONST.__const: 0x2440
+  __TEXT.__objc_stubs: 0xb400
+  __DATA_CONST.__got: 0x8a0
+  __DATA_CONST.__const: 0x2498
   __DATA_CONST.__objc_classlist: 0x1f8
   __DATA_CONST.__objc_catlist: 0x80
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3c90
+  __DATA_CONST.__objc_selrefs: 0x3cb8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x170
   __DATA_CONST.__objc_arraydata: 0x10
   __AUTH_CONST.__auth_got: 0x420
-  __AUTH_CONST.__const: 0x640
-  __AUTH_CONST.__cfstring: 0x69c0
-  __AUTH_CONST.__objc_const: 0x98a0
+  __AUTH_CONST.__const: 0x680
+  __AUTH_CONST.__cfstring: 0x6a20
+  __AUTH_CONST.__objc_const: 0x98d0
   __AUTH_CONST.__objc_intobj: 0x480
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH.__objc_data: 0x8c0
-  __DATA.__objc_ivar: 0x7a4
+  __DATA.__objc_ivar: 0x7a8
   __DATA.__data: 0xac0
-  __DATA.__bss: 0xa8
+  __DATA.__bss: 0xb8
   __DATA_DIRTY.__objc_data: 0xaf0
   __DATA_DIRTY.__bss: 0x1f8
   __DATA_DIRTY.__common: 0x8

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 27B6DF6F-F70E-3E70-A41F-1E84ECC46D9D
-  Functions: 2231
-  Symbols:   8230
-  CStrings:  5478
+  UUID: 3C73EFE4-297F-3A6B-A720-6227A92B7571
+  Functions: 2243
+  Symbols:   8267
+  CStrings:  5499
 
Symbols:
+ +[TVPMediaItemLoader _mediaServicesResetDidTimeout]
+ +[TVPMediaItemLoader _mediaServicesWereLost:]
+ +[TVPMediaItemLoader _mediaServicesWereReset:]
+ -[TVPMediaItemLoader _tvpMediaServicesWereReset:]
+ -[TVPMediaItemLoader disableAVAssetCacheAfterMediaServicesReset]
+ -[TVPMediaItemLoader setDisableAVAssetCacheAfterMediaServicesReset:]
+ GCC_except_table13
+ GCC_except_table25
+ GCC_except_table34
+ GCC_except_table55
+ GCC_except_table58
+ GCC_except_table80
+ GCC_except_table87
+ GCC_except_table92
+ GCC_except_table94
+ _AVAudioSessionMediaServicesWereLostNotification
+ _OBJC_IVAR_$_TVPMediaItemLoader._disableAVAssetCacheAfterMediaServicesReset
+ _TVPMediaItemLoaderStateWaitingForMediaServicesToReset
+ ___37-[TVPMediaItemLoader _avAssetOptions]_block_invoke.277
+ ___45+[TVPMediaItemLoader _mediaServicesWereLost:]_block_invoke
+ ___45+[TVPMediaItemLoader _mediaServicesWereLost:]_block_invoke_2
+ ___46+[TVPMediaItemLoader _mediaServicesWereReset:]_block_invoke
+ ___46+[TVPMediaItemLoader _mediaServicesWereReset:]_block_invoke_2
+ ___51-[TVPMediaItemLoader _registerStateMachineHandlers]_block_invoke.123
+ ___51-[TVPMediaItemLoader _registerStateMachineHandlers]_block_invoke.127
+ ___51-[TVPMediaItemLoader _registerStateMachineHandlers]_block_invoke.127.cold.1
+ ___51-[TVPMediaItemLoader _registerStateMachineHandlers]_block_invoke.127.cold.2
+ ___51-[TVPMediaItemLoader _registerStateMachineHandlers]_block_invoke.128
+ ___51-[TVPMediaItemLoader _registerStateMachineHandlers]_block_invoke.134
+ ___51-[TVPMediaItemLoader _registerStateMachineHandlers]_block_invoke.143
+ ___51-[TVPMediaItemLoader _registerStateMachineHandlers]_block_invoke.179
+ ___51-[TVPMediaItemLoader _registerStateMachineHandlers]_block_invoke.185
+ ___51-[TVPMediaItemLoader _registerStateMachineHandlers]_block_invoke.189
+ ___51-[TVPMediaItemLoader _registerStateMachineHandlers]_block_invoke.196
+ ___51-[TVPMediaItemLoader _registerStateMachineHandlers]_block_invoke.204
+ ___51-[TVPMediaItemLoader _registerStateMachineHandlers]_block_invoke.205
+ ___51-[TVPMediaItemLoader _registerStateMachineHandlers]_block_invoke.212
+ ___51-[TVPMediaItemLoader _registerStateMachineHandlers]_block_invoke.213
+ ___51-[TVPMediaItemLoader _registerStateMachineHandlers]_block_invoke.216
+ ___51-[TVPMediaItemLoader _registerStateMachineHandlers]_block_invoke_2.135
+ ___51-[TVPMediaItemLoader _registerStateMachineHandlers]_block_invoke_2.135.cold.1
+ ___51-[TVPMediaItemLoader _registerStateMachineHandlers]_block_invoke_2.135.cold.2
+ ___51-[TVPMediaItemLoader _registerStateMachineHandlers]_block_invoke_2.180
+ ___51-[TVPMediaItemLoader _registerStateMachineHandlers]_block_invoke_2.183
+ ___51-[TVPMediaItemLoader _registerStateMachineHandlers]_block_invoke_2.199
+ ___51-[TVPMediaItemLoader _registerStateMachineHandlers]_block_invoke_2.206
+ ___51-[TVPMediaItemLoader _registerStateMachineHandlers]_block_invoke_2.217
+ ___51-[TVPMediaItemLoader _registerStateMachineHandlers]_block_invoke_3.201
+ ___51-[TVPMediaItemLoader _registerStateMachineHandlers]_block_invoke_3.207
+ ___51-[TVPMediaItemLoader _registerStateMachineHandlers]_block_invoke_3.220
+ ___51-[TVPMediaItemLoader _registerStateMachineHandlers]_block_invoke_4.208
+ ___51-[TVPMediaItemLoader _registerStateMachineHandlers]_block_invoke_5.211
+ ___51-[TVPMediaItemLoader _registerStateMachineHandlers]_block_invoke_5.211.cold.1
+ ___58-[TVPMediaItemLoader _loadMediaItemMetadataAsynchronously]_block_invoke.499
+ ___58-[TVPMediaItemLoader _loadMediaItemMetadataAsynchronously]_block_invoke.501
+ ___58-[TVPMediaItemLoader _loadMediaItemMetadataAsynchronously]_block_invoke.502
+ ___58-[TVPMediaItemLoader _loadMediaItemMetadataAsynchronously]_block_invoke.510
+ ___58-[TVPMediaItemLoader _loadMediaItemMetadataAsynchronously]_block_invoke_2.503
+ ___58-[TVPMediaItemLoader _loadMediaItemMetadataAsynchronously]_block_invoke_2.511
+ ___block_descriptor_40_e8_32r_e5_v8?0lr32l8
+ ___block_descriptor_56_e8_32s40bs48w_e21_"NSString"16?0B8B12lw48l8s32l8s40l8
+ ___block_literal_global.210
+ ___block_literal_global.215
+ ___block_literal_global.219
+ ___block_literal_global.274
+ ___block_literal_global.85
+ ___block_literal_global.89
+ _objc_msgSend$_mediaServicesWereReset:
+ _objc_msgSend$disableAVAssetCacheAfterMediaServicesReset
+ _objc_msgSend$setDisableAVAssetCacheAfterMediaServicesReset:
+ _sStaticPropertyQueue
+ _sWaitingForMediaServicesToReset
- +[TVPMediaItemLoader initialize].cold.1
- -[TVPMediaItemLoader _avAudioSessionMediaServicesWereReset:]
- GCC_except_table26
- GCC_except_table27
- GCC_except_table30
- GCC_except_table69
- GCC_except_table76
- GCC_except_table81
- GCC_except_table83
- ___37-[TVPMediaItemLoader _avAssetOptions]_block_invoke.249
- ___51-[TVPMediaItemLoader _registerStateMachineHandlers]_block_invoke.102
- ___51-[TVPMediaItemLoader _registerStateMachineHandlers]_block_invoke.106
- ___51-[TVPMediaItemLoader _registerStateMachineHandlers]_block_invoke.106.cold.1
- ___51-[TVPMediaItemLoader _registerStateMachineHandlers]_block_invoke.106.cold.2
- ___51-[TVPMediaItemLoader _registerStateMachineHandlers]_block_invoke.107
- ___51-[TVPMediaItemLoader _registerStateMachineHandlers]_block_invoke.113
- ___51-[TVPMediaItemLoader _registerStateMachineHandlers]_block_invoke.122
- ___51-[TVPMediaItemLoader _registerStateMachineHandlers]_block_invoke.160
- ___51-[TVPMediaItemLoader _registerStateMachineHandlers]_block_invoke.163
- ___51-[TVPMediaItemLoader _registerStateMachineHandlers]_block_invoke.167
- ___51-[TVPMediaItemLoader _registerStateMachineHandlers]_block_invoke.174
- ___51-[TVPMediaItemLoader _registerStateMachineHandlers]_block_invoke.183
- ___51-[TVPMediaItemLoader _registerStateMachineHandlers]_block_invoke.190
- ___51-[TVPMediaItemLoader _registerStateMachineHandlers]_block_invoke_2.114
- ___51-[TVPMediaItemLoader _registerStateMachineHandlers]_block_invoke_2.114.cold.1
- ___51-[TVPMediaItemLoader _registerStateMachineHandlers]_block_invoke_2.114.cold.2
- ___51-[TVPMediaItemLoader _registerStateMachineHandlers]_block_invoke_2.158
- ___51-[TVPMediaItemLoader _registerStateMachineHandlers]_block_invoke_2.161
- ___51-[TVPMediaItemLoader _registerStateMachineHandlers]_block_invoke_2.184
- ___51-[TVPMediaItemLoader _registerStateMachineHandlers]_block_invoke_2.193
- ___51-[TVPMediaItemLoader _registerStateMachineHandlers]_block_invoke_3.179
- ___51-[TVPMediaItemLoader _registerStateMachineHandlers]_block_invoke_3.185
- ___51-[TVPMediaItemLoader _registerStateMachineHandlers]_block_invoke_4.186
- ___51-[TVPMediaItemLoader _registerStateMachineHandlers]_block_invoke_5.189
- ___51-[TVPMediaItemLoader _registerStateMachineHandlers]_block_invoke_5.189.cold.1
- ___58-[TVPMediaItemLoader _loadMediaItemMetadataAsynchronously]_block_invoke.471
- ___58-[TVPMediaItemLoader _loadMediaItemMetadataAsynchronously]_block_invoke.473
- ___58-[TVPMediaItemLoader _loadMediaItemMetadataAsynchronously]_block_invoke.474
- ___58-[TVPMediaItemLoader _loadMediaItemMetadataAsynchronously]_block_invoke.482
- ___58-[TVPMediaItemLoader _loadMediaItemMetadataAsynchronously]_block_invoke_2.475
- ___58-[TVPMediaItemLoader _loadMediaItemMetadataAsynchronously]_block_invoke_2.483
- ___60-[TVPMediaItemLoader _avAudioSessionMediaServicesWereReset:]_block_invoke
- ___block_literal_global.188
- ___block_literal_global.192
- ___block_literal_global.246
- ___block_literal_global.68
CStrings:
+ "%@ received TVPMediaItemLoaderMediaServicesWereResetNotification"
+ "@\"NSString\"16@?0B8B12"
+ "Handling AVAudioSessionMediaServicesWereResetNotification after delay.  Notifying instances"
+ "Media services are currently resetting.  Will wait until reset is complete to load AVAsset keys"
+ "Media services were reset"
+ "Media services were reset while using AVFoundation objects.  Posting failure event"
+ "Media services were reset.  Will load AVAsset keys"
+ "Received AVAudioSessionMediaServicesWereLostNotification"
+ "TB,N,V_disableAVAssetCacheAfterMediaServicesReset"
+ "TVPMediaItemLoader static property queue"
+ "TVPMediaItemLoaderMediaServicesWereResetNotification"
+ "Timed out waiting for media services to reset.  Manually triggering notification"
+ "Waiting for media services to reset"
+ "_disableAVAssetCacheAfterMediaServicesReset"
+ "_mediaServicesResetDidTimeout"
+ "_mediaServicesWereLost:"
+ "_mediaServicesWereReset:"
+ "_tvpMediaServicesWereReset:"
+ "disableAVAssetCacheAfterMediaServicesReset"
+ "setDisableAVAssetCacheAfterMediaServicesReset:"
- "Handling AVAudioSessionMediaServicesWereResetNotification after delay"
- "_avAudioSessionMediaServicesWereReset:"

```
