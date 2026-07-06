## IOKit

> `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit`

```diff

-  __TEXT.__text: 0xbc330
+  __TEXT.__text: 0xbc320
   __TEXT.__objc_methlist: 0x150
   __TEXT.__cstring: 0xf1e3
   __TEXT.__const: 0x10610
   __TEXT.__dlopen_cstrs: 0x57
   __TEXT.__oslogstring: 0x564f
   __TEXT.__gcc_except_tab: 0x578
-  __TEXT.__unwind_info: 0x2660
+  __TEXT.__unwind_info: 0x2668
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2600
+  __DATA_CONST.__const: 0x2640
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8

   __AUTH.__data: 0x78
   __DATA.__objc_ivar: 0x1c
   __DATA.__data: 0x5f0
-  __DATA.__bss: 0x648
+  __DATA.__bss: 0x660
   __DATA.__common: 0x100
   __DATA_DIRTY.__objc_data: 0xa0
   __DATA_DIRTY.__data: 0xc0
-  __DATA_DIRTY.__bss: 0x230
+  __DATA_DIRTY.__bss: 0x218
   __DATA_DIRTY.__common: 0xc
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
   - /usr/lib/system/libkxld.dylib
-  Functions: 3893
-  Symbols:   5659
+  Functions: 3895
+  Symbols:   5663
   CStrings:  4024
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__cstring : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__weak_got : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__got : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__weak_auth_got : content changed
~ __AUTH.__objc_data : content changed
~ __AUTH.__data : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
~ __DATA_DIRTY.__data : content changed
Symbols:
+ __IOHIDEventCopyDebugInfo
+ ___IOEthernetControllerSetDispatchQueue_block_invoke_3
+ ___IOEthernetControllerSetDispatchQueue_block_invoke_4
- __IOHIDEventDebugInfo
Functions:
~ _OSKextParseVersionString : 984 -> 976
~ _DoCFSerialize : 1668 -> 1660
~ _IOCFUnserializeparse : 3500 -> 3488
~ _getTag : 1100 -> 1108
~ __IODisplayCreateInfoDictionary : 6356 -> 6364
~ __ZN5kcgen8AdjustorI9Pointer32I12LittleEndianEE27adjustReferencesUsingInfoV2ERNSt3__16vectorIPvNS5_9allocatorIS7_EEEE : 2660 -> 2632
~ __ZN4TrieI10ExportInfoE17processExportNodeEPKhS3_S3_PciRNSt3__16vectorINS1_15EntryWithOffsetENS5_9allocatorIS7_EEEE : 564 -> 556
~ __ZNSt3__116__insertion_sortB9nqe220106INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPN4TrieI10ExportInfoE15EntryWithOffsetEEEvT1_SA_T0_ : 552 -> 540
~ __ZNSt3__126__insertion_sort_unguardedB9nqe220106INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPN4TrieI10ExportInfoE15EntryWithOffsetEEEvT1_SA_T0_ : 536 -> 544
~ __ZNSt3__127__insertion_sort_incompleteB9nqe220106INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPN4TrieI10ExportInfoE15EntryWithOffsetEEEbT1_SA_T0_ : 1172 -> 1160
~ __ZN5kcgen8AdjustorI9Pointer64I12LittleEndianEE27adjustReferencesUsingInfoV2ERNSt3__16vectorIPvNS5_9allocatorIS7_EEEE : 2660 -> 2632
~ ___macho_sect_in_lc : 324 -> 284
~ ___IOHIDPropertySaveToKeyWithSpecialKeys : 284 -> 276
~ ___IOHIDPropertyLoadFromKeyWithSpecialKeys : 228 -> 220
~ _OSKextCreatePrelinkedKernel : 16832 -> 16760
~ ___OSKextGetSegmentInfo : 668 -> 648
~ _IOEthernetControllerSetDispatchQueue : 380 -> 580
~ ___IOEthernetControllerSetDispatchQueue_block_invoke_2 : 24 -> 8
+ ___IOEthernetControllerSetDispatchQueue_block_invoke_3
+ _IOEthernetControllerRegisterBSDAttachCallback
~ _IOAVHDMIAudioClockRegenerationDataForLink : 236 -> 224
~ _IOAVVideoTimingGetITSource : 84 -> 92
~ __IOHIDEventSystemConnectionFilterEvent : 812 -> 824
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.MThar5/Sources/IOAVFamily_user/IOAV.cpp"
+ "OSKEXT_BUILD_DATE 16:11:41 Jun 27 2026"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qZ92ZE/Sources/IOAVFamily_user/IOAV.cpp"
- "OSKEXT_BUILD_DATE 00:30:14 Jun 11 2026"

```
