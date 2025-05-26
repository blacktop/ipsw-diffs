## CryptoTokenKit

> `/System/Library/Frameworks/CryptoTokenKit.framework/CryptoTokenKit`

```diff

-685.80.2.0.0
-  __TEXT.__text: 0x42ac4
-  __TEXT.__auth_stubs: 0xad0
-  __TEXT.__objc_methlist: 0x358c
-  __TEXT.__gcc_except_tab: 0x108c
+685.100.14.0.0
+  __TEXT.__text: 0x43240
+  __TEXT.__auth_stubs: 0xae0
+  __TEXT.__objc_methlist: 0x35ec
+  __TEXT.__gcc_except_tab: 0x10fc
   __TEXT.__const: 0x610
-  __TEXT.__cstring: 0x2971
-  __TEXT.__oslogstring: 0x2e43
+  __TEXT.__cstring: 0x29c6
+  __TEXT.__oslogstring: 0x2f36
   __TEXT.__dlopen_cstrs: 0x104
-  __TEXT.__unwind_info: 0x13e8
+  __TEXT.__unwind_info: 0x1430
   __TEXT.__objc_classname: 0xaad
-  __TEXT.__objc_methname: 0x7a4c
+  __TEXT.__objc_methname: 0x7bc4
   __TEXT.__objc_methtype: 0x1c23
-  __TEXT.__objc_stubs: 0x5cc0
-  __DATA_CONST.__got: 0x2e0
-  __DATA_CONST.__const: 0x1348
+  __TEXT.__objc_stubs: 0x5d60
+  __DATA_CONST.__got: 0x2e8
+  __DATA_CONST.__const: 0x13d8
   __DATA_CONST.__objc_classlist: 0x298
   __DATA_CONST.__objc_catlist: 0x0
   __DATA_CONST.__objc_protolist: 0x100
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x63c8
-  __DATA_CONST.__objc_selrefs: 0x1ce8
+  __DATA_CONST.__objc_const: 0x6478
+  __DATA_CONST.__objc_selrefs: 0x1d20
+  __DATA_CONST.__objc_protorefs: 0xa0
+  __DATA_CONST.__objc_classrefs: 0x350
+  __DATA_CONST.__objc_superrefs: 0x240
   __DATA_CONST.__objc_arraydata: 0x8
-  __AUTH_CONST.__cfstring: 0x2200
+  __AUTH_CONST.__cfstring: 0x2220
+  __AUTH_CONST.__const: 0x520
   __AUTH_CONST.__objc_const: 0x90
-  __AUTH_CONST.__const: 0x400
   __AUTH_CONST.__objc_intobj: 0x1c8
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_ptr: 0x10
-  __AUTH_CONST.__auth_got: 0x578
+  __AUTH_CONST.__auth_got: 0x580
   __AUTH.__objc_data: 0x50
-  __DATA.__objc_protorefs: 0xa0
-  __DATA.__objc_classrefs: 0x350
-  __DATA.__objc_superrefs: 0x240
-  __DATA.__objc_ivar: 0x500
-  __DATA.__data: 0xe10
-  __DATA.__bss: 0x110
-  __DATA_DIRTY.__const: 0x5c0
+  __DATA.__objc_ivar: 0x510
+  __DATA.__data: 0xe30
+  __DATA.__bss: 0xe0
+  __DATA_DIRTY.__const: 0x4e0
   __DATA_DIRTY.__objc_const: 0x2010
   __DATA_DIRTY.__objc_data: 0x19a0
-  __DATA_DIRTY.__bss: 0x2a8
+  __DATA_DIRTY.__bss: 0x2c0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1750
-  Symbols:   6260
-  CStrings:  2553
+  Functions: 1765
+  Symbols:   6310
+  CStrings:  2576
 
Symbols:
+ -[TKClientToken _testing_noAutomaticReconnect]
+ -[TKClientToken set_testing_noAutomaticReconnect:]
+ -[TKRemoteSEPKey remoteKeyID]
+ -[TKSharedResource invalidate]
+ -[TKSharedResourceSlot releaseResourceImmediatelly:]
+ -[TKSmartCardSlotEngine powerDownIdleTimeout]
+ -[TKSmartCardSlotEngine setPowerDownIdleTimeout:]
+ -[TKSmartCardSlotProxy processNotificationParameters:]
+ -[TKSmartCardSlotProxy slotInitialized]
+ GCC_except_table102
+ GCC_except_table121
+ GCC_except_table142
+ GCC_except_table145
+ GCC_except_table148
+ GCC_except_table34
+ GCC_except_table74
+ _OBJC_IVAR_$_TKClientToken.__testing_noAutomaticReconnect
+ _OBJC_IVAR_$_TKRemoteSEPKey._remoteKeyID
+ _OBJC_IVAR_$_TKSmartCardSlotEngine._powerDownIdleTimeout
+ _OBJC_IVAR_$_TKSmartCardSlotProxy._queuedParameters
+ ___32-[TKSmartCardSlot makeSmartCard]_block_invoke.125
+ ___34-[TKExtensionClientToken endpoint]_block_invoke.62
+ ___35-[TKRemoteSEPKey withError:invoke:]_block_invoke.92
+ ___35-[TKRemoteSEPKey withError:invoke:]_block_invoke.92.cold.1
+ ___35-[TKRemoteSEPKey withError:invoke:]_block_invoke.96
+ ___35-[TKRemoteSEPKey withError:invoke:]_block_invoke_2
+ ___35-[TKRemoteSEPKey withError:invoke:]_block_invoke_2.cold.1
+ ___35-[TKRemoteSEPKey withError:invoke:]_block_invoke_2.cold.2
+ ___37-[TKSmartCard querySessionWithReply:]_block_invoke.218
+ ___37-[TKSmartCard querySessionWithReply:]_block_invoke.221
+ ___37-[TKSmartCard querySessionWithReply:]_block_invoke.223
+ ___37-[TKSmartCard querySessionWithReply:]_block_invoke.228
+ ___37-[TKSmartCard querySessionWithReply:]_block_invoke_2.220
+ ___37-[TKSmartCard querySessionWithReply:]_block_invoke_2.220.cold.1
+ ___37-[TKSmartCard querySessionWithReply:]_block_invoke_2.222
+ ___37-[TKSmartCard querySessionWithReply:]_block_invoke_2.222.cold.1
+ ___37-[TKSmartCard querySessionWithReply:]_block_invoke_2.227
+ ___37-[TKSmartCard querySessionWithReply:]_block_invoke_2.227.cold.1
+ ___37-[TKSmartCard transmitRequest:reply:]_block_invoke.244
+ ___39-[TKSmartCard releaseSessionWithReply:]_block_invoke.211
+ ___39-[TKSmartCard releaseSessionWithReply:]_block_invoke_2.212
+ ___39-[TKSmartCard releaseSessionWithReply:]_block_invoke_3.213
+ ___40-[TKExtensionClientToken SEPKeyEndpoint]_block_invoke.72
+ ___41-[TKExtensionClientToken watcherEndpoint]_block_invoke.69
+ ___43-[TKSmartCard sendIns:p1:p2:data:le:reply:]_block_invoke.279
+ ___43-[TKSmartCardSessionEngine transmit:reply:]_block_invoke.390
+ ___43-[TKSmartCardSessionEngine transmit:reply:]_block_invoke.390.cold.1
+ ___43-[TKSmartCardSessionEngine transmit:reply:]_block_invoke.393
+ ___43-[TKSmartCardSessionEngine transmit:reply:]_block_invoke.393.cold.1
+ ___47-[TKExtensionClientToken configurationEndpoint]_block_invoke.66
+ ___52-[TKExtensionClientToken ensureConnectionWithError:]_block_invoke.73
+ ___52-[TKSharedResourceSlot releaseResourceImmediatelly:]_block_invoke
+ ___52-[TKSharedResourceSlot releaseResourceImmediatelly:]_block_invoke.cold.1
+ ___52-[TKSharedResourceSlot releaseResourceImmediatelly:]_block_invoke.cold.2
+ ___55-[TKSmartCardSlot connectToEndpoint:synchronous:reply:]_block_invoke.118
+ ___55-[TKSmartCardSlot connectToEndpoint:synchronous:reply:]_block_invoke.118.cold.1
+ ___55-[TKSmartCardSlot connectToEndpoint:synchronous:reply:]_block_invoke.119
+ ___55-[TKSmartCardSlot connectToEndpoint:synchronous:reply:]_block_invoke.119.cold.1
+ ___55-[TKSmartCardSlot connectToEndpoint:synchronous:reply:]_block_invoke.120
+ ___55-[TKSmartCardSlot connectToEndpoint:synchronous:reply:]_block_invoke.120.cold.1
+ ___block_descriptor_32_e25_v16?0"NSXPCConnection"8l
+ ___block_descriptor_32_e26_"NSXPCConnection"16?0^8l
+ ___block_descriptor_48_e8_32s40r_e17_v16?0"NSError"8lr40l8s32l8
+ ___block_descriptor_64_e8_32s40r48r56r_e45_v32?0"NSData"8"NSDictionary"16"NSError"24lr40l8r48l8s32l8r56l8
+ ___block_descriptor_89_e8_32s40s48s56s64s72r_e38_24?0"<TKRemoteSEPKeyProtocol>"8^16ls32l8s40l8s48l8s56l8s64l8r72l8
+ ___block_literal_global.124
+ ___block_literal_global.126
+ ___block_literal_global.128
+ ___block_literal_global.130
+ ___block_literal_global.134
+ ___block_literal_global.144
+ ___block_literal_global.146
+ ___block_literal_global.166
+ ___block_literal_global.194
+ ___block_literal_global.197
+ ___block_literal_global.215
+ ___block_literal_global.223
+ ___block_literal_global.226
+ ___block_literal_global.240
+ ___block_literal_global.252
+ ___block_literal_global.255
+ ___block_literal_global.257
+ ___block_literal_global.296
+ ___block_literal_global.389
+ ___block_literal_global.392
+ ___block_literal_global.395
+ ___block_literal_global.397
+ ___block_literal_global.425
+ ___block_literal_global.65
+ ___block_literal_global.68
+ ___block_literal_global.71
+ ___block_literal_global.810
+ ___block_literal_global.82
+ ___block_literal_global.85
+ _calloc
+ _kSecKeyAlgorithmEdDSASignatureMessageCurve448SHAKE256
+ _objc_msgSend$_testing_noAutomaticReconnect
+ _objc_msgSend$powerDownIdleTimeout
+ _objc_msgSend$processNotificationParameters:
+ _objc_msgSend$releaseResourceImmediatelly:
+ _objc_msgSend$remoteKeyID
+ _objc_msgSend$slotInitialized
+ _withError:invoke:.connectionSlot
- -[TKSharedResourceSlot releaseResource]
- GCC_except_table100
- GCC_except_table11
- GCC_except_table119
- GCC_except_table140
- GCC_except_table143
- GCC_except_table146
- GCC_except_table72
- ___32-[TKSmartCardSlot makeSmartCard]_block_invoke.120
- ___34-[TKExtensionClientToken endpoint]_block_invoke.61
- ___35-[TKRemoteSEPKey withError:invoke:]_block_invoke.84
- ___37-[TKSmartCard querySessionWithReply:]_block_invoke.214
- ___37-[TKSmartCard querySessionWithReply:]_block_invoke.217
- ___37-[TKSmartCard querySessionWithReply:]_block_invoke.219
- ___37-[TKSmartCard querySessionWithReply:]_block_invoke.224
- ___37-[TKSmartCard querySessionWithReply:]_block_invoke_2.216
- ___37-[TKSmartCard querySessionWithReply:]_block_invoke_2.216.cold.1
- ___37-[TKSmartCard querySessionWithReply:]_block_invoke_2.218
- ___37-[TKSmartCard querySessionWithReply:]_block_invoke_2.218.cold.1
- ___37-[TKSmartCard querySessionWithReply:]_block_invoke_2.223
- ___37-[TKSmartCard querySessionWithReply:]_block_invoke_2.223.cold.1
- ___37-[TKSmartCard transmitRequest:reply:]_block_invoke.240
- ___39-[TKSharedResourceSlot releaseResource]_block_invoke
- ___39-[TKSharedResourceSlot releaseResource]_block_invoke.cold.1
- ___39-[TKSharedResourceSlot releaseResource]_block_invoke.cold.2
- ___39-[TKSmartCard releaseSessionWithReply:]_block_invoke.207
- ___39-[TKSmartCard releaseSessionWithReply:]_block_invoke_2.208
- ___39-[TKSmartCard releaseSessionWithReply:]_block_invoke_3.209
- ___40-[TKExtensionClientToken SEPKeyEndpoint]_block_invoke.71
- ___41-[TKExtensionClientToken watcherEndpoint]_block_invoke.68
- ___43-[TKSmartCard sendIns:p1:p2:data:le:reply:]_block_invoke.275
- ___43-[TKSmartCardSessionEngine transmit:reply:]_block_invoke.381
- ___43-[TKSmartCardSessionEngine transmit:reply:]_block_invoke.381.cold.1
- ___43-[TKSmartCardSessionEngine transmit:reply:]_block_invoke.384
- ___43-[TKSmartCardSessionEngine transmit:reply:]_block_invoke.384.cold.1
- ___47-[TKExtensionClientToken configurationEndpoint]_block_invoke.65
- ___52-[TKExtensionClientToken ensureConnectionWithError:]_block_invoke.72
- ___55-[TKSmartCardSlot connectToEndpoint:synchronous:reply:]_block_invoke.113
- ___55-[TKSmartCardSlot connectToEndpoint:synchronous:reply:]_block_invoke.113.cold.1
- ___55-[TKSmartCardSlot connectToEndpoint:synchronous:reply:]_block_invoke.114
- ___55-[TKSmartCardSlot connectToEndpoint:synchronous:reply:]_block_invoke.114.cold.1
- ___55-[TKSmartCardSlot connectToEndpoint:synchronous:reply:]_block_invoke.115
- ___55-[TKSmartCardSlot connectToEndpoint:synchronous:reply:]_block_invoke.115.cold.1
- ___block_descriptor_81_e8_32s40s48s56s64r_e38_24?0"<TKRemoteSEPKeyProtocol>"8^16ls32l8s40l8s48l8s56l8r64l8
- ___block_literal_global.119
- ___block_literal_global.123
- ___block_literal_global.125
- ___block_literal_global.133
- ___block_literal_global.143
- ___block_literal_global.145
- ___block_literal_global.193
- ___block_literal_global.198
- ___block_literal_global.211
- ___block_literal_global.222
- ___block_literal_global.235
- ___block_literal_global.248
- ___block_literal_global.251
- ___block_literal_global.253
- ___block_literal_global.254
- ___block_literal_global.295
- ___block_literal_global.380
- ___block_literal_global.383
- ___block_literal_global.386
- ___block_literal_global.388
- ___block_literal_global.416
- ___block_literal_global.64
- ___block_literal_global.67
- ___block_literal_global.70
- ___block_literal_global.806
- ___block_literal_global.81
- ___block_literal_global.94
- _objc_msgSend$releaseResource
CStrings:
+ "\x01\"\x12"
+ "%@: processing accumulated state changes, %d remain"
+ "@\"NSXPCConnection\"16@?0^@8"
+ "A\x19\"\x13"
+ "T@\"NSData\",R,N,V_remoteKeyID"
+ "T@\"NSString\",?,R,C"
+ "TB,N,V__testing_noAutomaticReconnect"
+ "TKRemoteSEPKey-serverConnection"
+ "Td,V_powerDownIdleTimeout"
+ "__testing_noAutomaticReconnect"
+ "_powerDownIdleTimeout"
+ "_queuedParameters"
+ "_remoteKeyID"
+ "_testing_noAutomaticReconnect"
+ "creating rsepkey xpc connection"
+ "failed to call remotesepkey repeatedly, giving up, error: %{public}@"
+ "failed to call remotesepkey, try %d, error %{public}@"
+ "invalidating rsepkey xpc connection"
+ "powerDownIdleTimeout"
+ "processNotificationParameters:"
+ "releaseResourceImmediatelly:"
+ "remoteKeyID"
+ "setPowerDownIdleTimeout:"
+ "set_testing_noAutomaticReconnect:"
+ "slotInitialized"
+ "v16@?0@\"NSXPCConnection\"8"
+ "\xf0A1"
- "\x01\"\x11"
- "A\x19\x12\x13"
- "releaseResource"
- "\xf011"

```
