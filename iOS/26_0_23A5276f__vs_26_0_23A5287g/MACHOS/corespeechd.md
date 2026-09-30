## corespeechd

> `/System/Library/PrivateFrameworks/CoreSpeech.framework/corespeechd`

```diff

-3500.104.2.0.0
-  __TEXT.__text: 0x170470
-  __TEXT.__auth_stubs: 0x16f0
-  __TEXT.__objc_stubs: 0x1eb20
-  __TEXT.__objc_methlist: 0x1853c
+3500.110.4.0.0
+  __TEXT.__text: 0x16ea40
+  __TEXT.__auth_stubs: 0x16e0
+  __TEXT.__objc_stubs: 0x1e7e0
+  __TEXT.__objc_methlist: 0x1841c
   __TEXT.__dlopen_cstrs: 0x2c5
   __TEXT.__const: 0x360
-  __TEXT.__gcc_except_tab: 0x3d78
-  __TEXT.__objc_methname: 0x3e89d
-  __TEXT.__cstring: 0x2adee
-  __TEXT.__oslogstring: 0x216ad
-  __TEXT.__objc_classname: 0x3532
-  __TEXT.__objc_methtype: 0x871f
-  __TEXT.__unwind_info: 0x5620
-  __DATA_CONST.__auth_got: 0xb90
-  __DATA_CONST.__got: 0x13d0
+  __TEXT.__gcc_except_tab: 0x3cc4
+  __TEXT.__objc_methname: 0x3e430
+  __TEXT.__cstring: 0x2a9cb
+  __TEXT.__oslogstring: 0x2157f
+  __TEXT.__objc_classname: 0x34dd
+  __TEXT.__objc_methtype: 0x8634
+  __TEXT.__unwind_info: 0x55e0
+  __DATA_CONST.__auth_got: 0xb88
+  __DATA_CONST.__got: 0x1380
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x5e40
-  __DATA_CONST.__cfstring: 0x88e0
-  __DATA_CONST.__objc_classlist: 0x980
+  __DATA_CONST.__const: 0x5db8
+  __DATA_CONST.__cfstring: 0x8860
+  __DATA_CONST.__objc_classlist: 0x978
   __DATA_CONST.__objc_catlist: 0x20
-  __DATA_CONST.__objc_protolist: 0x4f0
+  __DATA_CONST.__objc_protolist: 0x4e0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0xf8
+  __DATA_CONST.__objc_protorefs: 0xf0
   __DATA_CONST.__objc_superrefs: 0x7c0
   __DATA_CONST.__objc_intobj: 0xca8
   __DATA_CONST.__objc_doubleobj: 0x80

   __DATA_CONST.__objc_arrayobj: 0x150
   __DATA_CONST.__objc_dictobj: 0x348
   __DATA_CONST.__objc_floatobj: 0x4b0
-  __DATA.__objc_const: 0x271b8
-  __DATA.__objc_selrefs: 0xb8c0
-  __DATA.__objc_ivar: 0x1de0
-  __DATA.__objc_data: 0x5f00
-  __DATA.__data: 0x3b40
-  __DATA.__bss: 0x738
+  __DATA.__objc_const: 0x26fa0
+  __DATA.__objc_selrefs: 0xb7a0
+  __DATA.__objc_ivar: 0x1dc8
+  __DATA.__objc_data: 0x5eb0
+  __DATA.__data: 0x3a80
+  __DATA.__bss: 0x718
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox

   - /System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/BackgroundSystemTasks
   - /System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary
   - /System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams
-  - /System/Library/PrivateFrameworks/CascadeSets.framework/CascadeSets
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreEmbeddedSpeechRecognition.framework/CoreEmbeddedSpeechRecognition
   - /System/Library/PrivateFrameworks/CoreSpeechDataAnalytics.framework/CoreSpeechDataAnalytics

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  UUID: C35B9E88-1B63-3EB9-9768-8EF54C9A4577
-  Functions: 9346
-  Symbols:   1018
-  CStrings:  16705
+  UUID: 8C577632-9204-3CC4-8ED9-04561F9E1529
+  Functions: 9309
+  Symbols:   1007
+  CStrings:  16620
 
Symbols:
+ _OBJC_CLASS_$_CESRSpeechProfileDispatcher
- _AFLanguageCodeDidChangeDarwinNotification
- _CESRSpeechProfileUseCaseIdentifier
- _NSInternalInconsistencyException
- _OBJC_CLASS_$_CCSetChangeXPCListener
- _OBJC_CLASS_$_CESRSpeechProfileAdminServiceFactory
- _OBJC_CLASS_$_CESRSpeechProfileBuilder
- _OBJC_CLASS_$_CESRSpeechProfileEvaluationStatus
- _OBJC_CLASS_$_CESRSpeechProfileResourceMonitor
- _OBJC_CLASS_$_CESRSpeechProfileSiteManager
- _OBJC_CLASS_$_CESRTaskCoalescer
- _OBJC_CLASS_$_NSException
- _objc_exception_throw
CStrings:
+ "%s Failed to start audio stream in CSAttSiriSignalProvider, error : %{public}@"
+ "%s On-Device ASR: BGST: Done triggering daily speech profile maintenance."
+ "%s On-Device ASR: BGST: Done triggering daily subscription cleanup."
+ "%s On-Device ASR: BGST: Done triggering post-install speech profile migration."
+ "%s On-Device ASR: BGST: Done triggering post-install subscription."
+ "%s On-Device ASR: BGST: Triggering daily speech profile maintenance."
+ "%s On-Device ASR: BGST: Triggering post-install speech profile migration."
+ "-[CSHybridEndpointAnalyzer updateEndpointerThreshold:]"
+ "-[CSRemoraEndpointAnalyzer updateEndpointerThreshold:]_block_invoke"
+ "@\"CESRSpeechProfileDispatcher\""
+ "T@\"CESRSpeechProfileDispatcher\",&,N,V_cesrSpeechProfileDispatcher"
+ "_book"
+ "_cesrSpeechProfileDispatcher"
+ "_registerAndSubmitAllBGSystemTasks"
+ "_runDailySpeechProfileMaintenance"
+ "_runPostInstallANECompilation"
+ "_runPostInstallAssetSubscription"
+ "_runPostInstallSpeechProfileMigration"
+ "cesrSpeechProfileDispatcher"
+ "com.apple.siri.bg_system_task.daily-asset-subscription-cleanup"
+ "com.apple.siri.bg_system_task.post-install-asset-subscription"
+ "com.apple.siri.bg_system_task.post-install-speech-ane-compilation"
+ "handlePostInstallSubscriptions"
+ "setCesrSpeechProfileDispatcher:"
+ "snapshotBookmarksForLocale:toPath:"
+ "updateEndpointerThreshold:"
+ "v28@?0B8@\"NSString\"12@\"NSError\"20"
- "%s A supported notification was NOT handled: %@"
- "%s Connecting process with pid=(%d) is not entitled for the speech profile admin service - rejecting connection."
- "%s Evaluation is enabled, ignoring notification: %@"
- "%s Handling notification: %@"
- "%s Ignoring Cascade change notification because evaluation is enabled."
- "%s New connection established to process with pid=(%d)"
- "%s On-Device ASR: BGST: Done triggering daily subscription cleanup"
- "%s On-Device ASR: BGST: Done triggering post-upgrade subscriptions"
- "%s Performing daily speech profile maintenance."
- "%s Performing maintenance due to notification: %@"
- "%s Performing post-upgrade speech profile migration."
- "%s Received Cascade change notification for sets: %@"
- "%s Start failed, removing all observers"
- "%s Starting up..."
- "%s Unrecognized listener passed to delegate: %@"
- "+[CSPDispatcher sharedDispatcher]_block_invoke"
- "-[CSAttSiriSignalProvider _startAudioStreamingWithSignalOptions:completion:]"
- "-[CSAttSiriSignalProvider _startAudioStreamingWithSignalOptions:completion:]_block_invoke"
- "-[CSPDispatcher _adminServiceShouldAcceptNewConnection:]"
- "-[CSPDispatcher _notifyChangeToSets:]"
- "-[CSPDispatcher handleDarwinNotificationEventWithName:]"
- "-[CSPDispatcher handleDarwinNotificationEventWithName:]_block_invoke"
- "-[CSPDispatcher listener:shouldAcceptNewConnection:]"
- "-[CSPDispatcher runMaintenanceWithShouldDefer:completion:]_block_invoke"
- "-[CSPDispatcher runMigration:]_block_invoke"
- "-[CSPDispatcher setupXPCListeners]_block_invoke"
- "@\"CCSetChangeXPCListener\""
- "@\"CESRSpeechProfileSiteManager\""
- "@\"CESRTaskCoalescer\""
- "@\"CSPDispatcher\""
- "@\"NSObject<CESRSpeechProfileAdminServiceProvider>\""
- "CESRSpeechProfileAdminService"
- "CESRSpeechProfileResourceMonitorDelegate"
- "CSPDispatcher"
- "CSPDispatcher Set Change Queue"
- "CSPRegisterAndSubmitPostInstallMigrationTask_block_invoke"
- "T@\"CESRTaskCoalescer\",R,N,V_taskCoalescer"
- "T@\"CSPDispatcher\",&,N,V_cspDispatcher"
- "T@\"NSXPCListener\",R,N,V_adminServiceListener"
- "Vv28@0:8B16@?20"
- "Vv28@0:8B16@?<v@?q>20"
- "Vv32@0:8@\"CCSerializedSetEnumerator\"16@?<v@?q>24"
- "Vv32@0:8@\"NSString\"16@?<v@?q>24"
- "_adminServiceListener"
- "_adminServiceProvider"
- "_adminServiceShouldAcceptNewConnection:"
- "_cspDispatcher"
- "_defaultTaskCoalescerWithQueue:"
- "_initWithQueue:"
- "_initWithQueue:adminServiceProvider:speechProfileSiteManager:"
- "_listenerWithMachServiceName:delegate:"
- "_notifyChangeToSets:"
- "_runPostUpgradeANECompilation"
- "_runPostUpgradeSubscriptions"
- "_setChangeListener"
- "_speechProfileSiteManager"
- "_supportedDarwinNotifications"
- "_supportedNotifications"
- "_taskCoalescer"
- "_wait"
- "adminService"
- "adminServiceListener"
- "beginEvaluationWithSetEnumerator:completion:"
- "com.apple.corespeech.corespeechd.speechprofileadmin"
- "com.apple.corespeech.corespeechd.speechprofileadmin.service"
- "com.apple.corespeechd.speechprofileassetstartup"
- "com.apple.corespeechd.speechprofileassetupdate"
- "com.apple.corespeechd.speechprofilefirstunlock"
- "com.apple.corespeechd.speechprofilemaintenance"
- "com.apple.corespeechd.speechprofilemigration"
- "com.apple.corespeechd.speechprofilesetchange"
- "com.apple.corespeechd.speechprofilesettingschange"
- "com.apple.corespeechd.speechprofilesysdiagnosestarted"
- "com.apple.siri.bg_system_task.daily-subscription-cleanup"
- "com.apple.siri.bg_system_task.post-upgrade-speech-ane-compilation"
- "com.apple.siri.bg_system_task.post-upgrade-subscriptions"
- "com.apple.sysdiagnose.sysdiagnoseStarted"
- "cspDispatcher"
- "deleteInactiveSites"
- "deleteLegacyProfiles"
- "endEvaluation:"
- "exceptionWithName:reason:userInfo:"
- "handlePostUpgradeSubscriptions"
- "handleSiteAvailableForPersona:"
- "handleSiteUnavailableForPersona:"
- "handleSiteUnavailableSoonForPersona:"
- "handleSysdiagnoseStarted"
- "handleUpdatedSets:"
- "init unsupported"
- "initWithIdentifier:batchHandlerBlock:queue:useCase:"
- "initWithManagerName:coalescenceInterval:coalescenceDelay:executionQueue:"
- "initWithQueue:speechProfileSiteManager:"
- "isEvaluationEnabled"
- "performMaintenance:"
- "rebuildSpeechProfileForUserId:completion:"
- "registerBackgroundSystemTasks"
- "resourceAvailableForPersona:"
- "resourceUnavailableForPersona:"
- "resourceUnavailableSoonForPersona:"
- "setCspDispatcher:"
- "setWithSet:"
- "sharedStatus"
- "submitTaskWithId:taskBlock:completion:"
- "taskCoalescer"
- "triggerMaintenance:completion:"
- "updateRequiredLocales"
- "v16@?0@\"NSSet\"8"
- "valueForEntitlement:"

```
