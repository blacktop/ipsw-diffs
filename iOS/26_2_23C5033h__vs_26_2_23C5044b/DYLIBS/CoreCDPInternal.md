## CoreCDPInternal

> `/System/Library/PrivateFrameworks/CoreCDPInternal.framework/CoreCDPInternal`

```diff

-416.250.2.0.0
-  __TEXT.__text: 0x86da8
+416.250.4.0.0
+  __TEXT.__text: 0x8714c
   __TEXT.__auth_stubs: 0x11b0
-  __TEXT.__objc_methlist: 0x511c
+  __TEXT.__objc_methlist: 0x5144
   __TEXT.__const: 0x7d0
-  __TEXT.__oslogstring: 0x123ee
-  __TEXT.__cstring: 0xd2b5
-  __TEXT.__gcc_except_tab: 0xa00
+  __TEXT.__oslogstring: 0x1240e
+  __TEXT.__cstring: 0xd3a5
+  __TEXT.__gcc_except_tab: 0xa2c
   __TEXT.__dlopen_cstrs: 0xb0
   __TEXT.__swift5_typeref: 0x37f
   __TEXT.__swift5_fieldmd: 0x80

   __TEXT.__swift5_capture: 0x200
   __TEXT.__swift_as_entry: 0x60
   __TEXT.__swift_as_ret: 0x58
-  __TEXT.__unwind_info: 0x1b50
+  __TEXT.__unwind_info: 0x1b70
   __TEXT.__eh_frame: 0x910
   __TEXT.__objc_classname: 0xc99
-  __TEXT.__objc_methname: 0xe779
+  __TEXT.__objc_methname: 0xe80a
   __TEXT.__objc_methtype: 0x260b
-  __TEXT.__objc_stubs: 0xbac0
-  __DATA_CONST.__got: 0xfe8
-  __DATA_CONST.__const: 0x2140
+  __TEXT.__objc_stubs: 0xbb60
+  __DATA_CONST.__got: 0xff8
+  __DATA_CONST.__const: 0x2168
   __DATA_CONST.__objc_classlist: 0x290
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x180
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3538
+  __DATA_CONST.__objc_selrefs: 0x3568
   __DATA_CONST.__objc_protorefs: 0x50
   __DATA_CONST.__objc_superrefs: 0x158
-  __DATA_CONST.__objc_arraydata: 0x158
+  __DATA_CONST.__objc_arraydata: 0x160
   __AUTH_CONST.__auth_got: 0x8e8
   __AUTH_CONST.__const: 0xab0
-  __AUTH_CONST.__cfstring: 0x8680
+  __AUTH_CONST.__cfstring: 0x8800
   __AUTH_CONST.__objc_const: 0xf890
-  __AUTH_CONST.__objc_intobj: 0x150
+  __AUTH_CONST.__objc_intobj: 0x168
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH.__objc_data: 0x1020
   __AUTH.__data: 0x58
   __DATA.__objc_ivar: 0x394
   __DATA.__data: 0x1210
-  __DATA.__bss: 0x470
+  __DATA.__bss: 0x460
   __DATA_DIRTY.__objc_data: 0xa60
   __DATA_DIRTY.__data: 0x140
   __DATA_DIRTY.__bss: 0x168

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 2D7AA5E0-04C7-32F9-9688-986E02513199
-  Functions: 2869
-  Symbols:   9346
-  CStrings:  6111
+  UUID: 450AE2C3-0A07-3AA7-8401-7DE2F1CBDE3C
+  Functions: 2874
+  Symbols:   9367
+  CStrings:  6143
 
Symbols:
+ +[CDPDAnalyticsTransport getDNUAllowedCfuTypes]
+ +[CDPDAnalyticsTransport getDNUAllowedCfuTypes].cold.1
+ -[CDPDAnalyticsTransport _allowedCFUStringsForEvent:]
+ -[CDPDAnalyticsTransport _isDNUEvent:]
+ -[CDPDAnalyticsTransport _sanitizeCFUStrings:allowedStrings:]
+ -[CDPDAnalyticsTransport _sanitizeCFUTypesInEvent:]
+ -[CDPDAnalyticsTransport sanitizeEventForSEPBasedEscrowRepairRateLimitDaysLeftForEvent:attribute:]
+ -[CDPDAnalyticsTransport sanitizeEventForSEPBasedEscrowRepairRateLimitDaysLeftForEvent:attribute:].cold.1
+ -[CDPDClientHandler synchronizeUserVisibleKeychainSyncEligibilityForContext:completion:].cold.1
+ -[CDPDOctagonTrustProxyImpl _cdpSepBasedEscrowRepairStateFromEscrowCheckCallResult:]
+ GCC_except_table63
+ ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.2151
+ ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.2151.cold.1
+ ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.2152
+ ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.2152.cold.1
+ ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.2215
+ ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.2215.cold.1
+ ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.2215.cold.2
+ ___47+[CDPDAnalyticsTransport getDNUAllowedCfuTypes]_block_invoke
+ ___61-[CDPDAnalyticsTransport _sanitizeCFUStrings:allowedStrings:]_block_invoke
+ ___68-[CDPDOctagonTrustProxyImpl escrowCheckWithIsBackground:completion:]_block_invoke.35
+ ___81-[CDPDAnalyticsTransport configureSessionForEvent:sendEventBlock:telemetryQueue:]_block_invoke.2216
+ ___81-[CDPDAnalyticsTransport configureSessionForEvent:sendEventBlock:telemetryQueue:]_block_invoke_2.2218
+ ___81-[CDPDAnalyticsTransport configureSessionForEvent:sendEventBlock:telemetryQueue:]_block_invoke_2.2218.cold.1
+ ___block_descriptor_40_e8_32s_e21_B24?0"NSString"8Q16ls32l8
+ ___block_descriptor_64_e8_32s40s48bs56r_e45_v24?0"OTEscrowCheckCallResult"8"NSError"16ls32l8s48l8r56l8s40l8
+ ___block_literal_global.1016
+ ___block_literal_global.1027
+ ___block_literal_global.1131
+ ___block_literal_global.1175
+ ___block_literal_global.1210
+ ___block_literal_global.1287
+ ___block_literal_global.1316
+ ___block_literal_global.2119
+ ___block_literal_global.2131
+ ___block_literal_global.2148
+ ___block_literal_global.2220
+ ___block_literal_global.513
+ _getDNUAllowedCfuTypes.dnuApprovedCFUTypes
+ _getDNUAllowedCfuTypes.onceToken
+ _kCDPAnalyticsSEPBasedEscrowRepairRateLimitDaysLeft
+ _kCDPAnalyticsSEPBasedEscrowRepairState
+ _objc_msgSend$_allowedCFUStringsForEvent:
+ _objc_msgSend$_cdpSepBasedEscrowRepairStateFromEscrowCheckCallResult:
+ _objc_msgSend$_isDNUEvent:
+ _objc_msgSend$_sanitizeCFUStrings:allowedStrings:
+ _objc_msgSend$_sanitizeCFUTypesInEvent:
+ _objc_msgSend$daysLeftOnRateLimit
+ _objc_msgSend$getDNUAllowedCfuTypes
+ _objc_msgSend$isManagedAccount
+ _objc_msgSend$rateLimitState
+ _objc_msgSend$sanitizeEventForSEPBasedEscrowRepairRateLimitDaysLeftForEvent:attribute:
- +[CDPDAnalyticsTransport getAllowedStringsForInternalTelemetry]
- +[CDPDAnalyticsTransport getAllowedStringsForInternalTelemetry].cold.1
- -[CDPDAnalyticsTransport sanitizeEventForInternalReporting:key:value:]
- -[CDPDAnalyticsTransport santizeEventForPendingCFUType:value:]
- -[CDPDAnalyticsTransport shouldSanitizeEventForInternalReporting:]
- GCC_except_table62
- ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.2114
- ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.2114.cold.1
- ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.2115
- ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.2115.cold.1
- ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.2178
- ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.2178.cold.1
- ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.2178.cold.2
- ___37-[CDPDAnalyticsTransport _sendEvent:]_block_invoke_2
- ___63+[CDPDAnalyticsTransport getAllowedStringsForInternalTelemetry]_block_invoke
- ___68-[CDPDOctagonTrustProxyImpl escrowCheckWithIsBackground:completion:]_block_invoke.32
- ___81-[CDPDAnalyticsTransport configureSessionForEvent:sendEventBlock:telemetryQueue:]_block_invoke.2179
- ___81-[CDPDAnalyticsTransport configureSessionForEvent:sendEventBlock:telemetryQueue:]_block_invoke_2.2181
- ___81-[CDPDAnalyticsTransport configureSessionForEvent:sendEventBlock:telemetryQueue:]_block_invoke_2.2181.cold.1
- ___block_descriptor_72_e8_32s40s48bs56r64r_e45_v24?0"OTEscrowCheckCallResult"8"NSError"16lr56l8s32l8s40l8r64l8s48l8
- ___block_literal_global.1013
- ___block_literal_global.1024
- ___block_literal_global.1128
- ___block_literal_global.1172
- ___block_literal_global.1249
- ___block_literal_global.1278
- ___block_literal_global.2081
- ___block_literal_global.2093
- ___block_literal_global.2095
- ___block_literal_global.2111
- ___block_literal_global.2183
- ___block_literal_global.510
- _allowedStringsForInternalTelemetry
- _getAllowedStringsForInternalTelemetry.allowedAttributesDict
- _getAllowedStringsForInternalTelemetry.onceToken
- _objc_msgSend$getAllEventsForDataSanitization
- _objc_msgSend$getAllowedStringsForInternalTelemetry
- _objc_msgSend$sanitizeEventForInternalReporting:key:value:
- _objc_msgSend$santizeEventForPendingCFUType:value:
- _objc_msgSend$shouldSanitizeEventForInternalReporting:
CStrings:
+ "B24@?0@\"NSString\"8Q16"
+ "Received not approved data for event %@ attribute %@"
+ "Shared iPad not allowed for keychain sync"
+ "_allowedCFUStringsForEvent:"
+ "_cdpSepBasedEscrowRepairStateFromEscrowCheckCallResult:"
+ "_isDNUEvent:"
+ "_sanitizeCFUStrings:allowedStrings:"
+ "_sanitizeCFUTypesInEvent:"
+ "accountReclaim"
+ "addPhoneNumber"
+ "adpUnEnroll"
+ "cancelBeneficiaryClaim"
+ "changePhoneNumber"
+ "com.apple.appleaccount.addAbsintheHeader"
+ "daysLeftOnRateLimit"
+ "getDNUAllowedCfuTypes"
+ "isManagedAccount"
+ "rateLimitState"
+ "resetPassword"
+ "sanitizeEventForSEPBasedEscrowRepairRateLimitDaysLeftForEvent:attribute:"
+ "securityUpdate"
+ "securityUpgrade"
+ "simSwapUpdatePhoneNumber"
+ "verifyPhoneNumber"
+ "verifyPrimaryEmail"
- "Unapproved CFUType %@ received in telemetry for %@ attribute"
- "getAllowedStringsForInternalTelemetry"
- "sanitizeEventForInternalReporting:key:value:"
- "santizeEventForPendingCFUType:value:"
- "shouldSanitizeEventForInternalReporting:"

```
