## AudioServerDriverTransports_IOP

> `/System/Library/PrivateFrameworks/AudioServerDriverTransports_IOP.framework/Versions/A/AudioServerDriverTransports_IOP`

```diff

-230.2.0.0.0
-  __TEXT.__text: 0xeb80
-  __TEXT.__auth_stubs: 0x530
-  __TEXT.__objc_methlist: 0xa90
-  __TEXT.__gcc_except_tab: 0x1234
-  __TEXT.__const: 0x128
-  __TEXT.__oslogstring: 0xdf5
-  __TEXT.__cstring: 0xe79
-  __TEXT.__unwind_info: 0x6f0
-  __TEXT.__objc_classname: 0x32e
-  __TEXT.__objc_methname: 0x11fb
-  __TEXT.__objc_methtype: 0x93e
-  __TEXT.__objc_stubs: 0x1200
-  __DATA_CONST.__got: 0x150
+240.42.0.0.0
+  __TEXT.__text: 0xf768
+  __TEXT.__auth_stubs: 0x5d0
+  __TEXT.__objc_methlist: 0xc2c
+  __TEXT.__gcc_except_tab: 0x13b0
+  __TEXT.__const: 0x150
+  __TEXT.__oslogstring: 0xe95
+  __TEXT.__cstring: 0xe6e
+  __TEXT.__unwind_info: 0x790
+  __TEXT.__objc_classname: 0x359
+  __TEXT.__objc_methname: 0x134d
+  __TEXT.__objc_methtype: 0xb25
+  __TEXT.__objc_stubs: 0x1300
+  __DATA_CONST.__got: 0x170
   __DATA_CONST.__const: 0x88
   __DATA_CONST.__objc_classlist: 0xc0
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x18
+  __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5a8
+  __DATA_CONST.__objc_selrefs: 0x678
   __DATA_CONST.__objc_superrefs: 0x90
-  __AUTH_CONST.__auth_got: 0x2b0
-  __AUTH_CONST.__const: 0x288
+  __AUTH_CONST.__auth_got: 0x300
+  __AUTH_CONST.__const: 0x2b8
   __AUTH_CONST.__cfstring: 0x300
-  __AUTH_CONST.__objc_const: 0x18f8
+  __AUTH_CONST.__objc_const: 0x1748
   __AUTH_CONST.__objc_intobj: 0x168
   __AUTH.__objc_data: 0x780
-  __DATA.__objc_ivar: 0x60
-  __DATA.__data: 0x128
+  __DATA.__objc_ivar: 0x64
+  __DATA.__data: 0x188
   __DATA.__bss: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2ED446BF-B229-368C-BAD3-FE853FF57225
-  Functions: 430
-  Symbols:   1068
-  CStrings:  562
+  UUID: 6BE48692-2489-3F6C-B403-13135D4FE80F
+  Functions: 442
+  Symbols:   1121
+  CStrings:  578
 
Symbols:
+ -[ASDTIOPAudioIOBufferDevice ioBufferRef]
+ -[ASDTIOPAudioLPMicDevice exclavesStatusTracker]
+ -[ASDTIOPAudioLPMicDevice nonSecureInputEnableProperty]
+ -[ASDTIOPAudioLPMicDevice nonSecureInputEnabled]
+ -[ASDTIOPAudioLPMicDevice performPowerStateIdle:]
+ -[ASDTIOPAudioLPMicDevice performPowerStatePrepare:].cold.2
+ -[ASDTIOPAudioLPMicDevice setNonSecureInputEnableProperty:]
+ -[ASDTIOPAudioLPMicDevice setupCustomProperties:]
+ -[ASDTIOPAudioLPMicDevice setupCustomProperties:].cold.1
+ -[ASDTIOPAudioLPMicDevice setupExclavesStatusTracker]
+ -[ASDTIOPAudioLPMicDevice setupSamplingRates:]
+ -[ASDTIOPAudioLPMicDevice subclassInitWithConfig:]
+ -[ASDTIOPAudioLPMicDevice subclassInitWithConfig:].cold.1
+ -[ASDTIOPAudioLPMicDevice subclassInitWithConfig:].cold.2
+ -[ASDTIOPAudioLPMicDevice subclassInitWithConfig:].cold.3
+ -[ASDTIOPAudioLPMicStream .cxx_construct]
+ -[ASDTIOPAudioLPMicStream ioBufferRef]
+ -[ASDTIOPAudioLPMicStream setupPhysicalFormats:]
+ ASDTIOPLogType.cold.1
+ GCC_except_table26
+ GCC_except_table33
+ GCC_except_table38
+ OBJC_IVAR_$_ASDTIOPAudioIOBufferDevice._memoryMap
+ OBJC_IVAR_$_ASDTIOPAudioLPMicDevice._exclavesStatusTracker
+ OBJC_IVAR_$_ASDTIOPAudioLPMicDevice._exclavesStatusTrackerOnce
+ OBJC_IVAR_$_ASDTIOPAudioLPMicDevice._nonSecureInputEnableProperty
+ OBJC_IVAR_$_ASDTIOPAudioLPMicStream._ioBufferMap
+ _OBJC_CLASS_$_ASDTNonSecurePathEnableProperty
+ _ZN4ASDT8IOPAudio5LPMic10UserClient15MapEngineStatusEv.cold.1
+ _ZN4ASDT8IOPAudio5LPMic10UserClient15MapEngineStatusEv.cold.2
+ _ZN4ASDT8IOPAudio8IOBuffer10UserClient11MapIOBufferEv.cold.1
+ __48-[ASDTIOPAudioLPMicDevice exclavesStatusTracker]_block_invoke.cold.1
+ __OBJC_$_PROP_LIST_ASDTExclavesStatusTrackerHostProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_ASDTExclavesStatusTrackerHostProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_ASDTExclavesStatusTrackerHostProtocol
+ __OBJC_$_PROTOCOL_REFS_ASDTExclavesStatusTrackerHostProtocol
+ __OBJC_LABEL_PROTOCOL_$_ASDTExclavesStatusTrackerHostProtocol
+ __OBJC_PROTOCOL_$_ASDTExclavesStatusTrackerHostProtocol
+ __ZN10applesauce2CF13DictionaryRef8from_getEPK14__CFDictionary
+ __ZN10applesauce2CF7details23find_at_key_or_optionalIjNS0_9StringRefEEENSt3__18optionalIT_EEPK14__CFDictionaryOT0_NS1_15counterpart_tagE
+ __ZN10applesauce2CF9ObjectRefIPK10__CFStringED1Ev
+ __ZN10applesauce2CF9ObjectRefIPK14__CFDictionaryED1Ev
+ __ZN4ASDT11IOMemoryMap7ReleaseEv
+ __ZN4ASDT11IOMemoryMapD1Ev
+ __ZN4ASDT11IOMemoryMapaSEOS0_
+ __ZN4ASDT12IOUserClient11SetPropertyERKN10applesauce2CF9StringRefERKNS2_13DictionaryRefEb
+ __ZN4ASDT12IOUserClient14OpenConnectionEv
+ __ZN4ASDT12IOUserClient9MapMemoryEjj
+ __ZN4ASDT12IOUserClientC2Ejj
+ __ZN4ASDT6Ramper7ProcessEjPKvPvNS_8Exclaves6Sensor6StatusE
+ __ZN4ASDT8Exclaves13StatusTracker6CreateERKNSt3__112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEE
+ __ZN4ASDT8IOPAudio12VoiceTrigger10UserClientC2Ejj
+ __ZN4ASDT8IOPAudio5LPMic10UserClient15MapEngineStatusEv
+ __ZN4ASDT8IOPAudio8IOBuffer10UserClient11MapIOBufferEv
+ __ZN4ASDT9IOConnectC1Ev
+ __ZNK4ASDT12IOUserClient10CallMethodEjPKyjPKvmPyPjPvPmb
+ __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne190102Ev
+ __ZNSt11logic_errorC2EPKc
+ __ZNSt12length_errorC1B8ne190102EPKc
+ __ZNSt12length_errorD1Ev
+ __ZNSt3__111shared_lockINS_12shared_mutexEED2B8ne190102Ev
+ __ZNSt3__111unique_lockINS_12shared_mutexEED2B8ne190102Ev
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne190102ILi0EEEPKc
+ __ZNSt3__120__throw_length_errorB8ne190102EPKc
+ __ZTISt12length_error
+ __ZTVN4ASDT11IOMemoryMapE
+ __ZTVSt12length_error
+ __ZdlPv
+ __Znwm
+ ___48-[ASDTIOPAudioLPMicDevice exclavesStatusTracker]_block_invoke
+ ___block_descriptor_40_ea8_32s_e5_v8?0l
+ ___block_descriptor_97_e195_i40?0I8r^{AudioServerPlugInIOCycleInfo=QI{AudioTimeStamp=dQdQ{SMPTETime=ssIIIssss}II}{AudioTimeStamp=dQdQ{SMPTETime=ssIIIssss}II}{AudioTimeStamp=dQdQ{SMPTETime=ssIIIssss}II}(?=dd)d}12^v20^v28I36l
+ ___copy_helper_block_ea8_32s
+ ___destroy_helper_block_ea8_32s
+ _asdt_exclaves_available
+ _memmove
+ _objc_msgSend$addCustomProperty:
+ _objc_msgSend$asdtAddNonSecurePathEnable
+ _objc_msgSend$createForInput
+ _objc_msgSend$enabled
+ _objc_msgSend$exclavesStatusTracker
+ _objc_msgSend$ioBufferFramesSizeMax
+ _objc_msgSend$ioBufferFramesUnexpectedSizeCount
+ _objc_msgSend$ioBufferRef
+ _objc_msgSend$lpMicEngineStatus
+ _objc_msgSend$nonSecureInputEnableProperty
+ _objc_msgSend$nonSecureInputEnabled
+ _objc_msgSend$ramper
+ _objc_msgSend$setNonSecureInputEnableProperty:
+ _objc_msgSend$setupCustomProperties:
+ _objc_msgSend$setupExclavesStatusTracker
+ _objc_msgSend$timestampPeriod
+ _strlen
- +[ASDTIOPAudioLPMicDevice defaultSamplingRate]
- -[ASDTIOPAudioIOBufferDevice ioBuffer]
- -[ASDTIOPAudioIOBufferDevice releaseIOBuffer].cold.1
- -[ASDTIOPAudioIOBufferDevice setIoBuffer:]
- -[ASDTIOPAudioIOBufferDevice setIoBufferSize:]
- -[ASDTIOPAudioLPMicDevice initWithConfig:withDeviceManager:andPlugin:].cold.2
- -[ASDTIOPAudioLPMicDevice initWithConfig:withDeviceManager:andPlugin:].cold.3
- -[ASDTIOPAudioLPMicDevice initWithConfig:withDeviceManager:andPlugin:].cold.4
- -[ASDTIOPAudioLPMicDevice initWithConfig:withDeviceManager:andPlugin:].cold.5
- -[ASDTIOPAudioLPMicDevice setupCustomProperties]
- -[ASDTIOPAudioLPMicDevice updateFromStreamDescription].cold.3
- -[ASDTIOPAudioLPMicStream ioBuffer]
- GCC_except_table18
- GCC_except_table32
- GCC_except_table34
- OBJC_IVAR_$_ASDTIOPAudioIOBufferDevice._descriptor
- OBJC_IVAR_$_ASDTIOPAudioIOBufferDevice._ioBuffer
- OBJC_IVAR_$_ASDTIOPAudioIOBufferDevice._ioBufferSize
- OBJC_IVAR_$_ASDTIOPAudioLPMicStream._ioBuffer
- _OBJC_CLASS_$_NSMutableSet
- _ZN4ASDT8IOPAudio5LPMic10UserClient15MapEngineStatusERPNS1_12EngineStatusE.cold.1
- _ZN4ASDT8IOPAudio5LPMic10UserClient15MapEngineStatusERPNS1_12EngineStatusE.cold.2
- _ZN4ASDT8IOPAudio8IOBuffer10UserClient11MapIOBufferERNS1_16BufferDescriptorE.cold.1
- __ZN10applesauce2CF13DictionaryRefC1EPK14__CFDictionary
- __ZN10applesauce2CF19DictionaryRef_proxy5at_asIjNS0_9StringRefEEENSt3__18optionalIT_EEOT0_
- __ZN4ASDT12IOUserClient11SetPropertyERKN10applesauce2CF9StringRefERKNS2_13DictionaryRefE
- __ZN4ASDT12IOUserClient13ReleaseMemoryEPv
- __ZN4ASDT12IOUserClient14OpenConnectionEj
- __ZN4ASDT12IOUserClient9MapMemoryEjjRj
- __ZN4ASDT12IOUserClientC2Ej
- __ZN4ASDT12IOUserClientaSEj
- __ZN4ASDT8IOPAudio12VoiceTrigger10UserClientC2Ej
- __ZN4ASDT8IOPAudio12VoiceTrigger10UserClientaSEj
- __ZN4ASDT8IOPAudio13ClientManager10UserClientaSEj
- __ZN4ASDT8IOPAudio16IsolatedIOBuffer10UserClientaSEj
- __ZN4ASDT8IOPAudio5LPMic10UserClient15MapEngineStatusERPNS1_12EngineStatusE
- __ZN4ASDT8IOPAudio5LPMic10UserClientaSEj
- __ZN4ASDT8IOPAudio8IOBuffer10UserClient11MapIOBufferERNS1_16BufferDescriptorE
- __ZN4ASDT8IOPAudio8IOBuffer10UserClientaSEj
- __ZNK4ASDT12IOUserClient10CallMethodEjPKyjPKvmPyPjPvPm
- __ZNSt3__111shared_lockINS_12shared_mutexEED2B8ne180100Ev
- __ZNSt3__111unique_lockINS_12shared_mutexEED2B8ne180100Ev
- ___block_descriptor_68_e195_i40?0I8r^{AudioServerPlugInIOCycleInfo=QI{AudioTimeStamp=dQdQ{SMPTETime=ssIIIssss}II}{AudioTimeStamp=dQdQ{SMPTETime=ssIIIssss}II}{AudioTimeStamp=dQdQ{SMPTETime=ssIIIssss}II}(?=dd)d}12^v20^v28I36l
- _objc_msgSend$addObject:
- _objc_msgSend$allObjects
- _objc_msgSend$containsObject:
- _objc_msgSend$exclavesSensorManager
- _objc_msgSend$samplingRates
- _objc_msgSend$setWithArray:
- _objc_msgSend$setupCustomProperties
- _objc_msgSend$statusTracker
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
