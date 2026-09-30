## AuthenticationServicesCore

> `/System/Library/PrivateFrameworks/AuthenticationServicesCore.framework/AuthenticationServicesCore`

```diff

-621.2.5.10.10
-  __TEXT.__text: 0xaccf0
+621.3.6.10.1
+  __TEXT.__text: 0xaccf4
   __TEXT.__auth_stubs: 0x2230
   __TEXT.__objc_methlist: 0x3280
-  __TEXT.__const: 0xabf8
+  __TEXT.__const: 0xad68
   __TEXT.__cstring: 0x4192
   __TEXT.__oslogstring: 0x3930
   __TEXT.__gcc_except_tab: 0x2b0

   __AUTH.__objc_data: 0x240
   __AUTH.__data: 0x50
   __DATA.__objc_ivar: 0x3e4
-  __DATA.__data: 0x2350
+  __DATA.__data: 0x21e0
   __DATA.__bss: 0xf8d0
   __DATA.__common: 0x190
   __DATA_DIRTY.__objc_data: 0x1ce0
-  __DATA_DIRTY.__data: 0x1250
+  __DATA_DIRTY.__data: 0x1260
   __DATA_DIRTY.__bss: 0xf20
   __DATA_DIRTY.__common: 0x88
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 8AC8FEAC-1D03-39F0-AAF8-5587001F8167
+  UUID: 5F9A65F1-85C6-3515-BF6E-72F2BB302558
   Functions: 4137
   Symbols:   4963
   CStrings:  2555
Symbols:
+ ___block_descriptor_48_e8_32s40bs_e64_v24?0"ASCPlatformPublicKeyCredentialRegistration"8"NSError"16ls32l8s40l8
- ___block_descriptor_40_e8_32bs_e64_v24?0"ASCPlatformPublicKeyCredentialRegistration"8"NSError"16ls32l8
Functions:
~ ___124-[ASCAgent _requestConditionalRegistrationOnProvider:listenerEndpoint:presentationContext:requestContext:completionHandler:]_block_invoke.106 : 784 -> 804
~ -[ASCCredentialRequestContext isUsingWebBrowserOnlyOptions] : 492 -> 476
~ sub_2191c2804 -> sub_219381808 : 204 -> 192
~ sub_2191c2ae4 -> _objectdestroyTm : 192 -> 64
~ _objectdestroyTm -> sub_219381b1c : 64 -> 204

```
