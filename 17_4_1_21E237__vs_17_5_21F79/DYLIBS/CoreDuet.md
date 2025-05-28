## CoreDuet

> `/System/Library/PrivateFrameworks/CoreDuet.framework/CoreDuet`

```diff

-1852.19.0.2.0
-  __TEXT.__text: 0x19095c
+1852.22.0.0.0
+  __TEXT.__text: 0x18da80
   __TEXT.__auth_stubs: 0x1460
-  __TEXT.__objc_methlist: 0xff84
-  __TEXT.__cstring: 0x159c5
-  __TEXT.__oslogstring: 0x1801b
-  __TEXT.__const: 0x3d8
-  __TEXT.__gcc_except_tab: 0x61a8
+  __TEXT.__objc_methlist: 0xff74
+  __TEXT.__cstring: 0x152b2
+  __TEXT.__oslogstring: 0x1765f
+  __TEXT.__const: 0x3d0
+  __TEXT.__gcc_except_tab: 0x5c8c
   __TEXT.__dlopen_cstrs: 0x5e
-  __TEXT.__unwind_info: 0x52f0
-  __TEXT.__objc_classname: 0x2c29
-  __TEXT.__objc_methname: 0x24f19
-  __TEXT.__objc_methtype: 0x6038
-  __TEXT.__objc_stubs: 0x16840
+  __TEXT.__unwind_info: 0x520c
+  __TEXT.__objc_classname: 0x2c20
+  __TEXT.__objc_methname: 0x24ee3
+  __TEXT.__objc_methtype: 0x5ffa
+  __TEXT.__objc_stubs: 0x16800
   __DATA_CONST.__got: 0x340
   __DATA_CONST.__const: 0x37e8
   __DATA_CONST.__objc_classlist: 0xc20
   __DATA_CONST.__objc_catlist: 0x70
   __DATA_CONST.__objc_protolist: 0x218
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1c628
-  __DATA_CONST.__objc_selrefs: 0x7c08
+  __DATA_CONST.__objc_const: 0x1c3e8
+  __DATA_CONST.__objc_selrefs: 0x7c00
   __DATA_CONST.__objc_protorefs: 0x70
   __DATA_CONST.__objc_classrefs: 0xdf8
   __DATA_CONST.__objc_superrefs: 0x690
   __DATA_CONST.__objc_arraydata: 0x630
-  __AUTH_CONST.__cfstring: 0x12fc0
+  __AUTH_CONST.__cfstring: 0x12a60
   __AUTH_CONST.__objc_const: 0x8c78
   __AUTH_CONST.__const: 0x1880
   __AUTH_CONST.__objc_intobj: 0x2298

   __AUTH_CONST.__auth_ptr: 0x10
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__auth_got: 0xa40
-  __AUTH.__objc_data: 0x4a10
-  __DATA.__objc_ivar: 0x17a0
-  __DATA.__data: 0x2198
-  __DATA.__bss: 0x388
+  __AUTH.__objc_data: 0x4a60
+  __DATA.__objc_ivar: 0x1758
+  __DATA.__data: 0x2270
+  __DATA.__bss: 0x2e0
   __DATA.__common: 0x38
   __DATA_DIRTY.__const: 0x18
-  __DATA_DIRTY.__objc_data: 0x2f30
+  __DATA_DIRTY.__objc_data: 0x2ee0
   __DATA_DIRTY.__data: 0x8
-  __DATA_DIRTY.__bss: 0x430
+  __DATA_DIRTY.__bss: 0x400
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/CoreData.framework/CoreData

   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 8777
-  Symbols:   27058
-  CStrings:  11727
+  Functions: 8759
+  Symbols:   26996
+  CStrings:  11627
 
Symbols:
+ ___51-[_DKSync2Coordinator __performSyncWithCompletion:]_block_invoke.559
+ ___67-[_DKSync2Coordinator _registerTriggeredSyncActivityWithIsStartup:]_block_invoke.631
+ ___87-[_DKSyncLocalKnowledgeStorage syncHistoryForPeer:streamName:transportName:type:error:]_block_invoke.89
+ ___block_descriptor_64_e8_32s40s48s56bs_e51_v32?0"NSDictionary"8"NSDictionary"16"NSError"24ls32l8s40l8s48l8s56l8
+ ___block_literal_global.226
+ ___block_literal_global.34
+ ___block_literal_global.366
+ ___block_literal_global.37
+ ___block_literal_global.48
+ ___block_literal_global.561
+ ___block_literal_global.69
+ ___block_literal_global.777
+ ___block_literal_global.85
+ ___block_literal_global.88
+ ___block_literal_global.91
+ __unnamed_array_storage.263
+ __unnamed_array_storage.575
+ _sharedInstance.initialized.223
+ _sharedInstance.initialized.363
+ _sharedInstance.sharedInstance.224
+ _sharedInstance.sharedInstance.364
- -[_CDMutablePerfMetric startTelemetryWithOSActivity:]
- -[_DKPerformSyncDownOperation endPerfMetrics]
- -[_DKPerformSyncDownOperation startPerfMetrics]
- -[_DKPerformSyncDownPeerAdditionsOperation endPerfMetrics]
- -[_DKPerformSyncDownPeerAdditionsOperation startPerfMetrics]
- -[_DKPerformSyncDownPeerDeletionsOperation endPerfMetrics]
- -[_DKPerformSyncDownPeerDeletionsOperation startPerfMetrics]
- -[_DKPerformSyncDownPeerOperation endPerfMetrics]
- -[_DKPerformSyncDownPeerOperation startPerfMetrics]
- -[_DKPerformSyncUpChangeOperation endPerfMetrics]
- -[_DKPerformSyncUpChangeOperation startPerfMetrics]
- -[_DKPerformSyncUpHistoryAdditionsOperation endPerfMetrics]
- -[_DKPerformSyncUpHistoryAdditionsOperation startPerfMetrics]
- -[_DKPerformSyncUpHistoryDeletionsOperation endPerfMetrics]
- -[_DKPerformSyncUpHistoryDeletionsOperation startPerfMetrics]
- -[_DKPerformSyncUpHistoryOperation endPerfMetrics]
- -[_DKPerformSyncUpHistoryOperation startPerfMetrics]
- GCC_except_table103
- GCC_except_table130
- GCC_except_table134
- GCC_except_table138
- _OBJC_IVAR_$__DKPerformSyncDownOperation._perfEvent
- _OBJC_IVAR_$__DKPerformSyncDownOperation._perfMetric
- _OBJC_IVAR_$__DKPerformSyncDownPeerAdditionsOperation._perfEvent
- _OBJC_IVAR_$__DKPerformSyncDownPeerAdditionsOperation._perfMetric
- _OBJC_IVAR_$__DKPerformSyncDownPeerDeletionsOperation._perfEvent
- _OBJC_IVAR_$__DKPerformSyncDownPeerDeletionsOperation._perfMetric
- _OBJC_IVAR_$__DKPerformSyncDownPeerOperation._perfEvent
- _OBJC_IVAR_$__DKPerformSyncDownPeerOperation._perfMetric
- _OBJC_IVAR_$__DKPerformSyncUpChangeOperation._perfEvent
- _OBJC_IVAR_$__DKPerformSyncUpChangeOperation._perfMetric
- _OBJC_IVAR_$__DKPerformSyncUpHistoryAdditionsOperation._perfEvent
- _OBJC_IVAR_$__DKPerformSyncUpHistoryAdditionsOperation._perfMetric
- _OBJC_IVAR_$__DKPerformSyncUpHistoryDeletionsOperation._perfEvent
- _OBJC_IVAR_$__DKPerformSyncUpHistoryDeletionsOperation._perfMetric
- _OBJC_IVAR_$__DKPerformSyncUpHistoryOperation._perfEvent
- _OBJC_IVAR_$__DKPerformSyncUpHistoryOperation._perfMetric
- _OBJC_IVAR_$__DKSync2Coordinator._perfEvent
- _OBJC_IVAR_$__DKSync2Coordinator._perfMetric
- __CDPerfMetricStartTimingWithTelemetry
- ___51-[_DKSync2Coordinator __performSyncWithCompletion:]_block_invoke.563
- ___67-[_DKSync2Coordinator _registerTriggeredSyncActivityWithIsStartup:]_block_invoke.635
- ___87-[_DKSyncLocalKnowledgeStorage syncHistoryForPeer:streamName:transportName:type:error:]_block_invoke.114
- ___block_descriptor_80_e8_32s40s48s56s64bs72r_e51_v32?0"NSDictionary"8"NSDictionary"16"NSError"24ls32l8s40l8s48l8s64l8s56l8r72l8
- ___block_literal_global.104
- ___block_literal_global.113
- ___block_literal_global.116
- ___block_literal_global.247
- ___block_literal_global.413
- ___block_literal_global.47
- ___block_literal_global.565
- ___block_literal_global.785
- ___block_literal_global.82
- __unnamed_array_storage.291
- __unnamed_array_storage.616
- _objc_msgSend$family
- _objc_msgSend$startTelemetryWithOSActivity:
- _sharedInstance.initialized.244
- _sharedInstance.initialized.410
- _sharedInstance.sharedInstance.245
- _sharedInstance.sharedInstance.411
CStrings:
+ "\x05\x12"
+ "\x06\x14\x11"
+ "\a\x11"
+ "\a\x13(\x11\x16"
- "\x06!"
- "\x06!\x14\x11"
- "\x06\"\x11"
- "\x062"
- "\a\x13$%\x11\x16"
- "\a#"
- "@\"_CDMutablePerfMetric\""
- "Duet: PerformSyncDownOperation(Cloud)"
- "Duet: PerformSyncDownOperation(Rapport)"
- "Duet: PerformSyncDownPeerAdditionsOperation(Cloud)"
- "Duet: PerformSyncDownPeerAdditionsOperation(Rapport)"
- "Duet: PerformSyncDownPeerDeletionsOperation(Cloud)"
- "Duet: PerformSyncDownPeerDeletionsOperation(Rapport)"
- "Duet: PerformSyncDownPeerOperation(Cloud)"
- "Duet: PerformSyncDownPeerOperation(Rapport)"
- "Duet: PerformSyncUpChangeOperation(Cloud)"
- "Duet: PerformSyncUpChangeOperation(Rapport)"
- "Duet: PerformSyncUpHistoryAdditionsOperation(Cloud)"
- "Duet: PerformSyncUpHistoryAdditionsOperation(Rapport)"
- "Duet: PerformSyncUpHistoryDeletionsOperation(Cloud)"
- "Duet: PerformSyncUpHistoryDeletionsOperation(Rapport)"
- "Duet: PerformSyncUpHistoryOperation(Cloud)"
- "Duet: PerformSyncUpHistoryOperation(Rapport)"
- "Duet: Syncing"
- "Duet: deleting events from local database"
- "Duet: fetching bookmark from local database"
- "Duet: fetching event deletions from local database"
- "Duet: fetching events from local database"
- "Duet: fetching sync history from local database"
- "Duet: fetching windows from local database"
- "Duet: handling beacon request via rapport"
- "Duet: handling fetch context values request via rapport"
- "Duet: handling fetch context values response via rapport"
- "Duet: handling fetch deleted event ids request via rapport"
- "Duet: handling fetch deleted event ids response via rapport"
- "Duet: handling fetch events request via rapport"
- "Duet: handling fetch events response via rapport"
- "Duet: handling fetch source device id request via rapport"
- "Duet: handling fetch source device id response via rapport"
- "Duet: handling sent context values response via rapport"
- "Duet: handling sent context values via rapport"
- "Duet: handling subscribe to context value changes request via rapport"
- "Duet: handling subscribe to context value changes response via rapport"
- "Duet: handling unsubscribe to context value changes request via rapport"
- "Duet: handling unsubscribe to context value changes response via rapport"
- "Duet: rapport compression"
- "Duet: rapport decompression"
- "Duet: saving bookmark to local database"
- "Duet: saving events to local database"
- "Duet: saving window to local database"
- "Duet: sending fetch context values request via rapport"
- "Duet: sending fetch deleted event ids request via rapport"
- "Duet: sending fetch events request via rapport"
- "Duet: sending fetch source device id request via rapport"
- "Duet: sending send context values via rapport"
- "Duet: sending subscribe to context value changes request via rapport"
- "Duet: sending unsubscribe to context value changes request via rapport"
- "Local Storage"
- "PerformSyncDownOperation"
- "PerformSyncDownPeerAdditionsOperation"
- "PerformSyncDownPeerDeletionsOperation"
- "PerformSyncDownPeerOperation"
- "PerformSyncUpChangeOperation"
- "PerformSyncUpHistoryAdditionsOperation"
- "PerformSyncUpHistoryDeletionsOperation"
- "PerformSyncUpHistoryOperation"
- "Syncing"
- "_perfEvent"
- "_perfMetric"
- "deleting events from local database"
- "fetching bookmark from local database"
- "fetching event deletions from local database"
- "fetching events from local database"
- "fetching sync history from local database"
- "fetching windows from local database"
- "handling beacon request via rapport"
- "handling fetch context values request via rapport"
- "handling fetch context values response via rapport"
- "handling fetch deleted event ids request via rapport"
- "handling fetch deleted event ids response via rapport"
- "handling fetch events request via rapport"
- "handling fetch events response via rapport"
- "handling fetch source device id request via rapport"
- "handling fetch source device id response via rapport"
- "handling sent context values response via rapport"
- "handling sent context values via rapport"
- "handling subscribe to context value changes request via rapport"
- "handling subscribe to context value changes response via rapport"
- "handling unsubscribe to context value changes request via rapport"
- "handling unsubscribe to context value changes response via rapport"
- "rapport compression"
- "rapport decompression"
- "saving bookmark to local database"
- "saving events to local database"
- "saving window to local database"
- "sending fetch context values request via rapport"
- "sending fetch deleted event ids request via rapport"
- "sending fetch events request via rapport"
- "sending fetch source device id request via rapport"
- "sending send context values via rapport"
- "sending subscribe to context value changes request via rapport"
- "sending unsubscribe to context value changes request via rapport"
- "startTelemetryWithOSActivity:"
- "{_CDPerfEvent=\"startTime\"d\"endTime\"d}"

```
