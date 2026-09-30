## DocumentManager

> `/System/Library/PrivateFrameworks/DocumentManager.framework/DocumentManager`

```diff

-367.4.8.0.0
-  __TEXT.__text: 0x365b0
+367.5.1.0.0
+  __TEXT.__text: 0x366e4
   __TEXT.__auth_stubs: 0x860
   __TEXT.__objc_methlist: 0x2e1c
   __TEXT.__const: 0x190
   __TEXT.__cstring: 0x4bec
   __TEXT.__ustring: 0x6a2
-  __TEXT.__oslogstring: 0x31e7
+  __TEXT.__oslogstring: 0x3252
   __TEXT.__gcc_except_tab: 0x998
   __TEXT.__unwind_info: 0xec8
   __TEXT.__objc_classname: 0x787

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 326B7E13-609D-3A5C-AF73-C8754B24FB57
-  Functions: 1264
-  Symbols:   4872
-  CStrings:  3294
+  UUID: 9E0B75B1-4EB2-36CB-8B86-EF70B4235F7F
+  Functions: 1265
+  Symbols:   4878
+  CStrings:  3296
 
Symbols:
+ ___86-[UIDocumentBrowserViewController renameDocumentAtURL:proposedName:completionHandler:]_block_invoke_2.cold.1
Functions:
~ ___86-[UIDocumentBrowserViewController renameDocumentAtURL:proposedName:completionHandler:]_block_invoke_2 : 224 -> 308
+ _OUTLINED_FUNCTION_15
+ _OUTLINED_FUNCTION_3
- _OUTLINED_FUNCTION_15
~ +[DOCFileRenamingSupport fallbackRename:toProposedName:error:] : 584 -> 760
- _OUTLINED_FUNCTION_3
~ ___84-[UIDocumentBrowserViewController _requestAnimationInfoForDocumentAtURL:completion:]_block_invoke_7.cold.1 : 132 -> 128
~ ___81-[UIDocumentBrowserViewController revealDocumentAtURL:importIfNeeded:completion:]_block_invoke_2.126.cold.1 : 88 -> 84
~ ___92-[UIDocumentBrowserViewController _importDocumentAtURL:neighbourURL:mode:completionHandler:]_block_invoke_2.143.cold.1 : 88 -> 84
~ ___57-[UIDocumentBrowserViewController _didPickItemBookmarks:]_block_invoke.cold.1 : 88 -> 84
~ ___57-[UIDocumentBrowserViewController _didPickItemBookmarks:]_block_invoke.cold.2 : 88 -> 84
~ ___78-[UIDocumentBrowserViewController _iOS_didRequestDocumentCreationWithHandler:]_block_invoke.cold.1 : 80 -> 76
~ -[UIDocumentBrowserViewController renameDocumentAtURL:proposedName:completionHandler:].cold.4 : 80 -> 68
~ -[UIDocumentBrowserViewController renameDocumentAtURL:proposedName:completionHandler:].cold.5 : 80 -> 68
+ ___86-[UIDocumentBrowserViewController renameDocumentAtURL:proposedName:completionHandler:]_block_invoke_2.cold.1
CStrings:
+ "Failed to update the sandbox extension for %@: %d"
+ "Failed to update the sandbox extension from %@ to %@: %d"

```
