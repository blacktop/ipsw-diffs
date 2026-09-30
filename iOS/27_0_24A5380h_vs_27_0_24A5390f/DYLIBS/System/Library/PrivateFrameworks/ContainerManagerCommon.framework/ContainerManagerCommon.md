## ContainerManagerCommon

> `/System/Library/PrivateFrameworks/ContainerManagerCommon.framework/ContainerManagerCommon`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_protos`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`

```diff

-833.0.0.0.0
-  __TEXT.__text: 0xf1ad0
-  __TEXT.__objc_methlist: 0xac8c
-  __TEXT.__const: 0x1320
-  __TEXT.__cstring: 0x94b9
+833.0.3.0.0
+  __TEXT.__text: 0xf2ffc
+  __TEXT.__objc_methlist: 0xad2c
+  __TEXT.__const: 0x1330
+  __TEXT.__cstring: 0x94f0
   __TEXT.__swift5_typeref: 0x6d3
-  __TEXT.__oslogstring: 0xe509
+  __TEXT.__oslogstring: 0xe701
   __TEXT.__constg_swiftt: 0x670
   __TEXT.__swift5_reflstr: 0x3da
   __TEXT.__swift5_fieldmd: 0x4c8

   __TEXT.__swift5_mpenum: 0x10
   __TEXT.__swift5_capture: 0x78
   __TEXT.__swift5_protos: 0x18
-  __TEXT.__gcc_except_tab: 0x22e0
+  __TEXT.__gcc_except_tab: 0x240c
   __TEXT.__ustring: 0x16c
-  __TEXT.__unwind_info: 0x2518
+  __TEXT.__unwind_info: 0x2530
   __TEXT.__eh_frame: 0x5d8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1880
+  __DATA_CONST.__const: 0x18f8
   __DATA_CONST.__objc_classlist: 0x5c8
   __DATA_CONST.__objc_catlist: 0x28
-  __DATA_CONST.__objc_protolist: 0x520
+  __DATA_CONST.__objc_protolist: 0x528
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3700
+  __DATA_CONST.__objc_selrefs: 0x3750
   __DATA_CONST.__objc_protorefs: 0xc8
   __DATA_CONST.__objc_superrefs: 0x4b0
   __DATA_CONST.__objc_arraydata: 0x2e0
-  __DATA_CONST.__got: 0x438
+  __DATA_CONST.__got: 0x500
   __AUTH_CONST.__const: 0x12c8
-  __AUTH_CONST.__cfstring: 0x4ca0
-  __AUTH_CONST.__objc_const: 0x17050
+  __AUTH_CONST.__cfstring: 0x4ce0
+  __AUTH_CONST.__objc_const: 0x170d0
   __AUTH_CONST.__objc_dictobj: 0x118
   __AUTH_CONST.__objc_intobj: 0x1548
   __AUTH_CONST.__objc_arrayobj: 0xf0
   __AUTH_CONST.__auth_got: 0x12d0
-  __AUTH.__objc_data: 0xed8
-  __AUTH.__data: 0x198
-  __DATA.__objc_ivar: 0xc0c
-  __DATA.__data: 0x3ba0
+  __AUTH.__objc_data: 0xd70
+  __AUTH.__data: 0xd0
+  __DATA.__objc_ivar: 0xc14
+  __DATA.__data: 0x3bb0
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0xf88
-  __DATA.__common: 0x18
-  __DATA_DIRTY.__objc_data: 0x2f08
-  __DATA_DIRTY.__data: 0x308
-  __DATA_DIRTY.__bss: 0x618
-  __DATA_DIRTY.__common: 0x40
+  __DATA.__bss: 0xef8
+  __DATA_DIRTY.__objc_data: 0x3070
+  __DATA_DIRTY.__data: 0x448
+  __DATA_DIRTY.__bss: 0x6b0
+  __DATA_DIRTY.__common: 0x58
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 3639
-  Symbols:   8438
-  CStrings:  2000
+  Functions: 3653
+  Symbols:   8474
+  CStrings:  2012
 
Symbols:
+ +[MCMPOSIXUser _getCachedUID:GID:name:flush:onCacheMiss:]
+ +[MCMPOSIXUser _posixUserWithUID:GID:name:]
+ -[MCMContainerClassPath _readPendingHints]
+ -[MCMContainerClassPath _writePendingHints:]
+ -[MCMContainerClassPath decrementPendingHint:]
+ -[MCMContainerClassPath incrementPendingHint:]
+ -[MCMContainerClassPath pendingHint:]
+ -[MCMContainerClassPath resetPendingHint:]
+ -[MCMPOSIXPermission initWithUID:GID:mode:posixUser:isNull:]
+ -[MCMPOSIXUser naturalized]
+ -[MCMUserIdentity naturalized]
+ GCC_except_table1564
+ GCC_except_table1714
+ GCC_except_table1718
+ GCC_except_table1878
+ GCC_except_table1884
+ GCC_except_table1986
+ GCC_except_table2120
+ GCC_except_table2261
+ GCC_except_table2278
+ GCC_except_table2279
+ GCC_except_table2344
+ GCC_except_table2402
+ GCC_except_table2423
+ GCC_except_table2492
+ GCC_except_table2504
+ GCC_except_table2573
+ GCC_except_table2583
+ GCC_except_table2608
+ GCC_except_table2631
+ GCC_except_table2641
+ GCC_except_table2667
+ GCC_except_table2670
+ GCC_except_table2675
+ GCC_except_table2721
+ GCC_except_table2725
+ GCC_except_table2890
+ GCC_except_table2893
+ GCC_except_table2970
+ _OBJC_IVAR_$_MCMContainerClassPath._lock
+ _OBJC_IVAR_$_MCMContainerClassPath._lock_caseSensitive
+ _OBJC_IVAR_$_MCMContainerClassPath._lock_caseSensitiveDetermined
+ _OBJC_IVAR_$_MCMContainerClassPath._lock_classURLCreated
+ _OBJC_IVAR_$_MCMContainerClassPath._lock_supportsDataProtection
+ _OBJC_IVAR_$_MCMContainerClassPath._lock_supportsDataProtectionDetermined
+ _OBJC_IVAR_$_MCMContainerClassPath._lock_symlinkClassURLCreated
+ _OBJC_IVAR_$_MCMContainerClassPath._pendingHintsLock
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MCMContainerPathHasPendingHints
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MCMContainerPathHasPendingHints
+ __OBJC_$_PROTOCOL_REFS_MCMContainerPathHasPendingHints
+ __OBJC_LABEL_PROTOCOL_$_MCMContainerPathHasPendingHints
+ __OBJC_PROTOCOL_$_MCMContainerPathHasPendingHints
+ ___34+[MCMPOSIXUser posixUserWithName:]_block_invoke
+ ___37+[MCMPOSIXUser posixUserWithUID:GID:]_block_invoke
+ ___42-[MCMContainerClassPath _readPendingHints]_block_invoke
+ ___43+[MCMPOSIXUser _posixUserWithUID:GID:name:]_block_invoke
+ ___44-[MCMContainerClassPath _writePendingHints:]_block_invoke
+ ___57+[MCMPOSIXUser _getCachedUID:GID:name:flush:onCacheMiss:]_block_invoke
+ ___block_descriptor_48_e19_"MCMPOSIXUser"8?0l
+ ___block_descriptor_48_e8_32s_e19_"MCMPOSIXUser"8?0ls32l8
+ ___block_descriptor_56_e8_32s40r48r_e17_B16?0"NSError"8lr40l8r48l8s32l8
+ ___block_descriptor_60_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56r_e17_B16?0"NSError"8lr56l8s32l8s40l8s48l8
+ __getCachedUID:GID:name:flush:onCacheMiss:.cacheByName
+ __getCachedUID:GID:name:flush:onCacheMiss:.cacheByUID
+ __getCachedUID:GID:name:flush:onCacheMiss:.cacheByUIDGID
+ __getCachedUID:GID:name:flush:onCacheMiss:.onceToken
+ _objc_msgSend$_getCachedUID:GID:name:flush:onCacheMiss:
+ _objc_msgSend$_posixUserWithUID:GID:name:
+ _objc_msgSend$_readPendingHints
+ _objc_msgSend$_writePendingHints:
+ _objc_msgSend$dataUsingEncoding:
+ _objc_msgSend$decrementPendingHint:
+ _objc_msgSend$incrementPendingHint:
+ _objc_msgSend$initWithUID:GID:mode:posixUser:isNull:
+ _objc_msgSend$naturalized
+ _objc_msgSend$numberWithUnsignedLong:
+ _objc_msgSend$pendingHint:
+ _objc_msgSend$resetPendingHint:
+ _objc_msgSend$withOpenFileDoBlock:
- +[MCMPOSIXUser _getCachedUID:flush:onCacheMiss:]
- +[MCMPOSIXUser _posixUserWithUID:name:useUID:]
- GCC_except_table1563
- GCC_except_table1713
- GCC_except_table1717
- GCC_except_table1877
- GCC_except_table1883
- GCC_except_table1984
- GCC_except_table2118
- GCC_except_table2259
- GCC_except_table2276
- GCC_except_table2277
- GCC_except_table2342
- GCC_except_table2400
- GCC_except_table2421
- GCC_except_table2490
- GCC_except_table2502
- GCC_except_table2571
- GCC_except_table2581
- GCC_except_table2606
- GCC_except_table2629
- GCC_except_table2639
- GCC_except_table2663
- GCC_except_table2668
- GCC_except_table2673
- GCC_except_table2731
- GCC_except_table2877
- GCC_except_table2880
- GCC_except_table2956
- _OBJC_IVAR_$_MCMContainerClassPath._caseSensitive
- _OBJC_IVAR_$_MCMContainerClassPath._caseSensitiveDetermined
- _OBJC_IVAR_$_MCMContainerClassPath._classURLCreated
- _OBJC_IVAR_$_MCMContainerClassPath._supportsDataProtection
- _OBJC_IVAR_$_MCMContainerClassPath._supportsDataProtectionDetermined
- _OBJC_IVAR_$_MCMContainerClassPath._symlinkClassURLCreated
- ___33+[MCMPOSIXUser posixUserWithUID:]_block_invoke
- ___46+[MCMPOSIXUser _posixUserWithUID:name:useUID:]_block_invoke
- ___48+[MCMPOSIXUser _getCachedUID:flush:onCacheMiss:]_block_invoke
- ___block_descriptor_40_e22_"MCMPOSIXUser"12?0I8l
- ___block_descriptor_52_e8_32s40s_e5_v8?0ls32l8s40l8
- __getCachedUID:flush:onCacheMiss:.cache
- __getCachedUID:flush:onCacheMiss:.onceToken
- _objc_msgSend$_getCachedUID:flush:onCacheMiss:
- _objc_msgSend$_posixUserWithUID:name:useUID:
CStrings:
+ "02:13:54"
+ "@\"MCMPOSIXUser\"8@?0"
+ "Attempted to look up posix user with nil name."
+ "B16@?0@\"NSError\"8"
+ "Could not read pending hints, JSON decode failed; classPath = %@, error = %@"
+ "Could not read pending hints; classPath = %@, error = %@"
+ "Could not write pending hints, JSON encode failed; classPath = %@, error = %@"
+ "Could not write pending hints; classPath = %@, error = %@"
+ "Failed to naturalize POSIX user; user = %@"
+ "Jul  8 2026"
+ "MobileContainerManager-833.0.3~136"
+ "Pending hints xattr did not decode to a dictionary; classPath = %@, top-level type = %@"
+ "Removing [%@] xattr on [%@]"
+ "Unable to get user (%u/[%@]); error = %{public}s"
+ "Writing [%@] xattr to [%@]; value = %@"
+ "com.apple.containermanager.hints"
+ "dp"
- "02:57:11"
- "@\"MCMPOSIXUser\"12@?0I8"
- "Jun 23 2026"
- "MobileContainerManager-833~402"
- "Unable to get user (%u/[%@]/%{public}d); error = %{public}s"
```
