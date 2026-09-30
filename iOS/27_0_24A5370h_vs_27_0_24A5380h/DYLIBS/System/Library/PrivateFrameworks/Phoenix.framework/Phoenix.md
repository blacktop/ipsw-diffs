## Phoenix

> `/System/Library/PrivateFrameworks/Phoenix.framework/Phoenix`

```diff

-  __TEXT.__text: 0x236a8
+  __TEXT.__text: 0x22b94
   __TEXT.__objc_methlist: 0x1d5c
-  __TEXT.__const: 0xbc
+  __TEXT.__const: 0xb0
   __TEXT.__dlopen_cstrs: 0x4b
   __TEXT.__gcc_except_tab: 0x150
   __TEXT.__cstring: 0x249f

   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xf0
   __DATA_CONST.__objc_arraydata: 0x40
-  __DATA_CONST.__got: 0x2f8
+  __DATA_CONST.__got: 0x2e8
   __AUTH_CONST.__const: 0x180
   __AUTH_CONST.__cfstring: 0x18e0
   __AUTH_CONST.__objc_const: 0x3a70
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__objc_doubleobj : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH.__objc_data : content changed
~ __DATA.__data : content changed
Functions:
~ -[AXPhoenixEventMonitor init] : 240 -> 236
~ -[AXPhoenixEventMonitor dealloc] : 88 -> 84
~ -[AXPhoenixEventMonitor addObserver:] : 268 -> 248
~ ___37-[AXPhoenixEventMonitor addObserver:]_block_invoke : 200 -> 196
~ -[AXPhoenixEventMonitor removeObserver:] : 268 -> 248
~ ___40-[AXPhoenixEventMonitor removeObserver:]_block_invoke : 160 -> 156
~ -[AXPhoenixEventMonitor enumerateObserversInQueue:] : 268 -> 248
~ -[AXPhoenixEventMonitor enumerateObservers:] : 384 -> 376
~ -[AXPhoenixMitigator initWithDelegate:configuration:] : 552 -> 548
~ -[AXPhoenixMitigator startWithCompletion:] : 264 -> 244
~ ___42-[AXPhoenixMitigator startWithCompletion:]_block_invoke : 496 -> 488
~ -[AXPhoenixMitigator stop] : 196 -> 180
~ -[AXPhoenixMitigator isRunning] : 244 -> 224
~ -[AXPhoenixMitigator dealloc] : 120 -> 116
~ -[AXPhoenixMitigator setIsHandHeld:] : 420 -> 396
~ -[AXPhoenixMitigator setDisplayOn:] : 440 -> 412
~ -[AXPhoenixMitigator setDeviceLocked:] : 420 -> 396
~ -[AXPhoenixMitigator setTouchOn:] : 444 -> 420
~ -[AXPhoenixMitigator _subscribeEventMonitors] : 216 -> 200
~ -[AXPhoenixMitigator _unsubscribeEventMonitors] : 308 -> 304
~ -[AXPhoenixMitigator phoenixEventMonitorDidReceiveEvent:] : 224 -> 208
~ -[AXPhoenixMitigator phoenixDeviceLockMonitor:didReceiveDeviceLockStateChanged:timestamp:] : 268 -> 256
~ -[AXPhoenixMitigator phoenixDisplayStatusMonitor:didReceiveDisplayStateChanged:timestamp:] : 268 -> 256
~ -[AXPhoenixMitigator gestureMonitorDidReceiveWakeGesture:timestamp:] : 288 -> 268
~ -[AXPhoenixMitigator gestureMonitorDidReceiveSleepGesture:timestamp:] : 288 -> 268
~ -[AXPhoenixClassifierRNNModelWindow updateHistoryShape:] : 456 -> 452
~ -[AXPhoenixClassifierRNNModelWindow setFoundTap:] : 40 -> 44
~ -[AXPhoenixClassifierRNNModelInputData updateInputShape:] : 308 -> 304
~ -[AXPhoenixClassifierRNN initWithDelegate:modelURL:configuration:] : 1420 -> 1348
~ -[AXPhoenixClassifierRNN handleAccelerometerData:withTimestamp:] : 244 -> 220
~ -[AXPhoenixClassifierRNN reset] : 196 -> 180
~ ___31-[AXPhoenixClassifierRNN reset]_block_invoke : 176 -> 168
~ -[AXPhoenixClassifierRNN setTapSpeed:] : 84 -> 76
~ -[AXPhoenixClassifierRNN _initializeModelFromURL:outError:] : 1948 -> 1920
~ -[AXPhoenixClassifierRNN _windowData:] : 1200 -> 1180
~ -[AXPhoenixClassifierRNN _handleAccelerometerData:withTimestamp:] : 896 -> 884
~ -[AXPhoenixClassifierRNN _updateAccelerationData] : 2844 -> 2788
~ -[AXPhoenixClassifierRNN _evaluateTapData] : 1316 -> 1284
~ ___59-[AXPhoenixClassifierRNN _logWindowData:doubleTap:tapData:]_block_invoke : 136 -> 140
~ -[AXPhoenixClassifierRNN _multiArrayInputForClassifierWithError:] : 1124 -> 1008
~ -[AXPhoenixClassifierRNN setFalsePositiveLoggingEnabled:] : 40 -> 44
~ -[AXPhoenixWakeGestureMonitor init] : 204 -> 200
~ -[AXPhoenixWakeGestureMonitor _didReceiveWakeGesture] : 228 -> 208
~ -[AXPhoenixWakeGestureMonitor _didReceiveSleepGesture] : 228 -> 208
~ -[AXPhoenixWakeGestureMonitor wakeGestureTimestamp] : 44 -> 40
~ -[AXPhoenixWakeGestureMonitor setWakeGestureTimestamp:] : 52 -> 48
~ -[AXPhoenixWakeGestureMonitor dismissalTimestamp] : 44 -> 40
~ -[AXPhoenixWakeGestureMonitor setDismissalTimestamp:] : 52 -> 48
~ -[AXPhoenixWakeGestureMonitor gestureManager] : 44 -> 40
~ -[AXPhoenixWakeGestureMonitor setGestureManager:] : 68 -> 64
~ -[AXPhoenixWakeGestureMonitor .cxx_destruct] : 64 -> 60
~ _CoreMotionLibraryCore : 180 -> 168
~ ___CoreMotionLibraryCore_block_invoke : 148 -> 140
~ -[AXPhoenixBlobbyUploader _hmacSHA1WithKey:forData:] : 352 -> 348
~ -[AXPhoenixBlobbyUploader _getAuthorizationForRequest:headers:] : 968 -> 956
~ -[AXPhoenixBlobbyUploader _urlRequestForFileAtPath:bucket:prefix:error:] : 1856 -> 1832
~ -[AXPhoenixBlobbyUploader _uploadPackage:bucket:prefix:withCompletion:] : 788 -> 760
~ -[AXPhoenixBlobbyUploader _uploadPackagePath:bucket:prefix:withCompletion:] : 600 -> 568
~ ___75-[AXPhoenixBlobbyUploader _uploadPackagePath:bucket:prefix:withCompletion:]_block_invoke : 676 -> 644
~ -[AXPhoenixBlobbyUploader uploadPackages:toBucket:withCompletion:] : 436 -> 404
~ ___66-[AXPhoenixBlobbyUploader uploadPackages:toBucket:withCompletion:]_block_invoke : 896 -> 868
~ ___66-[AXPhoenixBlobbyUploader uploadPackages:toBucket:withCompletion:]_block_invoke.102 : 872 -> 864
~ -[AXPhoenixBlobbyUploader init] : 648 -> 616
~ -[AXPhoenixAnalytics initWithConfiguration:modelVersion:assetVersion:] : 408 -> 396
~ -[AXPhoenixAnalytics logEventWithType:machAbsoluteTime:context:completion:] : 1172 -> 1148
~ -[AXPhoenixAnalytics _sendEvent:completion:] : 424 -> 408
~ +[AXPhoenixDataCollectionUtils moveFiles:from:to:] : 1012 -> 988
~ -[AXPhoenixMetadataLogger initWithMetadata:] : 220 -> 216
~ -[AXPhoenixMetadataLogger writeMetadataToFileWithSensors:withAnnotations:withFalsePositivesMetadata:] : 2004 -> 1916
~ -[AXPhoenixMetadataLogger _deviceModelName] : 184 -> 300
~ -[AXPhoenixGestureDetector initWithDelegate:] : 440 -> 420
~ -[AXPhoenixGestureDetector _initializeAssetDrivenComponentsWithLocalURL:assetVersion:] : 984 -> 936
~ -[AXPhoenixGestureDetector _startWithCompletion:] : 264 -> 244
~ ___49-[AXPhoenixGestureDetector _startWithCompletion:]_block_invoke : 616 -> 592
~ -[AXPhoenixGestureDetector _stopWithCompletion:] : 384 -> 364
~ ___48-[AXPhoenixGestureDetector _stopWithCompletion:]_block_invoke : 356 -> 348
~ -[AXPhoenixGestureDetector setTapSpeed:] : 72 -> 68
~ ___59-[AXPhoenixGestureDetector _startClassifierWithCompletion:]_block_invoke : 848 -> 828
~ -[AXPhoenixGestureDetector setFalsePositiveLoggingEnabled:] : 280 -> 284
~ -[AXPhoenixGestureDetector setRnnModelEnabled:] : 284 -> 268
~ ___47-[AXPhoenixGestureDetector setRnnModelEnabled:]_block_invoke : 252 -> 232
~ ___47-[AXPhoenixGestureDetector setRnnModelEnabled:]_block_invoke_2 : 820 -> 788
~ ___47-[AXPhoenixGestureDetector setRnnModelEnabled:]_block_invoke.53 : 480 -> 472
~ -[AXPhoenixGestureDetector phoenixClassifier:failedWithError:] : 296 -> 276
~ ___62-[AXPhoenixGestureDetector phoenixClassifier:failedWithError:]_block_invoke : 380 -> 360
~ -[AXPhoenixGestureDetector phoenixClassifierDidDetectDoubleTap:data:context:] : 344 -> 308
~ ___77-[AXPhoenixGestureDetector phoenixClassifierDidDetectDoubleTap:data:context:]_block_invoke_2 : 536 -> 532
~ -[AXPhoenixGestureDetector phoenixClassifierDidDetectTripleTap:data:context:] : 344 -> 308
~ ___77-[AXPhoenixGestureDetector phoenixClassifierDidDetectTripleTap:data:context:]_block_invoke_2 : 536 -> 532
~ -[AXPhoenixGestureDetector phoenixMitigator:didFailWithError:] : 420 -> 400
~ ___62-[AXPhoenixGestureDetector phoenixMitigator:didFailWithError:]_block_invoke : 92 -> 88
~ -[AXPhoenixGestureDetector phoenixMitigator:displayOnDidChange:] : 284 -> 268
~ ___64-[AXPhoenixGestureDetector phoenixMitigator:displayOnDidChange:]_block_invoke : 696 -> 656
~ -[AXPhoenixGestureDetector phoenixMitigator:touchOnDidChange:] : 244 -> 232
~ -[AXPhoenixGestureDetector modelDidUpdate:assetVersion:] : 312 -> 288
~ ___56-[AXPhoenixGestureDetector modelDidUpdate:assetVersion:]_block_invoke : 576 -> 552
~ ___56-[AXPhoenixGestureDetector modelDidUpdate:assetVersion:]_block_invoke.124 : 872 -> 836
~ ___56-[AXPhoenixGestureDetector modelDidUpdate:assetVersion:]_block_invoke.128 : 496 -> 488
~ -[AXPhoenixClassifierConfiguration init] : 160 -> 156
~ -[AXPhoenixClassifierConfiguration initWithDictionary:missingKeys:] : 228 -> 224
~ -[AXPhoenixDeviceLockMonitor init] : 156 -> 152
~ -[AXPhoenixDeviceLockMonitor _startMonitoringWithQueue:] : 220 -> 204
~ -[AXPhoenixDeviceLockMonitor isDeviceLocked] : 48 -> 44
~ -[AccelerometerData initWithData:timestamp:] : 208 -> 204
~ -[AccelerometerBuffer initWithCapacity:accelerometerSampleRateInHz:] : 244 -> 232
~ ___32-[AccelerometerBuffer logBuffer]_block_invoke : 492 -> 488
~ ___32-[AccelerometerBuffer logBuffer]_block_invoke.41 : 472 -> 424
~ -[AccelerometerBuffer csv] : 244 -> 224
~ -[AccelerometerBuffer description] : 228 -> 208
~ -[Prediction initWithModelOutput:] : 448 -> 412
~ -[PredictionsBuffer initWithConfiguration:] : 364 -> 340
~ -[PredictionsBuffer reset] : 120 -> 128
~ -[PredictionsBuffer addPrediction:] : 1140 -> 1116
~ -[PredictionsBuffer logBuffer] : 228 -> 208
~ ___30-[PredictionsBuffer logBuffer]_block_invoke : 476 -> 428
~ -[AXPhoenixClassifier initWithDelegate:modelURL:configuration:] : 1624 -> 1544
~ -[AXPhoenixClassifier dealloc] : 112 -> 108
~ -[AXPhoenixClassifier handleAccelerometerData:withTimestamp:] : 244 -> 220
~ -[AXPhoenixClassifier reset] : 196 -> 180
~ -[AXPhoenixClassifier _initializeModelFromURL:outError:] : 1952 -> 1908
~ -[AXPhoenixClassifier _createMultiArrayWithError:] : 220 -> 216
~ -[AXPhoenixClassifier _windowData:] : 1032 -> 1020
~ -[AXPhoenixClassifier _handleAccelerometerData:withTimestamp:] : 2104 -> 2088
~ ___56-[AXPhoenixClassifier _logWindowData:doubleTap:tapData:]_block_invoke : 136 -> 140
~ -[AXPhoenixClassifier _clippedDataShowsPrediction:] : 1360 -> 1352
~ -[AXPhoenixClassifier _clippedMultiArrayInputWithError:beforeTime:] : 964 -> 900
~ -[AXPhoenixClassifier _multiArrayInputForClassifierWithError:] : 964 -> 900
~ -[AXPhoenixClassifier setFalsePositiveLoggingEnabled:] : 40 -> 44
~ -[AXPhoenixDataCollectionManager init] : 256 -> 252
~ -[AXPhoenixDataCollectionManager timerTick] : 244 -> 228
~ -[AXPhoenixDataCollectionManager removeOldData] : 1208 -> 1192
~ -[AXPhoenixDataCollectionManager uploadPackages] : 2232 -> 2204
~ -[AXPhoenixDataCollectionManager updateUploadStatus:error:] : 340 -> 320
~ -[AXPhoenixDataCollectionManager reportFalsePositive:] : 420 -> 416
~ -[AXPhoenixDataCollectionManager setIsRunning:] : 40 -> 44
~ -[AXPhoenixDataArchiver initWithPath:] : 452 -> 448
~ -[AXPhoenixDataArchiver addDirectoryToArchive:withDirName:] : 724 -> 716
~ -[AXPhoenixAssetMonitor initWithDelegate:] : 504 -> 476
~ -[AXPhoenixAnalyticsEvent initWithEventType:eventInfo:] : 204 -> 200
~ -[AXPhoenixAnalyticsEvent initWithCoder:] : 432 -> 400
~ -[AXPhoenixAnalyticsEvent _jsonData] : 744 -> 740
~ -[AXPhoenixDisplayStatusMonitor init] : 168 -> 164
~ -[AXPhoenixDisplayStatusMonitor _startMonitoringWithQueue:] : 260 -> 240
~ -[AXPhoenixDisplayStatusMonitor isDisplayOn] : 48 -> 44
~ -[AXPhoenixDisplayStatusMonitor notifyToken] : 44 -> 40
~ -[AXPhoenixDisplayStatusMonitor setNotifyToken:] : 52 -> 48
~ -[AXPhoenixDisplayStatusMonitor queue] : 44 -> 40
~ -[AXPhoenixDisplayStatusMonitor setQueue:] : 68 -> 64
~ -[AXPhoenixDisplayStatusMonitor .cxx_destruct] : 64 -> 60
~ -[AXPhoenixMitigatorConfiguration init] : 160 -> 156
~ -[AXPhoenixMitigatorConfiguration initWithDictionary:missingKeys:] : 228 -> 224
~ -[AXPhoenixMitigatorConfiguration setDisableWhenDisplayOff:] : 40 -> 44
~ -[AXPhoenixMitigatorConfiguration setDisableWhenDeviceLocked:] : 40 -> 44
~ -[AXPhoenixConfiguration init] : 160 -> 156
~ -[AXPhoenixConfiguration initWithContentsOfFileAtPath:] : 888 -> 884
~ -[AXPhoenixDataLogger init] : 220 -> 216
~ -[AXPhoenixDataLogger logClassifierData:isDoubleTap:startTime:endTime:completion:] : 412 -> 388
~ ___82-[AXPhoenixDataLogger logClassifierData:isDoubleTap:startTime:endTime:completion:]_block_invoke : 1992 -> 1932
~ -[AXPhoenixDataPackager initWithFileSuffixes:fromDataDirectory:] : 228 -> 224
~ -[AXPhoenixDataPackager packageDataUsingFiles:] : 764 -> 756
~ -[AXPhoenixDataPackager isValidFile:] : 400 -> 392
~ -[AXPhoenixDataPackager _createPackageDirectory:withPackageDirectoryName:] : 688 -> 684
~ -[BackTapRNNInput initWithModel_input:history:] : 236 -> 232
~ -[BackTapRNNOutput initWithOutput:updated_history:] : 236 -> 232
~ -[BackTapRNN initWithMLModel:] : 212 -> 208
~ +[BackTapRNN loadContentsOfURL:configuration:completionHandler:] : 300 -> 280
~ ___64+[BackTapRNN loadContentsOfURL:configuration:completionHandler:]_block_invoke : 204 -> 200
~ -[BackTapRNN predictionFromFeatures:completionHandler:] : 276 -> 260
~ ___55-[BackTapRNN predictionFromFeatures:completionHandler:]_block_invoke : 360 -> 340
~ -[BackTapRNN predictionFromFeatures:options:completionHandler:] : 316 -> 300
~ ___63-[BackTapRNN predictionFromFeatures:options:completionHandler:]_block_invoke : 360 -> 340
~ -[backtapInput initWithModel_input:] : 188 -> 184
~ -[backtapOutput initWithModel_output:] : 188 -> 184
~ -[backtap initWithMLModel:] : 212 -> 208
~ +[backtap loadContentsOfURL:configuration:completionHandler:] : 300 -> 280
~ ___61+[backtap loadContentsOfURL:configuration:completionHandler:]_block_invoke : 204 -> 200
~ -[backtap predictionFromFeatures:completionHandler:] : 276 -> 260
~ ___52-[backtap predictionFromFeatures:completionHandler:]_block_invoke : 284 -> 272
~ -[backtap predictionFromFeatures:options:completionHandler:] : 316 -> 300
~ ___60-[backtap predictionFromFeatures:options:completionHandler:]_block_invoke : 284 -> 272
~ _MachAbsoluteTimeToTimeIntervalSinceBoot : 124 -> 116
~ _MachAbsoluteTimeToTimeIntervalSinceBoot.79 : 124 -> 116
~ _MachAbsoluteTimeToTimeIntervalSinceBoot.625 : 124 -> 116
~ _MachAbsoluteTimeToTimeIntervalSinceBoot.1051 : 124 -> 116

```
