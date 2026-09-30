## securityd

> `/usr/libexec/securityd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__thread_vars`

```diff

-62460.2.3.0.0
-  __TEXT.__text: 0x266324
+62460.40.49.502.1
+  __TEXT.__text: 0x267174
   __TEXT.__auth_stubs: 0x4340
-  __TEXT.__objc_stubs: 0x1d9a0
+  __TEXT.__objc_stubs: 0x1d9e0
   __TEXT.__objc_methlist: 0x15e98
   __TEXT.__const: 0x910
-  __TEXT.__cstring: 0x227a6
-  __TEXT.__objc_methname: 0x2e67f
-  __TEXT.__oslogstring: 0x2feaa
+  __TEXT.__cstring: 0x22bd0
+  __TEXT.__objc_methname: 0x2e65f
+  __TEXT.__oslogstring: 0x2ff02
   __TEXT.__swift5_typeref: 0x372
   __TEXT.__swift5_fieldmd: 0x120
   __TEXT.__objc_classname: 0x2559
-  __TEXT.__objc_methtype: 0xb04a
+  __TEXT.__objc_methtype: 0xb0a4
   __TEXT.__constg_swiftt: 0x274
   __TEXT.__swift5_reflstr: 0xc3
   __TEXT.__swift5_capture: 0x1bc

   __TEXT.__swift_as_entry: 0x40
   __TEXT.__swift_as_ret: 0x3c
   __TEXT.__swift_as_cont: 0x48
-  __TEXT.__gcc_except_tab: 0xa078
-  __TEXT.__dlopen_cstrs: 0xb4
+  __TEXT.__dlopen_cstrs: 0x5a
+  __TEXT.__gcc_except_tab: 0xa0c8
   __TEXT.__ustring: 0x28
-  __TEXT.__unwind_info: 0x7cc0
+  __TEXT.__unwind_info: 0x7cb8
   __TEXT.__eh_frame: 0xa60
-  __DATA_CONST.__const: 0x149c0
-  __DATA_CONST.__cfstring: 0x1c540
+  __DATA_CONST.__const: 0x14a40
+  __DATA_CONST.__cfstring: 0x1c760
   __DATA_CONST.__objc_classlist: 0x910
   __DATA_CONST.__objc_catlist: 0x68
   __DATA_CONST.__objc_protolist: 0x260

   __DATA_CONST.__objc_dictobj: 0x78
   __DATA_CONST.__objc_arrayobj: 0x360
   __DATA_CONST.__auth_got: 0x21b0
-  __DATA_CONST.__got: 0x1530
+  __DATA_CONST.__got: 0x1550
   __DATA_CONST.__auth_ptr: 0x1d8
   __DATA.__objc_const: 0x23cd8
-  __DATA.__objc_selrefs: 0x98a0
+  __DATA.__objc_selrefs: 0x98b8
   __DATA.__objc_ivar: 0x1ae8
   __DATA.__objc_data: 0x5d98
-  __DATA.__data: 0x3150
+  __DATA.__data: 0x3158
   __DATA.__thread_vars: 0xc0
   __DATA.__thread_bss: 0x28
   - /AppleInternal/Library/Frameworks/TapToRadarKit.framework/TapToRadarKit

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 9917
-  Symbols:   1890
-  CStrings:  16411
+  Functions: 9920
+  Symbols:   1894
+  CStrings:  16432
 
Symbols:
+ _OBJC_CLASS_$_MetricSessionInfo
+ _OBJC_CLASS_$_TPMIDStableTrustedDeviceID
+ _kSecItemCountNonSyncableLive
+ _kSecItemCountNonSyncableTombstone
+ _kSecItemCountSyncableLive
+ _kSecItemCountSyncableTombstone
- _OBJC_CLASS_$_TPMIDStableTrustedDeviceIDPair
- _kSecurityRTCEventCategoryAccountDataAccessRecovery
CStrings:
+ " AND agrp IN (?"
+ " GROUP BY agrp"
+ " WHERE agrp IN (?"
+ " WHERE musr = ?"
+ "%@: (%@, %@, %@, %@, %@)"
+ "-[CuttlefishXPCWrapper prepareWithSpecificUser:epoch:machineID:bottleSalt:bottleID:modelID:deviceName:serialNumber:osVersion:stableTrustedDeviceID:flowID:deviceSessionID:policyVersion:policySecrets:syncUserControllableViews:secureElementIdentity:setting:signingPrivKeyPersistentRef:encPrivKeyPersistentRef:reply:]_block_invoke"
+ "-[CuttlefishXPCWrapper setAllowedMachineIDsWithSpecificUser:allowed:userInitiatedRemovals:evictedRemovals:unknownReasonRemovals:honorIDMSListChanges:version:flowID:deviceSessionID:canSendMetrics:altDSID:trustedDeviceHash:deletedDeviceHash:trustedDevicesUpdateTimestamp:idmsStableTrustedDevicesVersion:thisDeviceMachineID:reply:]_block_invoke"
+ "CREATE INDEX IF NOT EXISTS cert_agrp_musr_sync_tomb ON cert(agrp, musr, sync, tomb);"
+ "CREATE INDEX IF NOT EXISTS genp_agrp_musr_sync_tomb ON genp(agrp, musr, sync, tomb);"
+ "CREATE INDEX IF NOT EXISTS inet_agrp_musr_sync_tomb ON inet(agrp, musr, sync, tomb);"
+ "CREATE INDEX IF NOT EXISTS keys_agrp_musr_sync_tomb ON keys(agrp, musr, sync, tomb);"
+ "SELECT agrp,                                  SUM(CASE WHEN sync=0 AND tomb=0 THEN 1 ELSE 0 END) AS nonsync_live,                                  SUM(CASE WHEN sync=0 AND tomb=1 THEN 1 ELSE 0 END) AS nonsync_tomb,                                  SUM(CASE WHEN sync=1 AND tomb=0 THEN 1 ELSE 0 END) AS sync_live,                                  SUM(CASE WHEN sync=1 AND tomb=1 THEN 1 ELSE 0 END) AS sync_tomb                                  FROM %@                                  GROUP BY agrp"
+ "SELECT agrp, SUM(CASE WHEN sync=0 AND tomb=0 THEN 1 ELSE 0 END), SUM(CASE WHEN sync=0 AND tomb=1 THEN 1 ELSE 0 END), SUM(CASE WHEN sync=1 AND tomb=0 THEN 1 ELSE 0 END), SUM(CASE WHEN sync=1 AND tomb=1 THEN 1 ELSE 0 END) FROM %@"
+ "SecServerItemCountAllWithAccessGroups query template: %@"
+ "accessGroups must be a non-empty CFArray, got %@"
+ "afterAuthKitFetch:userInitiatedRemovals:evictedRemovals:unknownReasonRemovals:trustedDeviceHash:deletedDeviceHash:trustedDevicesUpdateTimestamp:accountIsDemo:version:idmsStableTrustedDevicesVersion:"
+ "applicationID"
+ "com.apple.private.security.access-group-item-counts"
+ "initWithMetrics:session:eventName:"
+ "initWithMetrics:session:eventName:canSendMetrics:"
+ "initWithSession:eventName:"
+ "item-counts"
+ "nonsync_live"
+ "nonsync_tomb"
+ "octagon-authkit: unable to fetch this device's machine ID for telemetry: %@"
+ "prepareWithSpecificUser:epoch:machineID:bottleSalt:bottleID:modelID:deviceName:serialNumber:osVersion:stableTrustedDeviceID:flowID:deviceSessionID:policyVersion:policySecrets:syncUserControllableViews:secureElementIdentity:setting:signingPrivKeyPersistentRef:encPrivKeyPersistentRef:reply:"
+ "sec_count_all_with_access_groups_id"
+ "sessionInfoWithAltDSID:"
+ "sessionInfoWithAltDSID:flowID:deviceSessionID:"
+ "setAllowedMachineIDsWithSpecificUser:allowed:userInitiatedRemovals:evictedRemovals:unknownReasonRemovals:honorIDMSListChanges:version:flowID:deviceSessionID:canSendMetrics:altDSID:trustedDeviceHash:deletedDeviceHash:trustedDevicesUpdateTimestamp:idmsStableTrustedDevicesVersion:thisDeviceMachineID:reply:"
+ "sync_live"
+ "sync_tomb"
+ "trusted stable id is missing components for machine %@"
+ "v148@0:8@\"TPSpecificUser\"16@\"NSSet\"24@\"NSSet\"32@\"NSSet\"40@\"NSSet\"48q56@\"NSString\"64@\"NSString\"72@\"NSString\"80B88@\"NSString\"92@\"NSString\"100@\"NSString\"108@\"NSNumber\"116@\"NSString\"124@\"NSString\"132@?<v@?B@\"NSError\">140"
+ "v172@0:8@\"TPSpecificUser\"16Q24@\"NSString\"32@\"NSString\"40@\"NSString\"48@\"NSString\"56@\"NSString\"64@\"NSString\"72@\"NSString\"80@\"TPStableTrustedDeviceID\"88@\"NSString\"96@\"NSString\"104@\"TPPolicyVersion\"112@\"NSDictionary\"120i128@\"TPPBSecureElementIdentity\"132@\"OTAccountSettings\"140@\"NSData\"148@\"NSData\"156@?<v@?@\"NSString\"@\"NSData\"@\"NSData\"@\"NSData\"@\"NSData\"@\"TPSyncingPolicy\"@\"NSError\">164"
+ "v172@0:8@16Q24@32@40@48@56@64@72@80@88@96@104@112@120i128@132@140@148@156@?164"
+ "v32@0:8@\"OTControlArguments\"16@?<v@?@\"NSSet\"@\"NSSet\"@\"NSSet\"@\"NSSet\"@\"NSString\"@\"NSString\"@\"NSString\"@\"NSNumber\"@\"NSString\"@\"OTMetricsSessionData\"q@\"NSError\">24"
+ "v52@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32B40@?<v@?@\"NSSet\"@\"NSSet\"@\"NSSet\"@\"NSSet\"@\"NSString\"@\"NSString\"@\"NSString\"@\"NSNumber\"@\"NSString\"@\"OTMetricsSessionData\"@\"NSError\">44"
+ "v92@0:8@16@24@32@40@48@56@64B72@76@84"
+ "v96@?0@\"NSSet\"8@\"NSSet\"16@\"NSSet\"24@\"NSSet\"32@\"NSString\"40@\"NSString\"48@\"NSString\"56@\"NSNumber\"64@\"NSString\"72@\"OTMetricsSessionData\"80@\"NSError\"88"
+ "zone-deletion"
+ "zone-deletion-operation"
- "%@: (%@, %@, %@)"
- "-[CuttlefishXPCWrapper prepareWithSpecificUser:epoch:machineID:bottleSalt:bottleID:modelID:deviceName:serialNumber:osVersion:stableTrustedDeviceID:policyVersion:policySecrets:syncUserControllableViews:secureElementIdentity:setting:signingPrivKeyPersistentRef:encPrivKeyPersistentRef:reply:]_block_invoke"
- "-[CuttlefishXPCWrapper setAllowedMachineIDsWithSpecificUser:allowedMachineIDs:userInitiatedRemovals:evictedRemovals:unknownReasonRemovals:honorIDMSListChanges:version:flowID:deviceSessionID:canSendMetrics:altDSID:trustedDeviceHash:deletedDeviceHash:trustedDevicesUpdateTimestamp:idmsStableTrustedDevicesVersion:midStableTrustedDeviceIDs:reply:]_block_invoke"
- "MetricsOverrideTestsAreEnabled"
- "SELECT agrp,                                  SUM(1 - tomb) AS count_tomb_0,                                  SUM(tomb) AS count_tomb_1                                  FROM %@                                  GROUP BY agrp"
- "afterAuthKitFetch:userInitiatedRemovals:evictedRemovals:unknownReasonRemovals:trustedDeviceHash:deletedDeviceHash:trustedDevicesUpdateTimestamp:accountIsDemo:version:idmsStableTrustedDevicesVersion:midStableTrustedDeviceIDs:"
- "bool soft_MetricsOverrideTestsAreEnabled(void)"
- "fetched MID/StableID pair is %@"
- "initWithCKKSMetrics:altDSID:eventName:testsAreEnabled:category:sendMetric:"
- "initWithKeychainCircleMetrics:altDSID:flowID:deviceSessionID:eventName:testsAreEnabled:canSendMetrics:category:"
- "prepareWithSpecificUser:epoch:machineID:bottleSalt:bottleID:modelID:deviceName:serialNumber:osVersion:stableTrustedDeviceID:policyVersion:policySecrets:syncUserControllableViews:secureElementIdentity:setting:signingPrivKeyPersistentRef:encPrivKeyPersistentRef:reply:"
- "setAllowedMachineIDsWithSpecificUser:allowedMachineIDs:userInitiatedRemovals:evictedRemovals:unknownReasonRemovals:honorIDMSListChanges:version:flowID:deviceSessionID:canSendMetrics:altDSID:trustedDeviceHash:deletedDeviceHash:trustedDevicesUpdateTimestamp:idmsStableTrustedDevicesVersion:midStableTrustedDeviceIDs:reply:"
- "tomb_0"
- "tomb_1"
- "trusted stable id in fetch TDL is missing components for machine %@"
- "v100@0:8@16@24@32@40@48@56@64B72@76@84@92"
- "v104@?0@\"NSSet\"8@\"NSSet\"16@\"NSSet\"24@\"NSSet\"32@\"NSString\"40@\"NSString\"48@\"NSString\"56@\"NSNumber\"64@\"NSString\"72@\"OTMetricsSessionData\"80@\"NSSet\"88@\"NSError\"96"
- "v148@0:8@\"TPSpecificUser\"16@\"NSSet\"24@\"NSSet\"32@\"NSSet\"40@\"NSSet\"48q56@\"NSString\"64@\"NSString\"72@\"NSString\"80B88@\"NSString\"92@\"NSString\"100@\"NSString\"108@\"NSNumber\"116@\"NSString\"124@\"NSSet\"132@?<v@?B@\"NSError\">140"
- "v156@0:8@\"TPSpecificUser\"16Q24@\"NSString\"32@\"NSString\"40@\"NSString\"48@\"NSString\"56@\"NSString\"64@\"NSString\"72@\"NSString\"80@\"TPStableTrustedDeviceID\"88@\"TPPolicyVersion\"96@\"NSDictionary\"104i112@\"TPPBSecureElementIdentity\"116@\"OTAccountSettings\"124@\"NSData\"132@\"NSData\"140@?<v@?@\"NSString\"@\"NSData\"@\"NSData\"@\"NSData\"@\"NSData\"@\"TPSyncingPolicy\"@\"NSError\">148"
- "v32@0:8@\"OTControlArguments\"16@?<v@?@\"NSSet\"@\"NSSet\"@\"NSSet\"@\"NSSet\"@\"NSString\"@\"NSString\"@\"NSString\"@\"NSNumber\"@\"NSString\"@\"OTMetricsSessionData\"@\"NSSet\"q@\"NSError\">24"
- "v52@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32B40@?<v@?@\"NSSet\"@\"NSSet\"@\"NSSet\"@\"NSSet\"@\"NSString\"@\"NSString\"@\"NSString\"@\"NSNumber\"@\"NSString\"@\"OTMetricsSessionData\"@\"NSSet\"@\"NSError\">44"
```
