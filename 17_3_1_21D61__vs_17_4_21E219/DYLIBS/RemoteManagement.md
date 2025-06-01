## RemoteManagement

> `/System/Library/PrivateFrameworks/RemoteManagement.framework/RemoteManagement`

```diff

-500.25.3.7.0
-  __TEXT.__text: 0x47904
-  __TEXT.__auth_stubs: 0x1400
-  __TEXT.__objc_methlist: 0x1970
-  __TEXT.__const: 0x122c
-  __TEXT.__cstring: 0x536b
-  __TEXT.__oslogstring: 0x1be0
-  __TEXT.__gcc_except_tab: 0x3fc
+500.25.5.10.0
+  __TEXT.__text: 0x4982c
+  __TEXT.__auth_stubs: 0x1430
+  __TEXT.__objc_methlist: 0x19e0
+  __TEXT.__const: 0x124c
+  __TEXT.__cstring: 0x56ab
+  __TEXT.__oslogstring: 0x1c04
+  __TEXT.__gcc_except_tab: 0x404
   __TEXT.__constg_swiftt: 0x988
   __TEXT.__swift5_typeref: 0x5f7
   __TEXT.__swift5_reflstr: 0x2e3

   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_assocty: 0x18
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x15c8
-  __TEXT.__eh_frame: 0x16b0
-  __TEXT.__objc_classname: 0x352
-  __TEXT.__objc_methname: 0x58e7
-  __TEXT.__objc_methtype: 0x839
-  __TEXT.__objc_stubs: 0x2ce0
+  __TEXT.__unwind_info: 0x1658
+  __TEXT.__eh_frame: 0x16f0
+  __TEXT.__objc_classname: 0x370
+  __TEXT.__objc_methname: 0x595f
+  __TEXT.__objc_methtype: 0x82b
+  __TEXT.__objc_stubs: 0x2da0
   __DATA_CONST.__got: 0x350
-  __DATA_CONST.__const: 0x618
-  __DATA_CONST.__objc_classlist: 0x158
+  __DATA_CONST.__const: 0x620
+  __DATA_CONST.__objc_classlist: 0x160
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x20f0
-  __DATA_CONST.__objc_selrefs: 0x12a8
-  __AUTH_CONST.__cfstring: 0x19a0
-  __AUTH_CONST.__objc_const: 0xe78
-  __AUTH_CONST.__const: 0x11f0
+  __DATA_CONST.__objc_const: 0x2160
+  __DATA_CONST.__objc_selrefs: 0x12f8
+  __DATA_CONST.__objc_protorefs: 0x8
+  __DATA_CONST.__objc_classrefs: 0x228
+  __DATA_CONST.__objc_superrefs: 0x68
+  __AUTH_CONST.__cfstring: 0x19c0
+  __AUTH_CONST.__objc_const: 0xf08
+  __AUTH_CONST.__const: 0x1230
   __AUTH_CONST.__objc_intobj: 0x30
-  __AUTH_CONST.__auth_got: 0xa10
-  __AUTH.__objc_data: 0x720
+  __AUTH_CONST.__auth_got: 0xa28
+  __AUTH.__objc_data: 0x770
   __AUTH.__data: 0xaa0
-  __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0x220
-  __DATA.__objc_superrefs: 0x68
   __DATA.__objc_ivar: 0xc8
-  __DATA.__data: 0x6a8
-  __DATA.__bss: 0x20a0
+  __DATA.__data: 0x688
+  __DATA.__bss: 0x20c0
   __DATA.__common: 0x40
   __DATA_DIRTY.__objc_data: 0x460
   __DATA_DIRTY.__bss: 0x78

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 0F0EFD7D-026E-3518-81B7-16F7151F4208
-  Functions: 1432
-  Symbols:   2844
-  CStrings:  1813
+  UUID: 2E974501-3FEE-32A9-A4E4-8A66EED97B9A
+  Functions: 1455
+  Symbols:   2889
+  CStrings:  1846
 
Symbols:
+ +[RMLog(managedDevice) managedDevice]
+ +[RMManagedDevice currentManagedDevice]
+ -[RMEnrollmentController _isDeviceOrSupervisedEnrollment]
+ -[RMManagedDevice getPropertyForKey:scope:]
+ -[RMManagedDevice isMDMEnrolled]
+ -[RMManagedDevice isSharediPad]
+ -[RMManagedDevice isSupervised]
+ -[RMManagedDevice mdmProfileIdentifier]
+ -[RMManagedDevice refreshState]
+ -[RMManagedDevice setProperty:forKey:scope:]
+ GCC_except_table10
+ GCC_except_table4
+ _OBJC_CLASS_$_RMManagedDevice
+ _OBJC_METACLASS_$_RMManagedDevice
+ _OUTLINED_FUNCTION_8
+ _RMConfigurationTypeApplicationSettings
+ __OBJC_$_CLASS_METHODS_RMLog(nsdata_rm|nsdictionary_rm|accountHelper|debounceTimer|device|enrollmentController|jsonUtilities|locations|managedDevice|managedKeychainController|managedTrustStoreController|mcAdapter|mdmHelper|sandbox|sharedLock|timeddispatch|xpcEvent|xpcNotifications)
+ __OBJC_$_CLASS_METHODS_RMManagedDevice
+ __OBJC_$_CLASS_PROP_LIST_RMManagedDevice
+ __OBJC_$_INSTANCE_METHODS_RMManagedDevice
+ __OBJC_$_PROP_LIST_RMManagedDevice
+ __OBJC_CLASS_RO_$_RMManagedDevice
+ __OBJC_METACLASS_RO_$_RMManagedDevice
+ ___119+[RMMDMHelper _enrollDDMChannelIfNeededWithController:profileIdentifier:enrollmentType:scope:username:personaID:error:]_block_invoke.28
+ ___119+[RMMDMHelper _enrollDDMChannelIfNeededWithController:profileIdentifier:enrollmentType:scope:username:personaID:error:]_block_invoke.28.cold.1
+ ___37+[RMLog(managedDevice) managedDevice]_block_invoke
+ ___39+[RMManagedDevice currentManagedDevice]_block_invoke
+ _currentManagedDevice.currentManagedDevice
+ _currentManagedDevice.onceToken
+ _managedDevice.onceToken
+ _managedDevice.result
+ _objc_msgSend$_isDeviceOrSupervisedEnrollment
+ _objc_msgSend$currentManagedDevice
+ _objc_msgSend$getPropertyForKey:scope:
+ _objc_msgSend$isSupervised
+ _objc_msgSend$memberQueueManagingProfileIdentifier
+ _objc_msgSend$refreshDetailsFromDisk
+ _objc_msgSend$setProperty:forKey:scope:
+ _objc_msgSend$string
- +[RMMDMHelper processDeclarativeManagementCommandWithProfileIdentifier:channelType:username:personaID:request:error:]
- +[RMMDMHelper unenrollWithProfileIdentifier:channelType:error:]
- GCC_except_table12
- GCC_except_table17
- __OBJC_$_CLASS_METHODS_RMLog(nsdata_rm|nsdictionary_rm|accountHelper|debounceTimer|device|enrollmentController|jsonUtilities|locations|managedKeychainController|managedTrustStoreController|mcAdapter|mdmHelper|sandbox|sharedLock|timeddispatch|xpcEvent|xpcNotifications)
- ___119+[RMMDMHelper _enrollDDMChannelIfNeededWithController:profileIdentifier:enrollmentType:scope:username:personaID:error:]_block_invoke.29
- ___119+[RMMDMHelper _enrollDDMChannelIfNeededWithController:profileIdentifier:enrollmentType:scope:username:personaID:error:]_block_invoke.29.cold.1
- _objc_msgSend$processDeclarativeManagementCommandWithProfileIdentifier:enrollmentType:scope:username:personaID:request:error:
- _objc_msgSend$unenrollWithProfileIdentifier:enrollmentType:scope:error:
CStrings:
+ "@32@0:8@16q24"
+ "Division by zero"
+ "Division results in an overflow"
+ "Insufficient space allocated to copy string contents"
+ "Processing RemoteManagement command for %{public}@, type: %{public}@."
+ "Processing unenroll request for %{public}@, type: %{public}@."
+ "RMManagedDevice"
+ "Swift/ContiguousArrayBuffer.swift"
+ "Swift/IntegerTypes.swift"
+ "Swift/StringTesting.swift"
+ "Swift/StringUTF8View.swift"
+ "Swift/UnsafeBufferPointer.swift"
+ "Swift/UnsafePointer.swift"
+ "Swift/UnsafeRawPointer.swift"
+ "T@\"RMManagedDevice\",R,N"
+ "Unexpectedly found nil while unwrapping an Optional value"
+ "UnsafeMutableBufferPointer with negative count"
+ "UnsafeMutablePointer.initialize overlapping range"
+ "UnsafeMutablePointer.initialize with negative count"
+ "UnsafeMutablePointer.moveInitialize with negative count"
+ "UnsafeMutableRawPointer.initializeMemory overlapping range"
+ "_isDeviceOrSupervisedEnrollment"
+ "com.apple.configuration.app.settings"
+ "currentManagedDevice"
+ "getPropertyForKey:scope:"
+ "invalid Collection: less than 'count' elements in collection"
+ "isMDMEnrolled"
+ "isSupervised"
+ "managedDevice"
+ "mdm"
+ "mdmProfileIdentifier"
+ "memberQueueManagingProfileIdentifier"
+ "refreshDetailsFromDisk"
+ "refreshState"
+ "setProperty:forKey:scope:"
+ "string"
+ "v40@0:8@16@24q32"
- "B40@0:8@16q24^@32"
- "B64@0:8@16q24@32@40@48^@56"
- "Processing RemoteManagement command for %{public}@."
- "Processing unenroll request for %{public}@."
- "mdm:%@"
- "processDeclarativeManagementCommandWithProfileIdentifier:channelType:username:personaID:request:error:"
- "unenrollWithProfileIdentifier:channelType:error:"

```
