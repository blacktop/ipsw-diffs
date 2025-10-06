## CoreCDPInternal

> `/System/Library/PrivateFrameworks/CoreCDPInternal.framework/CoreCDPInternal`

```diff

-416.125.2.0.0
-  __TEXT.__text: 0x85fb0
+416.125.6.0.0
+  __TEXT.__text: 0x86420
   __TEXT.__auth_stubs: 0x11b0
-  __TEXT.__objc_methlist: 0x50c4
-  __TEXT.__const: 0x6e8
-  __TEXT.__oslogstring: 0x1215e
-  __TEXT.__cstring: 0xd225
+  __TEXT.__objc_methlist: 0x50fc
+  __TEXT.__const: 0x718
+  __TEXT.__oslogstring: 0x121ce
+  __TEXT.__cstring: 0xd295
   __TEXT.__gcc_except_tab: 0xa00
   __TEXT.__dlopen_cstrs: 0xb0
   __TEXT.__swift5_typeref: 0x37f

   __TEXT.__swift5_capture: 0x200
   __TEXT.__swift_as_entry: 0x60
   __TEXT.__swift_as_ret: 0x58
-  __TEXT.__unwind_info: 0x1b28
+  __TEXT.__unwind_info: 0x1b38
   __TEXT.__eh_frame: 0x910
   __TEXT.__objc_classname: 0xc99
-  __TEXT.__objc_methname: 0xe65d
+  __TEXT.__objc_methname: 0xe71e
   __TEXT.__objc_methtype: 0x260b
-  __TEXT.__objc_stubs: 0xb960
+  __TEXT.__objc_stubs: 0xba20
   __DATA_CONST.__got: 0xfe8
   __DATA_CONST.__const: 0x2138
   __DATA_CONST.__objc_classlist: 0x290
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x180
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x34f0
+  __DATA_CONST.__objc_selrefs: 0x3518
   __DATA_CONST.__objc_protorefs: 0x50
   __DATA_CONST.__objc_superrefs: 0x158
-  __DATA_CONST.__objc_arraydata: 0x150
+  __DATA_CONST.__objc_arraydata: 0x158
   __AUTH_CONST.__auth_got: 0x8e8
-  __AUTH_CONST.__const: 0xa70
-  __AUTH_CONST.__cfstring: 0x8640
+  __AUTH_CONST.__const: 0xab0
+  __AUTH_CONST.__cfstring: 0x8680
   __AUTH_CONST.__objc_const: 0xf870
   __AUTH_CONST.__objc_intobj: 0x150
-  __AUTH_CONST.__objc_arrayobj: 0x90
-  __AUTH.__objc_data: 0x10e8
-  __AUTH.__data: 0x128
+  __AUTH_CONST.__objc_arrayobj: 0xa8
+  __AUTH.__objc_data: 0x1020
+  __AUTH.__data: 0x50
   __DATA.__objc_ivar: 0x394
-  __DATA.__data: 0x1210
-  __DATA.__bss: 0x450
-  __DATA_DIRTY.__objc_data: 0x998
-  __DATA_DIRTY.__data: 0x78
-  __DATA_DIRTY.__bss: 0x158
+  __DATA.__data: 0x11d0
+  __DATA.__bss: 0x470
+  __DATA_DIRTY.__objc_data: 0xa60
+  __DATA_DIRTY.__data: 0x190
+  __DATA_DIRTY.__bss: 0x168
   __DATA_DIRTY.__common: 0x18
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 8CF2705F-7E7B-3FA7-A5BA-54A7662D72D9
-  Functions: 2852
-  Symbols:   9293
-  CStrings:  6090
+  UUID: 4E1C6577-F480-3D90-826C-9A47ED268600
+  Functions: 2861
+  Symbols:   9324
+  CStrings:  6099
 
Symbols:
+ +[CDPDAnalyticsTransport getAllEventsForDataSanitization]
+ +[CDPDAnalyticsTransport getAllEventsForDataSanitization].cold.1
+ +[CDPDAnalyticsTransport getAllowedStringsForInternalTelemetry]
+ +[CDPDAnalyticsTransport getAllowedStringsForInternalTelemetry].cold.1
+ -[CDPDAnalyticsTransport sanitizeEventForInternalReporting:key:value:]
+ -[CDPDAnalyticsTransport santizeEventForPendingCFUType:value:]
+ -[CDPDAnalyticsTransport shouldSanitizeEventForInternalReporting:]
+ GCC_except_table62
+ ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.2114
+ ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.2114.cold.1
+ ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.2115
+ ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.2115.cold.1
+ ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.2178
+ ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.2178.cold.1
+ ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.2178.cold.2
+ ___37-[CDPDAnalyticsTransport _sendEvent:]_block_invoke_2
+ ___57+[CDPDAnalyticsTransport getAllEventsForDataSanitization]_block_invoke
+ ___63+[CDPDAnalyticsTransport getAllowedStringsForInternalTelemetry]_block_invoke
+ ___81-[CDPDAnalyticsTransport configureSessionForEvent:sendEventBlock:telemetryQueue:]_block_invoke.2179
+ ___81-[CDPDAnalyticsTransport configureSessionForEvent:sendEventBlock:telemetryQueue:]_block_invoke_2.2181
+ ___81-[CDPDAnalyticsTransport configureSessionForEvent:sendEventBlock:telemetryQueue:]_block_invoke_2.2181.cold.1
+ ___block_literal_global.1024
+ ___block_literal_global.1128
+ ___block_literal_global.1172
+ ___block_literal_global.1249
+ ___block_literal_global.1278
+ ___block_literal_global.2081
+ ___block_literal_global.2093
+ ___block_literal_global.2095
+ ___block_literal_global.2111
+ ___block_literal_global.2183
+ ___block_literal_global.510
+ _allowedStringsForInternalTelemetry
+ _getAllEventsForDataSanitization.eventsForDataSanitization
+ _getAllEventsForDataSanitization.onceToken
+ _getAllowedStringsForInternalTelemetry.allowedAttributesDict
+ _getAllowedStringsForInternalTelemetry.onceToken
+ _objc_msgSend$_continueRepairCloudDataProtectionStateWithCompletion:
+ _objc_msgSend$getAllEventsForDataSanitization
+ _objc_msgSend$getAllowedStringsForInternalTelemetry
+ _objc_msgSend$sanitizeEventForInternalReporting:key:value:
+ _objc_msgSend$santizeEventForPendingCFUType:value:
+ _objc_msgSend$shouldSanitizeEventForInternalReporting:
- GCC_except_table55
- ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.2101
- ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.2101.cold.1
- ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.2102
- ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.2102.cold.1
- ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.2165
- ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.2165.cold.1
- ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.2165.cold.2
- ___81-[CDPDAnalyticsTransport configureSessionForEvent:sendEventBlock:telemetryQueue:]_block_invoke.2166
- ___81-[CDPDAnalyticsTransport configureSessionForEvent:sendEventBlock:telemetryQueue:]_block_invoke_2.2168
- ___81-[CDPDAnalyticsTransport configureSessionForEvent:sendEventBlock:telemetryQueue:]_block_invoke_2.2168.cold.1
- ___block_literal_global.1002
- ___block_literal_global.1117
- ___block_literal_global.1161
- ___block_literal_global.1238
- ___block_literal_global.1267
- ___block_literal_global.2070
- ___block_literal_global.2082
- ___block_literal_global.2098
- ___block_literal_global.2170
- ___block_literal_global.496
CStrings:
+ "%@: Could not find a record matching serial number (%{sensitive}@) with source (%{public}ld)."
+ "%@: First usable record matching the serial number (%{sensitive}@) with source (%{public}ld) is (%{sensitive}@)"
+ "%{public}@: Processing device escrow record with id: %{mask.hash}@ (name: '%@', serial: %{sensitive}@)"
+ "%{public}@: Skipping record with serial number (%{sensitive}@). This device has a serial number of (%{sensitive}@)"
+ "%{public}@: There are no usable records for the local device matching serial number (%{sensitive}@)"
+ "Follow up factory manatee check returned an error for altDSID %{sensitive}@: %{public}@"
+ "Skipping account preflight for %{sensitive}@ due to presence of beneficiary identifier: %{mask.hash}@"
+ "Updating Walrus status for account %{sensitive}@, initiating silent auth."
+ "com.apple.security.escrowRepairOperationPasscodeChanged"
+ "com.apple.security.escrowRepairOperationPasscodeUnlocked"
+ "getAllEventsForDataSanitization"
+ "getAllowedStringsForInternalTelemetry"
+ "sanitizeEventForInternalReporting:key:value:"
+ "santizeEventForPendingCFUType:value:"
+ "shouldSanitizeEventForInternalReporting:"
- "%@: Could not find a record matching serial number (%@) with source (%{public}ld)."
- "%@: First usable record matching the serial number (%@) with source (%{public}ld) is (%@)"
- "%{public}@: Processing device escrow record with id: %{mask.hash}@ (name: '%@', serial: %@)"
- "%{public}@: Skipping record with serial number (%@). This device has a serial number of (%@)"
- "%{public}@: There are no usable records for the local device matching serial number (%@)"
- "Follow up factory manatee check returned an error for altDSID %@: %{public}@"
- "Skipping account preflight for %@ due to presence of beneficiary identifier: %{mask.hash}@"
- "Updating Walrus status for account %@, initiating silent auth."

```
