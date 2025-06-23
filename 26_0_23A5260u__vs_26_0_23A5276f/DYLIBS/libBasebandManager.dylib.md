## libBasebandManager.dylib

> `/usr/lib/libBasebandManager.dylib`

```diff

-1371.0.1.0.0
-  __TEXT.__text: 0x224ef4
+1377.2.0.0.0
+  __TEXT.__text: 0x2250e4
   __TEXT.__auth_stubs: 0x3200
   __TEXT.__init_offsets: 0x150
   __TEXT.__objc_methlist: 0x46c
   __TEXT.__const: 0xf128
-  __TEXT.__gcc_except_tab: 0x34bbc
-  __TEXT.__cstring: 0x7d0a
+  __TEXT.__gcc_except_tab: 0x34b74
+  __TEXT.__cstring: 0x7d06
   __TEXT.__oslogstring: 0xb991
-  __TEXT.__unwind_info: 0xa0f8
+  __TEXT.__unwind_info: 0xa0d8
   __TEXT.__objc_classname: 0x10d
   __TEXT.__objc_methname: 0x13e7
   __TEXT.__objc_methtype: 0x10f0
   __TEXT.__objc_stubs: 0x1100
-  __DATA_CONST.__got: 0x21d0
+  __DATA_CONST.__got: 0x21d8
   __DATA_CONST.__const: 0x2040
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x28

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprotobuf-lite.dylib
   - /usr/lib/libprotobuf.dylib
-  UUID: 4563D5E7-37BA-37BA-8E82-866EC6C0E128
-  Functions: 6027
-  Symbols:   18451
+  UUID: C41F8942-F732-3CDA-93E9-B634A95AEA1E
+  Functions: 6028
+  Symbols:   18449
   CStrings:  2770
 
Symbols:
+ __ZN3abm27kKeyTraceFlushTimerIntervalE
+ __ZN8defaults7bbtrace20flush_timer_intervalEv
+ ___block_descriptor_296_e8_40c35_ZTSNSt3__18weak_ptrI10LogTrackerEE56c67_ZTSZN10LogTracker30postLogCollectionInternal_syncEN3xpc4dictEE3$_5_e147_v48?0{Result=i{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}8{dict={object=^v}}40l
- ___block_descriptor_280_e8_40c35_ZTSNSt3__18weak_ptrI10LogTrackerEE56c67_ZTSZN10LogTracker30postLogCollectionInternal_syncEN3xpc4dictEE3$_5_e147_v48?0{Result=i{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}8{dict={object=^v}}40l
Functions:
~ __ZN8defaults7bbtrace3getERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEERS7_ : 2496 -> 2624
+ __ZN8defaults7bbtrace11live_filterEv
~ __Z23ABMGetRootVersionStringv : 84 -> 88
~ __ZN4prop7bbtrace3setERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_ : 5508 -> 5580
~ __ZN10LogTracker30postLogCollectionExternal_syncEN3xpc4dictE : 1320 -> 1264
~ __ZZN10LogTracker30postLogCollectionExternal_syncEN3xpc4dictEEN3$_2D1Ev : 108 -> 120
~ __ZN10LogTracker30postLogCollectionInternal_syncEN3xpc4dictE : 8964 -> 9044
~ __ZZN10LogTracker30postLogCollectionInternal_syncEN3xpc4dictEEN3$_6D1Ev : 116 -> 56
~ __ZZN10LogTracker30postLogCollectionInternal_syncEN3xpc4dictEEN3$_5D1Ev : 104 -> 116
~ __ZNSt3__110unique_ptrIZN10LogTracker30postLogCollectionExternal_syncEN3xpc4dictEE3$_2NS_14default_deleteIS4_EEED1B8ne200100Ev : 124 -> 68
~ __ZZN8dispatch6detail12group_notifyIZN10LogTracker30postLogCollectionExternal_syncEN3xpc4dictEE3$_2EEvP16dispatch_group_sP16dispatch_queue_sOT_NSt3__117integral_constantIbLb0EEEENUlPvE_8__invokeESF_ : 488 -> 628
~ __ZNSt3__110unique_ptrIZN10LogTracker30postLogCollectionInternal_syncEN3xpc4dictEE3$_6NS_14default_deleteIS4_EEED1B8ne200100Ev : 68 -> 76
~ __ZZN8dispatch6detail12group_notifyIZN10LogTracker30postLogCollectionInternal_syncEN3xpc4dictEE3$_6EEvP16dispatch_group_sP16dispatch_queue_sOT_NSt3__117integral_constantIbLb0EEEENUlPvE_8__invokeESF_ : 924 -> 1012
~ ____ZZN10LogTracker30postLogCollectionInternal_syncEN3xpc4dictEENK3$_6clEv_block_invoke : 564 -> 600
~ ___copy_helper_block_e8_40c35_ZTSNSt3__18weak_ptrI10LogTrackerEE56c67_ZTSZN10LogTracker30postLogCollectionInternal_syncEN3xpc4dictEE3$_5 : 152 -> 204
~ ___destroy_helper_block_e8_40c35_ZTSNSt3__18weak_ptrI10LogTrackerEE56c67_ZTSZN10LogTracker30postLogCollectionInternal_syncEN3xpc4dictEE3$_5 : 136 -> 76
~ __ZZN8dispatch6detail12group_notifyIKZN10LogTracker30postLogCollectionInternal_syncEN3xpc4dictEE3$_5EEvP16dispatch_group_sP16dispatch_queue_sOT_NSt3__117integral_constantIbLb0EEEENUlPvE_8__invokeESG_ : 400 -> 540
~ __ZNSt3__110unique_ptrIKZN10LogTracker30postLogCollectionInternal_syncEN3xpc4dictEE3$_5NS_14default_deleteIS5_EEED1B8ne200100Ev : 120 -> 68
CStrings:
+ "AppleBasebandManager-AppleBasebandServices_Manager-1377.2"
+ "AppleBasebandServices_Manager-1377.2"
- "AppleBasebandManager-AppleBasebandServices_Manager-1371.0.1"
- "AppleBasebandServices_Manager-1371.0.1"

```
