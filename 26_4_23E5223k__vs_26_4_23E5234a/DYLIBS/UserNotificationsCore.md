## UserNotificationsCore

> `/System/Library/PrivateFrameworks/UserNotificationsCore.framework/UserNotificationsCore`

```diff

-640.4.40.0.0
-  __TEXT.__text: 0x1ed08c
-  __TEXT.__auth_stubs: 0x3a60
-  __TEXT.__objc_methlist: 0x7adc
+640.4.40.101.0
+  __TEXT.__text: 0x1ed1b4
+  __TEXT.__auth_stubs: 0x3a40
+  __TEXT.__objc_methlist: 0x7ae4
   __TEXT.__cstring: 0xa693
-  __TEXT.__const: 0x10198
+  __TEXT.__const: 0x10188
   __TEXT.__gcc_except_tab: 0x710
-  __TEXT.__oslogstring: 0xe5d7
+  __TEXT.__oslogstring: 0xe627
   __TEXT.__dlopen_cstrs: 0xf4
   __TEXT.__constg_swiftt: 0x67b0
   __TEXT.__swift5_typeref: 0x5fac

   __TEXT.__swift_as_ret: 0x1e0
   __TEXT.__swift5_mpenum: 0x40
   __TEXT.__unwind_info: 0x5e20
-  __TEXT.__eh_frame: 0x7358
+  __TEXT.__eh_frame: 0x7328
   __TEXT.__objc_classname: 0x36a6
-  __TEXT.__objc_methname: 0x18f25
+  __TEXT.__objc_methname: 0x18f55
   __TEXT.__objc_methtype: 0x39bf
-  __TEXT.__objc_stubs: 0xf860
+  __TEXT.__objc_stubs: 0xf8a0
   __DATA_CONST.__got: 0x1560
   __DATA_CONST.__const: 0x1598
   __DATA_CONST.__objc_classlist: 0x6a0
   __DATA_CONST.__objc_catlist: 0x80
   __DATA_CONST.__objc_protolist: 0x2e0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x48c8
+  __DATA_CONST.__objc_selrefs: 0x48d8
   __DATA_CONST.__objc_protorefs: 0x170
   __DATA_CONST.__objc_superrefs: 0x200
-  __AUTH_CONST.__auth_got: 0x1d40
+  __AUTH_CONST.__auth_got: 0x1d30
   __AUTH_CONST.__const: 0xb0a0
   __AUTH_CONST.__cfstring: 0x64e0
   __AUTH_CONST.__objc_const: 0x24448

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: A2FC2AEE-742C-33C9-B2A9-3551F936D59A
-  Functions: 9002
-  Symbols:   13199
-  CStrings:  7287
+  UUID: AF132996-B846-3B93-A304-BCB098CE4001
+  Functions: 9000
+  Symbols:   13203
+  CStrings:  7290
 
Symbols:
+ -[UNCRemoteNotificationServer _queue_tokenForBundleIdentifier:]
+ _objc_msgSend$_queue_tokenForBundleIdentifier:
+ _objc_msgSend$perAppToken
CStrings:
+ "Received remote notification on topic %{public}@ for unknown token, dropping."
+ "_queue_tokenForBundleIdentifier:"
+ "perAppToken"

```
