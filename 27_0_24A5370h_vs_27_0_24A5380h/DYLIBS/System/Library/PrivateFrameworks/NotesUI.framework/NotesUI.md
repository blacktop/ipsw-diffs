## NotesUI

> `/System/Library/PrivateFrameworks/NotesUI.framework/NotesUI`

```diff

-  __TEXT.__text: 0x2b4058
+  __TEXT.__text: 0x2b5914
   __TEXT.__delay_stubs: 0x40
   __TEXT.__delay_helper: 0x6ec
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x173e8
-  __TEXT.__const: 0x9d64
+  __TEXT.__objc_methlist: 0x17428
+  __TEXT.__const: 0x9d54
   __TEXT.__cstring: 0x13f37
-  __TEXT.__gcc_except_tab: 0x48f0
-  __TEXT.__oslogstring: 0xa002
+  __TEXT.__gcc_except_tab: 0x4944
+  __TEXT.__oslogstring: 0xa152
   __TEXT.__ustring: 0x13a84
   __TEXT.__swift5_typeref: 0xc6ec
   __TEXT.__constg_swiftt: 0x3a00

   __TEXT.__swift_as_ret: 0x108
   __TEXT.__swift_as_cont: 0x1e0
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x9b90
-  __TEXT.__eh_frame: 0x4730
+  __TEXT.__unwind_info: 0x9bd0
+  __TEXT.__eh_frame: 0x46f0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x6488
+  __DATA_CONST.__const: 0x64d8
   __DATA_CONST.__objc_classlist: 0xad8
   __DATA_CONST.__objc_catlist: 0x2c8
   __DATA_CONST.__objc_catlist2: 0x10
   __DATA_CONST.__objc_protolist: 0x3c0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x10110
+  __DATA_CONST.__objc_selrefs: 0x10168
   __DATA_CONST.__objc_protorefs: 0x170
   __DATA_CONST.__objc_superrefs: 0x6b8
   __DATA_CONST.__objc_arraydata: 0x328
-  __DATA_CONST.__got: 0x2e90
+  __DATA_CONST.__got: 0x2ea0
   __AUTH_CONST.__const: 0x9d68
-  __AUTH_CONST.__cfstring: 0xc400
-  __AUTH_CONST.__objc_const: 0x24840
+  __AUTH_CONST.__cfstring: 0xc3c0
+  __AUTH_CONST.__objc_const: 0x24898
   __AUTH_CONST.__weak_auth_got: 0x18
   __AUTH_CONST.__objc_arrayobj: 0x1e0
   __AUTH_CONST.__objc_intobj: 0x630
   __AUTH_CONST.__objc_doubleobj: 0x120
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH_CONST.__auth_got: 0x31a0
-  __AUTH.__objc_data: 0x40a8
+  __AUTH_CONST.__auth_got: 0x31d0
+  __AUTH.__objc_data: 0x4008
   __AUTH.__data: 0x1bb0
-  __DATA.__objc_ivar: 0x1248
-  __DATA.__data: 0x578c
+  __DATA.__objc_ivar: 0x124c
+  __DATA.__data: 0x561c
   __DATA.__objc_stublist: 0x28
-  __DATA.__bss: 0x4500
+  __DATA.__bss: 0x3f50
   __DATA.__common: 0x70
-  __DATA_DIRTY.__objc_data: 0x4028
-  __DATA_DIRTY.__data: 0x2460
-  __DATA_DIRTY.__bss: 0x3fb0
+  __DATA_DIRTY.__objc_data: 0x40c8
+  __DATA_DIRTY.__data: 0x2600
+  __DATA_DIRTY.__bss: 0x4550
   __DATA_DIRTY.__common: 0x60
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 14839
-  Symbols:   33377
-  CStrings:  4699
+  Functions: 14844
+  Symbols:   33407
+  CStrings:  4700
 
Sections:
~ __TEXT.__init_offsets : content changed
~ __TEXT.__cstring : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_builtin : content changed
~ __TEXT.__swift5_fieldmd : content changed
~ __TEXT.__swift5_assocty : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift5_capture : content changed
~ __TEXT.__swift_as_entry : content changed
~ __TEXT.__swift_as_ret : content changed
~ __TEXT.__swift_as_cont : content changed
~ __TEXT.__swift5_mpenum : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_catlist2 : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__weak_got : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__weak_auth_got : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_doubleobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH.__data : content changed
~ __DATA.__objc_stublist : content changed
Symbols:
+ -[ICReindexEverythingBackgroundTask isRunningFullReindex]
+ -[ICReindexEverythingBackgroundTask rescheduleAndCallCompletion:error:]
+ -[ICReindexEverythingBackgroundTask runFullReindexResettingEverything:attachments:completion:]
+ -[ICReindexEverythingBackgroundTask setIsRunningFullReindex:]
+ _ICUseCoreDataCoreSpotlightIntegration
+ _OBJC_CLASS_$_ICReindexer
+ _OBJC_IVAR_$_ICReindexEverythingBackgroundTask._isRunningFullReindex
+ __OBJC_$_INSTANCE_VARIABLES_ICReindexEverythingBackgroundTask
+ ___74-[ICThumbnailGeneratorNote generateThumbnailWithConfiguration:completion:]_block_invoke_3
+ ___94-[ICReindexEverythingBackgroundTask runFullReindexResettingEverything:attachments:completion:]_block_invoke
+ ___block_descriptor_48_e8_32bs40w_e20_v20?0B8"NSError"12lw40l8s32l8
+ ___block_descriptor_50_e8_32bs40w_e17_v16?0"NSError"8lw40l8s32l8
+ ___swift_mutable_project_boxed_opaque_existential_1
+ _kICReindexAttachmentsOnLaunchKey
+ _objc_msgSend$determineIfReindexIsNeededFromClientStateWithCompletionHandler:
+ _objc_msgSend$indexPendingItemsWithCompletionHandler:
+ _objc_msgSend$isRunningFullReindex
+ _objc_msgSend$lineDirectionForLanguage:
+ _objc_msgSend$migrateSearchIndexVersionIfNeeded
+ _objc_msgSend$refreshDisplayTextForParagraphLinkAttachments:reason:
+ _objc_msgSend$rescheduleAndCallCompletion:error:
+ _objc_msgSend$runFullReindexResettingEverything:attachments:completion:
+ _objc_msgSend$setIsRunningFullReindex:
+ _objc_msgSend$systemCyanColor
+ _swift_makeBoxUnique
- +[ICDeviceSupport(UI) shouldShowWritingToolsButton]
- -[ICTodoButton(PlatformSpecificResponsibility) setHighlighted:]
- _OBJC_CLASS_$_WTAvailability
- ___51+[ICDeviceSupport(UI) shouldShowWritingToolsButton]_block_invoke
- _objc_msgSend$icaxCorrespondingParagraphText
- _objc_msgSend$isEnhancedSiriAvailable
- _shouldShowWritingToolsButton.onceToken
- _shouldShowWritingToolsButton.shouldShowExplicitWritingToolsButton
CStrings:
+ "Reindex BG task: CoreData/CoreSpotlight integration enabled; nothing to do"
+ "Reindex BG task: client state indicates a stale index; running full reindex"
+ "Reindex BG task: indexed pending items"
+ "Reindex BG task: indexing pending items failed, will retry on next wake. error: %@"
+ "Reindex BG task: no pending reindex, index is current, no pending items; rescheduling and exiting"
+ "Reindex BG task: running full reindex (everything: %@, attachments: %@)"
+ "Renamed linked section heading"
- "Reindex BG task: no pending reindex; rescheduling and exiting"
- "Reindex BG task: running deferred reindex"
- "completed: %@"
- "incomplete: %@"

```
