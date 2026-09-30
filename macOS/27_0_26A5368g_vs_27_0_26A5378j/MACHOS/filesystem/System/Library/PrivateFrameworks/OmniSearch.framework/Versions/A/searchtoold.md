## searchtoold

> `/System/Library/PrivateFrameworks/OmniSearch.framework/Versions/A/searchtoold`

```diff

-  __TEXT.__text: 0x5a4
-  __TEXT.__auth_stubs: 0x190
+  __TEXT.__text: 0x1b6c
+  __TEXT.__auth_stubs: 0x400
   __TEXT.__objc_stubs: 0x40
-  __TEXT.__const: 0x5a
-  __TEXT.__swift5_typeref: 0x21
-  __TEXT.__oslogstring: 0x24
+  __TEXT.__const: 0x98
+  __TEXT.__swift5_typeref: 0x61
+  __TEXT.__oslogstring: 0xc0
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__cstring: 0x1
+  __TEXT.__cstring: 0x61
   __TEXT.__objc_methname: 0x10
-  __TEXT.__unwind_info: 0x70
-  __DATA_CONST.__const: 0xd8
+  __TEXT.__unwind_info: 0xd0
+  __TEXT.__eh_frame: 0x70
+  __DATA_CONST.__const: 0x100
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0xd0
-  __DATA_CONST.__got: 0x48
-  __DATA_CONST.__auth_ptr: 0x20
+  __DATA_CONST.__auth_got: 0x208
+  __DATA_CONST.__got: 0x70
+  __DATA_CONST.__auth_ptr: 0x40
   __DATA.__objc_selrefs: 0x10
-  __DATA.__data: 0x38
+  __DATA.__data: 0x78
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/PrivateFrameworks/OmniSearch.framework/Versions/A/OmniSearch

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 6
-  Symbols:   48
-  CStrings:  3
+  Functions: 35
+  Symbols:   77
+  CStrings:  9
 
Sections:
~ __TEXT.__swift5_entry : content changed
~ __DATA.__objc_selrefs : content changed
Symbols:
+ _NSHomeDirectory
+ ___stack_chk_fail
+ ___stack_chk_guard
+ __set_user_dir_suffix
+ __swiftEmptyArrayStorage
+ __swiftImmortalRefCount
+ _bzero
+ _confstr
+ _exit
+ _free
+ _malloc_size
+ _memcpy
+ _memmove
+ _realpath$DARWIN_EXTSN
+ _sandbox_free_error
+ _sandbox_init_with_parameters
+ _strdup
+ _swift_allocObject
+ _swift_arrayDestroy
+ _swift_bridgeObjectRelease_n
+ _swift_bridgeObjectRetain
+ _swift_deallocClassInstance
+ _swift_getObjectType
+ _swift_initStackObject
+ _swift_isUniquelyReferenced_nonNull_native
+ _swift_once
+ _swift_release
+ _swift_setDeallocating
+ _swift_unknownObjectRetain
Functions:
~ _main : 1140 -> 1232
CStrings:
+ "/private/var/empty"
+ "DARWIN_CACHE_DIR"
+ "[sandbox] _set_user_dir_suffix failed; aborting"
+ "[sandbox] entered profile: %s"
+ "[sandbox] sandbox_init_with_parameters failed: %s"
+ "com.apple.omniSearch.searchtoold"

```
