## SymptomEvaluator

> `/System/Library/PrivateFrameworks/Symptoms.framework/Frameworks/SymptomEvaluator.framework/SymptomEvaluator`

```diff

-2001.80.5.0.0
-  __TEXT.__text: 0x258c3c
+2022.100.25.0.0
+  __TEXT.__text: 0x258ee8
   __TEXT.__auth_stubs: 0x22e0
-  __TEXT.__objc_methlist: 0x162e0
-  __TEXT.__cstring: 0x23920
-  __TEXT.__const: 0xaa0
-  __TEXT.__gcc_except_tab: 0x5278
-  __TEXT.__oslogstring: 0x40899
+  __TEXT.__objc_methlist: 0x17290
+  __TEXT.__cstring: 0x23957
+  __TEXT.__const: 0xab8
+  __TEXT.__gcc_except_tab: 0x5218
+  __TEXT.__oslogstring: 0x40c55
   __TEXT.__dlopen_cstrs: 0x56
-  __TEXT.evaluator_cfg: 0x634d
+  __TEXT.evaluator_cfg: 0x6417
   __TEXT.default_clp: 0x2fe0
   __TEXT.symptoms_clp: 0x5f90
   __TEXT.network_clp: 0x4b40
   __TEXT.baseband_clp: 0xee70
   __TEXT.bb_MAV_clp: 0xa690
-  __TEXT.bb_INT_clp: 0x68f0
+  __TEXT.bb_INT_clp: 0x68e0
   __TEXT.modules_clp: 0x16e0
-  __TEXT.__unwind_info: 0x6768
-  __TEXT.__objc_classname: 0x1d13
-  __TEXT.__objc_methname: 0x3b828
-  __TEXT.__objc_methtype: 0x6a05
-  __TEXT.__objc_stubs: 0x24fa0
-  __DATA_CONST.__got: 0xde8
-  __DATA_CONST.__const: 0x6520
-  __DATA_CONST.__objc_classlist: 0x848
+  __TEXT.__unwind_info: 0x66c8
+  __TEXT.__objc_classname: 0x1d37
+  __TEXT.__objc_methname: 0x3b996
+  __TEXT.__objc_methtype: 0x6a34
+  __TEXT.__objc_stubs: 0x251a0
+  __DATA_CONST.__got: 0xdf0
+  __DATA_CONST.__const: 0x6508
+  __DATA_CONST.__objc_classlist: 0x850
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x198
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc4a0
+  __DATA_CONST.__objc_selrefs: 0xc7a0
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x580
+  __DATA_CONST.__objc_superrefs: 0x588
   __DATA_CONST.__objc_arraydata: 0x810
   __AUTH_CONST.__auth_got: 0x1188
-  __AUTH_CONST.__auth_ptr: 0x18
-  __AUTH_CONST.__const: 0x2340
-  __AUTH_CONST.__cfstring: 0x1c9a0
-  __AUTH_CONST.__objc_const: 0x3c6e8
+  __AUTH_CONST.__auth_ptr: 0x20
+  __AUTH_CONST.__const: 0x2360
+  __AUTH_CONST.__cfstring: 0x1c9e0
+  __AUTH_CONST.__objc_const: 0x3b0a0
   __AUTH_CONST.__objc_arrayobj: 0x1c8
   __AUTH_CONST.__objc_dictobj: 0x898
   __AUTH_CONST.__objc_intobj: 0x780
   __AUTH_CONST.__objc_doubleobj: 0x50
   __AUTH_CONST.__objc_floatobj: 0x30
   __AUTH.__objc_data: 0x1568
-  __DATA.__objc_ivar: 0x2cb4
+  __DATA.__objc_ivar: 0x2ccc
   __DATA.__data: 0x1c60
   __DATA.__crash_info: 0x40
-  __DATA.__bss: 0x320
-  __DATA.__common: 0xb1
-  __DATA_DIRTY.__objc_data: 0x3d68
+  __DATA.__bss: 0x358
+  __DATA.__common: 0xa8
+  __DATA_DIRTY.__objc_data: 0x3db8
   __DATA_DIRTY.__data: 0xc8
-  __DATA_DIRTY.__bss: 0x15d0
+  __DATA_DIRTY.__bss: 0x15c8
   __DATA_DIRTY.__common: 0x1a0
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreData.framework/CoreData

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libspindump.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 10893
-  Symbols:   12201
-  CStrings:  22336
+  Functions: 10909
+  Symbols:   12351
+  CStrings:  22374
 
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
