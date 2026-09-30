## BackupAgent2

> `/usr/libexec/BackupAgent2`

```diff

-  __TEXT.__text: 0x90610
+  __TEXT.__text: 0x907ec
   __TEXT.__auth_stubs: 0x1850
-  __TEXT.__objc_stubs: 0xc960
-  __TEXT.__objc_methlist: 0x5fe4
+  __TEXT.__objc_stubs: 0xc9a0
+  __TEXT.__objc_methlist: 0x5ffc
   __TEXT.__const: 0x4b8
-  __TEXT.__cstring: 0x18eab
-  __TEXT.__oslogstring: 0xde9d
-  __TEXT.__objc_methname: 0xe7ac
+  __TEXT.__cstring: 0x18eed
+  __TEXT.__oslogstring: 0xdeda
+  __TEXT.__objc_methname: 0xe7e3
   __TEXT.__objc_classname: 0xa09
   __TEXT.__objc_methtype: 0x1e9d
-  __TEXT.__gcc_except_tab: 0x2118
-  __TEXT.__unwind_info: 0x1940
+  __TEXT.__gcc_except_tab: 0x2100
+  __TEXT.__unwind_info: 0x1948
   __DATA_CONST.__const: 0x1418
   __DATA_CONST.__cfstring: 0x94e0
   __DATA_CONST.__objc_classlist: 0x388

   __DATA_CONST.__objc_arrayobj: 0xd8
   __DATA_CONST.__objc_dictobj: 0x78
   __DATA_CONST.__auth_got: 0xc38
-  __DATA_CONST.__got: 0x4e0
+  __DATA_CONST.__got: 0x588
   __DATA_CONST.__auth_ptr: 0x18
   __DATA.__objc_const: 0x99f0
-  __DATA.__objc_selrefs: 0x3c98
+  __DATA.__objc_selrefs: 0x3ca8
   __DATA.__objc_ivar: 0x558
   __DATA.__objc_data: 0x2350
   __DATA.__data: 0x818

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 2450
+  Functions: 2452
   Symbols:   558
-  CStrings:  8247
+  CStrings:  8251
 
Sections:
~ __TEXT.__const : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_data : content changed
~ __DATA.__data : content changed
Functions:
~ sub_100042450 : 512 -> 552
- sub_1000457d0
+ sub_100045ae4
+ sub_10006cf40
+ sub_10006e300
CStrings:
+ "=pqldb= Unexpected open success when creating empty DB at %@"
+ "Failed to create SQLite database"
+ "_isSQLiteCannotOpenError"
+ "mb_openAtURL:withFlags:error:"
- "Can't find the database: %@"

```
