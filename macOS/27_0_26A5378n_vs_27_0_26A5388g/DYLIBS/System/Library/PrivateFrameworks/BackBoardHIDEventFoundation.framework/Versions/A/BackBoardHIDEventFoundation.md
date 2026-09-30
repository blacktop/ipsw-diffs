## BackBoardHIDEventFoundation

> `/System/Library/PrivateFrameworks/BackBoardHIDEventFoundation.framework/Versions/A/BackBoardHIDEventFoundation`

### Sections with Same Size but Changed Content

- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_builtin`
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
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__DATA_DIRTY.__data`

```diff

-868.0.0.0.0
-  __TEXT.__text: 0x44218
-  __TEXT.__objc_methlist: 0x23a0
-  __TEXT.__const: 0x68c
+873.200.0.0.0
+  __TEXT.__text: 0x44374
+  __TEXT.__objc_methlist: 0x23c0
+  __TEXT.__const: 0x694
   __TEXT.__constg_swiftt: 0x1b0
   __TEXT.__swift5_typeref: 0x225
   __TEXT.__swift5_reflstr: 0x12c
   __TEXT.__swift5_fieldmd: 0x1bc
   __TEXT.__swift5_builtin: 0x28
-  __TEXT.__cstring: 0x33d6
+  __TEXT.__cstring: 0x33bb
   __TEXT.__swift5_types: 0x24
   __TEXT.__swift5_proto: 0x24
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_assocty: 0x18
   __TEXT.__gcc_except_tab: 0x4a0
-  __TEXT.__oslogstring: 0x3350
-  __TEXT.__unwind_info: 0xc20
+  __TEXT.__oslogstring: 0x33b0
+  __TEXT.__unwind_info: 0xc18
   __TEXT.__eh_frame: 0x158
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x108
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1520
+  __DATA_CONST.__objc_selrefs: 0x1540
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x120
   __DATA_CONST.__objc_arraydata: 0x290
-  __DATA_CONST.__got: 0x430
+  __DATA_CONST.__got: 0x438
   __AUTH_CONST.__const: 0x1e48
-  __AUTH_CONST.__cfstring: 0x2bc0
-  __AUTH_CONST.__objc_const: 0x6280
+  __AUTH_CONST.__cfstring: 0x2ba0
+  __AUTH_CONST.__objc_const: 0x62e8
   __AUTH_CONST.__objc_intobj: 0x3d8
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__auth_got: 0x758
-  __AUTH.__objc_data: 0x2c0
-  __DATA.__objc_ivar: 0x484
-  __DATA.__data: 0xca0
+  __AUTH_CONST.__auth_got: 0x760
+  __AUTH.__objc_data: 0x1d0
+  __DATA.__objc_ivar: 0x490
+  __DATA.__data: 0xca8
   __DATA.__bss: 0x460
-  __DATA_DIRTY.__objc_data: 0xf00
+  __DATA_DIRTY.__objc_data: 0xff0
   __DATA_DIRTY.__data: 0x260
   __DATA_DIRTY.__bss: 0x1a8
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1147
-  Symbols:   2944
-  CStrings:  699
+  Functions: 1150
+  Symbols:   2957
+  CStrings:  701
 
Symbols:
+ -[BKIOHIDServiceMatcher _notifyObserver:servicesDidMatch:]
+ -[BKIOHIDServiceMatcher setSessionID:]
+ -[BKIOHIDServicePersistentPropertyController unregisterHandler:]
+ GCC_except_table371
+ GCC_except_table431
+ GCC_except_table444
+ GCC_except_table449
+ GCC_except_table456
+ GCC_except_table459
+ GCC_except_table494
+ GCC_except_table498
+ GCC_except_table725
+ GCC_except_table728
+ GCC_except_table765
+ GCC_except_table812
+ GCC_except_table873
+ GCC_except_table885
+ GCC_except_table917
+ OBJC_IVAR_$_BKIOHIDServiceMatcher._dataProviderSupportsSessionHoisting
+ OBJC_IVAR_$_BKIOHIDServiceMatcher._matcherID
+ OBJC_IVAR_$_BKIOHIDServiceMatcher._sessionID
+ _BKLogTouchEvents
+ _OBJC_CLASS_$_NSMapTable
+ __BKHIDServiceMatcherMap
+ __BKHIDServiceMatcherMapLock
+ __BKHIDServiceMatcherNextID
+ ___58-[BKIOHIDServiceMatcher _notifyObserver:servicesDidMatch:]_block_invoke
+ ___58-[BKIOHIDServiceMatcher _notifyObserver:servicesDidMatch:]_block_invoke_2
+ _objc_msgSend$hoistOnThread:forSessionID:
+ _objc_msgSend$mapTableWithKeyOptions:valueOptions:
- GCC_except_table369
- GCC_except_table429
- GCC_except_table442
- GCC_except_table447
- GCC_except_table454
- GCC_except_table457
- GCC_except_table492
- GCC_except_table496
- GCC_except_table723
- GCC_except_table726
- GCC_except_table762
- GCC_except_table809
- GCC_except_table870
- GCC_except_table882
- GCC_except_table914
- ___40-[BKIOHIDServiceMatcher _servicesAdded:]_block_invoke
- ___56-[BKIOHIDServiceMatcher _lock_asyncNotifyServicesAdded:]_block_invoke_2
CStrings:
+ "Matcher with ID %ld not found; ignoring"
+ "dealloc without invalidation matching %d invalidated %d"
+ "r"
- "dealloc without invalidation"
```
