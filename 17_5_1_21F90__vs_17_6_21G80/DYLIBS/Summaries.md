## Summaries

> `/System/Library/Health/FeedItemPlugins/Summaries.healthplugin/Summaries`

```diff

-4146.5.13.0.0
-  __TEXT.__text: 0x2a708c
+4146.6.10.0.0
+  __TEXT.__text: 0x2a4cd8
   __TEXT.__auth_stubs: 0x5480
   __TEXT.__objc_methlist: 0xc8
-  __TEXT.__cstring: 0xccb8
+  __TEXT.__cstring: 0xccd8
   __TEXT.__swift5_typeref: 0x32a0
   __TEXT.__const: 0x8024
   __TEXT.__constg_swiftt: 0x3de4

   __TEXT.__swift5_types: 0x330
   __TEXT.__swift5_mpenum: 0x10
   __TEXT.__swift5_protos: 0x58
-  __TEXT.__unwind_info: 0x5088
-  __TEXT.__eh_frame: 0x2fe8
+  __TEXT.__unwind_info: 0x508c
+  __TEXT.__eh_frame: 0x2fb0
   __TEXT.__objc_classname: 0x67
-  __TEXT.__objc_methname: 0x3679
+  __TEXT.__objc_methname: 0x36e7
   __TEXT.__objc_methtype: 0x252
   __DATA_CONST.__got: 0x13f0
   __DATA_CONST.__const: 0x188

   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x35c0
-  __DATA_CONST.__objc_selrefs: 0x13d8
+  __DATA_CONST.__objc_selrefs: 0x13f8
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_classrefs: 0x4f8
   __AUTH_CONST.__const: 0x9578

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 398653BC-79F6-3945-BF1D-4642A3EA507C
-  Functions: 7611
+  UUID: 051AA5D0-39EF-3C9F-A161-A67E3D6FD8D1
+  Functions: 7607
   Symbols:   424
-  CStrings:  1661
+  CStrings:  1665
 
CStrings:
+ "%s: %s HKCodableChartSharableModel model was nil"
+ "%s: %s SummaryTrendValue did not have appropriate info to make mean shift model for chart."
+ "%s: %s Unable to find displayType"
+ "%s: %s does not have a configuration for the requested audience %s"
+ "%s: %s does not have a swift chart diagram configuration."
+ "%s: %s there is no remote date interval for requested timescope %ld"
+ "%s: Collected %ld signals for generation of %s"
+ "%s: Created chart feed item for %s with %{private}s"
+ "%s: Created pluginFeedItem for hkType=%s with metadata=%s, viewModel=%{private}s"
+ "%s: Creating chart view model for %s with %ld points"
+ "%s: Creating request publisher for %s"
+ "%s: Creating request publisher for chart for %s"
+ "%s: Emitting chart generator for %s"
+ "%s: Emitting generator for %s"
+ "%s: Emitting generator for %s: %s"
+ "%s: Generated current value for %@ with boundedDataPresentDateInterval=%s, valueKind=%s, hasValueData=%{bool}d"
+ "%s: Generation is starting for %s"
+ "%s: No model found, deleting snidget feedItem for %s"
+ "%s: Unit preferences changed for %s, emitting generation signal for %s"
+ "%s: Unit preferences changed for %s, emitting generation signal for shared models"
+ "%s: Unreadable model, attempting to proceed with error case feedItem for %s"
+ "%s: Version mismatch deleted, deleting snidget feedItem for %s"
+ "%s:: No display type found for %s"
+ "%s_%s: First restore not concluded, doing nothing for %s"
+ "%s_%s: error when analyzing data: %s"
+ "%s_%s: error when querying data for trend: %s"
+ "Created hosting content for %@: header=%s, cv=%{private}s, viz=%s, metadata=%s"
+ "[%s]: %s does not have any model identifiers to observe in audience=%s, kinds=%s"
+ "[%s]: No display type could be found for %s for error case feedItem"
+ "[%s]_%s: correlated trend generation has started for: %s"
+ "[%s]_%s_%s: Executing query for date interval %s and configuration %s"
+ "[%{public}s]: No display type could be found for %s"
+ "[%{public}s]: No display type could be found for %s for error case feedItem"
+ "isAbleToWriteHealthSensitiveLogs"
+ "requiresSensitiveHealthLogs"
+ "sensitiveLoggingIdentifier"
+ "showSensitiveLogItems"
- "%s: %@ HKCodableChartSharableModel model was nil"
- "%s: %@ SummaryTrendValue did not have appropriate info to make mean shift model for chart."
- "%s: %@ Unable to find displayType"
- "%s: %@ does not have a configuration for the requested audience %s"
- "%s: %@ does not have a swift chart diagram configuration."
- "%s: %@ there is no remote date interval for requested timescope %ld"
- "%s: Collected %ld signals for generation of %@"
- "%s: Created chart feed item for %@ with %s"
- "%s: Created hosting content for %@: header=%s, cv=%s, viz=%s, metadata=%s"
- "%s: Created pluginFeedItem for hkType=%@ with metadata=%s, viewModel=%s"
- "%s: Creating chart view model for %@ with %ld points"
- "%s: Creating request publisher for %@"
- "%s: Creating request publisher for chart for %@"
- "%s: Emitting chart generator for %@"
- "%s: Emitting generator for %@"
- "%s: Emitting generator for %@: %s"
- "%s: Generated current value for %s with boundedDataPresentDateInterval=%s, valueKind=%s, hasValueData=%{bool}d"
- "%s: Generation is starting for %@"
- "%s: No model found, deleting snidget feedItem for %@"
- "%s: Unit preferences changed for %@, emitting generation signal for %s"
- "%s: Unit preferences changed for %@, emitting generation signal for shared models"
- "%s: Unreadable model, attempting to proceed with error case feedItem for %@"
- "%s: Version mismatch deleted, deleting snidget feedItem for %@"
- "%s:: No display type found for %@"
- "%s_%@: First restore not concluded, doing nothing for %s"
- "%s_%@: error when analyzing data: %s"
- "%s_%@: error when querying data for trend: %s"
- "[%s]: %@ does not have any model identifiers to observe in audience=%s, kinds=%s"
- "[%s]: No display type could be found for %@ for error case feedItem"
- "[%s]_%s: correlated trend generation has started for: %@"
- "[%s]_%s_%@: Executing query for date interval %s and configuration %s"
- "[%{public}s]: No display type could be found for %@"
- "[%{public}s]: No display type could be found for %@ for error case feedItem"

```
