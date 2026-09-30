## VideoSubscriberAccountUI

> `/System/Library/PrivateFrameworks/VideoSubscriberAccountUI.framework/VideoSubscriberAccountUI`

```diff

-593.20.1.0.0
-  __TEXT.__text: 0x596ac
+593.30.1.0.0
+  __TEXT.__text: 0x59928
   __TEXT.__auth_stubs: 0xb30
-  __TEXT.__objc_methlist: 0x8768
+  __TEXT.__objc_methlist: 0x8790
   __TEXT.__const: 0x2e2
-  __TEXT.__cstring: 0x53cc
+  __TEXT.__cstring: 0x541c
   __TEXT.__gcc_except_tab: 0x106c
   __TEXT.__oslogstring: 0x341b
   __TEXT.__ustring: 0x10

   __TEXT.__swift5_fieldmd: 0x28
   __TEXT.__swift5_proto: 0x10
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x1620
+  __TEXT.__unwind_info: 0x1628
   __TEXT.__eh_frame: 0x40
   __TEXT.__objc_classname: 0x13b7
-  __TEXT.__objc_methname: 0x14d65
+  __TEXT.__objc_methname: 0x14d74
   __TEXT.__objc_methtype: 0x356a
-  __TEXT.__objc_stubs: 0xe120
+  __TEXT.__objc_stubs: 0xe140
   __DATA_CONST.__got: 0xa10
-  __DATA_CONST.__const: 0x1970
+  __DATA_CONST.__const: 0x1998
   __DATA_CONST.__objc_classlist: 0x3f8
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x1f8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4af0
+  __DATA_CONST.__objc_selrefs: 0x4af8
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x310
   __DATA_CONST.__objc_arraydata: 0x60
   __AUTH_CONST.__auth_got: 0x5a8
   __AUTH_CONST.__const: 0x7b8
-  __AUTH_CONST.__cfstring: 0x45e0
+  __AUTH_CONST.__cfstring: 0x4600
   __AUTH_CONST.__objc_const: 0x15528
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_arrayobj: 0x78

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 04735ACD-F3BC-3CA9-BE63-E1970167999C
-  Functions: 2735
-  Symbols:   10162
-  CStrings:  5537
+  UUID: 0FD5AECA-B8FE-3755-8538-10AD45B2BE00
+  Functions: 2738
+  Symbols:   10171
+  CStrings:  5541
 
Symbols:
+ +[VSIdentityProviderLogoView preferredHeight]
+ -[VSTwoFactorEntryViewController_iOS viewWillTransitionToSize:withTransitionCoordinator:]
+ __OBJC_$_CLASS_METHODS_VSIdentityProviderLogoView
+ ___89-[VSTwoFactorEntryViewController_iOS viewWillTransitionToSize:withTransitionCoordinator:]_block_invoke
+ ___block_descriptor_40_e8_32s_e56_v16?0"<UIViewControllerTransitionCoordinatorContext>"8ls32l8
+ _objc_msgSend$animateAlongsideTransition:completion:
+ _objc_msgSend$constraintEqualToAnchor:multiplier:
+ _objc_msgSend$marginLength
- _objc_msgSend$constraintGreaterThanOrEqualToAnchor:
- _objc_msgSend$constraintLessThanOrEqualToAnchor:
Functions:
~ -[VSTwoFactorEntryViewController_iOS viewDidLoad] : 3132 -> 3188
+ -[VSTwoFactorEntryViewController_iOS viewWillTransitionToSize:withTransitionCoordinator:]
+ -[VSTwoFactorEntryViewController_iOS verifyButtonPressed:]
~ -[VSCredentialEntryViewController_iOS viewDidLoad] : 460 -> 472
+ +[VSIdentityProviderLogoView preferredHeight]
~ -[VSIdentityProviderLogoView _height] : 12 -> 40
~ -[VSIdentityProviderLogoView sizeThatFits:] : 44 -> 156
~ -[VSAutoAuthenticationViewController_iOS viewDidLoad] : 2940 -> 3080
CStrings:
+ "animateAlongsideTransition:completion:"
+ "constraintEqualToAnchor:multiplier:"
+ "logoHeight"
+ "marginLength"
+ "v16@?0@\"<UIViewControllerTransitionCoordinatorContext>\"8"
- "constraintGreaterThanOrEqualToAnchor:"
- "constraintLessThanOrEqualToAnchor:"

```
