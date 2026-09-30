## AssistantUI

> `/System/Library/PrivateFrameworks/AssistantUI.framework/AssistantUI`

```diff

-3500.87.2.0.0
-  __TEXT.__text: 0x571c4
+3500.91.1.1.1
+  __TEXT.__text: 0x574a4
   __TEXT.__auth_stubs: 0xef0
-  __TEXT.__objc_methlist: 0x6b7c
+  __TEXT.__objc_methlist: 0x6b84
   __TEXT.__const: 0x694
   __TEXT.__gcc_except_tab: 0x1664
-  __TEXT.__cstring: 0x7e9b
-  __TEXT.__oslogstring: 0x5051
+  __TEXT.__cstring: 0x7f2b
+  __TEXT.__oslogstring: 0x50a0
   __TEXT.__dlopen_cstrs: 0x46f
   __TEXT.__ustring: 0x1c
   __TEXT.__constg_swiftt: 0x20c

   __TEXT.__swift5_types: 0x18
   __TEXT.__unwind_info: 0x1ca8
   __TEXT.__objc_classname: 0xb09
-  __TEXT.__objc_methname: 0x160c2
+  __TEXT.__objc_methname: 0x16143
   __TEXT.__objc_methtype: 0x4594
-  __TEXT.__objc_stubs: 0xfd60
-  __DATA_CONST.__got: 0xc18
+  __TEXT.__objc_stubs: 0xfde0
+  __DATA_CONST.__got: 0xc20
   __DATA_CONST.__const: 0x1aa0
   __DATA_CONST.__objc_classlist: 0x198
   __DATA_CONST.__objc_catlist: 0xa0
   __DATA_CONST.__objc_protolist: 0x1a8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4fa0
+  __DATA_CONST.__objc_selrefs: 0x4fc0
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x110
   __AUTH_CONST.__auth_got: 0x788
   __AUTH_CONST.__const: 0xd70
-  __AUTH_CONST.__cfstring: 0x29c0
+  __AUTH_CONST.__cfstring: 0x2a00
   __AUTH_CONST.__objc_const: 0x7bf8
   __AUTH_CONST.__objc_doubleobj: 0x40
   __AUTH_CONST.__objc_intobj: 0x60

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: EE620066-0678-3D49-8A08-1CF33B36870A
-  Functions: 2337
-  Symbols:   8729
-  CStrings:  5103
+  UUID: 1C0B8E64-A0B7-3ACC-A96D-863C224C8129
+  Functions: 2338
+  Symbols:   8736
+  CStrings:  5113
 
Symbols:
+ -[AFUISiriSession _populateInvocationEventWithTypeToSiriInvocationContext:]
+ GCC_except_table345
+ _OBJC_CLASS_$_SISchemaTypeToSiriInvocationContext
+ ___123-[AFUISiriSession startCorrectedRequestWithText:correctionIdentifier:userSelectionResults:turnIdentifier:machAbsoluteTime:]_block_invoke.211
+ ___45-[AFUISiriSession _playPhaticWithCompletion:]_block_invoke.172
+ ___45-[AFUISiriSession _playPhaticWithCompletion:]_block_invoke.173
+ ___54-[AFUISiriSession _handleUnlockAppCommand:completion:]_block_invoke.215
+ ___54-[AFUISiriSession startRequestWithOptions:completion:]_block_invoke.119
+ ___54-[AFUISiriSession startRequestWithOptions:completion:]_block_invoke.124
+ ___55-[AFUISiriSession assistantConnectionRequestWillStart:]_block_invoke.127
+ ___56-[AFUISiriSession _handlePhotoPickerRequest:completion:]_block_invoke.258
+ ___56-[AFUISiriSession _handlePhotoPickerRequest:completion:]_block_invoke.258.cold.1
+ ___59-[AFUISiriSession _updateModesHeuristicsForRequestOptions:]_block_invoke.232
+ ___60-[AFUISiriSession _startRequestWithFinalOptions:completion:]_block_invoke.91
+ ___60-[AFUISiriSession _startRequestWithFinalOptions:completion:]_block_invoke.93
+ ___76-[AFUISiriSession _processInstrumentationForFinalOptionsAndGenerateNewTurn:]_block_invoke.88
+ ___block_literal_global.129
+ ___block_literal_global.132
+ ___block_literal_global.159
+ ___block_literal_global.162
+ ___block_literal_global.180
+ ___block_literal_global.182
+ ___block_literal_global.221
+ ___block_literal_global.225
+ ___block_literal_global.227
+ ___block_literal_global.55
+ ___block_literal_global.60
+ ___block_literal_global.65
+ _objc_msgSend$_populateInvocationEventWithTypeToSiriInvocationContext:
+ _objc_msgSend$reverseObjectEnumerator
+ _objc_msgSend$setBackgroundAppBundleId:
+ _objc_msgSend$setTypeToSiriContext:
- GCC_except_table344
- ___123-[AFUISiriSession startCorrectedRequestWithText:correctionIdentifier:userSelectionResults:turnIdentifier:machAbsoluteTime:]_block_invoke.202
- ___45-[AFUISiriSession _playPhaticWithCompletion:]_block_invoke.163
- ___45-[AFUISiriSession _playPhaticWithCompletion:]_block_invoke.164
- ___54-[AFUISiriSession _handleUnlockAppCommand:completion:]_block_invoke.206
- ___54-[AFUISiriSession startRequestWithOptions:completion:]_block_invoke.110
- ___54-[AFUISiriSession startRequestWithOptions:completion:]_block_invoke.115
- ___55-[AFUISiriSession assistantConnectionRequestWillStart:]_block_invoke.118
- ___56-[AFUISiriSession _handlePhotoPickerRequest:completion:]_block_invoke.248
- ___56-[AFUISiriSession _handlePhotoPickerRequest:completion:]_block_invoke.248.cold.1
- ___59-[AFUISiriSession _updateModesHeuristicsForRequestOptions:]_block_invoke.223
- ___60-[AFUISiriSession _startRequestWithFinalOptions:completion:]_block_invoke.82
- ___60-[AFUISiriSession _startRequestWithFinalOptions:completion:]_block_invoke.84
- ___76-[AFUISiriSession _processInstrumentationForFinalOptionsAndGenerateNewTurn:]_block_invoke.79
- ___block_literal_global.120
- ___block_literal_global.123
- ___block_literal_global.141
- ___block_literal_global.153
- ___block_literal_global.169
- ___block_literal_global.192
- ___block_literal_global.194
- ___block_literal_global.46
- ___block_literal_global.51
- ___block_literal_global.56
- ___block_literal_global.93
Functions:
~ -[AFUISiriSession _invocationEventForRequestOptions:localDataSource:] : 680 -> 708
+ -[AFUISiriSession _populateInvocationEventWithTypeToSiriInvocationContext:]
CStrings:
+ "%s #TypeToSiriInvocationContextSender The current backgroundAppBundleId is: %@"
+ "-[AFUISiriSession _populateInvocationEventWithTypeToSiriInvocationContext:]"
+ "_populateInvocationEventWithTypeToSiriInvocationContext:"
+ "com.apple.chrono.WidgetRenderer-Default"
+ "com.apple.siri.IntelligentLight"
+ "reverseObjectEnumerator"
+ "setBackgroundAppBundleId:"
+ "setTypeToSiriContext:"

```
