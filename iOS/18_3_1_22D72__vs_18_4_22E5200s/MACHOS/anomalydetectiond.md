## anomalydetectiond

> `/usr/libexec/anomalydetectiond`

```diff

-121.0.1.0.0
-  __TEXT.__text: 0x322320
-  __TEXT.__auth_stubs: 0x16d0
-  __TEXT.__objc_stubs: 0x8b60
-  __TEXT.__objc_methlist: 0x7e24
-  __TEXT.__const: 0x8c0d
-  __TEXT.__gcc_except_tab: 0xfe90
-  __TEXT.__cstring: 0x19052
-  __TEXT.__oslogstring: 0xf0df
-  __TEXT.__objc_classname: 0x1068
-  __TEXT.__objc_methtype: 0x6102
-  __TEXT.__objc_methname: 0xb4f9
+125.0.9.0.0
+  __TEXT.__text: 0x3294d4
+  __TEXT.__auth_stubs: 0x16e0
+  __TEXT.__objc_stubs: 0x8f40
+  __TEXT.__objc_methlist: 0x8c38
+  __TEXT.__const: 0x8d65
+  __TEXT.__gcc_except_tab: 0x108f8
+  __TEXT.__cstring: 0x1929c
+  __TEXT.__oslogstring: 0xf69f
+  __TEXT.__objc_classname: 0x10d1
+  __TEXT.__objc_methtype: 0x63a5
+  __TEXT.__objc_methname: 0xbc4f
   __TEXT.__ustring: 0x10ae
-  __TEXT.__unwind_info: 0xb8d8
+  __TEXT.__unwind_info: 0xb788
   __TEXT.__eh_frame: 0x590
-  __DATA_CONST.__auth_got: 0xb80
-  __DATA_CONST.__got: 0x570
-  __DATA_CONST.__auth_ptr: 0x30
-  __DATA_CONST.__const: 0x221e8
-  __DATA_CONST.__cfstring: 0x5d20
-  __DATA_CONST.__objc_classlist: 0x4b0
+  __DATA_CONST.__auth_got: 0xb88
+  __DATA_CONST.__got: 0x588
+  __DATA_CONST.__auth_ptr: 0x38
+  __DATA_CONST.__const: 0x22300
+  __DATA_CONST.__cfstring: 0x5e20
+  __DATA_CONST.__objc_classlist: 0x4c8
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
+  __DATA_CONST.__objc_superrefs: 0x448
+  __DATA_CONST.__objc_intobj: 0x1818
+  __DATA_CONST.__objc_arraydata: 0x240
+  __DATA_CONST.__objc_arrayobj: 0x30
+  __DATA_CONST.__objc_dictobj: 0x320
+  __DATA.__objc_const: 0x10520
+  __DATA.__objc_selrefs: 0x2f30
+  __DATA.__objc_ivar: 0x958
+  __DATA.__objc_data: 0x2fd0
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
+  Functions: 15253
+  Symbols:   568
+  CStrings:  8660
 
Symbols:
+ _OBJC_CLASS_$_GEONavigationListener
+ __ZNSt3__117bad_function_callD1Ev
+ __ZTINSt3__117bad_function_callE
+ __ZTVNSt3__117bad_function_callE
+ _container_system_group_path_for_identifier
- __ZNKSt9exception4whatEv
CStrings:
+ "\x17\x12\x115\x12"
+ "@\"CSGeoServicesListener\""
+ "@\"GEONavigationListener\""
+ "@56@0:8@16@24Q32d40@48"
+ "C24@0:8@16"
+ "CSGeoServicesListener"
+ "CSIgneousAnomalyEvent"
+ "CSIgneousHarvestTimeWindowSec"
+ "CSIgneousReadManifestTimeoutSec"
+ "CSStudiesServerUploaderIgneous"
+ "Entered LOI"
+ "Exited LOI"
+ "Failed to append data from file %@"
+ "Failed to finalize encrypting file %@"
+ "Failed to register with server to upload %@"
+ "Failed to remove file %@"
+ "Failed to start output file %@"
+ "File %@ doesn't contain value for key 'spooled'"
+ "File %@ has been encrypted as %@"
+ "File %@ is newer than all events in the manifest. Try again later"
+ "File %@ will be encrypted"
+ "File to be encrypted %@ doesn't exist"
+ "Finished reading %d events from manifest file %@"
+ "GEONavigationListenerDelegate"
+ "Group container not available"
+ "Initialized Igneous uploader: registered %d, monitoring %d, harvestTimeWindowSec %.0f, readManifestTimeoutSec %.0f"
+ "Manifest event count %d"
+ "Manifest is empty"
+ "No event reported in the manifest"
+ "On %@, spooler dir %@ doesn't exist"
+ "On filePicker, cannot create unarchiver"
+ "On filePicker, cannot read file %@. Try again later"
+ "On submitter, cannot create unarchiver"
+ "On submitter, cannot read file %@. Try again later"
+ "Picked file %@ for upload later"
+ "Registered with server to upload %@ as %@"
+ "Removed %@ since it doesn't match any event in the manifest"
+ "Removed %@ since it's too old"
+ "Sending %d mins of Kappa userinfo to CA"
+ "Sending %d mins of Marty userinfo to CA"
+ "StudiesUploaderIgneous"
+ "T@\"CSFolderMonitor\",&,V_filePickMonitor"
+ "TB,R,N,GisNavigationTransportTypeAvailable,V_navigationTransportTypeAvailable"
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
+ "[C] AlgBlock summary,A,%{public}llu,B,%{public}d,C,%{public}f,D,%{public}d,E,%{public}d,F,%{public}d,G,%{public}d,H,%{public}d,I,%{public}d,J,%{public}f,K,%{public}f,L,%{public}f,M,%{public}f,N,%{public}f,O,%{public}d,P,%{public}d,Q,%{public}d,R,%{public}d,S,%{public}d,T,%{public}d,U,%{public}f,config-1,%{public}f,config-2,%{public}f,config-3,%{public}f,config-4,%{public}f,config-5,%{public}f,config-6,%{public}f,config-7,%{public}f,config-8,%{public}f,config-9,%{public}f,config-10,%{public}f,config-11,%{public}f,config-12,%{public}f,config-13,%{public}f,config-14,%{public}f,config-15,%{public}f,config-16,%{public}f,config-17,%{public}f,config-18,%{public}f,config-19,%{public}f,config-20,%{public}f,config-21,%{public}f,config-22,%{public}f,config-23,%{public}f,config-24,%{public}f,config-25,%{public}f,config-26,%{public}f,config-27,%{public}f,config-28,%{public}f,config-29,%{public}f,config-30,%{public}f,config-31,%{public}f,config-32,%{public}f,config-33,%{public}f,config-34,%{public}f,config-35,%{public}f,config-36,%{public}f,config-37,%{public}f,config-38,%{public}f,config-39,%{public}f,config-40,%{public}f,config-41,%{public}f\n"
+ "[C] config-40,%f,config-41,%f"
+ "[RC] AlgBlock summary,A,%{public}llu,B,%{public}d,C,%{public}f,D,%{public}f,E,%{public}d,F,%{public}d,G,%{public}f,H,%{public}f,I,%{public}d,J,%{public}d,K,%{public}f,L,%{public}f,M,%{public}f,N,%{public}d,O,%{public}d,P,%{public}d,Q,%{public}d,R,%{public}f,S,%{public}d,T,%{public}d,U,%{public}f,config-1,%{public}f,config-2,%{public}f,config-3,%{public}f,config-4,%{public}f,config-5,%{public}f,config-6,%{public}f,config-7,%{public}f,config-8,%{public}f,config-9,%{public}f,config-10,%{public}f,config-11,%{public}f,config-12,%{public}f,config-13,%{public}f,config-14,%{public}f,config-15,%{public}f,config-16,%{public}f,config-17,%{public}f,config-18,%{public}f,config-19,%{public}f,config-20,%{public}f,config-21,%{public}f,config-22,%{public}f,config-23,%{public}f,config-24,%{public}f,config-25,%{public}f,config-26,%{public}f,config-27,%{public}f,config-28,%{public}f,config-29,%{public}f,config-30,%{public}f,config-31,%{public}f,config-32,%{public}f,config-33,%{public}f,config-34,%{public}f,config-35,%{public}f,config-36,%{public}f,config-37,%{public}f,config-38,%{public}f,config-39,%{public}f,config-40,%{public}f,config-41,%{public}f,config-42,%{public}f,config-43,%{public}f,config-44,%{public}f,config-45,%{public}f,config-46,%{public}f,config-47,%{public}f,config-48,%{public}f,config-49,%{public}f,config-50,%{public}f,config-51,%{public}f,config-52,%{public}f,config-53,%{public}f,config-54,%{public}f,config-55,%{public}f,config-56,%{public}f,config-57,%{public}f,config-58,%{public}f,config-59,%{public}f,config-60,%{public}f,config-61,%{public}f,config-62,%{public}f,config-63,%{public}f,config-64,%{public}f,config-65,%{public}f,config-66,%{public}f\n"
+ "[RC] config-64,%f,config-65,%f,config-66,%f"
+ "[TAH] %d %d %f %d %d %d %llu %llu %f %llu"
+ "_eventsInManifest"
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
+ "d24@0:8d16"
+ "dataWithContentsOfFile:"
+ "deltaVXYUnconditionalPlanarWithAudioThreshold"
+ "deltaVXYUnconditionalPlanarWithoutAudioThreshold"
+ "deltaVXYUnconditionalRolloverWithAudioThreshold"
+ "deltaVXYUnconditionalRolloverWithoutAudioThreshold"
+ "displayPoseState"
+ "eq_history_manifest_v1.txt"
+ "eventDurationMinutes"
+ "filePickMonitor"
+ "filePicker"
+ "fileURLWithFileSystemRepresentation:isDirectory:relativeToURL:"
+ "harvestTimeWindowSec"
+ "hasArrivalDate"
+ "hasDepartureDate"
+ "initWithDispatchSilo:"
+ "initWithQueue:"
+ "initWithSpoolerFolder:serverConfiguration:retentionPeriodInSeconds:outOfBandMetadataTimeout:defaultsKeyPostfix:"
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
+ "presentationTimestamp"
+ "quaternionWithoutPrediction"
+ "r"
+ "readManifestFromFile"
+ "readManifestTimeoutSec"
+ "readManifestTimestamp"
+ "setFilePickMonitor:"
+ "setHarvestTimeWindowSec:"
+ "setLat:"
+ "setLon:"
+ "setRadius:"
+ "setReadManifestTimeoutSec:"
+ "setReadManifestTimestamp:"
+ "slowRollZgTimeThreshold"
+ "speedLB"
+ "speedUB"
+ "startMonitoringVisits"
+ "stopMonitoringVisits"
+ "systemgroup.com.apple.safetyalerts"
+ "t"
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
+ "v36@0:8@\"GEONavigationListener\"16Q24i32"
+ "v36@0:8@16Q24i32"
+ "v40@0:8@\"GEONavigationListener\"16{?=dd}24"
+ "v40@0:8@16{?=dd}24"
+ "varianceN"
- "\x17\x12\x115\x11"
- "CSIgneousTokenCount"
- "CSIgneousTokenCountDefault"
- "CSIgneousTokenReplenishPeriod"
- "CSIgneousTokenReplenishTimestamp"
- "[C] AlgBlock summary,A,%{public}llu,B,%{public}d,C,%{public}f,D,%{public}d,E,%{public}d,F,%{public}d,G,%{public}d,H,%{public}d,I,%{public}d,J,%{public}f,K,%{public}f,L,%{public}f,M,%{public}f,N,%{public}f,O,%{public}d,P,%{public}d,Q,%{public}d,R,%{public}d,S,%{public}d,T,%{public}d,config-1,%{public}f,config-2,%{public}f,config-3,%{public}f,config-4,%{public}f,config-5,%{public}f,config-6,%{public}f,config-7,%{public}f,config-8,%{public}f,config-9,%{public}f,config-10,%{public}f,config-11,%{public}f,config-12,%{public}f,config-13,%{public}f,config-14,%{public}f,config-15,%{public}f,config-16,%{public}f,config-17,%{public}f,config-18,%{public}f,config-19,%{public}f,config-20,%{public}f,config-21,%{public}f,config-22,%{public}f,config-23,%{public}f,config-24,%{public}f,config-25,%{public}f,config-26,%{public}f,config-27,%{public}f,config-28,%{public}f,config-29,%{public}f,config-30,%{public}f,config-31,%{public}f,config-32,%{public}f,config-33,%{public}f,config-34,%{public}f,config-35,%{public}f,config-36,%{public}f,config-37,%{public}f,config-38,%{public}f,config-39,%{public}f\n"
- "[RC] AlgBlock summary,A,%{public}llu,B,%{public}d,C,%{public}f,D,%{public}f,E,%{public}d,F,%{public}d,G,%{public}f,H,%{public}f,I,%{public}d,J,%{public}d,K,%{public}f,L,%{public}f,M,%{public}f,N,%{public}d,O,%{public}d,P,%{public}d,Q,%{public}d,R,%{public}f,S,%{public}d,T,%{public}d,config-1,%{public}f,config-2,%{public}f,config-3,%{public}f,config-4,%{public}f,config-5,%{public}f,config-6,%{public}f,config-7,%{public}f,config-8,%{public}f,config-9,%{public}f,config-10,%{public}f,config-11,%{public}f,config-12,%{public}f,config-13,%{public}f,config-14,%{public}f,config-15,%{public}f,config-16,%{public}f,config-17,%{public}f,config-18,%{public}f,config-19,%{public}f,config-20,%{public}f,config-21,%{public}f,config-22,%{public}f,config-23,%{public}f,config-24,%{public}f,config-25,%{public}f,config-26,%{public}f,config-27,%{public}f,config-28,%{public}f,config-29,%{public}f,config-30,%{public}f,config-31,%{public}f,config-32,%{public}f,config-33,%{public}f,config-34,%{public}f,config-35,%{public}f,config-36,%{public}f,config-37,%{public}f,config-38,%{public}f,config-39,%{public}f,config-40,%{public}f,config-41,%{public}f,config-42,%{public}f,config-43,%{public}f,config-44,%{public}f,config-45,%{public}f,config-46,%{public}f,config-47,%{public}f,config-48,%{public}f,config-49,%{public}f,config-50,%{public}f,config-51,%{public}f,config-52,%{public}f,config-53,%{public}f,config-54,%{public}f,config-55,%{public}f,config-56,%{public}f,config-57,%{public}f,config-58,%{public}f,config-59,%{public}f,config-60,%{public}f,config-61,%{public}f,config-62,%{public}f,config-63,%{public}f\n"
- "[TAH] %d %d %f %d %d %llu %llu %f %llu"
- "acquiring igneous token"
- "igneousOut"

```
