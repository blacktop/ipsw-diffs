## NewsFoundation

> `/System/Library/PrivateFrameworks/NewsFoundation.framework/NewsFoundation`

```diff

-5345.2.0.0.0
-  __TEXT.__text: 0x84b4
-  __TEXT.__auth_stubs: 0x690
-  __TEXT.__objc_methlist: 0xb94
+5407.3.0.0.0
+  __TEXT.__text: 0x8720
+  __TEXT.__auth_stubs: 0x6b0
+  __TEXT.__objc_methlist: 0xbc4
   __TEXT.__const: 0xd8
-  __TEXT.__cstring: 0xbf0
+  __TEXT.__cstring: 0xc13
   __TEXT.__oslogstring: 0x44
   __TEXT.__gcc_except_tab: 0xb8
-  __TEXT.__unwind_info: 0x34c
+  __TEXT.__unwind_info: 0x3c8
   __TEXT.__objc_classname: 0x161
-  __TEXT.__objc_methname: 0x174c
-  __TEXT.__objc_methtype: 0x496
+  __TEXT.__objc_methname: 0x17aa
+  __TEXT.__objc_methtype: 0x4a7
   __TEXT.__objc_stubs: 0x1260
-  __DATA_CONST.__got: 0x50
+  __DATA_CONST.__got: 0x58
   __DATA_CONST.__const: 0x5e0
   __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1308
-  __DATA_CONST.__objc_selrefs: 0x738
+  __DATA_CONST.__objc_const: 0x1338
+  __DATA_CONST.__objc_selrefs: 0x748
   __DATA_CONST.__objc_classrefs: 0xe8
   __DATA_CONST.__objc_superrefs: 0x70
-  __AUTH_CONST.__const: 0x180
-  __AUTH_CONST.__cfstring: 0x580
-  __AUTH_CONST.__objc_const: 0x690
-  __AUTH_CONST.__auth_got: 0x358
-  __DATA.__objc_ivar: 0xc8
+  __AUTH_CONST.__cfstring: 0x5c0
+  __AUTH_CONST.__objc_const: 0x0
+  __AUTH_CONST.__const: 0x20
+  __AUTH_CONST.__auth_got: 0x368
+  __DATA.__objc_ivar: 0xcc
   __DATA.__data: 0x1f8
   __DATA.__bss: 0x20
+  __DATA_DIRTY.__const: 0x160
+  __DATA_DIRTY.__objc_const: 0x690
   __DATA_DIRTY.__objc_data: 0x500
   __DATA_DIRTY.__bss: 0x70
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Network.framework/Network
+  - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
   - /System/Library/PrivateFrameworks/Bom.framework/Bom
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0655656F-EF40-3E5F-AC2A-F24C8220C268
-  Functions: 330
-  Symbols:   1213
-  CStrings:  581
+  UUID: 52F31410-D61B-3808-8234-7C1C05945168
+  Functions: 335
+  Symbols:   1226
+  CStrings:  589
 
Symbols:
+ +[NFReachability _currentNetworkStatus]
+ -[NFMultiDelegate initWithDelegate:delegateProtocol:options:]
+ -[NFMultiDelegate lock]
+ -[NFMultiDelegate setLock:]
+ _NFSystemName
+ _OBJC_IVAR_$_NFMultiDelegate._lock
+ _SCNetworkReachabilityCreateWithAddress
+ _SCNetworkReachabilityGetFlags
+ ___block_literal_global.44
+ _kCFAllocatorDefault
+ _objc_msgSend$_currentNetworkStatus
+ _objc_msgSend$initWithDelegate:delegateProtocol:options:
- ___block_literal_global.38
- _objc_msgSend$addDelegate:
- _objc_msgSend$removeDelegate:
CStrings:
+ "@40@0:8@16@24Q32"
+ "ProductName"
+ "T@\"NFUnfairLock\",&,N,V_lock"
+ "_currentNetworkStatus"
+ "initWithDelegate:delegateProtocol:options:"
+ "j9Th5smJpdztHwc+i39zIg"

```
