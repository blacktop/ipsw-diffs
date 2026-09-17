## libCommCenterCommandDrivers.dylib

> `/System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterCommandDrivers.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__DATA_CONST.__const`
- `__AUTH_CONST.__cfstring`

```diff

-13487.1.0.0.0
-  __TEXT.__text: 0x342c0
+13494.0.0.0.0
+  __TEXT.__text: 0x34920
   __TEXT.__init_offsets: 0x8
-  __TEXT.__const: 0x4640
-  __TEXT.__gcc_except_tab: 0x4d2c
-  __TEXT.__cstring: 0x148d
-  __TEXT.__oslogstring: 0x17af
-  __TEXT.__unwind_info: 0x1ad0
-  __TEXT.__auth_stubs: 0xec0
+  __TEXT.__const: 0x4650
+  __TEXT.__gcc_except_tab: 0x4d50
+  __TEXT.__cstring: 0x1593
+  __TEXT.__oslogstring: 0x1acd
+  __TEXT.__unwind_info: 0x1ad8
+  __TEXT.__auth_stubs: 0xee0
   __DATA_CONST.__const: 0x768
   __DATA_CONST.__weak_got: 0x10
   __DATA_CONST.__got: 0x198
-  __AUTH_CONST.__const: 0x52a0
+  __AUTH_CONST.__const: 0x52b8
   __AUTH_CONST.__cfstring: 0xc0
   __AUTH_CONST.__weak_auth_got: 0x18
-  __AUTH_CONST.__auth_got: 0x750
+  __AUTH_CONST.__auth_got: 0x760
   __DATA_DIRTY.__common: 0x248
   __DATA_DIRTY.__bss: 0x30
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
   Functions: 1376
-  Symbols:   2580
-  CStrings:  443
+  Symbols:   2582
+  CStrings:  459
 
Symbols:
+ __Z8asString16DataCodingScheme
+ __ZN33DataSubscriptionBaseCommandDriver20configureUsableIccidEN10subscriber15HardwareSimSlotERKNSt3__112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEbNS2_8functionIFvbEEE
+ __os_log_debug_impl
+ _syslog$DARWIN_EXTSN
- __ZN33DataSubscriptionBaseCommandDriver20configureUsableIccidEN10subscriber15HardwareSimSlotERKNSt3__112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEb
- ___TUAssertTrigger
Functions:
~ __ZN3awd8asStringENS_5AppIDE : 60 -> 88
~ __ZN3awd8asStringENS_11ClientStateE : 60 -> 88
~ __ZN3awd8asStringENS_11PayloadTypeE : 60 -> 88
~ __ZN20DesenseCommandDriver23addSingleFrequencyToMapEyjjPNSt3__13mapIy11DesenseFreqNS0_4lessIyEENS0_9allocatorINS0_4pairIKyS2_EEEEEE : 372 -> 556
~ __ZNK22BasebandSettingsDriver22getFileTransferTimeoutEv : 44 -> 164
~ __ZN17CallCommandDriver20shouldMTCallContinueEbRK8CallInfo : 1472 -> 1752
~ __ZN15CallAudioDriver21supportCSDownlinkDtmfEv : 756 -> 900
~ __ZNK10subscriber16SimCommandDriver35handleSimConfigurationMismatch_syncERKNSt3__16vectorIhNS1_9allocatorIhEEEES7_ : 1032 -> 1112
~ __ZNK10subscriber16SimCommandDriver27getVinylCapabilitiesFromATRERKNSt3__16vectorIhNS1_9allocatorIhEEEE : 532 -> 712
~ __ZN10subscriber16SimCommandDriver11parseEapSimEPKN3ctu11OsLogLoggerENS_7SimTypeERKNSt3__16vectorIhNS6_9allocatorIhEEEERNS6_3mapINS_8AuthInfoESA_NS6_4lessISE_EENS8_INS6_4pairIKSE_SA_EEEEEE : 872 -> 1032
~ __Z18decodeOperatorNamePKN3ctu11OsLogLoggerERKNSt3__16vectorIhNS3_9allocatorIhEEEE16DataCodingScheme : 272 -> 396
~ __ZNK22PhonebookCommandDriver9swapPairsERNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE : 220 -> 320
~ __ZN22PhonebookCommandDriver18getVectorForStringERKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEb : 680 -> 684
~ __ZN33DataSubscriptionBaseCommandDriver20configureUsableIccidEN10subscriber15HardwareSimSlotERKNSt3__112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEb -> __ZN33DataSubscriptionBaseCommandDriver20configureUsableIccidEN10subscriber15HardwareSimSlotERKNSt3__112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEbNS2_8functionIFvbEEE : 28 -> 200
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/CoreTelephony/CommCenter/CommCenterCommandDrivers/Awd/AwdCommandDriver.cpp"
+ "Adding Frequency: %llu, Bandwidth: %u, Priority: %d"
+ "Assertion failure: ( %s ), in file %s, line: %d"
+ "Carrier has CarrierAllowsRingingMultipleDevices set to false or doesn't have that key defined"
+ "Carrier has CarrierAllowsRingingMultipleDevices set to true!"
+ "Decoding PLMN name of %lu bytes using coding scheme %s"
+ "Duplicated frequency (%llu), keeping higher bandwidth (%u)"
+ "No historical bytes, not capable"
+ "No report required"
+ "Queried hardware model config (%d) and suffix (%s)"
+ "SIM authenticate success; reporting result on card %s"
+ "Swapped the characters: %s"
+ "Vinyl capabilities byte: 0x%02x"
+ "We are on an Data-Only device AND we are on an external build"
+ "isInternalBuild: %d, dataDeviceWithAllowsRingingMultipleDevices: %d, dataOnlyDevice: %d, Thumper Secondar device: %d"
+ "supportCSDownlinkDtmf: EnableSOSVoiceLoopControl is true in operator bundle on %s"
```
