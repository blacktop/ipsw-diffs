## amsaccountsd

> `/System/Library/PrivateFrameworks/AppleMediaServices.framework/amsaccountsd`

```diff

-8.1.20.2.1
-  __TEXT.__text: 0xc4248
-  __TEXT.__auth_stubs: 0x2080
-  __TEXT.__objc_stubs: 0x93e0
-  __TEXT.__objc_methlist: 0x34f0
+8.2.10.0.0
+  __TEXT.__text: 0xc4c6c
+  __TEXT.__auth_stubs: 0x20c0
+  __TEXT.__objc_stubs: 0x94a0
+  __TEXT.__objc_methlist: 0x3568
   __TEXT.__const: 0x60d0
-  __TEXT.__objc_classname: 0xd6e
-  __TEXT.__objc_methname: 0xd3e3
-  __TEXT.__oslogstring: 0x99f2
-  __TEXT.__objc_methtype: 0x3b92
-  __TEXT.__cstring: 0x6ec8
-  __TEXT.__gcc_except_tab: 0xdd8
+  __TEXT.__objc_classname: 0xda0
+  __TEXT.__objc_methname: 0xdf25
+  __TEXT.__oslogstring: 0x9af2
+  __TEXT.__objc_methtype: 0x3e5c
+  __TEXT.__cstring: 0x6f08
+  __TEXT.__gcc_except_tab: 0xddc
   __TEXT.__dlopen_cstrs: 0x2ed
   __TEXT.__constg_swiftt: 0x104c
   __TEXT.__swift5_typeref: 0x132f

   __TEXT.__swift5_types: 0x148
   __TEXT.__swift5_protos: 0x48
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x2c40
+  __TEXT.__unwind_info: 0x2c70
   __TEXT.__eh_frame: 0x3618
-  __DATA_CONST.__auth_got: 0x1050
-  __DATA_CONST.__got: 0x990
+  __DATA_CONST.__auth_got: 0x1070
+  __DATA_CONST.__got: 0x9a0
   __DATA_CONST.__auth_ptr: 0x4b0
-  __DATA_CONST.__const: 0x5a10
+  __DATA_CONST.__const: 0x5a50
   __DATA_CONST.__cfstring: 0x3e80
   __DATA_CONST.__objc_classlist: 0x298
   __DATA_CONST.__objc_catlist: 0x90
-  __DATA_CONST.__objc_protolist: 0x240
+  __DATA_CONST.__objc_protolist: 0x250
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x58
   __DATA_CONST.__objc_superrefs: 0x190
   __DATA_CONST.__objc_intobj: 0x90
-  __DATA.__objc_const: 0xbad0
-  __DATA.__objc_selrefs: 0x2da0
-  __DATA.__objc_ivar: 0x334
+  __DATA.__objc_const: 0xc378
+  __DATA.__objc_selrefs: 0x2dd0
+  __DATA.__objc_ivar: 0x338
   __DATA.__objc_data: 0x1a90
-  __DATA.__data: 0x34f8
+  __DATA.__data: 0x35b8
   __DATA.__bss: 0x7108
   __DATA.__common: 0xa0
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 3949
-  Symbols:   942
-  CStrings:  3989
+  Functions: 3964
+  Symbols:   947
+  CStrings:  4086
 
Symbols:
+ __dispatch_source_type_signal
+ _dispatch_resume
+ _dispatch_source_cancel
+ _dispatch_source_create
+ _dispatch_source_set_event_handler
CStrings:
+ "\x01\x11"
+ "%!{(MISSING)public}@: Flush all keep alive transaction. remaining transactions = %!{(MISSING)public}@"
+ "%!{(MISSING)public}@: Multi-User is shutting down"
+ "%!{(MISSING)public}@: Received SIGTERM..."
+ "%!{(MISSING)public}@: [%!{(MISSING)public}@] Preferred media user for current accessory updated. Accessory = %!{(MISSING)public}@"
+ "@\"NSObject<OS_dispatch_source>\""
+ "HMAccessoryDelegate"
+ "HMAccessoryDelegatePrivate"
+ "T@\"AMSDHomeManager\",&,N,V_homeManager"
+ "_configurePreferredMediaUser:"
+ "_setupSignalHandlers"
+ "_sigTermSource"
+ "_tearDownMultiUser"
+ "accessory:didAddControlTarget:"
+ "accessory:didAddProfile:"
+ "accessory:didAddSymptomsHandler:"
+ "accessory:didRemoveControlTarget:"
+ "accessory:didRemoveProfile:"
+ "accessory:didUpdateApplicationDataForService:"
+ "accessory:didUpdateAssociatedServiceTypeForService:"
+ "accessory:didUpdateBulletinBoardNotificationForService:"
+ "accessory:didUpdateBundleID:"
+ "accessory:didUpdateConfigurationStateForService:"
+ "accessory:didUpdateConfiguredNameForService:"
+ "accessory:didUpdateDefaultNameForService:"
+ "accessory:didUpdateDevice:"
+ "accessory:didUpdateFirmwareUpdateAvailable:"
+ "accessory:didUpdateFirmwareVersion:"
+ "accessory:didUpdateHasAuthorizationDataForCharacteristic:"
+ "accessory:didUpdateLastKnownOperatingStateResponseForService:"
+ "accessory:didUpdateLastKnownSleepDiscoveryModeForService:"
+ "accessory:didUpdateLoggedInAccount:"
+ "accessory:didUpdateNameForService:"
+ "accessory:didUpdatePairingIdentity:"
+ "accessory:didUpdateServiceSubtypeForService:"
+ "accessory:didUpdateSettings:"
+ "accessory:didUpdateSoftwareVersion:"
+ "accessory:didUpdateStoreID:"
+ "accessory:didUpdateSupportsUWBUnlock:"
+ "accessory:didUpdateSupportsWalletKey:"
+ "accessory:didUpdateWifiNetworkInfo:"
+ "accessory:service:didUpdateValueForCharacteristic:"
+ "accessoryDidRemoveSymptomsHandler:"
+ "accessoryDidSetHasOnboardedForNaturalLighting:"
+ "accessoryDidUpdateAdditionalSetupRequired:"
+ "accessoryDidUpdateApplicationData:"
+ "accessoryDidUpdateAudioDestination:"
+ "accessoryDidUpdateAudioDestinationController:"
+ "accessoryDidUpdateAudioReturnChannelSupport:"
+ "accessoryDidUpdateCalibrationStatus:"
+ "accessoryDidUpdateControllable:"
+ "accessoryDidUpdateDiagnosticsTransferSupport:"
+ "accessoryDidUpdateHomeLevelLocationServiceSettingSupport:"
+ "accessoryDidUpdateMultiUserSupport:"
+ "accessoryDidUpdateName:"
+ "accessoryDidUpdatePairingIdentity:"
+ "accessoryDidUpdatePendingConfigurationIdentifier:"
+ "accessoryDidUpdatePreferredMediaUser:"
+ "accessoryDidUpdateReachability:"
+ "accessoryDidUpdateReachableTransports:"
+ "accessoryDidUpdateServices:"
+ "accessoryDidUpdateSupportsAnnounce:"
+ "accessoryDidUpdateSupportsAudioAnalysis:"
+ "accessoryDidUpdateSupportsCompanionInitiatedObliterate:"
+ "accessoryDidUpdateSupportsCompanionInitiatedRestart:"
+ "accessoryDidUpdateSupportsDoorbellChime:"
+ "accessoryDidUpdateSupportsDropIn:"
+ "accessoryDidUpdateSupportsJustSiri:"
+ "accessoryDidUpdateSupportsMediaActions:"
+ "accessoryDidUpdateSupportsMediaContentProfile:"
+ "accessoryDidUpdateSupportsMusicAlarm:"
+ "accessoryDidUpdateSupportsPreferredMediaUser:"
+ "accessoryDidUpdateSupportsRMVonAppleTV:"
+ "accessoryDidUpdateSupportsThirdPartyMusic:"
+ "accessoryDidUpdateSupportsUserMediaSettings:"
+ "accessoryDidUpdateTargetControlSupport:"
+ "accountIsEligibleForPushNotifications:accountStore:"
+ "flushAllKeepAliveTransactions"
+ "multiUserTokenFromCloudKitForAccount:homeUserIdentifier:qualityOfService:completion:"
+ "multiUserTokenFromKeychainForAccount:completion:"
+ "resetReleaseKeepAliveTransactionTimeDelayValue"
+ "storeMultiUserTokenInKeychainForAccount:token:completion:"
+ "teardownMultiUser"
+ "v24@0:8@\"HMAccessory\"16"
+ "v28@0:8@\"HMAccessory\"16B24"
+ "v32@0:8@\"HMAccessory\"16@\"ACAccount\"24"
+ "v32@0:8@\"HMAccessory\"16@\"HMAccessory\"24"
+ "v32@0:8@\"HMAccessory\"16@\"HMAccessoryProfile\"24"
+ "v32@0:8@\"HMAccessory\"16@\"HMAccessorySettings\"24"
+ "v32@0:8@\"HMAccessory\"16@\"HMCharacteristic\"24"
+ "v32@0:8@\"HMAccessory\"16@\"HMDevice\"24"
+ "v32@0:8@\"HMAccessory\"16@\"HMFPairingIdentity\"24"
+ "v32@0:8@\"HMAccessory\"16@\"HMFSoftwareVersion\"24"
+ "v32@0:8@\"HMAccessory\"16@\"HMFWiFiNetworkInfo\"24"
+ "v32@0:8@\"HMAccessory\"16@\"HMService\"24"
+ "v32@0:8@\"HMAccessory\"16@\"HMSymptomsHandler\"24"
+ "v32@0:8@\"HMAccessory\"16@\"NSString\"24"
+ "v32@?0@\"NSString\"8@\"NSObject<OS_os_transaction>\"16^B24"
+ "v40@0:8@\"ACAccount\"16@\"NSString\"24@?<v@?B@\"NSError\">32"
+ "v40@0:8@\"HMAccessory\"16@\"HMService\"24@\"HMCharacteristic\"32"
- "T@\"AMSDHomeManager\",R,N,V_homeManager"
- "_accountIsEligibleForPushNotifications:"
- "ams_isBackingAccountForActiveiCloudAccount"

```
