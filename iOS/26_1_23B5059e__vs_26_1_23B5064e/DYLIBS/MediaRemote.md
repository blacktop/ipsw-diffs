## MediaRemote

> `/System/Library/PrivateFrameworks/MediaRemote.framework/MediaRemote`

```diff

-4025.200.14.0.0
-  __TEXT.__text: 0x2f1a58
+4025.210.17.2.0
+  __TEXT.__text: 0x2f2820
   __TEXT.__auth_stubs: 0x16f0
-  __TEXT.__objc_methlist: 0x2af50
+  __TEXT.__objc_methlist: 0x2afa0
   __TEXT.__const: 0x5f8
-  __TEXT.__cstring: 0x2bae4
+  __TEXT.__cstring: 0x2bb21
   __TEXT.__oslogstring: 0xdb49
   __TEXT.__gcc_except_tab: 0x648c
   __TEXT.__dlopen_cstrs: 0x514
-  __TEXT.__ustring: 0x7a2
-  __TEXT.__unwind_info: 0xb220
+  __TEXT.__ustring: 0x796
+  __TEXT.__unwind_info: 0xb240
   __TEXT.__objc_classname: 0x4d83
-  __TEXT.__objc_methname: 0x4d2c8
-  __TEXT.__objc_methtype: 0x8fd0
-  __TEXT.__objc_stubs: 0x28320
+  __TEXT.__objc_methname: 0x4d38c
+  __TEXT.__objc_methtype: 0x9030
+  __TEXT.__objc_stubs: 0x28380
   __DATA_CONST.__got: 0x1440
-  __DATA_CONST.__const: 0xae18
+  __DATA_CONST.__const: 0xae90
   __DATA_CONST.__objc_classlist: 0x11a0
   __DATA_CONST.__objc_catlist: 0x60
   __DATA_CONST.__objc_protolist: 0x260
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xef78
+  __DATA_CONST.__objc_selrefs: 0xefa8
   __DATA_CONST.__objc_protorefs: 0x88
   __DATA_CONST.__objc_superrefs: 0xfc8
   __DATA_CONST.__objc_arraydata: 0x260
   __AUTH_CONST.__auth_got: 0xb88
   __AUTH_CONST.__const: 0x3080
-  __AUTH_CONST.__cfstring: 0x22fe0
-  __AUTH_CONST.__objc_const: 0x45b00
+  __AUTH_CONST.__cfstring: 0x23000
+  __AUTH_CONST.__objc_const: 0x45b98
   __AUTH_CONST.__objc_arrayobj: 0x180
   __AUTH_CONST.__objc_intobj: 0x4c8
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0x82f0
   __AUTH.__data: 0x10
-  __DATA.__objc_ivar: 0x3220
+  __DATA.__objc_ivar: 0x322c
   __DATA.__data: 0x1ce0
   __DATA.__bss: 0x870
   __DATA.__common: 0x8

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6EB46D04-0FB7-3198-8571-69660CCD8E63
-  Functions: 20132
-  Symbols:   55269
-  CStrings:  24332
+  UUID: A5636B83-BBF1-332B-AAD0-4A6859E71296
+  Functions: 20145
+  Symbols:   55302
+  CStrings:  24346
 
Symbols:
+ -[MRPlaybackSessionMigrateRequest _finalizeRequestWithAnalytics:]
+ -[MRPlaybackSessionMigrateRequest _findEventWithName:role:]
+ -[MRPlaybackSessionMigrateRequest _findEventWithName:role:inEvents:]
+ -[MRPlaybackSessionMigrateRequest _gatherMPPMetricsWithCompletion:]
+ -[MRPlaybackSessionMigrateRequest finalizeWithCompletion:]
+ -[MRPlaybackSessionRequest isPreflight]
+ -[MRPlaybackSessionRequest setIsPreflight:]
+ -[_MRPlaybackSessionRequestProtobuf hasIsPreflight]
+ -[_MRPlaybackSessionRequestProtobuf isPreflight]
+ -[_MRPlaybackSessionRequestProtobuf setHasIsPreflight:]
+ -[_MRPlaybackSessionRequestProtobuf setIsPreflight:]
+ OBJC_IVAR_$__MRPlaybackSessionRequestProtobuf._has
+ OBJC_IVAR_$__MRPlaybackSessionRequestProtobuf._isPreflight
+ _OBJC_IVAR_$_MRPlaybackSessionRequest._isPreflight
+ ___58-[MRPlaybackSessionMigrateRequest finalizeWithCompletion:]_block_invoke
+ ___65-[MRPlaybackSessionMigrateRequest _finalizeRequestWithAnalytics:]_block_invoke
+ ___67-[MRPlaybackSessionMigrateRequest _gatherMPPMetricsWithCompletion:]_block_invoke
+ ___67-[MRPlaybackSessionMigrateRequest _gatherMPPMetricsWithCompletion:]_block_invoke.cold.1
+ ___MRMediaRemotePlaybackSessionIsMigrationPossibleForPlayer_block_invoke_2
+ ____MRPSMPerformLegacyMigration_block_invoke.134
+ ____MRPSMPerformLegacyMigration_block_invoke_2.138
+ ____MRPSMPerformLegacyMigration_block_invoke_3.139
+ ____MRPSMPerformLegacyMigration_block_invoke_4.140
+ ___block_descriptor_48_e8_32s40bs_e56_v32?0"MRPlayerPath"8"MRPlayerPath"16"_MRPSMRecipe"24ls40l8s32l8
+ ___block_descriptor_52_e8_32s40bs_e57_v24?0"MRPlaybackSessionMigratePostMessage"8"NSError"16ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48bs_e22_v16?0"NSDictionary"8ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48bs_e54_v24?0"MRPlaybackSessionResponseMessage"8"NSError"16ls48l8s32l8s40l8
+ _objc_msgSend$finalizeWithCompletion:
+ _objc_msgSend$initWithIdentifier:type:
+ _objc_msgSend$isPreflight
+ _objc_msgSend$setIsPreflight:
- -[MRPlaybackSessionMigrateRequest finalize]
- -[MRPlaybackSessionMigrateRequest finalize].cold.1
- -[MRPlaybackSessionMigrateRequest finalize].cold.2
- ___43-[MRPlaybackSessionMigrateRequest finalize]_block_invoke
- ____MRPSMPerformLegacyMigration_block_invoke.139
- ____MRPSMPerformLegacyMigration_block_invoke_2.143
- ____MRPSMPerformLegacyMigration_block_invoke_3.144
- ____MRPSMPerformLegacyMigration_block_invoke_4.145
- ___block_descriptor_40_e8_32bs_e56_v32?0"MRPlayerPath"8"MRPlayerPath"16"_MRPSMRecipe"24ls32l8
- _objc_msgSend$finalize
CStrings:
+ "%.3fs"
+ "%@/%@/%@/isPreflight:%d"
+ "MPP_firstAudioFrameTimestamp"
+ "MPPfirstAudioFrameTimestamp"
+ "TB,N,V_isPreflight"
+ "_finalizeRequestWithAnalytics:"
+ "_isPreflight"
+ "finalizeWithCompletion:"
+ "hasIsPreflight"
+ "isPreflight"
+ "requestID=%@ failedPlayingAudio=%d"
+ "service:account:inviteDroppedForSessionID:fromID:error:"
+ "setHasIsPreflight:"
+ "setIsPreflight:"
+ "v56@0:8@\"IDSService\"16@\"IDSAccount\"24@\"NSString\"32@\"NSString\"40@\"NSError\"48"
+ "{?=\"isPreflight\"b1}"
- "%@/%@/%@"
- "ClearSourceQueue"
- "finalize"
- "requestID=%@ duration=%f failedPlayingAudio=%d"
- "\xc0\xdbN\xdc"
- "\xc0\xdbO\xdc"

```
