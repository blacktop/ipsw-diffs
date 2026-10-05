## locationd

> `/usr/libexec/locationd`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_proto`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__auth_ptr`

```diff

-3186.0.17.0.1
-  __TEXT.__text: 0x1aedd44
-  __TEXT.__auth_stubs: 0x6550
-  __TEXT.__objc_stubs: 0x3e4c0
+3186.0.21.0.0
+  __TEXT.__text: 0x1af6148
+  __TEXT.__auth_stubs: 0x6580
+  __TEXT.__objc_stubs: 0x3e8a0
   __TEXT.__init_offsets: 0xc08
-  __TEXT.__objc_methlist: 0x2e700
-  __TEXT.__const: 0x166878
-  __TEXT.__gcc_except_tab: 0xda518
-  __TEXT.__oslogstring: 0x2924c5
-  __TEXT.__cstring: 0x210791
-  __TEXT.__objc_methname: 0x5d09f
-  __TEXT.__objc_classname: 0x8097
-  __TEXT.__objc_methtype: 0x39037
+  __TEXT.__objc_methlist: 0x2e9b8
+  __TEXT.__const: 0x166968
+  __TEXT.__gcc_except_tab: 0xdaafc
+  __TEXT.__oslogstring: 0x29356c
+  __TEXT.__cstring: 0x21129e
+  __TEXT.__objc_methname: 0x5d66f
+  __TEXT.__objc_classname: 0x812d
+  __TEXT.__objc_methtype: 0x39766
   __TEXT.__dlopen_cstrs: 0x4a
   __TEXT.__ustring: 0xa5e
   __TEXT.__constg_swiftt: 0x5ec

   __TEXT.__swift_as_cont: 0x1c
   __TEXT.__swift5_proto: 0x4c
   __TEXT.__swift5_assocty: 0x30
-  __TEXT.__unwind_info: 0x88fd0
+  __TEXT.__unwind_info: 0x892c0
   __TEXT.__eh_frame: 0xf38
-  __DATA_CONST.__const: 0xc1ba8
-  __DATA_CONST.__cfstring: 0x44460
-  __DATA_CONST.__objc_classlist: 0x14c0
+  __DATA_CONST.__const: 0xc1d38
+  __DATA_CONST.__cfstring: 0x444e0
+  __DATA_CONST.__objc_classlist: 0x14d0
   __DATA_CONST.__objc_catlist: 0xc8
-  __DATA_CONST.__objc_protolist: 0xe48
+  __DATA_CONST.__objc_protolist: 0xe60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0xad0
-  __DATA_CONST.__objc_superrefs: 0x1318
+  __DATA_CONST.__objc_protorefs: 0xae0
+  __DATA_CONST.__objc_superrefs: 0x1328
   __DATA_CONST.__objc_arraydata: 0x1bb0
   __DATA_CONST.__objc_dictobj: 0xb18
   __DATA_CONST.__objc_intobj: 0x2e68
-  __DATA_CONST.__objc_doubleobj: 0x150
+  __DATA_CONST.__objc_doubleobj: 0x160
   __DATA_CONST.__objc_arrayobj: 0x978
   __DATA_CONST.__objc_floatobj: 0x80
   __DATA_CONST.__linkguard: 0x15
-  __DATA_CONST.__auth_got: 0x32c8
-  __DATA_CONST.__got: 0x25e0
+  __DATA_CONST.__auth_got: 0x32e0
+  __DATA_CONST.__got: 0x25e8
   __DATA_CONST.__auth_ptr: 0x6a0
-  __DATA.__objc_const: 0x4f670
-  __DATA.__objc_selrefs: 0x13b98
-  __DATA.__objc_ivar: 0x3bf4
-  __DATA.__objc_data: 0xd528
-  __DATA.__data: 0x62f08
+  __DATA.__objc_const: 0x4fc10
+  __DATA.__objc_selrefs: 0x13c80
+  __DATA.__objc_ivar: 0x3c48
+  __DATA.__objc_data: 0xd5c8
+  __DATA.__data: 0x63038
   __DATA.__common: 0x22100
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 113489
-  Symbols:   2915
-  CStrings:  85216
+  Functions: 113631
+  Symbols:   2919
+  CStrings:  85400
 
Symbols:
+ __dispatch_source_type_memorypressure
+ _dispatch_source_get_data
+ _memorystatus_control
+ _proc_pid_rusage
CStrings:
+ "!fBackupExcludedDirectoryExists"
+ "#ClearLocationAuthorization"
+ "#Quarantine refusing to quarantine a client we don't hold"
+ "#Spi, Must provide a bundle ID or a bundle path to clear a location authorization"
+ "#Spi, both bundle-id and bundle-path are either zero-length or nil"
+ "-[CLInternalService clearLocationAuthorizationForLoctoolWithBundleId:orBundlePath:withReplyBlock:]"
+ "-[CLInternalService setClientQuarantined:forBundleID:orBundlePath:replyBlock:]"
+ "-[CLMemoryPressureService applyOutcome:reason:]"
+ "-[CLMemoryPressureService beginService]"
+ "-[CLMemoryPressureService handlePressureEvent]"
+ "-[CLMemoryPressureService readFootprint]"
+ "-[CLMemoryPressureService registerForUpdates:]"
+ "-[CLMemoryPressureService setupFootprintPoll]"
+ "-[CLMemoryPressureService setupPressureEvents]"
+ "-[CLRoutineMonitor addLocationWithConditionalBackfill:nowTimestamp:trySendLocationsNow:]"
+ "-[CLWorkoutRecorder onMemoryPressureStatusUpdate:]"
+ "-[CLWorkoutRecorderTrigger stopRecordingForExternalReason:]"
+ "-[CMAngleInterpolator _disarmTimer]"
+ "-[CMAngleInterpolator _timerDidFire]"
+ "-[CMAngleInterpolator initWithQueue:delegate:mechanicalAngle:]"
+ "-[CMAngleInterpolator interpolateToAngle:duration:]"
+ "-[CMAngleInterpolator interpolateToAngle:duration:]_block_invoke"
+ "-[CMAngleInterpolator setCurrentMechanicalAngleDegrees:]_block_invoke"
+ "-[CMAngleInterpolator stop]"
+ "-[CMDeviceStateRelayManager _newAngleHIDEventForAngle:gestureBeganContinuousTimestampTicks:]"
+ "-[CMDeviceStateRelayManager _snapToAngleUpdate:]"
+ "-[CMDeviceStateRelayManager startUpdatesForPhysicalDevice:aopAngle:]_block_invoke"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreLocation/Shared/Motion/DeviceState/CLDeviceStateRelay.mm"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreLocation/Shared/Motion/DeviceState/CMAngleInterpolator.mm"
+ "::CLP::LogEntry::PrivateData::OtaEphemerisCrossCheckToFile_IsValid(value)"
+ "<unknown>"
+ "@\"<CLMemoryPressureServiceProtocol>\""
+ "@\"<CMAngleInterpolatorDelegate>\""
+ "@\"CMAngleInterpolator\""
+ "@WifiLogic, entry, register, clientActivityType, %{public}s -> %{public}d"
+ "@WifiLogic, entry, register, clientActivityType, %{public}s, unchanged, %{public}d"
+ "@WifiLogic, entry, unregister, clientActivityType, %{public}s -> %{public}d"
+ "@WifiLogic, entry, unregister, clientActivityType, %{public}s, unchanged, %{public}d"
+ "Already at angle; skipping interpolation"
+ "BufferedGnssLeech"
+ "CL: _CLDaemonClearLocationAuthorizationForLoctool"
+ "CL: _CLDaemonSetClientQuarantined"
+ "CL: received cryptex notification - rebuilding system services as they might have changed!"
+ "CLClientManager.AppInstallationChange"
+ "CLMemoryPressureService"
+ "CLMemoryPressureServiceClientProtocol"
+ "CLMemoryPressureServiceProtocol"
+ "CLMemoryPressureServiceSilo"
+ "CLMotionTypeAngleEventPhase motionTypeAngleEventPhaseFromReportEventPhase(CMAngleReportEventPhase)"
+ "CLWifiLocationProvider unavailable; disabling wifi provider"
+ "CLWorkoutRecorder: Memory pressure relieved, recording allowed."
+ "CLWorkoutRecorder: Memory pressure, recording disallowed."
+ "CLWorkoutRecorder: Unable to start recording, memory pressure."
+ "CLWorkoutRecorderTrigger: stopping recording, %{public}s"
+ "CMAngleInterpolator"
+ "CMAngleInterpolator.mm"
+ "CMAngleInterpolatorDelegate"
+ "DeviceStateRelayInterpolationDuration"
+ "IOHIDEventPhaseBits IOHIDEventPhaseFromMotionTypeAngleEventPhase(CLMotionTypeAngleEventPhase)"
+ "Interpolation must have non-negative duration"
+ "MemoryPressure"
+ "MemoryPressure: %{public}s %{public}.3f outside [%{public}.3f, %{public}.3f], using %{public}.3f"
+ "MemoryPressure: %{public}s bad bounds [%{public}.3f, %{public}.3f], using fallback %{public}.3f"
+ "MemoryPressure: %{public}s, system %{public}s, process %{public}s, guidance %{public}s, footprint %{public}lld, peak %{public}llu, resident %{public}llu, wired %{public}llu, pageins %{public}llu, limit %{public}lld, fraction %{public}.3f, jetsamPriority %{public}d, jetsamState 0x%{public}x"
+ "MemoryPressure: GET_PRIORITY_LIST returned %{public}d bytes, errno %{public}d"
+ "MemoryPressure: degraded start, pressureEvents %{public}d, footprintPoll %{public}d"
+ "MemoryPressure: failed to create footprint poll timer"
+ "MemoryPressure: failed to create memorypressure source"
+ "MemoryPressure: memorypressure event, flags 0x%{public}lx"
+ "MemoryPressure: proc_pid_rusage failed, errno %{public}d"
+ "MemoryPressure: register outside of service lifetime, dropping"
+ "MemoryPressure: relief %{public}.3f not below critical %{public}.3f, using defaults"
+ "MemoryPressureCriticalFootprintFraction"
+ "MemoryPressureForcePolling"
+ "MemoryPressureMaxUnusablePolls"
+ "MemoryPressurePollIntervalSeconds"
+ "MemoryPressureReliefFootprintFraction"
+ "MusicHandoffScan"
+ "Must have manager"
+ "NSURL *applicationSupportDirectory()"
+ "Physical angle changed to %{public}f, timestamp=%{public}llu, isSimulated=%{public}d"
+ "Quarantined"
+ "Raven: EnableRavenReducedNearbyRoadSegmentsQuery,%{public}d"
+ "Skipping %ld empty epochs across gap, from,%lf,to,%lf,phaseCorrection,%lf"
+ "Skipping install check for system client: %{private}@."
+ "Snapping angle to: %f"
+ "T@\"<CMAngleInterpolatorDelegate>\",W,N,VfDelegate"
+ "T@\"CMAngleInterpolator\",&,V_interpolator"
+ "T@\"NSNumber\",&,N"
+ "T@\"NSNumber\",&,V_effectiveAngle"
+ "T@\"NSNumber\",&,V_interpolationDuration"
+ "T@\"NSNumber\",R,N"
+ "TB,N,V_isSystemClient"
+ "Unrecognized angle report event phase: %{public}u"
+ "Unrecognized phase: %{public}u"
+ "WorkoutRecorderMemoryPressureGating"
+ "[CLAngleNotifier] Unrecognized phase 0x%{public}x"
+ "[CLSPUAngleServiceControl] Giving up creating %{public}@ after %{public}u retries; the calibration estimate and repair state won't be saved"
+ "[CLSPUAngleServiceControl] Retrying creation of the backup excluded directory in %{public}.0f s (retry %{public}u of %{public}u)"
+ "[Interpolation] Angle=%f"
+ "[Interpolation] Client requested to stop interpolation"
+ "[Interpolation] Setting current mechanical angle to %{public}@"
+ "[Interpolation] Starting interpolation timer"
+ "[Interpolation] Starting interpolation to %{public}f with duration %{public}fs"
+ "[Interpolation] Stopping interpolation timer"
+ "^{__IOHIDEvent=}52@0:8{?=iiffffBB}16Q44"
+ "_disarmTimer"
+ "_effectiveAngle"
+ "_forcePolling"
+ "_interpolationDuration"
+ "_interpolator"
+ "_isOnQueue"
+ "_isSystemClient"
+ "_memoryPressureDiscouragesRecording"
+ "_memoryPressureGatingEnabled"
+ "_memoryPressureServiceProxy"
+ "_newAngleHIDEventForAngle:gestureBeganContinuousTimestampTicks:"
+ "_policy"
+ "_pollIntervalSeconds"
+ "_pollTimer"
+ "_polling"
+ "_pressureSource"
+ "_snapToAngleUpdate:"
+ "_timerDidFire"
+ "addLocationWithConditionalBackfill:nowTimestamp:trySendLocationsNow:"
+ "angleInterpolator:didProduceAngle:gestureBeganContinuousTimestampTicks:"
+ "applyOutcome:reason:"
+ "cacheDirectoryURL"
+ "clearLocationAuthorizationForLoctoolAtCkp:withReply:"
+ "clearLocationAuthorizationForLoctoolWithBundleId:orBundlePath:withReplyBlock:"
+ "com.apple.CoreMotion.DeviceStateRelay.EventQueue"
+ "com.apple.locationd.DeviceStateRelayPrefsChanged"
+ "const char *toString(CMAngleReportEventPhase)"
+ "critical"
+ "currentInterpolatedAngleDegrees"
+ "currentMechanicalAngleDegrees"
+ "discouraged"
+ "double validatedDefault(double, double, double, double, const char *)"
+ "duration >= 0"
+ "effectiveAngle"
+ "fCurrentInterpolatedAngleDegrees"
+ "fCurrentMechanicalAngleDegrees"
+ "fDelegate"
+ "fGestureBeganContinuousTimestampTicks"
+ "fSimulator"
+ "feedAOPAngleUpdate:"
+ "handlePollTimerFired"
+ "handlePressureEvent"
+ "initWithQueue:delegate:mechanicalAngle:"
+ "interpolateToAngle:duration:"
+ "interpolationDuration"
+ "interpolator"
+ "isSystemClient"
+ "memory pressure"
+ "onMemoryPressureStatusUpdate:"
+ "readFootprint"
+ "readPreferencesAndConfigure"
+ "received buffered locations with no batch"
+ "scheduleBackupExcludedDirectoryRetry"
+ "setClientQuarantined:forBundleID:orBundlePath:replyBlock:"
+ "setClientQuarantined:quarantined:entity:withReply:"
+ "setCurrentMechanicalAngleDegrees:"
+ "setEffectiveAngle:"
+ "setInterpolationDuration:"
+ "setInterpolator:"
+ "setIsSystemClient:"
+ "setPollingEnabled:"
+ "setSyncEnvironmentUUID:"
+ "set_ota_ephemeris_cross_check_to_file"
+ "setupFootprintPoll"
+ "setupPressureEvents"
+ "startUpdatesForPhysicalDevice:aopAngle:"
+ "stopRecordingForExternalReason:"
+ "syncEnvironmentUUID"
+ "unquarantineClient:"
+ "v104@0:8{Status=iii{Footprint={optional<unsigned long long>=(?=cQ)B}QQQQ{optional<unsigned long long>=(?=cQ)B}iI}}16"
+ "v24@0:8@?<{Status=iii{Footprint={optional<unsigned long long>=(?=cQ)B}QQQQ{optional<unsigned long long>=(?=cQ)B}iI}}@?>16"
+ "v24@0:8R@\"<CLMemoryPressureServiceClientProtocol>\"16"
+ "v28@0:8f16d20"
+ "v32@0:8@\"CLClientKeyPath\"16@?<v@?>24"
+ "v32@0:8r^v16r*24"
+ "v36@0:8@16r^{Timestamp=dddB}24B32"
+ "v44@0:8@\"CLClientKeyPath\"16B24@\"NSString\"28@?<v@?B>36"
+ "v44@0:8@16B24@28@?36"
+ "v60@0:8@\"CMAngleInterpolator\"16{?=iiffffBB}24Q52"
+ "v60@0:8@16{?=iiffffBB}24Q52"
+ "virtual void CLDeviceStateRelay::visitAngleGestureEnded(const CMAngleServiceReport::AngleGestureEnded &)"
+ "void CLSPUAngleServiceControl::readPreferencesAndConfigureInternal(IsUserTriggered)"
+ "void CLSPUAngleServiceControl::scheduleBackupExcludedDirectoryRetry()"
+ "void writeDictionaryToURL(NSDictionary *, NSURL *)"
+ "warn"
+ "writePendingDataToDisk"
+ "{\"msg%{public}.0s\":\"#ClearLocationAuthorization nothing to remove\", \"Client\":%{public, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#ClearLocationAuthorization removed the client and started a new sync environment\", \"Client\":%{public, location:escape_only}@, \"syncEnvironmentUUID\":%{public, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#Quarantine marked quarantined over the internal SPI\", \"Client\":%{public, location:escape_only}@, \"Entity\":%{public, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#Quarantine refusing to quarantine a client we don't hold\", \"Client\":%{public, location:escape_only}@, \"Entity\":%{public, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#Quarantine unquarantine requested over the internal SPI\", \"Client\":%{public, location:escape_only}@, \"Entity\":%{public, location:escape_only}s, \"StillQuarantined\":%{public}hhd}"
+ "{\"msg%{public}.0s\":\"AppMonitor - application (un)installation notification\", \"notification\":%{public, location:escape_only}s, \"BundleId\":%{public, location:escape_only}s, \"BundlePath\":%{public, location:escape_only}s, \"ExecutablePath\":%{public, location:escape_only}s, \"registeredCkp\":%{public, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"Interpolation must have non-negative duration\", \"event\":%{public, location:escape_only}s, \"condition\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"Must have manager\", \"event\":%{public, location:escape_only}s, \"condition\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"_CLDaemonClearLocationAuthorizationForLoctool\", \"event\":%{public, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"_CLDaemonSetClientQuarantined\", \"event\":%{public, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"marking client quarantined because the app was uninstalled\", \"Client\":%{public, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"received cryptex notification - rebuilding system services as they might have changed!\", \"event\":%{public, location:escape_only}s}"
+ "{CLStrongPtr<NSNumber *>=\"fObjc\"@\"NSNumber\"}"
+ "{CMAngleSimulator=\"fStartAngleDegrees\"f\"fEndAngleDegrees\"f\"fDurationMicroseconds\"Q\"fDelayMicroseconds\"Q\"fOptions\"{OptionSet<CMAngleSimulatorOptions>=\"fStorage\"S}\"fStartTime\"Q\"fEndTime\"Q\"fCurrentAngle\"f\"fHasCurrentAngle\"B\"fStatus\"C\"fPerceptionFilter\"{CMAnglePerceptionFilter=\"fFilteredRotationRate\"{FirstOrderFilter<float>=\"fNumSamples\"i\"fAlpha\"f\"fFiltered\"f\"fDoWarmStart\"B}\"fFilteredAngle\"{FirstOrderFilter<float>=\"fNumSamples\"i\"fAlpha\"f\"fFiltered\"f\"fDoWarmStart\"B}\"fLatchAngleFilter\"{FirstOrderFilter<float>=\"fNumSamples\"i\"fAlpha\"f\"fFiltered\"f\"fDoWarmStart\"B}\"fStableAngle\"f\"fNormalizedAngle\"f\"fEventPhase\"S\"fIsAngleValid\"B\"fIsAngleStablePrevious\"B\"fProgressState\"C\"fProgress\"f\"fClosedBoundary\"f\"fOpenBoundary\"f\"fHESClosedConfirmed\"B\"fExceededClosedMax\"B}}"
+ "{Footprint={optional<unsigned long long>=(?=cQ)B}QQQQ{optional<unsigned long long>=(?=cQ)B}iI}16@0:8"
+ "{OSObjectPtr<NSObject<OS_dispatch_queue> *>=\"fPtr\"@\"NSObject<OS_dispatch_queue>\"}"
+ "{OSObjectPtr<NSObject<OS_dispatch_source> *>=\"fPtr\"@\"NSObject<OS_dispatch_source>\"}"
+ "{Status=iii{Footprint={optional<unsigned long long>=(?=cQ)B}QQQQ{optional<unsigned long long>=(?=cQ)B}iI}}8@?0"
+ "{unique_ptr<CLMemoryPressurePolicy, std::default_delete<CLMemoryPressurePolicy>>=\"\"{?=\"__ptr_\"^{CLMemoryPressurePolicy}}}"
+ "\xf0q"
- "-[CLRoutineMonitor addLocationWithConditionalBackfill:nowTimestamp:]"
- "-[CMDeviceStateManager queryDeviceStateBlocking]"
- "-[CMDeviceStateManager queryDeviceStateWithHandler:]"
- "-[CMDeviceStateRelayManager _newAngleHIDEventForAngle:]"
- "-[CMDeviceStateRelayManager startUpdatesForPhysicalDevice:]_block_invoke"
- "@WifiLogic, #warning, airborne register fired but no airborne clients found"
- "@WifiLogic, entry, register, clientActivityType, airborne"
- "@WifiLogic, entry, register, clientActivityType, maritime"
- "@WifiLogic, entry, unregister, clientActivityType, airborne"
- "@WifiLogic, entry, unregister, clientActivityType, maritime"
- "NSURL *backupExcludedDirectory()"
- "Skipping %ld empty epochs across gap, from,%lf,to,%lf"
- "T@\"NSNumber\",&,V_angle"
- "[CLSPUAngleServiceControl] Failed to write calibration cache: %{public}@"
- "^{__IOHIDEvent=}20@0:8f16"
- "_angle"
- "_dispatchAngleEventIfAvailable"
- "_dispatchVirtualEventsIfReady"
- "_newAngleHIDEventForAngle:"
- "dispatchVirtualEventsIfReady"
- "queryDeviceStateBlocking"
- "queryDeviceStateBlocking is unsupported and should not be used."
- "queryDeviceStateWithHandler is unsupported and should not be used."
- "queryDeviceStateWithHandler:"
- "setAngle:"
- "startUpdatesForPhysicalDevice:"
- "void CLSPUAngleServiceControl::readPreferencesAndConfigure(IsUserTriggered)"
- "{\"msg%{public}.0s\":\"AppMonitor - application (un)installation notification\", \"notification\":%{public, location:escape_only}s, \"BundleId\":%{public, location:escape_only}s, \"BundlePath\":%{public, location:escape_only}s, \"ExecutablePath\":%{public, location:escape_only}s}"
```
