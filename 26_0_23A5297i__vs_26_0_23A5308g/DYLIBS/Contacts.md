## Contacts

> `/System/Library/Frameworks/Contacts.framework/Contacts`

```diff

-3801.100.3.1.1
-  __TEXT.__text: 0x1b65f4
+3804.100.1.0.0
+  __TEXT.__text: 0x1b632c
   __TEXT.__auth_stubs: 0x3280
-  __TEXT.__objc_methlist: 0x1ad20
-  __TEXT.__const: 0x2058
+  __TEXT.__objc_methlist: 0x1ad40
+  __TEXT.__const: 0x20c8
   __TEXT.__gcc_except_tab: 0x3b2c
   __TEXT.__cstring: 0xc982
   __TEXT.__dlopen_cstrs: 0x8de
-  __TEXT.__oslogstring: 0xba8a
+  __TEXT.__oslogstring: 0xbaca
   __TEXT.__ustring: 0x12
   __TEXT.__constg_swiftt: 0xdc4
-  __TEXT.__swift5_typeref: 0xe9f
-  __TEXT.__swift5_reflstr: 0x942
-  __TEXT.__swift5_fieldmd: 0x8f8
+  __TEXT.__swift5_typeref: 0xea1
+  __TEXT.__swift5_reflstr: 0x968
+  __TEXT.__swift5_fieldmd: 0x904
   __TEXT.__swift5_builtin: 0x8c
   __TEXT.__swift5_assocty: 0x1c0
   __TEXT.__swift5_proto: 0xbc

   __TEXT.__swift5_capture: 0x5d4
   __TEXT.__swift_as_entry: 0x68
   __TEXT.__swift_as_ret: 0x5c
-  __TEXT.__unwind_info: 0x7e70
-  __TEXT.__eh_frame: 0x25b8
+  __TEXT.__unwind_info: 0x7e78
+  __TEXT.__eh_frame: 0x25c0
   __TEXT.__objc_classname: 0x43df
-  __TEXT.__objc_methname: 0x2b208
-  __TEXT.__objc_methtype: 0x53e4
-  __TEXT.__objc_stubs: 0x1e560
+  __TEXT.__objc_methname: 0x2b24e
+  __TEXT.__objc_methtype: 0x53c2
+  __TEXT.__objc_stubs: 0x1e580
   __DATA_CONST.__got: 0x1b50
-  __DATA_CONST.__const: 0x61c0
+  __DATA_CONST.__const: 0x6198
   __DATA_CONST.__objc_classlist: 0x10e0
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x308
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9600
+  __DATA_CONST.__objc_selrefs: 0x9618
   __DATA_CONST.__objc_protorefs: 0xd8
   __DATA_CONST.__objc_superrefs: 0x9b0
   __DATA_CONST.__objc_arraydata: 0x268
   __AUTH_CONST.__auth_got: 0x1950
-  __AUTH_CONST.__const: 0x6848
+  __AUTH_CONST.__const: 0x69c0
   __AUTH_CONST.__cfstring: 0xd9c0
-  __AUTH_CONST.__objc_const: 0x2ba78
+  __AUTH_CONST.__objc_const: 0x2bb08
   __AUTH_CONST.__objc_intobj: 0x5d0
   __AUTH_CONST.__objc_arrayobj: 0x1c8
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH.__objc_data: 0x56b0
+  __AUTH.__objc_data: 0x5638
   __AUTH.__data: 0x660
-  __DATA.__objc_ivar: 0x1254
+  __DATA.__objc_ivar: 0x1260
   __DATA.__data: 0x2d20
-  __DATA.__bss: 0x24a0
+  __DATA.__bss: 0x2460
   __DATA.__common: 0x80
-  __DATA_DIRTY.__objc_data: 0x5d48
+  __DATA_DIRTY.__objc_data: 0x5dc0
   __DATA_DIRTY.__data: 0x38
-  __DATA_DIRTY.__bss: 0xfe8
+  __DATA_DIRTY.__bss: 0x1028
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/ClassKit.framework/ClassKit
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: D7640C89-E1EB-36D3-B623-A7D40E53B888
-  Functions: 12422
-  Symbols:   36420
-  CStrings:  12756
+  UUID: 2A396AE2-3D4C-3775-B640-135005F813E8
+  Functions: 12426
+  Symbols:   36407
+  CStrings:  12759
 
Symbols:
+ -[CNContact selectedChannel]
+ -[CNContact setSelectedChannel:]
+ -[CNContactPosterDataService queue]
+ -[CNFavoritesEntryRepresentation equivalencyHash]
+ -[CNSharedProfileStateOracle updateContactForAutoUpdateWithError:].cold.2
+ -[_ListenerDelegate initWithService:queue:]
+ -[_ListenerDelegate queue]
+ -[_ListenerStoreAdapter countForFetchRequest:reply:].cold.2
+ -[_ListenerStoreAdapter countForFetchRequest:reply:].cold.3
+ -[_ListenerStoreAdapter executeCreateRequest:reply:].cold.2
+ -[_ListenerStoreAdapter executeCreateRequest:reply:].cold.3
+ -[_ListenerStoreAdapter executeDeleteRequest:reply:].cold.2
+ -[_ListenerStoreAdapter executeDeleteRequest:reply:].cold.3
+ -[_ListenerStoreAdapter executeFetchRequest:reply:].cold.2
+ -[_ListenerStoreAdapter executeFetchRequest:reply:].cold.3
+ -[_ListenerStoreAdapter executeUpdateRequest:reply:].cold.2
+ -[_ListenerStoreAdapter executeUpdateRequest:reply:].cold.3
+ -[_ListenerStoreAdapter queue]
+ _OBJC_IVAR_$_CNContact._selectedChannel
+ _OBJC_IVAR_$_CNContactPosterDataService._queue
+ _OBJC_IVAR_$__ListenerDelegate._queue
+ _OBJC_IVAR_$__ListenerStoreAdapter._queue
+ __PROTOCOLS__TtCVE8ContactsCSo14CNContactStore26FetchedChangeHistoryEvents22EventVisitorTranslator.2
+ ___49-[CNFavoritesEntryRepresentation equivalencyHash]_block_invoke
+ ___49-[CNFavoritesEntryRepresentation equivalencyHash]_block_invoke_2
+ ___49-[CNFavoritesEntryRepresentation equivalencyHash]_block_invoke_3
+ ___49-[CNFavoritesEntryRepresentation equivalencyHash]_block_invoke_4
+ ___49-[CNFavoritesEntryRepresentation equivalencyHash]_block_invoke_5
+ ___49-[CNFavoritesEntryRepresentation equivalencyHash]_block_invoke_6
+ ___block_literal_global.802
+ ___block_literal_global.853
+ ___block_literal_global.862
+ ___swift_memcpy8_8
+ _block_copy_helper.31
+ _block_descriptor.33
+ _block_destroy_helper.32
+ _descriptionForActionType:.cn_once_object_74
+ _descriptionForActionType:.cn_once_token_74
+ _descriptionForUpdateState:.cn_once_object_75
+ _descriptionForUpdateState:.cn_once_token_75
+ _objc_msgSend$_setQueue:
+ _objc_msgSend$initWithService:queue:
+ _symbolic Igh_
- +[CNSharedProfileStateOracle globalSharedProfileUpdateState]
- -[CNFavoritesEntryRepresentation equivilencyHash]
- -[_ListenerDelegate initWithService:]
- -[_ListenerStoreAdapter workloop]
- _OBJC_IVAR_$__ListenerStoreAdapter._workloop
- __PROTOCOLS__TtCVE8ContactsCSo14CNContactStore26FetchedChangeHistoryEvents22EventVisitorTranslator.3
- ___49-[CNFavoritesEntryRepresentation equivilencyHash]_block_invoke
- ___49-[CNFavoritesEntryRepresentation equivilencyHash]_block_invoke_2
- ___49-[CNFavoritesEntryRepresentation equivilencyHash]_block_invoke_3
- ___49-[CNFavoritesEntryRepresentation equivilencyHash]_block_invoke_4
- ___49-[CNFavoritesEntryRepresentation equivilencyHash]_block_invoke_5
- ___49-[CNFavoritesEntryRepresentation equivilencyHash]_block_invoke_6
- ___51-[_ListenerStoreAdapter executeFetchRequest:reply:]_block_invoke
- ___51-[_ListenerStoreAdapter executeFetchRequest:reply:]_block_invoke.cold.1
- ___51-[_ListenerStoreAdapter executeFetchRequest:reply:]_block_invoke.cold.2
- ___51-[_ListenerStoreAdapter executeFetchRequest:reply:]_block_invoke.cold.3
- ___52-[_ListenerStoreAdapter countForFetchRequest:reply:]_block_invoke
- ___52-[_ListenerStoreAdapter countForFetchRequest:reply:]_block_invoke.cold.1
- ___52-[_ListenerStoreAdapter countForFetchRequest:reply:]_block_invoke.cold.2
- ___52-[_ListenerStoreAdapter countForFetchRequest:reply:]_block_invoke.cold.3
- ___52-[_ListenerStoreAdapter executeCreateRequest:reply:]_block_invoke
- ___52-[_ListenerStoreAdapter executeCreateRequest:reply:]_block_invoke.cold.1
- ___52-[_ListenerStoreAdapter executeCreateRequest:reply:]_block_invoke.cold.2
- ___52-[_ListenerStoreAdapter executeCreateRequest:reply:]_block_invoke.cold.3
- ___52-[_ListenerStoreAdapter executeDeleteRequest:reply:]_block_invoke
- ___52-[_ListenerStoreAdapter executeDeleteRequest:reply:]_block_invoke.cold.1
- ___52-[_ListenerStoreAdapter executeDeleteRequest:reply:]_block_invoke.cold.2
- ___52-[_ListenerStoreAdapter executeDeleteRequest:reply:]_block_invoke.cold.3
- ___52-[_ListenerStoreAdapter executeUpdateRequest:reply:]_block_invoke
- ___52-[_ListenerStoreAdapter executeUpdateRequest:reply:]_block_invoke.cold.1
- ___52-[_ListenerStoreAdapter executeUpdateRequest:reply:]_block_invoke.cold.2
- ___52-[_ListenerStoreAdapter executeUpdateRequest:reply:]_block_invoke.cold.3
- ___block_descriptor_64_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
- ___block_literal_global.797
- ___block_literal_global.848
- ___block_literal_global.857
- _block_copy_helper.27
- _block_descriptor.29
- _block_destroy_helper.28
- _descriptionForActionType:.cn_once_object_73
- _descriptionForActionType:.cn_once_token_73
- _descriptionForUpdateState:.cn_once_object_74
- _descriptionForUpdateState:.cn_once_token_74
- _objc_msgSend$globalSharedProfileUpdateState
- _symbolic Ig_
CStrings:
+ "%04llx Did execute remote request"
+ "%04llx Will execute remote request: %@"
+ "Refusing to auto-update a contact which already has an image or wallpaper and default-sharing"
+ "T@\"NSObject<OS_dispatch_queue>\",R,V_queue"
+ "T@\"NSString\",C,V_selectedChannel"
+ "_selectedChannel"
+ "_setQueue:"
+ "equivalencyHash"
+ "initWithService:queue:"
+ "queue"
+ "selectedChannel"
+ "setSelectedChannel:"
- "%04llx Dequeuing remote request: %@"
- "%04llx Did reply to remote request"
- "%04llx Enqueuing remote request: %@"
- "@\"NSObject<OS_dispatch_workloop>\""
- "T@\"NSObject<OS_dispatch_workloop>\",R,V_workloop"
- "_workloop"
- "equivilencyHash"
- "globalSharedProfileUpdateState"
- "workloop"

```
