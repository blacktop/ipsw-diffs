## EmergencyAlerts

> `/System/Library/PrivateFrameworks/EmergencyAlerts.framework/EmergencyAlerts`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_superrefs`
- `__AUTH_CONST.__const`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-268.0.0.0.0
-  __TEXT.__text: 0x3de8
-  __TEXT.__objc_methlist: 0x184
+272.1.0.0.0
+  __TEXT.__text: 0x3f34
+  __TEXT.__objc_methlist: 0x1a0
   __TEXT.__const: 0x90
-  __TEXT.__cstring: 0x494
-  __TEXT.__oslogstring: 0x894
-  __TEXT.__unwind_info: 0x120
+  __TEXT.__cstring: 0x47a
+  __TEXT.__oslogstring: 0x966
+  __TEXT.__unwind_info: 0x138
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x268
+  __DATA_CONST.__const: 0x250
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x430
   __DATA_CONST.__objc_superrefs: 0x10
-  __DATA_CONST.__got: 0x170
+  __DATA_CONST.__got: 0x178
   __AUTH_CONST.__const: 0x60
-  __AUTH_CONST.__cfstring: 0x880
-  __AUTH_CONST.__objc_const: 0x1d0
+  __AUTH_CONST.__cfstring: 0x8a0
+  __AUTH_CONST.__objc_const: 0x1f0
   __AUTH_CONST.__auth_got: 0x0
-  __DATA.__objc_ivar: 0xc
+  __DATA.__objc_ivar: 0x10
   __DATA.__data: 0x8
   __DATA_DIRTY.__objc_data: 0xa0
   __DATA_DIRTY.__bss: 0x18

   - /System/Library/PrivateFrameworks/ToneLibrary.framework/ToneLibrary
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 72
-  Symbols:   351
-  CStrings:  125
+  Functions: 75
+  Symbols:   353
+  CStrings:  130
 
Symbols:
+ -[EACellBroadcastMessageListener preferredLanguageChanged:]
+ -[EAEmergencyAlertCenter preferredLanguageChanged:]
+ -[EAEmergencyAlertCenter registerNotificationCategories]
+ _CFBundleCopyLocalizedStringForLocalization
+ _CFBundleCreate
+ _OBJC_CLASS_$_NSSet
+ _OBJC_IVAR_$_EAEmergencyAlertCenter._preferredLanguage
+ ___59-[EACellBroadcastMessageListener preferredLanguageChanged:]_block_invoke
+ ___block_descriptor_48_e8_32s40s_e5_v8?0ls32l8s40l8
+ _kCFAllocatorDefault
+ _objc_msgSend$bundleURL
+ _objc_msgSend$preferredLanguageChanged:
+ _objc_msgSend$registerNotificationCategories
+ _objc_msgSend$setWithObjects:
- -[EAEmergencyAlertCenter registerInternalCategoriesIfNeeded]
- _EACategoryIdentifierGeoAlertWatch
- _EACategoryIdentifierGeoAlertWatchInternal
- _EACategoryIdentifierIgneous
- _OBJC_CLASS_$_NSMutableSet
- ___60-[EAEmergencyAlertCenter registerInternalCategoriesIfNeeded]_block_invoke
- ___block_descriptor_56_e8_32s40s48s_e15_v16?0"NSSet"8ls32l8s40l8s48l8
- _objc_msgSend$addObject:
- _objc_msgSend$getNotificationCategoriesWithCompletionHandler:
- _objc_msgSend$registerInternalCategoriesIfNeeded
- _objc_msgSend$set
- _objc_retain_x26
CStrings:
+ "Failed to create CFBundleRef from CMAS bundle URL"
+ "Language changing from %{public}@ to %{public}@"
+ "Localizable"
+ "Maps action title: %{public}@"
+ "No change in preferred language from %{public}@"
+ "Open in Maps"
+ "Registered emergency alert notification categories"
+ "Tap-to-Radar"
+ "Tap-to-Radar action title: %{public}@"
+ "en"
- "Registered internal notification categories with icons"
- "geo-alert-watch"
- "geo-alert-watch-internal"
- "igneous"
- "v16@?0@\"NSSet\"8"
```
