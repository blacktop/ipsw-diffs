## KeychainCircle

> `/System/Library/PrivateFrameworks/KeychainCircle.framework/KeychainCircle`

```diff

-61901.0.33.0.2
-  __TEXT.__text: 0x28da0
+61901.0.46.502.1
+  __TEXT.__text: 0x28a80
   __TEXT.__auth_stubs: 0x1030
-  __TEXT.__objc_methlist: 0x1d64
+  __TEXT.__objc_methlist: 0x1ddc
   __TEXT.__const: 0xd8
-  __TEXT.__dlopen_cstrs: 0x1a8
-  __TEXT.__gcc_except_tab: 0x15d8
-  __TEXT.__cstring: 0x3290
-  __TEXT.__oslogstring: 0x38aa
+  __TEXT.__dlopen_cstrs: 0x104
+  __TEXT.__gcc_except_tab: 0x1598
+  __TEXT.__cstring: 0x3266
+  __TEXT.__oslogstring: 0x397e
   __TEXT.__ustring: 0x32
-  __TEXT.__unwind_info: 0x848
-  __TEXT.__objc_classname: 0x2e4
-  __TEXT.__objc_methname: 0x4146
-  __TEXT.__objc_methtype: 0xf55
-  __TEXT.__objc_stubs: 0x2f80
-  __DATA_CONST.__got: 0x2b8
+  __TEXT.__unwind_info: 0x808
+  __TEXT.__objc_classname: 0x2e6
+  __TEXT.__objc_methname: 0x4214
+  __TEXT.__objc_methtype: 0xf65
+  __TEXT.__objc_stubs: 0x3020
+  __DATA_CONST.__got: 0x2e8
   __DATA_CONST.__const: 0x1218
   __DATA_CONST.__objc_classlist: 0xa8
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1020
+  __DATA_CONST.__objc_selrefs: 0x1050
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x88
   __AUTH_CONST.__auth_got: 0x828
   __AUTH_CONST.__const: 0x1e0
-  __AUTH_CONST.__cfstring: 0x3660
-  __AUTH_CONST.__objc_const: 0x2af0
+  __AUTH_CONST.__cfstring: 0x36c0
+  __AUTH_CONST.__objc_const: 0x2bb0
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH.__objc_data: 0x5a0
-  __DATA.__objc_ivar: 0x1fc
+  __DATA.__objc_ivar: 0x20c
   __DATA.__data: 0x318
-  __DATA.__bss: 0x168
+  __DATA.__bss: 0x160
   __DATA_DIRTY.__objc_data: 0xf0
-  __DATA_DIRTY.__bss: 0x68
+  __DATA_DIRTY.__bss: 0x30
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/Security.framework/Security
+  - /System/Library/PrivateFrameworks/AAAFoundation.framework/AAAFoundation
   - /System/Library/PrivateFrameworks/AppleKeyStore.framework/AppleKeyStore
+  - /System/Library/PrivateFrameworks/AuthKit.framework/AuthKit
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8BA194EF-B630-3BFF-8919-47B6CBCC51D5
-  Functions: 777
-  Symbols:   2959
-  CStrings:  2099
+  UUID: 343DA7B1-693E-38D5-A06A-2A2D7BF5242E
+  Functions: 775
+  Symbols:   2956
+  CStrings:  2113
 
Symbols:
+ -[KCJoiningAcceptSession piggybacking_version_for_tests]
+ -[KCJoiningAcceptSession setPiggybackingVersion:]
+ -[KCJoiningAcceptSession setPiggybacking_version_for_tests:]
+ -[KCJoiningRequestCircleSession piggybacking_version_for_tests]
+ -[KCJoiningRequestCircleSession setPiggybackingVersion:]
+ -[KCJoiningRequestCircleSession setPiggybacking_version_for_tests:]
+ -[OTPairingMessage hasVersion]
+ -[OTPairingMessage setHasVersion:]
+ -[OTPairingMessage setVersion:]
+ -[OTPairingMessage version]
+ GCC_except_table381
+ GCC_except_table388
+ GCC_except_table522
+ GCC_except_table531
+ GCC_except_table533
+ _OBJC_CLASS_$_AAFAnalyticsEvent
+ _OBJC_CLASS_$_AAFAnalyticsReporter
+ _OBJC_CLASS_$_AAFAnalyticsTransportRTC
+ _OBJC_CLASS_$_AKAccountManager
+ _OBJC_IVAR_$_KCJoiningAcceptSession._piggybacking_version_for_tests
+ _OBJC_IVAR_$_KCJoiningRequestCircleSession._piggybacking_version_for_tests
+ _OBJC_IVAR_$_OTPairingMessage._has
+ _OBJC_IVAR_$_OTPairingMessage._version
+ ___Block_byref_object_copy_.372
+ ___Block_byref_object_copy_.899
+ ___Block_byref_object_dispose_.373
+ ___Block_byref_object_dispose_.900
+ ___block_descriptor_56_e8_32s40r48r_e74_v56?0"NSString"8"NSData"16"NSData"24"NSData"32"NSData"40"NSError"48lr40l8s32l8r48l8
+ ___block_descriptor_tmp.1468
+ ___block_descriptor_tmp.1532
+ ___block_descriptor_tmp.1574
+ ___block_descriptor_tmp.1611
+ ___block_descriptor_tmp.71.1526
+ ___block_literal_global.1125
+ ___block_literal_global.1431
+ ___block_literal_global.1496
+ ___block_literal_global.1572
+ ___block_literal_global.266
+ ___block_literal_global.32
+ ___block_literal_global.36
+ ___block_literal_global.413
+ _apply_block_1.1475
+ _apply_block_2.1506
+ _kAAFDeviceSessionId
+ _kAAFFlowId
+ _objc_msgSend$hasVersion
+ _objc_msgSend$piggybacking_version_for_tests
+ _objc_msgSend$setPiggybacking_version_for_tests:
+ _objc_msgSend$setVersion:
+ _objc_msgSend$version
- GCC_except_table375
- GCC_except_table382
- GCC_except_table512
- GCC_except_table521
- GCC_except_table523
- GCC_except_table554
- GCC_except_table584
- GCC_except_table587
- GCC_except_table590
- _AAAFoundationLibrary
- _AAAFoundationLibraryCore
- _AAAFoundationLibraryCore.frameworkLibrary
- _AuthKitLibraryCore
- _AuthKitLibraryCore.frameworkLibrary
- ___AAAFoundationLibraryCore_block_invoke
- ___AuthKitLibraryCore_block_invoke
- ___Block_byref_object_copy_.386
- ___Block_byref_object_copy_.912
- ___Block_byref_object_dispose_.387
- ___Block_byref_object_dispose_.913
- ___block_descriptor_48_e8_32r40r_e74_v56?0"NSString"8"NSData"16"NSData"24"NSData"32"NSData"40"NSError"48lr32l8r40l8
- ___block_descriptor_tmp.1484
- ___block_descriptor_tmp.1547
- ___block_descriptor_tmp.1585
- ___block_descriptor_tmp.1622
- ___block_descriptor_tmp.71.1541
- ___block_literal_global.1134
- ___block_literal_global.1447
- ___block_literal_global.1513
- ___block_literal_global.1583
- ___block_literal_global.260
- ___block_literal_global.31
- ___block_literal_global.34.1408
- ___block_literal_global.422
- ___getAAFAnalyticsEventClass_block_invoke
- ___getAAFAnalyticsReporterClass_block_invoke
- ___getAAFAnalyticsTransportRTCClass_block_invoke
- ___getAKAccountManagerClass_block_invoke
- ___getkAAFDeviceSessionIdSymbolLoc_block_invoke
- ___getkAAFFlowIdSymbolLoc_block_invoke
- _apply_block_1.1491
- _apply_block_2.1523
- _audit_stringAAAFoundation
- _audit_stringAuthKit
- _getAAFAnalyticsEventClass.softClass
- _getAAFAnalyticsReporterClass.softClass
- _getAAFAnalyticsTransportRTCClass.softClass
- _getAKAccountManagerClass.softClass
- _getkAAFDeviceSessionId
- _getkAAFDeviceSessionIdSymbolLoc.ptr
- _getkAAFFlowIdSymbolLoc.ptr
CStrings:
+ "TQ,N,V_piggybacking_version_for_tests"
+ "TQ,N,V_version"
+ "Unexpected piggybacking version"
+ "_piggybacking_version_for_tests"
+ "_version"
+ "aafanalyticsevent-security: failed to weaklink AAAFoundation"
+ "aafanalyticsevent-security: failed to weaklink AuthKit"
+ "failed to decrypt voucher packet, fall back to legacy path, error: %@"
+ "failed to encrypt the voucher"
+ "hasVersion"
+ "joining: failed to encrypt voucher payload: %@"
+ "joining: unexpected piggybacking version, received: %llu"
+ "piggy version is 0"
+ "piggy version is 3"
+ "piggybacking_version_for_tests"
+ "setHasVersion:"
+ "setPiggybacking_version_for_tests:"
+ "setVersion:"
+ "version"
+ "{?=\"version\"b1}"
- "AAFAnalyticsEvent"
- "AAFAnalyticsReporter"
- "AAFAnalyticsTransportRTC"
- "AKAccountManager"
- "aafanalyticsevent-security: failed to softlink AAAFoundation"
- "aafanalyticsevent-security: failed to softlink AuthKit"
- "kAAFDeviceSessionId"
- "kAAFFlowId"
- "softlink:o:path:/System/Library/PrivateFrameworks/AAAFoundation.framework/AAAFoundation"
- "softlink:o:path:/System/Library/PrivateFrameworks/AuthKit.framework/AuthKit"

```
