## security-sysdiagnose

> `/usr/libexec/security-sysdiagnose`

```diff

-61901.120.56.0.1
-  __TEXT.__text: 0x3e2c
-  __TEXT.__auth_stubs: 0x800
+61901.120.60.0.0
+  __TEXT.__text: 0x3f70
+  __TEXT.__auth_stubs: 0x7f0
   __TEXT.__objc_stubs: 0x520
   __TEXT.__objc_methlist: 0xd0
   __TEXT.__const: 0x70

   __TEXT.__objc_classname: 0x3d
   __TEXT.__objc_methname: 0x411
   __TEXT.__objc_methtype: 0x17e
-  __TEXT.__cstring: 0xea7
+  __TEXT.__cstring: 0xeb3
   __TEXT.__oslogstring: 0xa8
   __TEXT.__unwind_info: 0x100
-  __DATA_CONST.__auth_got: 0x410
-  __DATA_CONST.__got: 0x118
+  __DATA_CONST.__auth_got: 0x408
+  __DATA_CONST.__got: 0x120
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x310
-  __DATA_CONST.__cfstring: 0xc80
+  __DATA_CONST.__cfstring: 0xc60
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 97A48AF8-8B98-3A55-B72A-2FF955911CEF
+  UUID: D539A69B-EC28-366D-82AE-C8E5A12312DA
   Functions: 34
   Symbols:   175
-  CStrings:  309
+  CStrings:  308
 
Symbols:
+ _CFStringCreateWithBytesNoCopy
+ _kCFAllocatorMalloc
- _CFStringAppendFormat
- _CFStringCreateMutable
Functions:
~ sub_1000012d0 : 172 -> 264
~ sub_1000033bc -> sub_100003418 : 724 -> 840
~ sub_1000045bc -> sub_10000468c : 476 -> 592
CStrings:
+ "0123456789ABCDEF"
- "%02X"

```
