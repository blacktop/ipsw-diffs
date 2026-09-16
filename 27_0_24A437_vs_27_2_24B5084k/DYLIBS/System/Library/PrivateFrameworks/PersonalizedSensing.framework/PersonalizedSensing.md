## PersonalizedSensing

> `/System/Library/PrivateFrameworks/PersonalizedSensing.framework/PersonalizedSensing`

```diff

-417.0.0.0.0
-  __TEXT.__text: 0xfbb4
+502.0.5.0.0
+  __TEXT.__text: 0xfe64
   __TEXT.__objc_methlist: 0x1570
-  __TEXT.__const: 0x138
-  __TEXT.__cstring: 0x14f0
+  __TEXT.__const: 0x140
+  __TEXT.__cstring: 0x15c2
   __TEXT.__oslogstring: 0x1499
-  __TEXT.__gcc_except_tab: 0x310
-  __TEXT.__unwind_info: 0x778
+  __TEXT.__gcc_except_tab: 0x31c
+  __TEXT.__unwind_info: 0x770
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xdd0
+  __DATA_CONST.__objc_selrefs: 0xde0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xa0
   __DATA_CONST.__objc_arraydata: 0x108
-  __DATA_CONST.__got: 0x1f0
+  __DATA_CONST.__got: 0x1f8
   __AUTH_CONST.__const: 0x180
-  __AUTH_CONST.__cfstring: 0x1b40
+  __AUTH_CONST.__cfstring: 0x1bc0
   __AUTH_CONST.__objc_const: 0x2398
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__auth_got: 0x0

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libperfcheck.dylib
   Functions: 531
-  Symbols:   1331
-  CStrings:  356
+  Symbols:   1334
+  CStrings:  355
 
Symbols:
+ _OBJC_CLASS_$_NSAssertionHandler
+ _objc_msgSend$currentHandler
+ _objc_msgSend$handleFailureInMethod:object:file:lineNumber:description:
Functions:
~ -[MODefaultsManager objectForKey:] : 236 -> 320
~ -[MODefaultsManager objectForKeyWithoutLog:] : 152 -> 248
~ -[MODefaultsManager deleteObjectForKey:] : 236 -> 312
~ -[MODefaultsManager setObject:forKey:] : 264 -> 348
~ -[MODefaultsManager setObjectWithoutLog:forKey:] : 88 -> 204
~ -[MOConnectionManager _getActiveConnection] : 688 -> 772
~ -[MOConnectionManager withProxyProvider:proxyHandler:onError:] : 412 -> 488
~ +[MODictionaryEncoder encodeDictionary:] : 308 -> 396
~ +[MODictionaryEncoder decodeToDictionary:] : 308 -> 396
~ +[MOPlatformInfo isSeedBuild] : 112 -> 8
CStrings:
- "PlatformInfoOverrideIsSeedBuild"
```
