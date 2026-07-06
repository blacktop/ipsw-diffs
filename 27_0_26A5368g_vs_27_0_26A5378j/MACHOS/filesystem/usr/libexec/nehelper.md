## nehelper

> `/usr/libexec/nehelper`

```diff

-  __TEXT.__text: 0x22874
-  __TEXT.__auth_stubs: 0xe00
+  __TEXT.__text: 0x23448
+  __TEXT.__auth_stubs: 0xe10
   __TEXT.__delay_helper: 0xdc
-  __TEXT.__objc_stubs: 0x2360
+  __TEXT.__objc_stubs: 0x2440
   __TEXT.__objc_methlist: 0x44c
   __TEXT.__const: 0x12c
   __TEXT.__gcc_except_tab: 0x8e8
-  __TEXT.__objc_methname: 0x1c88
-  __TEXT.__cstring: 0x3382
-  __TEXT.__oslogstring: 0x4094
+  __TEXT.__objc_methname: 0x1cca
+  __TEXT.__cstring: 0x3392
+  __TEXT.__oslogstring: 0x4118
   __TEXT.__objc_classname: 0x190
   __TEXT.__objc_methtype: 0x280
   __TEXT.__unwind_info: 0x3f0
-  __DATA_CONST.__const: 0xd00
+  __DATA_CONST.__const: 0xd60
   __DATA_CONST.__cfstring: 0x23e0
   __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_protolist: 0x10

   __DATA_CONST.__objc_arraydata: 0x610
   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_dictobj: 0x50
-  __DATA_CONST.__auth_got: 0x710
-  __DATA_CONST.__got: 0x298
+  __DATA_CONST.__auth_got: 0x718
+  __DATA_CONST.__got: 0x2b0
   __DATA.__objc_const: 0x17c8
-  __DATA.__objc_selrefs: 0x978
+  __DATA.__objc_selrefs: 0x9b0
   __DATA.__objc_ivar: 0xe4
   __DATA.__objc_data: 0x500
   __DATA.__data: 0xcc

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 244
-  Symbols:   305
-  CStrings:  1542
+  Functions: 246
+  Symbols:   307
+  CStrings:  1552
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
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
