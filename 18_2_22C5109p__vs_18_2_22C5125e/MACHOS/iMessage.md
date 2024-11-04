## iMessage

> `/System/Library/Messages/PlugIns/iMessage.imservice/iMessage`

```diff

-1402.300.129.2.15
-  __TEXT.__text: 0x92090
-  __TEXT.__auth_stubs: 0x1380
-  __TEXT.__objc_stubs: 0xb1e0
-  __TEXT.__objc_methlist: 0x216c
+1402.300.158.2.2
+  __TEXT.__text: 0x920b4
+  __TEXT.__auth_stubs: 0x1390
+  __TEXT.__objc_stubs: 0xb1c0
+  __TEXT.__objc_methlist: 0x2164
   __TEXT.__const: 0x37e
-  __TEXT.__gcc_except_tab: 0xa6e0
-  __TEXT.__cstring: 0x2fdd
-  __TEXT.__oslogstring: 0x13f46
+  __TEXT.__gcc_except_tab: 0xa6a4
+  __TEXT.__cstring: 0x2fed
+  __TEXT.__oslogstring: 0x13ed6
   __TEXT.__objc_classname: 0x4e2
-  __TEXT.__objc_methname: 0x1035c
-  __TEXT.__objc_methtype: 0x27b1
+  __TEXT.__objc_methname: 0x1035f
+  __TEXT.__objc_methtype: 0x2779
   __TEXT.__ustring: 0x4
-  __TEXT.__constg_swiftt: 0x158
+  __TEXT.__constg_swiftt: 0x168
   __TEXT.__swift5_typeref: 0x261
   __TEXT.__swift5_reflstr: 0x1f
   __TEXT.__swift5_fieldmd: 0x48

   __TEXT.__swift5_types: 0x8
   __TEXT.__swift5_capture: 0xa0
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x1da8
+  __TEXT.__unwind_info: 0x1da0
   __TEXT.__eh_frame: 0x2b8
-  __DATA_CONST.__auth_got: 0x9d0
+  __DATA_CONST.__auth_got: 0x9d8
   __DATA_CONST.__got: 0xda8
   __DATA_CONST.__auth_ptr: 0x18
-  __DATA_CONST.__const: 0x2ae0
+  __DATA_CONST.__const: 0x2b10
   __DATA_CONST.__cfstring: 0x3220
   __DATA_CONST.__objc_classlist: 0xd0
   __DATA_CONST.__objc_catlist: 0x38

   __DATA_CONST.__objc_arraydata: 0x30
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_arrayobj: 0x48
-  __DATA.__objc_const: 0x3560
+  __DATA.__objc_const: 0x3570
   __DATA.__objc_selrefs: 0x31d8
   __DATA.__objc_ivar: 0x1b0
-  __DATA.__objc_data: 0x378
+  __DATA.__objc_data: 0x380
   __DATA.__data: 0x790
   __DATA.__bss: 0x60
   __DATA_DIRTY.__objc_data: 0x500
-  __DATA_DIRTY.__data: 0xc
+  __DATA_DIRTY.__data: 0x8
   __DATA_DIRTY.__bss: 0x58
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftAppleArchive.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 1174
-  Symbols:   778
-  CStrings:  4165
+  Functions: 1176
+  Symbols:   780
+  CStrings:  4163
 
Symbols:
+ _IMInternationalForPhoneNumberWithOptions
+ __swift_FORCE_LOAD_$_swiftAppleArchive
CStrings:
+ "B16@?0@\"IDSDevice\"8"
+ "We did not have ids accounts to send scheduled messages out -- bailing {haveTokenURISToSendTo %!@(MISSING) hasPeerDevicesSupportingSendLater %!@(MISSING) idsAccount %!@(MISSING) devices %!@(MISSING)}"
+ "_combinedTransferUserInfoForAttachmentSendContexts:transfer:message:commonCapabilities:"
+ "attachToTransfer:message:commonCapabilities:"
+ "copyIsoCountryCodeForSubscriptionContext:"
+ "phoneNumbersOfActiveSubscriptions"
+ "receiveFileTransfer:transferGUID:topic:path:requestURLString:ownerID:signature:decryptionKey:fileSize:balloonBundleID:senderContext:progressBlock:completionBlock:"
- "Error moving safe transfer (%!@(MISSING)) to original transfer path (%!@(MISSING)) with error: %!@(MISSING)"
- "Error removing original transfer (%!@(MISSING)) error: %!@(MISSING)"
- "We did not have ids accounts to send scheduled messages out -- bailing {haveIDSDevicesToSendTo %!@(MISSING) haveTokenURISToSendTo %!@(MISSING) idsAccount %!@(MISSING) devices %!@(MISSING)}"
- "_combinedTransferUserInfoForAttachmentSendContexts:transfer:commonCapabilities:"
- "attachToTransfer:messageGUID:commonCapabilities:"
- "hasCTSubscriptionWithPhoneNumber:"
- "moveItemAtURL:toURL:error:"
- "receiveFileTransfer:transferGUID:topic:path:requestURLString:ownerID:signature:decryptionKey:fileSize:generatePreview:balloonBundleID:senderContext:progressBlock:completionBlock:"
- "v72@0:8@16{IMPreviewConstraints=d{CGSize=dd}dBBB}24@?64"

```
