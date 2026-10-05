## SiriActivation

> `/System/Library/PrivateFrameworks/SiriActivation.framework/SiriActivation`

```diff

-3605.24.1.0.0
-  __TEXT.__text: 0x73868
-  __TEXT.__objc_methlist: 0x7254
+3605.30.1.0.0
+  __TEXT.__text: 0x742c8
+  __TEXT.__objc_methlist: 0x72dc
   __TEXT.__const: 0x124c
-  __TEXT.__cstring: 0xcf62
-  __TEXT.__oslogstring: 0x9ae4
-  __TEXT.__gcc_except_tab: 0xcec
+  __TEXT.__cstring: 0xd0d2
+  __TEXT.__oslogstring: 0x9bc3
+  __TEXT.__gcc_except_tab: 0xd00
   __TEXT.__dlopen_cstrs: 0x1bc
   __TEXT.__swift5_typeref: 0x77a
   __TEXT.__constg_swiftt: 0x42c

   __TEXT.__swift5_protos: 0xc
   __TEXT.__swift5_mpenum: 0x14
   __TEXT.__swift_as_cont: 0x8c
-  __TEXT.__unwind_info: 0x26f0
+  __TEXT.__unwind_info: 0x2740
   __TEXT.__eh_frame: 0xf58
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x18c0
+  __DATA_CONST.__const: 0x1910
   __DATA_CONST.__objc_classlist: 0x3a8
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x1e0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x35f8
+  __DATA_CONST.__objc_selrefs: 0x3658
   __DATA_CONST.__objc_protorefs: 0x68
-  __DATA_CONST.__objc_superrefs: 0x2d8
+  __DATA_CONST.__objc_superrefs: 0x2e0
   __DATA_CONST.__objc_arraydata: 0x510
   __DATA_CONST.__got: 0xaa8
   __AUTH_CONST.__const: 0x14b0
   __AUTH_CONST.__cfstring: 0x50a0
-  __AUTH_CONST.__objc_const: 0xb5f8
+  __AUTH_CONST.__objc_const: 0xb640
   __AUTH_CONST.__objc_intobj: 0x978
   __AUTH_CONST.__objc_dictobj: 0x118
-  __AUTH_CONST.__auth_got: 0xbe8
+  __AUTH_CONST.__auth_got: 0xbf0
   __AUTH.__objc_data: 0x2190
   __AUTH.__data: 0x118
-  __DATA.__objc_ivar: 0x748
+  __DATA.__objc_ivar: 0x750
   __DATA.__data: 0x1710
   __DATA.__common: 0x270
   __DATA_DIRTY.__objc_data: 0x5f0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2971
-  Symbols:   4743
-  CStrings:  1856
+  Functions: 2988
+  Symbols:   4764
+  CStrings:  1867
 
Symbols:
+ -[SASActivationRequest isAutoPromptRequest]
+ -[SASHeater _replacePreheatBlock:]
+ -[SASHeater _scheduleBlockAfterTimeInterval:]
+ -[SASHeater init]
+ -[SASHeater preheatQueue]
+ -[SASHeater prepareForUseAfterTimeInterval:buttonDownTimestamp:]
+ -[SASHeater setPreheatQueue:]
+ -[SASMyriadController _goodnessScoreContextWithTimerFiring:alarmFiring:]
+ -[SASMyriadController _primeMTAlarmManagerState]
+ -[SASMyriadController _primeMTTimerManagerState]
+ -[SASMyriadController _runOnMyriadWorkQueueWithSelf:]
+ -[SASSignalServer prewarmFromButtonIdentifier:longPressInterval:buttonDownTimestamp:]
+ -[SiriActivationService prewarmFromButtonIdentifier:longPressInterval:buttonDownTimestamp:]
+ GCC_except_table106
+ GCC_except_table112
+ GCC_except_table163
+ GCC_except_table33
+ GCC_except_table38
+ GCC_except_table43
+ GCC_except_table44
+ GCC_except_table49
+ GCC_except_table56
+ GCC_except_table84
+ _OBJC_IVAR_$_SASHeater._lock
+ _OBJC_IVAR_$_SASHeater._preheatBlock
+ _OBJC_IVAR_$_SASHeater._preheatQueue
+ ___45-[SASHeater _scheduleBlockAfterTimeInterval:]_block_invoke
+ ___45-[SASHeater _scheduleBlockAfterTimeInterval:]_block_invoke_2
+ ___48-[SASMyriadController _primeMTAlarmManagerState]_block_invoke
+ ___48-[SASMyriadController _primeMTAlarmManagerState]_block_invoke_2
+ ___48-[SASMyriadController _primeMTTimerManagerState]_block_invoke
+ ___48-[SASMyriadController _primeMTTimerManagerState]_block_invoke_2
+ ___53-[SASMyriadController _runOnMyriadWorkQueueWithSelf:]_block_invoke
+ ___block_descriptor_40_e8_32s_e29_v16?0"SASMyriadController"8ls32l8
+ ___block_descriptor_40_e8_32w_e17_v16?0"NSArray"8lw32l8
+ _dispatch_block_cancel
- -[SASHeater preheatTimer]
- -[SASHeater setPreheatTimer:]
- GCC_except_table105
- GCC_except_table110
- GCC_except_table162
- GCC_except_table26
- GCC_except_table31
- GCC_except_table34
- GCC_except_table39
- GCC_except_table40
- GCC_except_table47
- GCC_except_table83
- _OBJC_IVAR_$_SASHeater._preheatTimer
- ___31-[SASHeater _cancelPreparation]_block_invoke
- ___44-[SASHeater prepareForUseAfterTimeInterval:]_block_invoke
CStrings:
+ "%s #myriad priming MTAlarmManager: %lu alarm(s)"
+ "%s #myriad priming MTTimerManager: %lu timer(s)"
+ "%s #myriad unenumerated siriContext type: %@, resolved speechRequestOptions generically"
+ "%s Scheduling preheat for %fs from now"
+ "-[SASHeater prepareForUseAfterTimeInterval:buttonDownTimestamp:]"
+ "-[SASMyriadController _primeMTAlarmManagerState]_block_invoke_2"
+ "-[SASMyriadController _primeMTTimerManagerState]_block_invoke_2"
+ "-[SASSignalServer prewarmFromButtonIdentifier:longPressInterval:buttonDownTimestamp:]"
+ "-[SiriActivationService prewarmFromButtonIdentifier:longPressInterval:buttonDownTimestamp:]"
+ "com.apple.siri.SASHeater.preheat"
+ "v16@?0@\"NSArray\"8"
+ "v16@?0@\"SASMyriadController\"8"
- "-[SiriActivationService prewarmFromButtonIdentifier:longPressInterval:]"
```
