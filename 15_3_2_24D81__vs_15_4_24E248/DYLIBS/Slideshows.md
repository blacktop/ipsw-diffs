## Slideshows

> `/System/Library/PrivateFrameworks/Slideshows.framework/Versions/A/Slideshows`

```diff

-1557.21.0.0.0
-  __TEXT.__text: 0x22f274
+1557.24.0.0.0
+  __TEXT.__text: 0x22d29c
   __TEXT.__auth_stubs: 0x1aa0
-  __TEXT.__objc_methlist: 0x17654
-  __TEXT.__const: 0x6e50
+  __TEXT.__objc_methlist: 0x189d0
+  __TEXT.__const: 0x6dd0
   __TEXT.__cstring: 0x19758
-  __TEXT.__gcc_except_tab: 0x702c
+  __TEXT.__gcc_except_tab: 0x62f4
   __TEXT.__oslogstring: 0x3c2
-  __TEXT.__unwind_info: 0x7768
+  __TEXT.__unwind_info: 0x7240
   __TEXT.__objc_classname: 0x1e29
   __TEXT.__objc_methname: 0x2a522
   __TEXT.__objc_methtype: 0xda4a

   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x180
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9400
+  __DATA_CONST.__objc_selrefs: 0x94f0
   __DATA_CONST.__objc_protorefs: 0x58
   __DATA_CONST.__objc_superrefs: 0xac0
   __DATA_CONST.__objc_arraydata: 0x90
   __AUTH_CONST.__auth_got: 0xd68
   __AUTH_CONST.__const: 0xb6e0
   __AUTH_CONST.__cfstring: 0x17fa0
-  __AUTH_CONST.__objc_const: 0x304f0
+  __AUTH_CONST.__objc_const: 0x2e088
   __AUTH_CONST.__objc_doubleobj: 0x30
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0xf0

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxml2.2.dylib
-  UUID: 806F3DCA-325D-3487-9E25-5D6CA037E937
-  Functions: 9589
-  Symbols:   21803
+  UUID: D8CF666C-1AA1-30B8-9929-133EBFD19EA3
+  Functions: 9561
+  Symbols:   21727
   CStrings:  14984
 
Symbols:
+ +[DDXMLNode nodeFree:].cold.1
+ +[MPDocument keyedUnarchiverWithData:assetKeyDelegate:mediaProperties:error:].cold.2
+ +[MPDocument unarchiveDocumentFromData:withAssetKeyDelegate:andMediaProperties:error:].cold.2
+ +[MRUtilities isOpenGLDisplayMaskSupported].cold.1
+ +[OMSlideshow initialize].cold.1
+ +[OMSlideshow unarchiveSlideshowFromData:withMediaURLs:andMediaItemLookupDelegate:error:].cold.2
+ +[OMSlideshowManager defaultManager].cold.1
+ -[MEExporter exportToFile:withOptions:error:].cold.3
+ -[MEExporter exportToFile:withOptions:error:].cold.4
+ -[MEPluginHTML5 exportToFile:andOptions:error:].cold.2
+ -[NSCoder(MPSafeUnarchiving) _mp_enforceValue:isType:withError:key:classes:entityClass:].cold.1
+ -[NSCoder(MPSafeUnarchiving) _mp_enforceValue:isType:withError:key:classes:entityClass:].cold.2
+ -[NSCoder(MPSafeUnarchiving) _mp_enforceValue:isType:withError:key:classes:entityClass:].cold.3
+ -[NSCoder(MPSafeUnarchiving) _mp_handleException:forType:key:classes:entityClass:].cold.1
+ -[OMSlideshow _writeToDictionary].cold.2
+ -[OMSlideshow authorMarimbaDocumentWithStyle:mediaURLS:attributes:].cold.3
+ -[OMSlideshow authorMarimbaDocumentWithStyle:mediaURLS:attributes:].cold.4
+ -[OMSlideshow encodeWithCoder:].cold.2
+ -[OMSlideshow initWithCoder:].cold.2
+ -[OMSlideshowTheme supportedCustomTransitions].cold.1
+ MRIsAppleTV.cold.1
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ _ZN14FunctionParserIdE8SimplifyEv.cold.1
+ _ZN14FunctionParserIdEC2EP9ParseInfoIdE.cold.1
+ _ZN14FunctionParserIfE8SimplifyEv.cold.1
+ _ZN14FunctionParserIfEC2EP9ParseInfoIfE.cold.1
+ _ZN15OperationParserIdE8SimplifyEv.cold.1
+ _ZN15OperationParserIdE8SimplifyEv.cold.2
+ _ZN15OperationParserIdEC2EP9ParseInfoIdES3_.cold.1
+ _ZN15OperationParserIfE8SimplifyEv.cold.1
+ _ZN15OperationParserIfE8SimplifyEv.cold.2
+ _ZN15OperationParserIfEC2EP9ParseInfoIfES3_.cold.1
+ _ZN19FunctionInterpreterIdE8SimplifyEv.cold.1
+ _ZN19FunctionInterpreterIdEC2E12FunctionTypeRS0_.cold.1
+ _ZN19FunctionInterpreterIdEC2EP9ParseInfoIdE.cold.1
+ _ZN19FunctionInterpreterIdEC2EPKc.cold.1
+ _ZN19FunctionInterpreterIdEC2Ed.cold.1
+ _ZN19FunctionInterpreterIfE8SimplifyEv.cold.1
+ _ZN19FunctionInterpreterIfEC2E12FunctionTypeRS0_.cold.1
+ _ZN19FunctionInterpreterIfEC2EP9ParseInfoIfE.cold.1
+ _ZN19FunctionInterpreterIfEC2EPKc.cold.1
+ _ZN19FunctionInterpreterIfEC2Ef.cold.1
+ _ZN25TwoArgumentFunctionParserIdE8SimplifyEv.cold.1
+ _ZN25TwoArgumentFunctionParserIdE8SimplifyEv.cold.2
+ _ZN25TwoArgumentFunctionParserIfE8SimplifyEv.cold.1
+ _ZN25TwoArgumentFunctionParserIfE8SimplifyEv.cold.2
+ _ZNK14FunctionParserIdE8MakeCopyEv.cold.1
+ _ZNK14FunctionParserIfE8MakeCopyEv.cold.1
+ _ZNK15OperationParserIdE8MakeCopyEv.cold.1
+ _ZNK15OperationParserIfE8MakeCopyEv.cold.1
+ _ZNK25TwoArgumentFunctionParserIdE8MakeCopyEv.cold.1
+ _ZNK25TwoArgumentFunctionParserIfE8MakeCopyEv.cold.1
+ __ZNKSt9type_infoeqB8ne190102ERKS_
- GCC_except_table1252
- GCC_except_table1283
- GCC_except_table1285
- GCC_except_table1287
- GCC_except_table1289
- GCC_except_table1291
- GCC_except_table1293
- GCC_except_table1295
- GCC_except_table1297
- GCC_except_table1299
- GCC_except_table1301
- GCC_except_table1303
- GCC_except_table1305
- GCC_except_table1307
- GCC_except_table1309
- GCC_except_table1311
- GCC_except_table1313
- GCC_except_table1315
- GCC_except_table1317
- GCC_except_table1319
- GCC_except_table1321
- GCC_except_table1323
- GCC_except_table1325
- GCC_except_table1327
- GCC_except_table1329
- GCC_except_table1331
- GCC_except_table1333
- GCC_except_table1335
- GCC_except_table1337
- GCC_except_table1339
- GCC_except_table1352
- GCC_except_table1364
- GCC_except_table1366
- GCC_except_table1372
- GCC_except_table1374
- GCC_except_table1386
- GCC_except_table1389
- GCC_except_table1391
- GCC_except_table1393
- GCC_except_table1395
- GCC_except_table1397
- GCC_except_table1399
- GCC_except_table1401
- GCC_except_table1403
- GCC_except_table1405
- GCC_except_table1407
- GCC_except_table1409
- GCC_except_table1411
- GCC_except_table1413
- GCC_except_table1415
- GCC_except_table1417
- GCC_except_table1419
- GCC_except_table1421
- GCC_except_table1423
- GCC_except_table1437
- GCC_except_table1439
- GCC_except_table1441
- GCC_except_table1443
- GCC_except_table1445
- GCC_except_table1447
- GCC_except_table1449
- GCC_except_table1451
- GCC_except_table1453
- GCC_except_table1455
- GCC_except_table1457
- GCC_except_table1459
- GCC_except_table1461
- GCC_except_table1463
- GCC_except_table1465
- GCC_except_table1467
- GCC_except_table1469
- GCC_except_table1471
- GCC_except_table1473
- GCC_except_table1475
- GCC_except_table1477
- GCC_except_table1479
- GCC_except_table1481
- GCC_except_table1483
- GCC_except_table1485
- GCC_except_table1487
- GCC_except_table1489
- GCC_except_table1491
- GCC_except_table1493
- GCC_except_table1506
- GCC_except_table1518
- GCC_except_table1520
- GCC_except_table1526
- GCC_except_table1528
- GCC_except_table1540
- GCC_except_table1543
- GCC_except_table1545
- GCC_except_table1547
- GCC_except_table1549
- GCC_except_table1551
- GCC_except_table1553
- GCC_except_table1555
- GCC_except_table1557
- GCC_except_table1559
- GCC_except_table1561
- GCC_except_table1563
- GCC_except_table1565
- GCC_except_table1567
- GCC_except_table1569
- GCC_except_table1571
- GCC_except_table1573
- GCC_except_table1575
- GCC_except_table1577
- GCC_except_table1578
- GCC_except_table1583
- GCC_except_table1585
- GCC_except_table1587
- GCC_except_table1588
- GCC_except_table1590
- GCC_except_table1591
- GCC_except_table1596
- GCC_except_table1598
- GCC_except_table1600
- GCC_except_table1601
- GCC_except_table1603
- GCC_except_table1646
- GCC_except_table1690
- GCC_except_table279
- GCC_except_table281
- GCC_except_table618
- GCC_except_table706
- GCC_except_table708
- GCC_except_table913
- GCC_except_table915
- __ZNKSt9type_infoeqB8ne180100ERKS_
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SlideshowOSX/Marimba/Sources/Common/XML/DDXMLElement.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SlideshowOSX/Marimba/Sources/Common/XML/DDXMLNode.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SlideshowOSX/SlideshowFramework/OMSlideshow.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/SlideshowOSX/Marimba/Sources/Common/XML/DDXMLElement.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/SlideshowOSX/Marimba/Sources/Common/XML/DDXMLNode.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/SlideshowOSX/SlideshowFramework/OMSlideshow.m"

```
