## SiriAppIntentsRuntime

> `/System/Library/PrivateFrameworks/SiriAppIntentsRuntime.framework/Versions/A/SiriAppIntentsRuntime`

```diff

-3600.82.29.0.0
-  __TEXT.__text: 0x7e280
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
+3605.15.1.0.0
+  __TEXT.__text: 0x939d8
+  __TEXT.__objc_methlist: 0x448
+  __TEXT.__const: 0x3810
+  __TEXT.__cstring: 0x1861
+  __TEXT.__constg_swiftt: 0x10d4
+  __TEXT.__swift5_typeref: 0x1a8b
+  __TEXT.__swift5_reflstr: 0xeea
+  __TEXT.__swift5_fieldmd: 0xc84
+  __TEXT.__oslogstring: 0x3e2d
+  __TEXT.__swift5_builtin: 0x50
+  __TEXT.__swift5_assocty: 0xe0
+  __TEXT.__swift5_proto: 0x1ac
+  __TEXT.__swift5_types: 0x104
+  __TEXT.__swift_as_entry: 0x264
+  __TEXT.__swift_as_ret: 0x208
+  __TEXT.__swift_as_cont: 0x3f4
+  __TEXT.__swift5_capture: 0x1b04
+  __TEXT.__swift5_protos: 0x8
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x2040
-  __TEXT.__eh_frame: 0x5108
+  __TEXT.__unwind_info: 0x26b8
+  __TEXT.__eh_frame: 0x5dc0
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
+  __DATA_CONST.__objc_selrefs: 0x410
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x4488
-  __AUTH_CONST.__objc_const: 0xee0
-  __AUTH_CONST.__auth_got: 0x17e8
-  __AUTH.__objc_data: 0xa0
-  __AUTH.__data: 0x6c8
-  __DATA.__data: 0x8a8
-  __DATA.__common: 0x90
-  __DATA_DIRTY.__objc_data: 0x9c0
+  __AUTH_CONST.__const: 0x4fe0
+  __AUTH_CONST.__objc_const: 0x1120
+  __AUTH_CONST.__auth_got: 0x1978
+  __AUTH.__objc_data: 0xf0
+  __AUTH.__data: 0xae8
+  __DATA.__data: 0xc48
+  __DATA.__common: 0xd0
+  __DATA_DIRTY.__objc_data: 0xa20
   __DATA_DIRTY.__data: 0xd38
   __DATA_DIRTY.__bss: 0xb80
-  __DATA_DIRTY.__common: 0x100
+  __DATA_DIRTY.__common: 0xf8
   - /System/Library/Frameworks/Combine.framework/Versions/A/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3003
-  Symbols:   172
-  CStrings:  340
+  Functions: 3574
+  Symbols:   180
+  CStrings:  378
 
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
+ "Failed to resolve most recent session: %@"
+ "FetchMostRecentSessionServerTimeoutSeconds"
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
- "Requesting events for %s until %s."
- "requestEvents(for:with:)"
```
