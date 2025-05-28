## MDMClientLibrary

> `/System/Library/PrivateFrameworks/MDMClientLibrary.framework/MDMClientLibrary`

```diff

-3.26.4.1.0
-  __TEXT.__text: 0x151ec
-  __TEXT.__auth_stubs: 0x650
-  __TEXT.__objc_methlist: 0xfcc
+3.26.5.12.0
+  __TEXT.__text: 0x15550
+  __TEXT.__auth_stubs: 0x660
+  __TEXT.__objc_methlist: 0xff4
   __TEXT.__const: 0x81
-  __TEXT.__gcc_except_tab: 0x2d4
-  __TEXT.__cstring: 0x1c64
+  __TEXT.__gcc_except_tab: 0x2e4
+  __TEXT.__cstring: 0x1c79
   __TEXT.__oslogstring: 0x1cc5
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__unwind_info: 0x4a8
+  __TEXT.__unwind_info: 0x4b8
   __TEXT.__objc_classname: 0x295
-  __TEXT.__objc_methname: 0x3c89
-  __TEXT.__objc_methtype: 0x7e2
-  __TEXT.__objc_stubs: 0x2bc0
+  __TEXT.__objc_methname: 0x3d2d
+  __TEXT.__objc_methtype: 0x7e5
+  __TEXT.__objc_stubs: 0x2c40
   __DATA_CONST.__got: 0x178
-  __DATA_CONST.__const: 0xdb0
+  __DATA_CONST.__const: 0xdb8
   __DATA_CONST.__objc_classlist: 0xa8
   __DATA_CONST.__objc_catlist: 0x0
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x2908
-  __DATA_CONST.__objc_selrefs: 0xe38
-  __AUTH_CONST.__cfstring: 0x2b60
+  __DATA_CONST.__objc_const: 0x2958
+  __DATA_CONST.__objc_selrefs: 0xe68
+  __DATA_CONST.__objc_protorefs: 0x10
+  __DATA_CONST.__objc_classrefs: 0x1c8
+  __DATA_CONST.__objc_superrefs: 0x60
+  __AUTH_CONST.__cfstring: 0x2b80
   __AUTH_CONST.__objc_const: 0xd8
   __AUTH_CONST.__objc_intobj: 0x30
-  __AUTH_CONST.__const: 0x80
-  __AUTH_CONST.__auth_got: 0x338
-  __DATA.__objc_protorefs: 0x10
-  __DATA.__objc_classrefs: 0x1c8
-  __DATA.__objc_superrefs: 0x60
-  __DATA.__objc_ivar: 0xdc
+  __AUTH_CONST.__const: 0xa0
+  __AUTH_CONST.__auth_got: 0x340
+  __DATA.__objc_ivar: 0xe0
   __DATA.__data: 0x480
   __DATA.__bss: 0x100
-  __DATA_DIRTY.__const: 0x2c0
+  __DATA_DIRTY.__const: 0x2a0
   __DATA_DIRTY.__objc_const: 0x828
   __DATA_DIRTY.__objc_data: 0x690
   __DATA_DIRTY.__bss: 0x40

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 428
-  Symbols:   2096
-  CStrings:  1210
+  Functions: 432
+  Symbols:   2112
+  CStrings:  1220
 
Symbols:
+ +[MDMConfiguration isDataSeparated]
+ -[MDMConfiguration copyMemberQueueIdentity]
+ -[MDMHTTPTransaction initWithURL:data:identity:pinnedCertificates:pinningRevocationCheckRequired:signMessage:isCheckin:isCheckout:isShortTransaction:rmAccountID:]
+ -[MDMHTTPTransaction isCheckout]
+ GCC_except_table10
+ GCC_except_table16
+ GCC_except_table18
+ GCC_except_table20
+ _CFRetain
+ _OBJC_IVAR_$_MDMHTTPTransaction._isCheckout
+ ___43-[MDMConfiguration copyMemberQueueIdentity]_block_invoke
+ ___54-[MDMClientCore _queue_createAndStartMDMXPCConnection]_block_invoke.111
+ ___block_literal_global.81
+ _kMDMLastInstallationDateKey
+ _objc_msgSend$copyMemberQueueIdentity
+ _objc_msgSend$initWithURL:data:identity:pinnedCertificates:pinningRevocationCheckRequired:signMessage:isCheckin:isCheckout:isShortTransaction:rmAccountID:
+ _objc_msgSend$isVisionDevice
+ _objc_msgSend$set
+ _objc_msgSend$setIgnoreAuthenticatorError:
- -[MDMHTTPTransaction initWithURL:data:identity:pinnedCertificates:pinningRevocationCheckRequired:signMessage:isCheckin:isShortTransaction:rmAccountID:]
- GCC_except_table11
- GCC_except_table15
- GCC_except_table17
- GCC_except_table19
- ___54-[MDMClientCore _queue_createAndStartMDMXPCConnection]_block_invoke.110
- ___block_literal_global.80
- _objc_msgSend$initWithURL:data:identity:pinnedCertificates:pinningRevocationCheckRequired:signMessage:isCheckin:isShortTransaction:rmAccountID:
CStrings:
+ "\x1d\x12\x11"
+ "@76@0:8@16@24^{__SecIdentity=}32@40B48B52B56B60B64@68"
+ "LastInstallationDate"
+ "T@\"NSString\",?,R,C"
+ "TB,R,N,V_isCheckout"
+ "_isCheckout"
+ "copyMemberQueueIdentity"
+ "initWithURL:data:identity:pinnedCertificates:pinningRevocationCheckRequired:signMessage:isCheckin:isCheckout:isShortTransaction:rmAccountID:"
+ "isCheckout"
+ "isVisionDevice"
+ "set"
+ "setIgnoreAuthenticatorError:"
- "\x11\x1e\x11"
- "@72@0:8@16@24^{__SecIdentity=}32@40B48B52B56B60@64"
- "initWithURL:data:identity:pinnedCertificates:pinningRevocationCheckRequired:signMessage:isCheckin:isShortTransaction:rmAccountID:"

```
