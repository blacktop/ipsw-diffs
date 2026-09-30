## anomalydetectiond

> `/usr/libexec/anomalydetectiond`

```diff

-121.0.1.0.0
-  __TEXT.__text: 0x32233c
-  __TEXT.__auth_stubs: 0x16d0
-  __TEXT.__objc_stubs: 0x8b60
-  __TEXT.__objc_methlist: 0x7e24
-  __TEXT.__const: 0x8c1d
-  __TEXT.__gcc_except_tab: 0xfe90
-  __TEXT.__cstring: 0x19052
-  __TEXT.__oslogstring: 0xf0df
-  __TEXT.__objc_classname: 0x1068
-  __TEXT.__objc_methtype: 0x6102
-  __TEXT.__objc_methname: 0xb4f9
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
-  __TEXT.__unwind_info: 0xb8d8
+  __TEXT.__unwind_info: 0xb6d8
   __TEXT.__eh_frame: 0x590
-  __DATA_CONST.__auth_got: 0xb80
-  __DATA_CONST.__got: 0x570
-  __DATA_CONST.__auth_ptr: 0x30
-  __DATA_CONST.__const: 0x221e8
-  __DATA_CONST.__cfstring: 0x5d20
-  __DATA_CONST.__objc_classlist: 0x4b0
+  __DATA_CONST.__auth_got: 0xb48
+  __DATA_CONST.__got: 0x590
+  __DATA_CONST.__auth_ptr: 0x38
+  __DATA_CONST.__const: 0x222d0
+  __DATA_CONST.__cfstring: 0x5f80
+  __DATA_CONST.__objc_classlist: 0x4c0
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x128
+  __DATA_CONST.__objc_protolist: 0x130
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0x430
-  __DATA_CONST.__objc_intobj: 0x1800
-  __DATA_CONST.__objc_arraydata: 0x1f0
-  __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA_CONST.__objc_dictobj: 0x280
-  __DATA.__objc_const: 0x11338
-  __DATA.__objc_selrefs: 0x2ae8
-  __DATA.__objc_ivar: 0x920
-  __DATA.__objc_data: 0x2ee0
-  __DATA.__data: 0x1ff0
-  __DATA.__bss: 0x238
+  __DATA_CONST.__objc_superrefs: 0x440
+  __DATA_CONST.__objc_intobj: 0x1818
+  __DATA_CONST.__objc_arraydata: 0x240
+  __DATA_CONST.__objc_arrayobj: 0x30
+  __DATA_CONST.__objc_dictobj: 0x320
+  __DATA.__objc_const: 0x10478
+  __DATA.__objc_selrefs: 0x2f68
+  __DATA.__objc_ivar: 0x954
+  __DATA.__objc_data: 0x2f80
+  __DATA.__data: 0x2060
+  __DATA.__bss: 0x230
   __DATA.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 15160
-  Symbols:   564
-  CStrings:  8506
+  Functions: 15237
+  Symbols:   561
+  CStrings:  8699
 
Symbols:
+ _OBJC_CLASS_$_GEONavigationListener
+ _OBJC_CLASS_$_UNNotificationIcon
+ __ZNSt3__117bad_function_callD1Ev
+ __ZTINSt3__117bad_function_callE
+ __ZTVNSt3__117bad_function_callE
+ _container_system_group_path_for_identifier
- __ZN18CLConnectionClient11sendMessageENSt3__110shared_ptrI19CLConnectionMessageEEU13block_pointerFvS3_E
- __ZN18CLConnectionClient11sendMessageENSt3__110shared_ptrI19CLConnectionMessageEEb
- __ZN18CLConnectionClient22setInterruptionHandlerEU13block_pointerFvvE
- __ZN18CLConnectionClient24setDefaultMessageHandlerEU13block_pointerFvNSt3__110shared_ptrI19CLConnectionMessageEEE
- __ZN18CLConnectionClient5startEv
- __ZN18CLConnectionClientC1ENSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEPU28objcproto17OS_dispatch_queue8NSObject
- __ZN19CLConnectionMessageC1ERKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE
- __ZNK19CLConnectionMessage22getDictionaryOfClassesEP5NSSet
- __ZNKSt9exception4whatEv
CStrings:
+ "\x17\x12\x115\x12"
+ "\x194"
+ ".fba_holding.cleanup"
+ "@\"CSGeoServicesListener\""
+ "@\"GEONavigationListener\""
+ "@32@0:8q16@24"
+ "@36@0:8Q16S24C28B32"
+ "@56@0:8@16@24Q32d40@48"
+ "B60@0:8B16@20@28d36@44^@52"
+ "C24@0:8@16"
+ "CSGeoServicesListener"
+ "CSIgneousAnomalyEvent"
+ "CSIgneousHarvestTimeWindowSec"
+ "CSIgneousReadManifestTimeoutSec"
+ "CSKappaConnectionBringupFeedbackAssistantMessage"
+ "CSKappaFeedbackAssistantConsentKey"
+ "CSKappaFeedbackAssistantUUIDKey"
+ "CSStudiesServerUploaderIgneous"
+ "Crash Detection Feedback"
+ "Entered LOI"
+ "Exited LOI"
+ "Failed to append data from file %@"
+ "Failed to finalize encrypting file %@"
+ "Failed to register with server to upload %@"
+ "Failed to remove file %@"
+ "Failed to start output file %@"
+ "FeedbackAssistantExpireDurationSeconds"
+ "File %@ doesn't contain value for key 'spooled'"
+ "File %@ has been encrypted as %@"
+ "File %@ is newer than all events in the manifest. Try again later"
+ "File %@ will be encrypted"
+ "File to be encrypted %@ doesn't exist"
+ "Finished reading %d events from manifest file %@"
+ "GEONavigationListenerDelegate"
+ "Group container not available"
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
+ "Manifest event count %d"
+ "Manifest is empty"
+ "Marty Session info coarseLat,%{sensitive}f,coarseLong,%{sensitive}f,companionEscalationDecisionCycle,%d,companionEscalationDecisionMotorbike,%d,didCompanionTriggerCycle,%d,didCompanionTriggerMotorbike,%d,didPlaceCallCycle,%d,didPlaceCallMotorbike,%d,didRaiseUICycle,%d,didRaiseUICycle_companion,%d,didRaiseUIMotorbike,%d,didRaiseUIMotorbike_companion,%d,escalationDecisionCycle,%d,escalationDecisionMotorbike,%d,isCompanionConnected,%d,isSOSAutoInitiatedCycle,%d,isSOSAutoInitiatedMotorbike,%d,isSOSUserInitiatedCycle,%d,isSOSUserInitiatedMotorbike,%d,locallyArmedBitmap,%d,numAlphaDetectedCycle,%d,numAlphaDetectedMotorbike,%d,numEarlyCrashesDetectedCycle,%d,numEarlyCrashesDetectedMotorbike,%d,numTriggersCycle,%d,numTriggersMotorbike,%d,overrideModeBitmap,%d,signalEnvironment,%d"
+ "Marty UserInfo:%@, ImproveSafety:%d"
+ "No event reported in the manifest"
+ "On %@, spooler dir %@ doesn't exist"
+ "On filePicker, cannot create unarchiver"
+ "On filePicker, cannot read file %@. Try again later"
+ "On submitter, cannot create unarchiver"
+ "On submitter, cannot read file %@. Try again later"
+ "Picked file %@ for upload later"
+ "Please tell us more about what you were doing around %@. \n\nFor example, were you recently in a car or some other moving platform? Were you actively moving or doing some other activity? \n\nWe'll use what you file to refine our iOS/watchOS Safety algorithms."
+ "Please tell us more about what you were doing around %@. \n\nFor example, were you recently in a car or some other moving platform? Were you actively moving or doing some other activity? \n\nWe'll use what you file to refine our iOS/watchOS Safety algorithms. \n\nNote: Two files containing sensor data have been automatically attached to the radar. You can go to the Attachments and delete each file, as well as the original sysdiagnose, if you do not wish for the information to be sent to the team."
+ "Registered with server to upload %@ as %@"
+ "Removed %@ since it doesn't match any event in the manifest"
+ "Removed %@ since it's too old"
+ "Sending %d mins of Kappa userinfo to CA"
+ "Sending %d mins of Marty userinfo to CA"
+ "StudiesUploaderIgneous"
+ "T@\"CSFolderMonitor\",&,V_feedbackHoldingMonitor"
+ "T@\"CSFolderMonitor\",&,V_filePickMonitor"
+ "TB,R,N,GisNavigationTransportTypeAvailable,V_navigationTransportTypeAvailable"
+ "T^{?=QSCB},R,N"
+ "Td,N,V_lat"
+ "Td,N,V_lon"
+ "Td,N,V_radius"
+ "Td,N,V_timestamp"
+ "Td,V_harvestTimeWindowSec"
+ "Td,V_readManifestTimeoutSec"
+ "Td,V_readManifestTimestamp"
+ "Ti,R,N,V_navigationTransportType"
+ "Unable to open manifest file %@"
+ "Unable to read manifest file %@"
+ "Updated transport type, %d"
+ "Uploaded %@ to server: %{public}d, deregister with server"
+ "While enqueuing for feedback assistant holding, file doesnt exist: %@"
+ "Your iPhone detected a possible crash earlier. If you're willing to answer a few questions about the event, your answers can improve crash detection."
+ "[C] AlgBlock summary,A,%{public}llu,B,%{public}d,C,%{public}f,D,%{public}d,E,%{public}d,F,%{public}d,G,%{public}d,H,%{public}d,I,%{public}d,J,%{public}f,K,%{public}f,L,%{public}f,M,%{public}f,N,%{public}f,O,%{public}d,P,%{public}d,Q,%{public}d,R,%{public}d,S,%{public}d,T,%{public}d,U,%{public}f,config-1,%{public}f,config-2,%{public}f,config-3,%{public}f,config-4,%{public}f,config-5,%{public}f,config-6,%{public}f,config-7,%{public}f,config-8,%{public}f,config-9,%{public}f,config-10,%{public}f,config-11,%{public}f,config-12,%{public}f,config-13,%{public}f,config-14,%{public}f,config-15,%{public}f,config-16,%{public}f,config-17,%{public}f,config-18,%{public}f,config-19,%{public}f,config-20,%{public}f,config-21,%{public}f,config-22,%{public}f,config-23,%{public}f,config-24,%{public}f,config-25,%{public}f,config-26,%{public}f,config-27,%{public}f,config-28,%{public}f,config-29,%{public}f,config-30,%{public}f,config-31,%{public}f,config-32,%{public}f,config-33,%{public}f,config-34,%{public}f,config-35,%{public}f,config-36,%{public}f,config-37,%{public}f,config-38,%{public}f,config-39,%{public}f,config-40,%{public}f,config-41,%{public}f\n"
+ "[C] config-40,%f,config-41,%f"
+ "[RC] AlgBlock summary,A,%{public}llu,B,%{public}d,C,%{public}f,D,%{public}f,E,%{public}d,F,%{public}d,G,%{public}f,H,%{public}f,I,%{public}d,J,%{public}d,K,%{public}f,L,%{public}f,M,%{public}f,N,%{public}d,O,%{public}d,P,%{public}d,Q,%{public}d,R,%{public}f,S,%{public}d,T,%{public}d,U,%{public}f,config-1,%{public}f,config-2,%{public}f,config-3,%{public}f,config-4,%{public}f,config-5,%{public}f,config-6,%{public}f,config-7,%{public}f,config-8,%{public}f,config-9,%{public}f,config-10,%{public}f,config-11,%{public}f,config-12,%{public}f,config-13,%{public}f,config-14,%{public}f,config-15,%{public}f,config-16,%{public}f,config-17,%{public}f,config-18,%{public}f,config-19,%{public}f,config-20,%{public}f,config-21,%{public}f,config-22,%{public}f,config-23,%{public}f,config-24,%{public}f,config-25,%{public}f,config-26,%{public}f,config-27,%{public}f,config-28,%{public}f,config-29,%{public}f,config-30,%{public}f,config-31,%{public}f,config-32,%{public}f,config-33,%{public}f,config-34,%{public}f,config-35,%{public}f,config-36,%{public}f,config-37,%{public}f,config-38,%{public}f,config-39,%{public}f,config-40,%{public}f,config-41,%{public}f,config-42,%{public}f,config-43,%{public}f,config-44,%{public}f,config-45,%{public}f,config-46,%{public}f,config-47,%{public}f,config-48,%{public}f,config-49,%{public}f,config-50,%{public}f,config-51,%{public}f,config-52,%{public}f,config-53,%{public}f,config-54,%{public}f,config-55,%{public}f,config-56,%{public}f,config-57,%{public}f,config-58,%{public}f,config-59,%{public}f,config-60,%{public}f,config-61,%{public}f,config-62,%{public}f,config-63,%{public}f,config-64,%{public}f,config-65,%{public}f,config-66,%{public}f\n"
+ "[RC] config-64,%f,config-65,%f,config-66,%f"
+ "[TAH] %d %d %f %d %d %d %llu %llu %f %llu"
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
+ "_eventsInManifest"
+ "_feedbackHoldingMonitor"
+ "_filePickMonitor"
+ "_geoServicesListener"
+ "_harvestTimeWindowSec"
+ "_lat"
+ "_lon"
+ "_navigationListener"
+ "_navigationTransportType"
+ "_navigationTransportTypeAvailable"
+ "_radius"
+ "_readManifestTimeoutSec"
+ "_readManifestTimestamp"
+ "_requestVisitState"
+ "checkWithManifest:"
+ "com.apple.anomalydetectiond.kappa.feedbackConsentResponse"
+ "com.apple.appleseed.FeedbackAssistant"
+ "createDirectoryAtURL:withIntermediateDirectories:attributes:error:"
+ "d24@0:8d16"
+ "dataWithContentsOfFile:"
+ "dataWithContentsOfURL:options:error:"
+ "dateByAddingUnit:value:toDate:options:"
+ "dateFromComponents:"
+ "dateWithHour:fromDate:"
+ "deltaVXYUnconditionalPlanarWithAudioThreshold"
+ "deltaVXYUnconditionalPlanarWithoutAudioThreshold"
+ "deltaVXYUnconditionalRolloverWithAudioThreshold"
+ "deltaVXYUnconditionalRolloverWithoutAudioThreshold"
+ "displayPoseState"
+ "enqueueHeldRecordingForUpload:"
+ "eq_history_manifest_v1.txt"
+ "eventDurationMinutes"
+ "feedbackAssistantHolding"
+ "feedbackHoldingMonitor"
+ "filePickMonitor"
+ "filePicker"
+ "fileURLWithFileSystemRepresentation:isDirectory:relativeToURL:"
+ "getFileUrlsForRecording:metadataUrl:mslUrl:withError:"
+ "hapticsOn"
+ "harvestTimeWindowSec"
+ "hasArrivalDate"
+ "hasDepartureDate"
+ "holdRecordingUntilFeedbackConsent:withError:"
+ "iconForApplicationIdentifier:"
+ "initFileURLWithPath:"
+ "initWithDispatchSilo:"
+ "initWithQueue:"
+ "initWithSpoolerFolder:serverConfiguration:retentionPeriodInSeconds:outOfBandMetadataTimeout:defaultsKeyPostfix:"
+ "initWithTimestamp:dramDurationMs:vehicularFlags:hapticsOn:"
+ "isFeedbackAssistantEligible"
+ "isInLOIVisit"
+ "isNavigationTransportTypeAvailable"
+ "isPitchStable"
+ "lat"
+ "locationManager:didReportVisit:"
+ "lon"
+ "manifest"
+ "mapsNavigationTransportType"
+ "maxMean"
+ "meanN"
+ "messages"
+ "minMean"
+ "mobilityCalibrationMessage"
+ "msl.protodata"
+ "navigationListener:didChangeNavigationState:transportType:"
+ "navigationListener:didUpdateActiveRouteData:"
+ "navigationListener:didUpdateCurrentRoadName:"
+ "navigationListener:didUpdateGuidanceState:"
+ "navigationListener:didUpdateNavigationVoiceVolume:"
+ "navigationListener:didUpdatePositionFromDestination:"
+ "navigationListener:didUpdatePositionFromManeuver:"
+ "navigationListener:didUpdatePositionFromSign:"
+ "navigationListener:didUpdateRideSelections:"
+ "navigationListener:didUpdateRouteSummary:"
+ "navigationListener:didUpdateStepIndex:"
+ "navigationListener:didUpdateStepNameInfo:"
+ "navigationListener:didUpdateTransitSummary:"
+ "navigationTransportType"
+ "navigationTransportTypeAvailable"
+ "normalGammaCalibrationBin"
+ "numberOfDetectedFaces"
+ "persistToDiskWithSpooledFile:spoolerDir:fileURL:enqueueTime:metadata:error:"
+ "presentationTimestamp"
+ "quaternionWithoutPrediction"
+ "r"
+ "readManifestFromFile"
+ "readManifestTimeoutSec"
+ "readManifestTimestamp"
+ "removeHeldRecording:"
+ "setFeedbackHoldingMonitor:"
+ "setFilePickMonitor:"
+ "setHarvestTimeWindowSec:"
+ "setHour:"
+ "setIcon:"
+ "setLat:"
+ "setLon:"
+ "setMinute:"
+ "setRadius:"
+ "setReadManifestTimeoutSec:"
+ "setReadManifestTimestamp:"
+ "setSecond:"
+ "slowRollZgTimeThreshold"
+ "speedLB"
+ "speedUB"
+ "startMonitoringVisits"
+ "stopMonitoringVisits"
+ "systemgroup.com.apple.safetyalerts"
+ "t"
+ "timeIntervalToNearestEightOClock:"
+ "updateN"
+ "updateParametersFromDefaultsConfig"
+ "upload"
+ "utcToIosSeconds:"
+ "v16@?0@\"NSURL\"8"
+ "v28@0:8@\"GEONavigationListener\"16i24"
+ "v32@0:8@\"GEONavigationListener\"16@\"GEONameInfo\"24"
+ "v32@0:8@\"GEONavigationListener\"16@\"GEONavigationGuidanceState\"24"
+ "v32@0:8@\"GEONavigationListener\"16@\"GEONavigationRouteSummary\"24"
+ "v32@0:8@\"GEONavigationListener\"16@\"GEONavigationRouteTransitSummary\"24"
+ "v32@0:8@\"GEONavigationListener\"16@\"NSArray\"24"
+ "v32@0:8@\"GEONavigationListener\"16@\"NSData\"24"
+ "v32@0:8@\"GEONavigationListener\"16@\"NSString\"24"
+ "v32@0:8@\"GEONavigationListener\"16Q24"
+ "v32@0:8@16^@24"
+ "v36@0:8@\"GEONavigationListener\"16Q24i32"
+ "v36@0:8@16Q24i32"
+ "v40@0:8@\"GEONavigationListener\"16{?=dd}24"
+ "v40@0:8@16{?=dd}24"
+ "v48@0:8@16^@24^@32^@40"
+ "varianceN"
+ "{?=\"timestamp\"Q\"dramDurationMs\"S\"vehicularFlags\"C\"hapticsOn\"B}"
- "\x17\x12\x115\x11"
- "\x184"
- "@32@0:8Q16S24C28"
- "B52@0:8B16@20d28@36^@44"
- "CSIgneousTokenCount"
- "CSIgneousTokenCountDefault"
- "CSIgneousTokenReplenishPeriod"
- "CSIgneousTokenReplenishTimestamp"
- "CSKappaConnection"
- "CSKappaConnectionQueue"
- "Connection Interrupted"
- "Couldn't retrieve localized push notification strings"
- "Created Feedback Assistant notification request:%@"
- "Failed to add Feedback Assistant notification request,error,%@"
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
- "[C] AlgBlock summary,A,%{public}llu,B,%{public}d,C,%{public}f,D,%{public}d,E,%{public}d,F,%{public}d,G,%{public}d,H,%{public}d,I,%{public}d,J,%{public}f,K,%{public}f,L,%{public}f,M,%{public}f,N,%{public}f,O,%{public}d,P,%{public}d,Q,%{public}d,R,%{public}d,S,%{public}d,T,%{public}d,config-1,%{public}f,config-2,%{public}f,config-3,%{public}f,config-4,%{public}f,config-5,%{public}f,config-6,%{public}f,config-7,%{public}f,config-8,%{public}f,config-9,%{public}f,config-10,%{public}f,config-11,%{public}f,config-12,%{public}f,config-13,%{public}f,config-14,%{public}f,config-15,%{public}f,config-16,%{public}f,config-17,%{public}f,config-18,%{public}f,config-19,%{public}f,config-20,%{public}f,config-21,%{public}f,config-22,%{public}f,config-23,%{public}f,config-24,%{public}f,config-25,%{public}f,config-26,%{public}f,config-27,%{public}f,config-28,%{public}f,config-29,%{public}f,config-30,%{public}f,config-31,%{public}f,config-32,%{public}f,config-33,%{public}f,config-34,%{public}f,config-35,%{public}f,config-36,%{public}f,config-37,%{public}f,config-38,%{public}f,config-39,%{public}f\n"
- "[RC] AlgBlock summary,A,%{public}llu,B,%{public}d,C,%{public}f,D,%{public}f,E,%{public}d,F,%{public}d,G,%{public}f,H,%{public}f,I,%{public}d,J,%{public}d,K,%{public}f,L,%{public}f,M,%{public}f,N,%{public}d,O,%{public}d,P,%{public}d,Q,%{public}d,R,%{public}f,S,%{public}d,T,%{public}d,config-1,%{public}f,config-2,%{public}f,config-3,%{public}f,config-4,%{public}f,config-5,%{public}f,config-6,%{public}f,config-7,%{public}f,config-8,%{public}f,config-9,%{public}f,config-10,%{public}f,config-11,%{public}f,config-12,%{public}f,config-13,%{public}f,config-14,%{public}f,config-15,%{public}f,config-16,%{public}f,config-17,%{public}f,config-18,%{public}f,config-19,%{public}f,config-20,%{public}f,config-21,%{public}f,config-22,%{public}f,config-23,%{public}f,config-24,%{public}f,config-25,%{public}f,config-26,%{public}f,config-27,%{public}f,config-28,%{public}f,config-29,%{public}f,config-30,%{public}f,config-31,%{public}f,config-32,%{public}f,config-33,%{public}f,config-34,%{public}f,config-35,%{public}f,config-36,%{public}f,config-37,%{public}f,config-38,%{public}f,config-39,%{public}f,config-40,%{public}f,config-41,%{public}f,config-42,%{public}f,config-43,%{public}f,config-44,%{public}f,config-45,%{public}f,config-46,%{public}f,config-47,%{public}f,config-48,%{public}f,config-49,%{public}f,config-50,%{public}f,config-51,%{public}f,config-52,%{public}f,config-53,%{public}f,config-54,%{public}f,config-55,%{public}f,config-56,%{public}f,config-57,%{public}f,config-58,%{public}f,config-59,%{public}f,config-60,%{public}f,config-61,%{public}f,config-62,%{public}f,config-63,%{public}f\n"
- "[TAH] %d %d %f %d %d %llu %llu %f %llu"
- "^{?=QSC}16@0:8"
- "_internalQueue"
- "acquiring igneous token"
- "defaultMessageHandler:"
- "igneousOut"
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
