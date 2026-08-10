## DoNotDisturbServer

> `/System/Library/PrivateFrameworks/DoNotDisturbServer.framework/DoNotDisturbServer`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__cstring`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
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
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-508.0.0.0.0
-  __TEXT.__text: 0xc2a34
-  __TEXT.__objc_methlist: 0xab14
+511.0.0.0.0
+  __TEXT.__text: 0xc2e78
+  __TEXT.__objc_methlist: 0xab1c
   __TEXT.__const: 0x718
   __TEXT.__cstring: 0x8da4
-  __TEXT.__oslogstring: 0x11900
+  __TEXT.__oslogstring: 0x119a0
   __TEXT.__gcc_except_tab: 0x10c4
   __TEXT.__dlopen_cstrs: 0x59
   __TEXT.__swift5_typeref: 0x294

   __TEXT.__swift_as_entry: 0x2c
   __TEXT.__swift_as_ret: 0x2c
   __TEXT.__swift_as_cont: 0x2c
-  __TEXT.__unwind_info: 0x2a38
+  __TEXT.__unwind_info: 0x2a50
   __TEXT.__eh_frame: 0x578
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x150
   __DATA_CONST.__objc_protolist: 0x3e8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4e08
+  __DATA_CONST.__objc_selrefs: 0x4e18
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x3f0
   __DATA_CONST.__objc_arraydata: 0x358
-  __DATA_CONST.__got: 0xf00
+  __DATA_CONST.__got: 0xf08
   __AUTH_CONST.__const: 0x1198
   __AUTH_CONST.__cfstring: 0x7b20
   __AUTH_CONST.__objc_const: 0x268f0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3942
-  Symbols:   9431
-  CStrings:  2291
+  Functions: 3950
+  Symbols:   9437
+  CStrings:  2294
 
Symbols:
+ -[DNDSCoreDataBackingStore _purgeLegacyPersistentHistoryAtURL:model:]
+ GCC_except_table13
+ GCC_except_table9
+ _OBJC_CLASS_$_NSPersistentStoreCoordinator
+ ___69-[DNDSCoreDataBackingStore _purgeLegacyPersistentHistoryAtURL:model:]_block_invoke
+ _objc_msgSend$_purgeLegacyPersistentHistoryAtURL:model:
+ _objc_msgSend$initWithManagedObjectModel:
- GCC_except_table11
CStrings:
+ "Legacy history purge: deleteHistory failed: %@"
+ "Legacy history purge: failed to open store with tracking on: %@"
+ "Legacy history purge: failed to remove store: %@"
```
