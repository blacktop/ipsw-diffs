## SiriCrossDeviceArbitration

> `/System/Library/PrivateFrameworks/SiriCrossDeviceArbitration.framework/SiriCrossDeviceArbitration`

```diff

-3404.29.1.0.0
-  __TEXT.__text: 0x2ffdc
+3404.36.1.0.0
+  __TEXT.__text: 0x31028
   __TEXT.__auth_stubs: 0x850
   __TEXT.__objc_methlist: 0x2fbc
   __TEXT.__dlopen_cstrs: 0x164
-  __TEXT.__const: 0x1d0
+  __TEXT.__const: 0x1e8
   __TEXT.__gcc_except_tab: 0x490
-  __TEXT.__oslogstring: 0x4bb4
-  __TEXT.__cstring: 0x5a30
-  __TEXT.__unwind_info: 0xcf8
+  __TEXT.__oslogstring: 0x5365
+  __TEXT.__cstring: 0x5a8d
+  __TEXT.__unwind_info: 0xcf0
   __TEXT.__objc_classname: 0x697
   __TEXT.__objc_methname: 0x7bcd
   __TEXT.__objc_methtype: 0x1923
   __TEXT.__objc_stubs: 0x5aa0
   __DATA_CONST.__got: 0x310
-  __DATA_CONST.__const: 0x10f8
+  __DATA_CONST.__const: 0x1118
   __DATA_CONST.__objc_classlist: 0x168
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8

   __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x53c
   __DATA.__data: 0x6a8
-  __DATA.__bss: 0x198
+  __DATA.__bss: 0x1a0
   __DATA_DIRTY.__objc_data: 0xdc0
   __DATA_DIRTY.__bss: 0x8
   __DATA_DIRTY.__common: 0x10

   - /usr/lib/swift/libswiftunistd.dylib
   Functions: 1174
   Symbols:   1513
-  CStrings:  2603
+  CStrings:  2636
 
CStrings:
+ "%s #scda Voice Trigger Replacing new (empty) record with DT record for in progress request %@ with VT Time %llu"
+ "%s #scda Voice Trigger stored record replaced (%{public}@) with record: %{public}@"
+ "%s #scda Voice trigger with active record (%@), replaced with record: %@"
+ "%s #scda Voice trigger with active record (%@), using new record: %@"
+ "%s #scda Voice trigger with active record (%@), using original with adjusted TB: %@"
+ "%s #scda Voice trigger with lower goodness (%du) arrived, replacing with goodness from: %@"
+ "%s #scda attention Original confidence was 0"
+ "%s #scda attention Original goodness before attention arrived was zero - likely an invalid Myriad advertisement from this device could make it lose an election"
+ "%s #scda attention boost arrived in wrong state: %{public}@"
+ "%s #scda attention original record: %@"
+ "%s #scda attention originalTB and originalConfidence collision, generating a new random TB"
+ "%s #scda attention reformulated record: %@"
+ "%s #scda endTime from a file is too old, secondsSinceTrigger=%f; Siri might respond from multiple devices"
+ "%s #scda force win on this device with context: %{public}@, triggerRecord: %{public}@"
+ "%s #scda watch trumping due to score being 0; watch might win election for little reason"
+ "%s CRITICAL ERROR: BTLE error: attempting to readvertise %@; Myriad to stop advertising and proceed as if win occurred, multi-response likely"
+ "%s Dropping stale VT: %f"
+ "%s canceling advertising with nil trigger record, this likely means Siri UI was already dismissed %{public}@"
+ "-[SCDACoordinator directTriggerRecord]"
+ "-[SCDACoordinator voiceTriggerRecord]"
+ "Adding advertisement to replies: %{public}@"
+ "Advertise"
+ "Advertising continuation: %{public}@"
+ "Advertising emergency handled record: %{public}@"
+ "Advertising emergency record: %{public}@"
+ "Advertising ~OUTGOING_TRIGGER: %{public}@"
+ "Entry"
+ "Sending suppression(DT) advertisement: %{public}@"
+ "Suppressing late arriver with advertisement: %{public}@"
+ "faceDetectedBoostWithContext: %{public}@"
+ "reset state machine"
+ "startAdvertisingFromAlertFiringVoiceTriggerWithContext: %{public}@"
+ "startAdvertisingFromDirectTriggerWithContext: %{public}@"
+ "startAdvertisingFromInTaskTriggerWithContext: %{public}@"
+ "startAdvertisingFromInTaskVoiceTriggerWithContext: %{public}@"
+ "startAdvertisingFromOutgoingTrigger: %{public}@"
+ "startAdvertisingFromVoiceTrigger: %{public}@"
+ "startAdvertisingFromVoiceTriggerAdjusted: %du"
+ "startAdvertisingFromVoiceTriggerAdjusted: %du context: %{public}@"
+ "startAdvertisingFromVoiceTriggerWithGoodnessScoreContext: %{public}@ context: %{public}@"
- "%s #scda Voice trigger with active record, using original with adjusted TB: %@"
- "%s #scda attention boost arrived in wrong state: %@"
- "%s #scda endTime from a file is too old, secondsSinceTrigger=%f"
- "%s #scda force win on this device with context: %@, triggerRecord: %@"
- "%s #scda watch trumping due to score being 0"
- "%s BTLE error: attempting to readvertise %@"
- "%s canceling advertising with nil trigger record, this likely means Siri UI was already dismissed %@"

```
