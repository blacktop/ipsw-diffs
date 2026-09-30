## SystemServiceMonitor

> `/System/Library/PrivateFrameworks/SystemServiceMonitor.framework/SystemServiceMonitor`

```diff

-3.100.6.0.0
-  __TEXT.__text: 0x21754
-  __TEXT.__auth_stubs: 0xbc0
+3.100.13.0.0
+  __TEXT.__text: 0x37590
+  __TEXT.__auth_stubs: 0xe80
   __TEXT.__objc_methlist: 0x104
-  __TEXT.__const: 0x4414
-  __TEXT.__cstring: 0xae3
-  __TEXT.__swift5_typeref: 0xfde
-  __TEXT.__swift5_capture: 0xd4
-  __TEXT.__swift5_reflstr: 0x462
-  __TEXT.__swift5_assocty: 0x110
-  __TEXT.__constg_swiftt: 0x1270
-  __TEXT.__swift5_builtin: 0x64
-  __TEXT.__swift5_mpenum: 0x30
-  __TEXT.__swift5_fieldmd: 0xc6c
-  __TEXT.__swift5_protos: 0x48
-  __TEXT.__swift5_proto: 0x47c
-  __TEXT.__swift5_types: 0x168
-  __TEXT.__swift_as_entry: 0x144
-  __TEXT.__swift_as_ret: 0x11c
-  __TEXT.__oslogstring: 0x109
-  __TEXT.__unwind_info: 0xfe0
-  __TEXT.__eh_frame: 0x1de8
+  __TEXT.__const: 0x5084
+  __TEXT.__cstring: 0x1143
+  __TEXT.__oslogstring: 0x78e
+  __TEXT.__swift5_typeref: 0x1264
+  __TEXT.__swift5_capture: 0x230
+  __TEXT.__swift5_reflstr: 0x6ae
+  __TEXT.__swift5_assocty: 0x140
+  __TEXT.__constg_swiftt: 0x15d8
+  __TEXT.__swift5_builtin: 0x78
+  __TEXT.__swift5_mpenum: 0x38
+  __TEXT.__swift5_fieldmd: 0xef4
+  __TEXT.__swift5_protos: 0x44
+  __TEXT.__swift5_proto: 0x558
+  __TEXT.__swift5_types: 0x19c
+  __TEXT.__swift_as_entry: 0x1e8
+  __TEXT.__swift_as_ret: 0x1d4
+  __TEXT.__unwind_info: 0x1738
+  __TEXT.__eh_frame: 0x3420
   __TEXT.__objc_classname: 0x17
   __TEXT.__objc_methname: 0x13f
   __TEXT.__objc_methtype: 0xad
-  __DATA_CONST.__got: 0xd0
-  __DATA_CONST.__const: 0x108
-  __DATA_CONST.__objc_classlist: 0x50
+  __DATA_CONST.__got: 0xf0
+  __DATA_CONST.__const: 0x118
+  __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xa0
   __DATA_CONST.__objc_protorefs: 0x10
-  __AUTH_CONST.__auth_got: 0x5e0
-  __AUTH_CONST.__auth_ptr: 0x300
-  __AUTH_CONST.__const: 0x21a8
-  __AUTH_CONST.__objc_const: 0x1130
-  __AUTH.__data: 0xac0
-  __DATA.__data: 0x9c0
-  __DATA.__bss: 0x8c40
-  __DATA.__common: 0x48
+  __AUTH_CONST.__auth_got: 0x740
+  __AUTH_CONST.__auth_ptr: 0x360
+  __AUTH_CONST.__const: 0x2eb8
+  __AUTH_CONST.__objc_const: 0x10c8
+  __AUTH.__objc_data: 0xa0
+  __AUTH.__data: 0xe68
+  __DATA.__data: 0xd88
+  __DATA.__bss: 0xa870
+  __DATA.__common: 0x78
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/PrivateFrameworks/RemoteServiceDiscovery.framework/RemoteServiceDiscovery
+  - /System/Library/PrivateFrameworks/RemoteXPC.framework/RemoteXPC
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftCore.dylib

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 1308
-  Symbols:   164
-  CStrings:  123
+  Functions: 1776
+  Symbols:   185
+  CStrings:  181
 
Symbols:
+ __swift_stdlib_bridgeErrorToNSError
+ _bzero
+ _objc_release_x21
+ _objc_release_x22
+ _objc_release_x27
+ _objc_retain_x8
+ _remote_device_copy_device_with_name
+ _remote_device_copy_service
+ _swift_arrayDestroy
+ _swift_arrayInitWithCopy
+ _swift_arrayInitWithTakeBackToFront
+ _swift_arrayInitWithTakeFrontToBack
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_enumFn_getEnumTag
+ _swift_cvw_initStructMetadataWithLayoutString
+ _swift_cvw_initWithCopy
+ _swift_cvw_initWithTake
+ _swift_cvw_initializeBufferWithCopyOfBuffer
+ _swift_release_n
+ _swift_updateClassMetadata2
+ _xpc_array_create
+ _xpc_array_get_count
+ _xpc_array_get_value
+ _xpc_dictionary_get_string
+ _xpc_remote_connection_activate
+ _xpc_remote_connection_cancel
+ _xpc_remote_connection_create_with_remote_service
+ _xpc_remote_connection_send_message_with_reply
+ _xpc_remote_connection_set_event_handler
- _objc_release_x24
- _objc_release_x26
- _objc_retain_x19
- _objc_retain_x21
- _swift_deallocPartialClassInstance
- _swift_enumFn_getEnumTag
- _swift_generic_assignWithCopy
- _swift_generic_assignWithTake
- _swift_generic_destroy
- _swift_generic_initWithCopy
- _swift_generic_initWithTake
- _swift_generic_initializeBufferWithCopyOfBuffer
- _swift_initStructMetadataWithLayoutString
- _xpc_connection_activate
- _xpc_connection_create_from_endpoint
- _xpc_connection_send_message_with_reply
- _xpc_connection_set_event_handler
- _xpc_dictionary_set_uuid
CStrings:
+ " but the expected service is "
+ "Adapater received event for %s but the expected service is %s"
+ "Both of the mach service name and the XPC endpoint are missing"
+ "Cancel the previous XPC session before retry."
+ "Didn't get the expected response type. Error: "
+ "Dupilcated Service Error: the service already exists"
+ "Failed to build up the connection due to "
+ "Failed to convert the request to a XPC object. "
+ "Failed to create the XPC session due to: "
+ "Failed to create the response xpc for the ServiceList response"
+ "Failed to send request due to "
+ "Failed to send the report due to an error: %@"
+ "Ignoring the connection lost handling since the previous connection is already cancelled."
+ "Received an event for service (%s) but that service doesn't register event handler."
+ "Received error reply. Error message: "
+ "Remote connection has not been established"
+ "SSMEncodedMessage"
+ "SSMEncodedResponse"
+ "SSMNotificationData"
+ "Service Session Not Ready Error: not ready for receiving service report or proceeding other communications"
+ "Service connection doesn't have an adapter attached"
+ "ServiceList response must have the original XPC provided"
+ "SystemServiceMonitor/ServiceMonitor.swift"
+ "The SSM remote service is not found on the device ("
+ "The XPC session doesn't exist. Already been closed?"
+ "The XPC session has already been established"
+ "The handler bucket should exist"
+ "The mach session doesn't exist. Forget to setup the connection?"
+ "The original xpc should always be nil when encoding ServiceInfo"
+ "The remote XPC session doesn't exist. Already been closed?"
+ "The remote device ("
+ "The service wait response should only contains the service being waited for, but got "
+ "Trying to register event handler for "
+ "Unsuorted message type, it must be a Request"
+ "[🔴] Failed to connect to the daemon. Will retry. Error: %@."
+ "[🔴] Failed to parse the Query object from the XPC event. Error: %@"
+ "[🔴] Failed to parse the notification from the xpc message. Error: %@"
+ "[🔴] Failed to send the Ping query response. Error: %@"
+ "[🔴] Unexpected message received on the notification channel for mach XPC request connection"
+ "[🔴] failed to send the 'Ping' report. Connection failed. Error: %@"
+ "[🔴] 🔔 Notification: Failed to parse the notification from the xpc_object_t. Error: %@"
+ "[🔴] 🔔 Notification: failed to send the 'StateUpdate' response. Error: %s"
+ "[🔴] 🔔 Notification: received error remote event from the daemon."
+ "[🔴] 🔔 Notification: unexpected XPC."
+ "[🟡] Received 'Ping' query related to outdated session. Ignore this 'Ping' query."
+ "[🟢] 🔔 Monitor Event: received event: %s on monitor: %s"
+ "_TtC20SystemServiceMonitor14ServiceMonitor"
+ "_TtC20SystemServiceMonitor16BaseEventAdapter"
+ "_TtC20SystemServiceMonitor17MuxedEventAdapter"
+ "_TtCC20SystemServiceMonitor17MuxedEventAdapterP33_D54473D7653BF912F1B4E706A0B5595018EventHandlerBucket"
+ "_eventAdapter"
+ "cachedState"
+ "com.apple.systemservicemonitor.request.remote"
+ "connectionUuid"
+ "currentState"
+ "duplicatedService"
+ "eventHandler"
+ "handlerBucketMap"
+ "handlerMap"
+ "monitorIdentifier"
+ "onStateChange"
+ "onUnavailable"
+ "registrationIdentifier"
+ "remoteConnection"
+ "remoteDeviceName"
+ "requestConnection"
+ "service"
+ "serviceIdentifier"
+ "serviceSessionNotReady"
+ "serviceUnavailable"
+ "services"
+ "state"
+ "xpcEndpoint"
+ "🔌 Base Adapter: the %s handler registration status: %{bool}d"
+ "🔌 Base Adapter: trying to register an Event Handler for %s"
+ "🔌 Muxed Adapter: failed to remove the handler, doesn't contain the handler bucket for service: %s"
+ "🔌 Muxed Adapter: successfully registered an Event Handler for %s"
+ "🔌 Muxed Adapter: successfully removed an Event Handler for %s"
+ "🔌 Muxed Adapter: trying to register an Event Handler for %s"
+ "🔗 Trying to connect to the daemon (sessionId: %s)"
- "Cannot create the request XPC session"
- "Failed to pack request into XPC object"
- "SSMQueryResponseData"
- "SSMReportResponseData "
- "SSMRequestResponseData "
- "SystemServiceMonitor/Message.swift"
- "SystemServiceMonitor/ReportClient.swift"
- "SystemServiceMonitor/ReportSessionConnection.swift"
- "The mach session doesn't exist"
- "The mach session doesn't exist. You may forget to call the connect() method"
- "The xpc connection is already established"
- "The xpc connection is not established"
- "_TtC20SystemServiceMonitor10CodableXPC"
- "_TtC20SystemServiceMonitor21ServiceMachConnection"
- "endpoint"
- "queue"
- "remoteDevice"
- "xpc"
- "xpcConnection"
- "xpcObject"
- "🔗 Trying to connect to the daemon..."
- "🧩 Using the localy built framework."

```
