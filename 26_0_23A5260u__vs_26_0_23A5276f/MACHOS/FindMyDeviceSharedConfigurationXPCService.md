## FindMyDeviceSharedConfigurationXPCService

> `/System/Library/PrivateFrameworks/FindMyDevice.framework/XPCServices/FindMyDeviceSharedConfigurationXPCService.xpc/FindMyDeviceSharedConfigurationXPCService`

```diff

-452.30.5.13.0
-  __TEXT.__text: 0xc71c
-  __TEXT.__auth_stubs: 0xb90
-  __TEXT.__objc_methlist: 0x1b4
-  __TEXT.__const: 0x7ca
-  __TEXT.__cstring: 0x3af
-  __TEXT.__swift5_typeref: 0x2e2
-  __TEXT.__objc_methname: 0x479
-  __TEXT.__swift5_capture: 0x168
-  __TEXT.__oslogstring: 0x5f2
+455.30.6.9.8
+  __TEXT.__text: 0xdf14
+  __TEXT.__auth_stubs: 0xc00
+  __TEXT.__objc_methlist: 0x1e4
+  __TEXT.__const: 0x7ba
+  __TEXT.__cstring: 0x48f
+  __TEXT.__swift5_typeref: 0x316
+  __TEXT.__objc_methname: 0x698
+  __TEXT.__swift5_capture: 0x1d0
+  __TEXT.__oslogstring: 0x722
   __TEXT.__constg_swiftt: 0x1a8
   __TEXT.__swift5_reflstr: 0x17f
   __TEXT.__swift5_fieldmd: 0x19c

   __TEXT.__swift5_proto: 0x4c
   __TEXT.__swift5_types: 0x28
   __TEXT.__objc_classname: 0x42
-  __TEXT.__objc_methtype: 0x149
+  __TEXT.__objc_methtype: 0x1b3
   __TEXT.__swift_as_entry: 0x8
   __TEXT.__swift_as_ret: 0x8
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x2c0
+  __TEXT.__unwind_info: 0x2e0
   __TEXT.__eh_frame: 0x198
-  __DATA_CONST.__auth_got: 0x5c8
-  __DATA_CONST.__got: 0x1d8
+  __DATA_CONST.__auth_got: 0x600
+  __DATA_CONST.__got: 0x210
   __DATA_CONST.__auth_ptr: 0x2a8
-  __DATA_CONST.__const: 0x650
+  __DATA_CONST.__const: 0x748
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA.__objc_const: 0x578
-  __DATA.__objc_selrefs: 0x1d0
+  __DATA.__objc_const: 0x5c8
+  __DATA.__objc_selrefs: 0x2a0
   __DATA.__objc_data: 0x168
-  __DATA.__data: 0x3b0
+  __DATA.__data: 0x3c0
   __DATA.__bss: 0xa40
   __DATA.__common: 0x28
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/AuthKit.framework/AuthKit
+  - /System/Library/PrivateFrameworks/CoreFollowUp.framework/CoreFollowUp
   - /System/Library/PrivateFrameworks/FindMyBase.framework/FindMyBase
   - /System/Library/PrivateFrameworks/FindMyDevice.framework/FindMyDevice
   - /System/Library/PrivateFrameworks/FindMyServerInteraction.framework/FindMyServerInteraction

   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: AC3208D9-ABC4-3932-8145-F79AAC4C8E77
-  Functions: 244
-  Symbols:   138
-  CStrings:  139
+  UUID: DE9088FC-1A64-30DF-97C2-59138C70537B
+  Functions: 264
+  Symbols:   145
+  CStrings:  179
 
Symbols:
+ _FLGroupIdentifierDevice
+ _OBJC_CLASS_$_FLFollowUpAction
+ _OBJC_CLASS_$_FLFollowUpController
+ _OBJC_CLASS_$_FLFollowUpItem
+ _OBJC_CLASS_$_FLFollowUpNotification
+ _OBJC_CLASS_$_NSBundle
+ _OBJC_CLASS_$_NSUUID
+ _objc_retain_x23
+ _objc_retain_x24
+ _objc_retain_x25
+ _swift_getObjCClassFromMetadata
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
CStrings:
+ "Device with serial number (%s) is covered by TnL. Posting CFU."
+ "Device with serial number (%s) is not covered. Cannot queue CFU."
+ "Failed to create the FU controller"
+ "Failed to create the Follow Up controller"
+ "Failed to post the follow up with error: %@"
+ "Localizable-WARRANTY_DIAGNOSTICS"
+ "TNL_CONTINUE_BUTTON"
+ "UUIDString"
+ "Unable to clear pending followup for id: com.apple.findmy.theftandloss.reminder with error: %@"
+ "actionWithLabel:url:"
+ "bundleForClass:"
+ "clearPendingFollowUpItemsWithUniqueIdentifiers:error:"
+ "clearTheftAndLossCFU:"
+ "com.apple.Preferences"
+ "com.apple.findmy.remoteuiservice.FMDCFUTheftAndLossReminderExtension"
+ "com.apple.findmy.theftandloss.reminder"
+ "informativeText"
+ "initWithClientIdentifier:"
+ "localizedStringForKey:value:table:"
+ "notification"
+ "postFollowUpItem:error:"
+ "requestTheftAndLossCFUWithString:andReply:"
+ "setActions:"
+ "setActivateAction:"
+ "setExtensionIdentifier:"
+ "setFirstNotificationDelay:"
+ "setFrequency:"
+ "setGroupIdentifier:"
+ "setIdentifier:"
+ "setInformativeText:"
+ "setNotification:"
+ "setSubtitleText:"
+ "setTargetBundleIdentifier:"
+ "setTitle:"
+ "setUniqueIdentifier:"
+ "subtitleText"
+ "title"
+ "v24@0:8@?16"
+ "v24@0:8@?<v@?@\"NSError\">16"
+ "v32@0:8@\"FMDSharedConfigurationFollowUpEntry\"16@?<v@?@\"NSError\">24"
- "Existing configuration for %{public}s has not yet expired %{public}@"

```
