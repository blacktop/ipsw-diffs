## CoreWiFi

> `/System/Library/PrivateFrameworks/CoreWiFi.framework/Versions/A/CoreWiFi`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_assocty`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift5_capture`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-1040.60.0.0.0
-  __TEXT.__text: 0x457df8
-  __TEXT.__objc_methlist: 0x124f0
+1040.67.0.0.0
+  __TEXT.__text: 0x45ab30
+  __TEXT.__objc_methlist: 0x12548
   __TEXT.__const: 0x9bf8
-  __TEXT.__cstring: 0x2b34e
-  __TEXT.__oslogstring: 0x2086c
-  __TEXT.__gcc_except_tab: 0x15a34
+  __TEXT.__cstring: 0x2b3fe
+  __TEXT.__oslogstring: 0x20a2c
+  __TEXT.__gcc_except_tab: 0x15bf0
   __TEXT.__dlopen_cstrs: 0x9cc
   __TEXT.__ustring: 0x4
   __TEXT.__swift5_typeref: 0x16b1

   __TEXT.__swift5_types: 0x1bc
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_capture: 0x1e0
-  __TEXT.__unwind_info: 0x4ca8
+  __TEXT.__unwind_info: 0x4cd8
   __TEXT.__eh_frame: 0x1278
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x10c0
+  __DATA_CONST.__const: 0x10c8
   __DATA_CONST.__objc_classlist: 0x400
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x130
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9198
+  __DATA_CONST.__objc_selrefs: 0x91d0
   __DATA_CONST.__objc_protorefs: 0x88
   __DATA_CONST.__objc_superrefs: 0x390
-  __DATA_CONST.__objc_arraydata: 0x1de8
+  __DATA_CONST.__objc_arraydata: 0x1da8
   __DATA_CONST.__got: 0xa78
-  __AUTH_CONST.__const: 0x9358
-  __AUTH_CONST.__cfstring: 0x1c8e0
-  __AUTH_CONST.__objc_const: 0x18158
-  __AUTH_CONST.__objc_intobj: 0x3d98
-  __AUTH_CONST.__objc_arrayobj: 0x4f8
+  __AUTH_CONST.__const: 0x9378
+  __AUTH_CONST.__cfstring: 0x1c9e0
+  __AUTH_CONST.__objc_const: 0x18180
+  __AUTH_CONST.__objc_intobj: 0x3e28
+  __AUTH_CONST.__objc_arrayobj: 0x4c8
   __AUTH_CONST.__objc_dictobj: 0x230
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__auth_got: 0x1080

   __AUTH.__data: 0x1c8
   __DATA.__objc_ivar: 0x157c
   __DATA.__data: 0x1d30
-  __DATA.__bss: 0xead0
+  __DATA.__bss: 0xeae0
   __DATA.__common: 0x38
   __DATA_DIRTY.__objc_data: 0x12e8
   __DATA_DIRTY.__data: 0x1f0

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 11074
-  Symbols:   22663
-  CStrings:  6762
+  Functions: 11090
+  Symbols:   22685
+  CStrings:  6772
 
Symbols:
+ -[CWFApple80211 NANRadioSchedule:]
+ -[CWFInterface NANRadioSchedule]
+ -[CWFNetworkProfile isConnectivityAssistEnabled]
+ -[CWFNetworkProfile setConnectivityAssistEnabled:]
+ -[CWFUIScanManager passpointANQPElementIDList]
+ -[CWFWiFiNetworkSharingManager __addCurrentNetworkToNetworkListForClientID:forceRegistration:addedColocatedNetworks:]
+ -[CWFXPCConnection queryNANRadioScheduleWithRequestParams:reply:]
+ -[CWFXPCRequestProxy __performUIScanWithScanResults:scanType:interfaceName:]
+ -[CWFXPCRequestProxy __startUIScanWithCacheResults:XPCRequest:responseInfo:]
+ GCC_except_table186
+ GCC_except_table294
+ GCC_except_table340
+ GCC_except_table412
+ GCC_except_table620
+ GCC_except_table626
+ GCC_except_table627
+ GCC_except_table652
+ GCC_except_table662
+ GCC_except_table669
+ GCC_except_table672
+ GCC_except_table688
+ GCC_except_table700
+ GCC_except_table721
+ GCC_except_table745
+ GCC_except_table790
+ GCC_except_table903
+ GCC_except_table915
+ _CWFNetworkProfilePropertyConnectivityAssistEnabledKey
+ _CWFPasspointScanResults
+ ___32-[CWFInterface NANRadioSchedule]_block_invoke
+ ___32-[CWFInterface NANRadioSchedule]_block_invoke_2
+ ___76-[CWFXPCRequestProxy __performUIScanWithScanResults:scanType:interfaceName:]_block_invoke
+ ___76-[CWFXPCRequestProxy __startUIScanWithCacheResults:XPCRequest:responseInfo:]_block_invoke
+ ___block_descriptor_72_e8_32s40s48s56bs_e34_v24?0"NSError"8"NSDictionary"16l
+ ___block_descriptor_80_e8_32s40s48s56s64s72r_e34_v24?0"NSError"8"NSDictionary"16l
+ ___copy_helper_block_e8_32s40s48s56s64s72r
+ _objc_msgSend$NANRadioSchedule:
+ _objc_msgSend$__addCurrentNetworkToNetworkListForClientID:forceRegistration:addedColocatedNetworks:
+ _objc_msgSend$__performUIScanWithScanResults:scanType:interfaceName:
+ _objc_msgSend$__startUIScanWithCacheResults:XPCRequest:responseInfo:
+ _objc_msgSend$isConnectivityAssistEnabled
+ _objc_msgSend$passpointANQPElementIDList
+ _objc_msgSend$queryNANRadioScheduleWithRequestParams:reply:
+ _objc_msgSend$setConnectivityAssistEnabled:
- -[CWFWiFiNetworkSharingManager __addCurrentNetworkToNetworkListForClientID:forceRegistration:]
- -[CWFXPCConnection __passpointScanResults:]
- GCC_except_table289
- GCC_except_table401
- GCC_except_table406
- GCC_except_table608
- GCC_except_table615
- GCC_except_table629
- GCC_except_table657
- GCC_except_table658
- GCC_except_table691
- GCC_except_table703
- GCC_except_table724
- GCC_except_table763
- GCC_except_table813
- GCC_except_table912
- GCC_except_table97
- ___block_descriptor_64_e8_32s40s48bs_e34_v24?0"NSError"8"NSDictionary"16l
- ___block_descriptor_72_e8_32s40s48s56s64r_e34_v24?0"NSError"8"NSDictionary"16l
- ___copy_helper_block_e8_32s40s48s56s64r
- _objc_msgSend$__addCurrentNetworkToNetworkListForClientID:forceRegistration:
- _objc_msgSend$__passpointScanResults:
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8ITM3r/Sources/CoreWiFi/Framework/CWFApple80211.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8ITM3r/Sources/CoreWiFi/Framework/CWFAssetCreatorFromRoot.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8ITM3r/Sources/CoreWiFi/Framework/CWFAssetLocal.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8ITM3r/Sources/CoreWiFi/Framework/CWFAssetPowerTable.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8ITM3r/Sources/CoreWiFi/Framework/CWFAssetPowerTableElector.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8ITM3r/Sources/CoreWiFi/Framework/CWFAssetPowerTableTelemetry.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8ITM3r/Sources/CoreWiFi/Framework/CWFAssetRootMonitor.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8ITM3r/Sources/CoreWiFi/Framework/CWFAssetSetManager.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8ITM3r/Sources/CoreWiFi/Framework/CWFAutoJoinManager.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8ITM3r/Sources/CoreWiFi/Framework/CWFBSS.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8ITM3r/Sources/CoreWiFi/Framework/CWFCloudSyncManager.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8ITM3r/Sources/CoreWiFi/Framework/CWFDiagnosticReporter.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8ITM3r/Sources/CoreWiFi/Framework/CWFEAP8021X.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8ITM3r/Sources/CoreWiFi/Framework/CWFHomeManager/CWFHomeManager.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8ITM3r/Sources/CoreWiFi/Framework/CWFHomeManager/CWFSensingAutoDataCollector.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8ITM3r/Sources/CoreWiFi/Framework/CWFHomeManager/CWFSensingHMADataCollector.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8ITM3r/Sources/CoreWiFi/Framework/CWFIO80211.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8ITM3r/Sources/CoreWiFi/Framework/CWFJITTDImpactEstimator.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8ITM3r/Sources/CoreWiFi/Framework/CWFKernelEventMonitor.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8ITM3r/Sources/CoreWiFi/Framework/CWFNearbyDeviceDiscoveryManager.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8ITM3r/Sources/CoreWiFi/Framework/CWFNearbySyncManager.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8ITM3r/Sources/CoreWiFi/Framework/CWFNetworkProfile.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8ITM3r/Sources/CoreWiFi/Framework/CWFPowerTableElectionTelemetry.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8ITM3r/Sources/CoreWiFi/Framework/CWFPrivateMACManager.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8ITM3r/Sources/CoreWiFi/Framework/CWFSCNetworkConfiguration.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8ITM3r/Sources/CoreWiFi/Framework/CWFSCNetworkInterface.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8ITM3r/Sources/CoreWiFi/Framework/CWFSCNetworkService.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8ITM3r/Sources/CoreWiFi/Framework/CWFUtilInternal.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8ITM3r/Sources/CoreWiFi/Framework/CWFUtilPrivate.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8ITM3r/Sources/CoreWiFi/Framework/CWFWiFiUserAgent.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8ITM3r/Sources/CoreWiFi/Framework/CWFXPCConnection.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8ITM3r/Sources/CoreWiFi/Framework/CWFXPCListener.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8ITM3r/Sources/CoreWiFi/Framework/CWFXPCManager.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8ITM3r/Sources/CoreWiFi/Framework/CWFXPCProxy.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8ITM3r/Sources/CoreWiFi/Framework/Categories/NSDictionary+CloudSync.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8ITM3r/Sources/CoreWiFi/Framework/WiFi Network Sharing/CWFWiFiNetworkSharingManager.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8ITM3r/Sources/CoreWiFi/Framework/WiFi Network Sharing/CWFWiFiNetworkSharingNetwork.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8ITM3r/Sources/CoreWiFi/Framework/WiFi Network Sharing/CWFWiFiNetworkSharingNetworkID.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8ITM3r/Sources/CoreWiFi/Framework/WiFi Network Sharing/CWFWiFiNetworkSharingStore.m"
+ "ConnectivityAssistEnabled"
+ "GET NAN RADIO SCHEDULE"
+ "NANRTM"
+ "[corewifi] @[%llu.%06llu] %{public}s (%{public}s:%u) Matched cached hybrid interface %{public}@ for APPLE80211_VIRT_IF_ROLE_NAN_DISCOVERY"
+ "[corewifi] AUTO-JOIN: [internal] Applying defaults override for [CWFAutoJoinTriggerAssociatedToNetworkRetry : CWFAutoJoinTriggerNANRealTimeModeEnded] throttle interval (default=%lus, override=%lus)"
+ "[corewifi] [wifi-network-sharing] Already added network for clientID (clientID=%{public}@, knownNetwork=%{public}@)"
+ "assoc_retry_nan_rt_throttle_interval"
+ "connectivityAssist=no, "
+ "isConnectivityAssistEnabled"
+ "nan_rt_ended"
+ "remotedevicekitwifid"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FADtVq/Sources/CoreWiFi/Framework/CWFApple80211.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FADtVq/Sources/CoreWiFi/Framework/CWFAssetCreatorFromRoot.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FADtVq/Sources/CoreWiFi/Framework/CWFAssetLocal.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FADtVq/Sources/CoreWiFi/Framework/CWFAssetPowerTable.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FADtVq/Sources/CoreWiFi/Framework/CWFAssetPowerTableElector.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FADtVq/Sources/CoreWiFi/Framework/CWFAssetPowerTableTelemetry.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FADtVq/Sources/CoreWiFi/Framework/CWFAssetRootMonitor.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FADtVq/Sources/CoreWiFi/Framework/CWFAssetSetManager.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FADtVq/Sources/CoreWiFi/Framework/CWFAutoJoinManager.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FADtVq/Sources/CoreWiFi/Framework/CWFBSS.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FADtVq/Sources/CoreWiFi/Framework/CWFCloudSyncManager.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FADtVq/Sources/CoreWiFi/Framework/CWFDiagnosticReporter.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FADtVq/Sources/CoreWiFi/Framework/CWFEAP8021X.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FADtVq/Sources/CoreWiFi/Framework/CWFHomeManager/CWFHomeManager.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FADtVq/Sources/CoreWiFi/Framework/CWFHomeManager/CWFSensingAutoDataCollector.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FADtVq/Sources/CoreWiFi/Framework/CWFHomeManager/CWFSensingHMADataCollector.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FADtVq/Sources/CoreWiFi/Framework/CWFIO80211.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FADtVq/Sources/CoreWiFi/Framework/CWFJITTDImpactEstimator.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FADtVq/Sources/CoreWiFi/Framework/CWFKernelEventMonitor.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FADtVq/Sources/CoreWiFi/Framework/CWFNearbyDeviceDiscoveryManager.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FADtVq/Sources/CoreWiFi/Framework/CWFNearbySyncManager.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FADtVq/Sources/CoreWiFi/Framework/CWFNetworkProfile.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FADtVq/Sources/CoreWiFi/Framework/CWFPowerTableElectionTelemetry.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FADtVq/Sources/CoreWiFi/Framework/CWFPrivateMACManager.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FADtVq/Sources/CoreWiFi/Framework/CWFSCNetworkConfiguration.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FADtVq/Sources/CoreWiFi/Framework/CWFSCNetworkInterface.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FADtVq/Sources/CoreWiFi/Framework/CWFSCNetworkService.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FADtVq/Sources/CoreWiFi/Framework/CWFUtilInternal.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FADtVq/Sources/CoreWiFi/Framework/CWFUtilPrivate.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FADtVq/Sources/CoreWiFi/Framework/CWFWiFiUserAgent.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FADtVq/Sources/CoreWiFi/Framework/CWFXPCConnection.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FADtVq/Sources/CoreWiFi/Framework/CWFXPCListener.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FADtVq/Sources/CoreWiFi/Framework/CWFXPCManager.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FADtVq/Sources/CoreWiFi/Framework/CWFXPCProxy.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FADtVq/Sources/CoreWiFi/Framework/Categories/NSDictionary+CloudSync.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FADtVq/Sources/CoreWiFi/Framework/WiFi Network Sharing/CWFWiFiNetworkSharingManager.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FADtVq/Sources/CoreWiFi/Framework/WiFi Network Sharing/CWFWiFiNetworkSharingNetwork.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FADtVq/Sources/CoreWiFi/Framework/WiFi Network Sharing/CWFWiFiNetworkSharingNetworkID.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FADtVq/Sources/CoreWiFi/Framework/WiFi Network Sharing/CWFWiFiNetworkSharingStore.m"
- "hrmwifid"
```
