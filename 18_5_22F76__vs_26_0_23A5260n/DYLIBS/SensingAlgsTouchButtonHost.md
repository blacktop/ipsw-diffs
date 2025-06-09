## SensingAlgsTouchButtonHost

> `/System/Library/PrivateFrameworks/SensingAlgsTouchButtonHost.framework/SensingAlgsTouchButtonHost`

```diff

-45.8.0.0.0
-  __TEXT.__text: 0xcd54
+69.0.0.0.0
+  __TEXT.__text: 0xda04
   __TEXT.__auth_stubs: 0x3f0
-  __TEXT.__objc_methlist: 0x668
-  __TEXT.__gcc_except_tab: 0xa0c
-  __TEXT.__const: 0x622
-  __TEXT.__oslogstring: 0xaf6
-  __TEXT.__cstring: 0x397
-  __TEXT.__unwind_info: 0x4f8
+  __TEXT.__objc_methlist: 0x6a8
+  __TEXT.__gcc_except_tab: 0xa58
+  __TEXT.__const: 0x6b5
+  __TEXT.__oslogstring: 0xb81
+  __TEXT.__cstring: 0x398
+  __TEXT.__unwind_info: 0x528
   __TEXT.__objc_classname: 0x7f
-  __TEXT.__objc_methname: 0x121d
-  __TEXT.__objc_methtype: 0x8a1
-  __TEXT.__objc_stubs: 0x780
+  __TEXT.__objc_methname: 0x135b
+  __TEXT.__objc_methtype: 0x8ed
+  __TEXT.__objc_stubs: 0x820
   __DATA_CONST.__got: 0x70
   __DATA_CONST.__const: 0xc0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x490
+  __DATA_CONST.__objc_selrefs: 0x4b8
   __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__objc_arraydata: 0x28
   __AUTH_CONST.__auth_got: 0x208
-  __AUTH_CONST.__const: 0xa10
+  __AUTH_CONST.__const: 0xb28
   __AUTH_CONST.__cfstring: 0x460
-  __AUTH_CONST.__objc_const: 0x970
+  __AUTH_CONST.__objc_const: 0x9d0
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_intobj: 0xf0
   __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0x6c
+  __DATA.__objc_ivar: 0x74
   __DATA.__data: 0x130
-  __DATA.__bss: 0x50
+  __DATA.__bss: 0x48
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1A93851D-0642-3AAF-B698-8D86AE23CE8D
-  Functions: 424
-  Symbols:   1264
-  CStrings:  434
+  UUID: BF1A1FBF-74A9-3629-B7C4-D10525F9837A
+  Functions: 446
+  Symbols:   1327
+  CStrings:  449
 
Symbols:
+ -[SASInterfaceTouchButtonHost doubleHalfPressEventsDescriptor]
+ -[SASInterfaceTouchButtonHost doubleHalfPressResults]
+ -[SASInterfaceTouchButtonHost processDoubleHalfPressResults:results:]
+ -[SASInterfaceTouchButtonHost setDoubleHalfPressEventsDescriptor:]
+ -[SASInterfaceTouchButtonHost setDoubleHalfPressResults:]
+ GCC_except_table145
+ GCC_except_table154
+ GCC_except_table71
+ GCC_except_table85
+ GCC_except_table93
+ GCC_except_table94
+ GCC_except_table95
+ GCC_except_table96
+ GCC_except_table98
+ GCC_except_table99
+ _OBJC_IVAR_$_SASInterfaceTouchButtonHost._doubleHalfPressEventsDescriptor
+ _OBJC_IVAR_$_SASInterfaceTouchButtonHost._doubleHalfPressResults
+ _OUTLINED_FUNCTION_35
+ __ZN14SABinaryWriter13addInjExtDataEbyybtjPKv
+ __ZN14SABinaryWriter17addExtractionDataEyybtjPKv
+ __ZN14SABinaryWriter9writeDataEtjPKv
+ __ZN14SADynamicArrayIjLt32EE12injectBufferEPKhm
+ __ZN14SADynamicArrayIjLt32EED0Ev
+ __ZN14SADynamicArrayIjLt32EED1Ev
+ __ZN16PacketCollectionC1Em9MemType_t
+ __ZN6SAListIjE5clearEv
+ __ZN6SAListIjE9push_backERKj
+ __ZN6SAListIjED2Ev
+ __ZN8NovaHost18DiscreteCalculator6updateER31TouchSensitiveButtonEventPacketR21ForceStageEventPacketb
+ __ZN8NovaHost19DoubleHalfPressStep10updateStepEP31TouchSensitiveButtonEventPacketP21ForceStageEventPacketPb
+ __ZN8NovaHost19DoubleHalfPressStep3runEv
+ __ZN8NovaHost19DoubleHalfPressStepC2EyR14SADynamicArrayI31TouchSensitiveButtonEventPacketLt32EERS1_I21ForceStageEventPacketLt32EERS1_IjLt32EE
+ __ZN8NovaHost19DoubleHalfPressStepD0Ev
+ __ZN8NovaHost19DoubleHalfPressStepD1Ev
+ __ZN8NovaHost19LiftoffVelocityStepC2EyR14SADynamicArrayI31TouchSensitiveButtonEventPacketLt32EERS1_I21ForceStageEventPacketLt32EER13PlainDataNodeIbE
+ __ZN8NovaHost22NovaButtonStateMachineD2Ev
+ __ZN8NovaHost25DoubleHalfPressRecognizer5resetEv
+ __ZN8NovaHost25DoubleHalfPressRecognizer6updateEP31TouchSensitiveButtonEventPacketP21ForceStageEventPacketPb
+ __ZN8NovaHost26NovaButtonStateMachineStepD2Ev
+ __ZNK14SADynamicArrayIjLt32EE12sendCallbackEPFvRK22AlgDataCallbackContentERS1_
+ __ZNK14SADynamicArrayIjLt32EE8contentsEv
+ __ZNK14SADynamicArrayIjLt32EE8numElemsEv
+ __ZTI13PlainDataNodeI20SADynamicArrayPacketIjLt32EEE
+ __ZTI13SA1DArrayBaseIjE
+ __ZTI14SADynamicArrayIjLt32EE
+ __ZTIN8NovaHost19DoubleHalfPressStepE
+ __ZTS13PlainDataNodeI20SADynamicArrayPacketIjLt32EEE
+ __ZTS13SA1DArrayBaseIjE
+ __ZTS14SADynamicArrayIjLt32EE
+ __ZTSN8NovaHost19DoubleHalfPressStepE
+ __ZTV14SADynamicArrayIjLt32EE
+ __ZTVN8NovaHost19DoubleHalfPressStepE
+ __ZThn168_NK14SADynamicArrayIjLt32EE8contentsEv
+ __ZThn168_NK14SADynamicArrayIjLt32EE8numElemsEv
+ __ZZ49-[SASInterfaceTouchButtonHost configureCallbacks]EN3$_48__invokeERK22AlgDataCallbackContent
+ _objc_msgSend$doubleHalfPressEventsDescriptor
+ _objc_msgSend$doubleHalfPressResults
+ _objc_msgSend$processDoubleHalfPressResults:results:
+ _objc_msgSend$setDoubleHalfPressEventsDescriptor:
+ _objc_msgSend$setDoubleHalfPressResults:
- GCC_except_table144
- GCC_except_table153
- GCC_except_table62
- GCC_except_table76
- GCC_except_table84
- GCC_except_table87
- GCC_except_table89
- GCC_except_table90
- _OUTLINED_FUNCTION_31
- _OUTLINED_FUNCTION_41
- _OUTLINED_FUNCTION_42
- __ZN14SABinaryWriter13addInjExtDataEbyybttPKv
- __ZN14SABinaryWriter17addExtractionDataEyybttPKv
- __ZN14SABinaryWriter9writeDataEttPKv
- __ZN6SAListIhE5clearEv
- __ZN6SAListIhE9push_backERKh
- __ZN6SAListIhED2Ev
- __ZN8NovaHost19LiftoffVelocityStepC2EyR14SADynamicArrayI31TouchSensitiveButtonEventPacketLt32EERS1_I21ForceStageEventPacketLt32EE
- __ZN8NovaHost22NovaButtonStateMachineD1Ev
CStrings:
+ "'!c"
+ "17.0.0 (clang-1700.3.9.904) [+internal-os]"
+ "23A5259s"
+ "SensingAlgsNovaHost-69~44"
+ "Tr^B,N,V_doubleHalfPressResults"
+ "Tr^{_SADynamicArrayDescriptor=SSSS},N,V_doubleHalfPressEventsDescriptor"
+ "[SASInterfaceTouchButtonHost] double half press = NO for %d-th event"
+ "[SASInterfaceTouchButtonHost] double half press = YES for %d-th event"
+ "_doubleHalfPressEventsDescriptor"
+ "_doubleHalfPressResults"
+ "doubleHalfPressEventsDescriptor"
+ "doubleHalfPressResults"
+ "processDoubleHalfPressResults:results:"
+ "r^B"
+ "r^B16@0:8"
+ "setDoubleHalfPressEventsDescriptor:"
+ "setDoubleHalfPressResults:"
+ "v24@0:8r^B16"
+ "v32@0:8r^{_SADynamicArrayDescriptor=SSSS}16r^B24"
- "'!C"
- "17.0.0 (clang-1700.0.13.5) [+internal-os]"
- "22F63"
- "SensingAlgsNovaHost-45.8~270"

```
