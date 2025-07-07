## appleh16camerad

> `/usr/sbin/appleh16camerad`

```diff

-4.15.3.0.0
-  __TEXT.__text: 0x827a8
-  __TEXT.__auth_stubs: 0x1f00
+4.18.5.0.0
+  __TEXT.__text: 0x82f98
+  __TEXT.__auth_stubs: 0x1fc0
   __TEXT.__objc_stubs: 0x1440
   __TEXT.__init_offsets: 0x14
   __TEXT.__objc_methlist: 0x268
-  __TEXT.__gcc_except_tab: 0x22c4
+  __TEXT.__gcc_except_tab: 0x2308
   __TEXT.__const: 0x2d90
-  __TEXT.__cstring: 0x89ff
+  __TEXT.__cstring: 0x8a3a
   __TEXT.__objc_classname: 0x89
-  __TEXT.__oslogstring: 0x5a50
+  __TEXT.__oslogstring: 0x5a52
   __TEXT.__objc_methname: 0x1577
   __TEXT.__objc_methtype: 0x10b3
-  __TEXT.__unwind_info: 0x1508
+  __TEXT.__unwind_info: 0x15b8
   __TEXT.__eh_frame: 0xa0
-  __DATA_CONST.__auth_got: 0xf90
-  __DATA_CONST.__got: 0xb78
+  __DATA_CONST.__auth_got: 0xff0
+  __DATA_CONST.__got: 0xba8
   __DATA_CONST.__auth_ptr: 0x60
-  __DATA_CONST.__const: 0xae58
+  __DATA_CONST.__const: 0xaea8
   __DATA_CONST.__cfstring: 0x3280
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x18

   __DATA.__objc_selrefs: 0x628
   __DATA.__objc_ivar: 0x34
   __DATA.__objc_data: 0xf0
-  __DATA.__data: 0x35cd88
+  __DATA.__data: 0x35fd80
   __DATA.__bss: 0x201
   __DATA.__common: 0x5c
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
   - /usr/lib/libz.1.dylib
-  UUID: D60D6225-5BD5-3C1A-B96E-9A77E9C9682F
-  Functions: 1635
-  Symbols:   887
-  CStrings:  2427
+  UUID: 9C6571E5-7961-3B42-8E5B-9FC46BDD1DD5
+  Functions: 1650
+  Symbols:   905
+  CStrings:  2428
 
Symbols:
+ __Block_copy
+ __Block_release
+ __ZNSt3__115__thread_structC1Ev
+ __ZNSt3__115__thread_structD1Ev
+ __ZNSt3__119__thread_local_dataEv
+ __ZNSt3__120__throw_system_errorEiPKc
+ __ZNSt3__16thread4joinEv
+ __ZNSt3__16threadD1Ev
+ _dispatch_get_context
+ _dispatch_group_notify
+ _dispatch_set_context
+ _dispatch_set_finalizer_f
+ _kFigCaptureStreamMetadata_DistortionCenterInBuffer
+ _kFigCaptureStreamMetadata_IntermediateTapDistortionCenterInBuffer
+ _kFigCaptureStreamMetadata_IntermediateTapTotalScalingFromPhysicalSensor
+ _kFigCaptureStreamMetadata_SecondaryScalerDistortionCenterInBuffer
+ _kFigCaptureStreamMetadata_SecondaryScalerTotalScalingFromPhysicalSensor
+ _kFigCaptureStreamMetadata_TotalScalingFromPhysicalSensor
+ _pthread_setspecific
- _dispatch_time
CStrings:
+ "%s - Couldn't understand which projector is on this device.\n"
+ "%s - GMC: failed to determine projector type\n"
+ "%s - device impact manager is unavailable, unable to query device impacts\n"
+ "%s - invalid instance of device impact manager\n"
+ "%s - queries must provide a valid dispatch group and impact context\n"
+ "4.18.5"
+ "QueryDeviceImpactsInternal"
+ "RPCRunGMC"
+ "SendDeviceImpacts_block_invoke"
+ "thread constructor failed"
+ "v20@?0^{sCIspCmdDeviceImpactEvent=BfiQ}8C16"
- "%s - Device impact manager does not support querying for device impacts\n"
- "%s - Device impact manager is NULL\n"
- "%s - Device impact manager is unavailable, unable to query device impacts\n"
- "%s - Timeout: failed to query device impacts, releasing impact manager\n"
- "4.15.3"
- "GetDeviceImpacts"
- "GetDeviceImpacts_block_invoke"
- "Timeout: failed to query device impacts\n"
- "test"
- "~H16ISPDeviceImpactManager"

```
