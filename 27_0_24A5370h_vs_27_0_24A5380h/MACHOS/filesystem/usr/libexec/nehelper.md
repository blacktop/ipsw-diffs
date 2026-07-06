## nehelper

> `/usr/libexec/nehelper`

```diff

-  __TEXT.__text: 0x24a70
-  __TEXT.__auth_stubs: 0x10a0
-  __TEXT.__objc_stubs: 0x2980
+  __TEXT.__text: 0x255e8
+  __TEXT.__auth_stubs: 0x10b0
+  __TEXT.__objc_stubs: 0x2a60
   __TEXT.__objc_methlist: 0x44c
   __TEXT.__const: 0x11c
   __TEXT.__gcc_except_tab: 0x7f8
-  __TEXT.__objc_methname: 0x1f5a
-  __TEXT.__cstring: 0x5f34
-  __TEXT.__oslogstring: 0x4a13
+  __TEXT.__objc_methname: 0x1f9c
+  __TEXT.__cstring: 0x5f44
+  __TEXT.__oslogstring: 0x4a97
   __TEXT.__objc_classname: 0x190
   __TEXT.__objc_methtype: 0x26e
-  __TEXT.__unwind_info: 0x3f0
-  __DATA_CONST.__const: 0xcb0
+  __TEXT.__unwind_info: 0x3e8
+  __DATA_CONST.__const: 0xd10
   __DATA_CONST.__cfstring: 0x51a0
   __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_protolist: 0x10

   __DATA_CONST.__objc_arraydata: 0x1350
   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_dictobj: 0x50
-  __DATA_CONST.__auth_got: 0x860
-  __DATA_CONST.__got: 0x398
+  __DATA_CONST.__auth_got: 0x868
+  __DATA_CONST.__got: 0x3b8
   __DATA_CONST.__auth_ptr: 0x8
   __DATA.__objc_const: 0x1788
-  __DATA.__objc_selrefs: 0xb00
+  __DATA.__objc_selrefs: 0xb38
   __DATA.__objc_ivar: 0xdc
   __DATA.__objc_data: 0x500
   __DATA.__data: 0xc8

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 245
-  Symbols:   380
-  CStrings:  2354
+  Functions: 247
+  Symbols:   382
+  CStrings:  2364
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__objc_arrayobj : content changed
~ __DATA_CONST.__objc_dictobj : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_data : content changed
~ __DATA.__data : content changed
Symbols:
+ _OBJC_CLASS_$_NSMutableData
+ ___NSDictionary0__struct
+ _qsort_b
- _OBJC_CLASS_$_NSPropertyListSerialization
CStrings:
+ "Failed to build the binary UUID cache"
+ "Failed to write the binary UUID cache to disk"
+ "allObjects"
+ "appendBytes:length:"
+ "appendData:"
+ "buildBinaryCacheFromDictionary: missing os-version or boot-uuid"
+ "buildBinaryCacheFromDictionary: total size %u exceeds MAX_CACHE_SIZE"
+ "data"
+ "dataWithCapacity:"
+ "i24@?0r^v8r^v16"
+ "mutableBytes"
+ "set"
+ "sortedArrayUsingSelector:"
- "Failed to serialize the cache plist: %@"
- "Failed to write the serialized cache to disk"
- "dataWithPropertyList:format:options:error:"

```
