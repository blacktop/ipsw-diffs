## VisualVoicemail

> `/System/Library/PrivateFrameworks/VisualVoicemail.framework/VisualVoicemail`

```diff

-956.0.0.0.0
-  __TEXT.__text: 0x1b554
-  __TEXT.__objc_methlist: 0x2010
-  __TEXT.__cstring: 0x101b
-  __TEXT.__gcc_except_tab: 0x554
-  __TEXT.__const: 0x78
-  __TEXT.__oslogstring: 0x2297
-  __TEXT.__unwind_info: 0x948
+958.0.0.0.0
+  __TEXT.__text: 0x1f54c
+  __TEXT.__objc_methlist: 0x2208
+  __TEXT.__cstring: 0x112b
+  __TEXT.__gcc_except_tab: 0x2ca8
+  __TEXT.__const: 0x80
+  __TEXT.__oslogstring: 0x2300
+  __TEXT.__unwind_info: 0x1090
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xb10
-  __DATA_CONST.__objc_classlist: 0x98
+  __DATA_CONST.__const: 0xb60
+  __DATA_CONST.__objc_classlist: 0xa8
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1378
+  __DATA_CONST.__objc_selrefs: 0x13b0
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x80
+  __DATA_CONST.__objc_superrefs: 0x90
   __DATA_CONST.__objc_arraydata: 0x400
-  __DATA_CONST.__got: 0x230
-  __AUTH_CONST.__const: 0x240
-  __AUTH_CONST.__cfstring: 0x1440
-  __AUTH_CONST.__objc_const: 0x3b90
+  __DATA_CONST.__got: 0x240
+  __AUTH_CONST.__const: 0x260
+  __AUTH_CONST.__cfstring: 0x1480
+  __AUTH_CONST.__objc_const: 0x4110
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__auth_got: 0x0
-  __DATA.__objc_ivar: 0x180
+  __AUTH.__objc_data: 0xa0
+  __DATA.__objc_ivar: 0x1b8
   __DATA.__data: 0x610
-  __DATA.__bss: 0x20
+  __DATA.__bss: 0x60
   __DATA_DIRTY.__objc_data: 0x5f0
-  __DATA_DIRTY.__bss: 0x70
+  __DATA_DIRTY.__bss: 0x30
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
+  - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 790
-  Symbols:   1770
-  CStrings:  359
+  Functions: 836
+  Symbols:   2005
+  CStrings:  368
 
Symbols:
+ +[VMVoicemailData supportsSecureCoding]
+ +[VMVoicemailDataContainer supportsSecureCoding]
+ -[VMVoicemailData .cxx_destruct]
+ -[VMVoicemailData callbackDestinationID]
+ -[VMVoicemailData callbackISOCountryCode]
+ -[VMVoicemailData date]
+ -[VMVoicemailData description]
+ -[VMVoicemailData duration]
+ -[VMVoicemailData encodeWithCoder:]
+ -[VMVoicemailData flags]
+ -[VMVoicemailData identifier]
+ -[VMVoicemailData initWithCoder:]
+ -[VMVoicemailData receiverDestinationID]
+ -[VMVoicemailData receiverISOCountryCode]
+ -[VMVoicemailData receiverLabelID]
+ -[VMVoicemailData remoteUID]
+ -[VMVoicemailData senderDestinationID]
+ -[VMVoicemailData senderISOCountryCode]
+ -[VMVoicemailData setCallbackDestinationID:]
+ -[VMVoicemailData setCallbackISOCountryCode:]
+ -[VMVoicemailData setDate:]
+ -[VMVoicemailData setDuration:]
+ -[VMVoicemailData setFlags:]
+ -[VMVoicemailData setIdentifier:]
+ -[VMVoicemailData setReceiverDestinationID:]
+ -[VMVoicemailData setReceiverISOCountryCode:]
+ -[VMVoicemailData setReceiverLabelID:]
+ -[VMVoicemailData setRemoteUID:]
+ -[VMVoicemailData setSenderDestinationID:]
+ -[VMVoicemailData setSenderISOCountryCode:]
+ -[VMVoicemailData setUuid:]
+ -[VMVoicemailData uuid]
+ -[VMVoicemailDataContainer .cxx_destruct]
+ -[VMVoicemailDataContainer dealloc]
+ -[VMVoicemailDataContainer encodeWithCoder:]
+ -[VMVoicemailDataContainer initWithCoder:]
+ -[VMVoicemailDataContainer initWithVoicemails:]
+ -[VMVoicemailDataContainer voicemails]
+ -[VMVoicemailManager voicemailsFromContainer:basePath:]
+ -[VMVoicemailManager voicemailsUpdated:basePath:]
+ GCC_except_table0
+ GCC_except_table10
+ GCC_except_table100
+ GCC_except_table101
+ GCC_except_table103
+ GCC_except_table104
+ GCC_except_table105
+ GCC_except_table106
+ GCC_except_table107
+ GCC_except_table108
+ GCC_except_table109
+ GCC_except_table11
+ GCC_except_table110
+ GCC_except_table111
+ GCC_except_table112
+ GCC_except_table113
+ GCC_except_table114
+ GCC_except_table115
+ GCC_except_table116
+ GCC_except_table117
+ GCC_except_table124
+ GCC_except_table126
+ GCC_except_table128
+ GCC_except_table13
+ GCC_except_table130
+ GCC_except_table136
+ GCC_except_table137
+ GCC_except_table138
+ GCC_except_table14
+ GCC_except_table140
+ GCC_except_table142
+ GCC_except_table143
+ GCC_except_table145
+ GCC_except_table147
+ GCC_except_table148
+ GCC_except_table15
+ GCC_except_table150
+ GCC_except_table151
+ GCC_except_table153
+ GCC_except_table156
+ GCC_except_table159
+ GCC_except_table16
+ GCC_except_table162
+ GCC_except_table165
+ GCC_except_table168
+ GCC_except_table17
+ GCC_except_table171
+ GCC_except_table174
+ GCC_except_table177
+ GCC_except_table18
+ GCC_except_table180
+ GCC_except_table183
+ GCC_except_table186
+ GCC_except_table189
+ GCC_except_table19
+ GCC_except_table192
+ GCC_except_table194
+ GCC_except_table195
+ GCC_except_table197
+ GCC_except_table198
+ GCC_except_table199
+ GCC_except_table2
+ GCC_except_table200
+ GCC_except_table202
+ GCC_except_table203
+ GCC_except_table205
+ GCC_except_table208
+ GCC_except_table211
+ GCC_except_table214
+ GCC_except_table217
+ GCC_except_table219
+ GCC_except_table220
+ GCC_except_table223
+ GCC_except_table224
+ GCC_except_table225
+ GCC_except_table228
+ GCC_except_table230
+ GCC_except_table232
+ GCC_except_table233
+ GCC_except_table235
+ GCC_except_table236
+ GCC_except_table238
+ GCC_except_table239
+ GCC_except_table24
+ GCC_except_table241
+ GCC_except_table243
+ GCC_except_table244
+ GCC_except_table247
+ GCC_except_table249
+ GCC_except_table25
+ GCC_except_table250
+ GCC_except_table253
+ GCC_except_table256
+ GCC_except_table257
+ GCC_except_table258
+ GCC_except_table259
+ GCC_except_table26
+ GCC_except_table260
+ GCC_except_table261
+ GCC_except_table262
+ GCC_except_table263
+ GCC_except_table264
+ GCC_except_table265
+ GCC_except_table27
+ GCC_except_table29
+ GCC_except_table30
+ GCC_except_table31
+ GCC_except_table33
+ GCC_except_table34
+ GCC_except_table35
+ GCC_except_table37
+ GCC_except_table38
+ GCC_except_table4
+ GCC_except_table40
+ GCC_except_table41
+ GCC_except_table43
+ GCC_except_table44
+ GCC_except_table45
+ GCC_except_table46
+ GCC_except_table47
+ GCC_except_table49
+ GCC_except_table5
+ GCC_except_table50
+ GCC_except_table51
+ GCC_except_table52
+ GCC_except_table53
+ GCC_except_table54
+ GCC_except_table55
+ GCC_except_table56
+ GCC_except_table57
+ GCC_except_table58
+ GCC_except_table60
+ GCC_except_table61
+ GCC_except_table63
+ GCC_except_table65
+ GCC_except_table66
+ GCC_except_table69
+ GCC_except_table7
+ GCC_except_table71
+ GCC_except_table73
+ GCC_except_table75
+ GCC_except_table78
+ GCC_except_table80
+ GCC_except_table82
+ GCC_except_table83
+ GCC_except_table85
+ GCC_except_table86
+ GCC_except_table87
+ GCC_except_table90
+ GCC_except_table93
+ GCC_except_table94
+ GCC_except_table95
+ GCC_except_table96
+ GCC_except_table97
+ GCC_except_table98
+ GCC_except_table99
+ _OBJC_CLASS_$_VMVoicemailData
+ _OBJC_CLASS_$_VMVoicemailDataContainer
+ _OBJC_IVAR_$_VMVoicemailData._callbackDestinationID
+ _OBJC_IVAR_$_VMVoicemailData._callbackISOCountryCode
+ _OBJC_IVAR_$_VMVoicemailData._date
+ _OBJC_IVAR_$_VMVoicemailData._duration
+ _OBJC_IVAR_$_VMVoicemailData._flags
+ _OBJC_IVAR_$_VMVoicemailData._identifier
+ _OBJC_IVAR_$_VMVoicemailData._receiverDestinationID
+ _OBJC_IVAR_$_VMVoicemailData._receiverISOCountryCode
+ _OBJC_IVAR_$_VMVoicemailData._receiverLabelID
+ _OBJC_IVAR_$_VMVoicemailData._remoteUID
+ _OBJC_IVAR_$_VMVoicemailData._senderDestinationID
+ _OBJC_IVAR_$_VMVoicemailData._senderISOCountryCode
+ _OBJC_IVAR_$_VMVoicemailData._uuid
+ _OBJC_IVAR_$_VMVoicemailDataContainer._voicemails
+ _OBJC_METACLASS_$_VMVoicemailData
+ _OBJC_METACLASS_$_VMVoicemailDataContainer
+ __OBJC_$_CLASS_METHODS_VMVoicemailData
+ __OBJC_$_CLASS_METHODS_VMVoicemailDataContainer
+ __OBJC_$_CLASS_PROP_LIST_VMVoicemailData
+ __OBJC_$_CLASS_PROP_LIST_VMVoicemailDataContainer
+ __OBJC_$_INSTANCE_METHODS_VMVoicemailData
+ __OBJC_$_INSTANCE_METHODS_VMVoicemailDataContainer
+ __OBJC_$_INSTANCE_VARIABLES_VMVoicemailData
+ __OBJC_$_INSTANCE_VARIABLES_VMVoicemailDataContainer
+ __OBJC_$_PROP_LIST_VMVoicemailData
+ __OBJC_$_PROP_LIST_VMVoicemailDataContainer
+ __OBJC_CLASS_PROTOCOLS_$_VMVoicemailData
+ __OBJC_CLASS_PROTOCOLS_$_VMVoicemailDataContainer
+ __OBJC_CLASS_RO_$_VMVoicemailData
+ __OBJC_CLASS_RO_$_VMVoicemailDataContainer
+ __OBJC_METACLASS_RO_$_VMVoicemailData
+ __OBJC_METACLASS_RO_$_VMVoicemailDataContainer
+ __Z16vm_framework_logv
+ __Z25xx_TUFormattedPhoneNumberP8NSStringS0_
+ __Z31VMVoicemailGetDataFileExtensionv
+ __Z32VMVoicemailDataPathForIdentifierP8NSStringm
+ __Z40VMVoicemailGetSummarizationFileExtensionv
+ __Z40VMVoicemailGetTranscriptionFileExtensionv
+ __Z41VMVoicemailSummarizationPathForIdentifierP8NSStringm
+ __Z41VMVoicemailTranscriptionPathForIdentifierP8NSStringm
+ __ZL39VMVoicemailManagerSerialQueueContextKey
+ __ZSt9terminatev
+ __ZZ16vm_framework_logvE4sLog
+ __ZZ16vm_framework_logvE9onceToken
+ __ZZ35+[VMClientWrapper isVMXPCAvailable]E16isVMXPCAvailable
+ __ZZ35+[VMClientWrapper isVMXPCAvailable]E9onceToken
+ __ZZ46+[VMClientWrapper voicemailClientXPCInterface]E12xpcInterface
+ __ZZ46+[VMClientWrapper voicemailClientXPCInterface]E9onceToken
+ __ZZ46+[VMClientWrapper voicemailServerXPCInterface]E12xpcInterface
+ __ZZ46+[VMClientWrapper voicemailServerXPCInterface]E9onceToken
+ ___49-[VMVoicemailManager voicemailsUpdated:basePath:]_block_invoke
+ ___55-[VMVoicemailManager voicemailsFromContainer:basePath:]_block_invoke
+ ____Z16vm_framework_logv_block_invoke
+ ___block_descriptor_32_e37_q24?0"VMVoicemail"8"VMVoicemail"16l
+ ___block_descriptor_40_ea8_32bs_e17_v16?0"NSError"8ls32l8
+ ___block_descriptor_40_ea8_32bs_e20_v20?0B8"NSError"12ls32l8
+ ___block_descriptor_40_ea8_32bs_e41_v24?0"VMVoicemailGreeting"8"NSError"16ls32l8
+ ___block_descriptor_40_ea8_32bs_e8_v16?0q8ls32l8
+ ___block_descriptor_40_ea8_32r_e17_v16?0"NSArray"8lr32l8
+ ___block_descriptor_40_ea8_32r_e17_v16?0"NSError"8lr32l8
+ ___block_descriptor_40_ea8_32r_e22_v16?0"NSDictionary"8lr32l8
+ ___block_descriptor_40_ea8_32r_e23_v24?0"CNContact"8^B16lr32l8
+ ___block_descriptor_40_ea8_32r_e8_v12?0B8lr32l8
+ ___block_descriptor_40_ea8_32r_e8_v16?0d8lr32l8
+ ___block_descriptor_40_ea8_32r_e8_v16?0q8lr32l8
+ ___block_descriptor_40_ea8_32s_e17_v16?0"NSError"8ls32l8
+ ___block_descriptor_40_ea8_32s_e28_B32?0"VMVoicemail"8Q16^B24ls32l8
+ ___block_descriptor_40_ea8_32s_e31_B32?0"CNLabeledValue"8Q16^B24ls32l8
+ ___block_descriptor_40_ea8_32s_e5_v8?0ls32l8
+ ___block_descriptor_40_ea8_32s_e8_v12?0B8ls32l8
+ ___block_descriptor_40_ea8_32w_e5_v8?0lw32l8
+ ___block_descriptor_41_ea8_32s_e5_v8?0ls32l8
+ ___block_descriptor_44_ea8_32w_e8_v12?0i8lw32l8
+ ___block_descriptor_48_ea8_32r40r_e17_v16?0"NSError"8lr32l8r40l8
+ ___block_descriptor_48_ea8_32r40r_e20_v20?0"NSArray"8B16lr32l8r40l8
+ ___block_descriptor_48_ea8_32r40r_e20_v20?0B8"NSError"12lr32l8r40l8
+ ___block_descriptor_48_ea8_32r40r_e20_v24?0Q8"NSError"16lr32l8r40l8
+ ___block_descriptor_48_ea8_32r40r_e23_v28?0B8Q12"NSError"20lr32l8r40l8
+ ___block_descriptor_48_ea8_32r40r_e30_v24?0"NSString"8"NSError"16lr32l8r40l8
+ ___block_descriptor_48_ea8_32r40r_e32_v28?0B8"NSArray"12"NSError"20lr32l8r40l8
+ ___block_descriptor_48_ea8_32r40r_e37_v28?0B8"NSDictionary"12"NSError"20lr32l8r40l8
+ ___block_descriptor_48_ea8_32r40r_e45_v24?0"VMQuickSwitchParameters"8"NSError"16lr32l8r40l8
+ ___block_descriptor_48_ea8_32r_e28_v32?0"VMVoicemail"8Q16^B24lr32l8
+ ___block_descriptor_48_ea8_32s40bs_e17_v16?0"NSError"8ls32l8s40l8
+ ___block_descriptor_48_ea8_32s40bs_e20_v20?0B8"NSError"12ls32l8s40l8
+ ___block_descriptor_48_ea8_32s40r_e17_v16?0"NSError"8ls32l8r40l8
+ ___block_descriptor_48_ea8_32s40r_e47_v24?0"VMVoicemailDataContainer"8"NSString"16lr40l8s32l8
+ ___block_descriptor_48_ea8_32s40r_e5_v8?0lr40l8s32l8
+ ___block_descriptor_48_ea8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_48_ea8_32s40w_e17_v16?0"NSError"8lw40l8s32l8
+ ___block_descriptor_48_ea8_32s40w_e8_v12?0i8lw40l8s32l8
+ ___block_descriptor_49_ea8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_49_ea8_32s40w_e17_v16?0"NSArray"8lw40l8s32l8
+ ___block_descriptor_49_ea8_32s40w_e28_v16?0"VMVoicemailManager"8lw40l8s32l8
+ ___block_descriptor_50_ea8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_52_ea8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_56_ea8_32r40r48r_e33_v28?0"NSString"8B16"NSError"20lr32l8r40l8r48l8
+ ___block_descriptor_56_ea8_32s40r48r_e17_v16?0"NSError"8ls32l8r40l8r48l8
+ ___block_descriptor_56_ea8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_56_ea8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_56_ea8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_57_ea8_32s40bs48w_e28_v16?0"VMVoicemailManager"8lw48l8s32l8s40l8
+ ___block_descriptor_57_ea8_32s40bs48w_e33_v36?0B8B12B16B20B24"NSNumber"28lw48l8s40l8s32l8
+ ___block_descriptor_57_ea8_32s40bs48w_e47_v24?0"VMVoicemailDataContainer"8"NSString"16lw48l8s40l8s32l8
+ ___block_descriptor_57_ea8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_61_ea8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_72_ea8_32s40s48s56s64s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
+ ___clang_call_terminate
+ ___cxa_begin_catch
+ ___gxx_personality_v0
+ _objc_msgSend$compare:
+ _objc_msgSend$fileURLWithPath:isDirectory:
+ _objc_msgSend$orderedSetWithArray:
+ _objc_msgSend$setCallbackISOCountryCode:
+ _objc_msgSend$setReceiverISOCountryCode:
+ _objc_msgSend$setSenderISOCountryCode:
+ _objc_msgSend$setSummarizationMetaDataURL:
+ _objc_msgSend$sortUsingComparator:
+ _objc_msgSend$stringByAppendingPathComponent:
+ _objc_msgSend$voicemailsFromContainer:basePath:
- -[VMVoicemailManager voicemailsUpdated:]
- GCC_except_table127
- GCC_except_table135
- GCC_except_table196
- GCC_except_table201
- GCC_except_table240
- GCC_except_table28
- GCC_except_table68
- GCC_except_table70
- GCC_except_table72
- GCC_except_table74
- GCC_except_table77
- GCC_except_table79
- GCC_except_table88
- _VMVoicemailManagerSerialQueueContextKey
- ___40-[VMVoicemailManager voicemailsUpdated:]_block_invoke
- ___block_descriptor_40_e8_32bs_e17_v16?0"NSError"8ls32l8
- ___block_descriptor_40_e8_32bs_e20_v20?0B8"NSError"12ls32l8
- ___block_descriptor_40_e8_32bs_e41_v24?0"VMVoicemailGreeting"8"NSError"16ls32l8
- ___block_descriptor_40_e8_32bs_e8_v16?0q8ls32l8
- ___block_descriptor_40_e8_32r_e17_v16?0"NSArray"8lr32l8
- ___block_descriptor_40_e8_32r_e17_v16?0"NSError"8lr32l8
- ___block_descriptor_40_e8_32r_e22_v16?0"NSDictionary"8lr32l8
- ___block_descriptor_40_e8_32r_e23_v24?0"CNContact"8^B16lr32l8
- ___block_descriptor_40_e8_32r_e8_v12?0B8lr32l8
- ___block_descriptor_40_e8_32r_e8_v16?0d8lr32l8
- ___block_descriptor_40_e8_32r_e8_v16?0q8lr32l8
- ___block_descriptor_40_e8_32s_e17_v16?0"NSError"8ls32l8
- ___block_descriptor_40_e8_32s_e28_B32?0"VMVoicemail"8Q16^B24ls32l8
- ___block_descriptor_40_e8_32s_e31_B32?0"CNLabeledValue"8Q16^B24ls32l8
- ___block_descriptor_40_e8_32s_e5_v8?0ls32l8
- ___block_descriptor_40_e8_32s_e8_v12?0B8ls32l8
- ___block_descriptor_40_e8_32w_e5_v8?0lw32l8
- ___block_descriptor_41_e8_32s_e5_v8?0ls32l8
- ___block_descriptor_44_e8_32w_e8_v12?0i8lw32l8
- ___block_descriptor_48_e8_32r40r_e17_v16?0"NSError"8lr32l8r40l8
- ___block_descriptor_48_e8_32r40r_e20_v20?0"NSArray"8B16lr32l8r40l8
- ___block_descriptor_48_e8_32r40r_e20_v20?0B8"NSError"12lr32l8r40l8
- ___block_descriptor_48_e8_32r40r_e20_v24?0Q8"NSError"16lr32l8r40l8
- ___block_descriptor_48_e8_32r40r_e23_v28?0B8Q12"NSError"20lr32l8r40l8
- ___block_descriptor_48_e8_32r40r_e30_v24?0"NSString"8"NSError"16lr32l8r40l8
- ___block_descriptor_48_e8_32r40r_e32_v28?0B8"NSArray"12"NSError"20lr32l8r40l8
- ___block_descriptor_48_e8_32r40r_e37_v28?0B8"NSDictionary"12"NSError"20lr32l8r40l8
- ___block_descriptor_48_e8_32r40r_e45_v24?0"VMQuickSwitchParameters"8"NSError"16lr32l8r40l8
- ___block_descriptor_48_e8_32r_e28_v32?0"VMVoicemail"8Q16^B24lr32l8
- ___block_descriptor_48_e8_32s40bs_e17_v16?0"NSError"8ls32l8s40l8
- ___block_descriptor_48_e8_32s40bs_e20_v20?0B8"NSError"12ls32l8s40l8
- ___block_descriptor_48_e8_32s40r_e17_v16?0"NSError"8ls32l8r40l8
- ___block_descriptor_48_e8_32s40s_e5_v8?0ls32l8s40l8
- ___block_descriptor_48_e8_32s40w_e17_v16?0"NSError"8lw40l8s32l8
- ___block_descriptor_48_e8_32s40w_e8_v12?0i8lw40l8s32l8
- ___block_descriptor_49_e8_32s40s_e5_v8?0ls32l8s40l8
- ___block_descriptor_49_e8_32s40w_e17_v16?0"NSArray"8lw40l8s32l8
- ___block_descriptor_49_e8_32s40w_e28_v16?0"VMVoicemailManager"8lw40l8s32l8
- ___block_descriptor_50_e8_32s40s_e5_v8?0ls32l8s40l8
- ___block_descriptor_52_e8_32s40s_e5_v8?0ls32l8s40l8
- ___block_descriptor_56_e8_32r40r48r_e33_v28?0"NSString"8B16"NSError"20lr32l8r40l8r48l8
- ___block_descriptor_56_e8_32s40r48r_e17_v16?0"NSError"8ls32l8r40l8r48l8
- ___block_descriptor_56_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
- ___block_descriptor_56_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
- ___block_descriptor_56_e8_32s40s_e5_v8?0ls32l8s40l8
- ___block_descriptor_57_e8_32s40bs48w_e22_v16?0"NSOrderedSet"8lw48l8s40l8s32l8
- ___block_descriptor_57_e8_32s40bs48w_e28_v16?0"VMVoicemailManager"8lw48l8s32l8s40l8
- ___block_descriptor_57_e8_32s40bs48w_e33_v36?0B8B12B16B20B24"NSNumber"28lw48l8s40l8s32l8
- ___block_descriptor_57_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
- ___block_descriptor_61_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
- ___block_descriptor_72_e8_32s40s48s56s64s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
- ___vm_framework_log_block_invoke
- _isVMXPCAvailable.isVMXPCAvailable
- _isVMXPCAvailable.onceToken
- _kVMConfidenceControllerTypeBetaHeaderPreferencesKey
- _kVMConfidenceControllerTypeOverallPreferencesKey
- _kVMConfidenceControllerTypeSegmentPreferencesKey
- _kVMSettingsDomain
- _objc_retain_x5
- _vm_framework_log
- _vm_framework_log.onceToken
- _vm_framework_log.sLog
- _voicemailClientXPCInterface.onceToken
- _voicemailClientXPCInterface.xpcInterface
- _voicemailServerXPCInterface.onceToken
- _voicemailServerXPCInterface.xpcInterface
- _xx_TUFormattedPhoneNumber
CStrings:
+ "%@ %p created with %lu voicemail(s)"
+ "%@ %p decoded with %lu voicemail(s)"
+ "%@ %p deleted (%lu voicemail(s))"
+ "%lu%s"
+ ".amr"
+ ".summary"
+ ".transcript"
+ "<%@ %p identifier=%@, uuid=%@, remoteUID=%@, date=%@, sender=%@, senderISO=%@, receiver=%@, receiverISO=%@, labelID=%@, callback=%@, callbackISO=%@, duration=%@, flags=%@>"
+ "VMVoicemailManager.mm"
+ "q24@?0@\"VMVoicemail\"8@\"VMVoicemail\"16"
+ "v24@?0@\"VMVoicemailDataContainer\"8@\"NSString\"16"
- "VMVoicemailManager.m"
- "v16@?0@\"NSOrderedSet\"8"
```
