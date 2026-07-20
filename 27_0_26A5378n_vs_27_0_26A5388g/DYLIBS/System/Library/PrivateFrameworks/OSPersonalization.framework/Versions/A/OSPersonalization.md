## OSPersonalization

> `/System/Library/PrivateFrameworks/OSPersonalization.framework/Versions/A/OSPersonalization`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-151.0.0.0.0
-  __TEXT.__text: 0x35140
-  __TEXT.__objc_methlist: 0x16ac
+153.0.0.0.0
+  __TEXT.__text: 0x350e8
+  __TEXT.__objc_methlist: 0x169c
   __TEXT.__const: 0xd728
-  __TEXT.__cstring: 0x564f
-  __TEXT.__oslogstring: 0x277b
-  __TEXT.__gcc_except_tab: 0x58c
-  __TEXT.__unwind_info: 0x6c8
+  __TEXT.__cstring: 0x5684
+  __TEXT.__oslogstring: 0x27b0
+  __TEXT.__gcc_except_tab: 0x708
+  __TEXT.__unwind_info: 0x6d0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1090
+  __DATA_CONST.__objc_selrefs: 0x1088
   __DATA_CONST.__objc_superrefs: 0x68
   __DATA_CONST.__got: 0x350
   __AUTH_CONST.__const: 0xc98
-  __AUTH_CONST.__cfstring: 0x3f60
+  __AUTH_CONST.__cfstring: 0x3f80
   __AUTH_CONST.__objc_const: 0x2610
   __AUTH_CONST.__auth_got: 0x5c0
   __AUTH.__objc_data: 0x690

   - /usr/lib/libauthinstall.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libpartition2_dynamic.dylib
-  Functions: 856
-  Symbols:   2454
-  CStrings:  626
+  Functions: 855
+  Symbols:   2453
+  CStrings:  627
 
Symbols:
+ GCC_except_table2
- +[OSPUtilities ignoreAuthInstallErrorInTestMode:]
- _objc_msgSend$ignoreAuthInstallErrorInTestMode:
Functions:
~ -[OSPPersonalizationOperation _personalize] : 3020 -> 3028
~ -[OSPPersonalizeCentauri __personalizeBundle:productionMode:securityMode:ticket:error:] : 5292 -> 5240
- +[OSPUtilities ignoreAuthInstallErrorInTestMode:]
CStrings:
+ "00:26:23"
+ "153"
+ "Jul 16 2026"
+ "Skipping Centauri personalization in test mode"
+ "Skipping personalization in test mode"
- "151"
- "21:19:13"
- "Ignoring error in test mode: %d"
- "Jun 30 2026"
```
