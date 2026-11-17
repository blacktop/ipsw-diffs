## NotesShared

> `/System/Library/PrivateFrameworks/NotesShared.framework/NotesShared`

```diff

-3001.60.6.0.0
-  __TEXT.__text: 0x34b670
+3001.60.10.0.0
+  __TEXT.__text: 0x351fc8
   __TEXT.__delay_stubs: 0x240
   __TEXT.__delay_helper: 0x830
-  __TEXT.__objc_methlist: 0x186ec
-  __TEXT.__const: 0xde18
-  __TEXT.__cstring: 0x19c44
-  __TEXT.__gcc_except_tab: 0xf260
-  __TEXT.__oslogstring: 0x1f5d9
+  __TEXT.__objc_methlist: 0x1873c
+  __TEXT.__const: 0xdfa8
+  __TEXT.__cstring: 0x19c64
+  __TEXT.__gcc_except_tab: 0xf294
+  __TEXT.__oslogstring: 0x1fa69
   __TEXT.__ustring: 0x39a
-  __TEXT.__swift5_typeref: 0x4570
-  __TEXT.__swift5_fieldmd: 0x2f8c
-  __TEXT.__constg_swiftt: 0x37f8
+  __TEXT.__swift5_typeref: 0x45c0
+  __TEXT.__swift5_fieldmd: 0x3008
+  __TEXT.__constg_swiftt: 0x39b4
   __TEXT.__swift5_builtin: 0x208
-  __TEXT.__swift5_reflstr: 0x2261
+  __TEXT.__swift5_reflstr: 0x2311
   __TEXT.__swift5_assocty: 0x7e0
   __TEXT.__swift5_protos: 0x58
   __TEXT.__swift5_proto: 0x994
-  __TEXT.__swift5_types: 0x39c
-  __TEXT.__swift5_capture: 0x1e7c
+  __TEXT.__swift5_types: 0x3a0
+  __TEXT.__swift5_capture: 0x1e2c
   __TEXT.__swift_as_entry: 0x188
   __TEXT.__swift_as_ret: 0x1b8
   __TEXT.__swift_as_cont: 0x3f4
   __TEXT.__swift5_mpenum: 0x74
-  __TEXT.__unwind_info: 0x128e0
-  __TEXT.__eh_frame: 0x894c
+  __TEXT.__unwind_info: 0x12a00
+  __TEXT.__eh_frame: 0x899c
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x6830
+  __DATA_CONST.__const: 0x68f0
   __DATA_CONST.__objc_classlist: 0xa88
   __DATA_CONST.__objc_catlist: 0x138
   __DATA_CONST.__objc_protolist: 0x238
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0xce38
+  __DATA_CONST.__objc_selrefs: 0xce88
   __DATA_CONST.__objc_protorefs: 0xc0
   __DATA_CONST.__objc_superrefs: 0x6c0
   __DATA_CONST.__objc_arraydata: 0x228
-  __DATA_CONST.__got: 0x2148
-  __AUTH_CONST.__const: 0xdce8
-  __AUTH_CONST.__cfstring: 0xfee0
-  __AUTH_CONST.__objc_const: 0x229c8
+  __DATA_CONST.__got: 0x2168
+  __AUTH_CONST.__const: 0xdc58
+  __AUTH_CONST.__cfstring: 0xff40
+  __AUTH_CONST.__objc_const: 0x22af8
   __AUTH_CONST.__weak_auth_got: 0x30
   __AUTH_CONST.__objc_intobj: 0x450
   __AUTH_CONST.__objc_arrayobj: 0x258
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH_CONST.__auth_got: 0x2b18
+  __AUTH_CONST.__auth_got: 0x2b60
   __AUTH.__objc_data: 0x2d60
-  __AUTH.__data: 0x1720
-  __DATA.__objc_ivar: 0xd8c
-  __DATA.__data: 0x4c04
+  __AUTH.__data: 0x18f8
+  __DATA.__objc_ivar: 0xd90
+  __DATA.__data: 0x4c84
   __DATA.__objc_stublist: 0x20
-  __DATA.__common: 0x188
+  __DATA.__common: 0x1a0
   __DATA_DIRTY.__objc_data: 0x4a68
   __DATA_DIRTY.__data: 0x1ca8
   __DATA_DIRTY.__bss: 0x2a38

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 18808
-  Symbols:   17917
-  CStrings:  5433
+  Functions: 18886
+  Symbols:   17948
+  CStrings:  5444
 
Symbols:
+ +[ICCloudContext isQuotaExceededError:]
+ +[ICCloudContext isServerThrottleError:]
+ -[ICCloudContext pushObjectsRecoveringFromTrash]
+ -[ICCloudContext retryTimerIsForQuotaExceeded]
+ -[ICCloudContext setRetryTimerIsForQuotaExceeded:]
+ -[ICNote containsWritingToolsGeneratedStrokes]
+ -[ICNote enumerateDrawingsUsingBlock:]
+ GCC_except_table166
+ GCC_except_table179
+ GCC_except_table191
+ GCC_except_table210
+ GCC_except_table230
+ GCC_except_table262
+ GCC_except_table272
+ GCC_except_table291
+ GCC_except_table301
+ GCC_except_table314
+ GCC_except_table316
+ GCC_except_table337
+ GCC_except_table360
+ GCC_except_table375
+ GCC_except_table385
+ GCC_except_table430
+ GCC_except_table457
+ GCC_except_table462
+ GCC_except_table467
+ _ICTTAttachmentNeedsConversionNotification
+ _ICTTAttachmentRequestConversion
+ _ICTTAttachmentRequestConversion.isRequestPending
+ _OBJC_CLASS_$_PKStroke
+ _OBJC_IVAR_$_ICCloudContext._retryTimerIsForQuotaExceeded
+ ___38-[ICNote enumerateDrawingsUsingBlock:]_block_invoke
+ ___39+[ICCloudContext isQuotaExceededError:]_block_invoke
+ ___40+[ICCloudContext isServerThrottleError:]_block_invoke
+ ___46-[ICNote containsWritingToolsGeneratedStrokes]_block_invoke
+ ___48-[ICCloudContext pushObjectsRecoveringFromTrash]_block_invoke
+ ___48-[ICCloudContext pushObjectsRecoveringFromTrash]_block_invoke_2
+ ___ICTTAttachmentRequestConversion_block_invoke
+ ___block_descriptor_32_e24_B32?0"NSError"8Q16^B24l
+ ___block_descriptor_40_e8_32bs_e26_v24?0"ICAttachment"8^B16ls32l8
+ ___block_descriptor_40_e8_32r_e23_v24?0"PKDrawing"8^B16lr32l8
+ ___block_descriptor_73_e8_32s40s_e5_v8?0ls32l8s40l8
+ _symbolic Say_____G 11NotesShared28LiveTranscriptionCoordinatorC16PendingUtterance33_45D858AA1D2B7DFA43905393E2F9198FLLV
+ _symbolic _____ 11NotesShared28LiveTranscriptionCoordinatorC16PendingUtterance33_45D858AA1D2B7DFA43905393E2F9198FLLV
+ _symbolic _____XDXMT 11NotesShared28LiveTranscriptionCoordinatorC
+ _symbolic _____y_____G s16IndexingIteratorV 10Foundation16AttributedStringV13CharacterViewV
+ _symbolic _____y_____G s16PartialRangeFromV 10Foundation16AttributedStringV5IndexV
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 11NotesShared28LiveTranscriptionCoordinatorC16PendingUtterance33_45D858AA1D2B7DFA43905393E2F9198FLLV
+ _symbolic _____z_Xx 10Foundation16AttributedStringV
+ _type_layout_string 11NotesShared28LiveTranscriptionCoordinatorC16PendingUtterance33_45D858AA1D2B7DFA43905393E2F9198FLLV
- GCC_except_table163
- GCC_except_table173
- GCC_except_table176
- GCC_except_table187
- GCC_except_table192
- GCC_except_table197
- GCC_except_table253
- GCC_except_table263
- GCC_except_table292
- GCC_except_table310
- GCC_except_table356
- GCC_except_table366
- GCC_except_table381
- GCC_except_table402
- GCC_except_table408
- GCC_except_table420
- GCC_except_table421
- GCC_except_table448
- GCC_except_table458
CStrings:
+ "@min.folderModificationDate"
+ "Deleting %lu note(s) that were in Recently Deleted longer than %.0f day(s) {cutoff: %{public}@, oldestTrashedDate: %{public}@, notes: %@}"
+ "Duplicating note… {originalNote: %@, folder: %@}"
+ "Failed merge %p: Couldn't copy note, keeping local note content."
+ "ICTTAttachmentNeedsConversionNotification"
+ "Not clearing the folder of note %@: its old folder %@ already dropped it in a merge"
+ "Pushing %lu object(s) recovering from trash without waiting for the quota retry timer"
+ "RecoverFromTrash"
+ "Removed %lu deleted note(s) from this device after their deletion synced {notes: %@}"
+ "Retrying operations after %ds {serverRetryAfter: %.0fs, backoff: %.0fs, error: %ld}"
+ "Saving live note %@ with no folder, so it's hidden until the launch task re-homes it {account: %@, mergingRecord: %d}"
+ "Setting note (%@) as recovering from trash {folder: %@}"
+ "[MSQFA] Account %@: Recently Deleted still owes a push after pushing it {note: %@, inCloud: %d, needsToBePushed: %d, needsToBeFetched: %d, locked: %d, hasAllMandatoryFields: %d, error: %@}"
+ "[MSQFA] Account %@: moving %lu note(s) to Recently Deleted {joined: %lu, blocked: %lu, blockedLocked: %lu, madeOrMovedAfterCutoff: %lu, cutoff: %{public}@, newestMovedDate: %{public}@}"
+ "[MSQFA] Account %@: not pushing %lu Recently Deleted note(s) yet; sync isn't ready {isReadyToSync: %d, isDisabled: %d, syncOnlyIfReachable: %d, isReachable: %d}"
+ "[MSQFA] Dropping %lu over-quota recovery refusal(s) that never reached the alert: a new push started first"
+ "[MSQFA] Push refused %lu note(s) moving out of Recently Deleted over quota; they're back in Recently Deleted {account: %@, op: %{public}@, error: %ld, alerting: %d}"
+ "[MSQFA] Simulating an over-quota refusal (ICSimulateQuotaExceededOnTrashRecovery is on), so not sending %@ with %lu trash recovery object(s)"
+ "v24@?0@\"PKDrawing\"8^B16"
- "Duplicating note… {originalNote: %@, folder: %@}%s:%d"
- "ICNote * _Nullable ICDuplicateNoteForRecovery(ICNote *__strong, ICFolder *__strong)"
- "Retrying operations after %ds"
- "Setting note (%@) as recovering from trash"
- "Simulating quota exceeded, so not sending %@ with %lu trash recovery objects"
- "[MSQFA] Account %@: Recently Deleted still owes a push after pushing it {note: %@, error: %@}"
- "[MSQFA] Account %@: moving %lu note(s) to Recently Deleted {joined: %lu, blocked: %lu, madeOrMovedAfterCutoff: %lu, cutoff: %{public}@, newestMovedDate: %{public}@}"
- "[MSQFA] Account %@: not pushing %lu Recently Deleted note(s) yet; sync isn't ready"
```
