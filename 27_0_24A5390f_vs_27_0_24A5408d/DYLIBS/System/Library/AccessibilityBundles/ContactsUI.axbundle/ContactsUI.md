## ContactsUI

> `/System/Library/AccessibilityBundles/ContactsUI.axbundle/ContactsUI`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-3045.0.0.0.0
-  __TEXT.__text: 0xce30
+3048.0.0.0.0
+  __TEXT.__text: 0xd360
   __TEXT.__objc_methlist: 0x18dc
-  __TEXT.__const: 0x20
-  __TEXT.__gcc_except_tab: 0x2c4
-  __TEXT.__cstring: 0x2982
-  __TEXT.__oslogstring: 0xa
+  __TEXT.__const: 0x38
+  __TEXT.__gcc_except_tab: 0x304
+  __TEXT.__cstring: 0x29a8
+  __TEXT.__oslogstring: 0x32f
   __TEXT.__unwind_info: 0x570
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__const: 0x3d0
   __DATA_CONST.__objc_classlist: 0x438
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x778
+  __DATA_CONST.__objc_selrefs: 0x788
   __DATA_CONST.__objc_superrefs: 0x180
   __DATA_CONST.__got: 0x228
   __AUTH_CONST.__const: 0x1c0
-  __AUTH_CONST.__cfstring: 0x33c0
+  __AUTH_CONST.__cfstring: 0x3440
   __AUTH_CONST.__objc_const: 0x4c78
   __AUTH_CONST.__auth_got: 0x0
   __DATA.__data: 0x8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 474
-  Symbols:   1535
-  CStrings:  440
+  Symbols:   1541
+  CStrings:  449
 
Symbols:
+ _AXAIWhiteGloveLoggingEnabled
+ _AXLogCommon
+ _NSStringFromClass
+ _objc_msgSend$rangeOfString:
+ _objc_msgSend$superclass
+ _objc_release_x28
Functions:
~ -[CNContactListCollectionViewCellAccessibility accessibilityLabel] : 472 -> 880
~ ___66-[CNContactListCollectionViewCellAccessibility accessibilityLabel]_block_invoke : 428 -> 1348
CStrings:
+ "_assetName"
+ "_symbolName"
+ "imageName"
+ "lock"
+ "rdar://166424765 CNContactListCollectionViewCell accessibilityLabel enter cellClass=%{public}@ accessoriesCount=%lu isEmergency=%d superLabel=%{private}@"
+ "rdar://166424765 CNContactListCollectionViewCell accessibilityLabel exit hasBlockedString=%d hasEmergencyString=%d superLabelLength=%lu superLabelContainsBlocked=%d"
+ "rdar://166424765 CNContactListCollectionViewCell accessory idx=%lu class=%{public}@ superclass=%{public}@ isCustomView=%d"
+ "rdar://166424765 CNContactListCollectionViewCell customAccessory idx=%lu customViewClass=%{public}@ customViewSuperclass=%{public}@ isImageView=%d"
+ "rdar://166424765 CNContactListCollectionViewCell imageView idx=%lu assetName=%{public}@ privateAssetName=%{public}@ underscoreAssetName=%{public}@ symbolName=%{public}@ imageName=%{public}@ hasImage=%d nosignMatch=%d"
```
