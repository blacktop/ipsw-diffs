## Contacts

> `/System/Library/Frameworks/Contacts.framework/Versions/A/Contacts`

```diff

-  __TEXT.__text: 0x1f7794
-  __TEXT.__objc_methlist: 0x1b768
+  __TEXT.__text: 0x1f76d0
+  __TEXT.__objc_methlist: 0x1b798
   __TEXT.__const: 0x49e0
   __TEXT.__gcc_except_tab: 0x327c
-  __TEXT.__cstring: 0xccd9
+  __TEXT.__cstring: 0xcd09
   __TEXT.__dlopen_cstrs: 0x9e4
   __TEXT.__oslogstring: 0xceca
   __TEXT.__ustring: 0xe

   __TEXT.__swift_as_entry: 0x70
   __TEXT.__swift_as_ret: 0x60
   __TEXT.__swift_as_cont: 0x98
-  __TEXT.__unwind_info: 0x8890
+  __TEXT.__unwind_info: 0x88b0
   __TEXT.__eh_frame: 0x30c0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x60
   __DATA_CONST.__objc_protolist: 0x328
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa2b0
+  __DATA_CONST.__objc_selrefs: 0xa2d0
   __DATA_CONST.__objc_protorefs: 0xf0
   __DATA_CONST.__objc_superrefs: 0x980
   __DATA_CONST.__objc_arraydata: 0x348
-  __DATA_CONST.__got: 0x1ad8
-  __AUTH_CONST.__const: 0xd081
+  __DATA_CONST.__got: 0x1b58
+  __AUTH_CONST.__const: 0xd0a1
   __AUTH_CONST.__cfstring: 0xe1e0
-  __AUTH_CONST.__objc_const: 0x2c430
+  __AUTH_CONST.__objc_const: 0x2c440
   __AUTH_CONST.__objc_intobj: 0x600
   __AUTH_CONST.__objc_arrayobj: 0x1f8
   __AUTH_CONST.__objc_dictobj: 0x230
   __AUTH_CONST.__auth_got: 0x12d0
-  __AUTH.__objc_data: 0x5798
+  __AUTH.__objc_data: 0x6148
   __AUTH.__data: 0x818
   __DATA.__objc_ivar: 0x121c
   __DATA.__data: 0x3930
-  __DATA.__bss: 0x64d0
+  __DATA.__bss: 0x64b0
   __DATA.__common: 0x98
-  __DATA_DIRTY.__objc_data: 0x6130
+  __DATA_DIRTY.__objc_data: 0x5780
   __DATA_DIRTY.__data: 0x40
-  __DATA_DIRTY.__bss: 0xce0
+  __DATA_DIRTY.__bss: 0xd10
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/ClassKit.framework/Versions/A/ClassKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 13666
-  Symbols:   26409
-  CStrings:  5151
+  Functions: 13675
+  Symbols:   26422
+  CStrings:  5152
 
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
+ __89+[CNAppleAccountAvatarUpdateHelper updateAppleAccountAvatarForAccount:contactIdentifier:]_block_invoke_2
+ ___47+[CNAppleAccountAvatarUpdateHelper updateQueue]_block_invoke
+ ___75+[CNAppleAccountAvatarUpdateHelper _drainUpdateQueueWithTimeoutForTesting:]_block_invoke
+ ___89+[CNAppleAccountAvatarUpdateHelper updateAppleAccountAvatarForAccount:contactIdentifier:]_block_invoke_2
+ _dispatch_queue_attr_make_with_autorelease_frequency
+ _dispatch_queue_attr_make_with_qos_class
+ _objc_msgSend$TypeIdentifier
+ _objc_msgSend$_drainUpdateQueueWithTimeoutForTesting:
+ _objc_msgSend$updateQueue
+ updateQueue.once
+ updateQueue.queue
- __89+[CNAppleAccountAvatarUpdateHelper updateAppleAccountAvatarForAccount:contactIdentifier:]_block_invoke
- _objc_msgSend$EntityTypeIdentifier
- _swift_getEnumCaseMultiPayload
CStrings:
+ "com.apple.contacts.apple-account-avatar-update"

```
