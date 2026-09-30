## AudioServerDriverTransports_IOP

> `/System/Library/PrivateFrameworks/AudioServerDriverTransports_IOP.framework/AudioServerDriverTransports_IOP`

```diff

-230.2.0.0.0
-  __TEXT.__text: 0xde68
-  __TEXT.__auth_stubs: 0x650
-  __TEXT.__objc_methlist: 0xa90
-  __TEXT.__gcc_except_tab: 0x1218
-  __TEXT.__const: 0x120
-  __TEXT.__oslogstring: 0xdf5
-  __TEXT.__cstring: 0xe79
-  __TEXT.__unwind_info: 0x6e8
-  __TEXT.__objc_classname: 0x32e
-  __TEXT.__objc_methname: 0x11fb
-  __TEXT.__objc_methtype: 0x93e
-  __TEXT.__objc_stubs: 0x1200
-  __DATA_CONST.__got: 0x150
-  __DATA_CONST.__const: 0xd8
+240.42.0.0.0
+  __TEXT.__text: 0xe9b4
+  __TEXT.__auth_stubs: 0x6f0
+  __TEXT.__objc_methlist: 0xc2c
+  __TEXT.__gcc_except_tab: 0x138c
+  __TEXT.__const: 0x148
+  __TEXT.__oslogstring: 0xe95
+  __TEXT.__cstring: 0xe6e
+  __TEXT.__unwind_info: 0x788
+  __TEXT.__objc_classname: 0x359
+  __TEXT.__objc_methname: 0x134d
+  __TEXT.__objc_methtype: 0xb25
+  __TEXT.__objc_stubs: 0x1300
+  __DATA_CONST.__got: 0x170
+  __DATA_CONST.__const: 0x100
   __DATA_CONST.__objc_classlist: 0xc0
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x18
+  __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5a8
+  __DATA_CONST.__objc_selrefs: 0x678
   __DATA_CONST.__objc_superrefs: 0x90
-  __AUTH_CONST.__auth_got: 0x340
+  __AUTH_CONST.__auth_got: 0x390
   __AUTH_CONST.__const: 0x228
   __AUTH_CONST.__cfstring: 0x300
-  __AUTH_CONST.__objc_const: 0x18f8
+  __AUTH_CONST.__objc_const: 0x1748
   __AUTH_CONST.__objc_intobj: 0x168
   __AUTH.__objc_data: 0x1e0
-  __DATA.__objc_ivar: 0x60
-  __DATA.__data: 0x128
+  __DATA.__objc_ivar: 0x64
+  __DATA.__data: 0x188
   __DATA.__bss: 0x8
   __DATA_DIRTY.__objc_data: 0x5a0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 426
-  Symbols:   671
-  CStrings:  540
+  Functions: 436
+  Symbols:   695
+  CStrings:  557
 
Symbols:
+ _OBJC_CLASS_$_ASDTNonSecurePathEnableProperty
+ __ZN4ASDT11IOMemoryMap7ReleaseEv
+ __ZN4ASDT11IOMemoryMapD1Ev
+ __ZN4ASDT11IOMemoryMapaSEOS0_
+ __ZN4ASDT12IOUserClient11SetPropertyERKN10applesauce2CF9StringRefERKNS2_13DictionaryRefEb
+ __ZN4ASDT12IOUserClient14OpenConnectionEv
+ __ZN4ASDT12IOUserClient9MapMemoryEjj
+ __ZN4ASDT12IOUserClientC2Ejj
+ __ZN4ASDT6Ramper7ProcessEjPKvPvNS_8Exclaves6Sensor6StatusE
+ __ZN4ASDT8Exclaves13StatusTracker6CreateERKNSt3__112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEE
+ __ZN4ASDT8IOPAudio5LPMic10UserClient15MapEngineStatusEv
+ __ZN4ASDT8IOPAudio8IOBuffer10UserClient11MapIOBufferEv
+ __ZN4ASDT9IOConnectC1Ev
+ __ZNK4ASDT12IOUserClient10CallMethodEjPKyjPKvmPyPjPvPmb
+ __ZNSt11logic_errorC2EPKc
+ __ZNSt12length_errorD1Ev
+ __ZTISt12length_error
+ __ZTVN4ASDT11IOMemoryMapE
+ __ZTVSt12length_error
+ __ZdlPv
+ __Znwm
+ _asdt_exclaves_available
+ _memmove
+ _strlen
- _OBJC_CLASS_$_NSMutableSet
- __ZN4ASDT12IOUserClient11SetPropertyERKN10applesauce2CF9StringRefERKNS2_13DictionaryRefE
- __ZN4ASDT12IOUserClient13ReleaseMemoryEPv
- __ZN4ASDT12IOUserClient14OpenConnectionEj
- __ZN4ASDT12IOUserClient9MapMemoryEjjRj
- __ZN4ASDT12IOUserClientC2Ej
- __ZN4ASDT12IOUserClientaSEj
- __ZN4ASDT8IOPAudio12VoiceTrigger10UserClientaSEj
- __ZN4ASDT8IOPAudio13ClientManager10UserClientaSEj
- __ZN4ASDT8IOPAudio16IsolatedIOBuffer10UserClientaSEj
- __ZN4ASDT8IOPAudio5LPMic10UserClient15MapEngineStatusERPNS1_12EngineStatusE
- __ZN4ASDT8IOPAudio5LPMic10UserClientaSEj
- __ZN4ASDT8IOPAudio8IOBuffer10UserClient11MapIOBufferERNS1_16BufferDescriptorE
- __ZN4ASDT8IOPAudio8IOBuffer10UserClientaSEj
- __ZNK4ASDT12IOUserClient10CallMethodEjPKyjPKvmPyPjPvPm
CStrings:
+ "%@: Failed to add non-secure input property."
+ "%@: Failed to allocate memory for status tracker."
+ "%@:%@: Bad physical format; ramper is nil."
+ "%@:%@: Bad stream format: Bbf: %u, period: %u"
+ "%@:%@: Non-secure input is disabled."
+ "@\"ASDTNonSecurePathEnableProperty\""
+ "ASDTExclavesStatusTrackerHostProtocol"
+ "T@\"ASDTNonSecurePathEnableProperty\",&,N,V_nonSecureInputEnableProperty"
+ "TI,R,N"
+ "T^*,R,N"
+ "^*16@0:8"
+ "_exclavesStatusTracker"
+ "_exclavesStatusTrackerOnce"
+ "_ioBufferMap"
+ "_memoryMap"
+ "_nonSecureInputEnableProperty"
+ "addCustomProperty:"
+ "asdtAddNonSecurePathEnable"
+ "basic_string"
+ "com.apple.sensors.mic"
+ "createForInput"
+ "enabled"
+ "exclavesStatusTracker"
+ "i24@0:8@16"
+ "ioBufferFramesSizeMax"
+ "ioBufferFramesUnexpectedSizeCount"
+ "ioBufferRef"
+ "nonSecureInputEnableProperty"
+ "nonSecureInputEnabled"
+ "performPowerStateIdle:"
+ "q"
+ "ramper"
+ "setNonSecureInputEnableProperty:"
+ "setupCustomProperties:"
+ "setupExclavesStatusTracker"
+ "setupPhysicalFormats:"
+ "setupSamplingRates:"
+ "subclassInitWithConfig:"
+ "{IOMemoryMap=\"_vptr$IOMemoryMap\"^^?\"mConnection\"{IOConnect=\"_vptr$IOConnect\"^^?\"mObject\"{shared_ptr<ASDT::IOConnect::Object>=\"__ptr_\"^{Object}\"__cntrl_\"^{__shared_weak_count}}\"mMutex\"{mutex=\"__m_\"{_opaque_pthread_mutex_t=\"__sig\"q\"__opaque\"[56c]}}\"mIsOpen\"B}\"mAddress\"^v\"mSize\"I\"mType\"I}"
+ "{unique_ptr<ASDT::Exclaves::StatusTracker, std::default_delete<ASDT::Exclaves::StatusTracker>>=\"__ptr_\"{__compressed_pair<ASDT::Exclaves::StatusTracker *, std::default_delete<ASDT::Exclaves::StatusTracker>>=\"__value_\"^{StatusTracker}}}"
+ "\xf0\x12"
+ "\xf0A"
+ "\xf0Q"
- "\""
- "%@: Sampling rate (%1.0lf) is not included in samplingRates!"
- "*"
- "*16@0:8"
- "-[ASDTIOPAudioIOBufferDevice releaseIOBuffer]"
- "1"
- "T*,N,V_ioBuffer"
- "TI,N,V_ioBufferSize"
- "^{EngineStatus=QQQQ}"
- "_descriptor"
- "_ioBuffer"
- "addObject:"
- "allObjects"
- "containsObject:"
- "d16@0:8"
- "defaultSamplingRate"
- "exclavesSensorManager"
- "ioBuffer"
- "samplingRates"
- "setIoBuffer:"
- "setIoBufferSize:"
- "setWithArray:"
- "setupCustomProperties"
- "statusTracker"
- "v24@0:8*16"
- "{BufferDescriptor=\"mBuffer\"*\"mSizeBytes\"I}"

```
