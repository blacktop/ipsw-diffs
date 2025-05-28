## NetworkServiceProxy

> `/System/Library/PrivateFrameworks/NetworkServiceProxy.framework/NetworkServiceProxy`

```diff

-702.100.16.0.1
-  __TEXT.__text: 0x891f8
+702.120.2.0.0
+  __TEXT.__text: 0x896a8
   __TEXT.__auth_stubs: 0x17f0
-  __TEXT.__objc_methlist: 0x6d18
+  __TEXT.__objc_methlist: 0x6d60
   __TEXT.__const: 0x588
   __TEXT.__gcc_except_tab: 0x12f4
-  __TEXT.__cstring: 0x6711
+  __TEXT.__cstring: 0x6725
   __TEXT.__oslogstring: 0x765f
-  __TEXT.__unwind_info: 0x19a4
+  __TEXT.__unwind_info: 0x195c
   __TEXT.__eh_frame: 0x38
   __TEXT.__objc_classname: 0x729
   __TEXT.__objc_methname: 0x111be
-  __TEXT.__objc_methtype: 0x1de6
-  __TEXT.__objc_stubs: 0xbf00
+  __TEXT.__objc_methtype: 0x1df3
+  __TEXT.__objc_stubs: 0xbf20
   __DATA_CONST.__got: 0x1e0
-  __DATA_CONST.__const: 0x1618
+  __DATA_CONST.__const: 0x1630
   __DATA_CONST.__objc_classlist: 0x250
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xa458
+  __DATA_CONST.__objc_const: 0xa498
   __DATA_CONST.__objc_selrefs: 0x3ce8
   __DATA_CONST.__objc_classrefs: 0x3b0
   __DATA_CONST.__objc_superrefs: 0x210
   __DATA_CONST.__objc_arraydata: 0x78
   __AUTH_CONST.__const: 0x1550
-  __AUTH_CONST.__cfstring: 0x7480
+  __AUTH_CONST.__cfstring: 0x74e0
   __AUTH_CONST.__objc_const: 0x1ea8
   __AUTH_CONST.__objc_intobj: 0x138
   __AUTH_CONST.__auth_ptr: 0x20

   __DATA.__data: 0x408
   __DATA.__common: 0x24
   __DATA.__bss: 0x8
-  __DATA_DIRTY.__objc_ivar: 0x29c
+  __DATA_DIRTY.__objc_ivar: 0x2a0
   __DATA_DIRTY.__objc_data: 0x2d0
   __DATA_DIRTY.__bss: 0x4a8
   __DATA_DIRTY.__common: 0x20

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2953
-  Symbols:   9334
-  CStrings:  5454
+  Functions: 2959
+  Symbols:   9347
+  CStrings:  5457
 
Symbols:
+ -[NSPPrivacyProxyProxyInfo StringAsAlgorithm:]
+ -[NSPPrivacyProxyProxyInfo algorithmAsString:]
+ -[NSPPrivacyProxyProxyInfo algorithm]
+ -[NSPPrivacyProxyProxyInfo hasAlgorithm]
+ -[NSPPrivacyProxyProxyInfo setAlgorithm:]
+ -[NSPPrivacyProxyProxyInfo setHasAlgorithm:]
+ _objc_msgSend$setAlgorithm:
CStrings:
+ "\x13\x17"
+ "NOT_SET"
+ "P384"
+ "X25519"
+ "{?=\"algorithm\"b1\"supportsFallback\"b1\"supportsResumption\"b1}"
- "\x03\x17"
- "{?=\"supportsFallback\"b1\"supportsResumption\"b1}"

```
