## SymptomNetworkDiagnosticsCore

> `/System/Library/PrivateFrameworks/SymptomNetworkDiagnosticsCore.framework/SymptomNetworkDiagnosticsCore`

```diff

-2153.0.0.0.0
-  __TEXT.__text: 0x8766c
+2158.40.3.0.0
+  __TEXT.__text: 0x81de4
   __TEXT.__auth_stubs: 0x1a00
   __TEXT.__objc_methlist: 0x190
-  __TEXT.__const: 0x3692
-  __TEXT.__swift5_typeref: 0xf4e
-  __TEXT.__cstring: 0x1804
-  __TEXT.__oslogstring: 0x3f26
-  __TEXT.__constg_swiftt: 0x1218
-  __TEXT.__swift5_reflstr: 0xd33
-  __TEXT.__swift5_fieldmd: 0xda4
+  __TEXT.__const: 0x3602
+  __TEXT.__swift5_typeref: 0xf24
+  __TEXT.__cstring: 0x1744
+  __TEXT.__oslogstring: 0x3c66
+  __TEXT.__constg_swiftt: 0x1188
+  __TEXT.__swift5_reflstr: 0xcd5
+  __TEXT.__swift5_fieldmd: 0xd68
   __TEXT.__swift5_types: 0xec
-  __TEXT.__swift5_capture: 0x5f8
+  __TEXT.__swift5_capture: 0x590
   __TEXT.__swift5_proto: 0x2b8
-  __TEXT.__swift_as_entry: 0x1c8
-  __TEXT.__swift_as_ret: 0x194
+  __TEXT.__swift_as_entry: 0x1b0
+  __TEXT.__swift_as_ret: 0x178
   __TEXT.__swift5_assocty: 0x80
   __TEXT.__swift5_acfuncs: 0x28
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x1c68
-  __TEXT.__eh_frame: 0x4050
+  __TEXT.__unwind_info: 0x1b80
+  __TEXT.__eh_frame: 0x3dc0
   __TEXT.__objc_classname: 0x52
   __TEXT.__objc_methname: 0x7cd
   __TEXT.__objc_methtype: 0xad

   __DATA_CONST.__objc_selrefs: 0x2e8
   __DATA_CONST.__objc_protorefs: 0x38
   __AUTH_CONST.__auth_got: 0xd00
-  __AUTH_CONST.__const: 0x2178
-  __AUTH_CONST.__objc_const: 0x1c10
+  __AUTH_CONST.__const: 0x2060
+  __AUTH_CONST.__objc_const: 0x1b40
   __AUTH.__data: 0x100
-  __DATA.__data: 0x640
+  __DATA.__data: 0x638
   __DATA.__bss: 0x51e0
   __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0x320
-  __DATA_DIRTY.__data: 0x1998
+  __DATA_DIRTY.__data: 0x18e8
   __DATA_DIRTY.__bss: 0xc28
-  __DATA_DIRTY.__common: 0x290
+  __DATA_DIRTY.__common: 0x280
   - /System/Library/Frameworks/CoreData.framework/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: A878C1C2-7BE8-36A1-A541-C955F29C970C
-  Functions: 2067
-  Symbols:   766
-  CStrings:  577
+  UUID: E3881E2D-53AE-3FD8-8313-1AA815BB3487
+  Functions: 2014
+  Symbols:   756
+  CStrings:  560
 
Symbols:
+ _block_copy_helper.5
+ _block_descriptor.7
+ _block_destroy_helper.6
- _block_copy_helper.7
- _block_descriptor.9
- _block_destroy_helper.8
- _symbolic _____SgXw 29SymptomNetworkDiagnosticsCore25NDFDeviceDiscoveryManagerC
- _symbolic _____SgXwz_Xx 29SymptomNetworkDiagnosticsCore25NDFDeviceDiscoveryManagerC
- _symbolic _____ySay_____GG 29SymptomNetworkDiagnosticsCore16NDFActorResponseV AA8NDFEventV
CStrings:
+ " \t\t browse duration: %ss, discover device type: %hhd"
+ "Error during subscription discovery+polling: %@"
+ "Failed to create subscription timer for discovery+polling"
+ "No endpoints discovered during subscription discovery"
+ "No more active clients, stopping polling"
+ "Starting subscription discovery+polling for device state and events [iteration %ld]"
+ "Starting subscription discovery+polling for device state and events with interval of %fs"
+ "Stopped subscription discovery+polling"
- " \t\t browse duration: %ss, discovery cadence: every %ss, discover device type: %hhd"
- "About to retrieve active events from actor at %s"
- "About to start periodic device discovery"
- "Device discovery is already inactive"
- "Error during periodic discovery+polling: %@"
- "Failed to create periodic timer for discovery+polling"
- "Failed to perform delegated discovery: %@"
- "Failed to retrieve active events from actor at %s: %@"
- "No discovered actors to poll events from"
- "No endpoints discovered during periodic discovery"
- "No more active clients, stopping periodic polling"
- "Performing device discovery [iteration %ld]"
- "Periodic device discovery is already active"
- "Polling all discovered actors for their active events"
- "Retrieved %ld active events from actor at %s: %s"
- "Started periodic device discovery [cadence: %f seconds]"
- "Starting periodic discovery+polling for device state and events [iteration %ld]"
- "Starting periodic discovery+polling for device state and events with interval of %fs"
- "Stopped periodic device discovery [cadence: %f seconds]"
- "Stopped periodic discovery+polling"
- "_discoveryCadence"
- "com.apple.symptomsd.discoveryTimer.queue"
- "discoveryCadence"
- "discovery_cadence"
- "isActive"

```
