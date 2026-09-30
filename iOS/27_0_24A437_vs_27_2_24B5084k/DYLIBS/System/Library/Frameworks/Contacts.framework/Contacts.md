## Contacts

> `/System/Library/Frameworks/Contacts.framework/Contacts`

```diff

-3844.100.1.0.0
-  __TEXT.__text: 0x2125e0
-  __TEXT.__objc_methlist: 0x1be70
+3846.200.41.0.0
+  __TEXT.__text: 0x212c78
+  __TEXT.__objc_methlist: 0x1be98
   __TEXT.__const: 0x4c60
-  __TEXT.__gcc_except_tab: 0x3c2c
-  __TEXT.__cstring: 0xcc19
-  __TEXT.__dlopen_cstrs: 0x91e
-  __TEXT.__oslogstring: 0xf75a
+  __TEXT.__gcc_except_tab: 0x3c3c
+  __TEXT.__cstring: 0xcc39
+  __TEXT.__dlopen_cstrs: 0x97e
+  __TEXT.__oslogstring: 0xf83a
   __TEXT.__ustring: 0x12
   __TEXT.__constg_swiftt: 0x16d4
   __TEXT.__swift5_typeref: 0x1b0b

   __TEXT.__swift_as_entry: 0xb8
   __TEXT.__swift_as_ret: 0xe0
   __TEXT.__swift_as_cont: 0x158
-  __TEXT.__unwind_info: 0xba88
+  __TEXT.__unwind_info: 0xbab0
   __TEXT.__eh_frame: 0x4000
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x66f0
+  __DATA_CONST.__const: 0x6728
   __DATA_CONST.__objc_classlist: 0x11b0
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x308
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9d70
+  __DATA_CONST.__objc_selrefs: 0x9d88
   __DATA_CONST.__objc_protorefs: 0xe0
   __DATA_CONST.__objc_superrefs: 0xa20
   __DATA_CONST.__objc_arraydata: 0x268
   __DATA_CONST.__got: 0x1db8
-  __AUTH_CONST.__const: 0x9211
+  __AUTH_CONST.__const: 0x9251
   __AUTH_CONST.__cfstring: 0xdfc0
   __AUTH_CONST.__objc_const: 0x2dbe0
   __AUTH_CONST.__objc_intobj: 0x5e8

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 14230
-  Symbols:   24344
-  CStrings:  3452
+  Functions: 14238
+  Symbols:   24354
+  CStrings:  3456
 
Symbols:
+ +[CNSharedProfileStateOracle shouldHideSharedProfileMenuInContacts]
+ +[_ExistingItemUpdater isRenderablePosterData:watchPosterImageData:]
+ -[_ExistingItemUpdater insertPoster:shouldBeCurrent:]
+ -[_ExistingItemUpdater updateExistingPostersWithPoster:shouldBeCurrent:]
+ _CNPosterDataPropertyDescriptionLog.cn_once_object_0
+ _CNPosterDataPropertyDescriptionLog.cn_once_token_0
+ __OBJC_$_CLASS_METHODS__ExistingItemUpdater
+ ___36-[_ExistingItemUpdater visitPoster:]_block_invoke_2
+ ___CNPosterDataPropertyDescriptionLog_block_invoke
+ ___block_descriptor_32_e38_B16?0"CNContactPosterManagedObject"8l
+ _objc_msgSend$hideSharedProfileMenuInContacts
+ _objc_msgSend$insertPoster:shouldBeCurrent:
+ _objc_msgSend$isRenderablePosterData:watchPosterImageData:
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
