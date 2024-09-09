# 18.0 (22A5346a) .vs 18.0 (22A5350a)

## IPSWs

- `iPhone16,2_18.0_22A5346a_Restore.ipsw`
- `iPhone16,2_18.0_22A5350a_Restore.ipsw`

## Kernel

### Version

| iOS | Version | Build | Date |
| :-- | :------ | :---- | :--- |
| 18.0 *(22A5346a)* | 24.0.0 | 11215.2.5~59 | Thu, 08Aug2024 01:20:03 PDT |
| 18.0 *(22A5350a)* | 24.0.0 | 11215.2.5~59 | Thu, 08Aug2024 01:20:03 PDT |

## MachO

### ⬆️ Updated (5)

<details>
  <summary><i>View Updated</i></summary>

#### ClarityBoard

>  `/System/Library/CoreServices/ClarityBoard.app/ClarityBoard`

```diff

-101.0.0.0.0
-  __TEXT.__text: 0xfa97c
+101.0.1.0.0
+  __TEXT.__text: 0xfac68
   __TEXT.__auth_stubs: 0x35b0
-  __TEXT.__objc_stubs: 0x7be0
-  __TEXT.__objc_methlist: 0x2f5c
+  __TEXT.__objc_stubs: 0x7c40
+  __TEXT.__objc_methlist: 0x2f6c
   __TEXT.__const: 0x153b0
   __TEXT.__cstring: 0x41ec
-  __TEXT.__objc_methname: 0xbb51
+  __TEXT.__objc_methname: 0xbb7f
   __TEXT.__objc_classname: 0x817
   __TEXT.__objc_methtype: 0x2946
-  __TEXT.__oslogstring: 0x411e
+  __TEXT.__oslogstring: 0x41fe
   __TEXT.__gcc_except_tab: 0x178
   __TEXT.__ustring: 0x408
   __TEXT.__constg_swiftt: 0x3060

   __TEXT.__swift5_types: 0x250
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x3238
+  __TEXT.__unwind_info: 0x3248
   __TEXT.__eh_frame: 0x24d8
   __DATA_CONST.__auth_got: 0x1ae8
-  __DATA_CONST.__got: 0x1278
-  __DATA_CONST.__auth_ptr: 0x11a0
+  __DATA_CONST.__got: 0x1288
+  __DATA_CONST.__auth_ptr: 0x1140
   __DATA_CONST.__const: 0xb148
   __DATA_CONST.__cfstring: 0x1a00
   __DATA_CONST.__objc_classlist: 0x2b0

   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA.__objc_const: 0x8808
-  __DATA.__objc_selrefs: 0x2c20
+  __DATA.__objc_selrefs: 0x2c38
   __DATA.__objc_ivar: 0x31c
   __DATA.__objc_data: 0x3620
   __DATA.__data: 0x6090

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 4492
-  Symbols:   1810
-  CStrings:  3242
+  Functions: 4495
+  Symbols:   1812
+  CStrings:  3248
 
Symbols:
+ _AX_CameraBundleName
+ _AX_PhotosBundleName
CStrings:
+ "isRestricted"
+ "Unable to include application %@ because it is restricted."
+ ">>> Unable to look up record for application with bundle identifier %@, but no error was provided."
+ "Error getting application record for app with identifier %@: %@"
+ "isAppRestricted"
+ "applicationState"

```

#### AccessibilitySettings

>  `/System/Library/PreferenceBundles/AccessibilitySettings.bundle/AccessibilitySettings`

```diff

-1765.4.1.0.0
-  __TEXT.__text: 0x15eff0
+1765.4.2.0.0
+  __TEXT.__text: 0x15f05c
   __TEXT.__auth_stubs: 0x4200
   __TEXT.__objc_stubs: 0x22320
   __TEXT.__objc_methlist: 0x11a64

   __TEXT.__swift5_proto: 0x90
   __TEXT.__swift5_types: 0xa8
   __TEXT.__swift5_capture: 0x148
-  __TEXT.__unwind_info: 0x5048
+  __TEXT.__unwind_info: 0x5050
   __TEXT.__eh_frame: 0x170
   __DATA_CONST.__auth_got: 0x2110
   __DATA_CONST.__got: 0x20c0

```

#### assistantd

>  `/System/Library/PrivateFrameworks/AssistantServices.framework/assistantd`

```diff

-3400.161.5.11.2
-  __TEXT.__text: 0x369fcc
+3400.161.5.11.3
+  __TEXT.__text: 0x369fe8
   __TEXT.__auth_stubs: 0x3450
   __TEXT.__objc_stubs: 0x45000
   __TEXT.__objc_methlist: 0x1d37c
   __TEXT.__const: 0x10998
   __TEXT.__gcc_except_tab: 0x47c4
-  __TEXT.__cstring: 0x50fcb
+  __TEXT.__cstring: 0x50fca
   __TEXT.__oslogstring: 0x3e18f
   __TEXT.__objc_classname: 0x51b3
   __TEXT.__objc_methname: 0x5cf62

   __TEXT.__unwind_info: 0xa3a8
   __TEXT.__eh_frame: 0xe70
   __DATA_CONST.__auth_got: 0x1a38
-  __DATA_CONST.__got: 0x3af8
+  __DATA_CONST.__got: 0x3b00
   __DATA_CONST.__auth_ptr: 0x18
   __DATA_CONST.__const: 0x15010
   __DATA_CONST.__cfstring: 0x124e0

   - /usr/lib/libresolv.9.dylib
   - /usr/lib/libz.1.dylib
   Functions: 14403
-  Symbols:   2877
+  Symbols:   2878
   CStrings:  26964
 
Symbols:
+ _kAFMAStartupActivatedNotification
CStrings:
+ "2"
+ "MobileAssistantDaemons-3400.161.5.11.3"
- "MobileAssistantDaemons-3400.161.5.11.2"
- "27"

```

#### ClarityCamera

>  `/Applications/ClarityCamera.app/ClarityCamera`

```diff

-101.0.0.0.0
+101.0.1.0.0
   __TEXT.__text: 0x1daac
   __TEXT.__auth_stubs: 0x14f0
   __TEXT.__objc_methlist: 0x148

   __TEXT.__eh_frame: 0x588
   __DATA_CONST.__auth_got: 0xa78
   __DATA_CONST.__got: 0x570
-  __DATA_CONST.__auth_ptr: 0x828
+  __DATA_CONST.__auth_ptr: 0x840
   __DATA_CONST.__const: 0x1248
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x40

```

#### SafariWidgetExtension

>  `/Applications/MobileSafari.app/PlugIns/SafariWidgetExtension.appex/SafariWidgetExtension`

```diff

-7619.1.26.30.4
+7619.1.26.30.5
   __TEXT.__text: 0x452fc
   __TEXT.__auth_stubs: 0x13e0
   __TEXT.__cstring: 0x2a2a

   __TEXT.__eh_frame: 0x1d14
   __DATA_CONST.__auth_got: 0x9f0
   __DATA_CONST.__got: 0x4b8
-  __DATA_CONST.__auth_ptr: 0xbd8
+  __DATA_CONST.__auth_ptr: 0xbb0
   __DATA_CONST.__const: 0x1730
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8

```


</details>

## DSC

### WebKit

| iOS | Version |
| :-- | :------ |
| 18.0 *(22A5346a)* | 619.1.26.30.4 |
| 18.0 *(22A5350a)* | 619.1.26.30.5 |

### Dylibs

#### ⬆️ Updated (14)

<details>
  <summary><i>View Updated</i></summary>

#### PhotosSwiftUICore

>  `/System/Library/PrivateFrameworks/PhotosSwiftUICore.framework/PhotosSwiftUICore`

```diff

-702.0.220.0.0
+702.0.230.0.0
   __TEXT.__text: 0x26e1f4
   __TEXT.__auth_stubs: 0x5480
   __TEXT.__objc_methlist: 0x3a8

   __DATA_CONST.__objc_selrefs: 0x9d8
   __DATA_CONST.__objc_protorefs: 0xa0
   __AUTH_CONST.__auth_got: 0x2a48
-  __AUTH_CONST.__auth_ptr: 0x2848
+  __AUTH_CONST.__auth_ptr: 0x2880
   __AUTH_CONST.__const: 0x10b18
   __AUTH_CONST.__objc_const: 0x85f0
   __AUTH.__objc_data: 0x548

```

#### AuthenticationServicesCore

>  `/System/Library/PrivateFrameworks/AuthenticationServicesCore.framework/AuthenticationServicesCore`

```diff

-619.1.26.30.4
+619.1.26.30.5
   __TEXT.__text: 0xb6270
   __TEXT.__auth_stubs: 0x2280
   __TEXT.__objc_methlist: 0x2618

   __DATA_CONST.__objc_superrefs: 0xe0
   __DATA_CONST.__objc_arraydata: 0x10
   __AUTH_CONST.__auth_got: 0x1150
-  __AUTH_CONST.__auth_ptr: 0x6c8
+  __AUTH_CONST.__auth_ptr: 0x6c0
   __AUTH_CONST.__const: 0x50b8
   __AUTH_CONST.__cfstring: 0x1d80
   __AUTH_CONST.__objc_const: 0x7880

```

#### MobileSafari

>  `/System/Library/PrivateFrameworks/MobileSafari.framework/MobileSafari`

```diff

-619.1.26.30.4
-  __TEXT.__text: 0x38d87c
+619.1.26.30.5
+  __TEXT.__text: 0x38da28
   __TEXT.__auth_stubs: 0x4370
-  __TEXT.__objc_methlist: 0x11c80
+  __TEXT.__objc_methlist: 0x11cb8
   __TEXT.__const: 0xe104
-  __TEXT.__cstring: 0x1654c
+  __TEXT.__cstring: 0x1659c
   __TEXT.__gcc_except_tab: 0x6a1c
   __TEXT.__oslogstring: 0x3179
   __TEXT.__ustring: 0x2100

   __TEXT.__swift5_types: 0x5a4
   __TEXT.__swift5_protos: 0x9c
   __TEXT.__swift5_mpenum: 0x2c
-  __TEXT.__unwind_info: 0xcc38
+  __TEXT.__unwind_info: 0xcc50
   __TEXT.__eh_frame: 0x55a0
   __TEXT.__objc_classname: 0x290e
-  __TEXT.__objc_methname: 0x3b83d
+  __TEXT.__objc_methname: 0x3b893
   __TEXT.__objc_methtype: 0x9852
   __TEXT.__objc_stubs: 0x21000
   __DATA_CONST.__got: 0x1b38

   __DATA_CONST.__objc_catlist: 0x158
   __DATA_CONST.__objc_protolist: 0x548
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc0f0
+  __DATA_CONST.__objc_selrefs: 0xc118
   __DATA_CONST.__objc_protorefs: 0x140
   __DATA_CONST.__objc_superrefs: 0x688
   __DATA_CONST.__objc_arraydata: 0x258
   __AUTH_CONST.__auth_got: 0x21d0
-  __AUTH_CONST.__auth_ptr: 0x1d00
+  __AUTH_CONST.__auth_ptr: 0x1ed0
   __AUTH_CONST.__const: 0x127c8
   __AUTH_CONST.__cfstring: 0x8480
-  __AUTH_CONST.__objc_const: 0x31e60
+  __AUTH_CONST.__objc_const: 0x31e90
   __AUTH_CONST.__objc_intobj: 0x480
   __AUTH_CONST.__objc_doubleobj: 0x130
   __AUTH_CONST.__objc_arrayobj: 0x210
-  __AUTH.__objc_data: 0xa5a8
-  __AUTH.__data: 0x5f68
+  __AUTH.__objc_data: 0xaa98
+  __AUTH.__data: 0x5fb8
   __DATA.__objc_ivar: 0x17e0
   __DATA.__data: 0x9238
   __DATA.__objc_stublist: 0x18
   __DATA.__bss: 0x11e78
   __DATA.__common: 0xe00
-  __DATA_DIRTY.__objc_data: 0x3080
-  __DATA_DIRTY.__data: 0xa10
+  __DATA_DIRTY.__objc_data: 0x2b90
+  __DATA_DIRTY.__data: 0x9c0
   __DATA_DIRTY.__bss: 0x40
   __DATA_DIRTY.__common: 0x1e0
   - /System/Library/Frameworks/AppIntents.framework/AppIntents

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 17762
+  Functions: 17767
   Symbols:   8290
-  CStrings:  13259
+  CStrings:  13267
 
CStrings:
+ "_SFBrowsingAssistantListCell"
+ "listCellDidInsertCell:"
+ "_SFBrowsingAssistantSwitchCell"
+ "_SFBrowsingAssistantPopUpCell"
+ "T@\"_TtC12MobileSafari15BlurrableButton\",N,R,VhideButton"
+ "T@\"_TtC12MobileSafari10MainButton\",N,R,VleadingButton"
+ "T@\"_TtC12MobileSafari10MainButton\",N,R,VtrailingButton"
+ "listCellDidDeleteCell:"
+ "SFMediaPlaybackButton"
- "_TtCC12MobileSafari17BrowsingAssistant10SwitchCell"
- "_TtCC12MobileSafari17BrowsingAssistant9PopUpCell"
- "_TtCC12MobileSafari17BrowsingAssistant8ListCell"
- "_TtC12MobileSafariP33_D7BF0D66B145A49B4D76AB70D20D9C9919MediaPlaybackButton"

```

#### MobileSafariUI

>  `/System/Library/PrivateFrameworks/MobileSafariUI.framework/MobileSafariUI`

```diff

-619.1.26.30.4
-  __TEXT.__text: 0x2117d0
+619.1.26.30.5
+  __TEXT.__text: 0x2117c4
   __TEXT.__auth_stubs: 0x2ca0
   __TEXT.__objc_methlist: 0x199fc
   __TEXT.__const: 0x1398

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 12279
+  Functions: 12276
   Symbols:   13832
   CStrings:  19944
 

```

#### PhotosGraph

>  `/System/Library/PrivateFrameworks/PhotosGraph.framework/PhotosGraph`

```diff

-702.0.220.0.0
+702.0.230.0.0
   __TEXT.__text: 0x6a69d4
   __TEXT.__auth_stubs: 0x46f0
   __TEXT.__objc_methlist: 0x29f4c

   __DATA_CONST.__objc_superrefs: 0x1530
   __DATA_CONST.__objc_arraydata: 0x3a58
   __AUTH_CONST.__auth_got: 0x2390
-  __AUTH_CONST.__auth_ptr: 0x1208
+  __AUTH_CONST.__auth_ptr: 0x1278
   __AUTH_CONST.__const: 0x28298
   __AUTH_CONST.__cfstring: 0x26c60
   __AUTH_CONST.__objc_const: 0x6e148

```

#### WebBookmarksSwift

>  `/System/Library/PrivateFrameworks/WebBookmarksSwift.framework/WebBookmarksSwift`

```diff

-7619.1.26.30.4
+7619.1.26.30.5
   __TEXT.__text: 0x4cf28
   __TEXT.__auth_stubs: 0x1260
   __TEXT.__objc_methlist: 0x1c0

   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
   __AUTH_CONST.__auth_got: 0x938
-  __AUTH_CONST.__auth_ptr: 0x460
+  __AUTH_CONST.__auth_ptr: 0x490
   __AUTH_CONST.__const: 0x1818
   __AUTH_CONST.__objc_const: 0x9a0
   __AUTH.__objc_data: 0x38

```

#### Photos

>  `/System/Library/Frameworks/Photos.framework/Photos`

```diff

-702.0.220.0.0
-  __TEXT.__text: 0x25b168
+702.0.230.0.0
+  __TEXT.__text: 0x25b4d0
   __TEXT.__auth_stubs: 0x2870
-  __TEXT.__objc_methlist: 0x1f6a0
+  __TEXT.__objc_methlist: 0x1f6b0
   __TEXT.__const: 0xf30
   __TEXT.__constg_swiftt: 0x1dc
   __TEXT.__swift5_typeref: 0x290

   __TEXT.__cstring: 0x2839b
   __TEXT.__swift5_capture: 0x6c
   __TEXT.__gcc_except_tab: 0x8e7c
-  __TEXT.__oslogstring: 0x1a45d
+  __TEXT.__oslogstring: 0x1a569
   __TEXT.__ustring: 0x4
   __TEXT.__dlopen_cstrs: 0x47
   __TEXT.__unwind_info: 0x7f00
   __TEXT.__eh_frame: 0x260
   __TEXT.__objc_classname: 0x32d7
-  __TEXT.__objc_methname: 0x62e09
+  __TEXT.__objc_methname: 0x62e3f
   __TEXT.__objc_methtype: 0x67f4
-  __TEXT.__objc_stubs: 0x356c0
+  __TEXT.__objc_stubs: 0x35700
   __DATA_CONST.__got: 0x2438
   __DATA_CONST.__const: 0x7478
   __DATA_CONST.__objc_classlist: 0xcb8
   __DATA_CONST.__objc_catlist: 0x70
   __DATA_CONST.__objc_protolist: 0x2e0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x115d8
+  __DATA_CONST.__objc_selrefs: 0x115e8
   __DATA_CONST.__objc_protorefs: 0x40
   __DATA_CONST.__objc_superrefs: 0xa68
   __DATA_CONST.__objc_arraydata: 0x908

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 12546
-  Symbols:   15173
-  CStrings:  22213
+  Functions: 12547
+  Symbols:   15174
+  CStrings:  22220
 
CStrings:
+ "incomingDirectoryPath"
+ "Will remove file at path: %@, for UUID:%@"
+ "_filePathIsInIncomingDirectory:"
+ "Failed to remove file at path: %@, for UUID:%{public}@ %@"
+ "File not in Incoming, skipping deletion: %@"
+ "File not in Incoming, skipping deletion: %@, for UUID:%{public}@"
+ "Unable to get relationship between incoming dir and %@: %@"

```

#### SafariServices

>  `/System/Library/Frameworks/SafariServices.framework/SafariServices`

```diff

-619.1.26.30.4
-  __TEXT.__text: 0x189478
+619.1.26.30.5
+  __TEXT.__text: 0x1893b0
   __TEXT.__auth_stubs: 0x18e0
   __TEXT.__objc_methlist: 0x1531c
   __TEXT.__const: 0x2a56
   __TEXT.__cstring: 0xee1e
-  __TEXT.__gcc_except_tab: 0xdb54
+  __TEXT.__gcc_except_tab: 0xdb30
   __TEXT.__oslogstring: 0x7e6c
   __TEXT.__ustring: 0x3c9e
   __TEXT.__dlopen_cstrs: 0x94e

   __TEXT.__swift5_types: 0x4
   __TEXT.__unwind_info: 0x87e8
   __TEXT.__objc_classname: 0x50ad
-  __TEXT.__objc_methname: 0x5c19d
+  __TEXT.__objc_methname: 0x5c15e
   __TEXT.__objc_methtype: 0x137a9
-  __TEXT.__objc_stubs: 0x37e00
+  __TEXT.__objc_stubs: 0x37de0
   __DATA_CONST.__got: 0x21c0
   __DATA_CONST.__const: 0x6e60
   __DATA_CONST.__objc_classlist: 0xab8
   __DATA_CONST.__objc_catlist: 0x148
   __DATA_CONST.__objc_protolist: 0x8d8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x108b0
+  __DATA_CONST.__objc_selrefs: 0x108a8
   __DATA_CONST.__objc_protorefs: 0x100
   __DATA_CONST.__objc_superrefs: 0x940
   __DATA_CONST.__objc_arraydata: 0x738

   - /usr/lib/swift/libswiftunistd.dylib
   Functions: 9226
   Symbols:   11140
-  CStrings:  17299
+  CStrings:  17298
 
CStrings:
- "canApplyAutoFillGracePeriodForUsername:inTabWithID:currentURL:"

```

#### AssistantServices

>  `/System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices`

```diff

-3400.161.5.11.2
+3400.161.5.11.3
   __TEXT.__text: 0x1a1b0c
   __TEXT.__auth_stubs: 0x1530
   __TEXT.__objc_methlist: 0x199a4
   __TEXT.__const: 0x458
   __TEXT.__gcc_except_tab: 0x2570
-  __TEXT.__cstring: 0x3b51a
+  __TEXT.__cstring: 0x3b57a
   __TEXT.__oslogstring: 0xff9c
   __TEXT.__dlopen_cstrs: 0x42e
   __TEXT.__unwind_info: 0x79d8

   __TEXT.__objc_methtype: 0xa8f8
   __TEXT.__objc_stubs: 0x23de0
   __DATA_CONST.__got: 0x1610
-  __DATA_CONST.__const: 0x80e8
+  __DATA_CONST.__const: 0x80f0
   __DATA_CONST.__objc_classlist: 0xda0
   __DATA_CONST.__objc_catlist: 0x290
   __DATA_CONST.__objc_protolist: 0x550

   __AUTH_CONST.__auth_got: 0xaa8
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__const: 0x3840
-  __AUTH_CONST.__cfstring: 0x266e0
+  __AUTH_CONST.__cfstring: 0x26700
   __AUTH_CONST.__objc_const: 0x39c08
   __AUTH_CONST.__objc_intobj: 0x22c8
   __AUTH_CONST.__objc_dictobj: 0xb68

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 11591
-  Symbols:   13782
-  CStrings:  18869
+  Symbols:   13783
+  CStrings:  18870
 
Symbols:
+ _kAFMAStartupActivatedNotification
CStrings:
+ "com.apple.MobileAsset.AutoAssetNotification^com.apple.MobileAsset.MAAutoAsset^STARTUP_ACTIVATED"

```

#### PasswordManagerUI

>  `/System/Library/PrivateFrameworks/PasswordManagerUI.framework/PasswordManagerUI`

```diff

-7619.1.26.30.4
+7619.1.26.30.5
   __TEXT.__text: 0x3e9af4
   __TEXT.__auth_stubs: 0x5750
   __TEXT.__objc_methlist: 0x14c0

   __DATA_CONST.__objc_protorefs: 0x100
   __DATA_CONST.__objc_superrefs: 0x20
   __AUTH_CONST.__auth_got: 0x2bb8
-  __AUTH_CONST.__auth_ptr: 0x3e40
+  __AUTH_CONST.__auth_ptr: 0x3d00
   __AUTH_CONST.__const: 0x129f8
   __AUTH_CONST.__cfstring: 0x4e0
   __AUTH_CONST.__objc_const: 0x99b8

```

#### PhotosIntelligence

>  `/System/Library/PrivateFrameworks/PhotosIntelligence.framework/PhotosIntelligence`

```diff

-702.0.220.0.0
+702.0.230.0.0
   __TEXT.__text: 0x3dfb70
   __TEXT.__auth_stubs: 0x4660
   __TEXT.__objc_methlist: 0x3da8

   __DATA_CONST.__objc_superrefs: 0x158
   __DATA_CONST.__objc_arraydata: 0x1e8
   __AUTH_CONST.__auth_got: 0x2340
-  __AUTH_CONST.__auth_ptr: 0x13c8
+  __AUTH_CONST.__auth_ptr: 0x1358
   __AUTH_CONST.__const: 0x1bab0
   __AUTH_CONST.__cfstring: 0x4840
   __AUTH_CONST.__objc_const: 0x10ef0

```

#### PhotosUIPrivate

>  `/System/Library/PrivateFrameworks/PhotosUIPrivate.framework/PhotosUIPrivate`

```diff

-702.0.220.0.0
+702.0.230.0.0
   __TEXT.__text: 0x57ed60
   __TEXT.__auth_stubs: 0x83b0
   __TEXT.__objc_methlist: 0x4ee54

   __DATA_CONST.__objc_superrefs: 0x1680
   __DATA_CONST.__objc_arraydata: 0x1878
   __AUTH_CONST.__auth_got: 0x41e8
-  __AUTH_CONST.__auth_ptr: 0x19f8
+  __AUTH_CONST.__auth_ptr: 0x1a20
   __AUTH_CONST.__const: 0xfbf8
   __AUTH_CONST.__cfstring: 0x2cba0
   __AUTH_CONST.__objc_const: 0xab6e0

```

#### PhotoAnalysis

>  `/System/Library/PrivateFrameworks/PhotoAnalysis.framework/PhotoAnalysis`

```diff

-702.0.220.0.0
+702.0.230.0.0
   __TEXT.__text: 0x1f9cfc
   __TEXT.__auth_stubs: 0x3440
   __TEXT.__objc_methlist: 0x5068

   __DATA_CONST.__objc_superrefs: 0x218
   __DATA_CONST.__objc_arraydata: 0x110
   __AUTH_CONST.__auth_got: 0x1a38
-  __AUTH_CONST.__auth_ptr: 0xb60
+  __AUTH_CONST.__auth_ptr: 0xb58
   __AUTH_CONST.__const: 0x8900
   __AUTH_CONST.__cfstring: 0x83c0
   __AUTH_CONST.__objc_const: 0x10f78

```

#### PhotosUICore

>  `/System/Library/PrivateFrameworks/PhotosUICore.framework/PhotosUICore`

```diff

-702.0.220.0.0
+702.0.230.0.0
   __TEXT.__text: 0x16d1098
   __TEXT.__auth_stubs: 0x11ce0
   __TEXT.__delay_helper: 0xec

   __DATA_CONST.__objc_arraydata: 0x4888
   __DATA_CONST.__vfx_script_tbl: 0x30
   __AUTH_CONST.__auth_got: 0x8e88
-  __AUTH_CONST.__auth_ptr: 0x71d0
+  __AUTH_CONST.__auth_ptr: 0x6c60
   __AUTH_CONST.__const: 0x4eeb0
   __AUTH_CONST.__cfstring: 0x7eb80
   __AUTH_CONST.__objc_const: 0x1c10d8

```


</details>

## EOF
