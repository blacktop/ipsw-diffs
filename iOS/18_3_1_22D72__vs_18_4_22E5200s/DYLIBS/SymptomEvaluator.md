## SymptomEvaluator

> `/System/Library/PrivateFrameworks/Symptoms.framework/Frameworks/SymptomEvaluator.framework/SymptomEvaluator`

```diff

-2001.80.5.0.0
-  __TEXT.__text: 0x254cdc
+2022.100.23.0.0
+  __TEXT.__text: 0x254fc8
   __TEXT.__auth_stubs: 0x22d0
-  __TEXT.__objc_methlist: 0x15f10
-  __TEXT.__cstring: 0x231f4
+  __TEXT.__objc_methlist: 0x16ea0
+  __TEXT.__cstring: 0x23231
   __TEXT.__const: 0xa78
-  __TEXT.__gcc_except_tab: 0x51e8
-  __TEXT.__oslogstring: 0x401f6
+  __TEXT.__gcc_except_tab: 0x5188
+  __TEXT.__oslogstring: 0x405b2
   __TEXT.__dlopen_cstrs: 0x56
-  __TEXT.evaluator_cfg: 0x634d
+  __TEXT.evaluator_cfg: 0x6417
   __TEXT.default_clp: 0x2fe0
   __TEXT.symptoms_clp: 0x5f90
   __TEXT.network_clp: 0x4b40

   __TEXT.bb_MAV_clp: 0xa690
   __TEXT.bb_INT_clp: 0x68f0
   __TEXT.modules_clp: 0x16e0
-  __TEXT.__unwind_info: 0x66a8
-  __TEXT.__objc_classname: 0x1ca0
-  __TEXT.__objc_methname: 0x3b3cc
-  __TEXT.__objc_methtype: 0x65a9
-  __TEXT.__objc_stubs: 0x24b00
-  __DATA_CONST.__got: 0xde8
-  __DATA_CONST.__const: 0x6500
-  __DATA_CONST.__objc_classlist: 0x828
+  __TEXT.__unwind_info: 0x6600
+  __TEXT.__objc_classname: 0x1cc4
+  __TEXT.__objc_methname: 0x3b53a
+  __TEXT.__objc_methtype: 0x65d8
+  __TEXT.__objc_stubs: 0x24d00
+  __DATA_CONST.__got: 0xdf0
+  __DATA_CONST.__const: 0x64e8
+  __DATA_CONST.__objc_classlist: 0x830
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x190
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc370
+  __DATA_CONST.__objc_selrefs: 0xc670
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x570
+  __DATA_CONST.__objc_superrefs: 0x578
   __DATA_CONST.__objc_arraydata: 0x820
   __AUTH_CONST.__auth_got: 0x1180
-  __AUTH_CONST.__auth_ptr: 0x18
-  __AUTH_CONST.__const: 0x2320
-  __AUTH_CONST.__cfstring: 0x1c000
-  __AUTH_CONST.__objc_const: 0x3b550
+  __AUTH_CONST.__auth_ptr: 0x20
+  __AUTH_CONST.__const: 0x2340
+  __AUTH_CONST.__cfstring: 0x1c040
+  __AUTH_CONST.__objc_const: 0x39f48
   __AUTH_CONST.__objc_arrayobj: 0x1c8
   __AUTH_CONST.__objc_dictobj: 0x8c0
   __AUTH_CONST.__objc_intobj: 0x750
   __AUTH_CONST.__objc_doubleobj: 0x50
   __AUTH_CONST.__objc_floatobj: 0x30
   __AUTH.__objc_data: 0x1428
-  __DATA.__objc_ivar: 0x2c4c
+  __DATA.__objc_ivar: 0x2c64
   __DATA.__data: 0x1c00
   __DATA.__crash_info: 0x40
-  __DATA.__bss: 0x320
-  __DATA.__common: 0xb1
-  __DATA_DIRTY.__objc_data: 0x3d68
+  __DATA.__bss: 0x358
+  __DATA.__common: 0xa8
+  __DATA_DIRTY.__objc_data: 0x3db8
   __DATA_DIRTY.__data: 0xc8
-  __DATA_DIRTY.__bss: 0x15b0
+  __DATA_DIRTY.__bss: 0x15a8
   __DATA_DIRTY.__common: 0x1a0
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreData.framework/CoreData

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libspindump.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 10811
-  Symbols:   12118
-  CStrings:  22135
+  Functions: 10827
+  Symbols:   12268
+  CStrings:  22174
 
Symbols:
+ _OBJC_CLASS_$_CellFallbackTrialExperimentHandler
+ _OBJC_METACLASS_$_CellFallbackTrialExperimentHandler
+ _kNWStatsSelectInterfaceCompanionLinkBluetooth
CStrings:
+ "\x02$\x11!\x121\x11\x14\x12"
+ "\b\x11\x12\x81\x14\x11'\x11#1"
+ "\t\tCFSM loop eval: %s for: %@, escal: %d, wificalling: %d, stationary: %d, cell-active: %d, wifi-active: %d, wifi-primary: %d, no-cost-adv: %d, wifi-rssi: %d, wifi-signal-exmp: %u, boosted %d"
+ "  %ld total reports for the day."
+ "@\"CellFallbackTrialExperimentHandler\""
+ "Bluetooth Data Usage for %@%@%@ on flow %llu - in/out: %@/%@,  delta_in/delta_out: %lld/%lld, total duration: %.3f"
+ "CFSM: Trial configuration: %@"
+ "CFSM: trialExperimentWithProjectIDHasBegun for %d/%@/%@/%@"
+ "CFSM: trialExperimentWithProjectIDHasBegun forceTurboRNFNum is %@"
+ "CFSM: trialExperimentWithProjectIDHasEnded for %d/%@/%@"
+ "CFSM: turbo_rnf %sabled, from fflag: %s, from trial: %s"
+ "CTShim: %s turbo mode upon barcode scan"
+ "CTShim: Asking baseband to activate turbo mode"
+ "CTShim: Received barcode %s scan symptom (%s qualifier)"
+ "CTShim: Unable to ask baseband to activate turbo mode, no coreTelephonyClient yet"
+ "CTShim: received notification of barcode activation from BarcodeSupport"
+ "CellFallbackTrialExperimentHandler"
+ "Could not activate"
+ "Dis"
+ "En"
+ "ForceTurboRNF"
+ "SYMPTOM_BARCODE_ACTIVATION"
+ "Successfully activated"
+ "SymptomAnalytics ServiceImpl: client has 'configuration' entitlement, rate-limit check waived"
+ "SymptomAnalytics ServiceImpl: found non-zero (%ld) fetch-offset (part of batched queries), rate-limit check waived"
+ "SymptomAnalytics ServiceImpl: query passed rate-limit check"
+ "T@\"CellFallbackTrialExperimentHandler\",&,N,V_trialExperimentHandler"
+ "TB,N,V_trialTurboRNF"
+ "TB,N,V_turboRNFFeatureFlagEnabled"
+ "TB,V_turboRNF"
+ "Turbo WiFi Assist is %sabled, grace period: %d"
+ "Unable to set configuration object when class name is nil! {object:%@}"
+ "_liveUsageCountForProcess: encountered unexpected nil tag (%llu previous errors)"
+ "_liveUsagePackForProcess: encountered unexpected nil tag (%llu previous errors)"
+ "_processBarcodeActivationNotification:"
+ "_setWiFiRSSIThresholds:"
+ "_trialTurboRNF"
+ "_turboRNF"
+ "_turboRNFFeatureFlagEnabled"
+ "_updateLiveUsage:wifiIn:wifiOut:cellIn:cellOut:wiredIn:wiredOut:btIn:btOut:xIn:xOut:isJumboFlow:isExpensive:closing:"
+ "activateTurboMode:"
+ "barcodeActivationObserver"
+ "btIN"
+ "btIN_exp"
+ "btOUT"
+ "btOUT_exp"
+ "deltaAccountingRxCompanionLinkBluetoothBytes"
+ "deltaAccountingTxCompanionLinkBluetoothBytes"
+ "evalTurboRNF"
+ "kNotificationBarcodeActivation"
+ "setBtIN:"
+ "setBtIN_exp:"
+ "setBtOUT:"
+ "setBtOUT_exp:"
+ "setTrialTurboRNF:"
+ "setTurboRNF:"
+ "setTurboRNFFeatureFlagEnabled:"
+ "trialTurboRNF"
+ "turboRNF"
+ "turboRNF grace period"
+ "turboRNFFeatureFlagEnabled"
+ "turbo_rnf"
+ "turbo_rnf (RSSI levels) is %sabled"
+ "turbo_rnf feature flag is %sabled"
+ "turbo_rnf fflag"
+ "v116@0:8@16q24q32q40q48q56q64q72q80q88q96B104B108B112"
+ "with"
+ "without"
- "\x02#\x11!\x121\x11\x14\x12"
- "\b\x11\x12\x81\x14\x11'\x11#"
- "\t\tCFSM loop eval: %s for: %@, escal: %d, wificalling: %d, stationary: %d, cell-active: %d, wifi-active: %d, wifi-primary: %d, wifi-rssi: %d, wifi-signal-exmp: %u, boosted %d"
- "  %ld total reports for the day is still under the limit of %d."
- "  Cannot generate report for unknown trigger type %lu."
- "  Reached limit of %ld RESOURCE_NOTIFY reports per day. Disallow report."
- " Unknown traffic and stall info version %d"
- "-f"
- "-l"
- "<-"
- "Delivering new GF active value to delegates. isActive: %{BOOL}d"
- "GF"
- "NW_L2_RADIO_TECHNOLOGY_TYPE_GF"
- "Received GF active changed notification, new status: %{BOOL}d"
- "T"
- "TB,N,V_isNonTerrestrialNetworkActive"
- "Unexpected network type %ld in journal entry"
- "_deliverNonTerrestrialNetworkActiveChangedTo:"
- "_isNonTerrestrialNetworkActive"
- "_updateLiveUsage:wifiIn:wifiOut:cellIn:cellOut:wiredIn:wiredOut:xIn:xOut:isJumboFlow:isExpensive:closing:"
- "ab"
- "do"
- "ff"
- "isNonTerrestrialNetworkActive"
- "isSatelliteSystem"
- "kNetworkType-unknown"
- "nonTerrestrialNetworkActiveChangedTo:"
- "setIsNonTerrestrialNetworkActive:"
- "t"
- "unexpected switch value %d"
- "v100@0:8@16q24q32q40q48q56q64q72q80B88B92B96"

```
