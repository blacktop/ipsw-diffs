## libswift_Concurrency.dylib

> `/usr/lib/swift/libswift_Concurrency.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`
- `__TEXT.__info_plist`

```diff

-6.4.0.31.5
-  __TEXT.__text: 0x7684c
+6.4.2.1.9
+  __TEXT.__text: 0x7687c
   __TEXT.__init_offsets: 0xc
   __TEXT.__const: 0x30aa
   __TEXT.__cstring: 0x23b6

   __AUTH_CONST.__auth_ptr: 0x0
   __AUTH.__data: 0xa70
   __DATA.__data: 0xf0
-  __DATA.__bss: 0x41d0
+  __DATA.__bss: 0x4140
   __DATA.__common: 0x88
-  __DATA_DIRTY.__data: 0x470
-  __DATA_DIRTY.__bss: 0x1b70
+  __DATA_DIRTY.__data: 0x468
+  __DATA_DIRTY.__bss: 0x1c00
   __DATA_DIRTY.__common: 0x69
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/system/libdispatch.dylib
-  Functions: 3079
-  Symbols:   5858
+  Functions: 3078
+  Symbols:   5856
   CStrings:  224
 
Symbols:
- _ZL19dispatchEnqueueFunc
- __ZL29initializeDispatchEnqueueFuncP16dispatch_queue_sPv11qos_class_t
Functions:
~ _swift_dispatchEnqueueGlobal : 180 -> 172
~ _swift_dispatchEnqueueMain : 32 -> 24
~ _swift_task_enqueueOnDispatchQueue : 32 -> 24
- _$ss23AsyncCompactMapSequenceVMa
~ _$ss23AsyncCompactMapSequenceV8IteratorV4next9isolationq_SgScA_pSgYi_tYa7FailureQzYKFTY1_ : 540 -> 544
~ _$ss22AsyncDropFirstSequenceV8IteratorV4next9isolation7ElementQzSgScA_pSgYi_tYa7FailureQzYKFTY0_ : 692 -> 696
~ _$ss22AsyncDropFirstSequenceV8IteratorV4next9isolation7ElementQzSgScA_pSgYi_tYa7FailureQzYKFTY2_ : 996 -> 1004
~ _$ss22AsyncDropWhileSequenceV8IteratorV4next9isolation7ElementQzSgScA_pSgYi_tYa7FailureQzYKFTY0_ : 720 -> 724
~ _$ss22AsyncDropWhileSequenceV8IteratorV4next9isolation7ElementQzSgScA_pSgYi_tYa7FailureQzYKFTY4_ : 956 -> 964
~ _$ss19AsyncFilterSequenceV8IteratorV4next9isolation7ElementQzSgScA_pSgYi_tYa7FailureQzYKFTY1_ : 520 -> 524
~ _$ss19AsyncFilterSequenceV8IteratorV4next9isolation7ElementQzSgScA_pSgYi_tYa7FailureQzYKFTY4_ : 160 -> 164
~ _$ss20AsyncFlatMapSequenceV8IteratorV4next9isolation7ElementQy_SgScA_pSgYi_tYa7FailureQzYKFTY0_ : 1100 -> 1104
~ _$ss20AsyncFlatMapSequenceV8IteratorV4next9isolation7ElementQy_SgScA_pSgYi_tYa7FailureQzYKFTY2_ : 1468 -> 1480
~ _$ss20AsyncFlatMapSequenceV8IteratorV4next9isolation7ElementQy_SgScA_pSgYi_tYa7FailureQzYKFTY4_ : 732 -> 740
~ _$ss20AsyncFlatMapSequenceV8IteratorV4next9isolation7ElementQy_SgScA_pSgYi_tYa7FailureQzYKFTY8_ : 1528 -> 1540
~ _$ss20AsyncFlatMapSequenceV8IteratorV4next9isolation7ElementQy_SgScA_pSgYi_tYa7FailureQzYKFTY11_ : 560 -> 568
~ _$ss16AsyncMapSequenceV8IteratorV4next9isolationq_SgScA_pSgYi_tYa7FailureQzYKFTY1_ : 536 -> 540
~ _$ss19AsyncPrefixSequenceV8IteratorV4next9isolation7ElementQzSgScA_pSgYi_tYa7FailureQzYKFTY0_ : 560 -> 564
~ _$ss24AsyncPrefixWhileSequenceV8IteratorV4next9isolation7ElementQzSgScA_pSgYi_tYa7FailureQzYKFTY2_ : 520 -> 524
~ _$sScs8IteratorV4next9isolationxSgScA_pSgYi_tYaq_YKFTY2_ : 128 -> 132
CStrings:
+ "Initialized count must be in 0 ... unsafeUninitializedCapacity."
- "Initialized count set to greater than specified capacity."
```
