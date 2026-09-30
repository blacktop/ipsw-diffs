## nfcd

> `filesystem/usr/libexec/nfcd`

```diff

-365.2.0.0.0
-  __TEXT.__text: 0x1f0d74
+365.3.1.0.0
+  __TEXT.__text: 0x1f10a8
   __TEXT.__auth_stubs: 0x17b0
   __TEXT.__delay_stubs: 0x500
   __TEXT.__delay_helper: 0x16f4
   __TEXT.__objc_stubs: 0xd400
   __TEXT.__objc_methlist: 0x9b40
   __TEXT.__const: 0x1384
-  __TEXT.__objc_methname: 0x14985
-  __TEXT.__cstring: 0x21a91
+  __TEXT.__objc_methname: 0x149b0
+  __TEXT.__cstring: 0x21b12
   __TEXT.__objc_classname: 0x1d80
-  __TEXT.__objc_methtype: 0x4df2
-  __TEXT.__oslogstring: 0x1f323
+  __TEXT.__objc_methtype: 0x4ded
+  __TEXT.__oslogstring: 0x1f392
   __TEXT.__unwind_info: 0x2dc8
   __DATA_CONST.__auth_got: 0xc80
   __DATA_CONST.__got: 0x5e8
   __DATA_CONST.__auth_ptr: 0x18
   __DATA_CONST.__const: 0x95a0
-  __DATA_CONST.__cfstring: 0x11540
+  __DATA_CONST.__cfstring: 0x11580
   __DATA_CONST.__objc_classlist: 0x620
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x390
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x1e8
   __DATA_CONST.__objc_superrefs: 0x460
-  __DATA_CONST.__objc_intobj: 0x77d0
+  __DATA_CONST.__objc_intobj: 0x77e8
   __DATA_CONST.__objc_arraydata: 0x1d30
   __DATA_CONST.__objc_arrayobj: 0x2d0
   __DATA_CONST.__objc_dictobj: 0xf28
   __DATA.__objc_const: 0x147e8
-  __DATA.__objc_selrefs: 0x4868
+  __DATA.__objc_selrefs: 0x4870
   __DATA.__objc_ivar: 0x10a4
   __DATA.__objc_data: 0x3d40
   __DATA.__data: 0x2b94
-  __DATA.__bss: 0x288
+  __DATA.__bss: 0x290
   __DATA.__common: 0x12
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libTelephonyBasebandDynamic.dylib
   - /usr/lib/libnfshared.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 63D2E997-1572-3768-9CEA-F9725AB0E511
-  Functions: 4162
+  UUID: 27035860-59E0-3941-B4FC-3B5A27D4262E
+  Functions: 4163
   Symbols:   585
-  CStrings:  13587
+  CStrings:  13594
 
CStrings:
+ "%{public}s:%i Attempt to perform express configuration while active session is running!"
+ "-[NFExpressModeManager _updateExpressConfigsWithBugCaptureReport:]"
+ "-[NFExpressModeManager getExpressPassConfigAndError:]"
+ "Attempt to perform express configuration while active session is running!"
+ "NFCD built from (B&I) Stockholm_Base-365.3.1"
+ "Vv28@0:8I16@?<v@?qB@\"NSArray\"@\"NSError\">20"
+ "_updateExpressConfigsWithBugCaptureReport:"
+ "active session running"
- "-[NFExpressModeManager getExpressPassConfig]"
- "-[NFExpressModeManager updateExpressConfigsWithBugCaptureReport:]"
- "NFCD built from (B&I) Stockholm_Base-365.2"
- "Vv28@0:8I16@?<v@?qB@\"NSDictionary\"@\"NSArray\">20"

```
