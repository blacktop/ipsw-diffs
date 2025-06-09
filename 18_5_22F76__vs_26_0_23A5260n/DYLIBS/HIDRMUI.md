## HIDRMUI

> `/System/Library/PrivateFrameworks/HIDRMUI.framework/HIDRMUI`

```diff

-64.0.0.0.0
-  __TEXT.__text: 0x6584
-  __TEXT.__auth_stubs: 0x430
+68.0.0.0.0
+  __TEXT.__text: 0x6c6c
+  __TEXT.__auth_stubs: 0x480
   __TEXT.__objc_methlist: 0x80c
   __TEXT.__const: 0x90
-  __TEXT.__gcc_except_tab: 0x3e8
-  __TEXT.__cstring: 0x579
+  __TEXT.__gcc_except_tab: 0x494
+  __TEXT.__cstring: 0x58e
   __TEXT.__ustring: 0x110
-  __TEXT.__oslogstring: 0x70c
-  __TEXT.__unwind_info: 0x258
+  __TEXT.__oslogstring: 0x75e
+  __TEXT.__unwind_info: 0x278
   __TEXT.__objc_classname: 0xcf
   __TEXT.__objc_methname: 0x1685
   __TEXT.__objc_methtype: 0x22f
   __TEXT.__objc_stubs: 0x1340
   __DATA_CONST.__got: 0x170
-  __DATA_CONST.__const: 0x220
+  __DATA_CONST.__const: 0x270
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x608
   __DATA_CONST.__objc_superrefs: 0x38
-  __AUTH_CONST.__auth_got: 0x228
+  __AUTH_CONST.__auth_got: 0x250
   __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__cfstring: 0x440
   __AUTH_CONST.__objc_const: 0xda8

   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A12D7E81-4C35-39B1-A9C7-8CAACFB98E41
-  Functions: 214
-  Symbols:   866
-  CStrings:  447
+  UUID: D698FF52-459E-3F32-B58F-47148661F688
+  Functions: 217
+  Symbols:   881
+  CStrings:  449
 
Symbols:
+ -[HIDRMUIUserAuthorizationManager addUserAuthorizationRequest:completion:].cold.1
+ GCC_except_table13
+ GCC_except_table47
+ ___71+[AuthRequestWrapper requestWrapperWithCompletion:andUserNotification:]_block_invoke
+ ___74-[HIDRMUIUserAuthorizationManager addUserAuthorizationRequest:completion:]_block_invoke.67
+ ___block_descriptor_48_e8_32bs40w_e20_v24?0q8"NSError"16lw40l8s32l8
+ ___block_descriptor_64_e8_32s40s48bs56r_e40_v24?0"IOUserNotification"8"NSError"16ls32l8s40l8r56l8s48l8
+ ___block_descriptor_80_e8_32s40s48r56r64w_e40_v24?0"IOUserNotification"8"NSError"16lw64l8s32l8r48l8s40l8r56l8
+ _objc_copyWeak
+ _objc_destroyWeak
+ _objc_initWeak
+ _objc_loadWeakRetained
+ _objc_msgSend$completionHandler
+ _objc_retain_x25
- GCC_except_table14
- GCC_except_table44
- ___block_descriptor_80_e8_32s40s48bs56r64r_e40_v24?0"IOUserNotification"8"NSError"16ls32l8r56l8s40l8r64l8s48l8
- _objc_msgSend$authRequests
CStrings:
+ "Invalid authorization request! (authorizationRequest.class: %@)"
+ "Not in pairing flow, ignoring input character! (character: '%C')"
+ "v24@?0q8@\"NSError\"16"
- "Not in pairing flow, ignoring input character!"

```
