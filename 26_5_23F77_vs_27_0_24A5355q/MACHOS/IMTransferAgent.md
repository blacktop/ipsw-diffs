## IMTransferAgent

> `/System/Library/PrivateFrameworks/IMTransferServices.framework/IMTransferAgent.app/IMTransferAgent`

```diff

-1450.600.61.2.7
-  __TEXT.__text: 0x2cf8
-  __TEXT.__auth_stubs: 0x500
-  __TEXT.__objc_stubs: 0x240
-  __TEXT.__const: 0x78
-  __TEXT.__gcc_except_tab: 0x3cc
-  __TEXT.__cstring: 0x580
-  __TEXT.__oslogstring: 0x4d0
-  __TEXT.__objc_methname: 0x34e
-  __TEXT.__unwind_info: 0x128
-  __DATA_CONST.__auth_got: 0x290
-  __DATA_CONST.__got: 0x58
-  __DATA_CONST.__const: 0x200
-  __DATA_CONST.__cfstring: 0x40
+1481.100.29.2.9
+  __TEXT.__text: 0x2ef8
+  __TEXT.__auth_stubs: 0x550
+  __TEXT.__objc_stubs: 0x2a0
+  __TEXT.__const: 0x80
+  __TEXT.__gcc_except_tab: 0x328
+  __TEXT.__cstring: 0x5dc
+  __TEXT.__oslogstring: 0x61f
+  __TEXT.__objc_methname: 0x392
+  __TEXT.__unwind_info: 0x140
+  __DATA_CONST.__const: 0x250
+  __DATA_CONST.__cfstring: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_selrefs: 0x90
+  __DATA_CONST.__auth_got: 0x2b8
+  __DATA_CONST.__got: 0x60
+  __DATA.__objc_selrefs: 0xa8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/MessageProtection.framework/MessageProtection
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E4DF7BEA-BA8C-3E9A-A56B-2C5B8C48CBD2
-  Functions: 18
-  Symbols:   97
-  CStrings:  127
+  UUID: 80C98D3D-251B-3898-B32E-901D50E82195
+  Functions: 21
+  Symbols:   103
+  CStrings:  140
 
Symbols:
+ _OBJC_CLASS_$_IMLockdownManager
+ _OBJC_CLASS_$_NSUserDefaults
+ _dispatch_after
+ _dispatch_time
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain
+ _objc_retainBlock
+ _objc_retain_x1
+ _objc_retain_x8
- ___stack_chk_fail
- ___stack_chk_guard
- _objc_retain_x28
CStrings:
+ "After a good %lld second nap, we can now reply with the completed download."
+ "Download is complete, but let's wait %lld seconds for testing purposes"
+ "Forcing reply dict to be nil for testing due to force-put-reply-fallback default"
+ "IMTransferAgent+Test"
+ "attachment-download-delay"
+ "force-put-reply-fallback"
+ "integerForKey:"
+ "isInternalInstall"
+ "messagesDomain"
+ "receiveFileTransfer:topic:path:requestURLString:ownerID:senderExemptFromLDM:signature:fileSize:decryptionKey:sourceAppID:progressBlock:completionBlock:"
+ "senderExemptFromLDM"
+ "xpc_dictionary_create_reply returned NULL for upload completion (transferID: %@), sending fallback message"
- "receiveFileTransfer:topic:path:requestURLString:ownerID:signature:fileSize:decryptionKey:sourceAppID:progressBlock:completionBlock:"

```
