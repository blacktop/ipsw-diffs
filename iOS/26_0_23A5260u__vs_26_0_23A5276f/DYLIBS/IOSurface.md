## IOSurface

> `/System/Library/Frameworks/IOSurface.framework/IOSurface`

```diff

-392.0.0.0.0
-  __TEXT.__text: 0x1397c
+392.2.1.0.0
+  __TEXT.__text: 0x13b70
   __TEXT.__auth_stubs: 0xe20
   __TEXT.__objc_methlist: 0x9e4
   __TEXT.__gcc_except_tab: 0x144
   __TEXT.__const: 0x153
   __TEXT.__oslogstring: 0x6ae
-  __TEXT.__cstring: 0x2906
-  __TEXT.__unwind_info: 0x530
+  __TEXT.__cstring: 0x2924
+  __TEXT.__unwind_info: 0x538
   __TEXT.__objc_classname: 0x192
   __TEXT.__objc_methname: 0x135e
   __TEXT.__objc_methtype: 0xc76
   __TEXT.__objc_stubs: 0xc40
   __DATA_CONST.__got: 0x180
-  __DATA_CONST.__const: 0xa38
+  __DATA_CONST.__const: 0xa40
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_superrefs: 0x60
   __AUTH_CONST.__auth_got: 0x728
   __AUTH_CONST.__const: 0x1f8
-  __AUTH_CONST.__cfstring: 0x1fe0
+  __AUTH_CONST.__cfstring: 0x2000
   __AUTH_CONST.__objc_const: 0x12e0
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH.__objc_data: 0x230

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 70A35CB2-F544-36CD-94FA-33B36FAB3182
-  Functions: 648
-  Symbols:   1906
-  CStrings:  1048
+  UUID: 11618387-0455-317C-91F1-CCE9045D43FF
+  Functions: 650
+  Symbols:   1911
+  CStrings:  1050
 
Symbols:
+ _createHorizontalDisparityAdjustmentFromStruct
+ _kIOSurfaceHorizontalDisparityAdjustment
+ _sniffHorizontalDisparityAdjustmentKeyToStruct
Functions:
~ __iosCreateDictionaryAddingMissingProperties : 820 -> 816
~ ____ensureKeySniffDictionaries_block_invoke : 3064 -> 3192
~ _IOSurfaceClientSetValue : 884 -> 880
~ _getDirtyMask : 648 -> 676
~ _IOSurfaceClientSetBulkAttachments : 248 -> 244
~ _IOSurfaceClientRemoveBulkAttachments : 208 -> 212
~ __insertAllKeysFromStruct : 1636 -> 1708
+ _createHorizontalDisparityAdjustmentFromStruct
+ _sniffHorizontalDisparityAdjustmentKeyToStruct
~ __IOSurfaceRemoteMethodClientSetBulkAttachments : 144 -> 148
~ __IOSurfaceRemoteMethodClientGetBulkAttachments : 164 -> 168
CStrings:
+ "HorizontalDisparityAdjustment"

```
