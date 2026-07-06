## GameCenterUI

> `/System/iOSSupport/System/Library/PrivateFrameworks/GameCenterUI.framework/Versions/A/GameCenterUI`

```diff

-  __TEXT.__text: 0x66e6c
-  __TEXT.__objc_methlist: 0x3c44
+  __TEXT.__text: 0x66ff0
+  __TEXT.__objc_methlist: 0x3c3c
   __TEXT.__const: 0x3164
-  __TEXT.__cstring: 0x2e93
-  __TEXT.__gcc_except_tab: 0x398
+  __TEXT.__cstring: 0x2eb3
+  __TEXT.__gcc_except_tab: 0x348
   __TEXT.__oslogstring: 0x2385
   __TEXT.__constg_swiftt: 0xe70
   __TEXT.__swift5_typeref: 0x6182

   __TEXT.__swift5_mpenum: 0x18
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift_as_cont: 0x224
-  __TEXT.__unwind_info: 0x2310
+  __TEXT.__unwind_info: 0x2328
   __TEXT.__eh_frame: 0x1e28
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x124c
-  __DATA_CONST.__objc_classlist: 0x200
+  __DATA_CONST.__const: 0x1274
+  __DATA_CONST.__objc_classlist: 0x1f8
   __DATA_CONST.__objc_catlist: 0xc8
   __DATA_CONST.__objc_protolist: 0xd0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x31b8
+  __DATA_CONST.__objc_selrefs: 0x3200
   __DATA_CONST.__objc_protorefs: 0x50
   __DATA_CONST.__objc_classrefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0xf0
+  __DATA_CONST.__objc_superrefs: 0xe8
   __DATA_CONST.__objc_arraydata: 0x8
-  __DATA_CONST.__got: 0xb30
+  __DATA_CONST.__got: 0xb48
   __AUTH_CONST.__const: 0x2bc0
   __AUTH_CONST.__cfstring: 0x18c0
-  __AUTH_CONST.__objc_const: 0x8c88
+  __AUTH_CONST.__objc_const: 0x8c58
   __AUTH_CONST.__objc_intobj: 0x1e0
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_got: 0x14e8
-  __AUTH.__objc_data: 0x1700
+  __AUTH.__objc_data: 0x16b0
   __AUTH.__data: 0x6e0
-  __DATA.__objc_ivar: 0x2d4
+  __DATA.__objc_ivar: 0x2e0
   __DATA.__data: 0x1388
   __DATA.__objc_stublist: 0x8
   __DATA.__bss: 0x1c00

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 3313
-  Symbols:   5106
-  CStrings:  723
+  Symbols:   5112
+  CStrings:  724
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift_as_entry : content changed
~ __TEXT.__swift_as_ret : content changed
~ __TEXT.__swift_as_cont : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_classrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH.__data : content changed
~ __DATA.__data : content changed
~ __DATA.__objc_stublist : content changed
~ __DATA_DIRTY.__objc_data : content changed
~ __DATA_DIRTY.__data : content changed
Symbols:
+ -[GKNoContentView updateConfiguration]
+ OBJC_IVAR_$_GKNoContentView._buttonTitle
+ OBJC_IVAR_$_GKNoContentView._message
+ OBJC_IVAR_$_GKNoContentView._title
+ _OBJC_CLASS_$_UIAction
+ _OBJC_CLASS_$_UIButtonConfiguration
+ _OBJC_CLASS_$_UIContentUnavailableConfiguration
+ _OBJC_CLASS_$_UIContentUnavailableView
+ ___38-[GKNoContentView updateConfiguration]_block_invoke
+ ___block_descriptor_40_e8_32w_e18_v16?0"UIAction"8lw32l8
+ _objc_msgSend$actionWithTitle:image:identifier:handler:
+ _objc_msgSend$button
+ _objc_msgSend$buttonProperties
+ _objc_msgSend$emptyConfiguration
+ _objc_msgSend$initWithConfiguration:
+ _objc_msgSend$plainButtonConfiguration
+ _objc_msgSend$setButton:
+ _objc_msgSend$setConfiguration:
+ _objc_msgSend$setPrimaryAction:
+ _objc_msgSend$setSecondaryText:
+ _objc_msgSend$updateConfiguration
- -[GKUIContentUnavailableView _titleFont]
- _OBJC_CLASS_$_GKUIContentUnavailableView
- _OBJC_CLASS_$__UIContentUnavailableView
- _OBJC_METACLASS_$_GKUIContentUnavailableView
- _OBJC_METACLASS_$__UIContentUnavailableView
- __OBJC_$_INSTANCE_METHODS_GKUIContentUnavailableView
- __OBJC_CLASS_RO_$_GKUIContentUnavailableView
- __OBJC_METACLASS_RO_$_GKUIContentUnavailableView
- ___33-[GKNoContentView initWithFrame:]_block_invoke
- _objc_msgSend$buttonTitle
- _objc_msgSend$initWithFrame:title:style:
- _objc_msgSend$message
- _objc_msgSend$setButtonAction:
- _objc_msgSend$setButtonTitle:
- _objc_msgSend$setMessage:
Functions:
~ -[GKUIContentUnavailableView _titleFont] -> -[GKNoContentView initWithFrame:] : 176 -> 776
~ -[GKNoContentView initWithFrame:] -> -[GKNoContentView updateConfiguration] : 924 -> 464
~ -[GKNoContentView setTitle:] : 20 -> 84
~ -[GKNoContentView setMessage:] : 20 -> 84
~ -[GKNoContentView setButtonTitle:] : 20 -> 84
~ -[GKNoContentView .cxx_destruct] : 124 -> 184
~ sub_2b3cffd2c -> sub_2bcf5ceb4 : 1040 -> 1036
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ky3Jt3/Sources/GameCenterUI_iosmac/Frameworks/GameCenterUI/iOS/Framework/API/GKFriendRequestComposeViewController.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ky3Jt3/Sources/GameCenterUI_iosmac/Frameworks/GameCenterUI/iOS/Framework/NSLayoutConstraint+GKAdditions.m"
+ "v16@?0@\"UIAction\"8"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4iVqCb/Sources/GameCenterUI_iosmac/Frameworks/GameCenterUI/iOS/Framework/API/GKFriendRequestComposeViewController.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4iVqCb/Sources/GameCenterUI_iosmac/Frameworks/GameCenterUI/iOS/Framework/NSLayoutConstraint+GKAdditions.m"

```
