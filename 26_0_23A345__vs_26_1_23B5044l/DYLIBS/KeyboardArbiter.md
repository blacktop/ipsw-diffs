## KeyboardArbiter

> `/System/Library/PrivateFrameworks/KeyboardArbiter.framework/KeyboardArbiter`

```diff

-9088.1.113.0.0
-  __TEXT.__text: 0x18ff0
-  __TEXT.__auth_stubs: 0x630
-  __TEXT.__objc_methlist: 0x1214
+9126.1.4.106.0
+  __TEXT.__text: 0x19178
+  __TEXT.__auth_stubs: 0x640
+  __TEXT.__objc_methlist: 0x1230
   __TEXT.__const: 0x100
-  __TEXT.__cstring: 0xf93
+  __TEXT.__cstring: 0xfba
   __TEXT.__oslogstring: 0x1a37
-  __TEXT.__gcc_except_tab: 0x910
+  __TEXT.__gcc_except_tab: 0x92c
   __TEXT.__dlopen_cstrs: 0xa4
-  __TEXT.__unwind_info: 0x5d0
+  __TEXT.__unwind_info: 0x5d8
   __TEXT.__objc_classname: 0x2f2
-  __TEXT.__objc_methname: 0x36e6
-  __TEXT.__objc_methtype: 0xc0b
-  __TEXT.__objc_stubs: 0x3000
-  __DATA_CONST.__got: 0x200
+  __TEXT.__objc_methname: 0x372f
+  __TEXT.__objc_methtype: 0xc45
+  __TEXT.__objc_stubs: 0x3020
+  __DATA_CONST.__got: 0x208
   __DATA_CONST.__const: 0x858
   __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xe30
+  __DATA_CONST.__objc_selrefs: 0xe40
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x60
   __DATA_CONST.__objc_arraydata: 0x80
-  __AUTH_CONST.__auth_got: 0x328
+  __AUTH_CONST.__auth_got: 0x330
   __AUTH_CONST.__const: 0x1e0
-  __AUTH_CONST.__cfstring: 0x900
-  __AUTH_CONST.__objc_const: 0x1d70
+  __AUTH_CONST.__cfstring: 0x920
+  __AUTH_CONST.__objc_const: 0x1d78
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x30

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 582BF736-B563-3C9A-94D3-156BC642D950
-  Functions: 377
-  Symbols:   1678
-  CStrings:  1090
+  UUID: 80258EB8-45CF-3B85-92E3-BBE5AF338F60
+  Functions: 378
+  Symbols:   1683
+  CStrings:  1096
 
Symbols:
+ -[_UIKeyboardArbiterClientHandle pointIsWithinKeyboardContent:onCompletion:]
+ _OBJC_CLASS_$_UIPeripheralHost
+ ___39-[_UIKeyboardArbiter attemptConnection]_block_invoke.122
+ ___43-[_UIKeyboardArbiter scheduleWindowTimeout]_block_invoke.126
+ ___57-[_UIKeyboardArbiter listener:shouldAcceptNewConnection:]_block_invoke.207
+ ___57-[_UIKeyboardArbiter listener:shouldAcceptNewConnection:]_block_invoke.325
+ ___58-[_UIKeyboardArbiter processWithPID:foreground:suspended:]_block_invoke.174
+ ___59-[_UIKeyboardArbiter runOperations:onHandler:fromFunction:]_block_invoke.125
+ ___61-[_UIKeyboardArbiter retrieveDebugInformationWithCompletion:]_block_invoke.77
+ ___65-[_UIKeyboardArbiter updateKeyboardStatus:fromHandler:fromFocus:]_block_invoke.148
+ ___65-[_UIKeyboardArbiter updateKeyboardStatus:fromHandler:fromFocus:]_block_invoke_2.151
+ ___72-[_UIKeyboardArbiterClientHandle takeProcessAssertionOnRemoteWithQueue:]_block_invoke.574
+ ___72-[_UIKeyboardArbiterClientHandle takeProcessAssertionOnRemoteWithQueue:]_block_invoke.579
+ ___block_literal_global.129
+ ___block_literal_global.131
+ ___block_literal_global.153
+ ___block_literal_global.176
+ ___block_literal_global.327
+ ___block_literal_global.536
+ ___block_literal_global.587
+ ___block_literal_global.784
+ _objc_msgSend$pointIsWithinKeyboardContent:
+ _objc_retainAutoreleasedReturnValue
- ___39-[_UIKeyboardArbiter attemptConnection]_block_invoke.119
- ___43-[_UIKeyboardArbiter scheduleWindowTimeout]_block_invoke.123
- ___57-[_UIKeyboardArbiter listener:shouldAcceptNewConnection:]_block_invoke.204
- ___57-[_UIKeyboardArbiter listener:shouldAcceptNewConnection:]_block_invoke.322
- ___58-[_UIKeyboardArbiter processWithPID:foreground:suspended:]_block_invoke.171
- ___59-[_UIKeyboardArbiter runOperations:onHandler:fromFunction:]_block_invoke.122
- ___61-[_UIKeyboardArbiter retrieveDebugInformationWithCompletion:]_block_invoke.74
- ___65-[_UIKeyboardArbiter updateKeyboardStatus:fromHandler:fromFocus:]_block_invoke.145
- ___65-[_UIKeyboardArbiter updateKeyboardStatus:fromHandler:fromFocus:]_block_invoke_2.148
- ___72-[_UIKeyboardArbiterClientHandle takeProcessAssertionOnRemoteWithQueue:]_block_invoke.571
- ___72-[_UIKeyboardArbiterClientHandle takeProcessAssertionOnRemoteWithQueue:]_block_invoke.576
- ___block_literal_global.126
- ___block_literal_global.128
- ___block_literal_global.147
- ___block_literal_global.173
- ___block_literal_global.324
- ___block_literal_global.533
- ___block_literal_global.583
- ___block_literal_global.777
Functions:
~ -[_UIKeyboardArbiter updateKeyboardStatus:fromHandler:fromFocus:] : 5572 -> 5776
~ -[_UIKeyboardArbiter newClientConnected:withExpectedState:onConnected:] : 840 -> 896
+ -[_UIKeyboardArbiterClientHandle pointIsWithinKeyboardContent:onCompletion:]
CStrings:
+ "com.apple.LocalAuthenticationUIService"
+ "pointIsWithinKeyboardContent:"
+ "pointIsWithinKeyboardContent:onCompletion:"
+ "v40@0:8{CGPoint=dd}16@?32"
+ "v40@0:8{CGPoint=dd}16@?<v@?B>32"

```
