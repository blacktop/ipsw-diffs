## libmobileassetd.dylib

> `/usr/lib/libmobileassetd.dylib`

```diff

-1487.100.105.502.1
-  __TEXT.__text: 0x2742f8
+1487.102.2.0.0
+  __TEXT.__text: 0x2745f8
   __TEXT.__auth_stubs: 0x2440
-  __TEXT.__objc_stubs: 0x22440
-  __TEXT.__objc_methlist: 0x10354
-  __TEXT.__const: 0x48ae
-  __TEXT.__cstring: 0x376fc
-  __TEXT.__objc_methname: 0x3d4bf
+  __TEXT.__objc_stubs: 0x22460
+  __TEXT.__objc_methlist: 0x10364
+  __TEXT.__const: 0x489e
+  __TEXT.__cstring: 0x3778c
+  __TEXT.__objc_methname: 0x3d4e3
   __TEXT.__objc_classname: 0xdf0
   __TEXT.__objc_methtype: 0x39d1
-  __TEXT.__oslogstring: 0x4b5af
+  __TEXT.__oslogstring: 0x4b650
   __TEXT.__gcc_except_tab: 0x2f34
   __TEXT.__dlopen_cstrs: 0x5a
   __TEXT.__swift5_typeref: 0x1093

   __DATA_CONST.__got: 0x680
   __DATA_CONST.__auth_ptr: 0xa20
   __DATA_CONST.__const: 0x6808
-  __DATA_CONST.__cfstring: 0x2b740
+  __DATA_CONST.__cfstring: 0x2b780
   __DATA_CONST.__objc_classlist: 0x3f0
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x97f8
+  __DATA_CONST.__objc_selrefs: 0x9800
   __DATA_CONST.__objc_arraydata: 0xb98
   __DATA_CONST.__objc_arrayobj: 0x270
   __DATA_CONST.__objc_intobj: 0x570

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 8332
-  Symbols:   15360
-  CStrings:  16679
+  Functions: 8333
+  Symbols:   15362
+  CStrings:  16683
 
Symbols:
+ -[MADAutoAssetControlManager isAtomicInstanceLatestToVendForSet:]
+ GCC_except_table415
+ GCC_except_table603
+ GCC_except_table605
+ GCC_except_table611
+ GCC_except_table613
+ GCC_except_table627
+ GCC_except_table759
+ __block_literal_global.4960
+ _objc_msgSend$isAtomicInstanceLatestToVendForSet:
- GCC_except_table414
- GCC_except_table602
- GCC_except_table604
- GCC_except_table610
- GCC_except_table612
- GCC_except_table626
- GCC_except_table758
- __block_literal_global.4954
CStrings:
+ "NIL"
+ "Starting built-in MobileAsset brain built Mar 11 2025 00:12:39"
+ "Starting downloaded MobileAsset brain (version: %@) built Mar 11 2025 00:12:39"
+ "[%{public}@]\n[CONSIDER-OVERFLOW-TRIM] {atomicInstanceTrimOverflowAfterPersisting} atomic-instance is latest-to-vend to set (keeping) | setAtomicInstance:%{public}@"
+ "[AUTO-SHORT-TERM][FILE]{%{public}@} attempted to persist SHORT-TERM atomic-instance file | filename:%{public}@ | setDescriptor:%{public}@ | setStatus:%{public}@ "
+ "isAtomicInstanceLatestToVendForSet:"
+ "unable to create SHORT-TERM lock atomic-instance file | filename:%@ | setDescriptor:%@ | errno:%i"
+ "{%@} An entry in latest-to-vend for set %@, %@, has latestDownloadedAtomicInstanceEntries that contain nil value. Entry: %@"
- "Starting built-in MobileAsset brain built Mar  3 2025 21:57:08"
- "Starting downloaded MobileAsset brain (version: %@) built Mar  3 2025 21:57:08"
- "[AUTO-SHORT-TERM][FILE]{_shortTermPersistSetStatus} created SHORT-TERM atomic-instance file | filename:%{public}@ | setDescriptor:%{public}@ | setStatus:%{public}@ "
- "unable to create SHORT-TERM lock atomic-instance file | filename:%@ | setDescriptor:%@"

```
