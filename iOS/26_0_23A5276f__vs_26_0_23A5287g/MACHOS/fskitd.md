## fskitd

> `/usr/libexec/fskitd`

```diff

-737.0.10.0.0
-  __TEXT.__text: 0x43648
+737.0.14.0.1
+  __TEXT.__text: 0x43c94
   __TEXT.__auth_stubs: 0xb00
-  __TEXT.__objc_stubs: 0x48e0
-  __TEXT.__objc_methlist: 0x1e74
+  __TEXT.__objc_stubs: 0x4960
+  __TEXT.__objc_methlist: 0x1e84
   __TEXT.__const: 0x130
-  __TEXT.__gcc_except_tab: 0x2344
-  __TEXT.__oslogstring: 0x3862
-  __TEXT.__cstring: 0x2c60
+  __TEXT.__gcc_except_tab: 0x2358
+  __TEXT.__oslogstring: 0x39f8
+  __TEXT.__cstring: 0x2ca6
   __TEXT.__objc_classname: 0x223
-  __TEXT.__objc_methname: 0x56d5
+  __TEXT.__objc_methname: 0x5715
   __TEXT.__objc_methtype: 0x1e6d
-  __TEXT.__unwind_info: 0xf60
+  __TEXT.__unwind_info: 0xf70
   __DATA_CONST.__auth_got: 0x590
-  __DATA_CONST.__got: 0x338
-  __DATA_CONST.__const: 0x20d0
+  __DATA_CONST.__got: 0x350
+  __DATA_CONST.__const: 0x20f8
   __DATA_CONST.__cfstring: 0x860
   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_protolist: 0x48

   __DATA_CONST.__objc_superrefs: 0x68
   __DATA_CONST.__objc_intobj: 0x18
   __DATA.__objc_const: 0x2190
-  __DATA.__objc_selrefs: 0x1668
+  __DATA.__objc_selrefs: 0x1688
   __DATA.__objc_ivar: 0x170
   __DATA.__objc_data: 0x5a0
   __DATA.__data: 0x6b0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  UUID: 608C8B52-E164-31EC-B742-10039F24AD3A
-  Functions: 1265
-  Symbols:   293
-  CStrings:  1926
+  UUID: 882C37CA-5365-384F-8BB5-C6687975D515
+  Functions: 1272
+  Symbols:   296
+  CStrings:  1938
 
Symbols:
+ _FSModuleIdentityAttributeSupportedSchemes
+ _OBJC_CLASS_$_FSServerURLResource
+ _OBJC_CLASS_$_NSArray
CStrings:
+ "%s: Extension (%@) doesn't have any supported schemes"
+ "%s: Extension (%@) doesn't support given resource (%@) scheme (%@)"
+ "%s: Extension (%@) supported scheme isn't an array, resource scheme isn't supported"
+ "%s: Extension (%@) supports given resource (%@) scheme (%@)"
+ "%s: Scheme for resource (%@) not supported by extension (%@)"
+ "%s: URL scheme is nil, extension (%@) doesn't support this resource (%@) scheme"
+ "-[fskitdXPCServer extensionSupportsResourceScheme:resource:]"
+ "B16@?0@8"
+ "extensionSupportsResourceScheme:resource:"
+ "fs_any_of:"
+ "scheme"
+ "url"

```
