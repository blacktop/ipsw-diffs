## KeyboardArbiter

> `/System/Library/PrivateFrameworks/KeyboardArbiter.framework/KeyboardArbiter`

```diff

-8506.1.101.0.0
-  __TEXT.__text: 0x18ad0
-  __TEXT.__auth_stubs: 0x660
+8603.0.0.0.0
+  __TEXT.__text: 0x18e08
+  __TEXT.__auth_stubs: 0x640
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

   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x60
   __DATA_CONST.__objc_arraydata: 0x80
-  __AUTH_CONST.__auth_got: 0x340
+  __AUTH_CONST.__auth_got: 0x330
   __AUTH_CONST.__const: 0x1a0
   __AUTH_CONST.__cfstring: 0x8e0
   __AUTH_CONST.__objc_const: 0x1d48

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: FACF92D9-DCC7-3EB8-8236-D9CD9BCE871F
+  UUID: AB3C406E-0CFA-3FAA-B236-97A7ED4BF98F
   Functions: 374
-  Symbols:   1665
-  CStrings:  1077
+  Symbols:   1663
+  CStrings:  1080
 
Symbols:
+ ___57-[_UIKeyboardArbiter listener:shouldAcceptNewConnection:]_block_invoke.196
+ ___57-[_UIKeyboardArbiter listener:shouldAcceptNewConnection:]_block_invoke.313
+ ___58-[_UIKeyboardArbiter processWithPID:foreground:suspended:]_block_invoke.163
+ ___65-[_UIKeyboardArbiter updateKeyboardStatus:fromHandler:fromFocus:]_block_invoke.137
+ ___65-[_UIKeyboardArbiter updateKeyboardStatus:fromHandler:fromFocus:]_block_invoke_2.140
+ ___72-[_UIKeyboardArbiterClientHandle takeProcessAssertionOnRemoteWithQueue:]_block_invoke.559
+ ___72-[_UIKeyboardArbiterClientHandle takeProcessAssertionOnRemoteWithQueue:]_block_invoke.564
+ ___block_descriptor_48_e8_32s40s_e74_v24?0"_UIKeyboardArbiterClientHandle"8"_UIKeyboardChangedInformation"16ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48s_e49_v24?0"<_UIKeyboardArbitrationClient>"8?<v?>16ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s56l8s48l8
+ ___block_literal_global.142
+ ___block_literal_global.165
+ ___block_literal_global.315
+ ___block_literal_global.521
+ ___block_literal_global.571
+ ___block_literal_global.765
- ___57-[_UIKeyboardArbiter listener:shouldAcceptNewConnection:]_block_invoke.193
- ___57-[_UIKeyboardArbiter listener:shouldAcceptNewConnection:]_block_invoke.310
- ___58-[_UIKeyboardArbiter processWithPID:foreground:suspended:]_block_invoke.160
- ___65-[_UIKeyboardArbiter updateKeyboardStatus:fromHandler:fromFocus:]_block_invoke_3
- ___65-[_UIKeyboardArbiter updateKeyboardStatus:fromHandler:fromFocus:]_block_invoke_4
- ___72-[_UIKeyboardArbiterClientHandle takeProcessAssertionOnRemoteWithQueue:]_block_invoke.556
- ___72-[_UIKeyboardArbiterClientHandle takeProcessAssertionOnRemoteWithQueue:]_block_invoke.561
- ___block_descriptor_56_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
- ___block_descriptor_72_e8_32s40s48s56s64s_e49_v24?0"<_UIKeyboardArbitrationClient>"8?<v?>16ls32l8s40l8s48l8s56l8s64l8
- ___block_descriptor_80_e8_32s40s48s56s64s72s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8
- ___block_literal_global.137
- ___block_literal_global.162
- ___block_literal_global.312
- ___block_literal_global.518
- ___block_literal_global.568
- ___block_literal_global.762
- _objc_retain_x26
- _objc_retain_x27
CStrings:
+ "================ Last detected blank keyboard at %@, firstTapOn: %@ ===================="
+ "[%@] %@ Resigns and informs previous active %@"
+ "[%@] %@(active=%@) taps on blank keyboard, activeInputDestinationHandle: %@, focusRequestedHandle: %@"
+ "v24@?0@\"_UIKeyboardArbiterClientHandle\"8@\"_UIKeyboardChangedInformation\"16"
- "================ Last detected blank keyboard at %@ ===================="

```
