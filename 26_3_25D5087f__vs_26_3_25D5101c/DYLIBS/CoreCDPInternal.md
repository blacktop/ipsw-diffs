## CoreCDPInternal

> `/System/Library/PrivateFrameworks/CoreCDPInternal.framework/Versions/A/CoreCDPInternal`

```diff

-416.325.0.0.0
-  __TEXT.__text: 0x8fd50
+416.325.3.0.0
+  __TEXT.__text: 0x8fd98
   __TEXT.__auth_stubs: 0xf70
   __TEXT.__objc_methlist: 0x501c
   __TEXT.__const: 0x7c2
-  __TEXT.__oslogstring: 0x11faa
-  __TEXT.__cstring: 0xce23
+  __TEXT.__oslogstring: 0x11fda
+  __TEXT.__cstring: 0xce33
   __TEXT.__gcc_except_tab: 0x9c8
   __TEXT.__dlopen_cstrs: 0xbc
   __TEXT.__constg_swiftt: 0x1c4

   __TEXT.__swift_as_entry: 0x60
   __TEXT.__swift_as_ret: 0x58
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x1b98
+  __TEXT.__unwind_info: 0x1b90
   __TEXT.__eh_frame: 0x910
   __TEXT.__objc_classname: 0xc4e
-  __TEXT.__objc_methname: 0xe504
-  __TEXT.__objc_methtype: 0x25e1
-  __TEXT.__objc_stubs: 0xb820
+  __TEXT.__objc_methname: 0xe542
+  __TEXT.__objc_methtype: 0x25ef
+  __TEXT.__objc_stubs: 0xb840
   __DATA_CONST.__got: 0xfc8
   __DATA_CONST.__const: 0x418
   __DATA_CONST.__objc_classlist: 0x280
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x178
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x34d8
+  __DATA_CONST.__objc_selrefs: 0x34e0
   __DATA_CONST.__objc_protorefs: 0x50
   __DATA_CONST.__objc_superrefs: 0x148
   __DATA_CONST.__objc_arraydata: 0x160
   __AUTH_CONST.__auth_got: 0x7c8
   __AUTH_CONST.__const: 0x2950
-  __AUTH_CONST.__cfstring: 0x8420
+  __AUTH_CONST.__cfstring: 0x8440
   __AUTH_CONST.__objc_const: 0xf2e8
   __AUTH_CONST.__objc_intobj: 0x150
   __AUTH_CONST.__objc_arrayobj: 0xa8

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 62512089-D04E-3789-ADC7-6D08A93B9D88
+  UUID: E7326B9E-0BB6-391E-9A29-56A90D264CEB
   Functions: 2884
-  Symbols:   6563
-  CStrings:  6032
+  Symbols:   6564
+  CStrings:  6036
 
Symbols:
+ -[CDPDAnalyticsTransport _replaceClientNameWithEvent:isIdentifiableApproved:]
+ -[CDPDAnalyticsTransport enforceIdentifiableDataPrivacyComplianceOnEvent:manager:]
+ -[CDPDAnalyticsTransport enforceIdentifiableDataPrivacyComplianceOnEvent:manager:].cold.1
+ -[CDPDAnalyticsTransport enforceIdentifiableDataPrivacyComplianceOnEvent:manager:].cold.2
+ -[CDPDAnalyticsTransport enforceIdentifiableDataPrivacyComplianceOnEvent:manager:].cold.3
+ __36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.2153
+ __36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.2153.cold.1
+ __36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.2154
+ __36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.2154.cold.1
+ __36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.2219
+ __36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.2219.cold.1
+ __36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.2219.cold.2
+ __81-[CDPDAnalyticsTransport configureSessionForEvent:sendEventBlock:telemetryQueue:]_block_invoke.2220
+ __81-[CDPDAnalyticsTransport configureSessionForEvent:sendEventBlock:telemetryQueue:]_block_invoke.2224
+ __81-[CDPDAnalyticsTransport configureSessionForEvent:sendEventBlock:telemetryQueue:]_block_invoke.2224.cold.1
+ __block_literal_global.1019
+ __block_literal_global.1030
+ __block_literal_global.1134
+ __block_literal_global.1178
+ __block_literal_global.1213
+ __block_literal_global.1290
+ __block_literal_global.1319
+ __block_literal_global.2122
+ __block_literal_global.2134
+ __block_literal_global.2150
+ __block_literal_global.2226
+ __block_literal_global.32
+ __block_literal_global.38
+ __block_literal_global.516
+ _objc_msgSend$_replaceClientNameWithEvent:isIdentifiableApproved:
+ _objc_msgSend$enforceIdentifiableDataPrivacyComplianceOnEvent:manager:
+ _objc_msgSend$identifiableTelemetryAllowedForAccount:
- +[CDPDAnalyticsTransport transportForEvent:].cold.2
- -[CDPDAnalyticsTransport _enforceIdentifiableDataPrivacyComplianceOnEvent:manager:]
- -[CDPDAnalyticsTransport _enforceIdentifiableDataPrivacyComplianceOnEvent:manager:].cold.1
- -[CDPDAnalyticsTransport _enforceIdentifiableDataPrivacyComplianceOnEvent:manager:].cold.2
- -[CDPDAnalyticsTransport _replaceClientNameWithEvent:]
- __36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.2151
- __36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.2151.cold.1
- __36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.2152
- __36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.2152.cold.1
- __36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.2217
- __36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.2217.cold.1
- __36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.2217.cold.2
- __81-[CDPDAnalyticsTransport configureSessionForEvent:sendEventBlock:telemetryQueue:]_block_invoke.2218
- __81-[CDPDAnalyticsTransport configureSessionForEvent:sendEventBlock:telemetryQueue:]_block_invoke.2222
- __81-[CDPDAnalyticsTransport configureSessionForEvent:sendEventBlock:telemetryQueue:]_block_invoke.2222.cold.1
- __block_literal_global.1016
- __block_literal_global.1027
- __block_literal_global.1131
- __block_literal_global.1175
- __block_literal_global.1210
- __block_literal_global.1287
- __block_literal_global.1316
- __block_literal_global.2119
- __block_literal_global.2131
- __block_literal_global.2148
- __block_literal_global.2224
- __block_literal_global.29
- __block_literal_global.35
- __block_literal_global.513
- _objc_msgSend$_enforceIdentifiableDataPrivacyComplianceOnEvent:manager:
- _objc_msgSend$_replaceClientNameWithEvent:
Functions:
~ +[CDPDAnalyticsTransport transportForEvent:] : 452 -> 400
~ -[CDPDAnalyticsTransport _enforceIdentifiableDataPrivacyComplianceOnEvent:manager:] -> -[CDPDAnalyticsTransport enforceIdentifiableDataPrivacyComplianceOnEvent:manager:] : 436 -> 656
~ -[CDPDAnalyticsTransport _replaceClientNameWithEvent:] -> -[CDPDAnalyticsTransport _replaceClientNameWithEvent:isIdentifiableApproved:] : 136 -> 104
~ -[CDPDAnalyticsTransport enforcePrivacyComplianceOnEvent:key:value:] : 988 -> 920
~ -[CDPDAnalyticsTransport _sendEvent:] : 524 -> 580
~ -[CDPDAnalyticsTransport _isDNUEvent:] : 80 -> 28
~ +[CDPDAnalyticsTransport transportForEvent:].cold.2 -> +[CDPDAnalyticsTransport flushTransportCache].cold.1 : 148 -> 60
~ +[CDPDAnalyticsTransport flushCaches].cold.2 -> +[CDPDAnalyticsTransport getAllEventsForDataSanitization].cold.1 : 60 -> 20
~ +[CDPDAnalyticsTransport transportForClientType:clientBundleId:clientName:].cold.1 -> +[CDPDAnalyticsTransport transportForClientType:clientBundleId:clientName:].cold.2 : 20 -> 64
~ +[CDPDAnalyticsTransport transportForClientType:clientBundleId:clientName:].cold.2 -> __75+[CDPDAnalyticsTransport transportForClientType:clientBundleId:clientName:]_block_invoke_2.cold.1 : 64 -> 116
~ __75+[CDPDAnalyticsTransport transportForClientType:clientBundleId:clientName:]_block_invoke_2.cold.1 -> __75+[CDPDAnalyticsTransport transportForClientType:clientBundleId:clientName:]_block_invoke_2.cold.2 : 116 -> 136
~ __75+[CDPDAnalyticsTransport transportForClientType:clientBundleId:clientName:]_block_invoke_2.cold.2 -> -[CDPDAnalyticsTransport _renewMissingDeviceSessionIDIfNeeded:manager:account:].cold.1 : 136 -> 148
CStrings:
+ "_replaceClientNameWithEvent:isIdentifiableApproved:"
+ "enforceIdentifiableDataPrivacyComplianceOnEvent:manager:"
+ "event (%@) is not approved for identifiable data collection. Removing eventCreationTime..."
+ "eventCreationTime"
+ "identifiableTelemetryAllowedForAccount:"
+ "v28@0:8@16B24"
- "Enabling Opt-In collection for event: %@"
- "_enforceIdentifiableDataPrivacyComplianceOnEvent:manager:"
- "_replaceClientNameWithEvent:"

```
