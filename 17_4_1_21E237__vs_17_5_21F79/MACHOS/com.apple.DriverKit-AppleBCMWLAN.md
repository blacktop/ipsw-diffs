## com.apple.DriverKit-AppleBCMWLAN

> `/System/Library/DriverExtensions/com.apple.DriverKit-AppleBCMWLAN.dext/com.apple.DriverKit-AppleBCMWLAN`

```diff

-1160.11.0.0.0
-  __TEXT.__text: 0x25c7dc
+1170.7.0.0.0
+  __TEXT.__text: 0x25bf3c
   __TEXT.__auth_stubs: 0x2d80
   __TEXT.__init_offsets: 0x1d4
-  __TEXT.__cstring: 0x85d5e
-  __TEXT.__const: 0x723a0
-  __TEXT.__oslogstring: 0x34c5
-  __TEXT.__unwind_info: 0x3cf4
+  __TEXT.__cstring: 0x85a42
+  __TEXT.__const: 0x72570
+  __TEXT.__oslogstring: 0x3464
+  __TEXT.__unwind_info: 0x3ce8
   __DATA_CONST.__auth_got: 0x16c0
   __DATA_CONST.__got: 0x108
-  __DATA_CONST.__const: 0x21c90
+  __DATA_CONST.__const: 0x219f0
   __DATA_CONST.__osclassinfo: 0x398
   __DATA.__data: 0x720
   __DATA.__bss: 0x950

   - /System/DriverKit/System/Library/PrivateFrameworks/OLYHALDriverKit.framework/OLYHALDriverKit
   - /System/DriverKit/usr/lib/libc++.dylib
   - @rpath/BroadcomWLANDriverKit.framework/BroadcomWLANDriverKit
-  UUID: 4FB44A11-555D-3965-B9F8-BA465F16B4B3
-  Functions: 7545
-  Symbols:   10396
-  CStrings:  13396
+  UUID: 5B04AAA2-6010-3478-BAD9-9E2036A77CB1
+  Functions: 7546
+  Symbols:   10393
+  CStrings:  13349
 
Symbols:
+ __ZN16AppleBCMWLANCore20cleanFWMulticastListEv
+ __ZN16AppleBCMWLANCore25setAllMulticastModeEnableEb
+ __ZN16AppleBCMWLANCore26_setAllMulticastModeEnableEb
+ __ZN16AppleBCMWLANCore8is4387UpEv
+ __ZN23AppleBCMWLANJoinAdapter10setJoiningEb
+ __ZN23AppleBCMWLANJoinManager28disableSupplicantEventsAsyncEv
+ __ZN24AppleBCMWLANPowerManager12getOPSStatusEP19apple80211_ops_data
+ __ZN28AppleBCMWLANSkywalkInterface25setAllMulticastModeEnableEb
+ __ZThn48_N28AppleBCMWLANSkywalkInterface25setAllMulticastModeEnableEb
- __ZL19kWakeToIntEnMapping
- __ZL24kSystemPowerStateMapping
- __ZL30kSystemPowerStateReportsLegend
- __ZL35kWakeToInterfaceEnableReportsLegend
- __ZN23AppleBCMWLANIOReporting26getMaxSupportedEventLogSetEv
- __ZN23AppleBCMWLANJoinAdapter28disableSupplicantEventsAsyncEv
- __ZN24AppleBCMWLANPowerManager12getOPSStatusEP16wl_ops_status_v1
- __ZN27AppleBCMWLANIOReportingCore23makeEventLogSetRateHistEh
- __ZN27AppleBCMWLANIOReportingCore23makeEventLogSetSizeHistEh
- __ZN27AppleBCMWLANIOReportingCore25createWakeToIntEnReporterE10SleepModes
- __ZN27AppleBCMWLANIOReportingCore30createSystemPowerStateReporterE26systemPowerStateCheckPoint
- __ZN27AppleBCMWLANIOReportingCore44sendWakeToInterfaceEnableTimeToCoreAnalyticsEjj
CStrings:
+ "\"AppleBCMWLANV3_driverkit-1170.7\""
+ "/AppleInternal/Library/BuildRoots/46e3eceb-fa0c-11ee-9172-fa87d3da4027/Applications/Xcode.app/Contents/Developer/Platforms/DriverKit.platform/Developer/SDKs/DriverKit.iPhoneOS23.5.Internal.sdk/System/DriverKit/System/Library/PrivateFrameworks/IO80211DriverKit.framework/PrivateHeaders/IO80211Util.h"
+ "AppleBCMWLANV3_driverkit-1170.7"
+ "Apr 14 2024 10:21:32"
+ "[dk] %s@%d: cleanFWMulticastList failed, error %s\n"
+ "[dk] %s@%d: resetMulticastList failed, error %s\n"
+ "[dk] %s@%d: setAllMulticast(false) failed, error %s\n"
+ "[dk] %s@%d: setAllMulticast(true) failed, error %s\n"
+ "[dk] %s@%d:OPS STATUS: Version=%d Len=%d slice_index=%d disable_obss=%d disable_reasons=%d disable_duration=%d applied_ops_config=%d partial_ops_dur=%d full_ops_dur=%d OPS Histogram[%d] [%d] [%d] [%d] [%d] nav_cnt=%d plcp_cnt=%d mybss_cnt=%d obss_cnt=%d miss_dur_cnt=%d miss_pret_cnt=%d max_dur_cnt=%d wake_cnt=%d bcn_wait_cnt=%d rx_time_mybss=%d,rx_time_ibss=%d,rx_time_obss=%d\n"
+ "[dk] %s@%d:OPS: Unable to allocate memory for rxBuffSize\n"
+ "[dk] %s@%d:setAllMulticastModeEnable( %d ) failed\n"
+ "_setAllMulticastModeEnable"
+ "cleanFWMulticastList"
+ "disableSupplicantEventsAsync"
+ "setAllMulticastModeEnable"
- "\"AppleBCMWLANV3_driverkit-1160.11\""
- "%c [dk] %s@%d:  received a supplicant event when we're not monitoring (reason=%lu status=%lu), \n"
- "/AppleInternal/Library/BuildRoots/2d3303f9-dd50-11ee-ac91-22c3409c8aad/Applications/Xcode.app/Contents/Developer/Platforms/DriverKit.platform/Developer/SDKs/DriverKit.iPhoneOS23.4.Internal.sdk/System/DriverKit/System/Library/PrivateFrameworks/IO80211DriverKit.framework/PrivateHeaders/IO80211Util.h"
- "AppleBCMWLANV3_driverkit-1160.11"
- "Event Log Hist"
- "Mar  8 2024 23:44:53"
- "SystemPowerState"
- "WakeToInterfaceEnable"
- "[dk] %s@%d: received a supplicant event when we're not monitoring (reason=%lu status=%lu), \n"
- "[dk] %s@%d:Failed to create IOReporter - ivars->fEventLogSetRateHistReporter\n"
- "[dk] %s@%d:Failed to create IOReporter - ivars->fEventLogSetSizeHistReporter\n"
- "[dk] %s@%d:Failed to create IOReporter - ivars->fEventLogSetStopwatch\n"
- "[dk] %s@%d:Failed to create histogram for %s %lld\n"
- "[dk] %s@%d:Invalid SleepMode type =%d\n"
- "com.apple.wifi.wakeToInterfaceEnableTime"
- "kSleepModeLPASAssociated"
- "kSleepModeNonWoW"
- "kSleepModeWoWAssociated"
- "kSleepModeWoWUnassociatedPNO"
- "kSystemAWDLLinkDisabled"
- "kSystemAWDLLinkEnabled"
- "kSystemBusPowerOff"
- "kSystemBusPowerOn"
- "kSystemDeltaPowerOff"
- "kSystemDeltaPowerOn"
- "kSystemLPASPowerOff"
- "kSystemLPASPowerOn"
- "kSystemPNOPowerOff"
- "kSystemPNOPowerOn"
- "kSystemSoftAPPowerOff"
- "kSystemSoftAPPowerOn"
- "kSystemUnassocPowerOff"
- "kSystemUnassocPowerOn"
- "kSystemWowPowerOff"
- "kSystemWowPowerOn"
- "makeEventLogSetRateHist"
- "makeEventLogSetSizeHist"
- "sendWakeToInterfaceEnableTimeToCoreAnalytics"
- "sleepModeLPASAssociated"
- "sleepModeNonWoW"
- "sleepModeWoWAssociated"
- "sleepModeWoWUnassociatedPNO"
- "system AWDL Link disabled"
- "system AWDL Link enabled"
- "system LPAS power off"
- "system LPAS power on"
- "system PNO power off"
- "system PNO power on"
- "system WoW power off"
- "system WoW power on"
- "system bus power off"
- "system bus power on"
- "system delta power off"
- "system delta power on"
- "system softAP power off"
- "system softAP power on"
- "system unassoc power off"
- "system unassoc power on"
- "wake to interface enable LPAS "
- "wake to interface enable Non WoW"
- "wake to interface enable PNO"
- "wake to interface enable WoW "

```
