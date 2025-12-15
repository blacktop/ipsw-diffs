## libCommCenterCommandDrivers.dylib

> `/System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterCommandDrivers.dylib`

```diff

-13126.1.1.0.0
-  __TEXT.__text: 0x36878
-  __TEXT.__auth_stubs: 0xf90
+13149.5.0.0.0
+  __TEXT.__text: 0x36f14
+  __TEXT.__auth_stubs: 0xfa0
   __TEXT.__init_offsets: 0x8
-  __TEXT.__const: 0x475c
-  __TEXT.__gcc_except_tab: 0x4eb4
-  __TEXT.__cstring: 0x162a
-  __TEXT.__oslogstring: 0x1925
+  __TEXT.__const: 0x476c
+  __TEXT.__gcc_except_tab: 0x4ecc
+  __TEXT.__cstring: 0x16cb
+  __TEXT.__oslogstring: 0x1c6d
   __TEXT.__unwind_info: 0x1818
   __DATA_CONST.__got: 0x1e8
   __DATA_CONST.__const: 0x958
-  __AUTH_CONST.__auth_got: 0x7d0
-  __AUTH_CONST.__const: 0x5048
+  __AUTH_CONST.__auth_got: 0x7d8
+  __AUTH_CONST.__const: 0x5058
   __AUTH_CONST.__cfstring: 0xc0
   __DATA_DIRTY.__common: 0x248
   __DATA_DIRTY.__bss: 0x40

   - /usr/lib/libTelephonyCapabilities.dylib
   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 2162B17D-125D-3561-8F68-C8191F0C122B
+  UUID: D72D4606-0E43-384B-AA8B-780D7EE679D4
   Functions: 1345
-  Symbols:   3558
-  CStrings:  464
+  Symbols:   3559
+  CStrings:  480
 
Symbols:
+ __Z8asString16DataCodingScheme
+ __ZN33DataSubscriptionBaseCommandDriver20configureUsableIccidEN10subscriber15HardwareSimSlotERKNSt3__112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEb
+ ___block_descriptor_tmp.45
+ ___block_descriptor_tmp.49
+ _syslog
- __ZN33DataSubscriptionBaseCommandDriver20configureUsableIccidERKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEb
- ___TUAssertTrigger
- ___block_descriptor_tmp.40
- ___block_descriptor_tmp.43
Functions:
~ __ZN3awd8asStringENS_5AppIDE : 60 -> 88
~ __ZN3awd8asStringENS_11ClientStateE : 60 -> 88
~ __ZN3awd8asStringENS_11PayloadTypeE : 60 -> 88
~ __ZN3awdlsERN3ctu16LogMessageBufferENSt3__110shared_ptrINS_10AppContextEEE : 1684 -> 1652
~ __ZN20DesenseCommandDriver23addSingleFrequencyToMapEyjjPNSt3__13mapIy11DesenseFreqNS0_4lessIyEENS0_9allocatorINS0_4pairIKyS2_EEEEEE : 376 -> 604
~ __ZNK22BasebandSettingsDriver22getFileTransferTimeoutEv : 44 -> 208
~ __ZN17CallCommandDriver20shouldMTCallContinueEbRK8CallInfo : 1332 -> 1616
~ __ZN15CallAudioDriver21supportCSDownlinkDtmfEv : 740 -> 960
~ __ZNK10subscriber16SimCommandDriver35handleSimConfigurationMismatch_syncERKNSt3__16vectorIhNS1_9allocatorIhEEEES7_ : 1052 -> 1132
~ __ZNK10subscriber16SimCommandDriver27getVinylCapabilitiesFromATRERKNSt3__16vectorIhNS1_9allocatorIhEEEE : 596 -> 776
~ __ZN10subscriber16SimCommandDriver11parseEapSimEPKN3ctu11OsLogLoggerENS_7SimTypeERKNSt3__16vectorIhNS6_9allocatorIhEEEERNS6_3mapINS_8AuthInfoESA_NS6_4lessISE_EENS8_INS6_4pairIKSE_SA_EEEEEE : 1076 -> 1236
~ __Z18decodeOperatorNamePKN3ctu11OsLogLoggerERKNSt3__16vectorIhNS3_9allocatorIhEEEE16DataCodingScheme : 272 -> 440
~ __ZNK22PhonebookCommandDriver9swapPairsERNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE : 216 -> 368
~ __ZN22PhonebookCommandDriver18getVectorForStringERKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEb : 868 -> 872
CStrings:
+ "#D Adding Frequency: %llu, Bandwidth: %u, Priority: %d"
+ "#D Carrier has CarrierAllowsRingingMultipleDevices set to false or doesn't have that key defined"
+ "#D Carrier has CarrierAllowsRingingMultipleDevices set to true!"
+ "#D Decoding PLMN name of %lu bytes using coding scheme %s"
+ "#D Duplicated frequency (%llu), keeping higher bandwidth (%u)"
+ "#D No historical bytes, not capable"
+ "#D No report required"
+ "#D Queried hardware model config (%d) and suffix (%s)"
+ "#D SIM authenticate success; reporting result on card %s"
+ "#D Swapped the characters: %s"
+ "#D Vinyl capabilities byte: 0x%02x"
+ "#D We are on an Data-Only device AND we are on an external build"
+ "#D isInternalBuild: %d, dataDeviceWithAllowsRingingMultipleDevices: %d, dataOnlyDevice: %d, Thumper Secondar device: %d"
+ "#D supportCSDownlinkDtmf: EnableSOSVoiceLoopControl is true in operator bundle on %s"
+ "/Library/Caches/com.apple.xbs/Sources/CoreTelephony/CommCenter/CommCenterCommandDrivers/Awd/AwdCommandDriver.cpp"
+ "Assertion failure: ( %s ), in file %s, line: %d"

```
