## DoNotDisturbServer

> `/System/Library/PrivateFrameworks/DoNotDisturbServer.framework/Versions/A/DoNotDisturbServer`

```diff

-508.0.0.0.0
-  __TEXT.__text: 0xc6a10
-  __TEXT.__objc_methlist: 0xa76c
+511.0.0.0.0
+  __TEXT.__text: 0xc6e98
+  __TEXT.__objc_methlist: 0xa774
   __TEXT.__const: 0x688
   __TEXT.__cstring: 0x8784
-  __TEXT.__oslogstring: 0x10280
+  __TEXT.__oslogstring: 0x10320
   __TEXT.__gcc_except_tab: 0xf00
   __TEXT.__swift5_typeref: 0x294
   __TEXT.__swift5_fieldmd: 0x144

   __TEXT.__swift_as_entry: 0x2c
   __TEXT.__swift_as_ret: 0x2c
   __TEXT.__swift_as_cont: 0x2c
-  __TEXT.__unwind_info: 0x2860
+  __TEXT.__unwind_info: 0x2878
   __TEXT.__eh_frame: 0x578
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x140
   __DATA_CONST.__objc_protolist: 0x3e0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4b20
+  __DATA_CONST.__objc_selrefs: 0x4b30
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x3d8
   __DATA_CONST.__objc_arraydata: 0x358
-  __DATA_CONST.__got: 0xe28
+  __DATA_CONST.__got: 0xe30
   __AUTH_CONST.__const: 0x2fc8
   __AUTH_CONST.__cfstring: 0x71a0
   __AUTH_CONST.__objc_const: 0x257a0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3865
-  Symbols:   9189
-  CStrings:  2124
+  Functions: 3873
+  Symbols:   9195
+  CStrings:  2127
 
Symbols:
+ -[DNDSCoreDataBackingStore _purgeLegacyPersistentHistoryAtURL:model:]
+ GCC_except_table17
+ GCC_except_table23
+ _OBJC_CLASS_$_NSPersistentStoreCoordinator
+ __69-[DNDSCoreDataBackingStore _purgeLegacyPersistentHistoryAtURL:model:]_block_invoke
+ ___69-[DNDSCoreDataBackingStore _purgeLegacyPersistentHistoryAtURL:model:]_block_invoke
+ _objc_msgSend$_purgeLegacyPersistentHistoryAtURL:model:
+ _objc_msgSend$initWithManagedObjectModel:
- GCC_except_table13
- GCC_except_table19
CStrings:
+ "Legacy history purge: deleteHistory failed: %@"
+ "Legacy history purge: failed to open store with tracking on: %@"
+ "Legacy history purge: failed to remove store: %@"
```
