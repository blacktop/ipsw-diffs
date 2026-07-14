## MessagesSettingsUI

> `/System/Library/PrivateFrameworks/MessagesSettingsUI.framework/MessagesSettingsUI`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__got`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`

```diff

-  __TEXT.__text: 0x2fd00
+  __TEXT.__text: 0x2fd20
   __TEXT.__auth_stubs: 0x11c0
   __TEXT.__delay_helper: 0xdc
   __TEXT.__objc_methlist: 0x1514

   __TEXT.__unwind_info: 0xd80
   __TEXT.__eh_frame: 0xb4
   __TEXT.__objc_classname: 0x852
-  __TEXT.__objc_methname: 0x538f
+  __TEXT.__objc_methname: 0x539f
   __TEXT.__objc_methtype: 0xe5e
   __TEXT.__objc_stubs: 0x3f20
   __DATA_CONST.__got: 0x670
Symbols:
+ _objc_msgSend$deviceIsLockedDownFor:senderOrigin:
- _objc_msgSend$deviceIsLockedDown
Functions:
~ -[CKSettingsSharedWithYouController specifiers] : 572 -> 580
~ -[CKSettingsSharedWithYouController sharedWithYouEnabled:] : 220 -> 228
~ -[CKSettingsSharedWithYouController appIsEnabled:] : 456 -> 464
~ -[CKSharedSettingsHelper _sharedWithYouEnabled] : 108 -> 116
CStrings:
+ "deviceIsLockedDownFor:senderOrigin:"
- "deviceIsLockedDown"
```
