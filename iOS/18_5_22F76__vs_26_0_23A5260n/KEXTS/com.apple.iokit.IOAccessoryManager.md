## com.apple.iokit.IOAccessoryManager

> `com.apple.iokit.IOAccessoryManager`

```diff

-1016.120.3.0.0
+1038.0.0.0.0
   __TEXT.__const: 0x328
-  __TEXT.__cstring: 0x10803
-  __TEXT.__os_log: 0x1077b
-  __TEXT_EXEC.__text: 0xefcf8
+  __TEXT.__cstring: 0x10b24
+  __TEXT.__os_log: 0x10bd8
+  __TEXT_EXEC.__text: 0xf6a38
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x7e8
-  __DATA.__common: 0x1630
-  __DATA.__bss: 0x11a
-  __DATA_CONST.__auth_got: 0x5b8
+  __DATA.__common: 0x1680
+  __DATA.__bss: 0x13a
+  __DATA_CONST.__auth_got: 0x5c0
   __DATA_CONST.__got: 0x1e0
   __DATA_CONST.__auth_ptr: 0x20
-  __DATA_CONST.__mod_init_func: 0x338
-  __DATA_CONST.__mod_term_func: 0x330
-  __DATA_CONST.__const: 0x29b48
-  __DATA_CONST.__kalloc_type: 0x2440
-  __DATA_DIRTY.__bss: 0x20
-  UUID: 14555532-F8C5-3CE3-893D-9E29AAFB93ED
-  Functions: 4821
+  __DATA_CONST.__mod_init_func: 0x348
+  __DATA_CONST.__mod_term_func: 0x340
+  __DATA_CONST.__const: 0x2a838
+  __DATA_CONST.__kalloc_type: 0x24c0
+  UUID: 1C7C5E1D-5E50-3750-931B-1338372C7B08
+  Functions: 4876
   Symbols:   0
-  CStrings:  2788
+  CStrings:  2829
 
CStrings:
+ "%s::%s(): Client missing entitlement!\n"
+ "%s::%s(): Invalid authorization status - cannot set authorization status to %d [%s] from user client in this state! (currentAuthorizationStatus: %d [%s])\n"
+ "%s::%s(): Invalid user authorization status - cannot set user authorization status to %d [%s] from user client in this state! (currentUserAuthorizationStatus: %d [%s])\n"
+ "%s::%s(): [%s%s%s] maxReceivingFrequency: %d, deferNotification: %s\n\n"
+ "%s::%s(): [%s%s%s] primaryDPDMStatus: %d, deferNotification: %s\n\n"
+ "%s::%s(): [%s%s%s] signalingPair: %d, deferNotification: %s\n\n"
+ "%s::%s(): [%s%s%s] signalingPin: %d, deferNotification: %s\n\n"
+ "%s::%s(): [%s%s%s] syncMode: %d, deferNotification: %s\n\n"
+ "%s::%s(): [%s@%s: %s%s%s] Transition to Unrestricted mode, adding transport hash to cache (if attached)... (%s)\n"
+ "%s::%s(): [%s@%s: %s%s%s] m_trmInfo.acmState.state: %d -> %d [%s -> %s], m_trmInfo.acmState.gracePeriodReason: %d -> %d [%s -> %s], m_trmInfo.acmState.profile: %d -> %d [%s -> %s], m_trmInfo.acmState.deviceLocked: %s -> %s, m_trmInfo.acmState.cacheMiss: %s -> %s, m_trmInfo.acmState.relaxedPeriod: %s -> %s\n"
+ "%s::%s(): [%s@%s: %s%s%s] policyReasonNumber: %d, gracePeriodReasonNumber: %d, profileNumber: %d, deviceLocked: %s, cacheMiss: %s, relaxedPeriod: %s\n"
+ "%s::%s(): [%s@%s: %s%s%s] policyReasonNumber: %s, gracePeriodReasonNumber: %s, profileNumber: %s, deviceLockedBoolean: %s, cacheMissBoolean: %s, cacheMissCountNumber: %s, cacheMissThresholdNumber: %s, relaxedPeriodBoolean: %s\n"
+ "121111121222121211111111221211112122221222222111"
+ "1211111212221212111111112212111121222212222221111"
+ "121111121222121211111111221211112122221222222111111111122"
+ "1211111212221212111111112212111121222212222221111222"
+ "12111112122212121111111122121111212222122222211122"
+ "1211111212221212111111112212111121222212222221112212"
+ "12111112122212121111111122121111212222122222211122122"
+ "121111121222121211111111221211112122221222222111222"
+ "12111112122212121111112111111222"
+ "A3502"
+ "A3503"
+ "Allow Automatically When Unlocked"
+ "Always Allow"
+ "Ask Every Time"
+ "Ask for New Accessories"
+ "Class Code"
+ "Device Id"
+ "IOPortTransportProtocolCCUSBPDSSAM"
+ "IOPortTransportStatePCIe"
+ "Max Receiving Frequency"
+ "Primary D+/D- Status"
+ "SSAM"
+ "Signaling Pair"
+ "Signaling Pin"
+ "Subsystem Id"
+ "Subsystem Vendor Id"
+ "Sync Mode"
+ "TRM_EffectiveConfigProfile"
+ "TRM_Profile"
+ "TRM_ProfileDescription"
+ "Vendor Id"
+ "[ERROR] %s::%s(): [%s@%s: %s%s%s] Error starting %s! Couldn't start!\n"
+ "[ERROR] %s::%s(): [%s@%s: %s%s%s] Error starting %s! No provider!\n"
+ "[ERROR] [%s@%s: %s%s%s] Couldn't read ACM TRM profile!\n"
+ "[ERROR] [%s@%s: %s%s%s] Couldn't read ACM TRM state!\n"
+ "_addProvisionedTransportsForRegistryEntry"
+ "setMaxReceivingFrequency"
+ "setPrimaryDPDMStatus"
+ "setSignalingPair"
+ "setSignalingPin"
+ "setSyncMode"
+ "site.IOPortTransportProtocolCCUSBPDSSAM"
+ "site.IOPortTransportStatePCIe"
+ "transport-usb-data-role"
+ "transports-provisioned"
- "%s::%s(): [%s@%s: %s%s%s] Transition to Unrestricted mode, adding transport hash to cache (if attached)... (%s@%s: %s)\n"
- "%s::%s(): [%s@%s: %s%s%s] m_trmInfo.acmState.state: %d -> %d [%s -> %s], m_trmInfo.acmState.gracePeriodReason: %d -> %d [%s -> %s], m_trmInfo.acmState.deviceLocked: %s -> %s, m_trmInfo.acmState.cacheMiss: %s -> %s, m_trmInfo.acmState.relaxedPeriod: %s -> %s\n"
- "%s::%s(): [%s@%s: %s%s%s] policyReasonNumber: %d, gracePeriodReasonNumber: %d, deviceLocked: %s, cacheMiss: %s, relaxedPeriod: %s\n"
- "%s::%s(): [%s@%s: %s%s%s] policyReasonNumber: %s, gracePeriodReasonNumber: %s, deviceLockedBoolean: %s, cacheMissBoolean: %s, cacheMissCountNumber: %s, cacheMissThresholdNumber: %s, relaxedPeriodBoolean: %s\n"
- "12111112122212121111111122121111212222122222111"
- "121111121222121211111111221211112122221222221111"
- "12111112122212121111111122121111212222122222111111111122"
- "121111121222121211111111221211112122221222221111222"
- "1211111212221212111111112212111121222212222211122"
- "121111121222121211111111221211112122221222221112212"
- "1211111212221212111111112212111121222212222211122122"
- "12111112122212121111111122121111212222122222111222"
- "[ERROR] Client missing entitlement!\n"
- "[ERROR] Invalid authorization status - cannot set authorization status to %d [%s] from user client in this state! (currentAuthorizationStatus: %d [%s])\n"
- "[ERROR] Invalid user authorization status - cannot set user authorization status to %d [%s] from user client in this state! (currentUserAuthorizationStatus: %d [%s])\n"
- "[ERROR] [%s@%s: %s%s%s] Couldn't find ACM TRM state!\n"

```
