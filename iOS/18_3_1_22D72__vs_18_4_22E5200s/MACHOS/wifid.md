## wifid

> `/usr/sbin/wifid`

```diff

-1825.3.0.0.0
-  __TEXT.__text: 0x193dac
-  __TEXT.__auth_stubs: 0x2640
-  __TEXT.__objc_stubs: 0x11ee0
-  __TEXT.__objc_methlist: 0x53e0
-  __TEXT.__objc_methname: 0x17323
-  __TEXT.__objc_classname: 0x7f4
-  __TEXT.__objc_methtype: 0x2c03
-  __TEXT.__const: 0x920
-  __TEXT.__gcc_except_tab: 0x1c4c
-  __TEXT.__cstring: 0x697b8
+1925.41.0.0.0
+  __TEXT.__text: 0x1a7fb8
+  __TEXT.__auth_stubs: 0x2720
+  __TEXT.__objc_stubs: 0x12580
+  __TEXT.__objc_methlist: 0x60e8
+  __TEXT.__gcc_except_tab: 0x1c5c
+  __TEXT.__const: 0x8e0
+  __TEXT.__cstring: 0x6ad03
+  __TEXT.__objc_methname: 0x17cdb
+  __TEXT.__objc_classname: 0x83a
+  __TEXT.__objc_methtype: 0x2d53
   __TEXT.__ustring: 0x4c2
-  __TEXT.__oslogstring: 0xdd4
+  __TEXT.__oslogstring: 0x1117
   __TEXT.__dlopen_cstrs: 0x1a5
-  __TEXT.__unwind_info: 0x3668
-  __DATA_CONST.__auth_got: 0x1330
-  __DATA_CONST.__got: 0x1668
-  __DATA_CONST.__auth_ptr: 0x18
-  __DATA_CONST.__const: 0x7050
-  __DATA_CONST.__cfstring: 0x1cee0
-  __DATA_CONST.__objc_classlist: 0x1d0
+  __TEXT.__unwind_info: 0x3b18
+  __DATA_CONST.__auth_got: 0x13a0
+  __DATA_CONST.__got: 0x15d8
+  __DATA_CONST.__auth_ptr: 0x150
+  __DATA_CONST.__const: 0x6f90
+  __DATA_CONST.__cfstring: 0x1d3e0
+  __DATA_CONST.__objc_classlist: 0x1e8
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0xc8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x1b0
-  __DATA_CONST.__objc_intobj: 0xe40
-  __DATA_CONST.__objc_arraydata: 0x460
-  __DATA_CONST.__objc_dictobj: 0x140
-  __DATA_CONST.__objc_arrayobj: 0x108
+  __DATA_CONST.__objc_superrefs: 0x1c8
+  __DATA_CONST.__objc_intobj: 0xe28
+  __DATA_CONST.__objc_arraydata: 0x4b0
+  __DATA_CONST.__objc_dictobj: 0x1e0
+  __DATA_CONST.__objc_arrayobj: 0x120
   __DATA_CONST.__objc_floatobj: 0x10
-  __DATA.__objc_const: 0xd700
-  __DATA.__objc_selrefs: 0x52b0
-  __DATA.__objc_ivar: 0x92c
-  __DATA.__objc_data: 0x1220
-  __DATA.__data: 0x1078
-  __DATA.__bss: 0x7e8
-  __DATA.__common: 0x58
+  __DATA.__objc_const: 0xca40
+  __DATA.__objc_selrefs: 0x5730
+  __DATA.__objc_ivar: 0x984
+  __DATA.__objc_data: 0x1310
+  __DATA.__data: 0x1090
+  __DATA.__bss: 0x820
+  __DATA.__common: 0x5c
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /System/Library/PrivateFrameworks/CPMS.framework/CPMS
   - /System/Library/PrivateFrameworks/CaptiveNetwork.framework/CaptiveNetwork
   - /System/Library/PrivateFrameworks/CarKit.framework/CarKit
+  - /System/Library/PrivateFrameworks/CarPlayServices.framework/CarPlayServices
   - /System/Library/PrivateFrameworks/ChronoServices.framework/ChronoServices
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreRoutine.framework/CoreRoutine

   - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libpcap.A.dylib
-  Functions: 5482
-  Symbols:   1323
-  CStrings:  15643
+  Functions: 7508
+  Symbols:   1341
+  CStrings:  15917
 
Symbols:
+ _CFNumberGetType
+ _CFPropertyListCreateDeepCopy
+ _CFSetCreateMutableCopy
+ _IOConnectCallAsyncMethod
+ _IONotificationPortGetMachPort
+ _IORegistryEntrySetCFProperties
+ _IOServiceOpen
+ _OBJC_CLASS_$_CRSAppHistoryController
+ _OBJC_CLASS_$_NSLock
+ _OBJC_CLASS_$_WiFiRemoteClientCountryCodeMonitor
+ _OBJC_EHTYPE_$_NSException
+ _bcmp
+ _dispatch_queue_attr_make_with_qos_class
+ _dlopen
+ _kDHCPSPropDHCPLease
+ _kWAMessageKeyPrivateMacHomeNetwork
+ _memcmp
+ _objc_begin_catch
+ _objc_end_catch
+ _os_variant_is_recovery
- _OBJC_CLASS_$_AnalyticsProcessor
- _OBJC_CLASS_$_CWFAutoJoinManager
CStrings:
+ " %s: ajScanRejectedInAWDLRealTime:%d "
+ " reasonString=%@"
+ " subreason=0x%x"
+ " subreasonString=%@"
+ "%@: isHidden=%d, isEAP=%d, isSAE=%d, isWPA=%d, isWEP=%d, WAPI=%d, type=%d, enabled=%@, saveData=%@, responsiveness=%@ (%@) isHome=%@, isForceFixed=%d, transitionDisabledFlags=%@, foundNanIe=%d, isPH=%d, isPublicAirPlayNetwork=%d, is6EDisabled=%d, hs20=%d, Channel=%d, isBundleIdentifierPresent=%d, PolicyUUID=%@"
+ "%s : country code (%@), source (%d)\n"
+ "%s Ignore Previous Hotspot %@ type (%s) disconnect reason %d"
+ "%s Ignore Previous Hotspot %@ type (%s) disconnect time since linkDown %f"
+ "%s MIS was enabled beyond the time window allowed for recovery: %f"
+ "%s Max recovery attempts %lu reached, not allowing recovery"
+ "%s Network with SSID: %@ is undetermined."
+ "%s: %s LMTPC for CarPlay"
+ "%s: %s not found"
+ "%s: ABC snapshotWithSignature signature: %@"
+ "%s: AWDL timeSinceLastAwdlStatsPost:%d"
+ "%s: Activate power save"
+ "%s: Auto join enabled by %@"
+ "%s: CRSAppHistoryController is unavailable."
+ "%s: CarPlay network channel %lu, flags %x"
+ "%s: Client '%@' requested %ds rate limit for event %d"
+ "%s: DHCP lease <MacAddr/HostName/Lease>: <%@/%@/%@>"
+ "%s: Deactivate power save"
+ "%s: Detected a stale MIS discovery enable request from client: %@ isAllowlisted:%u"
+ "%s: Device in Lock state over %d minutes. Disconnect from Personal Hotspot!!"
+ "%s: ENTER"
+ "%s: Error returned from addAnalyticsValues, err = %d\n"
+ "%s: Error: IOConnectCallAsyncMethod failed with err=%d"
+ "%s: Error: IOServiceAddMatchingNotification %@ failed with err=%d"
+ "%s: Error: IOServiceOpen failed with err=%d"
+ "%s: Error: failed to create carPlayPowerSaveDeferral.timer"
+ "%s: Hotspot Recommendation notification skiped due to Band exclusion in AWDL realtime mode "
+ "%s: IORegistryEntrySetCFProperties failed with error %x\n"
+ "%s: IOServiceAddMatchingNotification kIOMatchedNotification for %s failed (%d)!."
+ "%s: IOServiceAddMatchingNotification kIOTerminatedNotification for %s failed (%d)!."
+ "%s: Initialization failed"
+ "%s: Joining back voluntarily disconnected PH within %u minutes after disconnect, time since link down %.1f seconds"
+ "%s: LEAVE"
+ "%s: MIS global state is disabled"
+ "%s: MIS idle timer already running, timer state :%d"
+ "%s: MIS is already enabled?"
+ "%s: MIS is in recovery. Driver is available. Cancelling MIS idle timer and restarting MIS network!"
+ "%s: MIS recovery is already in progress?"
+ "%s: ManagedConfiguration is not ready yet"
+ "%s: No password returned for %@ %s"
+ "%s: Power save deferral for CarPlay Bonjour HS timed out"
+ "%s: Re-enable auto join of network %@"
+ "%s: Reactivate power save"
+ "%s: Recovering MIS from Dext restart"
+ "%s: Recovering MIS from WiFid restart"
+ "%s: Resetting SoftAP state"
+ "%s: Saving MIS State"
+ "%s: Simulated LQM Dict: %@"
+ "%s: WiFiNetworkIsCarrierBundleBased %d TelemetryApproved %d PayloadIdentifier %@"
+ "%s: _ABCReporter failing to init, skipping submitting reasonString: %@ \n"
+ "%s: attempted copy password fetch returned, passwordFetchTimedOut: %d, password is: %s"
+ "%s: auto join of network %@ is disabled"
+ "%s: cleaning up."
+ "%s: cpuName %s crashID %llu"
+ "%s: crashReasonString for ID %@ not found"
+ "%s: data not found in %@"
+ "%s: dictionary for cpuName %@ not found"
+ "%s: existingNetwork %@ has CWF specific attributes"
+ "%s: failed to allocate CRSAppHistoryController"
+ "%s: failed to allocate inAnalyticsValues"
+ "%s: incorrect number of arguments (=%d)"
+ "%s: initABCReporter already exists \n"
+ "%s: initialized"
+ "%s: network properties after adding missing keys: %@"
+ "%s: network properties after modified network: %@"
+ "%s: nil args"
+ "%s: nil firmwareAssertTable"
+ "%s: nil type (bad args)"
+ "%s: preserving CWF properies on existing network"
+ "%s: reasonString: %@ ABC snapshot response: %@"
+ "%s: rssi(%d), cca(%d), snr(%d), txFail(%d), bw(%d), reason(%d), subreason(%d), channel(%@)"
+ "%s: timed out waiting for crashID notification, cleaning up."
+ "%s: unexpected value for %@"
+ "%s: unhandled argument type %llu"
+ "%s: value is null for %@"
+ "%s: watchdogMonitor already initialized, reinitializing ..."
+ "-[ManagedConfigWrapper isMegaWiFiProfileInstalled]"
+ "-[ManagedConfigWrapper isWiFiNetworkMDMNetwork:]"
+ "-[ManagedConfigWrapper isWiFiNetworkSubjectToMDM:]"
+ "-[WiFiDiagnosticReporter initABCReporter]"
+ "-[WiFiDiagnosticReporter submitWiFiWatchdogReason:subtypeContext:]"
+ "-[WiFiDiagnosticReporter submitWiFiWatchdogReason:subtypeContext:]_block_invoke"
+ "-[WiFiManagerLifeCycle startOnQueue:group:]"
+ "-[WiFiSoftApStateMonitor initState:]"
+ "-[WiFiSoftApStateMonitor init]"
+ "-[WiFiSoftApStateMonitor isMisRecoveryAllowed]"
+ "-[WiFiSoftApStateMonitor resetState]"
+ "-[WiFiWatchdogMonitor checkForTimeout]"
+ "-[WiFiWatchdogMonitor dealloc]"
+ "-[WiFiWatchdogMonitor handleCrashNotificationWithID:andCPUName:]"
+ "-[WiFiWatchdogMonitor handleWatchdogTriggered]"
+ "-[WiFiWatchdogMonitor initWithIOService:]"
+ "/System/Library/PrivateFrameworks/SymptomDiagnosticReporter.framework/SymptomDiagnosticReporter"
+ "@\"NSLock\""
+ "@\"NSObject<OS_os_transaction>\""
+ "@\"SDRDiagnosticReporter\""
+ "APPLE80211KEY_MWS_ACCESSORY_COEX_CONFIG"
+ "AWDL_TIME_SINCE_LAST_POST"
+ "AppleWLANDriver"
+ "AppleWLANWatchdog"
+ "BringUpMethod"
+ "BundledIntentHandler"
+ "CarrierPayloadIdentifierTelemetryApproved"
+ "Control Center Widget"
+ "CrashIDNotification"
+ "DHCPStartFailed"
+ "DiscoveryRequestedAt"
+ "DispatchRateLimitedLQM"
+ "EnableCarPlayJoinAfterInCar"
+ "FAILED to set Device Analytics config."
+ "Got exception: %@"
+ "MIS in recovery from dext/wifid crash. Using previously selected channel: %u"
+ "MIS is enabled"
+ "NOT checking ranging samples based on self/peer PHYErr/bitflips!"
+ "NonNullMISSession"
+ "PHBringUp"
+ "PayloadIdentifier"
+ "Personal Hotspot Connection Inactive"
+ "PersonalHotspotRecoveryFromDextCrash"
+ "PersonalHotspotRecoveryFromWiFidCrash"
+ "RTT[%ld]: Status=%d, RTT=%d RSSI=%d SNR=%d Core=%d BitFlip=%d PHYErr=0x%x(%s) Peer-SNR=%d Peer-BitFlip=%d Peer-PHYErr=0x%x(%s)"
+ "SDRDiagnosticReporter"
+ "Shortcuts"
+ "Siri"
+ "SubmitDiagnosticSignatureLazy"
+ "T@\"CWFAutoJoinManager\",R"
+ "T@\"NSDate\",&,N,V_misEnabledAt"
+ "T@\"NSDate\",&,N,V_watchdogStartedTimestamp"
+ "T@\"NSDictionary\",&,N,V_firmwareAssertTable"
+ "T@\"NSLock\",&,N,V_appAttributeLock"
+ "T@\"NSLock\",&,N,V_appTrackerLock"
+ "T@\"NSMutableSet\",&,N,V_pendingAppAttributeQueries"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_internalQ"
+ "TB,N,GisMisHidden,V_misIsHidden"
+ "TB,N,V_isStateValid"
+ "TB,N,V_misEnabled"
+ "TQ,N,V_misBandWidth"
+ "TQ,N,V_misChannel"
+ "TQ,N,V_recoveryAttempts"
+ "TQ,N,V_userPreferredBand"
+ "WatchdogTriggered"
+ "WiFi Watchdog"
+ "WiFiDeviceGetNANInterfaceName"
+ "WiFiDeviceManagerSaveMISStateIfInRecovery"
+ "WiFiDeviceManagerSetLocale"
+ "WiFiDiagnosticReporter"
+ "WiFiMISState"
+ "WiFiManager-1925.41 Feb 16 2025 13:46:10"
+ "WiFiManager-1925.41 Feb 16 2025 13:46:39"
+ "WiFiNetworkGetCarrierPayloadIdentifierTelemetryApproved"
+ "WiFiSoftApStateMonitor"
+ "WiFiUsageWatchdogDetailsSubmitToCA"
+ "WiFiWatchdogMonitor"
+ "WirelessRadioManagerd"
+ "[corewifi] %s: %@"
+ "[corewifi] %s: CWFInterface initWithServiceType: failed"
+ "[corewifi] %s: chip reset completed"
+ "[corewifi] %s: encountered join error %@, performing join retry..."
+ "[corewifi] %s: encountered multiple (%d) failures, performing chip reset before retrying (remaining time %ds)..."
+ "[corewifi] %s: find and join %@ failed with error %@"
+ "[corewifi] %s: invalid band specified (%d), forcing to 2.4GHz"
+ "[corewifi] %s: join %@ succeeded (error=%@)"
+ "[corewifi] %s: join completed, candidate=%@, error=%@"
+ "[corewifi] %s: last error (%@), retry expired=%s exceeded=%s"
+ "[corewifi] %s: no join candidate, performing scan retry..."
+ "[corewifi] %s: no match in scan results, performing scan retry..."
+ "[corewifi] %s: null network name"
+ "[corewifi] %s: request %@, supported channels:%@"
+ "[corewifi] %s: retry exhausted, exiting join phase..."
+ "[corewifi] %s: retry exhausted, exiting scan phase..."
+ "[corewifi] %s: scan completed, requested channels=%@, result count=%d, matches=%d, error=%@"
+ "[corewifi] %s: timed out waiting for chip reset to complete"
+ "[corewifi] %s: unknown band %d for supported channel %d"
+ "^{IONotificationPort=}"
+ "_ABCReporter"
+ "__Unavailable__"
+ "__WiFiDeviceManagerAbortMISSessionStart"
+ "__WiFiDeviceManagerDeferPowerSaveForCarPlayBonjourHS"
+ "__WiFiDeviceManagerDonateCarPlayLinkMetricsToCarEvent"
+ "__WiFiDeviceManagerDonateCarPlayLinkMetricsToCarEvent_block_invoke"
+ "__WiFiDeviceManagerPowerSaveDeferralTimerCallback"
+ "__WiFiDeviceManagerRecoverMISFromDextCrash"
+ "__WiFiDeviceManagerRecoverMISFromWiFidCrash"
+ "__WiFiDeviceManagerSetLMTPC"
+ "__WiFiDeviceManagerUnifiedAutoJoinAllowJoinCandidate"
+ "__WiFiManagerDriverPublishedCallback"
+ "__WiFiManagerDriverTerminatedCallback"
+ "__WiFiManagerHandleStaleDiscoveryRequests_block_invoke"
+ "__WiFiManagerIsCarPlayAutoJoinEnabled"
+ "__WiFiWatchdogAsyncEventHandler"
+ "__WiFiWatchdogMonitorWatchdogCrashIDCallback"
+ "__WiFiWatchdogMonitorWatchdogTriggeredCallback"
+ "_appAttributeLock"
+ "_appTrackerLock"
+ "_crashIDIterator"
+ "_driverConnectHandle"
+ "_driverService"
+ "_firmwareAssertTable"
+ "_internalQ"
+ "_isStateValid"
+ "_misBandWidth"
+ "_misChannel"
+ "_misEnabled"
+ "_misEnabledAt"
+ "_misIsHidden"
+ "_notificationPort"
+ "_osTransaction"
+ "_pendingAppAttributeQueries"
+ "_recoveryAttempts"
+ "_remoteClientCountryCode"
+ "_userPreferredBand"
+ "_watchdogStartedTimestamp"
+ "_wdTriggeredIterator"
+ "addAnalyticsValues:toEvent:completion:"
+ "appAttributeLock"
+ "appTrackerLock"
+ "assertId"
+ "assistant_service"
+ "autoJoinManager"
+ "autoJoinedNetwork"
+ "checkForTimeout"
+ "com.apple.wifid.WatchdogMonitor"
+ "com.apple.wifid.watchdog-monitor"
+ "cpu"
+ "enable virtio header"
+ "enable_virtio_header"
+ "endedAt"
+ "enumerateKeysAndObjectsUsingBlock:"
+ "firmwareAssertTable"
+ "getRemoteClientCountryCode"
+ "handleCrashNotificationWithID:andCPUName:"
+ "handleWatchdogTriggered"
+ "initABCReporter"
+ "initState"
+ "initState:"
+ "initWithIOService:"
+ "internalQ"
+ "isCarPlayNetwork"
+ "isMisEnabled"
+ "isMisHidden"
+ "isMisRecoveryAllowed"
+ "isPayloadIdentifierTelemetryApproved"
+ "isStateValid"
+ "isStateValid=%u, misEnabled=%u, misEnabledAt=%@ misChannel=%lu, misBandWidth=%lu, misIsHidden=%u _userPreferredBand=%lu _recoveryAttempts=%lu"
+ "keyEnumerator"
+ "linkDownSubreason"
+ "lock"
+ "misBandWidth"
+ "misChannel"
+ "misEnabled"
+ "misEnabledAt"
+ "misIsHidden"
+ "misRecoveryAttempts"
+ "payloadIdentifier"
+ "pendingAppAttributeQueries"
+ "persistState"
+ "publisher:detectedMulticastError:fromMulticastReceiver:"
+ "publisher:receivedDataBlobForMulticastSession:fromPeer:"
+ "reason=0x%x"
+ "recoveryAttempts"
+ "recoveryStart"
+ "releaseBackgroundFileWritingMOC"
+ "releaseBackgroundProcessingMOC"
+ "releaseBackgroundReadingMOC"
+ "resetState"
+ "service matching:%u"
+ "service terminate:%u"
+ "setAppAttributeLock:"
+ "setAppTrackerLock:"
+ "setCarrierPayloadIdentifier:"
+ "setDisplayOff:"
+ "setFirmwareAssertTable:"
+ "setInternalQ:"
+ "setIsCarrierPayloadIdentifierTelemetryApproved:"
+ "setIsStateValid:"
+ "setMisBandWidth:"
+ "setMisChannel:"
+ "setMisEnabled:"
+ "setMisEnabledAt:"
+ "setMisIsHidden:"
+ "setPayloadIdentifier:"
+ "setPendingAppAttributeQueries:"
+ "setPrivateMacNetworkTypeHome:"
+ "setRecoveryAttempts:"
+ "setSARState:builtInReceiverOn:"
+ "setSetCountryCodeHandler:"
+ "setUserPreferredBand:"
+ "setWatchdogStartedTimestamp:"
+ "sharedDeviceAnalyticsClient"
+ "sharedWiFiDiagnosticReporter"
+ "signatureWithDomain:type:subType:subtypeContext:detectedProcess:triggerThresholdValues:"
+ "snapshotWithSignature:delay:events:payload:actions:reply:"
+ "startOnQueue:group:"
+ "stateDictionary"
+ "submitWiFiWatchdogReason:subtypeContext:"
+ "subscriber:detectedMulticastError:fromMulticastSender:"
+ "subscriber:receivedDataBlobForMulticastSession:fromPeer:"
+ "timeSinceLastAwdlStatsPost"
+ "unlock"
+ "updateRemoteClientCountryCode:"
+ "userPreferredBand"
+ "v32@?0@8@16^B24"
+ "v40@0:8@\"WiFiAwarePublisher\"16@\"NSData\"24@\"WiFiMACAddress\"32"
+ "v40@0:8@\"WiFiAwarePublisher\"16q24@\"WiFiMACAddress\"32"
+ "v40@0:8@\"WiFiAwareSubscriber\"16@\"NSData\"24@\"WiFiMACAddress\"32"
+ "v40@0:8@\"WiFiAwareSubscriber\"16q24@\"WiFiMACAddress\"32"
+ "v40@0:8@16q24@32"
+ "wasAlreadyAssociatedToNetwork"
+ "watchdogStartedTimestamp"
+ "wlan.ranging.disablePhyErrDiscarding=1"
+ "\x8f\xd3"
- "%@: isHidden=%d, isEAP=%d, isSAE=%d, isWPA=%d, isWEP=%d, WAPI=%d, type=%d, enabled=%@, saveData=%@, responsiveness=%@ (%@) isHome=%@, isForceFixed=%d, transitionDisabledFlags=%@, foundNanIe=%d, isPH=%d, isPublicAirPlayNetwork=%d, is6EDisabled=%d, hs20=%d, Channel=%d, isBundleIdentifierPresent=%d"
- "%s: CWFInterface initWithServiceType: failed"
- "%s: DHCP client hostnames: %@"
- "%s: Device in Lock state over an %d minutes. Disconnect from Hotspot!!"
- "%s: Enabled LMTPC for CarPlay"
- "%s: Enabling CarPlay auto join for UUID %@ network %@"
- "%s: MIS is in recovery. Driver is available. Restarting MIS network!"
- "%s: chip reset completed"
- "%s: encountered join error %@, performing join retry..."
- "%s: encountered multiple (%d) failures, performing chip reset before retrying (remaining time %ds)..."
- "%s: find and join %@ failed with error %@"
- "%s: invalid band specified (%d), forcing to 2.4GHz"
- "%s: join %@ succeeded (error=%@)"
- "%s: join completed, candidate=%@, error=%@"
- "%s: last error (%@), retry expired=%s exceeded=%s"
- "%s: no join candidate, performing scan retry..."
- "%s: no match in scan results, performing scan retry..."
- "%s: no password for %@"
- "%s: null network name"
- "%s: processed peer at index %ld"
- "%s: request %@, supported channels:%@"
- "%s: retry exhausted, exiting join phase..."
- "%s: retry exhausted, exiting scan phase..."
- "%s: scan completed, requested channels=%@, result count=%d, matches=%d, error=%@"
- "%s: station list %@"
- "%s: timed out waiting for LSApplicationRecord"
- "%s: timed out waiting for chip reset to complete"
- "%s: unknown band %d for supported channel %d"
- "-[WiFiManagerLifeCycle startOnQueue:]"
- "-[WiFiUserInteractionMonitor hasRealTimeAppProperty:]"
- "Error sending sleep state notification %d"
- "FAILED to  set Device Analytics config."
- "RTT[%ld]: Status=%d, RTT=%d RSSI=%d SNR=%d Core=%d BitFlip=%d PHYErr=%d(%s) Peer-SNR=%d Peer-BitFlip=%d Peer-PHYErr=%d(%s)"
- "Simulated LQM Dict: %@"
- "WiFiManager-1825.3 Jan 16 2025 06:26:29"
- "WiFiManager-1825.3 Jan 16 2025 06:26:53"
- "WirelessRadioMan"
- "__WiFiManagerEnableAutoJoinForCarPlay"
- "__getAutoJoinMetric:"
- "__getAutoJoinStatistics:"
- "__resetAutoJoinStatistics:"
- "discover"
- "duration"
- "iPad12,1"
- "iPad12,2"
- "setDwellTime:"
- "sharedAnalyticsProcessor"
- "sharedDeviceAnalyticsClientWithPersist"
- "startOnQueue:"
- "wasAlreadyAssociated"
- "\x8c\xd3"

```
