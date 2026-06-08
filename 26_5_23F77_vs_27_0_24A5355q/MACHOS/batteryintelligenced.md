## batteryintelligenced

> `/usr/libexec/batteryintelligenced`

```diff

-195.100.3.0.0
-  __TEXT.__text: 0x372a4
-  __TEXT.__auth_stubs: 0x880
-  __TEXT.__objc_stubs: 0x3880
-  __TEXT.__objc_methlist: 0x259c
-  __TEXT.__cstring: 0x2b8a
-  __TEXT.__objc_classname: 0x775
-  __TEXT.__objc_methtype: 0x80c
-  __TEXT.__const: 0x288
-  __TEXT.__objc_methname: 0x4622
-  __TEXT.__oslogstring: 0x5b5a
-  __TEXT.__gcc_except_tab: 0x268
-  __TEXT.__unwind_info: 0xc08
-  __DATA_CONST.__auth_got: 0x450
-  __DATA_CONST.__got: 0x240
-  __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0xa90
-  __DATA_CONST.__cfstring: 0x3120
-  __DATA_CONST.__objc_classlist: 0x1c0
-  __DATA_CONST.__objc_protolist: 0x40
+208.0.0.0.0
+  __TEXT.__text: 0x367bc
+  __TEXT.__auth_stubs: 0x920
+  __TEXT.__objc_stubs: 0x3ba0
+  __TEXT.__objc_methlist: 0x2844
+  __TEXT.__cstring: 0x2ecc
+  __TEXT.__objc_classname: 0x774
+  __TEXT.__objc_methtype: 0x109b
+  __TEXT.__const: 0x298
+  __TEXT.__objc_methname: 0x5039
+  __TEXT.__oslogstring: 0x63f5
+  __TEXT.__gcc_except_tab: 0x280
+  __TEXT.__unwind_info: 0xa30
+  __DATA_CONST.__const: 0xb38
+  __DATA_CONST.__cfstring: 0x33e0
+  __DATA_CONST.__objc_classlist: 0x1c8
+  __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x1a0
+  __DATA_CONST.__objc_superrefs: 0x1a8
   __DATA_CONST.__objc_arraydata: 0xca8
   __DATA_CONST.__objc_arrayobj: 0x570
-  __DATA_CONST.__objc_intobj: 0xd20
-  __DATA_CONST.__objc_doubleobj: 0x40
+  __DATA_CONST.__objc_intobj: 0xd50
+  __DATA_CONST.__objc_doubleobj: 0x50
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0x5eb8
-  __DATA.__objc_selrefs: 0x1148
-  __DATA.__objc_ivar: 0x270
-  __DATA.__objc_data: 0x1180
-  __DATA.__data: 0x370
-  __DATA.__bss: 0x210
+  __DATA_CONST.__auth_got: 0x4a0
+  __DATA_CONST.__got: 0x270
+  __DATA_CONST.__auth_ptr: 0x8
+  __DATA.__objc_const: 0x6430
+  __DATA.__objc_selrefs: 0x1328
+  __DATA.__objc_ivar: 0x27c
+  __DATA.__objc_data: 0x11d0
+  __DATA.__data: 0x3f0
+  __DATA.__bss: 0x230
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreML.framework/CoreML
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/BatteryIntelligence.framework/BatteryIntelligence
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreDuetContext.framework/CoreDuetContext
+  - /System/Library/PrivateFrameworks/IDS.framework/IDS
+  - /System/Library/PrivateFrameworks/IDSFoundation.framework/IDSFoundation
   - /System/Library/PrivateFrameworks/PerfPowerServicesReader.framework/PerfPowerServicesReader
   - /System/Library/PrivateFrameworks/PowerLog.framework/PowerLog
   - /System/Library/PrivateFrameworks/PowerUI.framework/PowerUI

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7D5B84E0-6F7D-3BD3-ACF6-1EF31B593BB6
-  Functions: 1159
-  Symbols:   226
-  CStrings:  2282
+  UUID: 9B538CE1-CD72-3CD3-BB4E-89BB115C9A5D
+  Functions: 1192
+  Symbols:   242
+  CStrings:  2478
 
Symbols:
+ _IDSCopyIDForDevice
+ _IDSDefaultPairedDevice
+ _IDSSendMessageOptionAlwaysSkipSelfKey
+ _IDSSendMessageOptionExpectsPeerResponseKey
+ _IDSSendMessageOptionTimeoutKey
+ _OBJC_CLASS_$_BIAccessoryEstimateInfo
+ _OBJC_CLASS_$_IDSService
+ _dispatch_barrier_async
+ _getConnectedAccessoriesInfo
+ _getConnectedAccessoryInfo
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_unsafeClaimAutoreleasedReturnValue
CStrings:
+ "%@ Charge Time"
+ "%@ reached %ld%% in %@. First estimate was %@."
+ "@\"IDSService\""
+ "Accessory"
+ "Accessory estimate for nsuuid %@ is stale (%.0f seconds old, threshold: %.0f seconds)"
+ "Accessory estimate: %@, additionalInformation: %ld"
+ "Accessory with nsuuid %@ not found in IOPowerSources, discarding estimate"
+ "Accessory with nsuuid %@ not found, discarding comparison"
+ "AccessoryChargeTime"
+ "AccessoryEstimates"
+ "Account: %@ (serviceName: %@)"
+ "Added destination from device %@: %@"
+ "BIIDSService"
+ "BatteryAnalysisAccessoryNotifications"
+ "Cleared all accessory estimates"
+ "DELEGATE CALLBACK: Active accounts changed (count: %lu)"
+ "DELEGATE CALLBACK: Devices changed (count: %lu)"
+ "DELEGATE CALLBACK: Message send failed (identifier: %@): %@"
+ "DELEGATE CALLBACK: Message sent successfully (identifier: %@)"
+ "Failed to encode accessoryEstimates: %@"
+ "Failed to load accessory estimates: %@"
+ "Failed to send message to IDS (type: %@): %@"
+ "IDS"
+ "IDS Device: %@ (name: %@)"
+ "IDS service initialized."
+ "IDSServiceDelegate"
+ "Invalid nsuuid for accessory estimate update"
+ "It will take %@ to charge to %ld%%."
+ "Key %@ not found in dictionary. Returning default value: %@"
+ "Key %@ not found in dictionary. Returning default value: %ld"
+ "Loaded %lu accessory estimates from defaults"
+ "Message must include messageType key"
+ "Message sent to IDS (type: %@, identifier: %@)"
+ "No devices found, using IDSDefaultPairedDevice"
+ "No matching IDS device found for fromID %@"
+ "No nsuuid available for device %@"
+ "Posting accessory estimate notification for device: %@"
+ "Received comparison from '%@': estimated %.0f sec, actual %.0f sec to %ld%%"
+ "Received estimate from '%@': %.0f sec to %ld%% with additionalInformation: %ld"
+ "Received message with invalid fromID"
+ "Received message without messageType - ignoring"
+ "Received unknown message type: %@"
+ "SOC mismatch for '%@': message reports %ld%%, IOPowerSources shows %ld%% (difference: %ld%%), discarding estimate"
+ "SOCVDebounce"
+ "Sent accessory estimates for %lu devices."
+ "Service accounts: %lu, devices: %lu"
+ "Skipping SBC event with missing or invalid metric values"
+ "Skipping daily event with missing or invalid CycleCount"
+ "Skipping daily event with missing or invalid TimeAtHighSoc"
+ "Successfully posted accessory comparison notification for device: %@."
+ "T@\"IDSService\",&,N,V_service"
+ "T@\"NSMutableDictionary\",&,V_accessoryEstimates"
+ "Unknown Device"
+ "Updated accessory estimate for nsuuid %@: %.0f sec to %ld%% (isFirstEstimate: %d, additionalInformation: %ld)"
+ "Watch estimate message will be processed for iPhones only."
+ "XPC handler is nil/invalid for accessory estimates. Client disconnected or connection invalid. Cannot deliver response."
+ "_accessoryEstimates"
+ "_service"
+ "accessoryEstimates"
+ "accessoryEstimatesWithHandler:"
+ "accounts"
+ "actualTime"
+ "addDelegate:queue:"
+ "applewatch"
+ "clearAccessoryEstimates"
+ "com.apple.batteryintelligence.ids"
+ "com.apple.batteryintelligenced.battery-analysis-service-accessory-estimates"
+ "com.apple.batteryintelligenced.battery-analysis-service-clear-accessory-estimates"
+ "com.apple.batteryintelligenced.battery-analysis-service-update-accessory-estimate"
+ "com.apple.batteryintelligenced.batteryanalysisaccessoryestimateupdated"
+ "com.apple.private.alloy.batteryintelligence"
+ "currentCapacity"
+ "devices"
+ "estimatedTime"
+ "handleWatchBatteryComparisonMessage:fromID:context:"
+ "handleWatchBatteryEstimateMessage:fromID:context:"
+ "initWithService:"
+ "messageType"
+ "nsuuid"
+ "nsuuidForIDSMessageFromID:"
+ "postAccessoryComparisonNotification:against:forDeviceName:toSOC:withIcon:"
+ "postAccessoryEstimateNotification:forDeviceName:toSOC:withIcon:"
+ "removeAllObjects"
+ "removeObjectForKey:"
+ "sendMessage:error:"
+ "sendMessage:toDestinations:priority:options:identifier:error:"
+ "service:account:didReceiveLocalNetworkHandshake:fromID:context:"
+ "service:account:identifier:didSendWithSuccess:error:"
+ "service:account:identifier:didSendWithSuccess:error:context:"
+ "service:account:identifier:fromID:hasBeenDeliveredWithContext:"
+ "service:account:identifier:hasBeenDeliveredWithContext:"
+ "service:account:identifier:sentBytes:totalBytes:"
+ "service:account:incomingData:fromID:context:"
+ "service:account:incomingMessage:fromID:context:"
+ "service:account:incomingOpportunisticData:withIdentifier:fromID:context:"
+ "service:account:incomingPendingMessageOfType:fromID:context:"
+ "service:account:incomingResourceAtURL:fromID:context:"
+ "service:account:incomingResourceAtURL:metadata:fromID:context:"
+ "service:account:incomingUnhandledProtobuf:fromID:context:"
+ "service:account:inviteDroppedForSessionID:fromID:context:error:"
+ "service:account:inviteReceivedForSession:fromID:"
+ "service:account:inviteReceivedForSession:fromID:withContext:"
+ "service:account:inviteReceivedForSession:fromID:withOptions:"
+ "service:account:pendingResourceWithMetadata:fromID:acknowledgementBlock:context:"
+ "service:account:receivedGroupSessionParticipantDataUpdate:"
+ "service:account:receivedGroupSessionParticipantUpdate:"
+ "service:account:receivedGroupSessionParticipantUpdate:context:"
+ "service:activeAccountsChanged:"
+ "service:connectedDevicesChanged:"
+ "service:devicesChanged:"
+ "service:didCancelMessageWithSuccess:error:identifier:"
+ "service:didSendOpportunisticDataWithIdentifier:toIDs:"
+ "service:didSwitchActivePairedDevice:acknowledgementBlock:"
+ "service:linkedDevicesChanged:"
+ "service:nearbyDevicesChanged:"
+ "serviceAllowedTrafficClassifiersDidReset:"
+ "serviceSpaceDidBecomeAvailable:"
+ "set"
+ "setAccessoryEstimates:"
+ "setClasses:forSelector:argumentIndex:ofReply:"
+ "setDeviceName:"
+ "setNsuuid:"
+ "setService:"
+ "setWithObjects:"
+ "socAtEstimateTime"
+ "unarchivedObjectOfClasses:fromData:error:"
+ "updateAccessoryEstimate:forNSUUID:forEndSOC:iosMonotonicAnchorTimeInNanoSeconds:isFirstEstimate:additionalInformation:"
+ "v24@0:8@\"IDSService\"16"
+ "v24@0:8@?<v@?@\"NSArray\"@\"NSError\">16"
+ "v32@0:8@\"IDSService\"16@\"NSArray\"24"
+ "v32@0:8@\"IDSService\"16@\"NSSet\"24"
+ "v40@0:8@\"IDSService\"16@\"IDSAccount\"24@\"IDSGroupSessionParticipantUpdate\"32"
+ "v40@0:8@\"IDSService\"16@\"IDSDevice\"24@?<v@?>32"
+ "v40@0:8@\"IDSService\"16@\"NSString\"24@\"NSArray\"32"
+ "v44@0:8@\"IDSService\"16B24@\"NSError\"28@\"NSString\"36"
+ "v44@0:8@16B24@28@36"
+ "v48@0:8@\"IDSService\"16@\"IDSAccount\"24@\"IDSGroupSessionParticipantUpdate\"32@\"IDSMessageContext\"40"
+ "v48@0:8@\"IDSService\"16@\"IDSAccount\"24@\"IDSSession\"32@\"NSString\"40"
+ "v48@0:8@\"IDSService\"16@\"IDSAccount\"24@\"NSString\"32@40"
+ "v48@0:8@16@24@32@40"
+ "v48@0:8d16@24q32@40"
+ "v52@0:8@\"IDSService\"16@\"IDSAccount\"24@\"NSString\"32B40@\"NSError\"44"
+ "v52@0:8@\"IDSService\"16@\"IDSAccount\"24B32@\"NSString\"36@\"NSData\"44"
+ "v52@0:8@16@24@32B40@44"
+ "v52@0:8@16@24B32@36@44"
+ "v56@0:8@\"IDSService\"16@\"IDSAccount\"24@\"IDSProtobuf\"32@\"NSString\"40@\"IDSMessageContext\"48"
+ "v56@0:8@\"IDSService\"16@\"IDSAccount\"24@\"IDSSession\"32@\"NSString\"40@\"NSData\"48"
+ "v56@0:8@\"IDSService\"16@\"IDSAccount\"24@\"IDSSession\"32@\"NSString\"40@\"NSDictionary\"48"
+ "v56@0:8@\"IDSService\"16@\"IDSAccount\"24@\"NSData\"32@\"NSString\"40@\"IDSMessageContext\"48"
+ "v56@0:8@\"IDSService\"16@\"IDSAccount\"24@\"NSDictionary\"32@\"NSString\"40@\"IDSMessageContext\"48"
+ "v56@0:8@\"IDSService\"16@\"IDSAccount\"24@\"NSString\"32@\"NSString\"40@48"
+ "v56@0:8@\"IDSService\"16@\"IDSAccount\"24@\"NSString\"32q40q48"
+ "v56@0:8@\"IDSService\"16@\"IDSAccount\"24@\"NSURL\"32@\"NSString\"40@\"IDSMessageContext\"48"
+ "v56@0:8@\"IDSService\"16@\"IDSAccount\"24q32@\"NSString\"40@\"IDSMessageContext\"48"
+ "v56@0:8@16@24@32@40@48"
+ "v56@0:8@16@24@32q40q48"
+ "v56@0:8@16@24q32@40@48"
+ "v56@0:8d16d24@32q40@48"
+ "v60@0:8@\"IDSService\"16@\"IDSAccount\"24@\"NSString\"32B40@\"NSError\"44@\"IDSMessageContext\"52"
+ "v60@0:8@16@24@32B40@44@52"
+ "v60@0:8d16@24q32q40B48q52"
+ "v64@0:8@\"IDSService\"16@\"IDSAccount\"24@\"NSData\"32@\"NSString\"40@\"NSString\"48@\"IDSMessageContext\"56"
+ "v64@0:8@\"IDSService\"16@\"IDSAccount\"24@\"NSDictionary\"32@\"NSString\"40@?<v@?B>48@\"IDSMessageContext\"56"
+ "v64@0:8@\"IDSService\"16@\"IDSAccount\"24@\"NSString\"32@\"NSString\"40@\"NSData\"48@\"NSError\"56"
+ "v64@0:8@\"IDSService\"16@\"IDSAccount\"24@\"NSURL\"32@\"NSDictionary\"40@\"NSString\"48@\"IDSMessageContext\"56"
+ "v64@0:8@16@24@32@40@48@56"
+ "v64@0:8@16@24@32@40@?48@56"
+ "watchBatteryComparison"
+ "watchBatteryEstimate"

```
