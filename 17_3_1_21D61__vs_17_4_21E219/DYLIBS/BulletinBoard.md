## BulletinBoard

> `/System/Library/PrivateFrameworks/BulletinBoard.framework/BulletinBoard`

```diff

-887.3.0.0.0
+887.101.0.0.0
   __TEXT.__text: 0x7588c
   __TEXT.__auth_stubs: 0x9e0
   __TEXT.__objc_methlist: 0x7580

   __TEXT.__dlopen_cstrs: 0x13e
   __TEXT.__unwind_info: 0x20cc
   __TEXT.__objc_classname: 0xbb3
-  __TEXT.__objc_methname: 0x127eb
+  __TEXT.__objc_methname: 0x127fd
   __TEXT.__objc_methtype: 0x2a5f
   __TEXT.__objc_stubs: 0xcb20
   __DATA_CONST.__got: 0x160

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x10bb0
   __DATA_CONST.__objc_selrefs: 0x3bc0
+  __DATA_CONST.__objc_protorefs: 0x80
+  __DATA_CONST.__objc_classrefs: 0x438
+  __DATA_CONST.__objc_superrefs: 0x208
   __DATA_CONST.__objc_arraydata: 0x140
   __AUTH_CONST.__cfstring: 0x6400
   __AUTH_CONST.__objc_const: 0x2548

   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__auth_got: 0x500
-  __AUTH.__objc_data: 0x550
-  __DATA.__objc_protorefs: 0x80
-  __DATA.__objc_classrefs: 0x438
-  __DATA.__objc_superrefs: 0x208
+  __AUTH.__objc_data: 0x4b0
   __DATA.__objc_ivar: 0x870
   __DATA.__data: 0xec0
   __DATA.__bss: 0xb8
-  __DATA_DIRTY.__objc_data: 0x13b0
+  __DATA_DIRTY.__objc_data: 0x1450
   __DATA_DIRTY.__data: 0x10
   __DATA_DIRTY.__bss: 0x1b8
   __DATA_DIRTY.__common: 0x70

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C6BBDD45-AE63-3E0E-82AC-67C1BBE29A29
+  UUID: 43ED2D5E-462C-36EF-B7D6-CD20F2CC61DD
   Functions: 3386
   Symbols:   10898
-  CStrings:  5462
+  CStrings:  5463
 
Symbols:
+ ___23-[BBServerConduit init]_block_invoke.59
+ ___34-[BBSettingsGateway allSectionIDs]_block_invoke.193
+ ___34-[BBSettingsGateway allSectionIDs]_block_invoke.196
+ ___35-[BBSettingsGateway allSectionInfo]_block_invoke.129
+ ___35-[BBSettingsGateway allSectionInfo]_block_invoke.132
+ ___37-[BBXPCSyncService _ensureConnection]_block_invoke.47
+ ___38-[BBSettingsGateway activeSectionInfo]_block_invoke.183
+ ___38-[BBSettingsGateway activeSectionInfo]_block_invoke.186
+ ___40-[BBSettingsGateway allActiveSectionIDs]_block_invoke.189
+ ___40-[BBSettingsGateway allActiveSectionIDs]_block_invoke.189.cold.1
+ ___44-[BBSettingsGateway allEffectiveSectionInfo]_block_invoke.122
+ ___44-[BBSettingsGateway allEffectiveSectionInfo]_block_invoke.126
+ ___45-[BBSettingsGateway sectionInfoForSectionID:]_block_invoke.171
+ ___45-[BBSettingsGateway sectionInfoForSectionID:]_block_invoke.174
+ ___46-[BBSettingsGateway sectionInfoForSectionIDs:]_block_invoke.142
+ ___46-[BBSettingsGateway sectionInfoForSectionIDs:]_block_invoke.145
+ ___50-[BBSettingsGateway getSectionInfoWithCompletion:]_block_invoke.134
+ ___50-[BBSettingsGateway getSectionInfoWithCompletion:]_block_invoke.134.cold.1
+ ___50-[BBSettingsGateway getSectionInfoWithCompletion:]_block_invoke.137
+ ___50-[BBSettingsGateway getSectionInfoWithCompletion:]_block_invoke.139
+ ___50-[BBSettingsGateway getSectionInfoWithCompletion:]_block_invoke_2.138
+ ___50-[BBSettingsGateway getSectionInfoWithCompletion:]_block_invoke_2.138.cold.1
+ ___51-[BBSettingsGateway effectiveGlobalAnnounceSetting]_block_invoke.219
+ ___54-[BBSettingsGateway _ensureBBServerSettingsConnection]_block_invoke.114
+ ___54-[BBSettingsGateway effectiveSectionInfoForSectionID:]_block_invoke.152
+ ___54-[BBSettingsGateway effectiveSectionInfoForSectionID:]_block_invoke.156
+ ___55-[BBSettingsGateway effectiveSectionInfoForSectionIDs:]_block_invoke.160
+ ___55-[BBSettingsGateway effectiveSectionInfoForSectionIDs:]_block_invoke.163
+ ___55-[BBSettingsGateway setEffectiveGlobalAnnounceSetting:]_block_invoke.214
+ ___57-[BBSettingsGateway _ensureSettingsPersistenceConnection]_block_invoke.118
+ ___58-[BBSettingsGateway effectiveGlobalAnnounceCarPlaySetting]_block_invoke.235
+ ___58-[BBSettingsGateway effectiveGlobalContentPreviewsSetting]_block_invoke.209
+ ___58-[BBSettingsGateway effectiveGlobalScheduledDeliveryTimes]_block_invoke.251
+ ___60-[BBSettingsGateway effectiveGlobalScheduledDeliverySetting]_block_invoke.243
+ ___61-[BBSettingsGateway effectiveGlobalAnnounceHeadphonesSetting]_block_invoke.227
+ ___62-[BBSettingsGateway setEffectiveGlobalAnnounceCarPlaySetting:]_block_invoke.230
+ ___62-[BBSettingsGateway setEffectiveGlobalContentPreviewsSetting:]_block_invoke.204
+ ___62-[BBSettingsGateway setEffectiveGlobalScheduledDeliveryTimes:]_block_invoke.246
+ ___63-[BBSettingsGateway getSectionInfoForSectionID:withCompletion:]_block_invoke.177
+ ___64-[BBSettingsGateway getSectionInfoForSectionIDs:withCompletion:]_block_invoke.148
+ ___64-[BBSettingsGateway getSectionInfoForSectionIDs:withCompletion:]_block_invoke_2.149
+ ___64-[BBSettingsGateway setEffectiveGlobalScheduledDeliverySetting:]_block_invoke.238
+ ___65-[BBSettingsGateway setEffectiveGlobalAnnounceHeadphonesSetting:]_block_invoke.222
+ ___67-[BBSettingsGateway getSectionInfoForActiveSectionsWithCompletion:]_block_invoke.199
+ ___71-[BBSettingsGateway effectiveGlobalNotificationListDisplayStyleSetting]_block_invoke.267
+ ___72-[BBSettingsGateway getEffectiveSectionInfoForSectionID:withCompletion:]_block_invoke.180
+ ___73-[BBSettingsGateway getEffectiveSectionInfoForSectionIDs:withCompletion:]_block_invoke.166
+ ___73-[BBSettingsGateway getEffectiveSectionInfoForSectionIDs:withCompletion:]_block_invoke_2.167
+ ___73-[BBSettingsGateway getEffectiveSectionInfoForSectionIDs:withCompletion:]_block_invoke_3.168
+ ___74-[BBRemoteDataProvider deliverResponse:forBulletinRequest:withCompletion:]_block_invoke.167
+ ___75-[BBSettingsGateway effectiveGlobalScheduledDeliveryShowNextSummarySetting]_block_invoke.259
+ ___75-[BBSettingsGateway setEffectiveGlobalNotificationListDisplayStyleSetting:]_block_invoke.262
+ ___79-[BBSettingsGateway setEffectiveGlobalScheduledDeliveryShowNextSummarySetting:]_block_invoke.254
+ ___83-[BBLocalDataProvider initWithPrincipalClass:serverQueue:initializationCompletion:]_block_invoke.420
+ ___BBServerRun_block_invoke.759
+ ___BBServerRun_block_invoke.762
+ ___block_literal_global.105
+ ___block_literal_global.110
+ ___block_literal_global.113
+ ___block_literal_global.117
+ ___block_literal_global.121
+ ___block_literal_global.125
+ ___block_literal_global.131
+ ___block_literal_global.136
+ ___block_literal_global.141
+ ___block_literal_global.144
+ ___block_literal_global.147
+ ___block_literal_global.151
+ ___block_literal_global.156
+ ___block_literal_global.159
+ ___block_literal_global.162
+ ___block_literal_global.165
+ ___block_literal_global.170
+ ___block_literal_global.173
+ ___block_literal_global.176
+ ___block_literal_global.179
+ ___block_literal_global.182
+ ___block_literal_global.185
+ ___block_literal_global.188
+ ___block_literal_global.192
+ ___block_literal_global.195
+ ___block_literal_global.198
+ ___block_literal_global.201
+ ___block_literal_global.203
+ ___block_literal_global.206
+ ___block_literal_global.208
+ ___block_literal_global.213
+ ___block_literal_global.216
+ ___block_literal_global.218
+ ___block_literal_global.221
+ ___block_literal_global.224
+ ___block_literal_global.226
+ ___block_literal_global.229
+ ___block_literal_global.232
+ ___block_literal_global.234
+ ___block_literal_global.237
+ ___block_literal_global.240
+ ___block_literal_global.242
+ ___block_literal_global.245
+ ___block_literal_global.248
+ ___block_literal_global.250
+ ___block_literal_global.253
+ ___block_literal_global.256
+ ___block_literal_global.258
+ ___block_literal_global.261
+ ___block_literal_global.264
+ ___block_literal_global.266
+ ___block_literal_global.42
+ ___block_literal_global.457
+ ___block_literal_global.459
+ ___block_literal_global.462
+ ___block_literal_global.51
+ ___block_literal_global.58
+ ___block_literal_global.61
+ ___block_literal_global.75
+ ___block_literal_global.756
+ ___block_literal_global.761
+ ___block_literal_global.765
+ ___block_literal_global.767
+ ___block_literal_global.769
+ ___block_literal_global.789
+ ___block_literal_global.793
+ ___block_literal_global.795
+ ___block_literal_global.800
+ ___block_literal_global.99
+ _clientInterface.__interface.103
+ _clientInterface.onceToken.102
- ___23-[BBServerConduit init]_block_invoke.58
- ___34-[BBSettingsGateway allSectionIDs]_block_invoke.192
- ___34-[BBSettingsGateway allSectionIDs]_block_invoke.195
- ___35-[BBSettingsGateway allSectionInfo]_block_invoke.128
- ___35-[BBSettingsGateway allSectionInfo]_block_invoke.131
- ___37-[BBXPCSyncService _ensureConnection]_block_invoke.46
- ___38-[BBSettingsGateway activeSectionInfo]_block_invoke.182
- ___38-[BBSettingsGateway activeSectionInfo]_block_invoke.185
- ___40-[BBSettingsGateway allActiveSectionIDs]_block_invoke.188
- ___40-[BBSettingsGateway allActiveSectionIDs]_block_invoke.188.cold.1
- ___44-[BBSettingsGateway allEffectiveSectionInfo]_block_invoke.121
- ___44-[BBSettingsGateway allEffectiveSectionInfo]_block_invoke.125
- ___45-[BBSettingsGateway sectionInfoForSectionID:]_block_invoke.170
- ___45-[BBSettingsGateway sectionInfoForSectionID:]_block_invoke.173
- ___46-[BBSettingsGateway sectionInfoForSectionIDs:]_block_invoke.141
- ___46-[BBSettingsGateway sectionInfoForSectionIDs:]_block_invoke.144
- ___50-[BBSettingsGateway getSectionInfoWithCompletion:]_block_invoke.133
- ___50-[BBSettingsGateway getSectionInfoWithCompletion:]_block_invoke.133.cold.1
- ___50-[BBSettingsGateway getSectionInfoWithCompletion:]_block_invoke.136
- ___50-[BBSettingsGateway getSectionInfoWithCompletion:]_block_invoke.138
- ___50-[BBSettingsGateway getSectionInfoWithCompletion:]_block_invoke_2.137
- ___50-[BBSettingsGateway getSectionInfoWithCompletion:]_block_invoke_2.137.cold.1
- ___51-[BBSettingsGateway effectiveGlobalAnnounceSetting]_block_invoke.218
- ___54-[BBSettingsGateway _ensureBBServerSettingsConnection]_block_invoke.113
- ___54-[BBSettingsGateway effectiveSectionInfoForSectionID:]_block_invoke.151
- ___54-[BBSettingsGateway effectiveSectionInfoForSectionID:]_block_invoke.155
- ___55-[BBSettingsGateway effectiveSectionInfoForSectionIDs:]_block_invoke.159
- ___55-[BBSettingsGateway effectiveSectionInfoForSectionIDs:]_block_invoke.162
- ___55-[BBSettingsGateway setEffectiveGlobalAnnounceSetting:]_block_invoke.213
- ___57-[BBSettingsGateway _ensureSettingsPersistenceConnection]_block_invoke.117
- ___58-[BBSettingsGateway effectiveGlobalAnnounceCarPlaySetting]_block_invoke.234
- ___58-[BBSettingsGateway effectiveGlobalContentPreviewsSetting]_block_invoke.208
- ___58-[BBSettingsGateway effectiveGlobalScheduledDeliveryTimes]_block_invoke.250
- ___60-[BBSettingsGateway effectiveGlobalScheduledDeliverySetting]_block_invoke.242
- ___61-[BBSettingsGateway effectiveGlobalAnnounceHeadphonesSetting]_block_invoke.226
- ___62-[BBSettingsGateway setEffectiveGlobalAnnounceCarPlaySetting:]_block_invoke.229
- ___62-[BBSettingsGateway setEffectiveGlobalContentPreviewsSetting:]_block_invoke.203
- ___62-[BBSettingsGateway setEffectiveGlobalScheduledDeliveryTimes:]_block_invoke.245
- ___63-[BBSettingsGateway getSectionInfoForSectionID:withCompletion:]_block_invoke.176
- ___64-[BBSettingsGateway getSectionInfoForSectionIDs:withCompletion:]_block_invoke.147
- ___64-[BBSettingsGateway getSectionInfoForSectionIDs:withCompletion:]_block_invoke_2.148
- ___64-[BBSettingsGateway setEffectiveGlobalScheduledDeliverySetting:]_block_invoke.237
- ___65-[BBSettingsGateway setEffectiveGlobalAnnounceHeadphonesSetting:]_block_invoke.221
- ___67-[BBSettingsGateway getSectionInfoForActiveSectionsWithCompletion:]_block_invoke.198
- ___71-[BBSettingsGateway effectiveGlobalNotificationListDisplayStyleSetting]_block_invoke.266
- ___72-[BBSettingsGateway getEffectiveSectionInfoForSectionID:withCompletion:]_block_invoke.179
- ___73-[BBSettingsGateway getEffectiveSectionInfoForSectionIDs:withCompletion:]_block_invoke.165
- ___73-[BBSettingsGateway getEffectiveSectionInfoForSectionIDs:withCompletion:]_block_invoke_2.166
- ___73-[BBSettingsGateway getEffectiveSectionInfoForSectionIDs:withCompletion:]_block_invoke_3.167
- ___74-[BBRemoteDataProvider deliverResponse:forBulletinRequest:withCompletion:]_block_invoke.166
- ___75-[BBSettingsGateway effectiveGlobalScheduledDeliveryShowNextSummarySetting]_block_invoke.258
- ___75-[BBSettingsGateway setEffectiveGlobalNotificationListDisplayStyleSetting:]_block_invoke.261
- ___79-[BBSettingsGateway setEffectiveGlobalScheduledDeliveryShowNextSummarySetting:]_block_invoke.253
- ___83-[BBLocalDataProvider initWithPrincipalClass:serverQueue:initializationCompletion:]_block_invoke.419
- ___BBServerRun_block_invoke.758
- ___BBServerRun_block_invoke.761
- ___block_literal_global.104
- ___block_literal_global.109
- ___block_literal_global.112
- ___block_literal_global.116
- ___block_literal_global.120
- ___block_literal_global.124
- ___block_literal_global.127
- ___block_literal_global.130
- ___block_literal_global.135
- ___block_literal_global.140
- ___block_literal_global.143
- ___block_literal_global.146
- ___block_literal_global.150
- ___block_literal_global.154
- ___block_literal_global.158
- ___block_literal_global.161
- ___block_literal_global.164
- ___block_literal_global.169
- ___block_literal_global.172
- ___block_literal_global.175
- ___block_literal_global.178
- ___block_literal_global.181
- ___block_literal_global.184
- ___block_literal_global.187
- ___block_literal_global.191
- ___block_literal_global.194
- ___block_literal_global.197
- ___block_literal_global.200
- ___block_literal_global.202
- ___block_literal_global.205
- ___block_literal_global.207
- ___block_literal_global.212
- ___block_literal_global.215
- ___block_literal_global.217
- ___block_literal_global.220
- ___block_literal_global.225
- ___block_literal_global.228
- ___block_literal_global.231
- ___block_literal_global.233
- ___block_literal_global.236
- ___block_literal_global.239
- ___block_literal_global.241
- ___block_literal_global.244
- ___block_literal_global.247
- ___block_literal_global.249
- ___block_literal_global.252
- ___block_literal_global.255
- ___block_literal_global.257
- ___block_literal_global.260
- ___block_literal_global.263
- ___block_literal_global.265
- ___block_literal_global.45
- ___block_literal_global.456
- ___block_literal_global.458
- ___block_literal_global.461
- ___block_literal_global.74
- ___block_literal_global.755
- ___block_literal_global.760
- ___block_literal_global.764
- ___block_literal_global.766
- ___block_literal_global.768
- ___block_literal_global.788
- ___block_literal_global.792
- ___block_literal_global.794
- ___block_literal_global.799
- _clientInterface.__interface.102
- _clientInterface.onceToken.101
CStrings:
+ "T@\"NSString\",?,R,C"

```
