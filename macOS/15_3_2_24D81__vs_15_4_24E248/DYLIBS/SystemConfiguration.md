## SystemConfiguration

> `/System/Library/Frameworks/SystemConfiguration.framework/Versions/A/SystemConfiguration`

```diff

-1351.80.2.0.0
-  __TEXT.__text: 0x83424
+1351.101.1.0.0
+  __TEXT.__text: 0x83678
   __TEXT.__auth_stubs: 0x2080
-  __TEXT.__const: 0x2a0
-  __TEXT.__cstring: 0x672c
+  __TEXT.__const: 0x2c0
+  __TEXT.__cstring: 0x673c
   __TEXT.__oslogstring: 0x5ea9
-  __TEXT.__unwind_info: 0xda8
-  __DATA_CONST.__got: 0x198
+  __TEXT.__unwind_info: 0xd70
+  __DATA_CONST.__got: 0x190
   __DATA_CONST.__const: 0x2b00
   __AUTH_CONST.__auth_got: 0x1040
   __AUTH_CONST.__const: 0xff0
-  __AUTH_CONST.__cfstring: 0x72c0
+  __AUTH_CONST.__cfstring: 0x72e0
   __DATA.__data: 0x4d8
   __DATA.__crash_info: 0x40
   __DATA.__common: 0x8

   - /System/Library/PrivateFrameworks/AppleSystemInfo.framework/Versions/A/AppleSystemInfo
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
-  UUID: C432C6F3-58A3-324A-AA32-9BE164948D73
-  Functions: 1335
-  Symbols:   2773
-  CStrings:  3049
+  UUID: 455660A4-CC4B-31F3-A2CC-FB56DDEC88B7
+  Functions: 1366
+  Symbols:   3007
+  CStrings:  3050
 
Symbols:
+ CNCopyCurrentNetworkInfo.cold.1
+ CNCopySupportedInterfaces.cold.1
+ CNMarkPortalOffline.cold.1
+ CNMarkPortalOnline.cold.1
+ CNSetSupportedSSIDs.cold.1
+ IPMonitorControlCreate.cold.1
+ SCDynamicStoreCopyLocalHostName.cold.1
+ SCDynamicStoreGetTypeID.cold.1
+ SCDynamicStoreSetDisconnectCallBack.cold.1
+ SCNetworkCategoryGetTypeID.cold.1
+ SCNetworkCategoryManagerCreateWithInterface.cold.1
+ SCNetworkCategoryManagerGetTypeID.cold.1
+ SCNetworkConnectionCanTunnelAddress.cold.1
+ SCNetworkConnectionCopyExtendedStatus.cold.1
+ SCNetworkConnectionCopyExtendedStatus.cold.2
+ SCNetworkConnectionCopyOnDemandInfo.cold.1
+ SCNetworkConnectionCopyServiceID.cold.1
+ SCNetworkConnectionCopyStatistics.cold.1
+ SCNetworkConnectionCopyStatistics.cold.2
+ SCNetworkConnectionCopyUserOptions.cold.1
+ SCNetworkConnectionCopyUserOptions.cold.2
+ SCNetworkConnectionCopyUserPreferences.cold.1
+ SCNetworkConnectionGetReachabilityInfo.cold.1
+ SCNetworkConnectionGetService.cold.1
+ SCNetworkConnectionGetStatus.cold.1
+ SCNetworkConnectionGetStatus.cold.2
+ SCNetworkConnectionGetType.cold.1
+ SCNetworkConnectionGetTypeID.cold.1
+ SCNetworkConnectionIsOnDemandSuspended.cold.1
+ SCNetworkConnectionOnDemandShouldRetryOnFailure.cold.1
+ SCNetworkConnectionResume.cold.1
+ SCNetworkConnectionScheduleWithRunLoop.cold.1
+ SCNetworkConnectionSelectServiceWithOptions.cold.1
+ SCNetworkConnectionSetClientInfo.cold.1
+ SCNetworkConnectionSetDispatchQueue.cold.1
+ SCNetworkConnectionStart.cold.1
+ SCNetworkConnectionStop.cold.1
+ SCNetworkConnectionSuspend.cold.1
+ SCNetworkConnectionTriggerOnDemandIfNeeded.cold.1
+ SCNetworkConnectionUnscheduleFromRunLoop.cold.1
+ SCNetworkInterfaceCreateWithInterface.cold.1
+ SCNetworkInterfaceForceConfigurationRefresh.cold.1
+ SCNetworkInterfaceGetAutoConfigure.cold.1
+ SCNetworkInterfaceGetAutoConfigure.cold.2
+ SCNetworkInterfaceGetBSDName.cold.1
+ SCNetworkInterfaceGetConfiguration.cold.1
+ SCNetworkInterfaceGetExtendedConfiguration.cold.1
+ SCNetworkInterfaceGetHardwareAddressString.cold.1
+ SCNetworkInterfaceGetInterface.cold.1
+ SCNetworkInterfaceGetInterfaceType.cold.1
+ SCNetworkInterfaceGetLocalizedDisplayName.cold.1
+ SCNetworkInterfaceGetQoSMarkingPolicy.cold.1
+ SCNetworkInterfaceGetSupportedInterfaceTypes.cold.1
+ SCNetworkInterfaceGetSupportedProtocolTypes.cold.1
+ SCNetworkInterfaceGetTypeID.cold.1
+ SCNetworkInterfaceProviderCreate.cold.1
+ SCNetworkInterfaceSetAutoConfigure.cold.1
+ SCNetworkInterfaceSetAutoConfigure.cold.2
+ SCNetworkInterfaceSetConfiguration.cold.1
+ SCNetworkInterfaceSetExtendedConfiguration.cold.1
+ SCNetworkInterfaceSetQoSMarkingPolicy.cold.1
+ SCNetworkInterfaceSupportsLowDataMode.cold.1
+ SCNetworkInterfaceTypeSetTemporaryOverrideCost.cold.1
+ SCNetworkProtocolGetConfiguration.cold.1
+ SCNetworkProtocolGetEnabled.cold.1
+ SCNetworkProtocolGetProtocolType.cold.1
+ SCNetworkProtocolGetTypeID.cold.1
+ SCNetworkProtocolSetConfiguration.cold.1
+ SCNetworkProtocolSetEnabled.cold.1
+ SCNetworkReachabilityCopyResolvedAddress.cold.3
+ SCNetworkReachabilityGetFlags.cold.3
+ SCNetworkReachabilityGetInterfaceIndex.cold.3
+ SCNetworkReachabilityGetTypeID.cold.1
+ SCNetworkReachabilityScheduleWithRunLoop.cold.5
+ SCNetworkReachabilityScheduleWithRunLoop.cold.6
+ SCNetworkReachabilitySetDispatchQueue.cold.3
+ SCNetworkReachabilityUnscheduleFromRunLoop.cold.4
+ SCNetworkServiceAddProtocolType.cold.3
+ SCNetworkServiceCopyExternalID.cold.1
+ SCNetworkServiceCopyProtocol.cold.1
+ SCNetworkServiceCopyProtocols.cold.1
+ SCNetworkServiceEstablishDefaultConfiguration.cold.1
+ SCNetworkServiceGetEnabled.cold.1
+ SCNetworkServiceGetInterface.cold.1
+ SCNetworkServiceGetPrimaryRank.cold.1
+ SCNetworkServiceGetServiceID.cold.1
+ SCNetworkServiceGetTypeID.cold.1
+ SCNetworkServiceRemove.cold.1
+ SCNetworkServiceRemoveProtocolType.cold.1
+ SCNetworkServiceSetEnabled.cold.1
+ SCNetworkServiceSetExternalID.cold.1
+ SCNetworkServiceSetName.cold.1
+ SCNetworkServiceSetPrimaryRank.cold.1
+ SCNetworkSetAddService.cold.1
+ SCNetworkSetCopySelectedVPNService.cold.1
+ SCNetworkSetCopyServices.cold.1
+ SCNetworkSetEstablishDefaultConfiguration.cold.1
+ SCNetworkSetEstablishDefaultInterfaceConfiguration.cold.2
+ SCNetworkSetGetName.cold.1
+ SCNetworkSetGetServiceOrder.cold.1
+ SCNetworkSetGetSetID.cold.1
+ SCNetworkSetGetTypeID.cold.1
+ SCNetworkSetRemove.cold.1
+ SCNetworkSetRemoveService.cold.1
+ SCNetworkSetSetCurrent.cold.1
+ SCNetworkSetSetName.cold.1
+ SCNetworkSetSetSelectedVPNService.cold.1
+ SCNetworkSetSetServiceOrder.cold.1
+ SCPreferencesGetTypeID.cold.1
+ SCPreferencesLock.cold.1
+ SCPreferencesScheduleWithRunLoop.cold.1
+ SCPreferencesSetCallback.cold.1
+ SCPreferencesSetDispatchQueue.cold.1
+ SCPreferencesSynchronize.cold.1
+ SCPreferencesUnscheduleFromRunLoop.cold.1
+ SCUserPreferencesCopyExtendedInterfaceConfiguration.cold.1
+ SCUserPreferencesCopyInterfaceTypeConfiguration.cold.1
+ SCUserPreferencesCopyName.cold.1
+ SCUserPreferencesCopyStartOptions.cold.1
+ SCUserPreferencesGetTypeID.cold.1
+ SCUserPreferencesGetUniqueID.cold.1
+ SCUserPreferencesIsForced.cold.1
+ SCUserPreferencesRemove.cold.1
+ SCUserPreferencesSetCurrent.cold.1
+ SCUserPreferencesSetExtendedInterfaceConfiguration.cold.1
+ SCUserPreferencesSetInterfaceTypeConfiguration.cold.1
+ SCUserPreferencesSetName.cold.1
+ _SCControlPrefsCreateCommon.cold.1
+ _SCDPluginExecCommand2.cold.3
+ _SCDPluginSpawnCommand.cold.2
+ _SCHelperExec.cold.1
+ _SCNetworkInterfaceCopyAllWithPreferences.cold.1
+ _SCNetworkInterfaceCopyAllWithPreferences.cold.2
+ _SCNetworkInterfaceCreateWithEntity.cold.1
+ _SCNetworkInterfaceCreateWithIONetworkInterfaceObject.cold.1
+ _SCNetworkInterfaceIsApplePreconfigured.cold.1
+ _SCNetworkInterfaceIsBluetoothP2P.cold.1
+ _SCNetworkInterfaceIsBluetoothPAN.cold.1
+ _SCNetworkInterfaceIsBluetoothPAN_NAP.cold.1
+ _SCNetworkInterfaceIsBuiltin.cold.1
+ _SCNetworkInterfaceIsCarPlay.cold.1
+ _SCNetworkInterfaceIsEphemeral.cold.1
+ _SCNetworkInterfaceIsHiddenConfiguration.cold.1
+ _SCNetworkInterfaceIsHiddenInterface.cold.1
+ _SCNetworkInterfaceIsSelfNamed.cold.1
+ _SCNetworkInterfaceIsTethered.cold.1
+ _SCNetworkInterfaceIsTetheredHotspot.cold.1
+ _SCNetworkInterfaceIsThunderbolt.cold.1
+ _SCNetworkInterfaceIsTrustRequired.cold.1
+ _SCNetworkInterfaceIsUserEthernet.cold.1
+ _SCNetworkInterfaceIsVMNET.cold.1
+ _SCNetworkInterfaceSupportsVMNETBridgedMode.cold.1
+ _SCNetworkServiceSetServiceID.cold.1
+ _SCNetworkSetCopyUserDefinedName.cold.1
+ _SCNetworkSetIsDefault.cold.1
+ _SCNetworkSetSetSetID.cold.1
+ _SC_crash.cold.1
+ _SC_dlopen.cold.1
+ _SC_getApplicationBundleID.cold.1
+ _SC_hw_model.cold.1
+ _SC_isInstallEnvironment.cold.1
+ __SCDynamicStoreCreateInternal.cold.1
+ __SCDynamicStoreCreateInternal.cold.2
+ __SCDynamicStoreDeallocate.cold.1
+ __SCDynamicStoreNormalize.cold.2
+ __SCDynamicStoreNormalize.cold.3
+ __SCGetThreadSpecificData.cold.1
+ __SCHelperServerPort.cold.1
+ __SCNSManagerCreateCommon.cold.1
+ __SCNSServiceCreate.cold.1
+ __SCNetworkCategoryCreate.cold.1
+ __SCNetworkCategoryManagerCopyActiveValueNoSession.cold.1
+ __SCNetworkConnectionCallBack.cold.3
+ __SCNetworkConnectionCopyExtendedStatus_block_invoke.cold.1
+ __SCNetworkConnectionCreatePrivate.cold.1
+ __SCNetworkConnectionScheduleWithRunLoop.cold.1
+ __SCNetworkConnectionScheduleWithRunLoop.cold.2
+ __SCNetworkConnectionTriggerOnDemandIfNeeded_block_invoke.cold.1
+ __SCNetworkConnectionTriggerOnDemandIfNeeded_block_invoke_2.cold.1
+ __SCNetworkInterfaceCopyOldLocalizedDisplayName.cold.1
+ __SCNetworkInterfaceCopyOldNonLocalizedDisplayName.cold.1
+ __SCNetworkInterfaceCopyStoredWithPreferences.cold.2
+ __SCNetworkInterfaceCreateCopy.cold.1
+ __SCNetworkInterfaceCreatePrivate.cold.1
+ __SCNetworkInterfaceCreateWithNIPreferencesUsingBSDName.cold.2
+ __SCNetworkInterfaceCreateWithStorageEntity.cold.1
+ __SCNetworkInterfaceGetConfiguration.cold.1
+ __SCNetworkInterfaceGetDefaultConfiguration.cold.1
+ __SCNetworkInterfaceGetNonLocalizedDisplayName.cold.1
+ __SCNetworkInterfaceGetUserDefinedName.cold.1
+ __SCNetworkInterfaceIsBusyMember.cold.1
+ __SCNetworkInterfaceOrder.cold.1
+ __SCNetworkInterfaceSetConfiguration.cold.1
+ __SCNetworkInterfaceSetDefaultConfiguration.cold.1
+ __SCNetworkInterfaceUpdateBSDName.cold.1
+ __SCNetworkProtocolCreatePrivate.cold.1
+ __SCNetworkReachabilityCreatePrivate.cold.2
+ __SCNetworkServiceCreatePrivate.cold.1
+ __SCNetworkServiceGetName.cold.1
+ __SCNetworkServiceMigrateNew.cold.1
+ __SCNetworkSetCreatePrivate.cold.1
+ __SCPreferencesCreate.cold.1
+ __SCPreferencesPath.cold.1
+ __SCPreferencesPath.cold.2
+ __SCPreferencesUpdateLockedState.cold.1
+ __SCUserPreferencesCreatePrivate.cold.1
+ __SC_log_enabled.cold.1
+ __SC_log_enabled.cold.2
+ ____SCDynamicStoreInitialize_block_invoke.cold.1
+ ____SCHelperServerPort_block_invoke.cold.1
+ __block_descriptor_tmp.68
+ __block_literal_global.70
+ __log_open_error_block_invoke.cold.1
+ _isA_CFArray
+ _is_preboot_environment
+ _scprefs_observer_watch.cold.1
+ checkInterfacePassword.cold.1
+ checkUserPreferencesPassword.cold.1
+ childrenReaped.cold.1
+ copy_default_set_name.cold.1
+ copy_default_set_name.cold.2
+ get_number_value.cold.1
+ log_open_error.cold.1
+ processNetworkInterface.cold.1
+ report_missing_entitlement.cold.1
+ updateServerPort.cold.1
- ___SCNetworkConnectionServerPort
- __block_descriptor_tmp.65
- __block_literal_global.67
- _get_preboot_path_prefix
CStrings:
+ "use-preboot-volume"
- ".."

```
