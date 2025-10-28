## PersonalizedSensing

> `/System/Library/PrivateFrameworks/PersonalizedSensing.framework/PersonalizedSensing`

```diff

 302.0.13.0.0
-  __TEXT.__text: 0x109f4
+  __TEXT.__text: 0x10744
   __TEXT.__auth_stubs: 0x5c0
   __TEXT.__objc_methlist: 0x1544
   __TEXT.__const: 0x130
-  __TEXT.__cstring: 0x1094
+  __TEXT.__cstring: 0xfc2
   __TEXT.__oslogstring: 0x135b
-  __TEXT.__gcc_except_tab: 0x328
-  __TEXT.__unwind_info: 0x5f0
+  __TEXT.__gcc_except_tab: 0x31c
+  __TEXT.__unwind_info: 0x5e8
   __TEXT.__objc_classname: 0x29e
-  __TEXT.__objc_methname: 0x316d
+  __TEXT.__objc_methname: 0x3124
   __TEXT.__objc_methtype: 0x53b
-  __TEXT.__objc_stubs: 0x2a20
-  __DATA_CONST.__got: 0x1f8
+  __TEXT.__objc_stubs: 0x29e0
+  __DATA_CONST.__got: 0x1f0
   __DATA_CONST.__const: 0x518
   __DATA_CONST.__objc_classlist: 0xc0
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xdc8
+  __DATA_CONST.__objc_selrefs: 0xdb8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xa0
   __DATA_CONST.__objc_arraydata: 0x10
   __AUTH_CONST.__auth_got: 0x2f8
   __AUTH_CONST.__const: 0x180
-  __AUTH_CONST.__cfstring: 0x17c0
+  __AUTH_CONST.__cfstring: 0x1740
   __AUTH_CONST.__objc_const: 0x2390
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x4b0

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libperfcheck.dylib
-  UUID: 770E05EE-A8AF-31C3-85E1-7CEF97BC009A
+  UUID: 905DC88E-3E96-3A2D-ACBB-A4A7324DAF9B
   Functions: 521
-  Symbols:   1962
-  CStrings:  1214
+  Symbols:   1959
+  CStrings:  1204
 
Symbols:
+ ___43-[MOConnectionManager _getActiveConnection]_block_invoke.3
+ ___43-[MOConnectionManager getSyncProxyProvider]_block_invoke.24
+ ___44-[MOConnectionManager getAsyncProxyProvider]_block_invoke.26
+ ___53-[MOConnectionManager _callProxy:usingBlock:onError:]_block_invoke.13
+ ___53-[MOConnectionManager _callProxy:usingBlock:onError:]_block_invoke_2.14
+ ___62-[MOConnectionManager withProxyProvider:proxyHandler:onError:]_block_invoke.17
+ ___62-[MOConnectionManager withProxyProvider:proxyHandler:onError:]_block_invoke.17.cold.1
- _OBJC_CLASS_$_NSAssertionHandler
- ___43-[MOConnectionManager _getActiveConnection]_block_invoke.8
- ___43-[MOConnectionManager getSyncProxyProvider]_block_invoke.34
- ___44-[MOConnectionManager getAsyncProxyProvider]_block_invoke.36
- ___53-[MOConnectionManager _callProxy:usingBlock:onError:]_block_invoke.20
- ___53-[MOConnectionManager _callProxy:usingBlock:onError:]_block_invoke_2.21
- ___62-[MOConnectionManager withProxyProvider:proxyHandler:onError:]_block_invoke.27
- ___62-[MOConnectionManager withProxyProvider:proxyHandler:onError:]_block_invoke.27.cold.1
- _objc_msgSend$currentHandler
- _objc_msgSend$handleFailureInMethod:object:file:lineNumber:description:
Functions:
~ -[MODefaultsManager objectForKey:] : 332 -> 248
~ -[MODefaultsManager objectForKeyWithoutLog:] : 260 -> 164
~ -[MODefaultsManager deleteObjectForKey:] : 356 -> 280
~ -[MODefaultsManager setObject:forKey:] : 392 -> 308
~ -[MODefaultsManager setObjectWithoutLog:forKey:] : 216 -> 100
~ -[MOConnectionManager _getActiveConnection] : 784 -> 700
~ -[MOConnectionManager withProxyProvider:proxyHandler:onError:] : 488 -> 412
~ +[MODictionaryEncoder encodeDictionary:] : 408 -> 320
~ +[MODictionaryEncoder decodeToDictionary:] : 408 -> 320
~ +[MOPlatformInfo isSeedBuild] : 8 -> 112
CStrings:
+ "PlatformInfoOverrideIsSeedBuild"
- "currentHandler"
- "handleFailureInMethod:object:file:lineNumber:description:"

```
