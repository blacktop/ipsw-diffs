## com.apple.CloudSharingUI.AddParticipants

> `/System/Library/PrivateFrameworks/CloudSharingUI.framework/PlugIns/com.apple.CloudSharingUI.AddParticipants.appex/com.apple.CloudSharingUI.AddParticipants`

```diff

-215.0.0.0.0
-  __TEXT.__text: 0x76100
-  __TEXT.__auth_stubs: 0x1540
+215.1.3.1.0
+  __TEXT.__text: 0x74ba8
+  __TEXT.__auth_stubs: 0x1560
   __TEXT.__objc_stubs: 0x1c0
-  __TEXT.__objc_methlist: 0x4b0
-  __TEXT.__const: 0x3a82
-  __TEXT.__cstring: 0x316f
-  __TEXT.__objc_methname: 0x1ada
+  __TEXT.__objc_methlist: 0x4bc
+  __TEXT.__const: 0x39c2
+  __TEXT.__cstring: 0x327f
+  __TEXT.__objc_methname: 0x1b94
   __TEXT.__objc_classname: 0x75
   __TEXT.__objc_methtype: 0x1e6
-  __TEXT.__swift5_typeref: 0x2014
-  __TEXT.__swift5_fieldmd: 0xda8
-  __TEXT.__constg_swiftt: 0xce8
+  __TEXT.__swift5_typeref: 0x2006
+  __TEXT.__swift5_fieldmd: 0xd80
+  __TEXT.__constg_swiftt: 0xcc4
   __TEXT.__swift5_builtin: 0xc8
-  __TEXT.__swift5_reflstr: 0xe65
+  __TEXT.__swift5_reflstr: 0xe35
   __TEXT.__swift5_assocty: 0x240
   __TEXT.__swift5_protos: 0x14
-  __TEXT.__swift5_proto: 0x138
-  __TEXT.__swift5_types: 0xb8
-  __TEXT.__oslogstring: 0x2a9a
-  __TEXT.__swift5_capture: 0xc18
+  __TEXT.__swift5_proto: 0x12c
+  __TEXT.__swift5_types: 0xb4
+  __TEXT.__oslogstring: 0x2c6a
+  __TEXT.__swift5_capture: 0xbd8
   __TEXT.__swift_as_entry: 0xe8
   __TEXT.__swift_as_ret: 0x138
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x15d8
+  __TEXT.__unwind_info: 0x15b0
   __TEXT.__eh_frame: 0x3a18
-  __DATA_CONST.__auth_got: 0xaa8
-  __DATA_CONST.__got: 0x500
-  __DATA_CONST.__auth_ptr: 0x660
-  __DATA_CONST.__const: 0x31e0
+  __DATA_CONST.__auth_got: 0xab8
+  __DATA_CONST.__got: 0x518
+  __DATA_CONST.__auth_ptr: 0x650
+  __DATA_CONST.__const: 0x3010
   __DATA_CONST.__cfstring: 0x20
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA.__objc_const: 0x12e0
-  __DATA.__objc_selrefs: 0x670
+  __DATA.__objc_const: 0x12e8
+  __DATA.__objc_selrefs: 0x6a8
   __DATA.__objc_ivar: 0x8
   __DATA.__objc_data: 0x5a8
   __DATA.__data: 0x19f0
-  __DATA.__bss: 0x2b90
+  __DATA.__bss: 0x2a10
   __DATA.__common: 0xb0
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/Combine.framework/Combine

   - /System/Library/PrivateFrameworks/CloudDocs.framework/CloudDocs
   - /System/Library/PrivateFrameworks/CloudSharing.framework/CloudSharing
   - /System/Library/PrivateFrameworks/CloudSharingUI.framework/CloudSharingUI
-  - /System/Library/PrivateFrameworks/FeatureFlags.framework/FeatureFlags
+  - /System/Library/PrivateFrameworks/IconServices.framework/IconServices
   - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: B2B00E24-7B05-356D-BC09-B340B30568A0
-  Functions: 1793
-  Symbols:   258
-  CStrings:  721
+  UUID: F3DEB5E1-F382-3B71-A433-5BE3ADFC84EF
+  Functions: 1770
+  Symbols:   261
+  CStrings:  735
 
Symbols:
+ _NSPOSIXErrorDomain
+ _OBJC_CLASS_$_ISIcon
+ _OBJC_CLASS_$_ISImageDescriptor
+ _OBJC_CLASS_$_UIScreen
- _OBJC_CLASS_$_NSUserDefaults
CStrings:
+ "CGImage"
+ "Created read-only FPSandboxingURLWrapper for URL %s"
+ "Created read/write FPSandboxingURLWrapper for URL %s"
+ "Failed to create read-only FPSandboxingURLWrapper for URL %s: %s"
+ "Failed to create read/write FPSandboxingURLWrapper for URL %s: %s\nTrying read-only instead..."
+ "com.apple.groups-folder"
+ "existingShareForFileWithURLWrapper:withReply:"
+ "iOS appIcon image: %@"
+ "iOS appIcon placeholder;  did prepareImage(forDescriptor:), is still placeHolder: %{bool}d"
+ "iOS appIcon: icon: %@"
+ "imageForDescriptor:"
+ "initWithCGImage:"
+ "initWithSize:scale:"
+ "initWithType:"
+ "mainScreen"
+ "placeholder"
+ "prepareImageForDescriptor:"
+ "scale"
+ "sharingStatusForWithURLWrapper:withReply:"
+ "startFileSharingWithURLWrapper:emailAddresses:phoneNumbers:accessType:permissionType:allowOthersToInvite:withReply:"
+ "startFileSharingWithURLWrapper:emailAddresses:phoneNumbers:optionsGroups:withReply:"
+ "userNameAndEmailWithURLWrapper:containerSetupInfo:withReply:"
+ "v32@0:8@\"FPSandboxingURLWrapper\"16@?<v@?@\"NSURL\"@\"CKShare\"@\"NSError\">24"
+ "v32@0:8@\"FPSandboxingURLWrapper\"16@?<v@?q@\"NSError\">24"
+ "v40@0:8@\"FPSandboxingURLWrapper\"16@\"CKContainerSetupInfo\"24@?<v@?@\"NSString\"@\"NSString\"@\"NSError\">32"
+ "v56@0:8@\"FPSandboxingURLWrapper\"16@\"NSArray\"24@\"NSArray\"32@\"NSArray\"40@?<v@?@\"NSURL\"@\"CKShare\"@\"NSError\">48"
+ "v68@0:8@\"FPSandboxingURLWrapper\"16@\"NSArray\"24@\"NSArray\"32q40q48B56@?<v@?@\"NSURL\"@\"CKShare\"@\"NSError\">60"
- "CloudSharingUI"
- "Gelato"
- "ShareAccessRequests"
- "ShareAccessRequestsEnabled"
- "boolForKey:"
- "existingShareForFile:withReply:"
- "objectForKey:"
- "standardUserDefaults"
- "startFileSharing:emailAddresses:phoneNumbers:accessType:permissionType:allowOthersToInvite:withReply:"
- "startFileSharing:emailAddresses:phoneNumbers:optionsGroups:withReply:"
- "userNameAndEmail:containerSetupInfo:withReply:"
- "v32@0:8@\"NSURL\"16@?<v@?@\"NSURL\"@\"CKShare\"@\"NSError\">24"
- "v40@0:8@\"NSURL\"16@\"CKContainerSetupInfo\"24@?<v@?@\"NSString\"@\"NSString\"@\"NSError\">32"

```
