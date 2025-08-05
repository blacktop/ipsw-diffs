## CoreSpeech

> `/System/Library/PrivateFrameworks/CoreSpeech.framework/CoreSpeech`

```diff

-3500.115.2.0.0
-  __TEXT.__text: 0x151c80
+3500.122.2.0.0
+  __TEXT.__text: 0x151dac
   __TEXT.__auth_stubs: 0x1b30
   __TEXT.__objc_methlist: 0x14394
   __TEXT.__const: 0x58c
   __TEXT.__dlopen_cstrs: 0x197
   __TEXT.__gcc_except_tab: 0x3cac
-  __TEXT.__cstring: 0x2749e
-  __TEXT.__oslogstring: 0x1edfe
+  __TEXT.__cstring: 0x274a0
+  __TEXT.__oslogstring: 0x1edb7
   __TEXT.__unwind_info: 0x4db8
   __TEXT.__objc_classname: 0x2e76
-  __TEXT.__objc_methname: 0x37a6c
+  __TEXT.__objc_methname: 0x37a7c
   __TEXT.__objc_methtype: 0x7a59
-  __TEXT.__objc_stubs: 0x1bf00
+  __TEXT.__objc_stubs: 0x1bf20
   __DATA_CONST.__got: 0x1a98
   __DATA_CONST.__const: 0x40f8
   __DATA_CONST.__objc_classlist: 0x840
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x490
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa7e8
+  __DATA_CONST.__objc_selrefs: 0xa7f0
   __DATA_CONST.__objc_protorefs: 0xa8
   __DATA_CONST.__objc_superrefs: 0x688
   __DATA_CONST.__objc_arraydata: 0x3e8
   __AUTH_CONST.__auth_got: 0xdb0
   __AUTH_CONST.__const: 0x1e00
-  __AUTH_CONST.__cfstring: 0x9380
+  __AUTH_CONST.__cfstring: 0x93a0
   __AUTH_CONST.__objc_const: 0x20368
   __AUTH_CONST.__objc_intobj: 0x990
   __AUTH_CONST.__objc_doubleobj: 0xb0

   __AUTH.__objc_data: 0x3e80
   __DATA.__objc_ivar: 0x18f8
   __DATA.__data: 0x3650
-  __DATA.__bss: 0x670
+  __DATA.__bss: 0x668
   __DATA.__common: 0x10
   __DATA_DIRTY.__objc_data: 0x1400
   __DATA_DIRTY.__data: 0xc0
-  __DATA_DIRTY.__bss: 0x150
+  __DATA_DIRTY.__bss: 0x158
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 996E341B-56CD-3B33-9A2B-43FE4E8113B2
+  UUID: E516DAC7-D46E-3665-A3DB-DF9F775203E2
   Functions: 7915
-  Symbols:   26013
-  CStrings:  15482
+  Symbols:   26014
+  CStrings:  15484
 
Symbols:
+ _AudioConverterFillComplexBuffer_BlockInvoke.26244
+ ___105-[CSHybridEndpointAnalyzer resetForNewRequestWithSampleRate:recordContext:recordOption:voiceTriggerInfo:]_block_invoke.437
+ ___105-[CSHybridEndpointAnalyzer resetForNewRequestWithSampleRate:recordContext:recordOption:voiceTriggerInfo:]_block_invoke.441
+ ___105-[CSHybridEndpointAnalyzer resetForNewRequestWithSampleRate:recordContext:recordOption:voiceTriggerInfo:]_block_invoke.444
+ ___46-[CSHybridEndpointAnalyzer processTaskString:]_block_invoke.397
+ ___48-[CSSpeechController CSXPCClient:didDisconnect:]_block_invoke.373
+ ___49-[CSAssetController _downloadAsset:withComplete:]_block_invoke.330
+ ___52-[CSSpeechController setCurrentRecordContext:error:]_block_invoke.249
+ ___54-[CSAssetController fetchRemoteMetaOfType:allowRetry:]_block_invoke.318
+ ___54-[CSSpeechController prepareRecordWithSettings:error:]_block_invoke.224
+ ___54-[CSSpeechController prepareRecordWithSettings:error:]_block_invoke.233
+ ___55-[CSSpeechController startRecordingWithSettings:error:]_block_invoke.279
+ ___55-[CSSpeechController startRecordingWithSettings:error:]_block_invoke.287
+ ___55-[CSSpeechController startRecordingWithSettings:error:]_block_invoke_2.288
+ ___60-[CSSpeechController handleStopRecordingRequestWithOptions:]_block_invoke.301
+ ___64-[CSEndpointerAssetManager _registerForAssetUpdateNotifications]_block_invoke.311
+ ___76-[CSHybridEndpointAnalyzer processOSDFeatures:withFrameDurationMs:withMHID:]_block_invoke.402
+ ___76-[CSHybridEndpointAnalyzer processOSDFeatures:withFrameDurationMs:withMHID:]_block_invoke.403
+ ___76-[CSHybridEndpointAnalyzer processOSDFeatures:withFrameDurationMs:withMHID:]_block_invoke.406
+ ___76-[CSHybridEndpointAnalyzer processOSDFeatures:withFrameDurationMs:withMHID:]_block_invoke.407
+ ___76-[CSHybridEndpointAnalyzer processOSDFeatures:withFrameDurationMs:withMHID:]_block_invoke.410
+ ___76-[CSHybridEndpointAnalyzer processOSDFeatures:withFrameDurationMs:withMHID:]_block_invoke.415
+ ___76-[CSHybridEndpointAnalyzer processOSDFeatures:withFrameDurationMs:withMHID:]_block_invoke.419
+ ___76-[CSHybridEndpointAnalyzer processOSDFeatures:withFrameDurationMs:withMHID:]_block_invoke_2.408
+ ___81-[CSSpeechController _activateAudioSessionWithReason:delay:delayRequested:error:]_block_invoke.235
+ ___81-[CSSpeechController _activateAudioSessionWithReason:delay:delayRequested:error:]_block_invoke.236
+ ___81-[CSSpeechController _activateAudioSessionWithReason:delay:delayRequested:error:]_block_invoke.237
+ ___81-[CSSpeechController _activateAudioSessionWithReason:delay:delayRequested:error:]_block_invoke.245
+ ___Block_byref_object_copy_.10152
+ ___Block_byref_object_copy_.10622
+ ___Block_byref_object_copy_.11829
+ ___Block_byref_object_copy_.13120
+ ___Block_byref_object_copy_.13539
+ ___Block_byref_object_copy_.14599
+ ___Block_byref_object_copy_.14934
+ ___Block_byref_object_copy_.15809
+ ___Block_byref_object_copy_.15922
+ ___Block_byref_object_copy_.17548
+ ___Block_byref_object_copy_.17840
+ ___Block_byref_object_copy_.18991
+ ___Block_byref_object_copy_.20126
+ ___Block_byref_object_copy_.20778
+ ___Block_byref_object_copy_.21390
+ ___Block_byref_object_copy_.21632
+ ___Block_byref_object_copy_.22265
+ ___Block_byref_object_copy_.22920
+ ___Block_byref_object_copy_.23191
+ ___Block_byref_object_copy_.23927
+ ___Block_byref_object_copy_.24718
+ ___Block_byref_object_copy_.25152
+ ___Block_byref_object_copy_.25990
+ ___Block_byref_object_copy_.26425
+ ___Block_byref_object_copy_.27244
+ ___Block_byref_object_copy_.6428
+ ___Block_byref_object_copy_.7381
+ ___Block_byref_object_copy_.8393
+ ___Block_byref_object_copy_.8989
+ ___Block_byref_object_dispose_.10153
+ ___Block_byref_object_dispose_.10623
+ ___Block_byref_object_dispose_.11830
+ ___Block_byref_object_dispose_.13121
+ ___Block_byref_object_dispose_.13540
+ ___Block_byref_object_dispose_.14600
+ ___Block_byref_object_dispose_.14935
+ ___Block_byref_object_dispose_.15810
+ ___Block_byref_object_dispose_.15923
+ ___Block_byref_object_dispose_.17549
+ ___Block_byref_object_dispose_.17841
+ ___Block_byref_object_dispose_.18992
+ ___Block_byref_object_dispose_.20127
+ ___Block_byref_object_dispose_.20779
+ ___Block_byref_object_dispose_.21391
+ ___Block_byref_object_dispose_.21633
+ ___Block_byref_object_dispose_.22266
+ ___Block_byref_object_dispose_.22921
+ ___Block_byref_object_dispose_.23192
+ ___Block_byref_object_dispose_.23928
+ ___Block_byref_object_dispose_.24719
+ ___Block_byref_object_dispose_.25153
+ ___Block_byref_object_dispose_.25991
+ ___Block_byref_object_dispose_.26426
+ ___Block_byref_object_dispose_.27245
+ ___Block_byref_object_dispose_.6429
+ ___Block_byref_object_dispose_.7382
+ ___Block_byref_object_dispose_.8394
+ ___Block_byref_object_dispose_.8990
+ ___block_literal_global.10.10771
+ ___block_literal_global.10.19520
+ ___block_literal_global.10.21076
+ ___block_literal_global.10.22128
+ ___block_literal_global.10257
+ ___block_literal_global.10403
+ ___block_literal_global.10639
+ ___block_literal_global.10797
+ ___block_literal_global.11.12107
+ ___block_literal_global.11013
+ ___block_literal_global.11225
+ ___block_literal_global.11684
+ ___block_literal_global.11856
+ ___block_literal_global.12.14093
+ ___block_literal_global.12117
+ ___block_literal_global.12217
+ ___block_literal_global.12339
+ ___block_literal_global.12647
+ ___block_literal_global.12753
+ ___block_literal_global.12809
+ ___block_literal_global.12864
+ ___block_literal_global.13.21077
+ ___block_literal_global.13.21223
+ ___block_literal_global.13.22129
+ ___block_literal_global.13327
+ ___block_literal_global.13443
+ ___block_literal_global.13669
+ ___block_literal_global.14.21148
+ ___block_literal_global.14086
+ ___block_literal_global.14432
+ ___block_literal_global.14489
+ ___block_literal_global.14678
+ ___block_literal_global.14696
+ ___block_literal_global.14807
+ ___block_literal_global.15332
+ ___block_literal_global.15417
+ ___block_literal_global.15909
+ ___block_literal_global.15951
+ ___block_literal_global.16.10385
+ ___block_literal_global.16.12097
+ ___block_literal_global.16.13328
+ ___block_literal_global.16.14490
+ ___block_literal_global.16.21078
+ ___block_literal_global.16595
+ ___block_literal_global.17.14433
+ ___block_literal_global.17.21149
+ ___block_literal_global.17069
+ ___block_literal_global.17078
+ ___block_literal_global.17124
+ ___block_literal_global.17158
+ ___block_literal_global.17422
+ ___block_literal_global.17498
+ ___block_literal_global.17606
+ ___block_literal_global.18.14777
+ ___block_literal_global.18.21224
+ ___block_literal_global.18069
+ ___block_literal_global.18138
+ ___block_literal_global.18168
+ ___block_literal_global.18731
+ ___block_literal_global.19011
+ ___block_literal_global.19318
+ ___block_literal_global.19399
+ ___block_literal_global.19537
+ ___block_literal_global.19652
+ ___block_literal_global.19697
+ ___block_literal_global.19713
+ ___block_literal_global.19991
+ ___block_literal_global.20.13304
+ ___block_literal_global.20.14434
+ ___block_literal_global.20.21150
+ ___block_literal_global.20.25135
+ ___block_literal_global.20043
+ ___block_literal_global.20148
+ ___block_literal_global.20224
+ ___block_literal_global.20425
+ ___block_literal_global.20762
+ ___block_literal_global.21.12754
+ ___block_literal_global.21062
+ ___block_literal_global.21075
+ ___block_literal_global.211
+ ___block_literal_global.21147
+ ___block_literal_global.21243
+ ___block_literal_global.21293
+ ___block_literal_global.21336
+ ___block_literal_global.21459
+ ___block_literal_global.22.17396
+ ___block_literal_global.22.21079
+ ___block_literal_global.22126
+ ___block_literal_global.22630
+ ___block_literal_global.22802
+ ___block_literal_global.22952
+ ___block_literal_global.23.21151
+ ___block_literal_global.23504
+ ___block_literal_global.23720
+ ___block_literal_global.23804
+ ___block_literal_global.239
+ ___block_literal_global.24.12755
+ ___block_literal_global.24181
+ ___block_literal_global.24854
+ ___block_literal_global.25.21080
+ ___block_literal_global.25176
+ ___block_literal_global.25508
+ ___block_literal_global.25798
+ ___block_literal_global.25847
+ ___block_literal_global.26.25124
+ ___block_literal_global.26026
+ ___block_literal_global.26131
+ ___block_literal_global.26361
+ ___block_literal_global.26494
+ ___block_literal_global.27.12756
+ ___block_literal_global.27039
+ ___block_literal_global.27255
+ ___block_literal_global.27529
+ ___block_literal_global.29.21081
+ ___block_literal_global.29.21152
+ ___block_literal_global.30.12757
+ ___block_literal_global.30.13289
+ ___block_literal_global.306
+ ___block_literal_global.329
+ ___block_literal_global.36.12758
+ ___block_literal_global.38.9139
+ ___block_literal_global.40.20740
+ ___block_literal_global.42.12759
+ ___block_literal_global.46.6462
+ ___block_literal_global.46.9131
+ ___block_literal_global.5.27530
+ ___block_literal_global.54.11215
+ ___block_literal_global.5687
+ ___block_literal_global.5798
+ ___block_literal_global.5984
+ ___block_literal_global.6.26021
+ ___block_literal_global.6086
+ ___block_literal_global.6109
+ ___block_literal_global.6495
+ ___block_literal_global.6632
+ ___block_literal_global.6915
+ ___block_literal_global.7.22127
+ ___block_literal_global.8.26125
+ ___block_literal_global.8.26495
+ ___block_literal_global.8.27531
+ ___block_literal_global.8565
+ ___block_literal_global.9171
+ ___block_literal_global.9223
+ ___block_literal_global.9340
+ ___block_literal_global.9748
+ __block_invoke.enableHeartbeat.11009
+ __compensateChannelDataIfNeeded:receivedNumChannels:.heartbeat.14587
+ __handleAudioChunk:.heartbeat_CORESPEECH_VOICETRIGGER_FIRSTPASS_LPCM_RECORD_BUFFER_AVAILABLE.18657
+ __keywordAnalyzerNDAPI:hasResultAvailable:forChannel:.heartbeat.10994
+ __keywordAnalyzerNDAPI:hasResultAvailable:forChannel:.heartbeat.18648
+ __keywordAnalyzerNDAPI:hasResultAvailable:forChannel:.heartbeat.26725
+ _objc_msgSend$setWithObjects:
+ _sharedController.onceToken.11855
+ _sharedController.sharedController.11857
+ _sharedHandler.onceToken.19317
+ _sharedHandler.onceToken.26025
+ _sharedHandler.sharedHandler.19319
+ _sharedHandler.sharedHandler.26027
+ _sharedHandlerDisabledOnDeviceCompilation.onceToken.26020
+ _sharedHandlerDisabledOnDeviceCompilation.sharedHandler.26022
+ _sharedInstance._sharedInstance.11685
+ _sharedInstance._sharedInstance.12865
+ _sharedInstance._sharedInstance.14808
+ _sharedInstance._sharedInstance.17125
+ _sharedInstance._sharedInstance.17423
+ _sharedInstance._sharedInstance.17499
+ _sharedInstance._sharedInstance.18139
+ _sharedInstance._sharedInstance.19653
+ _sharedInstance._sharedInstance.19992
+ _sharedInstance._sharedInstance.20044
+ _sharedInstance._sharedInstance.20225
+ _sharedInstance._sharedInstance.23505
+ _sharedInstance._sharedInstance.24182
+ _sharedInstance._sharedInstance.25848
+ _sharedInstance._sharedInstance.27256
+ _sharedInstance._sharedInstance.5688
+ _sharedInstance._sharedInstance.5799
+ _sharedInstance._sharedInstance.6087
+ _sharedInstance._sharedInstance.6633
+ _sharedInstance._sharedInstance.9224
+ _sharedInstance.onceToken.10402
+ _sharedInstance.onceToken.10638
+ _sharedInstance.onceToken.10796
+ _sharedInstance.onceToken.11683
+ _sharedInstance.onceToken.12808
+ _sharedInstance.onceToken.12863
+ _sharedInstance.onceToken.13442
+ _sharedInstance.onceToken.14806
+ _sharedInstance.onceToken.15331
+ _sharedInstance.onceToken.15416
+ _sharedInstance.onceToken.15908
+ _sharedInstance.onceToken.17123
+ _sharedInstance.onceToken.17421
+ _sharedInstance.onceToken.17497
+ _sharedInstance.onceToken.17605
+ _sharedInstance.onceToken.18068
+ _sharedInstance.onceToken.18137
+ _sharedInstance.onceToken.18167
+ _sharedInstance.onceToken.19536
+ _sharedInstance.onceToken.19651
+ _sharedInstance.onceToken.19990
+ _sharedInstance.onceToken.20042
+ _sharedInstance.onceToken.20223
+ _sharedInstance.onceToken.21061
+ _sharedInstance.onceToken.21242
+ _sharedInstance.onceToken.21335
+ _sharedInstance.onceToken.21458
+ _sharedInstance.onceToken.22629
+ _sharedInstance.onceToken.22801
+ _sharedInstance.onceToken.22951
+ _sharedInstance.onceToken.23503
+ _sharedInstance.onceToken.23803
+ _sharedInstance.onceToken.24180
+ _sharedInstance.onceToken.25507
+ _sharedInstance.onceToken.25846
+ _sharedInstance.onceToken.27038
+ _sharedInstance.onceToken.27254
+ _sharedInstance.onceToken.5686
+ _sharedInstance.onceToken.5797
+ _sharedInstance.onceToken.6085
+ _sharedInstance.onceToken.6631
+ _sharedInstance.onceToken.9222
+ _sharedInstance.sSharedInstance.18169
+ _sharedInstance.sharedInstance.12810
+ _sharedInstance.sharedInstance.13444
+ _sharedInstance.sharedInstance.15418
+ _sharedInstance.sharedInstance.18070
+ _sharedInstance.sharedInstance.19538
+ _sharedInstance.sharedInstance.21063
+ _sharedInstance.sharedInstance.21337
+ _sharedInstance.sharedInstance.22803
+ _sharedInstance.sharedInstance.22953
+ _sharedInstance.sharedInstance.27040
+ _sharedInstance.sharedManager.25509
+ _sharedInstance.sharedPolicy.21244
+ _sharedInstance.sharedPolicy.23805
+ _sharedInstance.sharedProvider.22631
+ _sharedManager.onceToken.17068
+ _sharedManager.onceToken.19010
+ _sharedManager.onceToken.6494
+ _sharedManager.onceToken.6914
+ _sharedManager.sharedManager.17070
+ _sharedManager.sharedManager.6496
+ _sharedManager.sharedManager.6916
+ _sharedMonitor.onceToken.20147
+ _sharedMonitor.sharedMonitor.20149
+ _sharedService.onceToken.15950
+ _sharedService.onceToken.25175
+ _sharedService.sharedService.25177
- _AudioConverterFillComplexBuffer_BlockInvoke.26263
- ___105-[CSHybridEndpointAnalyzer resetForNewRequestWithSampleRate:recordContext:recordOption:voiceTriggerInfo:]_block_invoke.431
- ___105-[CSHybridEndpointAnalyzer resetForNewRequestWithSampleRate:recordContext:recordOption:voiceTriggerInfo:]_block_invoke.435
- ___105-[CSHybridEndpointAnalyzer resetForNewRequestWithSampleRate:recordContext:recordOption:voiceTriggerInfo:]_block_invoke.438
- ___46-[CSHybridEndpointAnalyzer processTaskString:]_block_invoke.391
- ___48-[CSSpeechController CSXPCClient:didDisconnect:]_block_invoke.367
- ___49-[CSAssetController _downloadAsset:withComplete:]_block_invoke.327
- ___52-[CSSpeechController setCurrentRecordContext:error:]_block_invoke.246
- ___54-[CSAssetController fetchRemoteMetaOfType:allowRetry:]_block_invoke.315
- ___54-[CSSpeechController prepareRecordWithSettings:error:]_block_invoke.221
- ___54-[CSSpeechController prepareRecordWithSettings:error:]_block_invoke.230
- ___55-[CSSpeechController startRecordingWithSettings:error:]_block_invoke.276
- ___55-[CSSpeechController startRecordingWithSettings:error:]_block_invoke.284
- ___55-[CSSpeechController startRecordingWithSettings:error:]_block_invoke_2.285
- ___60-[CSSpeechController handleStopRecordingRequestWithOptions:]_block_invoke.298
- ___64-[CSEndpointerAssetManager _registerForAssetUpdateNotifications]_block_invoke.308
- ___76-[CSHybridEndpointAnalyzer processOSDFeatures:withFrameDurationMs:withMHID:]_block_invoke.396
- ___76-[CSHybridEndpointAnalyzer processOSDFeatures:withFrameDurationMs:withMHID:]_block_invoke.397
- ___76-[CSHybridEndpointAnalyzer processOSDFeatures:withFrameDurationMs:withMHID:]_block_invoke.398
- ___76-[CSHybridEndpointAnalyzer processOSDFeatures:withFrameDurationMs:withMHID:]_block_invoke.400
- ___76-[CSHybridEndpointAnalyzer processOSDFeatures:withFrameDurationMs:withMHID:]_block_invoke.401
- ___76-[CSHybridEndpointAnalyzer processOSDFeatures:withFrameDurationMs:withMHID:]_block_invoke.409
- ___76-[CSHybridEndpointAnalyzer processOSDFeatures:withFrameDurationMs:withMHID:]_block_invoke.413
- ___76-[CSHybridEndpointAnalyzer processOSDFeatures:withFrameDurationMs:withMHID:]_block_invoke_2.402
- ___81-[CSSpeechController _activateAudioSessionWithReason:delay:delayRequested:error:]_block_invoke.232
- ___81-[CSSpeechController _activateAudioSessionWithReason:delay:delayRequested:error:]_block_invoke.233
- ___81-[CSSpeechController _activateAudioSessionWithReason:delay:delayRequested:error:]_block_invoke.234
- ___81-[CSSpeechController _activateAudioSessionWithReason:delay:delayRequested:error:]_block_invoke.242
- ___Block_byref_object_copy_.10162
- ___Block_byref_object_copy_.10632
- ___Block_byref_object_copy_.11841
- ___Block_byref_object_copy_.13136
- ___Block_byref_object_copy_.13555
- ___Block_byref_object_copy_.14615
- ___Block_byref_object_copy_.14950
- ___Block_byref_object_copy_.15822
- ___Block_byref_object_copy_.15938
- ___Block_byref_object_copy_.17564
- ___Block_byref_object_copy_.17853
- ___Block_byref_object_copy_.18997
- ___Block_byref_object_copy_.20134
- ___Block_byref_object_copy_.20787
- ___Block_byref_object_copy_.21399
- ___Block_byref_object_copy_.21641
- ___Block_byref_object_copy_.22273
- ___Block_byref_object_copy_.22927
- ___Block_byref_object_copy_.23198
- ___Block_byref_object_copy_.23934
- ___Block_byref_object_copy_.24736
- ___Block_byref_object_copy_.25171
- ___Block_byref_object_copy_.26009
- ___Block_byref_object_copy_.26444
- ___Block_byref_object_copy_.27263
- ___Block_byref_object_copy_.6426
- ___Block_byref_object_copy_.7379
- ___Block_byref_object_copy_.8401
- ___Block_byref_object_copy_.8998
- ___Block_byref_object_dispose_.10163
- ___Block_byref_object_dispose_.10633
- ___Block_byref_object_dispose_.11842
- ___Block_byref_object_dispose_.13137
- ___Block_byref_object_dispose_.13556
- ___Block_byref_object_dispose_.14616
- ___Block_byref_object_dispose_.14951
- ___Block_byref_object_dispose_.15823
- ___Block_byref_object_dispose_.15939
- ___Block_byref_object_dispose_.17565
- ___Block_byref_object_dispose_.17854
- ___Block_byref_object_dispose_.18998
- ___Block_byref_object_dispose_.20135
- ___Block_byref_object_dispose_.20788
- ___Block_byref_object_dispose_.21400
- ___Block_byref_object_dispose_.21642
- ___Block_byref_object_dispose_.22274
- ___Block_byref_object_dispose_.22928
- ___Block_byref_object_dispose_.23199
- ___Block_byref_object_dispose_.23935
- ___Block_byref_object_dispose_.24737
- ___Block_byref_object_dispose_.25172
- ___Block_byref_object_dispose_.26010
- ___Block_byref_object_dispose_.26445
- ___Block_byref_object_dispose_.27264
- ___Block_byref_object_dispose_.6427
- ___Block_byref_object_dispose_.7380
- ___Block_byref_object_dispose_.8402
- ___Block_byref_object_dispose_.8999
- ___block_literal_global.10.10781
- ___block_literal_global.10.19528
- ___block_literal_global.10.21085
- ___block_literal_global.10.22137
- ___block_literal_global.10267
- ___block_literal_global.10413
- ___block_literal_global.10649
- ___block_literal_global.10807
- ___block_literal_global.11.12123
- ___block_literal_global.11023
- ___block_literal_global.11235
- ___block_literal_global.11694
- ___block_literal_global.11867
- ___block_literal_global.12.14109
- ___block_literal_global.12133
- ___block_literal_global.12233
- ___block_literal_global.12355
- ___block_literal_global.12663
- ___block_literal_global.12769
- ___block_literal_global.12825
- ___block_literal_global.12880
- ___block_literal_global.13.21086
- ___block_literal_global.13.21232
- ___block_literal_global.13.22138
- ___block_literal_global.13343
- ___block_literal_global.13459
- ___block_literal_global.13685
- ___block_literal_global.14.21157
- ___block_literal_global.14102
- ___block_literal_global.14448
- ___block_literal_global.14505
- ___block_literal_global.14694
- ___block_literal_global.14712
- ___block_literal_global.14823
- ___block_literal_global.15348
- ___block_literal_global.15433
- ___block_literal_global.15925
- ___block_literal_global.15967
- ___block_literal_global.16.10395
- ___block_literal_global.16.12113
- ___block_literal_global.16.13344
- ___block_literal_global.16.14506
- ___block_literal_global.16.21087
- ___block_literal_global.16611
- ___block_literal_global.17.14449
- ___block_literal_global.17.21158
- ___block_literal_global.17085
- ___block_literal_global.17094
- ___block_literal_global.17140
- ___block_literal_global.17174
- ___block_literal_global.17438
- ___block_literal_global.17514
- ___block_literal_global.17622
- ___block_literal_global.18.14793
- ___block_literal_global.18.21233
- ___block_literal_global.18087
- ___block_literal_global.18156
- ___block_literal_global.18186
- ___block_literal_global.18736
- ___block_literal_global.19019
- ___block_literal_global.19326
- ___block_literal_global.19407
- ___block_literal_global.19545
- ___block_literal_global.19660
- ___block_literal_global.19705
- ___block_literal_global.19721
- ___block_literal_global.19999
- ___block_literal_global.20.13320
- ___block_literal_global.20.14450
- ___block_literal_global.20.21159
- ___block_literal_global.20.25154
- ___block_literal_global.20051
- ___block_literal_global.20156
- ___block_literal_global.20232
- ___block_literal_global.20435
- ___block_literal_global.20771
- ___block_literal_global.208
- ___block_literal_global.21.12770
- ___block_literal_global.21071
- ___block_literal_global.21084
- ___block_literal_global.21156
- ___block_literal_global.21252
- ___block_literal_global.21302
- ___block_literal_global.21345
- ___block_literal_global.21468
- ___block_literal_global.22.17412
- ___block_literal_global.22.21088
- ___block_literal_global.22135
- ___block_literal_global.22637
- ___block_literal_global.22809
- ___block_literal_global.22959
- ___block_literal_global.23.21160
- ___block_literal_global.23510
- ___block_literal_global.236
- ___block_literal_global.23726
- ___block_literal_global.23811
- ___block_literal_global.24.12771
- ___block_literal_global.24188
- ___block_literal_global.24873
- ___block_literal_global.25.21089
- ___block_literal_global.25195
- ___block_literal_global.25527
- ___block_literal_global.25817
- ___block_literal_global.25866
- ___block_literal_global.26.25143
- ___block_literal_global.26045
- ___block_literal_global.26150
- ___block_literal_global.26380
- ___block_literal_global.26513
- ___block_literal_global.27.12772
- ___block_literal_global.27058
- ___block_literal_global.27274
- ___block_literal_global.27548
- ___block_literal_global.29.21090
- ___block_literal_global.29.21161
- ___block_literal_global.30.12773
- ___block_literal_global.30.13305
- ___block_literal_global.300
- ___block_literal_global.326
- ___block_literal_global.36.12774
- ___block_literal_global.38.9148
- ___block_literal_global.40.20749
- ___block_literal_global.42.12775
- ___block_literal_global.46.6460
- ___block_literal_global.46.9140
- ___block_literal_global.5.27549
- ___block_literal_global.54.11225
- ___block_literal_global.5685
- ___block_literal_global.5796
- ___block_literal_global.5982
- ___block_literal_global.6.26040
- ___block_literal_global.6084
- ___block_literal_global.6107
- ___block_literal_global.6493
- ___block_literal_global.6630
- ___block_literal_global.6913
- ___block_literal_global.7.22136
- ___block_literal_global.8.26144
- ___block_literal_global.8.26514
- ___block_literal_global.8.27550
- ___block_literal_global.8575
- ___block_literal_global.9180
- ___block_literal_global.9232
- ___block_literal_global.9349
- ___block_literal_global.9758
- __block_invoke.enableHeartbeat.11019
- __compensateChannelDataIfNeeded:receivedNumChannels:.heartbeat.14603
- __handleAudioChunk:.heartbeat_CORESPEECH_VOICETRIGGER_FIRSTPASS_LPCM_RECORD_BUFFER_AVAILABLE.18662
- __keywordAnalyzerNDAPI:hasResultAvailable:forChannel:.heartbeat.11004
- __keywordAnalyzerNDAPI:hasResultAvailable:forChannel:.heartbeat.18653
- __keywordAnalyzerNDAPI:hasResultAvailable:forChannel:.heartbeat.26744
- _sharedController.onceToken.11866
- _sharedController.sharedController.11868
- _sharedHandler.onceToken.19325
- _sharedHandler.onceToken.26044
- _sharedHandler.sharedHandler.19327
- _sharedHandler.sharedHandler.26046
- _sharedHandlerDisabledOnDeviceCompilation.onceToken.26039
- _sharedHandlerDisabledOnDeviceCompilation.sharedHandler.26041
- _sharedInstance._sharedInstance.11695
- _sharedInstance._sharedInstance.12881
- _sharedInstance._sharedInstance.14824
- _sharedInstance._sharedInstance.17141
- _sharedInstance._sharedInstance.17439
- _sharedInstance._sharedInstance.17515
- _sharedInstance._sharedInstance.18157
- _sharedInstance._sharedInstance.19661
- _sharedInstance._sharedInstance.20000
- _sharedInstance._sharedInstance.20052
- _sharedInstance._sharedInstance.20233
- _sharedInstance._sharedInstance.23511
- _sharedInstance._sharedInstance.24189
- _sharedInstance._sharedInstance.25867
- _sharedInstance._sharedInstance.27275
- _sharedInstance._sharedInstance.5686
- _sharedInstance._sharedInstance.5797
- _sharedInstance._sharedInstance.6085
- _sharedInstance._sharedInstance.6631
- _sharedInstance._sharedInstance.9233
- _sharedInstance.onceToken.10412
- _sharedInstance.onceToken.10648
- _sharedInstance.onceToken.10806
- _sharedInstance.onceToken.11693
- _sharedInstance.onceToken.12824
- _sharedInstance.onceToken.12879
- _sharedInstance.onceToken.13458
- _sharedInstance.onceToken.14822
- _sharedInstance.onceToken.15347
- _sharedInstance.onceToken.15432
- _sharedInstance.onceToken.15924
- _sharedInstance.onceToken.17139
- _sharedInstance.onceToken.17437
- _sharedInstance.onceToken.17513
- _sharedInstance.onceToken.17621
- _sharedInstance.onceToken.18086
- _sharedInstance.onceToken.18155
- _sharedInstance.onceToken.18185
- _sharedInstance.onceToken.19544
- _sharedInstance.onceToken.19659
- _sharedInstance.onceToken.19998
- _sharedInstance.onceToken.20050
- _sharedInstance.onceToken.20231
- _sharedInstance.onceToken.21070
- _sharedInstance.onceToken.21251
- _sharedInstance.onceToken.21344
- _sharedInstance.onceToken.21467
- _sharedInstance.onceToken.22636
- _sharedInstance.onceToken.22808
- _sharedInstance.onceToken.22958
- _sharedInstance.onceToken.23509
- _sharedInstance.onceToken.23810
- _sharedInstance.onceToken.24187
- _sharedInstance.onceToken.25526
- _sharedInstance.onceToken.25865
- _sharedInstance.onceToken.27057
- _sharedInstance.onceToken.27273
- _sharedInstance.onceToken.5684
- _sharedInstance.onceToken.5795
- _sharedInstance.onceToken.6083
- _sharedInstance.onceToken.6629
- _sharedInstance.onceToken.9231
- _sharedInstance.sSharedInstance.18187
- _sharedInstance.sharedInstance.12826
- _sharedInstance.sharedInstance.13460
- _sharedInstance.sharedInstance.15434
- _sharedInstance.sharedInstance.18088
- _sharedInstance.sharedInstance.19546
- _sharedInstance.sharedInstance.21072
- _sharedInstance.sharedInstance.21346
- _sharedInstance.sharedInstance.22810
- _sharedInstance.sharedInstance.22960
- _sharedInstance.sharedInstance.27059
- _sharedInstance.sharedManager.25528
- _sharedInstance.sharedPolicy.21253
- _sharedInstance.sharedPolicy.23812
- _sharedInstance.sharedProvider.22638
- _sharedManager.onceToken.17084
- _sharedManager.onceToken.19018
- _sharedManager.onceToken.6492
- _sharedManager.onceToken.6912
- _sharedManager.sharedManager.17086
- _sharedManager.sharedManager.6494
- _sharedManager.sharedManager.6914
- _sharedMonitor.onceToken.20155
- _sharedMonitor.sharedMonitor.20157
- _sharedService.onceToken.15966
- _sharedService.onceToken.25194
- _sharedService.sharedService.25196
Functions:
~ -[CSSpeechController endpointerModelVersion] : 536 -> 852
~ -[CSBundleAudioInjectionEngine setPluginBundleWithPath:withOutError:] : 992 -> 976
CStrings:
+ "%s return hybrid model version for sirix request: %{public}@"
+ "4"
+ "setWithObjects:"
- "%s return hybrid model version for request on HomePod or supported device + locale"
- "%s return hybrid model version for sirix request"

```
