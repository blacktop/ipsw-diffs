## DirectoryEditor

> `/System/Library/PrivateFrameworks/DirectoryEditor.framework/Versions/A/DirectoryEditor`

```diff

 71.0.0.0.0
-  __TEXT.__text: 0xa264
+  __TEXT.__text: 0xa234
   __TEXT.__auth_stubs: 0x1b0
-  __TEXT.__objc_methlist: 0xa20
+  __TEXT.__objc_methlist: 0xb3c
   __TEXT.__const: 0x30
   __TEXT.__cstring: 0x723
   __TEXT.__unwind_info: 0x260

   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xdf8
+  __DATA_CONST.__objc_selrefs: 0xe80
   __DATA_CONST.__objc_superrefs: 0x40
   __AUTH_CONST.__auth_got: 0xe0
   __AUTH_CONST.__const: 0x120
   __AUTH_CONST.__cfstring: 0xd60
-  __AUTH_CONST.__objc_const: 0x19c0
+  __AUTH_CONST.__objc_const: 0x17b0
   __AUTH.__objc_data: 0x2d0
   __DATA.__objc_ivar: 0x1c4
   __DATA.__data: 0xc0

   - /System/Library/Frameworks/SystemConfiguration.framework/Versions/A/SystemConfiguration
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 317CEB53-C081-3431-BD23-7D37B85229B8
+  UUID: 3F7E7050-D2BF-3F57-A0E1-1BB71DDF2B7A
   Functions: 220
   Symbols:   895
   CStrings:  903
Functions:
~ -[DirectoryEditorViewController setNode:isAuthed:authedAs:] : 220 -> 216
~ -[DirectoryEditorViewController query:foundResults:error:] : 1836 -> 1824
~ -[DirectoryEditorViewController setOdSession:] : 420 -> 424
~ -[DirectoryEditorViewController(PrivateMethods) searchTimer:] : 88 -> 92
~ -[DirectoryEditorViewController(PrivateMethods) saveChangesAlertDidEnd:returnCode:contextInfo:] : 308 -> 304
~ -[DefaultDirEditorPlugin addValueMenuItemSelected:] : 960 -> 964
~ -[DefaultDirEditorPlugin newAttributeSheetButtonHit:] : 976 -> 972
~ -[DefaultDirEditorPlugin(PrivateMethods) populateSelectedAttributeValue] : 956 -> 940
~ -[DefaultDirEditorPlugin(PrivateMethods) recordUnsavedEdits] : 796 -> 792
~ -[DefaultDirEditorPlugin(NSKeyValueObserving) observeValueForKeyPath:ofObject:change:context:] : 1328 -> 1312
~ -[DEDragReceiverView drawRect:] : 212 -> 216
~ -[NSTextField(XSAdditions) setDisplaysAsLabel:] : 228 -> 224

```
