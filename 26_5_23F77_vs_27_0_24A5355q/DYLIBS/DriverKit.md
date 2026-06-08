## DriverKit

> `/System/Library/Frameworks/DriverKit.framework/DriverKit`

```diff

-456.120.3.0.0
-  __TEXT.__text: 0x3610c
-  __TEXT.__auth_stubs: 0xbd0
+508.0.0.0.0
+  __TEXT.__text: 0x37c40
   __TEXT.__init_offsets: 0x8
-  __TEXT.__const: 0x5f3c
-  __TEXT.__cstring: 0x2e7d
+  __TEXT.__const: 0x5f7c
+  __TEXT.__cstring: 0x2f92
   __TEXT.__oslogstring: 0xe
-  __TEXT.__unwind_info: 0x190
-  __DATA_CONST.__got: 0x48
-  __DATA_CONST.__const: 0x4b0
+  __TEXT.__unwind_info: 0x1860
+  __TEXT.__auth_stubs: 0x0
+  __DATA_CONST.__const: 0x4f0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__structlayouts: 0x10
   __DATA_CONST.__osclassinfo: 0x158
-  __AUTH_CONST.__auth_got: 0x5e8
-  __AUTH_CONST.__const: 0x56f8
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__const: 0x5758
+  __AUTH_CONST.__weak_auth_got: 0x10
+  __AUTH_CONST.__auth_got: 0x5e0
   __DATA.__crash_info: 0x148
   __DATA.__common: 0x170
   __DATA.__bss: 0x448

   __DATA_DIRTY.__bss: 0x1008
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 3CF88333-A1B8-3D48-8C25-3585F49BADC9
-  Functions: 1555
-  Symbols:   2980
-  CStrings:  470
+  UUID: 4A179564-4E13-3C0E-93C7-2E814AE9ADDB
+  Functions: 1579
+  Symbols:   3024
+  CStrings:  476
 
Symbols:
+ __Z16OSUnserializeXMLPKcPFPK8OSObjectPvP12OSCollectionPK8OSStringS3_ES4_jPPS7_
+ __Z16OSUnserializeXMLPKcmPFPK8OSObjectPvP12OSCollectionPK8OSStringS3_ES4_jPPS7_
+ __Z26OSNumberCreateWithPortNamey
+ __ZL14createWorkLoopPKc
+ __ZL15OSObjectCopyOutP18IOUserServer_IVarsP8OSObjectbPy
+ __ZL15OSObjectCopyOutP18IOUserServer_IVarsP8OSObjectbPy.cold.1
+ __ZL15OSObjectCopyOutP18IOUserServer_IVarsP8OSObjectbPy.cold.2
+ __ZL28_absolutetime_to_nanosecondsyPyb
+ __ZL28_absolutetime_to_nanosecondsyPyb.cold.1
+ __ZL28_absolutetime_to_nanosecondsyPyb.cold.2
+ __ZL28_nanoseconds_to_absolutetimeyPyb
+ __ZL28_nanoseconds_to_absolutetimeyPyb.cold.1
+ __ZL28_nanoseconds_to_absolutetimeyPyb.cold.2
+ __ZL30TimerDispatchSourceWasCanceledP27IOTimerDispatchSource_IVars
+ __ZL47OSCreateSerializationFromBytesWithCopyInHandlerPKvmU13block_pointerFvS0_mEU13block_pointerFiyPP8OSObjectE
+ __ZL47OSCreateSerializationFromBytesWithCopyInHandlerPKvmU13block_pointerFvS0_mEU13block_pointerFiyPP8OSObjectE.cold.1
+ __ZL49OSCreateSerializationFromObjectWithCopyOutHandlerP8OSObjectU13block_pointerFiS0_PyE
+ __ZN15OSSerialization15createFromBytesEPKvmU13block_pointerFvS1_mEU13block_pointerFiyPP8OSObjectE
+ __ZN15OSSerialization16createFromObjectEP8OSObjectU13block_pointerFiS1_PyE
+ __ZN21IOTimerDispatchSource15WakeAtTime_ImplEyyy.cold.1
+ __ZN9IOService20CallPlatformFunctionEP8OSStringbP12OSDictionaryPS3_PFiP15OSMetaClassBase5IORPCE
+ __ZN9IOService25CallPlatformFunction_ImplEP8OSStringbP12OSDictionaryPS3_
+ __ZN9IOService27CallPlatformFunction_InvokeE5IORPCP15OSMetaClassBasePFiS2_P8OSStringbP12OSDictionaryPS6_E
+ ___Block_byref_object_copy_
+ ___Block_byref_object_dispose_
+ ____Z19OSObjectLogInternalP8OSObjectj_block_invoke.40
+ ____ZL15OSCopyInObjectsP18IOUserServer_IVarsP16IORPCMessageMachP12IORPCMessageb_block_invoke_2
+ ____ZL15OSCopyInObjectsP18IOUserServer_IVarsP16IORPCMessageMachP12IORPCMessageb_block_invoke_2.cold.1
+ ____ZL16OSCopyOutObjectsP18IOUserServer_IVarsP16IORPCMessageMachP12IORPCMessageb_block_invoke
+ ____ZL25createTimerDispatchSourceP27IOTimerDispatchSource_IVars18dispatch_clockid_tP16dispatch_queue_s_block_invoke
+ ____ZL25createTimerDispatchSourceP27IOTimerDispatchSource_IVars18dispatch_clockid_tP16dispatch_queue_s_block_invoke.269
+ ____ZL25createTimerDispatchSourceP27IOTimerDispatchSource_IVars18dispatch_clockid_tP16dispatch_queue_s_block_invoke_2
+ ____ZL31IOInterruptDispatchSourceThreadPv_block_invoke.258
+ ____ZL8LockTesti_block_invoke.226
+ ____ZL8LockTesti_block_invoke.230
+ ____ZN21IOTimerDispatchSource15WakeAtTime_ImplEyyy_block_invoke.cold.1
+ ____ZN21IOTimerDispatchSource4freeEv_block_invoke
+ ___block_descriptor_tmp.119
+ ___block_descriptor_tmp.168
+ ___block_descriptor_tmp.173
+ ___block_descriptor_tmp.179
+ ___block_descriptor_tmp.185
+ ___block_descriptor_tmp.188
+ ___block_descriptor_tmp.196
+ ___block_descriptor_tmp.201
+ ___block_descriptor_tmp.203
+ ___block_descriptor_tmp.229
+ ___block_descriptor_tmp.233
+ ___block_descriptor_tmp.253
+ ___block_descriptor_tmp.254
+ ___block_descriptor_tmp.257
+ ___block_descriptor_tmp.261
+ ___block_descriptor_tmp.265
+ ___block_descriptor_tmp.268
+ ___block_descriptor_tmp.270
+ ___block_descriptor_tmp.39
+ ___block_descriptor_tmp.45
+ ___block_descriptor_tmp.54
+ ___block_descriptor_tmp.57
+ ___block_descriptor_tmp.60
+ ___block_descriptor_tmp.63
+ ___block_descriptor_tmp.66
+ ___block_descriptor_tmp.69
+ ___block_descriptor_tmp.72
+ ___block_descriptor_tmp.75
+ _absolutetime_to_nanoseconds_roundup
+ _dispatch_time_from_nsec
+ _io_service_get_wait_info
+ _nanoseconds_to_absolutetime_roundup
- _OSCollectionTypeID.cold.1
- _OSCreateSerializationFromBytes.cold.1
- __ZL16OSCopyOutObjectsP18IOUserServer_IVarsP16IORPCMessageMachP12IORPCMessageb.cold.6
- __ZL16OSCopyOutObjectsP18IOUserServer_IVarsP16IORPCMessageMachP12IORPCMessageb.cold.7
- __ZN21IOTimerDispatchSource11Create_ImplEP15IODispatchQueuePPS_.cold.2
- ____Z19OSObjectLogInternalP8OSObjectj_block_invoke.42
- ____ZL15OSCopyInObjectsP18IOUserServer_IVarsP16IORPCMessageMachP12IORPCMessageb_block_invoke.cold.1
- ____ZL31IOInterruptDispatchSourceThreadPv_block_invoke.253
- ____ZL8LockTesti_block_invoke.221
- ____ZL8LockTesti_block_invoke.225
- ____ZN21IOTimerDispatchSource11Create_ImplEP15IODispatchQueuePPS__block_invoke
- ____ZN21IOTimerDispatchSource11Create_ImplEP15IODispatchQueuePPS__block_invoke_2
- ___block_descriptor_tmp.120
- ___block_descriptor_tmp.124
- ___block_descriptor_tmp.166
- ___block_descriptor_tmp.170
- ___block_descriptor_tmp.177
- ___block_descriptor_tmp.181
- ___block_descriptor_tmp.187
- ___block_descriptor_tmp.190
- ___block_descriptor_tmp.198
- ___block_descriptor_tmp.219
- ___block_descriptor_tmp.228
- ___block_descriptor_tmp.248
- ___block_descriptor_tmp.249
- ___block_descriptor_tmp.252
- ___block_descriptor_tmp.256
- ___block_descriptor_tmp.41
- ___block_descriptor_tmp.47
- ___block_descriptor_tmp.56
- ___block_descriptor_tmp.59
- ___block_descriptor_tmp.62
- ___block_descriptor_tmp.65
- ___block_descriptor_tmp.68
- _absolutetime_to_nanoseconds.cold.1
- _absolutetime_to_nanoseconds.cold.2
- _nanoseconds_to_absolutetime.cold.1
- _nanoseconds_to_absolutetime.cold.2
CStrings:
+ "IOTimerDispatchSource: *** DRIVERKIT CLIENT BUG ***: double timer cancellation"
+ "OSCopyInObjects_block_invoke_2"
+ "OSCreateSerializationFromBytesWithCopyInHandler"
+ "WakeAtTime_Impl"
+ "_absolutetime_to_nanoseconds"
+ "_nanoseconds_to_absolutetime"
+ "createTimerDispatchSource"
+ "dsource"
+ "failed to copy in object: 0x%x"
+ "i24@?0Q8^^{OSObject}16"
+ "i24@?0^{OSObject=^^?Aii^{OSMetaClass}^^?(?=^{OSObject_IVars}^{OSObject_LocalIVars})}8^Q16"
+ "kr == kIOReturnSuccess"
- "OSCollectionTypeID"
- "OSCopyInObjects_block_invoke"
- "OSCreateSerializationFromBytes"
- "absolutetime_to_nanoseconds"
- "inst->ivars->dsource"
- "nanoseconds_to_absolutetime"

```
