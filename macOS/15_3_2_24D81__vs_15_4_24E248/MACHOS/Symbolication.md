## Symbolication

> `/System/Library/Trace/Providers/Symbolication.bundle/Contents/MacOS/Symbolication`

```diff

-65.2.0.0.0
-  __TEXT.__text: 0x85c
-  __TEXT.__auth_stubs: 0x180
-  __TEXT.__objc_stubs: 0x160
-  __TEXT.__objc_methlist: 0x74
-  __TEXT.__const: 0x50
-  __TEXT.__cstring: 0x4d5
-  __TEXT.__objc_methname: 0x281
+84.100.20.0.0
+  __TEXT.__text: 0xd38
+  __TEXT.__auth_stubs: 0x1b0
+  __TEXT.__objc_stubs: 0x180
+  __TEXT.__objc_methlist: 0x130
+  __TEXT.__const: 0x60
+  __TEXT.__gcc_except_tab: 0xa0
+  __TEXT.__cstring: 0x58d
+  __TEXT.__objc_methname: 0x2b5
   __TEXT.__objc_classname: 0x2a
-  __TEXT.__objc_methtype: 0x195
-  __TEXT.__unwind_info: 0x98
-  __DATA_CONST.__auth_got: 0xc8
-  __DATA_CONST.__got: 0x30
-  __DATA_CONST.__const: 0x38
-  __DATA_CONST.__cfstring: 0x340
+  __TEXT.__objc_methtype: 0x1a5
+  __TEXT.__unwind_info: 0xb0
+  __DATA_CONST.__auth_got: 0xe8
+  __DATA_CONST.__got: 0x38
+  __DATA_CONST.__const: 0x68
+  __DATA_CONST.__cfstring: 0x3a0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA.__objc_const: 0x2c0
-  __DATA.__objc_selrefs: 0xa0
-  __DATA.__objc_ivar: 0x8
+  __DATA.__objc_const: 0x180
+  __DATA.__objc_selrefs: 0xe0
+  __DATA.__objc_ivar: 0xc
   __DATA.__objc_data: 0x50
   __DATA.__data: 0x60
   __DATA.__bss: 0x8

   - /System/Library/PrivateFrameworks/ktrace.framework/Versions/A/ktrace
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6F5F0917-D240-30D1-9E00-6A7296FF0549
-  Functions: 13
-  Symbols:   47
-  CStrings:  101
+  UUID: 71AAE122-18B7-3710-8A25-51B47E180523
+  Functions: 18
+  Symbols:   52
+  CStrings:  111
 
Symbols:
+ __Block_object_assign
+ __Block_object_dispose
+ __NSConcreteStackBlock
+ __Unwind_Resume
+ ___objc_personality_v0
CStrings:
+ "@\"NSDictionary\""
+ "Unrecognized symbolication amend method option: %@"
+ "Unrecognized symbolication amend option key: %@"
+ "Unrecognized symbolication record option key: %@"
+ "Unrecognized symbolication record option: %@"
+ "_incomingOptions"
+ "enumerateKeysAndObjectsUsingBlock:"
+ "v32@?0@\"NSString\"8@\"NSString\"16^B24"
- "Unrecognized symbolication method option: %@"

```
