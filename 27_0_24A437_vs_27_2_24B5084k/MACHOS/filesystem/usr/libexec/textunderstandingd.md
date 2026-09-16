## textunderstandingd

> `/usr/libexec/textunderstandingd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_entry`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_types`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`

```diff

-176.3.0.1.0
-  __TEXT.__text: 0x7fc
-  __TEXT.__auth_stubs: 0x2e0
+186.0.0.0.0
+  __TEXT.__text: 0xc8c
+  __TEXT.__auth_stubs: 0x3f0
   __TEXT.__objc_stubs: 0x160
   __TEXT.__objc_methlist: 0x1dc
-  __TEXT.__const: 0xba
+  __TEXT.__const: 0xc8
+  __TEXT.__objc_methtype: 0x18d
   __TEXT.__swift5_entry: 0x8
+  __TEXT.__swift5_typeref: 0x52
   __TEXT.__objc_classname: 0xdd
   __TEXT.__objc_methname: 0x31a
-  __TEXT.__objc_methtype: 0x17d
   __TEXT.__constg_swiftt: 0xb4
-  __TEXT.__swift5_typeref: 0x48
   __TEXT.__swift5_reflstr: 0x19
   __TEXT.__swift5_fieldmd: 0x50
   __TEXT.__swift5_capture: 0x10
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0xd8
-  __DATA_CONST.__const: 0xb0
+  __TEXT.__unwind_info: 0x108
+  __DATA_CONST.__const: 0xd8
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__auth_got: 0x178
-  __DATA_CONST.__got: 0x30
-  __DATA_CONST.__auth_ptr: 0x8
+  __DATA_CONST.__auth_got: 0x200
+  __DATA_CONST.__got: 0x60
+  __DATA_CONST.__auth_ptr: 0x18
   __DATA.__objc_const: 0x338
   __DATA.__objc_selrefs: 0x138
   __DATA.__objc_data: 0xd0
-  __DATA.__data: 0x1e0
-  __DATA.__common: 0x8
+  __DATA.__data: 0x210
+  __DATA.__common: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreSpotlight.framework/CoreSpotlight
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 29
-  Symbols:   63
-  CStrings:  72
+  Functions: 39
+  Symbols:   76
+  CStrings:  73
 
Symbols:
+ _OBJC_CLASS_$_OS_dispatch_queue
+ _OBJC_CLASS_$_OS_dispatch_source
+ __NSConcreteStackBlock
+ ___chkstk_darwin
+ __swiftEmptyArrayStorage
+ _exit
+ _objc_release_x27
+ _signal
+ _swift_getObjectType
+ _swift_getTypeByMangledNameInContext2
+ _swift_getTypeByMangledNameInContextInMetadataState2
+ _swift_getWitnessTable
+ _swift_retain_x2
CStrings:
+ "v8@?0"
```
