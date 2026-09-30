## Email

> `/System/Library/PrivateFrameworks/Email.framework/Email`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`

```diff

-3901.200.34.0.0
-  __TEXT.__text: 0xd3860
-  __TEXT.__objc_methlist: 0xcd6c
+3901.200.41.0.0
+  __TEXT.__text: 0xd40b8
+  __TEXT.__objc_methlist: 0xce24
   __TEXT.__const: 0x18c2
-  __TEXT.__gcc_except_tab: 0x1ac7c
+  __TEXT.__gcc_except_tab: 0x1ad70
   __TEXT.__cstring: 0xc369
   __TEXT.__ustring: 0x170
-  __TEXT.__oslogstring: 0x67e3
+  __TEXT.__oslogstring: 0x67f3
   __TEXT.__dlopen_cstrs: 0x160
   __TEXT.__swift5_typeref: 0x4aa
   __TEXT.__constg_swiftt: 0x538

   __TEXT.__swift5_capture: 0x48
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x8470
+  __TEXT.__unwind_info: 0x8518
   __TEXT.__eh_frame: 0x328
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x45e8
-  __DATA_CONST.__objc_classlist: 0x578
+  __DATA_CONST.__objc_classlist: 0x580
   __DATA_CONST.__objc_catlist: 0x78
   __DATA_CONST.__objc_protolist: 0x320
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6108
+  __DATA_CONST.__objc_selrefs: 0x6158
   __DATA_CONST.__objc_protorefs: 0x110
-  __DATA_CONST.__objc_superrefs: 0x470
+  __DATA_CONST.__objc_superrefs: 0x478
   __DATA_CONST.__objc_arraydata: 0x1e8
-  __DATA_CONST.__got: 0xc50
+  __DATA_CONST.__got: 0xc58
   __AUTH_CONST.__const: 0x1f40
   __AUTH_CONST.__cfstring: 0xa400
-  __AUTH_CONST.__objc_const: 0x169e8
+  __AUTH_CONST.__objc_const: 0x16b90
   __AUTH_CONST.__objc_intobj: 0x348
   __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH_CONST.__auth_got: 0xbc8
-  __AUTH.__objc_data: 0x200
+  __AUTH_CONST.__auth_got: 0xbd0
+  __AUTH.__objc_data: 0x250
   __AUTH.__data: 0x158
-  __DATA.__objc_ivar: 0xc34
+  __DATA.__objc_ivar: 0xc44
   __DATA.__data: 0x28c0
   __DATA_DIRTY.__objc_data: 0x3718
   __DATA_DIRTY.__data: 0x250

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5140
-  Symbols:   11252
+  Functions: 5157
+  Symbols:   11289
   CStrings:  2151
 
Symbols:
+ +[EMMessageBodyParsingUtils strippedQuoteBlockFromHTMLBody:]
+ -[EMAccountRepository accountIfAvailableForIdentifier:]
+ -[EMMailboxRepository _cachedAllMailboxObjectIDs]
+ -[EMMailboxRepository _cachedMailboxObjectIDsForMailboxType:]
+ -[EMMailboxRepository _cachedMailboxTypeForMailboxObjectID:cacheValid:]
+ -[EMMailboxRepository _failMailboxesPromiseAsTemporarilyUnavailable]
+ -[EMMailboxRepository availableMailboxTypeResolver]
+ -[EMMailboxRepository isMailboxCacheWarm]
+ -[EMMailboxRepository mailboxesFuture]
+ -[_EMAvailableMailboxTypeResolver .cxx_destruct]
+ -[_EMAvailableMailboxTypeResolver allMailboxObjectIDs]
+ -[_EMAvailableMailboxTypeResolver initWithRepository:]
+ -[_EMAvailableMailboxTypeResolver mailboxObjectIDsForMailboxType:]
+ -[_EMAvailableMailboxTypeResolver mailboxTypeForMailboxObjectID:]
+ _OBJC_CLASS_$__EMAvailableMailboxTypeResolver
+ _OBJC_IVAR_$_EMAccountRepository._accountsRequestInFlight
+ _OBJC_IVAR_$_EMMailbox._repository
+ _OBJC_IVAR_$_EMMailboxRepository._availableMailboxTypeResolver
+ _OBJC_IVAR_$__EMAvailableMailboxTypeResolver._repository
+ _OBJC_METACLASS_$__EMAvailableMailboxTypeResolver
+ __OBJC_$_INSTANCE_METHODS__EMAvailableMailboxTypeResolver
+ __OBJC_$_INSTANCE_VARIABLES__EMAvailableMailboxTypeResolver
+ __OBJC_$_PROP_LIST__EMAvailableMailboxTypeResolver
+ __OBJC_CLASS_PROTOCOLS_$__EMAvailableMailboxTypeResolver
+ __OBJC_CLASS_RO_$__EMAvailableMailboxTypeResolver
+ __OBJC_METACLASS_RO_$__EMAvailableMailboxTypeResolver
+ ___55-[EMAccountRepository accountIfAvailableForIdentifier:]_block_invoke
+ ___61-[EMMailboxRepository _cachedMailboxObjectIDsForMailboxType:]_block_invoke
+ ___remoteInterfaceForConnection_block_invoke
+ _objc_msgSend$_cachedAllMailboxObjectIDs
+ _objc_msgSend$_cachedMailboxObjectIDsForMailboxType:
+ _objc_msgSend$_cachedMailboxTypeForMailboxObjectID:cacheValid:
+ _objc_msgSend$_failMailboxesPromiseAsTemporarilyUnavailable
+ _objc_msgSend$accountIfAvailableForIdentifier:
+ _objc_msgSend$initWithRepository:
+ _objc_msgSend$strippedQuoteBlockFromHTMLBody:
+ _os_unfair_lock_trylock
+ _remoteInterfaceForConnection
- ___54-[EMMailboxRepository mailboxObjectIDsForMailboxType:]_block_invoke
CStrings:
+ "A1"
+ "Error establishing xpc connection: %{public}@"
- "A"
- "Error establishing xpc connection : %@"
```
