## Matter

> `/System/Library/Frameworks/Matter.framework/Matter`

```diff

-196.3.5.0.0
-  __TEXT.__text: 0x76e968
+196.4.4.0.0
+  __TEXT.__text: 0x752218
   __TEXT.__auth_stubs: 0x1270
-  __TEXT.__init_offsets: 0x8
-  __TEXT.__objc_methlist: 0x4b8c8
-  __TEXT.__const: 0x5f91b
-  __TEXT.__gcc_except_tab: 0xa2a94
-  __TEXT.__cstring: 0x3b12f
-  __TEXT.__oslogstring: 0x14a81
-  __TEXT.__unwind_info: 0x3ea50
-  __TEXT.__objc_classname: 0xc7ab
-  __TEXT.__objc_methname: 0xb197f
-  __TEXT.__objc_methtype: 0x6f84
-  __TEXT.__objc_stubs: 0x2dac0
-  __DATA_CONST.__got: 0x1ae0
-  __DATA_CONST.__const: 0x16d00
-  __DATA_CONST.__objc_classlist: 0x2538
+  __TEXT.__init_offsets: 0x10
+  __TEXT.__objc_methlist: 0x4a000
+  __TEXT.__const: 0x5faab
+  __TEXT.__gcc_except_tab: 0x9f2b8
+  __TEXT.__cstring: 0x3c5c9
+  __TEXT.__oslogstring: 0x157e4
+  __TEXT.__unwind_info: 0x3d178
+  __TEXT.__objc_classname: 0xc7d1
+  __TEXT.__objc_methname: 0xb1bd6
+  __TEXT.__objc_methtype: 0x6f8a
+  __TEXT.__objc_stubs: 0x2dc60
+  __DATA_CONST.__got: 0x1af8
+  __DATA_CONST.__const: 0x16df0
+  __DATA_CONST.__objc_classlist: 0x2548
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x17820
+  __DATA_CONST.__objc_selrefs: 0x17880
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x1950
+  __DATA_CONST.__objc_superrefs: 0x1960
   __DATA_CONST.__objc_arraydata: 0x28
   __AUTH_CONST.__auth_got: 0x950
   __AUTH_CONST.__auth_ptr: 0x18
-  __AUTH_CONST.__const: 0x1a210
-  __AUTH_CONST.__cfstring: 0x11700
-  __AUTH_CONST.__objc_const: 0x58d58
-  __AUTH_CONST.__objc_intobj: 0x53b8
+  __AUTH_CONST.__const: 0x1a578
+  __AUTH_CONST.__cfstring: 0x11860
+  __AUTH_CONST.__objc_const: 0x58ed8
+  __AUTH_CONST.__objc_intobj: 0x5388
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH.__objc_data: 0x17430
-  __AUTH.__data: 0x98
-  __DATA.__objc_ivar: 0x2f5c
+  __AUTH.__objc_data: 0x174d0
+  __AUTH.__data: 0x108
+  __DATA.__objc_ivar: 0x2f60
   __DATA.__data: 0x5e00
-  __DATA.__bss: 0x5398
+  __DATA.__bss: 0x53d8
   __DATA.__common: 0x100
   __DATA_DIRTY.__bss: 0x1b8
-  __DATA_DIRTY.__common: 0x790
+  __DATA_DIRTY.__common: 0x7f0
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreData.framework/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libdns_services.dylib
   - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 46228
-  Symbols:   2753
-  CStrings:  25377
+  Functions: 45705
+  Symbols:   2761
+  CStrings:  25564
 
Symbols:
+ _MTRDeviceControllerRegistrationControllerCompressedFabricIDKey
+ _MTRDeviceControllerRegistrationControllerIsRunningKey
+ _MTRDeviceControllerRegistrationControllerNodeIDKey
+ _MTRDeviceControllerRegistrationDeviceInternalStateKey
+ _OBJC_CLASS_$_MTRAttributeValueWaiter
+ _OBJC_CLASS_$_NSHashTable
+ _OBJC_CLASS_$_NSThread
+ _OBJC_METACLASS_$_MTRAttributeValueWaiter
CStrings:
+ "\x01\xf0\xf0\xf0\xf0R\x13\x13\x12"
+ "\x13\x16"
+ "\x14\x11"
+ "\x15\x16\x11\x13\"\"\x14\x11\x11"
+ "\x19"
+ " - Missing or malformed device Info"
+ " - Missing or malformed deviceInternalState"
+ " - Missing or malformed nodeID"
+ "%@ %p wait for attribute values canceled"
+ "%@ %p wait for attribute values completed"
+ "%@ %p wait for attribute values timed out"
+ "%@ %p wait for attribute values unknown error: %@"
+ "%@ %s"
+ "%@ Event %@ missing event number"
+ "%@ NULL host resolved, ignoring"
+ "%@ at least one of observed and expected value is not an NSArrray: %@, %@"
+ "%@ device:internalStateUpdated: handed state with invalid value for \"%@\": %@"
+ "%@ device:internalStateUpdated: handed state with no value for \"%@\": %@"
+ "%@ expected data-value is not an NSDictionary: %@"
+ "%@ expected or observed array-value contains entries that are not NSDictionary: %@, %@"
+ "%@ expected structure-value contains invalid field %@"
+ "%@ got invoke response for (%@, %@, %@) that has invalid data: %@"
+ "%@ got invoke response for (%@, %@, %@) that has invalid error object: %@"
+ "%@ got invoke response for (%@, %@, %@) with both values and error: %@, %@"
+ "%@ got invoke response for (%@, %@, %@) without values or error"
+ "%@ handed a response-value that is not a dictionary: %@"
+ "%@ injected attribute report is not well-formed: %@"
+ "%@ injected event report is not well-formed: %@"
+ "%@ invalid data-value reported: %@"
+ "%@ invalid device:internalStateUpdated dictionary: %@"
+ "%@ invalid device:internalStateUpdated: nodeID: %@"
+ "%@ invalid device:receivedAttributeReport: attributeReport: %@"
+ "%@ invalid device:receivedAttributeReport: nodeID: %@"
+ "%@ invalid device:receivedEventReport: eventReport: %@"
+ "%@ invalid device:receivedEventReport: nodeID: %@"
+ "%@ invalid deviceBecameActive: nodeID: %@"
+ "%@ invalid deviceConfigurationChanged: nodeID: %@"
+ "%@ no valid path for attribute report %@"
+ "%@ observed data-value is not an NSDictionary: %@"
+ "%@ observed structure-value contains invalid field %@"
+ "%@ observed to expected attribute data-value comparison does not expect comparing two nil dictionaries"
+ "%@ waitForAttributeValues no need to wait, values already match: %@"
+ "%@ waitForAttributeValues will wait up to %f seconds for %@"
+ "(*status == Status::UnsupportedEndpoint) || (*status == Status::UnsupportedCluster) || (*status == Status::UnsupportedAttribute)"
+ "-[MTRDevice_XPC device:internalStateUpdated:]"
+ "-[MTRDevice_XPC deviceConfigurationChanged:]"
+ "/Library/Caches/com.apple.xbs/Sources/CHIPFramework/connectedhomeip/src/app/ReadHandler.h"
+ "/Library/Caches/com.apple.xbs/Sources/CHIPFramework/connectedhomeip/src/app/codegen-data-model-provider/CodegenDataModelProvider.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/CHIPFramework/connectedhomeip/src/app/codegen-data-model-provider/CodegenDataModelProvider.h"
+ "/Library/Caches/com.apple.xbs/Sources/CHIPFramework/connectedhomeip/src/app/codegen-data-model-provider/CodegenDataModelProvider_Read.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/CHIPFramework/connectedhomeip/src/app/codegen-data-model-provider/CodegenDataModelProvider_Write.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/CHIPFramework/connectedhomeip/src/app/codegen-data-model-provider/EmberAttributeDataBuffer.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/CHIPFramework/connectedhomeip/src/app/data-model-provider/Provider.h"
+ "/Library/Caches/com.apple.xbs/Sources/CHIPFramework/connectedhomeip/src/darwin/Framework/CHIP/MTRCallbackBridgeBase.h"
+ "/Library/Caches/com.apple.xbs/Sources/CHIPFramework/connectedhomeip/src/darwin/Framework/CHIP/MTRDevice_XPC.mm"
+ "/Library/Caches/com.apple.xbs/Sources/CHIPFramework/connectedhomeip/src/lib/support/BufferReader.h"
+ "<%@: %@>"
+ "<%@: %p, node: %016llX-%016llX (%llu), VID: %@, PID: %@, WiFi: %@, Thread: %@, controller: %@ state: %lu>"
+ "@ observed to expected attribute data-value comparison does not expect a nil %s"
+ "@\"NSHashTable\""
+ "@48@0:8@16@24@32@?40"
+ "@48@0:8@16d24@32@?40"
+ "AppServer"
+ "Attribute report contains a weird entry: %@"
+ "Attribute report contains an entry that claims to be both data and error: %@"
+ "Attribute report is not an array: %@"
+ "B16@?0@\"MTRAttributePath\"8"
+ "B16@?0@\"MTREventPath\"8"
+ "B16@?0@\"NSDictionary\"8"
+ "B16@?0@\"NSError\"8"
+ "B16@?0@\"NSNumber\"8"
+ "B36@0:8@16@24B32"
+ "Battery Storage"
+ "Controller Factory Start"
+ "Controller Factory Stop"
+ "Data to write exceeds the attribute size claimed."
+ "Enumerate error: %s"
+ "Event report claims epoch timing but does not have the time: %@"
+ "Event report claims system uptime timing but does not have the time: %@"
+ "Event report contains a weird entry: %@"
+ "Event report contains an entry that claims to be both data and error: %@"
+ "Event report is not an array: %@"
+ "Failed during PASE session pairing request: %s"
+ "Failed to get data version for %d/0x%04X_%04X"
+ "Failed to load cluster entry: %s"
+ "Failed to load cluster info: %s"
+ "Failed to read attribute: %s"
+ "Heat Pump"
+ "Invoke response claims to have both data and error: %@"
+ "Invoke response claims to have data that is not a data-value: %@"
+ "Invoke response data is not of structure type: %@"
+ "Invoke response is not an array with exactly one entry: %@"
+ "Invoke response is not an array with the right things in it: %@"
+ "Invoke response is not an array: %@"
+ "MTRAttributeValueWaiter"
+ "MTRAwaitedAttributeState"
+ "MTRDeviceControllerRegistrationControllerCompressedFabricID"
+ "MTRDeviceControllerRegistrationControllerIsRunning"
+ "MTRDeviceControllerRegistrationControllerNodeID"
+ "MTRDeviceControllerRegistrationDeviceInternalState"
+ "MTRDeviceInternalPropertyDeviceCachePrimed"
+ "MTRDeviceInternalPropertyDeviceInternalState"
+ "MTRDeviceInternalPropertyEstimatedStartTime"
+ "MTRDeviceInternalPropertyEstimatedSubscriptionLatency"
+ "MaxContentBufferSize"
+ "Null data model while checking attribute properties."
+ "Read request on unknown cluster - no data version available"
+ "Reading attribute: Cluster=0x%04X_%04X Endpoint=0x%x AttributeId=0x%04X_%04X (expanded=%d)"
+ "Received controllerConfigurationUpdated: controllerNodeID %@ compressedFabricID %016lluX deviceInfoList %@"
+ "Solar Power"
+ "T@\"NSNumber\",&,N,V_highestObservedEventNumber"
+ "T@\"NSObject<OS_dispatch_queue>\",R,&,N,V_workQueue"
+ "T@\"NSObject<OS_dispatch_source>\",&,N,V_expirationTimer"
+ "T@\"NSUUID\",R,N,V_UUID"
+ "Trying to perform action on node ID 0x%016llX (%llu) with a non-concrete controller"
+ "Trying to perform action with PASE device with a non-concrete controller"
+ "Uknown time type for event report: %@"
+ "Unable to get cluster info for Endpoint 0x%x, Cluster 0x%04X_%04X"
+ "Water Heater"
+ "Write Version mismatch for Endpoint 0x%x, Cluster 0x%04X_%04X"
+ "Writing attribute: Cluster=0x%04X_%04X Endpoint=0x%x AttributeId=0x%04X_%04X"
+ "[%@]: %@"
+ "_UUID"
+ "_applicationCallback"
+ "_attributeDataValue:satisfiesValueExpectation:"
+ "_attributeValue:reportedForPath:"
+ "_attributeValue:reportedForPath:byDevice:"
+ "_attributeValueWaiters"
+ "_attributeWaitCanceled:"
+ "_attributeWaitTimedOut:"
+ "_cancelAllAttributeValueWaiters"
+ "_completion"
+ "_compressedFabricID"
+ "_doAttributeWaitCanceled:"
+ "_expirationTimer"
+ "_highestObservedEventNumber"
+ "_injectPossiblyInvalidEventReport:"
+ "_internalState:hasValidValuesForKeys:valueRequired:"
+ "_notifyAttributeValueWaiter:withError:"
+ "_notifyWithError:"
+ "_valueExpectations"
+ "_valueSatisfied"
+ "allValues"
+ "allValuesSatisfied"
+ "callStackSymbols"
+ "caseSessionMgr != nullptr"
+ "commandInfo.has_value()"
+ "controller:controllerConfigurationUpdated:"
+ "expected"
+ "expirationTimer"
+ "highestObservedEventNumber"
+ "initWithDevice:values:queue:completion:"
+ "observed"
+ "readAttributeMaxContentBufferSizeWithClusterStateCache:endpoint:queue:completion:"
+ "readAttributeMaxContentBufferSizeWithCompletion:"
+ "readAttributeMaxContentBufferSizeWithParams:"
+ "setExpirationTimer:"
+ "setHighestObservedEventNumber:"
+ "subscribeAttributeMaxContentBufferSizeWithParams:subscriptionEstablished:reportHandler:"
+ "waitForAttributeValues handed invalid data-value %@ for path %@"
+ "waitForAttributeValues:timeout:queue:completion:"
+ "weakObjectsHashTable"
+ "writer.Fit(written)"
+ "{MTRApplicationCallback=\"_vptr$ApplicationCallback\"^^?}"
- "\x01\xf0\xf0\xf0\xf0B\x13\x13\x12"
- "\x13\x13"
- "\x15\x16\x11\x13\"\"\x13\x11\x11"
- "%@ internal state updated"
- "-[MTRDevice_XPC device:stateChanged:]"
- "/Library/Caches/com.apple.xbs/Sources/CHIPFramework/connectedhomeip/src/app/util/ember-compatibility-functions.cpp"
- "<%@: %p, node: %016llX-%016llX (%llu), VID: %@, PID: %@, WiFi: %@, Thread: %@, controller: %@>"
- "Attribute type %x not handled"
- "Data to write exceedes the attribute size claimed."
- "Endpoint %x, Cluster 0x%04X_%04X not found in IsClusterDataVersionEqual!"
- "Endpoint %x, Cluster 0x%04X_%04X not found in ReadClusterDataVersion!"
- "EventList"
- "Failed to prepare data to write: %s"
- "MaxPreRollBufferSize"
- "Q\x12\xf0\xf0\xf0\xf0\xf0Q\xf0\xf0\xf0\xf0\xf0\xb1\xbc"
- "Reading attribute: Cluster=0x%04X_%04X Endpoint=%x AttributeId=0x%04X_%04X (expanded=%d)"
- "T@\"NSObject<OS_dispatch_queue>\",&,V_chipWorkQueue"
- "Vv32@0:8@\"NSUUID\"16@?<v@?@\"NSNumber\">24"
- "Vv32@0:8@\"NSUUID\"16@?<v@?@\"NSUUID\">24"
- "Vv32@0:8@\"NSUUID\"16@?<v@?B>24"
- "Vv32@0:8@16@?24"
- "Write Version mismatch for Endpoint %x, Cluster 0x%04X_%04X"
- "bytesStaged <= sizeof(stagingBuf)"
- "deviceController:controllerNodeIDWithReply:"
- "deviceController:getIsRunningWithReply:"
- "deviceController:getUniqueIdentifierWithReply:"
- "readAttributeEventListWithClusterStateCache:endpoint:queue:completion:"
- "readAttributeEventListWithCompletion:"
- "readAttributeEventListWithParams:"
- "readAttributeMaxPreRollBufferSizeWithClusterStateCache:endpoint:queue:completion:"
- "readAttributeMaxPreRollBufferSizeWithCompletion:"
- "readAttributeMaxPreRollBufferSizeWithParams:"
- "sizeof(value) <= gEmberAttributeIOBufferSpan.size()"
- "src/app/reporting/Read-Ember.cpp"
- "src/lib/support/BufferReader.cpp"
- "subscribeAttributeEventListWithParams:subscriptionEstablished:reportHandler:"
- "subscribeAttributeMaxPreRollBufferSizeWithParams:subscriptionEstablished:reportHandler:"
- "v16@?0@\"NSDate\"8"
- "v16@?0@\"NSNumber\"8"
- "v16@?0Q8"

```
