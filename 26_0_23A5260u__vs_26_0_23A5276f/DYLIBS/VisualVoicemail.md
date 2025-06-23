## VisualVoicemail

> `/System/Library/PrivateFrameworks/VisualVoicemail.framework/VisualVoicemail`

```diff

-897.0.0.0.0
-  __TEXT.__text: 0x19d20
+898.0.0.0.0
+  __TEXT.__text: 0x1a0f4
   __TEXT.__auth_stubs: 0x640
-  __TEXT.__objc_methlist: 0x1ea0
-  __TEXT.__cstring: 0xf62
-  __TEXT.__gcc_except_tab: 0x500
+  __TEXT.__objc_methlist: 0x1ee8
+  __TEXT.__cstring: 0xf69
+  __TEXT.__gcc_except_tab: 0x510
   __TEXT.__const: 0x78
-  __TEXT.__oslogstring: 0x1f72
-  __TEXT.__unwind_info: 0x818
+  __TEXT.__oslogstring: 0x2030
+  __TEXT.__unwind_info: 0x838
   __TEXT.__objc_classname: 0x2c3
-  __TEXT.__objc_methname: 0x45a6
-  __TEXT.__objc_methtype: 0xb45
-  __TEXT.__objc_stubs: 0x3160
+  __TEXT.__objc_methname: 0x4676
+  __TEXT.__objc_methtype: 0xb9a
+  __TEXT.__objc_stubs: 0x31c0
   __DATA_CONST.__got: 0x238
-  __DATA_CONST.__const: 0x9d0
+  __DATA_CONST.__const: 0x9f8
   __DATA_CONST.__objc_classlist: 0xa0
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1270
+  __DATA_CONST.__objc_selrefs: 0x12b0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x80
   __DATA_CONST.__objc_arraydata: 0x400
   __AUTH_CONST.__auth_got: 0x330
-  __AUTH_CONST.__const: 0x240
-  __AUTH_CONST.__cfstring: 0x1400
-  __AUTH_CONST.__objc_const: 0x3b68
+  __AUTH_CONST.__const: 0x200
+  __AUTH_CONST.__cfstring: 0x1440
+  __AUTH_CONST.__objc_const: 0x3bb8
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0x180

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: DB459BD1-75F7-3278-AC7A-896696C97754
-  Functions: 740
-  Symbols:   2662
-  CStrings:  1506
+  UUID: CFEFCD2E-4EC3-3C9A-9823-6E1C2FA3A9B4
+  Functions: 743
+  Symbols:   2671
+  CStrings:  1521
 
Symbols:
+ -[VMVoicemailManager setProgressFractionCompleted:]
+ -[VMVoicemailManager setProgressTotalUnitCount:]
+ -[VMVoicemailManager setTranscribing:fractionCompleted:totalUnitCount:]
+ -[VMVoicemailManager setTranscriptionProgress:]
+ GCC_except_table120
+ GCC_except_table130
+ GCC_except_table136
+ GCC_except_table139
+ GCC_except_table144
+ GCC_except_table147
+ GCC_except_table152
+ GCC_except_table157
+ GCC_except_table160
+ GCC_except_table163
+ GCC_except_table166
+ GCC_except_table169
+ GCC_except_table172
+ GCC_except_table182
+ GCC_except_table185
+ GCC_except_table196
+ GCC_except_table202
+ GCC_except_table208
+ GCC_except_table211
+ GCC_except_table214
+ ___35-[VMClientWrapper clientConnection]_block_invoke.194.cold.1
+ ___35-[VMClientWrapper clientConnection]_block_invoke.197
+ ___35-[VMClientWrapper clientConnection]_block_invoke.203
+ ___35-[VMVoicemailManager fetchAccounts]_block_invoke.122
+ ___38-[VMVoicemailManager isAccountOnline:]_block_invoke.124
+ ___42-[VMVoicemailManager isAccountSubscribed:]_block_invoke.123
+ ___43-[VMVoicemailManager transcriptionProgress]_block_invoke
+ ___48-[VMVoicemailManager setProgressTotalUnitCount:]_block_invoke
+ ___51-[VMVoicemailManager getServiceInfoForAccountUUID:]_block_invoke.107
+ ___51-[VMVoicemailManager setProgressFractionCompleted:]_block_invoke
+ ___55-[VMVoicemailManager messageCountForMailboxType:error:]_block_invoke.139
+ ___55-[VMVoicemailManager storageUsageForAccountUUID:error:]_block_invoke.131
+ ___56-[VMVoicemailManager greetingForAccountUUID:completion:]_block_invoke.136
+ ___57-[VMVoicemailManager createPersonalizedTranscript:error:]_block_invoke.105
+ ___57-[VMVoicemailManager createPersonalizedTranscript:error:]_block_invoke.105.cold.1
+ ___58-[VMVoicemailManager maximumPasscodeLengthForAccountUUID:]_block_invoke.129
+ ___58-[VMVoicemailManager minimumPasscodeLengthForAccountUUID:]_block_invoke.127
+ ___60-[VMVoicemailManager maximumGreetingDurationForAccountUUID:]_block_invoke.134
+ ___60-[VMVoicemailManager messageCountForMailboxType:completion:]_block_invoke.140
+ ___60-[VMVoicemailManager messageCountForMailboxType:read:error:]_block_invoke.141
+ ___60-[VMVoicemailManager setAccountProperties:properties:error:]_block_invoke.109
+ ___60-[VMVoicemailManager setGreeting:forAccountUUID:completion:]_block_invoke.138
+ ___60-[VMVoicemailManager setPasscode:forAccountUUID:completion:]_block_invoke.130
+ ___61-[VMVoicemailManager isCallVoicemailSupportedForAccountUUID:]_block_invoke.125
+ ___62-[VMVoicemailManager createTranscription:transcription:error:]_block_invoke.103
+ ___62-[VMVoicemailManager isGreetingChangeSupportedForAccountUUID:]_block_invoke.133
+ ___62-[VMVoicemailManager isPasscodeChangeSupportedForAccountUUID:]_block_invoke.126
+ ___64-[VMVoicemailManager messagesForMailboxType:limit:offset:error:]_block_invoke.143
+ ___65-[VMVoicemailManager messageCountForMailboxType:read:completion:]_block_invoke.142
+ ___69-[VMVoicemailManager messagesForMailboxType:read:limit:offset:error:]_block_invoke.144
+ ___71-[VMVoicemailManager setTranscribing:fractionCompleted:totalUnitCount:]_block_invoke
+ ___block_descriptor_57_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ ___block_literal_global.102
+ ___block_literal_global.121
+ ___block_literal_global.161
+ ___block_literal_global.188
+ ___block_literal_global.196
+ ___block_literal_global.200
+ _objc_msgSend$setCompletedUnitCount:
+ _objc_msgSend$setTotalUnitCount:
+ _objc_msgSend$totalUnitCount
+ _objc_msgSend$unsignedLongValue
- GCC_except_table126
- GCC_except_table132
- GCC_except_table135
- GCC_except_table140
- GCC_except_table143
- GCC_except_table148
- GCC_except_table153
- GCC_except_table156
- GCC_except_table159
- GCC_except_table162
- GCC_except_table165
- GCC_except_table168
- GCC_except_table174
- GCC_except_table181
- GCC_except_table192
- GCC_except_table198
- GCC_except_table204
- GCC_except_table207
- GCC_except_table210
- ___35-[VMClientWrapper clientConnection]_block_invoke.191
- ___35-[VMClientWrapper clientConnection]_block_invoke.191.cold.1
- ___35-[VMClientWrapper clientConnection]_block_invoke.200
- ___35-[VMVoicemailManager fetchAccounts]_block_invoke.120
- ___38-[VMVoicemailManager isAccountOnline:]_block_invoke.122
- ___38-[VMVoicemailManager setTranscribing:]_block_invoke
- ___38-[VMVoicemailManager setTranscribing:]_block_invoke.78
- ___38-[VMVoicemailManager setTranscribing:]_block_invoke.78.cold.1
- ___38-[VMVoicemailManager setTranscribing:]_block_invoke_2
- ___38-[VMVoicemailManager setTranscribing:]_block_invoke_2.cold.1
- ___42-[VMVoicemailManager isAccountSubscribed:]_block_invoke.121
- ___51-[VMVoicemailManager getServiceInfoForAccountUUID:]_block_invoke.105
- ___55-[VMVoicemailManager messageCountForMailboxType:error:]_block_invoke.137
- ___55-[VMVoicemailManager storageUsageForAccountUUID:error:]_block_invoke.129
- ___56-[VMVoicemailManager greetingForAccountUUID:completion:]_block_invoke.134
- ___57-[VMVoicemailManager createPersonalizedTranscript:error:]_block_invoke.103
- ___57-[VMVoicemailManager createPersonalizedTranscript:error:]_block_invoke.103.cold.1
- ___58-[VMVoicemailManager maximumPasscodeLengthForAccountUUID:]_block_invoke.127
- ___58-[VMVoicemailManager minimumPasscodeLengthForAccountUUID:]_block_invoke.125
- ___60-[VMVoicemailManager maximumGreetingDurationForAccountUUID:]_block_invoke.132
- ___60-[VMVoicemailManager messageCountForMailboxType:completion:]_block_invoke.138
- ___60-[VMVoicemailManager messageCountForMailboxType:read:error:]_block_invoke.139
- ___60-[VMVoicemailManager setAccountProperties:properties:error:]_block_invoke.107
- ___60-[VMVoicemailManager setGreeting:forAccountUUID:completion:]_block_invoke.136
- ___60-[VMVoicemailManager setPasscode:forAccountUUID:completion:]_block_invoke.128
- ___61-[VMVoicemailManager isCallVoicemailSupportedForAccountUUID:]_block_invoke.123
- ___62-[VMVoicemailManager createTranscription:transcription:error:]_block_invoke.101
- ___62-[VMVoicemailManager isGreetingChangeSupportedForAccountUUID:]_block_invoke.131
- ___62-[VMVoicemailManager isPasscodeChangeSupportedForAccountUUID:]_block_invoke.124
- ___64-[VMVoicemailManager messagesForMailboxType:limit:offset:error:]_block_invoke.141
- ___65-[VMVoicemailManager messageCountForMailboxType:read:completion:]_block_invoke.140
- ___69-[VMVoicemailManager messagesForMailboxType:read:limit:offset:error:]_block_invoke.142
- ___block_literal_global.100
- ___block_literal_global.119
- ___block_literal_global.163
- ___block_literal_global.185
- ___block_literal_global.193
- ___block_literal_global.197
- ___block_literal_global.77
- ___block_literal_global.80
- _objc_msgSend$requestTranscriptionProgress:
CStrings:
+ "Client received transcribing state change message from vmd. transcribing is %@"
+ "Client received transcription progress fraction completed from vmd. transcribing is %@, fractionCompleted is %@"
+ "Client received transcription progress total count from vmd. transcribing is %@, totalUnitCount is %@"
+ "No"
+ "T@\"NSProgress\",&,N,V_transcriptionProgress"
+ "Yes"
+ "setCompletedUnitCount:"
+ "setProgressFractionCompleted:"
+ "setProgressTotalUnitCount:"
+ "setTotalUnitCount:"
+ "setTranscribing:fractionCompleted:totalUnitCount:"
+ "setTranscriptionProgress:"
+ "totalUnitCount"
+ "unsignedLongValue"
+ "v24@0:8@\"NSNumber\"16"
+ "v24@0:8@?<v@?B@\"NSNumber\"@\"NSNumber\">16"
+ "v36@0:8B16@\"NSNumber\"20@\"NSNumber\"28"
+ "v36@0:8B16@20@28"
- "@\"NSProgress\"24@0:8@?<v@?B>16"
- "Client received transcribing: %d state change"
- "Error fetching initial state: %@"
- "Error fetching progress"
- "T@\"NSProgress\",R,N,V_transcriptionProgress"

```
