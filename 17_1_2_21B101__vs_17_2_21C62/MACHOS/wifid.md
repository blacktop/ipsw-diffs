## wifid

> `/usr/sbin/wifid`

```diff

-1663.10.0.0.0
-  __TEXT.__text: 0x17d50c
-  __TEXT.__auth_stubs: 0x2520
-  __TEXT.__objc_stubs: 0x10a40
-  __TEXT.__objc_methlist: 0x4fcc
-  __TEXT.__objc_methname: 0x16035
+1663.16.0.0.0
+  __TEXT.__text: 0x17e19c
+  __TEXT.__auth_stubs: 0x2550
+  __TEXT.__objc_stubs: 0x10b40
+  __TEXT.__objc_methlist: 0x4ff4
+  __TEXT.__objc_methname: 0x16151
   __TEXT.__objc_classname: 0x7ab
-  __TEXT.__objc_methtype: 0x2be1
+  __TEXT.__objc_methtype: 0x2be4
   __TEXT.__const: 0x8c0
   __TEXT.__gcc_except_tab: 0x17f4
-  __TEXT.__cstring: 0x63052
+  __TEXT.__cstring: 0x6369d
   __TEXT.__ustring: 0x4c2
   __TEXT.__oslogstring: 0x245
   __TEXT.__dlopen_cstrs: 0x1a5
-  __TEXT.__unwind_info: 0x3304
-  __DATA_CONST.__auth_got: 0x12a0
-  __DATA_CONST.__got: 0xfc8
-  __DATA_CONST.__auth_ptr: 0x130
-  __DATA_CONST.__const: 0x67e8
-  __DATA_CONST.__cfstring: 0x1b440
+  __TEXT.__unwind_info: 0x3320
+  __DATA_CONST.__auth_got: 0x12b8
+  __DATA_CONST.__got: 0xfd0
+  __DATA_CONST.__auth_ptr: 0x138
+  __DATA_CONST.__const: 0x6878
+  __DATA_CONST.__cfstring: 0x1b9e0
   __DATA_CONST.__objc_classlist: 0x1c0
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0xd0

   __DATA_CONST.__objc_dictobj: 0x140
   __DATA_CONST.__objc_arrayobj: 0xc0
   __DATA_CONST.__objc_floatobj: 0x10
-  __DATA.__objc_const: 0xd590
-  __DATA.__objc_selrefs: 0x4d70
+  __DATA.__objc_const: 0xd5c0
+  __DATA.__objc_selrefs: 0x4db0
   __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0x6a0
+  __DATA.__objc_classrefs: 0x6a8
   __DATA.__objc_superrefs: 0x1a0
-  __DATA.__objc_ivar: 0x8c4
+  __DATA.__objc_ivar: 0x8c8
   __DATA.__objc_data: 0x1180
   __DATA.__data: 0x1040
   __DATA.__bss: 0x7e0

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/Network.framework/Network
+  - /System/Library/Frameworks/NetworkExtension.framework/NetworkExtension
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
   - /System/Library/Frameworks/UserNotifications.framework/UserNotifications

   - /System/Library/PrivateFrameworks/CPMS.framework/CPMS
   - /System/Library/PrivateFrameworks/CaptiveNetwork.framework/CaptiveNetwork
   - /System/Library/PrivateFrameworks/CarKit.framework/CarKit
+  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreRoutine.framework/CoreRoutine
   - /System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi
   - /System/Library/PrivateFrameworks/CrashReporterSupport.framework/CrashReporterSupport

   - /System/Library/PrivateFrameworks/Symptoms.framework/Frameworks/ManagedEvent.framework/ManagedEvent
   - /System/Library/PrivateFrameworks/Symptoms.framework/Frameworks/SymptomAnalytics.framework/SymptomAnalytics
   - /System/Library/PrivateFrameworks/Symptoms.framework/Frameworks/SymptomPresentationFeed.framework/SymptomPresentationFeed
+  - /System/Library/PrivateFrameworks/TCC.framework/TCC
   - /System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities
   - /System/Library/PrivateFrameworks/WatchdogClient.framework/WatchdogClient
   - /System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics

   - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libpcap.A.dylib
-  Functions: 5237
-  Symbols:   1275
-  CStrings:  14712
+  Functions: 5248
+  Symbols:   1280
+  CStrings:  14776
 
Symbols:
+ _AnalyticsSendEventLazy
+ _OBJC_CLASS_$_NEPathController
+ _TCCAccessCopyBundleIdentifiersDisabledForService
+ _TCCAccessCopyBundleIdentifiersForService
+ _kTCCServiceBluetoothAlways
CStrings:
+ "#\x84\x11t"
+ "%s Updating 6G standalone property after iCloud sync on %@"
+ "%s bundleId has multicastAllow = %d set"
+ "%s bundleId present in fAllowedAppBundles %@"
+ "%s bundleId present in fDisallowedAppBundles %@"
+ "%s: Initialized with 5G status."
+ "%s: Initialized with No LTE status."
+ "%s: Initialized with roaming status."
+ "%s: WiFiBatteryMgmt :  No pending requests, exiting"
+ "%s: managerQueue is not SET"
+ "-[WiFiAIRAgent setWiFiManagerQueue:]"
+ "-[WiFiBlacklistNetwork initWithArgs:deviceManager:mergeWithNetworkProfile:]"
+ "@\"NSDictionary\"8@?0"
+ "@36@0:8^{__WiFiNetwork=}16^{__WiFiDeviceManager=}24B32"
+ "AddReason"
+ "AppBundleID"
+ "BTTCCState"
+ "BluetoothTCCDisabled"
+ "BluetoothTCCEnabled"
+ "BluetoothTCCUnknown"
+ "CoreAnalytics metricsDict %@"
+ "Hotspot20"
+ "LocalNetworkTCCDisabled"
+ "LocalNetworkTCCEnabled"
+ "LocalNetworkTCCState"
+ "LocalNetworkTCCUnknown"
+ "Operation"
+ "Process"
+ "Result"
+ "SecurityType"
+ "SessionBased"
+ "Setup"
+ "T@\"NSDate\",&,N,V_asyncPPMBudgetTimestamp"
+ "UsedPrefix"
+ "WiFiKnownNetworkAdded"
+ "WiFiManager-1663.16 Nov 12 2023 10:33:51"
+ "WiFiManager-1663.16 Nov 12 2023 10:34:15"
+ "__WiFiDeviceManagerUnifiedAutoJoinCheckForStandalone6G"
+ "__WiFiManagerBluetoothTCCState"
+ "__WiFiManagerLocalNetworkTCCState"
+ "__currentNetworkMergedScanRecord"
+ "__currentNetworkProfile"
+ "_asyncPPMBudgetTimestamp"
+ "asyncPPMBudgetTimestamp"
+ "com.apple.wifi.knownnetwork"
+ "copyAggregatePathRules"
+ "denyMulticast"
+ "duration"
+ "initWithArgs:deviceManager:mergeWithNetworkProfile:"
+ "kWiFiAddNetworkOriginator3rdParty"
+ "kWiFiAddNetworkOriginatorCarrierBundle"
+ "kWiFiAddNetworkOriginatorSetupAssistant"
+ "kWiFiAddNetworkOriginatorTapToSetup"
+ "kWiFiAddNetworkOriginatorUser"
+ "kWiFiAddNetworkOriginatorWallet"
+ "kWiFiManagerAddNetworkResultAlreadyAssociated"
+ "kWiFiManagerAddNetworkResultApplicationIsNotInForeground"
+ "kWiFiManagerAddNetworkResultAssociationFailed"
+ "kWiFiManagerAddNetworkResultExistingNetwork"
+ "kWiFiManagerAddNetworkResultInvalidBundleId"
+ "kWiFiManagerAddNetworkResultNetworkNotFound"
+ "kWiFiManagerAddNetworkResultRequestPending"
+ "kWiFiManagerAddNetworkResultSuccess"
+ "kWiFiManagerAddNetworkResultSystemCancelled"
+ "kWiFiManagerAddNetworkResultUnknownError"
+ "kWiFiManagerAddNetworkResultUserCancelled"
+ "kWiFiNetworkAuthFlagsEAP"
+ "kWiFiNetworkAuthFlagsOpen"
+ "kWiFiNetworkAuthFlagsWEP"
+ "kWiFiNetworkAuthFlagsWPA"
+ "matchSigningIdentifier"
+ "multicastPreferenceSet"
+ "setAsyncPPMBudgetTimestamp:"
- "#\x84\x11s"
- "%s: disabled with missing CarPlay UUID for CarPlay network %@ mode %d"
- "-[WiFiAIRAgent initWithManagerQueue:]"
- "-[WiFiBlacklistNetwork initWithArgs:deviceManager:]"
- "@32@0:8^{__WiFiNetwork=}16^{__WiFiDeviceManager=}24"
- "WiFiManager-1663.10 Oct  4 2023 23:06:44"
- "WiFiManager-1663.10 Oct  4 2023 23:07:09"
- "__currentNetwork"
- "initWithArgs:deviceManager:"

```
