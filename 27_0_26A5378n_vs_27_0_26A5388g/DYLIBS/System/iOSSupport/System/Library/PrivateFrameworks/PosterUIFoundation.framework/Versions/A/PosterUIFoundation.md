## PosterUIFoundation

> `/System/iOSSupport/System/Library/PrivateFrameworks/PosterUIFoundation.framework/Versions/A/PosterUIFoundation`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_floatobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__objc_ivar`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-347.100.0.0.0
-  __TEXT.__text: 0x93234
-  __TEXT.__objc_methlist: 0xaaec
+350.1.0.0.0
+  __TEXT.__text: 0x93660
+  __TEXT.__objc_methlist: 0xab14
   __TEXT.__const: 0xdc4
-  __TEXT.__oslogstring: 0x38c1
-  __TEXT.__cstring: 0x6553
+  __TEXT.__oslogstring: 0x3921
+  __TEXT.__cstring: 0x6593
   __TEXT.__gcc_except_tab: 0x163c
   __TEXT.__dlopen_cstrs: 0x1c0
   __TEXT.__swift5_typeref: 0x7f2

   __TEXT.__swift5_proto: 0x28
   __TEXT.__swift5_types: 0x2c
   __TEXT.__swift5_capture: 0x30
-  __TEXT.__unwind_info: 0x2878
+  __TEXT.__unwind_info: 0x2890
   __TEXT.__eh_frame: 0x40
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0xe0
   __DATA_CONST.__objc_protolist: 0x1c0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5890
+  __DATA_CONST.__objc_selrefs: 0x58b0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x410
   __DATA_CONST.__objc_arraydata: 0x18e0
-  __DATA_CONST.__got: 0xf38
+  __DATA_CONST.__got: 0xf48
   __AUTH_CONST.__const: 0x10c0
   __AUTH_CONST.__cfstring: 0x7ea0
   __AUTH_CONST.__objc_const: 0x1e9a8
   __AUTH_CONST.__objc_dictobj: 0xcf8
-  __AUTH_CONST.__objc_intobj: 0xd98
+  __AUTH_CONST.__objc_intobj: 0xdb0
   __AUTH_CONST.__objc_doubleobj: 0x2b0
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_floatobj: 0x10

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 4126
-  Symbols:   9673
-  CStrings:  1484
+  Functions: 4131
+  Symbols:   9679
+  CStrings:  1486
 
Symbols:
+ -[PUIPosterSnapshotter consecutiveStartupFailuresForTesting]
+ -[PUIPosterSnapshotter setConsecutiveStartupFailuresForTesting:]
+ -[PUIStylePickerHomeScreenItemView _compositingFilterNameForCurrentStyle]
+ __68-[PUIPosterSnapshotBundlePredicate(SQLiteAdditions) SQLitePredicate]_block_invoke_2
+ __68-[PUIPosterSnapshotBundlePredicate(SQLiteAdditions) SQLitePredicate]_block_invoke_3
+ _kCAFilterClearIconBlendMode
+ _kCAFilterScreenBlendMode
+ _objc_msgSend$_compositingFilterNameForCurrentStyle
+ _objc_msgSend$setAllowsColorMatching:
+ _objc_msgSend$setBackground:
- ___68-[PUIPosterSnapshotBundlePredicate(SQLiteAdditions) SQLitePredicate]_block_invoke_6
- ___68-[PUIPosterSnapshotBundlePredicate(SQLiteAdditions) SQLitePredicate]_block_invoke_7
- ___68-[PUIPosterSnapshotBundlePredicate(SQLiteAdditions) SQLitePredicate]_block_invoke_8
- _objc_msgSend$ICRIconLayer
CStrings:
+ "(%{public}@) Booted extension process is invalid (no error) — treating as a startup failure"
+ "(%{public}@) Exceeded %lu consecutive mid-snapshot interruptions, giving up"
+ "-[PUIPosterSnapshotter setConsecutiveStartupFailuresForTesting:]"
- "(%{public}@) Booted extension process is invalid but there was no error!"
```
