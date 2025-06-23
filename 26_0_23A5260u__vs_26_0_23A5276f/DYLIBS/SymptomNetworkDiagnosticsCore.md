## SymptomNetworkDiagnosticsCore

> `/System/Library/PrivateFrameworks/SymptomNetworkDiagnosticsCore.framework/SymptomNetworkDiagnosticsCore`

```diff

-2130.0.0.0.1
-  __TEXT.__text: 0x75874
-  __TEXT.__auth_stubs: 0x1890
+2138.0.0.0.0
+  __TEXT.__text: 0x77ed0
+  __TEXT.__auth_stubs: 0x18c0
   __TEXT.__objc_methlist: 0x188
-  __TEXT.__cstring: 0x1196
-  __TEXT.__const: 0x3350
-  __TEXT.__oslogstring: 0x399b
-  __TEXT.__constg_swiftt: 0x1074
-  __TEXT.__swift5_typeref: 0xdc4
-  __TEXT.__swift5_reflstr: 0x976
-  __TEXT.__swift5_fieldmd: 0xc0c
-  __TEXT.__swift5_types: 0xe0
+  __TEXT.__const: 0x3360
+  __TEXT.__swift5_typeref: 0xdb4
+  __TEXT.__cstring: 0x126a
+  __TEXT.__oslogstring: 0x3b43
+  __TEXT.__constg_swiftt: 0x10c4
+  __TEXT.__swift5_reflstr: 0x9e5
+  __TEXT.__swift5_fieldmd: 0xc30
   __TEXT.__swift5_proto: 0x29c
-  __TEXT.__swift5_capture: 0x44c
-  __TEXT.__swift_as_entry: 0x184
-  __TEXT.__swift_as_ret: 0x14c
+  __TEXT.__swift5_types: 0xe0
+  __TEXT.__swift5_capture: 0x468
+  __TEXT.__swift_as_entry: 0x194
+  __TEXT.__swift_as_ret: 0x164
   __TEXT.__swift5_assocty: 0x50
   __TEXT.__swift5_acfuncs: 0x28
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x1968
-  __TEXT.__eh_frame: 0x3be8
+  __TEXT.__unwind_info: 0x19d8
+  __TEXT.__eh_frame: 0x3da0
   __TEXT.__objc_classname: 0x52
   __TEXT.__objc_methname: 0x747
   __TEXT.__objc_methtype: 0xad
   __DATA_CONST.__got: 0x410
-  __DATA_CONST.__const: 0x1a0
+  __DATA_CONST.__const: 0x180
   __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x2c0
   __DATA_CONST.__objc_protorefs: 0x38
-  __AUTH_CONST.__auth_got: 0xc48
-  __AUTH_CONST.__const: 0x1c60
-  __AUTH_CONST.__objc_const: 0x1698
+  __AUTH_CONST.__auth_got: 0xc60
+  __AUTH_CONST.__const: 0x1c88
+  __AUTH_CONST.__objc_const: 0x16f8
   __AUTH.__data: 0x100
   __DATA.__data: 0x5e8
-  __DATA.__bss: 0x5018
-  __DATA.__common: 0x50
+  __DATA.__bss: 0x5010
+  __DATA.__common: 0x68
   __DATA_DIRTY.__objc_data: 0x2d0
-  __DATA_DIRTY.__data: 0x15a0
+  __DATA_DIRTY.__data: 0x15e0
   __DATA_DIRTY.__bss: 0xa50
-  __DATA_DIRTY.__common: 0x1f8
+  __DATA_DIRTY.__common: 0x1f0
   - /System/Library/Frameworks/CoreData.framework/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftDistributed.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: A6D85EE9-20A0-38DF-B2BD-AFF9EAA952F5
-  Functions: 1826
-  Symbols:   712
-  CStrings:  502
+  UUID: 3093991F-3FA9-355B-BC21-1F1F26EB49CD
+  Functions: 1855
+  Symbols:   702
+  CStrings:  510
 
Symbols:
+ _swift_conformsToProtocol2
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swiftDarwin_$_SymptomNetworkDiagnosticsCore
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_SymptomNetworkDiagnosticsCore
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_SymptomNetworkDiagnosticsCore
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_SymptomNetworkDiagnosticsCore
- _swift_conformsToProtocol
- _symbolic Su
- _symbolic _____ySuG 29SymptomNetworkDiagnosticsCore29NDFUserDefaultsBackedPropertyC
CStrings:
+ " \t\t debounce interval upon primary resident change: %ss"
+ " \t\t inter-polling discovery cadence: between %s-%ss, minimum duration between polls: %ss"
+ "Aborting further polling attempts for endpoint <%{private}s: %s>"
+ "Cannot get detection manager to proceed with misconfig detection for target device %s"
+ "Cannot get groupUUID of target device %s to proceed with misconfig detection"
+ "Cannot get primary resident to proceed with misconfig detection for target device %s"
+ "Compared DOI: %s with Primary: %s for af: %d, match: %{bool}d, sigsMatch: %{bool}d"
+ "DOI ID: %s, Primary ID: %s, matchSigV4: %{bool}d, matchSigV6: %{bool}d, sigsMatch: %{bool}d, ssidsMatch: %{bool}d, doubleNAT: %{bool}d, multicastTrafficBlocked: %{bool}d"
+ "DOI hashed SSID: %s, Primary hashed SSID: %s, ssidsMatch: %{bool}d"
+ "DOI multicastTrafficBlocked: %{bool}d, Primary multicastTrafficBlocked: %{bool}d"
+ "DOI natCountV4: %hd, Primary natCountV4: %hd, doubleNAT: %{bool}d"
+ "Detecting misconfiguration of DOI: %s against Primary: %s"
+ "Device polling is disallowed"
+ "Discovery+polling cancelled"
+ "Discovery+polling not in progress, nothing to stop"
+ "Error during periodic discovery+polling: %@"
+ "Failed to create periodic timer for discovery+polling"
+ "Failed to ping actor at endpoint %s: %@"
+ "Finished polling and processing for device <%{private}s: %s>"
+ "HomeKit property changed|"
+ "No endpoints discovered during periodic discovery"
+ "Notice: Sleeping %fs will exceed the next deadline of %f"
+ "Polling device state and events from <%{private}s: %s> [poll attempt: %ld]"
+ "Skipping misconfiguration detection as DOI and Primary are not in the same HomeKit group"
+ "Sleeping for %fs to try again..."
+ "Starting periodic discovery+polling for device state and events [iteration %ld]"
+ "Starting periodic discovery+polling for device state and events with interval of %fs"
+ "Stopped periodic discovery+polling"
+ "Successfully retrieved device state info and %ld active events from device <%{private}s: %s>"
+ "Updated primary resident ID for group %s to %s, all known primary residents: %s"
+ "Waiting for %f sec before triggering misconfig detection, elapsedSincePrimaryChanged: %f sec"
+ "[Group %s] Device with ID %s was neither the primary resident before, nor is it now"
+ "_discoveryTimerIntervalMaximum"
+ "_discoveryTimerIntervalMinimum"
+ "_primaryResidentChangeDebounceInterval"
+ "com.apple.symptomsd.NDFActorManagerDiscoveryAndPolling"
+ "currentDiscoveryInterval"
+ "discoveryTimer"
+ "polling_discovery_cadence_max"
+ "polling_discovery_cadence_min"
+ "primaryResidentLastUpdated"
+ "primary_resident_change_debounce_interval"
- " \t\t inter-polling discovery cadence: every %ss, requests per endpoint: %lu, duration between polls: %ss"
- "Cannot get detection manager to proceed with misconfig detection"
- "Cannot get groupUUID of device %s to proceed with misconfig detection"
- "Cannot get primary resident to proceed with misconfig detection"
- "Compared DOI: %s with main: %s for af: %d, match: %{bool}d, sigsMatch: %{bool}d"
- "DOI ID: %s, main ID: %s, matchSigV4: %{bool}d, matchSigV6: %{bool}d, sigsMatch: %{bool}d, ssidsMatch: %{bool}d, doubleNAT: %{bool}d, multicastTrafficBlocked: %{bool}d"
- "DOI hashed SSID: %s, main SSID: %s, ssidsMatch: %{bool}d"
- "DOI multicastTrafficBlocked: %{bool}d, main multicastTrafficBlocked: %{bool}d"
- "DOI natCountV4 is %hd, Main natCountV4 is %hd"
- "DOI natCountV4: %hd, main natCountV4: %hd, doubleNAT: %{bool}d"
- "DOI ssidObs is %s, Main ssidObs is %s"
- "Detecting misconfiguration of DOI: %s against %s"
- "Error during periodic event polling: %@"
- "Event polling cancelled"
- "Failed to create periodic timer for polling"
- "Failed to ping actor having endpoint %s: %@"
- "No endpoints discovered during periodic event polling"
- "Not polling for events as event polling is disabled"
- "Not polling for events as polling is disallowed"
- "Polling device state and events from <%{private}s: %s> [iteration %lu/%lu]"
- "Polling not in progress, nothing to stop"
- "Skipping misconfiguration detection as DOI and main device are not in the same HomeKit group"
- "Skipping misconfiguration detection as DOI and main device are the same"
- "Starting periodic event and device state polling"
- "Starting periodic event and device state polling [iteration %ld]"
- "Stopped periodic event polling"
- "Successfully retrieved %ld active events and device info from device <%{private}s: %s>"
- "Updated primary resident ID for %s to %s, all known primary residents: %s"
- "_numRequestsPerEndpoint"
- "_pollingTimerInterval"
- "com.apple.symptomsd.NDFActorManagerPolling"
- "pollingTimer"
- "polling_discovery_cadence"
- "requests_per_endpoint"

```
