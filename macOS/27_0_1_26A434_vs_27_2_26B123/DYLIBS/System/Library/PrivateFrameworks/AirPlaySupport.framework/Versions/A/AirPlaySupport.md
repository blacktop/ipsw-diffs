## AirPlaySupport

> `/System/Library/PrivateFrameworks/AirPlaySupport.framework/Versions/A/AirPlaySupport`

```diff

-980.77.5.3.0
-  __TEXT.__text: 0xc678c
+1005.13.1.0.0
+  __TEXT.__text: 0xc7184
   __TEXT.__objc_methlist: 0x374
-  __TEXT.__const: 0xee8
+  __TEXT.__const: 0xf10
   __TEXT.__dlopen_cstrs: 0x158
   __TEXT.__gcc_except_tab: 0x368
-  __TEXT.__cstring: 0x31fce
+  __TEXT.__cstring: 0x321f4
   __TEXT.__oslogstring: 0x1cc
-  __TEXT.__unwind_info: 0x1dd0
+  __TEXT.__unwind_info: 0x1de8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x26e0
+  __DATA_CONST.__const: 0x2718
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5f0
+  __DATA_CONST.__objc_selrefs: 0x5f8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x28
   __DATA_CONST.__objc_arraydata: 0x60
   __DATA_CONST.__got: 0x650
-  __AUTH_CONST.__const: 0x44a8
-  __AUTH_CONST.__cfstring: 0x7060
+  __AUTH_CONST.__const: 0x4508
+  __AUTH_CONST.__cfstring: 0x71c0
   __AUTH_CONST.__objc_const: 0x7a8
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_arrayobj: 0x48

   __AUTH.__data: 0x350
   __DATA.__objc_ivar: 0x2c
   __DATA.__data: 0x25b8
-  __DATA.__bss: 0xb08
+  __DATA.__bss: 0xb00
   __DATA_DIRTY.__objc_data: 0x1e0
   __DATA_DIRTY.__data: 0xa00
-  __DATA_DIRTY.__bss: 0x658
+  __DATA_DIRTY.__bss: 0x690
   - /System/Library/Frameworks/AudioToolbox.framework/Versions/A/AudioToolbox
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreMedia.framework/Versions/A/CoreMedia

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2613
-  Symbols:   5024
-  CStrings:  4289
+  Functions: 2626
+  Symbols:   5046
+  CStrings:  4307
 
Symbols:
+ APSIsHomeAccessory.sCheckOnce
+ APSIsHomeAccessory.sIsAPHomeAccessory
+ APSIsHomeTheaterSurroundEnabled.enabled
+ APSIsHomeTheaterSurroundEnabled.onceToken
+ APSIsUpdateInfoForwardingEnabled.sOnce
+ APSIsUpdateInfoForwardingEnabled.sUpdateInfoForwardingEnabled
+ APSSurroundToOdeonFallbackEnabled.sFallbackOnce
+ APSSurroundToOdeonFallbackEnabled.sIsFallbackEnabled
+ GCC_except_table1133
+ GCC_except_table1222
+ GCC_except_table1296
+ GCC_except_table1301
+ GCC_except_table1314
+ GCC_except_table1342
+ GCC_except_table1497
+ GCC_except_table1502
+ GCC_except_table1542
+ GCC_except_table1548
+ GCC_except_table1791
+ GCC_except_table1794
+ GCC_except_table1798
+ GCC_except_table193
+ GCC_except_table195
+ GCC_except_table2096
+ GCC_except_table2235
+ GCC_except_table2468
+ GCC_except_table2471
+ GCC_except_table2472
+ GCC_except_table2547
+ GCC_except_table500
+ GCC_except_table533
+ GCC_except_table947
+ _APSAudioHoseMetricCollectorSetSenderRTMetrics
+ _APSCMTimeMakeWithRTPTimestamp
+ _APSGetClusterMemberIDForSurroundRole
+ _APSGetSurroundRoleFromClusterMemberID
+ _APSGetSurroundRoleFromClusterSummary
+ _APSIsHomeAccessory
+ _APSIsHomeTheaterSurroundEnabled
+ _APSIsUpdateInfoForwardingEnabled
+ _APSSignalStrengthDBmFromScaled
+ _APSSignalStrengthScaledFromDBm
+ _APSSurroundToOdeonFallbackEnabled
+ ___APSIsHomeAccessory_block_invoke
+ ___APSIsHomeTheaterSurroundEnabled_block_invoke
+ ___APSIsUpdateInfoForwardingEnabled_block_invoke
+ ___APSSurroundToOdeonFallbackEnabled_block_invoke
+ _kAPSDynamicLatencyManagerVariantIdentifier_B525
+ _kAPSEndpointStreamAudioHoseRegistrarRegistrationOption_SurroundRole
+ _objc_msgSend$stringValue
- APSIsHomeKitManagerEnabled.sIsHomeKitManagerEnabled
- APSIsHomeKitManagerEnabled.sIsHomeKitManagerEnabledOnce
- GCC_except_table1132
- GCC_except_table1219
- GCC_except_table1295
- GCC_except_table1300
- GCC_except_table1313
- GCC_except_table1341
- GCC_except_table1490
- GCC_except_table1492
- GCC_except_table1532
- GCC_except_table1538
- GCC_except_table1778
- GCC_except_table1781
- GCC_except_table1784
- GCC_except_table192
- GCC_except_table194
- GCC_except_table2086
- GCC_except_table2225
- GCC_except_table2458
- GCC_except_table2461
- GCC_except_table2462
- GCC_except_table2534
- GCC_except_table499
- GCC_except_table532
- GCC_except_table946
- _APSIsHomeKitManagerEnabled
- ___APSIsHomeKitManagerEnabled_block_invoke
CStrings:
+ "### %@ [Glitch Underrun Start]. SeqNum: %u. RTPStartTime: %lld.\n"
+ "%@ Pre-warming audio HW\n"
+ "1609528"
+ "1622524"
+ "APSAudioHoseMetricCollectorSetSenderRTMetrics"
+ "APSEndpointStreamAudioHoseRegistrarRegistrationOption_SurroundRole"
+ "AudioAccessory11,1"
+ "B525"
+ "Boolean APSIsHomeAccessory(void)_block_invoke"
+ "HomeTheaterSurround"
+ "Pebble"
+ "ProcessLatencyReport endpointID: %@ inIsSessionReport: %s networkLatencyMs: %u prevMaxNetworkLatencyMs: %u outOfBoundsCount: %.0lf tloVarEstimateMs: %llu"
+ "Set APHomeAccessory behavior to %d because of defaults write\n"
+ "SurroundRole"
+ "[%{ptr}] Recorded %s range %u..<%u, EffectiveTUR: %u..<%u, flushed/pruned ranges: %@"
+ "almEndToEndLatencyOverrideP2PMs"
+ "disableSurroundToOdeon"
+ "flushed"
+ "forceAPHomeAccessory"
+ "hoseAUAudioIOAssertionDurationSecs"
+ "pruned"
+ "updateInfoForwardEnabled"
+ "void glitchReporter_LogGlitch(CFStringRef, APSGlitchReporterLogEventType, uint32_t, int64_t, Float64)"
- "MediaGroups"
- "ProcessLatencyReport endpointID: %@ inIsSessionReport: %s networkLatencyMs: %u prevMaxNetworkLatencyMs: %u outOfBoundsCount: %.0lf duringInitialRamp: %s tloVarEstimateMs: %llu"
- "[%{ptr}] Recorded flushed range %u..<%u, flushed ranges: %@"
- "tightSyncUUID"
- "void glitchReporter_LogGlitch(CFStringRef, uint32_t, int64_t, Float64)"
```
