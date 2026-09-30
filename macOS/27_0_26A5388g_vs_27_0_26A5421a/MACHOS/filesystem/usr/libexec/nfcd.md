## nfcd

> `/usr/libexec/nfcd`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA.__objc_const`
- `__DATA.__objc_data`

```diff

-370.40.2.0.0
-  __TEXT.__text: 0x1710b8
+370.42.1.0.0
+  __TEXT.__text: 0x171908
   __TEXT.__auth_stubs: 0x13f0
   __TEXT.__delay_helper: 0x1f4
-  __TEXT.__objc_stubs: 0x9ee0
-  __TEXT.__objc_methlist: 0x75c8
+  __TEXT.__objc_stubs: 0x9f00
+  __TEXT.__objc_methlist: 0x75e0
   __TEXT.__const: 0x10cc
-  __TEXT.__cstring: 0x18777
-  __TEXT.__oslogstring: 0x18567
+  __TEXT.__cstring: 0x1884c
+  __TEXT.__oslogstring: 0x185d6
   __TEXT.__objc_classname: 0x14f5
-  __TEXT.__objc_methname: 0x10a44
+  __TEXT.__objc_methname: 0x10a97
   __TEXT.__objc_methtype: 0x3dbf
-  __TEXT.__unwind_info: 0x1e58
+  __TEXT.__unwind_info: 0x1e60
   __DATA_CONST.__const: 0x6d70
-  __DATA_CONST.__cfstring: 0xe920
+  __DATA_CONST.__cfstring: 0xe980
   __DATA_CONST.__objc_classlist: 0x4d0
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x278

   __DATA_CONST.__objc_protorefs: 0x158
   __DATA_CONST.__objc_superrefs: 0x338
   __DATA_CONST.__objc_intobj: 0x5ef8
-  __DATA_CONST.__objc_arraydata: 0x1a20
+  __DATA_CONST.__objc_arraydata: 0x1a38
   __DATA_CONST.__objc_dictobj: 0xbe0
-  __DATA_CONST.__objc_arrayobj: 0x138
+  __DATA_CONST.__objc_arrayobj: 0x180
   __DATA_CONST.__auth_got: 0xa00
-  __DATA_CONST.__got: 0x708
+  __DATA_CONST.__got: 0x710
   __DATA.__objc_const: 0x10120
-  __DATA.__objc_selrefs: 0x3a78
+  __DATA.__objc_selrefs: 0x3a98
   __DATA.__objc_ivar: 0xcfc
   __DATA.__objc_data: 0x3020
-  __DATA.__data: 0x1df4
+  __DATA.__data: 0x1dfc
   __DATA.__bss: 0x200
   __DATA.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libnfshared.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3118
+  Functions: 3120
   Symbols:   509
-  CStrings:  8791
+  CStrings:  8803
 
CStrings:
+ "%{public}s:%i Overriding known bad wireless ECP frame to terminal type other"
+ "%{public}s:%i PACE config enabled"
+ "+[NFATLMobileSettings paceStaticRFAlwaysOn]"
+ "+[NFATLMobileSettings paceStaticRFBundleIds]"
+ "-[NFFieldNotificationECP1_0 initWithDictionary:]"
+ "NFCD built from (B&I) Stockholm_Base-370.42.1"
+ "PACE_STATIC_RF_ALWAYS_ON"
+ "PACE_STATIC_RF_BUNDLE_IDS"
+ "fr.gouv.france-identite"
+ "pace"
+ "paceStaticRFAlwaysOn"
+ "paceStaticRFBundleIds"
+ "setReaderModeDynamicBBA:staticBBA:"
- "NFCD built from (B&I) Stockholm_Base-370.40.2"
```
