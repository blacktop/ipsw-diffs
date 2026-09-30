## WalletBlastDoorService

> `/System/Library/PrivateFrameworks/WalletBlastDoorSupport.framework/Versions/A/XPCServices/WalletBlastDoorService.xpc/Contents/MacOS/WalletBlastDoorService`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_entry`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__DATA_CONST.__const`
- `__DATA.__objc_selrefs`

```diff

-325.100.1.0.0
-  __TEXT.__text: 0x8394
-  __TEXT.__auth_stubs: 0xa20
+327.100.2.0.0
+  __TEXT.__text: 0x17a3c
+  __TEXT.__auth_stubs: 0x19d0
   __TEXT.__objc_stubs: 0x40
-  __TEXT.__const: 0x242
-  __TEXT.__swift5_typeref: 0x144
+  __TEXT.__const: 0x3a0
+  __TEXT.__swift5_typeref: 0x339
   __TEXT.__swift5_entry: 0x8
   __TEXT.__constg_swiftt: 0x94
   __TEXT.__swift5_fieldmd: 0xa0
   __TEXT.__swift5_reflstr: 0x103
   __TEXT.__swift5_assocty: 0x18
-  __TEXT.__cstring: 0x48
+  __TEXT.__cstring: 0x22b
   __TEXT.__swift5_proto: 0x8
   __TEXT.__swift5_types: 0x10
+  __TEXT.__oslogstring: 0x32d
   __TEXT.__objc_methname: 0x25
-  __TEXT.__unwind_info: 0x160
-  __TEXT.__eh_frame: 0x190
+  __TEXT.__unwind_info: 0x298
+  __TEXT.__eh_frame: 0x770
   __DATA_CONST.__const: 0x1b8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0x518
-  __DATA_CONST.__got: 0xd8
-  __DATA_CONST.__auth_ptr: 0xd0
+  __DATA_CONST.__auth_got: 0xcf0
+  __DATA_CONST.__got: 0x428
+  __DATA_CONST.__auth_ptr: 0x200
   __DATA.__objc_selrefs: 0x10
-  __DATA.__data: 0x180
+  __DATA.__data: 0x300
   __DATA.__common: 0x18
   __DATA.__bss: 0x100
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 75
-  Symbols:   68
-  CStrings:  4
+  Functions: 135
+  Symbols:   80
+  CStrings:  28
 
Symbols:
+ __os_log_impl
+ _os_log_type_enabled
+ _swift_bridgeObjectRelease_n
+ _swift_dynamicCastClass
+ _swift_errorRelease
+ _swift_getTypeByMangledNameInContextInMetadataState2
+ _swift_once
+ _swift_slowAlloc
+ _swift_slowDealloc
+ _swift_unknownObjectRelease
+ _swift_unknownObjectRelease_n
+ _swift_unknownObjectRetain
CStrings:
+ "Discarding barcode because its message encoding is too long"
+ "Discarding barcode because its message is too long"
+ "Discarding order provider because its dark tracking logo name is too long"
+ "Discarding order provider because its light tracking logo name is too long"
+ "Discarding pickup fulfillment because its identifier is too long"
+ "Discarding return because its identifier is too long"
+ "Discarding shipping fulfillment because its identifier is too long"
+ "Discarding webServiceURL and authenticationToken because the authenticationToken is too long"
+ "Discarding webServiceURL and authenticationToken because the webServiceURL has an invalid scheme"
+ "Discarding webServiceURL and authenticationToken because the webServiceURL has no scheme"
+ "WalletOrderContent"
+ "changeNotifications"
+ "changeNotificationsInvalid"
+ "com.apple.BlastDoor"
+ "com.apple.BlastDoor.WalletOrderContent"
+ "fulfillmentInvalid"
+ "fulfillments.pickup.status"
+ "fulfillments.shipping.shippingType"
+ "fulfillments.shipping.status"
+ "orderContentInvalid"
+ "payment.transactions.status"
+ "payment.transactions.type"
+ "shippingTypeInvalid"
+ "transactionTypeInvalid"
```
