## Metal

> `/System/Library/Frameworks/Metal.framework/Metal`

```diff

-  __TEXT.__text: 0x1e69d0
-  __TEXT.__objc_methlist: 0x1eb1c
-  __TEXT.__cstring: 0x23313
-  __TEXT.__gcc_except_tab: 0xc37c
+  __TEXT.__text: 0x1e6a3c
+  __TEXT.__objc_methlist: 0x1eb6c
+  __TEXT.__cstring: 0x233f9
+  __TEXT.__gcc_except_tab: 0xc39c
   __TEXT.__const: 0x2d790
   __TEXT.__oslogstring: 0x22d6
   __TEXT.__ustring: 0x1be
-  __TEXT.__unwind_info: 0x8ad0
+  __TEXT.__unwind_info: 0x8b18
   __TEXT.__eh_frame: 0x78
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_protolist: 0x490
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0x8e18
+  __DATA_CONST.__objc_selrefs: 0x8e40
   __DATA_CONST.__objc_protorefs: 0x68
   __DATA_CONST.__objc_superrefs: 0xc08
   __DATA_CONST.__objc_arraydata: 0x8
-  __DATA_CONST.__got: 0x9a8
+  __DATA_CONST.__got: 0xa30
   __AUTH_CONST.__const: 0x4f80
-  __AUTH_CONST.__cfstring: 0x12c00
-  __AUTH_CONST.__objc_const: 0x46b60
+  __AUTH_CONST.__cfstring: 0x12ca0
+  __AUTH_CONST.__objc_const: 0x46ba0
   __AUTH_CONST.__weak_auth_got: 0x30
   __AUTH_CONST.__objc_intobj: 0x2a0
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__auth_got: 0xe98
-  __AUTH.__objc_data: 0x40b0
-  __DATA.__objc_ivar: 0x2228
-  __DATA.__data: 0x4488
-  __DATA.__bss: 0x374
+  __AUTH.__objc_data: 0x4380
+  __DATA.__objc_ivar: 0x222c
+  __DATA.__data: 0x4498
+  __DATA.__bss: 0x37c
   __DATA.__common: 0x40
-  __DATA_DIRTY.__objc_data: 0x4380
-  __DATA_DIRTY.__data: 0xd0
-  __DATA_DIRTY.__bss: 0x320
+  __DATA_DIRTY.__objc_data: 0x40b0
+  __DATA_DIRTY.__data: 0xc8
+  __DATA_DIRTY.__bss: 0x318
   __DATA_DIRTY.__common: 0x11
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 13486
-  Symbols:   42126
-  CStrings:  6971
+  Functions: 13492
+  Symbols:   42143
+  CStrings:  6982
 
Sections:
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__weak_got : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__weak_auth_got : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_doubleobj : content changed
Symbols:
+ -[MTLCompileOptionsInternal floatingPointConversionRoundingMode]
+ -[MTLCompileOptionsInternal setFloatingPointConversionRoundingMode:]
+ -[_MTL4ComputeCommandEncoder flushCompressionMetadata]
+ -[_MTLBinaryArchive newLibraryInArchiveWithPosition:libraryPath:]
+ -[_MTLResource compressionMetadata]
+ GCC_except_table1001
+ GCC_except_table1002
+ GCC_except_table1005
+ GCC_except_table1013
+ GCC_except_table1014
+ GCC_except_table1018
+ GCC_except_table1024
+ GCC_except_table1040
+ GCC_except_table165
+ GCC_except_table197
+ GCC_except_table226
+ GCC_except_table233
+ GCC_except_table235
+ GCC_except_table240
+ GCC_except_table248
+ GCC_except_table262
+ GCC_except_table295
+ GCC_except_table298
+ GCC_except_table304
+ GCC_except_table311
+ GCC_except_table313
+ GCC_except_table314
+ GCC_except_table317
+ GCC_except_table320
+ GCC_except_table325
+ GCC_except_table331
+ GCC_except_table334
+ GCC_except_table335
+ GCC_except_table338
+ GCC_except_table348
+ GCC_except_table357
+ GCC_except_table360
+ GCC_except_table367
+ GCC_except_table384
+ GCC_except_table388
+ GCC_except_table393
+ GCC_except_table416
+ GCC_except_table418
+ GCC_except_table425
+ GCC_except_table432
+ GCC_except_table443
+ GCC_except_table450
+ GCC_except_table454
+ GCC_except_table461
+ GCC_except_table465
+ GCC_except_table468
+ GCC_except_table472
+ GCC_except_table475
+ GCC_except_table479
+ GCC_except_table482
+ GCC_except_table483
+ GCC_except_table486
+ GCC_except_table506
+ GCC_except_table527
+ GCC_except_table538
+ GCC_except_table557
+ GCC_except_table572
+ GCC_except_table573
+ GCC_except_table582
+ GCC_except_table587
+ GCC_except_table588
+ GCC_except_table593
+ GCC_except_table594
+ GCC_except_table600
+ GCC_except_table601
+ GCC_except_table605
+ GCC_except_table608
+ GCC_except_table622
+ GCC_except_table646
+ GCC_except_table649
+ GCC_except_table653
+ GCC_except_table654
+ GCC_except_table658
+ GCC_except_table659
+ GCC_except_table663
+ GCC_except_table669
+ GCC_except_table678
+ GCC_except_table679
+ GCC_except_table682
+ GCC_except_table685
+ GCC_except_table689
+ GCC_except_table690
+ GCC_except_table694
+ GCC_except_table699
+ GCC_except_table703
+ GCC_except_table776
+ GCC_except_table782
+ GCC_except_table789
+ GCC_except_table794
+ GCC_except_table802
+ GCC_except_table805
+ GCC_except_table806
+ GCC_except_table811
+ GCC_except_table829
+ GCC_except_table848
+ GCC_except_table859
+ GCC_except_table860
+ GCC_except_table872
+ GCC_except_table877
+ GCC_except_table878
+ GCC_except_table912
+ GCC_except_table913
+ GCC_except_table923
+ GCC_except_table934
+ GCC_except_table938
+ GCC_except_table944
+ GCC_except_table948
+ GCC_except_table954
+ GCC_except_table955
+ GCC_except_table964
+ GCC_except_table975
+ _MTLPipelinePerformanceKeyGASNativeInstructionCount
+ _OBJC_IVAR_$_MTLCompileOptionsInternal._floatingPointConversionRoundingMode
+ __ZL19newErrorWithMessageP8NSString22MTLDynamicLibraryError
+ __ZN22MTLArchiveLinkResolver15newLibraryAtPosEyyP8NSString
+ __ZN26MTLArchiveLinkResolverImpl15newLibraryAtPosEyyP8NSString
+ _objc_msgSend$floatingPointConversionRoundingMode
+ _objc_msgSend$newLibraryInArchiveWithPosition:libraryPath:
+ _objc_msgSend$setFloatingPointConversionRoundingMode:
- GCC_except_table1000
- GCC_except_table1003
- GCC_except_table1010
- GCC_except_table1011
- GCC_except_table1016
- GCC_except_table1022
- GCC_except_table1038
- GCC_except_table128
- GCC_except_table175
- GCC_except_table204
- GCC_except_table238
- GCC_except_table259
- GCC_except_table275
- GCC_except_table287
- GCC_except_table290
- GCC_except_table294
- GCC_except_table297
- GCC_except_table303
- GCC_except_table309
- GCC_except_table312
- GCC_except_table316
- GCC_except_table319
- GCC_except_table324
- GCC_except_table326
- GCC_except_table327
- GCC_except_table333
- GCC_except_table336
- GCC_except_table337
- GCC_except_table343
- GCC_except_table345
- GCC_except_table363
- GCC_except_table372
- GCC_except_table383
- GCC_except_table387
- GCC_except_table414
- GCC_except_table417
- GCC_except_table422
- GCC_except_table427
- GCC_except_table430
- GCC_except_table441
- GCC_except_table449
- GCC_except_table453
- GCC_except_table460
- GCC_except_table467
- GCC_except_table470
- GCC_except_table477
- GCC_except_table480
- GCC_except_table481
- GCC_except_table484
- GCC_except_table504
- GCC_except_table525
- GCC_except_table556
- GCC_except_table571
- GCC_except_table578
- GCC_except_table585
- GCC_except_table586
- GCC_except_table591
- GCC_except_table592
- GCC_except_table596
- GCC_except_table599
- GCC_except_table603
- GCC_except_table606
- GCC_except_table620
- GCC_except_table644
- GCC_except_table647
- GCC_except_table650
- GCC_except_table651
- GCC_except_table656
- GCC_except_table657
- GCC_except_table660
- GCC_except_table661
- GCC_except_table677
- GCC_except_table680
- GCC_except_table683
- GCC_except_table687
- GCC_except_table688
- GCC_except_table691
- GCC_except_table692
- GCC_except_table696
- GCC_except_table697
- GCC_except_table701
- GCC_except_table721
- GCC_except_table774
- GCC_except_table787
- GCC_except_table792
- GCC_except_table799
- GCC_except_table80
- GCC_except_table800
- GCC_except_table804
- GCC_except_table807
- GCC_except_table815
- GCC_except_table816
- GCC_except_table825
- GCC_except_table846
- GCC_except_table858
- GCC_except_table868
- GCC_except_table871
- GCC_except_table874
- GCC_except_table910
- GCC_except_table911
- GCC_except_table921
- GCC_except_table932
- GCC_except_table936
- GCC_except_table942
- GCC_except_table946
- GCC_except_table951
- GCC_except_table952
- GCC_except_table962
- GCC_except_table973
- GCC_except_table999
- __ZN22MTLArchiveLinkResolver15newLibraryAtPosEyy
- __ZN26MTLArchiveLinkResolverImpl15newLibraryAtPosEyy
CStrings:
+ "%@ is not a valid data plane data type"
+ "-fmetal-rtz-fp-conversion "
+ "01:59:26"
+ "GAS native instruction count"
+ "Jun 27 2026"
+ "Jun 27 2026 01:59:26"
+ "MTLDynamicLibrary AIR compilation failed"
+ "MTLTensorDataTypeMetalFloat4E2M1"
+ "MTLTensorDataTypeMetalFloat8E4M3"
+ "MTLTensorDataTypeMetalFloat8E5M2"
+ "MTLTensorDataTypeMetalFloat8UE8M0"
+ "floatingPointConversionRoundingMode"
+ "floatingPointConversionRoundingMode ="
- "17:36:47"
- "Jun  9 2026"
- "Jun  9 2026 17:36:47"
- "MTLTensorDataTypeFloat4E2M1"
- "MTLTensorDataTypeFloat8E4M3"
- "MTLTensorDataTypeFloat8E5M2"
- "MTLTensorDataTypeFloat8UE8M0"

```
