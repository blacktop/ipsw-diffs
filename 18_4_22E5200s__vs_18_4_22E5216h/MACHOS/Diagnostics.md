## Diagnostics

> `/Applications/Diagnostics.app/Diagnostics`

```diff

 820.100.56.0.0
-  __TEXT.__text: 0x10e6b0
-  __TEXT.__auth_stubs: 0x3070
+  __TEXT.__text: 0x10ed34
+  __TEXT.__auth_stubs: 0x3060
   __TEXT.__objc_stubs: 0x6de0
   __TEXT.__objc_methlist: 0x6274
   __TEXT.__gcc_except_tab: 0xa98

   __TEXT.__swift_as_entry: 0x18
   __TEXT.__swift_as_ret: 0x1c
   __TEXT.__swift5_mpenum: 0x20
-  __TEXT.__unwind_info: 0x3618
+  __TEXT.__unwind_info: 0x3608
   __TEXT.__eh_frame: 0xa40
-  __DATA_CONST.__auth_got: 0x1848
+  __DATA_CONST.__auth_got: 0x1840
   __DATA_CONST.__got: 0xf28
-  __DATA_CONST.__auth_ptr: 0x1480
+  __DATA_CONST.__auth_ptr: 0x1440
   __DATA_CONST.__const: 0xa5e8
   __DATA_CONST.__cfstring: 0x1d60
   __DATA_CONST.__objc_classlist: 0x4a0

   __DATA.__objc_selrefs: 0x3b30
   __DATA.__objc_ivar: 0x38c
   __DATA.__objc_data: 0x8498
-  __DATA.__data: 0x5d18
+  __DATA.__data: 0x5cf8
   __DATA.__bss: 0x50b0
-  __DATA.__common: 0x160
+  __DATA.__common: 0x158
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
   Functions: 5645
-  Symbols:   1571
+  Symbols:   1570
   CStrings:  4393
 
Symbols:
+ _swift_cvw_allocateGenericValueMetadataWithLayoutString
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_enumFn_getEnumTag
+ _swift_cvw_initStructMetadataWithLayoutString
+ _swift_cvw_initWithCopy
+ _swift_cvw_initWithTake
+ _swift_cvw_initializeBufferWithCopyOfBuffer
+ _swift_cvw_instantiateLayoutString
- _swift_allocateGenericValueMetadataWithLayoutString
- _swift_enumFn_getEnumTag
- _swift_generic_assignWithCopy
- _swift_generic_assignWithTake
- _swift_generic_destroy
- _swift_generic_initWithCopy
- _swift_generic_initWithTake
- _swift_generic_initializeBufferWithCopyOfBuffer
- _swift_generic_instantiateLayoutString
- _swift_initStaticObject
- _swift_initStructMetadataWithLayoutString

```
