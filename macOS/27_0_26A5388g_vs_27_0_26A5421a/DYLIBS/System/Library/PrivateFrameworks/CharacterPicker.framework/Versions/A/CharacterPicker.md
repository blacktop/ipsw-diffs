## CharacterPicker

> `/System/Library/PrivateFrameworks/CharacterPicker.framework/Versions/A/CharacterPicker`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`

```diff

-322.0.0.0.0
-  __TEXT.__text: 0xaf450
-  __TEXT.__objc_methlist: 0x7814
+323.500.0.0.0
+  __TEXT.__text: 0xaf600
+  __TEXT.__objc_methlist: 0x7854
   __TEXT.__cstring: 0x3e9d
   __TEXT.__const: 0x51d4
   __TEXT.__gcc_except_tab: 0x7cc

   __DATA_CONST.__const: 0x760
   __DATA_CONST.__objc_classlist: 0x348
   __DATA_CONST.__objc_catlist: 0x40
-  __DATA_CONST.__objc_protolist: 0x100
+  __DATA_CONST.__objc_protolist: 0x108
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0x5028
+  __DATA_CONST.__objc_selrefs: 0x5048
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x258
   __DATA_CONST.__objc_arraydata: 0x448
-  __DATA_CONST.__got: 0xf68
+  __DATA_CONST.__got: 0xf70
   __AUTH_CONST.__const: 0x43f8
   __AUTH_CONST.__cfstring: 0x3ec0
-  __AUTH_CONST.__objc_const: 0xdf80
+  __AUTH_CONST.__objc_const: 0xe300
   __AUTH_CONST.__weak_auth_got: 0x18
   __AUTH_CONST.__objc_arrayobj: 0x258
   __AUTH_CONST.__objc_intobj: 0x198

   __AUTH_CONST.__auth_got: 0x17e0
   __AUTH.__objc_data: 0x2708
   __AUTH.__data: 0x668
-  __DATA.__objc_ivar: 0x78c
-  __DATA.__data: 0x1fb0
+  __DATA.__objc_ivar: 0x790
+  __DATA.__data: 0x2010
   __DATA.__bss: 0x3e88
   __DATA.__common: 0x68
   __DATA_DIRTY.__bss: 0x78

   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/QuartzCore.framework/Versions/A/QuartzCore
   - /System/Library/Frameworks/SwiftUI.framework/Versions/A/SwiftUI
+  - /System/Library/PrivateFrameworks/BackBoardServices.framework/Versions/A/BackBoardServices
   - /System/Library/PrivateFrameworks/CoreEmoji.framework/Versions/A/CoreEmoji
   - /System/Library/PrivateFrameworks/EmojiFoundation.framework/Versions/A/EmojiFoundation
   - /System/Library/PrivateFrameworks/InputAnalytics.framework/Versions/A/InputAnalytics

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 4708
-  Symbols:   12648
+  Functions: 4710
+  Symbols:   12661
   CStrings:  875
 
Symbols:
+ -[CPKPopover backgroundTouchObserver]
+ -[CPKPopover setBackgroundTouchObserver:]
+ -[CPKPopover touchDownOccurred]
+ OBJC_IVAR_$_CPKPopover._backgroundTouchObserver
+ _OBJC_CLASS_$_BKSTouchDeliveryObservationService
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BKSTouchDeliveryBackgroundObserving
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BKSTouchDeliveryBackgroundObserving
+ __OBJC_$_PROTOCOL_REFS_BKSTouchDeliveryBackgroundObserving
+ __OBJC_CLASS_PROTOCOLS_$_CPKPopover
+ __OBJC_LABEL_PROTOCOL_$_BKSTouchDeliveryBackgroundObserving
+ __OBJC_PROTOCOL_$_BKSTouchDeliveryBackgroundObserving
+ ___31-[CPKPopover touchDownOccurred]_block_invoke
+ _objc_msgSend$addBackgroundObserver:
+ _objc_msgSend$backgroundTouchObserver
+ _objc_msgSend$setBackgroundTouchObserver:
- __StartMonitoringExternalEvent
- __StopMonitoringExternalEvent
```
