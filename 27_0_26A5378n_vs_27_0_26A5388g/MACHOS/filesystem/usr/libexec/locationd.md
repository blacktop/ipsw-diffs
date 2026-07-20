## locationd

> `/usr/libexec/locationd`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__objc_classname`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_assocty`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_ivar`
- `__DATA.__bss`

```diff

-3176.0.0.0.0
-  __TEXT.__text: 0x67a550
-  __TEXT.__auth_stubs: 0x38e0
-  __TEXT.__objc_stubs: 0x10d40
+3183.0.0.0.0
+  __TEXT.__text: 0x67e2e0
+  __TEXT.__auth_stubs: 0x38f0
+  __TEXT.__objc_stubs: 0x10dc0
   __TEXT.__init_offsets: 0x184
-  __TEXT.__objc_methlist: 0x129d8
-  __TEXT.__const: 0x17698
-  __TEXT.__gcc_except_tab: 0x2a858
-  __TEXT.__cstring: 0x7a9f2
-  __TEXT.__oslogstring: 0x974f0
-  __TEXT.__objc_methname: 0x1fa7e
+  __TEXT.__objc_methlist: 0x12a38
+  __TEXT.__const: 0x17908
+  __TEXT.__gcc_except_tab: 0x2a918
+  __TEXT.__cstring: 0x7ac36
+  __TEXT.__oslogstring: 0x97c66
+  __TEXT.__objc_methname: 0x1fcce
   __TEXT.__objc_classname: 0x33f4
-  __TEXT.__objc_methtype: 0xef8c
+  __TEXT.__objc_methtype: 0xf15c
   __TEXT.__ustring: 0x346
-  __TEXT.__constg_swiftt: 0x41c
-  __TEXT.__swift5_typeref: 0x22d
+  __TEXT.__constg_swiftt: 0x424
+  __TEXT.__swift5_typeref: 0x241
   __TEXT.__swift5_reflstr: 0x19c
   __TEXT.__swift5_fieldmd: 0x244
-  __TEXT.__swift5_capture: 0x80
+  __TEXT.__swift5_capture: 0xbc
   __TEXT.__swift5_types: 0x34
-  __TEXT.__swift_as_entry: 0x14
-  __TEXT.__swift_as_ret: 0x14
-  __TEXT.__swift_as_cont: 0xc
+  __TEXT.__swift_as_entry: 0x1c
+  __TEXT.__swift_as_ret: 0x18
+  __TEXT.__swift_as_cont: 0x10
   __TEXT.__swift5_proto: 0x4c
   __TEXT.__swift5_assocty: 0x30
-  __TEXT.__unwind_info: 0x1aa30
-  __TEXT.__eh_frame: 0x590
-  __DATA_CONST.__const: 0x2bbf0
-  __DATA_CONST.__cfstring: 0x15d00
+  __TEXT.__unwind_info: 0x1abb8
+  __TEXT.__eh_frame: 0x620
+  __DATA_CONST.__const: 0x2c058
+  __DATA_CONST.__cfstring: 0x15d40
   __DATA_CONST.__objc_classlist: 0x8d0
   __DATA_CONST.__objc_catlist: 0x78
   __DATA_CONST.__objc_protolist: 0x5b0

   __DATA_CONST.__objc_arrayobj: 0x138
   __DATA_CONST.__objc_floatobj: 0x10
   __DATA_CONST.__linkguard: 0x15
-  __DATA_CONST.__auth_got: 0x1c90
+  __DATA_CONST.__auth_got: 0x1c98
   __DATA_CONST.__got: 0xc00
   __DATA_CONST.__auth_ptr: 0x2d0
-  __DATA.__objc_const: 0x1eae0
-  __DATA.__objc_selrefs: 0x77d0
+  __DATA.__objc_const: 0x1eb00
+  __DATA.__objc_selrefs: 0x7808
   __DATA.__objc_ivar: 0x1290
-  __DATA.__objc_data: 0x5b90
-  __DATA.__data: 0x56e0
+  __DATA.__objc_data: 0x5b98
+  __DATA.__data: 0x56e8
   __DATA.__common: 0x7e8
   __DATA.__bss: 0x2c50
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 27019
-  Symbols:   1390
-  CStrings:  24810
+  Functions: 27069
+  Symbols:   1391
+  CStrings:  24848
 
Symbols:
+ _$sSo13os_log_type_ta0A0E5errorABvgZ
CStrings:
+ "#Error,CLSE,getSignalEnvironment,file exists but could not be opened,%{public}s,potential file corruption"
+ "#Spi, Must provide a bundle path to promote a system service"
+ "#Spi,CLSimulation,setSimulationEnabled,%{public}d"
+ "#Warning,CLSE,getSignalEnvironment,file version,%u,does not match expected,%u,redownload"
+ "#WirelessClientInfo: type downgraded from %{public}d to %{public}d based on hAcc=%{public}.1f"
+ "#wci setting (%{sensitive}.7f,%{sensitive}.7f) acc %{public}.2f"
+ "#wci,ggselector,disabling restricted mode,reason,%{public}s,wifiAvailability,%{public}s,observedWifiIntervalSec,%{public}.1f,adaptiveThresholdSec,%{public}.1f,currentGapSec,%{public}.1f,isDriving,%{public}d,isDenseUrban,%{public}d,urban,%{public}d,graceActive,%{public}d,activeDurationSec,%{public}.1f,gnssActive,%{public}d"
+ "#wci,ggselector,enabling restricted mode,reason,%{public}s,wifiAvailability,%{public}s,observedWifiIntervalSec,%{public}.1f,adaptiveThresholdSec,%{public}.1f,currentGapSec,%{public}.1f,isDriving,%{public}d,isDenseUrban,%{public}d,urban,%{public}d,graceActive,%{public}d,gnssActive,%{public}d"
+ "#wci,ggselector,persisting GPS+GAL,observedWifiIntervalSec,%{public}.1f,releaseThresholdSec,%{public}.1f,currentGapSec,%{public}.1f,isDriving,%{public}d,wifiAvailability,%{public}s"
+ "#wci,ggselector,reconcile,wifiAvailability,%{public}s,observedWifiIntervalSec,%{public}.1f,adaptiveThresholdSec,%{public}.1f,currentGapSec,%{public}.1f,isDenseUrban,%{public}d,isDriving,%{public}d,urban,%{public}d,graceActive,%{public}d,wifiRadioOff,%{public}d,restricted,%{public}d"
+ "#wci,ggselector,session engaged,isDriving,%{public}d,observedWifiIntervalSec,%{public}.1f,wifiAvailability,%{public}s"
+ "#wci,ggselector,simulator for region mode set"
+ "#wci,ggselector,workout sustained mode reset,observedWifiIntervalSec,%{public}.1f,thresholdSec,%{public}.1f"
+ "#wci,ggselector,workout sustained mode started,observedWifiIntervalSec,%{public}.1f,releaseThresholdSec,%{public}.1f,requiredSec,%{public}.1f"
+ "#wci,ggselector,workout sustained mode,sustainedSec,%{public}.1f,requiredSec,%{public}.1f,ready,%{public}d"
+ "+[CLMapsXPCServiceManager sharedInstance]_block_invoke"
+ "-[CLInternalService promoteSystemServiceWithBundlePath:replyBlock:]"
+ "-[CLLocationControllerAdapter setSimulationEnabled:]"
+ "-[CLMapsXPCServiceManager collectMapDataOfType:aroundCoordinate:inRadius:allowNetwork:preferCachedTiles:isPedestrianOrCycling:clearTiles:callSynchronously:includeRoadNames:WithReply:]_block_invoke"
+ "-[CLMapsXPCServiceManager findTunnelEndPointFromLocation:roadID:clRoadID:projection:snapCourse:maxIterations:allowNetwork:preferCachedTiles:clearTiles:callSynchronously:withReply:]_block_invoke"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Daemon/Core/Awareness/CLLocationAwarenessProvider.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Daemon/Core/CSI/CLMachThreadSupport.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Daemon/Core/ClientManagement/CLClientManager_OSX.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Daemon/Core/ClientManagement/CLClientManager_OSX.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Daemon/Core/ClientManagement/CLClientManager_Type.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Daemon/Core/ClientManagement/CLClientManager_Unified.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Daemon/Core/ClientManagement/CLCorrectiveCompensatedLocationProvider.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Daemon/Core/ClientManagement/CLDaemonClient_OSX.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Daemon/Core/ClientManagement/CLDaemonCore_OSX.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Daemon/Core/ClientManagement/CLFilteredLocationController.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Daemon/Core/ClientManagement/CLInUseLevelTracker.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Daemon/Core/ClientManagement/CLInternalService.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Daemon/Core/ClientManagement/CLPersistentSubscription.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Daemon/Core/ClientManagement/CLPersistentSubscription.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Daemon/Core/ClientManagement/DaemonIdentifiableClients/CLDaemonBeaconIdentityCondition.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Daemon/Core/ClientManagement/DaemonIdentifiableClients/CLDaemonConditionLedger.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Daemon/Core/ClientManagement/DaemonIdentifiableClients/CLDaemonIdentifiableClient.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Daemon/Core/ClientManagement/DaemonIdentifiableClients/CLDaemonLocationUpdaterHistorical.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Daemon/Core/ClientManagement/DaemonIdentifiableClients/CLDaemonLocationUpdaterLive.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Daemon/Core/ClientManagement/DaemonIdentifiableClients/CLDaemonMonitor.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Daemon/Core/ClientManagement/DaemonIdentifiableClients/CLDaemonMonitoringRecord.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Daemon/Core/ClientManagement/Subscriptions/CLLocationSubscription.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Daemon/Core/CountryTracker/CLGeoIPCountryTracker.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Daemon/Core/Fence/CLBTLEFenceManager.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Daemon/Core/Fence/CLBTLERangeManager.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Daemon/Core/Fence/CLBeaconFenceAuthorizationManager.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Daemon/Core/Fence/CLFenceAuthorizationManager.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Daemon/Core/Fence/CLFenceManager.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Daemon/Core/Fence/CLFenceMonitor.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Daemon/Core/Fence/CLFenceMonitorLogic.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Daemon/Core/Fence/CLSignificantChangeManager.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Daemon/Core/StatusBarIcon/CLStatusBarIconManager_OSX.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Daemon/Core/Utilities/CLPolygonDatabase_OSX.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Daemon/Motion/GyroBiasEstimator/CLGyroBiasEstimator.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Daemon/Motion/GyroBiasEstimator/CLGyroBiasFitter.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Daemon/Motion/GyroBiasEstimator/CLGyroBiasFitter.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Daemon/Motion/GyroBiasEstimator/CLNonlinearGyroBiasFitter.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Daemon/Motion/Utilities/CLMotionCoprocessor.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Daemon/Positioning/Accessory/CLAccessoryLocationProvider.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Daemon/Positioning/Autopause/CLAutopauseProvider.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Daemon/Positioning/BTLEBeaconProvider/CLBTLEBeaconProvider.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Daemon/Positioning/BTLEBeaconProvider/CLBTLEBeaconProviderMock.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Daemon/Positioning/GPS/Core/CLGpsAssistant.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Daemon/Positioning/Network/CLNetworkLocationProvider_OSX.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Daemon/Positioning/Network/CLNetworkLocationRequester_OSX.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Daemon/Positioning/Network/CLWifiLocationDatabase.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Daemon/Positioning/Network/CLWifiTileBlobsTable.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Daemon/Positioning/Network/CLWifiTileHeaderDatabase.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Daemon/Positioning/SignalEnvironment/CLSignalEnvironmentProvider.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Daemon/Positioning/Tiles/CLEntryCache.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Daemon/Positioning/Tiles/CLTilesManager_OSX.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Daemon/Positioning/Tiles/CLTilesSetGlobalProperties.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Daemon/Positioning/Tiles/CLWifiTileFile.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Daemon/Positioning/Tiles/CLWifiTileParser.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Daemon/Positioning/Tiles/_CLWifiTileMetadataFetchTool.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Daemon/Positioning/Utilities/CLBatchedLocations.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Daemon/Positioning/Utilities/CLCell.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Daemon/Positioning/Utilities/CLKalmanFilter.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Daemon/Positioning/Utilities/CLLocationCalculator.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Daemon/Positioning/Utilities/CLManagedLocationDatabase.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Daemon/Positioning/Wifi1/CLWifiAccessPointLocationService.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Daemon/Positioning/Wifi1/CLWifiLocationProvider_OSX.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Daemon/Positioning/Wifi1/CLWifiTileCacheLogic.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Daemon/Shared/AppMonitor/CLAppMonitor.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Daemon/Shared/BacklightState/CLBacklightStateNotifier.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Daemon/Shared/BluetoothService/CLBluetoothService.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Daemon/Shared/Context/CLMotionState.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Daemon/Shared/DaemonStatus/CLDaemonStatus.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Daemon/Shared/DarwinNotifier/CLDarwinNotifier_OSX.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Daemon/Shared/DataProtectionManager/CLDataProtectionManager.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Daemon/Shared/Harvester/Collection/CLHLocationClassifier.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Daemon/Shared/Harvester/Collection/CLHNetworkController.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Daemon/Shared/Harvester/Collection/CLHRequestStore.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Daemon/Shared/Harvester/Common/CLHarvestRule.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Daemon/Shared/Harvester/Controller/CLHarvestController.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Daemon/Shared/Harvester/Controller/CLHarvestControllerExternal.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Daemon/Shared/Harvester/Policies/Proactive/CLPolicyProactive.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Daemon/Shared/Harvester/Service/CLHarvesterService.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Daemon/Shared/LocationController/CLLocationController.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Daemon/Shared/ProxPDPAndALSPhone/CLProxPDPAndALSPhoneNotifier.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Daemon/Shared/Simulation/CLSimulatedLocationProvider.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Daemon/Shared/TelephonyService/CLTelephonyService.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Daemon/Shared/TimeManager/CLTimeManager.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Daemon/Shared/Utilities/CLNotifierClientAdapter.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Daemon/Shared/Utilities/CLNotifierServiceAdapter.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Daemon/Shared/Utilities/CLPersistentDictionary.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Daemon/Shared/Utilities/CLPersistentStore_OSX.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Daemon/Shared/Utilities/CLPreferences.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Daemon/Shared/Utilities/CLRunningBufferStats_OSX.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Daemon/Shared/Utilities/CLSqliteDatabase.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Daemon/Shared/Utilities/CLSqliteDatabaseManager.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Daemon/Shared/Utilities/CLSqliteTransaction.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Daemon/Shared/WifiService/CLWifiServiceClient.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Daemon/Shared/WifiService/CLWifiService_OSX.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Framework/CoreLocation/CLConditionLedger.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Framework/MotionSensorLogging/MSLWriterManager.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Shared/Intersilo/CLCppContainer.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Shared/Logging/CLBinaryLog.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Shared/Motion/CLMotionCore.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Shared/Motion/DeviceMotion/CLSensorCalibrationStaticDetector.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Shared/Motion/DeviceMotion/CLSensorFusionServiceSPU.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Shared/Motion/Eclipse/CLSPUEclipseInterface.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Shared/Motion/IO/CLIoHidFastPathDevice.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Shared/Motion/IO/CLIoHidInterface.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Shared/Motion/IO/CLIoHidUtils.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Shared/Motion/IO/CLSPUHIDDriverInterface.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Shared/Motion/Notifiers/CLDeviceMotion.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Shared/Motion/SensorCalibration/CLGyroCalibrationDatabase.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Shared/Motion/SensorCalibration/CLGyroCalibrationDatabaseLocalMultiRun.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Shared/Motion/SensorCalibration/CLGyroCalibrationDatabaseLocalNonlinear.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Shared/Motion/SensorCalibration/CLGyroCalibrationDatabaseLocalShared.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Shared/Motion/SensorCalibration/CLSensorCalibrationController.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Shared/Utilities/CLClientManagerAuthorizationContext.mm"
+ "03:13:35"
+ "Assertion failed: !empty(), file /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Oscar/CMVectorBuffer.h, line 145,back() on empty buffer."
+ "Assertion failed: !empty(), file /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Oscar/CMVectorBuffer.h, line 210,variance() on empty buffer."
+ "Assertion failed: !empty(), file /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Oscar/CMVectorBuffer.h, line 93,mean() on empty buffer."
+ "Assertion failed: col < N, file /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Oscar/Math/CMFactoredMatrix.h, line 242,invalid col %zu > %zu."
+ "Assertion failed: col < N, file /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Oscar/Math/CMMatrix.h, line 73,invalid col %zu > %zu."
+ "Assertion failed: col < N, file /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Oscar/Math/CMMatrix.h, line 80,invalid col %zu > %zu."
+ "Assertion failed: col > row, file /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Oscar/Math/CMFactoredMatrix.h, line 243,invalid element %zu <= %zu."
+ "Assertion failed: i < N, file /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Oscar/Math/CMVector.h, line 299,invalid index %zu >= %zu."
+ "Assertion failed: i < N, file /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Oscar/Math/CMVector.h, line 305,invalid index %zu >= %zu."
+ "Assertion failed: i < fCapacity, file /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Oscar/CMQueue.h, line 233,i,%zu,capacity,%u."
+ "Assertion failed: i < size(), file /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Oscar/CMVectorBuffer.h, line 45,out of buffer range %zu."
+ "Assertion failed: lambda2 != 0, file /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Oscar/Math/CMOQuaternion.cpp, line 208,invalid weights."
+ "Assertion failed: ldx < M*N, file /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Oscar/Math/CMMatrix.h, line 86,invalid element %zu >= %zu."
+ "Assertion failed: row < M, file /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Oscar/Math/CMMatrix.h, line 72,invalid row %zu > %zu."
+ "Assertion failed: row < M, file /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Oscar/Math/CMMatrix.h, line 79,invalid row %zu > %zu."
+ "Assertion failed: row < N, file /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Oscar/Math/CMFactoredMatrix.h, line 196,invalid row %zu > %zu."
+ "B52@0:8@16B24B28B32B36B40^@44"
+ "CL: _CLDaemonPromoteSystemService"
+ "CLMM,CLTSP,CLMapHelperService XPCService asynchronous TEPA tunnel scan error,%{public}lld,domain,%{public}@,description,\"%{private}@\""
+ "CLMM,CLTSP,CLMapHelperService XPCService synchronous TEPA tunnel scan error,%{public}lld,domain,%{public}@,description,\"%{private}@\""
+ "CLMM,CLTSP,MapHelperService,XPCService returned findTunnelEndPoint,success,%{public}d,responseTime,%{public}.1lf,syncCall,%{public}d"
+ "CLSE,download request,url,%{public}s,storeTo,%{public}s,retryInterval,%{public}.1lf,corrupt,%{public}d"
+ "CLTSP,CLMM,MaphelperService,findTunnelEndPoint not supported on this platform"
+ "Failed to log gyro non factory cal because the number of samples (%zu) exceeds the max limit (%zu),imuIndex,%{public}u"
+ "Fence: fenceUpdate, %{private}s, bundle, %{private}s, type, %{private}-16s, loc, %{sensitive}12.7lf, %{sensitive}12.7lf, acc, %{public}4.0lf, distance, %{private}9.0lf, tech, %{private}4s%{private}s, trans, %{private}d, state, %{private}d, cont, %{private}d, fence, %{sensitive}12.8lf, %{sensitive}12.8lf, %{private}.1lf, %{private}.1lf, sCount, %{private}d, %{private}d, trig, %{private}d, %{private}d, sinceLastLoc, %{private}.1lf, events, 0x%{private}08x, status, %{private}-10s => %{private}-10s, settled state, %{private}s ==> %{private}s, cantShiftButNeedTo, %{private}d, sinceLastTransition, %{private}.1lf, significant, %d, loi, %d, wci, %{public}d, lastProximityStateTimestamp, %f, lastProximityState, %d, lastApproachingState, %d"
+ "GnssSimulatorModeForRegionWithMoreBds"
+ "Jul 11 2026"
+ "Jul 11 2026 03:15:03"
+ "LocationController,setting simulation to %{public}d for all location providers,isInternal,%{public}d"
+ "Nonlinear gyro database computed fit,imuIndex,%{public}u"
+ "Point gyro database prune, deleted %zu samples, %zu remain,imuIndex,%{public}u"
+ "collectMapDataOfType:aroundCoordinate:inRadius:allowNetwork:preferCachedTiles:isPedestrianOrCycling:clearTiles:callSynchronously:includeRoadNames:WithReply:"
+ "const Object_T *safeDecoder(CLCppContainer *, Callback) [Object_T = CLAppMonitor_Type::NotificationData, Callback = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Shared/Intersilo/CLCppContainer.h:228:46)]"
+ "const Object_T *safeDecoder(CLCppContainer *, Callback) [Object_T = CLAutopauseProvider_Type::NotificationData, Callback = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Shared/Intersilo/CLCppContainer.h:241:46)]"
+ "const Object_T *safeDecoder(CLCppContainer *, Callback) [Object_T = CLAutopauseProvider_Type::NotificationData, Callback = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Shared/Intersilo/CLCppContainer.h:250:46)]"
+ "const Object_T *safeDecoder(CLCppContainer *, Callback) [Object_T = CLBTLEBeaconProvider_Type::NotificationData, Callback = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Shared/Intersilo/CLCppContainer.h:228:46)]"
+ "const Object_T *safeDecoder(CLCppContainer *, Callback) [Object_T = CLBTLERangeManager_Type::NotificationData, Callback = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Shared/Intersilo/CLCppContainer.h:228:46)]"
+ "const Object_T *safeDecoder(CLCppContainer *, Callback) [Object_T = CLBacklightStateNotifier_Type::NotificationData, Callback = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Shared/Intersilo/CLCppContainer.h:228:46)]"
+ "const Object_T *safeDecoder(CLCppContainer *, Callback) [Object_T = CLBeaconFenceAuthorizationManager_Type::NotificationData, Callback = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Shared/Intersilo/CLCppContainer.h:228:46)]"
+ "const Object_T *safeDecoder(CLCppContainer *, Callback) [Object_T = CLBluetoothService_Type::NotificationData, Callback = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Shared/Intersilo/CLCppContainer.h:228:46)]"
+ "const Object_T *safeDecoder(CLCppContainer *, Callback) [Object_T = CLClientManager_Type::Name, Callback = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Shared/Intersilo/CLCppContainer.h:228:46)]"
+ "const Object_T *safeDecoder(CLCppContainer *, Callback) [Object_T = CLClientManager_Type::NotificationData, Callback = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Shared/Intersilo/CLCppContainer.h:228:46)]"
+ "const Object_T *safeDecoder(CLCppContainer *, Callback) [Object_T = CLClientManager_Type::RegInfo, Callback = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Shared/Intersilo/CLCppContainer.h:228:46)]"
+ "const Object_T *safeDecoder(CLCppContainer *, Callback) [Object_T = CLClientManager_Type::RegistrationIdentity, Callback = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Shared/Intersilo/CLCppContainer.h:228:46)]"
+ "const Object_T *safeDecoder(CLCppContainer *, Callback) [Object_T = CLDaemonStatus_Type::NotificationData, Callback = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Shared/Intersilo/CLCppContainer.h:228:46)]"
+ "const Object_T *safeDecoder(CLCppContainer *, Callback) [Object_T = CLDarwinNotifier_Type::NotificationData, Callback = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Shared/Intersilo/CLCppContainer.h:241:46)]"
+ "const Object_T *safeDecoder(CLCppContainer *, Callback) [Object_T = CLDarwinNotifier_Type::NotificationData, Callback = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Shared/Intersilo/CLCppContainer.h:250:46)]"
+ "const Object_T *safeDecoder(CLCppContainer *, Callback) [Object_T = CLDataProtectionManager_Type::NotificationData, Callback = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Shared/Intersilo/CLCppContainer.h:241:46)]"
+ "const Object_T *safeDecoder(CLCppContainer *, Callback) [Object_T = CLDataProtectionManager_Type::NotificationData, Callback = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Shared/Intersilo/CLCppContainer.h:250:46)]"
+ "const Object_T *safeDecoder(CLCppContainer *, Callback) [Object_T = CLFenceDataDownloadManager_Type::NotificationData, Callback = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Shared/Intersilo/CLCppContainer.h:228:46)]"
+ "const Object_T *safeDecoder(CLCppContainer *, Callback) [Object_T = CLFenceManager_Type::NotificationData, Callback = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Shared/Intersilo/CLCppContainer.h:228:46)]"
+ "const Object_T *safeDecoder(CLCppContainer *, Callback) [Object_T = CLFenceMonitor_Type::NotificationData, Callback = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Shared/Intersilo/CLCppContainer.h:228:46)]"
+ "const Object_T *safeDecoder(CLCppContainer *, Callback) [Object_T = CLGpsAssistant_Type::NotificationData, Callback = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Shared/Intersilo/CLCppContainer.h:241:46)]"
+ "const Object_T *safeDecoder(CLCppContainer *, Callback) [Object_T = CLGpsAssistant_Type::NotificationData, Callback = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Shared/Intersilo/CLCppContainer.h:250:46)]"
+ "const Object_T *safeDecoder(CLCppContainer *, Callback) [Object_T = CLGyroCalibrationDatabase_Type::NotificationData, Callback = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Shared/Intersilo/CLCppContainer.h:241:46)]"
+ "const Object_T *safeDecoder(CLCppContainer *, Callback) [Object_T = CLGyroCalibrationDatabase_Type::NotificationData, Callback = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Shared/Intersilo/CLCppContainer.h:250:46)]"
+ "const Object_T *safeDecoder(CLCppContainer *, Callback) [Object_T = CLLocationAwarenessProvider_Type::NotificationData, Callback = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Shared/Intersilo/CLCppContainer.h:228:46)]"
+ "const Object_T *safeDecoder(CLCppContainer *, Callback) [Object_T = CLLocationAwarenessProvider_Type::RegInfo, Callback = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Shared/Intersilo/CLCppContainer.h:228:46)]"
+ "const Object_T *safeDecoder(CLCppContainer *, Callback) [Object_T = CLLocationProvider_Type::NotificationData, Callback = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Shared/Intersilo/CLCppContainer.h:228:46)]"
+ "const Object_T *safeDecoder(CLCppContainer *, Callback) [Object_T = CLLocationProvider_Type::RegInfo, Callback = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Shared/Intersilo/CLCppContainer.h:228:46)]"
+ "const Object_T *safeDecoder(CLCppContainer *, Callback) [Object_T = CLMotionState_Type::NotificationData, Callback = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Shared/Intersilo/CLCppContainer.h:241:46)]"
+ "const Object_T *safeDecoder(CLCppContainer *, Callback) [Object_T = CLMotionState_Type::NotificationData, Callback = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Shared/Intersilo/CLCppContainer.h:250:46)]"
+ "const Object_T *safeDecoder(CLCppContainer *, Callback) [Object_T = CLNetworkLocationProvider_Type::NotificationData, Callback = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Shared/Intersilo/CLCppContainer.h:241:46)]"
+ "const Object_T *safeDecoder(CLCppContainer *, Callback) [Object_T = CLNetworkLocationProvider_Type::NotificationData, Callback = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Shared/Intersilo/CLCppContainer.h:250:46)]"
+ "const Object_T *safeDecoder(CLCppContainer *, Callback) [Object_T = CLProxPDPAndALSPhoneNotifier_Type::NotificationData, Callback = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Shared/Intersilo/CLCppContainer.h:241:46)]"
+ "const Object_T *safeDecoder(CLCppContainer *, Callback) [Object_T = CLProxPDPAndALSPhoneNotifier_Type::NotificationData, Callback = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Shared/Intersilo/CLCppContainer.h:250:46)]"
+ "const Object_T *safeDecoder(CLCppContainer *, Callback) [Object_T = CLSensorCalibrationController_Type::NotificationData, Callback = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Shared/Intersilo/CLCppContainer.h:241:46)]"
+ "const Object_T *safeDecoder(CLCppContainer *, Callback) [Object_T = CLSensorCalibrationController_Type::NotificationData, Callback = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Shared/Intersilo/CLCppContainer.h:250:46)]"
+ "const Object_T *safeDecoder(CLCppContainer *, Callback) [Object_T = CLSignalEnvironmentProvider_Type::NotificationData, Callback = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Shared/Intersilo/CLCppContainer.h:228:46)]"
+ "const Object_T *safeDecoder(CLCppContainer *, Callback) [Object_T = CLStatusBarIconManager_Type::NotificationData, Callback = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Shared/Intersilo/CLCppContainer.h:241:46)]"
+ "const Object_T *safeDecoder(CLCppContainer *, Callback) [Object_T = CLStatusBarIconManager_Type::NotificationData, Callback = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Shared/Intersilo/CLCppContainer.h:250:46)]"
+ "const Object_T *safeDecoder(CLCppContainer *, Callback) [Object_T = CLTelephonyService_Type::NotificationData, Callback = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Shared/Intersilo/CLCppContainer.h:228:46)]"
+ "const Object_T *safeDecoder(CLCppContainer *, Callback) [Object_T = CLTilesManager_Type::NotificationData, Callback = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Shared/Intersilo/CLCppContainer.h:228:46)]"
+ "const Object_T *safeDecoder(CLCppContainer *, Callback) [Object_T = CLTimeManager_Type::NotificationData, Callback = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Shared/Intersilo/CLCppContainer.h:241:46)]"
+ "const Object_T *safeDecoder(CLCppContainer *, Callback) [Object_T = CLTimeManager_Type::NotificationData, Callback = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Shared/Intersilo/CLCppContainer.h:250:46)]"
+ "const Object_T *safeDecoder(CLCppContainer *, Callback) [Object_T = CLWifiService_Type::NotificationData, Callback = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Shared/Intersilo/CLCppContainer.h:228:46)]"
+ "const Object_T *safeDecoder(CLCppContainer *, Callback) [Object_T = CLWifiService_Type::RegInfo, Callback = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Shared/Intersilo/CLCppContainer.h:228:46)]"
+ "const Object_T *safeDecoder(CLCppContainer *, Callback) [Object_T = char, Callback = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Shared/Intersilo/CLCppContainer.h:241:46)]"
+ "const Object_T *safeDecoder(CLCppContainer *, Callback) [Object_T = char, Callback = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Shared/Intersilo/CLCppContainer.h:250:46)]"
+ "const Object_T *safeDecoder(CLCppContainer *, Callback) [Object_T = std::list<CLBTLEBeaconRegion_Type::MonitoredRegion>, Callback = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Shared/Intersilo/CLCppContainer.h:228:46)]"
+ "deleteAdaptedNotifier"
+ "dense"
+ "entered dense urban — full GNSS mode"
+ "fetchGEOMapFeatureRoadDataAtIntersectionOf:allowNetwork:preferCachedTiles:isPedestrianOrCycling:clearTiles:useStartOfRoad:returnRoads:"
+ "fetchGEORoadDataAroundCoordinate:inRadius:allowNetwork:preferCachedTiles:isPedestrianOrCycling:clearTiles:includeRoadNames:withReply:"
+ "findTunnelEndPointFromLocation:roadID:clRoadID:projection:snapCourse:maxIterations:allowNetwork:preferCachedTiles:clearTiles:callSynchronously:withReply:"
+ "findTunnelEndPointFromLocation:roadID:clRoadID:projection:snapCourse:maxIterations:allowNetwork:preferCachedTiles:clearTiles:withReply:"
+ "gpsAltitudeUncertainty"
+ "https://cl3.apple.com/1/v3/"
+ "imuIndex"
+ "isQuarantinedClient:"
+ "makeIntersectionQueryCallUsingMapsAPIFor:allowNetwork:preferCachedTiles:isPedestrianOrCycling:clearTiles:useStartOfRoad:returnRoads:"
+ "moderate"
+ "promoteSystemServiceWithBundlePath:reply:"
+ "promoteSystemServiceWithBundlePath:replyBlock:"
+ "propertyA0"
+ "propertyA1"
+ "scanTunnelWalkingBackward:fromRoad:gmf:projection:snapCourse:maxIterations:allowNetwork:preferCachedTiles:"
+ "simulateManagementProviderChange called before AMF state was determined; ignoring"
+ "sparse"
+ "speedLimitMps"
+ "v68@0:8{CLLocationCoordinate2D=dd}16d32B40B44B48B52B56@?60"
+ "v68@0:8{CLLocationCoordinate2D=dd}16d32B40B44B48B52B56@?<v@?@\"NSArray\">60"
+ "v80@0:8q16{CLLocationCoordinate2D=dd}24d40B48B52B56B60B64B68@?72"
+ "v88@0:8{CLLocationCoordinate2D=dd}16Q32Q40d48d56i64B68B72B76@?80"
+ "v88@0:8{CLLocationCoordinate2D=dd}16Q32Q40d48d56i64B68B72B76@?<v@?@\"NSDictionary\">80"
+ "v92@0:8{CLLocationCoordinate2D=dd}16Q32Q40d48d56i64B68B72B76B80@?84"
+ "void CLGpsGalSelector::reset()"
+ "wifi dense enough to release"
+ "{\"msg%{public}.0s\":\"_CLDaemonPromoteSystemService\", \"event\":%{public, location:escape_only}s}"
+ "{CLOdometerEntry=dddddddddddiiiddddddddiiB{CLOdometerTrackProximityInfo=id}}24@0:8@16"
+ "{TunnelScanIterResult=BidddddB{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}}72@0:8B16{shared_ptr<CLMapRoad>=^{CLMapRoad}^{__shared_weak_count}}20@36d44d52i60B64B68"
- "#WirelessClientInfo: regulatory coords diverge from original fix (originalType=%{public}d, hAcc=%{public}.1f); substituting %{public}s"
- "#wci setting (%{sensitive}.3f,%{sensitive}.3f)"
- "#wci,ggselector,reconcile,disabling restricted mode,reason,%{public}s,policy,%{public}s,thldSec,%{public}.1f,gapSec,%{public}.1f,denseUrban,%{public}d,urban,%{public}d,graceActive,%{public}d,activeDurationSec,%{public}.1f,gnssActive,%{public}d"
- "#wci,ggselector,reconcile,enabling restricted mode,reason,%{public}s,policy,%{public}s,thldSec,%{public}.1f,gapSec,%{public}.1f,denseUrban,%{public}d,urban,%{public}d,graceActive,%{public}d,gnssActive,%{public}d"
- "#wci,ggselector,reconcile,policy,%{public}s,thldSec,%{public}.1f,gapSec,%{public}.1f,denseUrban,%{public}d,urban,%{public}d,graceActive,%{public}d,wifiRadioOff,%{public}d,restricted,%{public}d"
- "+[CLMapsXPCServiceManager sharedInstance]"
- "-[CLMapsXPCServiceManager collectMapDataOfType:aroundCoordinate:inRadius:allowNetwork:preferCachedTiles:isPedestrianOrCycling:clearTiles:callSynchronously:WithReply:]_block_invoke"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Daemon/Core/Awareness/CLLocationAwarenessProvider.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Daemon/Core/CSI/CLMachThreadSupport.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Daemon/Core/ClientManagement/CLClientManager_OSX.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Daemon/Core/ClientManagement/CLClientManager_OSX.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Daemon/Core/ClientManagement/CLClientManager_Type.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Daemon/Core/ClientManagement/CLClientManager_Unified.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Daemon/Core/ClientManagement/CLCorrectiveCompensatedLocationProvider.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Daemon/Core/ClientManagement/CLDaemonClient_OSX.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Daemon/Core/ClientManagement/CLDaemonCore_OSX.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Daemon/Core/ClientManagement/CLFilteredLocationController.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Daemon/Core/ClientManagement/CLInUseLevelTracker.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Daemon/Core/ClientManagement/CLInternalService.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Daemon/Core/ClientManagement/CLPersistentSubscription.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Daemon/Core/ClientManagement/CLPersistentSubscription.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Daemon/Core/ClientManagement/DaemonIdentifiableClients/CLDaemonBeaconIdentityCondition.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Daemon/Core/ClientManagement/DaemonIdentifiableClients/CLDaemonConditionLedger.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Daemon/Core/ClientManagement/DaemonIdentifiableClients/CLDaemonIdentifiableClient.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Daemon/Core/ClientManagement/DaemonIdentifiableClients/CLDaemonLocationUpdaterHistorical.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Daemon/Core/ClientManagement/DaemonIdentifiableClients/CLDaemonLocationUpdaterLive.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Daemon/Core/ClientManagement/DaemonIdentifiableClients/CLDaemonMonitor.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Daemon/Core/ClientManagement/DaemonIdentifiableClients/CLDaemonMonitoringRecord.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Daemon/Core/ClientManagement/Subscriptions/CLLocationSubscription.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Daemon/Core/CountryTracker/CLGeoIPCountryTracker.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Daemon/Core/Fence/CLBTLEFenceManager.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Daemon/Core/Fence/CLBTLERangeManager.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Daemon/Core/Fence/CLBeaconFenceAuthorizationManager.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Daemon/Core/Fence/CLFenceAuthorizationManager.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Daemon/Core/Fence/CLFenceManager.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Daemon/Core/Fence/CLFenceMonitor.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Daemon/Core/Fence/CLFenceMonitorLogic.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Daemon/Core/Fence/CLSignificantChangeManager.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Daemon/Core/StatusBarIcon/CLStatusBarIconManager_OSX.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Daemon/Core/Utilities/CLPolygonDatabase_OSX.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Daemon/Motion/GyroBiasEstimator/CLGyroBiasEstimator.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Daemon/Motion/GyroBiasEstimator/CLGyroBiasFitter.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Daemon/Motion/GyroBiasEstimator/CLGyroBiasFitter.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Daemon/Motion/GyroBiasEstimator/CLNonlinearGyroBiasFitter.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Daemon/Motion/Utilities/CLMotionCoprocessor.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Daemon/Positioning/Accessory/CLAccessoryLocationProvider.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Daemon/Positioning/Autopause/CLAutopauseProvider.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Daemon/Positioning/BTLEBeaconProvider/CLBTLEBeaconProvider.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Daemon/Positioning/BTLEBeaconProvider/CLBTLEBeaconProviderMock.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Daemon/Positioning/GPS/Core/CLGpsAssistant.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Daemon/Positioning/Network/CLNetworkLocationProvider_OSX.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Daemon/Positioning/Network/CLNetworkLocationRequester_OSX.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Daemon/Positioning/Network/CLWifiLocationDatabase.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Daemon/Positioning/Network/CLWifiTileBlobsTable.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Daemon/Positioning/Network/CLWifiTileHeaderDatabase.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Daemon/Positioning/SignalEnvironment/CLSignalEnvironmentProvider.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Daemon/Positioning/Tiles/CLEntryCache.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Daemon/Positioning/Tiles/CLTilesManager_OSX.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Daemon/Positioning/Tiles/CLTilesSetGlobalProperties.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Daemon/Positioning/Tiles/CLWifiTileFile.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Daemon/Positioning/Tiles/CLWifiTileParser.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Daemon/Positioning/Tiles/_CLWifiTileMetadataFetchTool.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Daemon/Positioning/Utilities/CLBatchedLocations.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Daemon/Positioning/Utilities/CLCell.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Daemon/Positioning/Utilities/CLKalmanFilter.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Daemon/Positioning/Utilities/CLLocationCalculator.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Daemon/Positioning/Utilities/CLManagedLocationDatabase.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Daemon/Positioning/Wifi1/CLWifiAccessPointLocationService.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Daemon/Positioning/Wifi1/CLWifiLocationProvider_OSX.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Daemon/Positioning/Wifi1/CLWifiTileCacheLogic.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Daemon/Shared/AppMonitor/CLAppMonitor.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Daemon/Shared/BacklightState/CLBacklightStateNotifier.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Daemon/Shared/BluetoothService/CLBluetoothService.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Daemon/Shared/Context/CLMotionState.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Daemon/Shared/DaemonStatus/CLDaemonStatus.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Daemon/Shared/DarwinNotifier/CLDarwinNotifier_OSX.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Daemon/Shared/DataProtectionManager/CLDataProtectionManager.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Daemon/Shared/Harvester/Collection/CLHLocationClassifier.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Daemon/Shared/Harvester/Collection/CLHNetworkController.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Daemon/Shared/Harvester/Collection/CLHRequestStore.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Daemon/Shared/Harvester/Common/CLHarvestRule.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Daemon/Shared/Harvester/Controller/CLHarvestController.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Daemon/Shared/Harvester/Controller/CLHarvestControllerExternal.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Daemon/Shared/Harvester/Policies/Proactive/CLPolicyProactive.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Daemon/Shared/Harvester/Service/CLHarvesterService.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Daemon/Shared/LocationController/CLLocationController.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Daemon/Shared/ProxPDPAndALSPhone/CLProxPDPAndALSPhoneNotifier.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Daemon/Shared/Simulation/CLSimulatedLocationProvider.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Daemon/Shared/TelephonyService/CLTelephonyService.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Daemon/Shared/TimeManager/CLTimeManager.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Daemon/Shared/Utilities/CLNotifierClientAdapter.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Daemon/Shared/Utilities/CLNotifierServiceAdapter.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Daemon/Shared/Utilities/CLPersistentDictionary.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Daemon/Shared/Utilities/CLPersistentStore_OSX.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Daemon/Shared/Utilities/CLPreferences.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Daemon/Shared/Utilities/CLRunningBufferStats_OSX.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Daemon/Shared/Utilities/CLSqliteDatabase.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Daemon/Shared/Utilities/CLSqliteDatabaseManager.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Daemon/Shared/Utilities/CLSqliteTransaction.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Daemon/Shared/WifiService/CLWifiServiceClient.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Daemon/Shared/WifiService/CLWifiService_OSX.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Framework/CoreLocation/CLConditionLedger.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Framework/MotionSensorLogging/MSLWriterManager.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Shared/Intersilo/CLCppContainer.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Shared/Logging/CLBinaryLog.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Shared/Motion/CLMotionCore.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Shared/Motion/DeviceMotion/CLSensorCalibrationStaticDetector.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Shared/Motion/DeviceMotion/CLSensorFusionServiceSPU.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Shared/Motion/Eclipse/CLSPUEclipseInterface.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Shared/Motion/IO/CLIoHidFastPathDevice.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Shared/Motion/IO/CLIoHidInterface.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Shared/Motion/IO/CLIoHidUtils.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Shared/Motion/IO/CLSPUHIDDriverInterface.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Shared/Motion/Notifiers/CLDeviceMotion.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Shared/Motion/SensorCalibration/CLGyroCalibrationDatabase.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Shared/Motion/SensorCalibration/CLGyroCalibrationDatabaseLocalMultiRun.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Shared/Motion/SensorCalibration/CLGyroCalibrationDatabaseLocalNonlinear.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Shared/Motion/SensorCalibration/CLGyroCalibrationDatabaseLocalShared.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Shared/Motion/SensorCalibration/CLSensorCalibrationController.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Shared/Utilities/CLClientManagerAuthorizationContext.mm"
- "23:04:10"
- "Assertion failed: !empty(), file /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Oscar/CMVectorBuffer.h, line 145,back() on empty buffer."
- "Assertion failed: !empty(), file /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Oscar/CMVectorBuffer.h, line 210,variance() on empty buffer."
- "Assertion failed: !empty(), file /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Oscar/CMVectorBuffer.h, line 93,mean() on empty buffer."
- "Assertion failed: col < N, file /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Oscar/Math/CMFactoredMatrix.h, line 242,invalid col %zu > %zu."
- "Assertion failed: col < N, file /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Oscar/Math/CMMatrix.h, line 81,invalid col %zu > %zu."
- "Assertion failed: col < N, file /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Oscar/Math/CMMatrix.h, line 88,invalid col %zu > %zu."
- "Assertion failed: col > row, file /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Oscar/Math/CMFactoredMatrix.h, line 243,invalid element %zu <= %zu."
- "Assertion failed: i < N, file /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Oscar/Math/CMVector.h, line 292,invalid index %zu >= %zu."
- "Assertion failed: i < N, file /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Oscar/Math/CMVector.h, line 298,invalid index %zu >= %zu."
- "Assertion failed: i < fCapacity, file /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Oscar/CMQueue.h, line 233,i,%zu,capacity,%u."
- "Assertion failed: i < size(), file /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Oscar/CMVectorBuffer.h, line 45,out of buffer range %zu."
- "Assertion failed: lambda2 != 0, file /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Oscar/Math/CMOQuaternion.cpp, line 208,invalid weights."
- "Assertion failed: ldx < M*N, file /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Oscar/Math/CMMatrix.h, line 94,invalid element %zu >= %zu."
- "Assertion failed: row < M, file /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Oscar/Math/CMMatrix.h, line 80,invalid row %zu > %zu."
- "Assertion failed: row < M, file /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Oscar/Math/CMMatrix.h, line 87,invalid row %zu > %zu."
- "Assertion failed: row < N, file /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Oscar/Math/CMFactoredMatrix.h, line 196,invalid row %zu > %zu."
- "B48@0:8@16B24B28B32B36^@40"
- "CLSE,download request,url,%{public}s,storeTo,%{public}s,retryInterval,%{public}.1lf"
- "CLSE,getSignalEnvironment,file version does not match expected"
- "Failed to log gyro non factory cal because the number of samples (%zu) exceeds the max limit (%zu)."
- "Fence: fenceUpdate, %{private}s, bundle, %{private}s, type, %{private}-16s, loc, %{sensitive}12.7lf, %{sensitive}12.7lf, acc, %{public}4.0lf, distance, %{private}9.0lf, tech, %{private}4s%{private}s, trans, %{private}d, state, %{private}d, cont, %{private}d, fence, %{sensitive}12.8lf, %{sensitive}12.8lf, %{private}.1lf, %{private}.1lf, sCount, %{private}d, %{private}d, trig, %{private}d, %{private}d, sinceLastLoc, %{private}.1lf, events, 0x%{private}08x, status, %{private}-10s => %{private}-10s, settled state, %{private}s ==> %{private}s, cantShiftButNeedTo, %{private}d, sinceLastTransition, %{private}.1lf, significant, %d, loi, %d, lastProximityStateTimestamp, %f, lastProximityState, %d, lastApproachingState, %d"
- "Jun 27 2026"
- "Jun 27 2026 23:05:50"
- "LocationController,setting simulation to %{public}d for all location providers"
- "Nonlinear gyro database computed fit."
- "Point gyro database prune, deleted %zu samples, %zu remain."
- "collectMapDataOfType:aroundCoordinate:inRadius:allowNetwork:preferCachedTiles:isPedestrianOrCycling:clearTiles:callSynchronously:WithReply:"
- "const Object_T *safeDecoder(CLCppContainer *, Callback) [Object_T = CLAppMonitor_Type::NotificationData, Callback = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Shared/Intersilo/CLCppContainer.h:228:46)]"
- "const Object_T *safeDecoder(CLCppContainer *, Callback) [Object_T = CLAutopauseProvider_Type::NotificationData, Callback = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Shared/Intersilo/CLCppContainer.h:241:46)]"
- "const Object_T *safeDecoder(CLCppContainer *, Callback) [Object_T = CLAutopauseProvider_Type::NotificationData, Callback = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Shared/Intersilo/CLCppContainer.h:250:46)]"
- "const Object_T *safeDecoder(CLCppContainer *, Callback) [Object_T = CLBTLEBeaconProvider_Type::NotificationData, Callback = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Shared/Intersilo/CLCppContainer.h:228:46)]"
- "const Object_T *safeDecoder(CLCppContainer *, Callback) [Object_T = CLBTLERangeManager_Type::NotificationData, Callback = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Shared/Intersilo/CLCppContainer.h:228:46)]"
- "const Object_T *safeDecoder(CLCppContainer *, Callback) [Object_T = CLBacklightStateNotifier_Type::NotificationData, Callback = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Shared/Intersilo/CLCppContainer.h:228:46)]"
- "const Object_T *safeDecoder(CLCppContainer *, Callback) [Object_T = CLBeaconFenceAuthorizationManager_Type::NotificationData, Callback = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Shared/Intersilo/CLCppContainer.h:228:46)]"
- "const Object_T *safeDecoder(CLCppContainer *, Callback) [Object_T = CLBluetoothService_Type::NotificationData, Callback = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Shared/Intersilo/CLCppContainer.h:228:46)]"
- "const Object_T *safeDecoder(CLCppContainer *, Callback) [Object_T = CLClientManager_Type::Name, Callback = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Shared/Intersilo/CLCppContainer.h:228:46)]"
- "const Object_T *safeDecoder(CLCppContainer *, Callback) [Object_T = CLClientManager_Type::NotificationData, Callback = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Shared/Intersilo/CLCppContainer.h:228:46)]"
- "const Object_T *safeDecoder(CLCppContainer *, Callback) [Object_T = CLClientManager_Type::RegInfo, Callback = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Shared/Intersilo/CLCppContainer.h:228:46)]"
- "const Object_T *safeDecoder(CLCppContainer *, Callback) [Object_T = CLClientManager_Type::RegistrationIdentity, Callback = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Shared/Intersilo/CLCppContainer.h:228:46)]"
- "const Object_T *safeDecoder(CLCppContainer *, Callback) [Object_T = CLDaemonStatus_Type::NotificationData, Callback = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Shared/Intersilo/CLCppContainer.h:228:46)]"
- "const Object_T *safeDecoder(CLCppContainer *, Callback) [Object_T = CLDarwinNotifier_Type::NotificationData, Callback = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Shared/Intersilo/CLCppContainer.h:241:46)]"
- "const Object_T *safeDecoder(CLCppContainer *, Callback) [Object_T = CLDarwinNotifier_Type::NotificationData, Callback = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Shared/Intersilo/CLCppContainer.h:250:46)]"
- "const Object_T *safeDecoder(CLCppContainer *, Callback) [Object_T = CLDataProtectionManager_Type::NotificationData, Callback = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Shared/Intersilo/CLCppContainer.h:241:46)]"
- "const Object_T *safeDecoder(CLCppContainer *, Callback) [Object_T = CLDataProtectionManager_Type::NotificationData, Callback = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Shared/Intersilo/CLCppContainer.h:250:46)]"
- "const Object_T *safeDecoder(CLCppContainer *, Callback) [Object_T = CLFenceDataDownloadManager_Type::NotificationData, Callback = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Shared/Intersilo/CLCppContainer.h:228:46)]"
- "const Object_T *safeDecoder(CLCppContainer *, Callback) [Object_T = CLFenceManager_Type::NotificationData, Callback = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Shared/Intersilo/CLCppContainer.h:228:46)]"
- "const Object_T *safeDecoder(CLCppContainer *, Callback) [Object_T = CLFenceMonitor_Type::NotificationData, Callback = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Shared/Intersilo/CLCppContainer.h:228:46)]"
- "const Object_T *safeDecoder(CLCppContainer *, Callback) [Object_T = CLGpsAssistant_Type::NotificationData, Callback = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Shared/Intersilo/CLCppContainer.h:241:46)]"
- "const Object_T *safeDecoder(CLCppContainer *, Callback) [Object_T = CLGpsAssistant_Type::NotificationData, Callback = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Shared/Intersilo/CLCppContainer.h:250:46)]"
- "const Object_T *safeDecoder(CLCppContainer *, Callback) [Object_T = CLGyroCalibrationDatabase_Type::NotificationData, Callback = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Shared/Intersilo/CLCppContainer.h:241:46)]"
- "const Object_T *safeDecoder(CLCppContainer *, Callback) [Object_T = CLGyroCalibrationDatabase_Type::NotificationData, Callback = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Shared/Intersilo/CLCppContainer.h:250:46)]"
- "const Object_T *safeDecoder(CLCppContainer *, Callback) [Object_T = CLLocationAwarenessProvider_Type::NotificationData, Callback = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Shared/Intersilo/CLCppContainer.h:228:46)]"
- "const Object_T *safeDecoder(CLCppContainer *, Callback) [Object_T = CLLocationAwarenessProvider_Type::RegInfo, Callback = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Shared/Intersilo/CLCppContainer.h:228:46)]"
- "const Object_T *safeDecoder(CLCppContainer *, Callback) [Object_T = CLLocationProvider_Type::NotificationData, Callback = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Shared/Intersilo/CLCppContainer.h:228:46)]"
- "const Object_T *safeDecoder(CLCppContainer *, Callback) [Object_T = CLLocationProvider_Type::RegInfo, Callback = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Shared/Intersilo/CLCppContainer.h:228:46)]"
- "const Object_T *safeDecoder(CLCppContainer *, Callback) [Object_T = CLMotionState_Type::NotificationData, Callback = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Shared/Intersilo/CLCppContainer.h:241:46)]"
- "const Object_T *safeDecoder(CLCppContainer *, Callback) [Object_T = CLMotionState_Type::NotificationData, Callback = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Shared/Intersilo/CLCppContainer.h:250:46)]"
- "const Object_T *safeDecoder(CLCppContainer *, Callback) [Object_T = CLNetworkLocationProvider_Type::NotificationData, Callback = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Shared/Intersilo/CLCppContainer.h:241:46)]"
- "const Object_T *safeDecoder(CLCppContainer *, Callback) [Object_T = CLNetworkLocationProvider_Type::NotificationData, Callback = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Shared/Intersilo/CLCppContainer.h:250:46)]"
- "const Object_T *safeDecoder(CLCppContainer *, Callback) [Object_T = CLProxPDPAndALSPhoneNotifier_Type::NotificationData, Callback = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Shared/Intersilo/CLCppContainer.h:241:46)]"
- "const Object_T *safeDecoder(CLCppContainer *, Callback) [Object_T = CLProxPDPAndALSPhoneNotifier_Type::NotificationData, Callback = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Shared/Intersilo/CLCppContainer.h:250:46)]"
- "const Object_T *safeDecoder(CLCppContainer *, Callback) [Object_T = CLSensorCalibrationController_Type::NotificationData, Callback = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Shared/Intersilo/CLCppContainer.h:241:46)]"
- "const Object_T *safeDecoder(CLCppContainer *, Callback) [Object_T = CLSensorCalibrationController_Type::NotificationData, Callback = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Shared/Intersilo/CLCppContainer.h:250:46)]"
- "const Object_T *safeDecoder(CLCppContainer *, Callback) [Object_T = CLSignalEnvironmentProvider_Type::NotificationData, Callback = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Shared/Intersilo/CLCppContainer.h:228:46)]"
- "const Object_T *safeDecoder(CLCppContainer *, Callback) [Object_T = CLStatusBarIconManager_Type::NotificationData, Callback = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Shared/Intersilo/CLCppContainer.h:241:46)]"
- "const Object_T *safeDecoder(CLCppContainer *, Callback) [Object_T = CLStatusBarIconManager_Type::NotificationData, Callback = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Shared/Intersilo/CLCppContainer.h:250:46)]"
- "const Object_T *safeDecoder(CLCppContainer *, Callback) [Object_T = CLTelephonyService_Type::NotificationData, Callback = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Shared/Intersilo/CLCppContainer.h:228:46)]"
- "const Object_T *safeDecoder(CLCppContainer *, Callback) [Object_T = CLTilesManager_Type::NotificationData, Callback = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Shared/Intersilo/CLCppContainer.h:228:46)]"
- "const Object_T *safeDecoder(CLCppContainer *, Callback) [Object_T = CLTimeManager_Type::NotificationData, Callback = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Shared/Intersilo/CLCppContainer.h:241:46)]"
- "const Object_T *safeDecoder(CLCppContainer *, Callback) [Object_T = CLTimeManager_Type::NotificationData, Callback = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Shared/Intersilo/CLCppContainer.h:250:46)]"
- "const Object_T *safeDecoder(CLCppContainer *, Callback) [Object_T = CLWifiService_Type::NotificationData, Callback = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Shared/Intersilo/CLCppContainer.h:228:46)]"
- "const Object_T *safeDecoder(CLCppContainer *, Callback) [Object_T = CLWifiService_Type::RegInfo, Callback = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Shared/Intersilo/CLCppContainer.h:228:46)]"
- "const Object_T *safeDecoder(CLCppContainer *, Callback) [Object_T = char, Callback = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Shared/Intersilo/CLCppContainer.h:241:46)]"
- "const Object_T *safeDecoder(CLCppContainer *, Callback) [Object_T = char, Callback = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Shared/Intersilo/CLCppContainer.h:250:46)]"
- "const Object_T *safeDecoder(CLCppContainer *, Callback) [Object_T = std::list<CLBTLEBeaconRegion_Type::MonitoredRegion>, Callback = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Shared/Intersilo/CLCppContainer.h:228:46)]"
- "default"
- "fetchGEOMapFeatureRoadDataAtIntersectionOf:allowNetwork:preferCachedTiles:isPedestrianOrCycling:clearTiles:returnRoads:"
- "fetchGEORoadDataAroundCoordinate:inRadius:allowNetwork:preferCachedTiles:isPedestrianOrCycling:clearTiles:withReply:"
- "https://cl3.apple.com/1/v2/"
- "kCLLocationType_Cell"
- "kCLLocationType_WiFi"
- "makeIntersectionQueryCallUsingMapsAPIFor:allowNetwork:preferCachedTiles:isPedestrianOrCycling:clearTiles:returnRoads:"
- "speedLimit"
- "v64@0:8{CLLocationCoordinate2D=dd}16d32B40B44B48B52@?56"
- "v64@0:8{CLLocationCoordinate2D=dd}16d32B40B44B48B52@?<v@?@\"NSArray\">56"
- "v76@0:8q16{CLLocationCoordinate2D=dd}24d40B48B52B56B60B64@?68"
- "{CLOdometerEntry=ddddddddddiiiddddddddiiB{CLOdometerTrackProximityInfo=id}}24@0:8@16"
```
