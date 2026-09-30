## nebulad

> `/System/Library/PrivateFrameworks/CameraUI.framework/Support/nebulad`

```diff

-4020.3.21.0.0
-  __TEXT.__text: 0x790
-  __TEXT.__auth_stubs: 0x230
-  __TEXT.__objc_stubs: 0x160
-  __TEXT.__objc_methlist: 0x5c
-  __TEXT.__const: 0x10
-  __TEXT.__gcc_except_tab: 0x28
-  __TEXT.__cstring: 0x7f
-  __TEXT.__objc_methname: 0x12a
-  __TEXT.__objc_classname: 0x1b
-  __TEXT.__objc_methtype: 0x38
-  __TEXT.__unwind_info: 0x98
-  __DATA_CONST.__auth_got: 0x128
-  __DATA_CONST.__got: 0x40
-  __DATA_CONST.__const: 0xe0
-  __DATA_CONST.__cfstring: 0x40
-  __DATA_CONST.__objc_classlist: 0x8
+4020.5.0.0.0
+  __TEXT.__text: 0x1890
+  __TEXT.__auth_stubs: 0x380
+  __TEXT.__objc_stubs: 0x420
+  __TEXT.__objc_methlist: 0x14c
+  __TEXT.__const: 0x28
+  __TEXT.__gcc_except_tab: 0x70
+  __TEXT.__cstring: 0x13f
+  __TEXT.__oslogstring: 0x493
+  __TEXT.__objc_methname: 0x528
+  __TEXT.__objc_classname: 0x3a
+  __TEXT.__objc_methtype: 0xf7
+  __TEXT.__unwind_info: 0x110
+  __DATA_CONST.__auth_got: 0x1d0
+  __DATA_CONST.__got: 0x58
+  __DATA_CONST.__const: 0x1c0
+  __DATA_CONST.__cfstring: 0x100
+  __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x8
-  __DATA.__objc_const: 0xf8
-  __DATA.__objc_selrefs: 0x70
-  __DATA.__objc_ivar: 0xc
-  __DATA.__objc_data: 0x50
-  __DATA.__bss: 0x10
+  __DATA_CONST.__objc_superrefs: 0x10
+  __DATA.__objc_const: 0x2b8
+  __DATA.__objc_selrefs: 0x138
+  __DATA.__objc_ivar: 0x24
+  __DATA.__objc_data: 0xa0
+  __DATA.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
+  - /System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/BackgroundSystemTasks
   - /System/Library/PrivateFrameworks/CameraUI.framework/CameraUI
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/PhotoLibraryServicesCore.framework/PhotoLibraryServicesCore
+  - /System/Library/PrivateFrameworks/PowerLog.framework/PowerLog
+  - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
+  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 12
-  Symbols:   52
-  CStrings:  30
+  Functions: 47
+  Symbols:   76
+  CStrings:  104
 
Symbols:
+ _objc_retain_x1
+ _objc_copyWeak
+ _objc_loadWeakRetained
+ _PPSCreateTelemetryIdentifier
+ __os_log_error_impl
+ _PPSSendTelemetry
+ _objc_retain_x23
+ _os_log_create
+ __os_log_impl
+ _objc_release_x24
+ _objc_retain_x22
+ _os_log_type_enabled
+ _objc_initWeak
+ _OBJC_CLASS_$_NSDictionary
+ _objc_release_x23
+ _objc_release_x9
+ _OBJC_CLASS_$_SBSCaptureButtonAppConfigurationCoordinator
+ _MGGetBoolAnswer
+ _objc_release
+ _objc_setProperty_nonatomic_copy
+ _objc_destroyWeak
+ _objc_retain_x19
+ _OBJC_CLASS_$_BGSystemTaskScheduler
+ _objc_alloc
CStrings:
+ "setTaskCompleted"
+ "@\"NSObject<OS_dispatch_queue>\""
+ "@?"
+ "_numberOfMetricsSubmitted"
+ "com.apple.camera"
+ "$"
+ "@\"<BSInvalidatable>\""
+ "Q"
+ "^{PPSTelemetryIdentifier=}16@0:8"
+ "addObserverForAssociatedAppUpdatesUsingBlock:"
+ "getCameraCaptureStreamID"
+ "set_numberMetricSubmisions:"
+ "Q16@0:8"
+ "T@\"NSObject<OS_dispatch_queue>\",R,N,V__metricQueue"
+ "__completion"
+ "eventName"
+ "v24@0:8@16"
+ "CAMDailySettingsUseCaseEvent"
+ "DailySettingsUseCaseEvent addObserverForAssociatedAppUpdatesUsingBlock error casting to strong"
+ "_metricQueue"
+ "Button"
+ "DailySettingsUseCaseEvent submitCameraCapturePreferencesWithCompletion not supported"
+ "__numberOfMetricsSubmitted"
+ "dictionaryWithObjects:forKeys:count:"
+ "TQ,N,V__numberMetricSubmisions"
+ "_appConfigurationController"
+ "@\"SBSCaptureButtonAppConfigurationCoordinator\""
+ "DailySettingsUseCaseEvent submitCameraCapturePreferencesWithCompletion called"
+ "DailySettingsUseCaseEvent submitCameraCapturePreferencesWithCompletion completed %!{(MISSING)public}@"
+ "@32@0:8@16@?24"
+ "_queue"
+ "invalidate"
+ "T@\"<BSInvalidatable>\",R,N,V__associatedAppObserver"
+ "__metricQueue"
+ "com.apple.camera.CAMNebulaDaemon.DailySettingsUseCaseEvent"
+ "CaptureButtonConfig"
+ "DailySettingsUseCaseEvent abort requested"
+ "DailySettingsUseCaseEvent isMetricSubmissionsCompleted _numberOfMetricsSubmitted %!{(MISSING)public}lu _numberMetricSubmisions %!{(MISSING)public}lu"
+ "DailySettingsUseCaseEvent submitMetrics completionSync error casting to strong"
+ "setExpirationHandler:"
+ "v24@0:8Q16"
+ "DailySettingsUseCaseEvent completed"
+ "T@\"SBSCaptureButtonAppConfigurationCoordinator\",R,N,V__appConfigurationController"
+ "_associatedAppObserver"
+ "dealloc"
+ "isMetricSubmissionsCompleted"
+ "registerForBackgroundTaskWithQueue:"
+ "registerForTaskWithIdentifier:usingQueue:launchHandler:"
+ "Config"
+ "DailySettingsUseCaseEvent addObserverForAssociatedAppUpdatesUsingBlock completion error casting to strong"
+ "T@?,C,N,V__completion"
+ "TQ,N,V__numberOfMetricsSubmitted"
+ "sharedScheduler"
+ "v16@?0@\"BGRepeatingSystemTask\"8"
+ "__associatedAppObserver"
+ "__numberMetricSubmisions"
+ "CameraButtonCapability"
+ "DailySettingsUseCaseEvent submitMetrics completionSync called"
+ "__appConfigurationController"
+ "submitCameraCapturePreferencesWithCompletion:"
+ "v16@?0@\"NSString\"8"
+ "DailySettingsUseCaseEvent submitMetrics completionSync completed"
+ "Nebula"
+ "_completion"
+ "set_numberOfMetricsSubmitted:"
+ "set_completion:"
+ "DailySettingsUseCaseEvent Registering to run in background"
+ "DailySettingsUseCaseEvent submitCameraCapturePreferencesWithCompletion error already submit"
+ "initWithQueue:andMetricsSubmittedBlock:"
+ "submitMetrics"
+ "@?16@0:8"
+ "DailySettingsUseCaseEvent Running in background"
+ "DailySettingsUseCaseEvent submitCameraCapturePreferencesWithCompletion dispatched with info %!{(MISSING)public}@"
+ "_numberMetricSubmisions"

```
