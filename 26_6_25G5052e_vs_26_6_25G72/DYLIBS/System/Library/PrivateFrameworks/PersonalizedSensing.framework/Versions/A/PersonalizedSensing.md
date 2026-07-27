## PersonalizedSensing

> `/System/Library/PrivateFrameworks/PersonalizedSensing.framework/Versions/A/PersonalizedSensing`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
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
-  __TEXT.__text: 0xfadc
+  __TEXT.__text: 0xf7f4
   __TEXT.__auth_stubs: 0x3c0
   __TEXT.__objc_methlist: 0x14dc
   __TEXT.__const: 0x118
-  __TEXT.__cstring: 0xf7c
+  __TEXT.__cstring: 0xeaa
   __TEXT.__oslogstring: 0xabb
-  __TEXT.__gcc_except_tab: 0x2cc
-  __TEXT.__unwind_info: 0x5c0
+  __TEXT.__gcc_except_tab: 0x2c4
+  __TEXT.__unwind_info: 0x5b8
   __TEXT.__objc_classname: 0x27b
-  __TEXT.__objc_methname: 0x2e9a
+  __TEXT.__objc_methname: 0x2e51
   __TEXT.__objc_methtype: 0x448
-  __TEXT.__objc_stubs: 0x25a0
-  __DATA_CONST.__got: 0x1b0
+  __TEXT.__objc_stubs: 0x2560
+  __DATA_CONST.__got: 0x1a8
   __DATA_CONST.__const: 0x160
   __DATA_CONST.__objc_classlist: 0xc0
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xce8
+  __DATA_CONST.__objc_selrefs: 0xcd8
   __DATA_CONST.__objc_superrefs: 0xa0
   __DATA_CONST.__objc_arraydata: 0x10
   __AUTH_CONST.__auth_got: 0x1f8
   __AUTH_CONST.__const: 0x380
-  __AUTH_CONST.__cfstring: 0x1760
+  __AUTH_CONST.__cfstring: 0x16e0
   __AUTH_CONST.__objc_const: 0x2358
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x4b0

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libperfcheck.dylib
   Functions: 515
-  Symbols:   1240
-  CStrings:  888
+  Symbols:   1237
+  CStrings:  887
 
Symbols:
- _OBJC_CLASS_$_NSAssertionHandler
- _objc_msgSend$currentHandler
- _objc_msgSend$handleFailureInMethod:object:file:lineNumber:description:
Functions:
~ -[MODefaultsManager objectForKey:] : 372 -> 280
~ -[MODefaultsManager objectForKeyWithoutLog:] : 288 -> 184
~ -[MODefaultsManager deleteObjectForKey:] : 388 -> 304
~ -[MODefaultsManager setObject:forKey:] : 428 -> 336
~ -[MODefaultsManager setObjectWithoutLog:forKey:] : 232 -> 108
~ -[MOConnectionManager _getActiveConnection] : 852 -> 760
~ -[MOConnectionManager withProxyProvider:proxyHandler:onError:] : 548 -> 464
~ +[MODictionaryEncoder encodeDictionary:] : 456 -> 360
~ +[MODictionaryEncoder decodeToDictionary:] : 456 -> 360
~ +[MOPlatformInfo isSeedBuild] : 8 -> 128
CStrings:
+ "PlatformInfoOverrideIsSeedBuild"
- "currentHandler"
- "handleFailureInMethod:object:file:lineNumber:description:"
```
