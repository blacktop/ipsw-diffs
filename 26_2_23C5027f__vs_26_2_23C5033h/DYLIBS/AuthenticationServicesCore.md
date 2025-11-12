## AuthenticationServicesCore

> `/System/Library/PrivateFrameworks/AuthenticationServicesCore.framework/AuthenticationServicesCore`

```diff

-623.1.12.10.4
-  __TEXT.__text: 0xc6fc0
+623.1.13.10.3
+  __TEXT.__text: 0xc7120
   __TEXT.__auth_stubs: 0x2600
-  __TEXT.__objc_methlist: 0x396c
+  __TEXT.__objc_methlist: 0x39b4
   __TEXT.__const: 0xca78
   __TEXT.__cstring: 0x5992
-  __TEXT.__oslogstring: 0x3fc0
+  __TEXT.__oslogstring: 0x4010
   __TEXT.__gcc_except_tab: 0x30c
   __TEXT.__ustring: 0x564
   __TEXT.__dlopen_cstrs: 0x48

   __TEXT.__swift_as_ret: 0x68
   __TEXT.__swift5_protos: 0x20
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x3460
+  __TEXT.__unwind_info: 0x3468
   __TEXT.__eh_frame: 0x44f8
   __TEXT.__objc_classname: 0x7aa
-  __TEXT.__objc_methname: 0xb31a
-  __TEXT.__objc_methtype: 0x2a60
-  __TEXT.__objc_stubs: 0x46c0
+  __TEXT.__objc_methname: 0xb35d
+  __TEXT.__objc_methtype: 0x2a7c
+  __TEXT.__objc_stubs: 0x46e0
   __DATA_CONST.__got: 0x8d8
   __DATA_CONST.__const: 0xc80
   __DATA_CONST.__objc_classlist: 0x1f8
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x180
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1db8
+  __DATA_CONST.__objc_selrefs: 0x1dc8
   __DATA_CONST.__objc_protorefs: 0xc0
   __DATA_CONST.__objc_superrefs: 0xf0
   __DATA_CONST.__objc_arraydata: 0x10
   __AUTH_CONST.__auth_got: 0x1310
   __AUTH_CONST.__const: 0x6388
   __AUTH_CONST.__cfstring: 0x2040
-  __AUTH_CONST.__objc_const: 0x7bb8
+  __AUTH_CONST.__objc_const: 0x7bf8
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0xd08

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 3FC4CC4B-6C6B-34D0-B669-9C2AEAF95291
-  Functions: 4906
-  Symbols:   5387
-  CStrings:  2875
+  UUID: A9A8A51A-1BA8-39A9-B350-192DA8104925
+  Functions: 4911
+  Symbols:   5398
+  CStrings:  2879
 
Symbols:
+ -[ASAgentAutoFillListener getPasskeysForRunningAssertionWithApplicationIdentifier:webPageURL:withCompletionHandler:]
+ -[ASCAgent isAutoFillOperation]
+ -[ASCAgent urlMatchesRequestOrigin:]
+ -[ASCAgent urlMatchesRequestOrigin:].cold.1
+ -[ASPublicKeyCredentialOperationTestDelegate isAutoFillOperation]
+ -[ASPublicKeyCredentialOperationTestDelegate urlMatchesRequestOrigin:]
+ ___block_literal_global.700
+ _objc_msgSend$autoFillPasskeysForOperationUUID:webPageURL:
+ _objc_msgSend$initWithString:
- -[ASAgentAutoFillListener getPasskeysForRunningAssertionWithApplicationIdentifier:withCompletionHandler:]
- ___block_literal_global.696
- _objc_msgSend$autoFillPasskeysForOperationUUID:
CStrings:
+ "B24@0:8@\"NSURL\"16"
+ "Received a webpage URL but the active passkey request has no origin specified"
+ "autoFillPasskeysForOperationUUID:webPageURL:"
+ "getPasskeysForRunningAssertionWithApplicationIdentifier:webPageURL:withCompletionHandler:"
+ "isAutoFillOperation"
+ "urlMatchesRequestOrigin:"
+ "v40@0:8@\"NSString\"16@\"NSURL\"24@?<v@?@\"NSArray\"@\"WBSPasskeyAutoFillFromNearbyDeviceOptions\">32"
- "autoFillPasskeysForOperationUUID:"
- "getPasskeysForRunningAssertionWithApplicationIdentifier:withCompletionHandler:"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSArray\"@\"WBSPasskeyAutoFillFromNearbyDeviceOptions\">24"

```
