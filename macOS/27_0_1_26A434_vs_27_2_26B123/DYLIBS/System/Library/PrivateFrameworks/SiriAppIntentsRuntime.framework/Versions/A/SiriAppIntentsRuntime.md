## SiriAppIntentsRuntime

> `/System/Library/PrivateFrameworks/SiriAppIntentsRuntime.framework/Versions/A/SiriAppIntentsRuntime`

```diff

-3600.82.29.0.0
-  __TEXT.__text: 0x85f3c
-  __TEXT.__objc_methlist: 0x404
-  __TEXT.__const: 0x29a0
-  __TEXT.__cstring: 0x1681
-  __TEXT.__constg_swiftt: 0xd7c
-  __TEXT.__swift5_typeref: 0x1455
-  __TEXT.__swift5_reflstr: 0xd43
-  __TEXT.__swift5_fieldmd: 0x9a8
-  __TEXT.__oslogstring: 0x359d
-  __TEXT.__swift5_builtin: 0x3c
-  __TEXT.__swift5_types: 0xbc
-  __TEXT.__swift_as_entry: 0x214
-  __TEXT.__swift_as_ret: 0x1d0
-  __TEXT.__swift_as_cont: 0x374
-  __TEXT.__swift5_proto: 0x104
-  __TEXT.__swift5_capture: 0x180c
-  __TEXT.__swift5_assocty: 0x98
-  __TEXT.__swift5_protos: 0x4
+3605.17.1.0.0
+  __TEXT.__text: 0x9d940
+  __TEXT.__objc_methlist: 0x464
+  __TEXT.__const: 0x3810
+  __TEXT.__cstring: 0x1861
+  __TEXT.__constg_swiftt: 0x10dc
+  __TEXT.__swift5_typeref: 0x1aa7
+  __TEXT.__swift5_reflstr: 0xeea
+  __TEXT.__swift5_fieldmd: 0xc84
+  __TEXT.__oslogstring: 0x3ead
+  __TEXT.__swift5_builtin: 0x50
+  __TEXT.__swift5_assocty: 0xe0
+  __TEXT.__swift5_proto: 0x1ac
+  __TEXT.__swift5_types: 0x104
+  __TEXT.__swift_as_entry: 0x26c
+  __TEXT.__swift_as_ret: 0x210
+  __TEXT.__swift_as_cont: 0x408
+  __TEXT.__swift5_capture: 0x1b4c
+  __TEXT.__swift5_protos: 0x8
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x1ca8
-  __TEXT.__eh_frame: 0x5100
+  __TEXT.__unwind_info: 0x2280
+  __TEXT.__eh_frame: 0x5ee8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x178
-  __DATA_CONST.__objc_classlist: 0x80
+  __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3f8
+  __DATA_CONST.__objc_selrefs: 0x418
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x4488
-  __AUTH_CONST.__objc_const: 0xee0
-  __AUTH_CONST.__auth_got: 0x17e8
-  __AUTH_CONST.__auth_ptr: 0x6e8
-  __AUTH.__objc_data: 0xa0
-  __AUTH.__data: 0x6c8
-  __DATA.__data: 0x8a8
-  __DATA.__bss: 0x1400
-  __DATA.__common: 0x90
-  __DATA_DIRTY.__objc_data: 0x9c0
-  __DATA_DIRTY.__data: 0xd38
+  __AUTH_CONST.__const: 0x5058
+  __AUTH_CONST.__objc_const: 0x1128
+  __AUTH_CONST.__auth_got: 0x1980
+  __AUTH_CONST.__auth_ptr: 0x7e0
+  __AUTH.__objc_data: 0xf0
+  __AUTH.__data: 0x900
+  __DATA.__data: 0xbe8
+  __DATA.__bss: 0x2880
+  __DATA.__common: 0xa0
+  __DATA_DIRTY.__objc_data: 0xa38
+  __DATA_DIRTY.__data: 0xf78
   __DATA_DIRTY.__bss: 0xb80
-  __DATA_DIRTY.__common: 0x100
+  __DATA_DIRTY.__common: 0x128
   - /System/Library/Frameworks/Combine.framework/Versions/A/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3003
-  Symbols:   172
-  CStrings:  340
+  Functions: 3605
+  Symbols:   180
+  CStrings:  380
 
Symbols:
+ _NSProcessInfoPowerStateDidChangeNotification
+ _NSProcessInfoThermalStateDidChangeNotification
+ _OBJC_CLASS_$_NSProcessInfo
+ _swift_getEnumCaseMultiPayload
+ _swift_makeBoxUnique
+ _swift_storeEnumTagMultiPayload
+ _swift_weakDestroy
+ _swift_weakInit
+ _swift_weakLoadStrong
- _OBJC_CLASS_$_AFConnection
CStrings:
+ "AFSettingsConnection"
+ "DeviceThermalNotificationHandler: kind=streamEnded"
+ "DeviceThermalNotificationHandler: streaming thermal transitions, seeded=%ld"
+ "DeviceThermalStateRecorder: started observing thermal transitions"
+ "Failed to encode device thermal state: %@"
+ "Failed to fetch session events (framed): %@"
+ "Failed to resolve most recent session: %@"
+ "FetchMostRecentSessionServerTimeoutSeconds"
+ "Fetching session events (framed) for %s from %s until %s"
+ "Fetching session events (json) for %s from %s until %s"
+ "Most recent session resolved: %s from %s to %s"
+ "MostRecentSessionResolver: all events for session %s were undecodable; skipping candidate"
+ "MostRecentSessionResolver: every event in slice failed to decode (%ld); first error: %s"
+ "MostRecentSessionResolver: skipped %ld undecodable event(s) in slice"
+ "No recent Siri session found within the searched lookback"
+ "Releasing the AFSettingsConnection injection session."
+ "Requesting events for %s from %s until %s."
+ "Resolving most recent session withinLast %fs"
+ "SearchAgentHydrationEventProto"
+ "Server-side timeout (%fs) fired for fetchMostRecentSession"
+ "SiriTrajectoryInstrumentationEvent"
+ "Starting to listen for SearchAgent HydrationEventProto events."
+ "Starting to listen for SiriTrajectoryInstrumentationEvent events."
+ "Transcript.Payload"
+ "XPCServer: Failed to decode SearchAgentProtoHydrationEvent: %@. InteractionId: %s"
+ "XPCServer: Failed to decode SiriTrajectoryInstrumentationEvent proto: %@. InteractionId: %s"
+ "XPCServer: SearchAgent HydrationEvent missing sessionID. Skipping event."
+ "XPCServer: Skipping SearchAgent HydrationEventProto event with empty protoBytes."
+ "XPCServer: Skipping SiriTrajectoryInstrumentationEvent event with empty protoBinaryData."
+ "com.apple.siriappintentsd.most-recent-session-resolve"
+ "fetchDeviceThermalState(forRequestID:from:to:with:)"
+ "fetchDeviceThermalState: no recorded sample for requestID=%s"
+ "fetchDeviceThermalState: requestID=%s thermalLevel=%ld lowPowerMode=%{bool}d"
+ "listenSearchAgentHydrationEventProto: kind=streamEnded"
+ "listenSiriTrajectoryInstrumentationEvent: kind=%s — dropping rather than scoping to interactionId (rdar://182856486)"
+ "listenSiriTrajectoryInstrumentationEvent: kind=streamEnded"
+ "missingSessionID"
+ "protoBinaryData"
+ "rawPayload"
+ "requestEvents(for:from:until:with:)"
+ "resolveMostRecentSessionOffCooperativePool(withinLast:fetch:fetchSession:)"
+ "retrieveSearchAgentHydration: kind=summary matched=%ld total=%ld sessionID=%s"
+ "retrieveSessionResumptionEventBundle: kind=summary matched=%ld yielded=%ld total=%ld embeddedEvents=%ld sessionID=%s"
+ "retrieveSiriTrajectoryInstrumentationEvent: kind=summary matched=%ld emptyIDs=%ld missingSessionID=%ld total=%ld sessionID=%s"
- "AFConnection ends the session."
- "Fetching session events for %s from %s until %s"
- "Requesting events for %s until %s."
- "requestEvents(for:with:)"
```
