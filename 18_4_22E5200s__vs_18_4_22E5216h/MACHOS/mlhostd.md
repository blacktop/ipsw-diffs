## mlhostd

> `/usr/libexec/mlhostd`

```diff

-3.5.24.0.0
-  __TEXT.__text: 0x48d4c
-  __TEXT.__auth_stubs: 0x1e30
+3.5.31.0.0
+  __TEXT.__text: 0x52f30
+  __TEXT.__auth_stubs: 0x1f10
   __TEXT.__objc_methlist: 0x290
-  __TEXT.__const: 0xc6c
+  __TEXT.__const: 0xc7c
   __TEXT.__cstring: 0x966b
   __TEXT.__swift5_entry: 0x8
   __TEXT.__constg_swiftt: 0x30c
-  __TEXT.__swift5_typeref: 0x83b
+  __TEXT.__swift5_typeref: 0x84b
   __TEXT.__swift5_builtin: 0x64
   __TEXT.__swift5_reflstr: 0x302
   __TEXT.__swift5_fieldmd: 0x2d0

   __TEXT.__objc_methname: 0xcce
   __TEXT.__objc_classname: 0x60
   __TEXT.__objc_methtype: 0x394
-  __TEXT.__oslogstring: 0x26fa
-  __TEXT.__swift5_capture: 0x23c
-  __TEXT.__swift_as_entry: 0x40
-  __TEXT.__swift_as_ret: 0x28
-  __TEXT.__unwind_info: 0x878
-  __TEXT.__eh_frame: 0x13a8
-  __DATA_CONST.__auth_got: 0xf18
+  __TEXT.__oslogstring: 0x27da
+  __TEXT.__swift5_capture: 0x240
+  __TEXT.__swift_as_entry: 0x44
+  __TEXT.__swift_as_ret: 0x2c
+  __TEXT.__unwind_info: 0x888
+  __TEXT.__eh_frame: 0x1498
+  __DATA_CONST.__auth_got: 0xf88
   __DATA_CONST.__got: 0x5f8
-  __DATA_CONST.__auth_ptr: 0x468
+  __DATA_CONST.__auth_ptr: 0x460
   __DATA_CONST.__const: 0x5288
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x58

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 638
-  Symbols:   795
-  CStrings:  1594
+  Functions: 642
+  Symbols:   811
+  CStrings:  1597
 
Symbols:
+ _$s20LighthouseBackground11KVDatastoreC17reduceMemoryUsageyyFTj
+ _$s20LighthouseBackground11TaskRequestV012nonRepeatingC0AA03NonfcD0VSgvg
+ _$s20LighthouseBackground11TaskRequestV09repeatingC0AA09RepeatingcD0VSgvg
+ _$s20LighthouseBackground11TaskRequestV09repeatingC0AA09RepeatingcD0VSgvs
+ _$s20LighthouseBackground11TaskRequestV18randomInitialDelaySdSgvg
+ _$s20LighthouseBackground11TaskRequestV18randomInitialDelaySdSgvs
+ _$s20LighthouseBackground20RepeatingTaskRequestV27minDurationBetweenInstancesSdSgvg
+ _$s20LighthouseBackground20RepeatingTaskRequestV27minDurationBetweenInstancesSdSgvs
+ _$s20LighthouseBackground20RepeatingTaskRequestV8intervalSdvg
+ _$s20LighthouseBackground20RepeatingTaskRequestVMa
+ _$s20LighthouseBackground20RepeatingTaskRequestVMn
+ _$s20LighthouseBackground21XPCIncomingConnectionC16bundleIdentifierSSSgvgTj
+ _$s20LighthouseBackground23NonRepeatingTaskRequestV13scheduleAfterSdvg
+ _$s20LighthouseBackground23NonRepeatingTaskRequestVMa
+ _$s20LighthouseBackground23NonRepeatingTaskRequestVMn
+ _$sSo18OS_dispatch_sourceC8DispatchE19MemoryPressureEventVSYACMc
+ _objc_retain_x25
+ _swift_cvw_allocateGenericValueMetadataWithLayoutString
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_initStructMetadataWithLayoutString
+ _swift_cvw_initWithCopy
+ _swift_cvw_initWithTake
+ _swift_cvw_initializeBufferWithCopyOfBuffer
- _$sSo18OS_dispatch_sourceC8DispatchE19MemoryPressureEventVSQACMc
- _swift_allocateGenericValueMetadataWithLayoutString
- _swift_generic_assignWithCopy
- _swift_generic_assignWithTake
- _swift_generic_destroy
- _swift_generic_initWithCopy
- _swift_generic_initWithTake
- _swift_generic_initializeBufferWithCopyOfBuffer
- _swift_initStructMetadataWithLayoutString
CStrings:
+ "Accepting connection from %d with entitlements: %s"
+ "Incoming connection from (pid: %d, bundleId: %s)"
+ "Reducing memory usage in KV store due to pressure."
+ "Updating minDurationBetweenInstances for push task %s to %f"
+ "Updating randomInitialDelay for push task %s to %f"
- "Accepting connection from: %d with entitlements: %s"
- "Incoming connection from: %d"

```
