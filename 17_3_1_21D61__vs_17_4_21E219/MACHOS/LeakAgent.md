## LeakAgent

> `/System/Library/PrivateFrameworks/DVTInstrumentsFoundation.framework/LeakAgent`

```diff

-64562.3.1.1.0
-  __TEXT.__text: 0x2f0c
-  __TEXT.__auth_stubs: 0x4e0
-  __TEXT.__objc_stubs: 0xb60
-  __TEXT.__objc_methlist: 0x5c
+64565.70.2.0.0
+  __TEXT.__text: 0x2fb0
+  __TEXT.__auth_stubs: 0x4f0
+  __TEXT.__objc_stubs: 0xbe0
+  __TEXT.__objc_methlist: 0x68
   __TEXT.__const: 0x68
-  __TEXT.__gcc_except_tab: 0x2d8
-  __TEXT.__objc_methname: 0x9a3
-  __TEXT.__cstring: 0x3b5
-  __TEXT.__oslogstring: 0x38d
+  __TEXT.__gcc_except_tab: 0x2c0
+  __TEXT.__objc_methname: 0xa27
+  __TEXT.__cstring: 0x524
+  __TEXT.__oslogstring: 0x353
   __TEXT.__objc_classname: 0x35
   __TEXT.__objc_methtype: 0x1a6
-  __TEXT.__unwind_info: 0xc8
-  __DATA_CONST.__auth_got: 0x280
+  __TEXT.__unwind_info: 0xcc
+  __DATA_CONST.__auth_got: 0x288
   __DATA_CONST.__got: 0x30
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x180
-  __DATA_CONST.__cfstring: 0x380
+  __DATA_CONST.__cfstring: 0x460
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_classrefs: 0xb8
+  __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_intobj: 0x18
   __DATA_CONST.__objc_arraydata: 0x60
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA.__objc_const: 0x4c8
-  __DATA.__objc_selrefs: 0x300
-  __DATA.__objc_classrefs: 0xb8
-  __DATA.__objc_superrefs: 0x8
+  __DATA.__objc_selrefs: 0x320
   __DATA.__objc_ivar: 0xc
   __DATA.__objc_data: 0x50
   __DATA.__data: 0x120

   - /System/Library/PrivateFrameworks/Symbolication.framework/Symbolication
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1C88215C-5B3E-3BB9-9433-65F792361F22
-  Functions: 21
-  Symbols:   121
-  CStrings:  255
+  UUID: 43066965-7504-3E52-91BB-7A582C9295A5
+  Functions: 22
+  Symbols:   122
+  CStrings:  272
 
Symbols:
+ _objc_retain_x22
+ _objc_retain_x28
- _objc_retain_x25
CStrings:
+ "Failed to generate memory graph for pid %u: %@"
+ "T@\"NSString\",?,R,C"
+ "failed to add nodes to VMUTaskMemoryScanner with the error \"%@\""
+ "failed to collect full disk stack logs with the error \"%@\""
+ "failed to create a VMUTaskMemoryScanner, probably because the target's libmalloc hasn't been initialized"
+ "failed to generate corpse: %#x - %s"
+ "initWithDomain:code:userInfo:"
+ "initWithFormat:"
+ "initWithFormat:arguments:"
+ "logAndGenerateReceiptForErrorWithFormat:"
+ "no valid task available"
+ "target process no longer exists"
- "failed to generate a corpse for pid %u (task: %#x): %#x - %s"
- "target process %u (%#x) no longer exists"

```
