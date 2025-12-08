# 26.2 (23C52) .vs 26.2 (23C54)

## IPSWs

- `iPhone18,1_26.2_23C52_Restore.ipsw`
- `iPhone18,1_26.2_23C54_Restore.ipsw`

## Kernel

### Version

| iOS | Version | Build | Date |
| :-- | :------ | :---- | :--- |
| 26.2 *(23C52)* | 25.2.0 | 12377.62.10~1 | Tue, 18Nov2025 21:11:04 PST |
| 26.2 *(23C54)* | 25.2.0 | 12377.62.10~1 | Tue, 18Nov2025 21:11:04 PST |

### iBoot

| iOS | Version |
| :-- | :------ |
| 26.2 *(23C52)* | iBoot-13822.62.5 |
| 26.2 *(23C54)* | iBoot-13822.62.5 |

## DSC

### WebKit

| iOS | Version |
| :-- | :------ |
| 26.2 *(23C52)* | 623.1.14.10.9 |
| 26.2 *(23C54)* | 623.1.14.10.9 |

### Dylibs

#### ⬆️ Updated (2)

<details>
  <summary><i>View Updated</i></summary>

#### CoreTelephony

>  `/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`

```diff

-13126.1.0.0.0
+13126.1.1.0.0
   __TEXT.__text: 0x194a7c
   __TEXT.__auth_stubs: 0x1990
   __TEXT.__objc_methlist: 0x1b52c
   __TEXT.__const: 0x1012
   __TEXT.__gcc_except_tab: 0x1f534
-  __TEXT.__cstring: 0x1f9f4
+  __TEXT.__cstring: 0x1f9f7
   __TEXT.__oslogstring: 0x409e
   __TEXT.__swift5_typeref: 0x17
   __TEXT.__unwind_info: 0xd2b0

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  UUID: F7FFFAA4-62D0-303F-A640-334CBBBD8BCA
+  UUID: CD222D07-A3D8-3E50-9356-35D328D0A60D
   Functions: 11304
   Symbols:   38301
   CStrings:  17179
CStrings:
+ "13126.1.1"
+ "13126.1.1~1"
- "13126.1"
- "13126.1~63"

```

#### SpringBoardHome

>  `/System/Library/PrivateFrameworks/SpringBoardHome.framework/SpringBoardHome`

```diff

-178.103.0.0.0
-  __TEXT.__text: 0x3307b4
+178.104.0.0.0
+  __TEXT.__text: 0x330a50
   __TEXT.__auth_stubs: 0x2d50
-  __TEXT.__objc_methlist: 0x3c1cc
+  __TEXT.__objc_methlist: 0x3c204
   __TEXT.__const: 0x6844
   __TEXT.__cstring: 0x1b77f
   __TEXT.__gcc_except_tab: 0x3f9c

   __TEXT.__swift5_capture: 0xffc
   __TEXT.__swift_as_entry: 0x8
   __TEXT.__swift_as_ret: 0x4
-  __TEXT.__unwind_info: 0xe460
+  __TEXT.__unwind_info: 0xe478
   __TEXT.__eh_frame: 0x990
   __TEXT.__objc_classname: 0x6e0b
-  __TEXT.__objc_methname: 0x9ab4a
+  __TEXT.__objc_methname: 0x9ac0b
   __TEXT.__objc_methtype: 0x1950f
-  __TEXT.__objc_stubs: 0x59900
+  __TEXT.__objc_stubs: 0x59960
   __DATA_CONST.__got: 0x2288
   __DATA_CONST.__const: 0x9718
   __DATA_CONST.__objc_classlist: 0x1278
   __DATA_CONST.__objc_catlist: 0x128
   __DATA_CONST.__objc_protolist: 0xb28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1ba90
+  __DATA_CONST.__objc_selrefs: 0x1baa8
   __DATA_CONST.__objc_protorefs: 0x148
   __DATA_CONST.__objc_superrefs: 0xe40
   __DATA_CONST.__objc_arraydata: 0x6d8
   __AUTH_CONST.__auth_got: 0x16b8
   __AUTH_CONST.__const: 0x63c8
   __AUTH_CONST.__cfstring: 0x15f80
-  __AUTH_CONST.__objc_const: 0x55788
+  __AUTH_CONST.__objc_const: 0x55798
   __AUTH_CONST.__objc_intobj: 0x8e8
   __AUTH_CONST.__objc_doubleobj: 0xf0
   __AUTH_CONST.__objc_arrayobj: 0x240

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 284FD078-7C28-3FF4-BBBB-2DBE84BA3D23
-  Functions: 22587
-  Symbols:   64343
-  CStrings:  30747
+  UUID: FB9195D2-149B-3B46-A0F7-9A12EF096790
+  Functions: 22592
+  Symbols:   64356
+  CStrings:  30750
 
Symbols:
+ -[SBFolderController overrideParentViewControllerForCustomIconImageViewControllerForIconView:]
+ -[SBRootFolderController isPageManagementUITransitioningToVisible]
+ -[SBRootFolderController overrideParentViewControllerForCustomIconImageViewControllerForIconView:]
+ -[SBRootFolderController pageManagementParentViewControllerForCustomIconImageViewControllerForIconView:]
+ -[SBRootFolderView isPageManagementUITransitioningToVisible]
+ GCC_except_table189
+ GCC_except_table224
+ GCC_except_table257
+ ___101-[SBRootFolderController _internalDismissWidgetAddSheet:clearAddSheetViewController:notifyObservers:]_block_invoke.118
+ ___128-[SBRootFolderController presentWidgetEditingViewControllerFromViewController:withAllowedSizeClasses:allowingNonStackableItems:]_block_invoke.117
+ ___block_literal_global.291
+ _objc_msgSend$isPageManagementUITransitioningToVisible
+ _objc_msgSend$overrideParentViewControllerForCustomIconImageViewControllerForIconView:
+ _objc_msgSend$pageManagementParentViewControllerForCustomIconImageViewControllerForIconView:
- GCC_except_table188
- GCC_except_table256
- ___101-[SBRootFolderController _internalDismissWidgetAddSheet:clearAddSheetViewController:notifyObservers:]_block_invoke.116
- ___128-[SBRootFolderController presentWidgetEditingViewControllerFromViewController:withAllowedSizeClasses:allowingNonStackableItems:]_block_invoke.115
- ___block_literal_global.131
- ___block_literal_global.285
CStrings:
+ "isPageManagementUITransitioningToVisible"
+ "overrideParentViewControllerForCustomIconImageViewControllerForIconView:"
+ "pageManagementParentViewControllerForCustomIconImageViewControllerForIconView:"

```


</details>

## EOF
