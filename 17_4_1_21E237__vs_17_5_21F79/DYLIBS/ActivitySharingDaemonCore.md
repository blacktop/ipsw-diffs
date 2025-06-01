## ActivitySharingDaemonCore

> `/System/Library/PrivateFrameworks/ActivitySharingDaemonCore.framework/ActivitySharingDaemonCore`

```diff

-752.6.0.0.0
-  __TEXT.__text: 0x6e874
+752.7.0.0.0
+  __TEXT.__text: 0x6ea6c
   __TEXT.__auth_stubs: 0xe90
-  __TEXT.__objc_methlist: 0x34f0
+  __TEXT.__objc_methlist: 0x3508
   __TEXT.__const: 0x128
-  __TEXT.__cstring: 0x2a6e
+  __TEXT.__cstring: 0x2a8a
   __TEXT.__gcc_except_tab: 0xad8
   __TEXT.__oslogstring: 0xd49b
-  __TEXT.__unwind_info: 0x1828
+  __TEXT.__unwind_info: 0x183c
   __TEXT.__objc_classname: 0xa00
-  __TEXT.__objc_methname: 0xf017
-  __TEXT.__objc_methtype: 0x28d6
-  __TEXT.__objc_stubs: 0xb180
-  __DATA_CONST.__got: 0x388
-  __DATA_CONST.__const: 0x34a0
+  __TEXT.__objc_methname: 0xf117
+  __TEXT.__objc_methtype: 0x2922
+  __TEXT.__objc_stubs: 0xb1e0
+  __DATA_CONST.__got: 0x390
+  __DATA_CONST.__const: 0x34a8
   __DATA_CONST.__objc_classlist: 0x1b8
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x138
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xdbf0
-  __DATA_CONST.__objc_selrefs: 0x2f90
+  __DATA_CONST.__objc_const: 0xdc20
+  __DATA_CONST.__objc_selrefs: 0x2fa8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_classrefs: 0x5e0
   __DATA_CONST.__objc_superrefs: 0x130
   __DATA_CONST.__objc_arraydata: 0xe8
-  __AUTH_CONST.__cfstring: 0x1b40
+  __AUTH_CONST.__cfstring: 0x1b60
   __AUTH_CONST.__const: 0xa40
   __AUTH_CONST.__objc_intobj: 0x150
   __AUTH_CONST.__objc_const: 0x1398

   __AUTH_CONST.__objc_doubleobj: 0x80
   __AUTH_CONST.__auth_got: 0x758
   __AUTH.__objc_data: 0x5a0
-  __DATA.__objc_ivar: 0x564
-  __DATA.__data: 0xea0
-  __DATA.__bss: 0xa0
+  __DATA.__objc_ivar: 0x568
+  __DATA.__data: 0xec0
+  __DATA.__bss: 0x80
   __DATA_DIRTY.__objc_data: 0xb90
   __DATA_DIRTY.__bss: 0x28
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6F78BCC4-ADAD-39C6-8118-D6FC2D1CF836
-  Functions: 2121
-  Symbols:   7930
-  CStrings:  3833
+  UUID: B8FF46E1-6BE4-32A7-98F0-3B3CAE9D394D
+  Functions: 2123
+  Symbols:   7940
+  CStrings:  3841
 
Symbols:
+ -[ASIDSMessageCenter _handleFinalizeHandshake:fromSenderAddress:receiverAddress:messageHandledCompletion:]
+ -[ASIDSMessageCenter _handleInviteRequest:fromSenderAddress:receiverAddress:messageHandledCompletion:]
+ -[ASIDSMessageCenter _handleInviteResponse:fromSenderAddress:receiverAddress:messageHandledCompletion:]
+ -[ASIDSMessageCenter _handleWithdrawInviteRequest:fromSenderAddress:receiverAddress:messageHandledCompletion:]
+ -[ASIDSMessageCenter _sendMessage:type:destinations:fromAddress:completion:]
+ -[ASIDSMessageCenter _sendPayload:type:destinations:fromAddress:completion:]
+ -[ASIDSMessageCenter sendInviteResponse:toDestinations:fromAddress:completion:]
+ -[ASMessage receiverAddress]
+ -[ASMessage setReceiverAddress:]
+ -[ASRelationshipManager messageCenter:didReceiveFinalizeHandshake:fromSenderAddress:receiverAddress:messageHandledCompletion:]
+ -[ASRelationshipManager messageCenter:didReceiveInviteRequest:fromSenderAddress:receiverAddress:messageHandledCompletion:]
+ -[ASRelationshipManager messageCenter:didReceiveInviteResponse:fromSenderAddress:receiverAddress:messageHandledCompletion:]
+ -[ASRelationshipManager messageCenter:didReceiveWithdrawInviteRequest:fromSenderAddress:receiverAddress:messageHandledCompletion:]
+ _ASMessageReceiverAddressKey
+ _IDSSendMessageOptionFromIDKey
+ _OBJC_IVAR_$_ASMessage._receiverAddress
+ ___122-[ASRelationshipManager messageCenter:didReceiveInviteRequest:fromSenderAddress:receiverAddress:messageHandledCompletion:]_block_invoke
+ ___122-[ASRelationshipManager messageCenter:didReceiveInviteRequest:fromSenderAddress:receiverAddress:messageHandledCompletion:]_block_invoke.322
+ ___122-[ASRelationshipManager messageCenter:didReceiveInviteRequest:fromSenderAddress:receiverAddress:messageHandledCompletion:]_block_invoke.325
+ ___122-[ASRelationshipManager messageCenter:didReceiveInviteRequest:fromSenderAddress:receiverAddress:messageHandledCompletion:]_block_invoke.326
+ ___122-[ASRelationshipManager messageCenter:didReceiveInviteRequest:fromSenderAddress:receiverAddress:messageHandledCompletion:]_block_invoke.cold.1
+ ___122-[ASRelationshipManager messageCenter:didReceiveInviteRequest:fromSenderAddress:receiverAddress:messageHandledCompletion:]_block_invoke_2
+ ___122-[ASRelationshipManager messageCenter:didReceiveInviteRequest:fromSenderAddress:receiverAddress:messageHandledCompletion:]_block_invoke_3
+ ___122-[ASRelationshipManager messageCenter:didReceiveInviteRequest:fromSenderAddress:receiverAddress:messageHandledCompletion:]_block_invoke_3.cold.1
+ ___123-[ASRelationshipManager messageCenter:didReceiveInviteResponse:fromSenderAddress:receiverAddress:messageHandledCompletion:]_block_invoke
+ ___123-[ASRelationshipManager messageCenter:didReceiveInviteResponse:fromSenderAddress:receiverAddress:messageHandledCompletion:]_block_invoke.328
+ ___123-[ASRelationshipManager messageCenter:didReceiveInviteResponse:fromSenderAddress:receiverAddress:messageHandledCompletion:]_block_invoke.331
+ ___123-[ASRelationshipManager messageCenter:didReceiveInviteResponse:fromSenderAddress:receiverAddress:messageHandledCompletion:]_block_invoke_2
+ ___123-[ASRelationshipManager messageCenter:didReceiveInviteResponse:fromSenderAddress:receiverAddress:messageHandledCompletion:]_block_invoke_2.329
+ ___123-[ASRelationshipManager messageCenter:didReceiveInviteResponse:fromSenderAddress:receiverAddress:messageHandledCompletion:]_block_invoke_2.cold.1
+ ___123-[ASRelationshipManager messageCenter:didReceiveInviteResponse:fromSenderAddress:receiverAddress:messageHandledCompletion:]_block_invoke_2.cold.2
+ ___123-[ASRelationshipManager messageCenter:didReceiveInviteResponse:fromSenderAddress:receiverAddress:messageHandledCompletion:]_block_invoke_2.cold.3
+ ___123-[ASRelationshipManager messageCenter:didReceiveInviteResponse:fromSenderAddress:receiverAddress:messageHandledCompletion:]_block_invoke_3
+ ___123-[ASRelationshipManager messageCenter:didReceiveInviteResponse:fromSenderAddress:receiverAddress:messageHandledCompletion:]_block_invoke_4
+ ___126-[ASRelationshipManager messageCenter:didReceiveFinalizeHandshake:fromSenderAddress:receiverAddress:messageHandledCompletion:]_block_invoke
+ ___126-[ASRelationshipManager messageCenter:didReceiveFinalizeHandshake:fromSenderAddress:receiverAddress:messageHandledCompletion:]_block_invoke.332
+ ___126-[ASRelationshipManager messageCenter:didReceiveFinalizeHandshake:fromSenderAddress:receiverAddress:messageHandledCompletion:]_block_invoke.cold.1
+ ___126-[ASRelationshipManager messageCenter:didReceiveFinalizeHandshake:fromSenderAddress:receiverAddress:messageHandledCompletion:]_block_invoke.cold.2
+ ___126-[ASRelationshipManager messageCenter:didReceiveFinalizeHandshake:fromSenderAddress:receiverAddress:messageHandledCompletion:]_block_invoke_2
+ ___130-[ASRelationshipManager messageCenter:didReceiveWithdrawInviteRequest:fromSenderAddress:receiverAddress:messageHandledCompletion:]_block_invoke
+ ___130-[ASRelationshipManager messageCenter:didReceiveWithdrawInviteRequest:fromSenderAddress:receiverAddress:messageHandledCompletion:]_block_invoke.333
+ ___130-[ASRelationshipManager messageCenter:didReceiveWithdrawInviteRequest:fromSenderAddress:receiverAddress:messageHandledCompletion:]_block_invoke_2
+ ___76-[ASIDSMessageCenter _sendPayload:type:destinations:fromAddress:completion:]_block_invoke
+ ___76-[ASIDSMessageCenter _sendPayload:type:destinations:fromAddress:completion:]_block_invoke.81
+ ___76-[ASIDSMessageCenter _sendPayload:type:destinations:fromAddress:completion:]_block_invoke.cold.1
+ ___block_descriptor_76_e8_32s40s48s56s64bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_80_e8_32s40s48s56s64s72bs_e26_v28?0B8B12B16"NSError"20ls72l8s32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_80_e8_32s40s48s56s64s72bs_e5_v8?0ls32l8s72l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_88_e8_32s40s48s56s64s72s80bs_e14_v16?0?<v?>8ls32l8s40l8s48l8s80l8s56l8s64l8s72l8
+ _objc_msgSend$_sendMessage:type:destinations:fromAddress:completion:
+ _objc_msgSend$_sendPayload:type:destinations:fromAddress:completion:
+ _objc_msgSend$messageCenter:didReceiveFinalizeHandshake:fromSenderAddress:receiverAddress:messageHandledCompletion:
+ _objc_msgSend$messageCenter:didReceiveInviteRequest:fromSenderAddress:receiverAddress:messageHandledCompletion:
+ _objc_msgSend$messageCenter:didReceiveInviteResponse:fromSenderAddress:receiverAddress:messageHandledCompletion:
+ _objc_msgSend$messageCenter:didReceiveWithdrawInviteRequest:fromSenderAddress:receiverAddress:messageHandledCompletion:
+ _objc_msgSend$receiverAddress
+ _objc_msgSend$sendInviteResponse:toDestinations:fromAddress:completion:
+ _objc_msgSend$setReceiverAddress:
+ _objc_msgSend$toID
- -[ASIDSMessageCenter _handleFinalizeHandshake:fromSenderAddress:messageHandledCompletion:]
- -[ASIDSMessageCenter _handleInviteRequest:fromSenderAddress:messageHandledCompletion:]
- -[ASIDSMessageCenter _handleInviteResponse:fromSenderAddress:messageHandledCompletion:]
- -[ASIDSMessageCenter _handleWithdrawInviteRequest:fromSenderAddress:messageHandledCompletion:]
- -[ASIDSMessageCenter _sendMessage:type:destinations:completion:]
- -[ASIDSMessageCenter _sendPayload:type:destinations:completion:]
- -[ASIDSMessageCenter sendInviteResponse:toDestinations:completion:]
- -[ASRelationshipManager messageCenter:didReceiveFinalizeHandshake:fromSenderAddress:messageHandledCompletion:]
- -[ASRelationshipManager messageCenter:didReceiveInviteRequest:fromSenderAddress:messageHandledCompletion:]
- -[ASRelationshipManager messageCenter:didReceiveInviteResponse:fromSenderAddress:messageHandledCompletion:]
- -[ASRelationshipManager messageCenter:didReceiveWithdrawInviteRequest:fromSenderAddress:messageHandledCompletion:]
- ___106-[ASRelationshipManager messageCenter:didReceiveInviteRequest:fromSenderAddress:messageHandledCompletion:]_block_invoke
- ___106-[ASRelationshipManager messageCenter:didReceiveInviteRequest:fromSenderAddress:messageHandledCompletion:]_block_invoke.322
- ___106-[ASRelationshipManager messageCenter:didReceiveInviteRequest:fromSenderAddress:messageHandledCompletion:]_block_invoke.325
- ___106-[ASRelationshipManager messageCenter:didReceiveInviteRequest:fromSenderAddress:messageHandledCompletion:]_block_invoke.326
- ___106-[ASRelationshipManager messageCenter:didReceiveInviteRequest:fromSenderAddress:messageHandledCompletion:]_block_invoke.cold.1
- ___106-[ASRelationshipManager messageCenter:didReceiveInviteRequest:fromSenderAddress:messageHandledCompletion:]_block_invoke_2
- ___106-[ASRelationshipManager messageCenter:didReceiveInviteRequest:fromSenderAddress:messageHandledCompletion:]_block_invoke_3
- ___106-[ASRelationshipManager messageCenter:didReceiveInviteRequest:fromSenderAddress:messageHandledCompletion:]_block_invoke_3.cold.1
- ___107-[ASRelationshipManager messageCenter:didReceiveInviteResponse:fromSenderAddress:messageHandledCompletion:]_block_invoke
- ___107-[ASRelationshipManager messageCenter:didReceiveInviteResponse:fromSenderAddress:messageHandledCompletion:]_block_invoke.328
- ___107-[ASRelationshipManager messageCenter:didReceiveInviteResponse:fromSenderAddress:messageHandledCompletion:]_block_invoke.331
- ___107-[ASRelationshipManager messageCenter:didReceiveInviteResponse:fromSenderAddress:messageHandledCompletion:]_block_invoke_2
- ___107-[ASRelationshipManager messageCenter:didReceiveInviteResponse:fromSenderAddress:messageHandledCompletion:]_block_invoke_2.329
- ___107-[ASRelationshipManager messageCenter:didReceiveInviteResponse:fromSenderAddress:messageHandledCompletion:]_block_invoke_2.cold.1
- ___107-[ASRelationshipManager messageCenter:didReceiveInviteResponse:fromSenderAddress:messageHandledCompletion:]_block_invoke_2.cold.2
- ___107-[ASRelationshipManager messageCenter:didReceiveInviteResponse:fromSenderAddress:messageHandledCompletion:]_block_invoke_2.cold.3
- ___107-[ASRelationshipManager messageCenter:didReceiveInviteResponse:fromSenderAddress:messageHandledCompletion:]_block_invoke_3
- ___107-[ASRelationshipManager messageCenter:didReceiveInviteResponse:fromSenderAddress:messageHandledCompletion:]_block_invoke_4
- ___110-[ASRelationshipManager messageCenter:didReceiveFinalizeHandshake:fromSenderAddress:messageHandledCompletion:]_block_invoke
- ___110-[ASRelationshipManager messageCenter:didReceiveFinalizeHandshake:fromSenderAddress:messageHandledCompletion:]_block_invoke.332
- ___110-[ASRelationshipManager messageCenter:didReceiveFinalizeHandshake:fromSenderAddress:messageHandledCompletion:]_block_invoke.cold.1
- ___110-[ASRelationshipManager messageCenter:didReceiveFinalizeHandshake:fromSenderAddress:messageHandledCompletion:]_block_invoke.cold.2
- ___110-[ASRelationshipManager messageCenter:didReceiveFinalizeHandshake:fromSenderAddress:messageHandledCompletion:]_block_invoke_2
- ___114-[ASRelationshipManager messageCenter:didReceiveWithdrawInviteRequest:fromSenderAddress:messageHandledCompletion:]_block_invoke
- ___114-[ASRelationshipManager messageCenter:didReceiveWithdrawInviteRequest:fromSenderAddress:messageHandledCompletion:]_block_invoke.333
- ___114-[ASRelationshipManager messageCenter:didReceiveWithdrawInviteRequest:fromSenderAddress:messageHandledCompletion:]_block_invoke_2
- ___64-[ASIDSMessageCenter _sendPayload:type:destinations:completion:]_block_invoke
- ___64-[ASIDSMessageCenter _sendPayload:type:destinations:completion:]_block_invoke.81
- ___64-[ASIDSMessageCenter _sendPayload:type:destinations:completion:]_block_invoke.cold.1
- ___block_descriptor_68_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s48l8s56l8
- ___block_descriptor_72_e8_32s40s48s56s64bs_e26_v28?0B8B12B16"NSError"20ls64l8s32l8s40l8s48l8s56l8
- ___block_descriptor_72_e8_32s40s48s56s64bs_e5_v8?0ls32l8s64l8s40l8s48l8s56l8
- ___block_descriptor_80_e8_32s40s48s56s64s72bs_e14_v16?0?<v?>8ls32l8s40l8s48l8s72l8s56l8s64l8
- _objc_msgSend$_sendMessage:type:destinations:completion:
- _objc_msgSend$_sendPayload:type:destinations:completion:
- _objc_msgSend$messageCenter:didReceiveFinalizeHandshake:fromSenderAddress:messageHandledCompletion:
- _objc_msgSend$messageCenter:didReceiveInviteRequest:fromSenderAddress:messageHandledCompletion:
- _objc_msgSend$messageCenter:didReceiveInviteResponse:fromSenderAddress:messageHandledCompletion:
- _objc_msgSend$messageCenter:didReceiveWithdrawInviteRequest:fromSenderAddress:messageHandledCompletion:
- _objc_msgSend$sendInviteResponse:toDestinations:completion:
CStrings:
+ "\x11\x13"
+ "ASMessageReceiverAddressKey"
+ "T@\"NSString\",C,N,V_receiverAddress"
+ "_handleFinalizeHandshake:fromSenderAddress:receiverAddress:messageHandledCompletion:"
+ "_handleInviteRequest:fromSenderAddress:receiverAddress:messageHandledCompletion:"
+ "_handleInviteResponse:fromSenderAddress:receiverAddress:messageHandledCompletion:"
+ "_handleWithdrawInviteRequest:fromSenderAddress:receiverAddress:messageHandledCompletion:"
+ "_receiverAddress"
+ "_sendMessage:type:destinations:fromAddress:completion:"
+ "_sendPayload:type:destinations:fromAddress:completion:"
+ "messageCenter:didReceiveFinalizeHandshake:fromSenderAddress:receiverAddress:messageHandledCompletion:"
+ "messageCenter:didReceiveInviteRequest:fromSenderAddress:receiverAddress:messageHandledCompletion:"
+ "messageCenter:didReceiveInviteResponse:fromSenderAddress:receiverAddress:messageHandledCompletion:"
+ "messageCenter:didReceiveWithdrawInviteRequest:fromSenderAddress:receiverAddress:messageHandledCompletion:"
+ "receiverAddress"
+ "sendInviteResponse:toDestinations:fromAddress:completion:"
+ "setReceiverAddress:"
+ "toID"
+ "v52@0:8@16i24@28@36@?44"
+ "v56@0:8@\"ASIDSMessageCenter\"16@\"ASCodableFinalizeHandshake\"24@\"NSString\"32@\"NSString\"40@?<v@?q>48"
+ "v56@0:8@\"ASIDSMessageCenter\"16@\"ASCodableInviteRequest\"24@\"NSString\"32@\"NSString\"40@?<v@?q>48"
+ "v56@0:8@\"ASIDSMessageCenter\"16@\"ASCodableInviteResponse\"24@\"NSString\"32@\"NSString\"40@?<v@?q>48"
+ "v56@0:8@\"ASIDSMessageCenter\"16@\"ASCodableWithdrawInviteRequest\"24@\"NSString\"32@\"NSString\"40@?<v@?q>48"
- "\x11\x12"
- "_handleFinalizeHandshake:fromSenderAddress:messageHandledCompletion:"
- "_handleInviteRequest:fromSenderAddress:messageHandledCompletion:"
- "_handleInviteResponse:fromSenderAddress:messageHandledCompletion:"
- "_handleWithdrawInviteRequest:fromSenderAddress:messageHandledCompletion:"
- "_sendMessage:type:destinations:completion:"
- "_sendPayload:type:destinations:completion:"
- "messageCenter:didReceiveFinalizeHandshake:fromSenderAddress:messageHandledCompletion:"
- "messageCenter:didReceiveInviteRequest:fromSenderAddress:messageHandledCompletion:"
- "messageCenter:didReceiveInviteResponse:fromSenderAddress:messageHandledCompletion:"
- "messageCenter:didReceiveWithdrawInviteRequest:fromSenderAddress:messageHandledCompletion:"
- "sendInviteResponse:toDestinations:completion:"
- "v48@0:8@\"ASIDSMessageCenter\"16@\"ASCodableFinalizeHandshake\"24@\"NSString\"32@?<v@?q>40"
- "v48@0:8@\"ASIDSMessageCenter\"16@\"ASCodableInviteRequest\"24@\"NSString\"32@?<v@?q>40"
- "v48@0:8@\"ASIDSMessageCenter\"16@\"ASCodableInviteResponse\"24@\"NSString\"32@?<v@?q>40"
- "v48@0:8@\"ASIDSMessageCenter\"16@\"ASCodableWithdrawInviteRequest\"24@\"NSString\"32@?<v@?q>40"

```
