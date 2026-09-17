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
-  __TEXT.__text: 0xb34
-  __TEXT.__auth_stubs: 0x2e0
+186.0.0.0.0
+  __TEXT.__text: 0xfc0
+  __TEXT.__auth_stubs: 0x3c0
   __TEXT.__objc_stubs: 0x160
   __TEXT.__objc_methlist: 0x1ac
-  __TEXT.__const: 0xd0
+  __TEXT.__const: 0xd8
+  __TEXT.__objc_methtype: 0x19d
   __TEXT.__swift5_entry: 0x8
+  __TEXT.__swift5_typeref: 0x52
   __TEXT.__objc_classname: 0xdd
   __TEXT.__objc_methname: 0x2e7
-  __TEXT.__objc_methtype: 0x18d
   __TEXT.__constg_swiftt: 0xa4
-  __TEXT.__swift5_typeref: 0x48
   __TEXT.__swift5_reflstr: 0x19
   __TEXT.__swift5_fieldmd: 0x50
   __TEXT.__swift5_capture: 0x10
   __TEXT.__swift5_types: 0x8
   __TEXT.__cstring: 0x3a
   __TEXT.__oslogstring: 0x190
-  __TEXT.__unwind_info: 0xc8
-  __DATA_CONST.__const: 0xb8
+  __TEXT.__unwind_info: 0xf8
+  __DATA_CONST.__const: 0xe0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__auth_got: 0x178
-  __DATA_CONST.__got: 0x40
-  __DATA_CONST.__auth_ptr: 0x8
+  __DATA_CONST.__auth_got: 0x1e8
+  __DATA_CONST.__got: 0x70
+  __DATA_CONST.__auth_ptr: 0x18
   __DATA.__objc_const: 0x328
   __DATA.__objc_selrefs: 0x128
   __DATA.__objc_data: 0xd0
-  __DATA.__data: 0x1d0
-  __DATA.__common: 0x8
+  __DATA.__data: 0x200
+  __DATA.__common: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreSpotlight.framework/Versions/A/CoreSpotlight
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 25
-  Symbols:   69
-  CStrings:  82
+  Functions: 35
+  Symbols:   79
+  CStrings:  83
 
Symbols:
+ _OBJC_CLASS_$_OS_dispatch_queue
+ _OBJC_CLASS_$_OS_dispatch_source
+ __NSConcreteStackBlock
+ ___chkstk_darwin
+ __swiftEmptyArrayStorage
+ _signal
+ _swift_getObjectType
+ _swift_getTypeByMangledNameInContext2
+ _swift_getTypeByMangledNameInContextInMetadataState2
+ _swift_getWitnessTable
CStrings:
+ "v8@?0"
```
