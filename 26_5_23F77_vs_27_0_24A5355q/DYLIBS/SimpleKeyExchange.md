## SimpleKeyExchange

> `/System/Library/PrivateFrameworks/AVConference.framework/Frameworks/SimpleKeyExchange.framework/SimpleKeyExchange`

```diff

-2205.3.1.0.0
-  __TEXT.__text: 0x4c20
-  __TEXT.__auth_stubs: 0x5a0
+2235.48.1.0.0
+  __TEXT.__text: 0x4c38
   __TEXT.__const: 0xdb0
   __TEXT.__gcc_except_tab: 0x3ac
   __TEXT.__cstring: 0x9b
   __TEXT.__unwind_info: 0x260
-  __DATA_CONST.__got: 0x48
+  __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x350
-  __AUTH_CONST.__auth_got: 0x2d8
+  __DATA_CONST.__weak_got: 0x8
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__cfstring: 0x40
+  __AUTH_CONST.__weak_auth_got: 0x28
+  __AUTH_CONST.__auth_got: 0x0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Security.framework/Security
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 0BFFE843-84C0-3013-917B-4787570C617A
+  UUID: E76FF335-BDC4-3428-8841-0D310814F8D8
   Functions: 88
   Symbols:   308
   CStrings:  10
Symbols:
+ __ZNSt12length_errorC1B9nqe220100EPKc
+ __ZNSt3__120__throw_length_errorB9nqe220100EPKc
+ __ZNSt3__16vectorIhNS_9allocatorIhEEE11__vallocateB9nqe220100Em
+ __ZNSt3__16vectorIhNS_9allocatorIhEEE20__throw_length_errorB9nqe220100Ev
+ __ZNSt3__16vectorIhNS_9allocatorIhEEEC2B9nqe220100Em
- __ZNSt12length_errorC1B9nqe210106EPKc
- __ZNSt3__120__throw_length_errorB9nqe210106EPKc
- __ZNSt3__16vectorIhNS_9allocatorIhEEE11__vallocateB9nqe210106Em
- __ZNSt3__16vectorIhNS_9allocatorIhEEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorIhNS_9allocatorIhEEEC2B9nqe210106Em
Functions:
~ ___SKEState_Create_block_invoke : 404 -> 408
~ __ZL22SKEState_CheckPeerCertP14SKEStateOpaque : 380 -> 384
~ __ZL27SKEState_CheckBlobCallbacksP14SKEStateOpaque : 156 -> 160
~ _SKEState_Destroy : 400 -> 404
~ _SKEState_SetBlob : 312 -> 316
~ __Z12skeDataToIntRK9cssm_dataRj : 80 -> 84

```
