## libCommCenterCommandDrivers.dylib

> `/System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterCommandDrivers.dylib`

```diff

-13171.6.0.0.0
-  __TEXT.__text: 0x364bc
-  __TEXT.__auth_stubs: 0xfa0
+13172.1.3.0.0
+  __TEXT.__text: 0x35e34
+  __TEXT.__auth_stubs: 0xf90
   __TEXT.__init_offsets: 0x8
-  __TEXT.__const: 0x4727
-  __TEXT.__gcc_except_tab: 0x4e98
-  __TEXT.__cstring: 0x1706
-  __TEXT.__oslogstring: 0x1cb0
+  __TEXT.__const: 0x4707
+  __TEXT.__gcc_except_tab: 0x4e80
+  __TEXT.__cstring: 0x1626
+  __TEXT.__oslogstring: 0x1968
   __TEXT.__unwind_info: 0x17e8
   __DATA_CONST.__got: 0x1e8
   __DATA_CONST.__const: 0x958
-  __AUTH_CONST.__auth_got: 0x7d8
-  __AUTH_CONST.__const: 0x5060
+  __AUTH_CONST.__auth_got: 0x7d0
+  __AUTH_CONST.__const: 0x5050
   __AUTH_CONST.__cfstring: 0xc0
   __DATA_DIRTY.__common: 0x248
   __DATA_DIRTY.__bss: 0x40

   - /usr/lib/libTelephonyCapabilities.dylib
   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 4F0E45AB-F553-3C90-B1D0-C78DBF1D9C86
+  UUID: A5EE36AF-6642-38E1-B052-C173F284577E
   Functions: 1347
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
~ __ZN3awdlsERN3ctu16LogMessageBufferENSt3__110shared_ptrINS_10AppContextEEE : 1624 -> 1656
~ __ZN20DesenseCommandDriver23addSingleFrequencyToMapEyjjPNSt3__13mapIy11DesenseFreqNS0_4lessIyEENS0_9allocatorINS0_4pairIKyS2_EEEEEE : 608 -> 380
~ __ZNK22BasebandSettingsDriver22getFileTransferTimeoutEv : 208 -> 44
~ __ZN17CallCommandDriver20shouldMTCallContinueEbRK8CallInfo : 1696 -> 1412
~ __ZN15CallAudioDriver21supportCSDownlinkDtmfEv : 956 -> 756
~ __ZNK10subscriber16SimCommandDriver35handleSimConfigurationMismatch_syncERKNSt3__16vectorIhNS1_9allocatorIhEEEES7_ : 1096 -> 1016
~ __ZNK10subscriber16SimCommandDriver27getVinylCapabilitiesFromATRERKNSt3__16vectorIhNS1_9allocatorIhEEEE : 756 -> 576
~ __ZN10subscriber16SimCommandDriver11parseEapSimEPKN3ctu11OsLogLoggerENS_7SimTypeERKNSt3__16vectorIhNS6_9allocatorIhEEEERNS6_3mapINS_8AuthInfoESA_NS6_4lessISE_EENS8_INS6_4pairIKSE_SA_EEEEEE : 1180 -> 1020
~ __Z18decodeOperatorNamePKN3ctu11OsLogLoggerERKNSt3__16vectorIhNS3_9allocatorIhEEEE16DataCodingScheme : 440 -> 272
~ __ZNK22PhonebookCommandDriver9swapPairsERNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE : 368 -> 216
~ __ZN22PhonebookCommandDriver18getVectorForStringERKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEb : 896 -> 892
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
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreTelephony/CommCenter/CommCenterCommandDrivers/Awd/AwdCommandDriver.cpp"
- "Assertion failure: ( %s ), in file %s, line: %d"

```
