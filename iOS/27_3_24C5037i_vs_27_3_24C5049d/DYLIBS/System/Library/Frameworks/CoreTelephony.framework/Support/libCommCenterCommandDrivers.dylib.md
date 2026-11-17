## libCommCenterCommandDrivers.dylib

> `/System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterCommandDrivers.dylib`

```diff

-13504.1.0.0.0
-  __TEXT.__text: 0x358e0
+13508.0.0.0.0
+  __TEXT.__text: 0x35338
   __TEXT.__init_offsets: 0x8
-  __TEXT.__const: 0x47b0
-  __TEXT.__gcc_except_tab: 0x4e10
-  __TEXT.__cstring: 0x2015
-  __TEXT.__oslogstring: 0x1c32
+  __TEXT.__const: 0x47a0
+  __TEXT.__gcc_except_tab: 0x4e00
+  __TEXT.__cstring: 0x1f35
+  __TEXT.__oslogstring: 0x1914
   __TEXT.__unwind_info: 0x1ae0
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x990
   __DATA_CONST.__weak_got: 0x10
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x5198
+  __AUTH_CONST.__const: 0x5180
   __AUTH_CONST.__cfstring: 0xc0
   __AUTH_CONST.__weak_auth_got: 0x18
   __AUTH_CONST.__auth_got: 0x0

   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
   Functions: 1388
-  Symbols:   2603
-  CStrings:  489
+  Symbols:   2602
+  CStrings:  473
 
Symbols:
+ ___TUAssertTrigger
- __Z8asString16DataCodingScheme
- _syslog
Functions:
~ __ZN3awd8asStringENS_5AppIDE : 88 -> 60
~ __ZN3awd8asStringENS_11ClientStateE : 88 -> 60
~ __ZN3awd8asStringENS_11PayloadTypeE : 88 -> 60
~ __ZN20DesenseCommandDriver23addSingleFrequencyToMapEyjjPNSt3__13mapIy11DesenseFreqNS0_4lessIyEENS0_9allocatorINS0_4pairIKyS2_EEEEEE : 556 -> 372
~ __ZNK22BasebandSettingsDriver22getFileTransferTimeoutEv : 164 -> 44
~ __ZN17CallCommandDriver20shouldMTCallContinueEbRK8CallInfo : 1752 -> 1472
~ __ZN15CallAudioDriver21supportCSDownlinkDtmfEv : 900 -> 756
~ __ZNK10subscriber16SimCommandDriver35handleSimConfigurationMismatch_syncERKNSt3__16vectorIhNS1_9allocatorIhEEEES7_ : 1112 -> 1032
~ __ZNK10subscriber16SimCommandDriver27getVinylCapabilitiesFromATRERKNSt3__16vectorIhNS1_9allocatorIhEEEE : 792 -> 624
~ __ZN10subscriber16SimCommandDriver11parseEapSimEPKN3ctu11OsLogLoggerENS_7SimTypeERKNSt3__16vectorIhNS6_9allocatorIhEEEERNS6_3mapINS_8AuthInfoESA_NS6_4lessISE_EENS8_INS6_4pairIKSE_SA_EEEEEE : 1032 -> 872
~ __Z18decodeOperatorNamePKN3ctu11OsLogLoggerERKNSt3__16vectorIhNS3_9allocatorIhEEEE16DataCodingScheme : 396 -> 272
~ __ZNK22PhonebookCommandDriver9swapPairsERNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE : 320 -> 220
~ __ZN22PhonebookCommandDriver18getVectorForStringERKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEb : 676 -> 672
CStrings:
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreTelephony/CommCenter/CommCenterCommandDrivers/Awd/AwdCommandDriver.cpp"
- "Adding Frequency: %llu, Bandwidth: %u, Priority: %d"
- "Assertion failure: ( %s ), in file %s, line: %d"
- "Carrier has CarrierAllowsRingingMultipleDevices set to false or doesn't have that key defined"
- "Carrier has CarrierAllowsRingingMultipleDevices set to true!"
- "Decoding PLMN name of %lu bytes using coding scheme %s"
- "Duplicated frequency (%llu), keeping higher bandwidth (%u)"
- "No historical bytes, not capable"
- "No report required"
- "Queried hardware model config (%d) and suffix (%s)"
- "SIM authenticate success; reporting result on card %s"
- "Swapped the characters: %s"
- "Vinyl capabilities byte: 0x%02x"
- "We are on an Data-Only device AND we are on an external build"
- "isInternalBuild: %d, dataDeviceWithAllowsRingingMultipleDevices: %d, dataOnlyDevice: %d, Thumper Secondar device: %d"
- "supportCSDownlinkDtmf: EnableSOSVoiceLoopControl is true in operator bundle on %s"
```
