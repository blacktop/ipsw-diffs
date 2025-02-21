## Symbolication

> `/System/Library/Trace/Providers/Symbolication.bundle/Symbolication`

```diff

-65.2.0.0.0
-  __TEXT.__text: 0x4d8
-  __TEXT.__auth_stubs: 0x170
-  __TEXT.__objc_stubs: 0x120
-  __TEXT.__objc_methlist: 0x74
-  __TEXT.__const: 0x50
-  __TEXT.__cstring: 0x121
-  __TEXT.__objc_methname: 0x260
+84.100.16.0.0
+  __TEXT.__text: 0x5d4
+  __TEXT.__auth_stubs: 0x190
+  __TEXT.__objc_stubs: 0x100
+  __TEXT.__objc_methlist: 0x130
+  __TEXT.__const: 0x58
+  __TEXT.__gcc_except_tab: 0x28
+  __TEXT.__cstring: 0x176
+  __TEXT.__objc_methname: 0x282
   __TEXT.__objc_classname: 0x2a
-  __TEXT.__objc_methtype: 0x195
-  __TEXT.__unwind_info: 0x88
-  __DATA_CONST.__auth_got: 0xc0
-  __DATA_CONST.__got: 0x28
-  __DATA_CONST.__const: 0x38
-  __DATA_CONST.__cfstring: 0x160
+  __TEXT.__objc_methtype: 0x1a5
+  __TEXT.__unwind_info: 0x98
+  __DATA_CONST.__auth_got: 0xd8
+  __DATA_CONST.__got: 0x30
+  __DATA_CONST.__const: 0x60
+  __DATA_CONST.__cfstring: 0x180
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA.__objc_const: 0x2c0
-  __DATA.__objc_selrefs: 0x90
-  __DATA.__objc_ivar: 0x8
+  __DATA.__objc_const: 0x180
+  __DATA.__objc_selrefs: 0xc0
+  __DATA.__objc_ivar: 0xc
   __DATA.__objc_data: 0x50
   __DATA.__data: 0x60
   __DATA.__bss: 0x8

   - /System/Library/PrivateFrameworks/ktrace.framework/ktrace
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 12
-  Symbols:   45
-  CStrings:  57
+  Functions: 15
+  Symbols:   49
+  CStrings:  60
 
Symbols:
+ __Block_object_dispose
+ __NSConcreteStackBlock
+ __Unwind_Resume
+ ___objc_personality_v0
+ _objc_release_x22
+ _objc_release_x8
+ _objc_retain_x19
+ _objc_retain_x2
+ _objc_retain_x21
- _objc_release_x19
- _objc_release_x23
- _objc_release_x24
- _objc_retainAutorelease
- _objc_retain_x24
CStrings:
+ "\x12"
+ "@\"NSDictionary\""
+ "Unrecognized symbolication record option key: %@"
+ "Unrecognized symbolication record option: %@"
+ "_incomingOptions"
+ "enumerateKeysAndObjectsUsingBlock:"
+ "v32@?0@\"NSString\"8@\"NSString\"16^B24"
- "\x11"
- "UTF8String"
- "Unrecognized symbolication method option: %@"
- "length"

```
