## MessagesBlastDoorSupport

> `/System/Library/PrivateFrameworks/MessagesBlastDoorSupport.framework/MessagesBlastDoorSupport`

```diff

-295.600.21.0.0
-  __TEXT.__text: 0x43864
-  __TEXT.__auth_stubs: 0x1e60
-  __TEXT.__objc_methlist: 0x5b4
-  __TEXT.__const: 0x2640
-  __TEXT.__cstring: 0xdf9
-  __TEXT.__gcc_except_tab: 0x64
-  __TEXT.__oslogstring: 0x36b
-  __TEXT.__constg_swiftt: 0x800
-  __TEXT.__swift5_typeref: 0xd06
+322.100.2.2.1
+  __TEXT.__text: 0x48c68
+  __TEXT.__objc_methlist: 0x60c
+  __TEXT.__const: 0x2630
+  __TEXT.__cstring: 0x9bc
+  __TEXT.__gcc_except_tab: 0x68
+  __TEXT.__oslogstring: 0x856
+  __TEXT.__constg_swiftt: 0x82c
+  __TEXT.__swift5_typeref: 0xd32
   __TEXT.__swift5_builtin: 0x64
-  __TEXT.__swift5_reflstr: 0x508
-  __TEXT.__swift5_fieldmd: 0x758
+  __TEXT.__swift5_reflstr: 0x538
+  __TEXT.__swift5_fieldmd: 0x774
   __TEXT.__swift5_assocty: 0x198
   __TEXT.__swift5_proto: 0x1ec
-  __TEXT.__swift5_types: 0xb0
-  __TEXT.__swift5_capture: 0xc40
+  __TEXT.__swift5_types: 0xb4
+  __TEXT.__swift5_capture: 0xc80
   __TEXT.__swift_as_entry: 0x8
   __TEXT.__swift_as_ret: 0x8
+  __TEXT.__swift_as_cont: 0xc
   __TEXT.__swift5_mpenum: 0x14
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__unwind_info: 0xbc0
-  __TEXT.__eh_frame: 0xf68
-  __TEXT.__objc_classname: 0x12f
-  __TEXT.__objc_methname: 0x1130
-  __TEXT.__objc_methtype: 0x3f7
-  __TEXT.__objc_stubs: 0xb40
-  __DATA_CONST.__got: 0x7d8
-  __DATA_CONST.__const: 0x1b8
+  __TEXT.__unwind_info: 0xbb0
+  __TEXT.__eh_frame: 0xe80
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x1d8
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x318
+  __DATA_CONST.__objc_selrefs: 0x328
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0xf40
-  __AUTH_CONST.__const: 0x30d8
+  __DATA_CONST.__got: 0x7b8
+  __AUTH_CONST.__const: 0x3230
   __AUTH_CONST.__cfstring: 0x280
-  __AUTH_CONST.__objc_const: 0x428
+  __AUTH_CONST.__objc_const: 0x470
   __AUTH_CONST.__objc_intobj: 0x18
+  __AUTH_CONST.__auth_got: 0x1068
   __AUTH.__objc_data: 0x158
-  __AUTH.__data: 0x458
+  __AUTH.__data: 0x498
   __DATA.__objc_ivar: 0x14
-  __DATA.__data: 0x7b0
-  __DATA.__bss: 0x3490
+  __DATA.__data: 0x8b0
+  __DATA.__bss: 0x3b90
   __DATA.__common: 0x8
-  __DATA_DIRTY.__objc_data: 0x280
-  __DATA_DIRTY.__data: 0x1a8
-  __DATA_DIRTY.__bss: 0x700
+  __DATA_DIRTY.__objc_data: 0x298
+  __DATA_DIRTY.__data: 0xa8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/ImageIO.framework/ImageIO
   - /System/Library/PrivateFrameworks/BlastDoor.framework/BlastDoor
+  - /System/Library/PrivateFrameworks/FeatureFlags.framework/FeatureFlags
   - /System/Library/PrivateFrameworks/LinkPresentationStyleSheetParsing.framework/LinkPresentationStyleSheetParsing
   - /System/Library/PrivateFrameworks/LockdownMode.framework/LockdownMode
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
-  - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
-  - /usr/lib/swift/libswiftVideoToolbox.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: F58C8428-70AB-3CCE-8794-63B8DBDC102D
-  Functions: 1297
-  Symbols:   865
-  CStrings:  313
+  UUID: F5500607-8153-33AA-91BE-22E71B6622A5
+  Functions: 1312
+  Symbols:   1260
+  CStrings:  157
 
Symbols:
+ -[IMMessagesBlastDoorInterface defuseNicknameDictionaryForUnknownSender:withKey:recordTag:processImageFields:resultHandler:]
+ -[IMMessagesBlastDoorInterface initWithBlastDoorInstanceType:senderExemptFromLDM:]
+ -[IMMessagesBlastDoorInterface senderExemptFromLDM]
+ _BlastDoorInstanceTypeUnknownSender
+ __PROPERTIES_IMMessagesBlastDoorInterfaceInternal
+ ___124-[IMMessagesBlastDoorInterface defuseNicknameDictionaryForUnknownSender:withKey:recordTag:processImageFields:resultHandler:]_block_invoke
+ ___block_descriptor_40_e8_32bs_e43_v24?0"BlastDoorBaseNickname"8"NSError"16ls32l8
+ ___swift__destructor
+ ___swift__destructor.2
+ ___swift_allocate_boxed_opaque_existential_1
+ ___swift_async_cont_functlets
+ ___swift_closure_destructor
+ ___swift_closure_destructor.101
+ ___swift_closure_destructor.104
+ ___swift_closure_destructor.107
+ ___swift_closure_destructor.11
+ ___swift_closure_destructor.110
+ ___swift_closure_destructor.113
+ ___swift_closure_destructor.116
+ ___swift_closure_destructor.119
+ ___swift_closure_destructor.122
+ ___swift_closure_destructor.125
+ ___swift_closure_destructor.128
+ ___swift_closure_destructor.132
+ ___swift_closure_destructor.135
+ ___swift_closure_destructor.139
+ ___swift_closure_destructor.14
+ ___swift_closure_destructor.142
+ ___swift_closure_destructor.145
+ ___swift_closure_destructor.148
+ ___swift_closure_destructor.151
+ ___swift_closure_destructor.154
+ ___swift_closure_destructor.157
+ ___swift_closure_destructor.160
+ ___swift_closure_destructor.163
+ ___swift_closure_destructor.166
+ ___swift_closure_destructor.169
+ ___swift_closure_destructor.17
+ ___swift_closure_destructor.172
+ ___swift_closure_destructor.175
+ ___swift_closure_destructor.178
+ ___swift_closure_destructor.181
+ ___swift_closure_destructor.185
+ ___swift_closure_destructor.189
+ ___swift_closure_destructor.193
+ ___swift_closure_destructor.196
+ ___swift_closure_destructor.199
+ ___swift_closure_destructor.199Tm
+ ___swift_closure_destructor.2
+ ___swift_closure_destructor.20
+ ___swift_closure_destructor.203
+ ___swift_closure_destructor.207
+ ___swift_closure_destructor.212
+ ___swift_closure_destructor.217
+ ___swift_closure_destructor.220
+ ___swift_closure_destructor.223
+ ___swift_closure_destructor.23
+ ___swift_closure_destructor.231
+ ___swift_closure_destructor.234
+ ___swift_closure_destructor.238
+ ___swift_closure_destructor.241
+ ___swift_closure_destructor.244
+ ___swift_closure_destructor.248
+ ___swift_closure_destructor.251
+ ___swift_closure_destructor.255
+ ___swift_closure_destructor.258
+ ___swift_closure_destructor.26
+ ___swift_closure_destructor.261
+ ___swift_closure_destructor.265
+ ___swift_closure_destructor.269
+ ___swift_closure_destructor.273
+ ___swift_closure_destructor.276
+ ___swift_closure_destructor.280
+ ___swift_closure_destructor.283
+ ___swift_closure_destructor.287
+ ___swift_closure_destructor.29
+ ___swift_closure_destructor.290
+ ___swift_closure_destructor.294
+ ___swift_closure_destructor.298
+ ___swift_closure_destructor.302
+ ___swift_closure_destructor.306
+ ___swift_closure_destructor.310
+ ___swift_closure_destructor.314
+ ___swift_closure_destructor.318
+ ___swift_closure_destructor.32
+ ___swift_closure_destructor.322
+ ___swift_closure_destructor.326
+ ___swift_closure_destructor.329
+ ___swift_closure_destructor.333
+ ___swift_closure_destructor.337
+ ___swift_closure_destructor.341
+ ___swift_closure_destructor.341Tm
+ ___swift_closure_destructor.344
+ ___swift_closure_destructor.344Tm
+ ___swift_closure_destructor.347
+ ___swift_closure_destructor.35
+ ___swift_closure_destructor.350
+ ___swift_closure_destructor.353
+ ___swift_closure_destructor.356
+ ___swift_closure_destructor.359
+ ___swift_closure_destructor.363
+ ___swift_closure_destructor.367
+ ___swift_closure_destructor.371
+ ___swift_closure_destructor.375
+ ___swift_closure_destructor.379
+ ___swift_closure_destructor.38
+ ___swift_closure_destructor.383
+ ___swift_closure_destructor.387
+ ___swift_closure_destructor.391
+ ___swift_closure_destructor.394
+ ___swift_closure_destructor.398
+ ___swift_closure_destructor.402
+ ___swift_closure_destructor.405
+ ___swift_closure_destructor.409
+ ___swift_closure_destructor.41
+ ___swift_closure_destructor.413
+ ___swift_closure_destructor.417
+ ___swift_closure_destructor.421
+ ___swift_closure_destructor.425
+ ___swift_closure_destructor.429
+ ___swift_closure_destructor.433
+ ___swift_closure_destructor.437
+ ___swift_closure_destructor.44
+ ___swift_closure_destructor.441
+ ___swift_closure_destructor.445
+ ___swift_closure_destructor.449
+ ___swift_closure_destructor.453
+ ___swift_closure_destructor.457
+ ___swift_closure_destructor.461
+ ___swift_closure_destructor.465
+ ___swift_closure_destructor.469
+ ___swift_closure_destructor.47
+ ___swift_closure_destructor.473
+ ___swift_closure_destructor.477
+ ___swift_closure_destructor.481
+ ___swift_closure_destructor.485
+ ___swift_closure_destructor.489
+ ___swift_closure_destructor.493
+ ___swift_closure_destructor.497
+ ___swift_closure_destructor.5
+ ___swift_closure_destructor.50
+ ___swift_closure_destructor.501
+ ___swift_closure_destructor.505
+ ___swift_closure_destructor.509
+ ___swift_closure_destructor.513
+ ___swift_closure_destructor.517
+ ___swift_closure_destructor.521
+ ___swift_closure_destructor.525
+ ___swift_closure_destructor.529
+ ___swift_closure_destructor.53
+ ___swift_closure_destructor.533
+ ___swift_closure_destructor.537
+ ___swift_closure_destructor.541
+ ___swift_closure_destructor.545
+ ___swift_closure_destructor.549
+ ___swift_closure_destructor.553
+ ___swift_closure_destructor.557
+ ___swift_closure_destructor.56
+ ___swift_closure_destructor.561
+ ___swift_closure_destructor.565
+ ___swift_closure_destructor.569
+ ___swift_closure_destructor.573
+ ___swift_closure_destructor.577
+ ___swift_closure_destructor.581
+ ___swift_closure_destructor.585
+ ___swift_closure_destructor.589
+ ___swift_closure_destructor.59
+ ___swift_closure_destructor.593
+ ___swift_closure_destructor.599
+ ___swift_closure_destructor.602
+ ___swift_closure_destructor.605
+ ___swift_closure_destructor.608
+ ___swift_closure_destructor.612
+ ___swift_closure_destructor.62
+ ___swift_closure_destructor.65
+ ___swift_closure_destructor.68
+ ___swift_closure_destructor.71
+ ___swift_closure_destructor.74
+ ___swift_closure_destructor.77
+ ___swift_closure_destructor.8
+ ___swift_closure_destructor.80
+ ___swift_closure_destructor.83
+ ___swift_closure_destructor.86
+ ___swift_closure_destructor.89
+ ___swift_closure_destructor.92
+ ___swift_closure_destructor.95
+ ___swift_closure_destructor.98
+ _memset
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$defuseNicknameDictionaryForUnknownSender:withKey:recordTag:processImageFields:resultHandler:
+ _objc_msgSend$initWithBlastDoorInstanceType:senderExemptFromLDM:
+ _objc_msgSend$initWithBlastDoorInstanceType:senderExemptFromLDM:useUniqueInstance:
+ _objc_msgSend$senderExemptFromLDM
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x5
+ _objc_retain_x6
+ _objc_retain_x7
+ _swift_allocBox
+ _swift_arrayDestroy
+ _swift_deallocBox
+ _swift_release_x1
+ _swift_release_x19
+ _swift_release_x20
+ _swift_release_x21
+ _swift_release_x22
+ _swift_release_x23
+ _swift_release_x24
+ _swift_release_x25
+ _swift_release_x26
+ _swift_release_x27
+ _swift_release_x28
+ _swift_release_x8
+ _swift_retain_x1
+ _swift_retain_x19
+ _swift_retain_x20
+ _swift_retain_x21
+ _swift_retain_x22
+ _swift_retain_x23
+ _swift_retain_x24
+ _swift_retain_x25
+ _swift_retain_x26
+ _swift_retain_x27
+ _swift_retain_x28
+ _swift_retain_x8
+ _symbolic SDyS2iG
+ _symbolic _____ 24MessagesBlastDoorSupport0abcD5PrefsO
+ _symbolic _____SgSo7NSErrorCSgIeyByy_ 9BlastDoor24_ObjCBaseNicknameWrapperC
+ _symbolic _____Sg______pSgIeggg_ 9BlastDoor24_ObjCBaseNicknameWrapperC s5ErrorP
+ _symbolic _____y___________pG s6ResultOsRi_zRi0_zrlE 9BlastDoor12BaseNicknameV s5ErrorP
- _NSGlobalDomain
- _OBJC_CLASS_$_NSUserDefaults
- _OBJC_CLASS_$_OS_os_log
- _OUTLINED_FUNCTION_3
- _OUTLINED_FUNCTION_4
- __swift_FORCE_LOAD_$_swiftCoreMedia
- __swift_FORCE_LOAD_$_swiftCoreMedia_$_MessagesBlastDoorSupport
- __swift_FORCE_LOAD_$_swiftVideoToolbox
- __swift_FORCE_LOAD_$_swiftVideoToolbox_$_MessagesBlastDoorSupport
- _objc_msgSend$objectForKey:inDomain:
- _objc_msgSend$standardUserDefaults
- _objectdestroy.196Tm
- _objectdestroy.321Tm
- _objectdestroy.324Tm
- _symbolic Say_____G s5UInt8V
- _symbolic _____ySwG s5SliceV
- _symbolic _____y______pG s23_ContiguousArrayStorageC s7CVarArgP
- _symbolic ypSg
CStrings:
+ "Defusing combined plugin attachment in BlastDoor (identifier: %{public}s)"
+ "Failed to resolve symlinks in source file: %s"
+ "Failed to resolve symlinks in temporary directory: %s"
+ "Failed to validate TrustKit image format: %s"
+ "Fatal error, unable to get IDSIncomingMessagePushPayload from TLD. %s"
+ "Fatal error, unable to get command from TLD. %s"
+ "Fatal error, unable to get command type from command %s"
+ "Generating TrustKit image for %s with maxPixelDim %s and scale %s"
+ "Generating multi-frame preview for %s maxPixelDim %s and scale %s"
+ "Invoking flow NOT exporting full resolution with maxPixelDim %s and scale %s"
+ "Message unpacking explosion: %{public}s"
+ "Retried message %s: date out of range: original %{public}s, timestamp %{public}s"
+ "Retried message %s: using original %{public}s vs timestamp %{public}s"
+ "Successfully wrote multi-frame image preview (%fs)"
+ "com.apple.Messages.blastdoor.relayGroupMutationUnpacker"
+ "com.apple.Messages.blastdoor.satelliteTextMessageUnpacker"
+ "com.apple.UnknownSendersBlastDoorService"
+ "v24@?0@\"BlastDoorBaseNickname\"8@\"NSError\"16"
- ".cxx_destruct"
- "@\"IMMessagesBlastDoorInterfaceInternal\""
- "@\"NSMutableArray\""
- "@\"NSOutputStream\""
- "@\"NSURL\""
- "@16@0:8"
- "@24@0:8@16"
- "@28@0:8@16B24"
- "@28@0:8@16f24"
- "@32@0:8@16^@24"
- "@32@0:8@16^q24"
- "@40@0:8@16@24^@32"
- "@40@0:8@16f24f28^@32"
- "@48@0:8@16@24@32^@40"
- "ASTC_Persistence"
- "B24@0:8@16"
- "B24@0:8^@16"
- "B40@0:8^{CGImage=}16d24^@32"
- "BlastDoorLiteMessageCompressor"
- "Defusing combined plugin attachment in BlastDoor (identifier: %{public}@)"
- "Failed to resolve symlinks in source file: %@"
- "Failed to resolve symlinks in temporary directory: %@"
- "Failed to validate TrustKit image format: %@"
- "Fatal error, unable to get IDSIncomingMessagePushPayload from TLD. %@"
- "Fatal error, unable to get command from TLD. %@"
- "Fatal error, unable to get command type from command %@"
- "Generating TrustKit image for %@ with maxPixelDim %@ and scale %@"
- "Generating multi-frame preview for %@ maxPixelDim %@ and scale %@"
- "IMCompression"
- "IMMessagesBlastDoorInterface"
- "IMMessagesBlastDoorInterfaceInternal"
- "Invoking flow NOT exporting full resolution with maxPixelDim %@ and scale %@"
- "LDMGlobalEnabled"
- "Message unpacking explosion: %{public}@"
- "OptimizedBitmap_Persistence"
- "Retried message %@: date out of range: original %{public}@, timestamp %{public}@"
- "Retried message %@: using original %{public}@ vs timestamp %{public}@"
- "Successfully wrote multi-frame image preview (%.3fs)"
- "T@\"IMMessagesBlastDoorInterfaceInternal\",&,N,V_interface"
- "T@\"NSMutableArray\",R,N,V_durations"
- "T@\"NSOutputStream\",R,N,V_outputStream"
- "T@\"NSURL\",R,N,V_outputURL"
- "Tf,R,N,V_scale"
- "URLForResource:withExtension:"
- "_TtCV24MessagesBlastDoorSupport21LiteMessageCompressorP33_DA63A1073879EBF040EC5744CF78DBB45Codec"
- "_durations"
- "_imDecompressData"
- "_imOptionallyDecompressData"
- "_interface"
- "_outputStream"
- "_outputURL"
- "_scale"
- "addObject:"
- "bd"
- "bundleForClass:"
- "bytes"
- "close"
- "codec"
- "compressData:codecID:"
- "compressor"
- "copy"
- "count"
- "createDirectoryAtURL:withIntermediateDirectories:attributes:error:"
- "dataWithData:"
- "dataWithLength:"
- "dataWithPropertyList:format:options:error:"
- "dealloc"
- "decontaminateTopLevelDictionary:resultHandler:"
- "defaultManager"
- "defuseBalloonPluginPayload:withIdentifier:context:error:"
- "defuseBalloonPluginPayload:withIdentifier:error:"
- "defuseBalloonPluginPayload:withIdentifier:resultHandler:"
- "defuseChatBotCSS:error:"
- "defuseCollaborationClearNoticePayload:resultHandler:"
- "defuseCollaborationNoticeActionDictionary:resultHandler:"
- "defuseCollaborationNoticePayload:resultHandler:"
- "defuseData:forPreviewType:resultHandler:"
- "defuseLiteRelayTextMessage:error:"
- "defuseLiteTextMessage:error:"
- "defuseNicknameCommand:error:"
- "defuseNicknameDictionary:withKey:recordTag:resultHandler:"
- "defuseNicknameDictionary:withKey:recordTag:wallpaperDataTag:wallpaperLowResDataTag:wallpaperMetadataTag:avatarRecipeDataTag:processImageFields:resultHandler:"
- "defuseNicknameDictionary:withKey:recordTag:wallpaperDataTag:wallpaperLowResDataTag:wallpaperMetadataTag:processImageFields:resultHandler:"
- "defuseNicknameDictionary:withKey:recordTag:wallpaperDataTag:wallpaperLowResDataTag:wallpaperMetadataTag:resultHandler:"
- "defuseRelayGroupMutationPayload:error:"
- "defuseRelayGroupMutationPayloadForData:error:"
- "defuseRelayReachabilityRequestPayload:error:"
- "defuseRelayReachabilityRequestPayloadForData:error:"
- "defuseRelayReachabilityResponsePayload:error:"
- "defuseRelayReachabilityResponsePayloadForData:error:"
- "defuseSMSDictionary:error:"
- "defuseSMSDictionary:resultHandler:"
- "defuseSatelliteSMSTextMessageDictionary:error:"
- "defuseTopLevelDictionary:context:error:"
- "defuseTopLevelDictionary:error:"
- "defuseTopLevelDictionary:resultHandler:"
- "defuseTranscriptBackground:resultHandler:"
- "defuseTranscriptBackgroundCommand:resultHandler:"
- "deleteStream"
- "dictionaryWithObjects:forKeys:count:"
- "durations"
- "enumerateByteRangesUsingBlock:"
- "f"
- "f16@0:8"
- "fileExistsAtPath:"
- "fileURLWithPathComponents:"
- "finalizeASTCWithError:"
- "finalizeOptimizedBitmapWithError:"
- "generateImagePreviewForFileURL:maxPixelDimension:scale:error:"
- "generateMetadataforAttachmentWithfileURL:resultHandler:"
- "generateMovieFramesForAttachmentWithFileURL:targetPixelWidth:targetPixelHeight:frameLimit:uniformSampling:framesPerSync:appliesPreferredTrackTransform:resultHandler:"
- "generateMoviePreviewForAttachmentWithFileURL:maxPixelDimension:minThumbnailPxSize:scale:frameInterval:resultHandler:"
- "generateMoviePreviewForAttachmentWithFileURL:maxPixelDimension:minThumbnailPxSize:scale:resultHandler:"
- "generatePreviewForEmojiImageWithFileURL:frameIndex:maxPixelDimension:resultHandler:"
- "generatePreviewForMultiFrameImageWithFileURL:destinationFileURL:maxPixelDimension:scale:maxFrameCount:isSticker:progressBlock:resultHandler:"
- "generatePreviewForMultiFrameImageWithFileURL:destinationFileURL:maxPixelDimension:scale:maxFrameCount:isSticker:resultHandler:"
- "generatePreviewforAnimatedImageWithfileURL:maxPixelDimension:index:maxCount:resultHandler:"
- "generatePreviewforAttachmentWithfileURL:error:"
- "generatePreviewforAttachmentWithfileURL:maxPixelDimension:scale:resultHandler:"
- "generatePreviewforAttachmentWithfileURL:resultHandler:"
- "generatePreviewforAudioMessageWithfileURL:resultHandler:"
- "generateSpamDetectionPreviewImageForFileURL:maxPixelDimension:scale:resultHandler:"
- "generateWorkoutPreviewForAttachmentWithFileURL:maxPixelDimension:scale:resultHandler:"
- "getMetadataForEmojiImageWithFileURL:maxStrikeCount:resultHandler:"
- "getMetadataforAnimatedImageWithfileURL:maxCount:resultHandler:"
- "increaseLengthBy:"
- "init"
- "initForWritingWithFileURL:scale:"
- "initWithBlastDoorInstanceType:"
- "initWithBlastDoorInstanceType:useUniqueInstance:"
- "interface"
- "length"
- "mutableBytes"
- "numberWithDouble:"
- "numberWithFloat:"
- "objectForKey:inDomain:"
- "open"
- "outputStream"
- "outputStreamWithURL:append:"
- "outputURL"
- "removeItemAtURL:error:"
- "scale"
- "setInterface:"
- "setLength:"
- "setObject:forKeyedSubscript:"
- "standardUserDefaults"
- "streamError"
- "supportsFeature:"
- "type"
- "v16@0:8"
- "v24@0:8@16"
- "v32@0:8@16@?24"
- "v36@0:8@16C24@?28"
- "v40@0:8@16@24@?32"
- "v40@0:8@16f24f28@?32"
- "v40@0:8@16q24@?32"
- "v44@0:8@16q24f32@?36"
- "v48@0:8@16@24@32@?40"
- "v48@0:8@16q24d32@?40"
- "v52@0:8@16f24q28q36@?44"
- "v56@0:8@16f24{CGSize=dd}28f44@?48"
- "v60@0:8@16@24f32f36q40B48@?52"
- "v60@0:8@16f24{CGSize=dd}28f44i48@?52"
- "v64@0:8@16f24{CGSize=dd}28f44q48@?56"
- "v68@0:8@16@24f32f36q40B48@?52@?60"
- "v72@0:8@16@24@32@40@48@56@?64"
- "v72@0:8@16q24q32q40B48q52B60@?64"
- "v76@0:8@16@24@32@40@48@56B64@?68"
- "v84@0:8@16@24@32@40@48@56@64B72@?76"
- "write:maxLength:"
- "writeASTCImage:duration:error:"
- "writeAsOptimizedBitmapWithImage:duration:error:"
- "writePropertyList:toStream:format:options:error:"

```
