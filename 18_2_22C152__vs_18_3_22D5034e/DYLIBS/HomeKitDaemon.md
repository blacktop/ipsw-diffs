## HomeKitDaemon

> `/System/Library/PrivateFrameworks/HomeKitDaemon.framework/HomeKitDaemon`

```diff

-1241.3.7.0.0
-  __TEXT.__text: 0xdad15c
-  __TEXT.__auth_stubs: 0x58f0
-  __TEXT.__objc_methlist: 0x7b120
-  __TEXT.__cstring: 0x68fbb
-  __TEXT.__swift5_typeref: 0x48f8
+1241.4.10.0.0
+  __TEXT.__text: 0xdb9124
+  __TEXT.__auth_stubs: 0x5900
+  __TEXT.__objc_methlist: 0x7b238
+  __TEXT.__cstring: 0x690c3
+  __TEXT.__swift5_typeref: 0x49dc
   __TEXT.__const: 0x19954
   __TEXT.__constg_swiftt: 0x4830
   __TEXT.__swift5_builtin: 0x2a8
   __TEXT.__swift5_reflstr: 0x3249
-  __TEXT.__swift5_fieldmd: 0x382c
+  __TEXT.__swift5_fieldmd: 0x3820
   __TEXT.__swift5_assocty: 0x650
   __TEXT.__swift5_proto: 0x86c
   __TEXT.__swift5_types: 0x3c4
-  __TEXT.__swift5_capture: 0x184c
+  __TEXT.__swift5_capture: 0x18ec
   __TEXT.__swift5_protos: 0xe0
-  __TEXT.__oslogstring: 0x125b38
+  __TEXT.__oslogstring: 0x126502
   __TEXT.__swift5_mpenum: 0xb0
-  __TEXT.__gcc_except_tab: 0x2a164
+  __TEXT.__gcc_except_tab: 0x2a128
   __TEXT.__dlopen_cstrs: 0x130
   __TEXT.__ustring: 0x1e
-  __TEXT.__unwind_info: 0x2a530
-  __TEXT.__eh_frame: 0x12d60
-  __TEXT.__objc_classname: 0x18976
-  __TEXT.__objc_methname: 0x147668
-  __TEXT.__objc_methtype: 0x2a260
-  __TEXT.__objc_stubs: 0xba120
-  __DATA_CONST.__got: 0x6880
-  __DATA_CONST.__const: 0x1b750
+  __TEXT.__unwind_info: 0x2a5e8
+  __TEXT.__eh_frame: 0x12e08
+  __TEXT.__objc_classname: 0x1897c
+  __TEXT.__objc_methname: 0x147837
+  __TEXT.__objc_methtype: 0x2a25d
+  __TEXT.__objc_stubs: 0xba100
+  __DATA_CONST.__got: 0x68a0
+  __DATA_CONST.__const: 0x1b7c8
   __DATA_CONST.__objc_classlist: 0x4588
   __DATA_CONST.__objc_catlist: 0x2e8
   __DATA_CONST.__objc_protolist: 0x1f98
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x361a0
+  __DATA_CONST.__objc_selrefs: 0x361e8
   __DATA_CONST.__objc_protorefs: 0x610
   __DATA_CONST.__objc_superrefs: 0x3378
   __DATA_CONST.__objc_arraydata: 0x32e8
-  __AUTH_CONST.__auth_got: 0x2c90
-  __AUTH_CONST.__auth_ptr: 0x1640
-  __AUTH_CONST.__const: 0x1c958
-  __AUTH_CONST.__cfstring: 0x5a260
-  __AUTH_CONST.__objc_const: 0x12bd20
-  __AUTH_CONST.__objc_intobj: 0x38a0
+  __AUTH_CONST.__auth_got: 0x2c98
+  __AUTH_CONST.__auth_ptr: 0x1560
+  __AUTH_CONST.__const: 0x1cb38
+  __AUTH_CONST.__cfstring: 0x5a400
+  __AUTH_CONST.__objc_const: 0x12beb8
+  __AUTH_CONST.__objc_intobj: 0x38b8
   __AUTH_CONST.__objc_arrayobj: 0x900
   __AUTH_CONST.__objc_doubleobj: 0x150
   __AUTH_CONST.__objc_dictobj: 0x2080
   __AUTH_CONST.__objc_floatobj: 0x10
-  __AUTH.__objc_data: 0x1b820
+  __AUTH.__objc_data: 0x1b818
   __AUTH.__data: 0x3a88
-  __DATA.__objc_ivar: 0x8ef0
-  __DATA.__data: 0x1b170
+  __DATA.__objc_ivar: 0x8f10
+  __DATA.__data: 0x1b130
   __DATA.__bss: 0x11430
   __DATA.__common: 0x308
   __DATA_DIRTY.__objc_data: 0x11400

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 56387
-  Symbols:   53363
-  CStrings:  80722
+  Functions: 56486
+  Symbols:   53408
+  CStrings:  80774
 
Symbols:
+ _HMAccessoryMatterDeviceTypeIDCodingKey
+ _HMAccessoryMatterDeviceTypeIDUpdateMessage
+ _HMAccessoryMatterDeviceTypeIDUpdateMessageKey
+ _OBJC_CLASS_$_HMMutableCHIPAccessorySetupPayload
+ _OBJC_CLASS_$_MTRRVCOperationalStateClusterErrorStateStruct
+ _nw_interface_get_name
- _OBJC_CLASS_$_MTRRVCOperationalStateClusterOperationalErrorEvent
CStrings:
+ "\x01\x14\x18"
+ "\x02?\x06\x1a\x12\x1d\x19$."
+ "\x16\x14\x11\x11"
+ "%lul"
+ "%s %s does not contain attribute value. payload=%s"
+ "%s Calling handleMatterAttributeMessage (Showing notification on THIS Apple TV) with payload=%@"
+ "%s Cannot build Native Matter cluster attribute message payload: We do not support bulletin for clusterID=%@"
+ "%s Cannot build RVC cluster attribute message payload: We do not support bulletin for attributeID=%@"
+ "%s Cannot build RVC operational error attribute message payload: previousValue=nil (error), or previousValue=0 (we handle this case with operational state attribute change)"
+ "%s Cannot build RVC operational error attribute message payload: value=%ld which we do not support for bulletin"
+ "%s Cannot build RVC operational state attribute message payload: Value is charging or docked but previousValue=%@ we do not support showing bulletin for"
+ "%s Cannot build RVC operational state attribute message payload: Value is error but previousValue=%@ we do not support showing bulletin for"
+ "%s Cannot build RVC operational state attribute message payload: Value is paused but previousValue=%@ we do not support showing bulletin for"
+ "%s Cannot build RVC operational state attribute message payload: Value is running but previousValue=%@ we do not support showing bulletin for"
+ "%s Cannot build matter attribute message payload for operational error: previous value is nil"
+ "%s Cannot build matter attribute message payload for operational state: previous value is nil"
+ "%s Error getting attribute changed message payload, returning. error=%@"
+ "%s Error reading operational error path. error=%@"
+ "%s Fetching matter pairings per request"
+ "%s No accessory to handle attribute report: %@"
+ "%s Not sending attribute changed message, nil payload, returning."
+ "%s Reading operational error path returned nil values"
+ "%s Sending bulletin attribute message to target=%s for device=%s with payload=%@"
+ "%s Since we currently do not support event reports for bulletins, this log should not appear. Please file a radar for RVC component. Remove this log when we support events for bulletins."
+ "%s report.value is not a MTRRVCOperationalStateClusterErrorStateStruct"
+ "%{public}@Accessory: %@, Updated matterDeviceTypeID to %@"
+ "%{public}@Accessory: %@, is paired - dropping provided device type update to %@"
+ "%{public}@Failed to fetch CHIPPairings per request: %@"
+ "%{public}@Fetching CHIP pairings per request"
+ "%{public}@Ignore event with no trigger for objectID %{public}@"
+ "%{public}@Message for Matter attribute bulletin is nil. Not posting bulletin. accessory=%@ attributePath=%@ value=%@"
+ "%{public}@Not allowed to post bulletin for Matter Attribute : %@"
+ "%{public}@[Pair-Verify %{public}@] matched service %{public}@ doesn't match the service transaction: %{public}@. Removing it to re-add."
+ "-seed"
+ "@64@0:8@16Q24@32@40@48Q56"
+ "HMDAccessoryMatterAttributeMessageAccessoryUUIDStringKey"
+ "HMDAccessoryMatterAttributeMessageAttributeFieldsKey"
+ "HMDAccessoryMatterAttributeMessageAttributeIDKey"
+ "HMDAccessoryMatterAttributeMessageClusterIDKey"
+ "HMDAccessoryMatterAttributeMessageEndpointIDKey"
+ "HMDAccessoryMatterAttributeMessageName"
+ "HMDAccessoryMatterAttributeMessageValueKey"
+ "HMDAttributePreviousValueMessageKey"
+ "HMDRVCOperationalStateCountdownTimeAttributeMessageKey"
+ "HMDRVCOperationalStateErrorStateAttributeMessageKey"
+ "Home is nil for accessory=%@, (likely just removed), cannot post HMDMatterAttributeChanged notification"
+ "PAUSED_"
+ "RVC_%@DUST_BIN_FULL"
+ "RVC_%@DUST_BIN_MISSING"
+ "RVC_%@FAILED_TO_FIND_DOCK"
+ "RVC_%@MOPPING_PAD_MISSING"
+ "RVC_%@VACUUM_STUCK"
+ "RVC_%@WATER_TANK_EMPTY"
+ "RVC_%@WATER_TANK_LID_OPEN"
+ "RVC_%@WATER_TANK_MISSING"
+ "RVC_CLEANING_COMPLETE"
+ "RVC_NOW_CLEANING"
+ "RVC_NOW_CLEANING_WITH_TIME_REMAINING"
+ "RVC_PAUSED"
+ "RVC_PAUSED_WITH_TIME_REMAINING"
+ "RVC_RETURNING_TO_DOCK"
+ "T@\"NSData\",C,V_ipv4Signature"
+ "T@\"NSData\",C,V_ipv6Signature"
+ "T@\"NSNumber\",C,N,V_matterDeviceTypeID"
+ "T@\"NSNumber\",C,V_matterDeviceTypeID"
+ "T@\"NSSet\",&,V_testAllKnownRootPublicKeys"
+ "T@\"NSString\",C,V_wifiAccessPointOUI"
+ "T@\"NSString\",C,V_wifiBSSID"
+ "T@\"NSString\",C,V_wifiSSID"
+ "TB,V_isIPAccessoryServer"
+ "TB,V_isInfraRelayInterfaceActive"
+ "TB,V_isSeenOnBonjour"
+ "TQ,V_mediaSystemConfiguration"
+ "_fetchPairingsFromAccessoryServer:completion:"
+ "_ipv4Signature"
+ "_ipv6Signature"
+ "_isIPAccessoryServer"
+ "_isInfraRelayInterfaceActive"
+ "_isSeenOnBonjour"
+ "_matterDeviceTypeID"
+ "_mediaSystemConfiguration"
+ "_testAllKnownRootPublicKeys"
+ "_wifiAccessPointOUI"
+ "_wifiBSSID"
+ "_wifiSSID"
+ "accessoryServer:didUpdateMatterDeviceTypeID:"
+ "attributePath.attributeID"
+ "attributePath.clusterID"
+ "deviceTypeID"
+ "fetchLastKnownPairingsWithCompletionHandler:"
+ "handleMatterAttributeMessage:"
+ "initWithHome:nodeId:endpointId:clusterId:commandId:source:"
+ "insertBulletinForMatterAttributeWithAccessory:attributePath:value:fields:"
+ "ipv4Signature"
+ "ipv6Signature"
+ "ir0"
+ "isBulletinSupportedForMatterPath:accessory:endpointID:"
+ "isIPAccessoryServer"
+ "isInfraRelayInterfaceActive"
+ "isSeenOnBonjour"
+ "matterAttributeBulletinMessageFor:attributePath:value:fields:"
+ "matterDeviceTypeID"
+ "mediaSystemConfiguration"
+ "runningModeForHomeUUID:"
+ "rvcOperationalErrorBulletinMessageForErrorStateID:includePausedInMessage:"
+ "setDeviceTypeID:"
+ "setIpv4Signature:"
+ "setIpv6Signature:"
+ "setIsIPAccessoryServer:"
+ "setIsInfraRelayInterfaceActive:"
+ "setIsSeenOnBonjour:"
+ "setMatterDeviceTypeID:"
+ "setMediaSystemConfiguration:"
+ "setTestAllKnownRootPublicKeys:"
+ "setWifiAccessPointOUI:"
+ "setWifiBSSID:"
+ "setWifiSSID:"
+ "submitLogEventForCommandResponse:nodeID:endpointID:clusterID:commandID:source:error:"
+ "testAllKnownRootPublicKeys"
+ "v72@0:8@16Q24@32@40@48Q56@64"
+ "wifiAccessPointOUI"
+ "wifiBSSID"
+ "wifiSSID"
+ "\x81\x11\x122!/\x03!\xf0\x11!"
- "\x02?\x06\x1a\x12\x1c\x19$."
- "\x16\x14\x11"
- "%s Fetching locally cached matter pairings"
- "%s No accessory/home to handle attribute report: %@"
- "%{public}@Fetching locally cached CHIP pairings"
- "%{public}@[%{public}@] Finished generation of home configuration log event for analytics"
- "%{public}@[%{public}@] Home Configuration got updated. Scheduling of new log event generation."
- "%{public}@[%{public}@] Starting generation of home configuration log event for analytics"
- "-internal"
- "@72@0:8@16Q24@32@40@48@56Q64"
- "Generate Home Configuration Log Event"
- "HMDRVCOperationCompletionEventCompletionErrorCodeMessageKey"
- "HMDRVCOperationCompletionEventMessageKey"
- "HMDRVCOperationCompletionEventPausedTimeMessageKey"
- "HMDRVCOperationCompletionEventTotalOperationalTimeMessageKey"
- "HMDRVCOperationalErrorEventErrorStateDetailsMessageKey"
- "HMDRVCOperationalErrorEventErrorStateIDMessageKey"
- "HMDRVCOperationalErrorEventErrorStateLabelMessageKey"
- "HMDRVCOperationalErrorEventMessageKey"
- "RVC_DUST_BIN_FULL"
- "RVC_DUST_BIN_MISSING"
- "RVC_FAILED_TO_FIND_CHARGING_DOCK"
- "RVC_MOP_CLEANING_PAD_MISSING"
- "RVC_OPERATION_COMPLETED"
- "RVC_STUCK"
- "RVC_WATER_TANK_EMPTY"
- "RVC_WATER_TANK_LID_OPEN"
- "RVC_WATER_TANK_MISSING"
- "T@\"NSData\",C,V_cachedIpv4Signature"
- "T@\"NSData\",C,V_cachedIpv6Signature"
- "T@\"NSObject\",N,R,Vfields"
- "T@\"NSString\",C,V_cachedWifiBSSID"
- "T@\"NSString\",C,V_cachedWifiSSID"
- "TB,V_cachedIsConnectedToInternet"
- "TQ,V_cachedCellularDataConnectionState"
- "TQ,V_cachedEthernetConnectionState"
- "TQ,V_cachedWifiConnectionState"
- "Tq,V_cachedBluetoothState"
- "_cachedBluetoothState"
- "_cachedCellularDataConnectionState"
- "_cachedEthernetConnectionState"
- "_cachedIpv4Signature"
- "_cachedIpv6Signature"
- "_cachedIsConnectedToInternet"
- "_cachedWifiBSSID"
- "_cachedWifiConnectionState"
- "_cachedWifiSSID"
- "cachedBluetoothState"
- "cachedCellularDataConnectionState"
- "cachedEthernetConnectionState"
- "cachedIpv4Signature"
- "cachedIpv6Signature"
- "cachedIsConnectedToInternet"
- "cachedWifiBSSID"
- "cachedWifiConnectionState"
- "cachedWifiSSID"
- "errorState"
- "errorStateDetails"
- "errorStateLabel"
- "fields"
- "initWithHome:nodeId:endpointId:clusterId:commandId:fields:source:"
- "pausedTime"
- "setCachedBluetoothState:"
- "setCachedCellularDataConnectionState:"
- "setCachedEthernetConnectionState:"
- "setCachedIpv4Signature:"
- "setCachedIpv6Signature:"
- "setCachedIsConnectedToInternet:"
- "setCachedWifiBSSID:"
- "setCachedWifiConnectionState:"
- "setCachedWifiSSID:"
- "submitLogEventForCommandResponse:nodeID:endpointID:clusterID:commandID:fields:source:error:"
- "v80@0:8@16Q24@32@40@48@56Q64@72"
- "\x81\x11\x122!/\x03!\xf0!"

```
