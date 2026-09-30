## AOSUI

> `/System/Library/PrivateFrameworks/AOSUI.framework/Versions/A/AOSUI`

```diff

-  __TEXT.__text: 0x113dc8
-  __TEXT.__objc_methlist: 0x10c3c
+  __TEXT.__text: 0x113a14
+  __TEXT.__objc_methlist: 0x10c34
   __TEXT.__const: 0x2c8
-  __TEXT.__cstring: 0x12ac2
-  __TEXT.__oslogstring: 0xcb7b
+  __TEXT.__cstring: 0x12a3c
+  __TEXT.__oslogstring: 0xccc2
   __TEXT.__gcc_except_tab: 0x173c
   __TEXT.__ustring: 0x132
   __TEXT.__dlopen_cstrs: 0x1f4

   __DATA_CONST.__objc_catlist: 0x60
   __DATA_CONST.__objc_protolist: 0x260
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9718
+  __DATA_CONST.__objc_selrefs: 0x9728
   __DATA_CONST.__objc_protorefs: 0x58
   __DATA_CONST.__objc_superrefs: 0x478
   __DATA_CONST.__objc_arraydata: 0x108
-  __DATA_CONST.__got: 0x1878
+  __DATA_CONST.__got: 0x1888
   __AUTH_CONST.__const: 0x42f0
-  __AUTH_CONST.__cfstring: 0xc940
+  __AUTH_CONST.__cfstring: 0xc8e0
   __AUTH_CONST.__objc_const: 0x2f370
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_doubleobj: 0x10

   - /usr/lib/libDiagnosticMessagesClient.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 7268
-  Symbols:   17081
-  CStrings:  4911
+  Functions: 7265
+  Symbols:   17080
+  CStrings:  4910
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_doubleobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH.__objc_data : content changed
~ __AUTH.__data : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
Symbols:
+ -[MMService dataclassActionsForEnablingDataclass]
+ -[MMService hasDataToMerge:]
+ GCC_except_table47
+ GCC_except_table53
+ GCC_except_table82
+ GCC_except_table85
+ GCC_except_table96
+ _objc_msgSend$dataclassActionsForEnablingDataclass
+ _objc_msgSend$hasDataToMerge:
+ _objc_msgSend$instanceMethodForSelector:
- -[MMCalendarsService _presentMergeDialogWithWindow:completionHandler:]
- -[iCloudFreeformService enableAlertMessage:]
- GCC_except_table54
- GCC_except_table81
- GCC_except_table94
- ___108-[MMContactsService performDataclassActionsForService:willEnable:shouldCreate:withWindow:completionHandler:]_block_invoke
- ___109-[MMRemindersService performDataclassActionsForService:willEnable:shouldCreate:withWindow:completionHandler:]_block_invoke
- ___70-[MMCalendarsService _presentMergeDialogWithWindow:completionHandler:]_block_invoke
- _kMMPropertyServiceEnableDataclassActions
- _objc_msgSend$_presentMergeDialogWithWindow:completionHandler:
CStrings:
+ "CONTINUE_AND_MERGE"
+ "DONT_MERGE"
+ "Disable dialog dismissed: serviceID=%@ returnCode=%ld"
+ "GENERIC_ENABLE_CONFIRMATION_TITLE"
+ "GENERIC_MERGE_CONFIRMATION_MESSAGE"
+ "GENERIC_MERGE_OR_DELETE_CONFIRMATION_MESSAGE"
+ "Merge dialog dismissed: serviceID=%@ returnCode=%ld"
+ "Presenting disable dialog: serviceID=%@ defaultActionType=%ld otherActionType=%ld"
+ "Presenting merge dialog: serviceID=%@ otherActionType=%ld"
+ "performDataclassActions: serviceID=%@ willEnable=%d shouldCreate=%d isPrimary=%d"
- "CALENDARS_MERGE_CONFIRMATION_MESSAGE"
- "CALENDARS_MERGE_CONFIRMATION_TITLE"
- "CONTACTS_MERGE_CONFIRMATION_MESSAGE"
- "CONTACTS_MERGE_CONFIRMATION_TITLE"
- "FREEFORM_MERGE_OR_DELETE_CONFIRMATION_MESSAGE"
- "MERGE_WITH_ICLOUD"
- "REMINDERS_MERGE_CONFIRMATION_MESSAGE"
- "REMINDERS_MERGE_CONFIRMATION_TITLE"

```
