## PhoneKit

> `/System/iOSSupport/System/Library/PrivateFrameworks/PhoneKit.framework/Versions/A/PhoneKit`

```diff

-153.100.1.1.25
-  __TEXT.__text: 0x18f58
-  __TEXT.__objc_methlist: 0x110c
+156.200.70.1.2
+  __TEXT.__text: 0x194e8
+  __TEXT.__objc_methlist: 0x112c
   __TEXT.__const: 0x754
-  __TEXT.__cstring: 0x9a3
-  __TEXT.__oslogstring: 0xf03
+  __TEXT.__cstring: 0x9d3
+  __TEXT.__oslogstring: 0x1013
   __TEXT.__gcc_except_tab: 0x174
   __TEXT.__ustring: 0x4
   __TEXT.__swift5_typeref: 0x195

   __TEXT.__swift_as_cont: 0xc
   __TEXT.__swift5_reflstr: 0x3
   __TEXT.__swift5_assocty: 0x18
-  __TEXT.__unwind_info: 0x878
+  __TEXT.__unwind_info: 0x880
   __TEXT.__eh_frame: 0x1b0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x11e8
+  __DATA_CONST.__objc_selrefs: 0x1200
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
-  __AUTH_CONST.__auth_got: 0x6a8
+  __AUTH_CONST.__auth_got: 0x6a0
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
-  Functions: 528
-  Symbols:   1500
-  CStrings:  189
+  Functions: 533
+  Symbols:   1510
+  CStrings:  193
 
Symbols:
+ -[PKRecentsController contactsFetchQueue]
+ -[PKRecentsController contactsUpdateGeneration]
+ -[PKRecentsController setContactsUpdateGeneration:]
+ GCC_except_table134
+ OBJC_IVAR_$_PKRecentsController._contactsFetchQueue
+ OBJC_IVAR_$_PKRecentsController._contactsUpdateGeneration
+ __44-[PKRecentsController handleUpdatedContacts]_block_invoke
+ __44-[PKRecentsController handleUpdatedContacts]_block_invoke_2
+ ___44-[PKRecentsController handleUpdatedContacts]_block_invoke_2
+ _objc_msgSend$contactsFetchQueue
+ _objc_msgSend$contactsUpdateGeneration
+ _objc_msgSend$setContactsUpdateGeneration:
- GCC_except_table132
- _objc_retain_x28
CStrings:
+ "[handleUpdatedContacts] Discarding stale contact fetch (generation %@, current %@)"
+ "[handleUpdatedContacts] Fetching contacts for %lu handles using contact store %@"
+ "[handleUpdatedContacts] Found %lu contacts for contact handle %{sensitive}@; caching the first contact %{sensitive}@"
+ "com.apple.calls.queue.%@.contactsFetch.%p"
```
