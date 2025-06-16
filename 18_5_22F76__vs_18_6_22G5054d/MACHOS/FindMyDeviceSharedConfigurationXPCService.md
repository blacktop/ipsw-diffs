## FindMyDeviceSharedConfigurationXPCService

> `/System/Library/PrivateFrameworks/FindMyDevice.framework/XPCServices/FindMyDeviceSharedConfigurationXPCService.xpc/FindMyDeviceSharedConfigurationXPCService`

```diff

-438.35.2.11.19
-  __TEXT.__text: 0xe2f0
-  __TEXT.__auth_stubs: 0xbc0
-  __TEXT.__objc_methlist: 0x1b4
-  __TEXT.__const: 0x77a
-  __TEXT.__cstring: 0x3af
-  __TEXT.__swift5_typeref: 0x2b6
-  __TEXT.__objc_methname: 0x479
-  __TEXT.__swift5_capture: 0x168
-  __TEXT.__oslogstring: 0x5f2
+438.36.4.2.4
+  __TEXT.__text: 0x10654
+  __TEXT.__auth_stubs: 0xbe0
+  __TEXT.__objc_methlist: 0x1e4
+  __TEXT.__const: 0x78a
+  __TEXT.__cstring: 0x4af
+  __TEXT.__swift5_typeref: 0x2c0
+  __TEXT.__objc_methname: 0x5c2
+  __TEXT.__swift5_capture: 0x1c0
+  __TEXT.__oslogstring: 0x722
   __TEXT.__constg_swiftt: 0x188
   __TEXT.__swift5_reflstr: 0x15f
   __TEXT.__swift5_fieldmd: 0x180

   __TEXT.__swift5_proto: 0x4c
   __TEXT.__swift5_types: 0x24
   __TEXT.__objc_classname: 0x42
-  __TEXT.__objc_methtype: 0x149
+  __TEXT.__objc_methtype: 0x170
   __TEXT.__swift_as_entry: 0x8
   __TEXT.__swift_as_ret: 0x8
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x2c8
+  __TEXT.__unwind_info: 0x2e0
   __TEXT.__eh_frame: 0x1a0
-  __DATA_CONST.__auth_got: 0x5e0
-  __DATA_CONST.__got: 0x1e8
+  __DATA_CONST.__auth_got: 0x5f0
+  __DATA_CONST.__got: 0x208
   __DATA_CONST.__auth_ptr: 0x298
-  __DATA_CONST.__const: 0x620
+  __DATA_CONST.__const: 0x738
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA.__objc_const: 0x578
-  __DATA.__objc_selrefs: 0x1d0
+  __DATA.__objc_const: 0x5c8
+  __DATA.__objc_selrefs: 0x248
   __DATA.__objc_data: 0x168
-  __DATA.__data: 0x3b0
+  __DATA.__data: 0x3a0
   __DATA.__bss: 0xa50
   __DATA.__common: 0x28
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/AuthKit.framework/AuthKit
+  - /System/Library/PrivateFrameworks/CoreFollowUp.framework/CoreFollowUp
   - /System/Library/PrivateFrameworks/FindMyBase.framework/FindMyBase
   - /System/Library/PrivateFrameworks/FindMyDevice.framework/FindMyDevice
   - /System/Library/PrivateFrameworks/FindMyServerInteraction.framework/FindMyServerInteraction

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: BACBBADB-963B-3F75-BCAB-2DBB2205CDDC
-  Functions: 247
-  Symbols:   145
-  CStrings:  139
+  UUID: 9FF943CA-19C6-3D72-842B-A54665D34650
+  Functions: 268
+  Symbols:   151
+  CStrings:  168
 
Symbols:
+ _FLGroupIdentifierDevice
+ _MobileGestalt_copy_deviceClass_obj
+ _OBJC_CLASS_$_FLFollowUpController
+ _OBJC_CLASS_$_FLFollowUpItem
+ _OBJC_CLASS_$_FLFollowUpNotification
+ _objc_retain_x23
CStrings:
+ "Device with serial number (%s) is covered by TnL. Posting CFU."
+ "Device with serial number (%s) is not covered. Cannot queue CFU."
+ "Enable AppleCare+ Theft & Loss"
+ "Failed to create the FU controller"
+ "Failed to create the Follow Up controller"
+ "Failed to post the follow up with error: %@"
+ "Find My is required to enable AppleCare+ Theft & Loss coverage for this "
+ "Unable to clear pending followup for id: com.apple.findmy.theftAndLoss.uniqueID with error: %@"
+ "clearPendingFollowUpItemsWithUniqueIdentifiers:error:"
+ "clearTheftAndLossCFU:"
+ "com.apple.Preferences"
+ "com.apple.findmy.sojourn.clientID"
+ "com.apple.findmy.theftAndLoss.uniqueID"
+ "informativeText..."
+ "initWithClientIdentifier:"
+ "postFollowUpItem:error:"
+ "requestTheftAndLossCFU:"
+ "setFirstNotificationDelay:"
+ "setFrequency:"
+ "setGroupIdentifier:"
+ "setInformativeText:"
+ "setNotification:"
+ "setSubtitleText:"
+ "setTargetBundleIdentifier:"
+ "setTitle:"
+ "setUniqueIdentifier:"
+ "title"
+ "v24@0:8@?16"
+ "v24@0:8@?<v@?@\"NSError\">16"
- "Existing configuration for %{public}s has not yet expired %{public}@"

```
