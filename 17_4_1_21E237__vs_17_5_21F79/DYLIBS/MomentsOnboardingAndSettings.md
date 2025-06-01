## MomentsOnboardingAndSettings

> `/System/Library/PrivateFrameworks/MomentsOnboardingAndSettings.framework/MomentsOnboardingAndSettings`

```diff

-130.0.11.0.0
-  __TEXT.__text: 0x17270
+130.0.19.0.0
+  __TEXT.__text: 0x17d4c
   __TEXT.__auth_stubs: 0xb40
-  __TEXT.__objc_methlist: 0x864
+  __TEXT.__objc_methlist: 0x8bc
   __TEXT.__const: 0x424
-  __TEXT.__gcc_except_tab: 0x31c
-  __TEXT.__cstring: 0x2939
-  __TEXT.__oslogstring: 0xd15
+  __TEXT.__gcc_except_tab: 0x324
+  __TEXT.__cstring: 0x2959
+  __TEXT.__oslogstring: 0xdf5
   __TEXT.__ustring: 0x8a
   __TEXT.__swift5_typeref: 0x32e
   __TEXT.__swift5_capture: 0xa4

   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_proto: 0x18
   __TEXT.__swift5_types: 0x30
-  __TEXT.__unwind_info: 0x6d4
-  __TEXT.__objc_classname: 0x281
-  __TEXT.__objc_methname: 0x32e6
-  __TEXT.__objc_methtype: 0xfba
-  __TEXT.__objc_stubs: 0x1780
+  __TEXT.__unwind_info: 0x6e8
+  __TEXT.__objc_classname: 0x283
+  __TEXT.__objc_methname: 0x33ae
+  __TEXT.__objc_methtype: 0xfc5
+  __TEXT.__objc_stubs: 0x1820
   __DATA_CONST.__got: 0x190
-  __DATA_CONST.__const: 0x660
+  __DATA_CONST.__const: 0x688
   __DATA_CONST.__objc_classlist: 0xb0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1f68
-  __DATA_CONST.__objc_selrefs: 0x9e8
+  __DATA_CONST.__objc_const: 0x1fc8
+  __DATA_CONST.__objc_selrefs: 0xa10
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_classrefs: 0x1d0
   __DATA_CONST.__objc_superrefs: 0x48
   __DATA_CONST.__objc_arraydata: 0x68
-  __AUTH_CONST.__cfstring: 0xf40
+  __AUTH_CONST.__cfstring: 0xf60
   __AUTH_CONST.__const: 0x4a8
   __AUTH_CONST.__objc_const: 0x598
   __AUTH_CONST.__objc_doubleobj: 0x10

   __AUTH_CONST.__auth_got: 0x5b0
   __AUTH.__objc_data: 0x840
   __AUTH.__data: 0x2b8
-  __DATA.__objc_ivar: 0xa0
+  __DATA.__objc_ivar: 0xa4
   __DATA.__objc_data: 0x20
   __DATA.__data: 0x4e8
   __DATA.__bss: 0x310

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: BED5D54E-CC19-3674-BA01-1055D7135322
-  Functions: 606
-  Symbols:   2108
-  CStrings:  1095
+  UUID: AD33C67E-2BFB-3472-AEF5-BD179DAE872E
+  Functions: 623
+  Symbols:   2149
+  CStrings:  1110
 
Symbols:
+ -[MOApprovedApplicationsManager _getApprovedApplicationsArrayAndRequireAccess:]
+ -[MOApprovedApplicationsManager _getApprovedApplicationsArray]
+ -[MOApprovedApplicationsManager _getApprovedApplicationsWithAccessArray]
+ -[MOApprovedApplicationsManager isClientUsingDataAccess:]
+ -[MOApprovedApplicationsManager registerClientsForDataAccess:]
+ -[MOOnboardingAndSettingsManager getClientsWithDataAccess:]
+ -[MOOnboardingAndSettingsManager isClientUsingDataAccess:]
+ -[MOOnboardingAndSettingsManager registerClientsForDataAccess:]
+ GCC_except_table37
+ GCC_except_table47
+ GCC_except_table54
+ _OBJC_IVAR_$_MOApprovedApplicationsManager._approvedApplicationsWithAccess
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ ___39-[MOOnboardingAndSettingsManager proxy]_block_invoke.122
+ ___39-[MOOnboardingAndSettingsManager proxy]_block_invoke.123
+ ___46-[MOOnboardingAndSettingsManager refreshCache]_block_invoke.131
+ ___46-[MOOnboardingAndSettingsManager refreshCache]_block_invoke_14
+ ___54-[MOOnboardingAndSettingsManager setState:forSetting:]_block_invoke.156
+ ___58-[MOOnboardingAndSettingsManager isClientUsingDataAccess:]_block_invoke
+ ___59-[MOOnboardingAndSettingsManager getClientsWithDataAccess:]_block_invoke
+ ___59-[MOOnboardingAndSettingsManager getClientsWithDataAccess:]_block_invoke.159
+ ___59-[MOOnboardingAndSettingsManager getClientsWithDataAccess:]_block_invoke.159.cold.1
+ ___59-[MOOnboardingAndSettingsManager getClientsWithDataAccess:]_block_invoke_2
+ ___59-[MOOnboardingAndSettingsManager getClientsWithDataAccess:]_block_invoke_3
+ ___59-[MOOnboardingAndSettingsManager getClientsWithDataAccess:]_block_invoke_3.cold.1
+ ___64-[MOOnboardingAndSettingsManager getApplicationsWithDataAccess:]_block_invoke.158
+ ___64-[MOOnboardingAndSettingsManager getApplicationsWithDataAccess:]_block_invoke.158.cold.1
+ ___66-[MOOnboardingAndSettingsManager _getStateForSetting:withHandler:]_block_invoke.155
+ ___66-[MOOnboardingAndSettingsManager _getStateForSetting:withHandler:]_block_invoke.155.cold.1
+ ___68-[MOOnboardingAndSettingsManager setOnboardingFlowCompletionStatus:]_block_invoke.141
+ ___69-[MOOnboardingAndSettingsManager getDiagnosticReporterConfiguration:]_block_invoke.157
+ ___69-[MOOnboardingAndSettingsManager getDiagnosticReporterConfiguration:]_block_invoke.157.cold.1
+ ___79-[MOApprovedApplicationsManager _getApprovedApplicationsArrayAndRequireAccess:]_block_invoke
+ ___80-[MOOnboardingAndSettingsManager _getOnboardingFlowCompletionStatusWithHandler:]_block_invoke.140
+ ___80-[MOOnboardingAndSettingsManager _getOnboardingFlowCompletionStatusWithHandler:]_block_invoke.140.cold.1
+ ___87-[MOOnboardingAndSettingsManager _getOnboardingFlowRefreshCompletionStatusWithHandler:]_block_invoke.145
+ ___87-[MOOnboardingAndSettingsManager _getOnboardingFlowRefreshCompletionStatusWithHandler:]_block_invoke.145.cold.1
+ ___block_descriptor_144_e8_32s40r48r56r64r72r80r88r96r104r112r120r128r136r_e5_v8?0ls32l8r40l8r48l8r56l8r64l8r72l8r80l8r88l8r96l8r104l8r112l8r120l8r128l8r136l8
+ ___block_descriptor_41_e8_32s_e29_B16?0"LSApplicationRecord"8ls32l8
+ ___block_literal_global.130
+ _objc_msgSend$_getApprovedApplicationsArray
+ _objc_msgSend$_getApprovedApplicationsArrayAndRequireAccess:
+ _objc_msgSend$_getApprovedApplicationsWithAccessArray
+ _objc_msgSend$getClientsWithDataAccess:
+ _objc_msgSend$getJournalingSuggestionsApprovedApplicationRecordForBundleIdentifier:
+ _objc_msgSend$isClientUsingDataAccess:
+ _objc_msgSend$registerClientsForDataAccess:
- -[MOApprovedApplicationsManager _getSupportedApplicationsArray]
- GCC_except_table36
- GCC_except_table46
- GCC_except_table53
- ___39-[MOOnboardingAndSettingsManager proxy]_block_invoke.117
- ___39-[MOOnboardingAndSettingsManager proxy]_block_invoke.118
- ___46-[MOOnboardingAndSettingsManager refreshCache]_block_invoke.126
- ___54-[MOOnboardingAndSettingsManager setState:forSetting:]_block_invoke.151
- ___63-[MOApprovedApplicationsManager _getSupportedApplicationsArray]_block_invoke
- ___64-[MOOnboardingAndSettingsManager getApplicationsWithDataAccess:]_block_invoke.153
- ___64-[MOOnboardingAndSettingsManager getApplicationsWithDataAccess:]_block_invoke.153.cold.1
- ___66-[MOOnboardingAndSettingsManager _getStateForSetting:withHandler:]_block_invoke.150
- ___66-[MOOnboardingAndSettingsManager _getStateForSetting:withHandler:]_block_invoke.150.cold.1
- ___68-[MOOnboardingAndSettingsManager setOnboardingFlowCompletionStatus:]_block_invoke.136
- ___69-[MOOnboardingAndSettingsManager getDiagnosticReporterConfiguration:]_block_invoke.152
- ___69-[MOOnboardingAndSettingsManager getDiagnosticReporterConfiguration:]_block_invoke.152.cold.1
- ___80-[MOOnboardingAndSettingsManager _getOnboardingFlowCompletionStatusWithHandler:]_block_invoke.135
- ___80-[MOOnboardingAndSettingsManager _getOnboardingFlowCompletionStatusWithHandler:]_block_invoke.135.cold.1
- ___87-[MOOnboardingAndSettingsManager _getOnboardingFlowRefreshCompletionStatusWithHandler:]_block_invoke.140
- ___87-[MOOnboardingAndSettingsManager _getOnboardingFlowRefreshCompletionStatusWithHandler:]_block_invoke.140.cold.1
- ___block_descriptor_136_e8_32s40r48r56r64r72r80r88r96r104r112r120r128r_e5_v8?0ls32l8r40l8r48l8r56l8r64l8r72l8r80l8r88l8r96l8r104l8r112l8r120l8r128l8
- ___block_literal_global.125
- _objc_msgSend$_getSupportedApplicationsArray
- _objc_msgSend$isJournalingSuggestionsAvailableForBundleIdentifier:
CStrings:
+ "\x02"
+ "@20@0:8B16"
+ "Client is checking data access usage..."
+ "Done registering client for data access: %@"
+ "MOStateClientsWithDataAccess"
+ "Registering client for data access: %@"
+ "_approvedApplicationsWithAccess"
+ "_getApprovedApplicationsArray"
+ "_getApprovedApplicationsArrayAndRequireAccess:"
+ "_getApprovedApplicationsWithAccessArray"
+ "getClientsWithDataAccess, count, %lu"
+ "getClientsWithDataAccess, remote process returned error: %@"
+ "getClientsWithDataAccess, result suppressed by interuption"
+ "getClientsWithDataAccess:"
+ "isClientUsingDataAccess:"
+ "registerClientsForDataAccess:"
- "Client is retrieving applications using data access..."
- "_getSupportedApplicationsArray"

```
