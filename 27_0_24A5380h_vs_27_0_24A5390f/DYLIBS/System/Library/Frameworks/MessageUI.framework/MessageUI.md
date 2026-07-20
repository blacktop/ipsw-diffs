## MessageUI

> `/System/Library/Frameworks/MessageUI.framework/MessageUI`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_floatobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-3895.100.17.2.1
-  __TEXT.__text: 0x14f114
+3897.100.8.2.5
+  __TEXT.__text: 0x14f7f0
   __TEXT.__delay_helper: 0x114
-  __TEXT.__objc_methlist: 0x129f4
-  __TEXT.__cstring: 0xa0d6
-  __TEXT.__gcc_except_tab: 0x25148
+  __TEXT.__objc_methlist: 0x12aac
+  __TEXT.__cstring: 0xa0e6
+  __TEXT.__gcc_except_tab: 0x25208
   __TEXT.__const: 0x1ff4
   __TEXT.__ustring: 0x4dc
-  __TEXT.__oslogstring: 0x5d6e
+  __TEXT.__oslogstring: 0x5e0e
   __TEXT.__dlopen_cstrs: 0x4bf
   __TEXT.__swift5_typeref: 0x1894
   __TEXT.__swift5_reflstr: 0x5a8

   __TEXT.__swift_as_entry: 0x28
   __TEXT.__swift_as_ret: 0x2c
   __TEXT.__swift_as_cont: 0x50
-  __TEXT.__unwind_info: 0xa588
+  __TEXT.__unwind_info: 0xa5c8
   __TEXT.__eh_frame: 0x5e8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x108
   __DATA_CONST.__objc_protolist: 0x418
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc200
+  __DATA_CONST.__objc_selrefs: 0xc278
   __DATA_CONST.__objc_protorefs: 0x68
   __DATA_CONST.__objc_superrefs: 0x4b0
-  __DATA_CONST.__objc_arraydata: 0x628
-  __DATA_CONST.__got: 0x1ee0
+  __DATA_CONST.__objc_arraydata: 0x648
+  __DATA_CONST.__got: 0x1ee8
   __AUTH_CONST.__const: 0x1c90
-  __AUTH_CONST.__cfstring: 0x8e40
-  __AUTH_CONST.__objc_const: 0x1a778
+  __AUTH_CONST.__cfstring: 0x8e60
+  __AUTH_CONST.__objc_const: 0x1a810
   __AUTH_CONST.__objc_floatobj: 0x20
   __AUTH_CONST.__objc_intobj: 0x1b0
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH_CONST.__objc_dictobj: 0x578
+  __AUTH_CONST.__objc_dictobj: 0x5a0
   __AUTH_CONST.__auth_got: 0x18f8
   __AUTH.__objc_data: 0x3588
   __AUTH.__data: 0x360
-  __DATA.__objc_ivar: 0x1144
+  __DATA.__objc_ivar: 0x1148
   __DATA.__data: 0x3818
-  __DATA.__bss: 0x1d50
+  __DATA.__bss: 0x1d60
   __DATA.__common: 0x2f8
   __DATA_DIRTY.__objc_data: 0xb90
   __DATA_DIRTY.__data: 0x8

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 6860
-  Symbols:   16197
-  CStrings:  2048
+  Functions: 6870
+  Symbols:   16218
+  CStrings:  2051
 
Symbols:
+ -[MFComposeWebView _composeToolbarShouldProvideWritingToolsButton]
+ -[MFComposeWebView _writingToolsBarButtonItem]
+ -[MFComposeWebView placeCaretBeforeSignature]
+ -[MFMailComposeView _horizontallySafeAreaAdjustedBounds]
+ -[MFMailComposeView _updateHeaderViewLayoutMargins]
+ -[MFMessageComposeViewController insertCompositionText:]
+ -[MFMessageComposeViewController setSuppressesShelfStaging:]
+ -[MFMessageComposeViewController supportsCompositionTextInsertion]
+ -[_MFMailCompositionContext setSuppressAppIntentDonation:]
+ -[_MFMailCompositionContext suppressAppIntentDonation]
+ GCC_except_table229
+ GCC_except_table265
+ _OBJC_IVAR_$__MFMailCompositionContext._suppressAppIntentDonation
+ _UIFontWeightRegular
+ _objc_msgSend$_composeToolbarShouldProvideWritingToolsButton
+ _objc_msgSend$_horizontallySafeAreaAdjustedBounds
+ _objc_msgSend$_updateHeaderViewLayoutMargins
+ _objc_msgSend$_writingToolsBarButtonItem
+ _objc_msgSend$insertCompositionText:
+ _objc_msgSend$isKeyboardVisible
+ _objc_msgSend$placeCaretBeforeSignature
+ _objc_msgSend$setKeyboardVisible:animate:
+ _objc_msgSend$setSuppressesShelfStaging:
+ _objc_msgSend$systemFontOfSize:weight:
- GCC_except_table242
- GCC_except_table252
- GCC_except_table268
CStrings:
+ ".MailOutline"
+ "<%p> Skipping attachment with no contentID-derived URL for fileName: %{public}@"
+ "<%p> Skipping attachment with no contentID-derived URL for identifier: %{public}@"
```
