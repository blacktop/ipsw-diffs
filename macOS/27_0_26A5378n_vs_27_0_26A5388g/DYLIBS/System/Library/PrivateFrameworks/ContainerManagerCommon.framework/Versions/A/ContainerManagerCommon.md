## ContainerManagerCommon

> `/System/Library/PrivateFrameworks/ContainerManagerCommon.framework/Versions/A/ContainerManagerCommon`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift5_capture`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-833.0.0.501.1
-  __TEXT.__text: 0xf653c
-  __TEXT.__objc_methlist: 0xaabc
-  __TEXT.__const: 0x1328
+833.0.3.0.0
+  __TEXT.__text: 0xf7a98
+  __TEXT.__objc_methlist: 0xab5c
+  __TEXT.__const: 0x1318
   __TEXT.__swift5_typeref: 0x6bb
-  __TEXT.__oslogstring: 0xcbb9
-  __TEXT.__cstring: 0x9c33
+  __TEXT.__oslogstring: 0xcdb1
+  __TEXT.__cstring: 0x9c62
   __TEXT.__constg_swiftt: 0x650
   __TEXT.__swift5_reflstr: 0x39a
   __TEXT.__swift5_fieldmd: 0x458

   __TEXT.__swift5_mpenum: 0x10
   __TEXT.__swift5_capture: 0x58
   __TEXT.__swift5_protos: 0x18
-  __TEXT.__gcc_except_tab: 0x21e0
+  __TEXT.__gcc_except_tab: 0x230c
   __TEXT.__ustring: 0x16c
-  __TEXT.__unwind_info: 0x2270
+  __TEXT.__unwind_info: 0x22a8
   __TEXT.__eh_frame: 0x5d8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__const: 0x440
   __DATA_CONST.__objc_classlist: 0x5b8
   __DATA_CONST.__objc_catlist: 0x28
-  __DATA_CONST.__objc_protolist: 0x528
+  __DATA_CONST.__objc_protolist: 0x530
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3620
+  __DATA_CONST.__objc_selrefs: 0x3668
   __DATA_CONST.__objc_protorefs: 0xc8
   __DATA_CONST.__objc_superrefs: 0x4a8
   __DATA_CONST.__objc_arraydata: 0x3c8
   __DATA_CONST.__got: 0x500
-  __AUTH_CONST.__const: 0x28b8
-  __AUTH_CONST.__cfstring: 0x5560
-  __AUTH_CONST.__objc_const: 0x16e98
+  __AUTH_CONST.__const: 0x2948
+  __AUTH_CONST.__cfstring: 0x55a0
+  __AUTH_CONST.__objc_const: 0x16f18
   __AUTH_CONST.__objc_dictobj: 0x3e8
   __AUTH_CONST.__objc_intobj: 0x1560
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH_CONST.__auth_got: 0x1128
   __AUTH.__objc_data: 0xcd0
   __AUTH.__data: 0xd0
-  __DATA.__objc_ivar: 0xbf4
-  __DATA.__data: 0x3b60
+  __DATA.__objc_ivar: 0xbfc
+  __DATA.__data: 0x3bc0
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0xd38
+  __DATA.__bss: 0xd58
   __DATA_DIRTY.__objc_data: 0x3070
   __DATA_DIRTY.__data: 0x450
-  __DATA_DIRTY.__bss: 0x860
+  __DATA_DIRTY.__bss: 0x850
   __DATA_DIRTY.__common: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 3621
-  Symbols:   8375
-  CStrings:  1966
+  Functions: 3635
+  Symbols:   8408
+  CStrings:  1978
 
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
+ GCC_except_table1555
+ GCC_except_table1702
+ GCC_except_table1706
+ GCC_except_table1865
+ GCC_except_table1871
+ GCC_except_table1973
+ GCC_except_table2109
+ GCC_except_table2259
+ GCC_except_table2276
+ GCC_except_table2277
+ GCC_except_table2342
+ GCC_except_table2387
+ GCC_except_table2408
+ GCC_except_table2477
+ GCC_except_table2489
+ GCC_except_table2555
+ GCC_except_table2567
+ GCC_except_table2592
+ GCC_except_table2619
+ GCC_except_table2644
+ GCC_except_table2647
+ GCC_except_table2654
+ GCC_except_table2702
+ GCC_except_table2706
+ GCC_except_table2875
+ GCC_except_table2878
+ GCC_except_table2955
+ OBJC_IVAR_$_MCMContainerClassPath._lock
+ OBJC_IVAR_$_MCMContainerClassPath._lock_caseSensitive
+ OBJC_IVAR_$_MCMContainerClassPath._lock_caseSensitiveDetermined
+ OBJC_IVAR_$_MCMContainerClassPath._lock_classURLCreated
+ OBJC_IVAR_$_MCMContainerClassPath._lock_supportsDataProtection
+ OBJC_IVAR_$_MCMContainerClassPath._lock_supportsDataProtectionDetermined
+ OBJC_IVAR_$_MCMContainerClassPath._lock_symlinkClassURLCreated
+ OBJC_IVAR_$_MCMContainerClassPath._pendingHintsLock
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
+ ___block_descriptor_48_e8_32s_e19_"MCMPOSIXUser"8?0l
+ ___block_descriptor_56_e8_32s40r48r_e17_B16?0"NSError"8l
+ ___block_descriptor_60_e8_32s40s48s_e5_v8?0l
+ ___block_descriptor_64_e8_32s40s48s56r_e17_B16?0"NSError"8l
+ _getCachedUID:GID:name:flush:onCacheMiss:.cacheByName
+ _getCachedUID:GID:name:flush:onCacheMiss:.cacheByUID
+ _getCachedUID:GID:name:flush:onCacheMiss:.cacheByUIDGID
+ _getCachedUID:GID:name:flush:onCacheMiss:.onceToken
+ _objc_msgSend$_getCachedUID:GID:name:flush:onCacheMiss:
+ _objc_msgSend$_posixUserWithUID:GID:name:
+ _objc_msgSend$_readPendingHints
+ _objc_msgSend$_writePendingHints:
+ _objc_msgSend$decrementPendingHint:
+ _objc_msgSend$incrementPendingHint:
+ _objc_msgSend$initWithUID:GID:mode:posixUser:isNull:
+ _objc_msgSend$naturalized
+ _objc_msgSend$numberWithUnsignedLong:
+ _objc_msgSend$withOpenFileDoBlock:
- +[MCMPOSIXUser _getCachedUID:flush:onCacheMiss:]
- +[MCMPOSIXUser _posixUserWithUID:name:useUID:]
- GCC_except_table1554
- GCC_except_table1701
- GCC_except_table1705
- GCC_except_table1864
- GCC_except_table1870
- GCC_except_table1971
- GCC_except_table2107
- GCC_except_table2257
- GCC_except_table2274
- GCC_except_table2275
- GCC_except_table2340
- GCC_except_table2385
- GCC_except_table2406
- GCC_except_table2475
- GCC_except_table2487
- GCC_except_table2553
- GCC_except_table2565
- GCC_except_table2590
- GCC_except_table2617
- GCC_except_table2640
- GCC_except_table2645
- GCC_except_table2652
- GCC_except_table2714
- GCC_except_table2862
- GCC_except_table2865
- GCC_except_table2941
- OBJC_IVAR_$_MCMContainerClassPath._caseSensitive
- OBJC_IVAR_$_MCMContainerClassPath._caseSensitiveDetermined
- OBJC_IVAR_$_MCMContainerClassPath._classURLCreated
- OBJC_IVAR_$_MCMContainerClassPath._supportsDataProtection
- OBJC_IVAR_$_MCMContainerClassPath._supportsDataProtectionDetermined
- OBJC_IVAR_$_MCMContainerClassPath._symlinkClassURLCreated
- ___33+[MCMPOSIXUser posixUserWithUID:]_block_invoke
- ___46+[MCMPOSIXUser _posixUserWithUID:name:useUID:]_block_invoke
- ___48+[MCMPOSIXUser _getCachedUID:flush:onCacheMiss:]_block_invoke
- ___block_descriptor_40_e22_"MCMPOSIXUser"12?0I8l
- ___block_descriptor_52_e8_32s40s_e5_v8?0l
- _getCachedUID:flush:onCacheMiss:.cache
- _getCachedUID:flush:onCacheMiss:.onceToken
- _objc_msgSend$_getCachedUID:flush:onCacheMiss:
- _objc_msgSend$_posixUserWithUID:name:useUID:
CStrings:
+ "23:41:39"
+ "@\"MCMPOSIXUser\"8@?0"
+ "Attempted to look up posix user with nil name."
+ "B16@?0@\"NSError\"8"
+ "Could not read pending hints, JSON decode failed; classPath = %@, error = %@"
+ "Could not read pending hints; classPath = %@, error = %@"
+ "Could not write pending hints, JSON encode failed; classPath = %@, error = %@"
+ "Could not write pending hints; classPath = %@, error = %@"
+ "Failed to naturalize POSIX user; user = %@"
+ "Jul  7 2026"
+ "MobileContainerManager-833.0.3~125"
+ "Pending hints xattr did not decode to a dictionary; classPath = %@, top-level type = %@"
+ "Removing [%@] xattr on [%@]"
+ "Unable to get user (%u/[%@]); error = %{public}s"
+ "Writing [%@] xattr to [%@]; value = %@"
+ "com.apple.containermanager.hints"
+ "dp"
- "21:14:46"
- "@\"MCMPOSIXUser\"12@?0I8"
- "Jun 29 2026"
- "MobileContainerManager-833.0.0.501.1~1"
- "Unable to get user (%u/[%@]/%{public}d); error = %{public}s"
```
