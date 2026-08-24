## libCommCenterCommandDrivers.dylib

> `/System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterCommandDrivers.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__DATA_CONST.__const`
- `__AUTH_CONST.__cfstring`

```diff

-13482.0.0.0.0
-  __TEXT.__text: 0x34efc
+13487.1.0.0.0
+  __TEXT.__text: 0x34948
   __TEXT.__init_offsets: 0x8
-  __TEXT.__const: 0x4650
-  __TEXT.__gcc_except_tab: 0x4d3c
-  __TEXT.__cstring: 0x1593
-  __TEXT.__oslogstring: 0x1acd
-  __TEXT.__unwind_info: 0x1888
-  __TEXT.__auth_stubs: 0xee0
+  __TEXT.__const: 0x4640
+  __TEXT.__gcc_except_tab: 0x4d2c
+  __TEXT.__cstring: 0x148d
+  __TEXT.__oslogstring: 0x17af
+  __TEXT.__unwind_info: 0x1880
+  __TEXT.__auth_stubs: 0xec0
   __DATA_CONST.__const: 0x768
   __DATA_CONST.__weak_got: 0x10
   __DATA_CONST.__got: 0x198
-  __AUTH_CONST.__const: 0x52c0
+  __AUTH_CONST.__const: 0x52a0
   __AUTH_CONST.__cfstring: 0xc0
   __AUTH_CONST.__weak_auth_got: 0x18
-  __AUTH_CONST.__auth_got: 0x760
+  __AUTH_CONST.__auth_got: 0x750
   __DATA.__bss: 0x8
   __DATA_DIRTY.__common: 0x248
   __DATA_DIRTY.__bss: 0x30

   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
   Functions: 1376
-  Symbols:   2582
-  CStrings:  459
+  Symbols:   2580
+  CStrings:  443
 
Symbols:
+ ___TUAssertTrigger
- __Z8asString16DataCodingScheme
- __os_log_debug_impl
- _syslog$DARWIN_EXTSN
Functions:
~ __ZN3awd8asStringENS_5AppIDE : 88 -> 60
~ __ZN3awd8asStringENS_11ClientStateE : 88 -> 60
~ __ZN3awd8asStringENS_11PayloadTypeE : 88 -> 60
~ __ZN20DesenseCommandDriver23addSingleFrequencyToMapEyjjPNSt3__13mapIy11DesenseFreqNS0_4lessIyEENS0_9allocatorINS0_4pairIKyS2_EEEEEE : 556 -> 372
~ __ZNK22BasebandSettingsDriver22getFileTransferTimeoutEv : 164 -> 44
~ __ZN17CallCommandDriver20shouldMTCallContinueEbRK8CallInfo : 1752 -> 1472
~ __ZN15CallAudioDriver21supportCSDownlinkDtmfEv : 900 -> 756
~ __ZNK10subscriber16SimCommandDriver35handleSimConfigurationMismatch_syncERKNSt3__16vectorIhNS1_9allocatorIhEEEES7_ : 1112 -> 1032
~ __ZNK10subscriber16SimCommandDriver27getVinylCapabilitiesFromATRERKNSt3__16vectorIhNS1_9allocatorIhEEEE : 712 -> 532
~ __ZN10subscriber16SimCommandDriver11parseEapSimEPKN3ctu11OsLogLoggerENS_7SimTypeERKNSt3__16vectorIhNS6_9allocatorIhEEEERNS6_3mapINS_8AuthInfoESA_NS6_4lessISE_EENS8_INS6_4pairIKSE_SA_EEEEEE : 1032 -> 872
~ __Z18decodeOperatorNamePKN3ctu11OsLogLoggerERKNSt3__16vectorIhNS3_9allocatorIhEEEE16DataCodingScheme : 396 -> 272
~ __ZNK22PhonebookCommandDriver9swapPairsERNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE : 320 -> 220
~ __ZN22PhonebookCommandDriver18getVectorForStringERKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEb : 684 -> 680
CStrings:
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/CoreTelephony/CommCenter/CommCenterCommandDrivers/Awd/AwdCommandDriver.cpp"
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
