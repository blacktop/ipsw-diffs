## ExchangeGraphAPI

> `/System/Library/PrivateFrameworks/ExchangeGraphAPI.framework/Versions/A/ExchangeGraphAPI`

```diff

 2060.20.1.0.0
-  __TEXT.__text: 0xd984
+  __TEXT.__text: 0xd970
   __TEXT.__auth_stubs: 0x2b0
-  __TEXT.__objc_methlist: 0x1bcc
+  __TEXT.__objc_methlist: 0x1e0c
   __TEXT.__const: 0x80
   __TEXT.__cstring: 0x7fd
   __TEXT.__gcc_except_tab: 0x398

   __DATA_CONST.__objc_classlist: 0x1d0
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9a0
+  __DATA_CONST.__objc_selrefs: 0xab8
   __DATA_CONST.__objc_superrefs: 0x28
   __AUTH_CONST.__auth_got: 0x168
   __AUTH_CONST.__const: 0x160
   __AUTH_CONST.__cfstring: 0x1220
-  __AUTH_CONST.__objc_const: 0x53c0
+  __AUTH_CONST.__objc_const: 0x4fb0
   __AUTH.__objc_data: 0x1220
   __DATA.__objc_ivar: 0x2a8
   __DATA.__data: 0x1e8

   - /System/Library/Frameworks/Security.framework/Versions/A/Security
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C8778282-571A-319E-BE08-FA05FE791211
-  Functions: 567
-  Symbols:   1576
+  UUID: 463C8342-FD72-3EE5-950F-BFA21C19E61F
+  Functions: 572
+  Symbols:   1581
   CStrings:  943
 
Symbols:
+ +[GraphAPIBinding log].cold.1
+ +[GraphDateUtils valueFromString:].cold.1
+ -[GraphAPIBinding cachedAccountStore].cold.1
+ GraphAPILogURLAuthenticationChallenge.cold.1
+ exchangeLog.cold.1
Functions:
~ +[GraphDateUtils valueFromString:] : 424 -> 408
~ _exchangeLog : 84 -> 68
~ _GraphAPILogURLResponse : 780 -> 768
~ _GraphAPILogURLAuthenticationChallenge : 720 -> 704
~ +[GraphAPIBinding log] : 84 -> 68
~ -[GraphAPIBinding cachedAccountStore] : 84 -> 68
~ -[GraphAPIBinding finishMessagesAndInvalidate] : 144 -> 148
~ -[GraphAPIBinding invalidateAndCancel] : 144 -> 148
~ -[GraphAPIBinding _errorFromTask:] : 408 -> 372
~ -[GraphAPIBinding _shouldFallbackFromError:] : 148 -> 144
~ -[GraphAPIBinding _sendRequestForBindingTask:] : 176 -> 180

```
