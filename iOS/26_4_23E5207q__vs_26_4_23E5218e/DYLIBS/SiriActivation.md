## SiriActivation

> `/System/Library/PrivateFrameworks/SiriActivation.framework/SiriActivation`

```diff

-3520.88.6.1.4
-  __TEXT.__text: 0x56b2c
+3520.90.2.1.1
+  __TEXT.__text: 0x56cc4
   __TEXT.__auth_stubs: 0xbb0
-  __TEXT.__objc_methlist: 0x63fc
+  __TEXT.__objc_methlist: 0x6414
   __TEXT.__const: 0x638
-  __TEXT.__cstring: 0xaa80
-  __TEXT.__oslogstring: 0x7d28
+  __TEXT.__cstring: 0xaaac
+  __TEXT.__oslogstring: 0x7db0
   __TEXT.__gcc_except_tab: 0xeac
   __TEXT.__dlopen_cstrs: 0x1bc
   __TEXT.__swift5_typeref: 0x102

   __TEXT.__swift5_proto: 0x18
   __TEXT.__swift_as_entry: 0x18
   __TEXT.__swift_as_ret: 0xc
-  __TEXT.__unwind_info: 0x1a18
+  __TEXT.__unwind_info: 0x1a28
   __TEXT.__eh_frame: 0x138
   __TEXT.__objc_classname: 0x115b
-  __TEXT.__objc_methname: 0xeb7d
-  __TEXT.__objc_methtype: 0x2531
-  __TEXT.__objc_stubs: 0x9c60
+  __TEXT.__objc_methname: 0xec5d
+  __TEXT.__objc_methtype: 0x2561
+  __TEXT.__objc_stubs: 0x9c80
   __DATA_CONST.__got: 0x708
   __DATA_CONST.__const: 0x1760
   __DATA_CONST.__objc_classlist: 0x350
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x158
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3050
+  __DATA_CONST.__objc_selrefs: 0x3060
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x2a8
   __DATA_CONST.__objc_arraydata: 0x500
   __AUTH_CONST.__auth_got: 0x5e8
   __AUTH_CONST.__const: 0x628
-  __AUTH_CONST.__cfstring: 0x4b60
+  __AUTH_CONST.__cfstring: 0x4b80
   __AUTH_CONST.__objc_const: 0xa2c0
   __AUTH_CONST.__objc_intobj: 0x900
   __AUTH_CONST.__objc_dictobj: 0x118

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 08E394BD-1891-3942-82DC-D3E4289E7E79
-  Functions: 2280
-  Symbols:   7798
-  CStrings:  4774
+  UUID: 3EF27B04-2A42-3899-BF11-F27B780A4921
+  Functions: 2282
+  Symbols:   7803
+  CStrings:  4781
 
Symbols:
+ +[SiriDirectActionContext messageComposeNewThreadDirectActionWithAppBundleId:fullName:phoneOrEmailAddress:contactId:]
+ -[SiriDirectActionContext _initWithDirectActionEvent:appBundleId:conversationGUID:fullName:phoneOrEmailAddress:contactId:isQuickTypeVisualIntelligence:]
+ _objc_msgSend$_initWithDirectActionEvent:appBundleId:conversationGUID:fullName:phoneOrEmailAddress:contactId:isQuickTypeVisualIntelligence:
+ _objc_msgSend$messageComposeNewThreadDirectActionWithAppBundleId:fullName:phoneOrEmailAddress:contactId:
- _objc_msgSend$_initWithDirectActionEvent:appBundleId:conversationGUID:fullName:phoneOrEmailAddress:isQuickTypeVisualIntelligence:
Functions:
~ -[SiriDirectActionContext _initWithDirectActionEvent:appBundleId:conversationGUID:fullName:phoneOrEmailAddress:] : 8 -> 40
~ -[SiriActivationService _overrideLockButtonStateIfNeededForRequestOptions:] : 312 -> 432
+ +[SiriDirectActionContext messageComposeNewThreadDirectActionWithAppBundleId:fullName:phoneOrEmailAddress:contactId:]
~ -[SiriDirectActionContext _initWithDirectActionEvent:appBundleId:conversationGUID:fullName:phoneOrEmailAddress:isQuickTypeVisualIntelligence:] : 468 -> 40
+ -[SiriDirectActionContext _initWithDirectActionEvent:appBundleId:conversationGUID:fullName:phoneOrEmailAddress:contactId:isQuickTypeVisualIntelligence:]
CStrings:
+ "%s #PreprocessNotification We are currently preprocessing a notification. Allowing the lock button press to fall through to SpringBoard"
+ "@48@0:8@16@24@32@40"
+ "@68@0:8q16@24@32@40@48@56B64"
+ "AssistantDirectActionEventMessagesContactId"
+ "_initWithDirectActionEvent:appBundleId:conversationGUID:fullName:phoneOrEmailAddress:contactId:isQuickTypeVisualIntelligence:"
+ "messageComposeNewThreadDirectActionWithAppBundleId:fullName:phoneOrEmailAddress:contactId:"

```
