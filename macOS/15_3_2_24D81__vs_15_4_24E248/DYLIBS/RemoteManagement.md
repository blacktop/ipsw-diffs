## RemoteManagement

> `/System/Library/PrivateFrameworks/RemoteManagement.framework/Versions/A/RemoteManagement`

```diff

-502.2.7.0.0
-  __TEXT.__text: 0x4db5c
-  __TEXT.__auth_stubs: 0x1360
-  __TEXT.__objc_methlist: 0x19ec
-  __TEXT.__const: 0x12cc
-  __TEXT.__cstring: 0x2bd7
+560.4.11.0.0
+  __TEXT.__text: 0x52204
+  __TEXT.__auth_stubs: 0x1330
+  __TEXT.__objc_methlist: 0x1b68
+  __TEXT.__const: 0x12dc
+  __TEXT.__cstring: 0x2917
   __TEXT.__oslogstring: 0x489b
-  __TEXT.__gcc_except_tab: 0x47c
+  __TEXT.__gcc_except_tab: 0x478
   __TEXT.__constg_swiftt: 0x988
   __TEXT.__swift5_typeref: 0x60b
   __TEXT.__swift5_reflstr: 0x2e3

   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_assocty: 0x18
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0xf60
-  __TEXT.__eh_frame: 0x16e8
+  __TEXT.__unwind_info: 0xf68
+  __TEXT.__eh_frame: 0x1708
   __TEXT.__objc_classname: 0x36f
-  __TEXT.__objc_methname: 0x57b9
-  __TEXT.__objc_methtype: 0x870
-  __TEXT.__objc_stubs: 0x2d80
+  __TEXT.__objc_methname: 0x589d
+  __TEXT.__objc_methtype: 0x87b
+  __TEXT.__objc_stubs: 0x2e00
   __DATA_CONST.__got: 0x568
-  __DATA_CONST.__const: 0x298
+  __DATA_CONST.__const: 0x2a0
   __DATA_CONST.__objc_classlist: 0x160
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x12f0
+  __DATA_CONST.__objc_selrefs: 0x1358
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x68
-  __AUTH_CONST.__auth_got: 0x9c0
+  __AUTH_CONST.__auth_got: 0x9a8
   __AUTH_CONST.__const: 0x1018
-  __AUTH_CONST.__cfstring: 0x1ae0
-  __AUTH_CONST.__objc_const: 0x3078
+  __AUTH_CONST.__cfstring: 0x1b20
+  __AUTH_CONST.__objc_const: 0x2e48
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH.__objc_data: 0xbd0
   __AUTH.__data: 0xaa0
   __DATA.__objc_ivar: 0xc8
-  __DATA.__data: 0x700
+  __DATA.__data: 0x6b0
   __DATA.__bss: 0x2140
-  __DATA.__common: 0x70
+  __DATA.__common: 0x30
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/CoreData.framework/Versions/A/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: B29A8F2D-AB8A-385B-9A32-9C587F57D46C
-  Functions: 1391
-  Symbols:   2170
-  CStrings:  1859
+  UUID: 095D2638-63B7-3CB6-84FD-415CE7572DDC
+  Functions: 1386
+  Symbols:   2212
+  CStrings:  1855
 
Symbols:
+ +[ACAccountStore(RemoteManagement) rm_defaultStore].cold.1
+ +[RMDateFormat _isoLocalTimeZoneDateFormatter].cold.1
+ +[RMDateFormat _isoLocalTimeZoneFractionalSecondsDateFormatter].cold.1
+ +[RMDateFormat _isoUTCDateFormatter].cold.1
+ +[RMDateFormat _isoUTCFractionalSecondsDateFormatter].cold.1
+ +[RMDevice currentDevice].cold.1
+ +[RMErrorUtilities _populateDescriptionInUserInfo:descriptionKey:arguments:].cold.1
+ +[RMErrorUtilities createTimeoutError]
+ +[RMFeatureFlags hasBridgeOS].cold.1
+ +[RMLocations _rootDirectoryURLInDomain:error:].cold.1
+ +[RMLocations assetCacheDirectoryURLCreateIfNeeded:]
+ +[RMLocations assetCacheDirectoryURLInDomain:createIfNeeded:]
+ +[RMLog(accountHelper) accountHelper].cold.1
+ +[RMLog(debounceTimer) debounceTimer].cold.1
+ +[RMLog(device) device].cold.1
+ +[RMLog(enrollmentController) enrollmentController].cold.1
+ +[RMLog(jsonUtilities) jsonUtilities].cold.1
+ +[RMLog(locations) locations].cold.1
+ +[RMLog(managedDevice) managedDevice].cold.1
+ +[RMLog(managedKeychainController) managedKeychainController].cold.1
+ +[RMLog(managedTrustStoreController) managedTrustStoreController].cold.1
+ +[RMLog(mcAdapter) mcAdapter].cold.1
+ +[RMLog(mdmHelper) mdmHelper].cold.1
+ +[RMLog(nsdata_rm) nsdata_rm].cold.1
+ +[RMLog(nsdictionary_rm) nsdictionary_rm].cold.1
+ +[RMLog(sandbox) sandbox].cold.1
+ +[RMLog(sharedLock) sharedLock].cold.1
+ +[RMLog(timeddispatch) timeddispatch].cold.1
+ +[RMLog(xpcEvent) xpcEvent].cold.1
+ +[RMLog(xpcNotifications) xpcNotifications].cold.1
+ +[RMMDMHelper enrollmentURLForProfileIdentifier:]
+ +[RMMDMHelper setActive:scope:]
+ +[RMManagedDevice currentManagedDevice].cold.1
+ +[RMManagedKeychainController lock].cold.1
+ +[RMManagedKeychainController modifierLock].cold.1
+ +[RMXPCNotifications sharedNotifier].cold.1
+ -[RMSynchronous waitForCompletionWithTimeout:]
+ -[RMTimedDispatch initAfterInterval:completionBlock:].cold.2
+ GCC_except_table22
+ _AssetCacheDirectoryName
+ __block_literal_global.39
+ _objc_msgSend$assetCacheDirectoryURLInDomain:createIfNeeded:
+ _objc_msgSend$dateWithTimeIntervalSinceNow:
+ _objc_msgSend$enrollmentURLForProfileIdentifier:
+ _objc_msgSend$lockWhenCondition:beforeDate:
+ _objc_msgSend$setActive:scope:
+ _swift_setDeallocating
+ _swift_unknownObjectRelease_n
- +[RMMDMHelper _setActive:scope:]
- GCC_except_table23
- __block_literal_global.36
- _objc_msgSend$_setActive:scope:
CStrings:
+ "AssetCache"
+ "B24@0:8d16"
+ "Error.Timeout"
+ "assetCacheDirectoryURLCreateIfNeeded:"
+ "assetCacheDirectoryURLInDomain:createIfNeeded:"
+ "createTimeoutError"
+ "dateWithTimeIntervalSinceNow:"
+ "enrollmentURLForProfileIdentifier:"
+ "lockWhenCondition:beforeDate:"
+ "setActive:scope:"
+ "waitForCompletionWithTimeout:"
- "Division by zero"
- "Division results in an overflow"
- "Insufficient space allocated to copy string contents"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/IntegerTypes.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.initialize with negative count"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "_setActive:scope:"
- "invalid Collection: less than 'count' elements in collection"

```
