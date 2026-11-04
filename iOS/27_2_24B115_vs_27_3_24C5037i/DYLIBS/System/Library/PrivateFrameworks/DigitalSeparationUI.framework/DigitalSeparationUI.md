## DigitalSeparationUI

> `/System/Library/PrivateFrameworks/DigitalSeparationUI.framework/DigitalSeparationUI`

```diff

-653.0.10.0.0
-  __TEXT.__text: 0x58fc4
-  __TEXT.__objc_methlist: 0x5610
-  __TEXT.__cstring: 0x4941
+653.0.15.0.0
+  __TEXT.__text: 0x59ca0
+  __TEXT.__objc_methlist: 0x5708
+  __TEXT.__cstring: 0x4ac1
   __TEXT.__const: 0x1014
   __TEXT.__gcc_except_tab: 0x83c
-  __TEXT.__oslogstring: 0x2897
+  __TEXT.__oslogstring: 0x28c7
   __TEXT.__dlopen_cstrs: 0x332
   __TEXT.__constg_swiftt: 0x788
   __TEXT.__swift5_typeref: 0x6be

   __TEXT.__swift_as_entry: 0x70
   __TEXT.__swift_as_ret: 0x90
   __TEXT.__swift_as_cont: 0x94
-  __TEXT.__unwind_info: 0x2128
+  __TEXT.__unwind_info: 0x2178
   __TEXT.__eh_frame: 0xe10
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x1320
-  __DATA_CONST.__objc_classlist: 0x208
+  __DATA_CONST.__objc_classlist: 0x210
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x35e8
+  __DATA_CONST.__objc_selrefs: 0x3640
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x1a8
+  __DATA_CONST.__objc_superrefs: 0x1b0
   __DATA_CONST.__objc_arraydata: 0x90
-  __DATA_CONST.__got: 0x8d8
-  __AUTH_CONST.__const: 0x11d8
-  __AUTH_CONST.__cfstring: 0x4be0
-  __AUTH_CONST.__objc_const: 0x11f38
+  __DATA_CONST.__got: 0x8e8
+  __AUTH_CONST.__const: 0x11f8
+  __AUTH_CONST.__cfstring: 0x4d80
+  __AUTH_CONST.__objc_const: 0x12d28
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__objc_intobj: 0x240
   __AUTH_CONST.__auth_got: 0x930
-  __AUTH.__objc_data: 0xd8
-  __DATA.__objc_ivar: 0x488
+  __AUTH.__objc_data: 0x128
+  __DATA.__objc_ivar: 0x494
   __DATA.__data: 0xda0
   __DATA.__common: 0x1f8
   __DATA_DIRTY.__objc_data: 0x1560
   __DATA_DIRTY.__data: 0x490
-  __DATA_DIRTY.__bss: 0x198
+  __DATA_DIRTY.__bss: 0x1a8
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/ContactsUI.framework/ContactsUI

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2497
-  Symbols:   3439
-  CStrings:  945
+  Functions: 2522
+  Symbols:   3473
+  CStrings:  960
 
Symbols:
+ -[DSEmergencyResetController disableSiriRecap:]
+ -[DSSiriRecapController .cxx_destruct]
+ -[DSSiriRecapController _pushNextPane]
+ -[DSSiriRecapController cellWithText:secondaryText:]
+ -[DSSiriRecapController delegate]
+ -[DSSiriRecapController disableSiriRecapAndPushNextPane]
+ -[DSSiriRecapController init]
+ -[DSSiriRecapController orderedCells]
+ -[DSSiriRecapController presentDisableConfirmationDialog]
+ -[DSSiriRecapController presentLearnMore]
+ -[DSSiriRecapController setDelegate:]
+ -[DSSiriRecapController setOrderedCells:]
+ -[DSSiriRecapController setUpWatchInfoCells]
+ -[DSSiriRecapController setViewModel:]
+ -[DSSiriRecapController shouldShow]
+ -[DSSiriRecapController tableView:cellForRowAtIndexPath:]
+ -[DSSiriRecapController tableView:editingStyleForRowAtIndexPath:]
+ -[DSSiriRecapController tableView:numberOfRowsInSection:]
+ -[DSSiriRecapController viewDidLoad]
+ -[DSSiriRecapController viewModel]
+ _OBJC_CLASS_$_DSSiriRecapController
+ _OBJC_CLASS_$_DSSiriRecapViewModel
+ _OBJC_IVAR_$_DSSiriRecapController._delegate
+ _OBJC_IVAR_$_DSSiriRecapController._orderedCells
+ _OBJC_IVAR_$_DSSiriRecapController._viewModel
+ _OBJC_METACLASS_$_DSSiriRecapController
+ __OBJC_$_INSTANCE_METHODS_DSSiriRecapController
+ __OBJC_$_INSTANCE_VARIABLES_DSSiriRecapController
+ __OBJC_$_PROP_LIST_DSSiriRecapController
+ __OBJC_CLASS_PROTOCOLS_$_DSSiriRecapController
+ __OBJC_CLASS_RO_$_DSSiriRecapController
+ __OBJC_METACLASS_RO_$_DSSiriRecapController
+ ___57-[DSSiriRecapController presentDisableConfirmationDialog]_block_invoke
+ ___57-[DSSiriRecapController presentDisableConfirmationDialog]_block_invoke_2
CStrings:
+ "DEVICE_PAIRED_DATE"
+ "DEVICE_SERIAL_NUMBER"
+ "DSSiriRecapController"
+ "Emergency Reset: finished disabling Siri Recap."
+ "Emergency Reset: started disabling Siri Recap."
+ "NAME"
+ "SIRI_RECAP_DETAIL"
+ "SIRI_RECAP_DETAIL_VIEW_CELL_ACTIVATION_DATE"
+ "SIRI_RECAP_DISABLE_BUTTON_TEXT"
+ "SIRI_RECAP_DISABLE_CONFIRMATION_MESSAGE"
+ "SIRI_RECAP_DISABLE_CONFIRMATION_TITLE"
+ "SIRI_RECAP_LEARN_MORE_URL"
+ "SIRI_RECAP_NAME_FALLBACK"
+ "SIRI_RECAP_TITLE"
+ "applewatch.radiowaves.left.and.right"
```
