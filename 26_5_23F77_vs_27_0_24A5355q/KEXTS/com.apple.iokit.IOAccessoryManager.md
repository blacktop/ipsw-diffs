## com.apple.iokit.IOAccessoryManager

> `com.apple.iokit.IOAccessoryManager`

```diff

-1044.120.2.0.0
-  __TEXT.__const: 0x2a8 sha256:db5f0bd7b4d06ca33dd05f01534536fee08bced8bae0cb49a00b6b8f8f89535c
-  __TEXT.__cstring: 0x10be9 sha256:ed0aa6eec7712f33d1b2fa85ae8821bec2041801524e2d413136b83bb6539772
-  __TEXT.__os_log: 0x10c86 sha256:be826abec6aa5f1d5dcdcea30f47e02b682073be7d48baa12dfea6cb04115849
-  __TEXT_EXEC.__text: 0xdf2dc sha256:035c641918eaa85a8425ed0dc3d1cf6d4320029fa6f3184348167cfa7cf765f1
+1062.0.0.0.1
+  __TEXT.__const: 0x2b8 sha256:0eda24c1de74c3a2ef749c9bfa4414e2f4df6c2d427a3c968e1108fe875bdee1
+  __TEXT.__cstring: 0x11009 sha256:58dd7153c28054df4b009939cc8e10f7acbea0bf8932120b2038fc5caa902ca2
+  __TEXT.__os_log: 0x12066 sha256:72cc0c5ae56c32006d3cb758ed1992bf9966770ce01dd5d5afe6ee2dc446dd41
+  __TEXT_EXEC.__text: 0xe465c sha256:8633518c7818947977ca6fbf3d5fd16a3b82cda4b40f06df5a7aaf44f534c295
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x7e8 sha256:5e122aeb5c5373b13a7cf21a7b36c3a5c1b30fd3a1c725660e6ff08557884ad5
-  __DATA.__common: 0x1680 sha256:32ead73abab870ab0c7ba67a2337215e63ae49394d3c22dbf133e7ce1c7a2a0a
-  __DATA.__bss: 0x13a sha256:5ac19cf6919b95ba1f59248a47bd88b2c4c855db62ccf5a26326a6a2f02eeefe
-  __DATA_CONST.__auth_got: 0x5c0 sha256:017c1f139955b1e952f0a4763bcfc34d005154d367a263fd75809214b324a986
-  __DATA_CONST.__got: 0x1e0 sha256:355526088deee63ce4e5a93dba3cf5987531c87d6d1889d6c6b9b725956d52b1
-  __DATA_CONST.__auth_ptr: 0x20 sha256:54b67c0272898ce8c270cad4877c5587d038e23f0e14477f98ce95877f78faa9
-  __DATA_CONST.__mod_init_func: 0x348 sha256:7516683e1ca0ce10c9b23672bee827f35311635b91e775addc2a676a9781979c
-  __DATA_CONST.__mod_term_func: 0x340 sha256:b733a02c56e66d2f9cee37ba730cdae1534d72399284ff5d43731581eb72c3e0
-  __DATA_CONST.__const: 0x2a878 sha256:e456a267e3d9899e102ae41fe309130a7bb699f2c3c772b334413409cf0706c4
-  __DATA_CONST.__kalloc_type: 0x24c0 sha256:d1be0ae8d350dac0e9322f2a1b8272061d09ce355731bd999edc409be7ca14f1
-  UUID: 26884187-C676-363B-AACE-AC5A96B3D766
-  Functions: 4945
+  __DATA.__data: 0x7e8 sha256:abbdd89dd4adbf27d4639af0d3212a3430d76d699863ff09f0775e24ace99ae8
+  __DATA.__common: 0x16a8 sha256:59f3dea33be39a9668c7419d8f1d0f0745bb9946978d0d90270c00fc57adbc3e
+  __DATA.__bss: 0x142 sha256:68b138c89671b1f8435c3ebeeff7720bc4ee002e907fe77787caed1d35d40e07
+  __DATA_CONST.__mod_init_func: 0x348 sha256:78b519215eb34e8a741f2fe3cea139e8cd7986a194587fe9a58d10a2dd1cf830
+  __DATA_CONST.__mod_term_func: 0x340 sha256:082fee8bcec2d625bb85034be37f126114b4639eee2a22c4ab637ce8e66bec9c
+  __DATA_CONST.__const: 0x2ac50 sha256:7257c2681448497d4e6f9a8262126a231fb01a13465896987efd41c05bb35465
+  __DATA_CONST.__kalloc_type: 0x2500 sha256:be45d47c1a451c4a04cdd8ad047a2da91b624317e65251676fac95c5785cd022
+  __DATA_CONST.__auth_got: 0x5d8 sha256:ce617bb2a4f1cd5a97efafdf963784398cdacb51a8d581fbf166052f083d508b
+  __DATA_CONST.__got: 0x1f0 sha256:e476fb861fe15df7583e103a9f2be06e6245124fca95bb21d94fac8b25f0f88b
+  __DATA_CONST.__auth_ptr: 0x20 sha256:ffa4a2ab8177c456e98ba56270d6471c0d092af42b114f282fdf9809cfd23aef
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
