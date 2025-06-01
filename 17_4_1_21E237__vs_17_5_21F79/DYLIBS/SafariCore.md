## SafariCore

> `/System/Library/PrivateFrameworks/SafariCore.framework/SafariCore`

```diff

-618.1.15.10.15
-  __TEXT.__text: 0xa299c
-  __TEXT.__auth_stubs: 0x1630
-  __TEXT.__objc_methlist: 0x7f30
-  __TEXT.__const: 0x332
-  __TEXT.__gcc_except_tab: 0x3d84
-  __TEXT.__cstring: 0xcca3
+618.2.12.10.9
+  __TEXT.__text: 0xa2d04
+  __TEXT.__auth_stubs: 0x1650
+  __TEXT.__objc_methlist: 0x7f50
+  __TEXT.__const: 0x362
+  __TEXT.__gcc_except_tab: 0x3dd4
+  __TEXT.__cstring: 0xccf3
   __TEXT.__ustring: 0x1e94
-  __TEXT.__oslogstring: 0x7d45
+  __TEXT.__oslogstring: 0x7d71
   __TEXT.__dlopen_cstrs: 0xf3
   __TEXT.__swift5_typeref: 0xf7
   __TEXT.__swift5_reflstr: 0xae

   __TEXT.__swift5_fieldmd: 0x6c
   __TEXT.__swift5_proto: 0xc
   __TEXT.__swift5_types: 0xc
-  __TEXT.__unwind_info: 0x39fc
+  __TEXT.__unwind_info: 0x3a88
   __TEXT.__eh_frame: 0x38
   __TEXT.__objc_classname: 0x131a
-  __TEXT.__objc_methname: 0x1bbb1
+  __TEXT.__objc_methname: 0x1bbef
   __TEXT.__objc_methtype: 0x2ed3
   __TEXT.__objc_stubs: 0xe1e0
   __DATA_CONST.__got: 0x388

   __DATA_CONST.__objc_protolist: 0xc8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0xa9b8
-  __DATA_CONST.__objc_selrefs: 0x51b8
+  __DATA_CONST.__objc_selrefs: 0x51d0
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_classrefs: 0x5c0
   __DATA_CONST.__objc_superrefs: 0x370
   __DATA_CONST.__objc_arraydata: 0x2630
-  __AUTH_CONST.__cfstring: 0x14f40
-  __AUTH_CONST.__const: 0x1958
+  __AUTH_CONST.__cfstring: 0x14f80
+  __AUTH_CONST.__const: 0x1978
   __AUTH_CONST.__objc_const: 0x3c18
   __AUTH_CONST.__objc_intobj: 0x288
   __AUTH_CONST.__objc_dictobj: 0x168
   __AUTH_CONST.__objc_arrayobj: 0x480
-  __AUTH_CONST.__auth_got: 0xb30
+  __AUTH_CONST.__auth_got: 0xb40
   __AUTH.__objc_data: 0x1788
   __AUTH.__data: 0x28
   __DATA.__got_weak: 0x8
   __DATA.__objc_ivar: 0x868
-  __DATA.__data: 0x9b8
+  __DATA.__data: 0x9a0
   __DATA.__bss: 0x590
   __DATA_DIRTY.__objc_data: 0x1360
-  __DATA_DIRTY.__data: 0x10
-  __DATA_DIRTY.__bss: 0x3d8
+  __DATA_DIRTY.__data: 0x28
+  __DATA_DIRTY.__bss: 0x3e0
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: A1256305-21DB-359F-8025-6B7A676BF53D
-  Functions: 4078
-  Symbols:   13507
-  CStrings:  10132
+  UUID: 52B8F899-9109-37DE-AE5D-415D77A9B38C
+  Functions: 4085
+  Symbols:   13529
+  CStrings:  10140
 
Symbols:
+ -[NSBundle(SafariCoreExtras) safari_isInSyncAgent]
+ -[NSString(SafariCoreExtras) safari_isSubpathOfPath:]
+ -[NSURL(SafariCoreExtras) safari_highLevelDomain]
+ -[WBSAnalyticsLogger reportAllProcessInfo:]
+ -[WBSAnalyticsLogger reportWebContentProcessInfo:]
+ -[WBSRemotelyUpdatableDataController _setUpDownloadedFileMonitoring].cold.1
+ GCC_except_table360
+ GCC_except_table362
+ GCC_except_table48
+ GCC_except_table50
+ ___43-[WBSAnalyticsLogger reportAllProcessInfo:]_block_invoke
+ ___46+[WBSFeatureAvailability shouldShowInternalUI]_block_invoke
+ ___50-[WBSAnalyticsLogger reportWebContentProcessInfo:]_block_invoke
+ ___block_literal_global.1076
+ ___block_literal_global.1078
+ ___block_literal_global.1087
+ ___block_literal_global.1089
+ ___block_literal_global.1091
+ ___block_literal_global.1136
+ ___block_literal_global.1163
+ ___block_literal_global.1165
+ ___block_literal_global.1167
+ ___block_literal_global.476
+ ___block_literal_global.57
+ ___block_literal_global.608
+ ___block_literal_global.626
+ ___block_literal_global.638
+ ___block_literal_global.647
+ ___block_literal_global.656
+ ___block_literal_global.675
+ ___block_literal_global.744
+ ___block_literal_global.76
+ ___block_literal_global.81
+ ___block_literal_global.839
+ ___block_literal_global.841
+ ___block_literal_global.875
+ ___block_literal_global.941
+ __unnamed_array_storage.481
+ __unnamed_array_storage.634
+ __unnamed_array_storage.635
+ __unnamed_array_storage.643
+ __unnamed_array_storage.644
+ __unnamed_array_storage.652
+ __unnamed_array_storage.653
+ __unnamed_array_storage.661
+ __unnamed_array_storage.662
+ __unnamed_array_storage.734
+ __unnamed_array_storage.735
+ __unnamed_array_storage.749
+ __unnamed_array_storage.750
+ __unnamed_array_storage.880
+ __unnamed_array_storage.881
+ _os_variant_has_internal_ui
+ _shouldShowInternalUI.hasInternalUI
+ _shouldShowInternalUI.onceToken
+ _strerror
- -[NSBundle(SafariCoreExtras) safari_isSafariApplicationPlatform]
- -[NSURL(SafariCoreExtras) safari_topLevelDomain]
- GCC_except_table40
- GCC_except_table49
- GCC_except_table51
- GCC_except_table81
- ___block_literal_global.1070
- ___block_literal_global.1072
- ___block_literal_global.1077
- ___block_literal_global.1079
- ___block_literal_global.1081
- ___block_literal_global.1130
- ___block_literal_global.1151
- ___block_literal_global.1153
- ___block_literal_global.1155
- ___block_literal_global.470
- ___block_literal_global.602
- ___block_literal_global.620
- ___block_literal_global.632
- ___block_literal_global.64
- ___block_literal_global.641
- ___block_literal_global.650
- ___block_literal_global.669
- ___block_literal_global.738
- ___block_literal_global.77
- ___block_literal_global.833
- ___block_literal_global.835
- ___block_literal_global.869
- ___block_literal_global.935
- __unnamed_array_storage.475
- __unnamed_array_storage.628
- __unnamed_array_storage.629
- __unnamed_array_storage.637
- __unnamed_array_storage.638
- __unnamed_array_storage.646
- __unnamed_array_storage.647
- __unnamed_array_storage.655
- __unnamed_array_storage.656
- __unnamed_array_storage.728
- __unnamed_array_storage.729
- __unnamed_array_storage.743
- __unnamed_array_storage.744
- __unnamed_array_storage.874
- __unnamed_array_storage.875
CStrings:
+ "/AppleInternal/Library/BuildRoots/0c8284c3-07b0-11ef-bffa-fa87d3da4027/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.5.Internal.sdk/usr/include/c++/v1/__memory/construct_at.h"
+ "/AppleInternal/Library/BuildRoots/0c8284c3-07b0-11ef-bffa-fa87d3da4027/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.5.Internal.sdk/usr/include/c++/v1/__tree"
+ "/AppleInternal/Library/BuildRoots/0c8284c3-07b0-11ef-bffa-fa87d3da4027/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.5.Internal.sdk/usr/include/c++/v1/__utility/exception_guard.h"
+ "/AppleInternal/Library/BuildRoots/0c8284c3-07b0-11ef-bffa-fa87d3da4027/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.5.Internal.sdk/usr/include/c++/v1/vector"
+ "Unable to open file (%s) for monitoring: %s"
+ "com.apple.Safari.AllProcessInfo"
+ "com.apple.Safari.WebContentProcessInfo"
+ "reportAllProcessInfo:"
+ "reportWebContentProcessInfo:"
+ "safari_highLevelDomain"
+ "safari_isInSyncAgent"
+ "safari_isSubpathOfPath:"
- "/AppleInternal/Library/BuildRoots/bf02bd17-e2a8-11ee-bddc-9ab3b1a34a63/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/include/c++/v1/__memory/construct_at.h"
- "/AppleInternal/Library/BuildRoots/bf02bd17-e2a8-11ee-bddc-9ab3b1a34a63/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/include/c++/v1/__tree"
- "/AppleInternal/Library/BuildRoots/bf02bd17-e2a8-11ee-bddc-9ab3b1a34a63/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/include/c++/v1/__utility/exception_guard.h"
- "/AppleInternal/Library/BuildRoots/bf02bd17-e2a8-11ee-bddc-9ab3b1a34a63/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/include/c++/v1/vector"
- "safari_isSafariApplicationPlatform"
- "safari_topLevelDomain"

```
