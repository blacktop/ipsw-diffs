## PhoneKit

> `/System/Library/PrivateFrameworks/PhoneKit.framework/PhoneKit`

```diff

-153.100.1.2.29
-  __TEXT.__text: 0x193ec
-  __TEXT.__objc_methlist: 0x110c
+156.200.70.2.2
+  __TEXT.__text: 0x1997c
+  __TEXT.__objc_methlist: 0x112c
   __TEXT.__const: 0x754
-  __TEXT.__cstring: 0x9b3
-  __TEXT.__oslogstring: 0xf23
+  __TEXT.__cstring: 0x9e3
+  __TEXT.__oslogstring: 0x1043
   __TEXT.__gcc_except_tab: 0x174
   __TEXT.__ustring: 0x4
   __TEXT.__swift5_typeref: 0x195

   __TEXT.__swift_as_cont: 0xc
   __TEXT.__swift5_reflstr: 0x3
   __TEXT.__swift5_assocty: 0x18
-  __TEXT.__unwind_info: 0x8b0
+  __TEXT.__unwind_info: 0x8b8
   __TEXT.__eh_frame: 0x1b0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x11f0
+  __DATA_CONST.__objc_selrefs: 0x1208
   __DATA_CONST.__objc_superrefs: 0x28
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__got: 0x3c0
   __AUTH_CONST.__const: 0x1e8
-  __AUTH_CONST.__cfstring: 0xce0
-  __AUTH_CONST.__objc_const: 0x1778
+  __AUTH_CONST.__cfstring: 0xd00
+  __AUTH_CONST.__objc_const: 0x17d8
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH_CONST.__auth_got: 0x6c8
+  __AUTH_CONST.__auth_got: 0x6c0
   __AUTH.__objc_data: 0xc0
   __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0xb8
+  __DATA.__objc_ivar: 0xc0
   __DATA.__data: 0x3a0
   __DATA_DIRTY.__objc_data: 0x230
   __DATA_DIRTY.__data: 0x68

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 530
-  Symbols:   1499
-  CStrings:  191
+  Functions: 535
+  Symbols:   1507
+  CStrings:  195
 
Symbols:
+ -[PKRecentsController contactsFetchQueue]
+ -[PKRecentsController contactsUpdateGeneration]
+ -[PKRecentsController setContactsUpdateGeneration:]
+ GCC_except_table135
+ _OBJC_IVAR_$_PKRecentsController._contactsFetchQueue
+ _OBJC_IVAR_$_PKRecentsController._contactsUpdateGeneration
+ ___44-[PKRecentsController handleUpdatedContacts]_block_invoke_2
+ _objc_msgSend$contactsFetchQueue
+ _objc_msgSend$contactsUpdateGeneration
+ _objc_msgSend$setContactsUpdateGeneration:
- GCC_except_table133
- _objc_retain_x28
CStrings:
+ "[handleUpdatedContacts] Discarding stale contact fetch (generation %@, current %@)"
+ "[handleUpdatedContacts] Fetching contacts for %lu handles using contact store %@"
+ "[handleUpdatedContacts] Found %lu contacts for contact handle %{sensitive}@; caching the first contact %{sensitive}@"
+ "com.apple.calls.queue.%@.contactsFetch.%p"
```
