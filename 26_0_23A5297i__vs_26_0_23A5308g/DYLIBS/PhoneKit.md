## PhoneKit

> `/System/Library/PrivateFrameworks/PhoneKit.framework/PhoneKit`

```diff

-100.100.18.1.5
-  __TEXT.__text: 0x15bc4
+103.100.8.2.2
+  __TEXT.__text: 0x15ecc
   __TEXT.__auth_stubs: 0xb30
-  __TEXT.__objc_methlist: 0x1014
+  __TEXT.__objc_methlist: 0x101c
   __TEXT.__const: 0x6b4
   __TEXT.__cstring: 0x92e
-  __TEXT.__oslogstring: 0xe13
+  __TEXT.__oslogstring: 0xe2d
   __TEXT.__gcc_except_tab: 0x1b8
   __TEXT.__ustring: 0x4
   __TEXT.__swift5_typeref: 0x113

   __TEXT.__unwind_info: 0x5d0
   __TEXT.__eh_frame: 0x160
   __TEXT.__objc_classname: 0x12d
-  __TEXT.__objc_methname: 0x4196
+  __TEXT.__objc_methname: 0x41df
   __TEXT.__objc_methtype: 0x497
-  __TEXT.__objc_stubs: 0x34a0
+  __TEXT.__objc_stubs: 0x34e0
   __DATA_CONST.__got: 0x378
   __DATA_CONST.__const: 0x4f0
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1158
+  __DATA_CONST.__objc_selrefs: 0x1160
   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_arraydata: 0x10
   __AUTH_CONST.__auth_got: 0x5a8

   __AUTH.__objc_data: 0x70
   __AUTH.__data: 0x28
   __DATA.__objc_ivar: 0xb4
-  __DATA.__data: 0x368
-  __DATA.__bss: 0x1b0
+  __DATA.__data: 0x360
+  __DATA.__bss: 0x1a0
   __DATA_DIRTY.__objc_data: 0x230
-  __DATA_DIRTY.__data: 0x48
-  __DATA_DIRTY.__bss: 0xb0
+  __DATA_DIRTY.__data: 0x50
+  __DATA_DIRTY.__bss: 0xc0
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/ContactsUI.framework/ContactsUI
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 5B6AE6EA-C52D-358A-B843-5C94E211CB43
-  Functions: 472
-  Symbols:   1848
-  CStrings:  1021
+  UUID: 350CC175-35CF-383D-9F78-DE79F04B8BC5
+  Functions: 473
+  Symbols:   1852
+  CStrings:  1023
 
Symbols:
+ -[PKRecentsController recentCallsDeletedFromCachedRecentCall:callHistoryControllerRecentCalls:]
+ ___block_literal_global.525
+ ___block_literal_global.527
+ _objc_msgSend$notifyDelegatesRecentsController:didCompleteFetchingCalls:
+ _objc_msgSend$recentCallsDeletedFromCachedRecentCall:callHistoryControllerRecentCalls:
- ___block_literal_global.524
- ___block_literal_global.526
Functions:
~ -[PKRecentsController fetchRecentCalls] : 1024 -> 1224
+ -[PKRecentsController recentCallsDeletedFromCachedRecentCall:callHistoryControllerRecentCalls:]
+ -[PKRecentsController analyticsLogger]
- -[PKRecentsController acceptedIntroductionsNotifier]
CStrings:
+ "Found %lu deleted objects"
+ "recentCallsDeletedFromCachedRecentCall:callHistoryControllerRecentCalls:"

```
