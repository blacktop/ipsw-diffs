## AppleMediaServicesUI

> `/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/AppleMediaServicesUI`

```diff

-7.2.17.2.6
-  __TEXT.__text: 0x1c3160
-  __TEXT.__auth_stubs: 0x4380
+7.3.1.0.0
+  __TEXT.__text: 0x1c31c8
+  __TEXT.__auth_stubs: 0x4390
   __TEXT.__objc_methlist: 0x1044c
   __TEXT.__const: 0xc694
   __TEXT.__gcc_except_tab: 0x1c38
   __TEXT.__oslogstring: 0x9df2
-  __TEXT.__cstring: 0xe819
+  __TEXT.__cstring: 0xe849
   __TEXT.__dlopen_cstrs: 0xe35
   __TEXT.__swift5_typeref: 0xee6e
   __TEXT.__constg_swiftt: 0x4b1c

   __TEXT.__unwind_info: 0x7708
   __TEXT.__eh_frame: 0x50f4
   __TEXT.__objc_classname: 0x2482
-  __TEXT.__objc_methname: 0x25921
+  __TEXT.__objc_methname: 0x25949
   __TEXT.__objc_methtype: 0x783c
   __TEXT.__objc_stubs: 0x1a9a0
   __DATA_CONST.__got: 0x1988

   __DATA_CONST.__objc_protorefs: 0xf8
   __DATA_CONST.__objc_superrefs: 0x680
   __DATA_CONST.__objc_arraydata: 0x330
-  __AUTH_CONST.__auth_got: 0x21d0
+  __AUTH_CONST.__auth_got: 0x21d8
   __AUTH_CONST.__const: 0x7740
   __AUTH_CONST.__cfstring: 0xace0
   __AUTH_CONST.__objc_const: 0x1f510

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: BF6BC25C-447A-3C92-90CC-F57C4AC66F04
+  UUID: 6A0A8C12-BE01-3625-8C01-E5731F9D2C1F
   Functions: 12752
-  Symbols:   24277
+  Symbols:   24278
   CStrings:  11294
 
Symbols:
+ +[AMSUIAgeVerificationCore _messageForResult:withBag:expiration:managingProfileName:dateFormatter:bundle:]
+ +[AMSUIAgeVerificationTask _dialogForResult:withBag:expiration:managingProfileName:dateFormatter:]
+ _objc_msgSend$_dialogForResult:withBag:expiration:managingProfileName:dateFormatter:
+ _objc_msgSend$_messageForResult:withBag:expiration:managingProfileName:dateFormatter:bundle:
+ _objc_retain_x6
- +[AMSUIAgeVerificationCore _messageForResult:withBag:expiration:dateFormatter:bundle:]
- +[AMSUIAgeVerificationTask _dialogForResult:withBag:expiration:dateFormatter:]
- _objc_msgSend$_dialogForResult:withBag:expiration:dateFormatter:
- _objc_msgSend$_messageForResult:withBag:expiration:dateFormatter:bundle:
Functions:
~ +[AMSUIAgeVerificationCore _messageForResult:withBag:expiration:dateFormatter:bundle:] -> +[AMSUIAgeVerificationCore _messageForResult:withBag:expiration:managingProfileName:dateFormatter:bundle:] : 344 -> 416
~ ___63-[AMSUIAgeVerificationTask _performTaskWithVerificationResult:]_block_invoke : 528 -> 532
~ +[AMSUIAgeVerificationTask _dialogForResult:withBag:expiration:dateFormatter:] -> +[AMSUIAgeVerificationTask _dialogForResult:withBag:expiration:managingProfileName:dateFormatter:] : 444 -> 472
CStrings:
+ "AGE_VERIFICATION_DIALOG_MESSAGE_MANAGING_PROFILE"
+ "_dialogForResult:withBag:expiration:managingProfileName:dateFormatter:"
+ "_messageForResult:withBag:expiration:managingProfileName:dateFormatter:bundle:"
- "_dialogForResult:withBag:expiration:dateFormatter:"
- "_messageForResult:withBag:expiration:dateFormatter:bundle:"
- "customer"

```
