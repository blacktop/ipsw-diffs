## PersonalizedSensing

> `/System/Library/PrivateFrameworks/PersonalizedSensing.framework/PersonalizedSensing`

```diff

 297.0.0.0.0
-  __TEXT.__text: 0x1085c
+  __TEXT.__text: 0x105a8
   __TEXT.__auth_stubs: 0x5c0
   __TEXT.__objc_methlist: 0x152c
   __TEXT.__const: 0x128
-  __TEXT.__cstring: 0x108c
+  __TEXT.__cstring: 0xfba
   __TEXT.__oslogstring: 0x135b
-  __TEXT.__gcc_except_tab: 0x328
-  __TEXT.__unwind_info: 0x5e0
+  __TEXT.__gcc_except_tab: 0x31c
+  __TEXT.__unwind_info: 0x5d8
   __TEXT.__objc_classname: 0x29e
-  __TEXT.__objc_methname: 0x3137
+  __TEXT.__objc_methname: 0x30ee
   __TEXT.__objc_methtype: 0x53b
-  __TEXT.__objc_stubs: 0x29e0
-  __DATA_CONST.__got: 0x1f8
+  __TEXT.__objc_stubs: 0x29a0
+  __DATA_CONST.__got: 0x1f0
   __DATA_CONST.__const: 0x518
   __DATA_CONST.__objc_classlist: 0xc0
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xdb8
+  __DATA_CONST.__objc_selrefs: 0xda8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xa0
   __DATA_CONST.__objc_arraydata: 0x10
   __AUTH_CONST.__auth_got: 0x2f8
   __AUTH_CONST.__const: 0x140
-  __AUTH_CONST.__cfstring: 0x17a0
+  __AUTH_CONST.__cfstring: 0x1720
   __AUTH_CONST.__objc_const: 0x2390
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x4b0

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libperfcheck.dylib
-  UUID: 272E0A6A-8263-3A80-8FBA-3CC41415BE5E
+  UUID: 41FB7A8A-C706-37DB-90F1-71C34910C107
   Functions: 515
-  Symbols:   1942
-  CStrings:  1210
+  Symbols:   1939
+  CStrings:  1200
 
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
~ +[MOPlatformInfo isSeedBuild] : 8 -> 108
CStrings:
+ "PlatformInfoOverrideIsSeedBuild"
- "currentHandler"
- "handleFailureInMethod:object:file:lineNumber:description:"

```
