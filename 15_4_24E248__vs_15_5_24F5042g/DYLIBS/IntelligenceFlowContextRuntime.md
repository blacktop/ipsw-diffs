## IntelligenceFlowContextRuntime

> `/System/Library/PrivateFrameworks/IntelligenceFlowContextRuntime.framework/Versions/A/IntelligenceFlowContextRuntime`

```diff

-197.0.8.201.0
-  __TEXT.__text: 0x6fc74
-  __TEXT.__auth_stubs: 0x28c0
+218.3.0.0.0
+  __TEXT.__text: 0x7267c
+  __TEXT.__auth_stubs: 0x2a90
   __TEXT.__objc_methlist: 0x4b0
-  __TEXT.__const: 0x18e8
-  __TEXT.__cstring: 0x1851
-  __TEXT.__swift5_typeref: 0x189f
-  __TEXT.__swift5_fieldmd: 0x964
-  __TEXT.__constg_swiftt: 0xee4
+  __TEXT.__const: 0x1920
+  __TEXT.__cstring: 0x19c1
+  __TEXT.__swift5_typeref: 0x18d3
+  __TEXT.__swift5_fieldmd: 0x9a8
+  __TEXT.__constg_swiftt: 0xfa0
   __TEXT.__swift5_builtin: 0xdc
-  __TEXT.__swift5_reflstr: 0x777
+  __TEXT.__swift5_reflstr: 0x7b7
   __TEXT.__swift5_assocty: 0x140
-  __TEXT.__swift5_protos: 0x34
-  __TEXT.__swift5_proto: 0x144
-  __TEXT.__swift5_types: 0xe0
-  __TEXT.__oslogstring: 0xf08
+  __TEXT.__swift5_protos: 0x38
+  __TEXT.__swift5_proto: 0x148
+  __TEXT.__swift5_types: 0xe4
+  __TEXT.__oslogstring: 0xee8
   __TEXT.__swift_as_entry: 0x128
   __TEXT.__swift_as_ret: 0x124
-  __TEXT.__swift5_capture: 0x420
+  __TEXT.__swift5_capture: 0x434
   __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__unwind_info: 0x1688
-  __TEXT.__eh_frame: 0x3788
+  __TEXT.__unwind_info: 0x16f8
+  __TEXT.__eh_frame: 0x3910
   __TEXT.__objc_classname: 0x75
-  __TEXT.__objc_methname: 0x1123
+  __TEXT.__objc_methname: 0x112f
   __TEXT.__objc_methtype: 0x470
   __TEXT.__objc_stubs: 0x1e0
-  __DATA_CONST.__got: 0x888
+  __DATA_CONST.__got: 0x8c8
   __DATA_CONST.__const: 0x188
-  __DATA_CONST.__objc_classlist: 0xc0
+  __DATA_CONST.__objc_classlist: 0xc8
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x658
   __DATA_CONST.__objc_protorefs: 0x40
-  __AUTH_CONST.__auth_got: 0x1468
-  __AUTH_CONST.__auth_ptr: 0x8b8
-  __AUTH_CONST.__const: 0x17a8
+  __AUTH_CONST.__auth_got: 0x1550
+  __AUTH_CONST.__auth_ptr: 0x928
+  __AUTH_CONST.__const: 0x17d0
   __AUTH_CONST.__cfstring: 0xc0
-  __AUTH_CONST.__objc_const: 0x15c8
+  __AUTH_CONST.__objc_const: 0x16c8
   __AUTH.__objc_data: 0x588
-  __AUTH.__data: 0x1428
-  __DATA.__data: 0x1308
+  __AUTH.__data: 0x1518
+  __DATA.__data: 0x12f8
   __DATA.__bss: 0x14a0
   __DATA.__common: 0x98
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 2063
-  Symbols:   225
-  CStrings:  485
+  Functions: 2094
+  Symbols:   226
+  CStrings:  496
 
Symbols:
+ _CGRectEqualToRect
+ _swift_makeBoxUnique
- _swift_getDynamicType
CStrings:
+ "%s %{public}ld commands, %{public}ld elements"
+ "%s fetching UI elements..."
+ "%s for %{public}s"
+ "%s found %ld on screen contents"
+ "%s initialization failed: SEM has no available index and unable to handle query. Skipping"
+ "%s initialization failed: no available morphun assets for %s to handle query. Skipping"
+ "%s unable to get bundleId for %s"
+ "%s unable to get entityInfo and/or content from contact match."
+ "%s userInfo[_NSAppEntityIdentifier] contains malformatted String"
+ "ContextRetrieval.ContextProvider"
+ "ContextRetrieval.SourceProvider"
+ "UIContext.TextEntityDetector"
+ "UIContext.onScreenContent"
+ "UIContext.retrieveUIElements"
+ "UIContext.uiContextElements"
+ "[%s] could not fetch place inferences due to error: %s"
+ "[%s] could not get POI category"
+ "[%s] could not get preferred name"
+ "[%s] couldn't create CLLocationManager"
+ "[%s] finished fetching source data for %{public}s"
+ "[%s] generated context returned %{public}ld values for %{public}s"
+ "[%s] not authorized to fetch location"
+ "[%s] starting fetching source data for %{public}s"
+ "[%s] unable to access CLLocationManager"
+ "[%s] unable to get source data"
+ "_TtC30IntelligenceFlowContextRuntime18UserSessionManager"
+ "activeUserPersonaId"
+ "context cache cannot be retrieved for %{public}s: %@"
+ "entityIdentifierValue(from:uiMetatdata:)"
+ "extractOnScreenContent(from:parameters:)"
+ "observeTask"
+ "received a signal for termination for %{public}s"
+ "refresh(contextProviders:interactionId:requestId:)"
+ "retrieveUIElements(options:)"
+ "retrieveUIElements(options:with:)"
+ "retrieveUIElementsWithOptions:with:"
+ "userManagement"
- "IFCR.ContextProvider"
- "IFCR.SourceProvider"
- "IFCR.TextEntityDetector"
- "SiriEntityMatcherEntityDetector initialization failed: SEM has no available index and unable to handle query. Skipping"
- "SiriEntityMatcherEntityDetector initialization failed: no available morphun assets for %s to handle query. Skipping"
- "UIContextRetriever.retrieveUIElements"
- "UIContextRetriever.retrieveUIElements: %{public}ld commands, %{public}ld elements"
- "UIContextRetriever.retrieveUIElements: fetching UI elements..."
- "UIContextRetriever.uiContextElements"
- "context cache cannot be retrieved: %@"
- "could not fetch place inferences for %s due to error: %s"
- "could not get POI category for %s"
- "could not get preferred name for %s"
- "couldn't create CLLocationManager for %s"
- "finished fetching source data for %{public}s for %{public}s"
- "generated context returned %{public}ld values for %{public}s for %{public}s"
- "not authorized to fetch location for %s"
- "received a signal for termination"
- "refreshing context cache for %{public}s"
- "retrieveUIElements(with:)"
- "retrieveUIElementsWith:"
- "starting fetching source data for %{public}s for %{public}s"
- "unable to access CLLocationManager for %s"
- "unable to get bundleId for %s"
- "unable to get source data for %s"
- "userInfo[_NSAppEntityIdentifier] contains malformatted String"

```
