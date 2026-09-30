## HMFoundation

> `/System/Library/PrivateFrameworks/HMFoundation.framework/HMFoundation`

```diff

-  __TEXT.__text: 0x966cc
+  __TEXT.__text: 0x97cbc
   __TEXT.__delay_stubs: 0x400
   __TEXT.__delay_helper: 0x294
-  __TEXT.__objc_methlist: 0x78d4
-  __TEXT.__const: 0x3018
+  __TEXT.__objc_methlist: 0x7944
+  __TEXT.__const: 0x3028
   __TEXT.__dlopen_cstrs: 0xf8
   __TEXT.__swift5_typeref: 0xb6e
   __TEXT.__swift5_reflstr: 0x42a
   __TEXT.__swift5_assocty: 0x88
-  __TEXT.__constg_swiftt: 0xdf0
+  __TEXT.__constg_swiftt: 0xe10
   __TEXT.__swift5_fieldmd: 0x7c4
   __TEXT.__swift5_proto: 0x6c
   __TEXT.__swift5_types: 0xb4
   __TEXT.__cstring: 0x312b
-  __TEXT.__swift5_capture: 0x64c
-  __TEXT.__swift_as_entry: 0x198
-  __TEXT.__swift_as_ret: 0x1c0
-  __TEXT.__swift_as_cont: 0x230
+  __TEXT.__swift5_capture: 0x670
+  __TEXT.__swift_as_entry: 0x19c
+  __TEXT.__swift_as_ret: 0x1c4
+  __TEXT.__swift_as_cont: 0x228
   __TEXT.__swift5_protos: 0x20
-  __TEXT.__oslogstring: 0x7ec5
-  __TEXT.__gcc_except_tab: 0x1954
+  __TEXT.__oslogstring: 0x801d
+  __TEXT.__gcc_except_tab: 0x1970
   __TEXT.__ustring: 0x8
-  __TEXT.__unwind_info: 0x3180
-  __TEXT.__eh_frame: 0x3130
+  __TEXT.__unwind_info: 0x31e0
+  __TEXT.__eh_frame: 0x3278
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1568
-  __DATA_CONST.__objc_classlist: 0x468
+  __DATA_CONST.__const: 0x15c8
+  __DATA_CONST.__objc_classlist: 0x478
   __DATA_CONST.__objc_catlist: 0xa8
   __DATA_CONST.__objc_protolist: 0x1d8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x30e8
+  __DATA_CONST.__objc_selrefs: 0x3100
   __DATA_CONST.__objc_protorefs: 0x40
-  __DATA_CONST.__objc_superrefs: 0x380
+  __DATA_CONST.__objc_superrefs: 0x388
   __DATA_CONST.__objc_arraydata: 0x20
   __DATA_CONST.__got: 0x820
-  __AUTH_CONST.__const: 0x22e8
+  __AUTH_CONST.__const: 0x2338
   __AUTH_CONST.__cfstring: 0x4ae0
-  __AUTH_CONST.__objc_const: 0xe4c8
+  __AUTH_CONST.__objc_const: 0xe638
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__auth_got: 0x1330
-  __AUTH.__objc_data: 0x1b30
-  __AUTH.__data: 0x2f0
+  __AUTH_CONST.__auth_got: 0x1348
+  __AUTH.__objc_data: 0x1b80
+  __AUTH.__data: 0x310
   __AUTH.__thread_vars: 0x18
   __AUTH.__thread_bss: 0x8
   __DATA.__objc_ivar: 0x1b0
-  __DATA.__data: 0x27c4
+  __DATA.__data: 0x27cc
   __DATA.__bss: 0xaa0
-  __DATA_DIRTY.__objc_ivar: 0x59c
-  __DATA_DIRTY.__objc_data: 0x1040
+  __DATA_DIRTY.__objc_ivar: 0x5a4
+  __DATA_DIRTY.__objc_data: 0x1090
   __DATA_DIRTY.__bss: 0x538
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 3640
-  Symbols:   9627
-  CStrings:  2010
+  Functions: 3657
+  Symbols:   9667
+  CStrings:  2014
 
Sections:
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__swift5_assocty : content changed
~ __TEXT.__swift5_fieldmd : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift5_types : content changed
~ __TEXT.__swift5_protos : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__got : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH.__thread_vars : content changed
Symbols:
+ -[HMFCoalescingTimer __fire]
+ -[HMFCoalescingTimer debounceInterval]
+ -[HMFCoalescingTimer initWithDebounceInterval:maximumInterval:options:]
+ -[HMFCoalescingTimer maximumInterval]
+ -[HMFCoalescingTimer nextFireInterval]
+ -[HMFCoalescingTimer resume]
+ -[HMFCoalescingTimer suspend]
+ -[HMFTimer nextFireInterval]
+ GCC_except_table41
+ GCC_except_table44
+ _HMFQualityOfServiceClassToString
+ _OBJC_CLASS_$_HMFCoalescingTimer
+ _OBJC_METACLASS_$_HMFCoalescingTimer
+ __DATA__TtCO12HMFoundation3HMF16AsyncSerialQueue
+ __IVARS__TtCO12HMFoundation3HMF16AsyncSerialQueue
+ __METACLASS_DATA__TtCO12HMFoundation3HMF16AsyncSerialQueue
+ __OBJC_$_INSTANCE_METHODS_HMFCoalescingTimer
+ __OBJC_$_INSTANCE_VARIABLES_HMFCoalescingTimer
+ __OBJC_$_PROP_LIST_HMFCoalescingTimer
+ __OBJC_CLASS_RO_$_HMFCoalescingTimer
+ __OBJC_METACLASS_RO_$_HMFCoalescingTimer
+ ___block_descriptor_56_e8_32s40s48s_e41_B32?0"<HMFMessageRegistration>"8Q16^B24ls32l8s40l8s48l8
+ _objc_msgSend$nextFireInterval
+ _swift_release_x26
+ _swift_task_localValuePop
+ _swift_task_localValuePush
+ _swift_updateClassMetadata2
+ _symbolic ShySOG
+ _symbolic _____ 12HMFoundation3HMFO16AsyncSerialQueueC
- GCC_except_table18
- _get_type_metadata 15Synchronization5MutexVy12HMFoundation3HMFO11ManualClockC5State33_465D37F0B3FF74F1DA60984A81E9136ELLVG noncopyable
- _swift_runtimeSupportsNoncopyableTypes
- _symbolic _____ 12HMFoundation3HMFO16AsyncSerialQueueV
CStrings:
+ "[%{public}@] [HMFCoalescingTimer] The debounce interval, %f, must be greater than 0"
+ "[%{public}@] [HMFCoalescingTimer] The maximum interval, %f, must be 0 or > the debounce interval, %f"
+ "[HMFCoalescingTimer] The debounce interval, %f, must be greater than 0"
+ "[HMFCoalescingTimer] The maximum interval, %f, must be 0 or > the debounce interval, %f"

```
