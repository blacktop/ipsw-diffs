## LocalAuthenticationCore

> `/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`

```diff

-2005.0.13.0.0
-  __TEXT.__text: 0xf54d0
-  __TEXT.__auth_stubs: 0x23e0
-  __TEXT.__objc_methlist: 0x97c0
+2005.0.31.0.0
+  __TEXT.__text: 0xf5454
+  __TEXT.__auth_stubs: 0x23f0
+  __TEXT.__objc_methlist: 0x97e0
   __TEXT.__const: 0x4ae4
-  __TEXT.__gcc_except_tab: 0x19e4
-  __TEXT.__oslogstring: 0x6321
-  __TEXT.__cstring: 0xddad
+  __TEXT.__gcc_except_tab: 0x19f0
+  __TEXT.__oslogstring: 0x6381
+  __TEXT.__cstring: 0xde07
   __TEXT.__dlopen_cstrs: 0x4bb
   __TEXT.__swift5_typeref: 0x1938
   __TEXT.__constg_swiftt: 0xf7c

   __TEXT.__swift5_protos: 0x24
   __TEXT.__swift_as_ret: 0xd8
   __TEXT.__swift5_mpenum: 0x1c
-  __TEXT.__unwind_info: 0x41c0
+  __TEXT.__unwind_info: 0x41d0
   __TEXT.__eh_frame: 0x22c0
   __TEXT.__objc_classname: 0x21c5
-  __TEXT.__objc_methname: 0xf761
-  __TEXT.__objc_methtype: 0x4766
-  __TEXT.__objc_stubs: 0xa420
+  __TEXT.__objc_methname: 0xf7e2
+  __TEXT.__objc_methtype: 0x4769
+  __TEXT.__objc_stubs: 0xa400
   __DATA_CONST.__got: 0xae8
-  __DATA_CONST.__const: 0x4880
+  __DATA_CONST.__const: 0x4870
   __DATA_CONST.__objc_classlist: 0x818
   __DATA_CONST.__objc_protolist: 0x618
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_protorefs: 0x260
   __DATA_CONST.__objc_superrefs: 0x4c0
   __DATA_CONST.__objc_arraydata: 0x40
-  __AUTH_CONST.__auth_got: 0x1200
-  __AUTH_CONST.__const: 0x3980
+  __AUTH_CONST.__auth_got: 0x1208
+  __AUTH_CONST.__const: 0x39a0
   __AUTH_CONST.__cfstring: 0x6380
-  __AUTH_CONST.__objc_const: 0x38b78
+  __AUTH_CONST.__objc_const: 0x38bf8
   __AUTH_CONST.__objc_intobj: 0x288
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH.__objc_data: 0x3128
   __AUTH.__data: 0xbf0
-  __DATA.__objc_ivar: 0x808
+  __DATA.__objc_ivar: 0x80c
   __DATA.__data: 0x4ea0
-  __DATA.__bss: 0x2c91
+  __DATA.__bss: 0x2ca1
   __DATA.__common: 0xa0
   __DATA_DIRTY.__objc_data: 0x2828
   __DATA_DIRTY.__data: 0x4e0

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: E8592E22-8743-3767-A53B-7B8ECFAE2DA4
-  Functions: 6295
-  Symbols:   21867
-  CStrings:  6739
+  UUID: 225EEA0D-EB93-3BAE-AE2F-04F115079CB3
+  Functions: 6300
+  Symbols:   21871
+  CStrings:  6746
 
Symbols:
+ -[LACBiomeEvaluationEvent dtoState]
+ -[LACBiomeEvaluationEvent initWithPolicy:errorCode:biometry:passcode:dtoState:ratchetState:callerBundleID:]
+ -[LACBiomeEvaluationEvent ratchetState]
+ -[LACFlags featureFlagPasscodeServicesUseKeyboardGuideEnabled]
+ -[LACFlags featureFlagPasscodeServicesUseKeyboardGuidePadsEnabled]
+ _LACBiomeEvaluationRatchetStateFromLACDTORatchetStateRawValue
+ _LACLogKeyboard
+ _LACLogKeyboard.__logObj
+ _LACLogKeyboard.cold.1
+ _LACLogKeyboard.onceToken
+ _LACPolicyOptionRedactErrors
+ _OBJC_IVAR_$_LACBiomeEvaluationEvent._dtoState
+ _OBJC_IVAR_$_LACBiomeEvaluationEvent._ratchetState
+ ___LACLogKeyboard_block_invoke
+ ___block_descriptor_tmp.128
+ ___block_descriptor_tmp.141
+ ___block_descriptor_tmp.151
+ ___block_descriptor_tmp.154
+ ___block_descriptor_tmp.170
+ ___block_literal_global.148
+ ___block_literal_global.153
+ ___block_literal_global.156
+ ___block_literal_global.172
+ _objc_msgSend$dtoState
+ _objc_msgSend$initWithPolicy:result:biometry:passcode:ratchetState:callerBundleId:ratchetArmingState:
+ _swift_dynamicCastObjCClass
- -[LACBiomeEvaluationEvent initWithPolicy:errorCode:biometry:passcode:ratchet:callerBundleID:]
- -[LACBiomeEvaluationEvent ratchet]
- -[LACSignpostEvent _sendWithMessage:]
- -[LACSignpostEvent sendWithMessage:]
- _OBJC_IVAR_$_LACBiomeEvaluationEvent._ratchet
- ___block_descriptor_32_e18_v16?0"NSString"8l
- ___block_descriptor_tmp.127
- ___block_descriptor_tmp.139
- ___block_descriptor_tmp.150
- ___block_descriptor_tmp.153
- ___block_descriptor_tmp.169
- ___block_literal_global.152
- ___block_literal_global.155
- ___block_literal_global.171
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swiftDarwin_$_LocalAuthenticationCore
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_LocalAuthenticationCore
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_LocalAuthenticationCore
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_LocalAuthenticationCore
- _objc_msgSend$_sendWithMessage:
- _objc_msgSend$initWithPolicy:result:biometry:passcode:ratchetState:callerBundleId:
- _objc_msgSend$ratchet
CStrings:
+ " enableTelemetry=YES "
+ "\"!"
+ "%@ received a new connection %@ for listener %@"
+ "%@ vending a new listener %@"
+ "%s invalidated, %@ listener"
+ "/.exclave"
+ "<LACBiomeEvaluationEvent caller: %@, policy: %d, errorCode: %d, dtoState: %d, ratchetState: %d, biometry: %@, passcode: %@>"
+ "@72@0:8q16q24@32@40q48q56@64"
+ "Keyboard"
+ "PasscodeServices_UseKeyboardGuide"
+ "PasscodeServices_UseKeyboardGuide_Pads"
+ "Tq,R,N,V_dtoState"
+ "Tq,R,N,V_ratchetState"
+ "_dtoState"
+ "dtoState"
+ "featureFlagPasscodeServicesUseKeyboardGuideEnabled"
+ "featureFlagPasscodeServicesUseKeyboardGuidePadsEnabled"
+ "initWithPolicy:errorCode:biometry:passcode:dtoState:ratchetState:callerBundleID:"
+ "initWithPolicy:result:biometry:passcode:ratchetState:callerBundleId:ratchetArmingState:"
- "%@ received a new connection %@"
- "%s invalidated"
- "<LACBiomeEvaluationEvent caller: %@, policy: %d, errorCode: %d, ratchet: %d, biometry: %@, passcode: %@>"
- "@64@0:8q16q24@32@40q48@56"
- "Tq,R,N,V_ratchet"
- "_ratchet"
- "_sendWithMessage:"
- "initWithPolicy:errorCode:biometry:passcode:ratchet:callerBundleID:"
- "initWithPolicy:result:biometry:passcode:ratchetState:callerBundleId:"
- "ratchet"
- "sendWithMessage:"
- "v16@?0@\"NSString\"8"

```
