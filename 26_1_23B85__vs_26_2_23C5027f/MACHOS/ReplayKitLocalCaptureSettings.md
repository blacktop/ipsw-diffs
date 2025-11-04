## ReplayKitLocalCaptureSettings

> `/System/Library/PreferenceBundles/ReplayKitLocalCaptureSettings.bundle/ReplayKitLocalCaptureSettings`

```diff

-680.7.1.1.2
-  __TEXT.__text: 0x2acc
-  __TEXT.__auth_stubs: 0x280
-  __TEXT.__objc_stubs: 0x900
-  __TEXT.__objc_methlist: 0x31c
+685.1.1.0.0
+  __TEXT.__text: 0x43c8
+  __TEXT.__auth_stubs: 0x3a0
+  __TEXT.__objc_stubs: 0xf20
+  __TEXT.__objc_methlist: 0x5fc
   __TEXT.__const: 0x68
-  __TEXT.__cstring: 0x656
-  __TEXT.__oslogstring: 0x55d
-  __TEXT.__objc_classname: 0x50
-  __TEXT.__objc_methname: 0x9df
-  __TEXT.__objc_methtype: 0x20c
-  __TEXT.__unwind_info: 0xd0
-  __DATA_CONST.__auth_got: 0x148
-  __DATA_CONST.__got: 0xd8
-  __DATA_CONST.__const: 0x68
-  __DATA_CONST.__cfstring: 0x320
-  __DATA_CONST.__objc_classlist: 0x8
+  __TEXT.__objc_methname: 0x1423
+  __TEXT.__cstring: 0x99c
+  __TEXT.__oslogstring: 0x6ff
+  __TEXT.__objc_classname: 0x92
+  __TEXT.__objc_methtype: 0x34a
+  __TEXT.__unwind_info: 0x128
+  __DATA_CONST.__auth_got: 0x1d8
+  __DATA_CONST.__got: 0x158
+  __DATA_CONST.__const: 0x90
+  __DATA_CONST.__cfstring: 0x680
+  __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x10
+  __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x8
-  __DATA.__objc_const: 0x2b0
-  __DATA.__objc_selrefs: 0x3a0
-  __DATA.__objc_ivar: 0x8
-  __DATA.__objc_data: 0x50
-  __DATA.__data: 0xc8
+  __DATA_CONST.__objc_superrefs: 0x18
+  __DATA_CONST.__objc_intobj: 0xf0
+  __DATA.__objc_const: 0xb30
+  __DATA.__objc_selrefs: 0x5e0
+  __DATA.__objc_ivar: 0x64
+  __DATA.__objc_data: 0xf0
+  __DATA.__data: 0x128
   __DATA.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
+  - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers
   - /System/Library/PrivateFrameworks/Preferences.framework/Preferences
+  - /System/Library/PrivateFrameworks/RTCReporting.framework/RTCReporting
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C15252CB-5EEE-3ED2-87A4-32AD3ACBFB4D
-  Functions: 44
-  Symbols:   81
-  CStrings:  254
+  UUID: 00EF1193-30A4-3B25-95AE-F314D52BD726
+  Functions: 104
+  Symbols:   121
+  CStrings:  465
 
Symbols:
+ _CGSizeZero
+ _OBJC_CLASS_$_NSConstantIntegerNumber
+ _OBJC_CLASS_$_NSDate
+ _OBJC_CLASS_$_NSDictionary
+ _OBJC_CLASS_$_NSMutableDictionary
+ _OBJC_CLASS_$_NSObject
+ _OBJC_CLASS_$_RPReportingAgent
+ _OBJC_CLASS_$_RPThermalPressure
+ _OBJC_CLASS_$_RTCReporting
+ _OBJC_METACLASS_$_RPReportingAgent
+ _OBJC_METACLASS_$_RPThermalPressure
+ ___NSDictionary0__struct
+ ___kCFBooleanTrue
+ __os_log_error_impl
+ _kOSThermalNotificationPressureLevelName
+ _kRTCReportingSessionInfoBatchEvent
+ _kRTCReportingSessionInfoClientBundleID
+ _kRTCReportingSessionInfoClientType
+ _kRTCReportingSessionInfoClientVersion
+ _kRTCReportingSessionInfoRequireUserInfo
+ _kRTCReportingSessionInfoSessionID
+ _kRTCReportingUserInfoClientName
+ _kRTCReportingUserInfoServiceName
+ _notify_cancel
+ _notify_get_state
+ _notify_register_check
+ _notify_register_dispatch
+ _objc_destroyWeak
+ _objc_enumerationMutation
+ _objc_loadWeakRetained
+ _objc_release_x1
+ _objc_release_x27
+ _objc_retain_x21
+ _objc_retain_x22
+ _objc_retain_x23
+ _objc_retain_x24
+ _objc_retain_x4
+ _objc_retain_x8
+ _objc_storeWeak
+ _objc_unsafeClaimAutoreleasedReturnValue
CStrings:
+ " [DEBUG] %{public}s:%d %@"
+ " [DEBUG] %{public}s:%d reported eventType:%d payloadDict=%@"
+ " [ERROR] %{public}s:%d error reporting eventType:%d error code:%d"
+ " [ERROR] %{public}s:%d payloadDict cannot be null!"
+ " [INFO] %{public}s:%d %p"
+ " [INFO] %{public}s:%d Reporting settings UI event: action=%ld"
+ " [INFO] %{public}s:%d level=%ld"
+ " [INFO] %{public}s:%d reporting with endReason=%ld"
+ " [INFO] %{public}s:%d unknown pressure level"
+ "!"
+ "%s%@"
+ "+[RPReportingAgent reportSettingsUIEventWithAction:]"
+ "+[RPReportingAgent sendReportEventWithType:dictionary:withServiceName:clientBundleId:sessionID:]"
+ "+[RPReportingAgent sendReportSessionEnded:endReason:withServiceName:clientBundleId:sessionID:payload:]"
+ ","
+ "-[RPReportingAgent collectSummaryEventMetrics]"
+ "-[RPReportingAgent initWithServiceName:]"
+ "-[RPReportingAgent thermalPressureDidChangeWithLevel:]"
+ "-[RPThermalPressure convertThermalPressureLevel:]"
+ "@\"<RPThermalPressureDelegate>\""
+ "@\"NSDate\""
+ "@\"NSMutableDictionary\""
+ "@\"NSString\""
+ "@\"RPThermalPressure\""
+ "ActiveDuration"
+ "AppAudioCaptureRate"
+ "AppAudioFrameCount"
+ "AudioOnly"
+ "BackCameraUsed"
+ "BroadcastExtensionBundleID"
+ "CHDR"
+ "ClientAppBundleID"
+ "CustomDir"
+ "EndReason"
+ "FrontCameraUsed"
+ "HQLRRecording"
+ "MRC"
+ "MicCaptureRate"
+ "MicFrameCount"
+ "Q"
+ "RPReportingAgent"
+ "RPThermalPressure"
+ "RPThermalPressureDelegate"
+ "RecordedFileSize"
+ "ReplayKit"
+ "SCKCapture"
+ "SaveDest"
+ "SettingsUIAction"
+ "T@\"<RPThermalPressureDelegate>\",W,N,V_delegate"
+ "T@\"NSDate\",N,V_captureStartTime"
+ "T@\"NSString\",&,N,V_serviceName"
+ "TB,N,V_audioOnlyRecording"
+ "TB,N,V_backCameraUsed"
+ "TB,N,V_frontCameraUsed"
+ "TB,N,V_isHDR"
+ "TB,N,V_usesCustomSaveDirectory"
+ "TPL"
+ "TQ,N,V_recordedFileSize"
+ "Tq,N,V_appAudioFrameCount"
+ "Tq,N,V_endReason"
+ "Tq,N,V_micFrameCount"
+ "Tq,N,V_mixedRealityCameraEnabled"
+ "Tq,N,V_saveDestinationType"
+ "Tq,N,V_videoCaptureRate"
+ "Tq,N,V_videoFrameCount"
+ "T{CGSize=dd},N,V_videoCaptureSize"
+ "VideoCaptureHeight"
+ "VideoCaptureRate"
+ "VideoCaptureWidth"
+ "VideoFrameCount"
+ "_appAudioFrameCount"
+ "_audioOnlyRecording"
+ "_backCameraUsed"
+ "_captureStartTime"
+ "_delegate"
+ "_endReason"
+ "_frontCameraUsed"
+ "_isHDR"
+ "_micFrameCount"
+ "_mixedRealityCameraEnabled"
+ "_newThermalLevel"
+ "_recordedFileSize"
+ "_saveDestinationType"
+ "_serviceName"
+ "_thermalLevel"
+ "_thermalLevelIntervalStartTime"
+ "_thermalNotificationToken"
+ "_thermalPressureMonitor"
+ "_thermalResults"
+ "_usesCustomSaveDirectory"
+ "_videoCaptureRate"
+ "_videoCaptureSize"
+ "_videoFrameCount"
+ "addToThermalResultsWithLevel:"
+ "allKeys"
+ "appAudioFrameCount"
+ "audioOnlyRecording"
+ "backCameraUsed"
+ "captureStartTime"
+ "code"
+ "collectSummaryEventMetrics"
+ "com.apple.Preferences"
+ "convertThermalPressureLevel:"
+ "countByEnumeratingWithState:objects:count:"
+ "date"
+ "delegate"
+ "dictionaryWithObjects:forKeys:count:"
+ "doubleValue"
+ "endReason"
+ "frontCameraUsed"
+ "getCurrentPressureLevel"
+ "getStateWithToken:"
+ "i"
+ "i20@0:8i16"
+ "init"
+ "initWithDictionary:"
+ "initWithServiceName:"
+ "isHDR"
+ "micFrameCount"
+ "mixedRealityCameraEnabled"
+ "numberWithDouble:"
+ "numberWithInteger:"
+ "numberWithLong:"
+ "numberWithUnsignedInt:"
+ "numberWithUnsignedInteger:"
+ "objectForKeyedSubscript:"
+ "q"
+ "q16@0:8"
+ "q20@0:8i16"
+ "recordedFileSize"
+ "removeAllObjects"
+ "reportEventWithType:dictionary:clientBundleId:"
+ "reportSCEventWithType:dictionary:streamID:"
+ "reportSCSessionErroredWithEventType:endReason:streamID:payload:"
+ "reportSessionEnded:endReason:withServiceName:clientBundleId:"
+ "reportSettingsUIEventWithAction:"
+ "resetReportingMetrics"
+ "resetThermalResults"
+ "saveDestinationType"
+ "sendOneMessageWithSessionInfo:userInfo:category:type:payload:error:"
+ "sendReportEventWithType:dictionary:withServiceName:clientBundleId:sessionID:"
+ "sendReportSessionEnded:endReason:withServiceName:clientBundleId:sessionID:payload:"
+ "serviceName"
+ "setAppAudioFrameCount:"
+ "setAudioOnlyRecording:"
+ "setBackCameraUsed:"
+ "setCaptureStartTime:"
+ "setEndReason:"
+ "setFrontCameraUsed:"
+ "setIsHDR:"
+ "setMicFrameCount:"
+ "setMixedRealityCameraEnabled:"
+ "setObject:forKeyedSubscript:"
+ "setRecordedFileSize:"
+ "setSaveDestinationType:"
+ "setServiceName:"
+ "setUsesCustomSaveDirectory:"
+ "setVideoCaptureRate:"
+ "setVideoCaptureSize:"
+ "setVideoFrameCount:"
+ "startMonitoring"
+ "stopMonitoring"
+ "stringByAppendingFormat:"
+ "thermalDescription"
+ "thermalPressureDidChangeWithLevel:"
+ "thermalPressureDidChangeWithThermalLevel:"
+ "timeIntervalSinceDate:"
+ "usesCustomSaveDirectory"
+ "v12@?0i8"
+ "v20@0:8i16"
+ "v24@0:8Q16"
+ "v24@0:8q16"
+ "v32@0:8{CGSize=dd}16"
+ "v36@0:8S16@20@28"
+ "v44@0:8S16@20@28@36"
+ "v52@0:8S16@20@28@36@44"
+ "v60@0:8S16@20@28@36@44@52"
+ "videoCaptureRate"
+ "videoCaptureSize"
+ "videoFrameCount"
+ "{CGSize=\"width\"d\"height\"d}"
+ "{CGSize=dd}16@0:8"

```
