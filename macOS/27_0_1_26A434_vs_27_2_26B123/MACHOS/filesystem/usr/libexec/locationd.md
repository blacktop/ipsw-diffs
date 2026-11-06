## locationd

> `/usr/libexec/locationd`

### Sections with Same Size but Changed Content

- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_proto`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`

```diff

-3185.0.6.0.0
-  __TEXT.__text: 0x678e88
-  __TEXT.__auth_stubs: 0x38f0
-  __TEXT.__objc_stubs: 0x10e00
-  __TEXT.__init_offsets: 0x184
-  __TEXT.__objc_methlist: 0x12a70
-  __TEXT.__const: 0x17fb8
-  __TEXT.__gcc_except_tab: 0x2ab1c
-  __TEXT.__cstring: 0x7af26
-  __TEXT.__oslogstring: 0x98b26
-  __TEXT.__objc_methname: 0x1fd8e
-  __TEXT.__objc_classname: 0x33f4
-  __TEXT.__objc_methtype: 0xf14c
+3186.0.22.0.0
+  __TEXT.__text: 0x67fdfc
+  __TEXT.__auth_stubs: 0x3910
+  __TEXT.__objc_stubs: 0x10f80
+  __TEXT.__init_offsets: 0x188
+  __TEXT.__objc_methlist: 0x12b60
+  __TEXT.__const: 0x17fe8
+  __TEXT.__gcc_except_tab: 0x2ad24
+  __TEXT.__cstring: 0x7b60a
+  __TEXT.__oslogstring: 0x9a080
+  __TEXT.__objc_methname: 0x2009e
+  __TEXT.__objc_classname: 0x3404
+  __TEXT.__objc_methtype: 0xf1dc
   __TEXT.__ustring: 0x346
   __TEXT.__constg_swiftt: 0x424
   __TEXT.__swift5_typeref: 0x241

   __TEXT.__swift_as_cont: 0x10
   __TEXT.__swift5_proto: 0x4c
   __TEXT.__swift5_assocty: 0x30
-  __TEXT.__info_plist: 0x66c
-  __TEXT.__unwind_info: 0x1e260
+  __TEXT.__info_plist: 0x674
+  __TEXT.__unwind_info: 0x1e3c8
   __TEXT.__eh_frame: 0x630
-  __DATA_CONST.__const: 0x2c160
-  __DATA_CONST.__cfstring: 0x15d00
+  __DATA_CONST.__const: 0x2c310
+  __DATA_CONST.__cfstring: 0x16100
   __DATA_CONST.__objc_classlist: 0x8d0
   __DATA_CONST.__objc_catlist: 0x78
-  __DATA_CONST.__objc_protolist: 0x5b0
+  __DATA_CONST.__objc_protolist: 0x5b8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x4a0
   __DATA_CONST.__objc_superrefs: 0x7d8
-  __DATA_CONST.__objc_arraydata: 0xb60
+  __DATA_CONST.__objc_arraydata: 0xc18
   __DATA_CONST.__objc_dictobj: 0x320
   __DATA_CONST.__objc_intobj: 0x1038
   __DATA_CONST.__objc_doubleobj: 0x40
-  __DATA_CONST.__objc_arrayobj: 0x138
+  __DATA_CONST.__objc_arrayobj: 0x198
   __DATA_CONST.__objc_floatobj: 0x10
   __DATA_CONST.__linkguard: 0x15
-  __DATA_CONST.__auth_got: 0x1c98
-  __DATA_CONST.__got: 0xc00
+  __DATA_CONST.__auth_got: 0x1ca8
+  __DATA_CONST.__got: 0xc08
   __DATA_CONST.__auth_ptr: 0x2d0
-  __DATA.__objc_const: 0x1eb70
-  __DATA.__objc_selrefs: 0x7838
-  __DATA.__objc_ivar: 0x1298
+  __DATA.__objc_const: 0x1ebf8
+  __DATA.__objc_selrefs: 0x78c0
+  __DATA.__objc_ivar: 0x129c
   __DATA.__objc_data: 0x5b98
-  __DATA.__data: 0x56e8
-  __DATA.__common: 0x7d8
-  __DATA.__bss: 0x2c60
+  __DATA.__data: 0x5748
+  __DATA.__common: 0x7f8
+  __DATA.__bss: 0x2ca0
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate
   - /System/Library/Frameworks/CFNetwork.framework/Versions/A/CFNetwork
   - /System/Library/Frameworks/CoreBluetooth.framework/Versions/A/CoreBluetooth

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 26947
-  Symbols:   1391
-  CStrings:  24939
+  Functions: 27027
+  Symbols:   1394
+  CStrings:  25078
 
Symbols:
+ _OBJC_CLASS_$_CLLocationCoordinate
+ _dispatch_block_create_with_qos_class
+ _qos_class_self
CStrings:
+ " LIMIT ? OFFSET ?"
+ "#CoreLocationAgent ignoring a disconnection from a connection that does not hold the agent slot"
+ "#CoreLocationAgent rejecting an unentitled connection"
+ "#CoreLocationAgent rejecting an unentitled sender on the agent MIG port"
+ "#Pinning Location unchanged (within range) and already authorized"
+ "#Pinning New Location has been preauthorized"
+ "#Pinning New Location received"
+ "#Pinning New location while already prompting for authorization."
+ "#Pinning Received a zero location!"
+ "#Pinning Received location is invalid. Let's have it dropped by next layers"
+ "#Quarantine refusing to quarantine a client we don't hold"
+ "#Spi, Must provide a bundle ID or a bundle path to clear a location authorization"
+ "#Spi, Must provide both a source and a destination bundle ID to copy authorization"
+ "#Spi, Refusing to copy authorization onto the same bundle ID"
+ "#Spi, appA to appB migration is iOS only"
+ "#Spi, clearing a location authorization outright is iOS only"
+ "#Warning fGetRandomMacsCachedStmt is not valid in CLWifiLocationDatabase!"
+ "#gfm, checkForGpsFailure, forced by CLGnssFailureMonitorForceFailure"
+ "#monitor no accessible container for client; bailing out (nil ledger)"
+ "#wci,ggselector,airborne override,currentRestrictedMode,%{public}d"
+ "#wci,ggselector,airborneClient,%{public}d"
+ "#wci,ggselector,airplaneMode,%{public}d"
+ "#wci,ggselector,constructed,deviceClass,%{public}d"
+ "%{public}s%{private}s"
+ "-[CLInternalService clearLocationAuthorizationForLoctoolWithBundleId:orBundlePath:withReplyBlock:]"
+ "-[CLInternalService copyAuthorizationFromBundleID:toBundleID:replyBlock:]"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/local/include/boost/uuid/string_generator.hpp"
+ "/AppleInternal/Library/Frameworks/CoreAutomationDevice.framework"
+ "/AppleInternal/Library/LocationBundles/FenceTester.bundle"
+ "/AppleInternal/Library/LocationBundles/LocationMonitor.bundle"
+ "/System/Library/LocationBundles/SystemCustomization.bundle"
+ "/System/Library/LocationBundles/WebBrowsingServices.bundle"
+ "/System/Library/PrivateFrameworks/HomeKitDaemon.framework"
+ "/System/Library/PrivateFrameworks/MobileWiFi.framework"
+ "22:02:52"
+ "<unknown>"
+ "@136@0:8{CLPIOSample=dddffffffffffffffffffffffCCCCCCS}16"
+ "@32@0:8r*16Q24"
+ "@WifiLocationDB, error, could not bind in getRandomMacs (table: %{public}s)"
+ "@WifiLocationDB, error, could not get scoped statement in getRandomMacs (table: %{public}s)"
+ "ATMaritime"
+ "AllowedAlways"
+ "AllowedAlwaysProvisionally"
+ "AllowedWhenInUse"
+ "Assertion failed: lambda2 != 0, file /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/CoreLocation/Oscar/Math/CMOQuaternion.cpp, line 172,invalid weights."
+ "AuthContext InUse:%d  RegResult Transient:%s Effective:%s  EffectiveMask:%d  ProvisionalMask:%d  DiagnosticMask:%d"
+ "BadServerSideCentroidDatabase"
+ "BufferedGnssLeech"
+ "CL: _CLDaemonClearLocationAuthorizationForLoctool"
+ "CL: _CLDaemonCopyAuthorization"
+ "CLAppMonitorQoS"
+ "CLClientManagerTestProtocol"
+ "CLGpsGalSelector::CLGpsGalSelector(id<CLIntersiloUniverse>, DeviceClass)"
+ "CLLS"
+ "CLRS,CLTSP,intervalCountMismatch,decoded,%{public}lu,recorded,%{public}lu"
+ "CLRS,CLTSP,malformedPackedAltitudeBlob,bytes,%{public}lu,stride,%{public}lu"
+ "CLRS,CLTSP,malformedPackedLocationBlob,bytes,%{public}lu,stride,%{public}lu"
+ "CLRS,CLTSP,malformedPackedOdometryBlob,bytes,%{public}lu,stride,%{public}lu"
+ "CLRS,CLTSP,packedAltitudeBlobAllocationFailed,samples,%{public}lu"
+ "CLRS,CLTSP,packedLocationBlobAllocationFailed,samples,%{public}lu"
+ "CLRS,CLTSP,packedOdometryBlobAllocationFailed,samples,%{public}lu"
+ "CLRS,CLTSP,unsupportedBatchInputSchemaVersion,decoded,%{public}lu,oldestSupported,%{public}lu,current,%{public}lu"
+ "CLWifiLocationProvider unavailable; disabling wifi provider"
+ "DaemonIdentifiableClient #dic was created with a non-registered (possibly uninstalled) / quarantined CKP. Bailing out."
+ "DeviceClass"
+ "FailedBlocklisted"
+ "FailedUnavailable"
+ "FailedUnverified"
+ "FailedUserDenied"
+ "HomeAccessory"
+ "Missing"
+ "MusicHandoffScan"
+ "Oct 13 2026"
+ "Oct 13 2026 22:04:47"
+ "Quarantined"
+ "RBSLAT #AppMonitor CL-ARM monitor still has no predicate"
+ "RBSLAT #AppMonitor CL-SUB no RBS state update since subscribe"
+ "RegistrationResultString"
+ "RequiresAgent"
+ "TB,N,GisClientActivityTypeMaritimeActive,V_clientActivityTypeMaritimeActive"
+ "TransientAwareRegistrationResultString"
+ "_clientActivityTypeMaritimeActive"
+ "airborne"
+ "altitudeSamplesPacked"
+ "clearLocationAuthorizationForLoctoolWithBundleId:orBundlePath:withReplyBlock:"
+ "clientActivityTypeMaritimeActive"
+ "com.apple.CalendarPebble"
+ "com.apple.Home.HomeWidgetTV"
+ "com.apple.MapKitTester"
+ "com.apple.PebbleSettingsApp"
+ "com.apple.WatchFacesWallpaperSupport.SnoopyPoster"
+ "com.apple.findmy"
+ "com.apple.locationd.migrateauthorization"
+ "com.apple.mobilesafari"
+ "com.apple.mobiletimer.WorldClocks"
+ "com.apple.private.locationd.corelocationagent"
+ "com.apple.weather.nonPersonal"
+ "com.apple.weather.widget"
+ "copyAuthorizationFromBundleID:toBundleID:replyBlock:"
+ "dataWithLength:"
+ "decodeBytesForKey:returnedLength:"
+ "distanceCalibratedPedometer"
+ "doNothingWithReply:"
+ "encodeBytes:length:forKey:"
+ "flushWithReply:"
+ "inHandDoubleTapBaseDetectorReset"
+ "intervalCount"
+ "isClientActivityTypeMaritimeActive"
+ "isSimulationRunningWithReply:"
+ "kCLClientRegistrationResultFailedUnverified"
+ "kCLLocationStreamingMessageActivityTypeMaritimeKey"
+ "locationSamplesPacked"
+ "odometrySamplesPacked"
+ "packedDataFromSamples:"
+ "pencilState"
+ "promoteSystemServiceWithBundlePath:withReply:"
+ "reconfigure"
+ "registerClientForTesting:allowUninstalled:withReply:"
+ "registeredKeyPathForBundleBackedApp:"
+ "samplesFromPackedBytes:length:"
+ "setClientActivityTypeMaritimeActive:"
+ "setClientQuarantined:quarantined:entity:withReply:"
+ "setSupportedAuthorizationMaskKeyChecker:withReply:"
+ "std::vector<CLMacAddress> CLWifiLocationDatabase::getRandomMacs(int)"
+ "toggleLocationUpdates:inFitnessSession:inAirborneSession:inMaritimeSession:emergencyEnablementAssertionActive:"
+ "unquarantineClient:"
+ "v1732@0:8i16{NotificationData={CLDaemonLocation=i{?=dd}ddddddddidi{?=dd}diIiiidB}{CLDaemonLocationPrivate=dddddfffBi{?=dd}diiB{?=ddBBidqddd}{?={?=iddddd{?=dd}dd}iQiiiidB}{?=dd}if{?=dd}ddiBddddddddBB{?=dd}diddddddB{shared_ptr<const CLDaemonLocationPrivate::AboveHorizonSatelliteVisibilityReport>=^{AboveHorizonSatelliteVisibilityReport}^{__shared_weak_count}}i{AltitudeInfo=dddi}CdddCCBii{?=I}{?=if}iiiBffffd{?=dddffffff}}{shared_ptr<CLBatchedLocations>=^{CLBatchedLocations}^{__shared_weak_count}}{TechnologyStatus=iB}Bd{?=dddd}{?=dd}{XtraFileAvailable=d{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}}i{LocationDerivedSpeed=ddd}{?=dddi}{?=ddddddB[3[3d]]dddQi}i{?=idddddd[5d]ddddii}{CLStrongPtr<NSData *>=@}{PredictedGnssAvailability=iidd}{CLRhythmicGnssStatusUpdate=iBi{bitset<2UL>=Q}BI}{CLRhythmicStreamingControl=B}{CLGNSSStateQueryAssertionReportData=ddd}{ProactiveLocationSessionStats=id}B{RecentLocationsRevised=ddd}{MapMatchingDriftSignal=iidddddid}{CLPIOSample=dddffffffffffffffffffffffCCCCCCS}{AnomalousGnssDetectionInfo=BBB}CC}20"
+ "v32@0:8@?<B@?@\"NSString\">16@?<v@?>24"
+ "v36@0:8@\"CLClientKeyPath\"16B24@?<v@?@\"NSString\">28"
+ "v36@0:8@16B24@?28"
+ "v36@0:8B16B20B24B28B32"
+ "v44@0:8@16B24@28@?36"
+ "void CLGpsGalSelector::onAirborneActivityChanged(bool)"
+ "void CLGpsGalSelector::onAirplaneModeChanged(bool)"
+ "void CLMovingApDetector::logGpsCellAndBadWifiCentroidDatabaseInfo(const std::unique_ptr<CLWifiLocationDatabase> &, CLDatabaseCountAnalytics &, const std::string &)"
+ "{\"msg%{public}.0s\":\"#AppMonitor bundleIds unchanged, skipping monitor reconfiguration\", \"bundleIds\":%{public}d}"
+ "{\"msg%{public}.0s\":\"#CoreLocationAgent ignoring a disconnection from a connection that does not hold the agent slot\", \"UserName\":%{public, location:escape_only}s, \"Connection\":%{public, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#CoreLocationAgent rejecting an unentitled connection\", \"Connection\":%{public, location:escape_only}s, \"PID\":%{public}d}"
+ "{\"msg%{public}.0s\":\"#CoreLocationAgent rejecting an unentitled sender on the agent MIG port\", \"PID\":%{public}d}"
+ "{\"msg%{public}.0s\":\"#Multiclient Setting maritime activity type\", \"state\":%{public}hhd}"
+ "{\"msg%{public}.0s\":\"#Multiclient toggling streaming\", \"state\":%{public}hhd, \"fitness\":%{public}hhd, \"airborne\":%{public}hhd, \"maritime\":%{public}hhd, \"emergency\":%{public}hhd}"
+ "{\"msg%{public}.0s\":\"#Pinning location changed, prompting for authorization\", \"previousLocation\":%{public, location:Encrypted_CLLocationCoordinate2D}.*P, \"newLocation\":%{public, location:Encrypted_CLLocationCoordinate2D}.*P}"
+ "{\"msg%{public}.0s\":\"#Quarantine marked quarantined over the internal SPI\", \"Client\":%{public, location:escape_only}@, \"Entity\":%{public, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#Quarantine refusing to quarantine a client we don't hold\", \"Client\":%{public, location:escape_only}@, \"Entity\":%{public, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#Quarantine unquarantine requested over the internal SPI\", \"Client\":%{public, location:escape_only}@, \"Entity\":%{public, location:escape_only}s, \"StillQuarantined\":%{public}hhd}"
+ "{\"msg%{public}.0s\":\"#monitor no accessible container for client; bailing out (nil ledger)\"}"
+ "{\"msg%{public}.0s\":\"DaemonIdentifiableClient #dic was created with a non-registered (possibly uninstalled) / quarantined CKP. Bailing out.\", \"connectingClient\":%{public, location:escape_only}@, \"unregisteredCkp\":%{public, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"Flush barrier reached\", \"fSimulationRunning\":%{public}hhd}"
+ "{\"msg%{public}.0s\":\"RBSLAT #AppMonitor CL-ARM first non-empty predicate supplied\", \"sinceMonitorCreatedMs\":%{public}d}"
+ "{\"msg%{public}.0s\":\"RBSLAT #AppMonitor CL-ARM monitor still has no predicate\", \"waitingMs\":%{public}d}"
+ "{\"msg%{public}.0s\":\"RBSLAT #AppMonitor CL-SUB no RBS state update since subscribe\", \"waitingMs\":%{public}d, \"pendingSubscribes\":%{public}d}"
+ "{\"msg%{public}.0s\":\"RBSLAT #AppMonitor QoS setting\", \"key\":%{public, location:escape_only}s, \"value\":%{public}d, \"qos\":%{public}d}"
+ "{\"msg%{public}.0s\":\"RBSLAT #AppMonitor subscribe qos\", \"phase\":%{public, location:escape_only}s, \"qos\":%{public}d, \"enqueueUs\":%{public}d, \"bundleIds\":%{public}d}"
+ "{\"msg%{public}.0s\":\"RBSLAT #AppMonitor subscribe sent\", \"phase\":%{public, location:escape_only}s, \"subscribeUs\":%{public}d}"
+ "{\"msg%{public}.0s\":\"Simulation running query\", \"fSimulationRunning\":%{public}hhd}"
+ "{\"msg%{public}.0s\":\"_CLDaemonClearLocationAuthorizationForLoctool\", \"event\":%{public, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"_CLDaemonCopyAuthorization\", \"event\":%{public, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"computing freshAuthorizationContext\", \"Client\":%{public, location:escape_only}@, \"BigSwitch\":%{public}hhd, \"InUseLevel\":%{public, location:CLClientInUseLevel}lld, \"StaticRegistration\":%{public, location:CLClientRegistrationResult}lld, \"TransientRegistration\":%{public, location:CLClientRegistrationResult}lld, \"EffectiveRegistration\":%{public, location:CLClientRegistrationResult}lld}"
+ "{\"msg%{public}.0s\":\"received daemon-side flush request\"}"
+ "{\"msg%{public}.0s\":\"received daemon-side isSimulationRunning request\"}"
+ "{CLStepCountEntry=dddIddddddIIdddi^{__CFString}BB{CLAccelerometerPace=ddd}IICII(FalseStepDetectorStateUnion={FalseStepDetectorState=b1b1b1b1b1b1b1b1}C)CCiII}24@0:8@16"
- "#Pinning Unsupported"
- "#Warning Attempt to call getAllEntries() without a backing database in CLWifiLocationDatabase!"
- "#Warning fGetAllEntriesQuery is not initialized in CLWifiLocationDatabase!"
- "#wci,ggselector,constructed,isWatch,%{public}d"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/include/boost/uuid/string_generator.hpp"
- "22:39:01"
- "@136@0:8{CLPIOSample=dddfffffffffffffffffffffCCCCCCS}16"
- "Assertion failed: lambda2 != 0, file /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/CoreLocation/Oscar/Math/CMOQuaternion.cpp, line 152,invalid weights."
- "Aug  8 2026"
- "Aug  8 2026 22:40:21"
- "AuthContext InUse:%d  RegResult:%d(%d) EffectiveMask:%d  ProvisionalMask:%d  DiagnosticMask:%d"
- "CLGpsGalSelector::CLGpsGalSelector(id<CLIntersiloUniverse>, bool)"
- "CLRS,CLTSP,unsupportedBatchInputSchemaVersion,decoded,%{public}lu,expected,%{public}lu"
- "promoteSystemServiceWithBundlePath:reply:"
- "std::vector<CLWifiLocationDatabaseEntry> CLWifiLocationDatabase::getAllEntries()"
- "toggleLocationUpdates:inFitnessSession:inAirborneSession:emergencyEnablementAssertionActive:"
- "v1732@0:8i16{NotificationData={CLDaemonLocation=i{?=dd}ddddddddidi{?=dd}diIiiidB}{CLDaemonLocationPrivate=dddddfffBi{?=dd}diiB{?=ddBBidqddd}{?={?=iddddd{?=dd}dd}iQiiiidB}{?=dd}if{?=dd}ddiBddddddddBB{?=dd}diddddddB{shared_ptr<const CLDaemonLocationPrivate::AboveHorizonSatelliteVisibilityReport>=^{AboveHorizonSatelliteVisibilityReport}^{__shared_weak_count}}i{AltitudeInfo=dddi}CdddCCBii{?=I}{?=if}iiiBffffd{?=dddffffff}}{shared_ptr<CLBatchedLocations>=^{CLBatchedLocations}^{__shared_weak_count}}{TechnologyStatus=iB}Bd{?=dddd}{?=dd}{XtraFileAvailable=d{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}}i{LocationDerivedSpeed=ddd}{?=dddi}{?=ddddddB[3[3d]]dddQi}i{?=idddddd[5d]ddddii}{CLStrongPtr<NSData *>=@}{PredictedGnssAvailability=iidd}{CLRhythmicGnssStatusUpdate=iBi{bitset<2UL>=Q}BI}{CLRhythmicStreamingControl=B}{CLGNSSStateQueryAssertionReportData=ddd}{ProactiveLocationSessionStats=id}B{RecentLocationsRevised=ddd}{MapMatchingDriftSignal=iidddddid}{CLPIOSample=dddfffffffffffffffffffffCCCCCCS}{AnomalousGnssDetectionInfo=BBB}CC}20"
- "v32@0:8B16B20B24B28"
- "void CLMovingApDetector::logGpsCellAndBadWifiCentroidDatabaseInfo(const std::unique_ptr<CLWifiLocationDatabase> &)"
- "{\"msg%{public}.0s\":\"#Multiclient toggling streaming\", \"state\":%{public}hhd, \"fitness\":%{public}hhd, \"airborne\":%{public}hhd, \"emergency\":%{public}hhd}"
- "{\"msg%{public}.0s\":\"computing freshAuthorizationContext\", \"Client\":%{public, location:escape_only}@, \"BigSwitch\":%{public}hhd, \"InUseLevel\":%{public, location:CLClientInUseLevel}lld}"
- "{CLStepCountEntry=dddIdddddIIdddi^{__CFString}BB{CLAccelerometerPace=ddd}IICII(FalseStepDetectorStateUnion={FalseStepDetectorState=b1b1b1b1b1b1b1b1}C)CCiII}24@0:8@16"
```
