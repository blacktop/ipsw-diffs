## RTTUtilities

> `/System/Library/PrivateFrameworks/RTTUtilities.framework/RTTUtilities`

```diff

-492.1.0.0.0
+494.0.0.0.0
   __TEXT.__text: 0x273f0
   __TEXT.__auth_stubs: 0x9d0
   __TEXT.__objc_methlist: 0x1d30

   __TEXT.__objc_methtype: 0x8ee
   __TEXT.__objc_stubs: 0x52a0
   __DATA_CONST.__got: 0x3a8
-  __DATA_CONST.__const: 0xf98
+  __DATA_CONST.__const: 0xfa0
   __DATA_CONST.__objc_classlist: 0x98
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x58

   - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
+  - /usr/lib/swift/libswiftCoreAudio_Private.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 88129430-BE10-36EB-8507-A0036C77C0B7
+  UUID: 0CF48F99-87CB-34FC-B4FB-8E217A40AB99
   Functions: 843
-  Symbols:   3124
+  Symbols:   3126
   CStrings:  1903
 
Symbols:
+ ___28-[RTTRemoteCall sendString:]_block_invoke.595
+ ___33-[RTTCall device:didReceiveText:]_block_invoke.419
+ ___38-[RTTDictionaryManager deleteIfNeeded]_block_invoke.285
+ ___44-[RTTRemoteCall responseForRequest:options:]_block_invoke.636
+ ___44-[RTTRemoteCall responseForRequest:options:]_block_invoke.638
+ ___44-[RTTRemoteCall responseForRequest:options:]_block_invoke.638.cold.1
+ ___49-[RTTRemoteCall callDidReceiveText:forUtterance:]_block_invoke.612
+ ___49-[RTTRemoteCall callDidReceiveText:forUtterance:]_block_invoke.616
+ ___55-[RTTRemoteCall newRapportClientWithDestinationDevice:]_block_invoke.628
+ ___55-[RTTRemoteCall newRapportClientWithDestinationDevice:]_block_invoke.629
+ ___61-[RTTRemoteCall sendCallIDChallengeToDeviceId:orAlternateId:]_block_invoke.632
+ ___block_literal_global.287
+ ___block_literal_global.289
+ ___block_literal_global.580
+ __swift_FORCE_LOAD_$_swiftCoreAudio_Private
+ __swift_FORCE_LOAD_$_swiftCoreAudio_Private_$_RTTUtilities
- ___28-[RTTRemoteCall sendString:]_block_invoke.592
- ___33-[RTTCall device:didReceiveText:]_block_invoke.416
- ___38-[RTTDictionaryManager deleteIfNeeded]_block_invoke.279
- ___44-[RTTRemoteCall responseForRequest:options:]_block_invoke.633
- ___44-[RTTRemoteCall responseForRequest:options:]_block_invoke.635
- ___44-[RTTRemoteCall responseForRequest:options:]_block_invoke.635.cold.1
- ___49-[RTTRemoteCall callDidReceiveText:forUtterance:]_block_invoke.609
- ___49-[RTTRemoteCall callDidReceiveText:forUtterance:]_block_invoke.613
- ___55-[RTTRemoteCall newRapportClientWithDestinationDevice:]_block_invoke.622
- ___55-[RTTRemoteCall newRapportClientWithDestinationDevice:]_block_invoke.626
- ___61-[RTTRemoteCall sendCallIDChallengeToDeviceId:orAlternateId:]_block_invoke.629
- ___block_literal_global.284
- ___block_literal_global.286
- ___block_literal_global.577

```
