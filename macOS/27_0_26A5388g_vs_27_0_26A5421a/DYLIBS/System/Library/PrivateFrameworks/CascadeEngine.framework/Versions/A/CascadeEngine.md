## CascadeEngine

> `/System/Library/PrivateFrameworks/CascadeEngine.framework/Versions/A/CascadeEngine`

```diff

-247.0.1.0.0
-  __TEXT.__text: 0x69278
-  __TEXT.__objc_methlist: 0x1eac
+250.0.0.3.0
+  __TEXT.__text: 0x69fec
+  __TEXT.__objc_methlist: 0x1ef4
   __TEXT.__const: 0x1268
-  __TEXT.__gcc_except_tab: 0x6c0
-  __TEXT.__cstring: 0x2aa4
-  __TEXT.__oslogstring: 0x6a29
-  __TEXT.__ustring: 0x7c
+  __TEXT.__gcc_except_tab: 0x6f4
+  __TEXT.__cstring: 0x2ba4
+  __TEXT.__ustring: 0x84
+  __TEXT.__oslogstring: 0x6b49
   __TEXT.__dlopen_cstrs: 0x47
   __TEXT.__swift5_typeref: 0xde0
   __TEXT.__swift5_reflstr: 0x31e

   __TEXT.__swift_as_entry: 0x98
   __TEXT.__swift_as_ret: 0x98
   __TEXT.__swift_as_cont: 0xdc
-  __TEXT.__unwind_info: 0x15d0
+  __TEXT.__unwind_info: 0x1600
   __TEXT.__eh_frame: 0x17a8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x288
+  __DATA_CONST.__const: 0x290
   __DATA_CONST.__objc_classlist: 0x128
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x120
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1a10
+  __DATA_CONST.__objc_selrefs: 0x1a70
   __DATA_CONST.__objc_protorefs: 0x60
   __DATA_CONST.__objc_superrefs: 0xe0
   __DATA_CONST.__objc_arraydata: 0x50
-  __DATA_CONST.__got: 0x678
-  __AUTH_CONST.__const: 0x3578
-  __AUTH_CONST.__cfstring: 0x1980
-  __AUTH_CONST.__objc_const: 0x50d8
+  __DATA_CONST.__got: 0x680
+  __AUTH_CONST.__const: 0x35d8
+  __AUTH_CONST.__cfstring: 0x1a20
+  __AUTH_CONST.__objc_const: 0x5148
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__auth_got: 0xd18
+  __AUTH_CONST.__auth_got: 0xd20
   __AUTH.__objc_data: 0x648
   __AUTH.__data: 0x50
-  __DATA.__objc_ivar: 0x2b8
+  __DATA.__objc_ivar: 0x2c4
   __DATA.__data: 0xe08
   __DATA.__bss: 0xb30
   __DATA_DIRTY.__objc_data: 0xb00

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 2344
-  Symbols:   2842
-  CStrings:  823
+  Functions: 2355
+  Symbols:   2874
+  CStrings:  831
 
Symbols:
+ -[CCDonationItemComponents deletedFieldTypes]
+ -[CCDonationItemComponents initWithSetKey:content:metaContent:isPatch:deletedFieldTypes:]
+ -[CCDonationServiceConnection _beginSetDonationWithItemType:encodedDescriptors:sourceVersion:sourceValidity:options:reply:]
+ -[CCDonationServiceConnection _drainNextPendingDonation]
+ -[CCDonationServiceConnection abortInFlightDonationOnConnectionInvalidation]
+ -[CCRapportSyncEngine descriptorsMatchEngineDomain:]
+ -[CCRapportSyncEngine syncErrorCodeFromLocalDeviceSiteError:]
+ -[CCSetStoreUpdateServiceExported abortInFlightDonationOnInvalidation]
+ -[CCSetVersionedMergeable localDeviceSiteAddingExpirationDate:error:]
+ GCC_except_table15
+ GCC_except_table23
+ GCC_except_table41
+ GCC_except_table43
+ GCC_except_table58
+ GCC_except_table65
+ GCC_except_table8
+ OBJC_IVAR_$_CCDonationItemComponents._deletedFieldTypes
+ OBJC_IVAR_$_CCDonationServiceConnection._connectionInvalidated
+ OBJC_IVAR_$_CCDonationServiceConnection._pendingDonations
+ _CCSetErrorForDatabaseError
+ _OBJC_CLASS_$_CCItemDeletedFieldTypes
+ __122-[CCDonationServiceConnection beginSetDonationWithItemType:encodedDescriptors:sourceVersion:sourceValidity:options:reply:]_block_invoke
+ ___61-[CCDonationServiceConnection _finalizeForStatus:replyBlock:]_block_invoke
+ ___70-[CCSetStoreUpdateServiceExported abortInFlightDonationOnInvalidation]_block_invoke
+ ___76-[CCDonationServiceConnection abortInFlightDonationOnConnectionInvalidation]_block_invoke
+ ___block_descriptor_40_e8_32s_e5_v8?0l
+ ___block_descriptor_84_e8_32s40s48s56s64bs72w_e5_v8?0l
+ _objc_msgSend$_beginSetDonationWithItemType:encodedDescriptors:sourceVersion:sourceValidity:options:reply:
+ _objc_msgSend$_drainNextPendingDonation
+ _objc_msgSend$abortInFlightDonationOnConnectionInvalidation
+ _objc_msgSend$abortInFlightDonationOnInvalidation
+ _objc_msgSend$copyApplyingPatch:deletedFieldTypes:error:
+ _objc_msgSend$deletedFieldTypes
+ _objc_msgSend$deletedFieldTypesWithPackedData:error:
+ _objc_msgSend$descriptorsMatchEngineDomain:
+ _objc_msgSend$documentCachePredicateFromAssociatedSetPredicate:documentCacheSet:error:
+ _objc_msgSend$fieldType
+ _objc_msgSend$initWithSetKey:content:metaContent:isPatch:deletedFieldTypes:
+ _objc_msgSend$isSourceItemIdentifierFieldType:
+ _objc_msgSend$localDeviceSiteAddingExpirationDate:error:
+ _objc_msgSend$predicateType
+ _objc_msgSend$removeObjectAtIndex:
+ _objc_msgSend$syncErrorCodeFromLocalDeviceSiteError:
- -[CCDonationItemComponents initWithSetKey:content:metaContent:isPatch:]
- -[CCSetVersionedMergeable localDeviceSiteAddingExpirationDate:]
- GCC_except_table11
- GCC_except_table21
- GCC_except_table37
- GCC_except_table39
- GCC_except_table64
- _objc_msgSend$copyApplyingPatch:error:
- _objc_msgSend$documentCachePredicateFromAssociatedSetPredicate:error:
- _objc_msgSend$initWithSetKey:content:metaContent:isPatch:
- _objc_msgSend$localDeviceSiteAddingExpirationDate:
CStrings:
+ "%@: Client connection invalidated with a donation in progress; aborting"
+ "%@: Donation already in progress; enqueuing behind %lu pending donation(s): %@"
+ "%@: Donation terminated; dequeuing next pending donation (%lu will remain queued behind it)"
+ "%@: Local source updating set with priors: %@"
+ "%@: Refusing donation: %@"
+ "Client XPC connection invalidated"
+ "Connection deallocated before queued donation could start: %@"
+ "Connection invalidated before donation could start: %@"
+ "Donation already in progress (%@) — refusing no-wait donation: %@"
+ "Requested set (%@) is not served by this sync engine's domain"
+ "Requested set's partition domain does not match this sync engine's domain"
- "%@: Local source updating set"
- "Donation already in progress (%@) — refusing new donation: %@"
- "Failed to get local device site"
```
