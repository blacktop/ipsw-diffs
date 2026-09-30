## SiriActivation

> `/System/Library/PrivateFrameworks/SiriActivation.framework/SiriActivation`

```diff

-3500.91.1.1.1
-  __TEXT.__text: 0x4eb24
+3500.99.4.0.0
+  __TEXT.__text: 0x4ed50
   __TEXT.__auth_stubs: 0xbe0
   __TEXT.__objc_methlist: 0x6014
   __TEXT.__const: 0x822
-  __TEXT.__cstring: 0xa04d
-  __TEXT.__oslogstring: 0x6d03
-  __TEXT.__gcc_except_tab: 0xe40
+  __TEXT.__cstring: 0xa06d
+  __TEXT.__oslogstring: 0x6dc5
+  __TEXT.__gcc_except_tab: 0xe5c
   __TEXT.__dlopen_cstrs: 0x1bc
   __TEXT.__swift5_typeref: 0x102
   __TEXT.__constg_swiftt: 0x160

   __TEXT.__unwind_info: 0x15f0
   __TEXT.__eh_frame: 0x138
   __TEXT.__objc_classname: 0x101d
-  __TEXT.__objc_methname: 0xdc5c
+  __TEXT.__objc_methname: 0xdcad
   __TEXT.__objc_methtype: 0x23b0
-  __TEXT.__objc_stubs: 0x9480
+  __TEXT.__objc_stubs: 0x94e0
   __DATA_CONST.__got: 0x6a8
   __DATA_CONST.__const: 0x1670
   __DATA_CONST.__objc_classlist: 0x330
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x150
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2dd0
+  __DATA_CONST.__objc_selrefs: 0x2de8
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x2a0
   __DATA_CONST.__objc_arraydata: 0x530

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 56B80ED3-6CB4-38DB-841C-220EF4D3DCAE
+  UUID: 305724B0-949C-342B-8067-474E44E11BC5
   Functions: 2164
-  Symbols:   7411
-  CStrings:  4530
+  Symbols:   7414
+  CStrings:  4537
 
Symbols:
+ ___22-[SASSystemState init]_block_invoke.185
+ ___32-[SASRemoteRequestManager _init]_block_invoke.92
+ ___32-[SASRemoteRequestManager _init]_block_invoke.92.cold.1
+ ___38-[SASHeater updatePredictedRouteIsZLL]_block_invoke.58
+ ___73-[SiriActivationService buttonTapFromButtonIdentifier:timestamp:context:]_block_invoke.138
+ ___93-[SiriActivationService _activatePresentationWithIdentifier:requestOptions:analyticsContext:]_block_invoke.174
+ ___block_literal_global.142
+ ___block_literal_global.181
+ ___block_literal_global.576
+ ___block_literal_global.581
+ ___block_literal_global.80
+ ___block_literal_global.87
+ ___block_literal_global.91
+ ___block_literal_global.95
+ _objc_msgSend$adjustedScoreOverride
+ _objc_msgSend$isAlwaysAllowedWhileDeviceLocked
+ _objc_msgSend$setAdjustedScoreOverride:
- ___22-[SASSystemState init]_block_invoke.179
- ___32-[SASRemoteRequestManager _init]_block_invoke.86
- ___32-[SASRemoteRequestManager _init]_block_invoke.86.cold.1
- ___38-[SASHeater updatePredictedRouteIsZLL]_block_invoke.52
- ___73-[SiriActivationService buttonTapFromButtonIdentifier:timestamp:context:]_block_invoke.132
- ___93-[SiriActivationService _activatePresentationWithIdentifier:requestOptions:analyticsContext:]_block_invoke.168
- ___block_literal_global.136
- ___block_literal_global.175
- ___block_literal_global.570
- ___block_literal_global.575
- ___block_literal_global.74
- ___block_literal_global.81
- ___block_literal_global.85
- ___block_literal_global.89
Functions:
~ -[SASMyriadController activateForRequest:withTimeout:visible:quiet:] : 5492 -> 5684
~ -[SiriActivationService _uiPresentationIdentifierWithActivation:activationPresentation:] : 332 -> 364
~ +[SASActivationDecision canActivateForCondition:] : 6244 -> 6576
CStrings:
+ "%s #activation NO: Mismatching info: uiPresentationIdentifier: %@ but car session exists."
+ "%s #activation: AFRequestInfo.isAlwaysAllowedWhileDeviceLocked = %@"
+ "%s #myriad adjustedScoreOverride %@"
+ "adjustedScoreOverride"
+ "isAlwaysAllowedWhileDeviceLocked"
+ "setAdjustedScoreOverride:"

```
