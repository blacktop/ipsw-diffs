## PosterFoundation

> `/System/Library/PrivateFrameworks/PosterFoundation.framework/PosterFoundation`

```diff

-290.112.0.0.0
-  __TEXT.__text: 0x433d8
+296.100.0.0.0
+  __TEXT.__text: 0x43bfc
   __TEXT.__auth_stubs: 0x1040
-  __TEXT.__objc_methlist: 0x3158
+  __TEXT.__objc_methlist: 0x3240
   __TEXT.__const: 0x196
-  __TEXT.__cstring: 0x3cf9
-  __TEXT.__oslogstring: 0x316f
-  __TEXT.__gcc_except_tab: 0x10f8
-  __TEXT.__unwind_info: 0x1258
-  __TEXT.__objc_classname: 0x720
-  __TEXT.__objc_methname: 0x7496
-  __TEXT.__objc_methtype: 0x1273
-  __TEXT.__objc_stubs: 0x56c0
-  __DATA_CONST.__got: 0x4e8
-  __DATA_CONST.__const: 0x1330
-  __DATA_CONST.__objc_classlist: 0x1a0
+  __TEXT.__cstring: 0x3d51
+  __TEXT.__oslogstring: 0x3142
+  __TEXT.__gcc_except_tab: 0x1100
+  __TEXT.__unwind_info: 0x1288
+  __TEXT.__objc_classname: 0x72b
+  __TEXT.__objc_methname: 0x75d8
+  __TEXT.__objc_methtype: 0x12a3
+  __TEXT.__objc_stubs: 0x57a0
+  __DATA_CONST.__got: 0x500
+  __DATA_CONST.__const: 0x1328
+  __DATA_CONST.__objc_classlist: 0x1a8
   __DATA_CONST.__objc_catlist: 0x78
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1d80
+  __DATA_CONST.__objc_selrefs: 0x1dd0
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x178
+  __DATA_CONST.__objc_superrefs: 0x180
   __DATA_CONST.__objc_arraydata: 0x128
   __AUTH_CONST.__auth_got: 0x830
-  __AUTH_CONST.__const: 0x920
-  __AUTH_CONST.__cfstring: 0x3c20
-  __AUTH_CONST.__objc_const: 0x80f0
+  __AUTH_CONST.__const: 0x900
+  __AUTH_CONST.__cfstring: 0x3d00
+  __AUTH_CONST.__objc_const: 0x8260
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_intobj: 0x60
-  __AUTH.__objc_data: 0x4b0
-  __DATA.__objc_ivar: 0x2dc
+  __AUTH.__objc_data: 0x500
+  __DATA.__objc_ivar: 0x2e8
   __DATA.__data: 0x850
-  __DATA.__bss: 0x98
+  __DATA.__bss: 0x90
   __DATA_DIRTY.__objc_data: 0xb90
   __DATA_DIRTY.__bss: 0x1f0
   __DATA_DIRTY.__common: 0xc

   - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
-  - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 508ADF14-6C44-332B-8624-B1F89FBA398A
-  Functions: 1589
-  Symbols:   5569
-  CStrings:  2833
+  UUID: 5CB014AE-4D28-3B01-9FEF-6E460521F021
+  Functions: 1608
+  Symbols:   5626
+  CStrings:  2867
 
Symbols:
+ +[PFFileSystemStagedURL commitStagedURLs:destinationURLsForSwap:stagingURLsForSwap:stagingURL:fileManager:error:].cold.1
+ +[PFLRUCache new]
+ -[PFFileSystemStagedURL commitDescription]
+ -[PFFileSystemStagedURL description]
+ -[PFFileSystemStagedURL initWithEndpoint:commitHandler:commitDescription:]
+ -[PFFileSystemStagedURL initWithEndpoint:commitHandler:commitDescription:].cold.1
+ -[PFFileSystemStagedURL initWithEndpoint:commitHandler:commitDescription:].cold.2
+ -[PFFileSystemStagedURL initWithEndpoint:commitHandler:commitDescription:].cold.3
+ -[PFLRUCache .cxx_destruct]
+ -[PFLRUCache _cleanup]
+ -[PFLRUCache _promoteObject:forKey:]
+ -[PFLRUCache capacity]
+ -[PFLRUCache copyWithZone:]
+ -[PFLRUCache count]
+ -[PFLRUCache initWithCapacity:]
+ -[PFLRUCache init]
+ -[PFLRUCache objectForKey:]
+ -[PFLRUCache objectForKey:ifNil:]
+ -[PFLRUCache removeAllObjects]
+ -[PFLRUCache removeObjectForKey:]
+ -[PFLRUCache setCapacity:]
+ -[PFLRUCache setObject:forKey:]
+ -[PFPosterArchiver _unarchiveWithHandler:manifest:error:].cold.13
+ GCC_except_table5
+ GCC_except_table66
+ _OBJC_CLASS_$_BSMutableOrderedDictionary
+ _OBJC_CLASS_$_BSOrderedDictionaryKeyStrategy
+ _OBJC_CLASS_$_PFLRUCache
+ _OBJC_IVAR_$_PFFileSystemStagedURL._commitDescription
+ _OBJC_IVAR_$_PFLRUCache._capacity
+ _OBJC_IVAR_$_PFLRUCache._storage
+ _OBJC_METACLASS_$_PFLRUCache
+ __OBJC_$_CLASS_METHODS_PFLRUCache
+ __OBJC_$_INSTANCE_METHODS_PFLRUCache
+ __OBJC_$_INSTANCE_VARIABLES_PFLRUCache
+ __OBJC_$_PROP_LIST_PFLRUCache
+ __OBJC_CLASS_PROTOCOLS_$_PFLRUCache
+ __OBJC_CLASS_RO_$_PFLRUCache
+ __OBJC_METACLASS_RO_$_PFLRUCache
+ ___27-[PFLRUCache copyWithZone:]_block_invoke
+ ___31-[PFOSUnfairLock performBlock:]_block_invoke
+ ___block_descriptor_40_e8_32s_e15_v32?0816^B24ls32l8
+ ___block_literal_global.28
+ _objc_msgSend$_cleanup
+ _objc_msgSend$_promoteObject:forKey:
+ _objc_msgSend$capacity
+ _objc_msgSend$initWithCapacity:keyOrderingStrategy:
+ _objc_msgSend$initWithEndpoint:commitHandler:commitDescription:
+ _objc_msgSend$pf_versionsURLForIdentifierURL:
+ _objc_msgSend$removeObjectAtIndex:
+ _objc_msgSend$sortByInsertionOrder
- -[PFFileSystemStagedURL initWithEndpoint:commitHandler:].cold.1
- -[PFFileSystemStagedURL initWithEndpoint:commitHandler:].cold.2
- GCC_except_table49
- _PFBundleIdentifierRequiresMemoryHogAssertion.cold.1
- _PFBundleIdentifierRequiresMemoryHogAssertion.onceToken
- ___30-[PFDebounceFilter allowEvent]_block_invoke
- ___PFBundleIdentifierRequiresMemoryHogAssertion_block_invoke
- ___PFBundleIdentifierRequiresMemoryHogAssertion_block_invoke.cold.1
- ___block_descriptor_48_e8_32s_e5_v8?0ls32l8
- ___block_literal_global.31
- ___block_literal_global.33
- __swift_FORCE_LOAD_$_swiftCoreImage
- __swift_FORCE_LOAD_$_swiftCoreImage_$_PosterFoundation
- _objc_msgSend$initWithEndpoint:commitHandler:
CStrings:
+ "@\"BSMutableOrderedDictionary\""
+ "@40@0:8@16@?24@32"
+ "PFLRUCache"
+ "T@\"NSString\",R,N,V_commitDescription"
+ "TQ,N,V_capacity"
+ "TQ,R,D,N"
+ "Unable to cleanup versionScratchURL: %@"
+ "[PFFileSystemStagedURL] error committing stagedURL: %{public}@"
+ "_capacity"
+ "_cleanup"
+ "_commitDescription"
+ "_promoteObject:forKey:"
+ "_storage"
+ "archiveObject"
+ "capacity"
+ "commitDescription"
+ "copyURL"
+ "createEndpoint"
+ "deleteEndpoint"
+ "initWithCapacity:keyOrderingStrategy:"
+ "initWithEndpoint:commitHandler:commitDescription:"
+ "objectForKey:ifNil:"
+ "removeObjectAtIndex:"
+ "setCapacity:"
+ "sortByInsertionOrder"
+ "unknown"
+ "writeData"
- "Memory hog assertions are not available on tvOS.  Please consult your nearest jetsam properties plist for available Jetsam bands you could request."

```
