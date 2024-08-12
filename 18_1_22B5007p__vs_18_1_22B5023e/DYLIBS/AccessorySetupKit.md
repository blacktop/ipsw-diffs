## AccessorySetupKit

> `/System/Library/Frameworks/AccessorySetupKit.framework/AccessorySetupKit`

```diff

-304.24.2.1.0
-  __TEXT.__text: 0x11538
-  __TEXT.__auth_stubs: 0xb30
-  __TEXT.__objc_methlist: 0xbc0
-  __TEXT.__cstring: 0x2067
+304.28.2.0.0
+  __TEXT.__text: 0x11aa8
+  __TEXT.__auth_stubs: 0xc40
+  __TEXT.__objc_methlist: 0xbf0
+  __TEXT.__cstring: 0x25f7
   __TEXT.__const: 0x3c6
-  __TEXT.__gcc_except_tab: 0x120
-  __TEXT.__oslogstring: 0x19b
-  __TEXT.__swift5_typeref: 0x270
-  __TEXT.__constg_swiftt: 0x1d4
-  __TEXT.__swift5_reflstr: 0x92
-  __TEXT.__swift5_fieldmd: 0x9c
+  __TEXT.__gcc_except_tab: 0x230
+  __TEXT.__oslogstring: 0x1cb
+  __TEXT.__swift5_typeref: 0x289
+  __TEXT.__constg_swiftt: 0x21c
+  __TEXT.__swift5_reflstr: 0xb1
+  __TEXT.__swift5_fieldmd: 0xb4
   __TEXT.__swift5_assocty: 0x48
-  __TEXT.__swift5_capture: 0x78
+  __TEXT.__swift5_capture: 0xa0
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_proto: 0x24
   __TEXT.__swift5_types: 0x10
-  __TEXT.__unwind_info: 0x440
+  __TEXT.__unwind_info: 0x470
   __TEXT.__objc_classname: 0x1c6
-  __TEXT.__objc_methname: 0x29db
-  __TEXT.__objc_methtype: 0x6f9
-  __TEXT.__objc_stubs: 0x2000
-  __DATA_CONST.__got: 0x2a8
-  __DATA_CONST.__const: 0x398
+  __TEXT.__objc_methname: 0x2abd
+  __TEXT.__objc_methtype: 0x6a7
+  __TEXT.__objc_stubs: 0x2100
+  __DATA_CONST.__got: 0x2e0
+  __DATA_CONST.__const: 0x4a0
   __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb88
+  __DATA_CONST.__objc_selrefs: 0xbd8
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_arraydata: 0x18
-  __AUTH_CONST.__auth_got: 0x5a8
-  __AUTH_CONST.__auth_ptr: 0x158
-  __AUTH_CONST.__const: 0x398
+  __AUTH_CONST.__auth_got: 0x630
+  __AUTH_CONST.__auth_ptr: 0x168
+  __AUTH_CONST.__const: 0x2f8
   __AUTH_CONST.__cfstring: 0x9e0
-  __AUTH_CONST.__objc_const: 0x1d88
+  __AUTH_CONST.__objc_const: 0x1e58
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH.__objc_data: 0x668
+  __AUTH.__objc_data: 0x6c0
   __AUTH.__data: 0x68
-  __DATA.__objc_ivar: 0xec
-  __DATA.__data: 0x600
+  __DATA.__objc_ivar: 0xf4
+  __DATA.__data: 0x670
   __DATA.__bss: 0x4a0
   __DATA.__common: 0x18
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth

   - /System/Library/PrivateFrameworks/DeviceAccess.framework/DeviceAccess
   - /System/Library/PrivateFrameworks/Preferences.framework/Preferences
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
+  - /System/Library/PrivateFrameworks/TCC.framework/TCC
   - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 399
-  Symbols:   533
-  CStrings:  856
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 404
+  Symbols:   559
+  CStrings:  893
 
Symbols:
+ _OBJC_CLASS_$_CBManager
+ _OBJC_CLASS_$_LSApplicationExtensionRecord
+ _OBJC_CLASS_$_LSBundleRecord
+ _OBJC_CLASS_$_UIApplication
+ _UpTicksToSeconds
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
+ _dispatch_sync
+ _dyld_program_sdk_at_least
+ _kTCCServiceBluetoothAlways
+ _mach_absolute_time
+ _pthread_mutex_lock
+ _pthread_mutex_unlock
+ _tcc_authorization_record_get_authorization_right
+ _tcc_credential_singleton_for_self
+ _tcc_message_options_create
+ _tcc_message_options_set_reply_handler_policy
+ _tcc_message_options_set_request_prompt_policy
+ _tcc_server_create
+ _tcc_server_message_request_authorization
+ _tcc_service_singleton_for_CF_name
CStrings:
+ "### Unable to activate picker, still have pending CBManagers %!d(MISSING)"
+ "### allowedToActivatePicker kTCCAccessPreflightDenied/kTCCAccessPreflightGranted"
+ "### allowedToActivatePicker kTCCAccessPreflightUnknown"
+ "### allowedToActivatePicker valid authorized devices"
+ "%!s(MISSING) called after invalidate"
+ "-[ASAccessorySession _fetchAuthorizedAccesoriesIfNeeded]"
+ "-[ASAccessorySession _fetchAuthorizedAccesoriesIfNeeded]_block_invoke"
+ "-[ASAccessorySession _handleDASessionEventHandler:session:]"
+ "-[ASAccessorySession _showPickerForDisplayItems:completionHandler:]_block_invoke_2"
+ "-[ASAccessorySession allowedToActivatePicker:]"
+ "-[ASAccessorySession failAuthorization:completionHandler:]_block_invoke"
+ "-[ASAccessorySession removeAccessory:completionHandler:]_block_invoke"
+ "-[ASAccessorySession renameAccessory:options:completionHandler:]_block_invoke"
+ "-[ASAccessorySession updateAccessory:settings:completionHandler:]_block_invoke"
+ "ASAccessorySession only supported from iOS 18."
+ "ASAccessorySettings cannot include bluetoothTransportBridgingIdentifier for a Bluetooth accessory paired with CTKD"
+ "ASDiscoveryDescriptor's bluetoothManufacturerDataBlob and bluetoothManufacturerDataMask requires a valid non-zero bluetoothCompanyIdentifier."
+ "ASDiscoveryDescriptor's bluetoothServiceDataBlob and bluetoothServiceDataMask requires a valid bluetoothServiceUUID"
+ "ASDiscoveryDescriptor's must include bluetoothCompanyIdentifier or bluetoothServiceUUID when using bluetoothNameSubstring."
+ "Application is not in foreground."
+ "CBManagers active with global permissions"
+ "Extension not supported"
+ "Migration not allowed since accessories are already authorized"
+ "Picker rate limited for repeated calls"
+ "T@\"NSObject<OS_dispatch_queue>\",R,N"
+ "Unable to update accessory: %!@(MISSING)"
+ "_didDismiss"
+ "_fetchAuthorizedAccesoriesIfNeeded"
+ "_handleDASessionEventHandler:session:"
+ "_tccStateUnkown"
+ "allowedToActivatePicker:"
+ "applicationState"
+ "bridingID %!@(MISSING)"
+ "bundleRecordForCurrentProcess"
+ "debounceCounter"
+ "failAccessory:"
+ "pickerDidSelectAccessory"
+ "relayPickerCompletion:"
+ "renameAccessory:currentName:updateSSID:overrideBundleID:"
+ "retrieveCurrentProcessSessionCount"
+ "setBridgingIdentifier:"
+ "setUserInitiated:"
+ "sharedApplication"
+ "showMigrationPickerWithOverrideBundleID:"
+ "showPickerWithOverrideBundleID:shouldRetrieveDisplayItems:needsBluetooth:needsWiFi:"
+ "startTicksFull"
+ "v24@?0@\"NSObject<OS_tcc_authorization_record>\"8^{__CFError=}16"
+ "v32@?0@\"DADevice\"8Q16^B24"
+ "v48@0:8@\"NSString\"16@\"NSNumber\"24@\"NSNumber\"32@\"NSNumber\"40"
+ "v48@0:8@\"NSString\"16@\"NSString\"24@\"NSNumber\"32@\"NSString\"40"
+ "v48@0:8@16@24@32@40"
- "-[ASAccessorySession _showPickerForDisplayItems:completionHandler:]_block_invoke"
- "-[ASAccessorySession _updateAccessory:settings:completionHandler:]"
- "-[ASAccessorySession fetchAuthorizedAccesoriesIfNeeded]"
- "-[ASAccessorySession fetchAuthorizedAccesoriesIfNeeded]_block_invoke"
- "-[ASAccessorySession handleDASessionEventHandler:session:]"
- "failAccessory:completionHandler:"
- "fetchAuthorizedAccesoriesIfNeeded"
- "handleDASessionEventHandler:session:"
- "renameAccessory:currentName:updateSSID:bundleID:completionHandler:"
- "showMigrationPickerWithClientBundleID:completionHandler:"
- "showPickerWithClientBundleID:shouldRetrieveDisplayItems:needsBluetooth:needsWiFi:completionHandler:"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSError\">24"
- "v56@0:8@\"NSString\"16@\"NSNumber\"24@\"NSNumber\"32@\"NSNumber\"40@?<v@?@\"NSError\">48"
- "v56@0:8@\"NSString\"16@\"NSString\"24@\"NSNumber\"32@\"NSString\"40@?<v@?@\"NSError\">48"
- "v56@0:8@16@24@32@40@?48"

```
