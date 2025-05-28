## ContainerManagerCommon

> `/System/Library/PrivateFrameworks/ContainerManagerCommon.framework/ContainerManagerCommon`

```diff

-582.60.2.0.0
-  __TEXT.__text: 0xb2e44
+582.80.2.0.0
+  __TEXT.__text: 0xb315c
   __TEXT.__auth_stubs: 0x19f0
-  __TEXT.__objc_methlist: 0x6940
+  __TEXT.__objc_methlist: 0x6950
   __TEXT.__const: 0x530
   __TEXT.__oslogstring: 0xd405
   __TEXT.__cstring: 0xd1e2
-  __TEXT.__gcc_except_tab: 0x1e04
+  __TEXT.__gcc_except_tab: 0x1e00
   __TEXT.__ustring: 0x43c
   __TEXT.__dlopen_cstrs: 0x66
-  __TEXT.__unwind_info: 0x194c
+  __TEXT.__unwind_info: 0x1944
   __TEXT.__objc_classname: 0x17f3
-  __TEXT.__objc_methname: 0xf3f4
-  __TEXT.__objc_methtype: 0x32e2
-  __TEXT.__objc_stubs: 0x9c60
+  __TEXT.__objc_methname: 0xf4ce
+  __TEXT.__objc_methtype: 0x3304
+  __TEXT.__objc_stubs: 0x9c80
   __DATA_CONST.__got: 0x138
-  __DATA_CONST.__const: 0x1598
+  __DATA_CONST.__const: 0x15c0
   __DATA_CONST.__objc_classlist: 0x528
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x280
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xf190
-  __DATA_CONST.__objc_selrefs: 0x2ac8
+  __DATA_CONST.__objc_const: 0xf1e0
+  __DATA_CONST.__objc_selrefs: 0x2ad0
   __DATA_CONST.__objc_arraydata: 0x250
   __AUTH_CONST.__const: 0x600
   __AUTH_CONST.__cfstring: 0x6200

   __DATA.__objc_protorefs: 0x18
   __DATA.__objc_classrefs: 0x5c8
   __DATA.__objc_superrefs: 0x480
-  __DATA.__objc_ivar: 0x900
+  __DATA.__objc_ivar: 0x908
   __DATA.__data: 0x1f28
   __DATA.__crash_info: 0x40
   __DATA.__bss: 0x108

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsandbox.1.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 2392
-  Symbols:   9213
-  CStrings:  4989
+  Functions: 2393
+  Symbols:   9219
+  CStrings:  4993
 
Symbols:
+ +[MCMContainerSchema containerSchemaWithMetadata:finalContainerPath:dataProtectionClass:libraryRepair:]
+ +[MCMContainerSchemaActionBase _resolveArguments:toSourcePathArgument:destPathArgument:destFinalPathArgument:context:]
+ +[MCMContainerSchemaContext contextWithHomeDirectoryURL:containerPath:finalContainerPath:POSIXMode:POSIXOwner:containerClass:dataProtectionClass:libraryRepair:identifier:]
+ -[MCMContainerSchema initWithMetadata:finalContainerPath:dataProtectionClass:libraryRepair:]
+ -[MCMContainerSchemaActionCopy initWithSourcePathArgument:destinationPathArgument:destFinalPathArgument:context:]
+ -[MCMContainerSchemaActionCopyContents initWithSourcePathArgument:destinationPathArgument:destFinalPathArgument:context:]
+ -[MCMContainerSchemaActionMove initWithSourcePathArgument:destinationPathArgument:destFinalPathArgument:context:]
+ -[MCMContainerSchemaActionMoveContents initWithSourcePathArgument:destinationPathArgument:destFinalPathArgument:context:]
+ -[MCMContainerSchemaActionSymlink initWithSourcePathArgument:destinationPathArgument:destFinalPathArgument:context:]
+ -[MCMContainerSchemaContext finalContainerPath]
+ -[MCMContainerSchemaContext initWithHomeDirectoryURL:containerPath:finalContainerPath:POSIXMode:POSIXOwner:containerClass:dataProtectionClass:libraryRepair:identifier:]
+ GCC_except_table1184
+ GCC_except_table1210
+ GCC_except_table1266
+ GCC_except_table1404
+ GCC_except_table1442
+ GCC_except_table1448
+ GCC_except_table1451
+ GCC_except_table1454
+ GCC_except_table1468
+ GCC_except_table1474
+ GCC_except_table1510
+ GCC_except_table1516
+ GCC_except_table1649
+ GCC_except_table1661
+ GCC_except_table1781
+ GCC_except_table1799
+ GCC_except_table1876
+ GCC_except_table1928
+ GCC_except_table1954
+ GCC_except_table1975
+ GCC_except_table1979
+ GCC_except_table2003
+ GCC_except_table2013
+ GCC_except_table2037
+ GCC_except_table2066
+ GCC_except_table2084
+ GCC_except_table2088
+ GCC_except_table2090
+ GCC_except_table2094
+ GCC_except_table2149
+ GCC_except_table2232
+ GCC_except_table2283
+ GCC_except_table2347
+ _OBJC_IVAR_$_MCMContainerSchemaActionSymlink._finalLinkURL
+ _OBJC_IVAR_$_MCMContainerSchemaContext._finalContainerPath
+ ___Block_byref_object_copy_.10903
+ ___Block_byref_object_copy_.11439
+ ___Block_byref_object_copy_.12245
+ ___Block_byref_object_copy_.12818
+ ___Block_byref_object_copy_.5837
+ ___Block_byref_object_copy_.6188
+ ___Block_byref_object_copy_.7242
+ ___Block_byref_object_copy_.7364
+ ___Block_byref_object_copy_.7526
+ ___Block_byref_object_copy_.8082
+ ___Block_byref_object_copy_.9766
+ ___Block_byref_object_dispose_.10904
+ ___Block_byref_object_dispose_.11440
+ ___Block_byref_object_dispose_.12246
+ ___Block_byref_object_dispose_.12819
+ ___Block_byref_object_dispose_.5838
+ ___Block_byref_object_dispose_.6189
+ ___Block_byref_object_dispose_.7243
+ ___Block_byref_object_dispose_.7365
+ ___Block_byref_object_dispose_.7527
+ ___Block_byref_object_dispose_.8083
+ ___Block_byref_object_dispose_.9767
+ ___block_descriptor_56_e8_32s40s48s_e19_B24?0"NSURL"8^16ls32l8s40l8s48l8
+ ___block_literal_global.10067
+ ___block_literal_global.10912
+ ___block_literal_global.11253
+ ___block_literal_global.11683
+ ___block_literal_global.11897
+ ___block_literal_global.12564
+ ___block_literal_global.12650
+ ___block_literal_global.12671
+ ___block_literal_global.5371
+ ___block_literal_global.6092
+ ___block_literal_global.6669
+ ___block_literal_global.6935
+ ___block_literal_global.7726
+ ___block_literal_global.7833
+ ___block_literal_global.8896
+ ___block_literal_global.9811
+ __unnamed_array_storage.8792
+ _defaultManager.onceToken.7715
+ _objc_msgSend$_resolveArguments:toSourcePathArgument:destPathArgument:destFinalPathArgument:context:
+ _objc_msgSend$containerSchemaWithMetadata:finalContainerPath:dataProtectionClass:libraryRepair:
+ _objc_msgSend$contextWithHomeDirectoryURL:containerPath:finalContainerPath:POSIXMode:POSIXOwner:containerClass:dataProtectionClass:libraryRepair:identifier:
+ _objc_msgSend$finalContainerPath
+ _objc_msgSend$initWithHomeDirectoryURL:containerPath:finalContainerPath:POSIXMode:POSIXOwner:containerClass:dataProtectionClass:libraryRepair:identifier:
+ _objc_msgSend$initWithMetadata:finalContainerPath:dataProtectionClass:libraryRepair:
+ _objc_msgSend$initWithSourcePathArgument:destinationPathArgument:destFinalPathArgument:context:
+ _sharedInstance.instance.10410
+ _sharedInstance.onceToken.10409
+ _sharedInstance.onceToken.8480
- +[MCMContainerSchema containerSchemaWithMetadata:dataProtectionClass:libraryRepair:]
- +[MCMContainerSchemaActionBase _resolveArguments:toSourcePathArgument:destPathArgument:context:]
- +[MCMContainerSchemaContext contextWithHomeDirectoryURL:containerPath:POSIXMode:POSIXOwner:containerClass:dataProtectionClass:libraryRepair:identifier:]
- -[MCMContainerSchema initWithMetadata:dataProtectionClass:libraryRepair:]
- -[MCMContainerSchemaActionCopy initWithSourcePathArgument:destinationPathArgument:context:]
- -[MCMContainerSchemaActionCopyContents initWithSourcePathArgument:destinationPathArgument:context:]
- -[MCMContainerSchemaActionMove initWithSourcePathArgument:destinationPathArgument:context:]
- -[MCMContainerSchemaActionMoveContents initWithSourcePathArgument:destinationPathArgument:context:]
- -[MCMContainerSchemaActionSymlink initWithSourcePathArgument:destinationPathArgument:context:]
- -[MCMContainerSchemaContext initWithHomeDirectoryURL:containerPath:POSIXMode:POSIXOwner:containerClass:dataProtectionClass:libraryRepair:identifier:]
- GCC_except_table1183
- GCC_except_table1209
- GCC_except_table1265
- GCC_except_table1403
- GCC_except_table1441
- GCC_except_table1447
- GCC_except_table1450
- GCC_except_table1453
- GCC_except_table1467
- GCC_except_table1473
- GCC_except_table1509
- GCC_except_table1515
- GCC_except_table1648
- GCC_except_table1660
- GCC_except_table1780
- GCC_except_table1797
- GCC_except_table1875
- GCC_except_table1927
- GCC_except_table1953
- GCC_except_table1974
- GCC_except_table1978
- GCC_except_table2002
- GCC_except_table2012
- GCC_except_table2036
- GCC_except_table2065
- GCC_except_table2083
- GCC_except_table2087
- GCC_except_table2089
- GCC_except_table2093
- GCC_except_table2148
- GCC_except_table2231
- GCC_except_table2282
- GCC_except_table2346
- ___Block_byref_object_copy_.10894
- ___Block_byref_object_copy_.11430
- ___Block_byref_object_copy_.12236
- ___Block_byref_object_copy_.12809
- ___Block_byref_object_copy_.5833
- ___Block_byref_object_copy_.6184
- ___Block_byref_object_copy_.7236
- ___Block_byref_object_copy_.7356
- ___Block_byref_object_copy_.7518
- ___Block_byref_object_copy_.8074
- ___Block_byref_object_copy_.9762
- ___Block_byref_object_dispose_.10895
- ___Block_byref_object_dispose_.11431
- ___Block_byref_object_dispose_.12237
- ___Block_byref_object_dispose_.12810
- ___Block_byref_object_dispose_.5834
- ___Block_byref_object_dispose_.6185
- ___Block_byref_object_dispose_.7237
- ___Block_byref_object_dispose_.7357
- ___Block_byref_object_dispose_.7519
- ___Block_byref_object_dispose_.8075
- ___Block_byref_object_dispose_.9763
- ___block_literal_global.10062
- ___block_literal_global.10903
- ___block_literal_global.11244
- ___block_literal_global.11674
- ___block_literal_global.11888
- ___block_literal_global.12555
- ___block_literal_global.12641
- ___block_literal_global.12662
- ___block_literal_global.5365
- ___block_literal_global.6088
- ___block_literal_global.6665
- ___block_literal_global.6931
- ___block_literal_global.7718
- ___block_literal_global.7825
- ___block_literal_global.8889
- ___block_literal_global.9807
- __unnamed_array_storage.8784
- _defaultManager.onceToken.7707
- _objc_msgSend$_resolveArguments:toSourcePathArgument:destPathArgument:context:
- _objc_msgSend$containerSchemaWithMetadata:dataProtectionClass:libraryRepair:
- _objc_msgSend$contextWithHomeDirectoryURL:containerPath:POSIXMode:POSIXOwner:containerClass:dataProtectionClass:libraryRepair:identifier:
- _objc_msgSend$initWithHomeDirectoryURL:containerPath:POSIXMode:POSIXOwner:containerClass:dataProtectionClass:libraryRepair:identifier:
- _objc_msgSend$initWithMetadata:dataProtectionClass:libraryRepair:
- _objc_msgSend$initWithSourcePathArgument:destinationPathArgument:context:
- _sharedInstance.instance.10405
- _sharedInstance.onceToken.10404
- _sharedInstance.onceToken.8472
CStrings:
+ "\x14\x12"
+ "18:12:58"
+ "@44@0:8@16@24i32@36"
+ "@48@0:8@\"<MCMActionArgument>\"16@\"<MCMActionArgument>\"24@\"<MCMActionArgument>\"32@\"MCMContainerSchemaContext\"40"
+ "@80@0:8@16@24@32S40@44Q52i60@64@72"
+ "Dec 20 2023"
+ "MobileContainerManager-582.80.2~58"
+ "T@\"MCMContainerPath\",R,N,V_finalContainerPath"
+ "_finalContainerPath"
+ "_finalLinkURL"
+ "_resolveArguments:toSourcePathArgument:destPathArgument:destFinalPathArgument:context:"
+ "containerSchemaWithMetadata:finalContainerPath:dataProtectionClass:libraryRepair:"
+ "contextWithHomeDirectoryURL:containerPath:finalContainerPath:POSIXMode:POSIXOwner:containerClass:dataProtectionClass:libraryRepair:identifier:"
+ "finalContainerPath"
+ "initWithHomeDirectoryURL:containerPath:finalContainerPath:POSIXMode:POSIXOwner:containerClass:dataProtectionClass:libraryRepair:identifier:"
+ "initWithMetadata:finalContainerPath:dataProtectionClass:libraryRepair:"
+ "initWithSourcePathArgument:destinationPathArgument:destFinalPathArgument:context:"
+ "v56@0:8@16^@24^@32^@40@48"
- "\x13\x12"
- "07:21:41"
- "@36@0:8@16i24@28"
- "@40@0:8@\"<MCMActionArgument>\"16@\"<MCMActionArgument>\"24@\"MCMContainerSchemaContext\"32"
- "@72@0:8@16@24S32@36Q44i52@56@64"
- "MobileContainerManager-582.60.2~54"
- "Nov 12 2023"
- "_resolveArguments:toSourcePathArgument:destPathArgument:context:"
- "containerSchemaWithMetadata:dataProtectionClass:libraryRepair:"
- "contextWithHomeDirectoryURL:containerPath:POSIXMode:POSIXOwner:containerClass:dataProtectionClass:libraryRepair:identifier:"
- "initWithHomeDirectoryURL:containerPath:POSIXMode:POSIXOwner:containerClass:dataProtectionClass:libraryRepair:identifier:"
- "initWithMetadata:dataProtectionClass:libraryRepair:"
- "initWithSourcePathArgument:destinationPathArgument:context:"
- "v48@0:8@16^@24^@32@40"

```
