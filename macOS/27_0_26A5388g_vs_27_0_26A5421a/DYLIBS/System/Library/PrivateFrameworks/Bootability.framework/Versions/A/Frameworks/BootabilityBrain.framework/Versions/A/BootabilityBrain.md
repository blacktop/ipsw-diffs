## BootabilityBrain

> `/System/Library/PrivateFrameworks/Bootability.framework/Versions/A/Frameworks/BootabilityBrain.framework/Versions/A/BootabilityBrain`

```diff

-88.0.1.0.0
-  __TEXT.__text: 0x29f718
-  __TEXT.__objc_methlist: 0x3b8c
+88.0.2.0.0
+  __TEXT.__text: 0x2a002c
+  __TEXT.__objc_methlist: 0x3b9c
   __TEXT.__const: 0xa67f8
-  __TEXT.__oslogstring: 0x81e1
-  __TEXT.__cstring: 0x53600
+  __TEXT.__oslogstring: 0x81f7
+  __TEXT.__cstring: 0x536c8
   __TEXT.__gcc_except_tab: 0x4940
-  __TEXT.__unwind_info: 0x7220
+  __TEXT.__unwind_info: 0x7238
   __TEXT.__eh_frame: 0x65c
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0x1838
+  __DATA_CONST.__objc_selrefs: 0x1870
   __DATA_CONST.__objc_superrefs: 0x250
   __DATA_CONST.__objc_arraydata: 0x30
-  __DATA_CONST.__got: 0x5c8
-  __AUTH_CONST.__const: 0x9c78
-  __AUTH_CONST.__cfstring: 0x18ec0
+  __DATA_CONST.__got: 0x5d0
+  __AUTH_CONST.__const: 0x9c98
+  __AUTH_CONST.__cfstring: 0x18ee0
   __AUTH_CONST.__objc_const: 0x6b00
   __AUTH_CONST.__weak_auth_got: 0x20
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__auth_got: 0x12b8
+  __AUTH_CONST.__auth_got: 0x12d0
   __AUTH.__objc_data: 0x1ef0
   __AUTH.__data: 0x6e0
   __AUTH.__thread_vars: 0x18
   __AUTH.__thread_bss: 0x20
   __DATA.__objc_ivar: 0x3e0
   __DATA.__data: 0x63f8
-  __DATA.__bss: 0x4e00
+  __DATA.__bss: 0x4e10
   __DATA.__common: 0x1118
   - /System/Library/Frameworks/CFNetwork.framework/Versions/A/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/liblzma.5.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 12714
-  Symbols:   16639
-  CStrings:  11888
+  Functions: 12730
+  Symbols:   16666
+  CStrings:  11894
 
Symbols:
+ -[AMSupportStaticURLSession shouldUpgrateToHTTPS]
+ _AMSupportEcDsaCreateSignature
+ _AMSupportEcDsaCreateSignatureSha256
+ _AMSupportEcDsaCreateSignatureSha384
+ _AMSupportEcDsaCreateSignatureSha512
+ _AMSupportEcDsaCreateSignatureWithCp
+ _AMSupportEcDsaVerifySignature
+ _CFBundleGetInfoDictionary
+ _CFBundleGetMainBundle
+ _Img4EncodeItemCopyAndTransferBuffer
+ _Img4EncodeSet
+ _OBJC_CLASS_$_NSURLComponents
+ _UARPLayer2RequestAssetBuffer
+ _UARPLayer2ReturnAssetBuffer
+ __AMSupportX509DecodeEcVerifySignatureDataWithOid
+ ___49-[AMSupportStaticURLSession shouldUpgrateToHTTPS]_block_invoke
+ _ccDRBGGetRngState
+ _disk_is_virtual
+ _objc_msgSend$componentsWithURL:resolvingAgainstBaseURL:
+ _objc_msgSend$isEqualToNumber:
+ _objc_msgSend$port
+ _objc_msgSend$scheme
+ _objc_msgSend$setPort:
+ _objc_msgSend$setScheme:
+ _objc_msgSend$shouldUpgrateToHTTPS
+ disk_is_virtual
+ shouldUpgrateToHTTPS.onceToken
+ shouldUpgrateToHTTPS.usingATS
- _Img4EncodeDictionary
CStrings:
+ "-[AMSupportStaticURLSession _urlRequestForHTTPMessage:]"
+ "22:06:58"
+ "88.0.2"
+ "Aug 11 2026"
+ "Helsinki_Restore_Host-58.0.45"
+ "Leaving custom port as is: %@"
+ "NSAppTransportSecurity"
+ "disk is vitual ?: %d\n"
+ "httpResponseData is NULL"
+ "libauthinstall-1155.0.5"
+ "using ATS, upgraded requestURL to https: %@"
- "00:26:54"
- "88.0.1"
- "Helsinki_Restore_Host-58.0.44"
- "Jul 16 2026"
- "libauthinstall-1155.0.4"
```
