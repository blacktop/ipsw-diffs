## NearbyInteraction

> `/System/Library/Frameworks/NearbyInteraction.framework/NearbyInteraction`

```diff

-507.0.4.0.0
-  __TEXT.__text: 0x32788
+507.0.5.0.0
+  __TEXT.__text: 0x32798
   __TEXT.__auth_stubs: 0x870
   __TEXT.__objc_methlist: 0x3ea8
   __TEXT.__gcc_except_tab: 0x55c0

   __TEXT.__unwind_info: 0x1f40
   __TEXT.__objc_classname: 0x5fc
   __TEXT.__objc_methname: 0x8d5e
-  __TEXT.__objc_methtype: 0x1629
+  __TEXT.__objc_methtype: 0x1637
   __TEXT.__objc_stubs: 0x4fa0
   __DATA_CONST.__got: 0x290
   __DATA_CONST.__const: 0xcb8

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: FF620333-355C-3214-901B-96D62C71951A
+  UUID: DFB4AE24-473C-392B-846F-F168C6C3AE9B
   Functions: 1457
   Symbols:   5186
   CStrings:  3353
Functions:
~ __Z24nsNumberArrayToStdVectorItEDaPK7NSArrayIP8NSNumberE : 548 -> 552
~ __ZNSt3__16vectorItNS_9allocatorItEEE11__vallocateB8ne200100Em : 56 -> 60
~ -[NISession uwbSessionInterruptedWithReason:timestamp:] : 804 -> 800
~ -[NISession uwbSessionInterruptionReasonEnded:timestamp:] : 1204 -> 1208
~ __ZNSt3__16vectorI33UWBSessionInterruptionBookkeepingNS_9allocatorIS1_EEE11__vallocateB8ne200100Em : 60 -> 64
~ __ZNSt3__16vectorImNS_9allocatorImEEE11__vallocateB8ne200100Em : 60 -> 64
CStrings:
+ "{AcwgM1MsgStruct={vector<unsigned short, std::allocator<unsigned short>>=^S^S{?=^S}}{vector<unsigned char, std::allocator<unsigned char>>=**{?=*}}CICS}16@0:8"
+ "{vector<UWBSessionInterruptionBookkeeping, std::allocator<UWBSessionInterruptionBookkeeping>>=\"__begin_\"^{UWBSessionInterruptionBookkeeping}\"__end_\"^{UWBSessionInterruptionBookkeeping}\"\"{?=\"__cap_\"^{UWBSessionInterruptionBookkeeping}}}"
- "{AcwgM1MsgStruct={vector<unsigned short, std::allocator<unsigned short>>=^S^S^S}{vector<unsigned char, std::allocator<unsigned char>>=***}CICS}16@0:8"
- "{vector<UWBSessionInterruptionBookkeeping, std::allocator<UWBSessionInterruptionBookkeeping>>=\"__begin_\"^{UWBSessionInterruptionBookkeeping}\"__end_\"^{UWBSessionInterruptionBookkeeping}\"__cap_\"^{UWBSessionInterruptionBookkeeping}}"

```
