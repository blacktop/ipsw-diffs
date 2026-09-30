## CardServices

> `/System/Library/PrivateFrameworks/CardServices.framework/CardServices`

```diff

-3500.5.1.0.0
-  __TEXT.__text: 0x20b8
-  __TEXT.__auth_stubs: 0x370
+3520.8.1.0.0
+  __TEXT.__text: 0x2204
+  __TEXT.__auth_stubs: 0x350
   __TEXT.__objc_methlist: 0x514
   __TEXT.__const: 0x60
   __TEXT.__cstring: 0x183
   __TEXT.__oslogstring: 0x1f2
   __TEXT.__gcc_except_tab: 0x88
-  __TEXT.__unwind_info: 0x118
+  __TEXT.__unwind_info: 0x140
   __TEXT.__objc_classname: 0x15b
   __TEXT.__objc_methname: 0x810
   __TEXT.__objc_methtype: 0x2e7

   __DATA_CONST.__objc_selrefs: 0x2c8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x1c8
+  __AUTH_CONST.__auth_got: 0x1b8
   __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__cfstring: 0xa0
   __AUTH_CONST.__objc_const: 0x1680

   - /System/Library/PrivateFrameworks/Cards.framework/Cards
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E2AB91EC-98B5-3F89-B622-C6BDB0CB5829
+  UUID: F2021BD8-CCD3-3933-82AE-CAF2C27B6597
   Functions: 65
-  Symbols:   427
+  Symbols:   425
   CStrings:  212
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x26
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x2
- _objc_retain_x3
Functions:
~ +[_CRSServiceBundleManager sharedInstance] : 160 -> 176
~ ___60-[_CRSServiceBundleManager getServiceBundlesWithCompletion:]_block_invoke : 208 -> 212
~ -[_CRSPassthroughService requestCard:reply:] : 132 -> 148
~ -[_CRSPassthroughService canSatisfyCardRequest:] : 68 -> 72
~ +[CRSIdentifiedServiceRegistry sharedInstance] : 160 -> 176
~ -[_CRSServiceBundle underlyingService] : 112 -> 120
~ -[_CRSServiceBundle serviceIdentifier] : 192 -> 208
~ -[CRSCardResponse setRequest:] : 20 -> 80
~ -[CRSCardResponse setCard:] : 20 -> 80
~ -[CRSCardRequest initWithContent:format:] : 220 -> 224
~ -[CRSCardRequest startWithReply:] : 440 -> 428
~ ___33-[CRSCardRequest startWithReply:]_block_invoke_2 : 844 -> 864
~ ___33-[CRSCardRequest startWithReply:]_block_invoke.52 : 164 -> 172
~ -[CRSCardRequest _loadAndRegisterBundleServices:] : 160 -> 168
~ ___49-[CRSCardRequest _loadAndRegisterBundleServices:]_block_invoke : 292 -> 296
~ -[CRSCardRequest _tryRemainingCardServices:reply:] : 252 -> 248
~ ___50-[CRSCardRequest _tryRemainingCardServices:reply:]_block_invoke : 604 -> 608
~ ___50-[CRSCardRequest _tryRemainingCardServices:reply:]_block_invoke.65 : 300 -> 304
~ ___50-[CRSCardRequest _tryRemainingCardServices:reply:]_block_invoke_2 : 372 -> 380
~ ___50-[CRSCardRequest _tryRemainingCardServices:reply:]_block_invoke.67 : 604 -> 612
~ -[CRSCardRequest setContent:] : 20 -> 80
~ +[CRSCardRequest(Conveniences) registerService:] : 100 -> 104
~ -[_CRSCardServiceBundle underlyingService] : 112 -> 120
~ -[_CRSCardServiceBundle canSatisfyCardRequest:] : 116 -> 120
~ -[_CRSCardServiceBundle servicePriorityForRequest:] : 116 -> 120

```
