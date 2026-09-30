## identityservicesd

> `/System/Library/PrivateFrameworks/IDS.framework/identityservicesd.app/identityservicesd`

```diff

-1856.100.1.0.0
-  __TEXT.__text: 0x7094e0
-  __TEXT.__auth_stubs: 0x54a0
-  __TEXT.__objc_stubs: 0x44580
-  __TEXT.__objc_methlist: 0x23dcc
-  __TEXT.__const: 0x41fb0
-  __TEXT.__gcc_except_tab: 0x292ec
-  __TEXT.__objc_methname: 0x6f48a
-  __TEXT.__cstring: 0x5585f
-  __TEXT.__oslogstring: 0x7a684
+1857.100.1.0.0
+  __TEXT.__text: 0x70f4cc
+  __TEXT.__auth_stubs: 0x54c0
+  __TEXT.__objc_stubs: 0x44600
+  __TEXT.__objc_methlist: 0x23e0c
+  __TEXT.__const: 0x42380
+  __TEXT.__gcc_except_tab: 0x2938c
+  __TEXT.__objc_methname: 0x6f625
+  __TEXT.__cstring: 0x55bcf
+  __TEXT.__oslogstring: 0x7a81a
   __TEXT.__objc_classname: 0x42d5
   __TEXT.__objc_methtype: 0x117fd
   __TEXT.__ustring: 0x4ca
   __TEXT.__dlopen_cstrs: 0xea
-  __TEXT.__swift5_typeref: 0x358c
-  __TEXT.__swift5_capture: 0x6f4
-  __TEXT.__constg_swiftt: 0x2b74
-  __TEXT.__swift5_reflstr: 0x1d88
-  __TEXT.__swift5_fieldmd: 0x1fec
+  __TEXT.__swift5_typeref: 0x3682
+  __TEXT.__swift5_capture: 0x72c
+  __TEXT.__constg_swiftt: 0x2c48
+  __TEXT.__swift5_reflstr: 0x1eee
+  __TEXT.__swift5_fieldmd: 0x20c0
   __TEXT.__swift5_builtin: 0x8c
   __TEXT.__swift5_protos: 0x54
-  __TEXT.__swift5_proto: 0x340
-  __TEXT.__swift5_types: 0x214
-  __TEXT.__swift5_assocty: 0x1c8
+  __TEXT.__swift5_proto: 0x354
+  __TEXT.__swift5_types: 0x21c
+  __TEXT.__swift5_assocty: 0x1e0
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0xf5b0
-  __TEXT.__eh_frame: 0x49c4
-  __DATA_CONST.__auth_got: 0x2a60
-  __DATA_CONST.__got: 0x32d8
-  __DATA_CONST.__auth_ptr: 0x618
-  __DATA_CONST.__const: 0x1b6e8
-  __DATA_CONST.__cfstring: 0x33560
-  __DATA_CONST.__objc_classlist: 0xe68
+  __TEXT.__unwind_info: 0xf6f0
+  __TEXT.__eh_frame: 0x4bb4
+  __DATA_CONST.__auth_got: 0x2a70
+  __DATA_CONST.__got: 0x3310
+  __DATA_CONST.__auth_ptr: 0x628
+  __DATA_CONST.__const: 0x1b7a8
+  __DATA_CONST.__cfstring: 0x33580
+  __DATA_CONST.__objc_classlist: 0xe70
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0x740
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x108
   __DATA_CONST.__objc_superrefs: 0xb40
-  __DATA_CONST.__objc_intobj: 0x1920
+  __DATA_CONST.__objc_intobj: 0x1968
   __DATA_CONST.__objc_arraydata: 0x5d8
   __DATA_CONST.__objc_arrayobj: 0x348
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__objc_dictobj: 0x50
-  __DATA.__objc_const: 0x482d8
-  __DATA.__objc_selrefs: 0x145f8
+  __DATA.__objc_const: 0x48508
+  __DATA.__objc_selrefs: 0x14670
   __DATA.__objc_ivar: 0x3110
-  __DATA.__objc_data: 0xb3b8
-  __DATA.__data: 0x9c08
-  __DATA.__bss: 0x8ab8
-  __DATA.__common: 0x508
+  __DATA.__objc_data: 0xb480
+  __DATA.__data: 0x9ea8
+  __DATA.__bss: 0x8db0
+  __DATA.__common: 0x518
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 19908
-  Symbols:   2613
-  CStrings:  33765
+  Functions: 20025
+  Symbols:   2616
+  CStrings:  33814
 
Symbols:
+ _IDSOffGridStatusPayloadStatusKey
+ _IDSOffGridStatusPayloadStatusTokenKey
+ _kIDSQualifiedContactsMetric
CStrings:
+ "03:51:15"
+ "Aug  8 2024"
+ "Canceling cleanup timer."
+ "Capturing metric - current IDSQualifiedContactsMetric: %!@(MISSING) differs from last metric: %!@(MISSING)"
+ "Cleanup timer fired."
+ "Closing our SD database."
+ "Container already loaded."
+ "Error fetching IDSQualifiedContactsCount: %!@(MISSING)"
+ "Error updating IDSQualifiedContactsCount: %!@(MISSING)"
+ "SD database is already closed."
+ "Scheduling a timer for provisioning payloads in: %!f(MISSING)sec shouldForce %!@(MISSING)"
+ "Starting SD database cleanup timer."
+ "_TtCOO17identityservicesd26SDPersistenceMigrationPlan21SDPersistenceSchemaV125IDSQualifiedContactsCount"
+ "_emergencyHandlesCount"
+ "_familyHandlesCount"
+ "_handlesCount"
+ "_offGridPayloadProvisioningTimerFiredShouldForce:"
+ "_primaryHandlesCount"
+ "_provisionOnInviteDebounceTimeInterval"
+ "_qualifiedEmergencyHandles"
+ "_qualifiedEmergencyHandlesIML"
+ "_qualifiedHandlesCount"
+ "_qualifiedHandlesIML"
+ "_qualifiedPrimaryHandles"
+ "_qualifiedPrimaryHandlesIML"
+ "_scheduleOffGridPayloadProvisioningTimerWithInterval:shouldForce:"
+ "_shouldIncludeDefaultDeviceAsDestinationForMessageWithParams:service:"
+ "cleanupTimer"
+ "cleanupTimerFired"
+ "emergencyHandlesCount"
+ "emergencyHandlesCount"
+ "familyHandlesCount"
+ "familyHandlesCount"
+ "handlesCount"
+ "lastQualifiedContactsMetric"
+ "pairedDeviceSupportsSendLaterMessages"
+ "primaryHandlesCount"
+ "primaryHandlesCount"
+ "qualifiedEmergencyHandles"
+ "qualifiedEmergencyHandles"
+ "qualifiedEmergencyHandlesIML"
+ "qualifiedEmergencyHandlesIML"
+ "qualifiedHandlesCount"
+ "qualifiedHandlesCount"
+ "qualifiedHandlesIML"
+ "qualifiedHandlesIML"
+ "qualifiedPrimaryHandles"
+ "qualifiedPrimaryHandles"
+ "qualifiedPrimaryHandlesIML"
+ "qualifiedPrimaryHandlesIML"
+ "shared-channels-cp-provision-on-invitation-debounce-delay-time-interval"
+ "shouldIncludeDefaultDeviceAsDestinationForMessageWithParams:"
+ "updateQualifiedContactsCountWithMetric:"
- "00:50:27"
- "Jul 27 2024"
- "Scheduling a timer for provisioning payloads in: %!f(MISSING)"
- "_offGridPayloadProvisioningTimerFired"
- "_scheduleOffGridPayloadProvisioningTimerWithInterval:"
- "_shouldIncludeDefaultDeviceAsDestinationForMessageForFromID:service:"
- "shouldIncludeDefaultDeviceAsDestinationForMessageForFromID:"

```
