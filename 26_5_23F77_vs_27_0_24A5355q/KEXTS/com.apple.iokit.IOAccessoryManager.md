## com.apple.iokit.IOAccessoryManager

> `com.apple.iokit.IOAccessoryManager`

```diff

-1044.120.2.0.0
-  __TEXT.__const: 0x2a8
-  __TEXT.__cstring: 0x10be9
-  __TEXT.__os_log: 0x10c86
-  __TEXT_EXEC.__text: 0xdf2dc
+1062.0.0.0.1
+  __TEXT.__const: 0x2b8
+  __TEXT.__cstring: 0x11009
+  __TEXT.__os_log: 0x12066
+  __TEXT_EXEC.__text: 0xe465c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x7e8
-  __DATA.__common: 0x1680
-  __DATA.__bss: 0x13a
-  __DATA_CONST.__auth_got: 0x5c0
-  __DATA_CONST.__got: 0x1e0
-  __DATA_CONST.__auth_ptr: 0x20
+  __DATA.__common: 0x16a8
+  __DATA.__bss: 0x142
   __DATA_CONST.__mod_init_func: 0x348
   __DATA_CONST.__mod_term_func: 0x340
-  __DATA_CONST.__const: 0x2a878
-  __DATA_CONST.__kalloc_type: 0x24c0
-  UUID: 26884187-C676-363B-AACE-AC5A96B3D766
-  Functions: 4945
+  __DATA_CONST.__const: 0x2ac50
+  __DATA_CONST.__kalloc_type: 0x2500
+  __DATA_CONST.__auth_got: 0x5d8
+  __DATA_CONST.__got: 0x1f0
+  __DATA_CONST.__auth_ptr: 0x20
+  UUID: 7C3B6EF0-3211-3DAA-8E9B-924CC6CD7DF3
+  Functions: 5004
   Symbols:   0
-  CStrings:  2841
+  CStrings:  2957
 
CStrings:
+ "%s::%s(): Copying cached LDCM waveform... (target: %s)\n"
+ "%s::%s(): Failed to create OSData!\n"
+ "%s::%s(): Getting measurement data queue... (target: %s)\n"
+ "%s::%s(): Initializing port type to: %d [%s]\n"
+ "%s::%s(): Mapping measurement data queue memory... (m_userClientDescription: %s)\n"
+ "%s::%s(): Matched transport service! (transportType: %d [%s], parentPortType: %d, parentPortNumber: %d, transportRestricted: %s)\n"
+ "%s::%s(): Measurement data queue is NULL\n"
+ "%s::%s(): No cached waveform available\n"
+ "%s::%s(): Output buffer too small: %u < %u\n"
+ "%s::%s(): Provider unavailable or inactive\n"
+ "%s::%s(): Queue memory descriptor is NULL\n"
+ "%s::%s(): Received authorization state change notification... (transport: %s, transportRestricted: %s)\n"
+ "%s::%s(): Registering notification port for measurement data queue... (m_userClientDescription: %s)\n"
+ "%s::%s(): Setting hash... (target: %s)\n"
+ "%s::%s(): Starting HID...\n"
+ "%s::%s(): Successfully copied cached waveform (size: %u bytes, timestamp: %llu)\n"
+ "%s::%s(): Successfully mapped measurement data queue memory\n"
+ "%s::%s(): Successfully registered notification port for measurement data queue\n"
+ "%s::%s(): Successfully returned measurement data queue memory type\n"
+ "%s::%s(): Unsupported architecture version: %d\n"
+ "%s::%s(): [%s%s%s] --- NO TRANSITION: systemAsleep=%s CLAIM WAKE (stay in LPW - measurement only)\n\n"
+ "%s::%s(): [%s%s%s] Cached waveform for dry→wet transition (timestamp: %llu, size: %u bytes)\n\n"
+ "%s::%s(): [%s%s%s] Cached waveform timestamp mismatch (requested: %llu, cached: %llu) - not returning\n\n"
+ "%s::%s(): [%s%s%s] Caching waveform for dry→wet transition (timestamp: %llu)\n\n"
+ "%s::%s(): [%s%s%s] Cleared waveform cache\n\n"
+ "%s::%s(): [%s%s%s] Dry + empty receptacle - disabling mitigations\n\n"
+ "%s::%s(): [%s%s%s] Dry + empty receptacle - disabling user override\n\n"
+ "%s::%s(): [%s%s%s] Dry but receptacle occupied - keeping mitigations as-is\n\n"
+ "%s::%s(): [%s%s%s] Dry→wet transition detected (prev: %u, curr: %u)\n\n"
+ "%s::%s(): [%s%s%s] Empty port, was Failed - resetting to Triggered to dismiss intrusive UI\n\n"
+ "%s::%s(): [%s%s%s] Handling mitigations for liquid state: %s\n\n"
+ "%s::%s(): [%s%s%s] Ignoring LPW notification - timer remains suspended\n\n"
+ "%s::%s(): [%s%s%s] No valid cached waveform available\n\n"
+ "%s::%s(): [%s%s%s] Periodic measurement timer created and started (interval: %llu ms)\n\n"
+ "%s::%s(): [%s%s%s] Processing measurement: systemAsleep=%s (timer=%s) reason=%u\n\n"
+ "%s::%s(): [%s%s%s] RAW DATA: status=0x%02x mostRecentMeas=0x%02x | portStatus=%u pin=%u completion=%u lowImp=%u\n\n"
+ "%s::%s(): [%s%s%s] Rescheduling mitigations poll timer on wake (was not scheduled during sleep)\n\n"
+ "%s::%s(): [%s%s%s] Retrieved cached waveform (timestamp: %llu, size: %u bytes)\n\n"
+ "%s::%s(): [%s%s%s] Scheduled immediate measurement on wake\n\n"
+ "%s::%s(): [%s%s%s] Skipping duplicate valid measurement (data unchanged)\n\n"
+ "%s::%s(): [%s%s%s] Sleep/wake notification handler registered for timer power management\n\n"
+ "%s::%s(): [%s%s%s] System entering sleep - suspending periodic measurement timer\n\n"
+ "%s::%s(): [%s%s%s] System wake from sleep - resuming periodic measurement timer\n\n"
+ "%s::%s(): [%s%s%s] Updated measurement timer interval: %llu ms (%s)\n\n"
+ "%s::%s(): [%s%s%s] Wet detected - enabling corrosion mitigations\n\n"
+ "%s::%s(): [%s%s%s] Wet detected - mitigations suppressed by user override\n\n"
+ "%s::%s(): [%s%s%s] Wet→dry transition detected (prev: %u, curr: %u)\n\n"
+ "%s::%s(): [%s%s%s] requestMeasurement called with reason: %u\n\n"
+ "%s::%s(): [%s%s%s] ←←← WET→DRY TRANSITION: systemAsleep=%s CLAIM WAKE (stay in LPW)\n\n"
+ "%s::%s(): [%s%s%s] →→→ DRY→WET TRANSITION: systemAsleep=%s CLAIM WAKE (full wake)\n\n"
+ "%s::%s(): [%s%s%s] ═══ LDCM INTERRUPT ═══ status=%d [%s]\n\n"
+ "%s::%s(): [%s%s%s] ✗✗✗ MEASUREMENT ERROR: %s (pin=%u completion=%u lowImp=%u)\n\n"
+ "%s::%s(): [%s@%s: %s%s%s] Calling ACMKernTRMAccessoryAuthorizedInDomain(0x%04x, 0x%04x)...\n"
+ "%s::%s(): [%s@%s: %s%s%s] Calling ACMKernTRMAuthorizedAccessoryDetachedInDomain(0x%04x, 0x%04x)...\n"
+ "%s::%s(): magSafeSupported: %s\n"
+ "121111121222121211111121111211221212222222212212121"
+ "121111121222121211212111221112112"
+ "CacheMiss"
+ "CacheMissCount"
+ "CacheMissThreshold"
+ "EffectiveConfigProfile"
+ "IOAccessoryHSAIDBusTransport:%s: Ignoring setPowerState during low-power wake\n"
+ "IOAccessoryIDBusSystemStates: Ignoring low-power wake\n"
+ "IOAccessoryManagerInductiveOOBPairingHostInfo"
+ "IOPortFeatureLDCM.dryToWet"
+ "IOPortFeatureLDCM.measurement"
+ "IOPortFeatureLDCM.wetToDry"
+ "IOPortFeatureLDCMDataQueue"
+ "LOOPBACK_FAILURE"
+ "LOOPBACK_MEASUREMENT"
+ "LOW_IMPEDANCE"
+ "NEGATIVE_CAP_RES"
+ "OVP_DETECTED"
+ "PREEMPTED"
+ "PolicyReason"
+ "RREF_FAILURE"
+ "RREF_MEASUREMENT"
+ "SNR_AMP_FAILURE"
+ "TRMDomain_Generic"
+ "TRMDomain_Inductive"
+ "UNKNOWN"
+ "[ERROR] [%s%s%s] Failed to copy raw LDCM data: 0x%x\n\n"
+ "[ERROR] [%s%s%s] Failed to copy waveform: 0x%x\n\n"
+ "[ERROR] [%s%s%s] Failed to create measurement data queue!\n\n"
+ "[ERROR] [%s%s%s] Failed to create measurement timer!\n\n"
+ "[ERROR] [%s%s%s] Failed to enqueue measurement data - queue may be full\n\n"
+ "[ERROR] [%s%s%s] Failed to enqueue measurement data: 0x%x\n\n"
+ "[ERROR] [%s%s%s] Failed to process LDCM V4 measurement data: 0x%x\n\n"
+ "[ERROR] [%s%s%s] Failed to process measurement data: 0x%x\n\n"
+ "[ERROR] [%s%s%s] Failed to register sleep/wake notification handler!\n\n"
+ "[ERROR] [%s%s%s] Failed to request measurement from lower layer: 0x%x\n\n"
+ "[ERROR] [%s%s%s] Failed to request periodic measurement: 0x%x\n\n"
+ "[ERROR] [%s%s%s] Invalid data length: %zu (expected %d)\n\n"
+ "[ERROR] [%s%s%s] Invalid waveform data length: %u (expected %d)\n\n"
+ "[ERROR] [%s%s%s] Lower layer returned NULL data\n\n"
+ "[ERROR] [%s%s%s] Lower layer returned NULL waveform\n\n"
+ "[ERROR] [%s%s%s] Unsupported architecture version: %d\n\n"
+ "[ERROR] [%s%s%s] rawData is NULL\n\n"
+ "[ERROR] [%s@%s: %s%s%s] ACMKernTRMAccessoryAuthorizedInDomain(0x%04x, 0x%04x) failed! (ret: %d)\n"
+ "[ERROR] [%s@%s: %s%s%s] ACMKernTRMAuthorizedAccessoryDetachedInDomain(0x%04x, 0x%04x) failed! (ret: %d)\n"
+ "_cacheWaveformForDryToWet"
+ "_clearWaveformCache"
+ "_copyCachedWaveform"
+ "_enqueueMeasurementData"
+ "_getCachedWaveform"
+ "_getMeasurementDataQueue"
+ "_handleMitigationsForLiquidState"
+ "_portWetDryStateTransitionCheck"
+ "_sleepWakeNotification"
+ "_updateMeasurementTimerInterval"
+ "clientMemoryForType"
+ "dry"
+ "getMagSafeSupported"
+ "has-ironman-charging"
+ "performCommandV3"
+ "processLDCMV4Measurement"
+ "registerNotificationPort"
+ "requestMeasurement"
+ "resetAllowedFeaturesGated"
+ "site.IOPortFeatureLDCMDataQueue"
+ "smc-ext-charger"
+ "start_block_invoke_2"
+ "start_block_invoke_3"
+ "wet"
- "%s::%s(): [%s@%s: %s%s%s] Calling ACMKernTRMAccessoryAuthorizedWithFlags(0x%04x)...\n"
- "%s::%s(): [%s@%s: %s%s%s] Calling ACMKernTRMAuthorizedAccessoryDetachedWithFlags(0x%04x)...\n"
- "1211111212221212111111211112112212"
- "121111121222121211212111221112"
- "TRM_EffectiveConfigProfile"
- "[ERROR] [%s@%s: %s%s%s] ACMKernTRMAccessoryAuthorizedWithFlags(0x%04x) failed! (ret: %d)\n"
- "[ERROR] [%s@%s: %s%s%s] ACMKernTRMAuthorizedAccessoryDetachedWithFlags(0x%04x) failed! (ret: %d)\n"
- "performCommandV2"

```
