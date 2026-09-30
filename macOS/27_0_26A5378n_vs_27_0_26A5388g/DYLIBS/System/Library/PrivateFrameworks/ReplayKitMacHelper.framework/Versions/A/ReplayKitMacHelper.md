## ReplayKitMacHelper

> `/System/Library/PrivateFrameworks/ReplayKitMacHelper.framework/Versions/A/ReplayKitMacHelper`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH.__objc_data`
- `__DATA.__data`

```diff

-740.53.1.0.0
-  __TEXT.__text: 0x8c2c
+740.57.1.0.0
+  __TEXT.__text: 0x8c3c
   __TEXT.__objc_methlist: 0xfac
   __TEXT.__const: 0xa0
   __TEXT.__oslogstring: 0x9a

   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc18
+  __DATA_CONST.__objc_selrefs: 0xc10
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x58
   __DATA_CONST.__got: 0x1d8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 268
-  Symbols:   908
+  Symbols:   907
   CStrings:  57
 
Symbols:
+ -[RPVideoEditorHostRemoteNSViewController editorExtensionDidFinishWithAction:]
+ -[RPVideoEditorViewServiceExtensionHostContext editorExtensionDidFinishWithAction:]
+ -[ReplayKitMacHelperClass editorExtensionDidFinishWithAction:]
+ _objc_msgSend$editorExtensionDidFinishWithAction:
- -[RPVideoEditorHostRemoteNSViewController onCancelButtonClickMessage]
- -[RPVideoEditorViewServiceExtensionHostContext onCancelButtonClickMessage]
- -[ReplayKitMacHelperClass viewControlerDidFinish]
- _objc_msgSend$onCancelButtonClickMessage
- _objc_msgSend$viewControlerDidFinish
Functions:
~ -[RPVideoEditorViewServiceExtensionHostContext onCancelButtonClickMessage] -> -[RPVideoEditorViewServiceExtensionHostContext editorExtensionDidFinishWithAction:] : 64 -> 72
~ -[RPVideoEditorHostRemoteNSViewController onCancelButtonClickMessage] -> -[RPVideoEditorHostRemoteNSViewController editorExtensionDidFinishWithAction:] : 64 -> 72
```
