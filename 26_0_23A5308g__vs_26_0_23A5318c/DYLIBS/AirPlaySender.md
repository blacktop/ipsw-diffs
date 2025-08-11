## AirPlaySender

> `/System/Library/PrivateFrameworks/AirPlaySender.framework/AirPlaySender`

```diff

-890.77.2.0.0
-  __TEXT.__text: 0x211048
-  __TEXT.__auth_stubs: 0x55d0
+890.79.1.1.0
+  __TEXT.__text: 0x211d58
+  __TEXT.__auth_stubs: 0x55f0
   __TEXT.__objc_methlist: 0x7c4
-  __TEXT.__cstring: 0x8263f
+  __TEXT.__cstring: 0x82cd5
   __TEXT.__const: 0x10070
   __TEXT.__gcc_except_tab: 0x96c
   __TEXT.__dlopen_cstrs: 0x61d
   __TEXT.__oslogstring: 0x7c5
-  __TEXT.__unwind_info: 0x51f8
+  __TEXT.__unwind_info: 0x51e0
   __TEXT.__objc_classname: 0x1c5
   __TEXT.__objc_methname: 0x2116
   __TEXT.__objc_methtype: 0xd78
   __TEXT.__objc_stubs: 0x1da0
   __DATA_CONST.__got: 0x1f78
-  __DATA_CONST.__const: 0x6b28
+  __DATA_CONST.__const: 0x6ba0
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x48

   __DATA_CONST.__objc_selrefs: 0x9b0
   __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_arraydata: 0x88
-  __AUTH_CONST.__auth_got: 0x2af8
+  __AUTH_CONST.__auth_got: 0x2b08
   __AUTH_CONST.__const: 0x7f00
-  __AUTH_CONST.__cfstring: 0x12660
+  __AUTH_CONST.__cfstring: 0x128a0
   __AUTH_CONST.__objc_const: 0xec0
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_intobj: 0x48

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F03CA2D5-B16A-3BCF-98B8-5475AA4479A9
-  Functions: 9767
-  Symbols:   24578
-  CStrings:  13435
+  UUID: 0430B07A-B797-3BA8-9E57-62D92135962D
+  Functions: 9773
+  Symbols:   24597
+  CStrings:  13489
 
Symbols:
+ _APMulticastProbeSenderUnregister.cold.16
+ _APMulticastProbeSenderUnregister.cold.17
+ _APMulticastProbeSenderUnregister.cold.18
+ _APMulticastProbeSenderUnregister.cold.19
+ _FigCFDictionarySetUInt64
+ ___APMulticastProbeSenderGetShared_block_invoke.cold.5
+ ___APMulticastProbeSenderGetShared_block_invoke.cold.6
+ ___APMulticastProbeSenderGetShared_block_invoke.cold.7
+ ___APMulticastProbeSenderGetShared_block_invoke.cold.8
+ ___block_descriptor_tmp.146
+ ___block_descriptor_tmp.153
+ ___block_descriptor_tmp.159
+ ___block_descriptor_tmp.587
+ ___block_descriptor_tmp.623
+ ___block_literal_global.148
+ ___block_literal_global.155
+ ___multicastProbeSender_createMC2UCProbingTimer_block_invoke
+ ___multicastProbeSender_createMC2UCProbingTimer_block_invoke_2
+ ___multicastProbeSender_probeForMC2UC_block_invoke
+ _multicastProbeSender_probeForMC2UC
+ _os_eligibility_get_domain_answer
- _APMulticastProbeSenderUpdateMC2UC.cold.1
- _APMulticastProbeSenderUpdateMC2UC.cold.2
- _APMulticastProbeSenderUpdateMC2UC.cold.3
- _APMulticastProbeSenderUpdateMC2UC.cold.4
- ___block_descriptor_tmp.580
- ___block_descriptor_tmp.616
- ___block_literal_global.89
- ___block_literal_global.96
- _multicastProbeSender_registerDeviceForAddressFamily.cold.13
- _multicastProbeSender_registerDeviceForAddressFamily.cold.14
- _multicastProbeSender_registerDeviceForAddressFamily.cold.15
- _multicastProbeSender_registerDeviceForAddressFamily.cold.16
- _multicastProbeSender_registerDeviceForAddressFamily.cold.17
- _multicastProbeSender_registerDeviceForAddressFamily.cold.18
- _multicastProbeSender_registerDeviceForAddressFamily.cold.19
- _multicastProbeSender_registerDeviceForAddressFamily.cold.20
- _multicastProbeSender_registerDeviceForAddressFamily.cold.21
- _multicastProbeSender_registerDeviceForAddressFamily.cold.22
- _multicastProbeSender_registerDeviceForAddressFamily.cold.23
- _multicastProbeSender_registerDeviceForAddressFamily.cold.24
- _multicastProbeSender_registerDeviceForAddressFamily.cold.25
CStrings:
+ "\tDetection stats\t: \"Percentage of time (Enabled) [IPv6]\" = %u%%\n"
+ "\tDetection stats\t: \"Percentage of time (Enabled)\" = %u%%\n"
+ "\tDetection stats : \"Percentage of time (Disabled) [IPv6]\" = %u%%\n"
+ "\tDetection stats : \"Percentage of time (Disabled)\" = %u%%\n"
+ "\tDetection stats : \"Status flip count [IPv6]\" = %d\n"
+ "\tDetection stats : \"Status flip count\" = %d\n"
+ "890.79.1.1"
+ "AirPlayMulticastProbeSenderQueue"
+ "Boolean apsession_isEligibleForPWDKeyExchange(void)"
+ "MC2UCDisabledTotalTimeTicks"
+ "MC2UCDisabledTotalTimeTicksIPv6"
+ "MC2UCEnabledTotalTimeTicks"
+ "MC2UCEnabledTotalTimeTicksIPv6"
+ "MC2UCInterfaceName"
+ "MC2UCLastStatusChangeTimeTicks"
+ "MC2UCLastStatusChangeTimeTicksIPv6"
+ "MC2UCStatusFlipCount"
+ "MC2UCStatusFlipCountIPv6"
+ "MC2UCStatusLatest"
+ "MC2UCStatusLatestIPv6"
+ "OSStatus multicastProbeSender_constructMulticastGroupInfoForAddressFamily(APMulticastProbeSenderRef, CFStringRef, sa_family_t, CFMutableDictionaryRef *)"
+ "OSStatus multicastProbeSender_createMC2UCProbingTimer(APMulticastProbeSenderRef)"
+ "OSStatus multicastProbeSender_probeForMC2UC(CMBaseObjectRef, sa_family_t)"
+ "OSStatus multicastProbeSender_probeForMC2UC(CMBaseObjectRef, sa_family_t)_block_invoke"
+ "[%{ptr}] MC2UC periodic probing timer created.\n"
+ "[%{ptr}] MC2UC probing periodic timer is resumed.\n"
+ "[%{ptr}] MC2UC probing periodic timer stopped.\n"
+ "[%{ptr}] [IPv%u] Updated Tx probe packet count for '%@' with TxProbePktsCount=%d.\n"
+ "[%{ptr}] [IPv4] MC2UC status for [%@] changed from old MC2UCStatus=%s to new MC2UCStatus=%s, MC2UCProbeBurstID=%d, timeSinceLastStateChange=%lus, TotalTimeSpentSoFarInStatus[%s]=%lus, statusFlipCount=%d.\n"
+ "[%{ptr}] [IPv6] MC2UC status for [%@] changed from old MC2UCStatus=%s to new MC2UCStatus=%s, MC2UCProbeBurstID=%d, timeSinceLastStateChange=%lus, TotalTimeSpentSoFarInStatus[%s]=%lus, statusFlipCount=%d\n"
+ "eligible"
+ "enable_pwd_for_3p"
+ "multicastProbeSender_createMC2UCProbingTimer"
+ "multicastProbeSender_probeForMC2UC_block_invoke"
+ "multicastToUnicastIPv6PercentageOfDisabledTime"
+ "multicastToUnicastIPv6PercentageOfEnabledTime"
+ "multicastToUnicastIPv6StatusFlipCount"
+ "multicastToUnicastPercentageOfDisabledTime"
+ "multicastToUnicastPercentageOfEnabledTime"
+ "multicastToUnicastStatusFlipCount"
+ "not eligible"
+ "os_eligibility for the PWD Key exchange is %s.\n"
+ "os_eligibility_get_domain_answer failed with errno %d: %s"
- "890.77.2"
- "OSStatus multicastProbeSender_constructMulticastGroupInfoForAddressFamily(APMulticastProbeSenderRef, const char *, sa_family_t, CFMutableDictionaryRef *)"
- "OSStatus multicastProbeSender_probeForMC2UC(CMBaseObjectRef, const char *, sa_family_t)"
- "[%{ptr}] Failed to retrieve the socket fd for ifaceName_addressFamily='%@' with err=%#m\n"
- "[%{ptr}] Updated Tx probe packet count for '%@' with TxProbePktsCount=%d [IPv%u].\n"
- "int multicastProbeSender_socketForMC2UCProbing(APMulticastProbeSenderRef, const char *, sa_family_t)"
- "multicastProbeSender_socketForMC2UCProbing"

```
