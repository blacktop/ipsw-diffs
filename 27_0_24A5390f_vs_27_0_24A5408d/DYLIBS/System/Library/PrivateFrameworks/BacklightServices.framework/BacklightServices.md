## BacklightServices

> `/System/Library/PrivateFrameworks/BacklightServices.framework/BacklightServices`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__weak_got`
- `__DATA_CONST.__objc_protorefs`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__weak_auth_got`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-6.0.38.0.0
-  __TEXT.__text: 0x29af4
-  __TEXT.__objc_methlist: 0x3824
-  __TEXT.__const: 0x138
-  __TEXT.__oslogstring: 0x2987
-  __TEXT.__cstring: 0x1b86
+6.0.42.1.0
+  __TEXT.__text: 0x2a070
+  __TEXT.__objc_methlist: 0x38f4
+  __TEXT.__const: 0x140
+  __TEXT.__oslogstring: 0x295e
+  __TEXT.__cstring: 0x1bc7
   __TEXT.__ustring: 0xfe
   __TEXT.__gcc_except_tab: 0xcb4
-  __TEXT.__unwind_info: 0x1060
+  __TEXT.__unwind_info: 0x1090
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0xdd0
-  __DATA_CONST.__objc_classlist: 0x358
+  __DATA_CONST.__objc_classlist: 0x360
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0x108
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1680
+  __DATA_CONST.__objc_selrefs: 0x16b8
   __DATA_CONST.__objc_protorefs: 0x28
-  __DATA_CONST.__objc_superrefs: 0x1b8
-  __DATA_CONST.__got: 0x400
+  __DATA_CONST.__objc_superrefs: 0x1c0
+  __DATA_CONST.__got: 0x408
   __AUTH_CONST.__const: 0x5c0
-  __AUTH_CONST.__cfstring: 0x23e0
-  __AUTH_CONST.__objc_const: 0x81b0
+  __AUTH_CONST.__cfstring: 0x2420
+  __AUTH_CONST.__objc_const: 0x8290
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x16d0
-  __DATA.__objc_ivar: 0x2e0
+  __AUTH.__objc_data: 0x1720
+  __DATA.__objc_ivar: 0x2e4
   __DATA.__data: 0xc68
   __DATA.__bss: 0xe1
   __DATA_DIRTY.__objc_data: 0xaa0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1336
-  Symbols:   3257
-  CStrings:  525
+  Functions: 1352
+  Symbols:   3283
+  CStrings:  531
 
Symbols:
+ +[BLSInvalidOnSystemSleepAttribute invalidateOnSystemSleepAfterMinimumActiveInterval:]
+ +[BLSInvalidOnSystemSleepAttribute supportsSecureCoding]
+ +[BLSValidOnSystemSleepAttribute validOnSystemSleep]
+ -[BLSBacklightSceneVisualState flipbookUsesLowPowerRendering]
+ -[BLSBacklightSceneVisualState isEqualAppearanceToVisualState:]
+ -[BLSBacklightSceneVisualState newVisualStateWithFlipbookUsesLowPowerRendering:]
+ -[BLSInvalidOnSystemSleepAttribute copyWithZone:]
+ -[BLSInvalidOnSystemSleepAttribute description]
+ -[BLSInvalidOnSystemSleepAttribute encodeWithCoder:]
+ -[BLSInvalidOnSystemSleepAttribute encodeWithXPCDictionary:]
+ -[BLSInvalidOnSystemSleepAttribute hash]
+ -[BLSInvalidOnSystemSleepAttribute initWithCoder:]
+ -[BLSInvalidOnSystemSleepAttribute initWithMinimumActiveInterval:]
+ -[BLSInvalidOnSystemSleepAttribute initWithXPCDictionary:]
+ -[BLSInvalidOnSystemSleepAttribute isEqual:]
+ -[BLSInvalidOnSystemSleepAttribute minimumActiveInterval]
+ _OBJC_CLASS_$_BLSValidOnSystemSleepAttribute
+ _OBJC_IVAR_$_BLSInvalidOnSystemSleepAttribute._minimumActiveInterval
+ _OBJC_METACLASS_$_BLSValidOnSystemSleepAttribute
+ __OBJC_$_CLASS_METHODS_BLSValidOnSystemSleepAttribute
+ __OBJC_$_INSTANCE_VARIABLES_BLSInvalidOnSystemSleepAttribute
+ __OBJC_$_PROP_LIST_BLSInvalidOnSystemSleepAttribute
+ __OBJC_CLASS_RO_$_BLSValidOnSystemSleepAttribute
+ __OBJC_METACLASS_RO_$_BLSValidOnSystemSleepAttribute
+ ___block_descriptor_104_e8_32s40r48r56r64r72r80r88r96r_e29_v32?0"BLSAttribute"8Q16^B24lr40l8r48l8s32l8r56l8r64l8r72l8r80l8r88l8r96l8
+ _objc_msgSend$flipbookUsesLowPowerRendering
+ _objc_msgSend$initWithMinimumActiveInterval:
+ _objc_msgSend$minimumActiveInterval
- ___block_descriptor_96_e8_32s40r48r56r64r72r80r88r_e29_v32?0"BLSAttribute"8Q16^B24lr40l8r48l8s32l8r56l8r64l8r72l8r80l8r88l8
- _objc_msgSend$isLowPowerRendering
CStrings:
+ "(+start) "
+ "FB "
+ "LPR "
+ "LPR-FB "
+ "flipbookUsesLPR"
+ "frameSpecifiersResponse %s%smodel.count:%lu %{public}@ for %{public}@"
+ "minimumActiveInterval"
- "performFrameSpecifiersRequest model.specifierCount:%lu dateSpecifers:%{public}@ for frameSpecifiers:%{public}@"
```
