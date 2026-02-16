## init_featureflags

> `/usr/libexec/init_featureflags`

```diff

-101.0.0.0.0
-  __TEXT.__text: 0xf58
-  __TEXT.__auth_stubs: 0x250
+103.0.0.0.0
+  __TEXT.__text: 0x1048
+  __TEXT.__auth_stubs: 0x260
   __TEXT.__objc_stubs: 0x3e0
   __TEXT.__objc_methlist: 0x14
   __TEXT.__const: 0x68
-  __TEXT.__cstring: 0x288
+  __TEXT.__cstring: 0x2ad
   __TEXT.__objc_classname: 0x5
   __TEXT.__objc_methtype: 0x8
   __TEXT.__objc_methname: 0x28d
-  __TEXT.__unwind_info: 0x78
-  __DATA_CONST.__auth_got: 0x130
+  __TEXT.__unwind_info: 0x80
+  __DATA_CONST.__auth_got: 0x138
   __DATA_CONST.__got: 0x60
   __DATA_CONST.__const: 0x40
   __DATA_CONST.__cfstring: 0x1a0

   __DATA_CONST.__objc_intobj: 0x48
   __DATA.__objc_const: 0x40
   __DATA.__objc_selrefs: 0xf8
-  __DATA.__data: 0x18
+  __DATA.__data: 0x20
   __DATA.__bss: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/FeatureFlagsSupport.framework/FeatureFlagsSupport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: DC718B13-BDC8-371C-9404-76477F7F953A
-  Functions: 7
-  Symbols:   56
-  CStrings:  70
+  UUID: 9EB29413-4F1B-3AA8-AE0B-A1A1AB078030
+  Functions: 14
+  Symbols:   57
+  CStrings:  71
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
+ _objc_retain_x25
+ _objc_retain_x26
- _objc_claimAutoreleasedReturnValue
- _objc_retain
- _objc_retain_x21
CStrings:
+ "/System/Library/FeatureFlags/Unified"

```
