## HealthAppHealthDaemon

> `/System/Library/PrivateFrameworks/HealthAppHealthDaemon.framework/HealthAppHealthDaemon`

```diff

-7027.1.36.2.7
-  __TEXT.__text: 0x46950
-  __TEXT.__objc_methlist: 0x1e14
-  __TEXT.__const: 0x21c0
-  __TEXT.__gcc_except_tab: 0x114
-  __TEXT.__cstring: 0x1775
-  __TEXT.__oslogstring: 0x23d4
+7027.1.45.2.4
+  __TEXT.__text: 0x472ec
+  __TEXT.__objc_methlist: 0x1ea0
+  __TEXT.__const: 0x21d0
+  __TEXT.__gcc_except_tab: 0x138
+  __TEXT.__cstring: 0x17b5
+  __TEXT.__oslogstring: 0x2514
   __TEXT.__constg_swiftt: 0x934
-  __TEXT.__swift5_typeref: 0x820
-  __TEXT.__swift5_fieldmd: 0x688
+  __TEXT.__swift5_typeref: 0x8ac
+  __TEXT.__swift5_fieldmd: 0x698
   __TEXT.__swift5_builtin: 0x3c
   __TEXT.__swift5_reflstr: 0x5a8
   __TEXT.__swift5_assocty: 0x1b8
   __TEXT.__swift5_proto: 0x174
   __TEXT.__swift5_types: 0xc0
-  __TEXT.__swift5_capture: 0x148
+  __TEXT.__swift5_capture: 0x1b8
   __TEXT.__swift5_protos: 0x18
   __TEXT.__swift_as_entry: 0x10
   __TEXT.__swift_as_ret: 0x10
   __TEXT.__swift_as_cont: 0x1c
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x1920
+  __TEXT.__unwind_info: 0x1970
   __TEXT.__eh_frame: 0x20d0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x640
+  __DATA_CONST.__const: 0x690
   __DATA_CONST.__objc_classlist: 0x120
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x150
+  __DATA_CONST.__objc_protolist: 0x158
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1430
-  __DATA_CONST.__objc_protorefs: 0x60
+  __DATA_CONST.__objc_selrefs: 0x1480
+  __DATA_CONST.__objc_protorefs: 0x68
   __DATA_CONST.__objc_superrefs: 0x80
   __DATA_CONST.__objc_arraydata: 0x8
-  __DATA_CONST.__got: 0x868
-  __AUTH_CONST.__const: 0x14d8
+  __DATA_CONST.__got: 0x878
+  __AUTH_CONST.__const: 0x15c8
   __AUTH_CONST.__cfstring: 0x900
-  __AUTH_CONST.__objc_const: 0x3090
+  __AUTH_CONST.__objc_const: 0x3190
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__auth_got: 0x10a8
-  __AUTH.__objc_data: 0x470
-  __AUTH.__data: 0xe8
-  __DATA.__objc_ivar: 0x11c
-  __DATA.__data: 0x1210
+  __AUTH_CONST.__auth_got: 0x10c8
+  __AUTH.__objc_data: 0x368
+  __AUTH.__data: 0xc0
+  __DATA.__objc_ivar: 0x124
+  __DATA.__data: 0x1120
   __DATA.__objc_stublist: 0x8
   __DATA.__common: 0x18
-  __DATA_DIRTY.__objc_data: 0xb88
-  __DATA_DIRTY.__data: 0x918
-  __DATA_DIRTY.__bss: 0xd80
+  __DATA_DIRTY.__objc_data: 0xc90
+  __DATA_DIRTY.__data: 0xa48
+  __DATA_DIRTY.__bss: 0xe00
   __DATA_DIRTY.__common: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1639
-  Symbols:   1882
-  CStrings:  311
+  Functions: 1670
+  Symbols:   1915
+  CStrings:  316
 
Symbols:
+ -[HDHealthAppDailyAnalyticsEvent _gatherPluginPayloadIHAGated:]
+ -[HDHealthAppDailyAnalyticsEvent _mergePluginPayload:into:]
+ -[HDHealthAppDailyAnalyticsEvent _payloadGatherer]
+ -[HDHealthAppDailyAnalyticsEvent pluginPayloadTimeout]
+ -[HDHealthAppDailyAnalyticsEvent setPluginPayloadTimeout:]
+ -[HDHealthAppDailyAnalyticsEvent setUnitTest_payloadGatherer:]
+ -[HDHealthAppDailyAnalyticsEvent unitTest_payloadGatherer]
+ GCC_except_table15
+ GCC_except_table8
+ _OBJC_IVAR_$_HDHealthAppDailyAnalyticsEvent._pluginPayloadTimeout
+ _OBJC_IVAR_$_HDHealthAppDailyAnalyticsEvent._unitTest_payloadGatherer
+ __PROTOCOLS__TtC21HealthAppHealthDaemon40HealthAppHealthDaemonOrchestrationClient
+ __PROTOCOL_INSTANCE_METHODS__TtP21HealthAppHealthDaemon39HealthAppDailyAnalyticsPayloadGathering_
+ __PROTOCOL_METHOD_TYPES__TtP21HealthAppHealthDaemon39HealthAppDailyAnalyticsPayloadGathering_
+ __PROTOCOL_PROTOCOLS__TtP21HealthAppHealthDaemon39HealthAppDailyAnalyticsPayloadGathering_
+ __PROTOCOL__TtP21HealthAppHealthDaemon39HealthAppDailyAnalyticsPayloadGathering_
+ ___59-[HDHealthAppDailyAnalyticsEvent _mergePluginPayload:into:]_block_invoke
+ ___63-[HDHealthAppDailyAnalyticsEvent _gatherPluginPayloadIHAGated:]_block_invoke
+ ___block_descriptor_48_e8_32s40s_e25_v32?0"NSString"816^B24ls32l8s40l8
+ ___block_descriptor_57_e8_32s40s48r_e34_v24?0"NSDictionary"8"NSError"16ls32l8r48l8s40l8
+ _objc_msgSend$_gatherPluginPayloadIHAGated:
+ _objc_msgSend$_mergePluginPayload:into:
+ _objc_msgSend$_payloadGatherer
+ _objc_msgSend$enumerateKeysAndObjectsUsingBlock:
+ _objc_msgSend$gatherIHAGatedDailyAnalyticsPayloadWithCompletion:
+ _objc_msgSend$gatherUnrestrictedDailyAnalyticsPayloadWithCompletion:
+ _objc_msgSend$pluginPayloadTimeout
+ _objc_retainBlock
+ _swift_retain_x23
+ _symbolic $s09HealthAppA6Daemon0aB30DailyAnalyticsPayloadGatheringP
+ _symbolic SDySSypGSg______pSgIeghgg_ s5ErrorP
+ _symbolic So12NSDictionaryCSgSo7NSErrorCSgIeyBhyy_
+ _symbolic _____XDXMT 09HealthAppA6Daemon0abaC19OrchestrationClientC
CStrings:
+ "%{public}@: Failed to gather plugin daily analytics payload (ihaGated=%{public}d) with error %{public}@"
+ "%{public}@: Plugin daily analytics payload key %{public}@ is already present in the event payload; dropping the plugin value."
+ "%{public}@: Timed out gathering plugin daily analytics payload (ihaGated=%{public}d)."
+ "v24@?0@\"NSDictionary\"8@\"NSError\"16"
+ "v32@?0@\"NSString\"8@16^B24"
```
