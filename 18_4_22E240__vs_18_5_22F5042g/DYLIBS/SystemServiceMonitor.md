## SystemServiceMonitor

> `/System/Library/PrivateFrameworks/SystemServiceMonitor.framework/SystemServiceMonitor`

```diff

-3.100.13.0.0
-  __TEXT.__text: 0x37590
-  __TEXT.__auth_stubs: 0xe80
+3.120.7.0.0
+  __TEXT.__text: 0x3c73c
+  __TEXT.__auth_stubs: 0xeb0
   __TEXT.__objc_methlist: 0x104
-  __TEXT.__const: 0x5084
-  __TEXT.__cstring: 0x1143
-  __TEXT.__oslogstring: 0x78e
-  __TEXT.__swift5_typeref: 0x1264
-  __TEXT.__swift5_capture: 0x230
-  __TEXT.__swift5_reflstr: 0x6ae
-  __TEXT.__swift5_assocty: 0x140
-  __TEXT.__constg_swiftt: 0x15d8
-  __TEXT.__swift5_builtin: 0x78
-  __TEXT.__swift5_mpenum: 0x38
-  __TEXT.__swift5_fieldmd: 0xef4
-  __TEXT.__swift5_protos: 0x44
-  __TEXT.__swift5_proto: 0x558
-  __TEXT.__swift5_types: 0x19c
-  __TEXT.__swift_as_entry: 0x1e8
-  __TEXT.__swift_as_ret: 0x1d4
-  __TEXT.__unwind_info: 0x1738
-  __TEXT.__eh_frame: 0x3420
+  __TEXT.__cstring: 0x1193
+  __TEXT.__const: 0x512c
+  __TEXT.__constg_swiftt: 0x1428
+  __TEXT.__swift5_typeref: 0x10cd
+  __TEXT.__swift5_fieldmd: 0xe6c
+  __TEXT.__swift5_types: 0x1a0
+  __TEXT.__swift5_capture: 0x2b0
+  __TEXT.__swift5_reflstr: 0x64e
+  __TEXT.__oslogstring: 0xb5e
+  __TEXT.__swift5_protos: 0x18
+  __TEXT.__swift5_proto: 0x588
+  __TEXT.__swift_as_entry: 0x154
+  __TEXT.__swift_as_ret: 0x14c
+  __TEXT.__swift5_assocty: 0x108
+  __TEXT.__swift5_builtin: 0x3c
+  __TEXT.__swift5_mpenum: 0x18
+  __TEXT.__unwind_info: 0x1828
+  __TEXT.__eh_frame: 0x33e0
   __TEXT.__objc_classname: 0x17
   __TEXT.__objc_methname: 0x13f
   __TEXT.__objc_methtype: 0xad
-  __DATA_CONST.__got: 0xf0
+  __DATA_CONST.__got: 0x110
   __DATA_CONST.__const: 0x118
   __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xa0
   __DATA_CONST.__objc_protorefs: 0x10
-  __AUTH_CONST.__auth_got: 0x740
-  __AUTH_CONST.__auth_ptr: 0x348
-  __AUTH_CONST.__const: 0x2eb8
-  __AUTH_CONST.__objc_const: 0x10c8
-  __AUTH.__objc_data: 0xa0
-  __AUTH.__data: 0xe68
-  __DATA.__data: 0xd88
-  __DATA.__bss: 0xa870
+  __AUTH_CONST.__auth_got: 0x758
+  __AUTH_CONST.__auth_ptr: 0x2c8
+  __AUTH_CONST.__const: 0x2dd8
+  __AUTH_CONST.__objc_const: 0x1000
+  __AUTH.__objc_data: 0xf0
+  __AUTH.__data: 0x1158
+  __DATA.__data: 0xc88
+  __DATA.__bss: 0xb770
   __DATA.__common: 0x78
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/RemoteServiceDiscovery.framework/RemoteServiceDiscovery

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 1776
-  Symbols:   185
-  CStrings:  181
+  Functions: 1811
+  Symbols:   195
+  CStrings:  193
 
Symbols:
+ _free
+ _malloc
+ _objc_release_x24
+ _objc_release_x25
+ _swift_cvw_initEnumMetadataMultiPayloadWithLayoutString
+ _swift_cvw_multiPayloadEnumGeneric_destructiveInjectEnumTag
+ _swift_cvw_multiPayloadEnumGeneric_getEnumTag
+ _swift_storeEnumTagMultiPayload
- _objc_release_x23
CStrings:
+ "Cannot start connecting since session is not activated"
+ "Couldn't connect to the daemon after retries. The state behavior might be unexpected (state: %s."
+ "Failed to process the query."
+ "Failed to send message synchrnously. "
+ "Failed to start a new connection. %s"
+ "Gave up retrying to connect sicne the core has been deactivated."
+ "Session has already activated"
+ "Session is not connected. "
+ "SessionUUIDString"
+ "Start a new connecting session in an ongoing connection."
+ "SystemServiceMonitor/ReportSessionCore.swift"
+ "Unexpected 'Ping' query received on the Mach session"
+ "[✅] Successfully reported the cached state. %s"
+ "[🔴] Failed to connect to the daemon. Will retry in %fs. Error: %@."
+ "[🔴] Failed to parse the Query object from the event stream. Error: %@"
+ "[🔴] Failed to parse the query from the xpc message. Error: %s"
+ "[🔴] Failed to reconnect and report the cached state. Error: %@"
+ "[🔴] XPC Connection lost."
+ "[🟡] Ignore the XPC unavailable handler because it's not for the current session"
+ "[🟡] Received unexpected 'Ping' query on the Mach session."
+ "[🟡] Received unsupported query messages. 'Ping' query is the only supported event on the event stream."
+ "[🟡] Session is not connected, waiting for the connected state."
+ "[🟡] Session is not within the specified timeout. Remove the waiting operation from the waiting queue."
+ "[🟢] Session is connected, unblock the waiting continuations."
+ "_TtC20SystemServiceMonitor26QueryEventStreamConnection"
+ "_TtC20SystemServiceMonitor27ReportMachSessionConnection"
+ "_connectionState"
+ "connectedContinuations"
+ "connectionUnavailableHandler"
+ "currentSessionUUID"
+ "incomingQueryHandler"
+ "unavailableReason"
+ "waitUntilConnected(within:)"
+ "⚙️ transitioning to state: %s"
+ "⛓️\u200d💥 Report Client Disconnected. Will try to reconnect and report the latest state upon reestablishing the connection."
+ "📨 Received query (%s)"
+ "🔗 Connecting to the daemon (connection UUID: %s)"
- "Failed to send message synchrnously because "
- "Handling connection lost"
- "Ignoring the connection lost handling since the previous connection is already cancelled."
- "RealCore: activating..."
- "SessionUUID"
- "SystemServiceMonitor/ReportSession.swift"
- "SystemServiceMonitor/ReportSessionState.swift"
- "The communication to the daemon is not established"
- "The session has already been activated"
- "The session has not been activated"
- "[🔴] Failed to connect to the daemon. Will retry. Error: %@."
- "[🔴] Failed to parse the Query object from the XPC event. Error: %@"
- "[🟡] Received 'Ping' query related to outdated session. Ignore this 'Ping' query."
- "_TtCC20SystemServiceMonitor13ReportSession26QueryEventStreamConnection"
- "_TtCC20SystemServiceMonitor13ReportSession27ReportMachSessionConnection"
- "connectionState"
- "connectionUuid"
- "getServiceState"
- "onConnectionLost"
- "onMessageReceived"
- "reportSessionCore"
- "⛭ Running..."
- "⛭ Transitioning to %s"
- "📨 Received stateQuery"
- "🔗 Trying to connect to the daemon (sessionId: %s)"

```
