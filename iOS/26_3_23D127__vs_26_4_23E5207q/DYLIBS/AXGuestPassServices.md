## AXGuestPassServices

> `/System/Library/PrivateFrameworks/AXGuestPassServices.framework/AXGuestPassServices`

```diff

-3191.7.24.0.0
-  __TEXT.__text: 0x10648
-  __TEXT.__auth_stubs: 0xc20
+3191.19.0.0.0
+  __TEXT.__text: 0x10724
+  __TEXT.__auth_stubs: 0xc40
   __TEXT.__objc_methlist: 0x384
   __TEXT.__const: 0x518
-  __TEXT.__cstring: 0x62f
+  __TEXT.__cstring: 0x29e
   __TEXT.__swift5_typeref: 0x28d
   __TEXT.__swift5_capture: 0x378
   __TEXT.__oslogstring: 0xa2b

   __TEXT.__swift_as_entry: 0x54
   __TEXT.__swift_as_ret: 0x54
   __TEXT.__unwind_info: 0x510
-  __TEXT.__eh_frame: 0x878
-  __TEXT.__objc_classname: 0x47
-  __TEXT.__objc_methname: 0x88a
-  __TEXT.__objc_methtype: 0x285
-  __TEXT.__objc_stubs: 0x20
+  __TEXT.__eh_frame: 0x848
+  __TEXT.__objc_classname: 0x181
+  __TEXT.__objc_methname: 0xb21
+  __TEXT.__objc_methtype: 0x3aa
+  __TEXT.__objc_stubs: 0x4a0
   __DATA_CONST.__got: 0x1b0
   __DATA_CONST.__const: 0xd0
   __DATA_CONST.__objc_classlist: 0x28

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x288
   __DATA_CONST.__objc_protorefs: 0x20
-  __AUTH_CONST.__auth_got: 0x618
+  __AUTH_CONST.__auth_got: 0x628
   __AUTH_CONST.__const: 0x9b8
   __AUTH_CONST.__objc_const: 0x588
   __AUTH.__objc_data: 0x420
   __AUTH.__data: 0xa0
-  __DATA.__data: 0x340
+  __DATA.__data: 0x310
   __DATA.__bss: 0x100
   __DATA_DIRTY.__objc_data: 0x98
-  __DATA_DIRTY.__data: 0x80
+  __DATA_DIRTY.__data: 0xb0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Network.framework/Network

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 56CAF328-D368-330E-83F8-E58E32A1AA76
-  Functions: 378
-  Symbols:   404
-  CStrings:  217
+  UUID: 0AADCBDE-FF7F-3619-957A-931C93367115
+  Functions: 379
+  Symbols:   443
+  CStrings:  212
 
Symbols:
+ _block_copy_helper.143
+ _block_copy_helper.149
+ _block_copy_helper.155
+ _block_copy_helper.161
+ _block_copy_helper.167
+ _block_copy_helper.170
+ _block_copy_helper.44
+ _block_copy_helper.51
+ _block_descriptor.145
+ _block_descriptor.151
+ _block_descriptor.157
+ _block_descriptor.163
+ _block_descriptor.169
+ _block_descriptor.172
+ _block_descriptor.46
+ _block_descriptor.53
+ _block_destroy_helper.144
+ _block_destroy_helper.150
+ _block_destroy_helper.156
+ _block_destroy_helper.162
+ _block_destroy_helper.168
+ _block_destroy_helper.171
+ _block_destroy_helper.45
+ _block_destroy_helper.52
+ _objc_msgSend$annul
+ _objc_msgSend$boolForSetting:
+ _objc_msgSend$canSendResponse
+ _objc_msgSend$deviceClassForBuddy
+ _objc_msgSend$filterManagedAssetsRepresentationForGuestPassTransfer:
+ _objc_msgSend$guestPassSessionIsActive
+ _objc_msgSend$info
+ _objc_msgSend$init
+ _objc_msgSend$initWithIdentifier:serviceBundleName:
+ _objc_msgSend$initWithInfo:responder:
+ _objc_msgSend$initWithInfo:timeout:forResponseOnQueue:withHandler:
+ _objc_msgSend$installGuestPassAcceptDialogGesture
+ _objc_msgSend$installGuestPassPINGesture
+ _objc_msgSend$invalidate
+ _objc_msgSend$isValid
+ _objc_msgSend$lock
+ _objc_msgSend$managedAssetsRepresentation
+ _objc_msgSend$openApplication:withOptions:completion:
+ _objc_msgSend$optionsWithDictionary:
+ _objc_msgSend$processIdentifier
+ _objc_msgSend$processInfo
+ _objc_msgSend$productVersionForBuddy
+ _objc_msgSend$registerUpdateBlock:forRetrieveSelector:withListener:
+ _objc_msgSend$removeGuestPassAcceptDialogGesture
+ _objc_msgSend$responderWithHandler:
+ _objc_msgSend$responseWithInfo:
+ _objc_msgSend$scheduledTimerWithTimeInterval:target:selector:userInfo:repeats:
+ _objc_msgSend$sendAsynchronousMessage:withIdentifier:targetAccessQueue:completion:
+ _objc_msgSend$sendResponse:
+ _objc_msgSend$sendSynchronousMessage:withIdentifier:error:
+ _objc_msgSend$server
+ _objc_msgSend$serviceWithDefaultShellEndpoint
+ _objc_msgSend$setDelegate:
+ _objc_msgSend$setFlag:forSetting:
+ _objc_msgSend$setNullificationHandler:
+ _objc_msgSend$unlock
+ _objc_release_x27
+ _objc_retain_x1
+ _objc_retain_x28
+ _objectdestroy.141Tm
+ _objectdestroy.55Tm
+ _objectdestroy.59Tm
+ _swift_bridgeObjectRetain_n
- _block_copy_helper.141
- _block_copy_helper.147
- _block_copy_helper.153
- _block_copy_helper.159
- _block_copy_helper.165
- _block_copy_helper.168
- _block_copy_helper.42
- _block_copy_helper.49
- _block_descriptor.143
- _block_descriptor.149
- _block_descriptor.155
- _block_descriptor.161
- _block_descriptor.167
- _block_descriptor.170
- _block_descriptor.44
- _block_descriptor.51
- _block_destroy_helper.142
- _block_destroy_helper.148
- _block_destroy_helper.154
- _block_destroy_helper.160
- _block_destroy_helper.166
- _block_destroy_helper.169
- _block_destroy_helper.43
- _block_destroy_helper.50
- _objc_retain_x26
- _objectdestroy.139Tm
- _objectdestroy.53Tm
- _objectdestroy.57Tm
CStrings:
+ "AXGuestPassService"
+ "AXGuestPassServices"

```
