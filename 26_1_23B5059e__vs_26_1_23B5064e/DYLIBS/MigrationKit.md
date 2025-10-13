## MigrationKit

> `/System/Library/PrivateFrameworks/MigrationKit.framework/MigrationKit`

```diff

-829.40.175.0.0
-  __TEXT.__text: 0x4ee5b4
-  __TEXT.__auth_stubs: 0x5550
-  __TEXT.__objc_methlist: 0x677c
-  __TEXT.__const: 0x28bc8
-  __TEXT.__oslogstring: 0xcef3
-  __TEXT.__gcc_except_tab: 0x13a4
-  __TEXT.__cstring: 0x1c421
-  __TEXT.__constg_swiftt: 0xcd58
-  __TEXT.__swift5_typeref: 0x9665
-  __TEXT.__swift5_builtin: 0x26c
-  __TEXT.__swift5_reflstr: 0xa2b9
-  __TEXT.__swift5_fieldmd: 0xb8e8
-  __TEXT.__swift5_assocty: 0x1d20
-  __TEXT.__swift5_proto: 0x1d24
-  __TEXT.__swift5_types: 0xb04
-  __TEXT.__swift_as_entry: 0xec0
-  __TEXT.__swift_as_ret: 0x1154
-  __TEXT.__swift5_protos: 0x170
-  __TEXT.__swift5_capture: 0x27f8
+829.40.191.0.0
+  __TEXT.__text: 0x4d082c
+  __TEXT.__auth_stubs: 0x55f0
+  __TEXT.__objc_methlist: 0x6a04
+  __TEXT.__const: 0x299d8
+  __TEXT.__oslogstring: 0xd0a3
+  __TEXT.__gcc_except_tab: 0x13f8
+  __TEXT.__cstring: 0x1d2b1
+  __TEXT.__constg_swiftt: 0xd0ec
+  __TEXT.__swift5_typeref: 0x9a21
+  __TEXT.__swift5_builtin: 0x280
+  __TEXT.__swift5_reflstr: 0xa609
+  __TEXT.__swift5_fieldmd: 0xbabc
+  __TEXT.__swift5_assocty: 0x1e50
+  __TEXT.__swift5_proto: 0x1ee0
+  __TEXT.__swift5_types: 0xafc
+  __TEXT.__swift_as_entry: 0xf14
+  __TEXT.__swift_as_ret: 0x11a8
+  __TEXT.__swift5_protos: 0x190
+  __TEXT.__swift5_capture: 0x2854
   __TEXT.__swift5_mpenum: 0xbc
-  __TEXT.__unwind_info: 0x11c08
-  __TEXT.__eh_frame: 0x2f3b0
-  __TEXT.__objc_classname: 0xd97
-  __TEXT.__objc_methname: 0xfb70
-  __TEXT.__objc_methtype: 0x37f5
-  __TEXT.__objc_stubs: 0x9260
-  __DATA_CONST.__got: 0x1818
-  __DATA_CONST.__const: 0x9c0
+  __TEXT.__unwind_info: 0x123e0
+  __TEXT.__eh_frame: 0x30a70
+  __TEXT.__objc_classname: 0xda9
+  __TEXT.__objc_methname: 0xffa5
+  __TEXT.__objc_methtype: 0x37ea
+  __TEXT.__objc_stubs: 0x97c0
+  __DATA_CONST.__got: 0x1820
+  __DATA_CONST.__const: 0x9b8
   __DATA_CONST.__objc_classlist: 0xac0
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x288
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4710
+  __DATA_CONST.__objc_selrefs: 0x4850
   __DATA_CONST.__objc_protorefs: 0x108
-  __DATA_CONST.__objc_superrefs: 0x308
-  __DATA_CONST.__objc_arraydata: 0x2b0
-  __AUTH_CONST.__auth_got: 0x2ac0
-  __AUTH_CONST.__const: 0x133a0
-  __AUTH_CONST.__cfstring: 0x47a0
-  __AUTH_CONST.__objc_const: 0x186a0
-  __AUTH_CONST.__objc_intobj: 0xca8
+  __DATA_CONST.__objc_superrefs: 0x310
+  __DATA_CONST.__objc_arraydata: 0x488
+  __AUTH_CONST.__auth_got: 0x2b10
+  __AUTH_CONST.__const: 0x13798
+  __AUTH_CONST.__cfstring: 0x5160
+  __AUTH_CONST.__objc_const: 0x189a8
+  __AUTH_CONST.__objc_intobj: 0xcc0
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__objc_arrayobj: 0x168
-  __AUTH.__objc_data: 0x6eb8
-  __AUTH.__data: 0x12c68
-  __DATA.__objc_ivar: 0x758
-  __DATA.__data: 0xae68
-  __DATA.__bss: 0x33cf0
-  __DATA.__common: 0x1330
+  __AUTH_CONST.__objc_arrayobj: 0x210
+  __AUTH.__objc_data: 0x6f08
+  __AUTH.__data: 0x133e8
+  __DATA.__objc_ivar: 0x794
+  __DATA.__data: 0xb2f0
+  __DATA.__bss: 0x35a00
+  __DATA.__common: 0x1380
   __DATA_DIRTY.__objc_data: 0x50
   __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers
   - /System/Library/Frameworks/_LocationEssentials.framework/_LocationEssentials
   - /System/Library/PrivateFrameworks/AccessibilityUtilities.framework/AccessibilityUtilities
+  - /System/Library/PrivateFrameworks/AccountSuggestions.framework/AccountSuggestions
   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
   - /System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices
   - /System/Library/PrivateFrameworks/AppleSRP.framework/AppleSRP

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 224CD530-BB65-307E-8B9D-BD21C013A818
-  Functions: 19095
-  Symbols:   12989
-  CStrings:  8944
+  UUID: 0D816518-1669-3E91-850F-9EDF58A0CA81
+  Functions: 19670
+  Symbols:   13305
+  CStrings:  9228
 
Symbols:
+ -[MKMessage UUID]
+ -[MKMessage account]
+ -[MKMessage attributedBody]
+ -[MKMessage chatStyle]
+ -[MKMessage handles]
+ -[MKMessage setAccount:]
+ -[MKMessage setAttributedBody:]
+ -[MKMessage setChatStyle:]
+ -[MKMessage setHandles:]
+ -[MKMessage setTimestampInNanoseconds:]
+ -[MKMessage setTimestampInSeconds:]
+ -[MKMessage setUUID:]
+ -[MKMessage timestampInNanoseconds]
+ -[MKMessage timestampInSeconds]
+ -[MKMessageAttachment UUID]
+ -[MKMessageAttachment filename]
+ -[MKMessageAttachment setFilename:]
+ -[MKMessageAttachment setTransferState:]
+ -[MKMessageAttachment setUUID:]
+ -[MKMessageAttachment transferState]
+ -[MKMessageAttachment write]
+ -[MKMessageGroup .cxx_destruct]
+ -[MKMessageGroup ID]
+ -[MKMessageGroup init]
+ -[MKMessageGroup roomName]
+ -[MKMessageGroup setID:]
+ -[MKMessageGroup setRoomName:]
+ -[MKMessageMigrator _import2:]
+ -[MKMessageMigrator _import2:].cold.1
+ -[MKMessageMigrator _import2:].cold.2
+ -[MKMessageMigrator _import:].cold.3
+ -[MKMessageMigrator _import:].cold.4
+ -[MKMessageMigrator _import:].cold.5
+ -[MKMessageMigrator _import:].cold.6
+ -[MKMessageMigrator _import:].cold.7
+ -[MKMessageMigrator _import:].cold.8
+ -[MKMessageMigrator _import:].cold.9
+ -[MKMessageMigrator _performSimpleQuery:]
+ -[MKMessageMigrator begin]
+ -[MKMessageMigrator chatIDForMessage:forHandleIDs:withGroup:]
+ -[MKMessageMigrator chatIDForMessage:forHandleIDs:withGroup:].cold.1
+ -[MKMessageMigrator close]
+ -[MKMessageMigrator commit]
+ -[MKMessageMigrator dealloc]
+ -[MKMessageMigrator delete:]
+ -[MKMessageMigrator delete:].cold.1
+ -[MKMessageMigrator delete:].cold.2
+ -[MKMessageMigrator deleteKV:]
+ -[MKMessageMigrator deleteKV:].cold.1
+ -[MKMessageMigrator deleteKV:].cold.2
+ -[MKMessageMigrator deleteKV]
+ -[MKMessageMigrator delete]
+ -[MKMessageMigrator dropTrigger:]
+ -[MKMessageMigrator dropTrigger:].cold.1
+ -[MKMessageMigrator dropTrigger:].cold.2
+ -[MKMessageMigrator dropTriggers]
+ -[MKMessageMigrator handleID:]
+ -[MKMessageMigrator handleIDs:]
+ -[MKMessageMigrator insertAttachment:withMessage:]
+ -[MKMessageMigrator insertAttachment:withMessage:].cold.1
+ -[MKMessageMigrator insertAttachment:withMessage:].cold.2
+ -[MKMessageMigrator insertChatForMessage:forHandleIDs:withGroup:]
+ -[MKMessageMigrator insertChatForMessage:forHandleIDs:withGroup:].cold.1
+ -[MKMessageMigrator insertChatForMessage:forHandleIDs:withGroup:].cold.2
+ -[MKMessageMigrator insertChatForMessage:forHandleIDs:withGroup:].cold.3
+ -[MKMessageMigrator insertHandle:]
+ -[MKMessageMigrator insertHandle:].cold.1
+ -[MKMessageMigrator insertHandle:].cold.2
+ -[MKMessageMigrator insertMessage:forHandleID:withGroup:]
+ -[MKMessageMigrator insertMessage:forHandleID:withGroup:].cold.1
+ -[MKMessageMigrator insertMessage:forHandleID:withGroup:].cold.2
+ -[MKMessageMigrator joinAttachment:message:]
+ -[MKMessageMigrator joinAttachment:message:].cold.1
+ -[MKMessageMigrator joinAttachment:message:].cold.2
+ -[MKMessageMigrator joinChat:handle:]
+ -[MKMessageMigrator joinChat:handle:].cold.1
+ -[MKMessageMigrator joinChat:handle:].cold.2
+ -[MKMessageMigrator joinChat:message:date:]
+ -[MKMessageMigrator joinChat:message:date:].cold.1
+ -[MKMessageMigrator joinChat:message:date:].cold.2
+ -[MKMessageMigrator notify]
+ -[MKMessageMigrator open]
+ -[MKMessageMigrator open].cold.1
+ -[MKMessageMigrator query:]
+ -[MKMessageMigrator query:].cold.1
+ -[MKMessageMigrator query:].cold.2
+ -[MKMessageMigrator rollback]
+ -[MKMessageMigrator updateClient]
+ -[MKMessageMigrator updateClient].cold.1
+ -[MKMessageMigrator updateClient].cold.2
+ -[MKWiFiInterface importWiFiNetworks:error:]
+ -[MKWiFiInterface importWiFiNetworks:error:].cold.1
+ -[MKWiFiInterface importWiFiNetworks:error:].cold.2
+ -[MKWiFiInterface importWiFiNetworks:error:].cold.3
+ _IMCreateSuperFormatStringWithAppendedFileTransfers
+ _OBJC_CLASS_$_IMFileManager
+ _OBJC_CLASS_$_MKMessageGroup
+ _OBJC_CLASS_$_NSArchiver
+ _OBJC_CLASS_$_NSAttributedString
+ _OBJC_IVAR_$_MKMessage._UUID
+ _OBJC_IVAR_$_MKMessage._account
+ _OBJC_IVAR_$_MKMessage._attributedBody
+ _OBJC_IVAR_$_MKMessage._chatStyle
+ _OBJC_IVAR_$_MKMessage._handles
+ _OBJC_IVAR_$_MKMessage._timestampInNanoseconds
+ _OBJC_IVAR_$_MKMessage._timestampInSeconds
+ _OBJC_IVAR_$_MKMessageAttachment._UUID
+ _OBJC_IVAR_$_MKMessageAttachment._filename
+ _OBJC_IVAR_$_MKMessageAttachment._transferState
+ _OBJC_IVAR_$_MKMessageGroup._ID
+ _OBJC_IVAR_$_MKMessageGroup._roomName
+ _OBJC_IVAR_$_MKMessageMigrator._accountGUID
+ _OBJC_IVAR_$_MKMessageMigrator._database
+ _OBJC_IVAR_$_MKMessageMigrator._groups
+ _OBJC_METACLASS_$_MKMessageGroup
+ __OBJC_$_INSTANCE_METHODS_MKMessageGroup
+ __OBJC_$_INSTANCE_VARIABLES_MKMessageGroup
+ __OBJC_$_PROP_LIST_MKMessageGroup
+ __OBJC_CLASS_RO_$_MKMessageGroup
+ __OBJC_METACLASS_RO_$_MKMessageGroup
+ ___29-[MKMessageMigrator _import:]_block_invoke
+ ___block_descriptor_32_e31_q24?0"NSNumber"8"NSNumber"16l
+ ___swift_allocate_boxed_opaque_existential_3Tm
+ ___swift_get_extra_inhabitant_index.190Tm
+ ___swift_get_extra_inhabitant_index.72Tm
+ ___swift_mutable_project_boxed_opaque_existential_2
+ ___swift_store_extra_inhabitant_index.191Tm
+ ___swift_store_extra_inhabitant_index.73Tm
+ ___unnamed_9
+ _associated conformance 12MigrationKit12ContactPhotoVAA22FileContentConvertibleAA0F0AaDP_AA0eF0
+ _associated conformance 12MigrationKit15EventAttachmentVAA22FileContentConvertibleAA0F0AaDP_AA0eF0
+ _associated conformance 12MigrationKit17CardAsyncSequenceVAA015InMemoryContentdE0AA7SuccessAA0hdE0P_AA0fgH11Convertible
+ _associated conformance 12MigrationKit17CardAsyncSequenceVScIAA7FailureScI_s5Error
+ _associated conformance 12MigrationKit17CardAsyncSequenceVSciAA0D8IteratorSci_ScI
+ _associated conformance 12MigrationKit17OnDiskFileContentVyxGAA0eF0AA8MetadataAaEP_AA03HaseF0
+ _associated conformance 12MigrationKit17OnDiskFileContentVyxGAA0eF0AA8MetadataAaEP_AA16HasExportFailure
+ _associated conformance 12MigrationKit19InMemoryDataContentVyxGAA0cdF0AA8MetadataAaEP_21InternalSwiftProtobuf7Message
+ _associated conformance 12MigrationKit19InMemoryDataContentVyxGAA0cdF0AA8MetadataAaEP_AA16HasExportFailure
+ _associated conformance 12MigrationKit20ContactPhotoSequenceVAA016FileContentAsyncE0AA7SuccessAA0ghE0P_AA0fG11Convertible
+ _associated conformance 12MigrationKit20ContactPhotoSequenceVScIAA7FailureScI_s5Error
+ _associated conformance 12MigrationKit20ContactPhotoSequenceVSciAA13AsyncIteratorSci_ScI
+ _associated conformance 12MigrationKit21OSMigrationMusicTrackVAA22FileContentConvertibleAA0G0AaDP_AA0fG0
+ _associated conformance 12MigrationKit23MusicTrackAsyncSequenceVAA011FileContenteF0AA7SuccessAA0heF0P_AA0gH11Convertible
+ _associated conformance 12MigrationKit23MusicTrackAsyncSequenceVScIAA7FailureScI_s5Error
+ _associated conformance 12MigrationKit23MusicTrackAsyncSequenceVSciAA0E8IteratorSci_ScI
+ _associated conformance 12MigrationKit24OSMigrationExportFailureV21InternalSwiftProtobuf26_MessageImplementationBaseAASH
+ _associated conformance 12MigrationKit24OSMigrationExportFailureV21InternalSwiftProtobuf26_MessageImplementationBaseAaD0I0
+ _associated conformance 12MigrationKit24OSMigrationExportFailureV21InternalSwiftProtobuf7MessageAAs28CustomDebugStringConvertible
+ _associated conformance 12MigrationKit24OSMigrationExportFailureVSHAASQ
+ _associated conformance 12MigrationKit24OSMigrationMusicPlaylistVAA9BatchableAA5BatchAaDP_AA13ObjectContent
+ _associated conformance 12MigrationKit24ObjectBatchAsyncSequenceV8IteratorVyx_GScIAA7FailureScI_s5Error
+ _associated conformance 12MigrationKit24ObjectBatchAsyncSequenceVyxGSciAA0E8IteratorSci_ScI
+ _associated conformance 12MigrationKit26MusicPlaylistAsyncSequenceVAA013ObjectContenteF0AA7SuccessAA0heF0P_21InternalSwiftProtobuf7Message
+ _associated conformance 12MigrationKit26MusicPlaylistAsyncSequenceVAA013ObjectContenteF0AA7SuccessAA0heF0P_AA9Batchable
+ _associated conformance 12MigrationKit26MusicPlaylistAsyncSequenceVScIAA7FailureScI_s5Error
+ _associated conformance 12MigrationKit29OSMigrationExportFailureStateO21InternalSwiftProtobuf4EnumAASH
+ _associated conformance 12MigrationKit29OSMigrationExportFailureStateO21InternalSwiftProtobuf4EnumAASY
+ _associated conformance 12MigrationKit29OSMigrationExportFailureStateOSHAASQ
+ _associated conformance 12MigrationKit29OSMigrationExportFailureStateOs12CaseIterableAA8AllCasessADP_Sl
+ _associated conformance 12MigrationKit30OSMigrationFileContentResponseV21InternalSwiftProtobuf26_MessageImplementationBaseAASH
+ _associated conformance 12MigrationKit30OSMigrationFileContentResponseV21InternalSwiftProtobuf26_MessageImplementationBaseAaD0J0
+ _associated conformance 12MigrationKit30OSMigrationFileContentResponseV21InternalSwiftProtobuf7MessageAAs28CustomDebugStringConvertible
+ _associated conformance 12MigrationKit30OSMigrationFileContentResponseVSHAASQ
+ _associated conformance 12MigrationKit31OSMigrationExportFailureSummaryV21InternalSwiftProtobuf26_MessageImplementationBaseAASH
+ _associated conformance 12MigrationKit31OSMigrationExportFailureSummaryV21InternalSwiftProtobuf26_MessageImplementationBaseAaD0J0
+ _associated conformance 12MigrationKit31OSMigrationExportFailureSummaryV21InternalSwiftProtobuf7MessageAAs28CustomDebugStringConvertible
+ _associated conformance 12MigrationKit31OSMigrationExportFailureSummaryVSHAASQ
+ _associated conformance 12MigrationKit31VoiceMemoRecordingAsyncSequenceVAA011FileContentfG0AA7SuccessAA0ifG0P_AA0hI11Convertible
+ _associated conformance 12MigrationKit31VoiceMemoRecordingAsyncSequenceVScIAA7FailureScI_s5Error
+ _associated conformance 12MigrationKit35FileContentConvertibleAsyncSequenceVyxGAA0cdfG0AA7SuccessAA0dfG0P_AA0cdE0
+ _associated conformance 12MigrationKit35FileContentConvertibleAsyncSequenceVyxGScIAA7FailureScI_s5Error
+ _associated conformance 12MigrationKit35FileContentConvertibleAsyncSequenceVyxGSciAA0F8IteratorSci_ScI
+ _associated conformance 12MigrationKit4CardVAA26InMemoryContentConvertibleAA0F0AaDP_AA0deF0
+ _associated conformance 12MigrationKit9VoiceMemoVAA22FileContentConvertibleAA0F0AaDP_AA0eF0
+ _associated conformance 12MigrationKit9WallpaperVAA22FileContentConvertibleAA0E0AaDP_AA0dE0
+ _associated conformance So18ACAccountDataclassaSHSCSQ
+ _associated conformance So18ACAccountDataclassas20_SwiftNewtypeWrapperSCSY
+ _associated conformance So18ACAccountDataclassas20_SwiftNewtypeWrapperSCs35_HasCustomAnyHashableRepresentation
+ _get_witness_table 12MigrationKit17OnDiskFileContentVyAA21OSMigrationMusicTrackVGAA0eF0HPyHC.1
+ _get_witness_table 12MigrationKit17OnDiskFileContentVyAA28OSMigrationVoiceMemoMetadataVGAA0eF0HPyHC.2
+ _objc_msgSend$addKnownNetworksForMigration:error:
+ _objc_msgSend$archivedDataWithRootObject:
+ _objc_msgSend$attributedBody
+ _objc_msgSend$chatIDForMessage:forHandleIDs:withGroup:
+ _objc_msgSend$defaultHFSFileManager
+ _objc_msgSend$delete:
+ _objc_msgSend$deleteKV
+ _objc_msgSend$deleteKV:
+ _objc_msgSend$dropTrigger:
+ _objc_msgSend$dropTriggers
+ _objc_msgSend$generatedRoomNameForGroupChat
+ _objc_msgSend$getCString:maxLength:encoding:
+ _objc_msgSend$handleID:
+ _objc_msgSend$handleIDs:
+ _objc_msgSend$handles
+ _objc_msgSend$hash
+ _objc_msgSend$insertAttachment:withMessage:
+ _objc_msgSend$insertChatForMessage:forHandleIDs:withGroup:
+ _objc_msgSend$insertHandle:
+ _objc_msgSend$insertMessage:forHandleID:withGroup:
+ _objc_msgSend$isSent
+ _objc_msgSend$joinAttachment:message:
+ _objc_msgSend$joinChat:handle:
+ _objc_msgSend$joinChat:message:date:
+ _objc_msgSend$makeDirectoriesInPath:mode:
+ _objc_msgSend$notify
+ _objc_msgSend$numberWithLongLong:
+ _objc_msgSend$pathExtensionForMIMEType:
+ _objc_msgSend$pathExtensionForUTIType:
+ _objc_msgSend$recipients
+ _objc_msgSend$roomName
+ _objc_msgSend$sender
+ _objc_msgSend$setAttributedBody:
+ _objc_msgSend$setHandles:
+ _objc_msgSend$setRoomName:
+ _objc_msgSend$setTimestampInNanoseconds:
+ _objc_msgSend$setTimestampInSeconds:
+ _objc_msgSend$setTransferState:
+ _objc_msgSend$setUUID:
+ _objc_msgSend$stringByResolvingAndStandardizingPath
+ _objc_msgSend$timestampInNanoseconds
+ _objc_msgSend$timestampInSeconds
+ _objc_msgSend$transferState
+ _objc_msgSend$uniformTypeIdentifier
+ _objc_msgSend$updateClient
+ _objc_msgSend$write
+ _sqlite3_bind_blob
+ _sqlite3_bind_int
+ _symbolic $s12MigrationKit14HasFileContentP
+ _symbolic $s12MigrationKit15InMemoryContentP
+ _symbolic $s12MigrationKit16HasContentStreamP
+ _symbolic $s12MigrationKit16HasExportFailureP
+ _symbolic $s12MigrationKit18ObjectBatchContentP
+ _symbolic $s12MigrationKit22HasResourceContentTypeP
+ _symbolic $s12MigrationKit23HasExportFailureSummaryP
+ _symbolic $s12MigrationKit26InMemoryContentConvertibleP
+ _symbolic $s12MigrationKit28InMemoryContentAsyncSequenceP
+ _symbolic 7Content_____Qz 12MigrationKit26InMemoryContentConvertibleP
+ _symbolic 8Metadata_____Qz 12MigrationKit15InMemoryContentP
+ _symbolic SaySo38PKExternalDeviceMigrationManifestEntryCG
+ _symbolic Say_____G 12MigrationKit29OSMigrationExportFailureStateO
+ _symbolic ScTy_____Sg______pG 12MigrationKit18OSMigrationV1FrameV06OneOf_E0O s5ErrorP
+ _symbolic ScTy_____Sg______pG 12MigrationKit36OSMigrationTargetToSourceFlowControlV06OneOf_defgH0O s5ErrorP
+ _symbolic Si_____Sg______pIegHyrzo_ 12MigrationKit18OSMigrationV1FrameV06OneOf_E0O s5ErrorP
+ _symbolic Si_____Sg______pIegHyrzo_ 12MigrationKit36OSMigrationTargetToSourceFlowControlV06OneOf_defgH0O s5ErrorP
+ _symbolic Si___________pIegHyrzo_ 10Foundation3URLV s5ErrorP
+ _symbolic Si___________pIegHyrzo_ 12MigrationKit13AppPropertiesV s5ErrorP
+ _symbolic So41PKExternalDeviceMigrationExportControllerC
+ _symbolic _____ 12MigrationKit17CardAsyncSequenceV
+ _symbolic _____ 12MigrationKit19AccountLazyMigratorV
+ _symbolic _____ 12MigrationKit19InMemoryDataContentV
+ _symbolic _____ 12MigrationKit20ContactPhotoSequenceV
+ _symbolic _____ 12MigrationKit20PersistedAccountDataV
+ _symbolic _____ 12MigrationKit23MusicTrackAsyncSequenceV
+ _symbolic _____ 12MigrationKit24OSMigrationExportFailureV
+ _symbolic _____ 12MigrationKit24ObjectBatchAsyncSequenceV
+ _symbolic _____ 12MigrationKit24ObjectBatchAsyncSequenceV8IteratorV
+ _symbolic _____ 12MigrationKit29OSMigrationExportFailureStateO
+ _symbolic _____ 12MigrationKit30OSMigrationFileContentResponseV
+ _symbolic _____ 12MigrationKit31OSMigrationExportFailureSummaryV
+ _symbolic _____ 12MigrationKit35FileContentConvertibleAsyncSequenceV
+ _symbolic _____ 12MigrationKit9VoiceMemoV
+ _symbolic _____ So18ACAccountDataclassa
+ _symbolic _____Sg 12MigrationKit24OSMigrationExportFailureV
+ _symbolic _____Sg 12MigrationKit29OSMigrationExportFailureStateO
+ _symbolic _____Sg 12MigrationKit31OSMigrationExportFailureSummaryV
+ _symbolic _____Sg_ABt 12MigrationKit24OSMigrationExportFailureV
+ _symbolic _____Sg_ABt 12MigrationKit31OSMigrationExportFailureSummaryV
+ _symbolic ______p 12MigrationKit13ObjectContentP
+ _symbolic ______p 12MigrationKit15InMemoryContentP
+ _symbolic ______p 12MigrationKit28InMemoryContentAsyncSequenceP
+ _symbolic ______pSg 21InternalSwiftProtobuf7MessageP
+ _symbolic ______p___________pIeghHnozo_ 12MigrationKit13ObjectContentP AA16HTTPPartResponseC s5ErrorP
+ _symbolic ______p______pSgIeghHnr_ 12MigrationKit26InMemoryContentConvertibleP AA0cdE0P
+ _symbolic _____yAAy__________G______pG s31AsyncThrowingCompactMapSequenceV 12MigrationKit04CardaE0V AC0H0V AC15InMemoryContentP
+ _symbolic _____ySaySo38PKExternalDeviceMigrationManifestEntryCGG s16IndexingIteratorV
+ _symbolic _____y_____G 12MigrationKit17OnDiskFileContentV AA21OSMigrationMusicTrackV
+ _symbolic _____y_____G 12MigrationKit17OnDiskFileContentV AA25OSMigrationWallpaperAssetV
+ _symbolic _____y_____G 12MigrationKit17OnDiskFileContentV AA29OSMigrationCalendarAttachmentV
+ _symbolic _____y_____G 12MigrationKit17OnDiskFileContentV AA31OSMigrationContactPhotoMetadataV
+ _symbolic _____y_____G 12MigrationKit19InMemoryDataContentV AA34OSMigrationWalletCardManifestEntryV
+ _symbolic _____y_____G 12MigrationKit24ObjectBatchAsyncSequenceV AA17OSMigrationAlarmsV
+ _symbolic _____y_____G 12MigrationKit24ObjectBatchAsyncSequenceV AA20OSMigrationCallArrayV
+ _symbolic _____y_____G 12MigrationKit24ObjectBatchAsyncSequenceV AA23OSMigrationAccountArrayV
+ _symbolic _____y_____G 12MigrationKit24ObjectBatchAsyncSequenceV AA23OSMigrationContactArrayV
+ _symbolic _____y_____G 12MigrationKit24ObjectBatchAsyncSequenceV AA24OSMigrationCalendarArrayV
+ _symbolic _____y_____G 12MigrationKit24ObjectBatchAsyncSequenceV AA29OSMigrationCalendarEventArrayV
+ _symbolic _____y_____G 12MigrationKit35FileContentConvertibleAsyncSequenceV AA15EventAttachmentV
+ _symbolic _____y_____G 12MigrationKit35FileContentConvertibleAsyncSequenceV AA9WallpaperV
+ _symbolic _____y_____G 9SwiftData15FetchDescriptorV 12MigrationKit18AccountPersistenceC
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 12MigrationKit20PersistedAccountDataV
+ _symbolic _____y______QPG 10Foundation9PredicateV 12MigrationKit18AccountPersistenceC
+ _symbolic _____y______QPGSg 10Foundation9PredicateV 12MigrationKit18AccountPersistenceC
+ _symbolic _____y__________G s31AsyncThrowingCompactMapSequenceV 12MigrationKit04CardaE0V AC0H0V
+ _symbolic _____y___________pG s6ResultOsRi_zRi0_zrlE 12MigrationKit15EventAttachmentV s5ErrorP
+ _symbolic _____y___________pG s6ResultOsRi_zRi0_zrlE 12MigrationKit21OSMigrationMusicTrackV s5ErrorP
+ _symbolic _____y___________pG s6ResultOsRi_zRi0_zrlE 12MigrationKit24OSMigrationMusicPlaylistV s5ErrorP
+ _symbolic _____y___________pG s6ResultOsRi_zRi0_zrlE 12MigrationKit4CardV s5ErrorP
+ _symbolic _____y___________pG s6ResultOsRi_zRi0_zrlE 12MigrationKit9VoiceMemoV s5ErrorP
+ _symbolic _____y___________pG s6ResultOsRi_zRi0_zrlE 12MigrationKit9WallpaperV s5ErrorP
+ _symbolic _____y___________pGSg s6ResultOsRi_zRi0_zrlE 12MigrationKit15EventAttachmentV s5ErrorP
+ _symbolic _____y___________pGSg s6ResultOsRi_zRi0_zrlE 12MigrationKit21OSMigrationMusicTrackV s5ErrorP
+ _symbolic _____y___________pGSg s6ResultOsRi_zRi0_zrlE 12MigrationKit24OSMigrationMusicPlaylistV s5ErrorP
+ _symbolic _____y___________pGSg s6ResultOsRi_zRi0_zrlE 12MigrationKit9WallpaperV s5ErrorP
+ _symbolic _____y___________p_GSg Scs8IteratorV 16MusicKitInternal13MigratedTrackV s5ErrorP
+ _symbolic _____y___________p_GSg Scs8IteratorV 16MusicKitInternal16MigratedPlaylistV s5ErrorP
+ _symbolic _____y_____yABy__________G______pGG s22AsyncDropFirstSequenceV s0a18ThrowingCompactMapD0V 12MigrationKit04CardaD0V AE0J0V AE15InMemoryContentP
+ _symbolic _____y_____y_____G_____G s31AsyncThrowingCompactMapSequenceV 12MigrationKit05ArrayaE0V 10Foundation4DataV AC16HTTPPartResponseC
+ _symbolic _____y_____y_____yACy__________G______pGG_____G s24AsyncThrowingMapSequenceV s0a9DropFirstD0V s0ab7CompactcD0V 12MigrationKit04CardaD0V AG0J0V AG15InMemoryContentP AG16HTTPPartResponseC
+ _symbolic _____yxG 12MigrationKit35FileContentConvertibleAsyncSequenceV
+ _symbolic _____yx_G 12MigrationKit24ObjectBatchAsyncSequenceV8IteratorV
+ _symbolic _____yx______pG s6ResultOsRi_zRi0_zrlE s5ErrorP
+ _type_layout_string 12MigrationKit12ContactPhotoV
+ _type_layout_string 12MigrationKit18ObjectBatchContentRzlAA0cD13AsyncSequenceV8IteratorVyx_G
+ _type_layout_string 12MigrationKit18ObjectBatchContentRzlAA0cD13AsyncSequenceVyxG
+ _type_layout_string 12MigrationKit19AccountLazyMigratorV
+ _type_layout_string 12MigrationKit20PersistedAccountDataV
- +[MKWiFiInterface _mkPrivateMacAddressType:]
- +[MKWiFiInterface _mkSecurityType:]
- _OBJC_CLASS_$_CWFNetworkProfile
- __DATA__TtC12MigrationKit21HTTPMultipartResponse
- __IVARS__TtC12MigrationKit21HTTPMultipartResponse
- __METACLASS_DATA__TtC12MigrationKit21HTTPMultipartResponse
- __OBJC_$_CLASS_METHODS_MKWiFiInterface
- ___27-[MKMessageMigrator import]_block_invoke
- ___block_descriptor_40_e8_32s_e5_v8?0ls32l8
- ___swift_get_extra_inhabitant_index.181Tm
- ___swift_get_extra_inhabitant_index.54Tm
- ___swift_store_extra_inhabitant_index.182Tm
- ___swift_store_extra_inhabitant_index.55Tm
- ___unnamed_10
- _associated conformance 12MigrationKit15ContactExporterV0C13PhotoSequenceVSTAA8IteratorST_St
- _associated conformance 12MigrationKit21CardMultipartResponseV8IteratorVScIAA7FailureScI_s5Error
- _associated conformance 12MigrationKit21CardMultipartResponseVSciAA13AsyncIteratorSci_ScI
- _associated conformance 12MigrationKit26MusicPlaylistAsyncSequenceV8IteratorVScIAA7FailureScI_s5Error
- _associated conformance 12MigrationKit26RecordingMultipartResponseV8IteratorVScIAA7FailureScI_s5Error
- _associated conformance 12MigrationKit26RecordingMultipartResponseVSciAA13AsyncIteratorSci_ScI
- _associated conformance 12MigrationKit26WallpaperMultipartResponseV8IteratorVScIAA7FailureScI_s5Error
- _associated conformance 12MigrationKit26WallpaperMultipartResponseVSciAA13AsyncIteratorSci_ScI
- _associated conformance 12MigrationKit27MusicTrackMultipartResponseV8IteratorVScIAA7FailureScI_s5Error
- _associated conformance 12MigrationKit27MusicTrackMultipartResponseVSciAA13AsyncIteratorSci_ScI
- _associated conformance 12MigrationKit29HTTPPartResponseAsyncSequenceV8IteratorVyx_GScIAA7FailureScI_s5Error
- _associated conformance 12MigrationKit29HTTPPartResponseAsyncSequenceVyxGSciAA0E8IteratorSci_ScI
- _associated conformance 12MigrationKit31VoiceMemoRecordingAsyncSequenceV8IteratorVScIAA7FailureScI_s5Error
- _associated conformance 12MigrationKit32EventAttachmentMultipartResponseV8IteratorVScIAA7FailureScI_s5Error
- _associated conformance 12MigrationKit32EventAttachmentMultipartResponseVSciAA13AsyncIteratorSci_ScI
- _block_copy_helper.4
- _block_descriptor.6
- _block_destroy_helper.5
- _flat unique ST_px7ElementSTRts_XP
- _objc_msgSend$_mkPrivateMacAddressType:
- _objc_msgSend$_mkSecurityType:
- _objc_msgSend$importWithCompletion:
- _symbolic $s12MigrationKit14MusicConverterP
- _symbolic 7ElementSTQyd__
- _symbolic So34PKExternalDeviceMigrationCardEntryC_SSt
- _symbolic _____ 12MigrationKit15ContactExporterV0C13PhotoSequenceV
- _symbolic _____ 12MigrationKit15ContactExporterV0C13PhotoSequenceV8IteratorV
- _symbolic _____ 12MigrationKit21CardMultipartResponseV
- _symbolic _____ 12MigrationKit21CardMultipartResponseV8IteratorV
- _symbolic _____ 12MigrationKit21HTTPMultipartResponseC
- _symbolic _____ 12MigrationKit26MusicPlaylistAsyncSequenceV8IteratorV
- _symbolic _____ 12MigrationKit26RecordingMultipartResponseV
- _symbolic _____ 12MigrationKit26RecordingMultipartResponseV8IteratorV
- _symbolic _____ 12MigrationKit26WallpaperMultipartResponseV
- _symbolic _____ 12MigrationKit26WallpaperMultipartResponseV8IteratorV
- _symbolic _____ 12MigrationKit27MusicTrackMultipartResponseV
- _symbolic _____ 12MigrationKit27MusicTrackMultipartResponseV8IteratorV
- _symbolic _____ 12MigrationKit29HTTPPartResponseAsyncSequenceV
- _symbolic _____ 12MigrationKit29HTTPPartResponseAsyncSequenceV8IteratorV
- _symbolic _____ 12MigrationKit31VoiceMemoRecordingAsyncSequenceV8IteratorV
- _symbolic _____ 12MigrationKit32EventAttachmentMultipartResponseV
- _symbolic _____ 12MigrationKit32EventAttachmentMultipartResponseV8IteratorV
- _symbolic _____9multipart_t 12MigrationKit21HTTPMultipartResponseC
- _symbolic _____Sg 12MigrationKit21OSMigrationMusicTrackV
- _symbolic _____Sg 12MigrationKit29OSMigrationMusicPlaylistArrayV
- _symbolic _____Sg 12MigrationKit4CardV
- _symbolic __________Xj lST_px7ElementRts_XPXGMq 12MigrationKit16HTTPPartResponseC
- _symbolic ________________pXj r0_lScI_px7ElementRts_q_7FailureRtsXPXGMq 12MigrationKit15EventAttachmentV s5ErrorP
- _symbolic ________________pXj r0_lScI_px7ElementRts_q_7FailureRtsXPXGMq 12MigrationKit21OSMigrationMusicTrackV s5ErrorP
- _symbolic ________________pXj r0_lScI_px7ElementRts_q_7FailureRtsXPXGMq 12MigrationKit4CardV s5ErrorP
- _symbolic ________________pXj r0_lScI_px7ElementRts_q_7FailureRtsXPXGMq 12MigrationKit9WallpaperV s5ErrorP
- _symbolic ________________pXj r0_lSci_px7ElementRts_q_7FailureRtsXPXGMq 12MigrationKit15EventAttachmentV s5ErrorP
- _symbolic ________________pXj r0_lSci_px7ElementRts_q_7FailureRtsXPXGMq 12MigrationKit21OSMigrationMusicTrackV s5ErrorP
- _symbolic ________________pXj r0_lSci_px7ElementRts_q_7FailureRtsXPXGMq 12MigrationKit4CardV s5ErrorP
- _symbolic ________________pXj r0_lSci_px7ElementRts_q_7FailureRtsXPXGMq 12MigrationKit9WallpaperV s5ErrorP
- _symbolic ___________pIeghHrzo_ 10Foundation3URLV s5ErrorP
- _symbolic ___________pIeghHrzo_ 12MigrationKit13AppPropertiesV s5ErrorP
- _symbolic __________y_____G______pXj r0_lScI_px7ElementRts_q_7FailureRtsXPXGMq 12MigrationKit17OnDiskFileContentV AE28OSMigrationVoiceMemoMetadataV s5ErrorP
- _symbolic __________y_____G______pXj r0_lSci_px7ElementRts_q_7FailureRtsXPXGMq 12MigrationKit17OnDiskFileContentV AE28OSMigrationVoiceMemoMetadataV s5ErrorP
- _symbolic ______p_____Sg______pIeghHnozo_ 12MigrationKit13ObjectContentP AA16HTTPPartResponseC s5ErrorP
- _symbolic ______p______11contentTypet 21InternalSwiftProtobuf7MessageP 12MigrationKit19ResourceContentTypeV
- _symbolic _____ySo34PKExternalDeviceMigrationCardEntryC_SStG s23_ContiguousArrayStorageC
- _symbolic _____y_____G 12MigrationKit18ArrayAsyncSequenceV AA15EventAttachmentV
- _symbolic _____y_____G 12MigrationKit18ArrayAsyncSequenceV AA21OSMigrationMusicTrackV
- _symbolic _____y_____G 12MigrationKit18ArrayAsyncSequenceV AA4CardV
- _symbolic _____y_____G 12MigrationKit18ArrayAsyncSequenceV AA9WallpaperV
- _symbolic _____y_____G 12MigrationKit29HTTPPartResponseAsyncSequenceV AA17OSMigrationAlarmsV
- _symbolic _____y_____G 12MigrationKit29HTTPPartResponseAsyncSequenceV AA20OSMigrationCallArrayV
- _symbolic _____y_____G 12MigrationKit29HTTPPartResponseAsyncSequenceV AA23OSMigrationAccountArrayV
- _symbolic _____y_____G 12MigrationKit29HTTPPartResponseAsyncSequenceV AA23OSMigrationContactArrayV
- _symbolic _____y_____G 12MigrationKit29HTTPPartResponseAsyncSequenceV AA24OSMigrationCalendarArrayV
- _symbolic _____y_____G 12MigrationKit29HTTPPartResponseAsyncSequenceV AA29OSMigrationCalendarEventArrayV
- _symbolic _____y_____G 12MigrationKit29HTTPPartResponseAsyncSequenceV AA29OSMigrationMusicPlaylistArrayV
- _symbolic _____y_____G s23_ContiguousArrayStorageC 12MigrationKit4CardV
- _symbolic _____y_____GSg 12MigrationKit17OnDiskFileContentV AA28OSMigrationVoiceMemoMetadataV
- _symbolic _____y___________pGSg s6ResultOsRi_zRi0_zrlE 12MigrationKit12ContactPhotoV s5ErrorP
- _symbolic _____y_____yAAy__________SgGGADG s15LazyMapSequenceV s0a6FilterC0V 12MigrationKit15ContactExporterV0g5PhotoC0V AE16HTTPPartResponseC
- _symbolic _____y_____y_____G_____G s23AsyncCompactMapSequenceV 12MigrationKit05ArrayaD0V 10Foundation4DataV AC16HTTPPartResponseC
- _symbolic _____y_____y___________pGG s23_ContiguousArrayStorageC s6ResultOsRi_zRi0_zrlE 12MigrationKit12ContactPhotoV s5ErrorP
- _symbolic _____yx_G 12MigrationKit29HTTPPartResponseAsyncSequenceV8IteratorV
- _type_layout_string 12MigrationKit15ContactExporterV0C13PhotoSequenceV
- _type_layout_string 12MigrationKit15ContactExporterV0C13PhotoSequenceV8IteratorV
- _type_layout_string 12MigrationKit21CardMultipartResponseV
- _type_layout_string 12MigrationKit21CardMultipartResponseV8IteratorV
- _type_layout_string 12MigrationKit26MusicPlaylistAsyncSequenceV
- _type_layout_string 12MigrationKit26MusicPlaylistAsyncSequenceV8IteratorV
- _type_layout_string 12MigrationKit26RecordingMultipartResponseV
- _type_layout_string 12MigrationKit26RecordingMultipartResponseV8IteratorV
- _type_layout_string 12MigrationKit26WallpaperMultipartResponseV
- _type_layout_string 12MigrationKit26WallpaperMultipartResponseV8IteratorV
- _type_layout_string 12MigrationKit27MusicTrackMultipartResponseV
- _type_layout_string 12MigrationKit27MusicTrackMultipartResponseV8IteratorV
- _type_layout_string 12MigrationKit31VoiceMemoRecordingAsyncSequenceV
- _type_layout_string 12MigrationKit31VoiceMemoRecordingAsyncSequenceV8IteratorV
- _type_layout_string 12MigrationKit32EventAttachmentMultipartResponseV
- _type_layout_string 12MigrationKit32EventAttachmentMultipartResponseV8IteratorV
- _type_layout_string 21InternalSwiftProtobuf7MessageRzl12MigrationKit29HTTPPartResponseAsyncSequenceV8IteratorVyx_G
- _type_layout_string 21InternalSwiftProtobuf7MessageRzl12MigrationKit29HTTPPartResponseAsyncSequenceVyxG
CStrings:
+ "%02d"
+ "%02x"
+ "/Library/SMS/sms.db"
+ "/var/mobile/Library/SMS/Attachments"
+ "<"
+ "Account has no valid type information: name=%s"
+ "Added account suggestion for: %{public}s - %s"
+ "Calendar not found"
+ "Converted metadata for voice memo: %s"
+ "Converted persisted account to MKAccountItem: type=%{public}s, username=%s"
+ "DELETE FROM %@"
+ "DELETE FROM kvtable WHERE key = ?"
+ "DROP TRIGGER IF EXISTS %@"
+ "EXPORT_FAILURE_STATE_EXPORT_FAILED"
+ "EXPORT_FAILURE_STATE_UNSPECIFIED"
+ "EXPORT_FAILURE_STATE_UNTRANSFERRABLE"
+ "Export contact photos"
+ "Export contacts"
+ "ExportFailureSummary"
+ "Exporting playlist: %s"
+ "Exporting track: %s"
+ "Failed creating HTTP response for data"
+ "Failed exporting OSMigrationExportFailure"
+ "Failed exporting card"
+ "Failed exporting next item"
+ "Failed exporting playlist"
+ "Failed exporting track"
+ "Failed exporting voice memo"
+ "Failed fetching home screen wallpaper"
+ "Failed fetching lock screen wallpaper"
+ "Failed serializing "
+ "Failed to GET /app-content/list response content"
+ "Failed to cast supported dataclass to ACAccount.Dataclass: %{public}s"
+ "Failed to convert file"
+ "Failed to copy WiFi network password. ssid=%@"
+ "Failed to create ACAccount for type: %{public}s"
+ "Failed to fetch accounts from database"
+ "Failed to fetch accounts from persistence database"
+ "FileContentResponse"
+ "Found %ld entries in manifest"
+ "Found %{public}ld accounts to import"
+ "INSERT INTO attachment (%@) VALUES (%@)"
+ "INSERT INTO chat (%@) VALUES (%@)"
+ "INSERT INTO chat_message_join (%@) VALUES (%@)"
+ "INSERT INTO handle (%@) VALUES (%@)"
+ "INSERT INTO message (%@) VALUES (%@)"
+ "INSERT INTO message_attachment_join (%@) VALUES (%@)"
+ "INSERT OR IGNORE INTO chat_handle_join (%@) VALUES (%@)"
+ "Lazy account migration completed. Imported: %{public}ld, Skipped: %ld"
+ "MKItemFailedCount"
+ "MKItemUntransferrableCount"
+ "MKMessageGroup"
+ "MigrationKit/AccountLazyMigrator.swift"
+ "MigrationKit/ArrayAsyncSequence.swift"
+ "MigrationKit/Card.swift"
+ "MigrationKit/CardAsyncSequence.swift"
+ "MigrationKit/ConnectionReader.swift"
+ "MigrationKit/ContactPhotoSequence.swift"
+ "MigrationKit/ContentAsyncSequence+HTTP.swift"
+ "MigrationKit/ContentHasher.swift"
+ "MigrationKit/ExportFailures.swift"
+ "MigrationKit/FileContentConvertibleAsyncSequence.swift"
+ "MigrationKit/FileContentDepot.swift"
+ "MigrationKit/MusicTrackAsyncSequence.swift"
+ "MigrationKit/ObjectBatchAsyncSequence.swift"
+ "Missing PK pass archive"
+ "No accounts found in persistence storage to import"
+ "OSMigrationExportFailure"
+ "One or more errors occurred while importing WiFi networks; check wifid logs for details. Most recent error:"
+ "P:%@"
+ "Received failure for OSMigrationAccessibilitySettings"
+ "Received failure for OSMigrationAsset"
+ "Received failure for OSMigrationCalendarAttachment"
+ "Received failure for OSMigrationContactPhotoMetadata"
+ "Received failure for OSMigrationFileProperties"
+ "Received failure for OSMigrationMessageAttachment"
+ "Received failure for OSMigrationMusicTrack"
+ "Received failure for OSMigrationVoiceMemoMetadata"
+ "Received failure for OSMigrationWalletCardManifestEntry"
+ "Received failure for OSMigrationWallpaperAsset"
+ "SELECT rowid FROM chat WHERE chat_identifier = ? LIMIT 1"
+ "SELECT rowid FROM chat WHERE room_name = ? LIMIT 1"
+ "SELECT rowid FROM handle WHERE id = ? LIMIT 1"
+ "SMS;+;%@"
+ "SMS;-;%@"
+ "Set ACPropertyFullName property: %s"
+ "Set IdentityEmailAddress property: %s"
+ "Set account description: %s"
+ "Stored account in persistence. Type: %s, Name: %s"
+ "T@\"NSArray\",&,N,V_handles"
+ "T@\"NSData\",&,N,V_attributedBody"
+ "T@\"NSString\",C,N,V_UUID"
+ "T@\"NSString\",C,N,V_account"
+ "T@\"NSString\",C,N,V_roomName"
+ "Tq,N,V_chatStyle"
+ "Tq,N,V_privateMacAddressType"
+ "Tq,N,V_securityType"
+ "Tq,N,V_timestampInNanoseconds"
+ "Tq,N,V_timestampInSeconds"
+ "Tq,N,V_transferState"
+ "UPDATE _SqliteDatabaseProperties SET value = ? WHERE key = ?"
+ "Unknown iOS account type raw value: %{public}ld"
+ "Unrecognized failure type "
+ "Untransferrable OSMigrationExportFailure"
+ "WiFi network's SSID exceeds max length. ssid=%@"
+ "WiFi network's password exceeds max length. length=%lu"
+ "Will import %ld network(s)"
+ "Will import network. ssid=%{private}s"
+ "_ClientVersion"
+ "_UUID"
+ "_accountGUID"
+ "_attributedBody"
+ "_chatStyle"
+ "_exportFailure"
+ "_groups"
+ "_handles"
+ "_import2:"
+ "_performAttestation(incomingChallengeHash:)"
+ "_performSimpleQuery:"
+ "_roomName"
+ "_sendControlMessage(_:maxAttempts:)"
+ "_timestampInNanoseconds"
+ "_timestampInSeconds"
+ "_transferState"
+ "_underlyingFailureWithMessage"
+ "_waitOrFail(caller:)"
+ "account_guid"
+ "account_id"
+ "account_login"
+ "addKnownNetworksForMigration:error:"
+ "archivedDataWithRootObject:"
+ "asDataContent()"
+ "asError"
+ "asMultipartResponse(query:)"
+ "asMultipartResponse(query:context:)"
+ "asSerializedData"
+ "associate(ssid:password:)"
+ "attachment"
+ "attachment id : %@"
+ "attachment id is missing"
+ "attachment join id is missing"
+ "attachment_id"
+ "attributedBody"
+ "cache_roomnames"
+ "chat"
+ "chat handle join id is missing"
+ "chat id : %@"
+ "chat id is missing"
+ "chat join id is missing"
+ "chatIDForMessage:forHandleIDs:withGroup:"
+ "chatLookupVersion"
+ "chatStyle"
+ "chatVersion"
+ "chat_handle_join"
+ "chat_id"
+ "chat_identifier"
+ "chat_message_join"
+ "completeMutualAttestation(caller:)"
+ "computeIdentity(fromStream:)"
+ "converted account to mkAccount: mkAccount.type: %s, mkAccount.username: %s for persistence storage"
+ "converted account to mkAccount: mkAccount.type: %{public}s, mkAccount.username: %s before lazy import"
+ "created_date"
+ "date_delivered"
+ "date_played"
+ "date_read"
+ "defaultHFSFileManager"
+ "delete"
+ "delete:"
+ "deleteKV"
+ "deleteKV:"
+ "did import a message"
+ "dropTrigger:"
+ "dropTriggers"
+ "export_failure"
+ "export_failure_summary"
+ "failed_items_count"
+ "failure_message"
+ "failure_messages"
+ "failure_state"
+ "fetchEvents(for:)"
+ "fileName"
+ "finished account lazy migration."
+ "generatedRoomNameForGroupChat"
+ "getAllAccounts()"
+ "getCString:maxLength:encoding:"
+ "group id : %@"
+ "group room name : %@"
+ "group_id"
+ "group_title"
+ "guid"
+ "handle"
+ "handle ids : %@"
+ "handle ids is missing"
+ "handleID:"
+ "handleIDs:"
+ "handle_id"
+ "handles"
+ "handles : %@"
+ "handles is missing"
+ "importAttachment(_:_:_:)"
+ "importResource(_:resource:context:clientFactory:)"
+ "importWiFiNetworks:error:"
+ "ingest(stream:context:)"
+ "insertAttachment:withMessage:"
+ "insertChatForMessage:forHandleIDs:withGroup:"
+ "insertHandle:"
+ "insertMessage:forHandleID:withGroup:"
+ "is_filtered"
+ "is_finished"
+ "is_from_me"
+ "is_outgoing"
+ "joinAttachment:message:"
+ "joinChat:handle:"
+ "joinChat:message:date:"
+ "last_addressed_handle"
+ "makeDirectoriesInPath:mode:"
+ "message id : %@"
+ "message id is missing"
+ "message_attachment_join"
+ "message_date"
+ "no matching account type for: %{public}s"
+ "not importing %{public}s calendar: %s"
+ "notify"
+ "numberWithLongLong:"
+ "original_guid"
+ "pathExtensionForMIMEType:"
+ "pathExtensionForUTIType:"
+ "properties"
+ "q24@?0@\"NSNumber\"8@\"NSNumber\"16"
+ "query : %@"
+ "readAppContentImportList(client:context:)"
+ "readUntil(_:buffer:)"
+ "roomName"
+ "room_name"
+ "send control message (#"
+ "send data control message (#"
+ "sendControlMessage(_:maxAttempts:)"
+ "sender handle id : %@"
+ "service_center"
+ "service_name"
+ "setAttributedBody:"
+ "setChatStyle:"
+ "setHandles:"
+ "setRoomName:"
+ "setTimestampInNanoseconds:"
+ "setTimestampInSeconds:"
+ "setTransferState:"
+ "setUUID:"
+ "skipping Apple account for persistence storage. Type: %s, Name: %s"
+ "skipping account. Type: %{public}s, Name: %s"
+ "start_date"
+ "stringByResolvingAndStandardizingPath"
+ "style"
+ "timestampInNanoseconds"
+ "timestampInSeconds"
+ "total_bytes"
+ "transferState"
+ "transfer_name"
+ "transfer_state"
+ "uncanonicalized_id"
+ "untransferrableStats"
+ "untransferrable_items_count"
+ "update failed. %d (%s)"
+ "updateClient"
+ "user_info"
+ "uti"
+ "verify_chat_insert"
+ "verify_chat_update"
+ "was_data_detected"
+ "will import a message"
+ "will import accounts from persistence"
+ "will import local calendar: %s"
+ "will run account lazy migration."
+ "write"
+ "writeStreamResponse(connection:stream:)"
- "AccountAsyncSequence next() is cancelled because the current Task is cancelled."
- "AlarmAsyncSequence next() is cancelled because the current Task is cancelled."
- "All playlists have been processed, returning nil"
- "Calendar with ID %s not found."
- "CalendarAsyncSequence next() is cancelled because the current Task is cancelled."
- "CallAsyncSequence next() is cancelled because the current Task is cancelled."
- "Calling wallet SPI for manifest entry"
- "Converted metadata for recording: %s"
- "Error calling wallet SPI"
- "Error fetching item with UUID: %s - %s"
- "Error fetching playlists"
- "EventAsyncSequence next() is cancelled because the current Task is cancelled."
- "Exporting contact photo; contactID=%s, size=%llu, type=%s"
- "Failed creating HTTP response for file"
- "Failed creating HTTP response for object"
- "Failed to GET /appContentExportList response content"
- "Failed to create response for contact photo"
- "Failed to export contact photo"
- "Failed to fetch home screen wallpaper"
- "Failed to fetch lock screen wallpaper"
- "Failed to get file size for"
- "Failed to open a voice memo file"
- "Handling /recordings request from client"
- "Handling contact photos request from client"
- "Handling contacts request from client"
- "MigrationKit/EventAttachmentMultipartResponse.swift"
- "MigrationKit/MusicTrackMultipartResponse.swift"
- "MigrationKit/RecordingMultipartResponse.swift"
- "MigrationKit/VoiceMemoExporter.swift"
- "MusicPlaylistAsyncSequence initialized with %ld playlists, batch size: %ld"
- "Q24@0:8q16"
- "Saved music track: %s"
- "Successfully exported %ld of %ld voice memos"
- "Successfully exported wallet"
- "Successfully imported account. Type: %s, Name: %s"
- "TQ,N,V_privateMacAddressType"
- "TQ,N,V_securityType"
- "WiFi Network Profile already exists ssid: %s, ssidString: %s"
- "X-OS-Migration-Error"
- "X-OS-Migration-File-Content-Identifier"
- "_TtC12MigrationKit21HTTPMultipartResponse"
- "_fileSize"
- "_mkPrivateMacAddressType:"
- "_mkSecurityType:"
- "_parts"
- "addKnownNetworkProfile:error:"
- "convertWiFiSecurityType(_:)"
- "converted account to mkAccount: mkAccount.type: %s, mkAccount.username: %s before import"
- "exporting playlistItem: %s"
- "exporting trackItem: %s"
- "failed ingesting image data"
- "failed to add a network. "
- "failed to export an item and will skip it."
- "failed to open an attachment file"
- "failed to open an music file"
- "importAttachment(_:_:)"
- "imported a network. %s"
- "next() is cancelled because the current Task is cancelled."
- "now streaming %s, size: %llu, fileSize: %llu, metadata : %s"
- "readAppContentImportList(client:)"
- "send control message: "
- "sendControlMessage(_:)"
- "setAutoJoinDisabled:"
- "setHiddenState:"
- "setPassword:knownNetworkProfile:error:"
- "setSupportedSecurityTypes:"
- "skipping account. Type: %s, Name: %s"
- "strongestSupportedSecurityType"
- "will batch %ld playlists (%ld to %ld)"
- "will save a conversation. %s"
- "will save a message. %s"

```
