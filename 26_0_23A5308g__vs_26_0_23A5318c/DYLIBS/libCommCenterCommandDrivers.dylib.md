## libCommCenterCommandDrivers.dylib

> `/System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterCommandDrivers.dylib`

```diff

-13090.3.0.0.0
-  __TEXT.__text: 0x36edc
-  __TEXT.__auth_stubs: 0xfa0
+13091.1.6.0.0
+  __TEXT.__text: 0x36840
+  __TEXT.__auth_stubs: 0xf90
   __TEXT.__init_offsets: 0x8
-  __TEXT.__const: 0x476c
-  __TEXT.__gcc_except_tab: 0x4ecc
-  __TEXT.__cstring: 0x16c3
-  __TEXT.__oslogstring: 0x1c6d
+  __TEXT.__const: 0x475c
+  __TEXT.__gcc_except_tab: 0x4eb4
+  __TEXT.__cstring: 0x1622
+  __TEXT.__oslogstring: 0x1925
   __TEXT.__unwind_info: 0x1818
   __DATA_CONST.__got: 0x1e8
   __DATA_CONST.__const: 0x958
-  __AUTH_CONST.__auth_got: 0x7d8
-  __AUTH_CONST.__const: 0x5050
+  __AUTH_CONST.__auth_got: 0x7d0
+  __AUTH_CONST.__const: 0x5048
   __AUTH_CONST.__cfstring: 0xc0
   __DATA_DIRTY.__common: 0x248
   __DATA_DIRTY.__bss: 0x40

   - /usr/lib/libTelephonyCapabilities.dylib
   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 497DF521-ADAB-354F-A6F9-2110251924C7
+  UUID: 3F282C23-AF8C-33AA-BCBA-57FED51799F3
   Functions: 1345
-  Symbols:   3559
-  CStrings:  480
+  Symbols:   3558
+  CStrings:  464
 
Symbols:
+ ___TUAssertTrigger
+ ___block_descriptor_tmp.40
+ ___block_descriptor_tmp.43
- __Z8asString16DataCodingScheme
- ___block_descriptor_tmp.45
- ___block_descriptor_tmp.49
- _syslog
Functions:
~ __ZN3awd8asStringENS_5AppIDE : 88 -> 60
~ __ZN3awd8asStringENS_11ClientStateE : 88 -> 60
~ __ZN3awd8asStringENS_11PayloadTypeE : 88 -> 60
~ __ZN3awdlsERN3ctu16LogMessageBufferENSt3__110shared_ptrINS_10AppContextEEE : 1652 -> 1684
~ __ZN20DesenseCommandDriver23addSingleFrequencyToMapEyjjPNSt3__13mapIy11DesenseFreqNS0_4lessIyEENS0_9allocatorINS0_4pairIKyS2_EEEEEE : 604 -> 376
~ __ZNK22BasebandSettingsDriver22getFileTransferTimeoutEv : 208 -> 44
~ __ZN17CallCommandDriver20shouldMTCallContinueEbRK8CallInfo : 1616 -> 1332
~ __ZN15CallAudioDriver21supportCSDownlinkDtmfEv : 960 -> 740
~ __ZNK10subscriber16SimCommandDriver35handleSimConfigurationMismatch_syncERKNSt3__16vectorIhNS1_9allocatorIhEEEES7_ : 1132 -> 1052
~ __ZNK10subscriber16SimCommandDriver27getVinylCapabilitiesFromATRERKNSt3__16vectorIhNS1_9allocatorIhEEEE : 776 -> 596
~ __ZN10subscriber16SimCommandDriver11parseEapSimEPKN3ctu11OsLogLoggerENS_7SimTypeERKNSt3__16vectorIhNS6_9allocatorIhEEEERNS6_3mapINS_8AuthInfoESA_NS6_4lessISE_EENS8_INS6_4pairIKSE_SA_EEEEEE : 1236 -> 1076
~ __Z18decodeOperatorNamePKN3ctu11OsLogLoggerERKNSt3__16vectorIhNS3_9allocatorIhEEEE16DataCodingScheme : 440 -> 272
~ __ZNK22PhonebookCommandDriver9swapPairsERNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE : 368 -> 216
~ __ZN22PhonebookCommandDriver18getVectorForStringERKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEb : 872 -> 868
CStrings:
- "#D Adding Frequency: %llu, Bandwidth: %u, Priority: %d"
- "#D Carrier has CarrierAllowsRingingMultipleDevices set to false or doesn't have that key defined"
- "#D Carrier has CarrierAllowsRingingMultipleDevices set to true!"
- "#D Decoding PLMN name of %lu bytes using coding scheme %s"
- "#D Duplicated frequency (%llu), keeping higher bandwidth (%u)"
- "#D No historical bytes, not capable"
- "#D No report required"
- "#D Queried hardware model config (%d) and suffix (%s)"
- "#D SIM authenticate success; reporting result on card %s"
- "#D Swapped the characters: %s"
- "#D Vinyl capabilities byte: 0x%02x"
- "#D We are on an Data-Only device AND we are on an external build"
- "#D isInternalBuild: %d, dataDeviceWithAllowsRingingMultipleDevices: %d, dataOnlyDevice: %d, Thumper Secondar device: %d"
- "#D supportCSDownlinkDtmf: EnableSOSVoiceLoopControl is true in operator bundle on %s"
- "/Library/Caches/com.apple.xbs/Sources/CoreTelephony/CommCenter/CommCenterCommandDrivers/Awd/AwdCommandDriver.cpp"
- "Assertion failure: ( %s ), in file %s, line: %d"

```
