## AccessorySetupKit

> `/System/Library/Frameworks/AccessorySetupKit.framework/Versions/A/AccessorySetupKit`

```diff

-313.1.0.0.0
-  __TEXT.__text: 0xe880
-  __TEXT.__auth_stubs: 0xbc0
-  __TEXT.__objc_methlist: 0xa18
-  __TEXT.__cstring: 0x2017
-  __TEXT.__const: 0x3b6
-  __TEXT.__gcc_except_tab: 0x1e0
+314.11.0.0.0
+  __TEXT.__text: 0xef28
+  __TEXT.__auth_stubs: 0xb60
+  __TEXT.__objc_methlist: 0xcf4
+  __TEXT.__cstring: 0x1e07
+  __TEXT.__const: 0x3c6
+  __TEXT.__gcc_except_tab: 0x1a8
   __TEXT.__oslogstring: 0x1cb
   __TEXT.__swift5_typeref: 0x289
   __TEXT.__constg_swiftt: 0x21c

   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_proto: 0x24
   __TEXT.__swift5_types: 0x10
-  __TEXT.__unwind_info: 0x3b8
-  __TEXT.__objc_classname: 0x155
-  __TEXT.__objc_methname: 0x218e
+  __TEXT.__unwind_info: 0x400
+  __TEXT.__objc_classname: 0x156
+  __TEXT.__objc_methname: 0x21fe
   __TEXT.__objc_methtype: 0x51b
-  __TEXT.__objc_stubs: 0x16a0
+  __TEXT.__objc_stubs: 0x1720
   __DATA_CONST.__got: 0x228
-  __DATA_CONST.__const: 0x328
+  __DATA_CONST.__const: 0x348
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x910
+  __DATA_CONST.__objc_selrefs: 0x9b0
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x28
   __DATA_CONST.__objc_arraydata: 0x18
-  __AUTH_CONST.__auth_got: 0x5f0
+  __AUTH_CONST.__auth_got: 0x5c0
   __AUTH_CONST.__const: 0x278
   __AUTH_CONST.__cfstring: 0x740
-  __AUTH_CONST.__objc_const: 0x1938
+  __AUTH_CONST.__objc_const: 0x1438
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x5d0
   __AUTH.__data: 0x58

   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftIOKit.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 8CAFE9E9-6828-3A39-A3EC-ABBFBBB34456
-  Functions: 347
-  Symbols:   918
-  CStrings:  772
+  UUID: E6E27484-6890-375B-8121-F1C61E0D226D
+  Functions: 397
+  Symbols:   977
+  CStrings:  765
 
Symbols:
+ +[ASAccessoryInfoViewFactory infoViewControllerFromDevice:].cold.1
+ -[ASAccessory initWithCoder:].cold.1
+ -[ASAccessory initWithXPCObject:error:].cold.1
+ -[ASAccessorySession _fetchAuthorizedAccesoriesIfNeeded].cold.1
+ -[ASAccessorySession _fetchBluetoothGlobalTCC]
+ -[ASAccessorySession _handleDASessionEventHandler:session:].cold.1
+ -[ASAccessorySession _handleDASessionEventHandler:session:].cold.2
+ -[ASAccessorySession _handleDASessionEventHandler:session:].cold.3
+ -[ASAccessorySession _handleDASessionEventHandler:session:].cold.4
+ -[ASAccessorySession _handleDASessionEventHandler:session:].cold.5
+ -[ASAccessorySession _handleDASessionEventHandler:session:].cold.6
+ -[ASAccessorySession _hasBluetoothASK]
+ -[ASAccessorySession _invalidated].cold.1
+ -[ASAccessorySession _validateDisplayItem:].cold.1
+ -[ASAccessorySession _validateDisplayItem:].cold.10
+ -[ASAccessorySession _validateDisplayItem:].cold.11
+ -[ASAccessorySession _validateDisplayItem:].cold.12
+ -[ASAccessorySession _validateDisplayItem:].cold.13
+ -[ASAccessorySession _validateDisplayItem:].cold.14
+ -[ASAccessorySession _validateDisplayItem:].cold.15
+ -[ASAccessorySession _validateDisplayItem:].cold.16
+ -[ASAccessorySession _validateDisplayItem:].cold.17
+ -[ASAccessorySession _validateDisplayItem:].cold.18
+ -[ASAccessorySession _validateDisplayItem:].cold.19
+ -[ASAccessorySession _validateDisplayItem:].cold.2
+ -[ASAccessorySession _validateDisplayItem:].cold.20
+ -[ASAccessorySession _validateDisplayItem:].cold.21
+ -[ASAccessorySession _validateDisplayItem:].cold.22
+ -[ASAccessorySession _validateDisplayItem:].cold.23
+ -[ASAccessorySession _validateDisplayItem:].cold.3
+ -[ASAccessorySession _validateDisplayItem:].cold.4
+ -[ASAccessorySession _validateDisplayItem:].cold.5
+ -[ASAccessorySession _validateDisplayItem:].cold.6
+ -[ASAccessorySession _validateDisplayItem:].cold.7
+ -[ASAccessorySession _validateDisplayItem:].cold.8
+ -[ASAccessorySession _validateDisplayItem:].cold.9
+ -[ASAccessorySession _verifyCoreBluetoothStateToActivatePicker:]
+ -[ASAccessorySession activateWithQueue:eventHandler:].cold.1
+ -[ASAccessorySession crashIfAccessorySetupBundleInfoKeysInvalid].cold.1
+ -[ASAccessorySession crashIfAccessorySetupBundleInfoKeysInvalid].cold.2
+ -[ASAccessorySession dealloc].cold.1
+ -[ASAccessorySession showPickerForDisplayItems:completionHandler:].cold.1
+ -[ASAccessorySession showPickerWithCompletionHandler:].cold.1
+ -[ASDiscoveryDescriptor initWithCoder:].cold.1
+ -[ASDiscoveryDescriptor initWithDiscoveryConfiguration:].cold.1
+ -[ASDiscoveryDescriptor initWithXPCObject:error:].cold.1
+ -[ASMigrationDisplayItem initWithCoder:].cold.1
+ -[ASMigrationDisplayItem initWithXPCObject:error:].cold.1
+ -[ASPickerDisplayItem initWithCoder:].cold.1
+ -[ASPickerDisplayItem initWithCoder:].cold.2
+ -[ASPickerDisplayItem initWithXPCObject:error:].cold.1
+ -[ASPickerDisplayItem initWithXPCObject:error:].cold.2
+ GCC_except_table50
+ OBJC_IVAR_$_ASAccessorySession._bluetoothTCCStateUnknown
+ _OUTLINED_FUNCTION_0
+ __32-[ASAccessorySession invalidate]_block_invoke.cold.1
+ __65-[ASAccessorySession updateAccessory:settings:completionHandler:]_block_invoke.cold.1
+ __65-[ASAccessorySession updateAccessory:settings:completionHandler:]_block_invoke.cold.2
+ ___46-[ASAccessorySession _fetchBluetoothGlobalTCC]_block_invoke
+ ___64-[ASAccessorySession _verifyCoreBluetoothStateToActivatePicker:]_block_invoke
+ ___block_descriptor_40_e8_32r_e36_v32?0"ASPickerDisplayItem"8Q16^B24lr32l8
+ _fetchBluetoothGlobalTCC.gLock
+ _fetchBluetoothGlobalTCC.tccServer
+ _objc_msgSend$_fetchBluetoothGlobalTCC
+ _objc_msgSend$_hasBluetoothASK
+ _objc_msgSend$_verifyCoreBluetoothStateToActivatePicker:
+ _objc_msgSend$enumerateObjectsUsingBlock:
+ _objc_msgSend$objectForKey:
- -[ASAccessorySession allowedToActivatePicker:]
- OBJC_IVAR_$_ASAccessorySession._tccStateUnkown
- ___46-[ASAccessorySession allowedToActivatePicker:]_block_invoke
- __swift_FORCE_LOAD_$_swiftFileProvider
- __swift_FORCE_LOAD_$_swiftFileProvider_$_AccessorySetupKit
- _objc_msgSend$allowedToActivatePicker:
- _swift_arrayDestroy
- allowedToActivatePicker:.gLock
- allowedToActivatePicker:.tccServer
CStrings:
+ "### _fetchBluetoothGlobalTCC Unknown"
+ "### _fetchBluetoothGlobalTCC reason: %d"
+ "-[ASAccessorySession _fetchBluetoothGlobalTCC]"
+ "-[ASAccessorySession _verifyCoreBluetoothStateToActivatePicker:]"
+ "NameCompare %lu"
+ "_bluetoothTCCStateUnknown"
+ "_fetchBluetoothGlobalTCC"
+ "_hasBluetoothASK"
+ "_verifyCoreBluetoothStateToActivatePicker:"
+ "enumerateObjectsUsingBlock:"
+ "objectForKey:"
+ "v32@?0@\"ASPickerDisplayItem\"8Q16^B24"
- "### allowedToActivatePicker kTCCAccessPreflightUnknown"
- "### allowedToActivatePicker valid authorized devices"
- "-[ASAccessorySession allowedToActivatePicker:]"
- "Fatal error"
- "Insufficient space allocated to copy string contents"
- "NameCompare %ld"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "_tccStateUnkown"
- "allowedToActivatePicker:"
- "invalid Collection: less than 'count' elements in collection"

```
