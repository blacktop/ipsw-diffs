## FindMyDeviceSharedConfigurationXPCService

> `/System/Library/PrivateFrameworks/FindMyDevice.framework/XPCServices/FindMyDeviceSharedConfigurationXPCService.xpc/FindMyDeviceSharedConfigurationXPCService`

```diff

-455.30.6.9.11
-  __TEXT.__text: 0xf310
-  __TEXT.__auth_stubs: 0xbe0
-  __TEXT.__objc_methlist: 0x1f4
-  __TEXT.__const: 0x7da
-  __TEXT.__cstring: 0x44f
-  __TEXT.__swift5_typeref: 0x33c
-  __TEXT.__objc_methname: 0x6ac
-  __TEXT.__swift5_capture: 0x234
-  __TEXT.__oslogstring: 0x7d2
+455.30.6.9.18
+  __TEXT.__text: 0x12ca8
+  __TEXT.__auth_stubs: 0xd20
+  __TEXT.__objc_methlist: 0x224
+  __TEXT.__const: 0x80a
+  __TEXT.__cstring: 0x59f
+  __TEXT.__swift5_typeref: 0x3fc
+  __TEXT.__objc_methname: 0x7e8
+  __TEXT.__swift5_capture: 0x23c
+  __TEXT.__oslogstring: 0x872
   __TEXT.__constg_swiftt: 0x1a8
-  __TEXT.__swift5_reflstr: 0x1bf
-  __TEXT.__swift5_fieldmd: 0x1b4
+  __TEXT.__swift5_reflstr: 0x1cf
+  __TEXT.__swift5_fieldmd: 0x1c0
   __TEXT.__swift5_builtin: 0x3c
   __TEXT.__swift5_assocty: 0x90
   __TEXT.__swift5_proto: 0x4c
   __TEXT.__swift5_types: 0x28
   __TEXT.__objc_classname: 0x42
   __TEXT.__objc_methtype: 0x1f7
-  __TEXT.__swift_as_entry: 0x8
-  __TEXT.__swift_as_ret: 0x8
+  __TEXT.__swift_as_entry: 0x10
+  __TEXT.__swift_as_ret: 0x14
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x300
-  __TEXT.__eh_frame: 0x1c0
-  __DATA_CONST.__auth_got: 0x5f0
-  __DATA_CONST.__got: 0x210
-  __DATA_CONST.__auth_ptr: 0x2b0
-  __DATA_CONST.__const: 0x810
+  __TEXT.__unwind_info: 0x3d8
+  __TEXT.__eh_frame: 0x3f0
+  __DATA_CONST.__auth_got: 0x690
+  __DATA_CONST.__got: 0x260
+  __DATA_CONST.__auth_ptr: 0x2d0
+  __DATA_CONST.__const: 0x840
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA.__objc_const: 0x5f0
-  __DATA.__objc_selrefs: 0x2a8
+  __DATA.__objc_const: 0x640
+  __DATA.__objc_selrefs: 0x310
   __DATA.__objc_data: 0x168
-  __DATA.__data: 0x3d0
+  __DATA.__data: 0x440
   __DATA.__bss: 0xa40
   __DATA.__common: 0x28
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /System/Library/PrivateFrameworks/FindMyServerInteraction.framework/FindMyServerInteraction
   - /System/Library/PrivateFrameworks/NewDeviceOutreach.framework/NewDeviceOutreach
   - /System/Library/PrivateFrameworks/PairedDeviceRegistry.framework/PairedDeviceRegistry
+  - /System/Library/PrivateFrameworks/SPOwner.framework/SPOwner
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: AE72CA20-3C5E-3163-A531-4ACC8CF48434
-  Functions: 279
-  Symbols:   145
-  CStrings:  185
+  UUID: 5260731E-62CE-322D-8688-BAFCCECF79F4
+  Functions: 318
+  Symbols:   155
+  CStrings:  211
 
Symbols:
+ _OBJC_CLASS_$_NSBundle
+ _OBJC_CLASS_$_SPOwnerInterface
+ _OBJC_CLASS_$_SPRepairDeviceAttributes
+ _OBJC_CLASS_$_SPRepairDeviceContext
+ _SPRepairDeviceContextTypeRepair
+ __swift_FORCE_LOAD_$_swiftCoreLocation
+ _objc_retain_x23
+ _swift_continuation_await
+ _swift_continuation_init
+ _swift_continuation_throwingResume
+ _swift_continuation_throwingResumeWithError
+ _swift_getObjCClassFromMetadata
- _swift_release_n
- _swift_retain_n
CStrings:
+ "CFU posted for %s."
+ "Cannot get device name for CFU error: %@"
+ "Cleared CFU posted for %s."
+ "Failed to access UTF8 data from deviceID"
+ "Localizable-REPAIR"
+ "REPAIR_CONFIRM_BUTTON"
+ "REPAIR_INFORMATIVE_TEXT_AFTER_DEVICE_NAME"
+ "REPAIR_INFORMATIVE_TEXT_BEFORE_DEVICE_NAME"
+ "bundleForClass:"
+ "clearRepairCFUWithDeviceID:completion:"
+ "com.apple.findmy.repair."
+ "customModalPresentationStyle"
+ "deviceAttributesForContext:completion:"
+ "deviceNameFromDeviceID(deviceID:)"
+ "initWithBool:"
+ "initWithMatchingFindMyIds:type:"
+ "localizedStringForKey:value:table:"
+ "name"
+ "postFollowUpItem:completion:"
+ "postRepairCFUWithDeviceID:completion:"
+ "repairInterface"
+ "setTypeIdentifier:"
+ "setUserInfo:"
+ "standardUserDefaults"
+ "v20@?0B8@\"NSError\"12"
+ "v24@?0@\"NSArray\"8@\"NSError\"16"

```
