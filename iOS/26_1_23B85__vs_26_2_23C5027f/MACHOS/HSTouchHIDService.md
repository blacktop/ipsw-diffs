## HSTouchHIDService

> `/System/Library/HIDPlugins/ServicePlugins/HSTouchHIDService.plugin/HSTouchHIDService`

```diff

 9110.1.0.0.0
-  __TEXT.__text: 0xc6394
+  __TEXT.__text: 0xc6408
   __TEXT.__auth_stubs: 0x1950
   __TEXT.__objc_stubs: 0x61c0
   __TEXT.__init_offsets: 0x1260

   __TEXT.__gcc_except_tab: 0xd684
   __TEXT.__cstring: 0xa180
   __TEXT.__oslogstring: 0x3704
-  __TEXT.__objc_methname: 0x6e7a
+  __TEXT.__objc_methname: 0x6e82
   __TEXT.__objc_classname: 0xb7d
-  __TEXT.__objc_methtype: 0x5400
+  __TEXT.__objc_methtype: 0x5446
   __TEXT.__unwind_info: 0x42a0
   __DATA_CONST.__auth_got: 0xcb8
   __DATA_CONST.__got: 0x270

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 30B4573F-B5E9-3220-8AAE-A7473200D145
+  UUID: 6716944B-91F1-3CAA-B23C-E7B44C4446B2
   Functions: 4692
   Symbols:   26062
   CStrings:  4490
Functions:
~ __ZNSt3__16vectorINS_6atomicIPKN6HSUtil8CoderKeyEEENS_9allocatorIS6_EEE11__vallocateB8ne200100Em : 60 -> 64
~ __ZNSt3__16vectorIU8__strongP8HIDEventNS_9allocatorIS3_EEE11__vallocateB8ne200100Em : 60 -> 64
~ __ZNSt3__16vectorINS0_IiNS_9allocatorIiEEEENS1_IS3_EEE11__vallocateB8ne200100Em : 76 -> 80
~ __ZNSt3__16vectorIiNS_9allocatorIiEEE11__vallocateB8ne200100Em : 60 -> 64
~ __ZNSt3__16vectorINS0_IiNS_9allocatorIiEEEENS1_IS3_EEE18__assign_with_sizeB8ne200100IPS3_S7_EEvT_T0_l : 376 -> 380
~ __ZNSt3__16vectorI18MTChordGestureSet_NS_9allocatorIS1_EEE24__emplace_back_slow_pathIJRKS1_EEEPS1_DpOT_ : 312 -> 316
~ __ZNSt3__16vectorI14MTActionEvent_NS_9allocatorIS1_EEE11__vallocateB8ne200100Em : 60 -> 64
~ __ZNSt3__16vectorI14MTActionEvent_NS_9allocatorIS1_EEE24__emplace_back_slow_pathIJRKS1_EEEPS1_DpOT_ : 308 -> 304
~ __ZNSt3__16vectorI15MTSlideGesture_NS_9allocatorIS1_EEE24__emplace_back_slow_pathIJRKS1_EEEPS1_DpOT_ : 312 -> 316
~ __ZNSt3__16vectorI13MTParserPath_NS_9allocatorIS1_EEE7reserveEm : 232 -> 248
~ __ZN13MTPathStates_35computePathAndFingerSpeedSymmetriesEi : 1220 -> 1224
~ __ZNSt3__16vectorI13MTParserPath_NS_9allocatorIS1_EEE24__emplace_back_slow_pathIJRK12MTParserTypeRK15MTParserOptionsEEEPS1_DpOT_ : 344 -> 356
~ __ZNSt3__16vectorI15MTSlideGesture_NS_9allocatorIS1_EEE18__assign_with_sizeB8ne200100IPS1_S6_EEvT_T0_l : 424 -> 428
~ __ZNSt3__16vectorI15MTSlideGesture_NS_9allocatorIS1_EEE11__vallocateB8ne200100Em : 76 -> 80
~ __ZNSt3__16vectorINS0_I16MTForceBehavior_NS_9allocatorIS1_EEEENS2_IS4_EEE11__vallocateB8ne200100Em : 76 -> 80
~ __ZNSt3__16vectorI16MTForceBehavior_NS_9allocatorIS1_EEE24__emplace_back_slow_pathIJRKS1_EEEPS1_DpOT_ : 336 -> 340
~ __ZNSt3__16vectorI20MTForceThresholding_NS_9allocatorIS1_EEE11__vallocateB8ne200100Em : 76 -> 80
~ -[HSTFrameParser sanitizeContactFrame:] : 1428 -> 1436
~ __ZNSt3__16vectorIN11HSTPipeline7ContactENS_9allocatorIS2_EEE11__vallocateB8ne200100Em : 60 -> 64
~ -[HSTPencilVirtualService _handleVendorEvent:] : 668 -> 672
~ -[HSTContactStabilizer _handleContactFrame:] : 788 -> 792
~ -[HSTContactStabilizerStats hsDecode:] : 808 -> 804
~ -[HSTHIDEventGenerator _cancelActiveContacts:] : 884 -> 900
~ -[HSTContactFrame decodeFromMap:] : 1232 -> 1236
CStrings:
+ "T{vector<std::vector<int>, std::allocator<std::vector<int>>>=^v^v{?=^v}},N,V_deltas"
+ "T{vector<std::vector<int>, std::allocator<std::vector<int>>>=^v^v{?=^v}},N,V_interpolatedDeltas"
+ "v40@0:8{vector<std::vector<int>, std::allocator<std::vector<int>>>=^v^v{?=^v}}16"
+ "{MTForceBehavior_=iiiBI{vector<float, std::allocator<float>>=^f^f{?=^f}}{vector<int, std::allocator<int>>=^i^i{?=^i}}{vector<int, std::allocator<int>>=^i^i{?=^i}}{vector<int, std::allocator<int>>=^i^i{?=^i}}{vector<int, std::allocator<int>>=^i^i{?=^i}}}28@0:8^{__MTForceConfig=}16i24"
+ "{basic_string<char, std::char_traits<char>, std::allocator<char>>=\"\"{?=\"__rep_\"(__rep=\"__s\"{__short=\"__data_\"[23c]\"__size_\"b7\"__is_long_\"b1}\"__l\"{__long=\"__data_\"*\"__size_\"Q\"__cap_\"b63\"__is_long_\"b1})}}"
+ "{vector<ContactStabilizer, std::allocator<ContactStabilizer>>=\"__begin_\"^{ContactStabilizer}\"__end_\"^{ContactStabilizer}\"\"{?=\"__cap_\"^{ContactStabilizer}}}"
+ "{vector<HIDEvent *, std::allocator<HIDEvent *>>=\"__begin_\"^@\"__end_\"^@\"\"{?=\"__cap_\"^@}}"
+ "{vector<HSTPipeline::Contact, std::allocator<HSTPipeline::Contact>>=\"__begin_\"^{Contact}\"__end_\"^{Contact}\"\"{?=\"__cap_\"^{Contact}}}"
+ "{vector<StatContact, std::allocator<StatContact>>=\"__begin_\"^{StatContact}\"__end_\"^{StatContact}\"\"{?=\"__cap_\"^{StatContact}}}"
+ "{vector<int, std::allocator<int>>=\"__begin_\"^i\"__end_\"^i\"\"{?=\"__cap_\"^i}}"
+ "{vector<std::vector<int>, std::allocator<std::vector<int>>>=\"__begin_\"^v\"__end_\"^v\"\"{?=\"__cap_\"^v}}"
+ "{vector<std::vector<int>, std::allocator<std::vector<int>>>=^v^v{?=^v}}16@0:8"
- "T{vector<std::vector<int>, std::allocator<std::vector<int>>>=^v^v^v},N,V_deltas"
- "T{vector<std::vector<int>, std::allocator<std::vector<int>>>=^v^v^v},N,V_interpolatedDeltas"
- "v40@0:8{vector<std::vector<int>, std::allocator<std::vector<int>>>=^v^v^v}16"
- "{MTForceBehavior_=iiiBI{vector<float, std::allocator<float>>=^f^f^f}{vector<int, std::allocator<int>>=^i^i^i}{vector<int, std::allocator<int>>=^i^i^i}{vector<int, std::allocator<int>>=^i^i^i}{vector<int, std::allocator<int>>=^i^i^i}}28@0:8^{__MTForceConfig=}16i24"
- "{basic_string<char, std::char_traits<char>, std::allocator<char>>=\"__rep_\"(__rep=\"__s\"{__short=\"__data_\"[23c]\"__size_\"b7\"__is_long_\"b1}\"__l\"{__long=\"__data_\"*\"__size_\"Q\"__cap_\"b63\"__is_long_\"b1})}"
- "{vector<ContactStabilizer, std::allocator<ContactStabilizer>>=\"__begin_\"^{ContactStabilizer}\"__end_\"^{ContactStabilizer}\"__cap_\"^{ContactStabilizer}}"
- "{vector<HIDEvent *, std::allocator<HIDEvent *>>=\"__begin_\"^@\"__end_\"^@\"__cap_\"^@}"
- "{vector<HSTPipeline::Contact, std::allocator<HSTPipeline::Contact>>=\"__begin_\"^{Contact}\"__end_\"^{Contact}\"__cap_\"^{Contact}}"
- "{vector<StatContact, std::allocator<StatContact>>=\"__begin_\"^{StatContact}\"__end_\"^{StatContact}\"__cap_\"^{StatContact}}"
- "{vector<int, std::allocator<int>>=\"__begin_\"^i\"__end_\"^i\"__cap_\"^i}"
- "{vector<std::vector<int>, std::allocator<std::vector<int>>>=\"__begin_\"^v\"__end_\"^v\"__cap_\"^v}"
- "{vector<std::vector<int>, std::allocator<std::vector<int>>>=^v^v^v}16@0:8"

```
