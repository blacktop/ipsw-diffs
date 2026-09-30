## SiriUIFoundation

> `/System/Library/PrivateFrameworks/SiriUIFoundation.framework/Versions/A/SiriUIFoundation`

```diff

-3600.55.30.0.0
-  __TEXT.__text: 0x7ea80
-  __TEXT.__objc_methlist: 0x4310
-  __TEXT.__const: 0x32dc
-  __TEXT.__cstring: 0x6176
-  __TEXT.__oslogstring: 0x5c17
-  __TEXT.__gcc_except_tab: 0x954
+3600.55.37.14.1
+  __TEXT.__text: 0x7f444
+  __TEXT.__objc_methlist: 0x43a0
+  __TEXT.__const: 0x32bc
+  __TEXT.__cstring: 0x60f6
+  __TEXT.__oslogstring: 0x5bf9
+  __TEXT.__gcc_except_tab: 0x95c
   __TEXT.__ustring: 0x22
   __TEXT.__dlopen_cstrs: 0x58
   __TEXT.__swift5_typeref: 0x119e
   __TEXT.__swift5_capture: 0x534
   __TEXT.__constg_swiftt: 0x13f0
-  __TEXT.__swift5_reflstr: 0xfda
-  __TEXT.__swift5_fieldmd: 0xe68
+  __TEXT.__swift5_reflstr: 0xfaa
+  __TEXT.__swift5_fieldmd: 0xe5c
   __TEXT.__swift5_builtin: 0x64
   __TEXT.__swift5_proto: 0x228
   __TEXT.__swift5_types: 0x118

   __TEXT.__swift5_protos: 0x28
   __TEXT.__swift5_assocty: 0x228
   __TEXT.__swift5_mpenum: 0x1c
-  __TEXT.__unwind_info: 0x21b8
+  __TEXT.__unwind_info: 0x21c8
   __TEXT.__eh_frame: 0x1950
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x560
+  __DATA_CONST.__const: 0x570
   __DATA_CONST.__objc_classlist: 0x300
   __DATA_CONST.__objc_catlist: 0x158
   __DATA_CONST.__objc_protolist: 0x158
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2c28
+  __DATA_CONST.__objc_selrefs: 0x2c98
   __DATA_CONST.__objc_protorefs: 0x78
   __DATA_CONST.__objc_superrefs: 0x160
   __DATA_CONST.__objc_arraydata: 0x20
-  __DATA_CONST.__got: 0x908
-  __AUTH_CONST.__const: 0x4b01
-  __AUTH_CONST.__cfstring: 0x21e0
-  __AUTH_CONST.__objc_const: 0x88a8
+  __DATA_CONST.__got: 0x928
+  __AUTH_CONST.__const: 0x4b31
+  __AUTH_CONST.__cfstring: 0x2200
+  __AUTH_CONST.__objc_const: 0x8938
   __AUTH_CONST.__objc_intobj: 0x108
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__auth_got: 0xbb0
+  __AUTH_CONST.__auth_got: 0xbb8
   __AUTH.__objc_data: 0xff0
   __AUTH.__data: 0xb98
-  __DATA.__objc_ivar: 0x408
-  __DATA.__data: 0x1520
+  __DATA.__objc_ivar: 0x410
+  __DATA.__data: 0x1508
   __DATA.__bss: 0x40f0
   __DATA.__common: 0x48
   __DATA_DIRTY.__objc_data: 0xef8

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3100
-  Symbols:   4590
-  CStrings:  1037
+  Functions: 3120
+  Symbols:   4619
+  CStrings:  1034
 
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
+ GCC_except_table112
+ GCC_except_table118
+ GCC_except_table129
+ GCC_except_table26
+ GCC_except_table42
+ GCC_except_table52
+ GCC_except_table89
+ GCC_except_table91
+ OBJC_IVAR_$_SRUIFSpeechSynthesizer._audioPowerLevelUpdatesEnabled
+ OBJC_IVAR_$_SRUIFSpeechSynthesizer._audioPowerSignpostID
+ _OBJC_CLASS_$_SISchemaUEIBreadcrumbReturned
+ _OBJC_CLASS_$_SISchemaUEICanvasToAppExpanded
+ _OBJC_CLASS_$_SISchemaUEIIslandToCanvasExpanded
+ _OBJC_CLASS_$_SISchemaUEILinkTapped
+ _OBJC_CLASS_$_SISchemaUEISourceListExpanded
+ ___54-[SRUIFInstrumentationManager emitCanvasToAppExpanded]_block_invoke
+ ___57-[SRUIFInstrumentationManager emitIslandToCanvasExpanded]_block_invoke
+ ___61-[SRUIFInstrumentationManager emitBreadcrumbReturnedIfNeeded]_block_invoke
+ ___69-[SRUIFInstrumentationManager emitSourceListExpandedWithSourceCount:]_block_invoke
+ ___87-[SRUIFInstrumentationManager emitLinkTappedWithType:isPersonalEntity:opensExternally:]_block_invoke
+ ___block_descriptor_61_e8_32s40w_e5_v8?0l
+ __swift_closure_destructor.194Tm
+ __swift_closure_destructor.201Tm
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
- GCC_except_table102
- GCC_except_table104
- GCC_except_table115
- GCC_except_table46
- GCC_except_table70
- GCC_except_table86
- GCC_except_table88
- GCC_except_table98
- _SRUIFIsCompanionVoiceResponseEnabled
- __OBJC_$_CLASS_METHODS_SRUIFSpeechSynthesizer
- __swift_closure_destructor.192Tm
- __swift_closure_destructor.199Tm
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
