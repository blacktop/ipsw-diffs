## NotesUI

> `/System/Library/PrivateFrameworks/NotesUI.framework/NotesUI`

```diff

-2952.62.3.0.0
-  __TEXT.__text: 0x2a2480
+2952.80.3.0.0
+  __TEXT.__text: 0x2a2510
   __TEXT.__auth_stubs: 0x6130
   __TEXT.__delay_stubs: 0x40
   __TEXT.__delay_helper: 0x6ec
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0x16be8
-  __TEXT.__const: 0xa004
+  __TEXT.__const: 0xa014
   __TEXT.__cstring: 0x16b19
-  __TEXT.__oslogstring: 0x95ec
-  __TEXT.__gcc_except_tab: 0x4b00
+  __TEXT.__oslogstring: 0x95dc
+  __TEXT.__gcc_except_tab: 0x4b0c
   __TEXT.__ustring: 0x139be
   __TEXT.__constg_swiftt: 0x3870
   __TEXT.__swift5_typeref: 0xcd2a

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: C120CD13-CCE0-3D14-93F2-165F109078C8
-  Functions: 14411
-  Symbols:   31589
+  UUID: 949189B3-41AF-3CBE-BE58-31C43D9C898E
+  Functions: 14413
+  Symbols:   31591
   CStrings:  16731
 
Symbols:
+ _OUTLINED_FUNCTION_13
Functions:
~ ___82-[ICTextController fixListWritingDirectionInAttributedString:forListItemsInRange:]_block_invoke_2 : 204 -> 232
~ -[ICCollaborationController acceptShareWithMetadata:attemptNumber:container:accountID:fetchObjectWithCompletionHandler:] : 1640 -> 1684
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_13
~ ___swift_instantiateConcreteTypeFromMangledNameV2 : 72 -> 84
~ ___swift_instantiateConcreteTypeFromMangledNameAbstractV2 : 72 -> 92
~ -[ICCollaborationController saveShare:withRootRecord:object:accountID:container:qualityOfService:completionHandler:].cold.1 : 184 -> 180
~ -[ICCollaborationController saveShare:withRootRecord:object:accountID:container:qualityOfService:completionHandler:].cold.2 : 184 -> 180
~ ___116-[ICCollaborationController saveShare:withRootRecord:object:accountID:container:qualityOfService:completionHandler:]_block_invoke_2.cold.1 : 164 -> 172
~ ___116-[ICCollaborationController saveShare:withRootRecord:object:accountID:container:qualityOfService:completionHandler:]_block_invoke_3.cold.1 : 240 -> 236
~ ___102-[ICCollaborationController removeShareIfNeededWithOwnedObjectID:countParticipants:completionHandler:]_block_invoke_3.cold.1 : 140 -> 132
~ ___120-[ICCollaborationController acceptShareWithMetadata:attemptNumber:container:accountID:fetchObjectWithCompletionHandler:]_block_invoke_2.cold.1 : 236 -> 240
~ ___120-[ICCollaborationController acceptShareWithMetadata:attemptNumber:container:accountID:fetchObjectWithCompletionHandler:]_block_invoke_2.cold.2 : 212 -> 216
~ ___120-[ICCollaborationController acceptShareWithMetadata:attemptNumber:container:accountID:fetchObjectWithCompletionHandler:]_block_invoke.147.cold.1 : 160 -> 168
CStrings:
+ "Accepting share: %@, account ID = %@, attemptNumber = %@"
+ "Error accepting share %@ %@: %@"
+ "Retrying accept share %@ %@"
+ "Share %@ accepted in operation %@"
- "Accepting shared object at URL: %@, account ID = %@, attemptNumber = %@"
- "Error accepting share at URL %@ %@: %@"
- "Retrying accept share at URL %@ %@"
- "Share accepted for URL %@ %@"

```
