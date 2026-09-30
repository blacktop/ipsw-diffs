## PowerUI

> `/System/Library/PrivateFrameworks/PowerUI.framework/PowerUI`

```diff

-696.60.4.0.0
-  __TEXT.__text: 0xd3504
-  __TEXT.__auth_stubs: 0xb20
-  __TEXT.__objc_methlist: 0x1cba4
-  __TEXT.__const: 0x638
-  __TEXT.__cstring: 0xee56
-  __TEXT.__oslogstring: 0xd41b
-  __TEXT.__gcc_except_tab: 0x12cc
-  __TEXT.__unwind_info: 0x1ff8
+702.100.14.0.0
+  __TEXT.__text: 0xdc6a0
+  __TEXT.__auth_stubs: 0xae0
+  __TEXT.__objc_methlist: 0x1cce4
+  __TEXT.__const: 0x670
+  __TEXT.__cstring: 0xee92
+  __TEXT.__oslogstring: 0xd806
+  __TEXT.__gcc_except_tab: 0x12b8
+  __TEXT.__unwind_info: 0x27a0
   __TEXT.__objc_classname: 0xd3a
-  __TEXT.__objc_methname: 0x3f7b3
-  __TEXT.__objc_methtype: 0x422d
-  __TEXT.__objc_stubs: 0xd660
+  __TEXT.__objc_methname: 0x3fa59
+  __TEXT.__objc_methtype: 0x4267
+  __TEXT.__objc_stubs: 0xd720
   __DATA_CONST.__got: 0x558
-  __DATA_CONST.__const: 0x15c8
+  __DATA_CONST.__const: 0x1618
   __DATA_CONST.__objc_classlist: 0x3b0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5960
+  __DATA_CONST.__objc_selrefs: 0x59e0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x380
-  __DATA_CONST.__objc_arraydata: 0x7188
-  __AUTH_CONST.__auth_got: 0x5a0
+  __DATA_CONST.__objc_arraydata: 0x71c0
+  __AUTH_CONST.__auth_got: 0x580
   __AUTH_CONST.__const: 0x6a0
-  __AUTH_CONST.__cfstring: 0xd260
-  __AUTH_CONST.__objc_const: 0x39290
-  __AUTH_CONST.__objc_intobj: 0xa38
-  __AUTH_CONST.__objc_arrayobj: 0x4b0
+  __AUTH_CONST.__cfstring: 0xd2e0
+  __AUTH_CONST.__objc_const: 0x393c0
+  __AUTH_CONST.__objc_intobj: 0xa68
+  __AUTH_CONST.__objc_arrayobj: 0x4e0
   __AUTH_CONST.__objc_dictobj: 0x2d0
   __AUTH_CONST.__objc_doubleobj: 0xd0
   __AUTH_CONST.__objc_floatobj: 0x10
-  __AUTH.__objc_data: 0x1b30
-  __DATA.__objc_ivar: 0x3de8
+  __AUTH.__objc_data: 0x1ae0
+  __DATA.__objc_ivar: 0x3df8
   __DATA.__data: 0x6c8
   __DATA.__bss: 0xd0
-  __DATA_DIRTY.__objc_data: 0x9b0
+  __DATA_DIRTY.__objc_data: 0xa00
   __DATA_DIRTY.__data: 0x20
   __DATA_DIRTY.__bss: 0x1d8
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8DAA23C7-4342-3BE3-8FFC-85CF58E21E69
-  Functions: 10330
-  Symbols:   28404
-  CStrings:  9652
+  UUID: 72EF0141-4F35-31AD-814D-15858D2B6E08
+  Functions: 10384
+  Symbols:   28620
+  CStrings:  9706
 
Symbols:
+ +[PowerUIAudioAccessorySmartChargeManager readArrayForPreferenceKey:].cold.1
+ +[PowerUISmartChargeUtilities dateForPreferenceKey:inDomain:].cold.1
+ +[PowerUISmartChargeUtilities numberForPreferenceKey:inDomain:].cold.1
+ +[PowerUISmartChargeUtilities readDictForPreferenceKey:inDomain:].cold.1
+ +[PowerUISmartChargeUtilities readStringForPreferenceKey:inDomain:].cold.1
+ -[PowerUIChargingController readNumberForPreferenceKey:].cold.1
+ -[PowerUISmartChargeClient availableChargeLimitsWithError:]
+ -[PowerUISmartChargeClient availableChargeLimitsWithHandler:]
+ -[PowerUISmartChargeClient temporarilyOverrideMCLTargetSoC:error:]
+ -[PowerUISmartChargeClient temporarilyOverrideMCLTargetSoC:withHandler:]
+ -[PowerUISmartChargeManager availableChargeLimitsWithHandler:]
+ -[PowerUISmartChargeManager availableChargeLimits]
+ -[PowerUISmartChargeManager clearMCLOverride]
+ -[PowerUISmartChargeManager client:temporarilyOverrideMCLTargetSoC:withHandler:]
+ -[PowerUISmartChargeManager client:temporarilyOverrideMCLTargetSoC:withHandler:].cold.1
+ -[PowerUISmartChargeManager client:temporarilyOverrideMCLTargetSoC:withHandler:].cold.2
+ -[PowerUISmartChargeManager deocCacheCurrentStateLock]
+ -[PowerUISmartChargeManager loadModeOfOperation]
+ -[PowerUISmartChargeManager mclOverridenUntilDate]
+ -[PowerUISmartChargeManager modeOfOperation]
+ -[PowerUISmartChargeManager readDateForPreferenceKey:].cold.1
+ -[PowerUISmartChargeManager readNumberForPreferenceKey:].cold.1
+ -[PowerUISmartChargeManager readStringForPreferenceKey:].cold.1
+ -[PowerUISmartChargeManager savedMCLTargetSoC]
+ -[PowerUISmartChargeManager setDeocCacheCurrentStateLock:]
+ -[PowerUISmartChargeManager setFullChargeDeadline:forDesktopMode:]
+ -[PowerUISmartChargeManager setMclOverridenUntilDate:]
+ -[PowerUISmartChargeManager setModeOfOperation:]
+ -[PowerUISmartChargeManager setSavedMCLTargetSoC:]
+ -[PowerUISmartChargeManager temporarilyOverrideMCLTargetSoC:]
+ -[PowerUISmartChargeManagerUnsupported availableChargeLimitsWithHandler:]
+ -[PowerUISmartChargeManagerUnsupported availableChargeLimits]
+ -[PowerUISmartChargeManagerUnsupported client:temporarilyOverrideMCLTargetSoC:withHandler:]
+ GCC_except_table100
+ GCC_except_table103
+ GCC_except_table106
+ GCC_except_table110
+ GCC_except_table113
+ GCC_except_table116
+ GCC_except_table132
+ GCC_except_table135
+ GCC_except_table139
+ GCC_except_table155
+ GCC_except_table162
+ GCC_except_table192
+ GCC_except_table508
+ GCC_except_table85
+ GCC_except_table89
+ GCC_except_table99
+ _OBJC_IVAR_$_PowerUISmartChargeManager._deocCacheCurrentStateLock
+ _OBJC_IVAR_$_PowerUISmartChargeManager._mclOverridenUntilDate
+ _OBJC_IVAR_$_PowerUISmartChargeManager._modeOfOperation
+ _OBJC_IVAR_$_PowerUISmartChargeManager._savedMCLTargetSoC
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_13
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_15
+ _OUTLINED_FUNCTION_16
+ _OUTLINED_FUNCTION_17
+ _OUTLINED_FUNCTION_18
+ ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.1017
+ ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.1038
+ ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.1043
+ ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.1051
+ ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.1060
+ ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.1067
+ ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.1071
+ ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.1073
+ ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.1075
+ ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.1083
+ ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.1083.cold.1
+ ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.1084
+ ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.1087
+ ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.1087.cold.1
+ ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.1088
+ ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke_2.1039
+ ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke_2.1045
+ ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke_2.1053
+ ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke_2.1062
+ ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke_2.1069
+ ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke_2.1077
+ ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke_2.1086
+ ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke_2.1086.cold.1
+ ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke_3.1041
+ ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke_3.1047
+ ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke_3.1047.cold.1
+ ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke_3.1058
+ ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke_3.1079
+ ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke_4.1081
+ ___34-[PowerUISmartChargeClient status]_block_invoke.143
+ ___40-[PowerUISmartChargeManager disableDEoC]_block_invoke.2002
+ ___42-[PowerUISmartChargeClient powerLogStatus]_block_invoke.145
+ ___44-[PowerUISmartChargeManager recordAnalytics]_block_invoke.1383
+ ___44-[PowerUISmartChargeManager recordAnalytics]_block_invoke.1402
+ ___44-[PowerUISmartChargeManager recordAnalytics]_block_invoke.1406
+ ___44-[PowerUISmartChargeManager recordAnalytics]_block_invoke.1407
+ ___45-[PowerUISmartChargeManager clearMCLOverride]_block_invoke
+ ___47-[PowerUISmartChargeClient fullChargeDeadline:]_block_invoke.146
+ ___50-[PowerUISmartChargeClient cecFullChargeDeadline:]_block_invoke.166
+ ___51-[PowerUISmartChargeClient resetEngagementOverride]_block_invoke.169
+ ___52-[PowerUISmartChargeClient lastUsedLeewayWithError:]_block_invoke.171
+ ___52-[PowerUISmartChargeClient lastUsedLeewayWithError:]_block_invoke.171.cold.1
+ ___57-[PowerUISmartChargeManager client:setState:withHandler:]_block_invoke.1976
+ ___59-[PowerUISmartChargeClient availableChargeLimitsWithError:]_block_invoke
+ ___59-[PowerUISmartChargeClient availableChargeLimitsWithError:]_block_invoke_2
+ ___60-[PowerUISmartChargeManager accessoryNFCConnectionCallback:]_block_invoke.2078
+ ___60-[PowerUISmartChargeManager accessoryNFCConnectionCallback:]_block_invoke.2078.cold.1
+ ___60-[PowerUISmartChargeManager accessoryNFCConnectionCallback:]_block_invoke.2078.cold.2
+ ___61-[PowerUISmartChargeManager temporarilyOverrideMCLTargetSoC:]_block_invoke
+ ___66-[PowerUISmartChargeClient legacy_client_isOBCEngagedWithHandler:]_block_invoke.152
+ ___66-[PowerUISmartChargeClient temporarilyOverrideMCLTargetSoC:error:]_block_invoke
+ ___66-[PowerUISmartChargeClient temporarilyOverrideMCLTargetSoC:error:]_block_invoke_2
+ ___76-[PowerUISmartChargeClient engageFrom:until:repeatUntil:overrideAllSignals:]_block_invoke.167
+ ___76-[PowerUISmartChargeClient engageFrom:until:repeatUntil:overrideAllSignals:]_block_invoke.167.cold.1
+ ___80-[PowerUISmartChargeManager checkWhetherMCLTempDisablementCanBeClearedOnPlugin:]_block_invoke.1986
+ ___87-[PowerUISmartChargeClient isOBCEngaged:chargeLimit:chargingOverrideAllowed:withError:]_block_invoke.162
+ ___87-[PowerUISmartChargeClient isOBCEngaged:chargeLimit:chargingOverrideAllowed:withError:]_block_invoke.162.cold.1
+ ___87-[PowerUISmartChargeClient simulateCurrentOutputAsOfDate:overrideAllSignals:withError:]_block_invoke.170
+ ___87-[PowerUISmartChargeClient simulateCurrentOutputAsOfDate:overrideAllSignals:withError:]_block_invoke.170.cold.1
+ ___94-[PowerUISmartChargeClient isOBCEngaged:isMaxChargeLimited:chargingOverrideAllowed:withError:]_block_invoke.150
+ ___94-[PowerUISmartChargeClient isOBCEngaged:isMaxChargeLimited:chargingOverrideAllowed:withError:]_block_invoke.150.cold.1
+ ___95-[PowerUISmartChargeClient smartChargingUIState:chargeLimit:chargingOverrideAllowed:withError:]_block_invoke.148
+ ___95-[PowerUISmartChargeClient smartChargingUIState:chargeLimit:chargingOverrideAllowed:withError:]_block_invoke.148.cold.1
+ ___block_descriptor_41_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_48_e8_32r40r_e29_v24?0"NSArray"8"NSError"16lr32l8r40l8
+ ___block_literal_global.1367
+ ___block_literal_global.155
+ ___block_literal_global.1552
+ ___block_literal_global.157
+ ___block_literal_global.1592
+ ___block_literal_global.1594
+ ___block_literal_global.160
+ ___block_literal_global.1627
+ ___block_literal_global.1632
+ ___block_literal_global.165
+ ___block_literal_global.1786
+ ___block_literal_global.2780
+ ___block_literal_global.2782
+ _objc_msgSend$availableChargeLimits
+ _objc_msgSend$availableChargeLimitsWithHandler:
+ _objc_msgSend$clearMCLOverride
+ _objc_msgSend$client:temporarilyOverrideMCLTargetSoC:withHandler:
+ _objc_msgSend$loadModeOfOperation
+ _objc_msgSend$setFullChargeDeadline:forDesktopMode:
+ _objc_msgSend$setModeOfOperation:
+ _objc_msgSend$temporarilyOverrideMCLTargetSoC:
- -[PowerUISmartChargeManager currentModeOfOperation]
- -[PowerUISmartChargeManager setFullChargeDeadline:]
- GCC_except_table102
- GCC_except_table105
- GCC_except_table108
- GCC_except_table119
- GCC_except_table124
- GCC_except_table131
- GCC_except_table147
- GCC_except_table154
- GCC_except_table184
- GCC_except_table487
- GCC_except_table84
- GCC_except_table95
- ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.1020
- ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.1025
- ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.1031
- ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.1033
- ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.1042
- ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.1053
- ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.1055
- ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.1057
- ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.1065
- ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.1065.cold.1
- ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.1066
- ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.1069
- ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.1069.cold.1
- ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.1070
- ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.999
- ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke_2.1021
- ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke_2.1027
- ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke_2.1035
- ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke_2.1044
- ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke_2.1051
- ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke_2.1059
- ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke_2.1068
- ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke_2.1068.cold.1
- ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke_3.1023
- ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke_3.1029
- ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke_3.1029.cold.1
- ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke_3.1040
- ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke_3.1061
- ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke_4.1063
- ___34-[PowerUISmartChargeClient status]_block_invoke.140
- ___40-[PowerUISmartChargeManager disableDEoC]_block_invoke.1965
- ___42-[PowerUISmartChargeClient powerLogStatus]_block_invoke.142
- ___44-[PowerUISmartChargeManager recordAnalytics]_block_invoke.1362
- ___44-[PowerUISmartChargeManager recordAnalytics]_block_invoke.1381
- ___44-[PowerUISmartChargeManager recordAnalytics]_block_invoke.1385
- ___44-[PowerUISmartChargeManager recordAnalytics]_block_invoke.1386
- ___47-[PowerUISmartChargeClient fullChargeDeadline:]_block_invoke.143
- ___50-[PowerUISmartChargeClient cecFullChargeDeadline:]_block_invoke.162
- ___51-[PowerUISmartChargeClient resetEngagementOverride]_block_invoke.165
- ___52-[PowerUISmartChargeClient lastUsedLeewayWithError:]_block_invoke.167
- ___52-[PowerUISmartChargeClient lastUsedLeewayWithError:]_block_invoke.167.cold.1
- ___57-[PowerUISmartChargeManager client:setState:withHandler:]_block_invoke.1952
- ___60-[PowerUISmartChargeManager accessoryNFCConnectionCallback:]_block_invoke.2043
- ___60-[PowerUISmartChargeManager accessoryNFCConnectionCallback:]_block_invoke.2043.cold.1
- ___60-[PowerUISmartChargeManager accessoryNFCConnectionCallback:]_block_invoke.2043.cold.2
- ___66-[PowerUISmartChargeClient legacy_client_isOBCEngagedWithHandler:]_block_invoke.149
- ___76-[PowerUISmartChargeClient engageFrom:until:repeatUntil:overrideAllSignals:]_block_invoke.163
- ___76-[PowerUISmartChargeClient engageFrom:until:repeatUntil:overrideAllSignals:]_block_invoke.163.cold.1
- ___87-[PowerUISmartChargeClient isOBCEngaged:chargeLimit:chargingOverrideAllowed:withError:]_block_invoke.158
- ___87-[PowerUISmartChargeClient isOBCEngaged:chargeLimit:chargingOverrideAllowed:withError:]_block_invoke.158.cold.1
- ___87-[PowerUISmartChargeClient simulateCurrentOutputAsOfDate:overrideAllSignals:withError:]_block_invoke.166
- ___87-[PowerUISmartChargeClient simulateCurrentOutputAsOfDate:overrideAllSignals:withError:]_block_invoke.166.cold.1
- ___87-[PowerUISmartChargeManager handleNewBatteryLevel:whileExternalConnected:fullyCharged:]_block_invoke
- ___94-[PowerUISmartChargeClient isOBCEngaged:isMaxChargeLimited:chargingOverrideAllowed:withError:]_block_invoke.147
- ___94-[PowerUISmartChargeClient isOBCEngaged:isMaxChargeLimited:chargingOverrideAllowed:withError:]_block_invoke.147.cold.1
- ___95-[PowerUISmartChargeClient smartChargingUIState:chargeLimit:chargingOverrideAllowed:withError:]_block_invoke.145
- ___95-[PowerUISmartChargeClient smartChargingUIState:chargeLimit:chargingOverrideAllowed:withError:]_block_invoke.145.cold.1
- ___block_literal_global.1346
- ___block_literal_global.152
- ___block_literal_global.1531
- ___block_literal_global.154
- ___block_literal_global.156
- ___block_literal_global.1571
- ___block_literal_global.1573
- ___block_literal_global.1604
- ___block_literal_global.1609
- ___block_literal_global.1765
- ___block_literal_global.2721
- ___block_literal_global.2723
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$currentModeOfOperation
- _objc_msgSend$setFullChargeDeadline:
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x5
- _objc_retain_x6
CStrings:
+ "%@ requests MCL target SoC override: %@, but MCL is not supported on this hardware!"
+ "%@ requests MCL target SoC override: %@, but this is not an available charge limit!"
+ "(previous/current) checkpoint: (%lu/%lu) - decisionMaker: (%ld/%ld) - decisionDate: %@ - MoO: (%lu/%lu)"
+ "@\"NSArray\"24@0:8^@16"
+ "Checkpoint before SoC handling %lu"
+ "Client %@ requests MCL target SoC temporary override: %@"
+ "Expected NSArray for key %@ but got %@"
+ "Expected NSDictionary for key %@ but got %@"
+ "Expected NSNumber for date key %@ but got %@"
+ "Expected NSNumber for key %@ but got %@"
+ "Expected NSString for key %@ but got %@"
+ "Loading MoO value: %lu"
+ "Loading checkpoint value: %lu"
+ "MCL target SoC overridden to %u until %@"
+ "MCL target SoC override date of %@ has passed, restore saved target SoC"
+ "MCL target SoC override date of %@ still upcoming"
+ "MCL target SoC restored to %u"
+ "MCLOverridenUntilDate"
+ "MCLSavedTargetSoC"
+ "MoO"
+ "MoO is already %lu"
+ "Returning currently desired UI state: %lu (mode: %lu), optimized charge limit: %lu, MCL target: %hhu%%, chargingOverrideAllowed: %u"
+ "Returning currently engaged state: %u, optimized charge limit: %lu, chargingOverrideAllowed: %u"
+ "Saved current MCL target SoC: %u"
+ "T@\"NSDate\",&,V_mclOverridenUntilDate"
+ "T@\"NSLock\",&,N,V_deocCacheCurrentStateLock"
+ "TC,V_savedMCLTargetSoC"
+ "TQ,N,V_modeOfOperation"
+ "Update MoO from %lu to %lu"
+ "_deocCacheCurrentStateLock"
+ "_mclOverridenUntilDate"
+ "_modeOfOperation"
+ "_savedMCLTargetSoC"
+ "availableChargeLimits"
+ "availableChargeLimitsWithError:"
+ "availableChargeLimitsWithHandler:"
+ "clearMCLOverride"
+ "client:temporarilyOverrideMCLTargetSoC:withHandler:"
+ "deocCacheCurrentStateLock"
+ "loadModeOfOperation"
+ "mclOverridenUntilDate"
+ "modeOfOperation"
+ "new MoO before: %lu - decision signal: %@"
+ "new moo after: %lu - decision signal: %@"
+ "savedMCLTargetSoC"
+ "setDeocCacheCurrentStateLock:"
+ "setFullChargeDeadline:forDesktopMode:"
+ "setMclOverridenUntilDate:"
+ "setModeOfOperation:"
+ "setSavedMCLTargetSoC:"
+ "temporarilyOverrideMCLTargetSoC:"
+ "temporarilyOverrideMCLTargetSoC:error:"
+ "temporarilyOverrideMCLTargetSoC:withHandler:"
+ "v24@0:8@?<v@?@\"NSArray\"@\"NSError\">16"
- "Loading checkpoint value: %@"
- "Returning currently desired UI state: %lu, charge limit: %lu, chargingOverrideAllowed: %u"
- "Returning currently engaged state: %u, charge limit: %lu, chargingOverrideAllowed: %u"
- "currentModeOfOperation"
- "setFullChargeDeadline:"

```
