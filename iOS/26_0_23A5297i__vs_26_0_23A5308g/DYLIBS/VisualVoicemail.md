## VisualVoicemail

> `/System/Library/PrivateFrameworks/VisualVoicemail.framework/VisualVoicemail`

```diff

-901.0.0.0.0
-  __TEXT.__text: 0x1a1c8
+902.0.0.0.0
+  __TEXT.__text: 0x19b74
   __TEXT.__auth_stubs: 0x640
-  __TEXT.__objc_methlist: 0x1ee8
-  __TEXT.__cstring: 0xf69
+  __TEXT.__objc_methlist: 0x1ed0
+  __TEXT.__cstring: 0xf50
   __TEXT.__gcc_except_tab: 0x510
   __TEXT.__const: 0x78
-  __TEXT.__oslogstring: 0x2030
-  __TEXT.__unwind_info: 0x858
-  __TEXT.__objc_classname: 0x2c3
-  __TEXT.__objc_methname: 0x4674
-  __TEXT.__objc_methtype: 0xb9a
+  __TEXT.__oslogstring: 0x1f79
+  __TEXT.__unwind_info: 0x848
+  __TEXT.__objc_classname: 0x2b7
+  __TEXT.__objc_methname: 0x468e
+  __TEXT.__objc_methtype: 0xb34
   __TEXT.__objc_stubs: 0x31c0
-  __DATA_CONST.__got: 0x238
+  __DATA_CONST.__got: 0x230
   __DATA_CONST.__const: 0x9f8
-  __DATA_CONST.__objc_classlist: 0xa0
+  __DATA_CONST.__objc_classlist: 0x98
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x12b0
+  __DATA_CONST.__objc_selrefs: 0x12a0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x80
   __DATA_CONST.__objc_arraydata: 0x400
   __AUTH_CONST.__auth_got: 0x330
   __AUTH_CONST.__const: 0x220
   __AUTH_CONST.__cfstring: 0x1440
-  __AUTH_CONST.__objc_const: 0x3bb8
+  __AUTH_CONST.__objc_const: 0x3b28
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0x180
   __DATA.__data: 0x610
   __DATA.__bss: 0x30
-  __DATA_DIRTY.__objc_data: 0x5a0
+  __DATA_DIRTY.__objc_data: 0x550
   __DATA_DIRTY.__bss: 0x60
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8F338AE8-EDB4-38D0-A909-CA990AABDE41
-  Functions: 746
-  Symbols:   2678
-  CStrings:  1521
+  UUID: C21D9E97-6DF6-3A8B-B3B2-49197CCB436A
+  Functions: 738
+  Symbols:   2656
+  CStrings:  1508
 
Symbols:
+ -[VMVoicemailManager call_transcriptionServiceStatusDidChange]
+ -[VMVoicemailManager isTranscriptionServiceAvailable]
+ -[VMVoicemailManager setTranscriptionServiceAvailable:]
+ GCC_except_table127
+ GCC_except_table135
+ GCC_except_table141
+ GCC_except_table149
+ GCC_except_table162
+ GCC_except_table165
+ GCC_except_table168
+ GCC_except_table171
+ GCC_except_table174
+ GCC_except_table177
+ GCC_except_table183
+ GCC_except_table187
+ GCC_except_table190
+ GCC_except_table201
+ GCC_except_table207
+ GCC_except_table213
+ GCC_except_table216
+ GCC_except_table77
+ GCC_except_table84
+ GCC_except_table88
+ GCC_except_table91
+ _OBJC_IVAR_$_VMVoicemailManager._transcriptionAvailable
+ ___35-[VMClientWrapper clientConnection]_block_invoke.193
+ ___35-[VMClientWrapper clientConnection]_block_invoke.193.cold.1
+ ___35-[VMClientWrapper clientConnection]_block_invoke.196
+ ___35-[VMClientWrapper clientConnection]_block_invoke.202
+ ___35-[VMVoicemailManager fetchAccounts]_block_invoke.124
+ ___38-[VMVoicemailManager isAccountOnline:]_block_invoke.126
+ ___42-[VMVoicemailManager isAccountSubscribed:]_block_invoke.125
+ ___44-[VMVoicemailManager call_accountsDidChange]_block_invoke.60
+ ___51-[VMVoicemailManager getServiceInfoForAccountUUID:]_block_invoke.109
+ ___53-[VMVoicemailManager isTranscriptionServiceAvailable]_block_invoke
+ ___55-[VMVoicemailManager messageCountForMailboxType:error:]_block_invoke.141
+ ___55-[VMVoicemailManager setTranscriptionServiceAvailable:]_block_invoke
+ ___55-[VMVoicemailManager storageUsageForAccountUUID:error:]_block_invoke.133
+ ___56-[VMVoicemailManager greetingForAccountUUID:completion:]_block_invoke.138
+ ___57-[VMVoicemailManager createPersonalizedTranscript:error:]_block_invoke.107
+ ___57-[VMVoicemailManager createPersonalizedTranscript:error:]_block_invoke.107.cold.1
+ ___58-[VMVoicemailManager maximumPasscodeLengthForAccountUUID:]_block_invoke.131
+ ___58-[VMVoicemailManager minimumPasscodeLengthForAccountUUID:]_block_invoke.129
+ ___60-[VMVoicemailManager maximumGreetingDurationForAccountUUID:]_block_invoke.136
+ ___60-[VMVoicemailManager messageCountForMailboxType:completion:]_block_invoke.142
+ ___60-[VMVoicemailManager messageCountForMailboxType:read:error:]_block_invoke.143
+ ___60-[VMVoicemailManager setAccountProperties:properties:error:]_block_invoke.111
+ ___60-[VMVoicemailManager setGreeting:forAccountUUID:completion:]_block_invoke.140
+ ___60-[VMVoicemailManager setPasscode:forAccountUUID:completion:]_block_invoke.132
+ ___61-[VMVoicemailManager isCallVoicemailSupportedForAccountUUID:]_block_invoke.127
+ ___62-[VMVoicemailManager call_transcriptionServiceStatusDidChange]_block_invoke
+ ___62-[VMVoicemailManager createTranscription:transcription:error:]_block_invoke.105
+ ___62-[VMVoicemailManager isGreetingChangeSupportedForAccountUUID:]_block_invoke.135
+ ___62-[VMVoicemailManager isPasscodeChangeSupportedForAccountUUID:]_block_invoke.128
+ ___64-[VMVoicemailManager messagesForMailboxType:limit:offset:error:]_block_invoke.145
+ ___65-[VMVoicemailManager messageCountForMailboxType:read:completion:]_block_invoke.144
+ ___69-[VMVoicemailManager messagesForMailboxType:read:limit:offset:error:]_block_invoke.146
+ ___block_descriptor_57_e8_32s40bs48w_e33_v36?0B8B12B16B20B24"NSNumber"28lw48l8s40l8s32l8
+ ___block_descriptor_61_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
+ ___block_literal_global.104
+ ___block_literal_global.123
+ ___block_literal_global.187
+ ___block_literal_global.195
+ ___block_literal_global.199
+ ___block_literal_global.65
+ _objc_msgSend$call_transcriptionServiceStatusDidChange
+ _objc_msgSend$isTranscriptionServiceAvailable
+ _objc_msgSend$transcriptionServiceStatusDidChange
- +[VMUtilities readDataFromFile:customClassSet:]
- +[VMUtilities readDataFromFile:customClassSet:].cold.1
- +[VMUtilities readDataFromFile:customClassSet:].cold.2
- +[VMUtilities readDataFromFile:customClassSet:].cold.3
- +[VMUtilities writeDataToFile:fileData:]
- +[VMUtilities writeDataToFile:fileData:].cold.1
- +[VMUtilities writeDataToFile:fileData:].cold.2
- +[VMUtilities writeDataToFile:fileData:].cold.3
- +[VMUtilities writeDataToFile:fileData:].cold.4
- -[VMVoicemailManager capabilities]
- -[VMVoicemailManager setCapabilities:]
- GCC_except_table120
- GCC_except_table130
- GCC_except_table136
- GCC_except_table139
- GCC_except_table147
- GCC_except_table160
- GCC_except_table163
- GCC_except_table166
- GCC_except_table169
- GCC_except_table172
- GCC_except_table178
- GCC_except_table182
- GCC_except_table185
- GCC_except_table196
- GCC_except_table202
- GCC_except_table208
- GCC_except_table211
- GCC_except_table214
- GCC_except_table66
- GCC_except_table83
- GCC_except_table86
- _OBJC_CLASS_$_NSMutableSet
- _OBJC_CLASS_$_VMUtilities
- _OBJC_IVAR_$_VMVoicemailManager._capabilities
- _OBJC_METACLASS_$_VMUtilities
- __OBJC_$_CLASS_METHODS_VMUtilities
- __OBJC_CLASS_RO_$_VMUtilities
- __OBJC_METACLASS_RO_$_VMUtilities
- ___35-[VMClientWrapper clientConnection]_block_invoke.194
- ___35-[VMClientWrapper clientConnection]_block_invoke.194.cold.1
- ___35-[VMClientWrapper clientConnection]_block_invoke.197
- ___35-[VMClientWrapper clientConnection]_block_invoke.203
- ___35-[VMVoicemailManager fetchAccounts]_block_invoke.122
- ___38-[VMVoicemailManager isAccountOnline:]_block_invoke.124
- ___38-[VMVoicemailManager setCapabilities:]_block_invoke
- ___42-[VMVoicemailManager isAccountSubscribed:]_block_invoke.123
- ___44-[VMVoicemailManager call_accountsDidChange]_block_invoke.58
- ___44-[VMVoicemailManager isTranscriptionEnabled]_block_invoke
- ___51-[VMVoicemailManager getServiceInfoForAccountUUID:]_block_invoke.107
- ___55-[VMVoicemailManager messageCountForMailboxType:error:]_block_invoke.139
- ___55-[VMVoicemailManager storageUsageForAccountUUID:error:]_block_invoke.131
- ___56-[VMVoicemailManager greetingForAccountUUID:completion:]_block_invoke.136
- ___57-[VMVoicemailManager createPersonalizedTranscript:error:]_block_invoke.105
- ___57-[VMVoicemailManager createPersonalizedTranscript:error:]_block_invoke.105.cold.1
- ___58-[VMVoicemailManager maximumPasscodeLengthForAccountUUID:]_block_invoke.129
- ___58-[VMVoicemailManager minimumPasscodeLengthForAccountUUID:]_block_invoke.127
- ___60-[VMVoicemailManager maximumGreetingDurationForAccountUUID:]_block_invoke.134
- ___60-[VMVoicemailManager messageCountForMailboxType:completion:]_block_invoke.140
- ___60-[VMVoicemailManager messageCountForMailboxType:read:error:]_block_invoke.141
- ___60-[VMVoicemailManager setAccountProperties:properties:error:]_block_invoke.109
- ___60-[VMVoicemailManager setGreeting:forAccountUUID:completion:]_block_invoke.138
- ___60-[VMVoicemailManager setPasscode:forAccountUUID:completion:]_block_invoke.130
- ___61-[VMVoicemailManager isCallVoicemailSupportedForAccountUUID:]_block_invoke.125
- ___62-[VMVoicemailManager createTranscription:transcription:error:]_block_invoke.103
- ___62-[VMVoicemailManager isGreetingChangeSupportedForAccountUUID:]_block_invoke.133
- ___62-[VMVoicemailManager isPasscodeChangeSupportedForAccountUUID:]_block_invoke.126
- ___64-[VMVoicemailManager messagesForMailboxType:limit:offset:error:]_block_invoke.143
- ___65-[VMVoicemailManager messageCountForMailboxType:read:completion:]_block_invoke.142
- ___69-[VMVoicemailManager messagesForMailboxType:read:limit:offset:error:]_block_invoke.144
- ___block_descriptor_57_e8_32s40bs48w_e58_v40?0"VMVoicemailCapabilities"8B16B20B24B28"NSNumber"32lw48l8s40l8s32l8
- ___block_descriptor_68_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s48l8s56l8
- ___block_literal_global.102
- ___block_literal_global.121
- ___block_literal_global.188
- ___block_literal_global.196
- ___block_literal_global.200
- ___block_literal_global.63
- _objc_msgSend$capabilities
- _objc_msgSend$fileURLWithPath:isDirectory:
- _objc_msgSend$setByAddingObjectsFromSet:
CStrings:
+ "Client is notifying delegate %@ using transcriptionServiceStatusDidChange"
+ "Client received transcription service availability status change message from vmd. transcription service available is %@"
+ "Delegate %@ does not support selector transcriptionServiceStatusDidChange"
+ "TB,R,N,GisTranscriptionServiceAvailable,V_transcriptionAvailable"
+ "_transcriptionAvailable"
+ "call_transcriptionServiceStatusDidChange"
+ "isTranscriptionServiceAvailable"
+ "setTranscriptionServiceAvailable:"
+ "transcriptionServiceStatusDidChange"
+ "v24@0:8@?<v@?BBBBB@\"NSNumber\">16"
+ "v36@?0B8B12B16B20B24@\"NSNumber\"28"
- "@\"VMVoicemailCapabilities\""
- "B32@0:8@16@24"
- "Client received new capabilities from vmd. vmd capabilities are %@"
- "Error %@ encountered while encoding file data for file :%@"
- "Error %@ unarchiving file: %@"
- "Error %@ while writing data for file: %@"
- "Error reading file %@, error: %@"
- "Error unarchiving data as file name empty."
- "Error writing data as received empty file path."
- "Error: Could not write data to file %@. Invalid URL."
- "File data %@ written to location: %@"
- "For file %@, unarchived object class: %@"
- "T@\"VMVoicemailCapabilities\",&,N,V_capabilities"
- "VMUtilities"
- "_capabilities"
- "capabilities"
- "fileURLWithPath:isDirectory:"
- "readDataFromFile:customClassSet:"
- "setByAddingObjectsFromSet:"
- "setCapabilities:"
- "v24@0:8@\"VMVoicemailCapabilities\"16"
- "v24@0:8@?<v@?@\"VMVoicemailCapabilities\"BBBB@\"NSNumber\">16"
- "v40@?0@\"VMVoicemailCapabilities\"8B16B20B24B28@\"NSNumber\"32"
- "writeDataToFile:fileData:"

```
