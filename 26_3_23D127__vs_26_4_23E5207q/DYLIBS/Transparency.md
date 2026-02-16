## Transparency

> `/System/Library/PrivateFrameworks/Transparency.framework/Transparency`

```diff

-1547.80.8.0.0
-  __TEXT.__text: 0x4aeb4
-  __TEXT.__auth_stubs: 0xdf0
-  __TEXT.__objc_methlist: 0x4470
-  __TEXT.__cstring: 0x27fe
-  __TEXT.__const: 0x12c0
-  __TEXT.__gcc_except_tab: 0x508
-  __TEXT.__oslogstring: 0x1ba2
+1547.100.130.0.0
+  __TEXT.__text: 0x4ca2c
+  __TEXT.__auth_stubs: 0xd80
+  __TEXT.__objc_methlist: 0x44fc
+  __TEXT.__cstring: 0x27ae
+  __TEXT.__const: 0x136b
+  __TEXT.__gcc_except_tab: 0x4ec
+  __TEXT.__oslogstring: 0x1bdc
   __TEXT.__swift5_typeref: 0x390
   __TEXT.__constg_swiftt: 0x2f0
   __TEXT.__swift5_reflstr: 0x4e9

   __TEXT.__swift5_types: 0x4c
   __TEXT.__swift5_assocty: 0x78
   __TEXT.__swift5_builtin: 0x14
-  __TEXT.__unwind_info: 0x1998
+  __TEXT.__unwind_info: 0x19b0
   __TEXT.__eh_frame: 0x4d0
-  __TEXT.__objc_classname: 0x724
-  __TEXT.__objc_methname: 0x760f
-  __TEXT.__objc_methtype: 0x1f3e
-  __TEXT.__objc_stubs: 0x5a00
-  __DATA_CONST.__got: 0x3f0
-  __DATA_CONST.__const: 0x1570
+  __TEXT.__objc_classname: 0x77b
+  __TEXT.__objc_methname: 0x7810
+  __TEXT.__objc_methtype: 0x1f9f
+  __TEXT.__objc_stubs: 0x5b80
+  __DATA_CONST.__got: 0x3f8
+  __DATA_CONST.__const: 0x1598
   __DATA_CONST.__objc_classlist: 0x210
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1e08
+  __DATA_CONST.__objc_selrefs: 0x1e50
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x180
-  __AUTH_CONST.__auth_got: 0x708
-  __AUTH_CONST.__const: 0x27c0
-  __AUTH_CONST.__cfstring: 0x38c0
-  __AUTH_CONST.__objc_const: 0x75a0
+  __AUTH_CONST.__auth_got: 0x6d0
+  __AUTH_CONST.__const: 0x2800
+  __AUTH_CONST.__cfstring: 0x3960
+  __AUTH_CONST.__objc_const: 0x7618
   __AUTH_CONST.__objc_intobj: 0x1b0
-  __AUTH.__objc_data: 0x308
-  __AUTH.__data: 0x2f0
-  __DATA.__objc_ivar: 0x3a0
-  __DATA.__data: 0x968
+  __AUTH.__objc_data: 0x268
+  __AUTH.__data: 0x2e8
+  __DATA.__objc_ivar: 0x3a8
+  __DATA.__data: 0x988
   __DATA.__bss: 0x2350
-  __DATA_DIRTY.__objc_data: 0x12b8
-  __DATA_DIRTY.__data: 0x38
-  __DATA_DIRTY.__bss: 0x1b0
+  __DATA_DIRTY.__objc_data: 0x1358
+  __DATA_DIRTY.__data: 0x30
+  __DATA_DIRTY.__bss: 0x1b8
   __DATA_DIRTY.__common: 0x30
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
+  - /System/Library/PrivateFrameworks/CoreTransparency.framework/CoreTransparency
   - /System/Library/PrivateFrameworks/FeatureFlags.framework/FeatureFlags
   - /System/Library/PrivateFrameworks/OSAnalytics.framework/OSAnalytics
   - /System/Library/PrivateFrameworks/ProtectedCloudStorage.framework/ProtectedCloudStorage

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  UUID: 0CC5E15A-8F99-32FE-A45F-EF60DD2F2069
-  Functions: 2484
-  Symbols:   6732
-  CStrings:  2776
+  UUID: 512F3A78-68F3-3354-9AFB-A4B13CA3EF08
+  Functions: 2498
+  Symbols:   6782
+  CStrings:  2797
 
Symbols:
+ +[TransparencyAnalytics doSuppressMetrics:]
+ +[TransparencySettings sharedSettings]
+ +[TransparencySettings sharedSettings].cold.1
+ -[KTIDSSession localSessionID]
+ -[KTIDSSession peerSessionID]
+ -[KTIDSSession setLocalSessionID:]
+ -[KTIDSSession setPeerSessionID:]
+ -[KTVerifierResult supportConditionalEnforcement]
+ -[TransparencyDaemon networkKTPublicKeyBag:queryOptions:traceUUID:complete:]
+ -[TransparencySettings deviceUserAgent]
+ -[TransparencySettings optionalEnforcement]
+ GCC_except_table89
+ _OBJC_IVAR_$_KTIDSSession._localSessionID
+ _OBJC_IVAR_$_KTIDSSession._peerSessionID
+ _OUTLINED_FUNCTION_0
+ __PROTOCOLS__TtC12Transparency8KTRepair.14
+ ___38+[TransparencySettings sharedSettings]_block_invoke
+ ___40-[TransparencyDaemon ktRepair:complete:]_block_invoke.669
+ ___40-[TransparencyStaticKey listKTSessions:]_block_invoke.335
+ ___40-[TransparencyStaticKey listKTSessions:]_block_invoke_2.337
+ ___40-[TransparencyStaticKey listKTSessions:]_block_invoke_2.337.cold.1
+ ___46+[TransparencySettings jsonDictFromPlistDict:]_block_invoke.157
+ ___49-[TransparencyStaticKey setupKTSession:complete:]_block_invoke.319
+ ___49-[TransparencyStaticKey setupKTSession:complete:]_block_invoke_2.322
+ ___49-[TransparencyStaticKey setupKTSession:complete:]_block_invoke_2.322.cold.1
+ ___50-[TransparencyStaticKey deleteKTSession:complete:]_block_invoke.328
+ ___50-[TransparencyStaticKey deleteKTSession:complete:]_block_invoke_2.330
+ ___50-[TransparencyStaticKey deleteKTSession:complete:]_block_invoke_2.330.cold.1
+ ___51-[TransparencyStaticKey getKTSessionByID:complete:]_block_invoke.348
+ ___51-[TransparencyStaticKey getKTSessionByID:complete:]_block_invoke_2.350
+ ___51-[TransparencyStaticKey getKTSessionByID:complete:]_block_invoke_2.350.cold.1
+ ___55-[TransparencyStaticKey getKTSessionByHandle:complete:]_block_invoke.342
+ ___55-[TransparencyStaticKey getKTSessionByHandle:complete:]_block_invoke_2.343
+ ___55-[TransparencyStaticKey getKTSessionByHandle:complete:]_block_invoke_2.343.cold.1
+ ___60+[TransparencyStaticKey sasTTR:toHandle:pushToken:complete:]_block_invoke.355
+ ___60+[TransparencyStaticKey sasTTR:toHandle:pushToken:complete:]_block_invoke_2.356
+ ___60+[TransparencyStaticKey sasTTR:toHandle:pushToken:complete:]_block_invoke_2.356.cold.1
+ ___67-[TransparencyDaemon validateURIs:queryOptions:traceUUID:complete:]_block_invoke.676
+ ___68-[TransparencyDaemon networkKTQuery:application:traceUUID:complete:]_block_invoke.654
+ ___68-[TransparencyDaemon networkKTQuery:application:traceUUID:complete:]_block_invoke_2.656
+ ___70+[KTLoggableData loggableDataForDeviceID:application:completionBlock:]_block_invoke.135
+ ___70+[KTLoggableData loggableDataForDeviceID:application:completionBlock:]_block_invoke.139
+ ___70-[TransparencyDaemon ktQuery:application:queryOptions:trace:complete:]_block_invoke.663
+ ___74-[TransparencyDaemon validateIDSData:ktQueryData:ktResponseData:complete:]_block_invoke.673
+ ___76-[TransparencyDaemon networkKTPublicKeyBag:queryOptions:traceUUID:complete:]_block_invoke
+ ___76-[TransparencyDaemon networkKTPublicKeyBag:queryOptions:traceUUID:complete:]_block_invoke.649
+ ___76-[TransparencyDaemon networkKTPublicKeyBag:queryOptions:traceUUID:complete:]_block_invoke.cold.1
+ ___76-[TransparencyDaemon networkKTPublicKeyBag:queryOptions:traceUUID:complete:]_block_invoke_2
+ ___76-[TransparencyDaemon networkKTPublicKeyBag:queryOptions:traceUUID:complete:]_block_invoke_2.651
+ ___76-[TransparencyDaemon networkKTQuery:application:traceUUID:timeout:complete:]_block_invoke.659
+ ___76-[TransparencyDaemon networkKTQuery:application:traceUUID:timeout:complete:]_block_invoke_2.660
+ ___81-[TransparencyDaemon validateSelfForThisDeviceForApplication:pushToken:complete:]_block_invoke.666
+ ___block_descriptor_40_e8_32bs_e45_v32?0"NSData"8"NSDictionary"16"NSError"24ls32l8
+ ___block_literal_global.126
+ ___block_literal_global.144
+ ___block_literal_global.146
+ ___block_literal_global.324
+ ___block_literal_global.327
+ ___block_literal_global.332
+ ___block_literal_global.334
+ ___block_literal_global.339
+ ___block_literal_global.341
+ ___block_literal_global.345
+ ___block_literal_global.347
+ ___block_literal_global.352
+ ___block_literal_global.354
+ ___block_literal_global.358
+ ___block_literal_global.658
+ ___block_literal_global.662
+ ___block_literal_global.665
+ ___block_literal_global.668
+ ___block_literal_global.672
+ ___block_literal_global.675
+ ___block_literal_global.96
+ ___kCFBooleanTrue
+ ___swift_get_extra_inhabitant_index.13Tm
+ ___swift_store_extra_inhabitant_index.14Tm
+ _objc_msgSend$deviceUserAgent
+ _objc_msgSend$initWithData:encoding:
+ _objc_msgSend$initWithInteger:
+ _objc_msgSend$integerValue
+ _objc_msgSend$localSessionID
+ _objc_msgSend$longLongValue
+ _objc_msgSend$networkKTPublicKeyBag:queryOptions:traceUUID:complete:
+ _objc_msgSend$optionalEnforcement
+ _objc_msgSend$peerSessionID
+ _objc_msgSend$setLocalSessionID:
+ _objc_msgSend$setPeerSessionID:
+ _objc_msgSend$sharedSettings
+ _objc_retain_x28
+ _sharedConnectionLock
+ _sharedSettings.onceToken
+ _sharedSettings.shared
- GCC_except_table87
- __PROTOCOLS__TtC12Transparency8KTRepair.12
- ___40-[TransparencyDaemon ktRepair:complete:]_block_invoke.664
- ___40-[TransparencyStaticKey listKTSessions:]_block_invoke.319
- ___40-[TransparencyStaticKey listKTSessions:]_block_invoke_2.321
- ___40-[TransparencyStaticKey listKTSessions:]_block_invoke_2.321.cold.1
- ___46+[TransparencySettings jsonDictFromPlistDict:]_block_invoke.154
- ___49-[TransparencyStaticKey setupKTSession:complete:]_block_invoke.303
- ___49-[TransparencyStaticKey setupKTSession:complete:]_block_invoke_2.306
- ___49-[TransparencyStaticKey setupKTSession:complete:]_block_invoke_2.306.cold.1
- ___50-[TransparencyStaticKey deleteKTSession:complete:]_block_invoke.312
- ___50-[TransparencyStaticKey deleteKTSession:complete:]_block_invoke_2.314
- ___50-[TransparencyStaticKey deleteKTSession:complete:]_block_invoke_2.314.cold.1
- ___51-[TransparencyStaticKey getKTSessionByID:complete:]_block_invoke.332
- ___51-[TransparencyStaticKey getKTSessionByID:complete:]_block_invoke_2.334
- ___51-[TransparencyStaticKey getKTSessionByID:complete:]_block_invoke_2.334.cold.1
- ___55-[TransparencyStaticKey getKTSessionByHandle:complete:]_block_invoke.326
- ___55-[TransparencyStaticKey getKTSessionByHandle:complete:]_block_invoke_2.327
- ___55-[TransparencyStaticKey getKTSessionByHandle:complete:]_block_invoke_2.327.cold.1
- ___60+[TransparencyStaticKey sasTTR:toHandle:pushToken:complete:]_block_invoke.339
- ___60+[TransparencyStaticKey sasTTR:toHandle:pushToken:complete:]_block_invoke_2.340
- ___60+[TransparencyStaticKey sasTTR:toHandle:pushToken:complete:]_block_invoke_2.340.cold.1
- ___67-[TransparencyDaemon validateURIs:queryOptions:traceUUID:complete:]_block_invoke.671
- ___68-[TransparencyDaemon networkKTQuery:application:traceUUID:complete:]_block_invoke.649
- ___68-[TransparencyDaemon networkKTQuery:application:traceUUID:complete:]_block_invoke_2.651
- ___70+[KTLoggableData loggableDataForDeviceID:application:completionBlock:]_block_invoke.129
- ___70+[KTLoggableData loggableDataForDeviceID:application:completionBlock:]_block_invoke.133
- ___70-[TransparencyDaemon ktQuery:application:queryOptions:trace:complete:]_block_invoke.658
- ___74-[TransparencyDaemon validateIDSData:ktQueryData:ktResponseData:complete:]_block_invoke.668
- ___76-[TransparencyDaemon networkKTQuery:application:traceUUID:timeout:complete:]_block_invoke.654
- ___76-[TransparencyDaemon networkKTQuery:application:traceUUID:timeout:complete:]_block_invoke_2.655
- ___81-[TransparencyDaemon validateSelfForThisDeviceForApplication:pushToken:complete:]_block_invoke.661
- ___block_literal_global.123
- ___block_literal_global.132
- ___block_literal_global.134
- ___block_literal_global.143
- ___block_literal_global.148
- ___block_literal_global.302
- ___block_literal_global.308
- ___block_literal_global.311
- ___block_literal_global.323
- ___block_literal_global.325
- ___block_literal_global.329
- ___block_literal_global.331
- ___block_literal_global.336
- ___block_literal_global.338
- ___block_literal_global.342
- ___block_literal_global.657
- ___block_literal_global.660
- ___block_literal_global.663
- ___block_literal_global.667
- ___block_literal_global.670
- ___swift_get_extra_inhabitant_index.14Tm
- ___swift_store_extra_inhabitant_index.15Tm
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x9
- _sharedConectionLock
- _swift_bridgeObjectRelease_n
CStrings:
+ "    supportConditionalEnforcement:%d\n"
+ "CKVOptionalEnforcement"
+ "Sending networkKTPublicKeyBag:traceUUID:timeout:complete:"
+ "T@\"NSString\",&,V_localSessionID"
+ "T@\"NSString\",&,V_peerSessionID"
+ "_localSessionID"
+ "_peerSessionID"
+ "doSuppressMetrics:"
+ "initWithData:encoding:"
+ "kt-suppress-metric"
+ "localSessionID"
+ "networkKTPublicKeyBag:queryOptions:traceUUID:complete:"
+ "optionalEnforcement"
+ "peerSessionID"
+ "setLocalSessionID:"
+ "setPeerSessionID:"
+ "sharedSettings"
+ "v32@?0@\"NSData\"8@\"NSDictionary\"16@\"NSError\"24"
+ "v48@0:8@\"NSString\"16@\"KTQueryOptions\"24@\"NSString\"32@?<v@?@\"NSData\"@\"NSDictionary\"@\"NSError\">40"
- "KTEnforceErrors"

```
