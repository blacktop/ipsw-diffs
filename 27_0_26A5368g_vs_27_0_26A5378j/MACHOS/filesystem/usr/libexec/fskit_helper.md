## fskit_helper

> `/usr/libexec/fskit_helper`

```diff

-  __TEXT.__text: 0x1604
-  __TEXT.__auth_stubs: 0x210
-  __TEXT.__objc_stubs: 0x300
-  __TEXT.__objc_methlist: 0x1ac
-  __TEXT.__cstring: 0x161
+  __TEXT.__text: 0x175c
+  __TEXT.__auth_stubs: 0x220
+  __TEXT.__objc_stubs: 0x340
+  __TEXT.__objc_methlist: 0x1b4
+  __TEXT.__cstring: 0x180
   __TEXT.__objc_classname: 0x53
-  __TEXT.__objc_methname: 0x365
-  __TEXT.__objc_methtype: 0x1b1
-  __TEXT.__oslogstring: 0x364
+  __TEXT.__objc_methname: 0x397
+  __TEXT.__objc_methtype: 0x1c3
+  __TEXT.__oslogstring: 0x3a1
   __TEXT.__gcc_except_tab: 0x34
-  __TEXT.__const: 0x50
+  __TEXT.__const: 0x58
   __TEXT.__unwind_info: 0xd0
   __DATA_CONST.__const: 0x60
   __DATA_CONST.__cfstring: 0x60

   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__auth_got: 0x118
-  __DATA_CONST.__got: 0x48
+  __DATA_CONST.__auth_got: 0x120
+  __DATA_CONST.__got: 0x50
   __DATA.__objc_const: 0x2b8
-  __DATA.__objc_selrefs: 0x180
+  __DATA.__objc_selrefs: 0x190
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0x120
   __DATA.__common: 0x8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  Functions: 31
-  Symbols:   50
-  CStrings:  112
+  Functions: 32
+  Symbols:   52
+  CStrings:  118
 
Sections:
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_data : content changed
~ __DATA.__data : content changed
Symbols:
+ _SANDBOX_CHECK_CANONICAL
+ _sandbox_check_by_audit_token
CStrings:
+ "FSKitHelper: sandbox denied %{public}s on %{public}s (rv=%d)"
+ "audit_token"
+ "file-read-data"
+ "file-write-data"
+ "i36@0:8@16r*24B32"
+ "sandboxCheckAuditToken:path:writable:"

```
