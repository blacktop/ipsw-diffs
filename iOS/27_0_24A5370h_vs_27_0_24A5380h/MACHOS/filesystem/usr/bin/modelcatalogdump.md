## modelcatalogdump

> `/usr/bin/modelcatalogdump`

```diff

-  __TEXT.__text: 0x16048
-  __TEXT.__auth_stubs: 0x1090
+  __TEXT.__text: 0x18694
+  __TEXT.__auth_stubs: 0x11e0
   __TEXT.__objc_stubs: 0x120
-  __TEXT.__const: 0x59c
+  __TEXT.__const: 0x5d4
   __TEXT.__swift5_entry: 0x8
   __TEXT.__constg_swiftt: 0xa0
-  __TEXT.__swift5_typeref: 0x3a1
-  __TEXT.__swift5_fieldmd: 0x78
-  __TEXT.__cstring: 0x5c6
+  __TEXT.__swift5_typeref: 0x3d1
+  __TEXT.__swift5_fieldmd: 0xc0
+  __TEXT.__cstring: 0x922
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_proto: 0x34
   __TEXT.__swift5_types: 0x10

   __TEXT.__swift_as_cont: 0x68
   __TEXT.__swift5_capture: 0x30
   __TEXT.__objc_methtype: 0xf
-  __TEXT.__swift5_reflstr: 0x2d
+  __TEXT.__swift5_reflstr: 0x70
   __TEXT.__objc_methname: 0x9e
-  __TEXT.__unwind_info: 0x4e8
-  __TEXT.__eh_frame: 0xe98
+  __TEXT.__unwind_info: 0x528
+  __TEXT.__eh_frame: 0xef8
   __DATA_CONST.__const: 0x3c0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0x850
-  __DATA_CONST.__got: 0x188
-  __DATA_CONST.__auth_ptr: 0x208
+  __DATA_CONST.__auth_got: 0x8f8
+  __DATA_CONST.__got: 0x198
+  __DATA_CONST.__auth_ptr: 0x220
   __DATA.__objc_selrefs: 0x48
-  __DATA.__data: 0x330
+  __DATA.__data: 0x378
   __DATA.__bss: 0x680
   __DATA.__common: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 448
-  Symbols:   119
-  CStrings:  43
+  Functions: 520
+  Symbols:   124
+  CStrings:  53
 
Sections:
~ __TEXT.__swift5_entry : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_builtin : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift5_types : content changed
~ __TEXT.__swift_as_entry : content changed
~ __TEXT.__swift_as_ret : content changed
~ __TEXT.__swift_as_cont : content changed
~ __TEXT.__swift5_capture : content changed
~ __DATA_CONST.__const : content changed
~ __DATA.__objc_selrefs : content changed
Symbols:
+ _objc_retain_x26
+ _swift_allocError
+ _swift_arrayDestroy
+ _swift_deallocClassInstance
+ _swift_release_x28
+ _swift_setDeallocating
+ _swift_willThrow
- _objc_retain_x25
- _swift_willThrowTypedImpl
CStrings:
+ " found, but no backing resources are present in the catalog"
+ " found, but none of its resources are present in the catalog"
+ "--resource, --resource-bundle, and --use-case are mutually exclusive"
+ "No resource bundle found with identifier: "
+ "No resource found with identifier: "
+ "Resource bundle "
+ "The identifier of the resource bundle. When provided, only the statuses of resources in this bundle are printed (skips device, use-case, and coherence sections)."
+ "The identifier of the resource. When provided, only this resource's status is printed (skips device, use-case, and coherence sections)."
+ "The identifier of the use case. When provided, only the statuses of resources backing this use case are printed (skips device, use-case, and coherence sections)."
+ "Unknown use case identifier: "

```
