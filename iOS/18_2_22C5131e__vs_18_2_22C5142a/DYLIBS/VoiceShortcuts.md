## VoiceShortcuts

> `/System/Library/PrivateFrameworks/VoiceShortcuts.framework/VoiceShortcuts`

```diff

-3217.0.4.0.0
-  __TEXT.__text: 0x116740
-  __TEXT.__auth_stubs: 0x3560
-  __TEXT.__objc_methlist: 0x529c
-  __TEXT.__cstring: 0x11f15
+3218.0.9.0.0
+  __TEXT.__text: 0x1168e4
+  __TEXT.__auth_stubs: 0x3570
+  __TEXT.__objc_methlist: 0x52ac
+  __TEXT.__cstring: 0x11f55
   __TEXT.__swift5_typeref: 0x2807
   __TEXT.__swift5_fieldmd: 0x15bc
   __TEXT.__const: 0x4398

   __TEXT.__swift5_protos: 0x64
   __TEXT.__swift5_proto: 0x390
   __TEXT.__swift5_types: 0x1c4
-  __TEXT.__oslogstring: 0x103ef
+  __TEXT.__oslogstring: 0x1049b
   __TEXT.__swift5_capture: 0x810
   __TEXT.__swift5_mpenum: 0x78
   __TEXT.__gcc_except_tab: 0x1384

   __TEXT.__unwind_info: 0x4950
   __TEXT.__eh_frame: 0x80e4
   __TEXT.__objc_classname: 0xe7f
-  __TEXT.__objc_methname: 0x16b92
+  __TEXT.__objc_methname: 0x16ba0
   __TEXT.__objc_methtype: 0x4b4b
-  __TEXT.__objc_stubs: 0x102e0
+  __TEXT.__objc_stubs: 0x10300
   __DATA_CONST.__got: 0x1b18
   __DATA_CONST.__const: 0x2990
   __DATA_CONST.__objc_classlist: 0x328

   __DATA_CONST.__objc_protorefs: 0xc0
   __DATA_CONST.__objc_superrefs: 0x1f0
   __DATA_CONST.__objc_arraydata: 0x60
-  __AUTH_CONST.__auth_got: 0x1ac0
-  __AUTH_CONST.__auth_ptr: 0xab8
+  __AUTH_CONST.__auth_got: 0x1ac8
+  __AUTH_CONST.__auth_ptr: 0xac0
   __AUTH_CONST.__const: 0x3e80
   __AUTH_CONST.__cfstring: 0x4560
   __AUTH_CONST.__objc_const: 0xd830

   - /System/Library/PrivateFrameworks/IntentsFoundation.framework/IntentsFoundation
   - /System/Library/PrivateFrameworks/InternalSwiftProtobuf.framework/InternalSwiftProtobuf
   - /System/Library/PrivateFrameworks/LinkServices.framework/LinkServices
+  - /System/Library/PrivateFrameworks/MobileInstallation.framework/MobileInstallation
   - /System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry
   - /System/Library/PrivateFrameworks/PairedSync.framework/PairedSync
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 6097
-  Symbols:   4459
-  CStrings:  6439
+  Functions: 6098
+  Symbols:   4461
+  CStrings:  6443
 
Symbols:
+ _MobileInstallationGetSystemAppMigrationStatus
CStrings:
+ "%s Can't determine validity of action right now, will try again later: %@"
+ "%s Fetching System App Migration Status failed with error %@"
+ "%s System App Migration Finished: %d"
+ "-[WFConfiguredSystemActionMigrator completedSystemAppMigration]"
+ "completedSystemAppMigration"
+ "initWithIntent:named:previewIcon:appShortcutIdentifier:templateParameterValues:contextualParameters:shortcutsMetadata:colorScheme:"
- "initWithIntent:named:previewIcon:appShortcutIdentifier:templateParameterValues:contextualParameters:shortcutsMetadata:"
- "setRequiresBuddyComplete:"

```
