## StatusKitAgentCore

> `/System/Library/PrivateFrameworks/StatusKitAgentCore.framework/StatusKitAgentCore`

```diff

-114.100.1.0.0
-  __TEXT.__text: 0xff6d4
+116.100.1.0.0
+  __TEXT.__text: 0xffc3c
   __TEXT.__auth_stubs: 0x1cf0
-  __TEXT.__objc_methlist: 0x7fec
+  __TEXT.__objc_methlist: 0x7ffc
   __TEXT.__const: 0x1d70
-  __TEXT.__cstring: 0x4e21
-  __TEXT.__oslogstring: 0x12e0f
-  __TEXT.__gcc_except_tab: 0x1194
+  __TEXT.__cstring: 0x4e91
+  __TEXT.__oslogstring: 0x12e6f
+  __TEXT.__gcc_except_tab: 0x1258
   __TEXT.__swift5_typeref: 0x163e
   __TEXT.__constg_swiftt: 0x6d0
   __TEXT.__swift5_reflstr: 0x617

   __TEXT.__swift5_types: 0x88
   __TEXT.__swift_as_entry: 0x224
   __TEXT.__swift_as_ret: 0x204
-  __TEXT.__unwind_info: 0x36e8
+  __TEXT.__unwind_info: 0x3728
   __TEXT.__eh_frame: 0x54f8
   __TEXT.__objc_classname: 0xed1
-  __TEXT.__objc_methname: 0x11c12
+  __TEXT.__objc_methname: 0x11c27
   __TEXT.__objc_methtype: 0x4a95
   __TEXT.__objc_stubs: 0x9be0
   __DATA_CONST.__got: 0x910
-  __DATA_CONST.__const: 0x1c90
+  __DATA_CONST.__const: 0x1cb8
   __DATA_CONST.__objc_classlist: 0x360
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x1c8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3508
+  __DATA_CONST.__objc_selrefs: 0x3510
   __DATA_CONST.__objc_protorefs: 0x88
   __DATA_CONST.__objc_superrefs: 0x258
   __DATA_CONST.__objc_arraydata: 0x18
   __AUTH_CONST.__auth_got: 0xe88
   __AUTH_CONST.__const: 0x30d0
   __AUTH_CONST.__cfstring: 0x24a0
-  __AUTH_CONST.__objc_const: 0xbcb0
+  __AUTH_CONST.__objc_const: 0xbcb8
   __AUTH_CONST.__objc_intobj: 0x108
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH.__objc_data: 0xb60
-  __AUTH.__data: 0x1e8
+  __AUTH.__objc_data: 0x938
+  __AUTH.__data: 0xe8
   __DATA.__objc_ivar: 0x620
-  __DATA.__data: 0x1600
-  __DATA.__bss: 0x1540
-  __DATA.__common: 0x10
-  __DATA_DIRTY.__objc_data: 0x1cb0
-  __DATA_DIRTY.__data: 0x920
-  __DATA_DIRTY.__bss: 0x750
-  __DATA_DIRTY.__common: 0x30
+  __DATA.__data: 0x1470
+  __DATA.__bss: 0x11c0
+  __DATA.__common: 0x8
+  __DATA_DIRTY.__objc_data: 0x1ed8
+  __DATA_DIRTY.__data: 0xb90
+  __DATA_DIRTY.__bss: 0xad0
+  __DATA_DIRTY.__common: 0x38
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/Combine.framework/Combine

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 6D3A4C19-636B-328D-9B12-1BEBA610322A
-  Functions: 4846
-  Symbols:   15605
-  CStrings:  4888
+  UUID: 7E6E2AFD-30D9-3B2D-A4AE-AD594983244E
+  Functions: 4851
+  Symbols:   15623
+  CStrings:  4893
 
Symbols:
+ +[SKAStatusEncryptionManager _decryptPayloadData:withIncomingRatchet:withRatchetIndex:signatureData:]
+ +[SKAStatusEncryptionManager _decryptPayloadData:withIncomingRatchet:withRatchetIndex:signatureData:].cold.1
+ +[SKAStatusEncryptionManager _decryptPayloadData:withIncomingRatchet:withRatchetIndex:signatureData:].cold.2
+ -[SKADatabaseManager _existingPresentDevicesForChannel:databaseContext:].cold.1
+ -[SKADatabaseManager saveContextIfNeeded:]
+ GCC_except_table103
+ GCC_except_table105
+ GCC_except_table107
+ GCC_except_table111
+ GCC_except_table117
+ GCC_except_table119
+ GCC_except_table124
+ GCC_except_table126
+ GCC_except_table128
+ GCC_except_table134
+ GCC_except_table139
+ GCC_except_table156
+ GCC_except_table158
+ GCC_except_table163
+ GCC_except_table165
+ GCC_except_table169
+ GCC_except_table193
+ GCC_except_table196
+ GCC_except_table198
+ GCC_except_table200
+ GCC_except_table89
+ GCC_except_table97
+ GCC_except_table99
+ ___101-[SKAPresenceManager _createPresenceChannelForPresenceIdentifier:options:databaseContext:completion:]_block_invoke.89
+ ___101-[SKAPresenceManager _createPresenceChannelForPresenceIdentifier:options:databaseContext:completion:]_block_invoke.89.cold.1
+ ___101-[SKAPresenceManager _createPresenceChannelForPresenceIdentifier:options:databaseContext:completion:]_block_invoke_2.91
+ ___107-[SKAPresenceManager _findOrCreatePresenceChannelForPresenceIdentifier:options:databaseContext:completion:]_block_invoke.88
+ ___107-[SKAPresenceManager _findOrCreatePresenceChannelForPresenceIdentifier:options:databaseContext:completion:]_block_invoke.88.cold.1
+ ___42-[SKADatabaseManager saveContextIfNeeded:]_block_invoke
+ ___63-[SKADatabaseManager presentDevicesForChannel:databaseContext:]_block_invoke
+ ___69-[SKADatabaseManager deleteAllPresenceAssertionsWithDatabaseContext:]_block_invoke
+ ___69-[SKADatabaseManager deleteAllPresenceAssertionsWithDatabaseContext:]_block_invoke.cold.1
+ ___69-[SKADatabaseManager deleteAllPresenceAssertionsWithDatabaseContext:]_block_invoke.cold.2
+ ___71-[SKADatabaseManager activePresenceAssertionsExistWithDatabaseContext:]_block_invoke
+ ___71-[SKADatabaseManager activePresenceAssertionsExistWithDatabaseContext:]_block_invoke.cold.1
+ ___72-[SKADatabaseManager deleteAllPresenceSubscriptionsWithDatabaseContext:]_block_invoke
+ ___72-[SKADatabaseManager deleteAllPresenceSubscriptionsWithDatabaseContext:]_block_invoke.cold.1
+ ___72-[SKADatabaseManager deleteAllPresenceSubscriptionsWithDatabaseContext:]_block_invoke.cold.2
+ ___96-[SKADatabaseManager existingPresenceAssertionForPresenceIdentifier:isPersonal:databaseContext:]_block_invoke
+ ___block_descriptor_56_e8_32s40bs48w_e40_v24?0"SKADatabaseChannel"8"NSError"16lw48l8s32l8s40l8
+ ___block_descriptor_56_e8_32s40s48r_e5_v8?0lr48l8s32l8s40l8
+ ___block_descriptor_80_e8_32s40s48s56s64bs72w_e40_v24?0"SKADatabaseChannel"8"NSError"16ls64l8s32l8s40l8s48l8s56l8w72l8
+ ___block_literal_global.121
+ _objc_msgSend$saveContextIfNeeded:
- -[SKADatabaseManager activePresenceAssertionsExistWithDatabaseContext:].cold.1
- -[SKADatabaseManager deleteAllPresenceAssertionsWithDatabaseContext:].cold.1
- -[SKADatabaseManager deleteAllPresenceAssertionsWithDatabaseContext:].cold.2
- -[SKADatabaseManager deleteAllPresenceSubscriptionsWithDatabaseContext:].cold.1
- -[SKADatabaseManager deleteAllPresenceSubscriptionsWithDatabaseContext:].cold.2
- -[SKAStatusEncryptionManager _decryptPayloadData:withIncomingRatchet:withRatchetIndex:signatureData:]
- -[SKAStatusEncryptionManager _decryptPayloadData:withIncomingRatchet:withRatchetIndex:signatureData:].cold.1
- -[SKAStatusEncryptionManager _decryptPayloadData:withIncomingRatchet:withRatchetIndex:signatureData:].cold.2
- GCC_except_table102
- GCC_except_table104
- GCC_except_table106
- GCC_except_table108
- GCC_except_table118
- GCC_except_table123
- GCC_except_table125
- GCC_except_table138
- GCC_except_table140
- GCC_except_table143
- GCC_except_table157
- GCC_except_table159
- GCC_except_table166
- GCC_except_table182
- GCC_except_table184
- GCC_except_table93
- GCC_except_table96
- GCC_except_table98
- ___101-[SKAPresenceManager _createPresenceChannelForPresenceIdentifier:options:databaseContext:completion:]_block_invoke.90.cold.1
- ___101-[SKAPresenceManager _createPresenceChannelForPresenceIdentifier:options:databaseContext:completion:]_block_invoke.91
- ___101-[SKAPresenceManager _createPresenceChannelForPresenceIdentifier:options:databaseContext:completion:]_block_invoke_2.92
- ___107-[SKAPresenceManager _findOrCreatePresenceChannelForPresenceIdentifier:options:databaseContext:completion:]_block_invoke.89
- ___107-[SKAPresenceManager _findOrCreatePresenceChannelForPresenceIdentifier:options:databaseContext:completion:]_block_invoke.89.cold.1
- ___49-[SKAPresenceManager recalculateActivityTracking]_block_invoke_2
- ___72-[SKADatabaseManager _existingPresentDevicesForChannel:databaseContext:]_block_invoke
- ___72-[SKADatabaseManager _existingPresentDevicesForChannel:databaseContext:]_block_invoke.cold.1
- ___block_descriptor_41_e8_32s_e5_v8?0ls32l8
- ___block_descriptor_48_e8_32s40bs_e40_v24?0"SKADatabaseChannel"8"NSError"16ls32l8s40l8
- ___block_literal_global.122
- _objc_msgSend$databaseAccountStatusChanged
CStrings:
+ "@\"SKAPresenceClient\""
+ "@\"SKAStatusPublishingServiceClient\""
+ "@\"SKAStatusSubscriptionServiceClient\""
+ "Not moving over to new channel for presence identifier %@. Old channel %@ is same as the new channel %@"
+ "saveContextIfNeeded:"

```
