## audioaccessoryd

> `/usr/libexec/audioaccessoryd`

```diff

-34.29.1.2.0
-  __TEXT.__text: 0x23dfb8
-  __TEXT.__auth_stubs: 0x2c20
-  __TEXT.__objc_stubs: 0x1d580
-  __TEXT.__objc_methlist: 0xda34
+35.9.1.1.0
+  __TEXT.__text: 0x23f180
+  __TEXT.__auth_stubs: 0x2bc0
+  __TEXT.__objc_stubs: 0x1d640
+  __TEXT.__objc_methlist: 0xda8c
   __TEXT.__const: 0x4210
-  __TEXT.__gcc_except_tab: 0x5b70
-  __TEXT.__cstring: 0x530d3
+  __TEXT.__gcc_except_tab: 0x5bb0
+  __TEXT.__cstring: 0x53823
   __TEXT.__objc_classname: 0xff3
-  __TEXT.__objc_methname: 0x2a385
+  __TEXT.__objc_methname: 0x2a455
   __TEXT.__objc_methtype: 0x3e59
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__oslogstring: 0x919a
+  __TEXT.__oslogstring: 0x915a
   __TEXT.__ustring: 0x10
-  __TEXT.__constg_swiftt: 0x1adc
+  __TEXT.__constg_swiftt: 0x1ad4
   __TEXT.__swift5_typeref: 0x189e
   __TEXT.__swift5_builtin: 0xa0
   __TEXT.__swift5_reflstr: 0x190b

   __TEXT.__swift5_capture: 0x1a28
   __TEXT.__swift5_protos: 0x14
   __TEXT.__swift5_mpenum: 0x14
-  __TEXT.__unwind_info: 0x6c60
+  __TEXT.__unwind_info: 0x6cb0
   __TEXT.__eh_frame: 0x1ca0
-  __DATA_CONST.__auth_got: 0x1620
-  __DATA_CONST.__got: 0xd68
+  __DATA_CONST.__auth_got: 0x15f0
+  __DATA_CONST.__got: 0xd50
   __DATA_CONST.__auth_ptr: 0x580
   __DATA_CONST.__const: 0xb9a0
   __DATA_CONST.__cfstring: 0xb320

   __DATA_CONST.__objc_dictobj: 0x500
   __DATA_CONST.__objc_arrayobj: 0x48
   __DATA_CONST.__objc_doubleobj: 0x40
-  __DATA.__objc_const: 0x1d578
-  __DATA.__objc_selrefs: 0x8af0
-  __DATA.__objc_ivar: 0x1730
+  __DATA.__objc_const: 0x1d5b8
+  __DATA.__objc_selrefs: 0x8b28
+  __DATA.__objc_ivar: 0x1738
   __DATA.__objc_data: 0x2fd0
-  __DATA.__data: 0x4c90
+  __DATA.__data: 0x4cc0
   __DATA.__bss: 0x6b70
   __DATA.__common: 0x3a0
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: D580D005-0A76-3E52-83EB-7368147BA40E
-  Functions: 11017
-  Symbols:   1284
-  CStrings:  17050
+  UUID: 7B2EA62A-6EB4-3E81-AE10-1D21E9A90F78
+  Functions: 11045
+  Symbols:   1275
+  CStrings:  17085
 
Symbols:
- _$s13OSEligibility0A6AnswerO2eeoiySbAC_ACtFZ
- _$s13OSEligibility0A6AnswerO8eligibleyA2CmFWC
- _$s13OSEligibility0A6AnswerOMa
- _$s13OSEligibility0A6DomainO7thoriumyA2CmFWC
- _$s13OSEligibility0A6DomainOMa
- _$s13OSEligibility0A6ResultV6answerAA0A6AnswerOvg
- _$s13OSEligibility0A6ResultV6result3forAcA0A6DomainO_tKFZ
- _$s13OSEligibility0A6ResultVMa
- _kTCCServiceAccessoryWiFiNetworkSharing
CStrings:
+ "### OSEligibility check failed for bundleID '%@': %{error}"
+ "### OSEligibility check failed: Missing access info for device: %@"
+ "-[SR3PRoutingDaemon _checkThoriumEligibility:]"
+ "-[SR3PRoutingDaemon _checkThoriumEligibility:]_block_invoke"
+ "-[SR3PRoutingDaemon _getDeviceType:]"
+ "-[SR3PRoutingDaemon _pairedDiscoveryEnsureStarted]"
+ "-[SR3PRoutingDaemon _pairedDiscoveryEnsureStarted]_block_invoke"
+ "-[SR3PRoutingDaemon _pairedDiscoveryEnsureStarted]_block_invoke_2"
+ "-[SR3PRoutingDaemon _pairedDiscoveryEnsureStarted]_block_invoke_3"
+ "-[SR3PRoutingDaemon _registerDADevicesAsHeadphones]"
+ "-[SR3PRoutingDaemon _startScanningIfNeeded]"
+ "-[SR3PRoutingDaemon _updateHeadphoneFromCBDevice:]"
+ "-[SR3PRoutingDaemon _updateHeadphoneFromDAAuthorizationChange]"
+ "BtAddressFromAAKDeviceInfo: _prefASKOverwrite to %@"
+ "BtAddressFromBtIdentifier: Device not found in paired devices for identifier: %@, checking connected devices"
+ "BtAddressFromBtIdentifier: Got BT address from connected CBDevice: %@"
+ "BtAddressFromBtIdentifier: Got BT address from paired devices: %@"
+ "CheckThoriumEligibility: Skipping bundleID '%@', state: %ld"
+ "Failed to get bundle ID from LSBundleRecord: %s"
+ "GetDeviceType: No matching device found for %@, returning CBDeviceTypeGeneric"
+ "GetDeviceType: btAddress is nil, returning CBDeviceTypeGeneric"
+ "HandleAudioSourceDevicesUpdate: Invalid secondary device address"
+ "HeadphoneFeatureQueryWithBtAddress: DADevice not found for btAddress %@"
+ "Invalid secondary device address"
+ "PrefMockAccessory: %s -> %s"
+ "RegisterDADevicesAsHeadphones: Registering %lu DA device(s) as headphones"
+ "RegisterDADevicesAsHeadphones: Registering device %@ with BT address %@"
+ "RegisterDADevicesAsHeadphones: Skipping device %@ - could not resolve BT address from identifier %@"
+ "RegisterDADevicesAsHeadphones: Skipping device %@ - not authorized with target service"
+ "RegisterDADevicesAsHeadphones: _prefASKOverwrite %@ btAddress %@"
+ "RegisterHeadphoneWithCompletionHandler: _prefASKOverwrite %@ btAddress %@"
+ "SR3P Paired Discovery activate failed: %{error}\n"
+ "SR3P Paired Discovery activated with %lu devices"
+ "SR3P Paired Discovery started."
+ "SR3P Pairing found device %@"
+ "SR3P Pairing lost device %@"
+ "SR3PMockAccessory"
+ "StartScanningIfNeeded: Found connected headphone %@, starting scan"
+ "StartScanningIfNeeded: No connected headphones found, skipping scan"
+ "Thorium eligible for bundleID '%@'"
+ "Thorium not eligible for bundleID '%@'"
+ "UpdateHeadphoneDeviceInfo: No bluetoothIdentifier in headphone"
+ "UpdateHeadphoneDeviceInfo: No headphone provided"
+ "_checkThoriumEligibility:"
+ "_getDeviceType:"
+ "_pairedDiscoveryEnsureStarted"
+ "_pairedDiscoveryEnsureStopped"
+ "_prefMockAccessory"
+ "_registerDADevicesAsHeadphones"
+ "_startScanningIfNeeded"
+ "_submitRegistrationMetric:"
+ "_updateHeadphoneFromCBDevice:"
+ "_updateHeadphoneFromDAAuthorizationChange"
+ "capability"
+ "com.apple.SmartRouting.3pDeviceRegistration"
+ "connectedCBDeviceUpdate: DADevice not found for identifier %@"
+ "initWithDomain:bundleID:persona:error:"
+ "📋 Bundle ID from LSBundleRecord: %s"
+ "📋 Bundle ID from application-identifier: %s"
- "### OSEligibility check failed: %{error}"
- "-[BTServicesDaemon _audioQualityShowBanner:title:deviceAddressString:messageKey:messageArgs:timeoutSeconds:]_block_invoke"
- "-[BTServicesDaemon openRadarforAudioQuality]"
- "-[SR3PRoutingDaemon _checkHeadphoneAuthorization]"
- "-[SR3PRoutingDaemon _checkThoriumEligibility]"
- "1551854"
- "815886"
- "Bluetooth Audio Quality Feedback"
- "BtAddressFromBtIdentifier: No connected CBDevice found for identifier: %@"
- "Client connection rejected - not EU region"
- "CoreBluetooth - HFP Audio | iOS"
- "Failed to get bundle ID from LSBundleRecord %s"
- "Keywords"
- "OSEligibility check failed: %s"
- "Performance"
- "Retrieved bundle ID from LSBundleRecord: %s"
- "_checkHeadphoneAuthorization"
- "_checkThoriumEligibility"
- "audioQuality - File Radar"
- "audioQuality banner timeout"
- "audioQuality user click, openradar"
- "audioQuality user dismiss"
- "audioQuality: banner action: %s, %{error}"
- "audioQuality: banner error for device %@"
- "initWithDomain:error:"

```
