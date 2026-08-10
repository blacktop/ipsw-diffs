## ControlCenterUI

> `/System/Library/PrivateFrameworks/ControlCenterUI.framework/ControlCenterUI`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__cstring`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_mpenum`
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
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA_DIRTY.__data`

```diff

-702.0.0.0.0
-  __TEXT.__text: 0xbb00c
-  __TEXT.__objc_methlist: 0xb4f0
+704.0.1.0.0
+  __TEXT.__text: 0xbb298
+  __TEXT.__objc_methlist: 0xb500
   __TEXT.__const: 0x2c3a
   __TEXT.__cstring: 0x4824
   __TEXT.__gcc_except_tab: 0x82c
   __TEXT.__oslogstring: 0x445b
   __TEXT.__dlopen_cstrs: 0x14e
-  __TEXT.__constg_swiftt: 0x2a5c
+  __TEXT.__constg_swiftt: 0x2a7c
   __TEXT.__swift5_typeref: 0x2c40
   __TEXT.__swift5_builtin: 0x1cc
-  __TEXT.__swift5_reflstr: 0x1de2
-  __TEXT.__swift5_fieldmd: 0x1380
+  __TEXT.__swift5_reflstr: 0x1e02
+  __TEXT.__swift5_fieldmd: 0x138c
   __TEXT.__swift5_assocty: 0x198
   __TEXT.__swift5_proto: 0xcc
   __TEXT.__swift5_types: 0x12c

   __TEXT.__swift_as_entry: 0xc
   __TEXT.__swift_as_ret: 0x4
   __TEXT.__swift_as_cont: 0x8
-  __TEXT.__unwind_info: 0x2d70
+  __TEXT.__unwind_info: 0x2d58
   __TEXT.__eh_frame: 0x3e8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x5b0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x68e8
+  __DATA_CONST.__objc_selrefs: 0x6928
   __DATA_CONST.__objc_protorefs: 0x228
   __DATA_CONST.__objc_superrefs: 0x1d0
   __DATA_CONST.__objc_arraydata: 0x68
-  __DATA_CONST.__got: 0xd28
+  __DATA_CONST.__got: 0xd30
   __AUTH_CONST.__const: 0x4471
   __AUTH_CONST.__cfstring: 0x2f80
-  __AUTH_CONST.__objc_const: 0x11108
+  __AUTH_CONST.__objc_const: 0x11190
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__auth_got: 0x1368
   __AUTH.__objc_data: 0x17d0
   __AUTH.__data: 0x6f0
-  __DATA.__objc_ivar: 0x738
-  __DATA.__data: 0x3a70
+  __DATA.__objc_ivar: 0x740
+  __DATA.__data: 0x3a80
   __DATA.__bss: 0x11a0
   __DATA.__common: 0x30
-  __DATA_DIRTY.__objc_data: 0x3a40
+  __DATA_DIRTY.__objc_data: 0x3a68
   __DATA_DIRTY.__data: 0xe60
   __DATA_DIRTY.__bss: 0x8c0
   __DATA_DIRTY.__common: 0x28

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 5045
-  Symbols:   7792
+  Symbols:   7802
   CStrings:  852
 
Symbols:
+ -[CCUIBluetoothModuleViewController _menuContentForActions:]
+ -[CCUIMainViewController overlayCompactStatusBar]
+ -[CCUIOverlayStatusBarPresentationProvider _addCompactStatusBarAlphaAnimationToBatch:transitionState:]
+ -[CCUIOverlayStatusBarPresentationProvider _compactStatusBarAlphaForTransitionState:]
+ GCC_except_table53
+ _OBJC_IVAR_$_CCUIBluetoothModuleViewController._lastPushedContextMenuContent
+ _OBJC_IVAR_$_CCUIMainViewController._appNameMenuBarProvider
+ _OBJC_IVAR_$_CCUIMainViewController._compactStatusBar
+ __UIStatusBarPartIdentifierCenter
+ ___102-[CCUIOverlayStatusBarPresentationProvider _addCompactStatusBarAlphaAnimationToBatch:transitionState:]_block_invoke
+ _objc_msgSend$_addCompactStatusBarAlphaAnimationToBatch:transitionState:
+ _objc_msgSend$_compactStatusBarAlphaForTransitionState:
+ _objc_msgSend$_menuContentForActions:
+ _objc_msgSend$appNameMenuBarProviderForControlCenterViewController:
+ _objc_msgSend$dictionaryWithCapacity:
+ _objc_msgSend$isEqualToDictionary:
+ _objc_msgSend$overlayCompactStatusBar
+ _objc_msgSend$setMenuBarProvider:
+ _objc_msgSend$setObject:forKeyedSubscript:
+ _objc_msgSend$subtitle
- -[CCUIMainViewController overlayLeadingStatusBar]
- -[CCUIOverlayStatusBarPresentationProvider _addLeadingStatusBarAlphaAnimationToBatch:transitionState:]
- -[CCUIOverlayStatusBarPresentationProvider _leadingStatusBarAlphaForTransitionState:]
- GCC_except_table50
- GCC_except_table52
- _OBJC_IVAR_$_CCUIMainViewController._compactLeadingStatusBar
- ___102-[CCUIOverlayStatusBarPresentationProvider _addLeadingStatusBarAlphaAnimationToBatch:transitionState:]_block_invoke
- _objc_msgSend$_addLeadingStatusBarAlphaAnimationToBatch:transitionState:
- _objc_msgSend$_leadingStatusBarAlphaForTransitionState:
- _objc_msgSend$overlayLeadingStatusBar
CStrings:
+ "\xf0\x92!b"
- "\xf0\x82!b"
```
