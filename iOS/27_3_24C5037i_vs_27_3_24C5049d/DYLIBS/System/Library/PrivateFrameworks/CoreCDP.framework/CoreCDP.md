## CoreCDP

> `/System/Library/PrivateFrameworks/CoreCDP.framework/CoreCDP`

```diff

-448.250.2.0.0
-  __TEXT.__text: 0x4e9b8
-  __TEXT.__objc_methlist: 0x3ac4
+448.250.5.0.0
+  __TEXT.__text: 0x4eb48
+  __TEXT.__objc_methlist: 0x3adc
   __TEXT.__const: 0x14e4
   __TEXT.__gcc_except_tab: 0x1114
   __TEXT.__oslogstring: 0x91ef
-  __TEXT.__cstring: 0x6831
+  __TEXT.__cstring: 0x6856
   __TEXT.__dlopen_cstrs: 0xca
   __TEXT.__ustring: 0x28
-  __TEXT.__unwind_info: 0x2048
+  __TEXT.__unwind_info: 0x2050
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x3020
+  __DATA_CONST.__const: 0x3028
   __DATA_CONST.__objc_classlist: 0x1a8
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x21f0
+  __DATA_CONST.__objc_selrefs: 0x2210
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0xe8
   __DATA_CONST.__objc_arraydata: 0xf8
   __DATA_CONST.__got: 0x4f8
   __AUTH_CONST.__const: 0x650
-  __AUTH_CONST.__cfstring: 0x40e0
+  __AUTH_CONST.__cfstring: 0x4100
   __AUTH_CONST.__objc_const: 0x8878
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x28

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2409
-  Symbols:   3920
-  CStrings:  1661
+  Functions: 2411
+  Symbols:   3923
+  CStrings:  1662
 
Symbols:
+ +[CDPUtilities reportMissingEntitlementWithContext:error:]
+ +[CDPUtilities shouldDenyAccessGivenIsEntitled:context:error:alwaysEnforced:]
+ _kCDPAnalyticsMissingEntitlementEvent
CStrings:
+ "com.apple.corecdp.missingEntitlement"
```
