## VisualVoicemail

> `/System/Library/PrivateFrameworks/VisualVoicemail.framework/VisualVoicemail`

```diff

-841.0.0.0.0
-  __TEXT.__text: 0x16bd0
+897.0.0.0.0
+  __TEXT.__text: 0x19d20
   __TEXT.__auth_stubs: 0x640
-  __TEXT.__objc_methlist: 0x1d40
-  __TEXT.__cstring: 0xe8d
-  __TEXT.__gcc_except_tab: 0x47c
-  __TEXT.__const: 0x68
-  __TEXT.__oslogstring: 0x15d8
-  __TEXT.__unwind_info: 0x790
-  __TEXT.__objc_classname: 0x2b7
-  __TEXT.__objc_methname: 0x4119
-  __TEXT.__objc_methtype: 0x9be
-  __TEXT.__objc_stubs: 0x2e40
-  __DATA_CONST.__got: 0x250
-  __DATA_CONST.__const: 0x868
-  __DATA_CONST.__objc_classlist: 0x98
+  __TEXT.__objc_methlist: 0x1ea0
+  __TEXT.__cstring: 0xf62
+  __TEXT.__gcc_except_tab: 0x500
+  __TEXT.__const: 0x78
+  __TEXT.__oslogstring: 0x1f72
+  __TEXT.__unwind_info: 0x818
+  __TEXT.__objc_classname: 0x2c3
+  __TEXT.__objc_methname: 0x45a6
+  __TEXT.__objc_methtype: 0xb45
+  __TEXT.__objc_stubs: 0x3160
+  __DATA_CONST.__got: 0x238
+  __DATA_CONST.__const: 0x9d0
+  __DATA_CONST.__objc_classlist: 0xa0
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1140
+  __DATA_CONST.__objc_selrefs: 0x1270
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x80
-  __DATA_CONST.__objc_arraydata: 0x170
+  __DATA_CONST.__objc_arraydata: 0x400
   __AUTH_CONST.__auth_got: 0x330
   __AUTH_CONST.__const: 0x240
-  __AUTH_CONST.__cfstring: 0x1300
-  __AUTH_CONST.__objc_const: 0x3a88
-  __AUTH_CONST.__objc_arrayobj: 0x30
+  __AUTH_CONST.__cfstring: 0x1400
+  __AUTH_CONST.__objc_const: 0x3b68
+  __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0x180
   __DATA.__data: 0x610
   __DATA.__bss: 0x20
-  __DATA_DIRTY.__objc_data: 0x550
+  __DATA_DIRTY.__objc_data: 0x5a0
   __DATA_DIRTY.__bss: 0x68
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B56642D0-866B-3D81-B48C-4581B796A969
-  Functions: 692
-  Symbols:   2516
-  CStrings:  1390
+  UUID: DB459BD1-75F7-3278-AC7A-896696C97754
+  Functions: 740
+  Symbols:   2662
+  CStrings:  1506
 
Symbols:
+ +[VMConfiguration VMAssetGasrSupportedLocales]
+ +[VMConfiguration VMAssetNgasrSupportedLocales:]
+ +[VMConfiguration VMPersonalizationSupportedLocales]
+ +[VMConfiguration getVMConcatenationDelimiterforLocale:]
+ +[VMConfiguration getVMLocaleSpeechAssetTypeforLocale:gasrEnabled:]
+ +[VMConfiguration getVMLocaleSpeechAssetTypeforLocaleIdentifier:gasrEnabled:]
+ +[VMUtilities readDataFromFile:customClassSet:]
+ +[VMUtilities readDataFromFile:customClassSet:].cold.1
+ +[VMUtilities readDataFromFile:customClassSet:].cold.2
+ +[VMUtilities readDataFromFile:customClassSet:].cold.3
+ +[VMUtilities writeDataToFile:fileData:]
+ +[VMUtilities writeDataToFile:fileData:].cold.1
+ +[VMUtilities writeDataToFile:fileData:].cold.2
+ +[VMUtilities writeDataToFile:fileData:].cold.3
+ +[VMUtilities writeDataToFile:fileData:].cold.4
+ -[VMVoicemail flagDescriptionStrings]
+ -[VMVoicemailManager call_accountStorageUsageChanged:storageUsage:]
+ -[VMVoicemailManager createPersonalizedTranscript:error:]
+ -[VMVoicemailManager createTranscription:transcription:error:]
+ -[VMVoicemailManager getServiceInfoForAccountUUID:]
+ -[VMVoicemailManager reportTranscriptionProblemForUUID:]
+ -[VMVoicemailManager reportTranscriptionRatedAccurateForUUID:forVoicemailUUID:]
+ -[VMVoicemailManager sendStateRequestForAccountUUID:]
+ -[VMVoicemailManager setAccountProperties:properties:error:]
+ -[VMVoicemailManager setStorageUsage:storageUsage:]
+ -[VMVoicemailManager storageUsageForAccountUUID:error:]
+ -[VMVoicemailTranscript initWithTranscriberResult:]
+ -[VMVoicemailTranscript setConfidence:]
+ -[VMVoicemailTranscript setTranscriptionString:]
+ GCC_except_table126
+ GCC_except_table132
+ GCC_except_table140
+ GCC_except_table143
+ GCC_except_table148
+ GCC_except_table153
+ GCC_except_table156
+ GCC_except_table159
+ GCC_except_table162
+ GCC_except_table165
+ GCC_except_table168
+ GCC_except_table174
+ GCC_except_table178
+ GCC_except_table181
+ GCC_except_table192
+ GCC_except_table198
+ GCC_except_table204
+ GCC_except_table207
+ GCC_except_table210
+ GCC_except_table74
+ GCC_except_table79
+ GCC_except_table83
+ GCC_except_table86
+ _OBJC_CLASS_$_NSMutableSet
+ _OBJC_CLASS_$_VMUtilities
+ _OBJC_METACLASS_$_VMUtilities
+ __OBJC_$_CLASS_METHODS_VMUtilities
+ __OBJC_CLASS_RO_$_VMUtilities
+ __OBJC_METACLASS_RO_$_VMUtilities
+ ___34-[VMVoicemailManager storageUsage]_block_invoke
+ ___35-[VMClientWrapper clientConnection]_block_invoke.191
+ ___35-[VMClientWrapper clientConnection]_block_invoke.191.cold.1
+ ___35-[VMClientWrapper clientConnection]_block_invoke.194
+ ___35-[VMClientWrapper clientConnection]_block_invoke.200
+ ___35-[VMVoicemailManager fetchAccounts]_block_invoke.120
+ ___38-[VMVoicemailManager isAccountOnline:]_block_invoke.122
+ ___38-[VMVoicemailManager setTranscribing:]_block_invoke.78
+ ___38-[VMVoicemailManager setTranscribing:]_block_invoke.78.cold.1
+ ___42-[VMVoicemailManager isAccountSubscribed:]_block_invoke.121
+ ___44-[VMVoicemailManager call_accountsDidChange]_block_invoke.58
+ ___47-[VMVoicemailManager call_voicemailsDidChange:]_block_invoke.34
+ ___48-[VMVoicemailManager call_capabilitiesDidChange]_block_invoke.41
+ ___48-[VMVoicemailManager call_onlineStatusDidChange]_block_invoke.38
+ ___49-[VMVoicemailManager call_syncInProgresDidChange]_block_invoke.47
+ ___51-[VMVoicemailManager getServiceInfoForAccountUUID:]_block_invoke
+ ___51-[VMVoicemailManager getServiceInfoForAccountUUID:]_block_invoke.105
+ ___51-[VMVoicemailManager getServiceInfoForAccountUUID:]_block_invoke.cold.1
+ ___51-[VMVoicemailManager setStorageUsage:storageUsage:]_block_invoke
+ ___53-[VMVoicemailManager sendStateRequestForAccountUUID:]_block_invoke
+ ___54-[VMVoicemailManager call_transcribingStatusDidChange]_block_invoke.55
+ ___55-[VMVoicemailManager call_managerStorageUsageDidChange]_block_invoke.50
+ ___55-[VMVoicemailManager messageCountForMailboxType:error:]_block_invoke.137
+ ___55-[VMVoicemailManager storageUsageForAccountUUID:error:]_block_invoke
+ ___55-[VMVoicemailManager storageUsageForAccountUUID:error:]_block_invoke.129
+ ___55-[VMVoicemailManager storageUsageForAccountUUID:error:]_block_invoke.cold.1
+ ___56-[VMVoicemailManager greetingForAccountUUID:completion:]_block_invoke.134
+ ___57-[VMVoicemailManager createPersonalizedTranscript:error:]_block_invoke
+ ___57-[VMVoicemailManager createPersonalizedTranscript:error:]_block_invoke.103
+ ___57-[VMVoicemailManager createPersonalizedTranscript:error:]_block_invoke.103.cold.1
+ ___57-[VMVoicemailManager createPersonalizedTranscript:error:]_block_invoke.cold.1
+ ___58-[VMVoicemailManager maximumPasscodeLengthForAccountUUID:]_block_invoke.127
+ ___58-[VMVoicemailManager minimumPasscodeLengthForAccountUUID:]_block_invoke.125
+ ___59-[VMVoicemailManager call_subscriptionStateStatusDidChange]_block_invoke.44
+ ___60-[VMVoicemailManager maximumGreetingDurationForAccountUUID:]_block_invoke.132
+ ___60-[VMVoicemailManager messageCountForMailboxType:completion:]_block_invoke.138
+ ___60-[VMVoicemailManager messageCountForMailboxType:read:error:]_block_invoke.139
+ ___60-[VMVoicemailManager setAccountProperties:properties:error:]_block_invoke
+ ___60-[VMVoicemailManager setAccountProperties:properties:error:]_block_invoke.107
+ ___60-[VMVoicemailManager setAccountProperties:properties:error:]_block_invoke.cold.1
+ ___60-[VMVoicemailManager setGreeting:forAccountUUID:completion:]_block_invoke.136
+ ___60-[VMVoicemailManager setPasscode:forAccountUUID:completion:]_block_invoke.128
+ ___61-[VMVoicemailManager isCallVoicemailSupportedForAccountUUID:]_block_invoke.123
+ ___62-[VMVoicemailManager createTranscription:transcription:error:]_block_invoke
+ ___62-[VMVoicemailManager createTranscription:transcription:error:]_block_invoke.101
+ ___62-[VMVoicemailManager createTranscription:transcription:error:]_block_invoke.cold.1
+ ___62-[VMVoicemailManager isGreetingChangeSupportedForAccountUUID:]_block_invoke.131
+ ___62-[VMVoicemailManager isPasscodeChangeSupportedForAccountUUID:]_block_invoke.124
+ ___64-[VMVoicemailManager messagesForMailboxType:limit:offset:error:]_block_invoke.141
+ ___65-[VMVoicemailManager messageCountForMailboxType:read:completion:]_block_invoke.140
+ ___67-[VMVoicemailManager call_accountStorageUsageChanged:storageUsage:]_block_invoke
+ ___69-[VMVoicemailManager messagesForMailboxType:read:limit:offset:error:]_block_invoke.142
+ ___79-[VMVoicemailManager reportTranscriptionRatedAccurateForUUID:forVoicemailUUID:]_block_invoke
+ ___block_descriptor_40_e8_32r_e22_v16?0"NSDictionary"8lr32l8
+ ___block_descriptor_48_e8_32r40r_e20_v20?0B8"NSError"12lr32l8r40l8
+ ___block_descriptor_48_e8_32r40r_e20_v24?0Q8"NSError"16lr32l8r40l8
+ ___block_descriptor_48_e8_32r40r_e37_v28?0B8"NSDictionary"12"NSError"20lr32l8r40l8
+ ___block_descriptor_48_e8_32s40r_e17_v16?0"NSError"8ls32l8r40l8
+ ___block_descriptor_49_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_56_e8_32s40r48r_e17_v16?0"NSError"8ls32l8r40l8r48l8
+ ___block_descriptor_56_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_57_e8_32s40bs48w_e58_v40?0"VMVoicemailCapabilities"8B16B20B24B28"NSNumber"32lw48l8s40l8s32l8
+ ___block_descriptor_68_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_literal_global.100
+ ___block_literal_global.119
+ ___block_literal_global.185
+ ___block_literal_global.193
+ ___block_literal_global.197
+ ___block_literal_global.63
+ ___block_literal_global.77
+ ___block_literal_global.80
+ _kVMAccountCallVoicemailSupportedKey
+ _kVMAccountOnlineKey
+ _kVMAccountProvisionedKey
+ _kVMAccountSubscribedKey
+ _kVMAccountUsageKey
+ _kVM_GASRTaskHint
+ _kVM_NGASRTaskHint
+ _objc_msgSend$VMAssetGasrSupportedLocales
+ _objc_msgSend$VMAssetNgasrSupportedLocales:
+ _objc_msgSend$_setError
+ _objc_msgSend$accountStorageUsageChanged:storageUsage:
+ _objc_msgSend$call_accountStorageUsageChanged:storageUsage:
+ _objc_msgSend$contextualizedTranscriberMultisegmentResult
+ _objc_msgSend$createPersonalizedTranscript:reply:
+ _objc_msgSend$createTranscription:transcription:reply:
+ _objc_msgSend$fileURLWithPath:isDirectory:
+ _objc_msgSend$flagDescriptionStrings
+ _objc_msgSend$getBytes:range:
+ _objc_msgSend$getServiceInfoForAccountUUID:reply:
+ _objc_msgSend$getVMLocaleSpeechAssetTypeforLocaleIdentifier:gasrEnabled:
+ _objc_msgSend$hasError
+ _objc_msgSend$position
+ _objc_msgSend$reportTranscriptionProblemForUUID:
+ _objc_msgSend$reportTranscriptionRatedAccurateForUUID:forVoicemailUUID:
+ _objc_msgSend$sendStateRequestForAccountUUID:
+ _objc_msgSend$setAccountProperties:properties:reply:
+ _objc_msgSend$setByAddingObjectsFromSet:
+ _objc_msgSend$setPosition:
+ _objc_msgSend$storageUsageForAccountUUID:reply:
+ _objc_msgSend$string
+ _objc_msgSend$text
+ _objc_msgSend$transcriptions
- -[VMLegacyAccount mailboxUsage]
- GCC_except_table130
- GCC_except_table138
- GCC_except_table141
- GCC_except_table144
- GCC_except_table147
- GCC_except_table150
- GCC_except_table157
- GCC_except_table160
- GCC_except_table171
- GCC_except_table177
- GCC_except_table183
- GCC_except_table186
- GCC_except_table189
- GCC_except_table64
- GCC_except_table77
- GCC_except_table81
- GCC_except_table84
- OBJC_IVAR_$_PBDataReader._bytes
- OBJC_IVAR_$_PBDataReader._error
- OBJC_IVAR_$_PBDataReader._length
- OBJC_IVAR_$_PBDataReader._pos
- ___35-[VMClientWrapper clientConnection]_block_invoke.169
- ___35-[VMClientWrapper clientConnection]_block_invoke.169.cold.1
- ___35-[VMClientWrapper clientConnection]_block_invoke.172
- ___35-[VMClientWrapper clientConnection]_block_invoke.178
- ___35-[VMVoicemailManager fetchAccounts]_block_invoke.103
- ___38-[VMVoicemailManager isAccountOnline:]_block_invoke.105
- ___38-[VMVoicemailManager setStorageUsage:]_block_invoke
- ___38-[VMVoicemailManager setTranscribing:]_block_invoke.68
- ___38-[VMVoicemailManager setTranscribing:]_block_invoke.68.cold.1
- ___42-[VMVoicemailManager isAccountSubscribed:]_block_invoke.104
- ___44-[VMVoicemailManager call_accountsDidChange]_block_invoke_2
- ___47-[VMVoicemailManager call_voicemailsDidChange:]_block_invoke_3
- ___48-[VMVoicemailManager call_capabilitiesDidChange]_block_invoke_2
- ___48-[VMVoicemailManager call_onlineStatusDidChange]_block_invoke_2
- ___49-[VMVoicemailManager call_syncInProgresDidChange]_block_invoke_2
- ___54-[VMVoicemailManager call_transcribingStatusDidChange]_block_invoke_2
- ___55-[VMVoicemailManager call_managerStorageUsageDidChange]_block_invoke_2
- ___55-[VMVoicemailManager messageCountForMailboxType:error:]_block_invoke.119
- ___56-[VMVoicemailManager greetingForAccountUUID:completion:]_block_invoke.116
- ___58-[VMVoicemailManager maximumPasscodeLengthForAccountUUID:]_block_invoke.110
- ___58-[VMVoicemailManager minimumPasscodeLengthForAccountUUID:]_block_invoke.108
- ___59-[VMVoicemailManager call_subscriptionStateStatusDidChange]_block_invoke_2
- ___60-[VMVoicemailManager maximumGreetingDurationForAccountUUID:]_block_invoke.114
- ___60-[VMVoicemailManager messageCountForMailboxType:completion:]_block_invoke.120
- ___60-[VMVoicemailManager messageCountForMailboxType:read:error:]_block_invoke.121
- ___60-[VMVoicemailManager setGreeting:forAccountUUID:completion:]_block_invoke.118
- ___60-[VMVoicemailManager setPasscode:forAccountUUID:completion:]_block_invoke.111
- ___61-[VMVoicemailManager isCallVoicemailSupportedForAccountUUID:]_block_invoke.106
- ___62-[VMVoicemailManager isGreetingChangeSupportedForAccountUUID:]_block_invoke.113
- ___62-[VMVoicemailManager isPasscodeChangeSupportedForAccountUUID:]_block_invoke.107
- ___64-[VMVoicemailManager messagesForMailboxType:limit:offset:error:]_block_invoke.123
- ___65-[VMVoicemailManager messageCountForMailboxType:read:completion:]_block_invoke.122
- ___69-[VMVoicemailManager messagesForMailboxType:read:limit:offset:error:]_block_invoke.124
- ___block_descriptor_57_e8_32s40bs48w_e45_v32?0"VMVoicemailCapabilities"8B16B20B24B28lw48l8s40l8s32l8
- ___block_descriptor_60_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
- ___block_literal_global.102
- ___block_literal_global.141
- ___block_literal_global.171
- ___block_literal_global.175
- ___block_literal_global.53
- ___block_literal_global.67
- ___block_literal_global.70
- ___block_literal_global.90
CStrings:
+ " "
+ "@24@0:8q16"
+ "B32@0:8@16@24"
+ "B40@0:8@16@24^@32"
+ "Client is notifying delegate %@ using accountStorageUsageChanged"
+ "Client is notifying delegate %@ using accountsDidChange"
+ "Client is notifying delegate %@ using capabilitiesDidChange"
+ "Client is notifying delegate %@ using greetingDidChangeByCarrier"
+ "Client is notifying delegate %@ using managerStorageUsageDidChange"
+ "Client is notifying delegate %@ using onlineStatusDidChange"
+ "Client is notifying delegate %@ using subscriptionStateStatusDidChange"
+ "Client is notifying delegate %@ using syncInProgresDidChange"
+ "Client is notifying delegate %@ using transcribingStatusDidChange"
+ "Client is notifying delegate %@ using voicemailsDidChangeInitial"
+ "Client post accounts changed notification"
+ "Client post capabilities changed notification"
+ "Client post online status changed notification"
+ "Client post storage usage changed notification"
+ "Client post subscription status changed notification"
+ "Client post sync in progress changed notification"
+ "Client post transcribing status changed notification"
+ "Client post voicemails changed notification"
+ "Client received storage usage changed message for account UUID %@, storage usage is %@%%"
+ "Client received voicemails updated message from vmd"
+ "Could not create transcription for %@ due to error %@"
+ "Could not retrieve service state for account UUID %@ due to error %@"
+ "Could not retrieve storage usage for account UUID %@ due to error %@"
+ "Could not set properties for account UUID %@ due to error %@"
+ "Delegate %@ does not support selector accountStorageUsageChanged"
+ "Delegate %@ does not support selector accountsDidChange"
+ "Delegate %@ does not support selector capabilitiesDidChange"
+ "Delegate %@ does not support selector greetingDidChangeByCarrier"
+ "Delegate %@ does not support selector managerStorageUsageDidChange"
+ "Delegate %@ does not support selector onlineStatusDidChange"
+ "Delegate %@ does not support selector subscriptionStateStatusDidChange"
+ "Delegate %@ does not support selector syncInProgresDidChange"
+ "Delegate %@ does not support selector transcribingStatusDidChange"
+ "Delegate %@ does not support selector voicemailsDidChangeInitial"
+ "Error %@ encountered while encoding file data for file :%@"
+ "Error %@ unarchiving file: %@"
+ "Error %@ while writing data for file: %@"
+ "Error reading file %@, error: %@"
+ "Error unarchiving data as file name empty."
+ "Error writing data as received empty file path."
+ "Error: Could not write data to file %@. Invalid URL."
+ "File data %@ written to location: %@"
+ "For file %@, unarchived object class: %@"
+ "Q32@0:8@16^@24"
+ "Segment dictation result:\"%@\" , confidence = %f"
+ "VMAccountCallVoicemailSupported"
+ "VMAccountOnline"
+ "VMAccountProvisioned"
+ "VMAccountSubscribed"
+ "VMAccountUsage"
+ "VMAssetGasrSupportedLocales"
+ "VMAssetNgasrSupportedLocales:"
+ "VMPersonalizationSupportedLocales"
+ "VMUtilities"
+ "_setError"
+ "accountStorageUsageChanged:storageUsage:"
+ "call_accountStorageUsageChanged:storageUsage:"
+ "contextualizedTranscriberMultisegmentResult"
+ "createPersonalizedTranscript: Results %@"
+ "createPersonalizedTranscript:error:"
+ "createPersonalizedTranscript:reply:"
+ "createTranscription:transcription:error:"
+ "createTranscription:transcription:reply:"
+ "fileURLWithPath:isDirectory:"
+ "flagDescriptionStrings"
+ "fr-CA"
+ "getBytes:range:"
+ "getServiceInfoForAccountUUID:"
+ "getServiceInfoForAccountUUID:reply:"
+ "getVMConcatenationDelimiterforLocale:"
+ "getVMLocaleSpeechAssetTypeforLocale:gasrEnabled:"
+ "getVMLocaleSpeechAssetTypeforLocaleIdentifier: Unsupported locale identifier = %@"
+ "getVMLocaleSpeechAssetTypeforLocaleIdentifier:gasrEnabled:"
+ "hasError"
+ "initWithTranscriberResult:"
+ "ko-KR"
+ "position"
+ "q28@0:8@16B24"
+ "readDataFromFile:customClassSet:"
+ "reportTranscriptionProblemForUUID:"
+ "reportTranscriptionRatedAccurateForUUID:forVoicemailUUID:"
+ "sendStateRequestForAccountUUID:"
+ "setAccountProperties:properties:error:"
+ "setAccountProperties:properties:reply:"
+ "setByAddingObjectsFromSet:"
+ "setConfidence:"
+ "setPosition:"
+ "setStorageUsage:storageUsage:"
+ "setTranscriptionString:"
+ "storageUsageForAccountUUID:error:"
+ "storageUsageForAccountUUID:reply:"
+ "string"
+ "text"
+ "transcriptions"
+ "v16@?0@\"NSDictionary\"8"
+ "v20@0:8f16"
+ "v24@0:8@?<v@?@\"VMVoicemailCapabilities\"BBBB@\"NSNumber\">16"
+ "v24@?0Q8@\"NSError\"16"
+ "v28@0:8B16@\"NSUUID\"20"
+ "v28@?0B8@\"NSDictionary\"12@\"NSError\"20"
+ "v32@0:8@\"NSURL\"16@?<v@?B@\"NSDictionary\"@\"NSError\">24"
+ "v32@0:8@\"NSUUID\"16@?<v@?@\"NSDictionary\">24"
+ "v32@0:8@\"NSUUID\"16@?<v@?Q@\"NSError\">24"
+ "v32@0:8@\"NSUUID\"16Q24"
+ "v32@0:8@16Q24"
+ "v40@0:8@\"NSURL\"16@\"NSURL\"24@?<v@?B@\"NSError\">32"
+ "v40@0:8@\"NSUUID\"16@\"NSDictionary\"24@?<v@?B@\"NSError\">32"
+ "v40@?0@\"VMVoicemailCapabilities\"8B16B20B24B28@\"NSNumber\"32"
+ "writeDataToFile:fileData:"
- "Client received new storage usage from vmd. Current storage level is %lu%%"
- "localeForTranscriptionLanguage: Flag lvmExpansionLiveOnEnabled enabled"
- "mailboxUsage"
- "v24@0:8@?<v@?@\"VMVoicemailCapabilities\"BBBB>16"
- "v32@?0@\"VMVoicemailCapabilities\"8B16B20B24B28"

```
