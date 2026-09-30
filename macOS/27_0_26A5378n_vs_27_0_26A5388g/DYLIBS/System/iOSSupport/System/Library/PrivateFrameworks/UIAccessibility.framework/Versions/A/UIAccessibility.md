## UIAccessibility

> `/System/iOSSupport/System/Library/PrivateFrameworks/UIAccessibility.framework/Versions/A/UIAccessibility`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-3234.2.0.0.0
-  __TEXT.__text: 0x68838
-  __TEXT.__objc_methlist: 0x6754
+3237.0.0.0.0
+  __TEXT.__text: 0x68474
+  __TEXT.__objc_methlist: 0x6794
   __TEXT.__const: 0x218
   __TEXT.__dlopen_cstrs: 0x162
   __TEXT.__gcc_except_tab: 0xbdc
-  __TEXT.__cstring: 0x6a29
-  __TEXT.__oslogstring: 0x2c21
+  __TEXT.__cstring: 0x6a50
+  __TEXT.__oslogstring: 0x2c07
   __TEXT.__ustring: 0x14
   __TEXT.__unwind_info: 0x19d0
   __TEXT.__objc_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0xa8
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5308
+  __DATA_CONST.__objc_selrefs: 0x5320
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0xe8
   __DATA_CONST.__objc_arraydata: 0x128
   __DATA_CONST.__got: 0xce8
   __AUTH_CONST.__const: 0x1208
-  __AUTH_CONST.__cfstring: 0x6100
-  __AUTH_CONST.__objc_const: 0x40d8
+  __AUTH_CONST.__cfstring: 0x6140
+  __AUTH_CONST.__objc_const: 0x40f8
   __AUTH_CONST.__objc_intobj: 0x4c8
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x48

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2532
-  Symbols:   6435
+  Functions: 2536
+  Symbols:   6441
   CStrings:  1131
 
Symbols:
+ -[NSObject(AXPrivCategory) _accessibilityLineForIndex:]
+ -[UITextAttachmentAccessibilityElement accessibilityImageDataSize]
+ -[UITextAttachmentAccessibilityElement accessibilityImageDataWithParameters:]
+ GCC_except_table1020
+ GCC_except_table1028
+ GCC_except_table1033
+ GCC_except_table1069
+ GCC_except_table1086
+ GCC_except_table1192
+ GCC_except_table1295
+ GCC_except_table1303
+ GCC_except_table1305
+ GCC_except_table1307
+ GCC_except_table1318
+ GCC_except_table1330
+ GCC_except_table1363
+ GCC_except_table1373
+ GCC_except_table1375
+ GCC_except_table1450
+ GCC_except_table1453
+ GCC_except_table1518
+ GCC_except_table1521
+ GCC_except_table1543
+ GCC_except_table1582
+ GCC_except_table1594
+ GCC_except_table1597
+ GCC_except_table1610
+ GCC_except_table1646
+ GCC_except_table1676
+ GCC_except_table1688
+ GCC_except_table1690
+ GCC_except_table1694
+ GCC_except_table1698
+ GCC_except_table1722
+ GCC_except_table1725
+ GCC_except_table1727
+ GCC_except_table1732
+ GCC_except_table1735
+ GCC_except_table1739
+ GCC_except_table1830
+ GCC_except_table1922
+ GCC_except_table1940
+ GCC_except_table2094
+ GCC_except_table2141
+ GCC_except_table2147
+ GCC_except_table2155
+ GCC_except_table2156
+ GCC_except_table2370
+ GCC_except_table2389
+ GCC_except_table2472
+ GCC_except_table913
+ GCC_except_table945
+ GCC_except_table976
+ GCC_except_table987
+ __UIAXRetainedAttachmentElement
+ _objc_msgSend$_accessibilityLineForIndex:
+ _objc_msgSend$attachment
- GCC_except_table1019
- GCC_except_table1027
- GCC_except_table1032
- GCC_except_table1068
- GCC_except_table1085
- GCC_except_table1191
- GCC_except_table1294
- GCC_except_table1302
- GCC_except_table1304
- GCC_except_table1306
- GCC_except_table1317
- GCC_except_table1329
- GCC_except_table1362
- GCC_except_table1371
- GCC_except_table1374
- GCC_except_table1449
- GCC_except_table1452
- GCC_except_table1517
- GCC_except_table1520
- GCC_except_table1542
- GCC_except_table1581
- GCC_except_table1593
- GCC_except_table1596
- GCC_except_table1609
- GCC_except_table1645
- GCC_except_table1675
- GCC_except_table1687
- GCC_except_table1689
- GCC_except_table1693
- GCC_except_table1697
- GCC_except_table1721
- GCC_except_table1724
- GCC_except_table1726
- GCC_except_table1731
- GCC_except_table1734
- GCC_except_table1738
- GCC_except_table1829
- GCC_except_table1921
- GCC_except_table1939
- GCC_except_table2091
- GCC_except_table2138
- GCC_except_table2143
- GCC_except_table2151
- GCC_except_table2152
- GCC_except_table2366
- GCC_except_table2385
- GCC_except_table2468
- GCC_except_table912
- GCC_except_table944
- GCC_except_table975
- GCC_except_table986
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.bbsH5m/Sources/AccessibilityFrameworks/Source/UIAccessibility/AXRemoteElement+UIAccessibility.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.bbsH5m/Sources/AccessibilityFrameworks/Source/UIAccessibility/NSBundle+UIAccessibilityLoader.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.bbsH5m/Sources/AccessibilityFrameworks/Source/UIAccessibility/NSObjectAccessibility.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.bbsH5m/Sources/AccessibilityFrameworks/Source/UIAccessibility/UIAccessibilityElementTraversal.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.bbsH5m/Sources/AccessibilityFrameworks/Source/UIAccessibility/UIAccessibilityNotification.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.bbsH5m/Sources/AccessibilityFrameworks/Source/UIAccessibility/UIAccessibilityOpaqueElementProvider.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.bbsH5m/Sources/AccessibilityFrameworks/Source/UIAccessibility/UIKitAccessibility.m"
+ "ImageAttachment-%lu"
+ "TextAttachment-%lu"
- "%ld"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uS7xWe/Sources/AccessibilityFrameworks/Source/UIAccessibility/AXRemoteElement+UIAccessibility.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uS7xWe/Sources/AccessibilityFrameworks/Source/UIAccessibility/NSBundle+UIAccessibilityLoader.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uS7xWe/Sources/AccessibilityFrameworks/Source/UIAccessibility/NSObjectAccessibility.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uS7xWe/Sources/AccessibilityFrameworks/Source/UIAccessibility/UIAccessibilityElementTraversal.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uS7xWe/Sources/AccessibilityFrameworks/Source/UIAccessibility/UIAccessibilityNotification.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uS7xWe/Sources/AccessibilityFrameworks/Source/UIAccessibility/UIAccessibilityOpaqueElementProvider.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uS7xWe/Sources/AccessibilityFrameworks/Source/UIAccessibility/UIKitAccessibility.m"
- "RequestAttributeValue"
```
