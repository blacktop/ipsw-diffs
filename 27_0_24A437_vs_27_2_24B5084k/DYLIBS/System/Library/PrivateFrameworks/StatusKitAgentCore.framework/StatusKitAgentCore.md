## StatusKitAgentCore

> `/System/Library/PrivateFrameworks/StatusKitAgentCore.framework/StatusKitAgentCore`

```diff

-154.100.1.0.0
-  __TEXT.__text: 0x1b18a0
-  __TEXT.__objc_methlist: 0xb0f0
-  __TEXT.__const: 0x5c08
-  __TEXT.__cstring: 0x96dc
-  __TEXT.__oslogstring: 0x192d6
-  __TEXT.__gcc_except_tab: 0xe90
+154.200.11.0.0
+  __TEXT.__text: 0x1b2570
+  __TEXT.__objc_methlist: 0xb110
+  __TEXT.__const: 0x5c28
+  __TEXT.__cstring: 0x977c
+  __TEXT.__oslogstring: 0x19416
+  __TEXT.__gcc_except_tab: 0xecc
   __TEXT.__swift5_typeref: 0x295e
   __TEXT.__constg_swiftt: 0x1c30
   __TEXT.__swift5_reflstr: 0x1527

   __TEXT.__swift_as_ret: 0x360
   __TEXT.__swift_as_cont: 0x6f8
   __TEXT.__swift5_acfuncs: 0x3c
-  __TEXT.__unwind_info: 0x7180
-  __TEXT.__eh_frame: 0x9d50
+  __TEXT.__unwind_info: 0x7190
+  __TEXT.__eh_frame: 0x9da8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__got: 0xd88
   __AUTH_CONST.__const: 0x6628
   __AUTH_CONST.__cfstring: 0x3260
-  __AUTH_CONST.__objc_const: 0x11740
-  __AUTH_CONST.__objc_intobj: 0x3d8
+  __AUTH_CONST.__objc_const: 0x11770
+  __AUTH_CONST.__objc_intobj: 0x3f0
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__auth_got: 0x1608
+  __AUTH_CONST.__auth_got: 0x1600
   __AUTH.__objc_data: 0x1360
   __AUTH.__data: 0x230
   __DATA.__objc_ivar: 0x808
   __DATA.__data: 0x1c90
   __DATA_DIRTY.__objc_data: 0x3ad0
-  __DATA_DIRTY.__data: 0x1f48
+  __DATA_DIRTY.__data: 0x1f38
   __DATA_DIRTY.__bss: 0x14d0
   __DATA_DIRTY.__common: 0xb0
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 7782
-  Symbols:   15883
-  CStrings:  2603
+  Functions: 7790
+  Symbols:   15885
+  CStrings:  2611
 
Symbols:
+ +[SKAMessagingProvider _isBlastdoorEnabledForServiceIdentifier:]
+ GCC_except_table3
+ GCC_except_table64
+ _$s18StatusKitAgentCore11SKACALoggerC20_checkErrorThreshold5event5error6client5clockyAA10SKACAEventO_So7NSErrorCAA14SKACALogClientCSgAA8SKAClock_ptFZTf4nnnen_nAA0Q7WrapperCys15ContinuousClockVG_Tg5Tf4nnnnd_n
+ _$s18StatusKitAgentCore14SKACALogClientC11descriptionSSvg
+ _$s18StatusKitAgentCore14SKACALogClientC11descriptionSSvgTo
+ _$s18StatusKitAgentCore14SKACALogClientC4hashSivg
+ _$s18StatusKitAgentCore14SKACALogClientC4hashSivgTo
+ _$s18StatusKitAgentCore14SKACALogClientC7isEqualySbypSgF
+ _$s18StatusKitAgentCore14SKACALogClientC7isEqualySbypSgFTo
+ _$sypSgWOcTm
+ __PROPERTIES_SKACALogClient
+ ___block_descriptor_64_e8_32s40s48bs_e49_v24?0"SKAUnpackedProtobufResponse"8"NSError"16ls32l8s40l8s48l8
+ ___logger_block_invoke
+ _objc_msgSend$_isBlastdoorEnabledForServiceIdentifier:
+ _objc_msgSend$rateLimiter
- +[SKAMessagingProvider _isBlastdoorEnabledForService:]
- +[SKAStatusServer sharedInstance]
- _$s18StatusKitAgentCore11SKACALogKeyO_yptWOc
- _$s18StatusKitAgentCore11SKACALoggerC20_checkErrorThreshold5event5error6client5clockyAA10SKACAEventO_So7NSErrorCAA14SKACALogClientCSgAA8SKAClock_ptFZTf4nnnen_nAA0Q7WrapperCys15ContinuousClockVG_Tt3g5
- _$s18StatusKitAgentCore14SKACALogClientCSgMR
- _$s18StatusKitAgentCore14SKACALogClientCSgMd
- _$sSGsE4next10upperBoundqd__qd___ts17FixedWidthIntegerRd__SURd__lFqd__s27SystemRandomNumberGeneratorVqd__AERszsACRd__SURd__r__lIetMnlr_Tpq5s6UInt64V_Tg5
- _$sSo8SKHandleCMaTm
- ___33+[SKAStatusServer sharedInstance]_block_invoke
- ___block_descriptor_56_e8_32s40bs_e49_v24?0"SKAUnpackedProtobufResponse"8"NSError"16ls32l8s40l8
- _objc_msgSend$_isBlastdoorEnabledForService:
- _sharedInstance.instance
- _sharedInstance.onceToken
- _swift_stdlib_random
CStrings:
+ "Delay for %s: using=%ss, next=%ss (max: %ss)"
+ "Not attempting repair for channel %{public}@ because of rate limit, reason: %@"
+ "Poll response checkpoint is 0, treating as an empty channel and applying state on channel %{public}@"
+ "Present device read from database has a missing required field: %@"
+ "Repeated error threshold (%ld within %lds) reached for %s; reporting to AutoBugCapture"
+ "SKADatabaseCoreDataAdapters"
+ "com.apple.StatusKit.presence.subscribeRegistration"
+ "com.apple.StatusKit.status.provisionedPayloads"
+ "provisionedPayloadCount"
- "Delay for %s: using=%ss (before jitter: %ss), next=%ss (max: %ss)"
```
