## CoreCDPInternal

> `/System/Library/PrivateFrameworks/CoreCDPInternal.framework/CoreCDPInternal`

```diff

-416.325.0.0.0
-  __TEXT.__text: 0x87110
+416.325.3.0.0
+  __TEXT.__text: 0x87160
   __TEXT.__auth_stubs: 0x11c0
   __TEXT.__objc_methlist: 0x5144
   __TEXT.__const: 0x7d0
-  __TEXT.__oslogstring: 0x1240e
-  __TEXT.__cstring: 0xd3a5
+  __TEXT.__oslogstring: 0x1243e
+  __TEXT.__cstring: 0xd3c5
   __TEXT.__gcc_except_tab: 0xa1c
   __TEXT.__dlopen_cstrs: 0xb0
   __TEXT.__swift5_typeref: 0x37f

   __TEXT.__swift5_capture: 0x200
   __TEXT.__swift_as_entry: 0x60
   __TEXT.__swift_as_ret: 0x58
-  __TEXT.__unwind_info: 0x1b70
+  __TEXT.__unwind_info: 0x1b68
   __TEXT.__eh_frame: 0x910
   __TEXT.__objc_classname: 0xc99
-  __TEXT.__objc_methname: 0xe80a
-  __TEXT.__objc_methtype: 0x260b
-  __TEXT.__objc_stubs: 0xbb60
+  __TEXT.__objc_methname: 0xe848
+  __TEXT.__objc_methtype: 0x2619
+  __TEXT.__objc_stubs: 0xbb80
   __DATA_CONST.__got: 0xff8
   __DATA_CONST.__const: 0x2168
   __DATA_CONST.__objc_classlist: 0x290
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x180
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3568
+  __DATA_CONST.__objc_selrefs: 0x3570
   __DATA_CONST.__objc_protorefs: 0x50
   __DATA_CONST.__objc_superrefs: 0x158
   __DATA_CONST.__objc_arraydata: 0x160
   __AUTH_CONST.__auth_got: 0x8f0
   __AUTH_CONST.__const: 0xab0
-  __AUTH_CONST.__cfstring: 0x8800
+  __AUTH_CONST.__cfstring: 0x8820
   __AUTH_CONST.__objc_const: 0xf890
   __AUTH_CONST.__objc_intobj: 0x168
   __AUTH_CONST.__objc_arrayobj: 0xa8

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: E5AEAD75-E50D-3EDF-8A83-06A968AF64B6
+  UUID: 739031FB-2C02-3649-AB8E-D6C9B3C787E6
   Functions: 2874
-  Symbols:   9368
-  CStrings:  6143
+  Symbols:   9369
+  CStrings:  6147
 
Symbols:
+ -[CDPDAnalyticsTransport _replaceClientNameWithEvent:isIdentifiableApproved:]
+ -[CDPDAnalyticsTransport enforceIdentifiableDataPrivacyComplianceOnEvent:manager:]
+ -[CDPDAnalyticsTransport enforceIdentifiableDataPrivacyComplianceOnEvent:manager:].cold.1
+ -[CDPDAnalyticsTransport enforceIdentifiableDataPrivacyComplianceOnEvent:manager:].cold.2
+ -[CDPDAnalyticsTransport enforceIdentifiableDataPrivacyComplianceOnEvent:manager:].cold.3
+ ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.2153
+ ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.2153.cold.1
+ ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.2154
+ ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.2154.cold.1
+ ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.2217
+ ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.2217.cold.1
+ ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.2217.cold.2
+ ___81-[CDPDAnalyticsTransport configureSessionForEvent:sendEventBlock:telemetryQueue:]_block_invoke.2218
+ ___81-[CDPDAnalyticsTransport configureSessionForEvent:sendEventBlock:telemetryQueue:]_block_invoke_2.2220
+ ___81-[CDPDAnalyticsTransport configureSessionForEvent:sendEventBlock:telemetryQueue:]_block_invoke_2.2220.cold.1
+ ___block_literal_global.1019
+ ___block_literal_global.1030
+ ___block_literal_global.1134
+ ___block_literal_global.1178
+ ___block_literal_global.1213
+ ___block_literal_global.1290
+ ___block_literal_global.1319
+ ___block_literal_global.2122
+ ___block_literal_global.2134
+ ___block_literal_global.2150
+ ___block_literal_global.2222
+ ___block_literal_global.32
+ ___block_literal_global.38
+ ___block_literal_global.516
+ _objc_msgSend$_replaceClientNameWithEvent:isIdentifiableApproved:
+ _objc_msgSend$enforceIdentifiableDataPrivacyComplianceOnEvent:manager:
+ _objc_msgSend$identifiableTelemetryAllowedForAccount:
- +[CDPDAnalyticsTransport transportForEvent:].cold.2
- -[CDPDAnalyticsTransport _enforceIdentifiableDataPrivacyComplianceOnEvent:manager:]
- -[CDPDAnalyticsTransport _enforceIdentifiableDataPrivacyComplianceOnEvent:manager:].cold.1
- -[CDPDAnalyticsTransport _enforceIdentifiableDataPrivacyComplianceOnEvent:manager:].cold.2
- -[CDPDAnalyticsTransport _replaceClientNameWithEvent:]
- ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.2151
- ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.2151.cold.1
- ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.2152
- ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.2152.cold.1
- ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.2215
- ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.2215.cold.1
- ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.2215.cold.2
- ___81-[CDPDAnalyticsTransport configureSessionForEvent:sendEventBlock:telemetryQueue:]_block_invoke.2216
- ___81-[CDPDAnalyticsTransport configureSessionForEvent:sendEventBlock:telemetryQueue:]_block_invoke_2.2218
- ___81-[CDPDAnalyticsTransport configureSessionForEvent:sendEventBlock:telemetryQueue:]_block_invoke_2.2218.cold.1
- ___block_literal_global.1016
- ___block_literal_global.1027
- ___block_literal_global.1131
- ___block_literal_global.1175
- ___block_literal_global.1210
- ___block_literal_global.1287
- ___block_literal_global.1316
- ___block_literal_global.2119
- ___block_literal_global.2131
- ___block_literal_global.2148
- ___block_literal_global.2220
- ___block_literal_global.29
- ___block_literal_global.513
- _objc_msgSend$_enforceIdentifiableDataPrivacyComplianceOnEvent:manager:
- _objc_msgSend$_replaceClientNameWithEvent:
Functions:
~ +[CDPDAnalyticsTransport transportForEvent:] : 380 -> 336
~ -[CDPDAnalyticsTransport _enforceIdentifiableDataPrivacyComplianceOnEvent:manager:] -> -[CDPDAnalyticsTransport enforceIdentifiableDataPrivacyComplianceOnEvent:manager:] : 372 -> 580
~ -[CDPDAnalyticsTransport _replaceClientNameWithEvent:] -> -[CDPDAnalyticsTransport _replaceClientNameWithEvent:isIdentifiableApproved:] : 132 -> 104
~ -[CDPDAnalyticsTransport enforcePrivacyComplianceOnEvent:key:value:] : 884 -> 824
~ -[CDPDAnalyticsTransport _sendEvent:] : 476 -> 524
~ -[CDPDAnalyticsTransport _isDNUEvent:] : 72 -> 28
~ +[CDPDAnalyticsTransport transportForEvent:].cold.2 -> +[CDPDAnalyticsTransport flushTransportCache].cold.1 : 140 -> 60
~ +[CDPDAnalyticsTransport flushCaches].cold.2 -> +[CDPDAnalyticsTransport getAllEventsForDataSanitization].cold.1 : 60 -> 20
~ +[CDPDAnalyticsTransport transportForClientType:clientBundleId:clientName:].cold.1 -> +[CDPDAnalyticsTransport transportForClientType:clientBundleId:clientName:].cold.2 : 20 -> 64
~ +[CDPDAnalyticsTransport transportForClientType:clientBundleId:clientName:].cold.2 -> ___75+[CDPDAnalyticsTransport transportForClientType:clientBundleId:clientName:]_block_invoke_2.cold.1 : 64 -> 116
~ ___75+[CDPDAnalyticsTransport transportForClientType:clientBundleId:clientName:]_block_invoke_2.cold.1 -> ___75+[CDPDAnalyticsTransport transportForClientType:clientBundleId:clientName:]_block_invoke_2.cold.2 : 116 -> 136
~ ___75+[CDPDAnalyticsTransport transportForClientType:clientBundleId:clientName:]_block_invoke_2.cold.2 -> -[CDPDAnalyticsTransport _renewMissingDeviceSessionIDIfNeeded:manager:account:].cold.1 : 136 -> 140
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
