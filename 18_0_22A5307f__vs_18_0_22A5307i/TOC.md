# 18.0 (22A5307f) .vs 18.0 (22A5307i)

## IPSWs

- `iPhone16,2_18.0_22A5307f_Restore.ipsw`
- `iPhone16,2_18.0_22A5307i_Restore.ipsw`

## Kernel

### Version

| iOS | Version | Build | Date |
| :-- | :------ | :---- | :--- |
| 18.0 *(22A5307f)* | 24.0.0 | 11215.0.132.502.2~1 | Wed, 03Jul2024 20:40:06 PDT |
| 18.0 *(22A5307i)* | 24.0.0 | 11215.0.132.502.2~1 | Wed, 03Jul2024 20:40:06 PDT |

## MachO

### 🆕 NEW (4)

- `/usr/lib/libmobileassetd.dylib`
- `/usr/lib/libobjc-trampolines.dylib`
- `/usr/lib/libstdc++.6.0.9.dylib`
- `/usr/libexec/BatteryAlgorithms.framework/BatteryAlgorithms`

### ⬆️ Updated (8)

<details>
  <summary><i>View Updated</i></summary>

#### MobileSlideShow

>  `/Applications/MobileSlideShow.app/MobileSlideShow`

```diff

-700.26.103.0.0
+700.26.104.0.0
   __TEXT.__text: 0x4b408
   __TEXT.__auth_stubs: 0x1b00
   __TEXT.__objc_stubs: 0x7dc0

   __TEXT.__eh_frame: 0xbc8
   __DATA_CONST.__auth_got: 0xd90
   __DATA_CONST.__got: 0xb70
-  __DATA_CONST.__auth_ptr: 0x5c8
+  __DATA_CONST.__auth_ptr: 0x5c0
   __DATA_CONST.__const: 0x31a0
   __DATA_CONST.__cfstring: 0x41a0
   __DATA_CONST.__objc_classlist: 0x78

```

#### com.apple.UIKit.ColorPicker

>  `/System/Library/Frameworks/UIKit.framework/PlugIns/com.apple.UIKit.ColorPicker.appex/com.apple.UIKit.ColorPicker`

```diff

-8071.2.103.0.0
+8071.2.104.0.0
   __TEXT.__text: 0x48100
   __TEXT.__auth_stubs: 0x1d50
   __TEXT.__objc_stubs: 0xd20

   __TEXT.__eh_frame: 0x680
   __DATA_CONST.__auth_got: 0xeb8
   __DATA_CONST.__got: 0x760
-  __DATA_CONST.__auth_ptr: 0xd10
+  __DATA_CONST.__auth_ptr: 0xbf8
   __DATA_CONST.__const: 0x21d8
   __DATA_CONST.__cfstring: 0xc0
   __DATA_CONST.__objc_classlist: 0x80

```

#### SafetyMonitorMessages

>  `/System/Library/Messages/iMessageApps/SafetyMonitorMessages.bundle/SafetyMonitorMessages`

```diff

 956.0.0.0.0
-  __TEXT.__text: 0x10c10
-  __TEXT.__auth_stubs: 0xc70
+  __TEXT.__text: 0x10c40
+  __TEXT.__auth_stubs: 0xca0
   __TEXT.__objc_methlist: 0xc8
   __TEXT.__swift5_typeref: 0x1a0
   __TEXT.__objc_methname: 0x7f3

   __TEXT.__swift5_fieldmd: 0x90
   __TEXT.__swift5_types: 0xc
   __TEXT.__unwind_info: 0x1d0
-  __DATA_CONST.__auth_got: 0x638
+  __DATA_CONST.__auth_got: 0x650
   __DATA_CONST.__got: 0x1b0
   __DATA_CONST.__auth_ptr: 0xc0
   __DATA_CONST.__const: 0x320

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 129
-  Symbols:   138
+  Symbols:   139
   CStrings:  60
 
Symbols:
+ _objc_retain_x9

```

#### AccessibilitySettings

>  `/System/Library/PreferenceBundles/AccessibilitySettings.bundle/AccessibilitySettings`

```diff

-1760.2.0.0.0
-  __TEXT.__text: 0x1619b8
+1760.3.1.0.0
+  __TEXT.__text: 0x1619a0
   __TEXT.__auth_stubs: 0x42f0
-  __TEXT.__objc_stubs: 0x221e0
+  __TEXT.__objc_stubs: 0x22200
   __TEXT.__objc_methlist: 0x11964
   __TEXT.__const: 0x18f0
   __TEXT.__gcc_except_tab: 0x31cc
-  __TEXT.__objc_methname: 0x302dc
+  __TEXT.__objc_methname: 0x302ec
   __TEXT.__cstring: 0x1715c
   __TEXT.__oslogstring: 0x36b7
   __TEXT.__objc_classname: 0x3eb4

   __DATA_CONST.__objc_floatobj: 0x20
   __DATA_CONST.__objc_dictobj: 0x9b0
   __DATA.__objc_const: 0x1ea60
-  __DATA.__objc_selrefs: 0xb318
+  __DATA.__objc_selrefs: 0xb320
   __DATA.__objc_ivar: 0xd2c
   __DATA.__objc_data: 0x8b60
   __DATA.__data: 0x2b82

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 7635
-  Symbols:   18123
+  Symbols:   18124
   CStrings:  3756
 
Symbols:
+ _objc_msgSend$isClassicDevice

```

#### WallpaperSettings

>  `/System/Library/PreferenceBundles/WallpaperSettings.bundle/WallpaperSettings`

```diff

-210.102.0.0.0
+210.104.0.0.0
   __TEXT.__text: 0x30700
   __TEXT.__auth_stubs: 0x1d10
   __TEXT.__objc_stubs: 0x40

   __TEXT.__eh_frame: 0x1150
   __DATA_CONST.__auth_got: 0xe90
   __DATA_CONST.__got: 0x568
-  __DATA_CONST.__auth_ptr: 0xa70
+  __DATA_CONST.__auth_ptr: 0xa40
   __DATA_CONST.__const: 0x19c8
   __DATA_CONST.__cfstring: 0x20
   __DATA_CONST.__objc_classlist: 0x50

```

#### bluetoothuserd

>  `/usr/libexec/bluetoothuserd`

```diff

-180.53.2.1.2
+180.53.2.1.3
   __TEXT.__text: 0x6c3ec
   __TEXT.__auth_stubs: 0x1b10
   __TEXT.__objc_methlist: 0x1bc

   __TEXT.__eh_frame: 0x1aa0
   __DATA_CONST.__auth_got: 0xd88
   __DATA_CONST.__got: 0x508
-  __DATA_CONST.__auth_ptr: 0x5d8
+  __DATA_CONST.__auth_ptr: 0x608
   __DATA_CONST.__const: 0x2978
   __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_protolist: 0xd0

```

#### ColorPickerUIService

>  `/Applications/ColorPickerUIService.app/ColorPickerUIService`

```diff

-8071.2.103.0.0
+8071.2.104.0.0
   __TEXT.__text: 0x48954
   __TEXT.__auth_stubs: 0x1d90
   __TEXT.__objc_stubs: 0xf80

   __TEXT.__eh_frame: 0x680
   __DATA_CONST.__auth_got: 0xed8
   __DATA_CONST.__got: 0x780
-  __DATA_CONST.__auth_ptr: 0xd40
+  __DATA_CONST.__auth_ptr: 0xd60
   __DATA_CONST.__const: 0x21d8
   __DATA_CONST.__cfstring: 0x100
   __DATA_CONST.__objc_classlist: 0xa8

```

#### FontPickerUIService

>  `/Applications/FontPickerUIService.app/FontPickerUIService`

```diff

-8071.2.103.0.0
+8071.2.104.0.0
   __TEXT.__text: 0x7df8c
   __TEXT.__auth_stubs: 0x2140
   __TEXT.__objc_stubs: 0x23a0

   __TEXT.__eh_frame: 0x6e8
   __DATA_CONST.__auth_got: 0x10b0
   __DATA_CONST.__got: 0xbb8
-  __DATA_CONST.__auth_ptr: 0xa00
+  __DATA_CONST.__auth_ptr: 0xa10
   __DATA_CONST.__const: 0x2f68
   __DATA_CONST.__cfstring: 0x360
   __DATA_CONST.__objc_classlist: 0x78

```


</details>

### 🔑 Entitlements

- [Entitlements DIFF](Entitlements.md)

## DSC

### WebKit

| iOS | Version |
| :-- | :------ |
| 18.0 *(22A5307f)* | 619.1.20.10.1 |
| 18.0 *(22A5307i)* | 619.1.20.10.1 |

### Dylibs

#### ⬆️ Updated (20)

<details>
  <summary><i>View Updated</i></summary>

- [/System/Library/Frameworks/CoreLocationUI.framework/CoreLocationUI](DYLIBS/CoreLocationUI.md)
- [/System/Library/Frameworks/_MapKit_SwiftUI.framework/_MapKit_SwiftUI](DYLIBS/_MapKit_SwiftUI.md)
- [/System/Library/PrivateFrameworks/KnowledgeGraphKit.framework/KnowledgeGraphKit](DYLIBS/KnowledgeGraphKit.md)
- [/System/Library/PrivateFrameworks/PaperBoardUI.framework/PaperBoardUI](DYLIBS/PaperBoardUI.md)
- [/System/Library/PrivateFrameworks/PhotoAnalysis.framework/PhotoAnalysis](DYLIBS/PhotoAnalysis.md)
- [/System/Library/PrivateFrameworks/PhotoLibraryServices.framework/PhotoLibraryServices](DYLIBS/PhotoLibraryServices.md)
- [/System/Library/PrivateFrameworks/PhotosGraph.framework/PhotosGraph](DYLIBS/PhotosGraph.md)
- [/System/Library/PrivateFrameworks/PhotosIntelligence.framework/PhotosIntelligence](DYLIBS/PhotosIntelligence.md)
- [/System/Library/PrivateFrameworks/PhotosSwiftUICore.framework/PhotosSwiftUICore](DYLIBS/PhotosSwiftUICore.md)
- [/System/Library/PrivateFrameworks/PhotosUICore.framework/PhotosUICore](DYLIBS/PhotosUICore.md)
- [/System/Library/PrivateFrameworks/PhotosUIPrivate.framework/PhotosUIPrivate](DYLIBS/PhotosUIPrivate.md)
- [/System/Library/PrivateFrameworks/PosterBoard.framework/PosterBoard](DYLIBS/PosterBoard.md)
- [/System/Library/PrivateFrameworks/PosterKit.framework/PosterKit](DYLIBS/PosterKit.md)
- [/System/Library/PrivateFrameworks/PosterUIFoundation.framework/PosterUIFoundation](DYLIBS/PosterUIFoundation.md)
- [/System/Library/PrivateFrameworks/SafetyMonitorUI.framework/SafetyMonitorUI](DYLIBS/SafetyMonitorUI.md)
- [/System/Library/PrivateFrameworks/SiriMessagesFlow.framework/SiriMessagesFlow](DYLIBS/SiriMessagesFlow.md)
- [/System/Library/PrivateFrameworks/SiriMessagesUI.framework/SiriMessagesUI](DYLIBS/SiriMessagesUI.md)
- [/System/Library/PrivateFrameworks/TextFormattingUI.framework/TextFormattingUI](DYLIBS/TextFormattingUI.md)
- [/System/Library/PrivateFrameworks/TextInputUI.framework/TextInputUI](DYLIBS/TextInputUI.md)
- [/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore](DYLIBS/UIKitCore.md)

</details>

## EOF
