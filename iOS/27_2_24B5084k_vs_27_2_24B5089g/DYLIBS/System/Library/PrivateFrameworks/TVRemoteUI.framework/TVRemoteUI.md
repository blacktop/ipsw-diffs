## TVRemoteUI

> `/System/Library/PrivateFrameworks/TVRemoteUI.framework/TVRemoteUI`

```diff

-627.10.45.0.0
-  __TEXT.__text: 0xd0a44
+627.10.47.0.0
+  __TEXT.__text: 0xd0c18
   __TEXT.__objc_methlist: 0xbc6c
   __TEXT.__const: 0x2624
   __TEXT.__cstring: 0x4e71

   __TEXT.__swift_as_entry: 0xc
   __TEXT.__swift_as_ret: 0x10
   __TEXT.__swift_as_cont: 0x20
-  __TEXT.__unwind_info: 0x3870
+  __TEXT.__unwind_info: 0x3878
   __TEXT.__eh_frame: 0xa20
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x60
   __DATA_CONST.__objc_protolist: 0x1f0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6c80
+  __DATA_CONST.__objc_selrefs: 0x6c90
   __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__objc_superrefs: 0x398
   __DATA_CONST.__objc_arraydata: 0x118
-  __DATA_CONST.__got: 0xe30
+  __DATA_CONST.__got: 0xe38
   __AUTH_CONST.__const: 0x30d0
   __AUTH_CONST.__cfstring: 0x38c0
   __AUTH_CONST.__objc_const: 0x156f0

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 4949
-  Symbols:   9862
+  Symbols:   9865
   CStrings:  1263
 
Symbols:
+ -[TVRAlertController initForTextPasswordType:styleProvider:]
+ _OBJC_CLASS_$_UIViewReservedRegionKind
+ _objc_msgSend$initForTextPasswordType:styleProvider:
+ _objc_msgSend$occlusionRegionKind
+ _objc_msgSend$reservedRegionsOfKind:
- -[TVRAlertController initForTextPasswordType:]
- _objc_msgSend$initForTextPasswordType:
Functions:
~ -[TVRAlertController initForTextPasswordType:] -> -[TVRAlertController initForTextPasswordType:styleProvider:] : 320 -> 352
~ -[TVRUINowPlayingViewController _computeAndApplyLayout] : 2036 -> 2020
~ -[TVRUIRemoteViewController _presentTextPasswordAlert] : 280 -> 312
~ -[TVRUIResizabilityLayoutManager _occlusionRegionFrame] : 20 -> 440
```
