## StorageManagement

> `/System/Library/PrivateFrameworks/StorageManagement.framework/Versions/A/StorageManagement`

```diff

-152.3.3.0.0
-  __TEXT.__text: 0x11eec
+152.5.2.0.0
+  __TEXT.__text: 0x11ecc
   __TEXT.__auth_stubs: 0x4a0
-  __TEXT.__objc_methlist: 0x22e0
+  __TEXT.__objc_methlist: 0x27a4
   __TEXT.__const: 0xea
   __TEXT.__cstring: 0x13e7
   __TEXT.__oslogstring: 0x7df

   __TEXT.__objc_methtype: 0x8cf
   __TEXT.__objc_stubs: 0x3660
   __DATA_CONST.__got: 0x268
-  __DATA_CONST.__const: 0x488
+  __DATA_CONST.__const: 0x490
   __DATA_CONST.__objc_classlist: 0x120
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1550
+  __DATA_CONST.__objc_selrefs: 0x15f8
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0xd0
   __AUTH_CONST.__auth_got: 0x260
   __AUTH_CONST.__const: 0x610
   __AUTH_CONST.__cfstring: 0x1ee0
-  __AUTH_CONST.__objc_const: 0x5680
+  __AUTH_CONST.__objc_const: 0x4db8
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0x410
   __DATA.__objc_ivar: 0x210

   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
+  - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIOKit.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: E5DF1F02-0840-3677-AF52-D5BB6D0F04B0
-  Functions: 778
-  Symbols:   2140
+  UUID: 5CDF176B-B859-3FEE-BC7F-AA51ED4FD041
+  Functions: 790
+  Symbols:   2154
   CStrings:  1689
 
Symbols:
+ +[STMCallbackManager sharedInstance].cold.1
+ +[STMExtension homeFolder].cold.1
+ +[STMHostExtensionContext extensionItemClasses].cold.1
+ +[STMOperationQueue concurrentBackgroundQueue].cold.1
+ +[STMOperationQueue serialBackgroundQueue].cold.1
+ -[NSExtensionItem(StorageMangement) setUserInfoObject:forKey:].cold.1
+ DispatchSourcesDictionary.cold.1
+ STMLocalizedStringFromFramework.cold.1
+ STMLogFile.cold.1
+ STMStorageIsInternalInstall.cold.1
+ STMStorageProductType.cold.1
+ STMStorageProductVersion.cold.1
+ __swift_FORCE_LOAD_$_swiftDataDetection
+ __swift_FORCE_LOAD_$_swiftDataDetection_$_StorageManagement

```
