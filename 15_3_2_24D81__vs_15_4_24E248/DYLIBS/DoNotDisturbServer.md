## DoNotDisturbServer

> `/System/Library/PrivateFrameworks/DoNotDisturbServer.framework/Versions/A/DoNotDisturbServer`

```diff

-433.4.2.0.0
-  __TEXT.__text: 0xcc600
-  __TEXT.__auth_stubs: 0x1160
-  __TEXT.__objc_methlist: 0x872c
+433.5.22.0.0
+  __TEXT.__text: 0xcc9c8
+  __TEXT.__auth_stubs: 0x1100
+  __TEXT.__objc_methlist: 0xa550
   __TEXT.__const: 0x418
-  __TEXT.__cstring: 0x8484
-  __TEXT.__oslogstring: 0xfa70
+  __TEXT.__cstring: 0x8374
+  __TEXT.__oslogstring: 0xfaa0
   __TEXT.__gcc_except_tab: 0xdc8
-  __TEXT.__swift5_typeref: 0x150
   __TEXT.__constg_swiftt: 0x14c
+  __TEXT.__swift5_typeref: 0x150
   __TEXT.__swift5_reflstr: 0xa6
   __TEXT.__swift5_fieldmd: 0xac
   __TEXT.__swift5_types: 0x10
   __TEXT.__swift5_capture: 0x120
   __TEXT.__swift5_proto: 0xc
-  __TEXT.__unwind_info: 0x26a0
-  __TEXT.__eh_frame: 0x538
-  __TEXT.__objc_classname: 0x2843
-  __TEXT.__objc_methname: 0x18ccc
-  __TEXT.__objc_methtype: 0x73a0
-  __TEXT.__objc_stubs: 0xfaa0
-  __DATA_CONST.__got: 0xda8
-  __DATA_CONST.__const: 0x9e0
+  __TEXT.__swift_as_entry: 0x2c
+  __TEXT.__swift_as_ret: 0x2c
+  __TEXT.__unwind_info: 0x26a8
+  __TEXT.__eh_frame: 0x540
+  __TEXT.__objc_classname: 0x2866
+  __TEXT.__objc_methname: 0x18db9
+  __TEXT.__objc_methtype: 0x73b9
+  __TEXT.__objc_stubs: 0xfbe0
+  __DATA_CONST.__got: 0xda0
+  __DATA_CONST.__const: 0xa08
   __DATA_CONST.__objc_classlist: 0x5e8
   __DATA_CONST.__objc_catlist: 0x138
-  __DATA_CONST.__objc_protolist: 0x3c0
+  __DATA_CONST.__objc_protolist: 0x3c8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4578
+  __DATA_CONST.__objc_selrefs: 0x4978
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x3d0
   __DATA_CONST.__objc_arraydata: 0x330
-  __AUTH_CONST.__auth_got: 0x8c0
+  __AUTH_CONST.__auth_got: 0x890
   __AUTH_CONST.__const: 0x2d50
-  __AUTH_CONST.__cfstring: 0x6de0
-  __AUTH_CONST.__objc_const: 0x28298
+  __AUTH_CONST.__cfstring: 0x6fe0
+  __AUTH_CONST.__objc_const: 0x24e28
   __AUTH_CONST.__objc_intobj: 0x2d0
   __AUTH_CONST.__objc_dictobj: 0x488
   __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH.__objc_data: 0x3cd0
   __AUTH.__data: 0x78
   __DATA.__objc_ivar: 0x9dc
-  __DATA.__data: 0x32a8
+  __DATA.__data: 0x3300
   __DATA.__bss: 0x3b0
   __DATA.__common: 0x1b0
   - /System/Library/Frameworks/ApplicationServices.framework/Versions/A/ApplicationServices

   - /System/Library/PrivateFrameworks/WorkflowUIServices.framework/Versions/A/WorkflowUIServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: BD62EBF1-7BA8-32C6-AF3D-F63971BDB5E7
-  Functions: 3692
-  Symbols:   10228
-  CStrings:  7207
+  UUID: C407D375-337B-3509-89AF-7954EF90B4F5
+  Functions: 3712
+  Symbols:   10278
+  CStrings:  7239
 
Symbols:
+ +[DNDContact(Contacts) keysToFetch].cold.1
+ +[DNDSAppInfoCache _fallbackAppInfoByBundleIdentifier].cold.1
+ +[DNDSClientDetailsProvider _defaultModuleDirectories].cold.1
+ +[DNDSContactProvider sharedContactStore].cold.1
+ +[DNDSKeybag sharedInstance].cold.1
+ +[DNDSReachability commonReachability].cold.1
+ +[DNDSSyncEngine sharedInstance].cold.1
+ +[DNDSWorkloop sharedDaemonWorkloop].cold.1
+ +[NSURL(BackingStores) dnds_globalConfigurationBackingStoreFileURL].cold.1
+ +[NSURL(BackingStores) dnds_idsSyncEngineMetadataFileURL].cold.1
+ +[NSURL(BackingStores) dnds_legacySettingsFileURL].cold.1
+ +[NSURL(BackingStores) dnds_localAssertionBackingStoreFileURL].cold.1
+ +[NSURL(BackingStores) dnds_locationAssertionExplicitRegionFileURL].cold.1
+ +[NSURL(BackingStores) dnds_locationAssertionUntilExitRegionFileURL].cold.1
+ +[NSURL(BackingStores) dnds_metricsBackingStoreFileURL].cold.1
+ +[NSURL(BackingStores) dnds_modeConfigurationsBackingStoreFileURL].cold.1
+ +[NSURL(BackingStores) dnds_modeConfigurationsSecureBackingStoreFileURL].cold.1
+ +[NSURL(BackingStores) dnds_placeholderModesLocalBackingStoreFileURL].cold.1
+ +[NSURL(BackingStores) dnds_rootDirectoryURL].cold.1
+ +[NSURL(BackingStores) dnds_settingsBackingStoreFileURL].cold.1
+ +[NSURL(BackingStores) dnds_syncEngineLastChanceFileURL].cold.1
+ +[NSURL(BackingStores) dnds_syncEngineMetadataFileURL].cold.1
+ -[DNDSExplicitRegionLocationLifetimeMonitor _updateWithCachedStateForRegions:]
+ -[DNDSExplicitRegionLocationLifetimeMonitor sysdiagnoseDataRedacted:]
+ -[DNDSLocationLifetimeMonitor sysdiagnoseDataForDate:redacted:]
+ -[DNDSLocationLifetimeMonitor sysdiagnoseDataIdentifier]
+ -[DNDSModeResolutionService _priorityForModeAssertion:].cold.1
+ -[DNDSUntilExitLocationLifetimeMonitor sysdiagnoseDataRedacted:]
+ DNDSRegisterLogging.cold.1
+ DNDSRunServer.cold.1
+ _DNDSSysdiagnoseDataProviders.cold.1
+ _DNDStringFromRegionState
+ __61-[DNDSSystemFocusConfigurationCoordinator handleStateUpdate:]_block_invoke.50
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_DNDSLocationSysdiagnoseContributor
+ __OBJC_$_PROTOCOL_METHOD_TYPES_DNDSLocationSysdiagnoseContributor
+ __OBJC_LABEL_PROTOCOL_$_DNDSLocationSysdiagnoseContributor
+ __OBJC_PROTOCOL_$_DNDSLocationSysdiagnoseContributor
+ ___63-[DNDSLocationLifetimeMonitor sysdiagnoseDataForDate:redacted:]_block_invoke
+ ___block_descriptor_33_e18_16?0"CLRegion"8l
+ ___swift_async_entry_functlets
+ ___swift_async_ret_functlets
+ __block_literal_global.378
+ __block_literal_global.395
+ __swift_FORCE_LOAD_$_swiftCompression
+ __swift_FORCE_LOAD_$_swiftCompression_$_DoNotDisturbServer
+ _objc_msgSend$_updateWithCachedStateForRegions:
+ _objc_msgSend$accuracyAuthorization
+ _objc_msgSend$authorizationStatus
+ _objc_msgSend$debugDescription
+ _objc_msgSend$isMonitoringAvailableForClass:
+ _objc_msgSend$locationServicesEnabled
+ _objc_msgSend$maximumRegionMonitoringDistance
+ _objc_msgSend$regionMonitoringAvailable
+ _objc_msgSend$requestStateForRegion:
+ _objc_msgSend$sysdiagnoseDataRedacted:
- __61-[DNDSSystemFocusConfigurationCoordinator handleStateUpdate:]_block_invoke.47
- __block_literal_global.308
- __block_literal_global.331
- _swift_arrayDestroy
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/DoNotDisturbServer/DoNotDisturbServer/DNDSGlobalConfigurationManager.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/DoNotDisturbServer/DoNotDisturbServer/DNDSLegacySettingsMigration.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/DoNotDisturbServer/DoNotDisturbServer/DNDSLocationLifetimeMonitor.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/DoNotDisturbServer/DoNotDisturbServer/DNDSMeDeviceService.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/DoNotDisturbServer/DoNotDisturbServer/DNDSModeAssertionManager.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/DoNotDisturbServer/DoNotDisturbServer/DNDSModeConfigurationManager.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/DoNotDisturbServer/DoNotDisturbServer/DNDSModernAssertionSyncManager.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/DoNotDisturbServer/DoNotDisturbServer/DNDSPlaceholderModeManager.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/DoNotDisturbServer/DoNotDisturbServer/DNDSSettingsManager.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/DoNotDisturbServer/DoNotDisturbServer/DNDSSyncEngine.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/DoNotDisturbServer/DoNotDisturbServer/Metrics/DNDSMetricsManager.m"
+ "<invalid(%ld)>"
+ "<read error>"
+ "<redacted>"
+ "@\"NSDictionary\"20@0:8B16"
+ "@16@?0@\"CLRegion\"8"
+ "Breakthrough %{public}@ allowed with reason: %@ for configuration %@ with event details: %@."
+ "Checked if event source is a contact: source=%{private}@, contact=%{BOOL}d"
+ "Checked if event source is a group contact: source=%{private}@, contact=%{BOOL}d"
+ "Checked if event source is a repeat: source=%{private}@, repeat=%{BOOL}d"
+ "Checked if event source is an emergency contact: source=%{private}@, emergencyContact=%{BOOL}d"
+ "Current DND state was calculated: state=%{private}@"
+ "DNDSLocationSysdiagnoseContributor"
+ "Generative models unavailable."
+ "Requesting cached state for region %{private}@."
+ "State was updated: currentState=%{private}@"
+ "State was updated: previousState=%{private}@"
+ "_updateWithCachedStateForRegions:"
+ "accuracyAuthorization"
+ "authorizationStatus"
+ "circularRegionMonitoringAvailable"
+ "enteredRegionIdentifiers"
+ "explicitRegion"
+ "isMonitoringAvailableForClass:"
+ "locationServicesEnabled"
+ "maximumRegionMonitoringDistance"
+ "regionMonitoringAvailable"
+ "requestStateForRegion:"
+ "stored"
+ "sysdiagnoseDataRedacted:"
+ "untilExit"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/DoNotDisturbServer/DoNotDisturbServer/DNDSGlobalConfigurationManager.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/DoNotDisturbServer/DoNotDisturbServer/DNDSLegacySettingsMigration.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/DoNotDisturbServer/DoNotDisturbServer/DNDSLocationLifetimeMonitor.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/DoNotDisturbServer/DoNotDisturbServer/DNDSMeDeviceService.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/DoNotDisturbServer/DoNotDisturbServer/DNDSModeAssertionManager.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/DoNotDisturbServer/DoNotDisturbServer/DNDSModeConfigurationManager.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/DoNotDisturbServer/DoNotDisturbServer/DNDSModernAssertionSyncManager.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/DoNotDisturbServer/DoNotDisturbServer/DNDSPlaceholderModeManager.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/DoNotDisturbServer/DoNotDisturbServer/DNDSSettingsManager.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/DoNotDisturbServer/DoNotDisturbServer/DNDSSyncEngine.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/DoNotDisturbServer/DoNotDisturbServer/Metrics/DNDSMetricsManager.m"
- "Breakthrough %{public}@ allowed for configuration %@ with event details: %@."
- "Checked if event source is a contact: source=%{public}@, contact=%{BOOL}d"
- "Checked if event source is a group contact: source=%{public}@, contact=%{BOOL}d"
- "Checked if event source is a repeat: source=%{public}@, repeat=%{BOOL}d"
- "Checked if event source is an emergency contact: source=%{public}@, emergencyContact=%{BOOL}d"
- "Current DND state was calculated: state=%{public}@"
- "Fatal error"
- "Generative models unavailable. Info: %s"
- "Insufficient space allocated to copy string contents"
- "State was updated: currentState=%{public}@"
- "State was updated: previousState=%{public}@"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "invalid Collection: less than 'count' elements in collection"

```
