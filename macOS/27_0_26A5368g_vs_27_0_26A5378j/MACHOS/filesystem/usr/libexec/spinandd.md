## spinandd

> `/usr/libexec/spinandd`

```diff

-  __TEXT.__text: 0xfc88
+  __TEXT.__text: 0x108fc
   __TEXT.__auth_stubs: 0x4d0
-  __TEXT.__objc_stubs: 0xc20
+  __TEXT.__objc_stubs: 0xcc0
   __TEXT.__objc_methlist: 0x3ec
   __TEXT.__const: 0x5e0
-  __TEXT.__objc_methname: 0xb37
-  __TEXT.__cstring: 0x3c94
+  __TEXT.__objc_methname: 0xbe7
+  __TEXT.__cstring: 0x4059
   __TEXT.__objc_classname: 0x59
   __TEXT.__objc_methtype: 0x3a4
-  __TEXT.__oslogstring: 0xb5b
-  __TEXT.__unwind_info: 0x330
+  __TEXT.__oslogstring: 0xbb5
+  __TEXT.__unwind_info: 0x350
+  __TEXT.__eh_frame: 0x38
   __DATA_CONST.__const: 0x298
-  __DATA_CONST.__cfstring: 0x340
+  __DATA_CONST.__cfstring: 0x3c0
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0x30
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__auth_got: 0x270
-  __DATA_CONST.__got: 0xd8
+  __DATA_CONST.__got: 0xe8
   __DATA_CONST.__auth_ptr: 0x10
   __DATA.__objc_const: 0x4d0
-  __DATA.__objc_selrefs: 0x400
+  __DATA.__objc_selrefs: 0x428
   __DATA.__objc_ivar: 0x1c
   __DATA.__objc_data: 0xf0
-  __DATA.__data: 0x1b0
-  __DATA.__bss: 0x52f0
+  __DATA.__data: 0x1c8
+  __DATA.__bss: 0x5300
   __DATA.__common: 0x270
   - /AppleInternal/Library/Frameworks/TapToRadarKit.framework/Versions/A/TapToRadarKit
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/Versions/A/CoreAnalytics
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 406
-  Symbols:   115
-  CStrings:  722
+  Functions: 433
+  Symbols:   117
+  CStrings:  751
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__objc_dictobj : content changed
~ __DATA_CONST.__auth_ptr : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_data : content changed
~ __DATA.__common : content changed
Symbols:
+ _OBJC_CLASS_$_NSData
+ _OBJC_CLASS_$_NSFileManager
CStrings:
+ "%@/rv_mismatch_%llu_b%u_p%u_lba%u"
+ "%s:%d:%s(): Dump_Page_Mismatch missing on internal build (b=%u p=%u)"
+ "%s:%d:%s(): Enabled RV full-compare mismatch injection on lba %u count down %u\n"
+ "%s:%d:%s(): Injecting RV full-compare mismatch on block %u page %u lba %u (flipping cache byte 0)\n"
+ "%s:%d:%s(): Internal build is missing Dump_Page_Mismatch callback"
+ "%s:%d:%s(): Jrnl program walker carries non-Jrnl LBA 0x%x"
+ "%s:%d:%s(): Logged Jrnl boot UECC block %u page %u pec %u time %llu (slot %d)\n"
+ "%s:%d:%s(): RV semantic mismatch block %u page %u lba %u data_match=%d sig_match=%d"
+ "%s:%d:%s(): RV semantic mismatch block %u page %u lba %u data_match=%d sig_match=%d sig_expected=0x%08x sig_actual=0x%08x data_first_diff_off=%zu\n"
+ "%s:%d:%s(): Skipping Jrnl boot UECC log for block 0 page 0 (reserved empty-slot sentinel)\n"
+ "/private/var/db/spinandd/dumps"
+ "140~367"
+ "Commands_Raw_Read_No_ECC"
+ "ErrInj_ReadVerifyCacheReady_Default"
+ "Gigadevice_Disable_ECC"
+ "Gigadevice_Enable_ECC"
+ "SPINAND: mkdir %{public}s failed: %{public}s"
+ "SPINAND: write %{public}s failed: %{public}s"
+ "Util_Log_Jrnl_Boot_UECC"
+ "Vendor_Interface_Disable_ECC_Dummy"
+ "Vendor_Interface_Enable_ECC_Dummy"
+ "Winbond_Disable_ECC"
+ "Winbond_Enable_ECC"
+ "_actual.bin"
+ "_expected.bin"
+ "createDirectoryAtPath:withIntermediateDirectories:attributes:error:"
+ "dataWithBytesNoCopy:length:freeWhenDone:"
+ "defaultManager"
+ "stringByAppendingString:"
+ "writeToFile:options:error:"
- "%s:%d:%s(): Disabling ECC is not supported yet"
- "%s:%d:%s(): Has_Internal_Content_Impl != ((void*)0)"
- "139~51"
- "Variant_Has_Internal_Content"
- "variant.c"

```
