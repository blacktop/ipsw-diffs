## libMemoryResourceException.dylib

> `/usr/lib/libMemoryResourceException.dylib`

```diff

-314.100.8.0.0
-  __TEXT.__text: 0x1aaa0
-  __TEXT.__auth_stubs: 0xcb0
-  __TEXT.__objc_methlist: 0x1594
-  __TEXT.__const: 0x178
-  __TEXT.__cstring: 0x1f0e
-  __TEXT.__oslogstring: 0xb7b
+314.100.11.0.0
+  __TEXT.__text: 0x1b008
+  __TEXT.__auth_stubs: 0xcc0
+  __TEXT.__objc_methlist: 0x15ac
+  __TEXT.__const: 0x188
+  __TEXT.__cstring: 0x1f20
+  __TEXT.__oslogstring: 0xd18
   __TEXT.__gcc_except_tab: 0x3bc
   __TEXT.__ustring: 0xd0
-  __TEXT.__unwind_info: 0x500
+  __TEXT.__unwind_info: 0x508
   __TEXT.__objc_classname: 0x19e
-  __TEXT.__objc_methname: 0x3887
-  __TEXT.__objc_methtype: 0x82b
-  __TEXT.__objc_stubs: 0x2c40
-  __DATA_CONST.__got: 0x278
+  __TEXT.__objc_methname: 0x3919
+  __TEXT.__objc_methtype: 0x836
+  __TEXT.__objc_stubs: 0x2c80
+  __DATA_CONST.__got: 0x280
   __DATA_CONST.__const: 0xe58
   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xf38
+  __DATA_CONST.__objc_selrefs: 0xf58
   __DATA_CONST.__objc_superrefs: 0x78
   __DATA_CONST.__objc_arraydata: 0x38
-  __AUTH_CONST.__auth_got: 0x668
+  __AUTH_CONST.__auth_got: 0x670
   __AUTH_CONST.__const: 0x280
-  __AUTH_CONST.__cfstring: 0x27c0
-  __AUTH_CONST.__objc_const: 0x2f48
+  __AUTH_CONST.__cfstring: 0x27e0
+  __AUTH_CONST.__objc_const: 0x2f78
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH.__objc_data: 0xf0
-  __DATA.__objc_ivar: 0x274
-  __DATA.__data: 0x4e8
+  __DATA.__objc_ivar: 0x278
+  __DATA.__data: 0x4f0
   __DATA.__common: 0x30
   __DATA_DIRTY.__objc_ivar: 0xc
   __DATA_DIRTY.__objc_data: 0x4b0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9FB77609-8391-3F22-B589-B667EAD26CD3
-  Functions: 490
-  Symbols:   2112
-  CStrings:  1672
+  UUID: 33DE3B8A-2BCC-3059-BBE3-6EF15E190DE9
+  Functions: 493
+  Symbols:   2124
+  CStrings:  1687
 
Symbols:
+ -[MemoryResourceException bundleVersion]
+ -[RMECacheEnumerator deleteFilesOlderThanThreshold:]
+ GCC_except_table23
+ GCC_except_table27
+ _CFBundleGetValueForInfoDictionaryKey
+ _MREMetaDataBundleVersionKey
+ _OBJC_IVAR_$_MemoryResourceException._bundleVersion
+ ___block_literal_global.474
+ _extractBundleVersion
+ _kCFBundleVersionKey
+ _objc_msgSend$dateWithTimeInterval:sinceDate:
+ _objc_msgSend$removeItemAtURL:error:
- GCC_except_table22
- GCC_except_table26
- ___block_literal_global.470
Functions:
~ -[MemoryResourceException createMetaDataDict] : 1524 -> 1548
+ -[RMECacheEnumerator deleteFilesOlderThanThreshold:]
+ _extractBundleVersion
~ -[MemoryResourceException createLiteMetaDataDict] : 332 -> 356
~ +[MemoryResourceException resourceExceptionFromTask:error:] : 1444 -> 1508
~ -[MemoryResourceException initWithMetaDataDict:andMemoryGraph:withError:] : 3280 -> 3352
+ -[MemoryResourceException coalitionBundleID]
~ -[MemoryResourceException .cxx_destruct] : 272 -> 284
CStrings:
+ "Delete old RME file at URL (%@), fileDate=%@ < ageThresholdDate=%@"
+ "Deleted %i files older than provided threshold of %f secs"
+ "Failed to get file creation date for RME file at URL (%@) due to error: %@"
+ "Failed to get non-zero file creation date for RME file at URL (%@)"
+ "Failed to remove old RME file at URL (%@) due to error: %@"
+ "Found old RME file at URL (%@), fileDate=%@ < ageThresholdDate=%@, attempting deletion"
+ "MRE_BundleVersion"
+ "T@\"NSString\",R,V_bundleVersion"
+ "_bundleVersion"
+ "bundleVersion"
+ "dateWithTimeInterval:sinceDate:"
+ "deleteFilesOlderThanThreshold:"
+ "i24@0:8d16"
+ "removeItemAtURL:error:"

```
