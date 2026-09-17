## PersonalizedSensing

> `/System/Library/PrivateFrameworks/PersonalizedSensing.framework/Versions/A/PersonalizedSensing`

```diff

-417.0.0.0.0
-  __TEXT.__text: 0xe31c
+502.0.5.0.0
+  __TEXT.__text: 0xe5e8
   __TEXT.__objc_methlist: 0x14fc
-  __TEXT.__const: 0x118
-  __TEXT.__cstring: 0x13ae
+  __TEXT.__const: 0x120
+  __TEXT.__cstring: 0x1480
   __TEXT.__oslogstring: 0xb60
-  __TEXT.__gcc_except_tab: 0x2b0
+  __TEXT.__gcc_except_tab: 0x2bc
   __TEXT.__unwind_info: 0x700
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xcf0
+  __DATA_CONST.__objc_selrefs: 0xd00
   __DATA_CONST.__objc_superrefs: 0xa0
   __DATA_CONST.__objc_arraydata: 0x108
-  __DATA_CONST.__got: 0x1a8
+  __DATA_CONST.__got: 0x1b0
   __AUTH_CONST.__const: 0x380
-  __AUTH_CONST.__cfstring: 0x1ac0
+  __AUTH_CONST.__cfstring: 0x1b40
   __AUTH_CONST.__objc_const: 0x2358
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__auth_got: 0x0

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libperfcheck.dylib
   Functions: 508
-  Symbols:   1239
-  CStrings:  311
+  Symbols:   1242
+  CStrings:  310
 
Symbols:
+ _OBJC_CLASS_$_NSAssertionHandler
+ _objc_msgSend$currentHandler
+ _objc_msgSend$handleFailureInMethod:object:file:lineNumber:description:
Functions:
~ -[MODefaultsManager objectForKey:] : 252 -> 340
~ -[MODefaultsManager objectForKeyWithoutLog:] : 160 -> 260
~ -[MODefaultsManager deleteObjectForKey:] : 252 -> 332
~ -[MODefaultsManager setObject:forKey:] : 288 -> 376
~ -[MODefaultsManager setObjectWithoutLog:forKey:] : 92 -> 212
~ -[MOConnectionManager _getActiveConnection] : 712 -> 800
~ -[MOConnectionManager withProxyProvider:proxyHandler:onError:] : 460 -> 540
~ +[MODictionaryEncoder encodeDictionary:] : 336 -> 428
~ +[MODictionaryEncoder decodeToDictionary:] : 336 -> 428
~ +[MOPlatformInfo isSeedBuild] : 120 -> 8
CStrings:
- "PlatformInfoOverrideIsSeedBuild"
```
