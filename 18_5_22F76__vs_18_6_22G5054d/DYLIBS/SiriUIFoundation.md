## SiriUIFoundation

> `/System/Library/PrivateFrameworks/SiriUIFoundation.framework/SiriUIFoundation`

```diff

-3405.30.3.11.5
-  __TEXT.__text: 0x3b728
+3406.15.1.0.0
+  __TEXT.__text: 0x3b818
   __TEXT.__auth_stubs: 0xd70
   __TEXT.__objc_methlist: 0x365c
-  __TEXT.__const: 0x6c8
+  __TEXT.__const: 0x728
   __TEXT.__cstring: 0x4dab
-  __TEXT.__oslogstring: 0x3721
-  __TEXT.__gcc_except_tab: 0x928
+  __TEXT.__oslogstring: 0x3791
+  __TEXT.__gcc_except_tab: 0x930
   __TEXT.__ustring: 0x22
   __TEXT.__constg_swiftt: 0x3f0
   __TEXT.__swift5_typeref: 0x330

   __TEXT.__unwind_info: 0x10a0
   __TEXT.__eh_frame: 0x218
   __TEXT.__objc_classname: 0x7a1
-  __TEXT.__objc_methname: 0xa880
+  __TEXT.__objc_methname: 0xa89d
   __TEXT.__objc_methtype: 0x17fa
   __TEXT.__objc_stubs: 0x6f60
   __DATA_CONST.__got: 0x688
-  __DATA_CONST.__const: 0x1570
+  __DATA_CONST.__const: 0x1598
   __DATA_CONST.__objc_classlist: 0x1d8
   __DATA_CONST.__objc_catlist: 0x140
   __DATA_CONST.__objc_protolist: 0xd8

   __AUTH_CONST.__auth_got: 0x6c8
   __AUTH_CONST.__const: 0x838
   __AUTH_CONST.__cfstring: 0x1dc0
-  __AUTH_CONST.__objc_const: 0x6160
+  __AUTH_CONST.__objc_const: 0x6180
   __AUTH_CONST.__objc_intobj: 0xf0
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0xa28
   __AUTH.__data: 0x368
-  __DATA.__objc_ivar: 0x37c
-  __DATA.__data: 0x9f0
+  __DATA.__objc_ivar: 0x380
+  __DATA.__data: 0x990
   __DATA.__bss: 0x6a0
   __DATA.__common: 0x48
   __DATA_DIRTY.__objc_data: 0x998

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: C34ACB46-A639-310E-93DC-BD407C38EF79
+  UUID: 557A1B95-43DB-39AA-A219-DC6803B58D8A
   Functions: 1508
-  Symbols:   4924
-  CStrings:  2895
+  Symbols:   4926
+  CStrings:  2897
 
Symbols:
+ _OBJC_IVAR_$_SRUIFStateFeedbackManager._pendingDelayToneFeedbackIDs
+ ___block_descriptor_48_e8_32s40w_e20_v24?0q8"NSError"16lw40l8s32l8
Functions:
~ -[SRUIFStateFeedbackManager initWithStateFeedbackProvider:delegate:] : 216 -> 240
~ -[SRUIFStateFeedbackManager _cancelFeedbackWithCompletion:] : 308 -> 316
~ -[SRUIFStateFeedbackManager _playDelayFeedback] : 212 -> 272
~ ___47-[SRUIFStateFeedbackManager _playDelayFeedback]_block_invoke : 412 -> 504
~ -[SRUIFStateFeedbackManager .cxx_destruct] : 112 -> 124
~ +[SRUIFUtilities parsedUtteranceFromText:context:spekableObjectProviding:] : 328 -> 332
~ sub_225a429bc -> sub_225cb3a84 : 2380 -> 2364
~ sub_225a433a4 -> sub_225cb445c : 1788 -> 1800
~ sub_225a43b34 -> sub_225cb4bf8 : 2020 -> 2008
~ sub_225a44394 -> sub_225cb544c : 112 -> 124
~ sub_225a44404 -> sub_225cb54c8 : 120 -> 168
~ sub_225a4447c -> sub_225cb5570 : 280 -> 276
CStrings:
+ "%s #statefeedback playDelayFeedback completion called, but returning early because the feedback has been cancelled."
+ "_pendingDelayToneFeedbackIDs"

```
