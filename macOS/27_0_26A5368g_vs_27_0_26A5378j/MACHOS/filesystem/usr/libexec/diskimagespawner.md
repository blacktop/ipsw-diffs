## diskimagespawner

> `/usr/libexec/diskimagespawner`

```diff

-  __TEXT.__text: 0x24fb8
+  __TEXT.__text: 0x24edc
   __TEXT.__auth_stubs: 0xa50
   __TEXT.__objc_stubs: 0x760
-  __TEXT.__objc_methlist: 0x43c
+  __TEXT.__objc_methlist: 0x424
   __TEXT.__const: 0x1897
-  __TEXT.__gcc_except_tab: 0x263c
+  __TEXT.__gcc_except_tab: 0x2638
   __TEXT.__cstring: 0x17ce
   __TEXT.__oslogstring: 0x837
   __TEXT.__objc_classname: 0x96
-  __TEXT.__objc_methname: 0xb3b
-  __TEXT.__objc_methtype: 0x4a8
+  __TEXT.__objc_methname: 0xae2
+  __TEXT.__objc_methtype: 0x491
   __TEXT.__unwind_info: 0x1340
   __DATA_CONST.__const: 0x35e8
   __DATA_CONST.__cfstring: 0x520

   __DATA_CONST.__got: 0x1a8
   __DATA_CONST.__auth_ptr: 0x8
   __DATA.__objc_const: 0x848
-  __DATA.__objc_selrefs: 0x378
+  __DATA.__objc_selrefs: 0x368
   __DATA.__objc_ivar: 0x10
   __DATA.__objc_data: 0x140
   __DATA.__data: 0x8a9

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 948
+  Functions: 946
   Symbols:   246
-  CStrings:  406
+  CStrings:  403
 
Sections:
~ __TEXT.__cstring : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_data : content changed
~ __DATA.__data : content changed
CStrings:
+ "errorWithDIException:prefix:error:"
+ "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.giQfGG/Sources/DiskImages2/app/backends/sg_vec.cpp:455:28)]"
+ "ssize_t transform(Fn &&, sg_vec_ref::iterator, const sg_vec_ref::iterator &, sg_vec_ref::iterator) [Fn = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.giQfGG/Sources/DiskImages2/app/utils.cpp:179:13)]"
- "@48@0:8r^v16@24@32^@40"
- "errorWithDIException:description:prefix:error:"
- "failWithDIException:description:error:"
- "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ZTSnA1/Sources/DiskImages2/app/backends/sg_vec.cpp:455:28)]"
- "nilWithDIException:description:error:"
- "ssize_t transform(Fn &&, sg_vec_ref::iterator, const sg_vec_ref::iterator &, sg_vec_ref::iterator) [Fn = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ZTSnA1/Sources/DiskImages2/app/utils.cpp:179:13)]"

```
