## HomeKitMatter

> `/System/Library/PrivateFrameworks/HomeKitMatter.framework/HomeKitMatter`

```diff

-1278.6.20.0.1
-  __TEXT.__text: 0x132aa4
+1278.6.26.0.0
+  __TEXT.__text: 0x133448
   __TEXT.__auth_stubs: 0xa40
-  __TEXT.__objc_methlist: 0x9c54
+  __TEXT.__objc_methlist: 0x9ccc
   __TEXT.__const: 0x158
   __TEXT.__dlopen_cstrs: 0x58
-  __TEXT.__gcc_except_tab: 0x2b80
-  __TEXT.__cstring: 0x6262
-  __TEXT.__oslogstring: 0x25b8f
+  __TEXT.__gcc_except_tab: 0x2b5c
+  __TEXT.__cstring: 0x6014
+  __TEXT.__oslogstring: 0x25c9d
   __TEXT.__ustring: 0x68
-  __TEXT.__unwind_info: 0x2cb8
+  __TEXT.__unwind_info: 0x2cc8
   __TEXT.__objc_classname: 0x133b
-  __TEXT.__objc_methname: 0x23b8b
-  __TEXT.__objc_methtype: 0x3817
-  __TEXT.__objc_stubs: 0x156a0
-  __DATA_CONST.__got: 0x990
-  __DATA_CONST.__const: 0x4550
+  __TEXT.__objc_methname: 0x23e0d
+  __TEXT.__objc_methtype: 0x3859
+  __TEXT.__objc_stubs: 0x15820
+  __DATA_CONST.__got: 0x998
+  __DATA_CONST.__const: 0x4530
   __DATA_CONST.__objc_classlist: 0x3e8
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x120
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6738
+  __DATA_CONST.__objc_selrefs: 0x67a8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x2c8
   __DATA_CONST.__objc_arraydata: 0x228
   __AUTH_CONST.__auth_got: 0x530
-  __AUTH_CONST.__const: 0xf00
-  __AUTH_CONST.__cfstring: 0x6620
-  __AUTH_CONST.__objc_const: 0xe9a8
+  __AUTH_CONST.__const: 0xec0
+  __AUTH_CONST.__cfstring: 0x6440
+  __AUTH_CONST.__objc_const: 0xe9c0
   __AUTH_CONST.__objc_intobj: 0x15d8
   __AUTH_CONST.__objc_arrayobj: 0x180
   __AUTH_CONST.__objc_doubleobj: 0x20

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 4079
-  Symbols:   4838
-  CStrings:  8249
+  Functions: 4085
+  Symbols:   4845
+  CStrings:  8255
 
Symbols:
+ _OBJC_CLASS_$_NSJSONSerialization
CStrings:
+ "%{public}@Accessory Configuration for %@/%@(%@) %@"
+ "%{public}@Accessory Configuration: Generate Accessory Configuration for '%@' by reason : %@"
+ "%{public}@Accessory Configuration: JSON conversion failed: %@"
+ "%{public}@Accessory Configuration: No Endpoints In Use at endpoint 0 of node %@"
+ "%{public}@Accessory Configuration: Setting timer to capture state information due to configuration change for accessory %@, timeout is %@"
+ "%{public}@Accessory Configuration: Setting timer to capture state information for %@ due to matter device reachable notification, timeout is %@"
+ "%{public}@Accessory Configuration: completed for server:%@ with Error: %@."
+ "%{public}@Accessory server operations disabled. Aborting generating accessory configuration information."
+ "%{public}@Characteristics Operation Queue: generate accessory configuration information job(%lu) complete."
+ "%{public}@Characteristics Operation Queue: generate accessory configuration information job(%lu) queued."
+ "%{public}@Characteristics Operation Queue: generate accessory configuration information job(%lu) started."
+ "%{public}@Failed to get endpoints for node %@"
+ "%{public}@No Matter device available to fetch SupportedThreadFeatures"
+ "%{public}@No Matter device controller available to generate accessory configuration information"
+ "%{public}@No endpoint found to contain Network Commissioning Cluster to fetch SupportedThreadFeatures"
+ "%{public}@No product label information available so using default name: %@"
+ "%{public}@Notifying delegate of Thread capabilities %@"
+ "%{public}@Notifying delegate of isWEDAccessory %@"
+ "%{public}@Processing handleNotifyUpdateAppliedForNodeID command {nodeID = %@, updateToken = %@, newVersion = %@}, is simply returning OK without performing any additional processing."
+ "%{public}@RockSetting was read with unexpected class type %@"
+ "%{public}@RockSupport was read with unexpected class type %@"
+ "%{public}@SupportedThreadFeatures attribute was nil"
+ "%{public}@Updating all characteristic values from MTRDevice cache for accessory %@"
+ "%{public}@Updating product label from %@ to %@"
+ "%{public}@Using metadata product label: %@ and vendor name: %@"
+ "%{public}@[Flow: %@] Failed to find current fabric index so not removing any users."
+ "%{public}@[NewFlow: %@] Removing all users"
+ "@48@0:8@16@24@32^@40"
+ "Accessory Configuration for %@/%@(%@)"
+ "Attributes"
+ "ClientClusters"
+ "ClusterID"
+ "ClusterInfo"
+ "ClusterRevision"
+ "DevicePaired"
+ "DeviceTypes"
+ "EndpointData"
+ "EndpointID"
+ "Endpoints"
+ "Events"
+ "Label"
+ "Reason"
+ "ServerClusters"
+ "T@\"NSString\",C,V_label"
+ "Time"
+ "_endpointIncludingClusterID:amongEndpoints:device:error:"
+ "_fetchAccessoryConfigurationForDevice:endpointID:callbackQueue:"
+ "_fetchAccessoryConfigurationForDevice:endpointID:clusterID:callbackQueue:"
+ "_fetchSupportedThreadFeatures"
+ "_label"
+ "_notifyDelegateOfMatterAccessoryIsWEDAccessory:"
+ "_notifyDelegateOfMatterAccessoryThreadCapabilities:"
+ "accessoryProductLabel"
+ "controller:commissioneeHasReceivedNetworkCredentials:"
+ "dataWithJSONObject:options:error:"
+ "dateToMatterEpoch:withTimeZone:"
+ "endpointForClusterID:mtrDevice:"
+ "endpointsWithMTRDevice:endpointID:"
+ "fetchAccessoryConfigurationForDevice:nodeId:server:reasonString:callbackQueue:completionHandler:"
+ "generateAccessoryConfigurationForReason:completionHandler:"
+ "hmmtr.descriptorClusterManager.temporary"
+ "initWithStartTime:endTime:withTimeZone:"
+ "localizedDescription"
+ "notifyMatterAccessoryIsWEDAccessory:"
+ "notifyMatterAccessoryThreadCapabilities:"
+ "readAttributeSupportedThreadFeaturesWithParams:"
+ "removeAllUsers"
+ "secondsFromGMTForDate:"
+ "supportedThreadFeatures"
+ "updateAllCharacteristicValuesPostHAPServiceEnumerationForAccessory:completion:"
+ "v32@0:8@\"MTRDeviceController\"16@\"NSNumber\"24"
+ "yyyy-MM-dd'T'HH:mm:ssZ"
- " %@ (revision %@), "
- " }; }; "
- "%{public}@Accessory server operations disabled. Aborting generating state capture information."
- "%{public}@Characteristics Operation Queue: generate state capture information job(%lu) complete."
- "%{public}@Characteristics Operation Queue: generate state capture information job(%lu) queued."
- "%{public}@Characteristics Operation Queue: generate state capture information job(%lu) started."
- "%{public}@No Matter device controller available to generate state capture information"
- "%{public}@No paired accessory found for nodeID %@ - ignore notification"
- "%{public}@No product name information available so using default name: %@"
- "%{public}@Processing handleNotifyUpdateAppliedForNodeID command {nodeID = %@, updateToken = %@, newVersion = %@}"
- "%{public}@Provided token %@ doesn't match assigned token %@ for accessory %@, accepting anyways"
- "%{public}@Received unexpected NotifyUpdateApplied when we were still waiting for ApplyUpdateRequest after BDX transfer completed for accessory %@"
- "%{public}@Request to generate state capture information"
- "%{public}@State Capture: Information for endpoint %@: %@"
- "%{public}@State Capture: Information for endpoint 0: %@"
- "%{public}@State Capture: Information generated for %@, triggered by reason %@ : %@"
- "%{public}@State Capture: No Endpoints In Use at endpoint 0 of node %@"
- "%{public}@State Capture: Setting timer to capture state information due to configuration change for accessory %@, timeout is %@"
- "%{public}@State Capture: Setting timer to capture state information for %@ due to matter device reachable notification, timeout is %@"
- "%{public}@State Capture: Timer expired, generate State Capture Information for Device Connected"
- "%{public}@State Capture: Timer expired, generate State Capture Information for configuration change"
- "%{public}@State Capture: completed for server:%@ with Error: %@."
- "%{public}@Updating product name from %@ to %@"
- "%{public}@Using metadata product name: %@ and vendor name: %@"
- "%{public}@[NewFlow: %@] Removing home user"
- "( ClusterID:%@ ClusterInfo: %@ ), "
- "( NodeID: %@; FabricID: %@, "
- "(AcceptedCommands: %@), "
- "(AcceptedCommands: ()), "
- "(Attributes: %@)"
- "(Attributes: ()), "
- "(ClientClusters: "
- "(ClientClusters: ()),"
- "(ClusterID : %@, ClusterInfo : %@), "
- "(ClusterRevision: %@), "
- "(DeviceTypes : ()), "
- "(DeviceTypes: "
- "(Events: %@), "
- "(Events: ()), "
- "(FeatureMap: %@), "
- "(GeneratedCommands: %@) "
- "(GeneratedCommands: ()), "
- "(PartsList: %@), "
- "(PartsList: ()), "
- "(ServerClusters : "
- "(ServerClusters : () ),"
- ")"
- "), "
- "HMMTRAccessoryServer State for %@/%@(%@)"
- "Model"
- "Name: %@, NodeID: %@, FabricID: %@, Category %@, ObjectID: %@, No state capture information available."
- "Name: %@, NodeID: %@, FabricID: %@, Category: %@, ObjectID: %@, State capture information: %@"
- "Reason: %@, Time: %@, Data: %@"
- "T@\"NSString\",C,V_model"
- "_fetchStateCaptureInformationForDevice:endpointID:callbackQueue:"
- "_fetchStateCaptureInformationForDevice:endpointID:clusterID:callbackQueue:"
- "_model"
- "dateToMatterEpoch:"
- "fetchStateCaptureInformationForDevice:nodeId:server:callbackQueue:completionHandler:"
- "generateStateCaptureInformationForReason:completionHandler:"
- "initWithStartTime:endTime:"
- "model"
- "removeHomeUser"
- "rockSettingValue"
- "{EndpointID: %@, EndpointData: %@}, "
- "{Endpoints: {EndpointID: %@, EndpointData: %@ }, "

```
