## BackBoardHIDEventFoundation

> `/System/Library/PrivateFrameworks/BackBoardHIDEventFoundation.framework/BackBoardHIDEventFoundation`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift5_assocty`
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
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH.__data`

```diff

-868.0.0.0.0
-  __TEXT.__text: 0x3cdc4
-  __TEXT.__objc_methlist: 0x22c8
+873.100.0.0.0
+  __TEXT.__text: 0x3cf84
+  __TEXT.__objc_methlist: 0x22e8
   __TEXT.__const: 0x68c
   __TEXT.__constg_swiftt: 0x1b0
   __TEXT.__swift5_typeref: 0x225
   __TEXT.__swift5_reflstr: 0x12c
   __TEXT.__swift5_fieldmd: 0x1b0
   __TEXT.__swift5_builtin: 0x28
-  __TEXT.__cstring: 0x3392
+  __TEXT.__cstring: 0x33af
   __TEXT.__swift5_types: 0x24
   __TEXT.__swift5_proto: 0x24
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_assocty: 0x18
   __TEXT.__gcc_except_tab: 0x3bc
-  __TEXT.__oslogstring: 0x32e0
-  __TEXT.__unwind_info: 0xc28
+  __TEXT.__oslogstring: 0x3308
+  __TEXT.__unwind_info: 0xc30
   __TEXT.__eh_frame: 0x158
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x108
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1480
+  __DATA_CONST.__objc_selrefs: 0x14a0
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x118
   __DATA_CONST.__objc_arraydata: 0x290
-  __DATA_CONST.__got: 0x400
+  __DATA_CONST.__got: 0x408
   __AUTH_CONST.__const: 0xb58
   __AUTH_CONST.__cfstring: 0x2b40
-  __AUTH_CONST.__objc_const: 0x6098
+  __AUTH_CONST.__objc_const: 0x6100
   __AUTH_CONST.__objc_intobj: 0x3d8
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__auth_got: 0x8e8
-  __AUTH.__objc_data: 0x4f0
+  __AUTH.__objc_data: 0x400
   __AUTH.__data: 0x148
-  __DATA.__objc_ivar: 0x45c
-  __DATA.__data: 0xca0
+  __DATA.__objc_ivar: 0x468
+  __DATA.__data: 0xca8
   __DATA.__bss: 0x460
-  __DATA_DIRTY.__objc_data: 0xc80
+  __DATA_DIRTY.__objc_data: 0xd70
   __DATA_DIRTY.__data: 0x118
   __DATA_DIRTY.__bss: 0x1a0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1086
-  Symbols:   2886
-  CStrings:  686
+  Functions: 1089
+  Symbols:   2898
+  CStrings:  688
 
Symbols:
+ -[BKIOHIDServiceMatcher _notifyObserver:servicesDidMatch:]
+ -[BKIOHIDServiceMatcher setSessionID:]
+ -[BKIOHIDServicePersistentPropertyController unregisterHandler:]
+ GCC_except_table336
+ GCC_except_table394
+ GCC_except_table407
+ GCC_except_table410
+ GCC_except_table416
+ GCC_except_table419
+ GCC_except_table664
+ GCC_except_table667
+ GCC_except_table702
+ GCC_except_table751
+ GCC_except_table812
+ GCC_except_table824
+ GCC_except_table856
+ _OBJC_CLASS_$_NSMapTable
+ _OBJC_IVAR_$_BKIOHIDServiceMatcher._dataProviderSupportsSessionHoisting
+ _OBJC_IVAR_$_BKIOHIDServiceMatcher._matcherID
+ _OBJC_IVAR_$_BKIOHIDServiceMatcher._sessionID
+ __BKHIDServiceMatcherMap
+ __BKHIDServiceMatcherMapLock
+ __BKHIDServiceMatcherNextID
+ ___58-[BKIOHIDServiceMatcher _notifyObserver:servicesDidMatch:]_block_invoke
+ ___58-[BKIOHIDServiceMatcher _notifyObserver:servicesDidMatch:]_block_invoke_2
+ _objc_msgSend$hoistOnThread:forSessionID:
+ _objc_msgSend$mapTableWithKeyOptions:valueOptions:
- GCC_except_table334
- GCC_except_table392
- GCC_except_table405
- GCC_except_table408
- GCC_except_table414
- GCC_except_table417
- GCC_except_table662
- GCC_except_table665
- GCC_except_table699
- GCC_except_table748
- GCC_except_table809
- GCC_except_table821
- GCC_except_table853
- ___40-[BKIOHIDServiceMatcher _servicesAdded:]_block_invoke
- ___56-[BKIOHIDServiceMatcher _lock_asyncNotifyServicesAdded:]_block_invoke_2
CStrings:
+ "Matcher with ID %ld not found; ignoring"
+ "dealloc without invalidation matching %d invalidated %d"
+ "r"
- "dealloc without invalidation"
```
