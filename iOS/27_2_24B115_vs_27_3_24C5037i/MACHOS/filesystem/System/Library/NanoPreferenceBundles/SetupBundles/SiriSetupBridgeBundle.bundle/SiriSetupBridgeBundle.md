## SiriSetupBridgeBundle

> `/System/Library/NanoPreferenceBundles/SetupBundles/SiriSetupBridgeBundle.bundle/SiriSetupBridgeBundle`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_capture`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA.__objc_const`

```diff

-1379.1.1.0.0
-  __TEXT.__text: 0x8c30
-  __TEXT.__auth_stubs: 0x930
-  __TEXT.__objc_stubs: 0x5a0
+1379.3.3.1.0
+  __TEXT.__text: 0x919c
+  __TEXT.__auth_stubs: 0x940
+  __TEXT.__objc_stubs: 0x6c0
   __TEXT.__objc_methlist: 0x424
-  __TEXT.__const: 0x178
+  __TEXT.__const: 0x2e2
   __TEXT.__cstring: 0x591
   __TEXT.__objc_classname: 0x12c
   __TEXT.__objc_methtype: 0x24c
-  __TEXT.__swift5_typeref: 0x199
+  __TEXT.__swift5_typeref: 0x1de
   __TEXT.__swift5_capture: 0xc0
-  __TEXT.__objc_methname: 0xa1b
-  __TEXT.__oslogstring: 0x5c3
-  __TEXT.__constg_swiftt: 0x244
-  __TEXT.__swift5_reflstr: 0xa7
-  __TEXT.__swift5_fieldmd: 0xa0
-  __TEXT.__swift5_types: 0x10
-  __TEXT.__unwind_info: 0x318
-  __DATA_CONST.__const: 0x428
+  __TEXT.__objc_methname: 0xadb
+  __TEXT.__oslogstring: 0x6b0
+  __TEXT.__constg_swiftt: 0x2a4
+  __TEXT.__swift5_reflstr: 0x13d
+  __TEXT.__swift5_fieldmd: 0x14c
+  __TEXT.__swift5_types: 0x20
+  __TEXT.__swift5_assocty: 0x18
+  __TEXT.__swift5_proto: 0x14
+  __TEXT.__unwind_info: 0x348
+  __DATA_CONST.__const: 0x5f0
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__auth_got: 0x4a0
-  __DATA_CONST.__got: 0x120
-  __DATA_CONST.__auth_ptr: 0x60
+  __DATA_CONST.__auth_got: 0x4a8
+  __DATA_CONST.__got: 0x130
+  __DATA_CONST.__auth_ptr: 0xc8
   __DATA.__objc_const: 0x488
-  __DATA.__objc_selrefs: 0x310
-  __DATA.__objc_data: 0x410
-  __DATA.__data: 0x288
-  __DATA.__common: 0x18
+  __DATA.__objc_selrefs: 0x358
+  __DATA.__objc_data: 0x408
+  __DATA.__data: 0x2a0
+  __DATA.__common: 0x28
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/UIKit.framework/UIKit

   - /System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry
   - /System/Library/PrivateFrameworks/SiriSetup.framework/SiriSetup
   - /System/Library/PrivateFrameworks/SpeakerRecognition.framework/SpeakerRecognition
+  - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement
+  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 190
-  Symbols:   150
-  CStrings:  204
+  Functions: 232
+  Symbols:   163
+  CStrings:  217
 
Symbols:
+ _AFPreferencesLanguageIsSupported
+ _MobileGestalt_get_assistantCapability
+ _MobileGestalt_get_current_device
+ _OBJC_CLASS_$_AFSiriAvailability
+ _OBJC_CLASS_$_AFSystemAssistantExperienceStatusManager
+ _OBJC_CLASS_$_UMUserManager
+ _objc_retain_x21
+ _objc_retain_x25
+ _swift_arrayDestroy
+ _swift_arrayInitWithCopy
+ _swift_arrayInitWithTakeBackToFront
+ _swift_arrayInitWithTakeFrontToBack
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_initWithCopy
+ _swift_cvw_initializeBufferWithCopyOfBuffer
+ _swift_release_x24
+ _swift_retain_x24
- _objc_retain_x27
- _swift_endAccess
- _swift_getSingletonMetadata
- _swift_release_x26
- _swift_retain_x26
- _swift_updateClassMetadata2
CStrings:
+ "Not Siri eligible: Siri is restricted"
+ "Not Siri eligible: device does not support Siri"
+ "Not Siri eligible: device is multi-user"
+ "Watch is not Orchid-aligned; classic Siri pages only, no Campo offer"
+ "bestSupportedLanguageCodeForLanguageCode:"
+ "fromPreferences"
+ "isCurrentLocaleNativelySupported"
+ "isLinwoodCapableIgnoringUserSetting"
+ "isMultiUser"
+ "sharedManager"
+ "siriAvailability"
+ "status"
+ "watchIsOrchidAligned"
```
