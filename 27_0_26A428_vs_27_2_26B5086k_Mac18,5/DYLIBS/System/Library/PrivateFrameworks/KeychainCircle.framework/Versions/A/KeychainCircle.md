## KeychainCircle

> `/System/Library/PrivateFrameworks/KeychainCircle.framework/Versions/A/KeychainCircle`

```diff

-62460.1.3.0.0
-  __TEXT.__text: 0x2b93c
+62460.40.49.501.1
+  __TEXT.__text: 0x2bbd8
   __TEXT.__lazy_helpers: 0x1a4
-  __TEXT.__objc_methlist: 0x1e2c
+  __TEXT.__objc_methlist: 0x1ebc
   __TEXT.__const: 0x110
   __TEXT.__dlopen_cstrs: 0xae
-  __TEXT.__gcc_except_tab: 0x1214
-  __TEXT.__cstring: 0x37c0
+  __TEXT.__gcc_except_tab: 0x122c
+  __TEXT.__cstring: 0x388b
   __TEXT.__oslogstring: 0x3aa9
   __TEXT.__ustring: 0x32
-  __TEXT.__unwind_info: 0xa38
+  __TEXT.__unwind_info: 0xa58
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xba0
-  __DATA_CONST.__objc_classlist: 0xa8
+  __DATA_CONST.__const: 0xbd8
+  __DATA_CONST.__objc_classlist: 0xb0
   __DATA_CONST.__objc_catlist: 0x20
-  __DATA_CONST.__objc_protolist: 0x38
+  __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1078
+  __DATA_CONST.__objc_selrefs: 0x1080
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x88
-  __DATA_CONST.__got: 0x2c0
-  __AUTH_CONST.__const: 0xa20
-  __AUTH_CONST.__cfstring: 0x3c60
-  __AUTH_CONST.__objc_const: 0x2c10
+  __DATA_CONST.__objc_superrefs: 0x98
+  __DATA_CONST.__got: 0x2c8
+  __AUTH_CONST.__const: 0xa40
+  __AUTH_CONST.__cfstring: 0x3d40
+  __AUTH_CONST.__objc_const: 0x2d90
   __AUTH_CONST.__lazy_load_got: 0x28
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__auth_got: 0x768
-  __AUTH.__objc_data: 0x578
-  __DATA.__objc_ivar: 0x214
-  __DATA.__data: 0x31c
+  __AUTH.__objc_data: 0x618
+  __DATA.__objc_ivar: 0x21c
+  __DATA.__data: 0x37c
   __DATA.__common: 0x8
-  __DATA_DIRTY.__objc_data: 0x118
-  __DATA_DIRTY.__bss: 0x30
+  __DATA_DIRTY.__objc_data: 0xc8
+  __DATA_DIRTY.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 822
-  Symbols:   2280
-  CStrings:  805
+  Functions: 829
+  Symbols:   2315
+  CStrings:  812
 
Symbols:
+ +[AAFAnalyticsEventSecurity reporterRTCAdapter]
+ +[AAFAnalyticsEventSecurity setReporterRTCAdapter:]
+ +[MetricSessionInfo sessionInfoWithAltDSID:]
+ +[MetricSessionInfo sessionInfoWithAltDSID:flowID:deviceSessionID:]
+ -[AAFAnalyticsEventSecurity initWithMetrics:session:eventName:]
+ -[AAFAnalyticsEventSecurity initWithMetrics:session:eventName:canSendMetrics:]
+ -[AAFAnalyticsEventSecurity initWithSession:eventName:]
+ -[MetricSessionInfo .cxx_destruct]
+ -[MetricSessionInfo altDSID]
+ -[MetricSessionInfo deviceSessionID]
+ -[MetricSessionInfo flowID]
+ -[MetricSessionInfo initWithAltDSID:]
+ -[MetricSessionInfo initWithAltDSID:flowID:deviceSessionID:]
+ -[SecurityAnalyticsReporterRTCActualAdapter init]
+ -[SecurityAnalyticsReporterRTCActualAdapter sendEvent:]
+ GCC_except_table565
+ GCC_except_table575
+ GCC_except_table577
+ OBJC_IVAR_$_MetricSessionInfo._altDSID
+ OBJC_IVAR_$_MetricSessionInfo._deviceSessionID
+ OBJC_IVAR_$_MetricSessionInfo._flowID
+ _OBJC_CLASS_$_MetricSessionInfo
+ _OBJC_CLASS_$_SecurityAnalyticsReporterRTCActualAdapter
+ _OBJC_METACLASS_$_MetricSessionInfo
+ _OBJC_METACLASS_$_SecurityAnalyticsReporterRTCActualAdapter
+ __OBJC_$_CLASS_METHODS_MetricSessionInfo
+ __OBJC_$_INSTANCE_METHODS_MetricSessionInfo
+ __OBJC_$_INSTANCE_METHODS_SecurityAnalyticsReporterRTCActualAdapter
+ __OBJC_$_INSTANCE_VARIABLES_MetricSessionInfo
+ __OBJC_$_PROP_LIST_MetricSessionInfo
+ __OBJC_$_PROP_LIST_SecurityAnalyticsReporterRTCActualAdapter
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SecurityAnalyticsReporterRTCAdapter
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SecurityAnalyticsReporterRTCAdapter
+ __OBJC_$_PROTOCOL_REFS_SecurityAnalyticsReporterRTCAdapter
+ __OBJC_CLASS_PROTOCOLS_$_SecurityAnalyticsReporterRTCActualAdapter
+ __OBJC_CLASS_RO_$_MetricSessionInfo
+ __OBJC_CLASS_RO_$_SecurityAnalyticsReporterRTCActualAdapter
+ __OBJC_LABEL_PROTOCOL_$_SecurityAnalyticsReporterRTCAdapter
+ __OBJC_METACLASS_RO_$_MetricSessionInfo
+ __OBJC_METACLASS_RO_$_SecurityAnalyticsReporterRTCActualAdapter
+ __OBJC_PROTOCOL_$_SecurityAnalyticsReporterRTCAdapter
+ ___47+[AAFAnalyticsEventSecurity reporterRTCAdapter]_block_invoke
+ ___55-[SecurityAnalyticsReporterRTCActualAdapter sendEvent:]_block_invoke
+ __reporterRTCAdapterOverride
+ _kSecurityRTCEventNamePrepareTDIDPresence
+ _kSecurityRTCEventNameTDLTDIDDuplicates
+ _kSecurityRTCEventNameTDLTDIDStability
+ _kSecurityRTCFieldAllowedRecordCount
+ _kSecurityRTCFieldDisallowedRecordCount
+ _kSecurityRTCFieldMachineRecordAllowed
+ _kSecurityRTCFieldStableIDDuplicateDeviceCount
+ _kSecurityRTCFieldStableTrustedDeviceIDInclusionEnabled
+ _objc_msgSend$initWithMetrics:session:eventName:
+ _objc_msgSend$initWithMetrics:session:eventName:canSendMetrics:
+ _objc_msgSend$initWithSession:eventName:
+ _objc_msgSend$reporterRTCAdapter
+ _objc_msgSend$sessionInfoWithAltDSID:flowID:deviceSessionID:
+ reporterRTCAdapter.defaultAdapter
+ reporterRTCAdapter.onceToken
+ sendEvent:.onceToken
+ sendEvent:.rtcReporter
- +[SecurityAnalyticsReporterRTC rtcAnalyticsReporter]
- -[AAFAnalyticsEventSecurity areTestsEnabled]
- -[AAFAnalyticsEventSecurity initWithCKKSMetrics:altDSID:eventName:testsAreEnabled:category:sendMetric:]
- -[AAFAnalyticsEventSecurity initWithKeychainCircleMetrics:altDSID:eventName:category:]
- -[AAFAnalyticsEventSecurity initWithKeychainCircleMetrics:altDSID:flowID:deviceSessionID:eventName:testsAreEnabled:canSendMetrics:category:]
- -[AAFAnalyticsEventSecurity setAreTestsEnabled:]
- GCC_except_table568
- GCC_except_table578
- GCC_except_table580
- OBJC_IVAR_$_AAFAnalyticsEventSecurity._areTestsEnabled
- _MetricsDisable
- _MetricsEnable
- _MetricsOverrideTestsAreEnabled
- _OBJC_CLASS_$_SecurityAnalyticsReporterRTC
- _OBJC_METACLASS_$_SecurityAnalyticsReporterRTC
- __OBJC_$_CLASS_METHODS_SecurityAnalyticsReporterRTC
- __OBJC_CLASS_RO_$_SecurityAnalyticsReporterRTC
- __OBJC_METACLASS_RO_$_SecurityAnalyticsReporterRTC
- ___52+[SecurityAnalyticsReporterRTC rtcAnalyticsReporter]_block_invoke
- _kSecurityRTCEventNameTDLDuplicateStableID
- _metricsAreEnabled
- _objc_msgSend$areTestsEnabled
- _objc_msgSend$initWithKeychainCircleMetrics:altDSID:flowID:deviceSessionID:eventName:testsAreEnabled:canSendMetrics:category:
- _objc_msgSend$rtcAnalyticsReporter
- rtcAnalyticsReporter.onceToken
- rtcAnalyticsReporter.rtcReporter
CStrings:
+ "allowedRecordCount"
+ "com.apple.security.prepareTDIDPresence"
+ "com.apple.security.tdlTDIDDuplicates"
+ "com.apple.security.tdlTDIDStability"
+ "disallowedRecordCount"
+ "machineRecordAllowed"
+ "stableIDDuplicateDeviceCount"
+ "stableTrustedDeviceIDInclusionEnabled"
- "com.apple.security.tdlDuplicateStableID"
```
