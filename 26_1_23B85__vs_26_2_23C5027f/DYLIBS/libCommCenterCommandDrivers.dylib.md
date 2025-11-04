## libCommCenterCommandDrivers.dylib

> `/System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterCommandDrivers.dylib`

```diff

-13114.1.0.0.0
-  __TEXT.__text: 0x36840
-  __TEXT.__auth_stubs: 0xf90
+13123.3.0.0.0
+  __TEXT.__text: 0x36f14
+  __TEXT.__auth_stubs: 0xfa0
   __TEXT.__init_offsets: 0x8
-  __TEXT.__const: 0x475c
-  __TEXT.__gcc_except_tab: 0x4eb4
-  __TEXT.__cstring: 0x1622
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
-  UUID: 7DCC9684-2916-34EF-8240-8DDCA3A07D28
+  UUID: 8A8AFA03-CD8A-38BE-9CEC-9267BCB30E56
   Functions: 1345
-  Symbols:   3558
-  CStrings:  464
+  Symbols:   3559
+  CStrings:  480
 
Symbols:
+ __Z8asString16DataCodingScheme
+ ___block_descriptor_tmp.45
+ ___block_descriptor_tmp.49
+ _syslog
- ___TUAssertTrigger
- ___block_descriptor_tmp.40
- ___block_descriptor_tmp.43
Functions:
~ __ZNSt3__16vectorIN3ctu2cf11CFSharedRefIK14__CFDictionaryEENS_9allocatorIS6_EEE9push_backB8ne200100ERKS6_ : 332 -> 336
~ __ZNSt3__16vectorItNS_9allocatorItEEE11__vallocateB8ne200100Em : 56 -> 60
~ __ZN3awd8asStringENS_5AppIDE : 60 -> 88
~ __ZN3awd8asStringENS_11ClientStateE : 60 -> 88
~ __ZN3awd8asStringENS_11PayloadTypeE : 60 -> 88
~ __ZN3awdlsERN3ctu16LogMessageBufferENSt3__110shared_ptrINS_10AppContextEEE : 1684 -> 1652
~ __ZNKSt3__120__shared_ptr_pointerIP21CommandDriversFactoryNS_10shared_ptrIS1_E27__shared_ptr_default_deleteIS1_S1_EENS_9allocatorIS1_EEE13__get_deleterERKSt9type_info : 60 -> 64
~ __ZN20DesenseCommandDriver23addSingleFrequencyToMapEyjjPNSt3__13mapIy11DesenseFreqNS0_4lessIyEENS0_9allocatorINS0_4pairIKyS2_EEEEEE : 376 -> 604
~ __ZN21NetworkListScanResult11addOperatorEPKN3ctu11OsLogLoggerERK19NetworkListOperator : 1852 -> 1856
~ __ZNK22BasebandSettingsDriver22getFileTransferTimeoutEv : 44 -> 208
~ __ZNKSt3__120__shared_ptr_pointerIP25InterfaceAppMapperServiceNS_10shared_ptrIS1_E27__shared_ptr_default_deleteIS1_S1_EENS_9allocatorIS1_EEE13__get_deleterERKSt9type_info : 60 -> 64
~ __ZN17CallCommandDriver20shouldMTCallContinueEbRK8CallInfo : 1332 -> 1616
~ __ZN15CallAudioDriver21supportCSDownlinkDtmfEv : 740 -> 960
~ __ZNK10subscriber16SimCommandDriver35handleSimConfigurationMismatch_syncERKNSt3__16vectorIhNS1_9allocatorIhEEEES7_ : 1052 -> 1132
~ __ZNK10subscriber16SimCommandDriver27getVinylCapabilitiesFromATRERKNSt3__16vectorIhNS1_9allocatorIhEEEE : 596 -> 776
~ __ZN10subscriber16SimCommandDriver11parseEapSimEPKN3ctu11OsLogLoggerENS_7SimTypeERKNSt3__16vectorIhNS6_9allocatorIhEEEERNS6_3mapINS_8AuthInfoESA_NS6_4lessISE_EENS8_INS6_4pairIKSE_SA_EEEEEE : 1076 -> 1236
~ __Z18decodeOperatorNamePKN3ctu11OsLogLoggerERKNSt3__16vectorIhNS3_9allocatorIhEEEE16DataCodingScheme : 272 -> 440
~ __Z24convertMaskToBandsForRaty21RadioAccessTechnology : 428 -> 448
~ __ZNK22PhonebookCommandDriver9swapPairsERNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE : 216 -> 368
~ __ZN22PhonebookCommandDriver18getVectorForStringERKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEb : 868 -> 872
~ __GLOBAL__sub_I_RegistrationRestResource.cpp : 3984 -> 4000
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
+ "{map<unsigned int, int, std::less<unsigned int>, std::allocator<std::pair<const unsigned int, int>>>={__tree<std::__value_type<unsigned int, int>, std::__map_value_compare<unsigned int, std::__value_type<unsigned int, int>, std::less<unsigned int>>, std::allocator<std::__value_type<unsigned int, int>>>=^v{?={__tree_end_node<std::__tree_node_base<void *> *>=^v}}{?=Q}}}8@?0"
- "{map<unsigned int, int, std::less<unsigned int>, std::allocator<std::pair<const unsigned int, int>>>={__tree<std::__value_type<unsigned int, int>, std::__map_value_compare<unsigned int, std::__value_type<unsigned int, int>, std::less<unsigned int>>, std::allocator<std::__value_type<unsigned int, int>>>=^v{__tree_end_node<std::__tree_node_base<void *> *>=^v}Q}}8@?0"

```
