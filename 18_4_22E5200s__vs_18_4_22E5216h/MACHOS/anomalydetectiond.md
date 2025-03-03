## anomalydetectiond

> `/usr/libexec/anomalydetectiond`

```diff

-125.0.9.0.0
-  __TEXT.__text: 0x3294d4
-  __TEXT.__auth_stubs: 0x16e0
-  __TEXT.__objc_stubs: 0x8f40
-  __TEXT.__objc_methlist: 0x8c38
-  __TEXT.__const: 0x8d65
-  __TEXT.__gcc_except_tab: 0x108f8
-  __TEXT.__cstring: 0x1929c
-  __TEXT.__oslogstring: 0xf69f
-  __TEXT.__objc_classname: 0x10d1
-  __TEXT.__objc_methtype: 0x63a5
-  __TEXT.__objc_methname: 0xbc4f
+125.0.13.0.0
+  __TEXT.__text: 0x32a12c
+  __TEXT.__auth_stubs: 0x1660
+  __TEXT.__objc_stubs: 0x9120
+  __TEXT.__objc_methlist: 0x8c00
+  __TEXT.__gcc_except_tab: 0x10b28
+  __TEXT.__const: 0x8d86
+  __TEXT.__cstring: 0x19684
+  __TEXT.__oslogstring: 0xfb3d
+  __TEXT.__objc_classname: 0x10bf
+  __TEXT.__objc_methtype: 0x6394
+  __TEXT.__objc_methname: 0xbde1
   __TEXT.__ustring: 0x10ae
-  __TEXT.__unwind_info: 0xb788
+  __TEXT.__unwind_info: 0xb6d8
   __TEXT.__eh_frame: 0x590
-  __DATA_CONST.__auth_got: 0xb88
-  __DATA_CONST.__got: 0x588
+  __DATA_CONST.__auth_got: 0xb48
+  __DATA_CONST.__got: 0x590
   __DATA_CONST.__auth_ptr: 0x38
-  __DATA_CONST.__const: 0x22300
-  __DATA_CONST.__cfstring: 0x5e20
-  __DATA_CONST.__objc_classlist: 0x4c8
+  __DATA_CONST.__const: 0x222d0
+  __DATA_CONST.__cfstring: 0x5f80
+  __DATA_CONST.__objc_classlist: 0x4c0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x130
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0x448
+  __DATA_CONST.__objc_superrefs: 0x440
   __DATA_CONST.__objc_intobj: 0x1818
   __DATA_CONST.__objc_arraydata: 0x240
   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_dictobj: 0x320
-  __DATA.__objc_const: 0x10520
-  __DATA.__objc_selrefs: 0x2f30
-  __DATA.__objc_ivar: 0x958
-  __DATA.__objc_data: 0x2fd0
+  __DATA.__objc_const: 0x10478
+  __DATA.__objc_selrefs: 0x2f68
+  __DATA.__objc_ivar: 0x954
+  __DATA.__objc_data: 0x2f80
   __DATA.__data: 0x2060
   __DATA.__bss: 0x230
   __DATA.__common: 0x8

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 15253
-  Symbols:   568
-  CStrings:  8660
+  Functions: 15237
+  Symbols:   561
+  CStrings:  8699
 
Symbols:
+ _OBJC_CLASS_$_UNNotificationIcon
- __ZN18CLConnectionClient11sendMessageENSt3__110shared_ptrI19CLConnectionMessageEEU13block_pointerFvS3_E
- __ZN18CLConnectionClient11sendMessageENSt3__110shared_ptrI19CLConnectionMessageEEb
- __ZN18CLConnectionClient22setInterruptionHandlerEU13block_pointerFvvE
- __ZN18CLConnectionClient24setDefaultMessageHandlerEU13block_pointerFvNSt3__110shared_ptrI19CLConnectionMessageEEE
- __ZN18CLConnectionClient5startEv
- __ZN18CLConnectionClientC1ENSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEPU28objcproto17OS_dispatch_queue8NSObject
- __ZN19CLConnectionMessageC1ERKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE
- __ZNK19CLConnectionMessage22getDictionaryOfClassesEP5NSSet
CStrings:
+ "\x194"
+ ".fba_holding.cleanup"
+ "@32@0:8q16@24"
+ "@36@0:8Q16S24C28B32"
+ "B60@0:8B16@20@28d36@44^@52"
+ "CSKappaConnectionBringupFeedbackAssistantMessage"
+ "CSKappaFeedbackAssistantConsentKey"
+ "CSKappaFeedbackAssistantUUIDKey"
+ "Crash Detection Feedback"
+ "FeedbackAssistantExpireDurationSeconds"
+ "If you are comfortable sharing, please tell us more about your incident. We'll use what you file to refine our iOS/watchOS Safety algorithms."
+ "If you are comfortable sharing, please tell us more about your incident. We'll use what you file to refine our iOS/watchOS Safety algorithms. \n\nNote: Two files containing sensor data have been automatically attached to the radar. You can go to the Attachments and delete each file, as well as the original sysdiagnose, if you do not wish for the information to be sent to the team."
+ "IgneousDetectionServiceUploaderOverrideRetentionPeriod"
+ "ImproveSafety:%d"
+ "Initialized Igneous uploader: registered %d, monitoring %d, harvestTimeWindowSec %.0f, readManifestTimeoutSec %.0f, retentionPeriod %llu"
+ "Kappa SessionInfo: %@"
+ "Kappa UserInfo:%@, ImproveSafety:%d"
+ "Kappa sessionInfo addition: coarseLat,%{sensitive}f"
+ "Kappa sessionInfo addition: coarseLong,%{sensitive}f"
+ "Kappa sessionInfo addition: signalEnvironment,%d"
+ "Kappa sessionInfo addition: sunElevation,%f"
+ "Marty Session info coarseLat,%{sensitive}f,coarseLong,%{sensitive}f,companionEscalationDecisionCycle,%d,companionEscalationDecisionMotorbike,%d,didCompanionTriggerCycle,%d,didCompanionTriggerMotorbike,%d,didPlaceCallCycle,%d,didPlaceCallMotorbike,%d,didRaiseUICycle,%d,didRaiseUICycle_companion,%d,didRaiseUIMotorbike,%d,didRaiseUIMotorbike_companion,%d,escalationDecisionCycle,%d,escalationDecisionMotorbike,%d,isCompanionConnected,%d,isSOSAutoInitiatedCycle,%d,isSOSAutoInitiatedMotorbike,%d,isSOSUserInitiatedCycle,%d,isSOSUserInitiatedMotorbike,%d,locallyArmedBitmap,%d,numAlphaDetectedCycle,%d,numAlphaDetectedMotorbike,%d,numEarlyCrashesDetectedCycle,%d,numEarlyCrashesDetectedMotorbike,%d,numTriggersCycle,%d,numTriggersMotorbike,%d,overrideModeBitmap,%d,signalEnvironment,%d"
+ "Marty UserInfo:%@, ImproveSafety:%d"
+ "Please tell us more about what you were doing around %@. \n\nFor example, were you recently in a car or some other moving platform? Were you actively moving or doing some other activity? \n\nWe'll use what you file to refine our iOS/watchOS Safety algorithms."
+ "Please tell us more about what you were doing around %@. \n\nFor example, were you recently in a car or some other moving platform? Were you actively moving or doing some other activity? \n\nWe'll use what you file to refine our iOS/watchOS Safety algorithms. \n\nNote: Two files containing sensor data have been automatically attached to the radar. You can go to the Attachments and delete each file, as well as the original sysdiagnose, if you do not wish for the information to be sent to the team."
+ "T@\"CSFolderMonitor\",&,V_feedbackHoldingMonitor"
+ "T^{?=QSCB},R,N"
+ "While enqueuing for feedback assistant holding, file doesnt exist: %@"
+ "Your iPhone detected a possible crash earlier. If you're willing to answer a few questions about the event, your answers can improve crash detection."
+ "[fba] Couldn't remove metadata file at %@, error,%@"
+ "[fba] Couldn't remove msl file at %@, error,%@"
+ "[fba] Couldn't retrieve localized push notification strings"
+ "[fba] Created Feedback Assistant notification request:%@"
+ "[fba] Enqueuing held recording: %@"
+ "[fba] Error creating directory: %@"
+ "[fba] Error deleting file: %@"
+ "[fba] Error holding MSL/metadata: %@"
+ "[fba] Error moving held file to spooler directory, %@"
+ "[fba] Error reading contents of: %@ error,%@"
+ "[fba] Error unarchiving metadata for: %@ error,%@"
+ "[fba] Failed to add Feedback Assistant notification request,error,%@"
+ "[fba] Feedback Assistant consent keys not found: %@"
+ "[fba] Files to remove: %@, %@"
+ "[fba] Holding recording: %@"
+ "[fba] Not showing Feedback Assistant survey, IS,%d,internal,%d,seed,%d,showSurveyOverride,%d,disableOverride,%d"
+ "[fba] Received Feedback Assistant Consent Response: consented,%d uuid,%@"
+ "[fba] Received Feedback Assistant bringup: uuid,%@"
+ "[fba] Removing held recording for: %@"
+ "[fba] SOS not in progress, attempt to enqueue UUID, if it was held"
+ "[fba] Scheduling notification delay of: %f seconds"
+ "[fba] Showing Feedback Assistant survey: IS,%d,internal,%d,seed,%d,showSurveyOverride,%d,disableOverride,%d"
+ "[fba] Successfully added Feedback Assistant notification request for %@"
+ "[fba] UUID in message is malformed"
+ "[fba] Unsupported session type for metadata saving, %d"
+ "[fba] cannot hold a nil recording"
+ "[fba] evaluating: %@"
+ "[fba] file age: %f > %f expired,%d"
+ "[fba] moving held file from: %@ to %@"
+ "^{?=QSCB}16@0:8"
+ "_feedbackHoldingMonitor"
+ "com.apple.anomalydetectiond.kappa.feedbackConsentResponse"
+ "com.apple.appleseed.FeedbackAssistant"
+ "createDirectoryAtURL:withIntermediateDirectories:attributes:error:"
+ "dataWithContentsOfURL:options:error:"
+ "dateByAddingUnit:value:toDate:options:"
+ "dateFromComponents:"
+ "dateWithHour:fromDate:"
+ "enqueueHeldRecordingForUpload:"
+ "feedbackAssistantHolding"
+ "feedbackHoldingMonitor"
+ "getFileUrlsForRecording:metadataUrl:mslUrl:withError:"
+ "hapticsOn"
+ "holdRecordingUntilFeedbackConsent:withError:"
+ "iconForApplicationIdentifier:"
+ "initFileURLWithPath:"
+ "initWithTimestamp:dramDurationMs:vehicularFlags:hapticsOn:"
+ "isFeedbackAssistantEligible"
+ "msl.protodata"
+ "persistToDiskWithSpooledFile:spoolerDir:fileURL:enqueueTime:metadata:error:"
+ "removeHeldRecording:"
+ "setFeedbackHoldingMonitor:"
+ "setHour:"
+ "setIcon:"
+ "setMinute:"
+ "setSecond:"
+ "timeIntervalToNearestEightOClock:"
+ "v32@0:8@16^@24"
+ "v48@0:8@16^@24^@32^@40"
+ "{?=\"timestamp\"Q\"dramDurationMs\"S\"vehicularFlags\"C\"hapticsOn\"B}"
- "\x184"
- "@32@0:8Q16S24C28"
- "B52@0:8B16@20d28@36^@44"
- "CSKappaConnection"
- "CSKappaConnectionQueue"
- "Connection Interrupted"
- "Couldn't retrieve localized push notification strings"
- "Created Feedback Assistant notification request:%@"
- "Failed to add Feedback Assistant notification request,error,%@"
- "Initialized Igneous uploader: registered %d, monitoring %d, harvestTimeWindowSec %.0f, readManifestTimeoutSec %.0f"
- "Not showing Feedback Assistant survey, IS,%d,internal,%d,seed,%d,showSurveyOverride,%d,disableOverride,%d"
- "On %@, your device detected a potential crash event. Hope you are safe. If you are able and willing, we'd appreciate your response to a few questions to help improve our safety features."
- "Please tell us more about what you were doing around %@ ... \n\nNote: Two files containing sensor data have been automatically attached to the radar. You can go to the Attachments and delete each file, as well as the original sysdiagnose, if you do not wish for the information to be sent to the team."
- "Please tell us more about your incident (optional)\n\nNote: Two files containing sensor data have been automatically attached to the radar. You can go to the Attachments and delete each file, as well as the original sysdiagnose, if you do not wish for the information to be sent to the team."
- "Please tell us more about your incident around %@."
- "Potential vehicle crash detected"
- "SessionInfo:%@"
- "SessionInfo:%@, ImproveSafety:%d"
- "Showing Feedback Assistant survey: IS,%d,internal,%d,seed,%d,showSurveyOverride,%d,disableOverride,%d"
- "Successfully added Feedback Assistant notification request"
- "T^{?=QSC},R,N"
- "UserInfo:%@, ImproveSafety:%d"
- "^{?=QSC}16@0:8"
- "_internalQueue"
- "defaultMessageHandler:"
- "initWithTimestamp:dramDurationMs:vehicularFlags:"
- "interruptionHandler"
- "persistToDiskWithSpooledFile:fileURL:enqueueTime:metadata:theError:"
- "response is nil"
- "sendCommand:"
- "sendCommand:withValue:"
- "sendTestCachedMessage:"
- "sendTestMessage:"
- "sendTestPowerAssertion:"
- "sendTestSMSignal:"
- "sendTestSOS"
- "sendTestTTR"
- "setDateStyle:"
- "setTimeStyle:"
- "testSMSignal"
- "v32@0:8{shared_ptr<CLConnectionMessage>=^{CLConnectionMessage}^{__shared_weak_count}}16"
- "{\"msg%{public}.0s\":\"defaultMessageHandler\", \"name\":%{public, location:escape_only}s, \"value\":%{public, location:escape_only}@}"
- "{\"msg%{public}.0s\":\"sendCommand\", \"name\":%{public, location:escape_only}s, \"value\":%{public, location:escape_only}@}"
- "{\"msg%{public}.0s\":\"sendTestMessage\", \"name\":%{public, location:escape_only}s, \"value\":%{public, location:escape_only}@}"
- "{\"msg%{public}.0s\":\"sendTestSMSignal\", \"name\":%{public, location:escape_only}s, \"value\":%{public, location:escape_only}@}"
- "{\"msg%{public}.0s\":\"sendTestSOS\", \"name\":%{public, location:escape_only}s, \"value\":%{public, location:escape_only}@}"
- "{\"msg%{public}.0s\":\"sendTestTTR\", \"name\":%{public, location:escape_only}s, \"value\":%{public, location:escape_only}@}"
- "{\"msg%{public}.0s\":\"sendTestTrigger\", \"name\":%{public, location:escape_only}s, \"value\":%{public, location:escape_only}@}"
- "{?=\"timestamp\"Q\"dramDurationMs\"S\"vehicularFlags\"C}"

```
