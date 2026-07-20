## ReplayKit

> `/System/Library/Frameworks/ReplayKit.framework/Versions/A/ReplayKit`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_classrefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__DATA.__data`

```diff

-740.53.1.0.0
-  __TEXT.__text: 0x31468
+740.57.1.0.0
+  __TEXT.__text: 0x31478
   __TEXT.__objc_methlist: 0x348c
   __TEXT.__const: 0x1a8
   __TEXT.__cstring: 0x66e0

   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x20a8
+  __DATA_CONST.__objc_selrefs: 0x20a0
   __DATA_CONST.__objc_protorefs: 0x70
   __DATA_CONST.__objc_classrefs: 0x10
   __DATA_CONST.__objc_superrefs: 0xd0

   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__auth_got: 0x508
-  __AUTH.__objc_data: 0xbe0
+  __AUTH.__objc_data: 0x5f0
   __DATA.__objc_ivar: 0x2ac
   __DATA.__data: 0xa38
   __DATA.__bss: 0x100
-  __DATA_DIRTY.__objc_data: 0x1e0
+  __DATA_DIRTY.__objc_data: 0x7d0
   __DATA_DIRTY.__bss: 0x50
   - /System/Library/Frameworks/AVFAudio.framework/Versions/A/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 1319
-  Symbols:   3057
+  Symbols:   3056
   CStrings:  841
 
Symbols:
+ -[RPPreviewViewController editorExtensionDidFinishWithAction:]
+ -[RPVideoEditorHostRemoteNSViewController editorExtensionDidFinishWithAction:]
+ -[RPVideoEditorViewServiceExtensionHostContext editorExtensionDidFinishWithAction:]
+ ___62-[RPPreviewViewController editorExtensionDidFinishWithAction:]_block_invoke
+ _objc_msgSend$editorExtensionDidFinishWithAction:
- -[RPPreviewViewController viewControlerDidFinish]
- -[RPVideoEditorHostRemoteNSViewController onCancelButtonClickMessage]
- -[RPVideoEditorViewServiceExtensionHostContext onCancelButtonClickMessage]
- ___49-[RPPreviewViewController viewControlerDidFinish]_block_invoke
- _objc_msgSend$onCancelButtonClickMessage
- _objc_msgSend$viewControlerDidFinish
Functions:
~ -[RPVideoEditorHostRemoteNSViewController onCancelButtonClickMessage] -> -[RPVideoEditorHostRemoteNSViewController editorExtensionDidFinishWithAction:] : 64 -> 72
~ -[RPVideoEditorViewServiceExtensionHostContext onCancelButtonClickMessage] -> -[RPVideoEditorViewServiceExtensionHostContext editorExtensionDidFinishWithAction:] : 64 -> 72
```
