## Contacts

> `/System/Library/Frameworks/Contacts.framework/Versions/A/Contacts`

```diff

-3844.100.1.0.0
-  __TEXT.__text: 0x1ea5b0
-  __TEXT.__objc_methlist: 0x1b830
-  __TEXT.__const: 0x49e0
-  __TEXT.__gcc_except_tab: 0x327c
-  __TEXT.__cstring: 0xcd99
-  __TEXT.__dlopen_cstrs: 0x9e4
-  __TEXT.__oslogstring: 0xcf8a
+3846.200.41.0.0
+  __TEXT.__text: 0x1eaca8
+  __TEXT.__objc_methlist: 0x1b858
+  __TEXT.__const: 0x49f0
+  __TEXT.__gcc_except_tab: 0x328c
+  __TEXT.__cstring: 0xcdb9
+  __TEXT.__dlopen_cstrs: 0xa44
+  __TEXT.__oslogstring: 0xd06a
   __TEXT.__ustring: 0xe
   __TEXT.__constg_swiftt: 0x12d4
   __TEXT.__swift5_typeref: 0x1863

   __TEXT.__swift_as_entry: 0x70
   __TEXT.__swift_as_ret: 0x60
   __TEXT.__swift_as_cont: 0x98
-  __TEXT.__unwind_info: 0xb268
+  __TEXT.__unwind_info: 0xb290
   __TEXT.__eh_frame: 0x30c0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2cb8
+  __DATA_CONST.__const: 0x2cf0
   __DATA_CONST.__objc_classlist: 0x1158
   __DATA_CONST.__objc_catlist: 0x60
   __DATA_CONST.__objc_protolist: 0x328
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa370
+  __DATA_CONST.__objc_selrefs: 0xa390
   __DATA_CONST.__objc_protorefs: 0xf0
   __DATA_CONST.__objc_superrefs: 0x980
   __DATA_CONST.__objc_arraydata: 0x348
   __DATA_CONST.__got: 0x1b70
-  __AUTH_CONST.__const: 0xd0e1
+  __AUTH_CONST.__const: 0xd121
   __AUTH_CONST.__cfstring: 0xe220
   __AUTH_CONST.__objc_const: 0x2c4b0
   __AUTH_CONST.__objc_intobj: 0x600

   __DATA.__common: 0x98
   __DATA_DIRTY.__objc_data: 0x58e8
   __DATA_DIRTY.__data: 0x40
-  __DATA_DIRTY.__bss: 0xf30
+  __DATA_DIRTY.__bss: 0xec0
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/ClassKit.framework/Versions/A/ClassKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 13695
-  Symbols:   23858
-  CStrings:  3355
+  Functions: 13703
+  Symbols:   23870
+  CStrings:  3359
 
Symbols:
+ +[CNSharedProfileStateOracle shouldHideSharedProfileMenuInContacts]
+ +[_ExistingItemUpdater isRenderablePosterData:watchPosterImageData:]
+ -[_ExistingItemUpdater insertPoster:shouldBeCurrent:]
+ -[_ExistingItemUpdater updateExistingPostersWithPoster:shouldBeCurrent:]
+ CNPosterDataPropertyDescriptionLog.cn_once_object_0
+ CNPosterDataPropertyDescriptionLog.cn_once_token_0
+ GCC_except_table48
+ __OBJC_$_CLASS_METHODS__ExistingItemUpdater
+ ___36-[_ExistingItemUpdater visitPoster:]_block_invoke_2
+ ___CNPosterDataPropertyDescriptionLog_block_invoke
+ ___block_descriptor_32_e38_B16?0"CNContactPosterManagedObject"8l
+ _objc_msgSend$hideSharedProfileMenuInContacts
+ _objc_msgSend$insertPoster:shouldBeCurrent:
+ _objc_msgSend$isRenderablePosterData:watchPosterImageData:
+ _objc_msgSend$setDeletionDate:
+ _objc_msgSend$updateExistingPostersWithPoster:shouldBeCurrent:
- -[_ExistingItemUpdater insertPoster:]
- -[_ExistingItemUpdater updateExistingPostersWithPoster:]
- _objc_msgSend$insertPoster:
- _objc_msgSend$updateExistingPostersWithPoster:
CStrings:
+ "Ignoring wallpaper with empty posterArchiveData for contact identifier: %{public}@ (metadata: %{public}s, sharedToMe: %{public}s, sensitive: %{public}s)"
+ "Not saving poster/image for contact identifier: %{public}@, error: %@"
+ "kMDItemRole ==\"*\" && _kMDItemIsZombie != 1"
+ "no"
+ "yes"
- "kMDItemRole ==\"*\""
```
