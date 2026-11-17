## TVRemoteUI

> `/System/Library/PrivateFrameworks/TVRemoteUI.framework/TVRemoteUI`

```diff

-627.20.10.0.0
-  __TEXT.__text: 0xd1578
-  __TEXT.__objc_methlist: 0xbca4
-  __TEXT.__const: 0x2614
-  __TEXT.__cstring: 0x4e91
-  __TEXT.__gcc_except_tab: 0x1e48
-  __TEXT.__oslogstring: 0x5e86
+627.20.15.0.0
+  __TEXT.__text: 0xd234c
+  __TEXT.__objc_methlist: 0xbcf4
+  __TEXT.__const: 0x2634
+  __TEXT.__cstring: 0x4f81
+  __TEXT.__gcc_except_tab: 0x1e4c
+  __TEXT.__oslogstring: 0x61c6
   __TEXT.__ustring: 0x34
   __TEXT.__dlopen_cstrs: 0xa2
   __TEXT.__constg_swiftt: 0x2e90

   __TEXT.__swift_as_entry: 0xc
   __TEXT.__swift_as_ret: 0x10
   __TEXT.__swift_as_cont: 0x20
-  __TEXT.__unwind_info: 0x3898
+  __TEXT.__unwind_info: 0x38b0
   __TEXT.__eh_frame: 0xa20
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1978
+  __DATA_CONST.__const: 0x1950
   __DATA_CONST.__objc_classlist: 0x5d8
   __DATA_CONST.__objc_catlist: 0x60
   __DATA_CONST.__objc_protolist: 0x1f0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6cf8
+  __DATA_CONST.__objc_selrefs: 0x6db8
   __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__objc_superrefs: 0x398
   __DATA_CONST.__objc_arraydata: 0x118
-  __DATA_CONST.__got: 0xe38
+  __DATA_CONST.__got: 0xe50
   __AUTH_CONST.__const: 0x30f0
-  __AUTH_CONST.__cfstring: 0x3900
-  __AUTH_CONST.__objc_const: 0x156f0
+  __AUTH_CONST.__cfstring: 0x3980
+  __AUTH_CONST.__objc_const: 0x15720
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x240
   __AUTH_CONST.__objc_doubleobj: 0x90

   __AUTH_CONST.__auth_got: 0xf28
   __AUTH.__objc_data: 0x6ab0
   __AUTH.__data: 0x670
-  __DATA.__objc_ivar: 0xbc0
+  __DATA.__objc_ivar: 0xbc4
   __DATA.__data: 0x2590
   __DATA.__common: 0x4c0
   __DATA_DIRTY.__objc_data: 0x820

   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /System/Library/PrivateFrameworks/SpringBoardUIServices.framework/SpringBoardUIServices
   - /System/Library/PrivateFrameworks/TVRemoteCore.framework/TVRemoteCore
+  - /System/Library/PrivateFrameworks/TextInput.framework/TextInput
   - /System/Library/PrivateFrameworks/UIFoundation.framework/UIFoundation
   - /System/Library/PrivateFrameworks/WiFiKit.framework/WiFiKit
   - /usr/lib/libAccessibility.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 4958
-  Symbols:   7126
-  CStrings:  1267
+  Functions: 4966
+  Symbols:   7137
+  CStrings:  1283
 
Symbols:
+ -[TVRCKeyboardAttributes(TVRemoteUI) removeDocumentText]
+ -[TVRKeyboardView _becomeFirstResponderIfDeferred]
+ -[TVRKeyboardView _hasReceivedDocumentTraits]
+ -[TVRKeyboardView _logAutoFillStateWithReason:]
+ -[TVRKeyboardView _setSessionDocumentTextIfNeeded:]
+ -[TVRKeyboardView focusDeferredForTraits]
+ -[TVRKeyboardView setFocusDeferredForTraits:]
+ _OBJC_CLASS_$_RTIDocumentState
+ _OBJC_CLASS_$_TIDocumentState
+ _OBJC_IVAR_$_TVRKeyboardView._focusDeferredForTraits
+ _UITextContentTypePassword
+ ___39-[TVRKeyboardView becomeFirstResponder]_block_invoke
- ___block_descriptor_72_e8_32s_e5_v8?0ls32l8
CStrings:
+ "%s attributes %p: RTI session %{bool}d, payload class %{public}@ (data length %lu), applying via %{public}@"
+ "%s gave up waiting for the TV's text input traits"
+ "%s ignoring keyboard hide, the scene is active (AutoFill or other system UI took focus)"
+ "%s skipping, these are the attributes already applied (%p)"
+ "%s skipping, these are the attributes already set (%p)"
+ "%s waiting for the TV's text input traits before taking focus"
+ "-[TVRAlertController setKeyboardAttributes:]"
+ "-[TVRCKeyboardAttributes(TVRemoteUI) applyToTextField:]"
+ "-[TVRKeyboardView becomeFirstResponder]_block_invoke"
+ "-[TVRKeyboardView setAttributes:]"
+ "AutoFill state (%{public}@): session bundleId '%{public}@', appId '%{public}@', autofillMode %ld, session secure %{bool}d, session contentType '%{public}@'; local secure %{bool}d, local contentType '%{public}@'; applied attributes %p (payload %lu bytes)"
+ "RTI payload"
+ "TV field traits: textContentType '%{public}@', secureTextEntry %{bool}d, keyboardType %ld; local secureTextEntry %{bool}d, textContentType '%{public}@'"
+ "began editing"
+ "ended editing"
+ "legacy attributes"
```
