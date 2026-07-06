## com.apple.driver.AudioDMACLLTEscalationDetector-T8150

> `com.apple.driver.AudioDMACLLTEscalationDetector-T8150`

```diff

   __TEXT.__const: 0x30
   __TEXT.__cstring: 0x5f2
   __TEXT.__os_log: 0x25e
-  __TEXT_EXEC.__text: 0x426c
+  __TEXT_EXEC.__text: 0x41b4
   __TEXT_EXEC.__auth_stubs: 0x280
   __DATA.__data: 0x188
   __DATA.__common: 0x60
Sections:
~ __TEXT.__cstring : content changed
~ __DATA.__data : content changed
~ __DATA_CONST.__mod_init_func : content changed
~ __DATA_CONST.__mod_term_func : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__kalloc_type : content changed
~ __DATA_CONST.__auth_got : content changed
~ __DATA_CONST.__got : content changed
Functions:
~ __ZN30AudioDMACLLTEscalationDetector15_recordSnapshotEv : 340 -> 292
~ _kprintf -> __ZN30AudioDMACLLTEscalationDetector26_captureAndProcessSnapshotEU13block_pointerFviES1_ : 520 -> 480
~ ____ZN30AudioDMACLLTEscalationDetector20callPlatformFunctionEPK8OSSymbolbPvS3_S3_S3__block_invoke_2 : 100 -> 52
~ sub_fffffe0009b34658 -> sub_fffffe0009b34e40 : 36 -> 20
~ sub_fffffe0009b3467c -> sub_fffffe0009b34e54 : 20 -> 36
~ ____ZN30AudioDMACLLTEscalationDetector17_handleInterruptsEP22IOInterruptEventSourcei_block_invoke_3 : 104 -> 56
CStrings:
+ "21:31:01"
+ "Jun 29 2026"
- "19:55:39"
- "Jun 18 2026"

```
