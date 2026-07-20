## PersonalizedSensing

> `/System/Library/PrivateFrameworks/PersonalizedSensing.framework/PersonalizedSensing`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

 308.0.3.0.0
-  __TEXT.__text: 0x11094
+  __TEXT.__text: 0x10dc8
   __TEXT.__auth_stubs: 0x560
   __TEXT.__objc_methlist: 0x1544
   __TEXT.__const: 0x130
-  __TEXT.__cstring: 0x1094
+  __TEXT.__cstring: 0xfc2
   __TEXT.__oslogstring: 0x135b
-  __TEXT.__gcc_except_tab: 0x330
-  __TEXT.__unwind_info: 0x628
+  __TEXT.__gcc_except_tab: 0x328
+  __TEXT.__unwind_info: 0x620
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
   __AUTH_CONST.__auth_got: 0x2c8
   __AUTH_CONST.__const: 0x180
-  __AUTH_CONST.__cfstring: 0x17c0
+  __AUTH_CONST.__cfstring: 0x1740
   __AUTH_CONST.__objc_const: 0x2390
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x4b0

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libperfcheck.dylib
   Functions: 533
-  Symbols:   1322
-  CStrings:  963
+  Symbols:   1319
+  CStrings:  962
 
Symbols:
- _OBJC_CLASS_$_NSAssertionHandler
- _objc_msgSend$currentHandler
- _objc_msgSend$handleFailureInMethod:object:file:lineNumber:description:
Functions:
~ -[MODefaultsManager objectForKey:] : 352 -> 264
~ -[MODefaultsManager objectForKeyWithoutLog:] : 276 -> 176
~ -[MODefaultsManager deleteObjectForKey:] : 368 -> 288
~ -[MODefaultsManager setObject:forKey:] : 400 -> 312
~ -[MODefaultsManager setObjectWithoutLog:forKey:] : 224 -> 104
~ -[MOConnectionManager _getActiveConnection] : 812 -> 724
~ -[MOConnectionManager withProxyProvider:proxyHandler:onError:] : 496 -> 416
~ +[MODictionaryEncoder encodeDictionary:] : 420 -> 328
~ +[MODictionaryEncoder decodeToDictionary:] : 420 -> 328
~ +[MOPlatformInfo isSeedBuild] : 8 -> 120
CStrings:
+ "PlatformInfoOverrideIsSeedBuild"
- "currentHandler"
- "handleFailureInMethod:object:file:lineNumber:description:"
```
