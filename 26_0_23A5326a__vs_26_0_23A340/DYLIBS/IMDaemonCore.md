## IMDaemonCore

> `/System/Library/PrivateFrameworks/IMDaemonCore.framework/IMDaemonCore`

```diff

-1448.100.1.2.74
-  __TEXT.__text: 0x300f34
-  __TEXT.__auth_stubs: 0x51d0
-  __TEXT.__objc_methlist: 0x18974
-  __TEXT.__const: 0x5768
-  __TEXT.__cstring: 0x14261
-  __TEXT.__gcc_except_tab: 0x2892c
-  __TEXT.__oslogstring: 0x4aba7
+1448.100.1.2.101
+  __TEXT.__text: 0x300034
+  __TEXT.__auth_stubs: 0x5130
+  __TEXT.__objc_methlist: 0x18994
+  __TEXT.__const: 0x5708
+  __TEXT.__cstring: 0x14241
+  __TEXT.__gcc_except_tab: 0x289a8
+  __TEXT.__oslogstring: 0x4abd7
   __TEXT.__ustring: 0x32c
   __TEXT.__dlopen_cstrs: 0x246
-  __TEXT.__constg_swiftt: 0x20e8
-  __TEXT.__swift5_typeref: 0x2844
+  __TEXT.__constg_swiftt: 0x20d4
+  __TEXT.__swift5_typeref: 0x27c0
   __TEXT.__swift5_builtin: 0x1b8
-  __TEXT.__swift5_reflstr: 0x10ef
-  __TEXT.__swift5_fieldmd: 0x13a8
+  __TEXT.__swift5_reflstr: 0x10ff
+  __TEXT.__swift5_fieldmd: 0x138c
   __TEXT.__swift5_assocty: 0x688
-  __TEXT.__swift5_capture: 0x1144
-  __TEXT.__swift5_proto: 0x2ec
-  __TEXT.__swift5_types: 0x1e4
-  __TEXT.__swift_as_entry: 0x294
-  __TEXT.__swift_as_ret: 0x34c
+  __TEXT.__swift5_capture: 0x1140
+  __TEXT.__swift5_proto: 0x2e4
+  __TEXT.__swift5_types: 0x1e0
+  __TEXT.__swift_as_entry: 0x298
+  __TEXT.__swift_as_ret: 0x354
   __TEXT.__swift5_protos: 0x24
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0xcb28
-  __TEXT.__eh_frame: 0x5cb4
-  __TEXT.__objc_classname: 0x3443
-  __TEXT.__objc_methname: 0x4b0e1
-  __TEXT.__objc_methtype: 0x9dd8
-  __TEXT.__objc_stubs: 0x2edc0
+  __TEXT.__unwind_info: 0xcae8
+  __TEXT.__eh_frame: 0x5c9c
+  __TEXT.__objc_classname: 0x3448
+  __TEXT.__objc_methname: 0x4b18c
+  __TEXT.__objc_methtype: 0x9ddb
+  __TEXT.__objc_stubs: 0x2ef40
   __DATA_CONST.__got: 0x3070
-  __DATA_CONST.__const: 0x6150
+  __DATA_CONST.__const: 0x61c8
   __DATA_CONST.__objc_classlist: 0x918
   __DATA_CONST.__objc_catlist: 0xe8
   __DATA_CONST.__objc_protolist: 0x6f8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xf4b8
+  __DATA_CONST.__objc_selrefs: 0xf4e8
   __DATA_CONST.__objc_protorefs: 0x240
   __DATA_CONST.__objc_superrefs: 0x580
   __DATA_CONST.__objc_arraydata: 0x140
-  __AUTH_CONST.__auth_got: 0x28f8
-  __AUTH_CONST.__const: 0x7818
+  __AUTH_CONST.__auth_got: 0x28a8
+  __AUTH_CONST.__const: 0x77b8
   __AUTH_CONST.__cfstring: 0xde40
   __AUTH_CONST.__objc_const: 0x1eff0
   __AUTH_CONST.__objc_intobj: 0x990

   __AUTH.__objc_data: 0x2e60
   __AUTH.__data: 0xa78
   __DATA.__objc_ivar: 0x10e0
-  __DATA.__data: 0x5190
-  __DATA.__bss: 0x4e90
+  __DATA.__data: 0x51e0
+  __DATA.__bss: 0x4d90
   __DATA.__common: 0x118
   __DATA_DIRTY.__objc_data: 0x3250
-  __DATA_DIRTY.__data: 0x20f0
+  __DATA_DIRTY.__data: 0x2120
   __DATA_DIRTY.__bss: 0x1450
   __DATA_DIRTY.__common: 0x1a8
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: F0617B1A-6C72-361A-B416-57C548FA6326
-  Functions: 12198
-  Symbols:   2887
-  CStrings:  20816
+  UUID: 1CCB55E8-F530-3C69-BB78-67AEED03D775
+  Functions: 12170
+  Symbols:   2886
+  CStrings:  20824
 
Symbols:
+ _IMChatPropertyLastReceivedSatelliteSMSRelayMessageDate
- _OBJC_CLASS_$_BGSystemTaskProgressMetrics
- _swift_isUniquelyReferenced_native
CStrings:
+ "Blastdoor lite relay message response %p received"
+ "Failed processing lite relay message through Blastdoor name=(%@); reason=(%@)"
+ "Lite"
+ "Piping lite relay message through Blastdoor"
+ "[%{public}s] already running?? waiting for existing task to finish"
+ "chat:groupIDUpdated:"
+ "chat:originalGroupIDUpdated:"
+ "defuseLiteRelayTextMessage:error:"
+ "hasFullTaskReports"
+ "isSatelliteContinuityEnabled"
+ "isSatelliteRelayEnabled"
+ "loadPTaskReportsForGroups:excludingReasons:loadFullReports:completionBlock:"
+ "personalOffGridModeWithCompletion:"
+ "sendLiteRelayData:senderContext:error:"
+ "sendingDecision - withSatelliteRelay: %@"
+ "setPreventsDeviceSleep:"
+ "shouldSatelliteRelayIncomingSMSMessagesWithCompletion:"
+ "v44@0:8@\"NSArray\"16@\"NSArray\"24B32@?<v@?@\"NSArray\">36"
- "[%{public}s] already running, waiting on existing task"
- "[%{public}s] failed to submit progress metric for flag %{public}s: %@"
- "[%{public}s] submitting progress metric for flag %{public}s with %ld remaining items"
- "com.apple.messages.message-processing.Metrics"
- "initWithIdentifier:qos:workloadCategory:expectedMetricValue:itemsCompleted:totalItemCount:"
- "loadPTaskReportsForGroups:excludingReasons:completionBlock:"
- "pendingActions"
- "reportProgressMetrics:error:"
- "totalItemCount"
- "v40@0:8@\"NSArray\"16@\"NSArray\"24@?<v@?@\"NSArray\">32"

```
