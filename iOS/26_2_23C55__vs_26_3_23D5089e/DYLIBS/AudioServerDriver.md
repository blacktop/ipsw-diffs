## AudioServerDriver

> `/System/Library/PrivateFrameworks/AudioServerDriver.framework/AudioServerDriver`

```diff

-1110.2.0.0.0
-  __TEXT.__text: 0x62014
-  __TEXT.__auth_stubs: 0xf60
-  __TEXT.__objc_methlist: 0x376c
-  __TEXT.__gcc_except_tab: 0x3310
-  __TEXT.__const: 0x7c4
-  __TEXT.__cstring: 0x38d4
-  __TEXT.__oslogstring: 0x26d5
-  __TEXT.__dof_ASDInterf: 0xe5f
-  __TEXT.__unwind_info: 0x1fd0
+1130.8.0.0.0
+  __TEXT.__text: 0x63200
+  __TEXT.__auth_stubs: 0xf70
+  __TEXT.__objc_methlist: 0x39ec
+  __TEXT.__gcc_except_tab: 0x33e4
+  __TEXT.__const: 0x7dc
+  __TEXT.__cstring: 0x38e9
+  __TEXT.__oslogstring: 0x27fd
+  __TEXT.__dof_ASDInterf: 0xf8b
+  __TEXT.__unwind_info: 0x2008
   __TEXT.__eh_frame: 0x100
   __TEXT.__objc_classname: 0x3da
-  __TEXT.__objc_methname: 0x6351
-  __TEXT.__objc_methtype: 0x1b61
-  __TEXT.__objc_stubs: 0x40c0
+  __TEXT.__objc_methname: 0x67bc
+  __TEXT.__objc_methtype: 0x1b71
+  __TEXT.__objc_stubs: 0x4380
   __DATA_CONST.__got: 0x270
   __DATA_CONST.__const: 0xa38
   __DATA_CONST.__objc_classlist: 0x168
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1708
+  __DATA_CONST.__objc_selrefs: 0x17e0
   __DATA_CONST.__objc_superrefs: 0x140
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__auth_got: 0x7c8
+  __AUTH_CONST.__auth_got: 0x7d0
   __AUTH_CONST.__const: 0x6c0
   __AUTH_CONST.__cfstring: 0x2320
-  __AUTH_CONST.__objc_const: 0x6298
+  __AUTH_CONST.__objc_const: 0x63f8
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0x4d8
+  __DATA.__objc_ivar: 0x4ec
   __DATA.__data: 0x3c8
   __DATA.__bss: 0xe8
   __DATA.__common: 0x8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 431106DE-BBA7-3721-BC1A-65FD29658B1F
-  Functions: 2180
-  Symbols:   6371
-  CStrings:  2454
+  UUID: 6FDBA04A-46FD-3410-B48F-6D14732E222C
+  Functions: 2240
+  Symbols:   6528
+  CStrings:  2498
 
Symbols:
+ -[ASDAudioDevice externalVoiceActivityDetectEnable]
+ -[ASDAudioDevice externalVoiceActivityDetectionState]
+ -[ASDAudioDevice getIsolatedZeroTimeStampBlockUnretainedPtr]
+ -[ASDAudioDevice getIsolatedZeroTimeStampBlock]
+ -[ASDAudioDevice isolatedInputLatency]
+ -[ASDAudioDevice isolatedInputSafetyOffset]
+ -[ASDAudioDevice isolatedOutputLatency]
+ -[ASDAudioDevice isolatedOutputSafetyOffset]
+ -[ASDAudioDevice isolatedSamplingRate]
+ -[ASDAudioDevice isolatedTimestampPeriod]
+ -[ASDAudioDevice setExternalVoiceActivityDetectEnable:]
+ -[ASDAudioDevice setExternalVoiceActivityDetectionState:]
+ -[ASDAudioDevice setGetIsolatedZeroTimeStampBlock:]
+ -[ASDAudioDevice setGetIsolatedZeroTimestampBlock:]
+ -[ASDAudioDevice setGetIsolatedZeroTimestampBlock:].cold.1
+ -[ASDAudioDevice setIsolatedInputLatency:]
+ -[ASDAudioDevice setIsolatedInputSafetyOffset:]
+ -[ASDAudioDevice setIsolatedOutputLatency:]
+ -[ASDAudioDevice setIsolatedOutputSafetyOffset:]
+ -[ASDAudioDevice setIsolatedSamplingRate:]
+ -[ASDAudioDevice setIsolatedTimestampPeriod:]
+ -[ASDAudioDevice setSupportsExternalVoiceActivityDetect:]
+ -[ASDAudioDevice supportsExternalVoiceActivityDetect]
+ -[ASDDSPAudioDevice getIsolatedZeroTimeStampBlock]
+ -[ASDDSPAudioDevice isolatedInputLatency]
+ -[ASDDSPAudioDevice isolatedInputSafetyOffset]
+ -[ASDDSPAudioDevice isolatedOutputLatency]
+ -[ASDDSPAudioDevice isolatedOutputSafetyOffset]
+ -[ASDDSPAudioDevice isolatedSamplingRate]
+ -[ASDDSPAudioDevice isolatedTimestampPeriod]
+ -[ASDDSPAudioDevice setIsolatedInputLatency:]
+ -[ASDDSPAudioDevice setIsolatedInputSafetyOffset:]
+ -[ASDDSPAudioDevice setIsolatedOutputLatency:]
+ -[ASDDSPAudioDevice setIsolatedOutputSafetyOffset:]
+ -[ASDDSPAudioDevice setIsolatedSamplingRate:]
+ -[ASDDSPAudioDevice setIsolatedTimestampPeriod:]
+ -[ASDDSPStream isolatedLatency]
+ -[ASDDSPStream prewarmInputDSPGraph:]
+ -[ASDDSPStream setIsolatedLatency:]
+ -[ASDObject isIsolatedQualifierWithSize:andData:]
+ -[ASDSRCAudioDevice getIsolatedZeroTimeStampBlock]
+ -[ASDSRCAudioDevice isolatedInputLatency]
+ -[ASDSRCAudioDevice isolatedInputSafetyOffset]
+ -[ASDSRCAudioDevice isolatedOutputLatency]
+ -[ASDSRCAudioDevice isolatedOutputSafetyOffset]
+ -[ASDSRCAudioDevice isolatedSamplingRate]
+ -[ASDSRCAudioDevice isolatedTimestampPeriod]
+ -[ASDSRCAudioDevice setIsolatedInputLatency:]
+ -[ASDSRCAudioDevice setIsolatedInputSafetyOffset:]
+ -[ASDSRCAudioDevice setIsolatedOutputLatency:]
+ -[ASDSRCAudioDevice setIsolatedOutputSafetyOffset:]
+ -[ASDSRCAudioDevice setIsolatedSamplingRate:]
+ -[ASDSRCAudioDevice setIsolatedTimestampPeriod:]
+ -[ASDStream isolatedLatency]
+ -[ASDStream setIsolatedLatency:]
+ GCC_except_table100
+ GCC_except_table113
+ GCC_except_table126
+ GCC_except_table130
+ GCC_except_table137
+ GCC_except_table142
+ GCC_except_table144
+ GCC_except_table155
+ GCC_except_table168
+ GCC_except_table170
+ GCC_except_table172
+ GCC_except_table76
+ GCC_except_table86
+ GCC_except_table88
+ GCC_except_table98
+ _OBJC_IVAR_$_ASDAudioDevice._externalVoiceActivityDetectEnable
+ _OBJC_IVAR_$_ASDAudioDevice._externalVoiceActivityDetectionState
+ _OBJC_IVAR_$_ASDAudioDevice._getIsolatedZeroTimeStampBlock
+ _OBJC_IVAR_$_ASDAudioDevice._getIsolatedZeroTimeStampBlockUnretained
+ _OBJC_IVAR_$_ASDAudioDevice._supportsExternalVoiceActivityDetect
+ __Z28ASD_GetIsolatedZeroTimeStampPP40AudioServerPlugInIsolatedDriverInterfacejjPdPyS3_
+ __ZN18ASDDSPStreamHelper20prewarmInputDSPGraphEj
+ __ZN18ASDDSPStreamHelper20prewarmInputDSPGraphEj.cold.1
+ __ZN18ASDDSPStreamHelper20prewarmInputDSPGraphEj.cold.2
+ __ZN18ASDDSPStreamHelper20prewarmInputDSPGraphEj.cold.3
+ __ZN18ASDDSPStreamHelper20prewarmInputDSPGraphEj.cold.4
+ __ZN18ASDDSPStreamHelper20prewarmInputDSPGraphEj.cold.5
+ __ZN18ASDDSPStreamHelper20prewarmInputDSPGraphEj.cold.6
+ __ZN18ASDDSPStreamHelper20prewarmInputDSPGraphEj.cold.7
+ _mach_absolute_time
+ _objc_msgSend$externalVoiceActivityDetectEnable
+ _objc_msgSend$externalVoiceActivityDetectionState
+ _objc_msgSend$firstObject
+ _objc_msgSend$getIsolatedZeroTimeStampBlock
+ _objc_msgSend$getIsolatedZeroTimeStampBlockUnretainedPtr
+ _objc_msgSend$isIsolatedQualifierWithSize:andData:
+ _objc_msgSend$isolatedInputLatency
+ _objc_msgSend$isolatedInputSafetyOffset
+ _objc_msgSend$isolatedLatency
+ _objc_msgSend$isolatedOutputLatency
+ _objc_msgSend$isolatedOutputSafetyOffset
+ _objc_msgSend$isolatedSamplingRate
+ _objc_msgSend$isolatedTimestampPeriod
+ _objc_msgSend$setExternalVoiceActivityDetectEnable:
+ _objc_msgSend$setIsolatedInputLatency:
+ _objc_msgSend$setIsolatedInputSafetyOffset:
+ _objc_msgSend$setIsolatedLatency:
+ _objc_msgSend$setIsolatedOutputLatency:
+ _objc_msgSend$setIsolatedOutputSafetyOffset:
+ _objc_msgSend$setIsolatedSamplingRate:
+ _objc_msgSend$setIsolatedTimestampPeriod:
+ _objc_msgSend$supportsExternalVoiceActivityDetect
- GCC_except_table110
- GCC_except_table123
- GCC_except_table124
- GCC_except_table133
- GCC_except_table134
- GCC_except_table141
- GCC_except_table152
- GCC_except_table165
- GCC_except_table167
- GCC_except_table169
- GCC_except_table51
- GCC_except_table75
CStrings:
+ " prewarmInputDSPGraph: Lock not acquired, skipping prewarming"
+ "/AppleInternal/Library/BuildRoots/4~CDyiugAWowAFGw1SIbSEdhmIa5Ey8lq7RusF6ME/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/System/Library/PrivateFrameworks/AudioToolboxCore.framework/PrivateHeaders/DSPGraph_Box.h"
+ "ASD_GetIsolatedZeroTimeStamp: ASD driver reference\n"
+ "B28@0:8I16r^v20"
+ "Failed to setup Graph output buffer for DSP prewarmInputDSPGraph\n"
+ "T@?,C,N,V_getIsolatedZeroTimeStampBlock"
+ "TB,N,V_externalVoiceActivityDetectEnable"
+ "TB,N,V_externalVoiceActivityDetectionState"
+ "TB,N,V_supportsExternalVoiceActivityDetect"
+ "Td,N"
+ "Unknown exception occurred."
+ "_externalVoiceActivityDetectEnable"
+ "_externalVoiceActivityDetectionState"
+ "_getIsolatedZeroTimeStampBlock"
+ "_getIsolatedZeroTimeStampBlockUnretained"
+ "_supportsExternalVoiceActivityDetect"
+ "externalVoiceActivityDetectEnable"
+ "externalVoiceActivityDetectionState"
+ "firstObject"
+ "getIsolatedZeroTimeStampBlock"
+ "getIsolatedZeroTimeStampBlockUnretainedPtr"
+ "ioBufferFrameSize %d passed to DSP prewarmInputDSPGraph exceeds ringbuffer capacity %d\n"
+ "isIsolatedQualifierWithSize:andData:"
+ "isolatedInputLatency"
+ "isolatedInputSafetyOffset"
+ "isolatedLatency"
+ "isolatedOutputLatency"
+ "isolatedOutputSafetyOffset"
+ "isolatedSamplingRate"
+ "isolatedTimestampPeriod"
+ "prewarmInputDSPGraph"
+ "prewarmInputDSPGraph:"
+ "setExternalVoiceActivityDetectEnable:"
+ "setExternalVoiceActivityDetectionState:"
+ "setGetIsolatedZeroTimeStampBlock:"
+ "setGetIsolatedZeroTimestampBlock:"
+ "setIsolatedInputLatency:"
+ "setIsolatedInputSafetyOffset:"
+ "setIsolatedLatency:"
+ "setIsolatedOutputLatency:"
+ "setIsolatedOutputSafetyOffset:"
+ "setIsolatedSamplingRate:"
+ "setIsolatedTimestampPeriod:"
+ "setSupportsExternalVoiceActivityDetect:"
+ "supportsExternalVoiceActivityDetect"
+ "\xf0\xf0\xf0q"
- "/AppleInternal/Library/BuildRoots/4~CB3iugB6c6BpAolH91fhxu9JYXq_LJHBfrfn3F4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/System/Library/PrivateFrameworks/AudioToolboxCore.framework/PrivateHeaders/DSPGraph_Box.h"
- "\xf0\xf0\xf0Q"

```
