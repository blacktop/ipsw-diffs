## Dyld

> `/System/Library/PrivateFrameworks/Dyld.framework/Versions/A/Dyld`

```diff

-  __TEXT.__text: 0x54140
+  __TEXT.__text: 0x53eb0
   __TEXT.__objc_methlist: 0x6ac
-  __TEXT.__const: 0x3280
-  __TEXT.__swift5_typeref: 0xd2d
+  __TEXT.__const: 0x3250
+  __TEXT.__swift5_typeref: 0xcf7
   __TEXT.__swift5_fieldmd: 0x122c
   __TEXT.__constg_swiftt: 0xf38
-  __TEXT.__cstring: 0x1436
+  __TEXT.__cstring: 0x1499
   __TEXT.__swift5_builtin: 0xdc
   __TEXT.__swift5_mpenum: 0x70
   __TEXT.__swift5_reflstr: 0xe26

   __TEXT.__swift5_types2: 0x2c
   __TEXT.__swift5_capture: 0x90
   __TEXT.__gcc_except_tab: 0xa98
-  __TEXT.__unwind_info: 0x1130
+  __TEXT.__unwind_info: 0x1140
   __TEXT.__eh_frame: 0x1430
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x370
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__got: 0x258
+  __DATA_CONST.__got: 0x240
   __AUTH_CONST.__const: 0x2308
   __AUTH_CONST.__cfstring: 0x60
   __AUTH_CONST.__objc_const: 0x1b70
   __AUTH_CONST.__weak_auth_got: 0x10
-  __AUTH_CONST.__auth_got: 0xa10
+  __AUTH_CONST.__auth_got: 0xa08
   __AUTH.__objc_data: 0x640
-  __AUTH.__data: 0x1658
-  __DATA.__data: 0xb50
+  __AUTH.__data: 0x1648
+  __DATA.__data: 0xb08
   __DATA.__crash_info: 0x148
   __DATA.__bss: 0x3010
   __DATA.__common: 0x60

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 1473
-  Symbols:   1139
-  CStrings:  172
+  Functions: 1466
+  Symbols:   1132
+  CStrings:  176
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__swift5_fieldmd : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_builtin : content changed
~ __TEXT.__swift5_mpenum : content changed
~ __TEXT.__swift5_assocty : content changed
~ __TEXT.__swift5_protos : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift5_types : content changed
~ __TEXT.__swift5_types2 : content changed
~ __TEXT.__swift5_capture : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__weak_auth_got : content changed
~ __AUTH.__objc_data : content changed
Symbols:
+ __ZNSt3__119__allocate_at_leastB9fqn220106INS_9allocatorIjEENS_16allocator_traitsIS2_EEEENS_19__allocation_resultINT0_7pointerENS6_9size_typeEEERT_m
+ __ZNSt3__16vectorIjNS_9allocatorIjEEE20__throw_length_errorB9fqn220106Ev
+ __ZNSt3__16vectorIjNS_9allocatorIjEEE24__emplace_back_slow_pathIJRKjEEEPjDpOT_
+ _task_resume2
+ _task_suspend2
+ _thread_resume2
+ _thread_suspend2
- _swift_runtimeSupportsNoncopyableTypes
- _task_resume
- _task_suspend
- _thread_resume
- _thread_suspend
- get_type_metadata 4Dyld10DeferrableOyAA11EnvironmentV4InfoVG noncopyable
- get_type_metadata 4Dyld10DeferrableOyAA11SharedCacheV13ProcessRecordV4InfoVG noncopyable
- get_type_metadata 4Dyld10DeferrableOyAA11SharedCacheV4InfoVG noncopyable
- get_type_metadata 4Dyld10DeferrableOyAA5ImageV4InfoVG noncopyable
- get_type_metadata 4Dyld10DeferrableOyAA7SegmentV4InfoVG noncopyable
- get_type_metadata 4Dyld10DeferrableOyAA8AOTImageV4InfoVG noncopyable
- get_type_metadata 4Dyld10DeferrableOyAA8SnapshotV4InfoVG noncopyable
- get_type_metadata 4Dyld10DeferrableOyAA8SubCacheV4InfoVG noncopyable
- get_type_metadata 4Dyld8MachTaskV noncopyable
CStrings:
+ "/Library/Developer/CoreSimulator/Caches/dyld/"
+ "ProcessScavenger.cpp"
+ "TaskSuspender"
+ "threadCount > 0"

```
