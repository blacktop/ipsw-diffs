## PhoneKit

> `/System/Library/PrivateFrameworks/PhoneKit.framework/PhoneKit`

```diff

-106.200.75.2.1
-  __TEXT.__text: 0x15db4
-  __TEXT.__auth_stubs: 0xb30
-  __TEXT.__objc_methlist: 0x101c
-  __TEXT.__const: 0x6c4
-  __TEXT.__cstring: 0x92e
-  __TEXT.__oslogstring: 0xe77
+106.200.81.2.12
+  __TEXT.__text: 0x19ed0
+  __TEXT.__auth_stubs: 0xcb0
+  __TEXT.__objc_methlist: 0x102c
+  __TEXT.__const: 0x754
+  __TEXT.__cstring: 0x933
+  __TEXT.__oslogstring: 0xea3
   __TEXT.__gcc_except_tab: 0x1a4
   __TEXT.__ustring: 0x4
-  __TEXT.__swift5_typeref: 0x113
-  __TEXT.__swift5_capture: 0x48
+  __TEXT.__swift5_typeref: 0x189
+  __TEXT.__swift5_fieldmd: 0x10
+  __TEXT.__constg_swiftt: 0x2c
+  __TEXT.__swift5_capture: 0x4c
+  __TEXT.__swift5_protos: 0x4
+  __TEXT.__swift5_proto: 0x8
   __TEXT.__swift_as_entry: 0x8
-  __TEXT.__swift_as_ret: 0x4
+  __TEXT.__swift_as_ret: 0x8
   __TEXT.__swift5_reflstr: 0x3
   __TEXT.__swift5_assocty: 0x18
-  __TEXT.__swift5_proto: 0x4
-  __TEXT.__unwind_info: 0x5c0
-  __TEXT.__eh_frame: 0x160
+  __TEXT.__unwind_info: 0x650
+  __TEXT.__eh_frame: 0x2b0
   __TEXT.__objc_classname: 0x12d
-  __TEXT.__objc_methname: 0x41c9
+  __TEXT.__objc_methname: 0x4263
   __TEXT.__objc_methtype: 0x497
-  __TEXT.__objc_stubs: 0x34c0
-  __DATA_CONST.__got: 0x378
-  __DATA_CONST.__const: 0x4c8
+  __TEXT.__objc_stubs: 0x3500
+  __DATA_CONST.__got: 0x3a8
+  __DATA_CONST.__const: 0x4a8
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1158
+  __DATA_CONST.__objc_selrefs: 0x1170
   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__auth_got: 0x5a8
-  __AUTH_CONST.__const: 0x1e0
+  __AUTH_CONST.__auth_got: 0x668
+  __AUTH_CONST.__const: 0x1f0
   __AUTH_CONST.__cfstring: 0xaa0
   __AUTH_CONST.__objc_const: 0x16a8
   __AUTH_CONST.__objc_dictobj: 0x28

   __AUTH.__objc_data: 0x70
   __AUTH.__data: 0x28
   __DATA.__objc_ivar: 0xb4
-  __DATA.__data: 0x360
+  __DATA.__data: 0x3d0
   __DATA.__bss: 0x1a0
   __DATA_DIRTY.__objc_data: 0x230
-  __DATA_DIRTY.__data: 0x50
+  __DATA_DIRTY.__data: 0x30
   __DATA_DIRTY.__bss: 0xc0
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/ContactsUI.framework/ContactsUI

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 377D1298-895E-3CAA-A21E-BF51A46F6194
-  Functions: 472
-  Symbols:   1847
-  CStrings:  1022
+  UUID: 0CEB9039-57E9-391F-A864-4864E00A7710
+  Functions: 512
+  Symbols:   1877
+  CStrings:  1025
 
Symbols:
+ -[PKRecentsController markRecentCallsAsReadWithPredicate:]
+ -[PKRecentsController notifyDelegatesRecentsControllerDidUpdateAcceptedContacts:]
+ GCC_except_table81
+ GCC_except_table93
+ ___58-[PKRecentsController markRecentCallsAsReadWithPredicate:]_block_invoke
+ ___81-[PKRecentsController notifyDelegatesRecentsControllerDidUpdateAcceptedContacts:]_block_invoke
+ ___81-[PKRecentsController notifyDelegatesRecentsControllerDidUpdateAcceptedContacts:]_block_invoke_2
+ ___block_literal_global.528
+ ___block_literal_global.530
+ ___swift_allocate_value_buffer
+ ___swift_destroy_boxed_opaque_existential_1
+ ___swift_instantiateConcreteTypeFromMangledNameV2
+ ___swift_project_boxed_opaque_existential_1
+ ___swift_project_value_buffer
+ __swiftEmptySetSingleton
+ __swift_stdlib_bridgeErrorToNSError
+ _objc_msgSend$markUnreadRecentCallsAsReadWithPredicate:
+ _objc_msgSend$notifyDelegatesRecentsControllerDidUpdateAcceptedContacts:
+ _objc_msgSend$recentsControllerDidUpdateAcceptedContacts:
+ _swift_deletedAsyncMethodErrorTu
+ _swift_errorRelease
+ _swift_errorRetain
+ _swift_isUniquelyReferenced_nonNull_bridgeObject
+ _swift_slowAlloc
+ _swift_slowDealloc
+ _symbolic $s8PhoneKit17BlockListProtocolP
+ _symbolic SaySo8CHHandleCG
+ _symbolic So8NSObjectCSg
+ _symbolic _____3key_Sb5valuet 20LiveCommunicationKit6HandleV
+ _symbolic ______SaySo8CHHandleCGt 20LiveCommunicationKit6HandleV
+ _symbolic ______p 8PhoneKit17BlockListProtocolP
+ _symbolic _____ySo8CHHandleCG s11_SetStorageC
+ _symbolic _____y_____G s11_SetStorageC 20LiveCommunicationKit6HandleV
+ _symbolic _____y_____SaySo8CHHandleCGG s18_DictionaryStorageC 20LiveCommunicationKit6HandleV
- -[PKRecentsController markRecentAudioCallsAsRead]
- GCC_except_table78
- GCC_except_table90
- ___49-[PKRecentsController markRecentAudioCallsAsRead]_block_invoke
- ___block_literal_global.525
- ___block_literal_global.527
- ___swift_instantiateConcreteTypeFromMangledName
- _objc_msgSend$markRecentAudioCallsAsRead
- _symbolic SaySo12CHRecentCallCG
- _symbolic ShySo8CHHandleCG
- _symbolic _____yShySo8CHHandleCGG s23_ContiguousArrayStorageC
CStrings:
+ "Failed to fetch blocked status: %@"
+ "markRecentCallsAsReadWithPredicate:"
+ "markUnreadRecentCallsAsReadWithPredicate:"
+ "notifyDelegatesRecentsControllerDidUpdateAcceptedContacts:"
+ "recentsControllerDidUpdateAcceptedContacts:"
- "markRecentAudioCallsAsRead"

```
