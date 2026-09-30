## airportd

> `/usr/libexec/airportd`

```diff

-19045.5.0.0.0
-  __TEXT.__text: 0xeba1c
-  __TEXT.__auth_stubs: 0x1f90
-  __TEXT.__objc_stubs: 0x11480
-  __TEXT.__objc_methlist: 0x5974
-  __TEXT.__objc_methname: 0x16014
-  __TEXT.__objc_classname: 0x3fe
-  __TEXT.__objc_methtype: 0x3d1c
-  __TEXT.__const: 0x1df8
-  __TEXT.__gcc_except_tab: 0x1e60
-  __TEXT.__cstring: 0x2b03c
-  __TEXT.__oslogstring: 0x9db
-  __TEXT.__unwind_info: 0x28c0
+19075.37.0.0.0
+  __TEXT.__text: 0xf3dbc
+  __TEXT.__auth_stubs: 0x20d0
+  __TEXT.__objc_stubs: 0x117a0
+  __TEXT.__objc_methlist: 0x6330
+  __TEXT.__const: 0xf48
+  __TEXT.__objc_methname: 0x163c9
+  __TEXT.__objc_classname: 0x414
+  __TEXT.__objc_methtype: 0x3d66
+  __TEXT.__gcc_except_tab: 0x1fd8
+  __TEXT.__cstring: 0x2def9
+  __TEXT.__oslogstring: 0x1326
+  __TEXT.__unwind_info: 0x2920
   __TEXT.__eh_frame: 0xf8
-  __DATA_CONST.__auth_got: 0xfd8
-  __DATA_CONST.__got: 0xa10
-  __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x34b0
-  __DATA_CONST.__cfstring: 0x9fc0
-  __DATA_CONST.__objc_classlist: 0x140
+  __DATA_CONST.__auth_got: 0x1078
+  __DATA_CONST.__got: 0xa18
+  __DATA_CONST.__auth_ptr: 0x20
+  __DATA_CONST.__const: 0x34d8
+  __DATA_CONST.__cfstring: 0xa940
+  __DATA_CONST.__objc_classlist: 0x148
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x140
-  __DATA_CONST.__objc_intobj: 0x15a8
-  __DATA_CONST.__objc_arraydata: 0x288
+  __DATA_CONST.__objc_superrefs: 0x148
+  __DATA_CONST.__objc_intobj: 0x1548
+  __DATA_CONST.__objc_arraydata: 0x2b0
   __DATA_CONST.__objc_arrayobj: 0x90
-  __DATA_CONST.__objc_dictobj: 0xc8
-  __DATA.__objc_const: 0x93a8
-  __DATA.__objc_selrefs: 0x4dc8
-  __DATA.__objc_ivar: 0x928
-  __DATA.__objc_data: 0xc80
+  __DATA_CONST.__objc_dictobj: 0x168
+  __DATA.__objc_const: 0x8580
+  __DATA.__objc_selrefs: 0x4fb8
+  __DATA.__objc_ivar: 0x95c
+  __DATA.__objc_data: 0xcd0
   __DATA.__data: 0x4b8
-  __DATA.__bss: 0x240
-  __DATA.__common: 0x140
+  __DATA.__common: 0x148
+  __DATA.__bss: 0x2f8
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/Versions/A/CoreLocation

   - /System/Library/Frameworks/SystemConfiguration.framework/Versions/A/SystemConfiguration
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/Versions/A/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreCaptureControl.framework/Versions/A/CoreCaptureControl
+  - /System/Library/PrivateFrameworks/CoreUtils.framework/Versions/A/CoreUtils
   - /System/Library/PrivateFrameworks/CoreWiFi.framework/Versions/A/CoreWiFi
   - /System/Library/PrivateFrameworks/IO80211.framework/Versions/A/IO80211
   - /System/Library/PrivateFrameworks/LockdownMode.framework/Versions/A/LockdownMode

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libpcap.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: DB17A5B1-29FA-3696-892E-A6F35BEC4BB4
-  Functions: 3183
-  Symbols:   856
-  CStrings:  9264
+  UUID: 7467DC5E-6961-32D7-B323-DEF18AB73F22
+  Functions: 3202
+  Symbols:   878
+  CStrings:  9605
 
Symbols:
+ _IOConnectCallAsyncMethod
+ _IONotificationPortGetMachPort
+ _IONotificationPortSetDispatchQueue
+ _IOPMGetCapabilitiesDescription
+ _IORegistryEntrySetCFProperties
+ _IOServiceClose
+ _IOServiceNameMatching
+ _IOServiceOpen
+ _NSStringFromClass
+ _OBJC_CLASS_$_CUSystemMonitor
+ _OBJC_CLASS_$_CWFHotspotClientManager
+ _OBJC_CLASS_$_WiFiRemoteClientCountryCodeMonitor
+ _OBJC_CLASS_$_WiFiUsageMonitor_UsbDevice
+ _convertApple80211ReturnToString
+ _dispatch_queue_attr_make_with_qos_class
+ _getpid
+ _notify_is_valid_token
+ _notify_register_dispatch
+ _objc_autoreleaseReturnValue
+ _objc_retainAutoreleasedReturnValue
+ _objc_storeStrong
+ _os_boot_mode_query
+ _os_parse_boot_arg_int
+ _pthread_threadid_np
- _OBJC_CLASS_$_CWFAutoJoinManager
- _kIOMasterPortDefault
CStrings:
+ " reasonString=%@"
+ " subreason=0x%x"
+ " subreasonString=%@"
+ "%s %s an AirPort interface."
+ "%s Adding, eventClass[0x%08x] eventType[0x%08x]"
+ "%s Removing, eventClass[0x%08x] eventType[0x%08x]"
+ "%s: ARP/NDP offloads disabled, not programming the offload, '%@'\n"
+ "%s: Failed to create xpc connection to p2pd for country code monitoring\n"
+ "%s: KEV_DL_IF_ATTACHED"
+ "%s: KEV_DL_IF_DETACHED"
+ "%s: No valid components format from SCDynamicStore: serviceKey:'%@'\n"
+ "%s: No valid protocolID from SCDynamicStore: serviceKey:'%@'\n"
+ "%s: No valid serviceID from SCDynamicStore: serviceKey:'%@'\n"
+ "%s: Not IPV4 protocolID from SCDynamicStore: serviceKey:'%@'\n"
+ "%s: Not interface_dict from SCDynamicStore: interface_key:'%@'\n"
+ "%s: Not interface_ifname from SCDynamicStore: interface_dict:'%@'\n"
+ "%s: Not interface_key from SCDynamicStore: serviceID:'%@'\n"
+ "%s: Null device node ifNameRef: '%@'\n"
+ "%s: Null device node: '%@'\n"
+ "%s: Null interface: interface_ifname '%@'\n"
+ "%s: SCDynamicStore save, @[%llu.%06llu] took %llu.%06llu, aquired took %llu.%06llu, unlock interface took %llu.%06llu, unlock global took %llu.%06llu\n"
+ "%s: SCDynamicStore save, @[%llu.%06llu] took %llu.%06llu, aquired took %llu.%06llu, unlock took %llu.%06llu\n"
+ "%s: SCDynamicStore save, @[%llu.%06llu] took %llu.%06llu, aquired took %llu.%06llu, unlock took %llu.%06llu, SC commit/apply %llu.%06llu\n"
+ "%s: SCDynamicStore save, @[%llu.%06llu] took %llu.%06llu, aquired took %llu.%06llu, unlock took %llu.%06llu, SC commit/apply took %llu.%06llu\n"
+ "%s: SCDynamice store interface_ifname '%@' != ifName '%@'\n"
+ "%s: setWiFiPowerState: @[%llu.%06llu], state[%u]\n"
+ "%s: setWiFiPowerState: @[%llu.%06llu], state[%u], issued Apple80211SetPower, tmpErr[%ld], request took %llu.%06llu\n"
+ "%s: setWiFiPowerState: @[%llu.%06llu], state[%u], issuing Apple80211SetPower\n"
+ "%s: setWiFiPowerState: @[%llu.%06llu], state[%u], took %llu.%06llu, powerPrefTS[%llu.%06llu] resetChipTS[%llu.%06llu] usageMonitorTS[%llu.%06llu] updatePowerOffTS[%llu.%06llu] powerReqTS[%llu.%06llu]\n"
+ "%{public}s install environment (RecoveryOS)"
+ "%{public}s: Initializing LPEM notification handler"
+ "-[CWXPCSubsystem __rememberWiFiNetwork:profileID:collocatedProfileID:password:is8021X:isUserMode8021X:isWEP40:isWEPOpenSystem:passpointDomain:remember:isAutoJoin:possiblyHidden:updateUserKeychain:interface:has6GHzOnlyBSS:isSetupNetwork:isPrivateMACFailureFallback:temporaryPrivateMACSetting:networkID:error:]"
+ "-[CWXPCSubsystem copyChanInfoListForInterfaceWithName:connection:error:]"
+ "-[CWXPCSubsystem updateAutoJoinDisableState]_block_invoke"
+ "-[CWXPCSubsystem updateWoWEnableState]_block_invoke"
+ "-[WiFiLocaleManagerUser updateRemoteClientCountryCode:]"
+ "-[WiFiWatchdogMonitor checkForTimeout]"
+ "-[WiFiWatchdogMonitor dealloc]"
+ "-[WiFiWatchdogMonitor handleCrashNotificationWithID:andCPUName:]"
+ "-[WiFiWatchdogMonitor handleWatchdogTriggered]"
+ "-[WiFiWatchdogMonitor initWithIOService:]"
+ "-[WiFiWatchdogMonitor initWithServiceName:]"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AirPort_executables/Tools/airportd/CWXPCSubsystem.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AirPort_executables/Tools/airportd/airportProcessCommand.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AirPort_executables/Tools/airportd/airportdAutoJoin.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AirPort_executables/Tools/airportd/airportdCommandLine.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AirPort_executables/Tools/airportd/airportdMain.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AirPort_executables/Tools/airportd/airportdPreferences.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AirPort_executables/Tools/airportd/configdIODriverInterface.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AirPort_executables/Tools/airportd/configdSCInterface.m"
+ "0x%llx"
+ "5"
+ "< %@:%p "
+ "<%@> AWDL assisted discovery mode is active, will not continue auto-join"
+ "<%@> AWDL real time mode is active, will not continue auto-join"
+ "<%@> Auto-join deferral is active, will not continue auto-join"
+ "<%@> Auto-join is disabled (via boot-arg), will not continue auto-join"
+ "<%@> Auto-join is disabled, will not continue auto-join"
+ "<%@> FAILED to configure scan offloads, returned error code %d (%s), aj_disabled=%s, PNO count[%lu]"
+ "<%@> Scan offloads will be %s (lpas_supported=%s, softap=%s, wow=%s, tcpka=%s, allow_unassoc_wakes=%s, allow_disconn_sleeps=%s, aj_disabled=%s, scan_offload_disabled_until=%@)"
+ "<%@> Successfully configured scan offloads, aj_disabled=%s, PNO count[%lu]"
+ "<%@> User login trigger with no console user, will not continue auto-join"
+ "<%s> Failed to create timer dispatch source"
+ "<%s> Failed to create timer q"
+ "<%s[%d]> %s: %s Adding, eventClass[0x%08x] eventType[0x%08x]\n"
+ "<%s[%d]> %s: %s Removing, eventClass[0x%08x] eventType[0x%08x]\n"
+ "<%s[%d]> %s: %s: KEV_DL_IF_ATTACHED\n"
+ "<%s[%d]> %s: %s: KEV_DL_IF_DETACHED\n"
+ "<%s[%d]> %s: <%@> AWDL assisted discovery mode is active, will not continue auto-join\n"
+ "<%s[%d]> %s: <%@> AWDL real time mode is active, will not continue auto-join\n"
+ "<%s[%d]> %s: <%@> Auto-join deferral is active, will not continue auto-join\n"
+ "<%s[%d]> %s: <%@> Auto-join is disabled (via boot-arg), will not continue auto-join\n"
+ "<%s[%d]> %s: <%@> Auto-join is disabled, will not continue auto-join\n"
+ "<%s[%d]> %s: <%@> FAILED to configure scan offloads, returned error code %d (%s), aj_disabled=%s, PNO count[%lu]\n"
+ "<%s[%d]> %s: <%@> Scan offloads will be %s (lpas_supported=%s, softap=%s, wow=%s, tcpka=%s, allow_unassoc_wakes=%s, allow_disconn_sleeps=%s, aj_disabled=%s, scan_offload_disabled_until=%@)\n"
+ "<%s[%d]> %s: <%@> Successfully configured scan offloads, aj_disabled=%s, PNO count[%lu]\n"
+ "<%s[%d]> %s: <%@> User login trigger with no console user, will not continue auto-join\n"
+ "<%s[%d]> %s: ABC snapshotWithSignature signature: %@\n"
+ "<%s[%d]> %s: ARP/NDP offloads disabled, not programming the offload, '%@'\n"
+ "<%s[%d]> %s: AUTO-JOIN %s for interface %@, took %.4f seconds, returned result '%s', error %@\n"
+ "<%s[%d]> %s: AUTO-JOIN STARTED for interface %@ (%@)\n"
+ "<%s[%d]> %s: Acknowledging sleep event, connection[%p] token[0x%08x]\n"
+ "<%s[%d]> %s: Acknowledging sleep event, connection[%p] token[0x%08x], gPMConnection[%p]\n"
+ "<%s[%d]> %s: Added success for node %@\n"
+ "<%s[%d]> %s: AirPort Interface <%s> <%d>, Infra interface, eventClass[0x%08x] eventType[0x%08x]\n"
+ "<%s[%d]> %s: AirPort Interface <%s> <%d>, added to device node list\n"
+ "<%s[%d]> %s: AutoJoin %s (assert=%s, activity=%s, join=%s, until=%@, prev=%s)\n"
+ "<%s[%d]> %s: Client associated to PH with effectiveHardwareMACAddress = %@\n"
+ "<%s[%d]> %s: Client disassoicated to PH with effectiveHardwareMACAddress = %@\n"
+ "<%s[%d]> %s: Failed to create xpc connection to p2pd for country code monitoring\n"
+ "<%s[%d]> %s: Free'ing node %@\n"
+ "<%s[%d]> %s: Health check alive, checkin@[%llu.%06llu], count[%llu] \n"
+ "<%s[%d]> %s: INITIAL SETUP => fallback to auto-join using NVRAM\n"
+ "<%s[%d]> %s: Ignoring redundant auto-join invocation for interface %@\n"
+ "<%s[%d]> %s: LPEM notification, token[0x%08x], interfaceName[%@], reason code (0x%llx), currentState[%u], get power currentState[%u], exiting w/[%lld]\n"
+ "<%s[%d]> %s: LPEM notification, token[0x%08x], interfaceName[%@], reason code (0x%llx), currentState[%u], set power lpemPowerState[%u]\n"
+ "<%s[%d]> %s: LPEM notification, token[0x%08x], interfaceName[%@], reason code (0x%llx), currentState[%u], set power state[%u]\n"
+ "<%s[%d]> %s: Link down event. Triggering auto-join.\n"
+ "<%s[%d]> %s: No valid components format from SCDynamicStore: serviceKey:'%@'\n"
+ "<%s[%d]> %s: No valid protocolID from SCDynamicStore: serviceKey:'%@'\n"
+ "<%s[%d]> %s: No valid serviceID from SCDynamicStore: serviceKey:'%@'\n"
+ "<%s[%d]> %s: Not IPV4 protocolID from SCDynamicStore: serviceKey:'%@'\n"
+ "<%s[%d]> %s: Not interface_dict from SCDynamicStore: interface_key:'%@'\n"
+ "<%s[%d]> %s: Not interface_ifname from SCDynamicStore: interface_dict:'%@'\n"
+ "<%s[%d]> %s: Not interface_key from SCDynamicStore: serviceID:'%@'\n"
+ "<%s[%d]> %s: Null device node ifNameRef: '%@'\n"
+ "<%s[%d]> %s: Null device node: '%@'\n"
+ "<%s[%d]> %s: Null interface: interface_ifname '%@'\n"
+ "<%s[%d]> %s: Received LPEM '%s' notification, token[0x%08x] gLPEMNotifyToken[0x%08x], allowed[%lld], interfaceName[%@], currentState[%u] hasPowerOverride[%u], doExit[%lld] exitCode[%lld]\n"
+ "<%s[%d]> %s: Removing: Freeing %@.\n"
+ "<%s[%d]> %s: SCDynamicStore save, @[%llu.%06llu] took %llu.%06llu, aquired took %llu.%06llu, unlock interface took %llu.%06llu, unlock global took %llu.%06llu\n"
+ "<%s[%d]> %s: SCDynamicStore save, @[%llu.%06llu] took %llu.%06llu, aquired took %llu.%06llu, unlock took %llu.%06llu\n"
+ "<%s[%d]> %s: SCDynamicStore save, @[%llu.%06llu] took %llu.%06llu, aquired took %llu.%06llu, unlock took %llu.%06llu, SC commit/apply %llu.%06llu\n"
+ "<%s[%d]> %s: SCDynamicStore save, @[%llu.%06llu] took %llu.%06llu, aquired took %llu.%06llu, unlock took %llu.%06llu, SC commit/apply took %llu.%06llu\n"
+ "<%s[%d]> %s: SCDynamice store interface_ifname '%@' != ifName '%@'\n"
+ "<%s[%d]> %s: ScDeinitInterface for device %@\n"
+ "<%s[%d]> %s: Starting hostap mode, suppressing link down recovery.\n"
+ "<%s[%d]> %s: System is sleeping, will not continue auto-join\n"
+ "<%s[%d]> %s: Thermal index %ld not above threshold %ld, will not continue auto-join\n"
+ "<%s[%d]> %s: WiFi interface %@ is not a primary interface, will not continue auto-join\n"
+ "<%s[%d]> %s: WiFi interface is OFF, will not continue auto-join\n"
+ "<%s[%d]> %s: WiFi interface is in SWAP mode, will not continue auto-join\n"
+ "<%s[%d]> %s: WiFi interface is in monitor mode, will not continue auto-join\n"
+ "<%s[%d]> %s: WoW %s (assert=%s, pref=%s activity=%s, ps=%s, icloud=%s, tcpka=%s, pno=%s, lpas=%s)\n"
+ "<%s[%d]> %s: _freeDevice for device %@\n"
+ "<%s[%d]> %s: caps = %s%s%s%s%s%s, connection[%p] token[0x%08x] capabilties[0x%08x], description:'%s', lastSleepType[0x%08x]/'%s', hibernateStateFound[%u] hibernateState[0x%08x/%u] hibernateMode[0x%08x/%d]\n"
+ "<%s[%d]> %s: driver %s (reason=0x%x, subreason=0x%x, flags=0x%x), node:isDriverAvailable=%u\n"
+ "<%s[%d]> %s: interface[%@], client[%@] power[%u], err[0x%08x/%u]\n"
+ "<%s[%d]> %s: scInitInterface for device %@\n"
+ "<%s[%d]> %s: setWiFiPowerState: @[%llu.%06llu], state[%u]\n"
+ "<%s[%d]> %s: setWiFiPowerState: @[%llu.%06llu], state[%u], issued Apple80211SetPower, tmpErr[%ld], request took %llu.%06llu\n"
+ "<%s[%d]> %s: setWiFiPowerState: @[%llu.%06llu], state[%u], issuing Apple80211SetPower\n"
+ "<%s[%d]> %s: setWiFiPowerState: @[%llu.%06llu], state[%u], took %llu.%06llu, powerPrefTS[%llu.%06llu] resetChipTS[%llu.%06llu] usageMonitorTS[%llu.%06llu] updatePowerOffTS[%llu.%06llu] powerReqTS[%llu.%06llu]\n"
+ "<%s[%d]> DYNAMIC STORE UPDATE FAILED for interface %@, returned error '%s', tid[0x%llx]/qTid[0x%llx] @[%llu.%06llu], took %llu.%06llu\n"
+ "<%s[%d]> DYNAMIC STORE UPDATE Successful for interface %@, tid[0x%llx]/qTid[0x%llx] @[%llu.%06llu], took %llu.%06llu\n"
+ "<%s[%d]> NVRAM-based known network is missing private MAC mode, applying default based on network type (%ld)\n"
+ "<%s[%d]> RETURN CURRENT TETHER DEVICE [%@]\n"
+ "<%s[%d]> start DYNAMIC STORE UPDATE for interface '%@', tid[0x%llx]/qTid[0x%llx] @[%llu.%06llu]\n"
+ "<%{public}s:%u> Invalid node ref"
+ "<%{public}s:%u> Invalid parameter"
+ "<%{public}s:%u> LPEM invalid token, ... skipping"
+ "<%{public}s:%u> LPEM not allowed, ... skipping"
+ "<%{public}s:%u> Null device node"
+ "<%{public}s:%u> Unable to '__setPowerWithRetry': err[0x%08x/%d]"
+ "<%{public}s:%u>, _serviceName['%{public}@']"
+ "<%{public}s:%u>: %s not found"
+ "<%{public}s:%u>: ENTER"
+ "<%{public}s:%u>: ENTER, crashID:%llu/0x%llx, cpuName:'%{public}@'"
+ "<%{public}s:%u>: Failed: IOConnectCallAsyncMethod failed with err=%d, _notificationPort[%p], _driverConnectHandle[%u] wakePort[%u] internalQ[%p]"
+ "<%{public}s:%u>: Failed: IONotificationPortCreate"
+ "<%{public}s:%u>: Failed: IOServiceAddMatchingNotification %@ failed with err=%d,  _notificationPort[%p]"
+ "<%{public}s:%u>: Failed: IOServiceAddMatchingNotification %@ failed with err=%d, _notificationPort[%p]"
+ "<%{public}s:%u>: Failed: IOServiceOpen failed with err=%d, type[%u]"
+ "<%{public}s:%u>: Failed: No valid service, _serviceName['%{public}@'] _driverService[%u]"
+ "<%{public}s:%u>: Failed: internalQ create"
+ "<%{public}s:%u>: IOConnectCallAsyncMethod '%{public}s' with err=%d, _serviceName['%{public}@'] _driverService[%u] _notificationPort[%p] _driverConnectHandle[%u] wakePort[%u] internalQ[%p]"
+ "<%{public}s:%u>: IORegistryEntrySetCFProperties failed with error %x, '%{public}@'\n"
+ "<%{public}s:%u>: Initialized [%p], _serviceName['%{public}@'] _driverService[%u] _notificationPort[%p] _driverConnectHandle[%u] wakePort[%u] internalQ[%p]"
+ "<%{public}s:%u>: LEAVE"
+ "<%{public}s:%u>: _serviceName['%{public}@'] _driverService[%u]"
+ "<%{public}s:%u>: _serviceName['%{public}@']: cleaning up, _driverService[%u] _notificationPort[%p] _driverConnectHandle[%u] _internalQ[%p]"
+ "<%{public}s:%u>: cpuName %s crashID %llu/0x%llx"
+ "<%{public}s:%u>: crashReasonString for ID %@ not found"
+ "<%{public}s:%u>: data not found in %@"
+ "<%{public}s:%u>: dictionary for cpuName %@ not found"
+ "<%{public}s:%u>: incorrect number of arguments (=%d)"
+ "<%{public}s:%u>: nil args"
+ "<%{public}s:%u>: nil firmwareAssertTable"
+ "<%{public}s:%u>: nil type (bad args)"
+ "<%{public}s:%u>: timed out waiting for crashID notification, cleaning up."
+ "<%{public}s:%u>: unhandled argument type %llu"
+ ">"
+ "@\"CUSystemMonitor\""
+ "@\"NSObject<OS_os_transaction>\""
+ "@20@0:8I16"
+ "ARP/NDP offloads disabled, not programming the offload, '%@'"
+ "AUTO-JOIN %s for interface %@, took %.4f seconds, returned result '%s', error %@"
+ "AUTO-JOIN STARTED for interface %@ (%@)"
+ "Aborted Sleep"
+ "Acknowledging sleep event, connection[%p] token[0x%08x]"
+ "Acknowledging sleep event, connection[%p] token[0x%08x], gPMConnection[%p]"
+ "Added success for node %@"
+ "AirPort Interface <%s> <%d>, Infra interface, eventClass[0x%08x] eventType[0x%08x]"
+ "AirPort Interface <%s> <%d>, added to device node list"
+ "AppleWLANDriver"
+ "AppleWLANWatchdog"
+ "AutoJoin %s (assert=%s, activity=%s, join=%s, until=%@, prev=%s)"
+ "AutoPowerOff"
+ "B132@0:8@16@24@32@40B48B52B56B60@64B72B76B80B84@88B96B100B104q108@116^@124"
+ "CrashIDNotification"
+ "Deep Idle"
+ "Free'ing node %@"
+ "Health check alive, checkin@[%llu.%06llu], count[%llu] "
+ "Hibernate"
+ "Hibernate Mode"
+ "INITIAL SETUP => fallback to auto-join using NVRAM"
+ "IOHibernateState"
+ "IOPMSystemSleepType"
+ "IOServiceMatched"
+ "Ignoring redundant auto-join invocation for interface %@"
+ "Invalid"
+ "Invalid IPv4 state dictionary for '%@'"
+ "LPEM"
+ "LPEM notification, token[0x%08x], interfaceName[%@], reason code (0x%llx), currentState[%u], get power currentState[%u], exiting w/[%lld]"
+ "LPEM notification, token[0x%08x], interfaceName[%@], reason code (0x%llx), currentState[%u], set power lpemPowerState[%u]"
+ "LPEM notification, token[0x%08x], interfaceName[%@], reason code (0x%llx), currentState[%u], set power state[%u]"
+ "NOISE_CTL_AGR"
+ "No SCDynamicStoreCreate store, '%@'"
+ "No valid components format from SCDynamicStore: serviceKey:'%@'"
+ "No valid protocolID from SCDynamicStore: serviceKey:'%@'"
+ "No valid serviceID from SCDynamicStore: serviceKey:'%@'"
+ "Normal Sleep"
+ "Not IPV4 protocolID from SCDynamicStore: serviceKey:'%@'"
+ "Not interface_dict from SCDynamicStore: interface_key:'%@'"
+ "Not interface_ifname from SCDynamicStore: interface_dict:'%@'"
+ "Not interface_key from SCDynamicStore: serviceID:'%@'"
+ "Null device node ifNameRef: '%@'"
+ "Null device node: '%@'"
+ "Null interface: interface_ifname '%@'"
+ "OS boot mode: '%{public}s'"
+ "PHDataUsageE"
+ "Received LPEM '%s' notification, token[0x%08x] gLPEMNotifyToken[0x%08x], allowed[%lld], interfaceName[%@], currentState[%u] hasPowerOverride[%u], doExit[%lld] exitCode[%lld]"
+ "Removing %@."
+ "Removing: Freeing %@."
+ "SCDynamicStore save, @[%llu.%06llu] took %llu.%06llu, aquired took %llu.%06llu, unlock interface took %llu.%06llu, unlock global took %llu.%06llu"
+ "SCDynamicStore save, @[%llu.%06llu] took %llu.%06llu, aquired took %llu.%06llu, unlock took %llu.%06llu"
+ "SCDynamicStore save, @[%llu.%06llu] took %llu.%06llu, aquired took %llu.%06llu, unlock took %llu.%06llu, SC commit/apply %llu.%06llu"
+ "SCDynamicStore save, @[%llu.%06llu] took %llu.%06llu, aquired took %llu.%06llu, unlock took %llu.%06llu, SC commit/apply took %llu.%06llu"
+ "SCDynamice store interface_ifname '%@' != ifName '%@'"
+ "Safe Sleep"
+ "ScDeinitInterface"
+ "ScDeinitInterface for device %@"
+ "Standby"
+ "System is sleeping, will not continue auto-join"
+ "T@\"CWFAutoJoinManager\",R"
+ "T@\"NSDate\",&,N,V_watchdogStartedTimestamp"
+ "T@\"NSDictionary\",&,N,V_firmwareAssertTable"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_internalQ"
+ "Thermal index %ld not above threshold %ld, will not continue auto-join"
+ "Usb Host Notification metrics: usbChange=%d, count=%lu, noiseDelta=%d\n"
+ "WatchdogTriggered"
+ "WiFi interface %@ is not a primary interface, will not continue auto-join"
+ "WiFi interface is OFF, will not continue auto-join"
+ "WiFi interface is in SWAP mode, will not continue auto-join"
+ "WiFi interface is in monitor mode, will not continue auto-join"
+ "WiFiPolicy"
+ "WiFiUsageWatchdogDetailsSubmitToCA"
+ "WiFiWatchdogMonitor"
+ "WoW %s (assert=%s, pref=%s activity=%s, ps=%s, icloud=%s, tcpka=%s, pno=%s, lpas=%s)"
+ "[airport]/%d @[%llu.%06llu] (%s:%d) %s"
+ "[corewifi] Initial display state %d"
+ "[corewifi] Updated display state %d"
+ "^{IONotificationPort=}"
+ "__WiFiWatchdogAsyncEventHandler"
+ "__WiFiWatchdogMonitorWatchdogCrashIDCallback"
+ "__WiFiWatchdogMonitorWatchdogTriggeredCallback"
+ "__defaultDualBandSingleAPRoamingProfile_6GHz"
+ "__defaultMultiAPRoamingProfile_6GHz"
+ "__rememberWiFiNetwork:profileID:collocatedProfileID:password:is8021X:isUserMode8021X:isWEP40:isWEPOpenSystem:passpointDomain:remember:isAutoJoin:possiblyHidden:updateUserKeychain:interface:has6GHzOnlyBSS:isSetupNetwork:isPrivateMACFailureFallback:temporaryPrivateMACSetting:networkID:error:"
+ "__teardownAutoJoinManager"
+ "_configureScanOffloadParameters"
+ "_crashIDIterator"
+ "_cuSystemMonitor"
+ "_driverConnectHandle"
+ "_driverService"
+ "_firmwareAssertTable"
+ "_freeDevice"
+ "_freeDevice for device %@"
+ "_getPowerState"
+ "_internalQ"
+ "_notificationPort"
+ "_osTransaction"
+ "_previousDisassocReason"
+ "_processLPEMNotification"
+ "_remoteClientCountryCode"
+ "_serviceName"
+ "_setPowerState"
+ "_watchdogStartedTimestamp"
+ "_wdTriggeredIterator"
+ "activateWithCompletion:"
+ "airportd.lpem-allowed"
+ "airportd.lpem-do-exit"
+ "airportd.lpem-exit-code"
+ "airportd.lpem-power-state"
+ "airportdProcessSystemConfigurationEvent - Autojoining on interface: %@"
+ "assertId"
+ "autoJoinManager"
+ "caps = %s%s%s%s%s%s, connection[%p] token[0x%08x] capabilties[0x%08x], description:'%s', lastSleepType[0x%08x]/'%s', hibernateStateFound[%u] hibernateState[0x%08x/%u] hibernateMode[0x%08x/%d]"
+ "checkForTimeout"
+ "clientAssociatedToHostPersonalHotspot:"
+ "clientDisassociated:"
+ "com.apple.airportd.WatchdogMonitor"
+ "com.apple.airportd.server.timer.q"
+ "com.apple.airportd.watchdog-monitor"
+ "com.apple.bluetooth.low-power-mode"
+ "copyChanInfoListForInterfaceWithName:connection:error:"
+ "cpu"
+ "defaultPrivateMACMode"
+ "driver %s (reason=0x%x, subreason=0x%x, flags=0x%x), node:isDriverAvailable=%u"
+ "enumerateObjectsUsingBlock:"
+ "firmwareAssertTable"
+ "getRemoteClientCountryCode"
+ "handleCrashNotificationWithID:andCPUName:"
+ "handleWatchdogTriggered"
+ "i1780@0:8{apple80211_network_data=ISCII{apple80211_channel=III}I[32C]{apple80211_key=IIISS[64C]I[8C]{ether_addr=[6C]}I[16C]I[16C][8C]}I[257C][257C]I[1024C]SS}16"
+ "initWithIOService:"
+ "initWithName:vid:isApple:locationID:"
+ "initWithServiceName:"
+ "interface[%@], client[%@] power[%u], err[0x%08x/%u]"
+ "internalQ"
+ "main"
+ "name"
+ "populateWithRssi:rssiInUse:rssi0:rssi1:rssiMode:noise:noise0:noise1:snr:selfCca:otherCca:interference:totalReportedCca:beaconPer:rxCrsGlitch:rxBadPLCP:rxStart:rxBphyCrsGlitch:rxBphyBadPLCP:sampleDuration:isHighCCAFor2GHz:"
+ "populateWithTxFrames:RxFrames:TxFails:TxRetries:RxRetries:TxRate:RxRate:txRTS:txRTSFail:txMpdu:txAMPDU:averageTxPer:"
+ "previousDisassocReason"
+ "scInitInterface"
+ "scInitInterface for device %@"
+ "screenOn"
+ "setCachedNetworkID:"
+ "setDispatchQueue:"
+ "setDisplayOff:"
+ "setFirmwareAssertTable:"
+ "setInternalQ:"
+ "setPreviousDisassocReason:"
+ "setScreenOnChangedHandler:"
+ "setSetCountryCodeHandler:"
+ "setUsbStatus:currentDevices:currentNoiseDelta:"
+ "setWatchdogStartedTimestamp:"
+ "setWiFiPowerState: @[%llu.%06llu], state[%u]"
+ "setWiFiPowerState: @[%llu.%06llu], state[%u], issued Apple80211SetPower, tmpErr[%ld], request took %llu.%06llu"
+ "setWiFiPowerState: @[%llu.%06llu], state[%u], issuing Apple80211SetPower"
+ "setWiFiPowerState: @[%llu.%06llu], state[%u], took %llu.%06llu, powerPrefTS[%llu.%06llu] resetChipTS[%llu.%06llu] usageMonitorTS[%llu.%06llu] updatePowerOffTS[%llu.%06llu] powerReqTS[%llu.%06llu]"
+ "snapshotWithSignature:delay:events:payload:actions:reply:"
+ "startAutoJoinForInterface_block_invoke_2"
+ "updateRemoteClientCountryCode:"
+ "v12@?0i8"
+ "v16@?0@\"NSString\"8"
+ "v32@0:8Q16@24"
+ "v32@?0@8Q16^B24"
+ "v3744@0:8{apple80211_awdl_statistics=IIIIIICCCCCCCCCQQQISIIIQ[6{histogramBin_s=dd(?=[8C]d)}][3{histogramBin_s=dd(?=[8C]d)}]{histogramBin_s=dd(?=[8C]d)}IIIIII[54{apple80211_awdl_state_statistics=IQ}][2[2{apple80211_awdl_srv_statistics=II[8{apple80211_awdl_srv_info=[32C]IQ}]}]][16{apple80211_awdl_services=CCIQ[32C]}]SSSSSSI{apple80211_awdl_d2d_migration_statistics=QQQiICCC}IICCC[8S]IIIIIIIIIIIIIIIII[3C]}16d3736"
+ "watchdogStartedTimestamp"
+ "{apple80211_awdl_statistics=\"version\"I\"flags\"I\"rxBytes\"I\"txBytes\"I\"numOfPacketFailures\"I\"selfInfraChannel\"I\"peerInfraChannel\"C\"numOfPeers\"C\"numOfCachedPeers\"C\"cachedPeersOn24G\"C\"cachedPeersOn5G\"C\"cachedPeersOnDFS\"C\"numOfCachedPeersNoInfra\"C\"numOfCachedPeersDiffInfra\"C\"numOfCachedPeersSameInfra\"C\"noServiceIdleTime\"Q\"sessionDuration\"Q\"suspendedDuration\"Q\"suspendCount\"I\"peerVersionBitmap\"S\"mcastRxBytes\"I\"mcastTxBytes\"I\"afRxBytes\"I\"numSyncChanges\"Q\"hopCount\"[6{histogramBin_s=\"binStart\"d\"binEnd\"d\"\"(?=\"count\"[8C]\"value\"d)}]\"parentRssi\"[3{histogramBin_s=\"binStart\"d\"binEnd\"d\"\"(?=\"count\"[8C]\"value\"d)}]\"txStatusDelay\"{histogramBin_s=\"binStart\"d\"binEnd\"d\"\"(?=\"count\"[8C]\"value\"d)}\"dfspAirplayConnected\"I\"dfspAirplayFailed\"I\"dfspCSAReceivedFromPeer\"I\"dfspCSAReceivedFromAP\"I\"dfspSuspect\"I\"dfspResume\"I\"awdlStates\"[54{apple80211_awdl_state_statistics=\"count\"I\"duration\"Q}]\"awdlServices\"[2[2{apple80211_awdl_srv_statistics=\"srvCount\"I\"srvAddDeleteCount\"I\"services\"[8{apple80211_awdl_srv_info=\"srvKey\"[32C]\"id\"I\"duration\"Q}]}]]\"awdlServicesCompact\"[16{apple80211_awdl_services=\"opCode\"C\"type\"C\"serviceId\"I\"duration\"Q\"serviceKey\"[32C]}]\"numAirplaySessions\"S\"numRTSessions\"S\"numDynSdbAirplayAllowed\"S\"numDynSdbEntrySuccess\"S\"numDynSdbExitDueToRate\"S\"numDynSdbReEntrySuccess\"S\"numInputPacketsDropped\"I\"d2dMigrationStats\"{apple80211_awdl_d2d_migration_statistics=\"sessionDuration\"Q\"txBytes\"Q\"rxBytes\"Q\"peerRssi\"i\"txFailureCount\"I\"channel\"C\"migrationRole\"C\"avgCCA\"C}\"selfInfraChannelFlags\"I\"peerInfraChannelFlags\"I\"cachedPeersOn6G\"C\"self6ECapable\"C\"cachedPeers6ECapable\"C\"lteRestrictedChannelsUsed\"[8S]\"numLteRestrictedChannelsUsed\"I\"numPeersWithZeroExtLen\"I\"peerChannelsteerAttemptCount_2G\"I\"peerChannelsteerAttemptCount_5G\"I\"peerChannelsteerBefore\"I\"peerChannelsteerAfter\"I\"psfDwellSessionCount\"I\"enableCount\"I\"totalDuration\"I\"inActiveDuration\"I\"activeDuration\"I\"percentageInactiveTime\"I\"timeToService\"I\"percentageInfraIdleTime\"I\"percentageInfraRealTime\"I\"percentageInfraNonRealTime\"I\"timeSinceLastAwdlStatsPost\"I\"oui\"[3C]}"
+ "{apple80211_network_data=ISCII{apple80211_channel=III}I[32C]{apple80211_key=IIISS[64C]I[8C]{ether_addr=[6C]}I[16C]I[16C][8C]}I[257C][257C]I[1024C]SS}24@0:8@16"
- "%s install environment (RecoveryOS)"
- "%s: ARP/NDP offloads disabled, not programming the offload\n"
- "%s: Null device node\n"
- "%s: SCDynamicStore took %llu.%06llu\n"
- "-[CWXPCSubsystem __rememberWiFiNetwork:profileID:collocatedProfileID:password:is8021X:isUserMode8021X:isWEP40:isWEPOpenSystem:passpointDomain:remember:isAutoJoin:possiblyHidden:updateUserKeychain:interface:has6GHzOnlyBSS:isSetupNetwork:isPrivateMACFailureFallback:temporaryPrivateMACSetting:error:]"
- "-[CWXPCSubsystem queryChanInfoListForInterfaceWithName:connection:error:]"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AirPort_executables/Tools/airportd/airportProcessCommand.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AirPort_executables/Tools/airportd/airportdCommandLine.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AirPort_executables/Tools/airportd/airportdMain.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AirPort_executables/Tools/airportd/airportdPreferences.m"
- "<%s[%d]> %s: ARP/NDP offloads disabled, not programming the offload\n"
- "<%s[%d]> %s: Acknowledging sleep event\n"
- "<%s[%d]> %s: AirPort Interface <%s> <%d>\n"
- "<%s[%d]> %s: Did create BSS details for scanning state usage\n"
- "<%s[%d]> %s: Did set scanning state for scanning usage monitor\n"
- "<%s[%d]> %s: Did update beacon info for scanning state usage\n"
- "<%s[%d]> %s: Processing event, count[%3lu]\n"
- "<%s[%d]> %s: SCDynamicStore took %llu.%06llu\n"
- "<%s[%d]> %s: Thermal index %d not above threshold %d, will not continue auto-join\n"
- "<%s[%d]> %s: Unexpected link down. Triggering auto-join.\n"
- "<%s[%d]> %s: Will create BSS details for scanning state usage\n"
- "<%s[%d]> %s: Will set scanning state for scanning usage monitor\n"
- "<%s[%d]> %s: Will update beacon info for scanning state usage\n"
- "<%s[%d]> %s: caps = %s%s%s%s%s%s\n"
- "<%s[%d]> %s: driver %s (reason=0x%x, subreason=0x%x, flags=0x%x)\n"
- "<%s[%d]> <%@> AWDL assisted discovery mode is active, will not continue auto-join\n"
- "<%s[%d]> <%@> AWDL real time mode is active, will not continue auto-join\n"
- "<%s[%d]> <%@> Auto-join deferral is active, will not continue auto-join\n"
- "<%s[%d]> <%@> Auto-join is disabled (via boot-arg), will not continue auto-join\n"
- "<%s[%d]> <%@> Auto-join is disabled, will not continue auto-join\n"
- "<%s[%d]> <%@> FAILED to configure scan offloads, returned error code %d (%s)\n"
- "<%s[%d]> <%@> Scan offloads will be %s (lpas_supported=%s, softap=%s, wow=%s, tcpka=%s, allow_unassoc_wakes=%s, allow_disconn_sleeps=%s, aj_disabled=%s, scan_offload_disabled_until=%@)\n"
- "<%s[%d]> <%@> Successfully configured scan offloads\n"
- "<%s[%d]> <%@> User login trigger with no console user, will not continue auto-join\n"
- "<%s[%d]> AUTO-JOIN %s for interface %@, took %.4f seconds, returned result '%s', error %@\n"
- "<%s[%d]> AUTO-JOIN STARTED for interface %@ (%@)\n"
- "<%s[%d]> AutoJoin %s (assert=%s, activity=%s, join=%s, until=%@, prev=%s)\n"
- "<%s[%d]> DYNAMIC STORE UPDATE FAILED for interface %@, returned error %s\n"
- "<%s[%d]> DYNAMIC STORE UPDATE Successful for interface %@\n"
- "<%s[%d]> INITIAL SETUP => fallback to auto-join using NVRAM\n"
- "<%s[%d]> Ignoring redundant auto-join invocation for interface %@\n"
- "<%s[%d]> ScDeinitInterface for device %@\n"
- "<%s[%d]> System is sleeping, will not continue auto-join\n"
- "<%s[%d]> WiFi interface %@ is not a primary interface, will not continue auto-join\n"
- "<%s[%d]> WiFi interface is OFF, will not continue auto-join\n"
- "<%s[%d]> WiFi interface is in SWAP mode, will not continue auto-join\n"
- "<%s[%d]> WiFi interface is in monitor mode, will not continue auto-join\n"
- "<%s[%d]> WoW %s (assert=%s, pref=%s activity=%s, ps=%s, icloud=%s, tcpka=%s, pno=%d, lpas=%s)\n"
- "<%s[%d]> scInitInterface for device %@\n"
- "<%s[%d]> start DYNAMIC STORE UPDATE for interface %@\n"
- "B124@0:8@16@24@32@40B48B52B56B60@64B72B76B80B84@88B96B100B104q108^@116"
- "Processing event, count[%3lu]"
- "SCDynamicStore took %llu.%06llu"
- "[airport] @[%llu.%06llu] (%s:%d) %s"
- "__getAutoJoinMetric:"
- "__getAutoJoinStatistics:"
- "__performScanWithChannels:ssidList:legacyScanSSID:maxAge:maxMissCount:maxWakeCount:maxAutoJoinCount:interfaceName:waitForWiFi:waitForBluetooth:token:priority:scanParametersOverride:allowDuringAWDLRealTimeMode:XPCConnection:reply:"
- "__rememberWiFiNetwork:profileID:collocatedProfileID:password:is8021X:isUserMode8021X:isWEP40:isWEPOpenSystem:passpointDomain:remember:isAutoJoin:possiblyHidden:updateUserKeychain:interface:has6GHzOnlyBSS:isSetupNetwork:isPrivateMACFailureFallback:temporaryPrivateMACSetting:error:"
- "__resetAutoJoinStatistics:"
- "duration"
- "filename=%s"
- "function=%s"
- "i1776@0:8{apple80211_network_data=ISCII{apple80211_channel=III}I[32C]{apple80211_key=IIISS[64C]I[8C]{ether_addr=[6C]}I[16C]I[16C][8C]}I[257C][257C]I[1024C]}16"
- "line=%d"
- "link_register=%llx"
- "minor_reason=0x%x"
- "populateWithRssi:rssi0:rssi1:rssiMode:noise:noise0:noise1:snr:selfCca:otherCca:interference:totalReportedCca:beaconPer:rxCrsGlitch:rxBadPLCP:rxStart:rxBphyCrsGlitch:rxBphyBadPLCP:sampleDuration:"
- "populateWithTxFrames:RxFrames:TxFails:TxRetries:RxRetries:TxRate:RxRate:txRTS:txRTSFail:txMpdu:txAMPDU:"
- "program_counter=%llx"
- "queryChanInfoListForInterfaceWithName:connection:error:"
- "snapshotWithSignature:duration:events:payload:actions:reply:"
- "sub_reason=0x%x"
- "trap_info_seq_num=%d"
- "v132@0:8@16@24@32d40q48q56q64@72B80B84q88q96@104B112@116@?124"
- "v3736@0:8{apple80211_awdl_statistics=IIIIIICCCCCCCCCQQQISIIIQ[6{histogramBin_s=dd(?=[8C]d)}][3{histogramBin_s=dd(?=[8C]d)}]{histogramBin_s=dd(?=[8C]d)}IIIIII[54{apple80211_awdl_state_statistics=IQ}][2[2{apple80211_awdl_srv_statistics=II[8{apple80211_awdl_srv_info=[32C]IQ}]}]][16{apple80211_awdl_services=CCIQ[32C]}]SSSSSSI{apple80211_awdl_d2d_migration_statistics=QQQiICCC}IICCC[8S]IIIIIIIIIIIIIIII[3C]}16d3728"
- "{apple80211_awdl_statistics=\"version\"I\"flags\"I\"rxBytes\"I\"txBytes\"I\"numOfPacketFailures\"I\"selfInfraChannel\"I\"peerInfraChannel\"C\"numOfPeers\"C\"numOfCachedPeers\"C\"cachedPeersOn24G\"C\"cachedPeersOn5G\"C\"cachedPeersOnDFS\"C\"numOfCachedPeersNoInfra\"C\"numOfCachedPeersDiffInfra\"C\"numOfCachedPeersSameInfra\"C\"noServiceIdleTime\"Q\"sessionDuration\"Q\"suspendedDuration\"Q\"suspendCount\"I\"peerVersionBitmap\"S\"mcastRxBytes\"I\"mcastTxBytes\"I\"afRxBytes\"I\"numSyncChanges\"Q\"hopCount\"[6{histogramBin_s=\"binStart\"d\"binEnd\"d\"\"(?=\"count\"[8C]\"value\"d)}]\"parentRssi\"[3{histogramBin_s=\"binStart\"d\"binEnd\"d\"\"(?=\"count\"[8C]\"value\"d)}]\"txStatusDelay\"{histogramBin_s=\"binStart\"d\"binEnd\"d\"\"(?=\"count\"[8C]\"value\"d)}\"dfspAirplayConnected\"I\"dfspAirplayFailed\"I\"dfspCSAReceivedFromPeer\"I\"dfspCSAReceivedFromAP\"I\"dfspSuspect\"I\"dfspResume\"I\"awdlStates\"[54{apple80211_awdl_state_statistics=\"count\"I\"duration\"Q}]\"awdlServices\"[2[2{apple80211_awdl_srv_statistics=\"srvCount\"I\"srvAddDeleteCount\"I\"services\"[8{apple80211_awdl_srv_info=\"srvKey\"[32C]\"id\"I\"duration\"Q}]}]]\"awdlServicesCompact\"[16{apple80211_awdl_services=\"opCode\"C\"type\"C\"serviceId\"I\"duration\"Q\"serviceKey\"[32C]}]\"numAirplaySessions\"S\"numRTSessions\"S\"numDynSdbAirplayAllowed\"S\"numDynSdbEntrySuccess\"S\"numDynSdbExitDueToRate\"S\"numDynSdbReEntrySuccess\"S\"numInputPacketsDropped\"I\"d2dMigrationStats\"{apple80211_awdl_d2d_migration_statistics=\"sessionDuration\"Q\"txBytes\"Q\"rxBytes\"Q\"peerRssi\"i\"txFailureCount\"I\"channel\"C\"migrationRole\"C\"avgCCA\"C}\"selfInfraChannelFlags\"I\"peerInfraChannelFlags\"I\"cachedPeersOn6G\"C\"self6ECapable\"C\"cachedPeers6ECapable\"C\"lteRestrictedChannelsUsed\"[8S]\"numLteRestrictedChannelsUsed\"I\"numPeersWithZeroExtLen\"I\"peerChannelsteerAttemptCount_2G\"I\"peerChannelsteerAttemptCount_5G\"I\"peerChannelsteerBefore\"I\"peerChannelsteerAfter\"I\"psfDwellSessionCount\"I\"enableCount\"I\"totalDuration\"I\"inActiveDuration\"I\"activeDuration\"I\"percentageInactiveTime\"I\"timeToService\"I\"percentageInfraIdleTime\"I\"percentageInfraRealTime\"I\"percentageInfraNonRealTime\"I\"oui\"[3C]}"
- "{apple80211_network_data=ISCII{apple80211_channel=III}I[32C]{apple80211_key=IIISS[64C]I[8C]{ether_addr=[6C]}I[16C]I[16C][8C]}I[257C][257C]I[1024C]}24@0:8@16"

```
