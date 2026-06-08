## MobileWiFi

> `/System/Library/PrivateFrameworks/MobileWiFi.framework/MobileWiFi`

```diff

-2000.6.0.0.0
-  __TEXT.__text: 0x2e8b4
-  __TEXT.__auth_stubs: 0xde0
-  __TEXT.__objc_methlist: 0x74
-  __TEXT.__cstring: 0x44e5
-  __TEXT.__const: 0x6b0
-  __TEXT.__oslogstring: 0x91f
-  __TEXT.__gcc_except_tab: 0x124
+2027.9.0.0.0
+  __TEXT.__text: 0x36938
+  __TEXT.__objc_methlist: 0x94
+  __TEXT.__cstring: 0x5bcb
+  __TEXT.__const: 0x740
+  __TEXT.__oslogstring: 0x271e
+  __TEXT.__gcc_except_tab: 0x110
   __TEXT.__dlopen_cstrs: 0xe9
-  __TEXT.__unwind_info: 0xab8
-  __TEXT.__objc_classname: 0x3f
-  __TEXT.__objc_methname: 0x10d4
-  __TEXT.__objc_methtype: 0xea
-  __TEXT.__objc_stubs: 0x1a00
-  __DATA_CONST.__got: 0x248
-  __DATA_CONST.__const: 0x10c8
+  __TEXT.__unwind_info: 0xb98
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x1110
   __DATA_CONST.__objc_classlist: 0x8
+  __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6a8
+  __DATA_CONST.__objc_selrefs: 0x758
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x700
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x450
-  __AUTH_CONST.__cfstring: 0x58a0
-  __AUTH_CONST.__objc_const: 0x120
-  __AUTH_CONST.__objc_intobj: 0x660
+  __AUTH_CONST.__cfstring: 0x5b00
+  __AUTH_CONST.__objc_const: 0x160
+  __AUTH_CONST.__objc_intobj: 0x6d8
+  __AUTH_CONST.__auth_got: 0x790
   __DATA.__objc_ivar: 0xc
   __DATA.__data: 0xf8
-  __DATA.__bss: 0x80
+  __DATA.__bss: 0x70
   __DATA_DIRTY.__objc_data: 0x50
   __DATA_DIRTY.__data: 0x80
   __DATA_DIRTY.__bss: 0x40

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E0EB1D80-3E7A-3936-B725-5AA9F0E79B62
-  Functions: 1160
-  Symbols:   2724
-  CStrings:  1801
+  UUID: 0F1DEF42-D18B-3BA4-898C-F4AF1BF84EC0
+  Functions: 1298
+  Symbols:   3051
+  CStrings:  1943
 
Symbols:
+ -[NSString(Utilities) paddedMACAddress]
+ -[NSString(Utilities) unpaddedMACAddress]
+ GCC_except_table249
+ GCC_except_table251
+ GCC_except_table7
+ _CWFGetOSLog
+ _CWFScanResultPropertyOSSpecificAttributesKey
+ _CoreWiFiAskToJoinModeFromWiFiAskToJoinPreference
+ _CoreWiFiAutoHotspotModeFromWiFiAutoHotspotMode
+ _CoreWiFiCompatibilityModeFromWiFi6ECompatibilityMode
+ _CoreWiFiNearbyShareableStatusFromWiFiNetworkShareableStatus
+ _OBJC_CLASS_$_CWFChannel
+ _WiFi6ECompatibilityModeFromCoreWiFiCompatibilityMode
+ _WiFiAskToJoinPreferenceFromCoreWiFiAskToJoinMode
+ _WiFiAutoHotspotModeFromCoreWiFiAutoHotspotMode
+ _WiFiDeviceClientAutoJoinBlacklistCommand.cold.1
+ _WiFiDeviceClientBssBlacklistCommandAndCopyResponse.cold.1
+ _WiFiDeviceClientNotifySoftError.cold.1
+ _WiFiDeviceClientRegisterResetInterfaceCallback
+ _WiFiDeviceClientRegisterRoamBasedCellDupRecStartCallback
+ _WiFiDeviceClientRegisterRoamBasedCellDupRecStopCallback
+ _WiFiManagerClientCopyGeoTagsForNetwork.cold.1
+ _WiFiManagerClientCopyGeoTagsForNetwork.cold.2
+ _WiFiManagerClientCopyGeoTagsForNetwork.cold.3
+ _WiFiManagerClientCopyKnownNetworksNearLocation.cold.1
+ _WiFiManagerClientCopyLocaleStats.cold.1
+ _WiFiManagerClientCopyLocaleStats.cold.2
+ _WiFiManagerClientCopyScoreForNetwork.cold.1
+ _WiFiManagerClientCopyScoreForNetwork.cold.2
+ _WiFiManagerClientCopyScoreForNetwork.cold.3
+ _WiFiManagerClientCopyScoreSortedKnownNetworksNearLocation.cold.1
+ _WiFiManagerClientGetAirplaneModePowerPreference.cold.1
+ _WiFiManagerClientGetHardwareFailure.cold.1
+ _WiFiManagerClientPurgeExpiredKnownNetworks.cold.1
+ _WiFiManagerClientResetNetworkSettings.cold.1
+ _WiFiManagerClientSetGeoTagForNetwork.cold.1
+ _WiFiManagerClientSetSimulatedMovementStates.cold.1
+ _WiFiManagerClientSetTestParamsAndCopyResponse.cold.1
+ _WiFiManagerClientSetUserInteractionNwOverride.cold.1
+ _WiFiManagerClientSetUserInteractionNwOverride.cold.2
+ _WiFiManagerClientSetUserInteractionNwOverride.cold.3
+ _WiFiManagerClientSetUserInteractionOverride.cold.1
+ _WiFiManagerClientSetUserInteractionOverride.cold.2
+ _WiFiManagerClientSetUserInteractionOverride.cold.3
+ _WiFiManagerClientWiFiCallHandoverNotification.cold.1
+ _WiFiNetworkCanExposeIMSI.cold.2
+ _WiFiNetworkCanExposeIMSI.cold.3
+ _WiFiNetworkCanExposeIMSI.cold.4
+ _WiFiNetworkCanExposeIMSI.cold.5
+ _WiFiNetworkCompareWithKnownNetwork.cold.1
+ _WiFiNetworkCopyFilteredRecordForClassDStorage
+ _WiFiNetworkCopyKeychainModDate.cold.1
+ _WiFiNetworkCopyLeakyStatus.cold.1
+ _WiFiNetworkCopyLeakyStatus.cold.2
+ _WiFiNetworkCopyLeakyStatus.cold.3
+ _WiFiNetworkCopyLeakyStatus.cold.4
+ _WiFiNetworkCopyLeakyStatus.cold.5
+ _WiFiNetworkCreateCoreWiFiScanResult.cold.1
+ _WiFiNetworkCreateFromPath.cold.2
+ _WiFiNetworkCreateFromPath.cold.3
+ _WiFiNetworkCreateWithSsid.cold.1
+ _WiFiNetworkCreateWithSsid.cold.2
+ _WiFiNetworkDisableAutoJoinUntilFirstUserJoin.cold.1
+ _WiFiNetworkGetAccessoryIdentifier.cold.1
+ _WiFiNetworkGetBundleIdentifier.cold.1
+ _WiFiNetworkGetCarPlayInternetCheckState
+ _WiFiNetworkGetChannel.cold.1
+ _WiFiNetworkGetChannelFlags.cold.1
+ _WiFiNetworkGetChannelWidthInMHz.cold.1
+ _WiFiNetworkGetChannelWidthInMHz.cold.2
+ _WiFiNetworkGetDisabledUntilDate.cold.1
+ _WiFiNetworkGetDisplayFriendlyName.cold.1
+ _WiFiNetworkGetHarvestSSIDStatus.cold.1
+ _WiFiNetworkGetLOIType.cold.1
+ _WiFiNetworkGetLOIType.cold.2
+ _WiFiNetworkGetLastHomeForceFixDate.cold.1
+ _WiFiNetworkGetNetworkOfInterestHomeType.cold.1
+ _WiFiNetworkGetNetworkOfInterestWorkType.cold.1
+ _WiFiNetworkGetOriginator.cold.1
+ _WiFiNetworkGetPasswordModificationDate.cold.1
+ _WiFiNetworkGetPrivacyProxyBlockedReason.cold.1
+ _WiFiNetworkGetProperty.cold.1
+ _WiFiNetworkGetProperty.cold.2
+ _WiFiNetworkIs6EModeOff.cold.1
+ _WiFiNetworkIsAPLeaky.cold.1
+ _WiFiNetworkIsCarPlay.cold.1
+ _WiFiNetworkIsCarPlay.cold.2
+ _WiFiNetworkIsCarrierBundleBased.cold.1
+ _WiFiNetworkIsExpirable.cold.1
+ _WiFiNetworkIsLowUserPreferenceNetwork
+ _WiFiNetworkIsWAC.cold.1
+ _WiFiNetworkIsWAC.cold.2
+ _WiFiNetworkListRecordsAreEqual
+ _WiFiNetworkMergeAutoJoinProperties.cold.1
+ _WiFiNetworkMergeAutoJoinProperties.cold.2
+ _WiFiNetworkRemoveAutoJoinProperties.cold.1
+ _WiFiNetworkRemoveInternalProperties.cold.1
+ _WiFiNetworkSetAccessoryIdentifier.cold.1
+ _WiFiNetworkSetCarPlayInternetCheckState
+ _WiFiNetworkSetDisplayFriendlyName.cold.1
+ _WiFiNetworkSetLastHomeForceFixDate.cold.1
+ _WiFiNetworkSetLastHomeForceFixDate.cold.2
+ _WiFiNetworkSetLastHomeForceFixDate.cold.3
+ _WiFiNetworkSetOriginatorName.cold.1
+ _WiFiNetworkSetPasswordModificationDate.cold.1
+ _WiFiNetworkSetPasswordModificationDate.cold.2
+ _WiFiNetworkSetPasswordModificationDate.cold.3
+ _WiFiNetworkSetPrivacyProxyBlockedReason.cold.1
+ _WiFiNetworkSetPrivacyProxyEnabled.cold.1
+ _WiFiNetworkSetProperty.cold.1
+ _WiFiNetworkSetProperty.cold.2
+ _WiFiNetworkSetPublicAirPlayNetwork.cold.1
+ _WiFiSecurityCopyAttributesForAllAirPortEntries.cold.1
+ _WiFiSecurityCopyPasswordModificationDate.cold.1
+ _WiFiSecurityIsPasswordSyncing.cold.1
+ _WiFiSecuritySetPasswordWithTimeout.cold.1
+ _WiFiSecuritySetPasswordWithTimeout.cold.2
+ _WiFiSecuritySetPasswordWithTimeout.cold.3
+ _WiFiSecuritySetPasswordWithTimeout.cold.4
+ _WiFiSecuritySetPasswordWithTimeout.cold.5
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSString_$_Utilities
+ __OBJC_$_CATEGORY_NSString_$_Utilities
+ __WiFiDeviceClientDispatchResetInterfaceEvent
+ __WiFiDeviceClientDispatchRoamBasedCellDupRecStartEvent
+ __WiFiDeviceClientDispatchRoamBasedCellDupRecStopEvent
+ __WiFiManagerClientGetCoreWiFiInterface.cold.1
+ ___WiFiNetworkCreateCoreWiFiNetworkProfile
+ ___WiFiNetworkCreateCoreWiFiNetworkProfile.cold.1
+ ___WiFiNetworkCreateCoreWiFiScanResult
+ ___WiFiNetworkCreateFromCoreWiFiNetworkProfile
+ ___WiFiNetworkCreateFromCoreWiFiScanResult
+ ___WiFiSecurityCreateQuery.cold.1
+ ___WiFiSecurityCreateQuery.cold.2
+ ___WiFiSecurityRemovePassword.cold.1
+ ___WiFiSecurityRemovePassword.cold.2
+ ___WiFiSecuritySavePasswordForPasswordBackup_block_invoke.18
+ ___WiFiSecuritySetPassword.cold.1
+ ___WiFiSecuritySetPassword.cold.2
+ ___WiFiSecuritySetPassword.cold.3
+ ___WiFiSecuritySetPassword.cold.4
+ ___WiFiSecuritySetPassword.cold.5
+ ___block_descriptor_72_e8_32o40r48r56r_e5_v8?0lr40l8r48l8r56l8s32l8
+ __os_log_send_and_compose_impl
+ __wifi_manager_client_dispatch_event.cold.7
+ _kWiFiAONTightbeamSentCreateInfraInterfaceKey
+ _kWiFiAONTightbeamSentCreateNanInterfaceKey
+ _kWiFiInternetSharingNetworkName
+ _kWiFiJoinPMAssertionResetIntervalKey
+ _kWiFiJoinPMAssertionResetTimestampKey
+ _kWiFiJoinPMAssertionTimeUsedKey
+ _kWiFiNetworkAttributeIsLowUserPreference
+ _kWiFiUserInteractionMonitorNetworkAgentAssertCountKey
+ _kWiFiUserInteractionMonitorSiriSessionKey
+ _objc_autoreleaseReturnValue
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$arrayWithCapacity:
+ _objc_msgSend$carPlayCheckForInternetConductedAt
+ _objc_msgSend$carPlayCheckForInternetState
+ _objc_msgSend$componentsJoinedByString:
+ _objc_msgSend$componentsSeparatedByString:
+ _objc_msgSend$hasPrefix:
+ _objc_msgSend$isCarPlayNetwork
+ _objc_msgSend$isEAP
+ _objc_msgSend$isPSK
+ _objc_msgSend$lowQualityAttribute
+ _objc_msgSend$lowUserPreferenceAttribute
+ _objc_msgSend$numberWithInteger:
+ _objc_msgSend$objectAtIndexedSubscript:
+ _objc_msgSend$setCarPlayCheckForInternetConductedAt:
+ _objc_msgSend$setCarPlayCheckForInternetState:
+ _objc_msgSend$setLowQualityAttribute:
+ _objc_msgSend$setLowUserPreferenceAttribute:
+ _objc_msgSend$setObject:atIndexedSubscript:
+ _objc_msgSend$stringByAppendingString:
+ _objc_msgSend$substringFromIndex:
+ _objc_release
+ _objc_release_x22
+ _objc_release_x23
+ _objc_release_x24
+ _objc_release_x25
+ _objc_release_x26
+ _objc_release_x27
+ _objc_release_x28
+ _objc_retain
+ _objc_retainAutorelease
+ _objc_retain_x19
+ _objc_retain_x20
+ _objc_retain_x24
+ _objc_retain_x8
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
- GCC_except_table244
- GCC_except_table245
- GCC_except_table246
- GCC_except_table253
- _MGGetProductType
- _WiFiManagerClientIsWiFiAlwaysOnSupported
- _WiFiManagerClientRemoveNetworkWithReason.cold.1
- _WiFiNetworkCreateCoreWiFiNetworkProfile.cold.1
- _WiFiNetworkCreateFromCoreWiFiScanResult.cold.1
- _WiFiNetworkPrivateMacNetworkType.cold.1
- ___WiFiSecuritySavePasswordForPasswordBackup_block_invoke.31
- ___block_descriptor_64_e8_32o40r48r_e5_v8?0lr40l8r48l8s32l8
- ___getCWFBSSClass_block_invoke
- ___getCWFBSSClass_block_invoke.cold.1
- ___getCWFChannelClass_block_invoke
- ___getCWFChannelClass_block_invoke.cold.1
- _getCWFBSSClass.softClass
- _getCWFChannelClass
- _getCWFChannelClass.softClass
- _getCWFScanResultPropertyOSSpecificAttributesKey
- _getCWFScanResultPropertyOSSpecificAttributesKey.cold.1
- _objc_autorelease
CStrings:
+ "%s - _WiFiCreateNetworksFromRecords failed"
+ "%s : Callback is null"
+ "%s : Current channel %d\n"
+ "%s CFNumberCreate failed"
+ "%s Error result %d"
+ "%s RSN auth type (%d) has no RSN IE"
+ "%s WPA auth type (%d) has no WPA IE"
+ "%s is called."
+ "%s no params"
+ "%s unhandled type trying to convert from apple8021_access_network_t -> WiFiAdvertisedNetworkType"
+ "%s: %@ - bcnloss:%d (%d %d) trgDisc:%d (%d %d)"
+ "%s: %@, %.3f %{public}@"
+ "%s: %@, %d"
+ "%s: %d, network <%@>, type %d"
+ "%s: Attempting to fetch non-syncable password for account %@"
+ "%s: BSS late roam data - %@ current BSS: %@"
+ "%s: BSS updated - current BSS: %@ (%{public}@)"
+ "%s: BSS updated - current BSS: %@ (awdl=%{public}@)"
+ "%s: BT MAC found in Apple IE %02X:%02X:%02X:%02X:%02X:%02X"
+ "%s: CFPropertyListCreateWithData returned with error %{public}@"
+ "%s: Cannot copy password for %@. Device wasn't unlocked yet"
+ "%s: Cannot get all airport keychain attributes. Device wasn't unlocked yet"
+ "%s: Cannot get keychain attributes for %@. Device wasn't unlocked yet"
+ "%s: Clearing disable-until property for SSID '%@'"
+ "%s: Creating new Late Roam Info %@ - %@"
+ "%s: Error: Empty password for account %@"
+ "%s: Failed to create CFNumber while setting NetworkAtLocationOfInterestType=%d"
+ "%s: Failed to create newBssDict"
+ "%s: Failed to create newBssList"
+ "%s: Failed to create newLateRoamInfoDict"
+ "%s: Failed to create newMaxDeltaRef"
+ "%s: Failed to create newMinDeltaRef"
+ "%s: Failed to get BSSID from %@"
+ "%s: Failed to get kWiFiNetworkAtLocationOfInterestTypeKey"
+ "%s: Found APPLE80211KEY_LEAKY_AP_LEARNED_DATA for network %@"
+ "%s: HS 2.0 account name from WiFiNetworkGetProperty() is %@"
+ "%s: HS20 - found matching attribute in GAS response - ssid1: %@, account1 %@; ssid2: %@, account: %@"
+ "%s: HS20 - ssid1: %@, account1: %@, domain1: %@; ssid2: %@, account2: %@, domain2: %@, GAS check: %d"
+ "%s: Invalid bundleId"
+ "%s: Network %@ is a WAC network"
+ "%s: Network is AllowedBeforeFirstUnlock but NOT setting the flag. Network is not profile-based."
+ "%s: Password for EAP profile NULL after fetch by account name and normal method, attempting password fetch by domain name "
+ "%s: Password for EAP profile still NULL after attempted fetch by domain name"
+ "%s: REMOVE password for %@"
+ "%s: Removed known BSS from index %ld"
+ "%s: Removing APPLE80211KEY_LEAKY_AP_LEARNED_DATA for network %@"
+ "%s: Removing password for %@"
+ "%s: Request already in progress"
+ "%s: SSID not valid length"
+ "%s: SSIDs match (%@), but networks have different HS20 properties."
+ "%s: Same SSID HS20 networks - network1: %@ (domain='%@'), network2: %@ (domain='%@')"
+ "%s: Set password not syncable for %@"
+ "%s: Setting HS 2.0 account name to %@ for network %@"
+ "%s: Setting NetworkLocationOfInterestType=%{public}@(%d) for %@"
+ "%s: Skip GAS content check for domainName %@ and domainName %@"
+ "%s: Unknown event type %llu dropping"
+ "%s: Updated BSS late roam data - %@ current BSS: %@"
+ "%s: WiFiNetworkIsAllowedBeforeFirstUnlock returned false. Network: %@"
+ "%s: __WiFiNetworkCopyPasswordForAccount() returned a %s password"
+ "%s: bad ieList type %ld"
+ "%s: bad record type %ld"
+ "%s: build array failed for mode (%d)"
+ "%s: build number failed for mode(%d)"
+ "%s: changes dictionary is null"
+ "%s: data at path %{public}@ is nil"
+ "%s: dispatching roamBasedCellDupRecStart callback (reason=lowRSSI)"
+ "%s: eventInfo dictionary is null"
+ "%s: failed to create CoreWiFi interface for CWFServiceTypeMobileWiFi"
+ "%s: failed to create query"
+ "%s: failed to create query for %@"
+ "%s: failed to get BSSID from %@"
+ "%s: for account %@"
+ "%s: for network <%@>,  modDate %{public}@"
+ "%s: found matching domain %@ on two accounts. Accounts are %@ and %@"
+ "%s: found matching domain name %@ in GAS response from scannedNetwork, marking %@ provisioned"
+ "%s: found response from 3GPP %@, marking %@ provisioned"
+ "%s: found response from NAI Realm %@, marking %@ provisioned"
+ "%s: found response from Roaming Consortium %@, marking %@ provisioned"
+ "%s: invalid EAP client configuration"
+ "%s: invalid bundle identifier given"
+ "%s: invalid geoTags"
+ "%s: invalid manager"
+ "%s: invalid network provided"
+ "%s: invalid network ref"
+ "%s: invalid server port"
+ "%s: invalid value buffer"
+ "%s: invalid value type"
+ "%s: known BSS list has grown beyond maximum. Removing %@"
+ "%s: known BSS stats for %@ - num. of BSS = %ld"
+ "%s: localeStats is NULL"
+ "%s: missing encrypted identity key"
+ "%s: moved leaky AP info to bss dictionary"
+ "%s: network %@ path %{public}@"
+ "%s: nil movementStates"
+ "%s: nil networks"
+ "%s: nil records"
+ "%s: nil scoreDict"
+ "%s: no eapProfile for %@"
+ "%s: no knownBssids"
+ "%s: null APPLE80211KEY_CHANNEL_WIDTH"
+ "%s: null account"
+ "%s: null bssid"
+ "%s: null bssidFromNetwork"
+ "%s: null destNetwork"
+ "%s: null eventDict."
+ "%s: null expire date, removing property"
+ "%s: null knownBssids"
+ "%s: null leaky number"
+ "%s: null modDate"
+ "%s: null network"
+ "%s: null network record"
+ "%s: null network record."
+ "%s: null network."
+ "%s: null networkRecord"
+ "%s: null networkRef"
+ "%s: null query"
+ "%s: null simId"
+ "%s: null srcNetwork"
+ "%s: null stateRef"
+ "%s: out of range value for key \"%{public}@\""
+ "%s: passwordFetchTimedOut: %d and keychainPassword is: %s"
+ "%s: passwordFetchTimedOut: %d, keychainPassword is: %s"
+ "%s: path is nil"
+ "%s: preserved disabledUntil for %@ network with %{public}@"
+ "%s: preserving all AJ-disabled-related properties for network %@"
+ "%s: record is of type %ld!!"
+ "%s: records is NULL"
+ "%s: records is of type %ld!!"
+ "%s: request is NULL!"
+ "%s: request:%{public}@"
+ "%s: retrieved %.3f"
+ "%s: retrieved %{public}@"
+ "%s: roaming is disabled for account %@"
+ "%s: roaming is enabled for account %@"
+ "%s: scanRequest is NULL"
+ "%s: scanRequest is of type %ld!!"
+ "%s: serialization failed"
+ "%s: skip %{public}@ merge for hs20 network %@"
+ "%s: skipping roamBasedCellDupRecStart callback (reason=%u is not lowRSSI)"
+ "%s: successfully prepared known BSS info for %@ (bssid: %@, channel: %{public}@)"
+ "%s: testParams:%{public}@"
+ "%s: unable to archive network dictionary"
+ "%s: unable to archive network dictionary in %{public}@"
+ "%s: unable to create WiFiNetworkRef at path %{public}@"
+ "%s: unable to create directory at path %{public}@"
+ "%s: updated known BSS list after removal - %@"
+ "%s: valueBuffer or valueBufferSize is NULL"
+ "%s:%d found MCCMNC in account %@"
+ "%s:%d found NAI Realm in accounts %@"
+ "%s:%d found NaiRealmArray count %ld %@"
+ "%s:%d found Roaming Consortium OI in accounts %@"
+ "%s:%d found RoamingConsortiumArray count %ld %@"
+ "%s:%d found cellInfoArray count %ld %@"
+ "%s:SecItemCopyMatching timed out, timeout %f\n"
+ "%s:[%@] Error result %d"
+ "%s:[%@] Error result %d \n"
+ "0"
+ ":"
+ "Both (%@) and (%@) force fixed. Preferred (1), the most recently force fixed: %@"
+ "Both (%@) and (%@) force fixed. Preferred (2), the most recently force fixed: %@"
+ "CarPlayInternetCheckConducted"
+ "CarPlayInternetCheckState"
+ "Disassoc due to partial Connectivity"
+ "FirstJoinWithNewMacTimestamp"
+ "Incorrect reason code, bailing out!"
+ "IsSiriSessionActive"
+ "LinkDownTimestamp"
+ "MacGenerationTimeStamp"
+ "Missing WiFiDeviceClientRef"
+ "NOI (1) '%@' has home-state"
+ "NOI (1) '%@' is forced-fix"
+ "NOI (1) forced-fix: preferred (1) %@ over %@"
+ "NOI (2) '%@' has home-state"
+ "NOI (2) forced-fix: Preferred (2) %@ over %@"
+ "NOI home-state: Preferred (2) %@ over %@"
+ "NOI home-state: preferred (1) %@ (as it's profile based) over %@"
+ "NOI home-state: preferred (1) %@ over %@"
+ "NOI home-state: preferred (1) %@ over %@ (which has no kWiFiPreferenceAddedAtKey)"
+ "NOI home-state: preferred (1) %@ over %@. %@ was added after %@"
+ "NOI home-state: preferred (2) %@ (as it's profile based) over %@"
+ "NOI home-state: preferred (2) %@ over %@ (which has no kWiFiPreferenceAddedAtKey)"
+ "NOI home-state: preferred (2) %@ over %@. %@ was added after %@"
+ "NOI: Profile based network (%@) was added AFTER network was force fixed  (%@), prefer profile based "
+ "NOI: Profile based network (%@) was added BEFORE network was force fixed (%@), prefer force fixed network "
+ "Network %@ Both autojoin and user join dates are NULL"
+ "NetworkAgentAssertCount"
+ "Preferences SpringBoard Carousel WiFiPickerExtens Setup budd sharingd demod BundledIntentHandler SiriViewService assistantd assistant_service Siri SettingsIntentExtension NanoSettings PineBoard TVSettings SoundBoard RealityControlCenter MuseBuddyApp mobilewifitool WirelessStress coreautomationd hrmwifid hermeswifid wifiutil NanoWiFiViewService ATKWiFiFramework WiFiViewService hQT XCTestInternalAngel HPSetup AirPlaySenderUIApp TVSetup deviceaccessd AccessorySetupUI Setup RealityCoverSheet WiFiProxUI"
+ "ROAM_SCAN_REASON"
+ "SCError Unavailable"
+ "SCPreferencesApplyChanges() %s"
+ "SCPreferencesCommitChanges() %s"
+ "SCPreferencesLock() %s"
+ "SCPreferencesUnlock() %s"
+ "WiFiAONTightbeamSentCreateInfraInterface"
+ "WiFiAONTightbeamSentCreateNanInterface"
+ "WiFiCoreWiFiUtil.m"
+ "WiFiDeviceClientAutoJoinBlacklistCommand"
+ "WiFiDeviceClientBssBlacklistCommandAndCopyResponse"
+ "WiFiDeviceClientCopyAirplayStatistics is unsupported"
+ "WiFiDeviceClientDestroyEAPTrustExceptionsForCurrentNetwork"
+ "WiFiDeviceClientNotifySoftError"
+ "WiFiDeviceClientSendWoWBlacklistCommandAndCopyResponse"
+ "WiFiGetPrivateMacNetworkIndices"
+ "WiFiInternetSharingNetworkName"
+ "WiFiJoinPMAssertionResetInterval"
+ "WiFiManagerClientAddNetworkAsync"
+ "WiFiManagerClientCopyGeoTagsForNetwork"
+ "WiFiManagerClientCopyKnownNetworksNearLocation"
+ "WiFiManagerClientCopyLocaleStats"
+ "WiFiManagerClientCopyMovementStates"
+ "WiFiManagerClientCopyNetworksWithBundleIdentifier"
+ "WiFiManagerClientCopyScoreForNetwork"
+ "WiFiManagerClientCopyScoreSortedKnownNetworksNearLocation"
+ "WiFiManagerClientGetAirplaneModePowerPreference"
+ "WiFiManagerClientGetHardwareFailure"
+ "WiFiManagerClientPurgeExpiredKnownNetworks"
+ "WiFiManagerClientRemoveNetworkWithReason"
+ "WiFiManagerClientRemoveNetworksWithBundleIdentifier"
+ "WiFiManagerClientResetNetworkSettings"
+ "WiFiManagerClientSetAirplaneModePowerPreference"
+ "WiFiManagerClientSetGeoTagForNetwork"
+ "WiFiManagerClientSetInCarState"
+ "WiFiManagerClientSetSimulatedMovementStates"
+ "WiFiManagerClientSetTestParamsAndCopyResponse"
+ "WiFiManagerClientSetUserInteractionNwOverride"
+ "WiFiManagerClientSetUserInteractionOverride"
+ "WiFiManagerClientSimulateNotification"
+ "WiFiManagerClientWiFiCallHandoverNotification"
+ "WiFiNetworkAddBundleIdentifier"
+ "WiFiNetworkAddOriginator"
+ "WiFiNetworkAddSIMIdentifier"
+ "WiFiNetworkArchiveToPath"
+ "WiFiNetworkAttributeIsLowUserPreference"
+ "WiFiNetworkCanExposeIMSI"
+ "WiFiNetworkCopyFilteredRecordForClassDStorage"
+ "WiFiNetworkCopyKeychainModDate"
+ "WiFiNetworkCopyLeakyStatus"
+ "WiFiNetworkCopyPreparedEAPProfile"
+ "WiFiNetworkCreateFromPath"
+ "WiFiNetworkCreateWithSsid"
+ "WiFiNetworkDisableAutoJoinUntilFirstUserJoin"
+ "WiFiNetworkFoundNanIe"
+ "WiFiNetworkGetAccessoryIdentifier"
+ "WiFiNetworkGetAdvertisedNetworkType"
+ "WiFiNetworkGetBundleIdentifier"
+ "WiFiNetworkGetCIntProperty"
+ "WiFiNetworkGetCarrierPayloadIdentifierTelemetryApproved"
+ "WiFiNetworkGetChannel"
+ "WiFiNetworkGetChannelFlags"
+ "WiFiNetworkGetChannelWidthInMHz"
+ "WiFiNetworkGetDisabledUntilDate"
+ "WiFiNetworkGetDisplayFriendlyName"
+ "WiFiNetworkGetExpireDate"
+ "WiFiNetworkGetForcedHomeFix"
+ "WiFiNetworkGetHarvestSSIDStatus"
+ "WiFiNetworkGetInt16Property"
+ "WiFiNetworkGetInt32Property"
+ "WiFiNetworkGetLOIType"
+ "WiFiNetworkGetLastHomeForceFixDate"
+ "WiFiNetworkGetNetworkOfInterestHomeType"
+ "WiFiNetworkGetNetworkOfInterestWorkType"
+ "WiFiNetworkGetNetworkQualityDate"
+ "WiFiNetworkGetNetworkQualityResponsiveness"
+ "WiFiNetworkGetOriginator"
+ "WiFiNetworkGetPasswordModificationDate"
+ "WiFiNetworkGetPrivacyProxyBlockedReason"
+ "WiFiNetworkGetPrivacyProxyEnabled"
+ "WiFiNetworkGetProperty"
+ "WiFiNetworkIs24GHzNetwork"
+ "WiFiNetworkIs6EModeOff"
+ "WiFiNetworkIsAPLeaky"
+ "WiFiNetworkIsAllowedBeforeFirstUnlock"
+ "WiFiNetworkIsApplePersonalHotspot"
+ "WiFiNetworkIsAutoJoinDisabledUntilFirstUserJoin"
+ "WiFiNetworkIsCarPlay"
+ "WiFiNetworkIsCarrierBundleBased"
+ "WiFiNetworkIsExpirable"
+ "WiFiNetworkIsInfrequentlyJoinedPublicNetwork"
+ "WiFiNetworkIsNanPH"
+ "WiFiNetworkIsPublicAirPlayNetwork"
+ "WiFiNetworkIsScannedNetworkMatchingHS20Account"
+ "WiFiNetworkIsWAC"
+ "WiFiNetworkIsWoWAllowed"
+ "WiFiNetworkMergeAutoJoinProperties"
+ "WiFiNetworkMergeForAssociation"
+ "WiFiNetworkMergeProperties"
+ "WiFiNetworkPrepareKnownBssList"
+ "WiFiNetworkRemoveAutoJoinProperties"
+ "WiFiNetworkRemoveBssFromKnownList"
+ "WiFiNetworkRemoveInternalProperties"
+ "WiFiNetworkRemoveSIMIdentifier"
+ "WiFiNetworkSetAccessoryIdentifier"
+ "WiFiNetworkSetBSSAWDLRealTimeModeTimestamp"
+ "WiFiNetworkSetBSSLocation"
+ "WiFiNetworkSetBSSProperty"
+ "WiFiNetworkSetBssDisconnectReason"
+ "WiFiNetworkSetBssLateRoamInfo"
+ "WiFiNetworkSetDisabledUntilDate"
+ "WiFiNetworkSetDisplayFriendlyName"
+ "WiFiNetworkSetExpireDate"
+ "WiFiNetworkSetForcedHomeFix"
+ "WiFiNetworkSetKnownBssUsageData"
+ "WiFiNetworkSetLOIType"
+ "WiFiNetworkSetLastHomeForceFixDate"
+ "WiFiNetworkSetNetworkQuality"
+ "WiFiNetworkSetOriginatorName"
+ "WiFiNetworkSetPasswordModificationDate"
+ "WiFiNetworkSetPrivacyProxyBlockedReason"
+ "WiFiNetworkSetPrivacyProxyEnabled"
+ "WiFiNetworkSetProperty"
+ "WiFiNetworkSetPublicAirPlayNetwork"
+ "WiFiNetworkUpdateWPARSNAuthType"
+ "WiFiSecurityCopyAttributesForAllAirPortEntries"
+ "WiFiSecurityCopyNonSyncablePassword"
+ "WiFiSecurityCopyNonSyncablePasswordWithTimeout"
+ "WiFiSecurityCopyNonSyncablePasswordWithTimeout_block_invoke"
+ "WiFiSecurityCopyPasswordModificationDate"
+ "WiFiSecurityCopyPasswordWithTimeout"
+ "WiFiSecurityCopyPasswordWithTimeout_block_invoke"
+ "WiFiSecurityIsPasswordSyncing"
+ "WiFiSecurityRemovePassword"
+ "WiFiSecuritySetPasswordWithTimeout"
+ "[corewifi] %{public}s (%{public}s:%u) saving %@ as %@"
+ "_WiFiDeviceClientDispatch24GHzNetworkInCriticalStateEvent"
+ "_WiFiDeviceClientDispatchBTScanIntervalRelaxEvent"
+ "_WiFiDeviceClientDispatchCarPlayNetworkTypeChangeEvent"
+ "_WiFiDeviceClientDispatchCatsUpdateEvent"
+ "_WiFiDeviceClientDispatchM1M4Handshake24GHzCountEvent"
+ "_WiFiDeviceClientDispatchP2pThreadCoexEvent"
+ "_WiFiDeviceClientDispatchRoamBasedCellDupRecStartEvent"
+ "_WiFiDeviceClientDispatchScanCacheUpdateEvent"
+ "_WiFiDeviceClientDispatchScanUpdateEvent"
+ "_WiFiDeviceClientDispatchTdConfirmedEvent"
+ "_WiFiManagerClientGetCoreWiFiInterface"
+ "__WiFiIsSameHS20Account"
+ "__WiFiManagerClientSetNetworksStateWithBundleIdentifier"
+ "__WiFiNetworkCopyPasswordForAccount"
+ "__WiFiNetworkCreateCoreWiFiNetworkProfile"
+ "__WiFiNetworkCreateFromCoreWiFiNetworkProfile"
+ "__WiFiNetworkEqual"
+ "__WiFiNetworkEqualIgnoreAuthType"
+ "__WiFiNetworkGetBtMacFromIe"
+ "__WiFiNetworkIsAppleDevice"
+ "__WiFiNetworkIsRecordValid"
+ "__WiFiNetworkIsWoWAllowed"
+ "__WiFiSecurityCopyPassword"
+ "__WiFiSecurityCreateQuery"
+ "__WiFiSecurityCreateWildcardAttributeQuery"
+ "__WiFiSecurityRemovePassword"
+ "__WiFiSecuritySetPassword"
+ "_wifi_manager_client_dispatch_event"
+ "_wifi_manager_client_dispatch_preferred_networks_change"
+ "_wifi_manager_client_dispatch_scan_results"
+ "_wifi_manager_client_dispatch_ui_event"
+ "joinPMAssertionResetTimestamp"
+ "joinPMAssertionTimeUsedKey"
+ "non-null"
+ "null"
+ "server_port is null\n"
- "%s: always on wifi %s"
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"SFPasswordSharingService\""
- "@16@0:8"
- "@?"
- "B32@0:8@\"SFPasswordSharingService\"16@\"NSString\"24"
- "B32@0:8@16@24"
- "BSSList"
- "CWFBSS"
- "CWFChannel"
- "Class getCWFBSSClass(void)_block_invoke"
- "Class getCWFChannelClass(void)_block_invoke"
- "DNSHeuristicsFailureStateInfo"
- "EAPProfile"
- "NAIRealmNameList"
- "NANServiceID"
- "OSSpecificAttributes"
- "Preferences SpringBoard Carousel WiFiPickerExtens Setup budd sharingd demod BundledIntentHandler SiriViewService assistantd assistant_service Siri SettingsIntentExtension NanoSettings PineBoard TVSettings SoundBoard RealityControlCenter MuseBuddyApp mobilewifitool WirelessStress coreautomationd wifiutil NanoWiFiViewService ATKWiFiFramework WiFiViewService hQT XCTestInternalAngel HPSetup AirPlaySenderUIApp TVSetup deviceaccessd AccessorySetupUI Setup RealityCoverSheet"
- "SFPasswordSharingServiceDelegate"
- "UTF8String"
- "WAPISubtype"
- "WEPSubtype"
- "WiFiManagerClientIsWiFiAlwaysOnSupported"
- "WiFiPasswordSharingSimulator"
- "_queue"
- "_replyHandler"
- "_service"
- "activate"
- "addEntriesFromDictionary:"
- "addObject:"
- "addReason"
- "allowedBeforeFirstUnlock"
- "appendFormat:"
- "array"
- "arrayByAddingObjectsFromArray:"
- "arrayWithObjects:count:"
- "beginTransaction:completionHandler:"
- "cStringUsingEncoding:"
- "captiveProfile"
- "carplayUUID"
- "cellularNetworkInfo"
- "channel"
- "clearTrafficRegistration:error:"
- "code"
- "containsObject:"
- "contentsAtPath:"
- "coordinate"
- "copy"
- "coreWiFiSpecificAttributes"
- "countByEnumeratingWithState:objects:count:"
- "createDirectoryAtPath:withIntermediateDirectories:attributes:error:"
- "createFileAtPath:contents:attributes:"
- "currentCalendar"
- "currentHandler"
- "dataUsingEncoding:"
- "dataWithPropertyList:format:options:error:"
- "dealloc"
- "defaultManager"
- "dictionary"
- "dictionaryWithObjects:forKeys:count:"
- "displayedOperatorName"
- "domainName"
- "doubleValue"
- "drain"
- "endTransaction:"
- "expirationDate"
- "fileExistsAtPath:"
- "flags"
- "handleFailureInFunction:file:lineNumber:description:"
- "hiddenState"
- "horizontalAccuracy"
- "init"
- "initWithCapacity:"
- "initWithCoordinate:altitude:horizontalAccuracy:verticalAccuracy:timestamp:"
- "initWithDictionary:isActive:"
- "initWithFormat:"
- "initWithScanRecord:includeProperties:"
- "initWithServiceType:"
- "intValue"
- "integerValue"
- "invalidate"
- "isAllowedInLockdownMode"
- "isAutoJoinDisabled"
- "isDNSHeuristicsFilteredNetwork"
- "isOpen"
- "isPasswordSharingDisabled"
- "isPayloadIdentifierTelemetryApproved"
- "isPersonalHotspot"
- "isPrivacyProxyEnabled"
- "isProfileBased"
- "isPublicAirPlayNetwork"
- "isServiceProviderRoamingEnabled"
- "isStandalone6G"
- "isWPA2"
- "lastAssociatedAt"
- "lastDiscoveredAt"
- "lastJoinedBySystemAt"
- "lastJoinedByUserAt"
- "length"
- "location"
- "logRedactionDisabled"
- "lowDataMode"
- "matchingKnownNetworkProfile"
- "movingAttribute"
- "mutableCopy"
- "networkName"
- "networkOfInterestHomeState"
- "networkOfInterestWorkState"
- "nextDateAfterDate:matchingComponents:options:"
- "not supported"
- "numberWithBool:"
- "numberWithDouble:"
- "numberWithInt:"
- "numberWithUnsignedInt:"
- "numberWithUnsignedInteger:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "payloadIdentifier"
- "payloadUUID"
- "privacyProxyBlockedReason"
- "propertyListWithData:options:format:error:"
- "psk"
- "publicAttribute"
- "roamingConsortiumList"
- "runWithSSID:reply:"
- "scanRecord"
- "service:receivedNetworkInfo:"
- "service:shouldPromptForNetwork:"
- "set"
- "setAWDLRealTimeModeTimestamp:"
- "setAddReason:"
- "setAddedAt:"
- "setAllowedBeforeFirstUnlock:"
- "setAutoJoinDisabled:"
- "setBSSID:"
- "setBSSList:"
- "setBundleID:"
- "setCaptiveProfile:"
- "setCarplayNetwork:"
- "setCarplayUUID:"
- "setCellularNetworkInfo:"
- "setChannel:"
- "setColocated2GHzRNRChannel:"
- "setColocated5GHzRNRChannel:"
- "setCoreWiFiSpecificAttributes:"
- "setDHCPServerID:"
- "setDHCPv6ServerID:"
- "setDNSHeuristicsFailureStateInfo:"
- "setDNSHeuristicsFilteredNetwork:"
- "setDelegate:"
- "setDictionary:"
- "setDispatchQueue:"
- "setDisplayedOperatorName:"
- "setDomainName:"
- "setEAPProfile:"
- "setExpirationDate:"
- "setFlags:"
- "setHiddenState:"
- "setHour:"
- "setIPv4NetworkSignature:"
- "setIPv6NetworkSignature:"
- "setInvalidationHandler:"
- "setLastAssociatedAt:"
- "setLastDiscoveredAt:"
- "setLastJoinedBySystemAt:"
- "setLastJoinedByUserAt:"
- "setLocation:"
- "setLowDataMode:"
- "setMinute:"
- "setMovingAttribute:"
- "setNAIRealmNameList:"
- "setNANServiceID:"
- "setNetworkGroupID:"
- "setNetworkGroupPriority:"
- "setNetworkName:"
- "setNetworkOfInterestHomeState:"
- "setNetworkOfInterestWorkState:"
- "setOSSpecificAttributes:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setPasswordSharingDisabled:"
- "setPayloadIdentifier:"
- "setPayloadUUID:"
- "setPersonalHotspot:"
- "setPrivacyProxyBlockedReason:"
- "setPrivacyProxyEnabled:"
- "setPublicAirPlayNetwork:"
- "setPublicAttribute:"
- "setRoamingConsortiumList:"
- "setSSID:"
- "setSecond:"
- "setServiceProviderRoamingEnabled:"
- "setStandalone6G:"
- "setSupportedSecurityTypes:"
- "setTrafficRegistration:error:"
- "setTransitionDisabledFlags:"
- "setUpdatedAt:"
- "setUserPreferredNetworkNames:"
- "setUserPreferredPasspointDomains:"
- "setWAPISubtype:"
- "setWEPSubtype:"
- "setWasHiddenBefore:"
- "shared"
- "stringByDeletingLastPathComponent"
- "stringWithCString:encoding:"
- "stringWithFormat:"
- "stringWithUTF8String:"
- "supported"
- "supportedOSSpecificKeys"
- "supportedSecurityTypes"
- "timeIntervalSinceReferenceDate"
- "transitionDisabledFlags"
- "unsignedIntValue"
- "unsignedIntegerValue"
- "updatedAt"
- "v16@0:8"
- "v32@0:8@\"SFPasswordSharingService\"16@\"SFPasswordSharingInfo\"24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "wasHiddenBefore"

```
