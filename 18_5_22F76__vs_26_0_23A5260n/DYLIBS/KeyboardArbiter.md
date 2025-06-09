## KeyboardArbiter

> `/System/Library/PrivateFrameworks/KeyboardArbiter.framework/KeyboardArbiter`

```diff

-8506.1.101.0.0
-  __TEXT.__text: 0x18ad0
-  __TEXT.__auth_stubs: 0x660
+9071.1.107.0.0
+  __TEXT.__text: 0x18e40
+  __TEXT.__auth_stubs: 0x630
   __TEXT.__objc_methlist: 0x11fc
   __TEXT.__const: 0x100
-  __TEXT.__cstring: 0xf01
-  __TEXT.__oslogstring: 0x19a2
-  __TEXT.__gcc_except_tab: 0x8f8
+  __TEXT.__cstring: 0xf5c
+  __TEXT.__oslogstring: 0x1a37
+  __TEXT.__gcc_except_tab: 0x900
   __TEXT.__dlopen_cstrs: 0xa4
   __TEXT.__unwind_info: 0x5d0
   __TEXT.__objc_classname: 0x2f2
-  __TEXT.__objc_methname: 0x364f
-  __TEXT.__objc_methtype: 0xbec
-  __TEXT.__objc_stubs: 0x2f60
-  __DATA_CONST.__got: 0x1f0
+  __TEXT.__objc_methname: 0x368c
+  __TEXT.__objc_methtype: 0xc0b
+  __TEXT.__objc_stubs: 0x2fc0
+  __DATA_CONST.__got: 0x200
   __DATA_CONST.__const: 0x858
   __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xe08
+  __DATA_CONST.__objc_selrefs: 0xe20
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x60
   __DATA_CONST.__objc_arraydata: 0x80
-  __AUTH_CONST.__auth_got: 0x340
+  __AUTH_CONST.__auth_got: 0x328
   __AUTH_CONST.__const: 0x1a0
-  __AUTH_CONST.__cfstring: 0x8e0
-  __AUTH_CONST.__objc_const: 0x1d48
+  __AUTH_CONST.__cfstring: 0x900
+  __AUTH_CONST.__objc_const: 0x1d68
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0x168
+  __DATA.__objc_ivar: 0x16c
   __DATA.__data: 0x420
   __DATA.__bss: 0x8
   __DATA_DIRTY.__objc_ivar: 0x18

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: FACF92D9-DCC7-3EB8-8236-D9CD9BCE871F
+  UUID: 42B3900D-3D29-3E8E-A710-F2BB513B084A
   Functions: 374
-  Symbols:   1665
-  CStrings:  1077
+  Symbols:   1668
+  CStrings:  1087
 
Symbols:
+ _OBJC_CLASS_$_BSServiceDispatchQueue
+ _OBJC_CLASS_$_BSServiceQuality
+ _OBJC_IVAR_$__UIKeyboardArbiter._bsQueue
+ ___39-[_UIKeyboardArbiter attemptConnection]_block_invoke.119
+ ___43-[_UIKeyboardArbiter scheduleWindowTimeout]_block_invoke.123
+ ___57-[_UIKeyboardArbiter listener:shouldAcceptNewConnection:]_block_invoke.200
+ ___57-[_UIKeyboardArbiter listener:shouldAcceptNewConnection:]_block_invoke.317
+ ___58-[_UIKeyboardArbiter processWithPID:foreground:suspended:]_block_invoke.167
+ ___59-[_UIKeyboardArbiter runOperations:onHandler:fromFunction:]_block_invoke.122
+ ___61-[_UIKeyboardArbiter retrieveDebugInformationWithCompletion:]_block_invoke.74
+ ___65-[_UIKeyboardArbiter updateKeyboardStatus:fromHandler:fromFocus:]_block_invoke.141
+ ___65-[_UIKeyboardArbiter updateKeyboardStatus:fromHandler:fromFocus:]_block_invoke_2.144
+ ___72-[_UIKeyboardArbiterClientHandle takeProcessAssertionOnRemoteWithQueue:]_block_invoke.565
+ ___72-[_UIKeyboardArbiterClientHandle takeProcessAssertionOnRemoteWithQueue:]_block_invoke.570
+ ___block_descriptor_48_e8_32s40s_e74_v24?0"_UIKeyboardArbiterClientHandle"8"_UIKeyboardChangedInformation"16ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48s_e49_v24?0"<_UIKeyboardArbitrationClient>"8?<v?>16ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s56l8s48l8
+ ___block_literal_global.143
+ ___block_literal_global.146
+ ___block_literal_global.169
+ ___block_literal_global.319
+ ___block_literal_global.527
+ ___block_literal_global.577
+ ___block_literal_global.771
+ _objc_msgSend$queue
+ _objc_msgSend$queueWithName:serviceQuality:
+ _objc_msgSend$userInteractive
- ___39-[_UIKeyboardArbiter attemptConnection]_block_invoke.115
- ___43-[_UIKeyboardArbiter scheduleWindowTimeout]_block_invoke.119
- ___57-[_UIKeyboardArbiter listener:shouldAcceptNewConnection:]_block_invoke.193
- ___57-[_UIKeyboardArbiter listener:shouldAcceptNewConnection:]_block_invoke.310
- ___58-[_UIKeyboardArbiter processWithPID:foreground:suspended:]_block_invoke.160
- ___59-[_UIKeyboardArbiter runOperations:onHandler:fromFunction:]_block_invoke.118
- ___61-[_UIKeyboardArbiter retrieveDebugInformationWithCompletion:]_block_invoke.70
- ___65-[_UIKeyboardArbiter updateKeyboardStatus:fromHandler:fromFocus:]_block_invoke_3
- ___65-[_UIKeyboardArbiter updateKeyboardStatus:fromHandler:fromFocus:]_block_invoke_4
- ___72-[_UIKeyboardArbiterClientHandle takeProcessAssertionOnRemoteWithQueue:]_block_invoke.556
- ___72-[_UIKeyboardArbiterClientHandle takeProcessAssertionOnRemoteWithQueue:]_block_invoke.561
- ___block_descriptor_56_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
- ___block_descriptor_72_e8_32s40s48s56s64s_e49_v24?0"<_UIKeyboardArbitrationClient>"8?<v?>16ls32l8s40l8s48l8s56l8s64l8
- ___block_descriptor_80_e8_32s40s48s56s64s72s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8
- ___block_literal_global.137
- ___block_literal_global.139
- ___block_literal_global.162
- ___block_literal_global.312
- ___block_literal_global.518
- ___block_literal_global.568
- ___block_literal_global.762
- _dispatch_queue_attr_make_with_qos_class
- _objc_retain_x26
- _objc_retain_x27
CStrings:
+ "================ Last detected blank keyboard at %@, firstTapOn: %@ ===================="
+ "@\"BSServiceDispatchQueue\""
+ "@\"BSServiceQueue\""
+ "[%@] %@ Resigns and informs previous active %@"
+ "[%@] %@(active=%@) taps on blank keyboard, activeInputDestinationHandle: %@, focusRequestedHandle: %@"
+ "_bsQueue"
+ "queue"
+ "queueWithName:serviceQuality:"
+ "userInteractive"
+ "v24@0:8@\"BSServiceQueue\"16"
+ "v24@?0@\"_UIKeyboardArbiterClientHandle\"8@\"_UIKeyboardChangedInformation\"16"
- "================ Last detected blank keyboard at %@ ===================="
- "v24@0:8@\"NSObject<OS_dispatch_queue>\"16"

```
