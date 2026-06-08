## WirelessDiagnostics

> `/System/Library/PrivateFrameworks/WirelessDiagnostics.framework/WirelessDiagnostics`

```diff

 998.0.0.0.0
-  __TEXT.__text: 0x33fa8
-  __TEXT.__auth_stubs: 0xe30
+  __TEXT.__text: 0x34070
   __TEXT.__init_offsets: 0x14
   __TEXT.__objc_methlist: 0x154
-  __TEXT.__gcc_except_tab: 0x30d4
-  __TEXT.__const: 0x15a3
-  __TEXT.__cstring: 0xbb7
-  __TEXT.__oslogstring: 0x1728
-  __TEXT.__unwind_info: 0x1ab8
-  __TEXT.__objc_classname: 0x47
-  __TEXT.__objc_methname: 0x4b0
-  __TEXT.__objc_methtype: 0x129
-  __TEXT.__objc_stubs: 0x380
-  __DATA_CONST.__got: 0x1a8
+  __TEXT.__gcc_except_tab: 0x2fec
+  __TEXT.__const: 0x1583
+  __TEXT.__cstring: 0xbad
+  __TEXT.__oslogstring: 0x15d7
+  __TEXT.__unwind_info: 0x1c00
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x418
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__weak_got: 0x8
   __DATA_CONST.__objc_selrefs: 0x1a8
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x728
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x1bc8
   __AUTH_CONST.__cfstring: 0x140
   __AUTH_CONST.__objc_const: 0x2b0
+  __AUTH_CONST.__weak_auth_got: 0x28
+  __AUTH_CONST.__auth_got: 0x720
   __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0x8
   __DATA.__common: 0x9

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprotobuf-lite.dylib
   - /usr/lib/libprotobuf.dylib
-  UUID: 467380D9-17DA-3409-A6B3-95A8D10D70A9
-  Functions: 1407
-  Symbols:   1444
-  CStrings:  326
+  UUID: 0DA644E0-4C73-35C3-B896-8588C7B331D0
+  Functions: 1424
+  Symbols:   1448
+  CStrings:  240
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_release_x24
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x8
- ___cxa_rethrow
- _objc_retainAutoreleasedReturnValue
CStrings:
+ "SetObserverConfiguration configured successfully"
+ "SetObserverConfiguration failed: %s"
+ "XPC connection failure"
+ "client.submitter:Sending done with metrics message for Trigger(cid=0x%x, trid=0x%x, sid=%u)"
+ "client.submitter:Sending metric submission message for metric 0x%x, profid 0x%x, Trigger(cid=0x%x, trid=0x%x, sid=%u)"
+ "client.submitter:Unable to send finished submission message because AWDServerFacade is not valid."
+ "client.submitter:Unable to send metric because AWDServerFacade is not valid."
+ "client.submitter:Unable to send trigger message because AWDServerFacade is not valid."
+ "client.trigger:\t- PROFILE 0x%x TRIGGER 0x%x"
+ "client.trigger: The following are Trigger IDs that component 0x%x expects:"
+ "client.trigger:CCFG for cid 0x%x has # of profiles: %d"
+ "client.trigger:Got profile with no id!"
+ "client.trigger:Random sample for 0x%x %s"
+ "client.trigger:Unable to set configuration because AWDServerFacade is no longer valid."
+ "client:CoreAnalytics shim: Error! getMetadataBase: XpcConnection is NULL"
+ "client:Error! sendMessage: XpcConnection is NULL"
+ "client:Failed to parse component configuration."
+ "client:Failed to xpc create connection."
+ "client:Got an unkown message from AWDD!"
+ "client:Got control message of type %d"
+ "client:In switch branch for pii/location message msg. cid=0x%x collectPII is %d, collectLocation is %d, shim is %d"
+ "client:Received Timer(tid=0x%x) notification message"
+ "client:Sending Trigger(cid=0x%x, trid=0x%x, sid=%u) to component: 0x%x"
+ "client:Sending component configuration to component: 0x%x"
+ "client:Sending message to register with dcid %d, component 0x%x, needsconfig: %d"
+ "client:XPC Connection invalidated; possibly a sandbox block?"
+ "client:libawd got message of type %d"
+ "client:xpc conenction NULL while registering as component 0x%x"
+ "core:==== BEGIN CLIENT STATE LOG ===="
+ "core:==== END CLIENT STATE LOG ===="
+ "core:Added an observer of AWDD startup notification"
+ "core:Component is 0x%x"
+ "core:Configuration not ready yet; buffering a metric until we get it (%zd total buffered)"
+ "core:CoreAnalytics shim: No baseline metadata returned (processing metric with cid 0x%x)"
+ "core:DeviceConfigurationId changing from %d to %d; marking clients as needing config"
+ "core:Dropping trigger for metric 0x%x"
+ "core:Got Unexpected PII/Location callback for component 0x%x (no component config!)"
+ "core:Got Unexpected Trigger(cid=0x%x, trid=0x%x, sid=%u) (no component config!)"
+ "core:Got Unexpected trigger 0x%x from component 0x%x"
+ "core:Got expected trigger 0x%x from component 0x%x"
+ "core:Got trigger metric 0x%x; Metric: %zd bytes [%s]"
+ "core:Sending a trigger for metric 0x%x"
+ "core:Timer(tid=0x%x) notification to clients of cid 0x%x"
+ "core:sendExpectedMetric did not find a submission id queue for metric 0x%x"
+ "core:setExpectedMetricsForTrigger found %zd queriable metrics for trigger 0x%x"
+ "logging-metric:AWDLoggingMetric: Got profile 0x%x with no trigger id."
+ "logging-metric:AWDLoggingMetric: Got profile with no profile id."
+ "logging-metric:Calling callback on Logging metric for Trigger(cid=0x%x, trid=0x%x, sid=%u)"
+ "logging-metric:Did not find a QueriableMetricCallbackBlockWithParameters for Logging."
+ "logging-metric:Found Log in configuration"
+ "logging-metric:Log's param #%d %s:%s"
+ "metric.buffer:\t\t- METRIC 0x%x: Buffer last %llu+%llu seconds"
+ "metric.buffer:\t\t- METRIC 0x%x: Buffer most recent %u metrics."
+ "metric.buffer:\t\t- METRIC 0x%x: Buffer most recent metric."
+ "metric.buffer:\t\t- METRIC 0x%x: UNKNOWN BUFFERING TYPE (%d)"
+ "metric.buffer:\t- TRIGGER: 0x%x PROFILE: 0x%x"
+ "metric.buffer:  - Metric: 0x%x %zd bytes (%llu.%03u seconds since epoch)"
+ "metric.buffer:About to erase metric with time %llums. Size is %zd; fMaxCount is %u"
+ "metric.buffer:Added a new metricContainer into buffer. State of the buffer after the add (may have too many metrics): "
+ "metric.buffer:Could not find buffer for metric 0x%x"
+ "metric.buffer:Could not find buffering info for Trigger(cid=0x%x, trid=0x%x, sid=%u)in timer function."
+ "metric.buffer:Could not find buffering info for metric 0x%x in timer function"
+ "metric.buffer:Could not find buffering info for trigger 0x%x"
+ "metric.buffer:Could not find profile info for Trigger(cid=0x%x, trid=0x%x, sid=%u)in timer function."
+ "metric.buffer:Deleted old metrics. State of the buffer after the delete (should be correct): "
+ "metric.buffer:Dispatching trigger 0x%x for profile 0x%x to metric 0x%x after %llu seconds (%llu ns)."
+ "metric.buffer:Found buffering info for metric 0x%x: callback"
+ "metric.buffer:Found buffering info for metric 0x%x: most recent"
+ "metric.buffer:Found buffering info for metric 0x%x: num before trigger"
+ "metric.buffer:Found buffering info for metric 0x%x: time before trigger"
+ "metric.buffer:Got unknown buffering info for metric 0x%x, Trigger(cid=0x%x, trid=0x%x, sid=%u)"
+ "metric.buffer:In _trigger with trigger 0x%x"
+ "metric.buffer:Not able to buffer metric 0x%x"
+ "metric.buffer:The following are how much to buffer each metric for a given trigger:"
+ "metric.buffer:Unable to allocate new metric buffer."
+ "metric.buffer:Unable to insert new buffer info into buffer info map for trigger 0x%x, metric 0x%x"
+ "metric.buffer:fMetricSubmitter Null."
+ "metric.buffer:pushMetricToDaemon: MetricSubmitter Null."
+ "metric.buffer:pushTriggerToDaemon: fMetricSubmitter Null."
+ "metric:Creating a metric container for metric id: 0x%x"
+ "metric:In postMetricWithId:object: for mid 0x%lx: unsupported NSObject type! (Got '%s')"
+ "server.conn:Calling callback on 24h-timer: %s"
+ "server.conn:Calling callback on metric: 0x%x"
+ "server.conn:No queriable callback for metric id 0x%x"
+ "server.conn:No queriable callback for metric id 0x%x for analytics"
- "#E SetObserverConfiguration failed: %s"
- "#E XPC connection failure"
- "#I SetObserverConfiguration configured successfully"
- ".cxx_destruct"
- "/var"
- "@\"PBCodable\""
- "@16@0:8"
- "@20@0:8I16"
- "@24@0:8I16B20"
- "AWDMetricContainer"
- "AWDMetricManager"
- "AWDObserver"
- "AWDServerConnection"
- "B24@0:8@16"
- "B24@0:8@?16"
- "B28@0:8@?16I24"
- "B28@0:8I16@?20"
- "I"
- "I16@0:8"
- "No Key"
- "Q16@0:8"
- "T@\"PBCodable\",&,N,V_metric"
- "TI,R,N,V_metricId"
- "UTF8String"
- "_metric"
- "_metricId"
- "addObject:"
- "arrayWithCapacity:"
- "bytes"
- "client.submitter:#E Unable to send finished submission message because AWDServerFacade is not valid."
- "client.submitter:#E Unable to send metric because AWDServerFacade is not valid."
- "client.submitter:#E Unable to send trigger message because AWDServerFacade is not valid."
- "client.submitter:#I Sending done with metrics message for Trigger(cid=0x%x, trid=0x%x, sid=%u)"
- "client.submitter:#I Sending metric submission message for metric 0x%x, profid 0x%x, Trigger(cid=0x%x, trid=0x%x, sid=%u)"
- "client.trigger:#E Got profile with no id!"
- "client.trigger:#E Unable to set configuration because AWDServerFacade is no longer valid."
- "client.trigger:#I \t- PROFILE 0x%x TRIGGER 0x%x"
- "client.trigger:#I  The following are Trigger IDs that component 0x%x expects:"
- "client.trigger:#I Random sample for 0x%x %s"
- "client.trigger:#N CCFG for cid 0x%x has # of profiles: %d"
- "client:#D libawd got message of type %d"
- "client:#E CoreAnalytics shim: Error! getMetadataBase: XpcConnection is NULL"
- "client:#E Error! sendMessage: XpcConnection is NULL"
- "client:#E Failed to parse component configuration."
- "client:#E Failed to xpc create connection."
- "client:#E Got an unkown message from AWDD!"
- "client:#E XPC Connection invalidated; possibly a sandbox block?"
- "client:#E xpc conenction NULL while registering as component 0x%x"
- "client:#I Got control message of type %d"
- "client:#I In switch branch for pii/location message msg. cid=0x%x collectPII is %d, collectLocation is %d, shim is %d"
- "client:#I Received Timer(tid=0x%x) notification message"
- "client:#I Sending Trigger(cid=0x%x, trid=0x%x, sid=%u) to component: 0x%x"
- "client:#I Sending component configuration to component: 0x%x"
- "client:#I Sending message to register with dcid %d, component 0x%x, needsconfig: %d"
- "core:#D Added an observer of AWDD startup notification"
- "core:#D Dropping trigger for metric 0x%x"
- "core:#D sendExpectedMetric did not find a submission id queue for metric 0x%x"
- "core:#D setExpectedMetricsForTrigger found %zd queriable metrics for trigger 0x%x"
- "core:#E Got Unexpected PII/Location callback for component 0x%x (no component config!)"
- "core:#E Got Unexpected Trigger(cid=0x%x, trid=0x%x, sid=%u) (no component config!)"
- "core:#E Got Unexpected trigger 0x%x from component 0x%x"
- "core:#I ==== BEGIN CLIENT STATE LOG ===="
- "core:#I ==== END CLIENT STATE LOG ===="
- "core:#I Component is 0x%x"
- "core:#I Configuration not ready yet; buffering a metric until we get it (%zd total buffered)"
- "core:#I CoreAnalytics shim: No baseline metadata returned (processing metric with cid 0x%x)"
- "core:#I DeviceConfigurationId changing from %d to %d; marking clients as needing config"
- "core:#I Got expected trigger 0x%x from component 0x%x"
- "core:#I Got trigger metric 0x%x; Metric: %zd bytes [%s]"
- "core:#I Sending a trigger for metric 0x%x"
- "core:#I Timer(tid=0x%x) notification to clients of cid 0x%x"
- "core:#I setExpectedMetricsForTrigger found %zd queriable metrics for trigger 0x%x"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "dataWithBytes:length:"
- "description"
- "dictionaryWithCapacity:"
- "dictionaryWithObjects:forKeys:count:"
- "dictionaryWithObjectsAndKeys:"
- "errorWithDomain:code:userInfo:"
- "flushToQueue:block:"
- "getAWDTimestamp"
- "getComponentConfigurationParameters"
- "hasTimestamp"
- "immutableData"
- "init"
- "initWithComponentId:"
- "initWithComponentId:andBlockOnConfiguration:"
- "initWithDomain:code:userInfo:"
- "length"
- "logging-metric:#E AWDLoggingMetric: Got profile 0x%x with no trigger id."
- "logging-metric:#E AWDLoggingMetric: Got profile with no profile id."
- "logging-metric:#E Did not find a QueriableMetricCallbackBlockWithParameters for Logging."
- "logging-metric:#I Calling callback on Logging metric for Trigger(cid=0x%x, trid=0x%x, sid=%u)"
- "logging-metric:#I Found Log in configuration"
- "logging-metric:#I Log's param #%d %s:%s"
- "longLongValue"
- "metric"
- "metric.buffer:#D   - Metric: 0x%x %zd bytes (%llu.%03u seconds since epoch)"
- "metric.buffer:#D About to erase metric with time %llums. Size is %zd; fMaxCount is %u"
- "metric.buffer:#D Added a new metricContainer into buffer. State of the buffer after the add (may have too many metrics): "
- "metric.buffer:#D Deleted old metrics. State of the buffer after the delete (should be correct): "
- "metric.buffer:#E Could not find buffer for metric 0x%x"
- "metric.buffer:#E Could not find buffering info for Trigger(cid=0x%x, trid=0x%x, sid=%u)in timer function."
- "metric.buffer:#E Could not find buffering info for metric 0x%x in timer function"
- "metric.buffer:#E Could not find profile info for Trigger(cid=0x%x, trid=0x%x, sid=%u)in timer function."
- "metric.buffer:#E Not able to buffer metric 0x%x"
- "metric.buffer:#E Unable to allocate new metric buffer."
- "metric.buffer:#E Unable to insert new buffer info into buffer info map for trigger 0x%x, metric 0x%x"
- "metric.buffer:#E fMetricSubmitter Null."
- "metric.buffer:#E pushMetricToDaemon: MetricSubmitter Null."
- "metric.buffer:#E pushTriggerToDaemon: fMetricSubmitter Null."
- "metric.buffer:#I \t\t- METRIC 0x%x: Buffer last %llu+%llu seconds"
- "metric.buffer:#I \t\t- METRIC 0x%x: Buffer most recent %u metrics."
- "metric.buffer:#I \t\t- METRIC 0x%x: Buffer most recent metric."
- "metric.buffer:#I \t\t- METRIC 0x%x: UNKNOWN BUFFERING TYPE (%d)"
- "metric.buffer:#I \t- TRIGGER: 0x%x PROFILE: 0x%x"
- "metric.buffer:#I Could not find buffering info for trigger 0x%x"
- "metric.buffer:#I Dispatching trigger 0x%x for profile 0x%x to metric 0x%x after %llu seconds (%llu ns)."
- "metric.buffer:#I Found buffering info for metric 0x%x: callback"
- "metric.buffer:#I Found buffering info for metric 0x%x: most recent"
- "metric.buffer:#I Found buffering info for metric 0x%x: num before trigger"
- "metric.buffer:#I Found buffering info for metric 0x%x: time before trigger"
- "metric.buffer:#I Got unknown buffering info for metric 0x%x, Trigger(cid=0x%x, trid=0x%x, sid=%u)"
- "metric.buffer:#I In _trigger with trigger 0x%x"
- "metric.buffer:#I The following are how much to buffer each metric for a given trigger:"
- "metric:#E In postMetricWithId:object: for mid 0x%lx: unsupported NSObject type! (Got '%s')"
- "metric:#I Creating a metric container for metric id: 0x%x"
- "metricId"
- "newMetricContainerWithIdentifier:"
- "null"
- "numberWithBool:"
- "numberWithDouble:"
- "numberWithLongLong:"
- "numberWithUnsignedLongLong:"
- "objectForKey:"
- "postMetricWithId:"
- "postMetricWithId:boolValue:"
- "postMetricWithId:integerValue:"
- "postMetricWithId:numberValue:"
- "postMetricWithId:object:"
- "postMetricWithId:stringValue:"
- "postMetricWithId:unsignedIntegerValue:"
- "registerComponentParametersChangeCallback:"
- "registerConfigChangeCallback:"
- "registerQueriableMetric:callback:"
- "registerQueriableMetricCallback:forIdentifier:"
- "server.conn:#D Calling callback on 24h-timer: %s"
- "server.conn:#D Calling callback on metric: 0x%x"
- "server.conn:#I No queriable callback for metric id 0x%x"
- "server.conn:#I No queriable callback for metric id 0x%x for analytics"
- "setConfiguration:callback:"
- "setDelegate:queue:"
- "setMetric:"
- "setObject:forKey:"
- "setTimestamp:"
- "stringWithUTF8String:"
- "submitMetric:"
- "timestamp"
- "v16@0:8"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8Q16"
- "v28@0:8Q16B24"
- "v32@0:8@16@?24"
- "v32@0:8@16^{dispatch_queue_s=}24"
- "v32@0:8Q16@24"
- "v32@0:8Q16Q24"
- "v32@0:8Q16q24"
- "v32@0:8^{dispatch_queue_s=}16@?24"
- "writeTo:"

```
