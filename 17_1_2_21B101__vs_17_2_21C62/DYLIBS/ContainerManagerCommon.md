## ContainerManagerCommon

> `/System/Library/PrivateFrameworks/ContainerManagerCommon.framework/ContainerManagerCommon`

```diff

-582.40.2.0.1
-  __TEXT.__text: 0xb28c8
+582.60.2.0.0
+  __TEXT.__text: 0xb2e44
   __TEXT.__auth_stubs: 0x19f0
-  __TEXT.__objc_methlist: 0x6918
-  __TEXT.__const: 0x540
-  __TEXT.__oslogstring: 0xd2b0
-  __TEXT.__cstring: 0xd1c3
-  __TEXT.__gcc_except_tab: 0x1dc4
+  __TEXT.__objc_methlist: 0x6940
+  __TEXT.__const: 0x530
+  __TEXT.__oslogstring: 0xd405
+  __TEXT.__cstring: 0xd1e2
+  __TEXT.__gcc_except_tab: 0x1e04
   __TEXT.__ustring: 0x43c
   __TEXT.__dlopen_cstrs: 0x66
-  __TEXT.__unwind_info: 0x1948
+  __TEXT.__unwind_info: 0x194c
   __TEXT.__objc_classname: 0x17f3
-  __TEXT.__objc_methname: 0xf33a
-  __TEXT.__objc_methtype: 0x32ba
-  __TEXT.__objc_stubs: 0x9c00
+  __TEXT.__objc_methname: 0xf3f4
+  __TEXT.__objc_methtype: 0x32e2
+  __TEXT.__objc_stubs: 0x9c60
   __DATA_CONST.__got: 0x138
-  __DATA_CONST.__const: 0x1570
+  __DATA_CONST.__const: 0x1598
   __DATA_CONST.__objc_classlist: 0x528
   __DATA_CONST.__objc_catlist: 0x20
-  __DATA_CONST.__objc_protolist: 0x278
+  __DATA_CONST.__objc_protolist: 0x280
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xefa0
-  __DATA_CONST.__objc_selrefs: 0x2ab0
+  __DATA_CONST.__objc_const: 0xf190
+  __DATA_CONST.__objc_selrefs: 0x2ac8
   __DATA_CONST.__objc_arraydata: 0x250
   __AUTH_CONST.__const: 0x600
-  __AUTH_CONST.__cfstring: 0x61e0
+  __AUTH_CONST.__cfstring: 0x6200
   __AUTH_CONST.__objc_const: 0x4480
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__objc_intobj: 0xf0

   __DATA.__objc_protorefs: 0x18
   __DATA.__objc_classrefs: 0x5c8
   __DATA.__objc_superrefs: 0x480
-  __DATA.__objc_ivar: 0x8f4
-  __DATA.__data: 0x1ec8
+  __DATA.__objc_ivar: 0x900
+  __DATA.__data: 0x1f28
   __DATA.__crash_info: 0x40
-  __DATA.__bss: 0xf8
+  __DATA.__bss: 0x108
   __DATA_DIRTY.__objc_data: 0x2c60
   __DATA_DIRTY.__data: 0x8
-  __DATA_DIRTY.__bss: 0x2f8
+  __DATA_DIRTY.__bss: 0x2f0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsandbox.1.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 2389
-  Symbols:   9193
-  CStrings:  4973
+  Functions: 2392
+  Symbols:   9213
+  CStrings:  4989
 
Symbols:
+ -[MCMCommandCreateOrLookupAppGroupByAppGroupIdentifier alwaysReturnPath]
+ -[MCMCommandCreateOrLookupAppGroupByAppGroupIdentifier clientIsAllowed]
+ -[MCMFSNode initWithINode:device:ctime:isDirectory:isSymlink:]
+ -[MCMFSNode isDirectory]
+ -[MCMFSNode isSymlink]
+ -[MCMFileManager fsSanitizedStringFromString:allowSpaces:]
+ GCC_except_table1028
+ GCC_except_table1032
+ GCC_except_table1033
+ GCC_except_table1183
+ GCC_except_table1209
+ GCC_except_table1265
+ GCC_except_table1403
+ GCC_except_table1441
+ GCC_except_table1453
+ GCC_except_table1467
+ GCC_except_table1473
+ GCC_except_table1509
+ GCC_except_table1515
+ GCC_except_table1648
+ GCC_except_table1660
+ GCC_except_table1780
+ GCC_except_table1797
+ GCC_except_table1798
+ GCC_except_table1875
+ GCC_except_table1927
+ GCC_except_table1953
+ GCC_except_table1974
+ GCC_except_table1978
+ GCC_except_table2002
+ GCC_except_table2012
+ GCC_except_table2036
+ GCC_except_table2065
+ GCC_except_table2083
+ GCC_except_table2087
+ GCC_except_table2089
+ GCC_except_table2093
+ GCC_except_table2148
+ GCC_except_table2231
+ GCC_except_table2282
+ GCC_except_table2346
+ GCC_except_table594
+ GCC_except_table595
+ GCC_except_table610
+ GCC_except_table661
+ GCC_except_table670
+ GCC_except_table676
+ GCC_except_table682
+ GCC_except_table685
+ GCC_except_table688
+ GCC_except_table717
+ GCC_except_table745
+ GCC_except_table790
+ GCC_except_table798
+ GCC_except_table802
+ GCC_except_table838
+ GCC_except_table839
+ GCC_except_table853
+ GCC_except_table857
+ GCC_except_table862
+ GCC_except_table867
+ GCC_except_table879
+ GCC_except_table886
+ GCC_except_table891
+ GCC_except_table897
+ GCC_except_table902
+ GCC_except_table910
+ GCC_except_table924
+ GCC_except_table934
+ GCC_except_table939
+ GCC_except_table945
+ GCC_except_table978
+ _OBJC_IVAR_$_MCMCommandCreateOrLookupAppGroupByAppGroupIdentifier._alwaysReturnPath
+ _OBJC_IVAR_$_MCMCommandCreateOrLookupAppGroupByAppGroupIdentifier._clientIsAllowed
+ _OBJC_IVAR_$_MCMFSNode._isDirectory
+ _OBJC_IVAR_$_MCMFSNode._isSymlink
+ __OBJC_$_PROP_LIST_MCMFSNode.87
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MCMFSNode
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MCMFSNode
+ __OBJC_$_PROTOCOL_REFS_MCMFSNode
+ __OBJC_LABEL_PROTOCOL_$_MCMFSNode
+ __OBJC_PROTOCOL_$_MCMFSNode
+ ___58-[MCMFileManager fsSanitizedStringFromString:allowSpaces:]_block_invoke
+ ___Block_byref_object_copy_.10894
+ ___Block_byref_object_copy_.11430
+ ___Block_byref_object_copy_.12236
+ ___Block_byref_object_copy_.12809
+ ___Block_byref_object_copy_.2103
+ ___Block_byref_object_copy_.2717
+ ___Block_byref_object_copy_.3305
+ ___Block_byref_object_copy_.3606
+ ___Block_byref_object_copy_.4315
+ ___Block_byref_object_copy_.5833
+ ___Block_byref_object_copy_.6184
+ ___Block_byref_object_copy_.7236
+ ___Block_byref_object_copy_.7356
+ ___Block_byref_object_copy_.7518
+ ___Block_byref_object_copy_.8074
+ ___Block_byref_object_copy_.9762
+ ___Block_byref_object_dispose_.10895
+ ___Block_byref_object_dispose_.11431
+ ___Block_byref_object_dispose_.12237
+ ___Block_byref_object_dispose_.12810
+ ___Block_byref_object_dispose_.2104
+ ___Block_byref_object_dispose_.2718
+ ___Block_byref_object_dispose_.3306
+ ___Block_byref_object_dispose_.3607
+ ___Block_byref_object_dispose_.4316
+ ___Block_byref_object_dispose_.5834
+ ___Block_byref_object_dispose_.6185
+ ___Block_byref_object_dispose_.7237
+ ___Block_byref_object_dispose_.7357
+ ___Block_byref_object_dispose_.7519
+ ___Block_byref_object_dispose_.8075
+ ___Block_byref_object_dispose_.9763
+ ___block_descriptor_56_e8_32s40r48r_e19_B24?0"NSURL"8^16ls32l8r40l8r48l8
+ ___block_literal_global.10062
+ ___block_literal_global.10903
+ ___block_literal_global.11244
+ ___block_literal_global.11674
+ ___block_literal_global.11888
+ ___block_literal_global.1203
+ ___block_literal_global.12555
+ ___block_literal_global.1261
+ ___block_literal_global.12641
+ ___block_literal_global.12662
+ ___block_literal_global.1358
+ ___block_literal_global.1681
+ ___block_literal_global.2213
+ ___block_literal_global.2548
+ ___block_literal_global.383
+ ___block_literal_global.4350
+ ___block_literal_global.5365
+ ___block_literal_global.6088
+ ___block_literal_global.6665
+ ___block_literal_global.6931
+ ___block_literal_global.7718
+ ___block_literal_global.7825
+ ___block_literal_global.8889
+ ___block_literal_global.9807
+ __unnamed_array_storage.1399
+ __unnamed_array_storage.1654
+ __unnamed_array_storage.2116
+ __unnamed_array_storage.3659
+ __unnamed_array_storage.8784
+ _defaultManager.onceToken.7707
+ _fsSanitizedStringFromString:allowSpaces:.forbiddenCharactersAllowingSpace
+ _fsSanitizedStringFromString:allowSpaces:.forbiddenCharactersDisallowingSpace
+ _fsSanitizedStringFromString:allowSpaces:.onceToken
+ _objc_msgSend$alwaysReturnPath
+ _objc_msgSend$clientIsAllowed
+ _objc_msgSend$fsSanitizedStringFromString:allowSpaces:
+ _objc_msgSend$initWithINode:device:ctime:isDirectory:isSymlink:
+ _objc_msgSend$isDirectory
+ _objc_msgSend$isSymlink
+ _sharedInstance.instance.10405
+ _sharedInstance.onceToken.10404
+ _sharedInstance.onceToken.8472
- -[MCMCommandCreateOrLookupAppGroupByAppGroupIdentifier iOSStyleHandling]
- -[MCMFSNode initWithINode:device:ctime:]
- -[MCMFileManager fsSanitizedStringFromString:]
- GCC_except_table1024
- GCC_except_table1030
- GCC_except_table1031
- GCC_except_table1181
- GCC_except_table1207
- GCC_except_table1263
- GCC_except_table1400
- GCC_except_table1438
- GCC_except_table1444
- GCC_except_table1464
- GCC_except_table1470
- GCC_except_table1506
- GCC_except_table1512
- GCC_except_table1645
- GCC_except_table1657
- GCC_except_table1777
- GCC_except_table1794
- GCC_except_table1795
- GCC_except_table1872
- GCC_except_table1924
- GCC_except_table1950
- GCC_except_table1971
- GCC_except_table1975
- GCC_except_table1999
- GCC_except_table2009
- GCC_except_table2033
- GCC_except_table2062
- GCC_except_table2080
- GCC_except_table2084
- GCC_except_table2086
- GCC_except_table2090
- GCC_except_table2145
- GCC_except_table2228
- GCC_except_table2279
- GCC_except_table2343
- GCC_except_table592
- GCC_except_table593
- GCC_except_table608
- GCC_except_table659
- GCC_except_table668
- GCC_except_table672
- GCC_except_table680
- GCC_except_table683
- GCC_except_table686
- GCC_except_table715
- GCC_except_table741
- GCC_except_table788
- GCC_except_table796
- GCC_except_table800
- GCC_except_table836
- GCC_except_table837
- GCC_except_table849
- GCC_except_table855
- GCC_except_table860
- GCC_except_table863
- GCC_except_table871
- GCC_except_table880
- GCC_except_table887
- GCC_except_table895
- GCC_except_table898
- GCC_except_table908
- GCC_except_table922
- GCC_except_table932
- GCC_except_table937
- GCC_except_table941
- GCC_except_table976
- _OBJC_IVAR_$_MCMCommandCreateOrLookupAppGroupByAppGroupIdentifier._iOSStyleHandling
- ___46-[MCMFileManager fsSanitizedStringFromString:]_block_invoke
- ___Block_byref_object_copy_.10830
- ___Block_byref_object_copy_.11365
- ___Block_byref_object_copy_.12171
- ___Block_byref_object_copy_.12744
- ___Block_byref_object_copy_.2054
- ___Block_byref_object_copy_.2660
- ___Block_byref_object_copy_.3247
- ___Block_byref_object_copy_.3547
- ___Block_byref_object_copy_.4256
- ___Block_byref_object_copy_.5774
- ___Block_byref_object_copy_.6125
- ___Block_byref_object_copy_.7171
- ___Block_byref_object_copy_.7291
- ___Block_byref_object_copy_.7453
- ___Block_byref_object_copy_.8009
- ___Block_byref_object_copy_.9698
- ___Block_byref_object_dispose_.10831
- ___Block_byref_object_dispose_.11366
- ___Block_byref_object_dispose_.12172
- ___Block_byref_object_dispose_.12745
- ___Block_byref_object_dispose_.2055
- ___Block_byref_object_dispose_.2661
- ___Block_byref_object_dispose_.3248
- ___Block_byref_object_dispose_.3548
- ___Block_byref_object_dispose_.4257
- ___Block_byref_object_dispose_.5775
- ___Block_byref_object_dispose_.6126
- ___Block_byref_object_dispose_.7172
- ___Block_byref_object_dispose_.7292
- ___Block_byref_object_dispose_.7454
- ___Block_byref_object_dispose_.8010
- ___Block_byref_object_dispose_.9699
- ___block_literal_global.10839
- ___block_literal_global.11180
- ___block_literal_global.11609
- ___block_literal_global.11823
- ___block_literal_global.1204
- ___block_literal_global.12490
- ___block_literal_global.12576
- ___block_literal_global.12597
- ___block_literal_global.1262
- ___block_literal_global.1359
- ___block_literal_global.1682
- ___block_literal_global.2164
- ___block_literal_global.2491
- ___block_literal_global.380
- ___block_literal_global.4291
- ___block_literal_global.5306
- ___block_literal_global.6029
- ___block_literal_global.6606
- ___block_literal_global.6873
- ___block_literal_global.7653
- ___block_literal_global.7760
- ___block_literal_global.8825
- ___block_literal_global.9743
- ___block_literal_global.9998
- __unnamed_array_storage.1400
- __unnamed_array_storage.1655
- __unnamed_array_storage.2067
- __unnamed_array_storage.3600
- __unnamed_array_storage.8720
- _defaultManager.onceToken.7642
- _fsSanitizedStringFromString:.forbiddenCharacters
- _fsSanitizedStringFromString:.onceToken
- _objc_msgSend$fsSanitizedStringFromString:
- _objc_msgSend$iOSStyleHandling
- _objc_msgSend$initWithINode:device:ctime:
- _sharedInstance.instance.10341
- _sharedInstance.onceToken.10340
- _sharedInstance.onceToken.8408
CStrings:
+ " "
+ "07:21:41"
+ "<%@: %p; inode = %llu, device = %d, ctime = %ld, isDirectory = %@, isSymlink = %@>"
+ "@\"NSString\"28@0:8@\"NSString\"16B24"
+ "@44@0:8Q16i24q28B36B40"
+ "Attempted to recover, but verification failed; identifier = [%@], uuid = %@, schemaVersion = %@"
+ "Cache entry failed verification, Data subdirectory doesn't target expectation; cacheEntry = %@, node = %@"
+ "Cache entry failed verification, could not stat Data subdirectory; cacheEntry = %@, error = [%@]"
+ "Invalid app group identifier [%{public}@]"
+ "MobileContainerManager-582.60.2~54"
+ "Nov 12 2023"
+ "TB,R,N,V_alwaysReturnPath"
+ "TB,R,N,V_clientIsAllowed"
+ "TB,R,N,V_isDirectory"
+ "TB,R,N,V_isSymlink"
+ "Tq,R,N"
+ "_alwaysReturnPath"
+ "_clientIsAllowed"
+ "_isDirectory"
+ "_isSymlink"
+ "alwaysReturnPath"
+ "clientIsAllowed"
+ "fsSanitizedStringFromString:allowSpaces:"
+ "initWithINode:device:ctime:isDirectory:isSymlink:"
+ "isDirectory"
+ "isSymlink"
- "02:33:54"
- "<%@: %p; inode = %llu, device = %d, ctime = %ld>"
- "@36@0:8Q16i24q28"
- "MobileContainerManager-582.40.2.0.1~310"
- "Oct 10 2023"
- "TB,R,N,V_iOSStyleHandling"
- "_iOSStyleHandling"
- "fsSanitizedStringFromString:"
- "iOSStyleHandling"
- "initWithINode:device:ctime:"

```
