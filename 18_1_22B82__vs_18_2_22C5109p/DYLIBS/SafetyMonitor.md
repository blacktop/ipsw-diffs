## SafetyMonitor

> `/System/Library/PrivateFrameworks/SafetyMonitor.framework/SafetyMonitor`

```diff

-976.0.1.0.0
-  __TEXT.__text: 0x73f38
-  __TEXT.__auth_stubs: 0x12f0
-  __TEXT.__objc_methlist: 0x41fc
+977.0.4.0.0
+  __TEXT.__text: 0x74df4
+  __TEXT.__auth_stubs: 0x1300
+  __TEXT.__objc_methlist: 0x42f4
   __TEXT.__const: 0x1268
-  __TEXT.__cstring: 0xb9ad
+  __TEXT.__cstring: 0xba3b
   __TEXT.__swift5_typeref: 0x50e
-  __TEXT.__oslogstring: 0x4320
+  __TEXT.__oslogstring: 0x438d
   __TEXT.__constg_swiftt: 0x45c
   __TEXT.__swift5_reflstr: 0x2be
   __TEXT.__swift5_fieldmd: 0x3f8

   __TEXT.__ustring: 0xd34
   __TEXT.__gcc_except_tab: 0xf64
   __TEXT.__dlopen_cstrs: 0x60
-  __TEXT.__unwind_info: 0x17f0
+  __TEXT.__unwind_info: 0x1840
   __TEXT.__eh_frame: 0x95c
-  __TEXT.__objc_classname: 0x9b5
-  __TEXT.__objc_methname: 0xbeab
-  __TEXT.__objc_methtype: 0x2173
-  __TEXT.__objc_stubs: 0x55e0
-  __DATA_CONST.__got: 0x4b8
-  __DATA_CONST.__const: 0x13f8
-  __DATA_CONST.__objc_classlist: 0x268
+  __TEXT.__objc_classname: 0x9f1
+  __TEXT.__objc_methname: 0xc332
+  __TEXT.__objc_methtype: 0x219e
+  __TEXT.__objc_stubs: 0x5820
+  __DATA_CONST.__got: 0x4c0
+  __DATA_CONST.__const: 0x1448
+  __DATA_CONST.__objc_classlist: 0x270
   __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x118
+  __DATA_CONST.__objc_protolist: 0x120
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1f38
+  __DATA_CONST.__objc_selrefs: 0x1fe0
   __DATA_CONST.__objc_protorefs: 0x38
-  __DATA_CONST.__objc_superrefs: 0x1a8
-  __AUTH_CONST.__auth_got: 0x988
+  __DATA_CONST.__objc_superrefs: 0x1b0
+  __AUTH_CONST.__auth_got: 0x990
   __AUTH_CONST.__auth_ptr: 0x300
   __AUTH_CONST.__const: 0xb68
-  __AUTH_CONST.__cfstring: 0x4e00
-  __AUTH_CONST.__objc_const: 0x9198
+  __AUTH_CONST.__cfstring: 0x4e40
+  __AUTH_CONST.__objc_const: 0x9620
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH.__objc_data: 0x1270
+  __AUTH.__objc_data: 0x12c0
   __AUTH.__data: 0x2d8
-  __DATA.__objc_ivar: 0x38c
-  __DATA.__data: 0x1300
+  __DATA.__objc_ivar: 0x394
+  __DATA.__data: 0x1360
   __DATA.__bss: 0x1600
   __DATA.__common: 0x110
-  __DATA_DIRTY.__objc_ivar: 0x1d8
+  __DATA_DIRTY.__objc_ivar: 0x1d4
   __DATA_DIRTY.__objc_data: 0x928
   __DATA_DIRTY.__data: 0xe8
   __DATA_DIRTY.__common: 0x18

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 2194
-  Symbols:   2203
-  CStrings:  3305
+  Functions: 2220
+  Symbols:   2237
+  CStrings:  3363
 
Symbols:
+ _OBJC_CLASS_$_NSHashTable
+ _OBJC_CLASS_$_SMAppDeletionManager
+ _OBJC_METACLASS_$_SMAppDeletionManager
+ _SMTerminationResultErrorCode
+ _SMTerminationResultErrorDomain
+ _SMTerminationResultReason
+ _SMTerminationResultSuccess
+ _objc_opt_respondsToSelector
CStrings:
+ "\x1f\x02\xc2"
+ "%!@(MISSING), %!s(MISSING), adding observer, %!@(MISSING)"
+ "%!@(MISSING), %!s(MISSING), querying isMessagesAppInstalled:, %!{(MISSING)bool}d"
+ "%!@(MISSING), %!s(MISSING), removing observer, %!@(MISSING)"
+ "-[SMAppDeletionManager _addObserver:]"
+ "-[SMAppDeletionManager _removeObserver:]"
+ "-[SMAppDeletionManager isMessagesAppInstalled]"
+ "@\"NSHashTable\""
+ "@320@0:8@16@24B32@36@44@52@60@68@76@84@92@100@108@116@124@132@140@148@156d164q172d180q188d196q204q212q220q228q236B244B248@252@260B268@272@280q288q296@304@312"
+ "FailureMessagesNotInstalled"
+ "LSApplicationWorkspaceObserverProtocol"
+ "SMAppDeletionManager"
+ "T@\"NSHashTable\",&,N,V_observers"
+ "T@\"NSObject<OS_dispatch_queue>\",R,N,V_queue"
+ "_addObserver:"
+ "_applicationsDidInstall:"
+ "_applicationsDidUninstall:"
+ "_databaseWasRebuilt"
+ "_notifyObserversForMessagesAppInstalled"
+ "_notifyObserversForMessagesAppUninstalled"
+ "_notifyObserversWithUpdatedMessagesInstallation"
+ "_observers"
+ "_removeObserver:"
+ "_setup"
+ "addObserver:"
+ "applicationIconDidChange:"
+ "applicationInstallsArePrioritized:arePaused:"
+ "applicationInstallsDidCancel:"
+ "applicationInstallsDidChange:"
+ "applicationInstallsDidPause:"
+ "applicationInstallsDidPrioritize:"
+ "applicationInstallsDidResume:"
+ "applicationInstallsDidStart:"
+ "applicationInstallsDidUpdateIcon:"
+ "applicationIsInstalled:"
+ "applicationStateDidChange:"
+ "applicationsDidChangePersonas:"
+ "applicationsDidFailToInstall:"
+ "applicationsDidFailToUninstall:"
+ "applicationsDidInstall:"
+ "applicationsDidUninstall:"
+ "applicationsWillInstall:"
+ "applicationsWillUninstall:"
+ "databaseWasRebuilt"
+ "deviceManagementPolicyDidChange:"
+ "helperPlaceholdersInstalled:"
+ "helperPlaceholdersUninstalled:"
+ "initWithIdentifier:shouldBeCleanedUpDate:cloudkitShareZoneCleanedUpSuccessfully:syncDate:keyReleaseMessageSendDate:scheduledSendExpiryDate:phoneCache:watchCache:sessionID:safetyCacheKey:allowReadToken:scheduleSendMessageGUID:unlockLocation:lockLocation:startingLocation:offWristLocation:parkedCarLocation:destinationMapItem:timeCacheUploadCompletion:maxCacheSize:maxLocationsInTrace:maxTimeBetweenCacheUpdates:numCacheUpdates:timeTilCacheRelease:numberOfSuccessfulCacheUpdates:numberOfMessageCancelling:numberOfSuccessfulMessageCancelling:numberOfMessageScheduling:numberOfSuccessfulMessageScheduling:wasCacheReleased:wasScheduledSendTriggered:locationOfTrigger:triggerDate:lockState:cacheUpdateBackstopExpiryDate:workoutEvents:numberOfHandoffBecomingActive:numberOfHandoffBecomingNonActive:earliestActiveDeviceIdentifier:latestActiveDeviceIdentifier:"
+ "isMessagesAppInstalled"
+ "networkUsageChanged:"
+ "observeLaunchProhibitedApps"
+ "observers"
+ "onMessagesAppInstalled"
+ "onMessagesAppUninstalled"
+ "pluginsDidInstall:"
+ "pluginsDidUninstall:"
+ "pluginsWillUninstall:"
+ "reason"
+ "removeObject:"
+ "removeObserver:"
+ "sessionID,%!@(MISSING),identifier,%!@(MISSING),syncDate,%!@(MISSING),keyReleaseMessageDate,%!@(MISSING),shouldBeCleanedUpDate,%!@(MISSING),allowReadToken,%!@(MISSING),safetyCacheKey,%!@(MISSING),cloudKitCleanedUp,%!d(MISSING),scheduledSendDate,%!@(MISSING),scheduledSendGUID,%!@(MISSING),startLocation,%!@(MISSING),unlockLocation,%!@(MISSING),lockLocation,%!@(MISSING),parkedCarLocation,%!@(MISSING),offWristLocation,%!@(MISSING),workoutEventsCount,%!l(MISSING)u,numberOfHandoffBecomingActive,%!l(MISSING)d,numberOfHandoffBecomingNonActive,%!l(MISSING)d,earliestActiveDeviceIdentifier,%!@(MISSING),latestActiveDeviceIdentifier,%!@(MISSING)"
+ "setObservers:"
+ "setup"
+ "v32@0:8@\"NSArray\"16@\"NSArray\"24"
- "\x1f\x03\xc2"
- "@328@0:8@16@24@32B40@44@52@60@68@76@84@92@100@108@116@124@132@140@148@156@164d172q180d188q196d204q212q220q228q236q244B252B256@260@268B276@280@288q296q304@312@320"
- "T@\"SMConversation\",&,N,V_conversation"
- "initWithIdentifier:conversation:shouldBeCleanedUpDate:cloudkitShareZoneCleanedUpSuccessfully:syncDate:keyReleaseMessageSendDate:scheduledSendExpiryDate:phoneCache:watchCache:sessionID:safetyCacheKey:allowReadToken:scheduleSendMessageGUID:unlockLocation:lockLocation:startingLocation:offWristLocation:parkedCarLocation:destinationMapItem:timeCacheUploadCompletion:maxCacheSize:maxLocationsInTrace:maxTimeBetweenCacheUpdates:numCacheUpdates:timeTilCacheRelease:numberOfSuccessfulCacheUpdates:numberOfMessageCancelling:numberOfSuccessfulMessageCancelling:numberOfMessageScheduling:numberOfSuccessfulMessageScheduling:wasCacheReleased:wasScheduledSendTriggered:locationOfTrigger:triggerDate:lockState:cacheUpdateBackstopExpiryDate:workoutEvents:numberOfHandoffBecomingActive:numberOfHandoffBecomingNonActive:earliestActiveDeviceIdentifier:latestActiveDeviceIdentifier:"
- "sessionID,%!@(MISSING),identifier,%!@(MISSING),receiverHandles,%!@(MISSING),syncDate,%!@(MISSING),keyReleaseMessageDate,%!@(MISSING),shouldBeCleanedUpDate,%!@(MISSING),allowReadToken,%!@(MISSING),safetyCacheKey,%!@(MISSING),cloudKitCleanedUp,%!d(MISSING),scheduledSendDate,%!@(MISSING),scheduledSendGUID,%!@(MISSING),startLocation,%!@(MISSING),unlockLocation,%!@(MISSING),lockLocation,%!@(MISSING),parkedCarLocation,%!@(MISSING),offWristLocation,%!@(MISSING),workoutEventsCount,%!l(MISSING)u,numberOfHandoffBecomingActive,%!l(MISSING)d,numberOfHandoffBecomingNonActive,%!l(MISSING)d,earliestActiveDeviceIdentifier,%!@(MISSING),latestActiveDeviceIdentifier,%!@(MISSING)"
- "setConversation:"

```
