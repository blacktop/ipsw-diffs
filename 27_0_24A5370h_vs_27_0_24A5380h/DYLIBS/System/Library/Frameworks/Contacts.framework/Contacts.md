## Contacts

> `/System/Library/Frameworks/Contacts.framework/Contacts`

```diff

-  __TEXT.__text: 0x2206d0
-  __TEXT.__objc_methlist: 0x1bde8
+  __TEXT.__text: 0x22096c
+  __TEXT.__objc_methlist: 0x1be18
   __TEXT.__const: 0x4c60
   __TEXT.__gcc_except_tab: 0x3c2c
-  __TEXT.__cstring: 0xcbc9
+  __TEXT.__cstring: 0xcbf9
   __TEXT.__dlopen_cstrs: 0x91e
   __TEXT.__oslogstring: 0xf67a
   __TEXT.__ustring: 0x12

   __TEXT.__swift_as_entry: 0xb8
   __TEXT.__swift_as_ret: 0xe0
   __TEXT.__swift_as_cont: 0x158
-  __TEXT.__unwind_info: 0x91e8
+  __TEXT.__unwind_info: 0x9208
   __TEXT.__eh_frame: 0x3ff0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x308
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9d08
+  __DATA_CONST.__objc_selrefs: 0x9d28
   __DATA_CONST.__objc_protorefs: 0xe0
   __DATA_CONST.__objc_superrefs: 0xa20
   __DATA_CONST.__objc_arraydata: 0x268
-  __DATA_CONST.__got: 0x1d48
-  __AUTH_CONST.__const: 0x91d1
+  __DATA_CONST.__got: 0x1db0
+  __AUTH_CONST.__const: 0x91f1
   __AUTH_CONST.__cfstring: 0xdfa0
-  __AUTH_CONST.__objc_const: 0x2db60
+  __AUTH_CONST.__objc_const: 0x2db70
   __AUTH_CONST.__objc_intobj: 0x600
   __AUTH_CONST.__objc_arrayobj: 0x1c8
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__auth_got: 0x1df0
-  __AUTH.__objc_data: 0x6358
+  __AUTH_CONST.__auth_got: 0x1de8
+  __AUTH.__objc_data: 0x6df8
   __AUTH.__data: 0x8a8
   __DATA.__objc_ivar: 0x1328
   __DATA.__data: 0x3ab8
-  __DATA.__bss: 0x65d0
+  __DATA.__bss: 0x65b0
   __DATA.__common: 0xa0
-  __DATA_DIRTY.__objc_data: 0x5e10
+  __DATA_DIRTY.__objc_data: 0x5370
   __DATA_DIRTY.__data: 0x20
-  __DATA_DIRTY.__bss: 0xbc8
+  __DATA_DIRTY.__bss: 0xbf8
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/ClassKit.framework/ClassKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 14203
-  Symbols:   39026
-  CStrings:  5230
+  Functions: 14213
+  Symbols:   39045
+  CStrings:  5231
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift_as_entry : content changed
~ __TEXT.__swift_as_ret : content changed
~ __TEXT.__swift_as_cont : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH.__data : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__data : content changed
Symbols:
+ +[CNAppleAccountAvatarUpdateHelper _drainUpdateQueueWithTimeoutForTesting:]
+ +[CNAppleAccountAvatarUpdateHelper updateQueue]
+ -[CNXPCContactsSupportTestDouble _waitForAvatarUpdatesForTesting]
+ ___47+[CNAppleAccountAvatarUpdateHelper updateQueue]_block_invoke
+ ___75+[CNAppleAccountAvatarUpdateHelper _drainUpdateQueueWithTimeoutForTesting:]_block_invoke
+ ___89+[CNAppleAccountAvatarUpdateHelper updateAppleAccountAvatarForAccount:contactIdentifier:]_block_invoke_2
+ _dispatch_queue_attr_make_with_autorelease_frequency
+ _objc_msgSend$TypeIdentifier
+ _objc_msgSend$_drainUpdateQueueWithTimeoutForTesting:
+ _objc_msgSend$updateQueue
+ _updateQueue.once
+ _updateQueue.queue
- _objc_msgSend$EntityTypeIdentifier
- _swift_getEnumCaseMultiPayload
CStrings:
+ "com.apple.contacts.apple-account-avatar-update"

```
