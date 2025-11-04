## HMFoundation

> `/System/Library/PrivateFrameworks/HMFoundation.framework/HMFoundation`

```diff

-893.0.0.0.0
-  __TEXT.__text: 0x88acc
-  __TEXT.__auth_stubs: 0x21b0
-  __TEXT.__objc_methlist: 0x78fc
-  __TEXT.__const: 0x27a8
+900.0.0.0.0
+  __TEXT.__text: 0x8b768
+  __TEXT.__auth_stubs: 0x2220
+  __TEXT.__objc_methlist: 0x78ec
+  __TEXT.__const: 0x2848
   __TEXT.__dlopen_cstrs: 0xf8
-  __TEXT.__cstring: 0x30af
-  __TEXT.__swift5_typeref: 0x9e3
-  __TEXT.__swift5_capture: 0x600
-  __TEXT.__swift_as_entry: 0x168
-  __TEXT.__swift_as_ret: 0x194
-  __TEXT.__swift5_reflstr: 0x373
-  __TEXT.__swift5_assocty: 0x18
-  __TEXT.__constg_swiftt: 0xd38
-  __TEXT.__swift5_fieldmd: 0x670
-  __TEXT.__swift5_protos: 0x1c
+  __TEXT.__cstring: 0x30e5
+  __TEXT.__swift5_typeref: 0xa7e
+  __TEXT.__swift5_capture: 0x67c
+  __TEXT.__swift_as_entry: 0x17c
+  __TEXT.__swift_as_ret: 0x1ac
+  __TEXT.__constg_swiftt: 0xd90
+  __TEXT.__swift5_reflstr: 0x395
+  __TEXT.__swift5_fieldmd: 0x69c
+  __TEXT.__swift5_types: 0xa0
+  __TEXT.__swift5_protos: 0x20
+  __TEXT.__oslogstring: 0x42f3
   __TEXT.__swift5_proto: 0x3c
-  __TEXT.__swift5_types: 0x9c
-  __TEXT.__oslogstring: 0x4213
-  __TEXT.__gcc_except_tab: 0x1c68
+  __TEXT.__swift5_assocty: 0x18
+  __TEXT.__gcc_except_tab: 0x1c48
   __TEXT.__ustring: 0x8
-  __TEXT.__unwind_info: 0x2ef8
-  __TEXT.__eh_frame: 0x2e98
+  __TEXT.__unwind_info: 0x3000
+  __TEXT.__eh_frame: 0x31e0
   __TEXT.__objc_classname: 0x111e
-  __TEXT.__objc_methname: 0xc8d3
+  __TEXT.__objc_methname: 0xc8d9
   __TEXT.__objc_methtype: 0x27d7
-  __TEXT.__objc_stubs: 0x93e0
-  __DATA_CONST.__got: 0x7f0
+  __TEXT.__objc_stubs: 0x9400
+  __DATA_CONST.__got: 0x7f8
   __DATA_CONST.__const: 0x1658
   __DATA_CONST.__objc_classlist: 0x460
   __DATA_CONST.__objc_catlist: 0xa8

   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x380
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__auth_got: 0x10e8
-  __AUTH_CONST.__const: 0x21d8
-  __AUTH_CONST.__cfstring: 0x4b60
+  __AUTH_CONST.__auth_got: 0x1120
+  __AUTH_CONST.__const: 0x22c8
+  __AUTH_CONST.__cfstring: 0x4b40
   __AUTH_CONST.__objc_const: 0xe3f0
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x1130
-  __AUTH.__data: 0x150
+  __AUTH.__data: 0x1d0
   __AUTH.__thread_vars: 0x18
   __AUTH.__thread_bss: 0x8
   __DATA.__objc_ivar: 0x198
-  __DATA.__data: 0x2490
+  __DATA.__data: 0x24d8
   __DATA.__bss: 0x514
   __DATA_DIRTY.__objc_ivar: 0x5b0
   __DATA_DIRTY.__objc_data: 0x1a40

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: D7DCFDB9-6615-34E8-88F5-70BA178798FA
-  Functions: 3461
-  Symbols:   9436
-  CStrings:  4621
+  UUID: E5532715-7898-332F-8C5B-F8D0D0F8E1D8
+  Functions: 3516
+  Symbols:   9450
+  CStrings:  4625
 
Symbols:
+ -[HMFMessageDispatcher orderedFilterClasses]
+ -[HMFMessageDispatcher setOrderedFilterClasses:]
+ GCC_except_table33
+ GCC_except_table42
+ GCC_except_table50
+ _HMFOperatingSystemVersionCompareWithLeeway
+ ___block_literal_global.143
+ ___block_literal_global.52
+ _objc_msgSend$callStackSymbols
+ _objc_msgSend$orderedFilterClasses
+ _objc_msgSend$setOrderedFilterClasses:
+ _swift_getEnumTagSinglePayloadGeneric
+ _swift_getSingletonMetadata
+ _swift_storeEnumTagSinglePayloadGeneric
+ _symbolic $s12HMFoundation3HMFO7LoggingP
+ _symbolic ScCyx_____G s5NeverO
+ _symbolic ScCyx______pG s5ErrorP
+ _symbolic ScSyyyYaYbcG
+ _symbolic _____ 12HMFoundation3HMFO16AsyncSerialQueueV
+ _symbolic _____yyyYaYbc_G ScS12ContinuationV
+ _symbolic _____yyyYaYbc_G ScS8IteratorV
+ _symbolic _____yyyYaYbc__G ScS12ContinuationV11YieldResultO
+ _symbolic _____yyyYaYbc__G ScS12ContinuationV15BufferingPolicyO
+ _symbolic xIeghHr_
- +[HMFActivity activityWithName:parent:assertions:block:]
- -[HMFActivity assertions]
- -[HMFActivity initWithName:parent:assertions:]
- GCC_except_table41
- GCC_except_table45
- ___block_literal_global.142
- ___block_literal_global.57
- _objc_msgSend$assertions
- _objc_msgSend$filterClasses
CStrings:
+ "%{public}@API Misuse: hmf_objectForKey with a nil key. Call stack: %@"
+ "%{public}@API Misuse: hmf_offsetForKeyValue with a nil key. Call stack: %@"
+ "%{public}@Message %@ dropped by %@"
+ "%{public}@Message was ignored by filter: %@"
+ "T@\"NSArray\",C,V_orderedFilterClasses"
+ "T@\"NSSet\",C"
+ "_orderedFilterClasses"
+ "callStackSymbols"
+ "orderedFilterClasses"
+ "performAndWait(_:)"
+ "setOrderedFilterClasses:"
- "Assertions"
- "Memory"
- "Power"
- "T@\"NSSet\",C,V_filterClasses"
- "_filterClasses"
- "activityWithName:parent:assertions:block:"
- "assertions"
- "initWithName:parent:assertions:"

```
