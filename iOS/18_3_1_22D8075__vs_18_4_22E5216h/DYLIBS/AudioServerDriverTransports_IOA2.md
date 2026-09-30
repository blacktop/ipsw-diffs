## AudioServerDriverTransports_IOA2

> `/System/Library/PrivateFrameworks/AudioServerDriverTransports_IOA2.framework/AudioServerDriverTransports_IOA2`

```diff

-230.2.0.0.0
-  __TEXT.__text: 0x35478
-  __TEXT.__auth_stubs: 0x1060
-  __TEXT.__objc_methlist: 0x1854
-  __TEXT.__gcc_except_tab: 0x5f24
-  __TEXT.__const: 0x710
-  __TEXT.__cstring: 0x1016
-  __TEXT.__oslogstring: 0x30d6
-  __TEXT.__unwind_info: 0x1e98
-  __TEXT.__objc_classname: 0x33e
-  __TEXT.__objc_methname: 0x2bbb
-  __TEXT.__objc_methtype: 0x1d9e
-  __TEXT.__objc_stubs: 0x2720
-  __DATA_CONST.__got: 0x280
-  __DATA_CONST.__const: 0x260
-  __DATA_CONST.__objc_classlist: 0xf0
+240.42.0.0.0
+  __TEXT.__text: 0x1e160
+  __TEXT.__auth_stubs: 0xae0
+  __TEXT.__objc_methlist: 0x11a4
+  __TEXT.__gcc_except_tab: 0x3fa8
+  __TEXT.__const: 0x130
+  __TEXT.__cstring: 0xe01
+  __TEXT.__oslogstring: 0x1835
+  __TEXT.__unwind_info: 0x1180
+  __TEXT.__objc_classname: 0x218
+  __TEXT.__objc_methname: 0x289b
+  __TEXT.__objc_methtype: 0x1446
+  __TEXT.__objc_stubs: 0x2260
+  __DATA_CONST.__got: 0x200
+  __DATA_CONST.__const: 0x210
+  __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc80
+  __DATA_CONST.__objc_selrefs: 0xbd8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0xd0
-  __AUTH_CONST.__auth_got: 0x840
-  __AUTH_CONST.__auth_ptr: 0x10
-  __AUTH_CONST.__const: 0x878
-  __AUTH_CONST.__cfstring: 0xc60
-  __AUTH_CONST.__objc_const: 0x2d28
+  __DATA_CONST.__objc_superrefs: 0x78
+  __AUTH_CONST.__auth_got: 0x580
+  __AUTH_CONST.__auth_ptr: 0x8
+  __AUTH_CONST.__const: 0xf8
+  __AUTH_CONST.__cfstring: 0xbe0
+  __AUTH_CONST.__objc_const: 0x1bd0
   __AUTH_CONST.__objc_intobj: 0x288
-  __AUTH.__objc_data: 0x960
-  __DATA.__objc_ivar: 0x198
+  __AUTH.__objc_data: 0x5a0
+  __DATA.__objc_ivar: 0x10c
   __DATA.__data: 0x1e8
-  __DATA.__common: 0x10
   __DATA.__bss: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1342
-  Symbols:   1816
-  CStrings:  1114
+  Functions: 670
+  Symbols:   982
+  CStrings:  932
 
Symbols:
+ _OBJC_CLASS_$_ASDTGlobalQueues
+ _OBJC_CLASS_$_ASDTNonSecurePathEnableProperty
+ __ZN4ASDT11IOMemoryMap7ReleaseEv
+ __ZN4ASDT11IOMemoryMapD1Ev
+ __ZN4ASDT11IOMemoryMapaSEOS0_
+ __ZN4ASDT12IOUserClient11SetPropertyERKN10applesauce2CF9StringRefEjb
+ __ZN4ASDT12IOUserClient14OpenConnectionEv
+ __ZN4ASDT12IOUserClient9MapMemoryEjj
+ __ZN4ASDT12IOUserClientC2Ejj
+ __ZN4ASDT14IOA2UserClient15MapEngineStatusEv
+ __ZN4ASDT14IOA2UserClient20MapIOBufferForStreamEj
+ __ZN4ASDT14IOA2UserClient21MapBlockControlBufferERKN10applesauce2CF13DictionaryRefE
+ __ZN4ASDT14IOA2UserClient26MapDataExchangeBlockBufferEj
+ __ZN4ASDT14IOA2UserClientC1Ejj
+ __ZN4ASDT14IOA2UserClientC2Ejj
+ __ZN4ASDT6Ramper7ProcessEjPKvPvNS_8Exclaves6Sensor6StatusE
+ __ZN4ASDT8Exclaves13StatusTracker6CreateERKNSt3__112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEE
+ __ZN4ASDT9IOConnectC1Ev
+ __ZNK4ASDT12IOUserClient10CallMethodEjPKyjPKvmPyPjPvPmb
+ __ZTVN4ASDT11IOMemoryMapE
+ _asdt_exclaves_available
+ _memset
+ _strlen
- _ASDTBaseLogType
- _CFArrayCreateMutable
- _CFArrayCreateMutableCopy
- _CFDictionaryCreateMutable
- _CFDictionaryCreateMutableCopy
- _CFEqual
- _CFStringCreateWithFormat
- _IOConnectCallMethod
- _IOConnectMapMemory64
- _IOConnectSetNotificationPort
- _IOConnectTrap0
- _IOConnectTrap6
- _IOConnectUnmapMemory64
- _IOIteratorNext
- _IOMainPort
- _IOObjectConformsTo
- _IOObjectIsEqualTo
- _IOObjectRelease
- _IOObjectRetain
- _IORegistryEntryCreateCFProperties
- _IORegistryEntryCreateCFProperty
- _IORegistryEntryGetChildIterator
- _IORegistryEntryGetParentIterator
- _IORegistryEntrySetCFProperty
- _IOServiceClose
- _IOServiceGetMatchingServices
- _IOServiceOpen
- _OBJC_CLASS_$_ASDTIOA2LegacyBooleanControl
- _OBJC_CLASS_$_ASDTIOA2LegacyControl
- _OBJC_CLASS_$_ASDTIOA2LegacyDevice
- _OBJC_CLASS_$_ASDTIOA2LegacyHeadsetInfoProperty
- _OBJC_CLASS_$_ASDTIOA2LegacyJackControl
- _OBJC_CLASS_$_ASDTIOA2LegacyLevelControl
- _OBJC_CLASS_$_ASDTIOA2LegacyMuteControl
- _OBJC_CLASS_$_ASDTIOA2LegacyOffsetStream
- _OBJC_CLASS_$_ASDTIOA2LegacyPhantomPowerControl
- _OBJC_CLASS_$_ASDTIOA2LegacyPhaseInvertControl
- _OBJC_CLASS_$_ASDTIOA2LegacySelectorControl
- _OBJC_CLASS_$_ASDTIOA2LegacyStream
- _OBJC_CLASS_$_ASDTStream
- _OBJC_CLASS_$_NSAssertionHandler
- _OBJC_METACLASS_$_ASDTIOA2LegacyBooleanControl
- _OBJC_METACLASS_$_ASDTIOA2LegacyControl
- _OBJC_METACLASS_$_ASDTIOA2LegacyDevice
- _OBJC_METACLASS_$_ASDTIOA2LegacyHeadsetInfoProperty
- _OBJC_METACLASS_$_ASDTIOA2LegacyJackControl
- _OBJC_METACLASS_$_ASDTIOA2LegacyLevelControl
- _OBJC_METACLASS_$_ASDTIOA2LegacyMuteControl
- _OBJC_METACLASS_$_ASDTIOA2LegacyOffsetStream
- _OBJC_METACLASS_$_ASDTIOA2LegacyPhantomPowerControl
- _OBJC_METACLASS_$_ASDTIOA2LegacyPhaseInvertControl
- _OBJC_METACLASS_$_ASDTIOA2LegacySelectorControl
- _OBJC_METACLASS_$_ASDTIOA2LegacyStream
- _OBJC_METACLASS_$_ASDTStream
- __ZN10CACFString10GetCStringEPK10__CFStringPcRjj
- __ZN12CADeprecated15CADispatchQueue11EventSource6RetainEv
- __ZN12CADeprecated15CADispatchQueue11EventSource7ReleaseEv
- __ZN12CADeprecated15CADispatchQueue13Dispatch_MainEbPvPFvS1_E
- __ZN12CADeprecated15CADispatchQueue13Dispatch_MainEbU13block_pointerFvvE
- __ZN12CADeprecated15CADispatchQueue15Dispatch_GlobalElbPvPFvS1_E
- __ZN12CADeprecated15CADispatchQueue15Dispatch_GlobalElbU13block_pointerFvvE
- __ZN12CADeprecated15CADispatchQueue18DispatchAfter_MainEyPvPFvS1_E
- __ZN12CADeprecated15CADispatchQueue18DispatchAfter_MainEyU13block_pointerFvvE
- __ZN12CADeprecated15CADispatchQueue18sGlobalSerialQueueE
- __ZN12CADeprecated15CADispatchQueue20DispatchAfter_GlobalElyPvPFvS1_E
- __ZN12CADeprecated15CADispatchQueue20DispatchAfter_GlobalElyU13block_pointerFvvE
- __ZN12CADeprecated15CADispatchQueue20GetGlobalSerialQueueEv
- __ZN12CADeprecated15CADispatchQueue22RemoveMachPortReceiverEjU13block_pointerFvvE
- __ZN12CADeprecated15CADispatchQueue22RemoveMachPortReceiverEjbb
- __ZN12CADeprecated15CADispatchQueue23InstallMachPortReceiverEjU13block_pointerFvvE
- __ZN12CADeprecated15CADispatchQueue27InitializeGlobalSerialQueueEPv
- __ZN12CADeprecated15CADispatchQueue29sGlobalSerialQueueInitializedE
- __ZN12CADeprecated15CADispatchQueue31RemoveMachPortDeathNotificationEj
- __ZN12CADeprecated15CADispatchQueue32InstallMachPortDeathNotificationEjU13block_pointerFvvE
- __ZN12CADeprecated15CADispatchQueueC1EPK10__CFString
- __ZN12CADeprecated15CADispatchQueueC1EPK10__CFStringP21dispatch_queue_attr_s
- __ZN12CADeprecated15CADispatchQueueC1EPK10__CFStringS3_
- __ZN12CADeprecated15CADispatchQueueC1EPK10__CFStringS3_P21dispatch_queue_attr_s
- __ZN12CADeprecated15CADispatchQueueC1EPKc
- __ZN12CADeprecated15CADispatchQueueC1EPKcP21dispatch_queue_attr_s
- __ZN12CADeprecated15CADispatchQueueC2EPK10__CFString
- __ZN12CADeprecated15CADispatchQueueC2EPK10__CFStringP21dispatch_queue_attr_s
- __ZN12CADeprecated15CADispatchQueueC2EPK10__CFStringS3_
- __ZN12CADeprecated15CADispatchQueueC2EPK10__CFStringS3_P21dispatch_queue_attr_s
- __ZN12CADeprecated15CADispatchQueueC2EPKc
- __ZN12CADeprecated15CADispatchQueueC2EPKcP21dispatch_queue_attr_s
- __ZN12CADeprecated15CADispatchQueueD0Ev
- __ZN12CADeprecated15CADispatchQueueD1Ev
- __ZN12CADeprecated15CADispatchQueueD2Ev
- __ZN12CADeprecated7CAMutex3TryERb
- __ZN12CADeprecated7CAMutex4LockEv
- __ZN12CADeprecated7CAMutex6UnlockEv
- __ZN12CADeprecated7CAMutex8UnlockerC1ERS0_
- __ZN12CADeprecated7CAMutex8UnlockerC2ERS0_
- __ZN12CADeprecated7CAMutex8UnlockerD1Ev
- __ZN12CADeprecated7CAMutex8UnlockerD2Ev
- __ZN12CADeprecated7CAMutexC1EPKc
- __ZN12CADeprecated7CAMutexC2EPKc
- __ZN12CADeprecated7CAMutexD0Ev
- __ZN12CADeprecated7CAMutexD1Ev
- __ZN12CADeprecated7CAMutexD2Ev
- __ZN13CAVolumeCurve10ResetRangeEv
- __ZN13CAVolumeCurve19SetTransferFunctionEj
- __ZN13CAVolumeCurve8AddRangeEiiff
- __ZN13CAVolumeCurveC1Ev
- __ZN13CAVolumeCurveC2Ev
- __ZN14CACFDictionary8AddArrayEPK10__CFStringPK9__CFArray
- __ZN14CACFDictionary9AddSInt32EPK10__CFStringi
- __ZN14CACFDictionary9AddUInt32EPK10__CFStringj
- __ZN14CACFDictionary9AddUInt64EPK10__CFStringy
- __ZN17CAAudioValueRange20PickCommonSampleRateERK15AudioValueRange
- __ZN24CAStreamBasicDescription12IsEquivalentERK27AudioStreamBasicDescriptionS2_j
- __ZN4ASDT10UCIterator14SetWillReleaseEb
- __ZN4ASDT10UCIterator4NextEv
- __ZN4ASDT10UCIterator6RetainEv
- __ZN4ASDT10UCIterator7ReleaseEv
- __ZN4ASDT10UCIteratorC1EP14__CFDictionary
- __ZN4ASDT10UCIteratorC1ERKS0_
- __ZN4ASDT10UCIteratorC1EjPKc
- __ZN4ASDT10UCIteratorC1EjPKcb
- __ZN4ASDT10UCIteratorC1Ejb
- __ZN4ASDT10UCIteratorC1Ev
- __ZN4ASDT10UCIteratorC2EP14__CFDictionary
- __ZN4ASDT10UCIteratorC2ERKS0_
- __ZN4ASDT10UCIteratorC2EjPKc
- __ZN4ASDT10UCIteratorC2EjPKcb
- __ZN4ASDT10UCIteratorC2Ejb
- __ZN4ASDT10UCIteratorC2Ev
- __ZN4ASDT10UCIteratorD1Ev
- __ZN4ASDT10UCIteratorD2Ev
- __ZN4ASDT10UCIteratoraSERKS0_
- __ZN4ASDT10UCIteratoraSEj
- __ZN4ASDT12IOA2UCDevice13CopyDeviceUIDEj
- __ZN4ASDT12IOA2UCDevice15MapEngineStatusERP20IOAudio2EngineStatus
- __ZN4ASDT12IOA2UCDevice15SetControlValueEjPj
- __ZN4ASDT12IOA2UCDevice15SetHogModeOwnerEi
- __ZN4ASDT12IOA2UCDevice15SetStreamActiveEjb
- __ZN4ASDT12IOA2UCDevice15StopIOWithFlagsEy
- __ZN4ASDT12IOA2UCDevice16SetupVolumeCurveEPK14__CFDictionaryR13CAVolumeCurve
- __ZN4ASDT12IOA2UCDevice16StartIOWithFlagsEy
- __ZN4ASDT12IOA2UCDevice18BestMatchForFormatEPK9__CFArrayRK27AudioStreamBasicDescriptionRS4_
- __ZN4ASDT12IOA2UCDevice18ReplaceControlInfoEj
- __ZN4ASDT12IOA2UCDevice18ReplaceControlListEv
- __ZN4ASDT12IOA2UCDevice18SupportsPreWarmingEj
- __ZN4ASDT12IOA2UCDevice18SupportsPreWarmingEv
- __ZN4ASDT12IOA2UCDevice19PerformConfigChangeERK20IOAudio2Notification
- __ZN4ASDT12IOA2UCDevice19ReleaseEngineStatusEP20IOAudio2EngineStatus
- __ZN4ASDT12IOA2UCDevice19ReplaceControlValueEji
- __ZN4ASDT12IOA2UCDevice20CopyControlInfo_NameEPK14__CFDictionary
- __ZN4ASDT12IOA2UCDevice20GetControlInfo_ClassEPK14__CFDictionary
- __ZN4ASDT12IOA2UCDevice20GetControlInfo_ScopeEPK14__CFDictionary
- __ZN4ASDT12IOA2UCDevice20GetControlInfo_ValueEPK14__CFDictionary
- __ZN4ASDT12IOA2UCDevice20MapIOBufferForStreamEjRjRPh
- __ZN4ASDT12IOA2UCDevice20MoveBlockControlDataEjjj
- __ZN4ASDT12IOA2UCDevice20SetClientDescriptionEyd
- __ZN4ASDT12IOA2UCDevice20SetMultiControlValueEjPKjjPjS3_
- __ZN4ASDT12IOA2UCDevice20SetNominalSampleRateEd
- __ZN4ASDT12IOA2UCDevice21MapBlockControlBufferEPK14__CFDictionaryjRjRPh
- __ZN4ASDT12IOA2UCDevice22GetControlInfo_ElementEPK14__CFDictionary
- __ZN4ASDT12IOA2UCDevice22GetControlInfo_VariantEPK14__CFDictionary
- __ZN4ASDT12IOA2UCDevice22SetStreamCurrentFormatEjRK27AudioStreamBasicDescription
- __ZN4ASDT12IOA2UCDevice24GetControlInfo_BaseClassEPK14__CFDictionary
- __ZN4ASDT12IOA2UCDevice24ReleaseIOBufferForStreamEjPh
- __ZN4ASDT12IOA2UCDevice24ReplaceMultiControlValueEP14__CFDictionaryPKjj
- __ZN4ASDT12IOA2UCDevice24ReplaceMultiControlValueEjPKjj
- __ZN4ASDT12IOA2UCDevice25CopyControlDictionaryByIDEPK9__CFArrayj
- __ZN4ASDT12IOA2UCDevice25CopyControlDictionaryByIDEj
- __ZN4ASDT12IOA2UCDevice25GetControlInfo_IsReadOnlyEPK14__CFDictionary
- __ZN4ASDT12IOA2UCDevice25MoveDataExchangeBlockDataEjbj
- __ZN4ASDT12IOA2UCDevice25ReleaseBlockControlBufferEjPh
- __ZN4ASDT12IOA2UCDevice26MapDataExchangeBlockBufferEjRjRPh
- __ZN4ASDT12IOA2UCDevice27ConstructASBDFromDictionaryEPK14__CFDictionaryR27AudioStreamBasicDescription
- __ZN4ASDT12IOA2UCDevice27ConstructASRDFromDictionaryEPK14__CFDictionaryR28AudioStreamRangedDescription
- __ZN4ASDT12IOA2UCDevice27ConstructDictionaryFromASBDERK27AudioStreamBasicDescription
- __ZN4ASDT12IOA2UCDevice28CopyControlDictionaryByIndexEPK9__CFArrayj
- __ZN4ASDT12IOA2UCDevice28CopyControlDictionaryByIndexEj
- __ZN4ASDT12IOA2UCDevice29CopyLevelControlInfo_RangeMapEPK14__CFDictionary
- __ZN4ASDT12IOA2UCDevice29GetControlDictionaryIndexByIDEPK9__CFArrayjRj
- __ZN4ASDT12IOA2UCDevice30ReleaseDataExchangeBlockBufferEjPh
- __ZN4ASDT12IOA2UCDevice31CopyBlockControlInfo_DescriptorEPK14__CFDictionary
- __ZN4ASDT12IOA2UCDevice33CopyControlInfo_PropertySelectorsEPK14__CFDictionary
- __ZN4ASDT12IOA2UCDevice33GetSliderControlInfo_MaximumValueEPK14__CFDictionary
- __ZN4ASDT12IOA2UCDevice33GetSliderControlInfo_MinimumValueEPK14__CFDictionary
- __ZN4ASDT12IOA2UCDevice33GetStereoPanControlInfo_LeftValueEPK14__CFDictionary
- __ZN4ASDT12IOA2UCDevice34GetStereoPanControlInfo_RightValueEPK14__CFDictionary
- __ZN4ASDT12IOA2UCDevice35CopySelectorControlInfo_SelectorMapEPK14__CFDictionary
- __ZN4ASDT12IOA2UCDevice35GetStereoPanControlInfo_CenterValueEPK14__CFDictionary
- __ZN4ASDT12IOA2UCDevice35GetStereoPanControlInfo_LeftChannelEPK14__CFDictionary
- __ZN4ASDT12IOA2UCDevice36GetLevelControlInfo_TransferFunctionEPK14__CFDictionary
- __ZN4ASDT12IOA2UCDevice36GetStereoPanControlInfo_RightChannelEPK14__CFDictionary
- __ZN4ASDT12IOA2UCDevice42CopySelectorControlInfo_MultiSelectorValueEPK14__CFDictionary
- __ZN4ASDT12IOA2UCDevice4DoIOEbjyy
- __ZN4ASDT12IOA2UCDevice6StopIOEv
- __ZN4ASDT12IOA2UCDevice7StartIOEv
- __ZN4ASDT12IOA2UCDevice9IsPrivateEj
- __ZN4ASDT12IOA2UCDeviceC1EPK14__CFDictionary
- __ZN4ASDT12IOA2UCDeviceC1ERKS0_
- __ZN4ASDT12IOA2UCDeviceC1Ej
- __ZN4ASDT12IOA2UCDeviceC1Ev
- __ZN4ASDT12IOA2UCDeviceC2EPK14__CFDictionary
- __ZN4ASDT12IOA2UCDeviceC2ERKS0_
- __ZN4ASDT12IOA2UCDeviceC2Ej
- __ZN4ASDT12IOA2UCDeviceC2Ev
- __ZN4ASDT12IOA2UCDeviceD0Ev
- __ZN4ASDT12IOA2UCDeviceD1Ev
- __ZN4ASDT12IOA2UCDeviceD2Ev
- __ZN4ASDT12IOA2UCDeviceaSERKS0_
- __ZN4ASDT12IOA2UCDeviceaSEj
- __ZN4ASDT12IOUserClient11SetPropertyERKN10applesauce2CF9StringRefEj
- __ZN4ASDT12IOUserClient13ReleaseMemoryEPv
- __ZN4ASDT12IOUserClient14OpenConnectionEj
- __ZN4ASDT12IOUserClient9MapMemoryEjjRj
- __ZN4ASDT12IOUserClientC2Ej
- __ZN4ASDT12IOUserClientaSEj
- __ZN4ASDT14IOA2UserClient15MapEngineStatusERP20IOAudio2EngineStatus
- __ZN4ASDT14IOA2UserClient20MapIOBufferForStreamEjRjRPh
- __ZN4ASDT14IOA2UserClient21MapBlockControlBufferERKN10applesauce2CF13DictionaryRefERjRPh
- __ZN4ASDT14IOA2UserClient26MapDataExchangeBlockBufferEjRjRPh
- __ZN4ASDT14IOA2UserClientC1Ej
- __ZN4ASDT14IOA2UserClientC2Ej
- __ZN4ASDT14IOA2UserClientaSEj
- __ZN4ASDT8UCObject10CallMethodEjPKyjPKvmPyPjPvPm
- __ZN4ASDT8UCObject10ConformsToEPKc
- __ZN4ASDT8UCObject10CopyObjectEv
- __ZN4ASDT8UCObject11SetPropertyEPK10__CFStringPKv
- __ZN4ASDT8UCObject11SetPropertyEjPK10__CFStringPKv
- __ZN4ASDT8UCObject13ReleaseMemoryEPvj
- __ZN4ASDT8UCObject14OpenConnectionEj
- __ZN4ASDT8UCObject15CloseConnectionEv
- __ZN4ASDT8UCObject15TestForLivenessEj
- __ZN4ASDT8UCObject16SetProperty_boolEPK10__CFStringb
- __ZN4ASDT8UCObject16SetProperty_boolEjPK10__CFStringb
- __ZN4ASDT8UCObject17CopyProperty_boolEjPK10__CFStringRb
- __ZN4ASDT8UCObject17PropertiesChangedEv
- __ZN4ASDT8UCObject18SetProperty_SInt32EPK10__CFStringi
- __ZN4ASDT8UCObject18SetProperty_SInt32EjPK10__CFStringi
- __ZN4ASDT8UCObject18SetProperty_UInt32EPK10__CFStringj
- __ZN4ASDT8UCObject18SetProperty_UInt32EjPK10__CFStringj
- __ZN4ASDT8UCObject19CopyProperty_SInt32EjPK10__CFStringRi
- __ZN4ASDT8UCObject19CopyProperty_UInt32EjPK10__CFStringRj
- __ZN4ASDT8UCObject20CopyProperty_CFArrayEjPK10__CFStringRPK9__CFArray
- __ZN4ASDT8UCObject20ServiceWasTerminatedEv
- __ZN4ASDT8UCObject21CopyParentByClassNameEjPKcS2_
- __ZN4ASDT8UCObject21CopyProperty_CFStringEjPK10__CFStringRS3_
- __ZN4ASDT8UCObject23CopyProperty_CACFStringEjPK10__CFStringR10CACFString
- __ZN4ASDT8UCObject25CopyProperty_CFDictionaryEjPK10__CFStringRPK14__CFDictionary
- __ZN4ASDT8UCObject29SetConnectionNotificationPortEjjPv
- __ZN4ASDT8UCObject34CopyChildWithIntegerPropertyValuesEjPK10__CFStringjS3_j
- __ZN4ASDT8UCObject35CopyMatchingObjectWithPropertyValueEPK14__CFDictionaryPK10__CFStringPKv
- __ZN4ASDT8UCObject5ClearEv
- __ZN4ASDT8UCObject6RetainEv
- __ZN4ASDT8UCObject7ReleaseEv
- __ZN4ASDT8UCObject8CallTrapEj
- __ZN4ASDT8UCObject9MapMemoryEjjRj
- __ZN4ASDT8UCObjectC1EPK14__CFDictionary
- __ZN4ASDT8UCObjectC1ERKS0_
- __ZN4ASDT8UCObjectC1Ej
- __ZN4ASDT8UCObjectC1Ev
- __ZN4ASDT8UCObjectC2EPK14__CFDictionary
- __ZN4ASDT8UCObjectC2ERKS0_
- __ZN4ASDT8UCObjectC2Ej
- __ZN4ASDT8UCObjectC2Ev
- __ZN4ASDT8UCObjectD0Ev
- __ZN4ASDT8UCObjectD1Ev
- __ZN4ASDT8UCObjectD2Ev
- __ZN4ASDT8UCObjectaSERKS0_
- __ZN4ASDT8UCObjectaSEj
- __ZN9CACFArray12AppendUInt32Ej
- __ZN9CACFArray13SetDictionaryEjPK14__CFDictionary
- __ZN9CACFArray16AppendDictionaryEPK14__CFDictionary
- __ZN9CAProcess13ProcessExistsEi
- __ZN9CAProcess6GetPIDEv
- __ZNK10CACFNumber10GetFixed32Ev
- __ZNK10CACFNumber10GetFixed64Ev
- __ZNK12CADeprecated15CADispatchQueue15DispatchBarrierEbPvPFvS1_E
- __ZNK12CADeprecated15CADispatchQueue15DispatchBarrierEbU13block_pointerFvvE
- __ZNK12CADeprecated15CADispatchQueue8DispatchEbPvPFvS1_E
- __ZNK12CADeprecated15CADispatchQueue8DispatchEbU13block_pointerFvvE
- __ZNK12CADeprecated15CADispatchQueue8DispatchEyPvPFvS1_E
- __ZNK12CADeprecated15CADispatchQueue8DispatchEyU13block_pointerFvvE
- __ZNK12CADeprecated7CAMutex22IsOwnedByCurrentThreadEv
- __ZNK12CADeprecated7CAMutex6IsFreeEv
- __ZNK13CAVolumeCurve12GetMaximumDBEv
- __ZNK13CAVolumeCurve12GetMinimumDBEv
- __ZNK13CAVolumeCurve13GetMaximumRawEv
- __ZNK13CAVolumeCurve13GetMinimumRawEv
- __ZNK13CAVolumeCurve14ConvertDBToRawEf
- __ZNK13CAVolumeCurve14ConvertRawToDBEi
- __ZNK13CAVolumeCurve17ConvertDBToScalarEf
- __ZNK13CAVolumeCurve17ConvertScalarToDBEf
- __ZNK13CAVolumeCurve18CheckForContinuityEv
- __ZNK13CAVolumeCurve18ConvertRawToScalarEi
- __ZNK13CAVolumeCurve18ConvertScalarToRawEf
- __ZNK13CAVolumeCurve29GetIsApplyingTransferFunctionEv
- __ZNK14CACFDictionary10GetFixed64EPK10__CFStringRd
- __ZNK14CACFDictionary12GetCACFArrayEPK10__CFStringR9CACFArray
- __ZNK14CACFDictionary13GetDictionaryEPK10__CFStringRPK14__CFDictionary
- __ZNK14CACFDictionary6HasKeyEPK10__CFString
- __ZNK14CACFDictionary7GetBoolEPK10__CFStringRb
- __ZNK14CACFDictionary8GetArrayEPK10__CFStringRPK9__CFArray
- __ZNK14CACFDictionary9GetCFTypeEPK10__CFStringRPKv
- __ZNK14CACFDictionary9GetSInt32EPK10__CFStringRi
- __ZNK14CACFDictionary9GetStringEPK10__CFStringRS2_
- __ZNK14CACFDictionary9GetUInt32EPK10__CFStringRj
- __ZNK14CACFDictionary9GetUInt64EPK10__CFStringRy
- __ZNK4ASDT10UCIterator11GetIteratorEv
- __ZNK4ASDT10UCIterator7IsValidEv
- __ZNK4ASDT12IOA2UCDevice10GetLatencyEb
- __ZNK4ASDT12IOA2UCDevice12CopyModelUIDEv
- __ZNK4ASDT12IOA2UCDevice13CopyDeviceUIDEv
- __ZNK4ASDT12IOA2UCDevice14CopyDeviceNameEv
- __ZNK4ASDT12IOA2UCDevice14CopyStreamListEb
- __ZNK4ASDT12IOA2UCDevice14GetClockDomainEv
- __ZNK4ASDT12IOA2UCDevice15CopyChannelNameEbj
- __ZNK4ASDT12IOA2UCDevice15CopyControlListEv
- __ZNK4ASDT12IOA2UCDevice15CopyHeadsetInfoEv
- __ZNK4ASDT12IOA2UCDevice15GetHogModeOwnerEv
- __ZNK4ASDT12IOA2UCDevice15GetSafetyOffsetEb
- __ZNK4ASDT12IOA2UCDevice16GetNumberStreamsEb
- __ZNK4ASDT12IOA2UCDevice16GetTransportTypeEv
- __ZNK4ASDT12IOA2UCDevice17GetRingBufferSizeEv
- __ZNK4ASDT12IOA2UCDevice17WantsDoIOTrapCallEb
- __ZNK4ASDT12IOA2UCDevice18CanBeDefaultDeviceEbb
- __ZNK4ASDT12IOA2UCDevice20GetNominalSampleRateEv
- __ZNK4ASDT12IOA2UCDevice21CopyChannelNumberNameEbj
- __ZNK4ASDT12IOA2UCDevice22CopyCustomPropertyInfoEv
- __ZNK4ASDT12IOA2UCDevice22CopyDeviceManufacturerEv
- __ZNK4ASDT12IOA2UCDevice22CopyResourceBundlePathEv
- __ZNK4ASDT12IOA2UCDevice23CopyChannelCategoryNameEbj
- __ZNK4ASDT12IOA2UCDevice23GetStreamInfoByID_IndexEj
- __ZNK4ASDT12IOA2UCDevice23GetStreamInfoByIndex_IDEbj
- __ZNK4ASDT12IOA2UCDevice24CopyDefaultChannelLayoutEb
- __ZNK4ASDT12IOA2UCDevice24CopyStreamDictionaryByIDEj
- __ZNK4ASDT12IOA2UCDevice25CopyDataExchangeBlockListEv
- __ZNK4ASDT12IOA2UCDevice25GetStreamInfoByID_LatencyEj
- __ZNK4ASDT12IOA2UCDevice25SupportsClientDescriptionEv
- __ZNK4ASDT12IOA2UCDevice27CopyStreamDictionaryByIndexEbj
- __ZNK4ASDT12IOA2UCDevice27GetNumberDataExchangeBlocksEv
- __ZNK4ASDT12IOA2UCDevice28GetStreamInfoByIndex_LatencyEbj
- __ZNK4ASDT12IOA2UCDevice30GetStreamInfoByID_TerminalTypeEj
- __ZNK4ASDT12IOA2UCDevice31GetStreamInfoByID_CurrentFormatEjR27AudioStreamBasicDescription
- __ZNK4ASDT12IOA2UCDevice33GetStreamInfoByID_StartingChannelEj
- __ZNK4ASDT12IOA2UCDevice33GetStreamInfoByIndex_TerminalTypeEbj
- __ZNK4ASDT12IOA2UCDevice34GetStreamInfoByIndex_CurrentFormatEbjR27AudioStreamBasicDescription
- __ZNK4ASDT12IOA2UCDevice35CopyDataExchangeBlockDictionaryByIDEj
- __ZNK4ASDT12IOA2UCDevice35CopyStreamInfoByID_AvailableFormatsEj
- __ZNK4ASDT12IOA2UCDevice36CopyConfigurationApplicationBundleIDEv
- __ZNK4ASDT12IOA2UCDevice36GetStreamInfoByIndex_StartingChannelEbj
- __ZNK4ASDT12IOA2UCDevice38CopyDataExchangeBlockDictionaryByIndexEj
- __ZNK4ASDT12IOA2UCDevice38CopyStreamInfoByIndex_AvailableFormatsEbj
- __ZNK4ASDT12IOA2UCDevice8IsHiddenEv
- __ZNK4ASDT12IOA2UCDevice9IsRunningEv
- __ZNK4ASDT12IOUserClient10CallMethodEjPKyjPKvmPyPjPvPm
- __ZNK4ASDT12IOUserClient10SharedLockEv
- __ZNK4ASDT8UCObject11HasPropertyEPK10__CFString
- __ZNK4ASDT8UCObject14CopyPropertiesEv
- __ZNK4ASDT8UCObject14IsServiceAliveEv
- __ZNK4ASDT8UCObject15CachePropertiesEv
- __ZNK4ASDT8UCObject16IsConnectionOpenEv
- __ZNK4ASDT8UCObject17CopyProperty_boolEPK10__CFStringRb
- __ZNK4ASDT8UCObject19CopyProperty_CFDataEPK10__CFStringRPK8__CFData
- __ZNK4ASDT8UCObject19CopyProperty_CFTypeEPK10__CFStringRPKv
- __ZNK4ASDT8UCObject19CopyProperty_SInt32EPK10__CFStringRi
- __ZNK4ASDT8UCObject19CopyProperty_UInt32EPK10__CFStringRj
- __ZNK4ASDT8UCObject20CopyProperty_CFArrayEPK10__CFStringRPK9__CFArray
- __ZNK4ASDT8UCObject20CopyProperty_Fixed32EPK10__CFStringRf
- __ZNK4ASDT8UCObject20CopyProperty_Fixed64EPK10__CFStringRd
- __ZNK4ASDT8UCObject21CopyProperty_CACFTypeEPK10__CFStringR10CACFObjectIPKvE
- __ZNK4ASDT8UCObject21CopyProperty_CFStringEPK10__CFStringRS3_
- __ZNK4ASDT8UCObject22CopyProperty_CACFArrayEPK10__CFStringR9CACFArray
- __ZNK4ASDT8UCObject23CopyProperty_CACFStringEPK10__CFStringR10CACFString
- __ZNK4ASDT8UCObject25CopyProperty_CFDictionaryEPK10__CFStringRPK14__CFDictionary
- __ZNK4ASDT8UCObject27CopyProperty_CACFDictionaryEPK10__CFStringR14CACFDictionary
- __ZNK4ASDT8UCObject7IsValidEv
- __ZNK4ASDT8UCObject9GetObjectEv
- __ZNK4ASDT8UCObject9IsEqualToEj
- __ZNK9CACFArray13GetDictionaryEjRPK14__CFDictionary
- __ZNK9CACFArray17GetCACFDictionaryEjR14CACFDictionary
- __ZNK9CACFArray9GetUInt32EjRj
- __ZNKSt9exception4whatEv
- __ZNSt13runtime_errorC1ERKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEPKc
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEPKcm
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6insertEmPKc
- __ZNSt3__16chrono12steady_clock3nowEv
- __ZNSt3__19to_stringEd
- __ZNSt9exceptionD2Ev
- __ZTIN12CADeprecated15CADispatchQueueE
- __ZTIN12CADeprecated7CAMutexE
- __ZTIN4ASDT12IOA2UCDeviceE
- __ZTIN4ASDT8UCObjectE
- __ZTISt9exception
- __ZTIi
- __ZTSN12CADeprecated15CADispatchQueueE
- __ZTSN12CADeprecated7CAMutexE
- __ZTSN4ASDT12IOA2UCDeviceE
- __ZTSN4ASDT8UCObjectE
- __ZTVN10__cxxabiv117__class_type_infoE
- __ZTVN10__cxxabiv121__vmi_class_type_infoE
- __ZTVN12CADeprecated15CADispatchQueueE
- __ZTVN12CADeprecated7CAMutexE
- __ZTVN4ASDT12IOA2UCDeviceE
- __ZTVN4ASDT8UCObjectE
- ___cxa_end_catch
- ___udivti3
- __dispatch_main_q
- __dispatch_queue_attr_concurrent
- __dispatch_source_type_mach_recv
- __dispatch_source_type_mach_send
- _bootstrap_port
- _dispatch_after_f
- _dispatch_async_f
- _dispatch_barrier_async
- _dispatch_barrier_async_f
- _dispatch_barrier_sync
- _dispatch_barrier_sync_f
- _dispatch_get_global_queue
- _dispatch_once_f
- _dispatch_release
- _dispatch_resume
- _dispatch_retain
- _dispatch_source_cancel
- _dispatch_source_create
- _dispatch_source_set_cancel_handler
- _dispatch_source_set_event_handler
- _dispatch_sync_f
- _kASDTIOA2LegacyDeviceKeyDeviceUID
- _kASDTIOA2LegacyDeviceKeyIsPrivate
- _kIOMainPortDefault
- _mach_port_deallocate
- _mach_port_mod_refs
- _mach_task_self_
- _objc_release_x9
- _objc_retain_x23
- _objc_retain_x28
- _powf
- _pthread_equal
- _pthread_mutex_destroy
- _pthread_mutex_init
- _pthread_mutex_lock
- _pthread_mutex_trylock
- _pthread_mutex_unlock
- _pthread_self
- _strcmp
CStrings:
+ "%@: Failed to add non-secure input property."
+ "%@: Failed to allocate memory for status tracker."
+ "%@: Failed to get stream dictionary for ID: %u"
+ "%@:%@: Bad physical format; ramper is nil."
+ "%@:%@: Bad stream format: Bbf: %u, period: %u"
+ "%@:%@: Non-secure input is disabled."
+ "@\"ASDTNonSecurePathEnableProperty\""
+ "ASDTExclavesStatusTrackerHostProtocol"
+ "T@\"ASDTNonSecurePathEnableProperty\",&,N,V_nonSecureInputEnableProperty"
+ "T^v,R,N"
+ "^*16@0:8"
+ "_exclavesStatusTracker"
+ "_exclavesStatusTrackerOnce"
+ "_ioBufferMap"
+ "_nonSecureInputEnableProperty"
+ "_setupExclavesStatusTracker"
+ "asdtAddNonSecurePathEnable"
+ "basic_string"
+ "com.apple.sensors.mic"
+ "concurrent"
+ "createForInput"
+ "enabled"
+ "exclavesStatusTracker"
+ "ioBufferFramesSizeMax"
+ "ioBufferFramesUnexpectedSizeCount"
+ "ioBufferRef"
+ "nonSecureInputEnableProperty"
+ "nonSecureInputEnabled"
+ "ramper"
+ "setNonSecureInputEnableProperty:"
+ "setupPhysicalFormats:"
+ "setupSamplingRates:"
+ "subclassInitWithConfig:"
+ "{IOMemoryMap=\"_vptr$IOMemoryMap\"^^?\"mConnection\"{IOConnect=\"_vptr$IOConnect\"^^?\"mObject\"{shared_ptr<ASDT::IOConnect::Object>=\"__ptr_\"^{Object}\"__cntrl_\"^{__shared_weak_count}}\"mMutex\"{mutex=\"__m_\"{_opaque_pthread_mutex_t=\"__sig\"q\"__opaque\"[56c]}}\"mIsOpen\"B}\"mAddress\"^v\"mSize\"I\"mType\"I}"
+ "{unique_ptr<ASDT::Exclaves::StatusTracker, std::default_delete<ASDT::Exclaves::StatusTracker>>=\"__ptr_\"{__compressed_pair<ASDT::Exclaves::StatusTracker *, std::default_delete<ASDT::Exclaves::StatusTracker>>=\"__value_\"^{StatusTracker}}}"
+ "\xf01"
+ "\xf0\x91"
+ "\xf0\xa1"
+ "\xf0\xf0\xf0\xf0\xb2\x13\x13"
- "\x01\x11"
- " "
- " CADispatchQueue::CADispatchQueue: failed to create the dispatch queue"
- " CADispatchQueue::GetGlobalSerialQueue: there is no global serial queue"
- " CADispatchQueue::InstallMachPortDeathNotification: a mach port is required"
- " CADispatchQueue::InstallMachPortDeathNotification: failed to create the mach port event source"
- " CADispatchQueue::InstallMachPortReceiver: a mach port is required"
- " CADispatchQueue::InstallMachPortReceiver: failed to create the mach port event source"
- " CADispatchQueue::RemoveMachPortReceiver: deallocating the receive right failed, Error: 0x%X"
- " CADispatchQueue::RemoveMachPortReceiver: deallocating the send right failed, Error: 0x%X"
- " CADispatchQueue::~CADispatchQueue: Implicitly removing the mach port receviers. It is best to explicitly call RemoveMachPortRecevier()."
- " CAMutex::CAMutex: Could not init the mutex"
- " CAMutex::Lock: Could not lock the mutex"
- " CAMutex::Try: call to pthread_mutex_trylock failed, Error: %d (%s)"
- " CAMutex::Unlock: A thread is attempting to unlock a Mutex it doesn't own"
- " CAMutex::Unlock: Could not unlock the mutex"
- " CAVolumeCurve::AddRange: new point overlaps"
- " ExistingSampleRate: "
- " HALS_IOA2Device::_IOAudio2DeviceNotificationPortMessageHandler: failed to receive the message, Error: 0x%X"
- " HAL_IOA2PhysicalDevice::SetMultiControlValue: got an error when telling the hardware to change a multi control value, Error: 0x%X"
- " IOA2UCDevice::CopyHeadsetInfo: could not allocate an empty dictionary"
- " IOA2UCDevice::CopyLevelControlInfoByIndex_RangeMap: there is no range map"
- " IOA2UCDevice::CopySelectorControlInfoByIndex_SelectorMap: there is no selector map"
- " IOA2UCDevice::CopySelectorControlInfo_MultiSelectorValue: there is no selector value"
- " IOA2UCDevice::CopyStreamInfoByID_AvailableFormats: there are no available formats"
- " IOA2UCDevice::CopyStreamInfoByIndex_AvailableFormats: there are no available formats"
- " IOA2UCDevice::GetBlockControlInfoByID_Descriptor: there is no descriptor"
- " IOA2UCDevice::GetControlInfoByIndex_BaseClass: there is no control base class"
- " IOA2UCDevice::GetControlInfoByIndex_Class: there is no control class"
- " IOA2UCDevice::GetControlInfoByIndex_Class: there is no control scope"
- " IOA2UCDevice::GetControlInfoByIndex_Element: there is no control scope"
- " IOA2UCDevice::GetControlInfoByIndex_Value: there is no control value"
- " IOA2UCDevice::GetSliderControlInfoByIndex_MaximumValue: there is no maximum control value"
- " IOA2UCDevice::GetSliderControlInfoByIndex_MinimumValue: there is no minimum control value"
- " IOA2UCDevice::GetStereoPanControlInfoByIndex_CenterValue: there is no center value"
- " IOA2UCDevice::GetStereoPanControlInfoByIndex_LeftChannel: there is no left channel"
- " IOA2UCDevice::GetStereoPanControlInfoByIndex_LeftChannel: there is no right channel"
- " IOA2UCDevice::GetStereoPanControlInfoByIndex_LeftValue: there is no left value"
- " IOA2UCDevice::GetStereoPanControlInfoByIndex_RightValue: there is no right value"
- " IOA2UCDevice::GetStreamInfoByID_CurrentFormat: the current format is not formatted correctly"
- " IOA2UCDevice::GetStreamInfoByID_CurrentFormat: there is no current format"
- " IOA2UCDevice::GetStreamInfoByID_StartingChannel: there is no starting channel number"
- " IOA2UCDevice::GetStreamInfoByIndex_CurrentFormat: the current format is not formatted correctly"
- " IOA2UCDevice::GetStreamInfoByIndex_CurrentFormat: there is no current format"
- " IOA2UCDevice::GetStreamInfoByIndex_ID: there is no stream ID"
- " IOA2UCDevice::GetStreamInfoByIndex_StartingChannel: there is no starting channel number"
- " IOA2UCDevice::IOA2UCDevice: this is not an IOAudio2Device"
- " IOA2UCDevice::MapBlockControlBuffer: no control for the given ID"
- " IOA2UCDevice::MapDataExchangeBlockBuffer: no data exchange block for the given ID"
- " IOA2UCDevice::MapEngineStatus: Mapped engine status is not large enough."
- " IOA2UCDevice::MapIOBufferForStream: no stream for the given ID"
- " IOA2UCDevice::MoveBlockControlData: got an error when telling the hardware to move the block control data, Error: 0x%X"
- " IOA2UCDevice::MoveDataExchangeBlockData: got an error when telling the hardware to move the block control data, Error: 0x%X"
- " IOA2UCDevice::PerformConfigChange: got an error from the call down to the driver, Error: 0x%X"
- " IOA2UCDevice::SetClientDescription: got an error when telling the hardware to change client description, Error: 0x%X"
- " IOA2UCDevice::SetControlValue: got an error when telling the hardware to change a control value, Error: 0x%X"
- " IOA2UCDevice::SetNominalSampleRate: got an error when telling the hardware to change a control value, Error: 0x%X"
- " IOA2UCDevice::SetStreamActive: got an error when telling the hardware to turn a stream on or off, Error: 0x%X"
- " IOA2UCDevice::SetStreamCurrentFormat: got an error when telling the hardware to set the stream format, Error: 0x%X"
- " IOA2UCDevice::StartIO: got an error when telling the hardware to start, Error: 0x%X"
- " IOA2UCDevice::StartIOWithFlags: got an error when telling the hardware to start, Error: 0x%X"
- " IOA2UCDevice::StopIO: got an error when telling the hardware to stop, Error: 0x%X"
- " IOA2UCDevice::StopIOWithFlags: got an error when telling the hardware to stop, Error: 0x%X"
- " IOA2UCDevice::operator=: this is not an IOAudio2Device"
- " Major problem: Unlocker attempted to unlock a mutex not owned by the current thread!"
- " UCObject::CacheProperties: failed to get the properties from the IO Registry, Error: 0x%X"
- " UCObject::CopyMatchingObjectWithPropertyValue: IOMainPort failed, Error: 0x%X"
- " UCObject::CopyProperties: failed to get the properties from the IO Registry, Error: 0x%X"
- " UCObject::MapMemory: failed to map in the memory, Error: 0x%X"
- " UCObject::MapMemory: mapped in a NULL pointer"
- " UCObject::OpenConnection: failed to open a connection, Error: 0x%X"
- " UCObject::SetConnectionNotificationPort: Cannot set the connection's's notification port., Error: 0x%X"
- " UCObject::SetProperty: got an error from the IORegistry, Error: 0x%X"
- "%@ PerformStartIO"
- "%@ PerformStartIO faked, result %d"
- "%@ PerformStartIO returned, result %d"
- "%@ PerformStopIO"
- "%@ PerformStopIO returned. result %d"
- "%@ PerformUnderlyingStopIO returned, result %d"
- "%@: Failed to create stream."
- "%@: Using deprecated method to create streams."
- "%@: Waited to long to StartIO while change request is in progress."
- "%s.%@.%@"
- "%s.%@.%@.concurrent"
- "*"
- "*16@0:8"
- "-[ASDTIOA2LegacyDevice blockIORequests]"
- "-[ASDTIOA2LegacyDevice ioa2Device]"
- "-[ASDTIOA2LegacyDevice releaseIORequests]"
- "-[ASDTIOA2LegacyDevice startIORequest]"
- "-[ASDTIOA2LegacyDevice stopIORequest]"
- "1"
- "@\"ASDTIOA2LegacyDevice\""
- "@\"NSString\"8@?0"
- "@24@0:8I16I20"
- "@44@0:8{vector<unsigned int, std::allocator<unsigned int>>=^I^I{__compressed_pair<unsigned int *, std::allocator<unsigned int>>=^I}}16I40"
- "A"
- "ASDTIOA2LegacyBooleanControl"
- "ASDTIOA2LegacyControl"
- "ASDTIOA2LegacyDevice"
- "ASDTIOA2LegacyDevice.mm"
- "ASDTIOA2LegacyHeadsetInfoProperty"
- "ASDTIOA2LegacyJackControl"
- "ASDTIOA2LegacyLevelControl"
- "ASDTIOA2LegacyMuteControl"
- "ASDTIOA2LegacyOffsetStream"
- "ASDTIOA2LegacyPhantomPowerControl"
- "ASDTIOA2LegacyPhaseInvertControl"
- "ASDTIOA2LegacySelectorControl"
- "ASDTIOA2LegacyStream"
- "B24@0:8^v16"
- "B36@0:8^*16^I24I32"
- "Buffer mapped with size %d"
- "Buffer released"
- "CADispatchQueue::PortDeathListMutex"
- "CADispatchQueue::PortReceiverListMutex"
- "CAException"
- "Caught CAException %d %4.4s"
- "Caught OSStatus exception %d %4.4s"
- "Error creating streams"
- "Error performing config change: %d"
- "I20@0:8I16"
- "I8@?0"
- "IOA2Device %@ IO state = %s"
- "IOService"
- "SetSampleRateSynchronously failed. DesiredSampleRate: "
- "SetSampleRateSynchronously timed out"
- "Signaled sample rate waiting thread"
- "T*,N,V_blockMap"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_concurrentQueue"
- "TB,N,V_marked"
- "TI,N,V_blockSize"
- "TI,R,N,V_userClientID"
- "Unknown exception caught!"
- "Waiting to be signaled from IOA2 config change notification thread..."
- "Woke! currentRate = %f, desiredRate = %f"
- "^{IOA2UCDevice=^^?II{CACFDictionary=^{__CFDictionary}BB}BBBB}16@0:8"
- "^{IOAudio2EngineStatus=QQQQQ}"
- "^{IOAudio2EngineStatus=QQQQQ}16@0:8"
- "_addInputStreams:"
- "_addOutputStreams:"
- "_availableFormatsForStream:"
- "_blockSize"
- "_buildFormatList"
- "_closeConnection"
- "_concurrentQueue"
- "_currentFormatForStream:"
- "_deviceLock"
- "_getIOA2EngineStatus"
- "_getStartingChannel"
- "_getStreamListUCIDLists"
- "_ioBuffer"
- "_machDispatchQueue"
- "_mapIOBuffer:ofSize:forStream:"
- "_mapIOBuffers"
- "_markOrCreateControlsWithDictionaries:"
- "_markOrCreateStreamsWithIDs:direction:"
- "_marked"
- "_pushActiveState"
- "_pushStreamActiveStates"
- "_releaseIOBuffer:"
- "_releaseIOBuffer:forStream:"
- "_releaseIOBuffers"
- "_removeInputStreams:"
- "_removeOutputStreams:"
- "_streamStartingChannel:"
- "_synchronizeStreamsOrReturnForRemoval:"
- "_synchronizeWithHardware"
- "_ucDeviceNotificationPort"
- "_updateControls:"
- "addObjectsFromArray:"
- "arrayByAddingObjectsFromArray:"
- "blockIORequests"
- "blockMap"
- "blockSize"
- "com.apple.audio.CADispatchQueue.SerialQueue"
- "com.apple.audio.macaudio.IOA2.event"
- "concurrentQueue"
- "createStreamForUserClientID:direction:"
- "currentHandler"
- "d8@?0"
- "deviceName"
- "doStartIO"
- "doStopIO"
- "exclavesSensorManager"
- "handleFailureInMethod:object:file:lineNumber:description:"
- "indexOfObject:"
- "initWithCapacity:"
- "ioBuffer"
- "isRunning"
- "manufacturerName"
- "modelUID"
- "performStartIO"
- "performStopIO"
- "releaseIORequests"
- "scopedLock"
- "setBlockMap:"
- "setBlockSize:"
- "setConcurrentQueue:"
- "startIORequest"
- "statusTracker"
- "std::exception caught: %s."
- "stopIORequest"
- "synchronizeWithRegistry"
- "v24@0:8*16"
- "v24@0:8B16I20"
- "v28@0:8*16I24"
- "v36@0:8^*16^I24I32"
- "v60@0:8{AudioStreamBasicDescription=dIIIIIIII}16I56"
- "{AudioStreamBasicDescription=dIIIIIIII}20@0:8I16"
- "{CAVolumeCurve=\"mTag\"I\"mCurveMap\"{map<CARawPoint, CADBPoint, std::less<CARawPoint>, std::allocator<std::pair<const CARawPoint, CADBPoint>>>=\"__tree_\"{__tree<std::__value_type<CARawPoint, CADBPoint>, std::__map_value_compare<CARawPoint, std::__value_type<CARawPoint, CADBPoint>, std::less<CARawPoint>>, std::allocator<std::__value_type<CARawPoint, CADBPoint>>>=\"__begin_node_\"^v\"__pair1_\"{__compressed_pair<std::__tree_end_node<std::__tree_node_base<void *> *>, std::allocator<std::__tree_node<std::__value_type<CARawPoint, CADBPoint>, void *>>>=\"__value_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}}\"__pair3_\"{__compressed_pair<unsigned long, std::__map_value_compare<CARawPoint, std::__value_type<CARawPoint, CADBPoint>, std::less<CARawPoint>>>=\"__value_\"Q}}}\"mIsApplyingTransferFunction\"B\"mTransferFunction\"I\"mRawToScalarExponentNumerator\"f\"mRawToScalarExponentDenominator\"f}"
- "{CAVolumeCurve=I{map<CARawPoint, CADBPoint, std::less<CARawPoint>, std::allocator<std::pair<const CARawPoint, CADBPoint>>>={__tree<std::__value_type<CARawPoint, CADBPoint>, std::__map_value_compare<CARawPoint, std::__value_type<CARawPoint, CADBPoint>, std::less<CARawPoint>>, std::allocator<std::__value_type<CARawPoint, CADBPoint>>>=^v{__compressed_pair<std::__tree_end_node<std::__tree_node_base<void *> *>, std::allocator<std::__tree_node<std::__value_type<CARawPoint, CADBPoint>, void *>>>={__tree_end_node<std::__tree_node_base<void *> *>=^v}}{__compressed_pair<unsigned long, std::__map_value_compare<CARawPoint, std::__value_type<CARawPoint, CADBPoint>, std::less<CARawPoint>>>=Q}}}BIff}24@0:8@16"
- "{array<std::vector<unsigned int>, 2UL>=[2{vector<unsigned int, std::allocator<unsigned int>>=^I^I{__compressed_pair<unsigned int *, std::allocator<unsigned int>>=^I}}]}16@0:8"
- "{unique_lock<std::recursive_mutex>=^{recursive_mutex}B}16@0:8"
- "{unique_ptr<ASDT::IOA2UCDevice, std::default_delete<ASDT::IOA2UCDevice>>=\"__ptr_\"{__compressed_pair<ASDT::IOA2UCDevice *, std::default_delete<ASDT::IOA2UCDevice>>=\"__value_\"^{IOA2UCDevice}}}"
- "{unique_ptr<ASDT::MachPort, std::default_delete<ASDT::MachPort>>=\"__ptr_\"{__compressed_pair<ASDT::MachPort *, std::default_delete<ASDT::MachPort>>=\"__value_\"^{MachPort}}}"
- "{unique_ptr<CADeprecated::CADispatchQueue, std::default_delete<CADeprecated::CADispatchQueue>>=\"__ptr_\"{__compressed_pair<CADeprecated::CADispatchQueue *, std::default_delete<CADeprecated::CADispatchQueue>>=\"__value_\"^{CADispatchQueue}}}"
- "\xf0\xf0\xf0B"
- "\xf0\xf0\xf0\x92\x13\x13"

```
