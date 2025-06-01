## MailKit

> `/System/Library/PrivateFrameworks/MailKit.framework/MailKit`

```diff

-3774.500.171.2.3
-  __TEXT.__text: 0x152f8
-  __TEXT.__auth_stubs: 0x520
-  __TEXT.__objc_methlist: 0x17f0
-  __TEXT.__gcc_except_tab: 0x2948
-  __TEXT.__cstring: 0x118f
+3774.600.62.0.0
+  __TEXT.__text: 0x153a8
+  __TEXT.__auth_stubs: 0x530
+  __TEXT.__objc_methlist: 0x1808
+  __TEXT.__gcc_except_tab: 0x295c
+  __TEXT.__cstring: 0x118a
   __TEXT.__const: 0x10
-  __TEXT.__oslogstring: 0xc2b
+  __TEXT.__oslogstring: 0xbeb
   __TEXT.__ustring: 0x3c6
   __TEXT.__unwind_info: 0xef8
-  __TEXT.__objc_classname: 0x527
-  __TEXT.__objc_methname: 0x4551
-  __TEXT.__objc_methtype: 0xb5a
-  __TEXT.__objc_stubs: 0x2ae0
+  __TEXT.__objc_classname: 0x528
+  __TEXT.__objc_methname: 0x45c7
+  __TEXT.__objc_methtype: 0xb5e
+  __TEXT.__objc_stubs: 0x2b60
   __DATA_CONST.__got: 0x160
-  __DATA_CONST.__const: 0x668
+  __DATA_CONST.__const: 0x640
   __DATA_CONST.__objc_classlist: 0xf8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xc0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x2dd0
-  __DATA_CONST.__objc_selrefs: 0xeb0
+  __DATA_CONST.__objc_const: 0x2e00
+  __DATA_CONST.__objc_selrefs: 0xed0
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_classrefs: 0x1d0
+  __DATA_CONST.__objc_classrefs: 0x1d8
   __DATA_CONST.__objc_superrefs: 0xd8
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__cfstring: 0x1160
-  __AUTH_CONST.__objc_const: 0x90
-  __AUTH_CONST.__const: 0x80
+  __AUTH_CONST.__cfstring: 0x1180
+  __AUTH_CONST.__objc_const: 0x0
+  __AUTH_CONST.__const: 0xc0
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__auth_got: 0x2a0
-  __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0x1fc
+  __AUTH_CONST.__auth_got: 0x2a8
+  __DATA.__objc_ivar: 0x200
   __DATA.__data: 0x900
   __DATA.__bss: 0x88
-  __DATA_DIRTY.__const: 0x1e0
-  __DATA_DIRTY.__objc_const: 0xf70
-  __DATA_DIRTY.__objc_data: 0x960
+  __DATA_DIRTY.__const: 0x1a0
+  __DATA_DIRTY.__objc_const: 0x1000
+  __DATA_DIRTY.__objc_data: 0x9b0
   __DATA_DIRTY.__data: 0x8
   __DATA_DIRTY.__bss: 0xa0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/PlugInKit.framework/PlugInKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8068DADC-78DB-3333-87A1-FEB2771E67A1
-  Functions: 570
-  Symbols:   2566
-  CStrings:  1262
+  UUID: 80F9B7E2-9DC9-3091-ABDD-4DF2908DBFCE
+  Functions: 572
+  Symbols:   2576
+  CStrings:  1269
 
Symbols:
+ -[MEMessage initWithState:encryptionState:signatureState:subject:recipients:from:dataSent:dateReceived:headers:rawData:senderMetadata:]
+ -[MEMessage setSignatureState:]
+ -[MEMessage signatureState]
+ _OBJC_CLASS_$_NSThread
+ _OBJC_IVAR_$_MEMessage._signatureState
+ ___block_literal_global.44
+ ___block_literal_global.53
+ _dispatch_get_global_queue
+ _objc_msgSend$beginExtensionRequestWithOptions:inputItems:error:
+ _objc_msgSend$extensionHostContext
+ _objc_msgSend$initWithState:encryptionState:signatureState:subject:recipients:from:dataSent:dateReceived:headers:rawData:senderMetadata:
+ _objc_msgSend$isMainThread
+ _objc_msgSend$resultIfAvailable:
+ _objc_msgSend$setComposeExtensionHostDelegate:
- -[MEMessage initWithState:encryptionState:subject:recipients:from:dataSent:dateReceived:headers:rawData:senderMetadata:]
- ___block_descriptor_48_ea8_32s40w_e33_v24?0"<NSCopying>"8"NSError"16lw40l8s32l8
- ___block_literal_global.41
- ___block_literal_global.50
- _objc_msgSend$beginExtensionRequestWithOptions:inputItems:completion:
- _objc_msgSend$initWithState:encryptionState:subject:recipients:from:dataSent:dateReceived:headers:rawData:senderMetadata:
CStrings:
+ "'\x11"
+ "@104@0:8q16q24q32@40@48@56@64@72@80@88@96"
+ "EFPropertyKey_signatureState"
+ "The remote extension proxy is not available."
+ "Tq,N,V_signatureState"
+ "_signatureState"
+ "beginExtensionRequestWithOptions:inputItems:error:"
+ "initWithState:encryptionState:signatureState:subject:recipients:from:dataSent:dateReceived:headers:rawData:senderMetadata:"
+ "isMainThread"
+ "resultIfAvailable:"
+ "setSignatureState:"
+ "signatureState"
- "("
- "@96@0:8q16q24@32@40@48@56@64@72@80@88"
- "The -[NSExtension beginExtensionRequestWithOptions:inputItems:completion:] method is taking over 10 seconds."
- "beginExtensionRequestWithOptions:inputItems:completion:"
- "initWithState:encryptionState:subject:recipients:from:dataSent:dateReceived:headers:rawData:senderMetadata:"
- "v24@?0@\"<NSCopying>\"8@\"NSError\"16"

```
