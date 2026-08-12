## SiriUIFoundation

> `/System/Library/PrivateFrameworks/SiriUIFoundation.framework/SiriUIFoundation`

```diff

-3600.55.30.0.0
-  __TEXT.__text: 0x910e8
-  __TEXT.__objc_methlist: 0x46b8
-  __TEXT.__const: 0x389c
-  __TEXT.__cstring: 0x66f6
-  __TEXT.__oslogstring: 0x6fcb
-  __TEXT.__gcc_except_tab: 0x97c
+3600.55.37.11.2
+  __TEXT.__text: 0x9193c
+  __TEXT.__objc_methlist: 0x4748
+  __TEXT.__const: 0x387c
+  __TEXT.__cstring: 0x6676
+  __TEXT.__oslogstring: 0x6fab
+  __TEXT.__gcc_except_tab: 0x984
   __TEXT.__ustring: 0x22
   __TEXT.__dlopen_cstrs: 0x58
   __TEXT.__swift5_typeref: 0x1594
   __TEXT.__swift5_capture: 0x734
   __TEXT.__constg_swiftt: 0x14d4
-  __TEXT.__swift5_reflstr: 0x112a
-  __TEXT.__swift5_fieldmd: 0xf88
+  __TEXT.__swift5_reflstr: 0x10fa
+  __TEXT.__swift5_fieldmd: 0xf7c
   __TEXT.__swift5_builtin: 0x64
   __TEXT.__swift5_proto: 0x254
   __TEXT.__swift5_types: 0x130

   __TEXT.__swift5_protos: 0x28
   __TEXT.__swift5_assocty: 0x228
   __TEXT.__swift5_mpenum: 0x1c
-  __TEXT.__unwind_info: 0x2690
+  __TEXT.__unwind_info: 0x2738
   __TEXT.__eh_frame: 0x23c8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1978
+  __DATA_CONST.__const: 0x19b0
   __DATA_CONST.__objc_classlist: 0x330
   __DATA_CONST.__objc_catlist: 0x160
   __DATA_CONST.__objc_protolist: 0x160
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2f38
+  __DATA_CONST.__objc_selrefs: 0x2fa8
   __DATA_CONST.__objc_protorefs: 0x78
   __DATA_CONST.__objc_superrefs: 0x178
   __DATA_CONST.__objc_arraydata: 0x30
-  __DATA_CONST.__got: 0xa78
+  __DATA_CONST.__got: 0xa98
   __AUTH_CONST.__const: 0x3aa1
-  __AUTH_CONST.__cfstring: 0x23a0
-  __AUTH_CONST.__objc_const: 0x8ff0
+  __AUTH_CONST.__cfstring: 0x23c0
+  __AUTH_CONST.__objc_const: 0x9080
   __AUTH_CONST.__objc_intobj: 0x120
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__auth_got: 0xf38
+  __AUTH_CONST.__auth_got: 0xf40
   __AUTH.__objc_data: 0x1170
   __AUTH.__data: 0xc28
-  __DATA.__objc_ivar: 0x430
-  __DATA.__data: 0x1768
+  __DATA.__objc_ivar: 0x438
+  __DATA.__data: 0x1750
   __DATA.__bss: 0x4670
   __DATA.__common: 0x48
   __DATA_DIRTY.__objc_data: 0xf48

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3358
-  Symbols:   4809
-  CStrings:  1132
+  Functions: 3376
+  Symbols:   4837
+  CStrings:  1129
 
Symbols:
+ -[SRUIFInstrumentationManager clearPendingLinkTapBreadcrumb]
+ -[SRUIFInstrumentationManager emitBreadcrumbReturnedIfNeeded]
+ -[SRUIFInstrumentationManager emitCanvasToAppExpanded]
+ -[SRUIFInstrumentationManager emitIslandToCanvasExpanded]
+ -[SRUIFInstrumentationManager emitLinkTappedWithType:isPersonalEntity:opensExternally:]
+ -[SRUIFInstrumentationManager emitSourceListExpandedWithSourceCount:]
+ -[SRUIFInstrumentationManager emitUUFRShownForPresentationType:dialogPhase:mode:viewRegion:]
+ -[SRUIFInstrumentationManager pendingLinkTapBreadcrumbTurn]
+ -[SRUIFInstrumentationManager setPendingLinkTapBreadcrumbTurn:]
+ -[SRUIFSpeechSynthesizer audioPowerLevelUpdatesEnabled]
+ -[SRUIFSpeechSynthesizer setAudioPowerLevelUpdatesEnabled:]
+ GCC_except_table102
+ GCC_except_table104
+ GCC_except_table111
+ GCC_except_table20
+ GCC_except_table36
+ GCC_except_table40
+ GCC_except_table63
+ GCC_except_table79
+ _OBJC_CLASS_$_SISchemaUEIBreadcrumbReturned
+ _OBJC_CLASS_$_SISchemaUEICanvasToAppExpanded
+ _OBJC_CLASS_$_SISchemaUEIIslandToCanvasExpanded
+ _OBJC_CLASS_$_SISchemaUEILinkTapped
+ _OBJC_CLASS_$_SISchemaUEISourceListExpanded
+ _OBJC_IVAR_$_SRUIFSpeechSynthesizer._audioPowerLevelUpdatesEnabled
+ _OBJC_IVAR_$_SRUIFSpeechSynthesizer._audioPowerSignpostID
+ ___54-[SRUIFInstrumentationManager emitCanvasToAppExpanded]_block_invoke
+ ___57-[SRUIFInstrumentationManager emitIslandToCanvasExpanded]_block_invoke
+ ___61-[SRUIFInstrumentationManager emitBreadcrumbReturnedIfNeeded]_block_invoke
+ ___69-[SRUIFInstrumentationManager emitSourceListExpandedWithSourceCount:]_block_invoke
+ ___87-[SRUIFInstrumentationManager emitLinkTappedWithType:isPersonalEntity:opensExternally:]_block_invoke
+ ___block_descriptor_61_e8_32s40w_e5_v8?0lw40l8s32l8
+ ___swift_closure_destructor.194Tm
+ ___swift_closure_destructor.201Tm
+ _keypath_get_selector_audioPowerLevelUpdatesEnabled
+ _objc_msgSend$audioPowerLevelUpdatesEnabled
+ _objc_msgSend$initWithTurnIdentifier:
+ _objc_msgSend$pendingLinkTapBreadcrumbTurn
+ _objc_msgSend$removePersistentDomainForName:
+ _objc_msgSend$setAudioPowerLevelUpdatesEnabled:
+ _objc_msgSend$setIsPersonalEntity:
+ _objc_msgSend$setLinkType:
+ _objc_msgSend$setPendingLinkTapBreadcrumbTurn:
+ _objc_msgSend$setSourceCount:
- +[SRUIFSiriFeatureFlag(SWEFeatureFlags) isAssistedLinwoodVoiceResponseFromCompanionEnabled]
- +[SRUIFSpeechSynthesizer _inlineStreamMarkerRequestTextForText:inlineStreamId:companionVoiceResponseEnabled:]
- GCC_except_table28
- GCC_except_table38
- GCC_except_table60
- GCC_except_table74
- GCC_except_table76
- GCC_except_table86
- GCC_except_table88
- GCC_except_table90
- GCC_except_table97
- _SRUIFIsCompanionVoiceResponseEnabled
- __OBJC_$_CLASS_METHODS_SRUIFSpeechSynthesizer
- ___swift_closure_destructor.192Tm
- ___swift_closure_destructor.199Tm
- _objc_msgSend$_inlineStreamMarkerRequestTextForText:inlineStreamId:companionVoiceResponseEnabled:
CStrings:
+ "PendingLinkTapBreadcrumbTurnIdentifier"
+ "TTSAudioPowerPolling"
+ "com.apple.SiriViewService.tests"
+ "\xd2"
- "\v6"
- "%@%@\\%@"
- "%s #tts inline-stream marker+text from streamId: %@"
- "+[SRUIFSpeechSynthesizer _inlineStreamMarkerRequestTextForText:inlineStreamId:companionVoiceResponseEnabled:]"
- "GenerateCompanionVoiceResponse"
- "assisted_linwood_voice_response_from_companion"
- "\xc2"
```
