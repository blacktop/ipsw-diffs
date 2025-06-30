## VoiceTriggerUI

> `/System/Library/PrivateFrameworks/VoiceTriggerUI.framework/VoiceTriggerUI`

```diff

-3406.4.1.0.0
-  __TEXT.__text: 0x655b0
+3406.5.1.0.0
+  __TEXT.__text: 0x65858
   __TEXT.__auth_stubs: 0x1850
-  __TEXT.__objc_methlist: 0x4c2c
+  __TEXT.__objc_methlist: 0x4c3c
   __TEXT.__const: 0x2054
   __TEXT.__gcc_except_tab: 0xa00
-  __TEXT.__cstring: 0x626e
-  __TEXT.__oslogstring: 0x2285
+  __TEXT.__cstring: 0x62be
+  __TEXT.__oslogstring: 0x2305
   __TEXT.__swift5_typeref: 0x2aea
   __TEXT.__swift5_capture: 0x370
   __TEXT.__swift5_fieldmd: 0x638

   __TEXT.__swift5_types: 0x74
   __TEXT.__swift_as_entry: 0x28
   __TEXT.__swift_as_ret: 0x24
-  __TEXT.__unwind_info: 0x1760
+  __TEXT.__unwind_info: 0x1768
   __TEXT.__eh_frame: 0x678
   __TEXT.__objc_classname: 0x973
-  __TEXT.__objc_methname: 0xd59d
+  __TEXT.__objc_methname: 0xd5c8
   __TEXT.__objc_methtype: 0x2d5f
-  __TEXT.__objc_stubs: 0x8820
+  __TEXT.__objc_stubs: 0x8860
   __DATA_CONST.__got: 0x960
   __DATA_CONST.__const: 0xae0
   __DATA_CONST.__objc_classlist: 0x1e0
   __DATA_CONST.__objc_protolist: 0x118
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x32d8
+  __DATA_CONST.__objc_selrefs: 0x32e0
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x130
   __DATA_CONST.__objc_arraydata: 0x378
   __AUTH_CONST.__auth_got: 0xc38
   __AUTH_CONST.__const: 0x1238
   __AUTH_CONST.__cfstring: 0x2ca0
-  __AUTH_CONST.__objc_const: 0x7550
+  __AUTH_CONST.__objc_const: 0x7570
   __AUTH_CONST.__objc_arrayobj: 0x138
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_intobj: 0x3d8
   __AUTH.__objc_data: 0x15e0
   __AUTH.__data: 0x940
-  __DATA.__objc_ivar: 0x5ec
+  __DATA.__objc_ivar: 0x5f0
   __DATA.__data: 0x1498
   __DATA.__bss: 0x1190
   __DATA.__common: 0x40

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 75544AC8-B719-383B-B3B7-8FC6B2D21807
-  Functions: 2278
-  Symbols:   5784
-  CStrings:  3698
+  UUID: 9ED80ECB-F920-3856-90DD-095F8210BCE5
+  Functions: 2279
+  Symbols:   5789
+  CStrings:  3703
 
Symbols:
+ -[VTUIGMEnrollmentViewController viewWillAppear:]
+ _OBJC_IVAR_$_VTUIGMEnrollmentViewController._isSkippingIntroduction
+ _objc_msgSend$_userDidTapContinueButton
+ _objc_msgSend$popToViewController:animated:
+ _objc_msgSend$viewControllers
- _objc_msgSend$popViewControllerAnimated:
Functions:
~ -[VTUIGMEnrollmentViewController _userDidTapContinueButton] : 520 -> 656
+ -[VTUIGMEnrollmentViewController viewWillAppear:]
~ -[VTUIGMEnrollmentViewController onboardingControllerRequestsGoingBack:] : 192 -> 524
~ -[VTUIGMEnrollmentViewController _pushVisualIntelligenceIntro] : 116 -> 164
CStrings:
+ "%s #gmenrollment Enrollment skipped with enrollmentType: %lu"
+ "%s #gmenrollment Unexpected view controller index that we can't pop to: %ld"
+ "-[VTUIGMEnrollmentViewController onboardingControllerRequestsGoingBack:]"
+ "_isSkippingIntroduction"
+ "popToViewController:animated:"
+ "viewControllers"
- "popViewControllerAnimated:"

```
