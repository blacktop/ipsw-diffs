## hpmdiagnose

> `/usr/bin/hpmdiagnose`

```diff

-624.100.15.0.0
-  __TEXT.__text: 0x10b94
-  __TEXT.__auth_stubs: 0x420
+647.0.0.0.0
+  __TEXT.__text: 0x1009c
+  __TEXT.__auth_stubs: 0x480
   __TEXT.__objc_stubs: 0x19e0
   __TEXT.__objc_methlist: 0xff0
-  __TEXT.__cstring: 0x1e71
+  __TEXT.__cstring: 0x1e80
   __TEXT.__const: 0x93
-  __TEXT.__objc_methname: 0x25a4
-  __TEXT.__objc_classname: 0xc4
+  __TEXT.__objc_methname: 0x25ac
+  __TEXT.__objc_classname: 0xb5
   __TEXT.__objc_methtype: 0x604
-  __TEXT.__unwind_info: 0x388
-  __DATA_CONST.__auth_got: 0x218
-  __DATA_CONST.__got: 0x78
+  __TEXT.__unwind_info: 0x328
   __DATA_CONST.__const: 0x68
   __DATA_CONST.__cfstring: 0x26a0
   __DATA_CONST.__objc_classlist: 0x50

   __DATA_CONST.__objc_arraydata: 0xe28
   __DATA_CONST.__objc_arrayobj: 0x348
   __DATA_CONST.__objc_dictobj: 0xed8
+  __DATA_CONST.__auth_got: 0x248
+  __DATA_CONST.__got: 0x78
   __DATA.__objc_const: 0xc88
   __DATA.__objc_selrefs: 0x948
   __DATA.__objc_ivar: 0x98

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0F767053-8788-31CD-B0C8-16CC9A86CDE5
+  UUID: DE0C9573-CE18-37AE-AA49-4A06EA8A5101
   Functions: 331
-  Symbols:   94
+  Symbols:   100
   CStrings:  1133
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x5
- _objc_retainAutoreleasedReturnValue
CStrings:
+ "initWithUnsignedChar:"
- "initWithChar:"

```
