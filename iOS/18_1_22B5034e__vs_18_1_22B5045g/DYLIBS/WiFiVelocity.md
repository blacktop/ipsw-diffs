## WiFiVelocity

> `/System/Library/PrivateFrameworks/WiFiVelocity.framework/WiFiVelocity`

```diff

-1005.90.0.0.0
-  __TEXT.__text: 0x2de50
+1005.95.0.0.0
+  __TEXT.__text: 0x2cc64
   __TEXT.__auth_stubs: 0x710
-  __TEXT.__objc_methlist: 0x2974
+  __TEXT.__objc_methlist: 0x28fc
   __TEXT.__const: 0xc8
   __TEXT.__gcc_except_tab: 0x290
-  __TEXT.__cstring: 0x743d
-  __TEXT.__oslogstring: 0x168d
+  __TEXT.__cstring: 0x7247
+  __TEXT.__oslogstring: 0x122e
   __TEXT.__ustring: 0x656
-  __TEXT.__unwind_info: 0xaf8
-  __TEXT.__objc_classname: 0x276
-  __TEXT.__objc_methname: 0x5f14
-  __TEXT.__objc_methtype: 0xded
-  __TEXT.__objc_stubs: 0x4de0
-  __DATA_CONST.__got: 0x298
-  __DATA_CONST.__const: 0x17d0
-  __DATA_CONST.__objc_classlist: 0xf0
+  __TEXT.__unwind_info: 0xac8
+  __TEXT.__objc_classname: 0x25e
+  __TEXT.__objc_methname: 0x5cc4
+  __TEXT.__objc_methtype: 0xdbd
+  __TEXT.__objc_stubs: 0x4b40
+  __DATA_CONST.__got: 0x280
+  __DATA_CONST.__const: 0x1768
+  __DATA_CONST.__objc_classlist: 0xe8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1740
+  __DATA_CONST.__objc_selrefs: 0x1670
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0xe8
+  __DATA_CONST.__objc_superrefs: 0xe0
   __DATA_CONST.__objc_arraydata: 0x58
   __AUTH_CONST.__auth_got: 0x398
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__const: 0x1c0
-  __AUTH_CONST.__cfstring: 0xa140
-  __AUTH_CONST.__objc_const: 0x4b88
+  __AUTH_CONST.__const: 0x120
+  __AUTH_CONST.__cfstring: 0xa120
+  __AUTH_CONST.__objc_const: 0x4a58
   __AUTH_CONST.__objc_intobj: 0x138
   __AUTH_CONST.__objc_arrayobj: 0x78
-  __AUTH.__objc_data: 0x1e0
-  __DATA.__objc_ivar: 0x3d4
+  __AUTH.__objc_data: 0x190
+  __DATA.__objc_ivar: 0x3c4
   __DATA.__data: 0x1e0
   __DATA.__bss: 0x8
   __DATA_DIRTY.__objc_data: 0x780

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1177
-  Symbols:   1399
-  CStrings:  2759
+  Functions: 1162
+  Symbols:   1381
+  CStrings:  2699
 
Symbols:
- _NSFilePosixPermissions
- _OBJC_CLASS_$_RPFileTransferSession
- _OBJC_CLASS_$_RPFileTransferItem
CStrings:
- "itemURL"
- "addItem:"
- "_publicKeySelf"
- "[wifivelocity] %!s(MISSING) (%!s(MISSING):%!u(MISSING)) Set file permissions to %!h(MISSING)d on: %!{(MISSING)public}@"
- "[wifivelocity] %!s(MISSING) (%!s(MISSING):%!u(MISSING)) File Receiver, Session Keys: self: %!{(MISSING)public}@, peer: %!{(MISSING)public}@"
- "[wifivelocity] File Receiver, Transfer Progress: %!{(MISSING)public}@"
- "-[W5FileTransferManager startW5FileReceiverWithPeerPublicKey:reply:]_block_invoke"
- "[wifivelocity] %!s(MISSING) (%!s(MISSING):%!u(MISSING)) Unable to set file permissions, error: %!{(MISSING)public}@ for: %!{(MISSING)public}@"
- "prepareTemplateAndReturnError:"
- "W5FileTransferManager.m"
- "[wifivelocity] File Receiver, Received Item: %!{(MISSING)public}@"
- "[wifivelocity] %!s(MISSING) (%!s(MISSING):%!u(MISSING)) File Sender, Adding item: %!{(MISSING)public}@"
- "setAttributes:ofItemAtPath:error:"
- "_stop"
- "setReceivedItemHandler:"
- "[wifivelocity] File Sender, Item Completion, error: %!{(MISSING)public}@"
- "[wifivelocity] File Sender, Transfer Progress: %!{(MISSING)public}@"
- "[wifivelocity] %!s(MISSING) (%!s(MISSING):%!u(MISSING)) File Receiver Init, targetID: %!{(MISSING)public}@, prepareTemplateAndReturnError, error = %!{(MISSING)public}@"
- "setDispatchQueue:"
- "finish"
- "-[W5FileTransferManager startW5FileReceiverWithPeerPublicKey:reply:]"
- "startW5FileSenderForFile:"
- "_setupWithTargetID:"
- "setTargetID:"
- "-[W5FileTransferManager initializeSenderWithTargetID:peerPublicKey:]"
- "v24@?0@\"RPFileTransferItem\"8@?<v@?@\"NSError\">16"
- "T@\"NSData\",R,N,V_publicKeySelf"
- "setFilename:"
- "_tempDirPath"
- "initializeSenderWithTargetID:peerPublicKey:"
- "startW5FileReceiverWithPeerPublicKey:reply:"
- "setItemURL:"
- "setProgressHandler:"
- "setTemporaryDirectoryURL:"
- "selfPublicKey"
- "fileURLWithPath:isDirectory:"
- "v32@0:8@16@24"
- "_session"
- "setPeerPublicKey:"
- "numberWithShort:"
- "\x04"
- "/var/run/com.apple.wifivelocity"
- "[wifivelocity] %!s(MISSING) (%!s(MISSING):%!u(MISSING)) File Sender: Session Activated"
- "[wifivelocity] %!s(MISSING) (%!s(MISSING):%!u(MISSING)) Session Keys: self: %!{(MISSING)public}@, peer: %!{(MISSING)public}@, Filepath: %!{(MISSING)public}@"
- "com.apple.wifivelocity.file-transfer"
- "[wifivelocity] File Sender, Transfer Completion, error: %!{(MISSING)public}@"
- "activate"
- "W5FileTransferManager"
- "initializeReceiverWithTargetID:"
- "@\"NSURL\""
- "-[W5FileTransferManager initializeReceiverWithTargetID:]"
- "peerPublicKey"
- "-[W5FileTransferManager startW5FileSenderForFile:]"
- "v16@?0@\"RPFileTransferProgress\"8"
- "@\"RPFileTransferSession\""
- "[wifivelocity] File Sender, Received item: %!{(MISSING)public}@"
- "publicKeySelf"
- "[wifivelocity] %!s(MISSING) (%!s(MISSING):%!u(MISSING)) File Receiver: Session Activated"
- "[wifivelocity] %!s(MISSING) (%!s(MISSING):%!u(MISSING)) File Sender Init, targetID: %!{(MISSING)public}@, prepareTemplateAndReturnError, error = %!{(MISSING)public}@"
- "setCompletionHandler:"

```
