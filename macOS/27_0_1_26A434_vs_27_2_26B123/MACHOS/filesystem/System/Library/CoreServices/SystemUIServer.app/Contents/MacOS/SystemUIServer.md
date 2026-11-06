## SystemUIServer

> `/System/Library/CoreServices/SystemUIServer.app/Contents/MacOS/SystemUIServer`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_proto`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-555.0.2.0.0
-  __TEXT.__text: 0x44464
-  __TEXT.__auth_stubs: 0x2cf0
-  __TEXT.__objc_stubs: 0x3820
-  __TEXT.__objc_methlist: 0x1844
-  __TEXT.__const: 0x3488
+555.1.4.0.0
+  __TEXT.__text: 0x44614
+  __TEXT.__auth_stubs: 0x2d00
+  __TEXT.__objc_stubs: 0x38c0
+  __TEXT.__objc_methlist: 0x187c
+  __TEXT.__const: 0x3492
   __TEXT.__gcc_except_tab: 0x584
-  __TEXT.__objc_methname: 0x4bb5
-  __TEXT.__cstring: 0x1f32
+  __TEXT.__objc_methname: 0x4c95
+  __TEXT.__cstring: 0x1f62
   __TEXT.__oslogstring: 0x134e
   __TEXT.__objc_classname: 0x33f
-  __TEXT.__objc_methtype: 0xe89
+  __TEXT.__objc_methtype: 0xeb9
   __TEXT.__ustring: 0xe4
   __TEXT.__swift5_typeref: 0xa76
   __TEXT.__constg_swiftt: 0xc5c

   __TEXT.__swift5_protos: 0x20
   __TEXT.__swift5_assocty: 0x1c0
   __TEXT.__swift5_builtin: 0x64
-  __TEXT.__unwind_info: 0x1ad8
+  __TEXT.__unwind_info: 0x1ae8
   __TEXT.__eh_frame: 0x7e8
-  __DATA_CONST.__const: 0x3c98
-  __DATA_CONST.__cfstring: 0x1920
+  __DATA_CONST.__const: 0x3c88
+  __DATA_CONST.__cfstring: 0x1940
   __DATA_CONST.__objc_classlist: 0xc8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x78
-  __DATA_CONST.__auth_got: 0x1688
+  __DATA_CONST.__auth_got: 0x1690
   __DATA_CONST.__got: 0x6d8
   __DATA_CONST.__auth_ptr: 0x4c8
-  __DATA.__objc_const: 0x52d8
-  __DATA.__objc_selrefs: 0x14d0
-  __DATA.__objc_ivar: 0x1d4
+  __DATA.__objc_const: 0x5338
+  __DATA.__objc_selrefs: 0x14f8
+  __DATA.__objc_ivar: 0x1e0
   __DATA.__objc_data: 0x800
   __DATA.__data: 0xad0
   __DATA.__crash_info: 0x148

   - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2313
-  Symbols:   1071
-  CStrings:  1564
+  Functions: 2319
+  Symbols:   1072
+  CStrings:  1577
 
Symbols:
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
- _CGSSetSymbolicHotKeyEnabled
CStrings:
+ "E"
+ "Q"
+ "_borrowVISpaceHotKeyForCapture"
+ "_cancelAllVISpaceHotKeyBorrows"
+ "_enableVisualIntelligenceHotKeysLocked:"
+ "_returnVISpaceHotKeyBorrow:"
+ "_setVISpaceHotKeyRegistered:"
+ "_viHotKeyLock"
+ "_viSpaceHotKeyBorrowCount"
+ "_viSpaceHotKeyCancelCount"
+ "com.apple.screencapture.resume-vi-hotkey"
+ "v24@0:8Q16"
+ "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"
```
